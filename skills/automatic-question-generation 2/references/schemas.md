# Workflow Schemas

JSON schemas for the educational content generation workflow.

## Comprehension Question Schema

All questions must be **single-select MCQs** with **5 options** (1 key + 4 distractors).

```json
{
  "question_id": "CQ1",
  "question_text": "string",
  "options": [
    "A. option1",
    "B. option2", 
    "C. option3",
    "D. option4",
    "E. option5"
  ],
  "correct_answer": ["A. option1"],
  "bloom_level": "Remembering | Understanding | Applying",
  "difficulty": "medium | medium-hard | hard",
  "source_evidence": "specific fact from source",
  "distractor_rationale": {
    "B": "why this is a plausible wrong answer",
    "C": "why this is a plausible wrong answer",
    "D": "why this is a plausible wrong answer",
    "E": "why this is a plausible wrong answer"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_qualifiers": true,
    "no_stem_repetition": true,
    "no_absolute_terms": true
  }
}
```

## MCQ Best Practices Checklist

| Criterion | Description |
|-----------|-------------|
| single_key | Exactly one unambiguous correct answer |
| key_length_balanced | Key similar in length to distractors |
| plausible_distractors | All distractors based on real misconceptions |
| no_grammar_hints | No grammatical clues revealing answer |
| no_all_none_above | No "all of the above" or "none of the above" |
| no_ambiguity | Clear, unambiguous wording |
| no_double_negatives | No confusing double negations |
| no_qualifiers | No "sometimes," "usually" in options |
| no_stem_repetition | Key doesn't echo stem wording |
| no_absolute_terms | No "always," "never" (unless testing exceptions) |

## Bloom's Distribution Requirement

```json
{
  "Remembering": ["CQ1", "CQ2", "CQ3"],
  "Understanding": ["CQ4", "CQ5", "CQ6"],
  "Applying": ["CQ7", "CQ8", "CQ9"]
}
```

## Familiarity Question Schema (FQ1-FQ4)

Pre-test quiz to assess prior knowledge before the paired learning activity. Both explainers and learners complete this before interaction.

```json
{
  "question_id": "FQ1",
  "question": "How familiar are you with [terms/concepts]?",
  "options": ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"],
  "answer_type": "Single-select",
  "category": "Domain-specific | Task-specific",
  "bloom_level": "Remembering | Understanding"
}
```

### Generation Rules

- Maximum **3 examples** in each question stem
- Keep straightforward without giving away comprehension quiz content
- Domain-specific questions (FQ1-FQ2): Broader about the domain, not task-specific
- Topic-specific questions (FQ3-FQ4): Focus on the specific topic

### Question Patterns

| Question | Category | Bloom's Level | Pattern |
|----------|----------|---------------|---------|
| FQ1 | Domain-specific | Remembering | "How familiar are you with [COMMON TERMS OR DEFINITIONS IN A DOMAIN]?" |
| FQ2 | Domain-specific | Understanding | "How well do you understand [CONCEPTS OR MECHANISMS IN A DOMAIN]?" |
| FQ3 | Task-specific | Remembering | "How familiar are you with [COMMON TERMS, DEFINITIONS, OR BASIC FACTS OF A GIVEN TOPIC]?" |
| FQ4 | Task-specific | Understanding | "How well do you understand [CONCEPTS, MECHANISMS, OR CAUSAL RELATIONSHIPS OF A GIVEN TOPIC]?" |

### Likert Scale Options

**Familiarity (FQ1, FQ3)**:
```json
["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"]
```

**Understanding (FQ2, FQ4)**:
```json
["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"]
```

## Task Data Schema

```json
{
  "task_id": "lowercase-words-with-dashes (3-4 words)",
  "task_title": "string (≤5 words)",
  "task_topic": "string (≤8 words)",
  "task_description": "string (~50 words)",
  "task_instruction_explainer": "string",
  "task_instruction_learner": "string",
  "formulas": {} | "NA"
}
```

### Task ID Rules

- Lowercase only
- Words separated by dashes
- Ideal: 3 words (2 dashes), e.g., `nutrition-label-basics`
- Maximum: 4 words (3 dashes)
- Used for filenames: `{task-id}.md`, `{task-id}.pdf`

## Metadata Schema

```json
{
  "domain": "Education/STEM | Health | Finance | Civic | Legal",
  "use_case": "string (task type within domain)",
  "use_case_description": "string (documentation only)",
  "knowledge_dimensions": ["factual", "conceptual", "procedural", "metacognitive"],
  "reference_material_filename": "{task-id}.pdf",
  "reference_material_source": "string",
  "task_inspiration": "string (optional)",
  "ai_system_prompt": "You are a helpful AI assistant that provides clear, informative, and educational information."
}
```

## Workflow State Schema

```json
{
  "workflow_id": "string",
  "status": "initiated | in_progress | review_required | completed | failed",
  "domain": "Health | Finance | Civic | Legal | Education/STEM",
  "stages": {
    "curriculum_design": {"status": "pending | success | failed"},
    "source_discovery": {"status": "pending | success | failed"},
    "domain_review": {"status": "pending | success | failed"},
    "question_writing": {"status": "pending | success | failed"},
    "psychometric_review": {"status": "pending | success | failed"},
    "formatting": {"status": "pending | success | failed"}
  },
  "quality_flags": [],
  "final_output": {
    "task_id": "string",
    "question_count": 9,
    "average_difficulty": "medium-hard"
  }
}
```

## Question Difficulty Schema

```json
{
  "question_id": "CQ1",
  "difficulty_assessment": {
    "source_dependency": "1-10 (10 = impossible without source)",
    "distractor_quality": "1-10 (10 = all highly plausible)",
    "common_sense_answerable": false,
    "estimated_success_rate": "40-75%"
  },
  "overall_score": 8.5,
  "pass_threshold": 7.0
}
```
