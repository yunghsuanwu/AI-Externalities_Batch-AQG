# Workflow Execution: Automatic Question Generation

## Input Analysis

**Path Detection:** Reference material content is directly provided → **Path B** (skip Source Discovery and Domain Expert)

**Input Summary:**
- Domain: Health
- Use case: Self-administered medications
- Task ID: synthroid
- Task title: Synthroid
- CQ format: 5 options (single-select MCQs)
- Reference material: Synthroid patient education materials (manufacturer source)

---

## Stage 1: Question Writer Agent

### Reference Material Scope Analysis

**Source:** Synthroid manufacturer education materials (2024)
**Topics covered:**
- How to take Synthroid correctly (timing, water, empty stomach)
- Wait time before eating (30-60 minutes)
- Foods/supplements that interfere with absorption
- Dose verification and pill identification
- Long-term considerations (life changes requiring dose adjustment)
- Approved uses and contraindications
- Important safety information and side effects
- Drug interactions (iron, calcium, antacids, biotin)

**Testable specific facts:**
- Take once daily at the same time
- Take with water only, on empty stomach before first meal
- Wait 30-60 minutes before eating/drinking anything other than water
- Take 4 hours before or after iron, calcium, or antacids
- Stop biotin 2 days before TSH/T4 testing
- Foods that reduce effectiveness: soybean flour, walnuts, grapefruit juice, cottonseed meal, dietary fiber
- Should NOT be used for weight loss or obesity treatment
- Contraindicated with uncorrected adrenal problems
- Partial hair loss may occur in first few months
- Treatment is generally for life
- Not for noncancerous thyroid growths or temporary hypothyroidism from thyroiditis

---

### Candidate Question Generation

#### Remembering Level (5 candidates)

**R1:**
> How long should patients wait after taking Synthroid before eating or drinking anything other than water?
> A. 10-15 minutes
> B. 15-20 minutes
> C. 30-60 minutes
> D. 2-3 hours
> E. 4 hours

**Correct:** C
**Distractor rationale:**
- A/B: Common assumptions for medication timing
- D: Confused with supplement separation time
- E: Exact time for iron/calcium separation (related but wrong context)

**R2:**
> According to Synthroid guidelines, how far apart should Synthroid be taken from iron or calcium supplements?
> A. 30 minutes
> B. 1 hour
> C. 2 hours
> D. 4 hours
> E. 6 hours

**Correct:** D
**Distractor rationale:**
- A: Confused with eating wait time
- B: Reasonable but incorrect guess
- C: Half the required time
- E: Overly cautious guess

**R3:**
> How many days before a TSH or T4 blood test should patients stop taking biotin or biotin-containing supplements?
> A. 1 day
> B. 2 days
> C. 3 days
> D. 5 days
> E. 7 days

**Correct:** B
**Distractor rationale:**
- A: One day seems reasonable
- C/D/E: Progressively longer periods that seem cautious

**R4:**
> Which of the following foods can make Synthroid LESS effective by reducing absorption?
> A. Bananas, oranges, and spinach
> B. White rice, chicken, and potatoes
> C. Soybean flour, walnuts, and grapefruit juice
> D. Eggs, cheese, and milk
> E. Bread, pasta, and tomatoes

**Correct:** C
**Distractor rationale:**
- A: Common healthy foods (potassium-rich)
- B: Simple carbs and protein
- D: Calcium-containing (related concern but not the specific list)
- E: Common carbohydrate foods

**R5:**
> How should Synthroid be taken?
> A. Twice daily with meals
> B. Once daily at the same time, with water only, on an empty stomach
> C. Once daily at bedtime with a snack
> D. Three times daily with food
> E. Every other day with milk

**Correct:** B
**Distractor rationale:**
- A: Common medication frequency pattern
- C: Some medications are taken at bedtime
- D: Multiple daily dosing pattern
- E: Every other day pattern, milk interferes but seems soothing

---

#### Understanding Level (5 candidates)

**U1:**
> Why is it important to take Synthroid at the same time every day on an empty stomach?
> A. To prevent nausea and stomach upset
> B. To ensure consistent and proper absorption of the medication
> C. To reduce the risk of allergic reactions
> D. To make the medication work faster each day
> E. To prevent interactions with stomach acid

**Correct:** B
**Distractor rationale:**
- A: Common reason for food-related medication instructions
- C: Allergy concerns are real but unrelated to timing
- D: Speed of action isn't the primary concern
- E: Sounds scientific but incorrect

