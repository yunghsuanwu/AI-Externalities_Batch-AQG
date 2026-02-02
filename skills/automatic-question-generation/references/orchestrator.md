# Orchestrator Agent

Coordinates the automatic question generation workflow between specialized agents, selecting the appropriate path based on input provided.

## Responsibilities

1. Receive topic requests and detect input type (basic vs. with sources)
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

## Input Format

The user provides input in the following structured format:

```
The below information is what you should use when filling out the **Metadata** and **Task data** tables in the final output markdown file.
* Domain: [domain name]
* Use case: [use case name]
* Use case description: [description]
* Knowledge dimensions: [factual/conceptual/procedural/metacognitive]
* Reference material (if any): [URL or filename]
* Sample questions (if any): [URL or filename]
* Reference material source (if any): [source description]
* Comprehension quiz source (if any): [source description]
* Task inspiration (if any): [inspiration source]
* Task ID: [task-id]
* Task title: [Task Title]
* Task description: [description]
```

### Field Mapping

| Input Field | Maps To | Used By |
|-------------|---------|---------|
| Domain | Metadata: Domain | Consistency Agent |
| Use case | Metadata: Use case | Consistency Agent |
| Use case description | Metadata: Use case description | Consistency Agent |
| Knowledge dimensions | Metadata: Knowledge dimensions | Consistency Agent |
| Reference material | Source for Question Writer | Path detection, Sample Question Extractor, Question Writer |
| Sample questions | Inspiration for Question Writer | Sample Question Extractor (if extraction requested), Question Writer |
| Reference material source | Metadata: Reference material source | Consistency Agent |
| Comprehension quiz source | Metadata: Comprehension quiz source | Consistency Agent |
| Task inspiration | Metadata: Task inspiration | Consistency Agent |
| Task ID | Task data: Task ID, filenames | Consistency Agent |
| Task title | Task data: Task title | Consistency Agent |
| Task description | Task data: Task description | Consistency Agent |
| MCQ format | CQ option count | Question Writer, Consistency Agent |
| Additional prompts | Workflow modification | Orchestrator (e.g., "extract sample questions") |

### Handling Reference Material and Sample Questions

**If URL provided:**
- Fetch the URL to retrieve content
- Use fetched content as source material

**If filename provided:**
- Look for attached PDF in the trigger message
- Use attached PDF as source material

**If neither provided:**
- Trigger Path A (Source Discovery)

### Input Detection Logic

```
IF "Reference material (if any)" OR "Sample questions (if any)" has a value (URL or filename):
    → Path B (skip SOURCE_DISCOVERY and DOMAIN_EXPERT)
    → Fetch URL or use attached PDF
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

### Both Paths
- QUESTION_WRITER produces <12 candidates → request more questions before psychometric review
- PSYCHOMETRIC_REVIEWER rejects >50% questions → route back to QUESTION_WRITER with specific guidance
- PSYCHOMETRIC_REVIEWER finds <3 acceptable questions at any Bloom's level → route back to QUESTION_WRITER
- CURRICULUM_DESIGNER finds learning objectives don't align with questions → flag for review
- Any agent returns "ESCALATE" → flag for human review

## Quality Gates

Before proceeding to next stage:
- Previous agent output matches expected schema
- No unresolved quality flags
- Required fields populated
- Question difficulty standards met (for question-related stages)

Never skip quality gates. Difficulty standards are non-negotiable.
