---
name: automatic-question-generation
description: Multi-agent workflow for automatically generating psychometrically sound multiple-choice questions (MCQs) for the Empirica platform. Produces 9 comprehension questions (CQ1-CQ9) across Bloom's taxonomy levels (Remembering, Understanding, Applying) that discriminate between learners who studied and those who didn't. Triggers on requests to generate quiz questions, create MCQs, build question banks, produce assessments, or create comprehension tests for any domain (Health, Finance, Legal, Civic, Education/STEM).
---

# Automatic Question Generation

A multi-agent system for automatically generating **genuinely challenging assessment questions** that measure actual learning.

## ⚠️ Core Quality Standard: Discrimination

**The purpose of assessment is to distinguish learners who studied from those who didn't.**

| Metric | Target (5 options) | Target (4 options) |
|--------|--------------------|--------------------|
| Informed learner accuracy | 50-75% | 50-75% |
| Uninformed adult accuracy | ~20% (chance) | ~25% (chance) |
| Each distractor attraction | ~20% of uninformed | ~25% of uninformed |

**If an uninformed adult could score >40%, the questions are too easy.**

## Question Difficulty Requirements

### What Makes Questions CHALLENGING

✅ Tests specific facts/thresholds that require reading the material  
✅ All 4 wrong answers are based on real misconceptions  
✅ Requires integration of multiple concepts  
✅ Complex scenarios with competing reasonable options  
✅ Cannot be answered through common sense or elimination  

### What Makes Questions TOO EASY (Reject These)

❌ Answerable by common sense ("Should you save money?")  
❌ One obviously correct answer among absurd options  
❌ Tests basic definitions everyone knows  
❌ Correct answer stands out (longer, more detailed)  
❌ Exploitable through test-taking strategies  

## Workflow

The workflow adapts based on input provided:

### Path A: Basic Input Only
When given only `domain` and `topic_title` (no reference material or sample questions):
```
Topic → Source Discovery → Domain Review → Question Writing → 
Psychometric Review → Curriculum Design → Formatting
```

### Path B: Source Materials Provided
When given reference material and/or sample questions (as PDF attachments, URLs, or directly extracted text content):
```
Topic + Sources → [Sample Question Extraction*] → Question Writing → 
Psychometric Review → Curriculum Design → Formatting
```
*Sample Question Extraction runs when "extract sample questions" prompt is provided

### Path B with Extraction (Detailed)
When sample questions need filtering to match reference material scope:
```
1. Reference Material Analysis (identify scope boundaries)
2. Sample Question Extraction (filter to in-scope questions only)
3. Question Writing (use extracted questions as inspiration)
4. Psychometric Review → Curriculum Design → Formatting
```

**Key principle:** Familiarity quiz and learning objectives are derived FROM the comprehension quiz, not before it. This ensures learning objectives reflect exactly what students need to know to answer the questions.

## Additional Prompts

When triggering this skill, you may include additional prompts beyond the standard input fields. These prompts modify or extend the workflow.

### "Extract Sample Questions"

Use this prompt when you provide a sample questions document that contains questions beyond the scope of the reference material.

**When to use:**
- Sample questions document covers multiple topics, but only some relate to your reference material
- Review questions from a textbook chapter that includes content outside your specific scope
- Question banks that need filtering to match your reference material

**What it does:**
The Sample Question Extractor agent will:
1. Analyze the reference material to identify its scope (topics, concepts, facts covered)
2. Review each question in the sample questions document
3. Extract ONLY questions that can be answered using information in the reference material
4. Flag questions that are partially in scope (some options require out-of-scope knowledge)
5. Output a filtered set of in-scope questions for the Question Writer to use as inspiration

**Example usage:**
```
Domain: Health
Task ID: nutrition-labels
Task title: Reading Nutrition Labels
Reference material: FDA_Nutrition_Facts_Label_Guide.pdf
Sample questions: Chapter_5_Review_Questions.pdf
Additional prompt: Extract sample questions - the review questions cover all of Chapter 5, but only sections 5.2-5.4 relate to the FDA guide.
```

