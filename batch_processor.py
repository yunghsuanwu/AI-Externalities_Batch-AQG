#!/usr/bin/env python3
"""
Batch Processor for Automatic Question Generation

This script enables overnight batch processing of quiz generation tasks
using the Anthropic Batch API (50% cost savings vs real-time).

Usage:
    # Submit a batch
    python batch_processor.py submit --input tasks.json
    
    # Check batch status
    python batch_processor.py status --batch-id batch_abc123
    
    # Retrieve results when complete
    python batch_processor.py results --batch-id batch_abc123 --output ./results/

Requirements:
    pip install anthropic python-dotenv
    
    Set your API key in a .env file:
    ANTHROPIC_API_KEY=your-key-here
"""

import anthropic
import json
import argparse
import os
import sys
import time
import re
from pathlib import Path
from datetime import datetime
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

try:
    import pdfplumber  # type: ignore[import-untyped]
except ImportError:  # pragma: no cover - optional dependency
    pdfplumber = None

try:
    import PyPDF2  # type: ignore[import-untyped]
except ImportError:  # pragma: no cover - optional dependency
    PyPDF2 = None

# Load environment variables from .env file
load_dotenv()


# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULT_MODEL = "claude-opus-4-5-20251101"  # Use Claude Opus 4.5 by default
MAX_TOKENS = 16000  # Sufficient for full quiz output
# Try local skills directory first, then fall back to the original path
SKILL_DIR = Path(__file__).parent / "skills" / "automatic-question-generation"
FALLBACK_SKILL_DIR = Path("/mnt/skills/user/automatic-question-generation")

# Files to include in system prompt (order matters)
SKILL_FILES = [
    "SKILL.md",
    "references/orchestrator.md",
    "references/question-writer.md",
    "references/psychometric-reviewer.md",
    "references/curriculum-designer.md",
    "references/consistency-agent.md",
    "references/output-template.md",
    "references/schemas.md",
    # Path A only (include for completeness)
    "references/source-discovery.md",
    "references/domain-experts.md",
    "references/sample-question-extractor.md",
]


# ============================================================================
# SYSTEM PROMPT BUILDER
# ============================================================================

def build_system_prompt(skill_dir: Path = None) -> str:
    """
    Build the full system prompt by concatenating skill files.
    """
    if skill_dir is None:
        # Try local directory first, then fallback
        if SKILL_DIR.exists():
            skill_dir = SKILL_DIR
        elif FALLBACK_SKILL_DIR.exists():
            skill_dir = FALLBACK_SKILL_DIR
        else:
            print(f"Error: SKILL directory not found!", file=sys.stderr)
            print(f"  Tried: {SKILL_DIR}", file=sys.stderr)
            print(f"  Tried: {FALLBACK_SKILL_DIR}", file=sys.stderr)
            print(f"  Please download the SKILL files and place them in: {SKILL_DIR}", file=sys.stderr)
            sys.exit(1)
    
    sections = []
    
    sections.append("""You are an expert assessment designer running the Automatic Question Generation workflow.

Follow the skill instructions below precisely. Execute all agents in sequence as specified.
Output the final formatted quiz in Empirica template format.

<skill_instructions>
""")
    
    missing_files = []
    for filename in SKILL_FILES:
        filepath = skill_dir / filename
        if filepath.exists():
            content = filepath.read_text()
            sections.append(f"\n\n<!-- {filename} -->\n{content}")
        else:
            missing_files.append(filename)
            print(f"Warning: Skill file not found: {filepath}", file=sys.stderr)
    
    if missing_files:
        print(f"\nWarning: {len(missing_files)} skill file(s) missing. The system prompt may be incomplete.", file=sys.stderr)
    
    sections.append("\n</skill_instructions>")
    
    return "".join(sections)


# ============================================================================
# OUTPUT EXTRACTION
# ============================================================================

def _strip_quality_summary(content: str) -> str:
    """Remove the Quality Summary section from the end of extracted content."""
    for pattern in (r"\n---\s*\n\s*## Quality Summary.*", r"\n## Quality Summary.*"):
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return content[: match.start()].strip()
    return content


