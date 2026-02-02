# Consistency & Formatting Agent

Formats all generated content to the Empirica platform template structure, ensuring identical output format across multiple generation rounds.

## Position in Workflow

This agent runs LAST, after the curriculum designer has derived learning objectives and familiarity quiz content from the finalized comprehension quiz.

## Input Sources

This agent receives data from multiple sources:

### 1. User-Provided Input (from trigger message)

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

### 2. Curriculum Designer Output

| Field | Used For |
|-------|----------|
| FQ1-FQ4 questions | Familiarity Quiz section |
| Learning objectives | Informing Task instructions |

### 3. Psychometric Reviewer Output

| Field | Used For |
|-------|----------|
| CQ1-CQ9 finalized questions | Comprehension Quiz section |
| Question themes | Task instruction for Explainer/Learner |

### Auto-Generated Fields

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

---

### 4. Task Instructions Generation

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

---

## Familiarity Quiz Structure (FQ1-FQ4 ONLY)

Generate only 4 custom familiarity questions. Standard questions (FQ5-FQ11) are NOT included in the output file.

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

## Comprehension Quiz Structure (CQ1-CQ9)

### Question Distribution

| Questions | Bloom's Level |
|-----------|---------------|
| CQ1-CQ3 | Remembering |
| CQ4-CQ6 | Understanding |
| CQ7-CQ9 | Applying |

### Option Format

Number of options is configurable via input. **Default is 5 options (A-E).**

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

### Comprehension Quiz Validation
- [ ] CQ1-CQ9 present (9 questions)
- [ ] CQ1-CQ3 are Remembering
- [ ] CQ4-CQ6 are Understanding
- [ ] CQ7-CQ9 are Applying
- [ ] Each CQ has correct number of options (5 by default, or 4 if specified)
- [ ] Options formatted as `"A. [text]"`
- [ ] Correct answers include letter AND full text

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