**Scope determination criteria:**
- Question stem references concepts explained in reference material
- All answer options (including distractors) relate to in-scope content
- Required knowledge to answer is present in reference material
- Questions testing definitions, facts, or procedures not in reference material are OUT of scope

## Input Format

When triggering this skill, provide input in the following format:

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
* CQ format (if any): [e.g., "single-select MCQs with 5 options and one correct answer"]
```

### Input Field Details

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| Domain | Yes | - | e.g., STEM Education, Non-STEM education, Health, Finance, Civic |
| Use case | Yes | - | Subcategory within domain (e.g., Computer science principles, Social sciences) |
| Use case description | Yes | - | Brief description for documentation |
| Knowledge dimensions | Yes | - | Bloom's taxonomy: factual, conceptual, procedural, metacognitive |
| Reference material | Optional | - | PDF attachment OR URL to fetch. Triggers Path B if provided |
| Reference material content | Optional | - | Directly extracted text from PDF or other source. Triggers Path B if provided. Use when text has already been extracted from a document. |
| Sample questions | Optional | - | PDF attachment OR URL. Used as inspiration for question style |
| Sample questions content | Optional | - | Directly extracted text from sample questions document. Use when text has already been extracted. |
| Reference material source | Optional | - | Documentation of where material came from |
| Comprehension quiz source | Optional | - | Documentation of question source |
| Task inspiration | Optional | - | What inspired this task |
| Task ID | Yes | - | lowercase-with-dashes format |
| Task title | Yes | - | ≤5 words, title case |
| Task description | Yes | - | ~50 words describing the learning task |
| CQ format | Optional | 5 options | Number of options per CQ (4 or 5) |

### Path Detection Logic

```
IF "Reference material" OR "Reference material content" OR "Sample questions" OR "Sample questions content" is provided:
    → Path B (start with Question Writer)
    → IF URL provided: Fetch URL
    → IF filename provided: Use attached PDF
    → IF content provided: Use directly provided text (no fetching needed)
    IF "extract sample questions" prompt is included:
        → Run Sample Question Extractor BEFORE Question Writer
        → Filter sample questions to reference material scope
ELSE:
    → Path A (start with Source Discovery)
    → IF source discovery guidance is provided, process it first
