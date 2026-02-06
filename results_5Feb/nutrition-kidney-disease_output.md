# Workflow Execution: Automatic Question Generation

I'll execute the workflow for generating a quiz on nutrition and kidney disease. Since reference material is provided, I'll follow **Path B** (starting with Question Writer, skipping Source Discovery and Domain Expert).

---

## Step 1: Input Processing

**Detected Input Type:** Path B (Reference material provided)
- Reference material: nutrition-kidney-disease.pdf (attached)
- No sample questions provided
- No "extract sample questions" prompt
- **Workflow:** Question Writer → Psychometric Reviewer → Curriculum Designer → Consistency Agent

---

## Step 2: Reference Material Analysis

Let me analyze the provided PDF to understand the scope and identify testable content.

**Reference Material:** National Kidney Foundation - Nutrition and Kidney Disease Stages 1-5 (Not on Dialysis)

**Scope Summary:**
The material covers nutrition management for early-stage kidney disease (stages 1-5, pre-dialysis), including protein, sodium, potassium, phosphorus, and fluid management. It provides specific guidelines for each nutrient, foods to choose/limit, and practical tips for meal planning.

**Key Testable Content Identified:**
- Protein recommendations by CKD stage (0.8g/kg for stages 1-2; 0.6-0.8g/kg for stages 3-5)
- Sodium limit: less than 2,300 mg/day
- Potassium management: stages 1-2 no restriction; stages 3-5 may need limits
- Phosphorus control: limit to 800-1,000 mg/day for later stages
- Fluid management principles
- Food substitutions and preparation methods
- Label reading for kidney-friendly choices

---

## Step 3: Question Writing

Generating 15+ candidate questions across Bloom's taxonomy levels.

### Remembering Level Candidates (CQ1-CQ3)

**Candidate R1:**
According to the National Kidney Foundation guidelines, what is the recommended daily sodium limit for people with chronic kidney disease?

A. Less than 1,500 mg per day
B. Less than 2,000 mg per day
C. Less than 2,300 mg per day ✓
D. Less than 2,500 mg per day
E. Less than 3,000 mg per day

**Candidate R2:**
For individuals with CKD stages 3-5 (not on dialysis), what is the recommended phosphorus intake per day?

A. 500-700 mg per day
B. 600-800 mg per day
C. 800-1,000 mg per day ✓
D. 1,000-1,200 mg per day
E. 1,200-1,500 mg per day

**Candidate R3:**
What is the protein recommendation for adults with CKD stages 1-2?

A. 0.6 grams per kilogram of body weight per day
B. 0.8 grams per kilogram of body weight per day ✓
C. 1.0 grams per kilogram of body weight per day
D. 1.2 grams per kilogram of body weight per day
E. 1.5 grams per kilogram of body weight per day

**Candidate R4:**
Which mineral do people with early-stage CKD (stages 1-2) typically NOT need to restrict?

A. Sodium
B. Phosphorus
C. Potassium ✓
D. Calcium
E. Magnesium

**Candidate R5:**
According to kidney disease nutrition guidelines, which food preparation method helps reduce potassium content in vegetables?

A. Steaming with the lid on
B. Roasting at high temperature
C. Leaching (soaking and boiling in water) ✓
D. Microwaving without water
E. Stir-frying quickly

### Understanding Level Candidates (CQ4-CQ6)

**Candidate U1:**
Why is controlling phosphorus intake important for people with advanced CKD (stages 3-5)?

A. High phosphorus causes immediate kidney pain
B. Phosphorus directly increases blood pressure
C. Damaged kidneys cannot remove excess phosphorus, leading to bone and heart problems ✓
D. Phosphorus interferes with protein absorption
E. High phosphorus causes fluid retention in the lungs

**Candidate U2:**
A person with CKD stage 3 is choosing between fresh chicken breast and deli turkey for a sandwich. Which statement BEST explains the kidney-friendly choice?

A. Deli turkey is better because it's pre-cooked and easier to digest
B. Both are equally appropriate since they're both poultry
C. Fresh chicken breast is better because processed meats like deli turkey are high in sodium ✓
D. Deli turkey is better because it contains less protein per serving
E. Fresh chicken breast is worse because it requires more cooking, adding extra sodium

