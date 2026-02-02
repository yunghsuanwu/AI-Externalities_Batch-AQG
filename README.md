# Batch Question Generator

Automated overnight batch processing for the Automatic Question Generation skill using the Anthropic Batch API.

## Overview

This toolkit enables you to:
1. **Prepare batch inputs** — Create properly formatted task files from templates, CSV, or interactive entry
2. **Submit batches** — Send multiple tasks to run overnight (50% cost savings vs real-time API)
3. **Retrieve results** — Download completed quiz outputs as markdown files

## Quick Start

```bash
# 1. Set up virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install --upgrade pip
pip install anthropic python-dotenv

# 3. Set up your API key
# Create .env file and add your ANTHROPIC_API_KEY:
# ANTHROPIC_API_KEY=your-api-key-here

# 4. Set up SKILL files (see SKILL Setup below)
# Download the SKILL files and place them in: ./skills/automatic-question-generation/

# 5. Fill in tasks.csv with your tasks
# Reference materials go in ./reference_materials/ folder

# 6. Convert CSV to JSON
python input_generator.py from-csv --input tasks.csv --output tasks.json

# 7. Validate the input
python input_generator.py validate --input tasks.json

# 8. Submit the batch (runs overnight)
python batch_processor.py submit --input tasks.json

# 9. Check status next morning
python batch_processor.py status --batch-id batch_xxx

# 10. Download results when complete
python batch_processor.py results --batch-id batch_xxx --output ./quiz_outputs/
```

**Note:** Remember to activate your virtual environment (`source venv/bin/activate`) each time you open a new terminal session.

## Installation

### Using Virtual Environment (Recommended)

```bash
# Create virtual environment (first time only)
python3 -m venv venv

# Activate virtual environment (every time you work on the project)
source venv/bin/activate

# Install dependencies (first time only)
pip install --upgrade pip
pip install anthropic python-dotenv

# Verify installation
pip list | grep -E "(anthropic|python-dotenv)"

# When done working, deactivate:
deactivate
```

### Without Virtual Environment

```bash
pip install anthropic python-dotenv
```

## Quick Reference

### Virtual Environment Commands

```bash
# Navigate to project directory
cd /Users/WuYung-Hsuan/Desktop/coding-stuff/AI-Externalities_Batch-AQG

# Activate virtual environment (do this every time you open a new terminal)
source venv/bin/activate

# Deactivate when done
deactivate
```

### Workflow Commands

```bash
# Convert CSV to JSON
python input_generator.py from-csv --input tasks.csv --output tasks.json

# Validate input
python input_generator.py validate --input tasks.json

# OPTION 1: Test with regular API (quick testing, immediate results)
python batch_processor.py test --input tasks.json --output ./test_results

# OPTION 2: Submit batch API (cost-effective for large batches)
python batch_processor.py submit --input tasks.json --dry-run  # Test first
python batch_processor.py submit --input tasks.json            # Real submission

# Check batch status
python batch_processor.py status --batch-id YOUR_BATCH_ID

# Retrieve batch results when complete
python batch_processor.py results --batch-id YOUR_BATCH_ID --output ./results/

# List recent batches
python batch_processor.py list
```

**Remember:** Always activate your virtual environment (`source venv/bin/activate`) before running these commands!

## SKILL Setup

The batch processor requires SKILL files to generate questions. The code looks for them in:
- `./skills/automatic-question-generation/` (local directory - preferred)
- `/mnt/skills/user/automatic-question-generation` (fallback)

**You need to download the SKILL files and place them in the local directory.** The required structure is:

```
skills/
└── automatic-question-generation/
    ├── SKILL.md
    └── references/
        ├── orchestrator.md
        ├── question-writer.md
        ├── psychometric-reviewer.md
        ├── curriculum-designer.md
        ├── consistency-agent.md
        ├── output-template.md
        ├── schemas.md
        ├── source-discovery.md
        ├── domain-experts.md
        └── sample-question-extractor.md
```