def extract_final_output(full_content: str, task_id: str) -> Optional[str]:
    """
    Extract the final output section from the full workflow output.
    
    Looks for "# Final Output: {task_id}.md" followed by a markdown code block,
    and extracts the content within that code block (until closing ``` or end of file).
    
    Returns the extracted final output, or None if not found.
    """
    # Pattern to find the final output section
    # Handle both cases: with closing ``` or without (content until end of file)
    pattern = rf"# Final Output:\s*{re.escape(task_id)}\.md\s*\n```markdown\n(.*?)(?:```|$)"
    
    match = re.search(pattern, full_content, re.DOTALL)
    if match:
        return _strip_quality_summary(match.group(1).strip())
    
    # Fallback: look for the Empirica template header pattern directly
    # This handles cases where the format might be slightly different
    empirica_pattern = r"# [^:]+: [^\n]+\n\n\| \*\*Metadata\*\*.*"
    match = re.search(empirica_pattern, full_content, re.DOTALL)
    if match:
        # Extract from the header to the end of file (or until next major section)
        start_pos = match.start()
        remaining = full_content[start_pos:]
        # Try to find end markers like "## Workflow Summary" or "---" that indicate end
        end_markers = [
            r"\n## Workflow Summary",
            r"\n---\n\n## Workflow Summary",
            r"\n\*\*Estimated completion time:",
            r"\n---\s*\n\s*## Quality Summary",
            r"\n## Quality Summary",
        ]
        for marker in end_markers:
            end_match = re.search(marker, remaining, re.DOTALL)
            if end_match:
                return _strip_quality_summary(remaining[: end_match.start()].strip())
        # If no end marker, strip Quality Summary if present and return the rest
        return _strip_quality_summary(remaining.strip())
    
    return None


# ============================================================================
# INPUT FORMATTING
# ============================================================================


