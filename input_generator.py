#!/usr/bin/env python3
"""
Input Template Generator for Automatic Question Generation

This tool helps create properly formatted input files for batch processing.

Usage:
    # Create a blank template
    python input_generator.py template --output tasks.json --count 5
    
    # Convert from CSV
    python input_generator.py from-csv --input tasks.csv --output tasks.json
    
    # Validate an existing input file
    python input_generator.py validate --input tasks.json
    
    # Interactive mode - guided entry
    python input_generator.py interactive --output tasks.json
"""

import json
import csv
import argparse
import sys
from pathlib import Path
from typing import Optional, List, Dict, Any


# ============================================================================
# FIELD DEFINITIONS
# ============================================================================

REQUIRED_FIELDS = [
    "domain",
    "use_case", 
    "use_case_description",
    "knowledge_dimensions",
    "task_id",
    "task_title",
]

OPTIONAL_FIELDS = [
    "reference_material",
    "sample_questions",
    "reference_material_source",
    "comprehension_quiz_source",
    "task_inspiration",
    "task_description",
    "cq_format",
    "additional_prompts",
]

FIELD_DESCRIPTIONS = {
    "domain": "Domain name (e.g., Health, Finance, STEM Education, Civic)",
    "use_case": "Subcategory within domain (e.g., Nutrition, Tax preparation)",
    "use_case_description": "Brief description of the use case for documentation",
    "knowledge_dimensions": "Bloom's taxonomy: factual, conceptual, procedural, metacognitive (comma-separated)",
    "task_id": "Lowercase with dashes (e.g., nutrition-labels, credit-scores)",
    "task_title": "≤5 words, title case (e.g., Reading Nutrition Labels)",
    "reference_material": "URL or filename of reference PDF (triggers Path B)",
    "sample_questions": "URL or filename of sample questions for inspiration",
    "reference_material_source": "Documentation of where the material came from",
    "comprehension_quiz_source": "Documentation of question source if any",
    "task_inspiration": "What inspired this task",
    "task_description": "~50 words describing the learning task",
    "cq_format": "Question format (e.g., 'single-select MCQs with 5 options')",
    "additional_prompts": "List of additional instructions (e.g., 'extract sample questions')",
}

FIELD_EXAMPLES = {
    "domain": "Health",
    "use_case": "Medication adherence",
    "use_case_description": "Understanding prescription medication instructions and interactions",
    "knowledge_dimensions": "factual/procedural",
    "task_id": "thyroid-medication",
    "task_title": "Thyroid Medication Management",
    "reference_material": "https://example.com/levothyroxine-guide.pdf",
    "sample_questions": "",
    "reference_material_source": "FDA patient medication guide",
    "comprehension_quiz_source": "",
    "task_inspiration": "Common medication compliance issues",
    "task_description": "Learn proper administration of thyroid medication including timing, food interactions, and supplement considerations.",
    "cq_format": "single-select MCQs with 5 options and one correct answer",
    "additional_prompts": [],
}

# Common domains and use cases for suggestions
DOMAIN_SUGGESTIONS = {
    "Health": [
        "Medication adherence",
        "Chronic disease management", 
        "Preventive care",
        "Nutrition",
        "Mental health",
    ],
    "Finance": [
        "Tax preparation",
        "Retirement planning",
        "Credit management",
        "Insurance",
        "Budgeting",
    ],
    "STEM Education": [
        "Computer science principles",
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
    ],
    "Civic": [
        "Voting rights",
        "Government processes",
        "Legal rights",
        "Community resources",
    ],
}


# ============================================================================
# TEMPLATE GENERATION
# ============================================================================

def create_blank_template(count: int = 1) -> dict:
    """
    Create a blank template with the specified number of task slots.
    """
    tasks = []
    
    for i in range(1, count + 1):
        task = {
            "_comment": f"Task {i} - Fill in required fields, delete optional fields if not needed",
            "domain": "",
            "use_case": "",
            "use_case_description": "",
            "knowledge_dimensions": "factual/conceptual/procedural",
            "task_id": f"task-{i}",
            "task_title": f"Task {i} Title",
            # Optional fields with placeholders
            "reference_material": "(optional) URL or filename",
            "sample_questions": "(optional) URL or filename", 
            "reference_material_source": "(optional)",
            "comprehension_quiz_source": "(optional)",
            "task_inspiration": "(optional)",
            "task_description": "(optional) ~50 words",
            "cq_format": "single-select MCQs with 5 options and one correct answer",
            "additional_prompts": [],
        }
        tasks.append(task)
    
    return {
        "_instructions": {
            "overview": "Fill in each task below. Required fields must have values.",
            "required_fields": REQUIRED_FIELDS,
            "optional_fields": "Delete or leave empty if not needed. Remove (optional) placeholders.",
            "knowledge_dimensions": "Use: factual, conceptual, procedural, metacognitive (slash-separated)",
            "path_selection": "If reference_material is provided → Path B (uses your source). Otherwise → Path A (discovers sources)",
        },
        "_field_descriptions": FIELD_DESCRIPTIONS,
        "_example_task": FIELD_EXAMPLES,
        "tasks": tasks,
    }