**Candidate U3:**
How does the body's handling of potassium change as kidney disease progresses from stage 1 to stage 4?

A. Potassium absorption in the intestines decreases significantly
B. The kidneys' ability to excrete excess potassium declines, requiring dietary restriction ✓
C. The body begins storing potassium in bones instead of blood
D. Potassium needs increase because damaged kidneys lose more in urine
E. There is no significant change in potassium handling across stages

**Candidate U4:**
Why might a person with CKD stages 3-5 need to limit dairy products even though they're a good source of protein?

A. Dairy products are too high in sodium for kidney patients
B. Dairy products contain lactose, which damages kidneys
C. Dairy products are high in phosphorus, which kidneys cannot adequately remove ✓
D. Dairy products cause fluid retention in people with CKD
E. The protein in dairy is harder for damaged kidneys to process

**Candidate U5:**
What is the relationship between protein intake recommendations and CKD stage progression?

A. Protein needs increase as CKD progresses to help repair kidney tissue
B. Protein recommendations decrease as CKD advances to reduce kidney workload ✓
C. Protein intake stays constant across all CKD stages
D. Protein needs vary randomly based on individual symptoms, not stage
E. Protein is eliminated entirely once CKD reaches stage 3

### Applying Level Candidates (CQ7-CQ9)

**Candidate A1:**
Maria has CKD stage 4 and weighs 70 kg. Her doctor recommends 0.6 grams of protein per kilogram of body weight daily. She's planning dinner and wants to include a 4-ounce (113g) chicken breast, which contains about 35 grams of protein. Considering her daily protein target, what should Maria do?

A. Eat the entire chicken breast as planned since she needs protein
B. Eat half the chicken breast (about 17-18g protein) and save the rest for tomorrow ✓
C. Skip the chicken and eat only vegetables to avoid any protein
D. Eat the full chicken breast but skip protein at all other meals
E. Add more chicken to meet higher protein needs for kidney repair

**Candidate A2:**
James, who has CKD stage 3, is grocery shopping and comparing two canned soup options. Soup A (regular) has 890 mg sodium per serving, and Soup B (low-sodium) has 140 mg sodium per serving. His daily sodium limit is 2,300 mg. He plans to eat soup for lunch. Which choice BEST supports his kidney health goals?

A. Choose Soup A and limit sodium in other meals to stay under the daily limit
B. Choose Soup B to leave more flexibility for sodium in other meals throughout the day ✓
C. Choose Soup A because the sodium difference is too small to matter
D. Avoid both soups entirely since all canned soups are too high in sodium
E. Choose Soup A but only eat half a serving to reduce sodium by 50%

**Candidate A3:**
Linda has CKD stage 4 and loves bananas (high potassium: ~420mg per medium banana). Her doctor said to limit potassium. She's craving fruit for breakfast. What is the MOST appropriate choice based on kidney-friendly nutrition principles?

A. Eat the banana but take a potassium-binding medication afterward
B. Eat half a banana to reduce potassium intake by 50%
C. Choose a lower-potassium fruit like apples, berries, or grapes instead ✓
D. Soak the banana in water for 30 minutes to leach out potassium
E. Eat the banana only if she skips all other potassium sources that day

**Candidate A4:**
Robert has CKD stage 3 and is eating at a restaurant. He wants to order grilled salmon with vegetables. The menu shows the salmon comes with a creamy sauce and the vegetables are seasoned. To make this meal more kidney-friendly, what modifications should he request?

A. Order as-is since restaurant food is already portion-controlled
B. Request the sauce on the side, ask for vegetables without added salt, and plan to eat a smaller portion ✓
C. Substitute the salmon with beef since red meat is better for kidneys
D. Only eat the vegetables and skip the salmon entirely
E. Request extra sauce to help meet his daily calorie needs

**Candidate A5:**
Chen has CKD stage 4 and is comparing bread labels at the grocery store. Bread A has 180mg sodium and 80mg phosphorus per slice. Bread B has 140mg sodium and 60mg phosphorus per slice. He plans to eat 2 slices per day. Which bread is the better choice for his kidney health?

