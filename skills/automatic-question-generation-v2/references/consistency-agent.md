# Consistency & Formatting Agent

Formats all generated content to the Empirica platform template structure, ensuring identical output format across multiple generation rounds.

## Position in Workflow

### Paths A/B
This agent runs LAST, after the curriculum designer has derived learning objectives and familiarity quiz content from the finalized comprehension quiz.

### Path C (Expansion)
This agent runs LAST, after the psychometric reviewer has finalized CQ10-CQ15. In Path C, this agent operates in **expansion mode**: it appends new questions to an existing file and conditionally updates Task instructions, while preserving all frozen sections.

## Input Sources

This agent receives data from multiple sources depending on the active path:

### 1. User-Provided Input (from trigger message)

#### Paths A/B: Structured Input Fields

| User Input Field | Maps To |
|------------------|---------|
| Domain | Metadata: Domain |
| Use case | Metadata: Use case |
| Use case description | Metadata: Use case description |
| Knowledge dimensions | Metadata: Knowledge dimensions |
| Reference material source | Metadata: Reference material source |
| Comprehension quiz source | Metadata: Comprehension quiz source |
| Task inspiration | Metadata: Task inspiration |
| Task ID | Task data: Task ID, filenames |
| Task title | Task data: Task title, Header |
| Task description | Task data: Task description |

#### Path C: Existing Task File

| Source | Used For |
|--------|----------|
| Existing markdown file | All frozen content (Metadata, Task data, FQ1-FQ4, CQ1-CQ9) — copied verbatim |
| Reference material content | Context for evaluating Task instruction updates |

### 2. Curriculum Designer Output (Paths A/B only)

| Field | Used For |
|-------|----------|
| FQ1-FQ4 questions | Familiarity Quiz section |
| Learning objectives | Informing Task instructions |

### 3. Psychometric Reviewer Output

| Field | Used For |
|-------|----------|
| CQ1-CQ9 finalized questions | Comprehension Quiz section (Paths A/B) |
| CQ10-CQ15 finalized questions | Comprehension Quiz expansion (Path C) |
| Question themes | Task instruction for Explainer/Learner |

### Auto-Generated Fields (Paths A/B only)

| Field | How Generated |
|-------|---------------|
| Reference material filename | `{task-id}.pdf` from Task ID |
| AI system prompt | Fixed: `You are a helpful AI assistant that provides clear, informative, and educational information.` |
| Task topic | Same as or elaborates Task title |
| Task instruction for Explainer | Derived from CQ themes |
| Task instruction for Learner | Derived from CQ7-CQ9 problem types |
| Formulas | `NA` unless math content present |

## Critical Consistency Requirements

This agent ensures every generated task file follows the EXACT same structure. Deviations break downstream processing.

---

## Output File Structure

### 1. Header Format

```markdown
# [Use case]: [Task title]
```

**Format rules:**
- Use case and task title separated by colon and space
- First letter of use case capitalized, rest lowercase (unless proper noun)
- Task title in sentence case

**Examples:**
- `# Computer science principles: Safe computing`
- `# Social sciences: Measuring public opinion`

---

### 2. Metadata Table

```markdown
| **Metadata** | For researchers only |
|---|---|
| **Domain** | [domain] |
| **Use case** | [use_case] |
| **Use case description** | [description] |
| **Knowledge dimensions** | [dimensions] |
| **Reference material filename** | [task-id].pdf |
| **Reference material source** | [source] |
| **Comprehension quiz source** | [source] |
| **Task inspiration** | [inspiration] |
| **AI system prompt** | You are a helpful AI assistant that provides clear, informative, and educational information. |
```

**IMPORTANT:** Do NOT include [STORED], [USED], [NOT STORED] tags in the filled template.

**Path C:** Copy this table verbatim from the existing file. Do NOT modify any fields.

---

### 3. Task Data Table

```markdown
| **Task data** | Displayed for participants |
|---|---|
| **Task ID** | [task-id] |
| **Task title** | [title] |
| **Task topic** | [topic] |
| **Task description** | [description] |
| **Task instruction for Explainer** | [instructions] |
| **Task instruction for Learner** | [instructions] |
| **Formulas** | NA |
```

**Path C:** Copy Task ID, Task title, Task topic, and Formulas verbatim. For Task description, Task instruction for Explainer, and Task instruction for Learner, apply the Path C Task Instruction Update Logic (see below).

---

### 4. Task Instructions Generation (Paths A/B)

Derive from comprehension quiz content.

**Task description pattern (~50 words):**
```
[Context sentence about the topic]. In this task, you will need to learn as much as you can about [topic], including [2-3 key areas extracted from CQ themes].
```

**Explainer instruction pattern:**
```
You will need to provide clear and accurate information about [topic] to your partner later. Your partner may come with specific questions with details, including but not exhaustive of [theme 1], [theme 2], and [theme 3], so pay attention to these details.
```

**Learner instruction pattern:**
```
Your partner will have gained knowledge about [topic], and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: 1. [Problem type from CQ7-9]. 2. [Problem type from CQ7-9]. 3. [Problem type from CQ7-9].
```

