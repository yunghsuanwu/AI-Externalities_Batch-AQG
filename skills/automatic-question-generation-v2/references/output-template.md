# Output Template

Complete Empirica platform task file template based on validated examples.

## Template Structure Overview

### Paths A/B (Standard — 9 CQs)
```
# [Use case]: [Task title]

[Metadata Table]
[Task Data Table]

## Familiarity Quiz
[FQ1-FQ4: Custom questions only]

## Comprehension Quiz
[CQ1-CQ9]
```

### Path C (Expanded — 15 CQs)
```
# [Use case]: [Task title]

[Metadata Table]              ← FROZEN from existing file
[Task Data Table]             ← Conditionally updated (3 fields only)

## Familiarity Quiz
[FQ1-FQ4]                    ← FROZEN from existing file

## Comprehension Quiz
[CQ1-CQ9]                    ← FROZEN from existing file
[CQ10-CQ15]                  ← NEW (appended)
```

**Note:** Standard questions FQ5-FQ11 (AI Self-Efficacy, Communication Self-Efficacy) are NOT included in the generated output file. They are added separately by the platform.

---

## Complete Template (Paths A/B)

```markdown
# [Use case]: [Task title]

| **Metadata** | For researchers only |
|---|---|
| **Domain** | [domain] |
| **Use case** | [use_case] |
| **Use case description** | [description] |
| **Knowledge dimensions** | [knowledge_dimensions] |
| **Reference material filename** | [task-id].pdf |
| **Reference material source** | [source] |
| **Comprehension quiz source** | [source] |
| **Task inspiration** | [inspiration] |
| **AI system prompt** | You are a helpful AI assistant that provides clear, informative, and educational information. |

| **Task data** | Displayed for participants |
|---|---|
| **Task ID** | [task-id] |
| **Task title** | [Task title] |
| **Task topic** | [Task topic] |
| **Task description** | [Task description] |
| **Task instruction for Explainer** | [Explainer instructions] |
| **Task instruction for Learner** | [Learner instructions] |
| **Formulas** | NA |


## Familiarity Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ1 |
| **Question** | Participants | How familiar are you with [domain terms, max 3 examples]? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ2 |
| **Question** | Participants | How well do you understand [domain concepts]? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ3 |
| **Question** | Participants | How familiar are you with [task terms, max 3 examples]? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ4 |
| **Question** | Participants | How well do you understand [task concepts]? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Understanding |

## Comprehension Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ1 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ2 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ3 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ4 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ5 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ6 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ7 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ8 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ9 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Applying |
```

---

## Path C Expansion Template (CQ10-CQ15 only)

When operating in Path C, CQ1-CQ9 are copied verbatim from the existing file. The following CQ10-CQ15 tables are **appended** after the last existing CQ (CQ9):

```markdown
| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ10 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ11 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ12 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ13 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ14 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ15 |
| **Question** | Participants | [question] |
| **Options** | Participants | ["A. [option1]", "B. [option2]", "C. [option3]", "D. [option4]", "E. [option5]"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["[Letter]. [full correct option text]"] |
| **Bloom's level** | Researcher-only | Applying |
```

---

## Field Specifications

### Metadata Fields

| Field | Required | Format | Example |
|-------|----------|--------|---------|
| Domain | Yes | Category | `STEM Education`, `Non-STEM education` |
| Use case | Yes | Subcategory | `Computer science principles`, `Social sciences` |
| Use case description | Yes | 1-2 sentences | `Learn about core principles...` |
| Knowledge dimensions | Yes | Bloom's taxonomy | `Conceptual`, `Factual`, `Conceptual/factual` |
| Reference material filename | Auto | `{task-id}.pdf` | `safe-computing.pdf` |
| Reference material source | Yes | Brief description | `The RMs are drawn from Barron's (2ed).` |
| Comprehension quiz source | Yes | Brief description | `The CQs are drawn from...` |
| Task inspiration | Optional | Source reference | `Drawn from College Board AP...` |
| AI system prompt | Fixed | Always this exact text | `You are a helpful AI assistant...` |

### Task Data Fields

| Field | Max Length | Format |
|-------|------------|--------|
| Task ID | 4 words | `lowercase-with-dashes` |
| Task title | 5 words | Title case |
| Task topic | 8 words | Matches or elaborates title |
| Task description | ~50 words | Single paragraph |
| Task instruction for Explainer | ~60 words | Single paragraph |
| Task instruction for Learner | ~80 words | Numbered list (1. 2. 3.) |
| Formulas | N/A | `NA` or LaTeX dictionary |

---

## Familiarity Quiz Structure (FQ1-FQ4)

Only 4 custom questions are generated. Standard questions (FQ5-FQ11) are NOT included in the output.

| Question | Category | Bloom's Level | Question Stem | Options |
|----------|----------|---------------|---------------|---------|
| FQ1 | Domain-specific | Remembering | "How familiar are you with..." | Familiarity scale |
| FQ2 | Domain-specific | Understanding | "How well do you understand..." | Understanding scale |
| FQ3 | Task-specific | Remembering | "How familiar are you with..." | Familiarity scale |
| FQ4 | Task-specific | Understanding | "How well do you understand..." | Understanding scale |

### Likert Scales

**Remembering (FQ1, FQ3):**
```json
["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"]
```

**Understanding (FQ2, FQ4):**
```json
["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"]
```

