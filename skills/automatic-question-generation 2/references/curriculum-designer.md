# Curriculum Designer Agent

Derives learning objectives and familiarity quiz terms FROM the completed comprehension quiz, ensuring alignment between what students learn and what they're tested on.

## Position in Workflow

This agent runs AFTER the psychometric reviewer has finalized the 9 comprehension questions (CQ1-CQ9). This ensures learning objectives reflect exactly what students need to know to answer the questions.

## Responsibilities

1. Analyze each comprehension question to identify required knowledge/skills
2. Derive specific, measurable learning objectives from the questions
3. Generate familiarity quiz terms (FQ1-FQ4) based on prerequisite knowledge
4. Ensure learning objectives map directly to comprehension questions
5. Verify alignment between familiarity quiz, learning objectives, and comprehension quiz

## Input Format

```json
{
  "workflow_id": "string",
  "domain": "Health" | "Finance" | "Civic" | "Legal" | "Education/STEM",
  "topic_title": "string",
  "source_materials": ["validated source URLs/references"],
  "comprehension_quiz": {
    "CQ1": { "question": "...", "correct_answer": "...", "bloom_level": "Remembering" },
    "CQ2": { "question": "...", "correct_answer": "...", "bloom_level": "Remembering" },
    "CQ3": { "question": "...", "correct_answer": "...", "bloom_level": "Remembering" },
    "CQ4": { "question": "...", "correct_answer": "...", "bloom_level": "Understanding" },
    "CQ5": { "question": "...", "correct_answer": "...", "bloom_level": "Understanding" },
    "CQ6": { "question": "...", "correct_answer": "...", "bloom_level": "Understanding" },
    "CQ7": { "question": "...", "correct_answer": "...", "bloom_level": "Applying" },
    "CQ8": { "question": "...", "correct_answer": "...", "bloom_level": "Applying" },
    "CQ9": { "question": "...", "correct_answer": "...", "bloom_level": "Applying" }
  }
}
```

## Output Format

```json
{
  "workflow_id": "string",
  "status": "ready" | "alignment_issues",
  "task_title": "string (≤5 words)",
  "task_id": "string (lowercase-with-dashes, 3-4 words)",
  "task_topic": "string (≤8 words)",
  "task_description": "string",
  "use_case": "string",
  "knowledge_dimensions": ["factual", "conceptual", "procedural", "metacognitive"],
  "learning_objectives": [
    {
      "id": "LO1",
      "text": "After completing this topic, learners will be able to...",
      "bloom_level": "Remembering" | "Understanding" | "Applying",
      "maps_to_questions": ["CQ1", "CQ2"]
    }
  ],
  "familiarity_questions": {
    "FQ1": "How familiar are you with [DOMAIN TERMS]?",
    "FQ2": "How well do you understand [DOMAIN CONCEPTS]?",
    "FQ3": "How familiar are you with [TASK TERMS]?",
    "FQ4": "How well do you understand [TASK CONCEPTS]?"
  },
  "key_concepts": ["concepts extracted from comprehension questions"],
  "question_to_objective_mapping": {
    "CQ1": "LO1",
    "CQ2": "LO1"
  }
}
```

## Deriving Learning Objectives from Questions

### Process

1. **Analyze each CQ**: What specific knowledge or skill does answering this question require?
2. **Group related questions**: Which questions test similar knowledge areas?
3. **Write objectives**: Create learning objectives that, if achieved, would enable correct answers
4. **Verify coverage**: Every CQ must map to at least one learning objective

### Derivation Rules

| Question Type | Derivation Approach |
|---------------|---------------------|
| CQ1-CQ3 (Remembering) | Extract specific facts, thresholds, criteria tested → "Identify/Recall/List [specific fact]" |
| CQ4-CQ6 (Understanding) | Identify relationships/mechanisms tested → "Explain/Distinguish/Summarize [concept]" |
| CQ7-CQ9 (Applying) | Identify decision rules/procedures tested → "Apply/Determine/Select [in scenario]" |

### Example Derivation

**Input CQ (Remembering):**
> "What is the minimum internal temperature for safely cooked chicken?"
> Correct: 165°F