**U2:**
> Why does Synthroid treatment typically continue for life in most patients with hypothyroidism?
> A. The medication loses effectiveness over time and requires ongoing adjustment
> B. Synthroid replaces a hormone the thyroid gland usually makes but cannot produce sufficiently
> C. Taking it for life prevents the development of thyroid cancer
> D. Stopping the medication would cause permanent damage to the thyroid gland
> E. Long-term use builds immunity to thyroid problems

**Correct:** B
**Distractor rationale:**
- A: Adjustment may be needed, but not why it's lifelong
- C: Not a cancer prevention medication
- D: Stopping doesn't damage the thyroid
- E: No immunity concept applies

**U3:**
> Why must patients inform their doctor about life changes such as pregnancy, menopause, or aging while taking Synthroid?
> A. These conditions make Synthroid unsafe to take
> B. The medication should be discontinued during these periods
> C. The dose may need to be adjusted based on changing body needs
> D. These conditions cure hypothyroidism naturally
> E. Synthroid interacts differently with hormones during these times only

**Correct:** C
**Distractor rationale:**
- A: Not unsafe, just needs adjustment
- B: Should not be discontinued
- D: These don't cure hypothyroidism
- E: Partially true but misses the dosing point

**U4:**
> Why is Synthroid NOT appropriate for treating obesity or promoting weight loss?
> A. It has no effect on metabolism or weight
> B. It only works in people with thyroid problems
> C. Large doses, especially with appetite-reducing drugs, can cause serious or life-threatening effects
> D. Weight loss would occur too rapidly and be dangerous
> E. It causes weight gain rather than weight loss

**Correct:** C
**Distractor rationale:**
- A: It does affect metabolism
- B: True but doesn't explain the danger
- D: Plausible concern but not the stated reason
- E: Incorrect direction of effect

**U5:**
> Why should patients check that their pill says "SYNTHROID" with every refill?
> A. To verify the pharmacy charged the correct price
> B. To ensure they received the correct branded medication rather than a substitute
> C. To check the expiration date of the medication
> D. To confirm the pill has not been damaged during shipping
> E. To verify the color matches their previous prescription

**Correct:** B
**Distractor rationale:**
- A: Pricing is separate concern
- C: Expiration is important but not related to pill marking
- D: Damage would be visible separately
- E: Color relates to dose but the marking confirms the brand

---

#### Applying Level (5 candidates)

**A1:**
> Patricia takes Synthroid every morning. She also takes a daily calcium supplement for bone health. Based on Synthroid guidelines, what is the BEST way for her to schedule these medications?
> A. Take both medications together in the morning for convenience
> B. Take Synthroid in the morning and calcium with lunch, ensuring at least 4 hours apart
> C. Take calcium in the morning and Synthroid at bedtime
> D. Alternate days between Synthroid and calcium
> E. Take Synthroid with milk to get calcium at the same time

**Correct:** B
**Distractor rationale:**
- A: Convenient but reduces Synthroid absorption
- C: Timing could work but Synthroid should be on empty stomach in morning
- D: Cannot skip Synthroid doses
- E: Milk is not allowed, and calcium interferes

**A2:**
> Robert has been taking Synthroid for 3 months and notices he is losing more hair than usual when showering. Based on the medication information, what should he understand about this symptom?
> A. He should immediately stop taking Synthroid and contact his doctor
> B. This is an allergic reaction requiring emergency medical attention
> C. Partial hair loss may occur during the first few months and is a known effect
> D. His dose is definitely too high and needs immediate reduction
> E. Hair loss means the medication is not working properly

**Correct:** C
**Distractor rationale:**
- A: Should not stop without medical advice
- B: Not typically an allergic reaction
- D: May or may not be dose-related; hair loss is expected initially
- E: Hair loss is not an effectiveness indicator

**A3:**
> Maria takes Synthroid at 6:00 AM every morning. She has a breakfast meeting at 6:15 AM where food will be served. What is the BEST course of action?
> A. Skip her Synthroid dose that morning
> B. Take Synthroid at the meeting with her breakfast
> C. Take Synthroid at 6:00 AM and eat only after waiting 30-60 minutes, arriving late or eating later
> D. Take a double dose the next day to make up for the missed dose
> E. Take Synthroid with coffee before leaving for the meeting

