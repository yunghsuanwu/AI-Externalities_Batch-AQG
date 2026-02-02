# Domain Expert Agents

Specialized validators for domain-specific accuracy. Ensures questions test correct information.

## Common Output Format

```json
{
  "workflow_id": "string",
  "status": "approved" | "approved_with_notes" | "revision_required" | "rejected",
  "source_assessment": [
    {
      "url": "string",
      "authority_rating": "authoritative" | "acceptable" | "questionable",
      "currency": "current" | "dated" | "outdated"
    }
  ],
  "accuracy_review": [
    {
      "claim": "specific claim from content",
      "assessment": "accurate" | "inaccurate" | "outdated",
      "correction": "correct information if needed"
    }
  ],
  "question_accuracy": [
    {
      "question_id": "CQ1",
      "correct_answer_verified": true | false,
      "issues": "any accuracy problems"
    }
  ]
}
```

---

## Health Domain Expert

### Source Authority Tiers

**TIER 1**: CDC, NIH, FDA, HHS, peer-reviewed journals, Mayo Clinic, Cleveland Clinic

**TIER 2**: AHA, ACS, ADA, state health departments, WHO

**NOT ACCEPTABLE**: Health blogs, supplement companies, social media

### Currency Requirements

- **Current**: Within 3 years
- **Rapidly changing topics** (vaccines, COVID): Within 1 year

### Verify Question Accuracy

For each health question, confirm:
- Correct answer matches current clinical guidelines
- Thresholds/values are up-to-date
- No dangerous misinformation in any option

---

## Finance Domain Expert

### Source Authority Tiers

**TIER 1**: IRS, SEC, CFPB, FDIC, SSA, DOL, Federal Reserve

**TIER 2**: FINRA, state regulators, NEFE, Jump$tart

**NOT ACCEPTABLE**: Financial product marketing, personal finance blogs

### Check for Outdated Values

Verify annually:
- IRA/401(k) contribution limits
- Tax brackets and standard deduction
- FDIC insurance limits
- Social Security thresholds

### Verify Question Accuracy

For each finance question:
- Numerical values are current
- Regulatory requirements are accurate
- No misleading financial advice in any option

---

## Legal Domain Expert

### Source Authority Tiers

**TIER 1**: U.S. Courts, DOJ, EEOC, DOL, HUD, OSHA, FTC

**TIER 2**: State court self-help, ACLU, Legal Aid, Cornell LII, Nolo

**NOT ACCEPTABLE**: Legal forums, non-attorney blogs

### Jurisdiction Sensitivity

Flag when content:
- Presents state-specific rules as universal
- Doesn't note significant state variations
- May mislead about legal rights

### Verify Question Accuracy

For each legal question:
- Legal principles are correctly stated
- Jurisdiction limitations are noted where relevant
- No option could lead to harmful misunderstanding of rights
