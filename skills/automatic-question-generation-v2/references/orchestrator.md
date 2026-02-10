# Orchestrator Agent

Coordinates the automatic question generation workflow between specialized agents, selecting the appropriate path based on input provided.

## Responsibilities

1. Receive topic requests and detect input type (basic vs. with sources vs. expansion)
2. Select appropriate workflow path based on input
3. Route tasks to appropriate agents in correct sequence
4. Monitor outputs for completeness and quality flags
5. Handle exceptions and escalate issues requiring human review
6. Track workflow state and provide status updates

## Input Detection & Path Selection

### Path A: Basic Input Only
**Trigger:** Input contains only `domain` and `topic_title` (no `source_materials`)

```
1. SOURCE_DISCOVERY → finds authoritative references with testable content
2. DOMAIN_EXPERT → validates source accuracy
3. QUESTION_WRITER → generates challenging candidate questions
4. PSYCHOMETRIC_REVIEWER → enforces difficulty standards, selects best 9
5. CURRICULUM_DESIGNER → derives learning objectives and familiarity quiz FROM comprehension quiz
6. CONSISTENCY_AGENT → formats to Empirica template
```

### Path B: Source Materials Provided
**Trigger:** Input contains `domain`, `topic_title`, AND `source_materials` (optionally with `sample_questions`)

```
1. [SAMPLE_QUESTION_EXTRACTOR]* → filters sample questions to reference material scope
2. QUESTION_WRITER → generates challenging candidate questions (using provided sources, inspired by sample questions if provided)
3. PSYCHOMETRIC_REVIEWER → enforces difficulty standards, selects best 9
4. CURRICULUM_DESIGNER → derives learning objectives and familiarity quiz FROM comprehension quiz
5. CONSISTENCY_AGENT → formats to Empirica template
```

*SAMPLE_QUESTION_EXTRACTOR runs only when:
- Both reference material AND sample questions are provided
- Additional prompt includes "extract sample questions" instruction
- Sample questions may contain content outside reference material scope

**Key principle:** Curriculum design always happens AFTER question writing. Learning objectives and familiarity quiz are derived from the final comprehension questions.

### Path C: Expansion (Add CQ10-CQ15 to Existing Task)
**Trigger:** Input contains an existing markdown task file (with populated Metadata, Task data, Familiarity Quiz, and CQ1-CQ9) AND reference material content

```
1. INPUT_VALIDATION → verify existing file has CQ1-CQ9 and reference material is present
2. MATERIAL_COVERAGE_ANALYSIS → compare CQ1-CQ9 against reference material to identify under-covered concepts
3. QUESTION_WRITER → generates 9-12 candidate questions (3-4 per Bloom's level), prioritizing under-covered concepts
4. PSYCHOMETRIC_REVIEWER → enforces difficulty standards, selects best 2 per Bloom's level (6 total)
5. CONSISTENCY_AGENT → appends CQ10-CQ15 to existing file; conditionally updates Task instructions
```

**Key differences from Paths A/B:**
- Skips SOURCE_DISCOVERY, DOMAIN_EXPERT, and CURRICULUM_DESIGNER entirely
- Does NOT generate or modify the Familiarity Quiz (FQ1-FQ4 are frozen)
- Existing CQ1-CQ9, Metadata, and Familiarity Quiz are read-only
- MATERIAL_COVERAGE_ANALYSIS produces a coverage map passed to QUESTION_WRITER
- QUESTION_WRITER receives CQ1-CQ9 as context to avoid concept overlap AND the coverage map to prioritize under-covered material
- CONSISTENCY_AGENT operates in "expansion mode" (append + conditional update)

#### Material Coverage Analysis (Path C, Step 2)

This step runs AFTER input validation and BEFORE question writing. It systematically compares the existing CQ1-CQ9 against the reference material to produce a **coverage map** that guides new question generation.

**Procedure:**

1. **Extract reference material concepts**: Parse the reference material and identify all distinct key concepts, facts, thresholds, procedures, relationships, and themes. Group them into logical topic clusters.

2. **Map existing CQ coverage**: For each CQ1-CQ9, identify which specific concepts from the reference material it tests (both in the stem and in the correct answer / distractors).

3. **Produce coverage map**:

```json
{
  "covered_concepts": [
    {
      "concept": "Description of concept",
      "tested_by": ["CQ1", "CQ5"],
      "bloom_levels_tested": ["Remembering", "Understanding"]
    }
  ],
  "under_covered_concepts": [
    {
      "concept": "Description of under-covered concept",
      "importance": "high | medium | low",
      "testability": "high | medium | low",
      "suggested_bloom_levels": ["Remembering", "Applying"],
      "rationale": "Why this concept is important and testable"
    }
  ],
  "coverage_summary": {
    "total_reference_concepts": 25,
    "concepts_tested_by_cq1_cq9": 12,
    "concepts_not_tested": 13,
    "coverage_percentage": "48%"
  }
}
```