def create_example_batch() -> dict:
    """
    Create a batch with realistic example tasks.
    """
    return {
        "tasks": [
            {
                "domain": "Health",
                "use_case": "Medication adherence",
                "use_case_description": "Understanding prescription medication instructions and interactions",
                "knowledge_dimensions": "factual/procedural",
                "task_id": "thyroid-medication",
                "task_title": "Thyroid Medication Management",
                "reference_material": "https://www.accessdata.fda.gov/drugsatfda_docs/label/levothyroxine.pdf",
                "reference_material_source": "FDA prescribing information",
                "task_description": "Learn proper administration of thyroid medication including timing, food interactions, and supplement considerations.",
                "cq_format": "single-select MCQs with 5 options and one correct answer",
            },
            {
                "domain": "Finance",
                "use_case": "Tax preparation",
                "use_case_description": "Understanding federal income tax forms and requirements",
                "knowledge_dimensions": "factual/procedural/conceptual",
                "task_id": "w4-withholding",
                "task_title": "W-4 Tax Withholding",
                "reference_material": "https://www.irs.gov/pub/irs-pdf/fw4.pdf",
                "reference_material_source": "IRS Form W-4 Instructions",
                "task_description": "Learn how to properly complete Form W-4 for tax withholding, including claiming dependents and additional withholding.",
                "cq_format": "single-select MCQs with 5 options and one correct answer",
            },
            {
                "domain": "STEM Education",
                "use_case": "Computer science principles",
                "use_case_description": "Fundamental programming concepts for beginners",
                "knowledge_dimensions": "conceptual/procedural",
                "task_id": "python-loops",
                "task_title": "Python Loop Structures",
                # No reference_material = Path A (source discovery)
                "task_description": "Learn the differences between for loops and while loops in Python, including when to use each type.",
                "cq_format": "single-select MCQs with 4 options and one correct answer",
            },
        ]
    }


# ============================================================================
# CSV CONVERSION
# ============================================================================

def convert_from_csv(csv_path: str) -> dict:
    """
    Convert a CSV file to the JSON task format.
    
    CSV columns should match field names (snake_case).
    """
    tasks = []
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
            task = {}
            
            for field in REQUIRED_FIELDS + OPTIONAL_FIELDS:
                if field in row and row[field] and row[field].strip():
                    value = row[field].strip()
                    
                    # Handle special fields
                    if field == "additional_prompts" and value:
                        # Split by semicolon for multiple prompts
                        task[field] = [p.strip() for p in value.split(";") if p.strip()]
                    elif field == "knowledge_dimensions":
                        # Normalize separators
                        task[field] = value.replace(",", "/").replace(" ", "")
                    else:
                        task[field] = value
            
            # Validate required fields
            missing = [f for f in REQUIRED_FIELDS if f not in task or not task[f]]
            if missing:
                print(f"Warning: Row {row_num} missing required fields: {missing}", file=sys.stderr)
                continue
            
            tasks.append(task)
    
    print(f"Converted {len(tasks)} tasks from CSV")
    return {"tasks": tasks}


def generate_csv_template(output_path: str) -> None:
    """
    Generate a CSV template file with headers and example row.
    """
    all_fields = REQUIRED_FIELDS + OPTIONAL_FIELDS
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_fields)
        writer.writeheader()
        
        # Write example row
        example = {k: FIELD_EXAMPLES.get(k, "") for k in all_fields}
        if "additional_prompts" in example and isinstance(example["additional_prompts"], list):
            example["additional_prompts"] = "; ".join(example["additional_prompts"])
        writer.writerow(example)
    
    print(f"CSV template created: {output_path}")
    print(f"Required columns: {', '.join(REQUIRED_FIELDS)}")


# ============================================================================
# VALIDATION
# ============================================================================

