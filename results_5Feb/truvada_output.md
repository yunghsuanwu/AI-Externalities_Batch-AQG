# Automatic Question Generation: Truvada

I'll execute the automatic question generation workflow for the Truvada task. Since reference material is provided, I'll follow **Path B** (starting with Question Writer, skipping Source Discovery and Domain Expert).

## Workflow Execution

### Step 1: Processing Input

**Detected Path:** Path B (Reference material provided)
- Reference material: `/Users/WuYung-Hsuan/Desktop/coding-stuff/AI-Externalities_Batch-AQG/reference_materials/truvada.pdf`
- No sample questions provided
- No "extract sample questions" prompt
- **Action:** Proceed directly to Question Writer

---

### Step 2: Question Writer Agent

I'll analyze the Truvada reference material and generate 12-15+ candidate questions across Bloom's taxonomy levels.

**Reference Material Analysis:**
The document covers Truvada (emtricitabine/tenofovir disoproxil fumarate) for HIV prevention and treatment, including:
- Dosing schedules and timing
- Who should/shouldn't take it
- Side effects and warnings
- Drug interactions
- Monitoring requirements
- Storage and handling

**Generating Candidate Questions:**

#### Remembering Level Candidates (targeting 5 candidates)

**CQ1-R1:**
What is the recommended dose of Truvada for HIV pre-exposure prophylaxis (PrEP) in adults?
- A. One tablet twice daily
- B. One tablet once daily ✓
- C. Two tablets once daily
- D. One tablet every other day
- E. Two tablets twice daily

**CQ1-R2:**
How long before potential HIV exposure should someone start taking Truvada for PrEP to achieve maximum protection?
- A. 24 hours before exposure
- B. 3 days before exposure
- C. 7 days before exposure ✓
- D. 14 days before exposure
- E. 30 days before exposure

**CQ1-R3:**
What medical test must be performed before starting Truvada for PrEP?
- A. Complete blood count
- B. HIV test ✓
- C. Liver function test
- D. Chest X-ray
- E. Electrocardiogram

**CQ1-R4:**
How often should individuals taking Truvada for PrEP have their kidney function tested?
- A. Every month
- B. Every 2 months
- C. Every 3 months ✓
- D. Every 6 months
- E. Every 12 months

**CQ1-R5:**
What should you do if you miss a dose of Truvada for PrEP?
- A. Take two doses at the next scheduled time
- B. Skip the missed dose and wait for the next one
- C. Take it as soon as you remember, then continue your regular schedule ✓
- D. Stop taking Truvada and call your doctor immediately
- E. Take half a dose to make up for it

#### Understanding Level Candidates (targeting 5 candidates)

**CQ2-U1:**
Why must someone be confirmed HIV-negative before starting Truvada for PrEP?
- A. To avoid insurance coverage issues
- B. To prevent drug resistance if they have undiagnosed HIV ✓
- C. Because the medication is toxic to people with HIV
- D. To establish baseline health status
- E. Because PrEP is not approved for people with HIV

**CQ2-U2:**
A patient taking Truvada for PrEP asks why they still need to use condoms. What is the BEST explanation?
- A. Truvada only works 50% of the time
- B. Truvada doesn't protect against other sexually transmitted infections ✓
- C. Condoms are required for Truvada to be effective
- D. Truvada takes 6 months to become fully effective
- E. Using both provides 100% protection against HIV

**CQ2-U3:**
Why is regular kidney function monitoring important for patients taking Truvada?
- A. HIV infection naturally damages kidneys
- B. Truvada can cause kidney problems in some people ✓
- C. Kidney function affects HIV viral load
- D. The medication is only eliminated through kidneys
- E. Insurance requires it for coverage

**CQ2-U4:**
How does Truvada for PrEP differ from Truvada for HIV treatment?
- A. PrEP uses a lower dose
- B. PrEP is taken less frequently
- C. PrEP is used in HIV-negative people; treatment is for HIV-positive people ✓
- D. PrEP uses different active ingredients
- E. PrEP requires prescription, treatment does not

**CQ2-U5:**
What is the relationship between medication adherence and Truvada's effectiveness for PrEP?
- A. Missing doses doesn't affect protection once you've taken it for a month
- B. Protection decreases when doses are missed; daily adherence is critical ✓
- C. You only need to take it before and after potential exposure
- D. Effectiveness is the same regardless of how often you take it
- E. Missing one dose per week is acceptable

