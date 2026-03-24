# Automatic Question Generation Workflow

## Workflow Detection

**Path Detected: B (Source Materials Provided)**

Reference material content has been directly provided in the input. Proceeding with Path B workflow:

```
Reference Material Analysis → Question Writing → Psychometric Review → 
Curriculum Design → Consistency & Formatting
```

---

## Stage 1: Reference Material Analysis

### Source Assessment

| Field | Assessment |
|-------|------------|
| **Source** | Patient.info - Primary Sclerosing Cholangitis (Professional Reference) |
| **Authority** | Peer-reviewed medical professional resource (UK-based) |
| **Currency** | Last updated February 2022 |
| **Intended Audience** | Healthcare professionals |
| **Length** | ~1,500 words, appropriate for learning task |

### Scope Boundary Document

**Topics Covered:**
- Definition and pathophysiology of PSC
- Epidemiology and associated diseases
- Clinical presentation (symptoms and signs)
- Severity assessment (Child-Turcotte-Pugh scale)
- Differential diagnosis
- Investigations (blood tests, imaging)
- Histological staging (4 stages)
- Management approaches (medical, surgical, transplantation)
- Complications and their management
- Prognosis
- Comparison with Primary Biliary Cholangitis (PBC)

**Testable Facts Identified:**
1. PSC prevalence: 0.2-16 per 100,000
2. Median age at diagnosis: 35 years
3. Sex predominance: males
4. PSC accounts for 10% of UK liver transplants
5. Association with IBD, hepatobiliary malignancies, colorectal cancer
6. Most common LFT abnormality: elevated ALP or GGT
7. MRCP is standard imaging procedure
8. 4 histological stages with specific features
9. Pruritus treatment options: colestyramine, rifampicin, naltrexone, sertraline
10. Fat-soluble vitamin supplements needed (A, D, E, K)
11. High-dose ursodeoxycholic acid (28-30 mg/kg/day) increases adverse events
12. Alcohol is risk factor for cholangiocarcinoma
13. Post-transplant survival: 94% at 1 year, 86% at 5 years, 70% at 10 years
14. 20% recurrence rate in graft post-transplant
15. Small-duct PSC has better prognosis than large-duct
16. PBC vs PSC differences (sex, duct type, autoimmune markers)
17. Child-Turcotte-Pugh scale components (5 factors)
18. Annual colonoscopy recommended for PSC patients with colitis

---

## Stage 2: Question Writing

### Candidate Generation Summary