def validate_input(input_path: str) -> bool:
    """
    Validate an input JSON file.
    """
    print(f"\nValidating: {input_path}")
    print("-" * 60)
    
    try:
        with open(input_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON: {e}")
        return False
    
    # Extract tasks
    if isinstance(data, dict) and "tasks" in data:
        tasks = data["tasks"]
    elif isinstance(data, list):
        tasks = data
    else:
        print("✗ Input must be a JSON array or object with 'tasks' array")
        return False
    
    print(f"Found {len(tasks)} tasks\n")
    
    all_valid = True
    task_ids = set()
    
    for i, task in enumerate(tasks):
        task_id = task.get("task_id", f"task_{i}")
        print(f"Task: {task_id}")
        
        # Check for duplicate IDs
        if task_id in task_ids:
            print(f"  ⚠ Warning: Duplicate task_id '{task_id}'")
        task_ids.add(task_id)
        
        # Check required fields
        missing = []
        for field in REQUIRED_FIELDS:
            if field not in task or not task[field]:
                missing.append(field)
        
        if missing:
            print(f"  ✗ Missing required fields: {missing}")
            all_valid = False
        else:
            print(f"  ✓ All required fields present")
        
        # Check task_id format
        if "task_id" in task:
            tid = task["task_id"]
            if " " in tid or tid != tid.lower():
                print(f"  ⚠ Warning: task_id should be lowercase-with-dashes: '{tid}'")
        
        # Check reference material path
        if "reference_material" in task and task["reference_material"]:
            ref = task["reference_material"]
            if ref.startswith("(optional)"):
                print(f"  ⚠ Warning: reference_material still has placeholder text")
            elif not ref.startswith("http") and not Path(ref).exists():
                print(f"  ⚠ Warning: reference_material file not found: {ref}")
            else:
                print(f"  ✓ Path B (using provided reference material)")
        else:
            print(f"  ✓ Path A (will discover sources)")
        
        # Check knowledge dimensions
        if "knowledge_dimensions" in task:
            kd = task["knowledge_dimensions"]
            valid_dims = {"factual", "conceptual", "procedural", "metacognitive"}
            dims = set(kd.replace(",", "/").lower().split("/"))
            invalid = dims - valid_dims
            if invalid:
                print(f"  ⚠ Warning: Invalid knowledge dimensions: {invalid}")
        
        print()
    
    print("-" * 60)
    if all_valid:
        print("✓ Validation passed!")
    else:
        print("✗ Validation failed - fix errors above")
    
    return all_valid


# ============================================================================
# INTERACTIVE MODE
# ============================================================================

def interactive_entry() -> dict:
    """
    Guided interactive task entry.
    """
    print("\n" + "=" * 60)
    print("INTERACTIVE TASK ENTRY")
    print("=" * 60)
    print("\nI'll guide you through creating task entries.")
    print("Press Enter to use default values shown in [brackets].")
    print("Type 'done' when finished adding tasks.\n")
    
    tasks = []
    
    while True:
        print(f"\n--- Task {len(tasks) + 1} ---")
        
        # Check if user wants to continue
        if tasks:
            cont = input("\nAdd another task? [y]/n: ").strip().lower()
            if cont == 'n' or cont == 'done':
                break
        
        task = {}
        
        # Domain with suggestions
        print("\nAvailable domains:", ", ".join(DOMAIN_SUGGESTIONS.keys()))
        task["domain"] = input(f"Domain: ").strip()
        
        # Use case with suggestions if domain matches
        if task["domain"] in DOMAIN_SUGGESTIONS:
            print(f"Suggested use cases for {task['domain']}: {', '.join(DOMAIN_SUGGESTIONS[task['domain']])}")
        task["use_case"] = input(f"Use case: ").strip()
        
        # Use case description
        task["use_case_description"] = input(f"Use case description: ").strip()
        
        # Knowledge dimensions
        print("\nKnowledge dimensions (factual/conceptual/procedural/metacognitive)")
        kd = input(f"Knowledge dimensions [factual/conceptual]: ").strip()
        task["knowledge_dimensions"] = kd if kd else "factual/conceptual"
        
        # Task ID and title
        suggested_id = task["use_case"].lower().replace(" ", "-")[:30] if task["use_case"] else "new-task"
        task_id = input(f"Task ID [{suggested_id}]: ").strip()
        task["task_id"] = task_id if task_id else suggested_id
        
        task["task_title"] = input(f"Task title (≤5 words): ").strip()
        
        # Reference material (determines path)
        print("\nReference material (URL or filename). Leave empty for Path A (source discovery)")
        ref = input(f"Reference material: ").strip()
        if ref:
            task["reference_material"] = ref
            ref_source = input(f"Reference material source (e.g., 'FDA guidelines'): ").strip()
            if ref_source:
                task["reference_material_source"] = ref_source
        
        # Sample questions
        sample = input(f"Sample questions (URL/filename, optional): ").strip()
        if sample:
            task["sample_questions"] = sample
        
        # Task description
        desc = input(f"Task description (~50 words, optional): ").strip()
        if desc:
            task["task_description"] = desc
        
        # CQ format
        cq = input(f"CQ format [5 options]: ").strip()
        if cq:
            task["cq_format"] = cq
        else:
            task["cq_format"] = "single-select MCQs with 5 options and one correct answer"
        
        # Additional prompts
        print("\nAdditional prompts (e.g., 'extract sample questions'). Enter each on new line, empty line to finish:")
        prompts = []
        while True:
            p = input("  > ").strip()
            if not p:
                break
            prompts.append(p)
        if prompts:
            task["additional_prompts"] = prompts
        
        tasks.append(task)
        print(f"\n✓ Task '{task['task_id']}' added!")
    
    return {"tasks": tasks}


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Input template generator for batch quiz generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Create a blank template with 5 task slots
    python input_generator.py template --output tasks.json --count 5
    
    # Create a template with realistic examples
    python input_generator.py example --output example_tasks.json
    
    # Create a CSV template
    python input_generator.py csv-template --output tasks.csv
    
    # Convert from CSV to JSON
    python input_generator.py from-csv --input tasks.csv --output tasks.json
    
    # Validate an input file
    python input_generator.py validate --input tasks.json
    
    # Interactive guided entry
    python input_generator.py interactive --output tasks.json
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Template command
    template_parser = subparsers.add_parser("template", help="Create a blank template")
    template_parser.add_argument("--output", "-o", required=True, help="Output JSON file")
    template_parser.add_argument("--count", "-n", type=int, default=1, help="Number of task slots (default: 1)")
    
    # Example command
    example_parser = subparsers.add_parser("example", help="Create template with realistic examples")
    example_parser.add_argument("--output", "-o", required=True, help="Output JSON file")
    
    # CSV template command
    csv_template_parser = subparsers.add_parser("csv-template", help="Create a CSV template")
    csv_template_parser.add_argument("--output", "-o", required=True, help="Output CSV file")
    
    # From CSV command
    from_csv_parser = subparsers.add_parser("from-csv", help="Convert CSV to JSON")
    from_csv_parser.add_argument("--input", "-i", required=True, help="Input CSV file")
    from_csv_parser.add_argument("--output", "-o", required=True, help="Output JSON file")
    
    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate an input file")
    validate_parser.add_argument("--input", "-i", required=True, help="Input JSON file to validate")
    
    # Interactive command
    interactive_parser = subparsers.add_parser("interactive", help="Interactive guided entry")
    interactive_parser.add_argument("--output", "-o", required=True, help="Output JSON file")
    
    # Fields command (show field descriptions)
    fields_parser = subparsers.add_parser("fields", help="Show all field descriptions")
    
    args = parser.parse_args()
    
    if args.command == "template":
        data = create_blank_template(args.count)
        with open(args.output, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Blank template created: {args.output}")
        print(f"Contains {args.count} task slot(s)")
        
    elif args.command == "example":
        data = create_example_batch()
        with open(args.output, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Example batch created: {args.output}")
        print(f"Contains {len(data['tasks'])} example tasks")
        
    elif args.command == "csv-template":
        generate_csv_template(args.output)
        
    elif args.command == "from-csv":
        data = convert_from_csv(args.input)
        with open(args.output, "w") as f:
            json.dump(data, f, indent=2)
        print(f"JSON file created: {args.output}")
        
    elif args.command == "validate":
        validate_input(args.input)
        
    elif args.command == "interactive":
        data = interactive_entry()
        with open(args.output, "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n✓ Saved {len(data['tasks'])} tasks to: {args.output}")
        
    elif args.command == "fields":
        print("\nField Descriptions:")
        print("=" * 60)
        print("\nREQUIRED FIELDS:")
        for field in REQUIRED_FIELDS:
            print(f"  {field}")
            print(f"    {FIELD_DESCRIPTIONS[field]}")
        print("\nOPTIONAL FIELDS:")
        for field in OPTIONAL_FIELDS:
            print(f"  {field}")
            print(f"    {FIELD_DESCRIPTIONS[field]}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