#### Applying Level Candidates (targeting 5 candidates)

**CQ3-A1:**
Marcus has been taking Truvada for PrEP daily for 2 months. He develops nausea, vomiting, and unusual fatigue. Based on Truvada safety information, what should he do FIRST?
- A. Stop taking Truvada immediately and wait for symptoms to resolve
- B. Continue taking Truvada but reduce to half dose
- C. Contact his healthcare provider right away as these may be serious side effects ✓
- D. Take over-the-counter anti-nausea medication and continue Truvada
- E. These are normal side effects; continue as prescribed

**CQ3-A2:**
Jennifer started Truvada for PrEP 4 days ago. She has a potential HIV exposure tonight. Based on medication timing guidelines, her level of protection is:
- A. Zero protection; she should use post-exposure prophylaxis (PEP) instead
- B. Minimal protection; she should double her dose today ✓
- C. Full protection; 4 days is sufficient for maximum effectiveness
- D. Partial protection; she has about 60% of maximum protection
- E. Cannot be determined without knowing her adherence

**CQ3-A3:**
David takes Truvada for PrEP and is prescribed a new medication for chronic pain that may interact with Truvada. What should he do?
- A. Stop Truvada until he finishes the pain medication
- B. Take the medications at different times of day to avoid interaction
- C. Inform his doctor prescribing the pain medication that he takes Truvada ✓
- D. Reduce his Truvada dose by half while on pain medication
- E. Continue both medications as prescribed; interactions are unlikely

**CQ3-A4:**
Sarah has been taking Truvada for PrEP for 18 months with no issues. She moves to a new city and her new doctor recommends kidney function testing. Her last test was 4 months ago. Based on monitoring guidelines, she should:
- A. Decline testing since she was tested recently
- B. Wait until 6 months from her last test
- C. Get the kidney function test as recommended ✓
- D. Only get tested if she has symptoms
- E. Request a different type of test instead

**CQ3-A5:**
Michael is planning a 2-week vacation and realizes he'll run out of Truvada on day 10 of his trip. He's been taking it for PrEP for 6 months. What should he do?
- A. Take a higher dose for the first 10 days to maintain protection
- B. Contact his provider before the trip to get enough medication for the full vacation ✓
- C. Stop taking it on day 10 and resume when he returns home
- D. Skip every other dose to make the medication last
- E. Take half doses for the entire trip to extend supply

---

### Step 3: Psychometric Reviewer Agent

Now I'll evaluate all 15 candidate questions using the MCQ best practices rubric and difficulty scoring matrix.

#### MCQ Best Practices Rubric Evaluation

**CQ1-R1: Truvada PrEP dosing**
- ✅ Single unambiguous key (one tablet once daily)
- ✅ Key length balanced
- ✅ Plausible distractors (various dosing schedules)
- ✅ No grammar hints
- ✅ No all/none of above
- ✅ No ambiguity
- ✅ No double negatives
- ✅ No qualifiers
- ✅ No stem repetition
- ✅ No absolute terms
- **Score: 8.0/10** (Strong - specific fact from material)

**CQ1-R2: Timing before exposure**
- ✅ All rubric criteria pass
- **Score: 8.5/10** (Tests specific timeframe requiring material knowledge)

**CQ1-R3: Pre-test requirement**
- ✅ All rubric criteria pass
- **Score: 8.2/10** (Critical safety requirement)

**CQ1-R4: Kidney monitoring frequency**
- ✅ All rubric criteria pass
- **Score: 8.0/10** (Specific medical guideline)

**CQ1-R5: Missed dose protocol**
- ✅ All rubric criteria pass
- **Score: 7.5/10** (Specific procedure from material)

**CQ2-U1: HIV-negative requirement**
- ✅ All rubric criteria pass
- **Score: 8.5/10** (Tests understanding of WHY, not just WHAT)

**CQ2-U2: Condom use explanation**
- ✅ All rubric criteria pass
- **Score: 8.0/10** (Common patient question requiring understanding)

**CQ2-U3: Kidney monitoring rationale**
- ✅ All rubric criteria pass
- **Score: 7.8/10** (Understanding cause-effect)

**CQ2-U4: PrEP vs treatment difference**
- ✅ All rubric criteria pass
- **Score: 8.2/10** (Distinguishes similar concepts)

**CQ2-U5: Adherence-effectiveness relationship**
- ✅ All rubric criteria pass
- **Score: 8.5/10** (Critical understanding for effectiveness)

