"""
Task expansion prep: convert a CSV of task_ids into a JSON file with full paths
and extracted content from existing task .md files and reference material PDFs.

Usage:
    python task-expansion-prep.py --input task-expansion-input.csv --output task-expansion-output.json
"""
import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Optional

try:
    import pdfplumber  # type: ignore[import-untyped]
except ImportError:
    pdfplumber = None

try:
    import PyPDF2  # type: ignore[import-untyped]
except ImportError:
    PyPDF2 = None

DEFAULT_MAX_REFERENCE_CHARS = 50000

# Directories relative to this script
REFERENCE_MATERIALS_DIR = Path(__file__).parent / "reference_materials"
EXISTING_TASK_DIR = Path(__file__).parent / "existing_tasks"


def _extract_text_from_path(ref_path: Path, max_chars: int = DEFAULT_MAX_REFERENCE_CHARS) -> Optional[str]:
    """
    Extract text from a local file. Prefer pdfplumber for PDFs, then PyPDF2, then plain text.
    Returns None on failure or if no library is available. Truncates to max_chars.
    """
    if not ref_path.exists():
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
            except Exception as e:
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
            except Exception as e:
                print(f"Warning: PyPDF2 failed for {ref_path}: {e}", file=sys.stderr)
                text = None
        if text is None and (pdfplumber is None and PyPDF2 is None):
            print(
                f"Warning: Neither pdfplumber nor PyPDF2 installed; cannot extract PDF: {ref_path}",
                file=sys.stderr,
            )
    else:
        try:
            text = ref_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"Warning: failed to read file {ref_path}: {e}", file=sys.stderr)
            text = None

    if text is None:
        return None

    text = text.strip()
    if not text:
        return None

    if len(text) > max_chars:
        print(
            f"Info: {ref_path.name} truncated to first {max_chars} characters.",
            file=sys.stderr,
        )
        text = text[:max_chars] + "\n\n[Reference material truncated for length]"

    return text


def convert_from_csv(
    csv_path: str,
    reference_materials_dir: Optional[Path] = None,
    existing_task_dir: Optional[Path] = None,
) -> dict:
    """
    Convert a CSV file (with at least a task_id column) to JSON task-expansion format.
    Each row becomes a task dict with task_id, full paths, and extracted content.
    """
    if reference_materials_dir is None:
        reference_materials_dir = REFERENCE_MATERIALS_DIR
    if existing_task_dir is None:
        existing_task_dir = EXISTING_TASK_DIR

    tasks = []

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "task_id" not in (reader.fieldnames or []):
            raise ValueError("CSV must have a 'task_id' column")

        for row_num, row in enumerate(reader, start=2):
            task_id = (row.get("task_id") or "").strip()
            if not task_id:
                print(f"Warning: Row {row_num} has empty task_id, skipping", file=sys.stderr)
                continue

            existing_task_file = task_id + ".md"
            reference_material_file = task_id + ".pdf"
            existing_path = existing_task_dir / existing_task_file
            reference_path = reference_materials_dir / reference_material_file

            task = {
                "path": "C",
                "task_id": task_id,
                "existing_task_file": str(existing_path.resolve()),
                "existing_task_content": _extract_text_from_path(existing_path),
                "reference_material_file": str(reference_path.resolve()),
                "reference_material_content": _extract_text_from_path(reference_path),
            }
            tasks.append(task)

    print(f"Converted {len(tasks)} tasks from CSV", file=sys.stderr)
    return {"tasks": tasks}


REQUIRED_TASK_KEYS = (
    "path",
    "task_id",
    "existing_task_file",
    "existing_task_content",
    "reference_material_file",
    "reference_material_content",
)


def validate_expansion_output(json_path: str) -> bool:
    """
    Validate that a task-expansion JSON file has the correct structure and flag
    any tasks with missing required fields or missing extracted content.
    Returns True if all tasks are valid, False otherwise.
    """
    print(f"\nValidating: {json_path}", file=sys.stderr)
    print("-" * 60, file=sys.stderr)

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"✗ Failed to load JSON: {e}", file=sys.stderr)
        return False

    if not isinstance(data, dict) or "tasks" not in data:
        print("✗ Root must be an object with a 'tasks' array", file=sys.stderr)
        return False

    tasks = data["tasks"]
    if not isinstance(tasks, list):
        print("✗ 'tasks' must be an array", file=sys.stderr)
        return False

    all_valid = True
    missing_content: list[str] = []
    invalid_structure: list[tuple[int, str]] = []

    for i, task in enumerate(tasks):
        if not isinstance(task, dict):
            invalid_structure.append((i, "task is not an object"))
            all_valid = False
            continue

        missing_keys = [k for k in REQUIRED_TASK_KEYS if k not in task]
        if missing_keys:
            invalid_structure.append(
                (i, f"task_id={task.get('task_id', '?')} missing keys: {missing_keys}")
            )
            all_valid = False

        task_id = task.get("task_id", "?")
        existing_content = task.get("existing_task_content")
        reference_content = task.get("reference_material_content")

        if existing_content is None or (isinstance(existing_content, str) and not existing_content.strip()):
            missing_content.append(f"{task_id} (missing existing_task_content)")
            all_valid = False
        if reference_content is None or (isinstance(reference_content, str) and not reference_content.strip()):
            missing_content.append(f"{task_id} (missing reference_material_content)")
            all_valid = False

    print(f"Total tasks: {len(tasks)}", file=sys.stderr)
    if invalid_structure:
        print(f"\n✗ Invalid structure ({len(invalid_structure)}):", file=sys.stderr)
        for idx, msg in invalid_structure:
            print(f"  [{idx}] {msg}", file=sys.stderr)
    if missing_content:
        print(f"\n✗ Missing content ({len(missing_content)}):", file=sys.stderr)
        for item in missing_content:
            print(f"  - {item}", file=sys.stderr)

    if all_valid:
        print("\n✓ All tasks are valid and have required content.", file=sys.stderr)
    else:
        print(
            f"\n✗ Validation failed: {len(invalid_structure)} structural issue(s), "
            f"{len(missing_content)} missing content.",
            file=sys.stderr,
        )

    return all_valid


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert task-expansion CSV to JSON with extracted content, or validate a JSON file."
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to run")

    # convert_from_csv: CSV -> JSON
    convert_parser = subparsers.add_parser("convert_from_csv", help="Convert CSV to task-expansion JSON")
    convert_parser.add_argument("--input", "-i", required=True, help="Input CSV path (must have task_id column)")
    convert_parser.add_argument("--output", "-o", required=True, help="Output JSON path")

    # validate: check JSON from previous step
    validate_parser = subparsers.add_parser("validate", help="Validate a task-expansion JSON file")
    validate_parser.add_argument("--input", "-i", required=True, help="JSON file to validate (e.g. output from convert_from_csv)")

    args = parser.parse_args()

    if args.command == "convert_from_csv":
        data = convert_from_csv(args.input)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Wrote {args.output}", file=sys.stderr)
    elif args.command == "validate":
        ok = validate_expansion_output(args.input)
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()