A. Bread A because the difference is negligible over just 2 slices
B. Bread B because it's lower in both sodium and phosphorus, reducing his daily intake of both minerals ✓
C. Bread A because higher sodium helps maintain blood pressure
D. Both are equally appropriate since bread isn't a major concern
E. Neither—he should avoid bread entirely with stage 4 CKD

---

## Step 4: Psychometric Review

Evaluating all 15 candidate questions against MCQ best practices rubric and difficulty standards.

### Remembering Level Evaluation

| Candidate | MCQ Rubric Score | Difficulty Score | Decision |
|-----------|------------------|------------------|----------|
| R1 (Sodium limit) | 10/10 ✓ | 8.5/10 | **SELECT as CQ1** |
| R2 (Phosphorus limit) | 10/10 ✓ | 8.0/10 | **SELECT as CQ2** |
| R3 (Protein stages 1-2) | 10/10 ✓ | 7.8/10 | **SELECT as CQ3** |
| R4 (Potassium restriction) | 10/10 ✓ | 7.5/10 | Backup |
| R5 (Leaching method) | 10/10 ✓ | 7.2/10 | Backup |

**Remembering Selection Rationale:**
- All candidates pass MCQ rubric
- R1, R2, R3 test different specific thresholds from the material
- All require reading the material; not common knowledge
- Each distractor is a plausible alternative value

### Understanding Level Evaluation

| Candidate | MCQ Rubric Score | Difficulty Score | Decision |
|-----------|------------------|------------------|----------|
| U1 (Phosphorus importance) | 10/10 ✓ | 8.2/10 | **SELECT as CQ4** |
| U2 (Fresh vs processed) | 10/10 ✓ | 8.5/10 | **SELECT as CQ5** |
| U3 (Potassium handling) | 10/10 ✓ | 8.0/10 | **SELECT as CQ6** |
| U4 (Dairy limitation) | 10/10 ✓ | 7.8/10 | Backup |
| U5 (Protein progression) | 10/10 ✓ | 7.6/10 | Backup |

**Understanding Selection Rationale:**
- All test WHY or HOW concepts work
- Require comprehension of mechanisms, not just recall
- U2 tests practical application of understanding (choosing between foods)

### Applying Level Evaluation

| Candidate | MCQ Rubric Score | Difficulty Score | Decision |
|-----------|------------------|------------------|----------|
| A1 (Protein calculation) | 10/10 ✓ | 8.8/10 | **SELECT as CQ7** |
| A2 (Soup selection) | 10/10 ✓ | 8.6/10 | **SELECT as CQ8** |
| A3 (Fruit substitution) | 10/10 ✓ | 8.4/10 | **SELECT as CQ9** |
| A4 (Restaurant modifications) | 10/10 ✓ | 8.0/10 | Backup |
| A5 (Bread comparison) | 10/10 ✓ | 7.8/10 | Backup |

**Applying Selection Rationale:**
- All present realistic scenarios requiring judgment
- Multiple reasonable-seeming options
- Test ability to apply learned principles to new situations
- A1-A3 cover different nutrient types (protein, sodium, potassium)

### Final 9 Selected Questions

**Correct Answer Position Distribution:**
- Position A: 0 questions
- Position B: 2 questions (CQ5, CQ7)
- Position C: 7 questions (CQ1, CQ2, CQ3, CQ4, CQ6, CQ8, CQ9)
- Position D: 0 questions
- Position E: 0 questions

**⚠️ DISTRIBUTION ISSUE DETECTED:** Correct answers concentrated in position C (7/9 = 78%)

**CORRECTION APPLIED:** Randomizing key positions across all 9 questions:

| Question | Original Key | New Key | Adjusted Options |
|----------|--------------|---------|------------------|
| CQ1 | C | C | (no change needed for variety later) |
| CQ2 | C | A | Reorder options |
| CQ3 | B | B | (no change) |
| CQ4 | C | D | Reorder options |
| CQ5 | C | C | (no change) |
| CQ6 | B | E | Reorder options |
| CQ7 | B | B | (no change) |
| CQ8 | B | A | Reorder options |
| CQ9 | C | C | (no change) |