### 5. Path C: Task Instruction Update Logic

After CQ10-CQ15 are finalized, compare the themes they test against the current Task instructions in the existing file. Update ONLY if new themes are introduced:

**Task description**: If CQ10-CQ15 introduce a major topic area not already mentioned in the "including [areas]" clause, append it. Otherwise copy the existing value verbatim.

**Explainer instruction**: If CQ10-CQ15 introduce themes not already in the "including but not exhaustive of" list, add them to the list. Do NOT remove any existing themes. Otherwise copy the existing value verbatim.

**Learner instruction**: If CQ14-CQ15 (Applying level) introduce problem types not already in the existing numbered list, add them as items 4-5. Do NOT remove or renumber existing items 1-3. Otherwise copy the existing value verbatim.

**If CQ10-CQ15 cover the same themes already represented in CQ1-CQ9, leave all three Task instruction fields unchanged (copy verbatim).**

---

## Familiarity Quiz Structure (FQ1-FQ4 ONLY)

Generate only 4 custom familiarity questions. Standard questions (FQ5-FQ11) are NOT included in the output file.

**Path C:** Copy the entire Familiarity Quiz section verbatim from the existing file. Do NOT modify any FQ questions.

| Question | Category | Bloom's Level | Question Pattern | Options |
|----------|----------|---------------|------------------|---------|
| FQ1 | Domain-specific | Remembering | "How familiar are you with [domain terms]?" | Familiarity scale |
| FQ2 | Domain-specific | Understanding | "How well do you understand [domain concepts]?" | Understanding scale |
| FQ3 | Task-specific | Remembering | "How familiar are you with [task terms]?" | Familiarity scale |
| FQ4 | Task-specific | Understanding | "How well do you understand [task concepts]?" | Understanding scale |

### Likert Scales

**Remembering (FQ1, FQ3):**
```json
["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"]
```

**Understanding (FQ2, FQ4):**
```json
["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"]
```

### FQ Table Format

Each FQ uses this exact table structure:

```markdown
| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ[N] |
| **Question** | Participants | [question text] |
| **Options** | Participants | [options array] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | [Domain-specific | Task-specific] |
| **Bloom's level** | Researcher-only | [Remembering | Understanding] |
```

---

## Comprehension Quiz Structure

### Question Distribution

#### Paths A/B (9 questions)

| Questions | Bloom's Level |
|-----------|---------------|
| CQ1-CQ3 | Remembering |
| CQ4-CQ6 | Understanding |
| CQ7-CQ9 | Applying |

#### Path C: Expanded (15 questions total)

| Questions | Bloom's Level | Source |
|-----------|---------------|--------|
| CQ1-CQ3 | Remembering | Existing (frozen) |
| CQ4-CQ6 | Understanding | Existing (frozen) |
| CQ7-CQ9 | Applying | Existing (frozen) |
| CQ10-CQ11 | Remembering | New (generated) |
| CQ12-CQ13 | Understanding | New (generated) |
| CQ14-CQ15 | Applying | New (generated) |

**Path C:** CQ1-CQ9 must be copied verbatim from the existing file. CQ10-CQ15 are appended after CQ9 using the exact same table format.

### Option Format

Number of options is configurable via input. **Default is 5 options (A-E).**

**Path C:** Match the option count used in the existing CQ1-CQ9. If existing questions use 5 options, CQ10-CQ15 must also use 5 options.

**5 options (default):**
```markdown
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
```

**4 options (if specified):**
```markdown
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]"] |
```

### CQ Table Format

```markdown
| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ[N] |
| **Question** | Participants | [question text] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | [Remembering | Understanding | Applying] |
```

**Note:** Use 5 options (A-E) by default. Use 4 options (A-D) only if specified in input.

### Correct Answer Format

Include the full option text with letter prefix:

```markdown
| **Correct answers** | Researcher-only | ["B. Random selection allows generalization to the larger population"] |
```

---

## Complete Output Template

### Paths A/B Template (9 CQs)

```markdown
# [Use case]: [Task title]

| **Metadata** | For researchers only |
|---|---|
| **Domain** | [domain] |
| **Use case** | [use_case] |
| **Use case description** | [description] |
| **Knowledge dimensions** | [dimensions] |
| **Reference material filename** | [task-id].pdf |
| **Reference material source** | [source] |
| **Comprehension quiz source** | [source] |
| **Task inspiration** | [inspiration] |
| **AI system prompt** | You are a helpful AI assistant that provides clear, informative, and educational information. |

| **Task data** | Displayed for participants |
|---|---|
| **Task ID** | [task-id] |
| **Task title** | [title] |
| **Task topic** | [topic] |
| **Task description** | [description] |
| **Task instruction for Explainer** | [instructions] |
| **Task instruction for Learner** | [instructions] |
| **Formulas** | NA |


## Familiarity Quiz

[FQ1 table]

[FQ2 table]

[FQ3 table]

[FQ4 table]

## Comprehension Quiz

[CQ1 table]

[CQ2 table]

[CQ3 table]

[CQ4 table]

[CQ5 table]

[CQ6 table]

[CQ7 table]

[CQ8 table]

[CQ9 table]
```