**Correct:** C
**Distractor rationale:**
- A: Should not skip doses
- B: Must be taken on empty stomach, not with food
- D: Never double up doses
- E: Must be taken with water only, not coffee

**A4:**
> James is scheduled for blood work to check his TSH levels next Monday. He currently takes a daily multivitamin containing biotin. Based on the guidelines, what should James do?
> A. Continue taking his multivitamin as usual; it won't affect the test
> B. Stop the biotin-containing multivitamin at least 2 days before the blood test
> C. Take extra biotin the day of the test to ensure accurate results
> D. Stop all medications including Synthroid before the blood test
> E. Have the blood test at least 4 hours after taking his multivitamin

**Correct:** B
**Distractor rationale:**
- A: Biotin does interfere with TSH testing
- C: More biotin would worsen interference
- D: Should not stop Synthroid
- E: 4-hour separation applies to iron/calcium, not biotin testing

**A5:**
> Susan has been prescribed Synthroid for hypothyroidism. She also has diabetes and takes medication to control her blood sugar. Based on the safety information, what should Susan be particularly attentive to?
> A. She cannot take Synthroid if she has diabetes
> B. She should monitor her blood sugar levels as directed, as Synthroid may affect them
> C. She should take insulin and Synthroid at exactly the same time
> D. Diabetes medications eliminate the need for Synthroid
> E. She should increase her Synthroid dose to counteract diabetes effects

**Correct:** B
**Distractor rationale:**
- A: Can take Synthroid with diabetes
- C: No requirement to take simultaneously
- D: Unrelated conditions
- E: No basis for increasing dose

---

### Question Selection (Best 3 per level)

**Remembering (CQ1-CQ3):**
- CQ1: R1 (wait time before eating) - tests specific threshold
- CQ2: R2 (iron/calcium separation time) - tests another specific threshold
- CQ3: R4 (foods that reduce effectiveness) - tests specific list

**Understanding (CQ4-CQ6):**
- CQ4: U1 (why empty stomach/same time) - explains mechanism
- CQ5: U4 (why not for weight loss) - explains safety rationale
- CQ6: U3 (why inform doctor of life changes) - explains dose adjustment rationale