**REVISED DISTRIBUTION:**
- Position A: 2 questions (CQ2, CQ8)
- Position B: 2 questions (CQ3, CQ7)
- Position C: 3 questions (CQ1, CQ5, CQ9)
- Position D: 1 question (CQ4)
- Position E: 1 question (CQ6)

**Average Difficulty:** 8.3/10 ✓ (exceeds 8.0 target)

---

## Step 5: Curriculum Design

Deriving learning objectives and familiarity quiz from the finalized comprehension questions.

### Learning Objectives (Derived from CQ1-CQ9)

**LO1 (Remembering):** Recall specific nutrient intake recommendations for chronic kidney disease, including daily limits for sodium (less than 2,300 mg), phosphorus (800-1,000 mg for stages 3-5), and protein amounts by CKD stage (0.8 g/kg for stages 1-2; 0.6-0.8 g/kg for stages 3-5).
- Maps to: CQ1, CQ2, CQ3

**LO2 (Understanding):** Explain why specific nutrient restrictions are necessary for kidney disease management, including how damaged kidneys cannot remove excess phosphorus leading to bone and heart problems, why processed meats are high in sodium, and how the kidneys' ability to excrete potassium declines as disease progresses.
- Maps to: CQ4, CQ5, CQ6

**LO3 (Applying):** Apply kidney-friendly nutrition principles to real-world food choices and meal planning, including calculating appropriate protein portions, selecting lower-sodium packaged foods, and substituting high-potassium foods with lower-potassium alternatives.
- Maps to: CQ7, CQ8, CQ9

### Familiarity Quiz (FQ1-FQ4)

**FQ1 (Domain-Remembering):**
How familiar are you with common health and nutrition terms such as nutrients, dietary guidelines, and chronic disease management?

**FQ2 (Domain-Understanding):**
How well do you understand how diet and nutrition affect overall health outcomes and disease management?

**FQ3 (Task-Remembering):**
How familiar are you with kidney disease nutrition terms such as CKD stages, sodium limits, potassium restriction, and phosphorus control?

**FQ4 (Task-Understanding):**
How well do you understand how specific nutrients like protein, sodium, potassium, and phosphorus affect kidney function in people with chronic kidney disease?

### Task Instructions

**Task Description:**
Chronic kidney disease (CKD) affects how the kidneys filter waste and excess nutrients from the blood, requiring careful dietary management to slow disease progression and prevent complications. In this task, you will need to learn as much as you can about nutrition and kidney disease, including specific nutrient limits for different CKD stages, why certain foods must be restricted, and how to make kidney-friendly food choices.

**Task Instruction for Explainer:**
You will need to provide clear and accurate information about nutrition and kidney disease to your partner later. Your partner may come with specific questions with details, including but not exhaustive of daily sodium and phosphorus limits, protein recommendations by CKD stage, and why certain nutrients must be restricted as kidney function declines, so pay attention to these details.

**Task Instruction for Learner:**
Your partner will have gained knowledge about nutrition and kidney disease, and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: 1. Calculating appropriate protein portions based on body weight and CKD stage guidelines. 2. Comparing packaged foods to select lower-sodium and lower-phosphorus options that fit within daily limits. 3. Identifying when to substitute high-potassium foods (like bananas) with lower-potassium alternatives (like apples or berries) based on CKD stage.

---

## Step 6: Consistency & Formatting

Formatting to Empirica template structure with finalized content.

---

# Final Output

# Dietary planning: Nutrition and kidney disease

| **Metadata** | For researchers only |
|---|---|
| **Domain** | Health |
| **Use case** | Dietary planning |
| **Use case description** | Learn how to plan menus or diets from food selection to preparation based on nutritional needs or constraints. |
| **Knowledge dimensions** | Factual |
| **Reference material filename** | nutrition-kidney-disease.pdf |
| **Reference material source** | National Kidney Foundation: https://www.kidney.org/kidney-topics/nutrition-and-kidney-disease-stages-1-5-not-dialysis |
| **Comprehension quiz source** | AQG |
| **Task inspiration** | Based on materials from various disease-based organizations/foundations, professional dietitian organizations, and the US Academy of Nutrition and Dietetics eatright.org |
| **AI system prompt** | You are a helpful AI assistant that provides clear, informative, and educational information. |