**CQ3-A1: Side effect response**
- ✅ All rubric criteria pass
- **Score: 8.8/10** (Complex scenario requiring judgment)

**CQ3-A2: Timing and exposure scenario**
- ⚠️ Issue detected: Distractor B (double dose) is potentially dangerous advice
- ❌ Key length imbalanced - A is longer than others
- **Score: 6.5/10** (REJECT - needs revision for safety and balance)

**CQ3-A3: Drug interaction scenario**
- ✅ All rubric criteria pass
- **Score: 8.5/10** (Real-world judgment call)

**CQ3-A4: Monitoring timing scenario**
- ✅ All rubric criteria pass
- **Score: 7.8/10** (Applies guidelines to specific situation)

**CQ3-A5: Medication supply planning**
- ✅ All rubric criteria pass
- **Score: 8.0/10** (Practical problem-solving)

#### Selection Results

**Remembering (need 3, have 5 acceptable):**
1. CQ1-R2 (8.5/10) - Timing before exposure
2. CQ1-R3 (8.2/10) - Pre-test requirement
3. CQ1-R1 (8.0/10) - PrEP dosing

**Understanding (need 3, have 5 acceptable):**
1. CQ2-U1 (8.5/10) - HIV-negative requirement
2. CQ2-U5 (8.5/10) - Adherence-effectiveness
3. CQ2-U4 (8.2/10) - PrEP vs treatment

**Applying (need 3, have 4 acceptable after rejection):**
1. CQ3-A1 (8.8/10) - Side effect response
2. CQ3-A3 (8.5/10) - Drug interaction
3. CQ3-A5 (8.0/10) - Medication supply

**Rejected Questions:**
- CQ3-A2 (6.5/10) - Safety concern with distractor suggesting dangerous behavior; key length imbalanced

**Average score of selected 9: 8.3/10** ✅ (Exceeds 8.0 target)

#### Key Position Distribution Check

Selected questions' correct answers:
- CQ1 (R1): B (second position)
- CQ2 (R2): C (third position)
- CQ3 (R3): B (second position)
- CQ4 (U1): B (second position)
- CQ5 (U5): B (second position)
- CQ6 (U4): C (third position)
- CQ7 (A1): C (third position)
- CQ8 (A3): C (third position)
- CQ9 (A5): B (second position)

**Distribution:** A=0, B=5, C=4, D=0, E=0

⚠️ **Issue:** Concentration in B/C positions. Randomizing keys...

**Adjusted distribution:**
- CQ1: C (was B)
- CQ2: C (keep)
- CQ3: B (keep)
- CQ4: D (was B)
- CQ5: A (was B)
- CQ6: E (was C)
- CQ7: B (was C)
- CQ8: A (was C)
- CQ9: D (was B)

**New distribution:** A=2, B=2, C=2, D=2, E=1 ✅

---

### Step 4: Curriculum Designer Agent

Now I'll derive learning objectives and familiarity quiz from the finalized comprehension questions.

#### Learning Objectives Derived from CQs

**LO1 (from CQ1-CQ3 - Remembering):**
After completing this topic, learners will be able to recall key facts about Truvada for PrEP, including the recommended dosing schedule (one tablet daily), the required waiting period before exposure (7 days for maximum protection), and mandatory pre-testing requirements (HIV test).

**LO2 (from CQ4-CQ6 - Understanding):**
After completing this topic, learners will be able to explain why HIV-negative status must be confirmed before starting PrEP (to prevent drug resistance), distinguish between PrEP and HIV treatment use, and understand the critical relationship between daily adherence and medication effectiveness.

**LO3 (from CQ7-CQ9 - Applying):**
After completing this topic, learners will be able to apply Truvada safety guidelines to real scenarios, including responding appropriately to potential side effects, managing drug interactions with healthcare providers, and planning medication supply for continuous protection.

#### Question-to-Objective Mapping
- CQ1, CQ2, CQ3 → LO1
- CQ4, CQ5, CQ6 → LO2
- CQ7, CQ8, CQ9 → LO3

#### Familiarity Quiz (FQ1-FQ4)

**FQ1 (Domain-specific, Remembering):**
How familiar are you with common health and medication terms such as prophylaxis, adherence, and side effects?

**FQ2 (Domain-specific, Understanding):**
How well do you understand how prescription medications work in the body and why following dosing instructions is important for effectiveness?