If the SKILL directory is not found, the batch processor will exit with an error message showing where to place the files.

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

### Option A: Start from CSV (Recommended)

This is the main workflow - fill in `tasks.csv` and convert to JSON:

```bash
# Generate CSV template (if needed)
python input_generator.py csv-template --output tasks.csv

# Edit tasks.csv in Excel/Google Sheets
# - Put reference material filenames in the reference_material column
# - Reference materials should be in ./reference_materials/ folder

# Convert CSV to JSON
python input_generator.py from-csv --input tasks.csv --output tasks.json
```

### Reference Materials

Place your reference material files (PDFs, text files, etc.) in the `reference_materials/` folder. In your `tasks.csv`, specify the filename (or relative path) in the `reference_material` column. For example:

- If you have `reference_materials/thyroid-guide.pdf`, use `thyroid-guide.pdf` in the CSV
- URLs (starting with `http://` or `https://`) are also supported

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

## Testing vs Batch Processing

### Option 1: Test with Regular API (Quick Testing)

Use this to test a few tasks quickly before submitting a full batch:

```bash
# Test with regular API (processes immediately, saves results as they complete)
python batch_processor.py test --input tasks.json --output ./test_results

# Test with custom concurrency settings
python batch_processor.py test --input tasks.json --workers 3 --delay 2.0

# Test with different model
python batch_processor.py test --input tasks.json --model claude-sonnet-4-5-20250929
```

**Output Structure:**
```
test_results/
├── synthroid_output.md          # Full workflow output
├── final/
│   └── synthroid.md            # Final quiz (clean, ready to use)
└── synthroid_error.json         # Errors (if any)
```

**Benefits:**
- ✅ Immediate results (minutes instead of hours)
- ✅ See results as they complete
- ✅ Good for testing 1-10 tasks

**Trade-offs:**
- ❌ Full price (no 50% discount)
- ❌ Need to manage rate limits
- ❌ Slower for large batches (75+ tasks)

### Option 2: Batch API (Production)

Use this for processing many tasks cost-effectively:

```bash
# Normal submission
python batch_processor.py submit --input tasks.json

# Dry run (validate without submitting)
python batch_processor.py submit --input tasks.json --dry-run

# Use different model
python batch_processor.py submit --input tasks.json --model claude-sonnet-4-5-20250929
```

**Benefits:**
- ✅ 50% cost savings
- ✅ No rate limit concerns
- ✅ Best for 10+ tasks

**Trade-offs:**
- ❌ Takes up to 24 hours
- ❌ Results retrieved later

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

Results are saved in two locations:

**Full Output:**
- `{task_id}_output.md` — Complete workflow output with all processing steps

**Final Output (in `final/` subfolder):**
- `final/{task_id}.md` — Extracted final quiz in Empirica template format (clean, ready to use)
- `{task_id}_error.json` — Error details if task failed (in main output directory)

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
AI-Externalities_Batch-AQG/
├── batch_processor.py          # Main batch submission/retrieval
├── input_generator.py          # CSV to JSON converter
├── tasks.csv                   # Your input tasks (fill this in)
├── tasks.json                  # Generated from tasks.csv
├── README.md                   # This file
├── .env                        # Your API key (ANTHROPIC_API_KEY=your-key-here)
├── .gitignore                  # Git ignore rules
├── reference_materials/        # Put your reference PDFs/files here
│   └── (your files here)
└── skills/                     # SKILL files (you need to download these)
    └── automatic-question-generation/
        ├── SKILL.md
        └── references/
            └── (skill reference files)
```

## Tips for Large Batches

1. **Validate first** — Always run validation before submitting
2. **Start small** — Test with 2-3 tasks before submitting 50+
3. **Use descriptive task_ids** — Makes results easier to track
4. **Group similar tasks** — Same domain tasks are easier to review
5. **Check reference URLs** — Ensure all URLs are accessible before submission