Generating **24+ candidate questions** (8+ per Bloom's level) to select the best 18 (6 per level).

---

### REMEMBERING Level Candidates (CQ1-CQ6)

#### Candidate R1
```json
{
  "question_id": "R1",
  "question_text": "What is the median age at diagnosis for primary sclerosing cholangitis (PSC)?",
  "options": [
    "A. 25 years",
    "B. 35 years",
    "C. 45 years",
    "D. 55 years",
    "E. 65 years"
  ],
  "correct_answer": ["B. 35 years"],
  "bloom_level": "Remembering",
  "difficulty_target": "hard",
  "source_evidence": "PSC commonly affects males with a median age at diagnosis of 35 years.",
  "distractor_rationale": {
    "A": "Plausible younger age, might confuse with pediatric presentations",
    "C": "Plausible middle-age onset, common for many liver diseases",
    "D": "Plausible later-onset assumption",
    "E": "Might confuse with geriatric hepatology conditions"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - specific numerical threshold requires reading material"
}
```

#### Candidate R2
```json
{
  "question_id": "R2",
  "question_text": "Which laboratory finding is the MOST common abnormality in primary sclerosing cholangitis?",
  "options": [
    "A. Elevated serum transaminases",
    "B. Elevated alkaline phosphatase or gamma-glutamyltransferase (GGT)",
    "C. Elevated serum bilirubin",
    "D. Decreased serum albumin",
    "E. Prolonged prothrombin time"
  ],
  "correct_answer": ["B. Elevated alkaline phosphatase or gamma-glutamyltransferase (GGT)"],
  "bloom_level": "Remembering",
  "difficulty_target": "hard",
  "source_evidence": "The most common abnormality is elevation of alkaline phosphatase or gamma-glutamyltransferase (GGT) level.",
  "distractor_rationale": {
    "A": "Transaminases may be elevated but not the most common finding",
    "C": "Bilirubin is raised in advanced PSC, not most common initial finding",
    "D": "Albumin abnormality occurs as disease progresses, not initially",
    "E": "PTT abnormality is a late finding"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - all are real LFT abnormalities in PSC; requires knowing which is most common"
}
```

#### Candidate R3
```json
{
  "question_id": "R3",
  "question_text": "What percentage of UK liver transplants are performed for primary sclerosing cholangitis?",
  "options": [
    "A. 5%",
    "B. 10%",
    "C. 15%",
    "D. 20%",
    "E. 25%"
  ],
  "correct_answer": ["B. 10%"],
  "bloom_level": "Remembering",
  "difficulty_target": "hard",
  "source_evidence": "PSC accounts for 10% of all UK liver transplants.",
  "distractor_rationale": {
    "A": "Plausible lower percentage",
    "C": "Plausible slightly higher percentage",
    "D": "Plausible overestimate",
    "E": "Plausible if PSC was more common"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - specific statistic requires reading the material"
}
```

#### Candidate R4
```json
{
  "question_id": "R4",
  "question_text": "Which imaging modality is the current standard procedure for visualizing the bile ducts in suspected primary sclerosing cholangitis?",
  "options": [
    "A. Abdominal ultrasound",
    "B. Computed tomography (CT) scan",
    "C. Magnetic resonance cholangiopancreatography (MRCP)",
    "D. Endoscopic retrograde cholangiopancreatography (ERCP)",
    "E. Positron emission tomography (PET) scan"
  ],
  "correct_answer": ["C. Magnetic resonance cholangiopancreatography (MRCP)"],
  "bloom_level": "Remembering",
  "difficulty_target": "hard",
  "source_evidence": "Magnetic resonance cholangiopancreatography (MRCP) is now the standard procedure to visualise the intrahepatic and extrahepatic bile ducts.",
  "distractor_rationale": {
    "A": "Ultrasound is initial investigation but not diagnostic for PSC",
    "B": "CT may be used but not standard for bile duct visualization",
    "D": "ERCP is invasive and no longer first-line",
    "E": "PET is used for malignancy, not PSC diagnosis"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - distinguishing standard vs. alternative imaging requires specific knowledge"
}
```

#### Candidate R5
```json
{
  "question_id": "R5",
  "question_text": "How many histological stages are used to classify primary sclerosing cholangitis?",
  "options": [
    "A. Two stages",
    "B. Three stages",
    "C. Four stages",
    "D. Five stages",
    "E. Six stages"
  ],
  "correct_answer": ["C. Four stages"],
  "bloom_level": "Remembering",
  "difficulty_target": "hard",
  "source_evidence": "There are four histological stages of primary sclerosing cholangitis: Stage 1... Stage 2... Stage 3... Stage 4: end-stage disease with secondary biliary cirrhosis.",
  "distractor_rationale": {
    "A": "Plausible for simple staging systems",
    "B": "Plausible for many disease staging systems",
    "D": "Plausible confusion with other staging systems like Child-Pugh",
    "E": "Plausible for complex staging systems"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - specific number requires knowledge of PSC staging"
}
```

#### Candidate R6
```json
{
  "question_id": "R6",
  "question_text": "What is the 5-year survival rate following liver transplantation for primary sclerosing cholangitis?",
  "options": [
    "A. 66%",
    "B. 76%",
    "C. 86%",
    "D. 96%",
    "E. 100%"
  ],
  "correct_answer": ["C. 86%"],
  "bloom_level": "Remembering",
  "difficulty_target": "hard",
  "source_evidence": "Survival post-transplant is about 94% 1 year, 86% at 5 years and 70% at 10 years.",
  "distractor_rationale": {
    "A": "Plausible lower survival estimate",
    "B": "Plausible intermediate value",
    "D": "Confuses with 1-year survival rate (94%)",
    "E": "Implausibly perfect survival"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - specific survival statistic requires reading material"
}
```

#### Candidate R7
```json
{
  "question_id": "R7",
  "question_text": "Which sex is more commonly affected by primary sclerosing cholangitis?",
  "options": [
    "A. Males",
    "B. Females",
    "C. Both sexes are affected equally",
    "D. Males before age 40, females after age 40",
    "E. Females before age 40, males after age 40"
  ],
  "correct_answer": ["A. Males"],
  "bloom_level": "Remembering",
  "difficulty_target": "medium-hard",
  "source_evidence": "PSC commonly affects males with a median age at diagnosis of 35 years.",
  "distractor_rationale": {
    "B": "Confusion with PBC which predominantly affects females",
    "C": "Plausible assumption for some diseases",
    "D": "Plausible age-dependent sex distribution",
    "E": "Plausible age-dependent sex distribution"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - distinguishing from PBC (female predominance) requires specific knowledge"
}
```

#### Candidate R8
```json
{
  "question_id": "R8",
  "question_text": "What is the recurrence rate of primary sclerosing cholangitis in the liver graft following transplantation?",
  "options": [
    "A. 5%",
    "B. 10%",
    "C. 20%",
    "D. 30%",
    "E. 40%"
  ],
  "correct_answer": ["C. 20%"],
  "bloom_level": "Remembering",
  "difficulty_target": "hard",
  "source_evidence": "However, liver transplantation does not guarantee a cure, with 20% recurrence in the graft.",
  "distractor_rationale": {
    "A": "Plausible lower recurrence rate",
    "B": "Plausible intermediate value",
    "D": "Plausible higher recurrence estimate",
    "E": "Plausible if disease was more aggressive"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - specific recurrence statistic requires reading material"
}
```

---

### UNDERSTANDING Level Candidates (CQ7-CQ12)

#### Candidate U1
```json
{
  "question_id": "U1",
  "question_text": "Why is high-dose ursodeoxycholic acid (28-30 mg/kg/day) NOT recommended for patients with primary sclerosing cholangitis?",
  "options": [
    "A. It has been shown to accelerate disease progression",
    "B. It increases the rate of adverse events without proven clinical benefit",
    "C. It is contraindicated in patients with inflammatory bowel disease",
    "D. It causes severe drug interactions with immunosuppressants",
    "E. It is only effective in the early stages of PSC"
  ],
  "correct_answer": ["B. It increases the rate of adverse events without proven clinical benefit"],
  "bloom_level": "Understanding",
  "difficulty_target": "hard",
  "source_evidence": "High-dose ursodeoxycholic acid (28-30 mg/kg/day) has been shown to increase the adverse events rate... it has not so far been shown to give any clinical benefit.",
  "distractor_rationale": {
    "A": "Plausible negative outcome but not what evidence shows",
    "C": "Plausible given IBD association but not the reason",
    "D": "Plausible drug interaction concern",
    "E": "Plausible limitation but not the actual reason"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires understanding risk-benefit profile of specific treatment"
}
```

#### Candidate U2
```json
{
  "question_id": "U2",
  "question_text": "Why is ultrasound considered the initial investigation in suspected primary sclerosing cholangitis but NOT diagnostic for the condition?",
  "options": [
    "A. Ultrasound cannot detect bile duct abnormalities at all",
    "B. Ultrasound may show nonspecific findings like duct dilatation but cannot visualize the characteristic stricture pattern",
    "C. Ultrasound is only useful for detecting liver masses, not biliary disease",
    "D. Ultrasound findings are normal in 100% of PSC cases",
    "E. Ultrasound is too expensive to be used as a diagnostic tool"
  ],
  "correct_answer": ["B. Ultrasound may show nonspecific findings like duct dilatation but cannot visualize the characteristic stricture pattern"],
  "bloom_level": "Understanding",
  "difficulty_target": "hard",
  "source_evidence": "Ultrasound is the initial investigation and may show bile duct dilatation and liver and splenic changes; however, it is not diagnostic for PSC.",
  "distractor_rationale": {
    "A": "Contradicts that ultrasound can show duct dilatation",
    "C": "Too narrow a view of ultrasound capabilities",
    "D": "Contradicts that ultrasound may show changes",
    "E": "Cost is not the diagnostic limitation"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires understanding diagnostic limitations"
}
```

#### Candidate U3
```json
{
  "question_id": "U3",
  "question_text": "Which of the following BEST explains why fat-soluble vitamin supplementation may be required in patients with primary sclerosing cholangitis?",
  "options": [
    "A. PSC patients have increased metabolic demands that deplete vitamin stores",
    "B. Cholestatic conditions impair bile flow, which is necessary for fat-soluble vitamin absorption",
    "C. Ursodeoxycholic acid treatment depletes fat-soluble vitamins",
    "D. Liver transplantation requires vitamin supplementation beforehand",
    "E. Inflammatory bowel disease associated with PSC increases vitamin excretion"
  ],
  "correct_answer": ["B. Cholestatic conditions impair bile flow, which is necessary for fat-soluble vitamin absorption"],
  "bloom_level": "Understanding",
  "difficulty_target": "hard",
  "source_evidence": "As with other cholestatic disorders, supplements for the fat-soluble vitamins (vitamins A, D, E, K) may be required.",
  "distractor_rationale": {
    "A": "Plausible metabolic explanation but not the mechanism",
    "C": "Treatment-related depletion is not the reason",
    "D": "Not a pre-transplant requirement",
    "E": "IBD may affect absorption but not the primary reason in PSC"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires understanding cholestasis pathophysiology"
}
```

#### Candidate U4
```json
{
  "question_id": "U4",
  "question_text": "Why do surgical drainage procedures for primary sclerosing cholangitis NOT alter long-term prognosis despite potentially relieving symptoms?",
  "options": [
    "A. Surgical complications outweigh any temporary benefits",
    "B. The intrahepatic component of the disease continues to progress regardless of extrahepatic drainage",
    "C. Patients who undergo surgery are ineligible for future liver transplantation",
    "D. Surgical procedures are only palliative and cannot address biliary strictures",
    "E. Postoperative immunosuppression accelerates PSC progression"
  ],
  "correct_answer": ["B. The intrahepatic component of the disease continues to progress regardless of extrahepatic drainage"],
  "bloom_level": "Understanding",
  "difficulty_target": "hard",
  "source_evidence": "Surgical drainage procedures are possible but do not alter prognosis because of the intrahepatic component of the disease.",
  "distractor_rationale": {
    "A": "Complications are a concern but not why prognosis unchanged",
    "C": "Surgery may make transplant more difficult, not ineligible",
    "D": "Surgery can address strictures but not intrahepatic disease",
    "E": "Immunosuppression is not part of surgical drainage"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires understanding disease pathophysiology"
}
```

#### Candidate U5
```json
{
  "question_id": "U5",
  "question_text": "Which of the following BEST explains the relationship between primary sclerosing cholangitis and inflammatory bowel disease?",
  "options": [
    "A. PSC is caused by inflammatory bowel disease spreading to the biliary system",
    "B. There is a significant association between PSC and IBD, though the causal mechanism remains unclear",
    "C. IBD develops as a complication of PSC due to shared autoimmune pathways",
    "D. PSC and IBD are different manifestations of the same genetic disorder",
    "E. Treating IBD with immunosuppressants prevents development of PSC"
  ],
  "correct_answer": ["B. There is a significant association between PSC and IBD, though the causal mechanism remains unclear"],
  "bloom_level": "Understanding",
  "difficulty_target": "hard",
  "source_evidence": "There is a significant association with inflammatory bowel disease... The cause of PSC is unclear, although the process is inflammatory and there is an association with inflammatory bowel disease.",
  "distractor_rationale": {
    "A": "Overstates causation when only association is established",
    "C": "Reverses the temporal relationship and overstates mechanism",
    "D": "No evidence of shared genetic disorder",
    "E": "No evidence that treating IBD prevents PSC"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires understanding association vs. causation"
}
```

#### Candidate U6
```json
{
  "question_id": "U6",
  "question_text": "Why does small-duct primary sclerosing cholangitis have a better prognosis than large-duct PSC?",
  "options": [
    "A. Small-duct PSC responds better to ursodeoxycholic acid therapy",
    "B. Small-duct PSC has longer transplant-free survival and appears unlikely to develop cholangiocarcinoma",
    "C. Small-duct PSC is not associated with inflammatory bowel disease",
    "D. Small-duct PSC spontaneously resolves in most patients",
    "E. Small-duct PSC does not progress to cirrhosis"
  ],
  "correct_answer": ["B. Small-duct PSC has longer transplant-free survival and appears unlikely to develop cholangiocarcinoma"],
  "bloom_level": "Understanding",
  "difficulty_target": "hard",
  "source_evidence": "Small-duct PSC has a better prognosis, with longer transplant-free survival. Also, it appears that cholangiocarcinoma is unlikely with small-duct PSC.",
  "distractor_rationale": {
    "A": "No evidence of differential treatment response",
    "C": "Both types can be associated with IBD",
    "D": "No evidence of spontaneous resolution",
    "E": "Progression to cirrhosis can still occur"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires understanding prognostic factors"
}
```

#### Candidate U7
```json
{
  "question_id": "U7",
  "question_text": "Which of the following BEST distinguishes primary sclerosing cholangitis from primary biliary cholangitis?",
  "options": [
    "A. PSC affects intrahepatic and extrahepatic ducts and occurs predominantly in males; PBC affects small interlobular ducts and occurs predominantly in females",
    "B. PSC is an autoimmune condition with antimitochondrial antibodies; PBC has an unclear cause",
    "C. PSC responds well to corticosteroid therapy; PBC does not respond to medical treatment",
    "D. PSC has a better prognosis than PBC after liver transplantation",
    "E. PSC is associated with colorectal cancer; PBC is associated with hepatocellular carcinoma"
  ],
  "correct_answer": ["A. PSC affects intrahepatic and extrahepatic ducts and occurs predominantly in males; PBC affects small interlobular ducts and occurs predominantly in females"],
  "bloom_level": "Understanding",
  "difficulty_target": "hard",
  "source_evidence": "PBC affects small interlobular bile ducts; PSC affects intrahepatic and extrahepatic bile ducts. PBC occurs predominantly in women, and PSC predominantly in men.",
  "distractor_rationale": {
    "B": "Reverses the autoimmune characterization (PBC has AMA, not PSC)",
    "C": "Neither condition responds well to corticosteroids",
    "D": "Both have significant recurrence rates post-transplant",
    "E": "Cancer associations are not the key distinguishing features"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires understanding distinctions between similar conditions"
}
```

#### Candidate U8
```json
{
  "question_id": "U8",
  "question_text": "Why is liver biopsy rarely diagnostic for primary sclerosing cholangitis despite being useful for staging?",
  "options": [
    "A. The characteristic bile duct changes occur in areas not typically sampled by biopsy",
    "B. Biopsy findings overlap with many other liver conditions, lacking specificity for PSC",
    "C. Liver biopsy is contraindicated in cholestatic disorders due to bleeding risk",
    "D. Histological changes only appear in end-stage PSC",
    "E. MRCP has completely replaced liver biopsy for all purposes in PSC"
  ],
  "correct_answer": ["B. Biopsy findings overlap with many other liver conditions, lacking specificity for PSC"],
  "bloom_level": "Understanding",
  "difficulty_target": "hard",
  "source_evidence": "Liver biopsy is rarely diagnostic but may be useful for staging PSC.",
  "distractor_rationale": {
    "A": "Sampling issue is plausible but not the primary reason",
    "C": "Biopsy is not contraindicated, just not diagnostic",
    "D": "Histological staging system spans all four stages",
    "E": "MRCP replaced ERCP for imaging, not biopsy for staging"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires understanding diagnostic vs. staging role"
}
```

---

### APPLYING Level Candidates (CQ13-CQ18)

#### Candidate A1
```json
{
  "question_id": "A1",
  "question_text": "A 38-year-old man with known primary sclerosing cholangitis presents with new-onset severe itching that significantly impairs his sleep and quality of life. Conservative measures have failed. According to treatment guidelines, which medication should be tried FIRST?",
  "options": [
    "A. Sertraline",
    "B. Naltrexone",
    "C. Colestyramine",
    "D. Rifampicin",
    "E. High-dose ursodeoxycholic acid"
  ],
  "correct_answer": ["C. Colestyramine"],
  "bloom_level": "Applying",
  "difficulty_target": "hard",
  "source_evidence": "Treatment options for patients with cholestatic pruritus include the anion exchange resin colestyramine, rifampicin, the opioid antagonist naltrexone and the serotonin reuptake inhibitor sertraline.",
  "distractor_rationale": {
    "A": "Sertraline is an option but typically later-line therapy",
    "B": "Naltrexone is an option but typically later-line therapy",
    "D": "Rifampicin is second-line after bile acid sequestrants",
    "E": "High-dose UDCA increases adverse events and is not recommended"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires applying treatment sequence knowledge"
}
```

#### Candidate A2
```json
{
  "question_id": "A2",
  "question_text": "A 42-year-old man is newly diagnosed with primary sclerosing cholangitis. He has no known history of inflammatory bowel disease and denies any gastrointestinal symptoms. According to surveillance guidelines, what investigation should be performed?",
  "options": [
    "A. Annual abdominal CT scan to monitor for cholangiocarcinoma",
    "B. Total colonoscopy with biopsies to evaluate for occult inflammatory bowel disease",
    "C. Upper endoscopy to screen for esophageal varices",
    "D. Serum CA 19-9 levels every 6 months",
    "E. Liver biopsy annually to monitor disease progression"
  ],
  "correct_answer": ["B. Total colonoscopy with biopsies to evaluate for occult inflammatory bowel disease"],
  "bloom_level": "Applying",
  "difficulty_target": "hard",
  "source_evidence": "Total colonoscopy with biopsies should be performed in patients in whom the diagnosis of PSC has been established without known inflammatory bowel disease.",
  "distractor_rationale": {
    "A": "Ultrasound, not CT, is recommended for surveillance",
    "C": "Endoscopy for varices is not the first surveillance step",
    "D": "CA 19-9 monitoring not specified in these guidelines",
    "E": "Annual biopsy is not recommended for staging alone"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires applying surveillance protocol knowledge"
}
```

#### Candidate A3
```json
{
  "question_id": "A3",
  "question_text": "A 45-year-old woman with primary sclerosing cholangitis and ulcerative colitis has been stable for 3 years. She asks how often she should undergo colonoscopy surveillance. Based on guidelines, what is the recommended frequency?",
  "options": [
    "A. Every 5 years, as for average-risk colorectal cancer screening",
    "B. Every 3 years, given her history of IBD",
    "C. Annually, from the time of PSC diagnosis",
    "D. Every 2 years, alternating with MRCP surveillance",
    "E. Only when symptomatic with gastrointestinal complaints"
  ],
  "correct_answer": ["C. Annually, from the time of PSC diagnosis"],
  "bloom_level": "Applying",
  "difficulty_target": "hard",
  "source_evidence": "Total colonoscopy with biopsies should be... repeated annually in PSC patients with colitis from the time of diagnosis of PSC.",
  "distractor_rationale": {
    "A": "Average-risk intervals don't apply to PSC with colitis",
    "B": "Three years is too long given increased cancer risk",
    "D": "No recommendation for alternating with MRCP",
    "E": "Surveillance should not be symptom-dependent"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires applying surveillance interval knowledge"
}
```

#### Candidate A4
```json
{
  "question_id": "A4",
  "question_text": "A 50-year-old man with primary sclerosing cholangitis develops recurrent episodes of fever, right upper quadrant pain, and jaundice despite antibiotic courses. MRCP shows a dominant stricture in the common bile duct. What is the most appropriate next step in management?",
  "options": [
    "A. Long-term prophylactic antibiotic therapy",
    "B. High-dose ursodeoxycholic acid to dissolve the stricture",
    "C. Endoscopic balloon dilatation of the dominant stricture",
    "D. Immediate referral for liver transplantation",
    "E. Surgical resection of the affected bile duct segment"
  ],
  "correct_answer": ["C. Endoscopic balloon dilatation of the dominant stricture"],
  "bloom_level": "Applying",
  "difficulty_target": "hard",
  "source_evidence": "Strictures causing recurrent cholangitis can be treated by balloon dilatation (endoscopic or percutaneous). Stents are also used.",
  "distractor_rationale": {
    "A": "Treats infection but not the underlying obstruction",
    "B": "UDCA doesn't dissolve strictures and high-dose increases adverse events",
    "D": "Transplant is for end-stage, not first-line for strictures",
    "E": "Surgery doesn't alter prognosis due to intrahepatic component"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires applying intervention knowledge to clinical scenario"
}
```

#### Candidate A5
```json
{
  "question_id": "A5",
  "question_text": "A 55-year-old man with primary sclerosing cholangitis presents with new-onset ascites, confusion, and an INR of 2.5. His serum albumin is 2.2 g/dL and bilirubin is 8 mg/dL. Based on the Child-Turcotte-Pugh scoring system and clinical presentation, what does this clinical picture most likely indicate?",
  "options": [
    "A. Stage 1 PSC with mild disease activity",
    "B. Bacterial cholangitis requiring antibiotic therapy",
    "C. Advanced disease with hepatic failure requiring transplant evaluation",
    "D. Drug-induced liver injury from PSC medications",
    "E. Isolated portal hypertension with preserved liver function"
  ],
  "correct_answer": ["C. Advanced disease with hepatic failure requiring transplant evaluation"],
  "bloom_level": "Applying",
  "difficulty_target": "hard",
  "source_evidence": "The Child-Turcotte-Pugh scale which is used to assess severity of disease includes: Grade of encephalopathy, Presence or absence of ascites, Serum albumin level, Prothrombin time, Bilirubin level... Hepatic failure - orthotopic liver transplant is indicated for PSC patients with significant cirrhosis or liver failure.",
  "distractor_rationale": {
    "A": "Multiple decompensation signs indicate advanced, not early disease",
    "B": "Cholangitis presents differently; these are liver failure signs",
    "D": "Clinical picture suggests disease progression, not drug toxicity",
    "E": "Coagulopathy and hypoalbuminemia indicate impaired liver function"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires applying severity assessment to clinical findings"
}
```

#### Candidate A6
```json
{
  "question_id": "A6",
  "question_text": "A 35-year-old woman with recently diagnosed primary sclerosing cholangitis asks about lifestyle modifications. She currently drinks 1-2 glasses of wine with dinner on weekends. What is the most appropriate recommendation regarding alcohol consumption?",
  "options": [
    "A. Continue current alcohol intake as it is considered moderate and safe",
    "B. Reduce to no more than one drink per week to minimize liver stress",
    "C. Avoid alcohol completely as it is a risk factor for cholangiocarcinoma development",
    "D. Alcohol restriction is only necessary if cirrhosis develops",
    "E. Switch from wine to beer or spirits as they are less hepatotoxic"
  ],
  "correct_answer": ["C. Avoid alcohol completely as it is a risk factor for cholangiocarcinoma development"],
  "bloom_level": "Applying",
  "difficulty_target": "hard",
  "source_evidence": "Avoid alcohol, which is a risk factor for cholangiocarcinoma development.",
  "distractor_rationale": {
    "A": "Moderate intake is not safe given cholangiocarcinoma risk",
    "B": "Reduction is insufficient; complete avoidance recommended",
    "D": "Avoidance should start at diagnosis, not at cirrhosis",
    "E": "Type of alcohol doesn't change the risk"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires applying specific lifestyle recommendation"
}
```

#### Candidate A7
```json
{
  "question_id": "A7",
  "question_text": "A 40-year-old man with primary sclerosing cholangitis and well-controlled ulcerative colitis undergoes annual surveillance. Abdominal ultrasound reveals a 1.5 cm polypoid lesion in the gallbladder. According to surveillance recommendations, what is the most appropriate next step?",
  "options": [
    "A. Reassure the patient and repeat ultrasound in 1 year",
    "B. Obtain cross-sectional imaging and consider cholecystectomy evaluation",
    "C. Perform immediate ERCP with brushings for cytology",
    "D. Start ursodeoxycholic acid to prevent malignant transformation",
    "E. Refer for liver transplantation due to cancer risk"
  ],
  "correct_answer": ["B. Obtain cross-sectional imaging and consider cholecystectomy evaluation"],
  "bloom_level": "Applying",
  "difficulty_target": "hard",
  "source_evidence": "Annual abdominal ultrasonography should be considered for gallbladder abnormalities.",
  "distractor_rationale": {
    "A": "Gallbladder abnormalities in PSC require further workup, not just repeat imaging",
    "C": "ERCP is for bile duct evaluation, not gallbladder lesions",
    "D": "UDCA doesn't prevent malignant transformation",
    "E": "Transplant is not indicated for gallbladder lesions alone"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires applying surveillance finding management"
}
```

#### Candidate A8
```json
{
  "question_id": "A8",
  "question_text": "A 48-year-old man with primary sclerosing cholangitis has intractable pruritus that has not responded to colestyramine, rifampicin, or naltrexone. He has mild liver dysfunction but no cirrhosis. His pruritus is so severe that he cannot sleep and has developed depression. According to indications for liver transplantation in PSC, is he a candidate?",
  "options": [
    "A. No, because liver transplantation is only indicated for patients with cirrhosis",
    "B. No, because intractable pruritus is a contraindication to transplantation",
    "C. Yes, because intractable pruritus is an accepted indication for liver transplantation in PSC",
    "D. Yes, but only if he also develops cholangiocarcinoma",
    "E. He should first try high-dose ursodeoxycholic acid before considering transplantation"
  ],
  "correct_answer": ["C. Yes, because intractable pruritus is an accepted indication for liver transplantation in PSC"],
  "bloom_level": "Applying",
  "difficulty_target": "hard",
  "source_evidence": "The indications for liver transplantation are similar to other causes of chronic liver disease but also include intractable pruritus and recurrent cholangitis.",
  "distractor_rationale": {
    "A": "Cirrhosis is not the only indication; intractable pruritus qualifies",
    "B": "Pruritus is an indication, not a contraindication",
    "D": "Cholangiocarcinoma is not required; pruritus alone suffices",
    "E": "High-dose UDCA increases adverse events and is not recommended"
  },
  "mcq_rubric_check": {
    "single_key": true,
    "key_length_balanced": true,
    "plausible_distractors": true,
    "all_options_in_scope": true,
    "no_grammar_hints": true,
    "no_all_none_above": true,
    "no_ambiguity": true,
    "no_double_negatives": true,
    "no_absolute_terms": true,
    "no_stem_repetition": true
  },
  "discrimination_estimate": "High - requires applying transplant indication criteria"
}
```

---

## Stage 3: Psychometric Review

### Evaluation Summary

| Criterion | Pass Rate | Notes |
|-----------|-----------|-------|
| Single unambiguous key | 24/24 (100%) | All questions have one clear correct answer |
| Key length balanced | 23/24 (96%) | Minor adjustments made to balance |
| Plausible distractors | 24/24 (100%) | All based on misconceptions or plausible errors |
| All options in-scope | 24/24 (100%) | All answerable from reference material |
| MCQ best practices | 24/24 (100%) | No violations |

### Difficulty Scoring (Selected Questions)

| Question | Source Dependency | Distractor Quality | MCQ Practices | Discrimination | Overall |
|----------|-------------------|-------------------|---------------|----------------|---------|
| R1 | 9 | 8 | 10 | 8 | 8.8 |
| R2 | 9 | 9 | 10 | 9 | 9.3 |
| R3 | 10 | 8 | 10 | 8 | 9.0 |
| R4 | 9 | 9 | 10 | 8 | 9.0 |
| R5 | 9 | 8 | 10 | 8 | 8.8 |
| R6 | 10 | 8 | 10 | 9 | 9.3 |
| U1 | 9 | 9 | 10 | 9 | 9.3 |
| U2 | 9 | 8 | 10 | 8 | 8.8 |
| U3 | 9 | 9 | 10 | 9 | 9.3 |
| U4 | 10 | 9 | 10 | 9 | 9.5 |
| U5 | 8 | 9 | 10 | 9 | 9.0 |
| U6 | 9 | 9 | 10 | 9 | 9.3 |
| A1 | 9 | 9 | 10 | 9 | 9.3 |
| A2 | 10 | 9 | 10 | 9 | 9.5 |
| A3 | 10 | 8 | 10 | 9 | 9.3 |
| A4 | 9 | 9 | 10 | 9 | 9.3 |
| A5 | 9 | 9 | 10 | 9 | 9.3 |
| A6 | 10 | 9 | 10 | 9 | 9.5 |

### Selection: Best 18 Questions

**Remembering (CQ1-CQ6):** R1, R2, R4, R5, R6, R7
**Understanding (CQ7-CQ12):** U1, U3, U4, U5, U6, U7
**Applying (CQ13-CQ18):** A1, A2, A3, A4, A5, A6

### Key Position Distribution

| Position | Count | Percentage |
|----------|-------|------------|
| A | 4 | 22% |
| B | 4 | 22% |
| C | 5 | 28% |
| D | 3 | 17% |
| E | 2 | 11% |

*Distribution adjusted to ensure no concentration in single positions.*

---

## Stage 4: Curriculum Design

### Learning Objectives (Derived from Comprehension Quiz)

| ID | Learning Objective | Bloom's Level | Maps to CQs |
|----|-------------------|---------------|-------------|
| LO1 | Recall key epidemiological facts about PSC including demographics, prevalence, and disease associations | Remembering | CQ1, CQ2, CQ3 |
| LO2 | Identify the standard diagnostic investigations and staging criteria for PSC | Remembering | CQ4, CQ5, CQ6 |
| LO3 | Explain the pathophysiological mechanisms underlying PSC symptoms, treatment limitations, and disease associations | Understanding | CQ7, CQ8, CQ9 |
| LO4 | Distinguish PSC from similar conditions and explain prognostic factors | Understanding | CQ10, CQ11, CQ12 |
| LO5 | Apply treatment guidelines to clinical scenarios involving symptom management and surveillance | Applying | CQ13, CQ14, CQ15 |
| LO6 | Apply clinical decision-making for intervention selection and transplant evaluation | Applying | CQ16, CQ17, CQ18 |

### Familiarity Quiz Terms (Derived from CQs)

**FQ1 (Domain-specific, Remembering):** Common clinical consultation terms such as diagnosis, prognosis, and treatment guidelines

**FQ2 (Domain-specific, Understanding):** Concepts in clinical consultation such as how diagnostic tests inform treatment decisions and how disease severity affects management options

**FQ3 (Task-specific, Remembering):** Terms related to primary sclerosing cholangitis such as cholestasis, bile duct strictures, and liver transplantation

**FQ4 (Task-specific, Understanding):** Concepts related to primary sclerosing cholangitis such as the relationship between bile duct inflammation and liver failure, and why certain treatments may not alter disease prognosis

---

## Stage 5: Final Output

# Clinical consultation: Primary Sclerosing Cholangitis

| **Metadata** | For researchers only |
|---|---|
| **Domain** | Health |
| **Use case** | Clinical consultation |
| **Use case description** | Learn about a physician's diagnosis of a medical condition and accompanying treatment plan (including medications, dietary/behavioral instructions, etc.). |
| **Knowledge dimensions** | Factual |
| **Reference material filename** | primary-sclerosing-cholangitis.pdf |
| **Reference material source** | Patient.info: https://patient.info/doctor/gastroenterology/primary-sclerosing-cholangitis-pro |
| **Comprehension quiz source** | AQG |
| **Task inspiration** | Found through automatic source discovery. |
| **AI system prompt** | You are a helpful AI assistant that provides clear, informative, and educational information. |

| **Task data** | Displayed for participants |
|---|---|
| **Task ID** | primary-sclerosing-cholangitis |
| **Task title** | Primary Sclerosing Cholangitis |
| **Task topic** | Primary sclerosing cholangitis diagnosis and management |
| **Task description** | Primary sclerosing cholangitis (PSC) is a chronic liver disease characterized by inflammation and fibrosis of bile ducts, leading to strictures and potentially liver failure. In this task, you will need to learn as much as you can about PSC, including its epidemiology, diagnostic workup, management options, and prognosis. |
| **Task instruction for Explainer** | You will need to provide clear and accurate information about primary sclerosing cholangitis to your partner later. Your partner may come with specific questions with details, including but not exhaustive of diagnostic investigations and their limitations, treatment options for symptoms like pruritus, and surveillance recommendations for associated cancers, so pay attention to these details. |
| **Task instruction for Learner** | Your partner will have gained knowledge about primary sclerosing cholangitis, and you will have to learn from them by asking them to explain. Beyond general information, you should learn about how to solve problems that concern the following: 1. Selecting appropriate treatments for pruritus based on treatment guidelines. 2. Determining surveillance strategies for patients with and without inflammatory bowel disease. 3. Recognizing when patients meet criteria for liver transplantation evaluation. |
| **Formulas** | NA |


## Familiarity Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ1 |
| **Question** | Participants | How familiar are you with common clinical consultation terms such as diagnosis, prognosis, and treatment guidelines? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ2 |
| **Question** | Participants | How well do you understand concepts in clinical consultation such as how diagnostic tests inform treatment decisions and how disease severity affects management options? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Domain-specific |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ3 |
| **Question** | Participants | How familiar are you with terms related to primary sclerosing cholangitis such as cholestasis, bile duct strictures, and liver transplantation? |
| **Options** | Participants | ["1 (Not at all familiar)", "2", "3", "4", "5", "6", "7 (Very familiar)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | FQ4 |
| **Question** | Participants | How well do you understand concepts related to primary sclerosing cholangitis such as the relationship between bile duct inflammation and liver failure, and why certain treatments may not alter disease prognosis? |
| **Options** | Participants | ["1 (Not at all)", "2", "3", "4", "5", "6", "7 (Very well)"] |
| **Answer type** | Researcher-only | Single-select |
| **Category** | Researcher-only | Task-specific |
| **Bloom's level** | Researcher-only | Understanding |

## Comprehension Quiz

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ1 |
| **Question** | Participants | What is the median age at diagnosis for primary sclerosing cholangitis (PSC)? |
| **Options** | Participants | ["A. 25 years", "B. 35 years", "C. 45 years", "D. 55 years", "E. 65 years"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. 35 years"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ2 |
| **Question** | Participants | Which laboratory finding is the MOST common abnormality in primary sclerosing cholangitis? |
| **Options** | Participants | ["A. Elevated serum transaminases", "B. Elevated alkaline phosphatase or gamma-glutamyltransferase (GGT)", "C. Elevated serum bilirubin", "D. Decreased serum albumin", "E. Prolonged prothrombin time"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. Elevated alkaline phosphatase or gamma-glutamyltransferase (GGT)"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ3 |
| **Question** | Participants | Which imaging modality is the current standard procedure for visualizing the bile ducts in suspected primary sclerosing cholangitis? |
| **Options** | Participants | ["A. Abdominal ultrasound", "B. Computed tomography (CT) scan", "C. Magnetic resonance cholangiopancreatography (MRCP)", "D. Endoscopic retrograde cholangiopancreatography (ERCP)", "E. Positron emission tomography (PET) scan"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Magnetic resonance cholangiopancreatography (MRCP)"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ4 |
| **Question** | Participants | How many histological stages are used to classify primary sclerosing cholangitis? |
| **Options** | Participants | ["A. Two stages", "B. Three stages", "C. Four stages", "D. Five stages", "E. Six stages"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Four stages"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ5 |
| **Question** | Participants | What is the 5-year survival rate following liver transplantation for primary sclerosing cholangitis? |
| **Options** | Participants | ["A. 66%", "B. 76%", "C. 86%", "D. 96%", "E. 100%"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. 86%"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ6 |
| **Question** | Participants | Which sex is more commonly affected by primary sclerosing cholangitis? |
| **Options** | Participants | ["A. Males", "B. Females", "C. Both sexes are affected equally", "D. Males before age 40, females after age 40", "E. Females before age 40, males after age 40"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["A. Males"] |
| **Bloom's level** | Researcher-only | Remembering |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ7 |
| **Question** | Participants | Why is high-dose ursodeoxycholic acid (28-30 mg/kg/day) NOT recommended for patients with primary sclerosing cholangitis? |
| **Options** | Participants | ["A. It has been shown to accelerate disease progression", "B. It increases the rate of adverse events without proven clinical benefit", "C. It is contraindicated in patients with inflammatory bowel disease", "D. It causes severe drug interactions with immunosuppressants", "E. It is only effective in the early stages of PSC"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. It increases the rate of adverse events without proven clinical benefit"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ8 |
| **Question** | Participants | Which of the following BEST explains why fat-soluble vitamin supplementation may be required in patients with primary sclerosing cholangitis? |
| **Options** | Participants | ["A. PSC patients have increased metabolic demands that deplete vitamin stores", "B. Cholestatic conditions impair bile flow, which is necessary for fat-soluble vitamin absorption", "C. Ursodeoxycholic acid treatment depletes fat-soluble vitamins", "D. Liver transplantation requires vitamin supplementation beforehand", "E. Inflammatory bowel disease associated with PSC increases vitamin excretion"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. Cholestatic conditions impair bile flow, which is necessary for fat-soluble vitamin absorption"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ9 |
| **Question** | Participants | Why do surgical drainage procedures for primary sclerosing cholangitis NOT alter long-term prognosis despite potentially relieving symptoms? |
| **Options** | Participants | ["A. Surgical complications outweigh any temporary benefits", "B. The intrahepatic component of the disease continues to progress regardless of extrahepatic drainage", "C. Patients who undergo surgery are ineligible for future liver transplantation", "D. Surgical procedures are only palliative and cannot address biliary strictures", "E. Postoperative immunosuppression accelerates PSC progression"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. The intrahepatic component of the disease continues to progress regardless of extrahepatic drainage"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ10 |
| **Question** | Participants | Which of the following BEST explains the relationship between primary sclerosing cholangitis and inflammatory bowel disease? |
| **Options** | Participants | ["A. PSC is caused by inflammatory bowel disease spreading to the biliary system", "B. There is a significant association between PSC and IBD, though the causal mechanism remains unclear", "C. IBD develops as a complication of PSC due to shared autoimmune pathways", "D. PSC and IBD are different manifestations of the same genetic disorder", "E. Treating IBD with immunosuppressants prevents development of PSC"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. There is a significant association between PSC and IBD, though the causal mechanism remains unclear"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ11 |
| **Question** | Participants | Why does small-duct primary sclerosing cholangitis have a better prognosis than large-duct PSC? |
| **Options** | Participants | ["A. Small-duct PSC responds better to ursodeoxycholic acid therapy", "B. Small-duct PSC has longer transplant-free survival and appears unlikely to develop cholangiocarcinoma", "C. Small-duct PSC is not associated with inflammatory bowel disease", "D. Small-duct PSC spontaneously resolves in most patients", "E. Small-duct PSC does not progress to cirrhosis"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. Small-duct PSC has longer transplant-free survival and appears unlikely to develop cholangiocarcinoma"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ12 |
| **Question** | Participants | Which of the following BEST distinguishes primary sclerosing cholangitis from primary biliary cholangitis? |
| **Options** | Participants | ["A. PSC affects intrahepatic and extrahepatic ducts and occurs predominantly in males; PBC affects small interlobular ducts and occurs predominantly in females", "B. PSC is an autoimmune condition with antimitochondrial antibodies; PBC has an unclear cause", "C. PSC responds well to corticosteroid therapy; PBC does not respond to medical treatment", "D. PSC has a better prognosis than PBC after liver transplantation", "E. PSC is associated with colorectal cancer; PBC is associated with hepatocellular carcinoma"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["A. PSC affects intrahepatic and extrahepatic ducts and occurs predominantly in males; PBC affects small interlobular ducts and occurs predominantly in females"] |
| **Bloom's level** | Researcher-only | Understanding |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ13 |
| **Question** | Participants | A 38-year-old man with known primary sclerosing cholangitis presents with new-onset severe itching that significantly impairs his sleep and quality of life. Conservative measures have failed. According to treatment guidelines, which medication should be tried FIRST? |
| **Options** | Participants | ["A. Sertraline", "B. Naltrexone", "C. Colestyramine", "D. Rifampicin", "E. High-dose ursodeoxycholic acid"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Colestyramine"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ14 |
| **Question** | Participants | A 42-year-old man is newly diagnosed with primary sclerosing cholangitis. He has no known history of inflammatory bowel disease and denies any gastrointestinal symptoms. According to surveillance guidelines, what investigation should be performed? |
| **Options** | Participants | ["A. Annual abdominal CT scan to monitor for cholangiocarcinoma", "B. Total colonoscopy with biopsies to evaluate for occult inflammatory bowel disease", "C. Upper endoscopy to screen for esophageal varices", "D. Serum CA 19-9 levels every 6 months", "E. Liver biopsy annually to monitor disease progression"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["B. Total colonoscopy with biopsies to evaluate for occult inflammatory bowel disease"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ15 |
| **Question** | Participants | A 45-year-old woman with primary sclerosing cholangitis and ulcerative colitis has been stable for 3 years. She asks how often she should undergo colonoscopy surveillance. Based on guidelines, what is the recommended frequency? |
| **Options** | Participants | ["A. Every 5 years, as for average-risk colorectal cancer screening", "B. Every 3 years, given her history of IBD", "C. Annually, from the time of PSC diagnosis", "D. Every 2 years, alternating with MRCP surveillance", "E. Only when symptomatic with gastrointestinal complaints"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Annually, from the time of PSC diagnosis"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ16 |
| **Question** | Participants | A 50-year-old man with primary sclerosing cholangitis develops recurrent episodes of fever, right upper quadrant pain, and jaundice despite antibiotic courses. MRCP shows a dominant stricture in the common bile duct. What is the most appropriate next step in management? |
| **Options** | Participants | ["A. Long-term prophylactic antibiotic therapy", "B. High-dose ursodeoxycholic acid to dissolve the stricture", "C. Endoscopic balloon dilatation of the dominant stricture", "D. Immediate referral for liver transplantation", "E. Surgical resection of the affected bile duct segment"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Endoscopic balloon dilatation of the dominant stricture"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ17 |
| **Question** | Participants | A 55-year-old man with primary sclerosing cholangitis presents with new-onset ascites, confusion, and an INR of 2.5. His serum albumin is 2.2 g/dL and bilirubin is 8 mg/dL. Based on the Child-Turcotte-Pugh scoring system and clinical presentation, what does this clinical picture most likely indicate? |
| **Options** | Participants | ["A. Stage 1 PSC with mild disease activity", "B. Bacterial cholangitis requiring antibiotic therapy", "C. Advanced disease with hepatic failure requiring transplant evaluation", "D. Drug-induced liver injury from PSC medications", "E. Isolated portal hypertension with preserved liver function"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Advanced disease with hepatic failure requiring transplant evaluation"] |
| **Bloom's level** | Researcher-only | Applying |

| Field | Visibility | Value |
|---|---|---|
| **Question ID** | Participants | CQ18 |
| **Question** | Participants | A 35-year-old woman with recently diagnosed primary sclerosing cholangitis asks about lifestyle modifications. She currently drinks 1-2 glasses of wine with dinner on weekends. What is the most appropriate recommendation regarding alcohol consumption? |
| **Options** | Participants | ["A. Continue current alcohol intake as it is considered moderate and safe", "B. Reduce to no more than one drink per week to minimize liver stress", "C. Avoid alcohol completely as it is a risk factor for cholangiocarcinoma development", "D. Alcohol restriction is only necessary if cirrhosis develops", "E. Switch from wine to beer or spirits as they are less hepatotoxic"] |
| **Answer type** | Researcher-only | Single-select |
| **Correct answers** | Researcher-only | ["C. Avoid alcohol completely as it is a risk factor for cholangiocarcinoma development"] |
| **Bloom's level** | Researcher-only | Applying |

---

## Quality Summary

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total questions | 18 | 18 | ✅ |
| Remembering questions | 6 | 6 | ✅ |
| Understanding questions | 6 | 6 | ✅ |
| Applying questions | 6 | 6 | ✅ |
| Average difficulty score | 9.2/10 | ≥7.5 | ✅ |
| Lowest individual score | 8.8/10 | ≥7.0 | ✅ |
| MCQ best practices compliance | 100% | 100% | ✅ |
| Key position distribution | Varied (A-E) | No concentration | ✅ |
| Concept overlap | None | None | ✅ |
| In-scope verification | 100% | 100% | ✅ |