### Path C Template (15 CQs — expanded)

```markdown
# [Use case]: [Task title]                    ← FROZEN: copy from existing file

| **Metadata** | For researchers only |        ← FROZEN: copy entire table from existing file
|---|---|
| ... |

| **Task data** | Displayed for participants |  ← CONDITIONALLY UPDATED: see modification scope
|---|---|
| ... |


## Familiarity Quiz                            ← FROZEN: copy entire section from existing file

[FQ1-FQ4 tables — verbatim from existing file]

## Comprehension Quiz

[CQ1 table — FROZEN from existing file]

[CQ2 table — FROZEN from existing file]

[CQ3 table — FROZEN from existing file]

[CQ4 table — FROZEN from existing file]

[CQ5 table — FROZEN from existing file]

[CQ6 table — FROZEN from existing file]

[CQ7 table — FROZEN from existing file]

[CQ8 table — FROZEN from existing file]

[CQ9 table — FROZEN from existing file]

[CQ10 table — NEW: Remembering]

[CQ11 table — NEW: Remembering]

[CQ12 table — NEW: Understanding]

[CQ13 table — NEW: Understanding]

[CQ14 table — NEW: Applying]

[CQ15 table — NEW: Applying]
```

---

## Validation Checklist

### Structure Validation
- [ ] Header follows `# [Use case]: [Task title]` format
- [ ] Metadata table has all 9 fields
- [ ] Task data table has all 7 fields
- [ ] No [STORED]/[USED]/[NOT STORED] tags in output

### Naming Validation
- [ ] Task ID is lowercase with dashes only
- [ ] Task ID has 1-3 dashes (2-4 words)
- [ ] Output filename matches `{task-id}.md`
- [ ] Reference material filename matches `{task-id}.pdf`
- [ ] Task title ≤ 5 words
- [ ] Task topic ≤ 8 words

### Familiarity Quiz Validation
- [ ] FQ1-FQ4 present (4 custom questions only)
- [ ] FQ1-FQ2 are Domain-specific (Remembering, Understanding)
- [ ] FQ3-FQ4 are Task-specific (Remembering, Understanding)
- [ ] Correct Likert scales used for each Bloom's level
- [ ] NO FQ5-FQ11 in output file
- [ ] Total: 4 FQ questions

### Comprehension Quiz Validation (Paths A/B)
- [ ] CQ1-CQ9 present (9 questions)
- [ ] CQ1-CQ3 are Remembering
- [ ] CQ4-CQ6 are Understanding
- [ ] CQ7-CQ9 are Applying
- [ ] Each CQ has correct number of options (5 by default, or 4 if specified)
- [ ] Options formatted as `"A. [text]"`
- [ ] Correct answers include letter AND full text

### Comprehension Quiz Validation (Path C — Expansion)
- [ ] CQ1-CQ15 present (15 questions total)
- [ ] CQ1-CQ9 are identical to the existing file (no modifications)
- [ ] CQ10-CQ11 are Remembering
- [ ] CQ12-CQ13 are Understanding
- [ ] CQ14-CQ15 are Applying
- [ ] CQ10-CQ15 use the same option count as CQ1-CQ9
- [ ] CQ10-CQ15 follow the exact same table format as CQ1-CQ9
- [ ] Options formatted as `"A. [text]"`
- [ ] Correct answers include letter AND full text
- [ ] No concept overlap between CQ10-CQ15 and CQ1-CQ9

### Path C Frozen Content Validation
- [ ] Metadata table is identical to existing file
- [ ] Task data frozen fields (Task ID, Task title, Task topic, Formulas) are identical to existing file
- [ ] FQ1-FQ4 are identical to existing file
- [ ] CQ1-CQ9 are identical to existing file

### Table Format Validation
- [ ] All tables use `| Field | Visibility | Value |` header
- [ ] All tables use `|---|---|---|` separator
- [ ] Field names are bold (`**Question ID**`)
- [ ] Options are JSON arrays with double quotes

---

## Common Errors to Avoid

| Error | Correct Format |
|-------|----------------|
| Wrong number of options | 5 options (A-E) by default, 4 options (A-D) if specified |
| Missing letter prefix in options | `"A. Option text"` |
| Including FQ5-FQ11 | Only FQ1-FQ4 in output |
| Including [STORED] tags | Remove all field usage tags |
| Wrong Likert scale | Familiarity scale for Remembering, Understanding scale for Understanding |
| Inconsistent table structure | Use exact Field/Visibility/Value format |
| (Path C) Modifying frozen sections | CQ1-CQ9, Metadata, FQ1-FQ4 must be verbatim copies |
| (Path C) Removing existing Task instruction content | Only append to existing themes/items, never remove |
| (Path C) Mismatched option count in CQ10-CQ15 | Must match option count used in existing CQ1-CQ9 |