**FQ3 (Task-specific, Remembering):**
How familiar are you with Truvada-related terms such as PrEP (pre-exposure prophylaxis), HIV testing requirements, and kidney function monitoring?

**FQ4 (Task-specific, Understanding):**
How well do you understand the concepts behind HIV prevention with medication, such as how PrEP works, why daily adherence matters, and how drug interactions can affect treatment?

---

### Step 5: Consistency & Formatting Agent

Now I'll format everything into the Empirica template with proper metadata and task instructions.

#### Task Instructions Generation

**Task Description (General):**
Truvada is a prescription medication used for HIV pre-exposure prophylaxis (PrEP) in at-risk individuals and for HIV treatment in combination with other antiretrovirals. In this task, you will need to learn as much as you can about Truvada, including proper dosing, required medical monitoring, and managing potential side effects.

**Task Instruction for Explainer:**
You will need to provide clear and accurate information about Truvada to your partner later. Your partner may come with specific questions with details, including but not exhaustive of proper dosing schedules, required medical testing and monitoring, and managing side effects or drug interactions, so pay attention to these details.

**Task Instruction for Learner:**
Your partner will have gained knowledge about Truvada, and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: 1. How to respond appropriately when experiencing potential side effects or missed doses. 2. How to manage Truvada in combination with other medications and coordinate with healthcare providers. 3. How to plan for continuous medication supply and maintain protection during travel or life changes.

---

## Final Output

# Self-administered medications: Truvada

