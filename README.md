# Batch Question Generator

Automated overnight batch processing for the Automatic Question Generation skill using the Anthropic Batch API.

## Overview

This toolkit enables you to:
1. **Prepare batch inputs** — Create properly formatted task files from templates, CSV, or interactive entry
2. **Submit batches** — Send multiple tasks to run overnight (50% cost savings vs real-time API)
3. **Retrieve results** — Download completed quiz outputs as markdown files

## Quick Start

```bash
# 1. Set your API key
export ANTHROPIC_API_KEY="your-key-here"

# 2. Create example tasks file
python input_generator.py example --output my_tasks.json

# 3. Validate the input
python input_generator.py validate --input my_tasks.json

# 4. Submit the batch (runs overnight)
python batch_processor.py submit --input my_tasks.json

# 5. Check status next morning
python batch_processor.py status --batch-id batch_xxx

# 6. Download results when complete
python batch_processor.py results --batch-id batch_xxx --output ./quiz_outputs/
```

## Installation

```bash
pip install anthropic --break-system-packages
```

## Workflow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Prepare Input  │────▶│  Submit Batch    │────▶│  Retrieve       │
│                 │     │                  │     │  Results        │
│  - Template     │     │  (runs overnight)│     │                 │
│  - CSV import   │     │  50% cost saving │     │  - MD files     │
│  - Interactive  │     │                  │     │  - Error logs   │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

## Input Preparation

### Option A: Start from Template

```bash
# Create blank template with 10 task slots
python input_generator.py template --output tasks.json --count 10

# Edit tasks.json in your favorite editor
```

### Option B: Start from CSV (Best for Spreadsheet Users)

```bash
# Generate CSV template
python input_generator.py csv-template --output tasks.csv

# Edit in Excel/Google Sheets, then convert
python input_generator.py from-csv --input tasks.csv --output tasks.json
```

### Option C: Interactive Guided Entry

```bash
python input_generator.py interactive --output tasks.json
```

### Option D: Example File

```bash
python input_generator.py example --output example_tasks.json
```

## Input Format

Each task requires these fields:

| Field | Required | Description |
|-------|----------|-------------|
| `domain` | ✓ | Health, Finance, STEM Education, Civic, etc. |
| `use_case` | ✓ | Subcategory (e.g., "Medication adherence") |
| `use_case_description` | ✓ | Brief description for documentation |
| `knowledge_dimensions` | ✓ | factual/conceptual/procedural/metacognitive |
| `task_id` | ✓ | lowercase-with-dashes identifier |
| `task_title` | ✓ | ≤5 words, title case |
| `reference_material` | | URL or filename → triggers Path B |
| `sample_questions` | | URL or filename for inspiration |
| `cq_format` | | Default: "5 options" |
| `additional_prompts` | | List of extra instructions |

### Example Task

```json
{
  "domain": "Health",
  "use_case": "Medication adherence",
  "use_case_description": "Understanding prescription medication instructions",
  "knowledge_dimensions": "factual/procedural",
  "task_id": "thyroid-medication",
  "task_title": "Thyroid Medication Management",
  "reference_material": "https://www.accessdata.fda.gov/drugsatfda_docs/label/levothyroxine.pdf",
  "reference_material_source": "FDA prescribing information",
  "cq_format": "single-select MCQs with 5 options and one correct answer"
}
```

## Batch Submission

### Submit Tasks

```bash
# Normal submission
python batch_processor.py submit --input tasks.json

# Dry run (validate without submitting)
python batch_processor.py submit --input tasks.json --dry-run

# Use different model
python batch_processor.py submit --input tasks.json --model claude-sonnet-4-5-20250929
```

### Monitor Progress

```bash
# Check specific batch
python batch_processor.py status --batch-id batch_abc123

# List all recent batches
python batch_processor.py list
```

### Retrieve Results

```bash
# Download all completed results
python batch_processor.py results --batch-id batch_abc123 --output ./results/
```

Results are saved as:
- `{task_id}_output.md` — Completed quiz in Empirica format
- `{task_id}_error.json` — Error details if task failed

## Path Selection Logic

The skill automatically selects the workflow path based on your input:

| Input Provided | Path | Behavior |
|---------------|------|----------|
| No reference_material | **Path A** | Source Discovery → Domain Review → Question Writing → ... |
| reference_material URL/file | **Path B** | Question Writing → Psychometric Review → ... |

## Cost Savings

The Batch API provides **50% discount** compared to real-time API calls:

| Model | Real-time | Batch |
|-------|-----------|-------|
| Claude Sonnet 4 | $3/$15 per MTok | $1.50/$7.50 per MTok |

For 50 quiz generation tasks: ~$15 batch vs ~$30 real-time.

## Troubleshooting

### "Missing required field" error
Run validation to identify issues:
```bash
python input_generator.py validate --input tasks.json
```

### Batch stuck in "processing"
Batches can take up to 24 hours. Check status periodically:
```bash
python batch_processor.py status --batch-id batch_xxx
```

### Some tasks failed
Check the error files in your output directory:
```bash
cat ./results/task-id_error.json
```

Common issues:
- Invalid reference_material URL (404)
- URL blocked by robots.txt
- Reference material too long for context window

## File Structure

```
batch_question_generator/
├── batch_processor.py    # Main batch submission/retrieval
├── input_generator.py    # Input file creation tools
├── README.md            # This file
├── examples/
│   ├── tasks.json       # Example task file
│   └── tasks.csv        # Example CSV format
└── batch_*_info.json    # Auto-generated batch tracking files
```

## Tips for Large Batches

1. **Validate first** — Always run validation before submitting
2. **Start small** — Test with 2-3 tasks before submitting 50+
3. **Use descriptive task_ids** — Makes results easier to track
4. **Group similar tasks** — Same domain tasks are easier to review
5. **Check reference URLs** — Ensure all URLs are accessible before submission