```

### "Source Discovery Guidance" (Path A Only)

Use this prompt when you want to direct the Source Discovery agent toward specific types of sources.

**When to use:**
- You have a preference for certain source types (e.g., "government fact sheets" vs "full guides")
- You have an example source in mind and want similar ones (e.g., "something like the IRS W-4 instructions")
- You want to narrow the topic scope before searching
- You have audience requirements (e.g., "sources for first-time homebuyers")
- You want to exclude certain source types (e.g., "avoid academic papers")

**What it does:**
The Source Discovery agent will:
1. Extract explicit constraints and preferences from your guidance
2. Infer your intent (what you're trying to achieve)
3. Modify the default authority hierarchy if needed
4. Formulate search queries that honor your guidance
5. Document its reasoning transparently in the output

**Example usage:**
```
Domain: Finance
Task ID: overdraft-fees
Task title: Understanding Overdraft Fees
Additional prompt: Look for a specific bank's fee schedule document, something like Chase or Wells Fargo's checking account disclosures. Should be a real document customers would receive, not educational content about fees in general.
```

**Types of guidance you can provide:**

| Guidance Type | Example |
|---------------|---------|
| Source type preference | "Look for government fact sheets rather than full guides" |
| Specific examples | "Something like the IRS W-4 instructions" |
| Topic narrowing | "Focus on overdraft fees specifically, not all bank fees" |
| Audience specification | "Sources written for first-time homebuyers" |
| Exclusions | "Avoid academic papers" |
| Format requirements | "Must be available as PDF" |

### ⚠️ Human Clarification Mode (Revert Mode)

**CRITICAL:** If the input mentions reference materials or sample questions (i.e., the "Reference material" or "Sample questions" field is filled in) but:
- No PDF files are actually attached, AND
- No valid, fetchable URLs are provided, AND
- No direct text content is provided in the "Reference material content" or "Sample questions content" fields

**DO NOT** attempt to perform a web search or find alternative sources independently.

**Instead, STOP and ask the human for clarification:**
> "I see you've indicated reference materials should be provided, but I don't see any attached PDFs, valid URLs, or direct text content. Could you please:
> 1. Attach the PDF file(s), OR
> 2. Provide the URL(s) to fetch, OR
> 3. Provide the extracted text content directly in the 'Reference material content' field, OR
> 4. Confirm you'd like me to proceed with Path A (source discovery) instead?"

This prevents generating questions based on incorrect or unintended source material.

## Agent Files

| Agent | Purpose | Critical Standards |
|-------|---------|-------------------|
| [source-discovery.md](references/source-discovery.md) | Find sources (Path A only) | Sources must have specific, testable facts |
| [domain-experts.md](references/domain-experts.md) | Validate accuracy (Path A only) | Verify all content against source |
| [sample-question-extractor.md](references/sample-question-extractor.md) | Filter sample questions to reference material scope | Only extract questions answerable from reference material |
| [question-writer.md](references/question-writer.md) | Generate questions | 15+ candidates; uses sample_questions as inspiration if provided |
| [psychometric-reviewer.md](references/psychometric-reviewer.md) | **Reject easy questions** | Score ≥7/10, reject >40% of candidates |
| [curriculum-designer.md](references/curriculum-designer.md) | Define learning objectives & familiarity quiz | Derive from final comprehension quiz |
| [consistency-agent.md](references/consistency-agent.md) | Format output | Empirica template structure; **grammar/typo check (American English spelling and punctuation)** |
| [orchestrator.md](references/orchestrator.md) | Coordinate workflow | Detect input type, select path, route revisions |

## Bloom's Taxonomy Targets

| Level | Questions | Cognitive Verbs | What It Tests |
|-------|-----------|-----------------|---------------|
| Remembering | CQ1-CQ3 | recall, define, describe, identify, choose, label, match | Specific facts, thresholds, criteria NOT commonly known |
| Understanding | CQ4-CQ6 | categorize, determine, explain, paraphrase, illustrate, summarize | WHY things work, HOW concepts relate, WHAT distinguishes similar items |
| Applying | CQ7-CQ9 | apply, use, calculate, predict, modify, organize, show | Judgment calls with multiple factors, edge cases, realistic constraints |

## MCQ Writing Best Practices

All questions must be **single-select MCQs** with **4 or 5 options** (1 key + 3-4 distractors) as specified in input. Default is 5 options.

### ⚠️ No Explicit References to Source Materials

**CRITICAL:** Students will NOT have access to the reference materials during the quiz. Questions must test internalized knowledge, not recall of specific document details.

**AVOID:**
- "According to the materials..."
- "According to [specific source name]..."
- "The document states that..."
- "As mentioned in the reading..."
- Questions that require memorizing specific statistics, percentages, or passing details
- Questions about document structure or organization

**INSTEAD, test:**
- Concept definitions and their applications
- Fundamental facts and principles
- Causal relationships and reasoning
- Problem-solving using learned concepts
- Distinctions between similar concepts

**Example transformation:**
- ❌ "According to the CDC guidelines, what percentage of adults should get screened?"
- ✅ "At what age should adults begin routine colorectal cancer screening?"

| Guideline | Do | Don't |
|-----------|-----|-------|
| Key length | Match distractor length | Make key significantly longer |
| Distractors | Base on real misconceptions | Use absurd options |
| Grammar | Match across all options | Include hints revealing answer |
| Options | Use specific answers | Use "all/none of the above" |
| Wording | Clear, unambiguous | Double negatives, qualifiers |
| Negatives | State clearly ("NOT" in caps) | Hide negative phrasing |
| Absolutes | Avoid or use sparingly | "always," "never" in distractors only |
| Key position | Vary across all options | Concentrate in middle positions |

## Generation Workflow

1. Generate **>3 candidates per Bloom's level** (12-15+ total)
2. Evaluate against MCQ best practices rubric
3. Select **best 3 per level** based on difficulty and discrimination
4. Verify key position distribution across all options

## Distractor Quality Standard

Every wrong answer must:
1. Be based on a documented misconception or plausible error
2. Attract roughly equal share of uninformed guesses (~20% for 5 options, ~25% for 4 options)
3. Be similar in length and structure to correct answer
4. Require subject knowledge to eliminate

**If any distractor would attract <10% of guesses, the question fails.**

## Example: Weak vs Strong Question

### ❌ TOO EASY (Reject)
> "What should you do during a heart attack?"  
> A. Ignore it  B. Call 911  C. Exercise  D. Sleep  E. Eat

**Problem:** Anyone knows to call 911. Distractors are absurd.

### ✅ CHALLENGING (Accept)
> "Maria, 67, develops jaw pain, nausea, and lightheadedness but no chest pain. Her husband thinks it's indigestion. Based on heart attack warning signs, the BEST response is:"  
> A. Give antacids and wait 30 minutes  
> B. Drive her to urgent care for evaluation  
> C. Call 911 immediately ✓  
> D. Have her rest and monitor symptoms  
> E. Wait to see if chest pain develops

**Why it works:** Requires knowing (1) women have different symptoms, (2) absence of chest pain doesn't rule out heart attack, (3) 911 > driving. All distractors are reasonable-sounding actions.

## Quality Gates

- [ ] All 9 questions score ≥7.0/10
- [ ] Average score ≥7.5/10
- [ ] No question answerable by common sense
- [ ] All distractors rated "Good" or better
- [ ] No two questions test the same fact
- [ ] Correct answers distributed across all option positions
- [ ] **In-scope verification:** Every question (stem + all options) is answerable solely from the reference material; no external knowledge required beyond what's in the source

## Consistency Check Requirements

The final consistency check must verify:

### Grammar and Language Standards
- [ ] **American English spelling** (e.g., "color" not "colour", "analyze" not "analyse")
- [ ] **American English punctuation** (e.g., periods and commas inside quotation marks)
- [ ] No typos or misspellings
- [ ] Consistent capitalization throughout
- [ ] Proper subject-verb agreement
- [ ] Clear, unambiguous sentence structure

### Format Consistency
- [ ] All questions follow the same structural pattern
- [ ] Option labeling is consistent (A, B, C, D, E)
- [ ] Punctuation at end of options is consistent (all with periods or all without)

## Task Instructions Pattern

When generating task instructions, follow these exact patterns:

### Task Description (General) — ~50 words
**Pattern:** "[One-sentence introduction of the topic]. In this task, you will need to learn as much as you can about [topic]."

### Task Instruction for Explainer (Concise)
**Pattern:** "You will need to provide clear and accurate information about [topic] to your partner later. Your partner may come with specific questions with details, including but not exhaustive of [general themes from the quiz, mention top 3]."

### Task Instruction for Learner (Concise)
**Pattern:** "Your partner will have gained knowledge about [topic], and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: [specific problem types from the quiz, mention top 3]."

### Example Task Instructions

**Topic:** The Mongol Empire

**General:**
> The Mongol Empire, founded by Genghis Khan in the 13th century, became the largest contiguous land empire in history, dramatically altering interactions between Europe and Asia. In this task, you will need to learn as much as you can about the Mongol Empire, including its conquests, administration across different regions, and lasting historical impacts.

**Explainer:**
> You will need to provide clear and accurate information about the Mongol Empire to your partner later. Your partner may come with specific questions with details, including but not exhaustive of Mongol military tactics and conquests, the impact of Mongol rule on Russia and China, and the spread of the Black Death through trade routes, so pay attention to these details.

**Learner:**
> Your partner will have gained knowledge about the Mongol Empire, and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: 1. How Mongol rule affected different conquered regions in distinct ways, as well as which regions the Mongols failed to conquer despite multiple attempts. 2. The broader consequences of increased trade and connectivity during the Mongol period, in the context of the Black Death. 3. Strategic military considerations for dynasties dealing with Mongol threats after the empire's decline.

## Output Format

See [output-template.md](references/output-template.md) for complete Empirica template.

## Schemas

See [schemas.md](references/schemas.md) for JSON structures.