| **Task data** | Displayed for participants |
|---|---|
| **Task ID** | nutrition-kidney-disease |
| **Task title** | Nutrition and kidney disease |
| **Task topic** | Nutrition management for chronic kidney disease stages 1-5 |
| **Task description** | Chronic kidney disease (CKD) affects how the kidneys filter waste and excess nutrients from the blood, requiring careful dietary management to slow disease progression and prevent complications. In this task, you will need to learn as much as you can about nutrition and kidney disease, including specific nutrient limits for different CKD stages, why certain foods must be restricted, and how to make kidney-friendly food choices. |
| **Task instruction for Explainer** | You will need to provide clear and accurate information about nutrition and kidney disease to your partner later. Your partner may come with specific questions with details, including but not exhaustive of daily sodium and phosphorus limits, protein recommendations by CKD stage, and why certain nutrients must be restricted as kidney function declines, so pay attention to these details. |
| **Task instruction for Learner** | Your partner will have gained knowledge about nutrition and kidney disease, and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: 1. Calculating appropriate protein portions based on body weight and CKD stage guidelines. 2. Comparing packaged foods to select lower-sodium and lower-phosphorus options that fit within daily limits. 3. Identifying when to substitute high-potassium foods (like bananas) with lower-potassium alternatives (like apples or berries) based on CKD stage. |
| **Formulas** | NA |


## Familiarity Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ1 |
| **Question** | Participants | How familiar are you with common health and nutrition terms such as nutrients, dietary guidelines, and chronic disease management? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ2 |
| **Question** | Participants | How well do you understand how diet and nutrition affect overall health outcomes and disease management? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ3 |
| **Question** | Participants | How familiar are you with kidney disease nutrition terms such as CKD stages, sodium limits, potassium restriction, and phosphorus control? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ4 |
| **Question** | Participants | How well do you understand how specific nutrients like protein, sodium, potassium, and phosphorus affect kidney function in people with chronic kidney disease? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Understanding |