def _load_reference_material_content(reference_value: str, max_chars: int = 50000) -> Optional[str]:
    """
    Given a reference_material field value, try to load and return its text content.

    Behavior:
    - If the value is an HTTP(S) URL, we do NOT fetch it here (just return None);
      the URL string itself is already included in the prompt.
    - If the value looks like a local path or filename:
        * Resolve relative paths against ./reference_materials/
        * If it's a PDF: use pdfplumber if available, else PyPDF2
        * Otherwise, try to read it as a text file (UTF-8, fallback to errors='ignore')
    - The returned text is truncated to max_chars to avoid blowing up context size.
    """
    # Do not attempt network fetching here
    if reference_value.startswith("http://") or reference_value.startswith("https://"):
        return None

    base_dir = Path(__file__).parent
    ref_path = Path(reference_value)

    # If it's not absolute, assume it's inside ./reference_materials/
    if not ref_path.is_absolute():
        ref_path = base_dir / "reference_materials" / ref_path

    if not ref_path.exists():
        print(f"Warning: reference material not found at path: {ref_path}", file=sys.stderr)
        return None

    text: Optional[str] = None

    if ref_path.suffix.lower() == ".pdf":
        if pdfplumber is not None:
            try:
                with pdfplumber.open(ref_path) as pdf:
                    pages_text = []
                    for page in pdf.pages:
                        page_text = page.extract_text() or ""
                        pages_text.append(page_text)
                    text = "\n\n".join(pages_text)
            except Exception as e:  # pragma: no cover - defensive
                print(f"Warning: pdfplumber failed for {ref_path}: {e}", file=sys.stderr)
                text = None
        if text is None and PyPDF2 is not None:
            try:
                with ref_path.open("rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    pages_text = []
                    for page in reader.pages:
                        page_text = page.extract_text() or ""
                        pages_text.append(page_text)
                    text = "\n\n".join(pages_text)
            except Exception as e:  # pragma: no cover - defensive
                print(f"Warning: PyPDF2 failed for {ref_path}: {e}", file=sys.stderr)
                text = None
        if text is None and pdfplumber is None and PyPDF2 is None:
            print(
                f"Warning: Neither pdfplumber nor PyPDF2 installed; cannot extract PDF: {ref_path}",
                file=sys.stderr,
            )
    else:
        # Fallback: treat as plain text file
        try:
            text = ref_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:  # pragma: no cover - defensive
            print(f"Warning: failed to read reference material file {ref_path}: {e}", file=sys.stderr)
            text = None

    if text is None:
        return None

    text = text.strip()
    if not text:
        return None

    # Truncate very long documents to keep prompts manageable
    if len(text) > max_chars:
        print(
            f"Info: reference material at {ref_path} is long; "
            f"truncating to first {max_chars} characters for prompt.",
            file=sys.stderr,
        )
        text = text[:max_chars] + "\n\n[Reference material truncated for length]"

    return text


def format_task_input(task: dict) -> str:
    """
    Format a task dictionary into the expected input prompt.
    """
    lines = ["Generate a quiz using the automatic quiz generation skill.", "", "Input:"]
    
    # Required fields
    required = ["domain", "use_case", "use_case_description", "knowledge_dimensions", "task_id", "task_title"]
    for field in required:
        if field not in task:
            raise ValueError(f"Missing required field: {field}")
    
    # Field mapping (snake_case to display format)
    field_map = {
        "domain": "Domain",
        "use_case": "Use case",
        "use_case_description": "Use case description",
        "knowledge_dimensions": "Knowledge dimensions",
        "reference_material": "Reference material",
        "sample_questions": "Sample questions",
        "reference_material_source": "Reference material source",
        "comprehension_quiz_source": "Comprehension quiz source",
        "task_inspiration": "Task inspiration",
        "task_id": "Task ID",
        "task_title": "Task title",
        "task_description": "Task description",
        "cq_format": "CQ format",
    }
    
    for key, label in field_map.items():
        if key in task and task[key]:
            value = task[key]
            if key == "knowledge_dimensions" and isinstance(value, list):
                value = "/".join(value)
            lines.append(f"* {label}: {value}")

    # Use pre-extracted reference_material_content if present; else load from path (fallback).
    ref_value = task.get("reference_material")
    if ref_value:
        ref_content = task.get("reference_material_content") or _load_reference_material_content(ref_value)
        if ref_content:
            lines.append("")
            lines.append("Reference material content (from local file):")
            lines.append(ref_content)
    
    # Additional prompts (if any)
    if "additional_prompts" in task and task["additional_prompts"]:
        lines.append("")
        lines.append("Additional prompts:")
        for prompt in task["additional_prompts"]:
            lines.append(f"- {prompt}")
    
    return "\n".join(lines)


# ============================================================================
# BATCH OPERATIONS
# ============================================================================

def submit_batch(input_file: str, model: str = DEFAULT_MODEL, dry_run: bool = False) -> Optional[str]:
    """
    Submit a batch of tasks for processing.
    
    Returns the batch ID.
    """
    # Load tasks
    with open(input_file, "r") as f:
        data = json.load(f)
    
    if isinstance(data, dict) and "tasks" in data:
        tasks = data["tasks"]
    elif isinstance(data, list):
        tasks = data
    else:
        raise ValueError("Input must be a JSON array or object with 'tasks' array")

    # Dry-run: require reference_material_content for every task with local reference_material
    if dry_run:
        missing = []
        for task in tasks:
            ref = task.get("reference_material")
            if ref and not ref.startswith(("http://", "https://")):
                content = task.get("reference_material_content")
                if not content or not str(content).strip():
                    missing.append(task.get("task_id", "<no task_id>"))
        if missing:
            raise ValueError(
                "reference_material_content is missing or empty for tasks with local reference_material. "
                "Run 'input_generator.py from-csv' to extract and embed content. Task IDs: " + ", ".join(missing)
            )

    print(f"Found {len(tasks)} tasks to process")
    
    # Build system prompt
    system_prompt = build_system_prompt()
    print(f"System prompt size: {len(system_prompt):,} characters")
    
    # Create batch requests
    requests = []
    for task in tasks:
        task_id = task.get("task_id", f"task_{len(requests)}")
        
        try:
            user_message = format_task_input(task)
        except ValueError as e:
            print(f"Skipping task {task_id}: {e}", file=sys.stderr)
            continue
        
        request = {
            "custom_id": task_id,
            "params": {
                "model": model,
                "max_tokens": MAX_TOKENS,
                "system": system_prompt,
                "messages": [{"role": "user", "content": user_message}]
            }
        }
        requests.append(request)
    
    print(f"Created {len(requests)} valid batch requests")
    
    if dry_run:
        print("\n[DRY RUN] Would submit the following requests:")
        for req in requests[:2]:  # Show first 2
            print(f"  - {req['custom_id']}")
        if len(requests) > 2:
            print(f"  ... and {len(requests) - 2} more")
        return None
    
    # Submit to Anthropic
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.", file=sys.stderr)
        print("  Please set it in your .env file or export it:", file=sys.stderr)
        print("  export ANTHROPIC_API_KEY='your-key-here'", file=sys.stderr)
        sys.exit(1)
    
    client = anthropic.Anthropic(api_key=api_key)
    
    print("\nSubmitting batch to Anthropic API...")
    batch = client.beta.messages.batches.create(requests=requests)
    
    print(f"\n✓ Batch submitted successfully!")
    print(f"  Batch ID: {batch.id}")
    print(f"  Status: {batch.processing_status}")
    print(f"  Created: {batch.created_at}")
    
    # Save batch info for later retrieval
    batch_info = {
        "batch_id": batch.id,
        "created_at": batch.created_at.isoformat() if hasattr(batch.created_at, 'isoformat') else str(batch.created_at),
        "task_count": len(requests),
        "task_ids": [r["custom_id"] for r in requests],
        "input_file": input_file,
        "model": model,
    }
    
    info_file = f"batch_{batch.id}_info.json"
    with open(info_file, "w") as f:
        json.dump(batch_info, f, indent=2)
    print(f"  Info saved: {info_file}")
    
    return batch.id


def check_status(batch_id: str) -> dict:
    """
    Check the status of a batch.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.", file=sys.stderr)
        sys.exit(1)
    
    client = anthropic.Anthropic(api_key=api_key)
    batch = client.beta.messages.batches.retrieve(batch_id)
    
    # Safely unpack request_counts – the SDK type may not expose
    # all attributes (e.g., no `.total` field), so use getattr.
    request_counts = getattr(batch, "request_counts", None)
    if request_counts is not None:
        total = getattr(request_counts, "total", None)
        succeeded = getattr(request_counts, "succeeded", None)
        failed = getattr(request_counts, "errored", None)
        processing = getattr(request_counts, "processing", None)
    else:
        total = succeeded = failed = processing = None
    
    status = {
        "batch_id": batch.id,
        "status": batch.processing_status,
        "created_at": str(batch.created_at),
        "ended_at": str(batch.ended_at) if batch.ended_at else None,
        "request_counts": {
            "total": total,
            "succeeded": succeeded,
            "failed": failed,
            "processing": processing,
        },
    }
    
    print(f"\nBatch Status: {batch_id}")
    print(f"  Status: {status['status']}")
    print(f"  Created: {status['created_at']}")
    if status['ended_at']:
        print(f"  Ended: {status['ended_at']}")
    
    # Display progress if we have any count information
    counts = status['request_counts']
    if counts['total'] is not None:
        print(f"  Progress: {counts['succeeded'] or 0}/{counts['total']} succeeded, {counts['failed'] or 0} failed")
    elif counts['succeeded'] is not None or counts['failed'] is not None or counts['processing'] is not None:
        # Show what we have even if total is missing
        parts = []
        if counts['succeeded'] is not None:
            parts.append(f"{counts['succeeded']} succeeded")
        if counts['failed'] is not None:
            parts.append(f"{counts['failed']} failed")
        if counts['processing'] is not None:
            parts.append(f"{counts['processing']} processing")
        if parts:
            print(f"  Progress: {', '.join(parts)}")
    
    return status


def retrieve_results(batch_id: str, output_dir: str) -> None:
    """
    Retrieve results from a completed batch.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.", file=sys.stderr)
        sys.exit(1)
    
    client = anthropic.Anthropic(api_key=api_key)
    
    # Check status first
    batch = client.beta.messages.batches.retrieve(batch_id)
    if batch.processing_status != "ended":
        print(f"Batch is not complete. Status: {batch.processing_status}")
        return
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\nRetrieving results for batch: {batch_id}")
    
    # Stream results
    succeeded = 0
    failed = 0
    
    for result in client.beta.messages.batches.results(batch_id):
        task_id = result.custom_id
        
        if result.result.type == "succeeded":
            # Extract the response content
            response = result.result.message
            content = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    content += block.text
            
            # Save full output as markdown file
            output_file = output_path / f"{task_id}_output.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)
            
            # Extract and save final output to subfolder
            final_output = extract_final_output(content, task_id)
            if final_output:
                final_dir = output_path / "final"
                final_dir.mkdir(parents=True, exist_ok=True)
                final_file = final_dir / f"{task_id}.md"
                with open(final_file, "w", encoding="utf-8") as f:
                    f.write(final_output)
                succeeded += 1
                print(f"  ✓ {task_id} → {output_file} and {final_file}")
            else:
                succeeded += 1
                print(f"  ✓ {task_id} → {output_file} (final output extraction failed)")
        else:
            # Save error info
            error_file = output_path / f"{task_id}_error.json"
            with open(error_file, "w") as f:
                json.dump({
                    "task_id": task_id,
                    "error_type": result.result.type,
                    "error": str(result.result.error) if hasattr(result.result, 'error') else "Unknown error"
                }, f, indent=2)
            
            failed += 1
            print(f"  ✗ {task_id} (error saved to {error_file})")
    
    print(f"\nComplete: {succeeded} succeeded, {failed} failed")
    print(f"Results saved to: {output_path}")


def process_regular_api(input_file: str, output_dir: str = "./test_results", model: str = DEFAULT_MODEL, max_workers: int = 5, delay: float = 1.2) -> None:
    """
    Process tasks using regular API calls (for testing).
    
    This processes tasks immediately and saves results as they complete.
    Use this for quick testing before submitting a full batch.
    
    Args:
        input_file: JSON file with tasks
        output_dir: Directory to save results
        model: Model to use
        max_workers: Number of concurrent requests (default: 5 to avoid rate limits)
        delay: Delay between requests in seconds (default: 1.2 to respect rate limits)
    """
    # Load tasks
    with open(input_file, "r") as f:
        data = json.load(f)
    
    if isinstance(data, dict) and "tasks" in data:
        tasks = data["tasks"]
    elif isinstance(data, list):
        tasks = data
    else:
        raise ValueError("Input must be a JSON array or object with 'tasks' array")
    
    print(f"Found {len(tasks)} tasks to process using regular API")
    print(f"Using {max_workers} concurrent workers with {delay}s delay between requests")
    print(f"Results will be saved to: {output_dir}\n")
    
    # Build system prompt
    system_prompt = build_system_prompt()
    print(f"System prompt size: {len(system_prompt):,} characters\n")
    
    # Get API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.", file=sys.stderr)
        print("  Please set it in your .env file or export it:", file=sys.stderr)
        sys.exit(1)
    
    client = anthropic.Anthropic(api_key=api_key)
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    def process_task(task: dict, index: int) -> tuple[str, bool, str]:
        """Process a single task and return (task_id, success, message)"""
        task_id = task.get("task_id", f"task_{index}")
        
        try:
            user_message = format_task_input(task)
        except ValueError as e:
            return (task_id, False, f"Validation error: {e}")
        
        try:
            # Make API call
            message = client.messages.create(
                model=model,
                max_tokens=MAX_TOKENS,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}]
            )
            
            # Extract content
            content = ""
            for block in message.content:
                if hasattr(block, 'text'):
                    content += block.text
            
            # Save full output
            output_file = output_path / f"{task_id}_output.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)
            
            # Extract and save final output to subfolder
            final_output = extract_final_output(content, task_id)
            if final_output:
                final_dir = output_path / "final"
                final_dir.mkdir(parents=True, exist_ok=True)
                final_file = final_dir / f"{task_id}.md"
                with open(final_file, "w", encoding="utf-8") as f:
                    f.write(final_output)
                return (task_id, True, f"Saved to {output_file} and {final_file}")
            else:
                return (task_id, True, f"Saved to {output_file} (final output extraction failed)")
            
        except Exception as e:
            # Save error
            error_file = output_path / f"{task_id}_error.json"
            with open(error_file, "w", encoding="utf-8") as f:
                json.dump({
                    "task_id": task_id,
                    "error_type": type(e).__name__,
                    "error": str(e)
                }, f, indent=2)
            
            return (task_id, False, f"Error: {str(e)}")
    
    # Process tasks with concurrency control
    succeeded = 0
    failed = 0
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_task = {
            executor.submit(process_task, task, i): (i, task.get("task_id", f"task_{i}"))
            for i, task in enumerate(tasks)
        }
        
        # Process results as they complete
        for future in as_completed(future_to_task):
            index, task_id = future_to_task[future]
            try:
                result_task_id, success, message = future.result()
                if success:
                    succeeded += 1
                    print(f"  [{index+1}/{len(tasks)}] ✓ {result_task_id}: {message}")
                else:
                    failed += 1
                    print(f"  [{index+1}/{len(tasks)}] ✗ {result_task_id}: {message}", file=sys.stderr)
            except Exception as e:
                failed += 1
                print(f"  [{index+1}/{len(tasks)}] ✗ {task_id}: Unexpected error: {e}", file=sys.stderr)
            
            # Rate limiting delay
            if delay > 0:
                time.sleep(delay)
    
    elapsed_time = time.time() - start_time
    
    print(f"\n{'='*60}")
    print(f"Complete: {succeeded} succeeded, {failed} failed")
    print(f"Time elapsed: {elapsed_time:.1f} seconds ({elapsed_time/60:.1f} minutes)")
    print(f"Results saved to: {output_path}")
    print(f"{'='*60}")