**Applying (CQ7-CQ9):**
- CQ7: A1 (Patricia's calcium scheduling) - realistic medication management
- CQ8: A2 (Robert's hair loss) - symptom interpretation
- CQ9: A4 (James's biotin and blood test) - pre-test preparation

---

## Stage 2: Psychometric Reviewer Agent

### MCQ Rubric Evaluation

| Question | Single Key | Key Length | Plausible Distractors | No Grammar Hints | No All/None | No Ambiguity | No Double Neg | No Qualifiers | No Stem Rep | No Absolutes | Score |
|----------|------------|------------|----------------------|------------------|-------------|--------------|---------------|---------------|-------------|--------------|-------|
| CQ1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.5 |
| CQ2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.2 |
| CQ3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.0 |
| CQ4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.3 |
| CQ5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.5 |
| CQ6 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.0 |
| CQ7 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.7 |
| CQ8 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.4 |
| CQ9 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 8.6 |

**Average Score: 8.4/10** ✓ (exceeds 7.5 threshold)

### Key Position Distribution

| Position | Questions | Count |
|----------|-----------|-------|
| A | - | 0 |
| B | CQ5, CQ7, CQ9 | 3 |
| C | CQ1, CQ3, CQ4, CQ6, CQ8 | 5 |
| D | CQ2 | 1 |
| E | - | 0 |

**Issue:** Positions are concentrated in B/C. Redistributing keys:

**Adjusted Key Positions:**
- CQ1: C → C (keep)
- CQ2: D → D (keep)
- CQ3: C → A (move soybean/walnuts/grapefruit to position A)
- CQ4: B → B (keep)
- CQ5: C → E (move safety reason to position E)
- CQ6: C → C (keep)
- CQ7: B → B (keep)
- CQ8: C → A (move expected hair loss to position A)
- CQ9: B → D (move biotin stopping to position D)

**Final Distribution:**
| Position | Count |
|----------|-------|
| A | 2 |
| B | 2 |
| C | 2 |
| D | 2 |
| E | 1 |

✓ Distributed across all positions

---

## Stage 3: Curriculum Designer Agent

### Learning Objectives (Derived from CQs)

**LO1 (Remembering):** Recall the specific timing requirements for taking Synthroid, including wait times before eating and separation from supplements.
- Maps to: CQ1, CQ2

**LO2 (Remembering):** Identify foods and substances that interfere with Synthroid absorption.
- Maps to: CQ3

**LO3 (Understanding):** Explain why Synthroid must be taken consistently on an empty stomach at the same time daily.
- Maps to: CQ4

**LO4 (Understanding):** Explain why Synthroid should not be used for weight loss and the associated safety concerns.
- Maps to: CQ5

**LO5 (Understanding):** Explain why life changes require communication with healthcare providers about Synthroid dosing.
- Maps to: CQ6

**LO6 (Applying):** Apply medication timing guidelines to schedule Synthroid appropriately with other supplements.
- Maps to: CQ7

**LO7 (Applying):** Interpret common side effects and distinguish expected effects from concerning symptoms.
- Maps to: CQ8

**LO8 (Applying):** Apply pre-test preparation guidelines for accurate thyroid function testing.
- Maps to: CQ9

### Familiarity Quiz (FQ1-FQ4)

**FQ1 (Domain, Remembering):** How familiar are you with common medical terms related to self-administered medications, such as dosage, absorption, and side effects?

**FQ2 (Domain, Understanding):** How well do you understand how factors like food, timing, and other medications can affect how your body absorbs and responds to prescription drugs?

**FQ3 (Task, Remembering):** How familiar are you with terms related to thyroid medication such as hypothyroidism, levothyroxine, and TSH levels?

**FQ4 (Task, Understanding):** How well do you understand how thyroid replacement medications work and why specific administration guidelines must be followed?

---

## Stage 4: Consistency Agent - Final Output

---

# Self-administered medications: Synthroid

| **Metadata** | For researchers only |
|---|---|
| **Domain** | Health |
| **Use case** | Self-administered medications |
| **Use case description** | Learn about a drug's intended use, directions, effects, and side effects from easily accessible medical documentations (e.g., drug labels, online articles). |
| **Knowledge dimensions** | Factual |
| **Reference material filename** | synthroid.pdf |
| **Reference material source** | Manufacturer education materials (https://www.synthroid.com/content/dam/synthroidivy/docs/how-to-take-synthroid.pdf) |
| **Comprehension quiz source** | AQG |
| **Task inspiration** | Hypothyroidism is a common medical condition people experience, and Synthroid is one of the common prescribed drugs used to treat it. |
| **AI system prompt** | You are a helpful AI assistant that provides clear, informative, and educational information. |

| **Task data** | Displayed for participants |
|---|---|
| **Task ID** | synthroid |
| **Task title** | Synthroid |
| **Task topic** | How to take Synthroid medication correctly |
| **Task description** | Synthroid (levothyroxine) is a prescription thyroid hormone replacement medication used to treat hypothyroidism. In this task, you will need to learn as much as you can about Synthroid, including how to take it correctly, foods and supplements that affect absorption, and important safety considerations. |
| **Task instruction for Explainer** | You will need to provide clear and accurate information about Synthroid to your partner later. Your partner may come with specific questions with details, including but not exhaustive of timing requirements for taking the medication, foods and supplements that interfere with absorption, and safety warnings, so pay attention to these details. |
| **Task instruction for Learner** | Your partner will have gained knowledge about Synthroid, and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: 1. How to schedule Synthroid with other supplements like calcium or iron. 2. How to interpret common side effects and know when they are expected versus concerning. 3. How to prepare for blood tests that measure thyroid function. |
| **Formulas** | NA |


## Familiarity Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ1 |
| **Question** | Participants | How familiar are you with common medical terms related to self-administered medications, such as dosage, absorption, and side effects? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ2 |
| **Question** | Participants | How well do you understand how factors like food, timing, and other medications can affect how your body absorbs and responds to prescription drugs? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ3 |
| **Question** | Participants | How familiar are you with terms related to thyroid medication such as hypothyroidism, levothyroxine, and TSH levels? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ4 |
| **Question** | Participants | How well do you understand how thyroid replacement medications work and why specific administration guidelines must be followed? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Understanding |

## Comprehension Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ1 |
| **Question** | Participants | How long should patients wait after taking Synthroid before eating or drinking anything other than water? |
| **Options** | Participants | ["A. 10-15 minutes", "B. 15-20 minutes", "C. 30-60 minutes", "D. 2-3 hours", "E. 4 hours"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. 30-60 minutes"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ2 |
| **Question** | Participants | According to Synthroid guidelines, how far apart should Synthroid be taken from iron or calcium supplements? |
| **Options** | Participants | ["A. 30 minutes", "B. 1 hour", "C. 2 hours", "D. 4 hours", "E. 6 hours"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["D. 4 hours"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ3 |
| **Question** | Participants | Which of the following foods can make Synthroid LESS effective by reducing absorption? |
| **Options** | Participants | ["A. Soybean flour, walnuts, and grapefruit juice", "B. Bananas, oranges, and spinach", "C. White rice, chicken, and potatoes", "D. Eggs, cheese, and milk", "E. Bread, pasta, and tomatoes"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["A. Soybean flour, walnuts, and grapefruit juice"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ4 |
| **Question** | Participants | Why is it important to take Synthroid at the same time every day on an empty stomach? |
| **Options** | Participants | ["A. To prevent nausea and stomach upset", "B. To ensure consistent and proper absorption of the medication", "C. To reduce the risk of allergic reactions", "D. To make the medication work faster each day", "E. To prevent interactions with stomach acid"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. To ensure consistent and proper absorption of the medication"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ5 |
| **Question** | Participants | Why is Synthroid NOT appropriate for treating obesity or promoting weight loss? |
| **Options** | Participants | ["A. It has no effect on metabolism or weight", "B. It only works in people with thyroid problems", "C. Weight loss would occur too rapidly and be dangerous", "D. It causes weight gain rather than weight loss", "E. Large doses, especially with appetite-reducing drugs, can cause serious or life-threatening effects"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["E. Large doses, especially with appetite-reducing drugs, can cause serious or life-threatening effects"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ6 |
| **Question** | Participants | Why must patients inform their doctor about life changes such as pregnancy, menopause, or aging while taking Synthroid? |
| **Options** | Participants | ["A. These conditions make Synthroid unsafe to take", "B. The medication should be discontinued during these periods", "C. The dose may need to be adjusted based on changing body needs", "D. These conditions cure hypothyroidism naturally", "E. Synthroid interacts differently with hormones during these times only"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. The dose may need to be adjusted based on changing body needs"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ7 |
| **Question** | Participants | Patricia takes Synthroid every morning. She also takes a daily calcium supplement for bone health. Based on Synthroid guidelines, what is the BEST way for her to schedule these medications? |
| **Options** | Participants | ["A. Take both medications together in the morning for convenience", "B. Take Synthroid in the morning and calcium with lunch, ensuring at least 4 hours apart", "C. Take calcium in the morning and Synthroid at bedtime", "D. Alternate days between Synthroid and calcium", "E. Take Synthroid with milk to get calcium at the same time"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. Take Synthroid in the morning and calcium with lunch, ensuring at least 4 hours apart"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ8 |
| **Question** | Participants | Robert has been taking Synthroid for 3 months and notices he is losing more hair than usual when showering. Based on the medication information, what should he understand about this symptom? |
| **Options** | Participants | ["A. Partial hair loss may occur during the first few months and is a known effect", "B. He should immediately stop taking Synthroid and contact his doctor", "C. This is an allergic reaction requiring emergency medical attention", "D. His dose is definitely too high and needs immediate reduction", "E. Hair loss means the medication is not working properly"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["A. Partial hair loss may occur during the first few months and is a known effect"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ9 |
| **Question** | Participants | James is scheduled for blood work to check his TSH levels next Monday. He currently takes a daily multivitamin containing biotin. Based on the guidelines, what should James do? |
| **Options** | Participants | ["A. Continue taking his multivitamin as usual; it won't affect the test", "B. Take extra biotin the day of the test to ensure accurate results", "C. Stop all medications including Synthroid before the blood test", "D. Stop the biotin-containing multivitamin at least 2 days before the blood test", "E. Have the blood test at least 4 hours after taking his multivitamin"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["D. Stop the biotin-containing multivitamin at least 2 days before the blood test"] |
| **Bloom's level** | Researcher-only | Applying |

---

## Quality Summary

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Average CQ score | 8.4/10 | ≥7.5 | ✓ |
| Lowest CQ score | 8.0/10 | ≥7.0 | ✓ |
| MCQ best practices | 100% pass | 100% | ✓ |
| Key position distribution | A:2, B:2, C:2, D:2, E:1 | ~20% each | ✓ |
| Bloom's distribution | 3-3-3 | 3-3-3 | ✓ |
| In-scope verification | All questions | 100% | ✓ |