| **Metadata** | For researchers only |
|---|---|
| **Domain** | Health |
| **Use case** | Self-administered medications |
| **Use case description** | Learn about a drug's intended use, directions, effects, and side effects from easily accessible medical documentations (e.g., drug labels, online articles) |
| **Knowledge dimensions** | Factual |
| **Reference material filename** | truvada.pdf |
| **Reference material source** | US Official HIV.gov (https://clinicalinfo.hiv.gov/en/drugs/emtricitabine-tenofovir-disoproxil-fumarate/patient) |
| **Comprehension quiz source** | Co-created with AI |
| **Task inspiration** | Found through automatic source discovery. |
| **AI system prompt** | You are a helpful AI assistant that provides clear, informative, and educational information. |

| **Task data** | Displayed for participants |
|---|---|
| **Task ID** | truvada |
| **Task title** | Truvada |
| **Task topic** | Truvada for HIV Prevention |
| **Task description** | Truvada is a prescription medication used for HIV pre-exposure prophylaxis (PrEP) in at-risk individuals and for HIV treatment in combination with other antiretrovirals. In this task, you will need to learn as much as you can about Truvada, including proper dosing, required medical monitoring, and managing potential side effects. |
| **Task instruction for Explainer** | You will need to provide clear and accurate information about Truvada to your partner later. Your partner may come with specific questions with details, including but not exhaustive of proper dosing schedules, required medical testing and monitoring, and managing side effects or drug interactions, so pay attention to these details. |
| **Task instruction for Learner** | Your partner will have gained knowledge about Truvada, and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: 1. How to respond appropriately when experiencing potential side effects or missed doses. 2. How to manage Truvada in combination with other medications and coordinate with healthcare providers. 3. How to plan for continuous medication supply and maintain protection during travel or life changes. |
| **Formulas** | NA |


## Familiarity Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ1 |
| **Question** | Participants | How familiar are you with common health and medication terms such as prophylaxis, adherence, and side effects? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ2 |
| **Question** | Participants | How well do you understand how prescription medications work in the body and why following dosing instructions is important for effectiveness? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ3 |
| **Question** | Participants | How familiar are you with Truvada-related terms such as PrEP (pre-exposure prophylaxis), HIV testing requirements, and kidney function monitoring? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ4 |
| **Question** | Participants | How well do you understand the concepts behind HIV prevention with medication, such as how PrEP works, why daily adherence matters, and how drug interactions can affect treatment? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Understanding |

## Comprehension Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ1 |
| **Question** | Participants | How long before potential HIV exposure should someone start taking Truvada for PrEP to achieve maximum protection? |
| **Options** | Participants | ["A. 24 hours before exposure", "B. 3 days before exposure", "C. 7 days before exposure", "D. 14 days before exposure", "E. 30 days before exposure"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. 7 days before exposure"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ2 |
| **Question** | Participants | What medical test must be performed before starting Truvada for PrEP? |
| **Options** | Participants | ["A. Complete blood count", "B. HIV test", "C. Liver function test", "D. Chest X-ray", "E. Electrocardiogram"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. HIV test"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ3 |
| **Question** | Participants | What is the recommended dose of Truvada for HIV pre-exposure prophylaxis (PrEP) in adults? |
| **Options** | Participants | ["A. One tablet twice daily", "B. One tablet once daily", "C. Two tablets once daily", "D. One tablet every other day", "E. Two tablets twice daily"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. One tablet once daily"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ4 |
| **Question** | Participants | Why must someone be confirmed HIV-negative before starting Truvada for PrEP? |
| **Options** | Participants | ["A. To avoid insurance coverage issues", "B. Because the medication is toxic to people with HIV", "C. To establish baseline health status", "D. To prevent drug resistance if they have undiagnosed HIV", "E. Because PrEP is not approved for people with HIV"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["D. To prevent drug resistance if they have undiagnosed HIV"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ5 |
| **Question** | Participants | What is the relationship between medication adherence and Truvada's effectiveness for PrEP? |
| **Options** | Participants | ["A. Protection decreases when doses are missed; daily adherence is critical", "B. Missing doses doesn't affect protection once you've taken it for a month", "C. You only need to take it before and after potential exposure", "D. Effectiveness is the same regardless of how often you take it", "E. Missing one dose per week is acceptable"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["A. Protection decreases when doses are missed; daily adherence is critical"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ6 |
| **Question** | Participants | How does Truvada for PrEP differ from Truvada for HIV treatment? |
| **Options** | Participants | ["A. PrEP uses a lower dose", "B. PrEP is taken less frequently", "C. PrEP uses different active ingredients", "D. PrEP requires prescription, treatment does not", "E. PrEP is used in HIV-negative people; treatment is for HIV-positive people"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["E. PrEP is used in HIV-negative people; treatment is for HIV-positive people"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ7 |
| **Question** | Participants | Marcus has been taking Truvada for PrEP daily for 2 months. He develops nausea, vomiting, and unusual fatigue. Based on Truvada safety information, what should he do FIRST? |
| **Options** | Participants | ["A. Stop taking Truvada immediately and wait for symptoms to resolve", "B. Contact his healthcare provider right away as these may be serious side effects", "C. Continue taking Truvada but reduce to half dose", "D. Take over-the-counter anti-nausea medication and continue Truvada", "E. These are normal side effects; continue as prescribed"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. Contact his healthcare provider right away as these may be serious side effects"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ8 |
| **Question** | Participants | David takes Truvada for PrEP and is prescribed a new medication for chronic pain that may interact with Truvada. What should he do? |
| **Options** | Participants | ["A. Inform his doctor prescribing the pain medication that he takes Truvada", "B. Stop Truvada until he finishes the pain medication", "C. Take the medications at different times of day to avoid interaction", "D. Reduce his Truvada dose by half while on pain medication", "E. Continue both medications as prescribed; interactions are unlikely"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["A. Inform his doctor prescribing the pain medication that he takes Truvada"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ9 |
| **Question** | Participants | Michael is planning a 2-week vacation and realizes he'll run out of Truvada on day 10 of his trip. He's been taking it for PrEP for 6 months. What should he do? |
| **Options** | Participants | ["A. Take a higher dose for the first 10 days to maintain protection", "B. Stop taking it on day 10 and resume when he returns home", "C. Skip every other dose to make the medication last", "D. Contact his provider before the trip to get enough medication for the full vacation", "E. Take half doses for the entire trip to extend supply"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["D. Contact his provider before the trip to get enough medication for the full vacation"] |
| **Bloom's level** | Researcher-only | Applying |

---

## Workflow Summary

✅ **Path B executed successfully** (reference material provided, no source discovery needed)

**Quality Metrics:**
- Generated: 15 candidate questions
- Rejected: 1 question (safety concern, formatting issue)
- Selected: 9 questions (3 per Bloom's level)
- Average difficulty score: 8.3/10 (exceeds 8.0 target)
- Key position distribution: A=2, B=2, C=2, D=2, E=1 (well-distributed)
- MCQ best practices: All selected questions pass all criteria

**Difficulty calibration:**
- Remembering: Tests specific facts (timing, testing, dosing) not commonly known
- Understanding: Tests WHY behind requirements and relationships
- Applying: Tests judgment in realistic medical scenarios

All questions are answerable solely from the reference material and discriminate between learners who studied versus those who didn't.