def list_batches(limit: int = 10) -> None:
    """
    List recent batches.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.", file=sys.stderr)
        sys.exit(1)
    
    client = anthropic.Anthropic(api_key=api_key)
    
    print(f"\nRecent batches (up to {limit}):")
    print("-" * 80)
    
    batches = client.beta.messages.batches.list(limit=limit)
    for batch in batches.data:
        status_icon = "✓" if batch.processing_status == "ended" else "⏳"
        print(f"  {status_icon} {batch.id}  |  {batch.processing_status}  |  {batch.created_at}")


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Batch processor for Automatic Question Generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Submit a batch of tasks
    python batch_processor.py submit --input tasks.json
    
    # Dry run (validate without submitting)
    python batch_processor.py submit --input tasks.json --dry-run
    
    # Check batch status
    python batch_processor.py status --batch-id batch_abc123
    
    # Retrieve completed results
    python batch_processor.py results --batch-id batch_abc123 --output ./results/
    
    # List recent batches
    python batch_processor.py list
    
    # Test with regular API (for quick testing before batch)
    python batch_processor.py test --input tasks.json --output ./test_results
    python batch_processor.py test --input tasks.json --workers 3 --delay 2.0
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Submit command
    submit_parser = subparsers.add_parser("submit", help="Submit a batch for processing")
    submit_parser.add_argument("--input", "-i", required=True, help="Input JSON file with tasks")
    submit_parser.add_argument("--model", "-m", default=DEFAULT_MODEL, help=f"Model to use (default: {DEFAULT_MODEL})")
    submit_parser.add_argument("--dry-run", action="store_true", help="Validate without submitting")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Check batch status")
    status_parser.add_argument("--batch-id", "-b", required=True, help="Batch ID to check")
    
    # Results command
    results_parser = subparsers.add_parser("results", help="Retrieve batch results")
    results_parser.add_argument("--batch-id", "-b", required=True, help="Batch ID to retrieve")
    results_parser.add_argument("--output", "-o", default="./batch_results", help="Output directory")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List recent batches")
    list_parser.add_argument("--limit", "-n", type=int, default=10, help="Number of batches to show")
    
    # Test command (regular API)
    test_parser = subparsers.add_parser("test", help="Test with regular API calls (for quick testing)")
    test_parser.add_argument("--input", "-i", required=True, help="Input JSON file with tasks")
    test_parser.add_argument("--output", "-o", default="./test_results", help="Output directory (default: ./test_results)")
    test_parser.add_argument("--model", "-m", default=DEFAULT_MODEL, help=f"Model to use (default: {DEFAULT_MODEL})")
    test_parser.add_argument("--workers", "-w", type=int, default=5, help="Number of concurrent requests (default: 5)")
    test_parser.add_argument("--delay", "-d", type=float, default=1.2, help="Delay between requests in seconds (default: 1.2)")
    
    args = parser.parse_args()
    
    if args.command == "submit":
        submit_batch(args.input, args.model, args.dry_run)
    elif args.command == "status":
        check_status(args.batch_id)
    elif args.command == "results":
        retrieve_results(args.batch_id, args.output)
    elif args.command == "list":
        list_batches(args.limit)
    elif args.command == "test":
        process_regular_api(args.input, args.output, args.model, args.workers, args.delay)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