**Derived Learning Objective:**
> "LO1: Recall the FDA-recommended minimum internal cooking temperatures for common proteins (chicken: 165°F, ground beef: 160°F, pork: 145°F)"
> Maps to: CQ1, CQ2

**Input CQ (Applying):**
> "Maria's thermometer reads 155°F in the thickest part of a chicken breast. What should she do?"
> Correct: Continue cooking until it reaches 165°F

**Derived Learning Objective:**
> "LO3: Apply safe cooking temperature guidelines to determine when meat is safe to serve"
> Maps to: CQ7

## Task ID Generation

Generate Task ID from Task Title:
- **Format**: lowercase words separated by dashes
- **Ideal**: 3 words (2 dashes), e.g., `nutrition-label-basics`
- **Maximum**: 4 words (3 dashes)
- **Rules**: Remove articles, keep distinctive terms

Task ID determines filenames:
- Output: `{task-id}.md`
- Reference material: `{task-id}.pdf`

## Familiarity Quiz Terms (FQ1-FQ4)

Generate a 4-question custom familiarity quiz based on prerequisite knowledge needed for the comprehension quiz. These questions cover TWO Bloom's levels (Remembering and Understanding) for both domain and task.

### Derivation from Comprehension Quiz

1. **Identify prerequisite terms**: What domain/topic terms appear in the CQs?
2. **Identify prerequisite concepts**: What must students understand before tackling the CQs?
3. **Generate FQ1-FQ2**: Domain knowledge (Remembering, Understanding)
4. **Generate FQ3-FQ4**: Task-specific knowledge (Remembering, Understanding)

### Question Structure

| Question | Category | Bloom's Level | Question Pattern | Options |
|----------|----------|---------------|------------------|---------|
| FQ1 | Domain-specific | Remembering | "How familiar are you with [domain terms]?" | Familiarity scale |
| FQ2 | Domain-specific | Understanding | "How well do you understand [domain concepts]?" | Understanding scale |
| FQ3 | Task-specific | Remembering | "How familiar are you with [task terms from CQs]?" | Familiarity scale |
| FQ4 | Task-specific | Understanding | "How well do you understand [task concepts from CQs]?" | Understanding scale |

### Likert Scales

**Remembering (FQ1, FQ3):**
```json
["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"]
```

**Understanding (FQ2, FQ4):**
```json
["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"]
```

### Generation Rules

- Maximum **3 examples** in each question stem
- Terms in FQ3-FQ4 should reflect concepts ACTUALLY TESTED in comprehension quiz
- Keep straightforward without giving away comprehension quiz answers
- FQ1-FQ2 should be broader domain terms, not task-specific

### Example

**Input Comprehension Quiz (summarized):**
- Domain: Computer science principles
- Task: Safe computing
- CQ1-3: Test definitions (phishing, encryption, metadata)
- CQ4-6: Test understanding (cyber attack types, security vs privacy)
- CQ7-9: Test application (identifying phishing, evaluating scenarios)

**Derived Familiarity Quiz:**

| FQ | Question |
|----|----------|
| FQ1 | How familiar are you with common computer science terms and definitions such as algorithms, variables, and data types? |
| FQ2 | How well do you understand the concepts behind basic programming logic, such as sequential execution of code, conditional statements, and loop structures? |
| FQ3 | How familiar are you with safe computing terms and definitions such as phishing, encryption, and multifactor authentication? |
| FQ4 | How well do you understand the concepts and mechanisms behind safe computing, such as how different types of cyber attacks compromise data or how encryption protects information? |

### Note on Standard Questions (FQ5-FQ11)

FQ5-FQ11 are standard questions about AI Self-Efficacy and Communication Self-Efficacy that are the same across all tasks. These are **NOT included in the generated output file** - they are added separately by the platform.

## Alignment Verification

Before marking status as "ready", verify:

- [ ] Every CQ maps to at least one learning objective
- [ ] Every learning objective maps to at least one CQ
- [ ] FQ3-FQ4 terms/concepts relate to the comprehension questions
- [ ] Learning objectives use appropriate Bloom's verbs for their level
- [ ] A student who achieves all learning objectives could answer all CQs
- [ ] All 4 custom FQ questions generated (FQ1-FQ4)

If alignment issues are found, flag with specific concerns for review.
