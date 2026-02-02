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
    pip install anthropic --break-system-packages
    
    Set your API key:
    export ANTHROPIC_API_KEY="your-key-here"
"""

import anthropic
import json
import argparse
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional


# ============================================================================
# CONFIGURATION
# ============================================================================

DEFAULT_MODEL = "claude-sonnet-4-5-20250929"  # Cost-effective for batch
MAX_TOKENS = 16000  # Sufficient for full quiz output
SKILL_DIR = Path("/mnt/skills/user/automatic-question-generation")

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

def build_system_prompt(skill_dir: Path = SKILL_DIR) -> str:
    """
    Build the full system prompt by concatenating skill files.
    """
    sections = []
    
    sections.append("""You are an expert assessment designer running the Automatic Question Generation workflow.

Follow the skill instructions below precisely. Execute all agents in sequence as specified.
Output the final formatted quiz in Empirica template format.

<skill_instructions>
""")
    
    for filename in SKILL_FILES:
        filepath = skill_dir / filename
        if filepath.exists():
            content = filepath.read_text()
            sections.append(f"\n\n<!-- {filename} -->\n{content}")
        else:
            print(f"Warning: Skill file not found: {filepath}", file=sys.stderr)
    
    sections.append("\n</skill_instructions>")
    
    return "".join(sections)


# ============================================================================
# INPUT FORMATTING
# ============================================================================

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
    client = anthropic.Anthropic()
    
    print("\nSubmitting batch to Anthropic API...")
    batch = client.batches.create(requests=requests)
    
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
    client = anthropic.Anthropic()
    batch = client.batches.retrieve(batch_id)
    
    status = {
        "batch_id": batch.id,
        "status": batch.processing_status,
        "created_at": str(batch.created_at),
        "ended_at": str(batch.ended_at) if batch.ended_at else None,
        "request_counts": {
            "total": batch.request_counts.total if hasattr(batch, 'request_counts') else None,
            "succeeded": batch.request_counts.succeeded if hasattr(batch, 'request_counts') else None,
            "failed": batch.request_counts.errored if hasattr(batch, 'request_counts') else None,
            "processing": batch.request_counts.processing if hasattr(batch, 'request_counts') else None,
        }
    }
    
    print(f"\nBatch Status: {batch_id}")
    print(f"  Status: {status['status']}")
    print(f"  Created: {status['created_at']}")
    if status['ended_at']:
        print(f"  Ended: {status['ended_at']}")
    if status['request_counts']['total']:
        counts = status['request_counts']
        print(f"  Progress: {counts['succeeded']}/{counts['total']} succeeded, {counts['failed']} failed")
    
    return status


def retrieve_results(batch_id: str, output_dir: str) -> None:
    """
    Retrieve results from a completed batch.
    """
    client = anthropic.Anthropic()
    
    # Check status first
    batch = client.batches.retrieve(batch_id)
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
    
    for result in client.batches.results(batch_id):
        task_id = result.custom_id
        
        if result.result.type == "succeeded":
            # Extract the response content
            response = result.result.message
            content = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    content += block.text
            
            # Save as markdown file
            output_file = output_path / f"{task_id}_output.md"
            with open(output_file, "w") as f:
                f.write(content)
            
            succeeded += 1
            print(f"  ✓ {task_id} → {output_file}")
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


def list_batches(limit: int = 10) -> None:
    """
    List recent batches.
    """
    client = anthropic.Anthropic()
    
    print(f"\nRecent batches (up to {limit}):")
    print("-" * 80)
    
    batches = client.batches.list(limit=limit)
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
    
    args = parser.parse_args()
    
    if args.command == "submit":
        submit_batch(args.input, args.model, args.dry_run)
    elif args.command == "status":
        check_status(args.batch_id)
    elif args.command == "results":
        retrieve_results(args.batch_id, args.output)
    elif args.command == "list":
        list_batches(args.limit)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