4. **Rank under-covered concepts** by combined importance and testability (high/high first) to produce a prioritized list for the QUESTION_WRITER.

**Routing:** Pass the full coverage map to QUESTION_WRITER alongside the existing CQ1-CQ9 context and reference material content.

## Input Format

### Paths A/B Input Format

The user provides input in the following structured format:

```
The below information is what you should use when filling out the **Metadata** and **Task data** tables in the final output markdown file.
* Domain: [domain name]
* Use case: [use case name]
* Use case description: [description]
* Knowledge dimensions: [factual/conceptual/procedural/metacognitive]
* Reference material (if any): [URL or filename]
* Reference material content (if any): [directly extracted text from PDF or other source]
* Sample questions (if any): [URL or filename]
* Sample questions content (if any): [directly extracted text from sample questions document]
* Reference material source (if any): [source description]
* Comprehension quiz source (if any): [source description]
* Task inspiration (if any): [inspiration source]
* Task ID: [task-id]
* Task title: [Task Title]
* Task description: [description]
```

### Path C Input Format

```jsonc
{
  "path": "C",
  "task_id": "debt-collection-rights",
  "existing_task_file": "/path/to/debt-collection-rights.md",
  "existing_task_content": "# Self-diagnosis: Amyloidosis\n\n| **Metadata** |...",
  "reference_material_file": "/path/to/debt-collection-rights.pdf",
  "reference_material_content": "..."
}
```

### Field Mapping

#### Paths A/B Field Mapping

| Input Field | Maps To | Used By |
|-------------|---------|---------|
| Domain | Metadata: Domain | Consistency Agent |
| Use case | Metadata: Use case | Consistency Agent |
| Use case description | Metadata: Use case description | Consistency Agent |
| Knowledge dimensions | Metadata: Knowledge dimensions | Consistency Agent |
| Reference material | Source for Question Writer | Path detection, Sample Question Extractor, Question Writer |
| Reference material content | Source for Question Writer (direct text) | Path detection, Sample Question Extractor, Question Writer |
| Sample questions | Inspiration for Question Writer | Sample Question Extractor (if extraction requested), Question Writer |
| Sample questions content | Inspiration for Question Writer (direct text) | Sample Question Extractor (if extraction requested), Question Writer |
| Reference material source | Metadata: Reference material source | Consistency Agent |
| Comprehension quiz source | Metadata: Comprehension quiz source | Consistency Agent |
| Task inspiration | Metadata: Task inspiration | Consistency Agent |
| Task ID | Task data: Task ID, filenames | Consistency Agent |
| Task title | Task data: Task title | Consistency Agent |
| Task description | Task data: Task description | Consistency Agent |
| MCQ format | CQ option count | Question Writer, Consistency Agent |
| Additional prompts | Workflow modification | Orchestrator (e.g., "extract sample questions") |

#### Path C Field Mapping

| Input Field | Required | Used By | Purpose |
|-------------|----------|---------|---------|
| `path` | Yes | Orchestrator | Must be `"C"` to trigger Path C |
| `task_id` | Yes | Orchestrator, Consistency Agent | Identifies the task; must match Task ID in existing file |
| `existing_task_file` | Optional | Traceability only | File path to the `.md` file. Not used directly if `existing_task_content` is provided. |
| `existing_task_content` | **Yes** | Orchestrator, Question Writer, Consistency Agent | Full markdown content of existing task. Source of all frozen content. **ERROR if missing or empty.** |
| `reference_material_file` | Optional | Traceability only | File path to the reference PDF. Not used directly if `reference_material_content` is provided. |
| `reference_material_content` | **Yes** | Question Writer, Psychometric Reviewer | Extracted text from reference material. Used to generate CQ10-CQ15. **ERROR if missing or empty.** |

### Handling Reference Material and Sample Questions

**If URL provided:**
- Fetch the URL to retrieve content
- Use fetched content as source material

**If filename provided:**
- Look for attached PDF in the trigger message
- Use attached PDF as source material

**If direct content provided (Reference material content / Sample questions content):**
- Use the provided text directly as source material
- No fetching or file access needed
- This is the preferred method when text has already been extracted from PDFs upstream

**If neither provided:**
- Trigger Path A (Source Discovery)

**Priority order when multiple input types are provided:**
1. Direct content (if "Reference material content" or "Sample questions content" has value) — use this
2. Attached PDF (if filename provided and file is attached) — use this
3. URL (if valid URL provided) — fetch and use this
4. None — trigger Path A

### Input Detection Logic