---

## Comprehension Quiz Structure

### Bloom's Distribution

#### Paths A/B (9 questions)

| Questions | Bloom's Level | Question Types |
|-----------|---------------|----------------|
| CQ1-CQ3 | Remembering | Definitions, facts, identification |
| CQ4-CQ6 | Understanding | Explanations, classifications, scenarios |
| CQ7-CQ9 | Applying | Complex scenarios, problem-solving, judgment |

#### Path C Expanded (15 questions total)

| Questions | Bloom's Level | Question Types | Source |
|-----------|---------------|----------------|--------|
| CQ1-CQ3 | Remembering | Definitions, facts, identification | Existing (frozen) |
| CQ4-CQ6 | Understanding | Explanations, classifications, scenarios | Existing (frozen) |
| CQ7-CQ9 | Applying | Complex scenarios, problem-solving, judgment | Existing (frozen) |
| CQ10-CQ11 | Remembering | Definitions, facts, identification | New (generated) |
| CQ12-CQ13 | Understanding | Explanations, classifications, scenarios | New (generated) |
| CQ14-CQ15 | Applying | Complex scenarios, problem-solving, judgment | New (generated) |

### Option Format

Number of options is configurable. **Default is 5 options (A-E).**

**5 options (default):**
```json
["A. [option text]", "B. [option text]", "C. [option text]", "D. [option text]", "E. [option text]"]
```

**4 options (if specified in input):**
```json
["A. [option text]", "B. [option text]", "C. [option text]", "D. [option text]"]
```

### Correct Answer Format

Include letter prefix AND full option text:
```json
["B. Random selection allows generalization to the larger population"]
```

---

## Examples from Validated Tasks

### Example 1: Safe Computing (STEM)

**Header:** `# Computer science principles: Safe computing`

**FQ1 (Domain, Remembering):**
> How familiar are you with common computer science terms and definitions such as algorithms, variables, and data types?

**FQ2 (Domain, Understanding):**
> How well do you understand the concepts behind basic programming logic, such as sequential execution of code, conditional statements, and loop structures?

**FQ3 (Task, Remembering):**
> How familiar are you with safe computing terms and definitions such as phishing, encryption, and multifactor authentication?

**FQ4 (Task, Understanding):**
> How well do you understand the concepts and mechanisms behind safe computing, such as how different types of cyber attacks compromise data or how encryption protects information?

### Example 2: Measuring Public Opinion (Non-STEM)

**Header:** `# Social sciences: Measuring public opinion`

**FQ1 (Domain, Remembering):**
> How familiar are you with common terms and definitions used in social sciences, such as institutions, norms, power structures, and social groups?

**FQ2 (Domain, Understanding):**
> How well do you understand how social, political, and economic factors interact to shape human behavior and societal outcomes?

**FQ3 (Task, Remembering):**
> How familiar are you with key terms related to measuring public opinion, such as probability sampling, random digit dialing, and selection bias?

**FQ4 (Task, Understanding):**
> How well do you understand how factors like sampling methods and survey design affect the accuracy of public opinion polls?

---

## Validation Checklist

### Structure
- [ ] Header follows `# [Use case]: [Task title]` format
- [ ] Metadata table has all 9 rows
- [ ] Task data table has all 7 rows
- [ ] Two blank lines after Task data table, before Familiarity Quiz

### Naming
- [ ] Task ID is lowercase with dashes
- [ ] Task ID has 1-3 dashes (2-4 words)
- [ ] Reference material filename is `{task-id}.pdf`
- [ ] Task title ≤ 5 words
- [ ] Task topic ≤ 8 words

### Familiarity Quiz
- [ ] FQ1-FQ4 present (4 custom questions only)
- [ ] FQ1-FQ2 are Domain-specific (Remembering, Understanding)
- [ ] FQ3-FQ4 are Task-specific (Remembering, Understanding)
- [ ] Correct Likert scale for each Bloom's level
- [ ] NO FQ5-FQ11 in output (standard questions added by platform)
- [ ] Total: 4 FQ questions in output

### Comprehension Quiz (Paths A/B)
- [ ] CQ1-CQ9 present (9 questions)
- [ ] CQ1-CQ3 are Remembering
- [ ] CQ4-CQ6 are Understanding
- [ ] CQ7-CQ9 are Applying
- [ ] Each CQ has correct number of options (5 by default, or 4 if specified)
- [ ] Options formatted as `"A. [text]"`
- [ ] Correct answers include letter AND full text

### Comprehension Quiz (Path C — Expansion)
- [ ] CQ1-CQ15 present (15 questions total)
- [ ] CQ1-CQ9 are identical to existing file (verbatim)
- [ ] CQ10-CQ11 are Remembering
- [ ] CQ12-CQ13 are Understanding
- [ ] CQ14-CQ15 are Applying
- [ ] CQ10-CQ15 use same option count as CQ1-CQ9
- [ ] CQ10-CQ15 follow exact same table format as CQ1-CQ9
- [ ] No concept overlap between CQ10-CQ15 and CQ1-CQ9

### Tables
- [ ] All tables use `| Field | Visibility | Value |` header
- [ ] All tables use `|---|---|---|` separator
- [ ] Field names are bold (`**Question ID**`)
- [ ] Options are JSON arrays with double quotes