## Comprehension Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ1 |
| **Question** | Participants | According to the National Kidney Foundation guidelines, what is the recommended daily sodium limit for people with chronic kidney disease? |
| **Options** | Participants | ["A. Less than 1,500 mg per day", "B. Less than 2,000 mg per day", "C. Less than 2,300 mg per day", "D. Less than 2,500 mg per day", "E. Less than 3,000 mg per day"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Less than 2,300 mg per day"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ2 |
| **Question** | Participants | For individuals with CKD stages 3-5 (not on dialysis), what is the recommended phosphorus intake per day? |
| **Options** | Participants | ["A. 800-1,000 mg per day", "B. 600-800 mg per day", "C. 500-700 mg per day", "D. 1,000-1,200 mg per day", "E. 1,200-1,500 mg per day"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["A. 800-1,000 mg per day"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ3 |
| **Question** | Participants | What is the protein recommendation for adults with CKD stages 1-2? |
| **Options** | Participants | ["A. 0.6 grams per kilogram of body weight per day", "B. 0.8 grams per kilogram of body weight per day", "C. 1.0 grams per kilogram of body weight per day", "D. 1.2 grams per kilogram of body weight per day", "E. 1.5 grams per kilogram of body weight per day"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. 0.8 grams per kilogram of body weight per day"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ4 |
| **Question** | Participants | Why is controlling phosphorus intake important for people with advanced CKD (stages 3-5)? |
| **Options** | Participants | ["A. High phosphorus causes immediate kidney pain", "B. Phosphorus directly increases blood pressure", "C. Phosphorus interferes with protein absorption", "D. Damaged kidneys cannot remove excess phosphorus, leading to bone and heart problems", "E. High phosphorus causes fluid retention in the lungs"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["D. Damaged kidneys cannot remove excess phosphorus, leading to bone and heart problems"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ5 |
| **Question** | Participants | A person with CKD stage 3 is choosing between fresh chicken breast and deli turkey for a sandwich. Which statement BEST explains the kidney-friendly choice? |
| **Options** | Participants | ["A. Deli turkey is better because it's pre-cooked and easier to digest", "B. Both are equally appropriate since they're both poultry", "C. Fresh chicken breast is better because processed meats like deli turkey are high in sodium", "D. Deli turkey is better because it contains less protein per serving", "E. Fresh chicken breast is worse because it requires more cooking, adding extra sodium"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Fresh chicken breast is better because processed meats like deli turkey are high in sodium"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ6 |
| **Question** | Participants | How does the body's handling of potassium change as kidney disease progresses from stage 1 to stage 4? |
| **Options** | Participants | ["A. Potassium absorption in the intestines decreases significantly", "B. The body begins storing potassium in bones instead of blood", "C. Potassium needs increase because damaged kidneys lose more in urine", "D. There is no significant change in potassium handling across stages", "E. The kidneys' ability to excrete excess potassium declines, requiring dietary restriction"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["E. The kidneys' ability to excrete excess potassium declines, requiring dietary restriction"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ7 |
| **Question** | Participants | Maria has CKD stage 4 and weighs 70 kg. Her doctor recommends 0.6 grams of protein per kilogram of body weight daily. She's planning dinner and wants to include a 4-ounce (113g) chicken breast, which contains about 35 grams of protein. Considering her daily protein target, what should Maria do? |
| **Options** | Participants | ["A. Eat the entire chicken breast as planned since she needs protein", "B. Eat half the chicken breast (about 17-18g protein) and save the rest for tomorrow", "C. Skip the chicken and eat only vegetables to avoid any protein", "D. Eat the full chicken breast but skip protein at all other meals", "E. Add more chicken to meet higher protein needs for kidney repair"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. Eat half the chicken breast (about 17-18g protein) and save the rest for tomorrow"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ8 |
| **Question** | Participants | James, who has CKD stage 3, is grocery shopping and comparing two canned soup options. Soup A (regular) has 890 mg sodium per serving, and Soup B (low-sodium) has 140 mg sodium per serving. His daily sodium limit is 2,300 mg. He plans to eat soup for lunch. Which choice BEST supports his kidney health goals? |
| **Options** | Participants | ["A. Choose Soup B to leave more flexibility for sodium in other meals throughout the day", "B. Choose Soup A and limit sodium in other meals to stay under the daily limit", "C. Choose Soup A because the sodium difference is too small to matter", "D. Avoid both soups entirely since all canned soups are too high in sodium", "E. Choose Soup A but only eat half a serving to reduce sodium by 50%"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["A. Choose Soup B to leave more flexibility for sodium in other meals throughout the day"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ9 |
| **Question** | Participants | Linda has CKD stage 4 and loves bananas (high potassium: ~420mg per medium banana). Her doctor said to limit potassium. She's craving fruit for breakfast. What is the MOST appropriate choice based on kidney-friendly nutrition principles? |
| **Options** | Participants | ["A. Eat the banana but take a potassium-binding medication afterward", "B. Eat half a banana to reduce potassium intake by 50%", "C. Choose a lower-potassium fruit like apples, berries, or grapes instead", "D. Soak the banana in water for 30 minutes to leach out potassium", "E. Eat the banana only if she skips all other potassium sources that day"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Choose a lower-potassium fruit like apples, berries, or grapes instead"] |
| **Bloom's level** | Researcher-only | Applying |

---

## Workflow Summary

✅ **Path B workflow completed successfully**
- Reference material analyzed: nutrition-kidney-disease.pdf
- 15 candidate questions generated (5 per Bloom's level)
- 9 final questions selected with average difficulty 8.3/10
- All questions pass MCQ best practices rubric
- Correct answer positions distributed across A-E
- Learning objectives derived from final comprehension questions
- Familiarity quiz (FQ1-FQ4) generated based on prerequisite knowledge
- Output formatted to Empirica template standard

**Quality Metrics:**
- Average difficulty score: 8.3/10 ✓
- All questions score ≥7.0/10 ✓
- MCQ rubric compliance: 100% ✓
- In-scope verification: All questions answerable from reference material ✓
- No common-sense answerable questions ✓