```
IF "path" == "C":
    → Path C (Expansion)
    → Validate: "existing_task_content" is present and non-empty
        → If missing/empty: ERROR "Path C requires existing_task_content for task_id: [task_id]"
    → Validate: "reference_material_content" is present and non-empty
        → If missing/empty: ERROR "Path C requires reference_material_content for task_id: [task_id]"
    → Validate: existing_task_content contains CQ1-CQ9
        → If missing: ERROR "existing_task_content for task_id: [task_id] does not contain CQ1-CQ9"
    → Extract CQ1-CQ9 content as context for Question Writer
    → Run MATERIAL_COVERAGE_ANALYSIS: compare CQ1-CQ9 against reference_material_content → produce coverage_map
    → Pass reference_material_content + CQ1-CQ9 context + coverage_map to QUESTION_WRITER
    → Route through PSYCHOMETRIC_REVIEWER → CONSISTENCY_AGENT (expansion mode)
ELSE IF "Reference material (if any)" OR "Reference material content (if any)" OR "Sample questions (if any)" OR "Sample questions content (if any)" has a value:
    → Path B (skip SOURCE_DISCOVERY and DOMAIN_EXPERT)
    → IF content provided directly: Use the provided text as-is
    → ELSE IF URL provided: Fetch URL
    → ELSE IF filename provided: Use attached PDF
    IF additional prompt includes "extract sample questions":
        → Run SAMPLE_QUESTION_EXTRACTOR first
        → Filter sample questions to reference material scope
        → Pass extracted questions to QUESTION_WRITER
    ELSE:
        → Pass directly to QUESTION_WRITER
ELSE:
    → Path A (full workflow starting with SOURCE_DISCOVERY)
```

## Output Format

```json
{
  "workflow_id": "unique identifier",
  "current_stage": "stage name",
  "path": "A | B | C",
  "next_agent": "agent name",
  "payload": {},
  "quality_flags": [],
  "human_review_required": false
}
```

## Routing Rules

### Path A Only (Basic Input)
- SOURCE_DISCOVERY returns <1 valid source → HALT, request human input
- DOMAIN_EXPERT flags accuracy concerns → route back to SOURCE_DISCOVERY

### Path B with Extraction
- SAMPLE_QUESTION_EXTRACTOR extracts <50% of sample questions → flag that sample questions may not match reference material well
- SAMPLE_QUESTION_EXTRACTOR extracts 0 questions → HALT, request different sample questions or proceed without inspiration
- SAMPLE_QUESTION_EXTRACTOR identifies many partial-scope questions → provide adaptation suggestions to QUESTION_WRITER

### Path C (Expansion)
- `existing_task_content` is missing or empty → ERROR, flag task_id and skip to next task in batch
- `reference_material_content` is missing or empty → ERROR, flag task_id and skip to next task in batch
- `existing_task_content` does not contain CQ1-CQ9 → ERROR, flag task_id and skip to next task in batch
- MATERIAL_COVERAGE_ANALYSIS finds 0 under-covered concepts → flag as warning; QUESTION_WRITER should still generate questions testing different aspects/depths of already-covered concepts
- MATERIAL_COVERAGE_ANALYSIS finds <6 under-covered concepts → QUESTION_WRITER may combine under-covered concepts with fresh angles on covered concepts
- QUESTION_WRITER produces <9 candidates → request more questions before psychometric review
- PSYCHOMETRIC_REVIEWER rejects >50% of candidates → route back to QUESTION_WRITER with specific guidance
- PSYCHOMETRIC_REVIEWER finds <2 acceptable questions at any Bloom's level → route back to QUESTION_WRITER for that level
- PSYCHOMETRIC_REVIEWER identifies concept overlap with CQ1-CQ9 → reject overlapping questions, request replacements
- CONSISTENCY_AGENT detects modifications to frozen sections → HALT, flag as error, re-run
- Any agent returns "ESCALATE" → flag for human review

### All Paths
- QUESTION_WRITER produces insufficient candidates → request more questions before psychometric review
- PSYCHOMETRIC_REVIEWER rejects >50% questions → route back to QUESTION_WRITER with specific guidance
- Any agent returns "ESCALATE" → flag for human review

## Quality Gates

Before proceeding to next stage:
- Previous agent output matches expected schema
- No unresolved quality flags
- Required fields populated
- Question difficulty standards met (for question-related stages)

### Path C Additional Quality Gates
- CQ1-CQ9 in output are identical to CQ1-CQ9 in input
- Metadata table in output is identical to input
- Familiarity Quiz in output is identical to input
- CQ10-CQ15 test concepts distinct from CQ1-CQ9
- CQ10-CQ15 preferentially test under-covered concepts identified in the Material Coverage Analysis
- Correct answer positions are distributed across CQ10-CQ15

Never skip quality gates. Difficulty standards are non-negotiable.
