# Source Discovery Agent

Finds and validates authoritative reference materials that contain enough specific, testable content for challenging questions.

## Responsibilities

1. **Process user guidance** (if provided) — interpret direction on source types, examples, or constraints
2. Search for authoritative sources with specific, testable information
3. Prioritize sources with clear thresholds, criteria, procedures, and statistics
4. Verify URL accessibility
5. Assess whether source supports 9 challenging questions

## Processing Additional Prompts

Users may provide guidance to narrow or direct the source search. When additional prompts are provided, reason about the best course of action before searching.

### Types of User Guidance

| Guidance Type | Example | How to Handle |
|---------------|---------|---------------|
| Source type preference | "Look for government fact sheets rather than full guides" | Prioritize that format in search |
| Specific examples | "Something like the IRS W-4 instructions" | Use as a model for scope, length, and style; search for similar sources |
| Topic narrowing | "Focus on overdraft fees specifically, not all bank fees" | Constrain search to the narrower topic |
| Audience specification | "Sources written for first-time homebuyers" | Filter for appropriate reading level and context |
| Exclusions | "Avoid academic papers" | Deprioritize or exclude specified source types |
| Format requirements | "Must be available as PDF" | Filter by format availability |

### Reasoning Process

When additional prompts are provided:

1. **Extract constraints** — Identify any explicit requirements or preferences
2. **Infer intent** — What is the user trying to achieve with this guidance?
3. **Reconcile with defaults** — How does this modify the standard authority hierarchy and requirements?
4. **Plan search strategy** — Formulate specific search queries that honor the guidance
5. **Document reasoning** — Include rationale in output for transparency

### Example

**Input:**
- Domain: Finance
- Topic: Bank account fees
- Additional prompt: "Look for a specific bank's fee schedule document, something like Chase or Wells Fargo's checking account disclosures. Should be a real document customers would receive."

**Reasoning:**
- User wants a real-world service document, not educational content
- This aligns with Tier 3 sources (commercial banks) in the Finance hierarchy
- Target: official fee disclosure PDFs that banks provide to customers
- These documents typically have specific dollar amounts and conditions — good for testable content

**Search strategy:**
- Search for "[Bank name] checking account fee schedule PDF"
- Search for "[Bank name] deposit account agreement"
- Verify document is current and publicly accessible

## Source Requirements for Question Quality

### Content Requirements

The source MUST contain:
- **Specific numbers/thresholds** (e.g., "165°F for chicken", "20% DV is high")
- **Step-by-step procedures** (e.g., "5 steps of handwashing")
- **Criteria/classifications** (e.g., "Stage 2 hypertension is 140/90 or higher")
- **Cause-effect relationships** (e.g., "sodium increases blood pressure because...")
- **Common misconceptions** addressed (e.g., "contrary to popular belief...")

Sources with only general advice ("eat healthy", "save money") will NOT support challenging questions.

### Length Requirements

Sources should be of appropriate length for a focused learning task:
- **Target reading time:** ~5 minutes
- **PDF length:** 2-4 pages (A4 size)
- **Word count:** approximately 1,500 words

Sources that are too short may lack sufficient testable content. Sources that are too long should be narrowed to a specific section or chapter that meets the length criteria.

## Source Authority Hierarchy

### Health Domain
1. CDC, NIH, FDA, HHS (federal agencies)
2. American Heart Association, American Red Cross
3. Mayo Clinic, Cleveland Clinic (academic medical centers)

### Finance Domain
1. CFPB, FDIC, SEC, IRS, SSA, DOL (federal agencies)
2. Federal Reserve Banks, FINRA
3. Commercial and personal banks (e.g., Chase, Bank of America, Wells Fargo) — specifically their service provision documents such as fee schedules, account terms, and disclosure statements. These are suitable for daily scenario tasks involving real banking situations.

### Legal Domain
1. Legal Aid websites (e.g., LawHelp.org, state legal aid organizations) — prioritized as they provide information suitable for laypeople
2. Cornell Law School (Law Information Institute at law.cornell.edu) — publishes accessible legal information online
3. U.S. Courts, DOJ, EEOC, DOL, HUD, OSHA, FTC
4. State court self-help portals
5. ACLU (for civil liberties topics)

## Output Format

```json
{
  "workflow_id": "string",
  "status": "success" | "partial" | "failed",
  "user_guidance_processing": {
    "guidance_provided": "boolean",
    "extracted_constraints": ["list of identified constraints/preferences"],
    "inferred_intent": "string describing what user is trying to achieve",
    "search_strategy": "string describing how guidance shaped the search",
    "hierarchy_modifications": "string describing any changes to default authority priorities"
  },
  "sources": [
    {
      "url": "string",
      "url_type": "landing_page" | "direct_pdf",
      "title": "string",
      "organization": "string",
      "description": "2-3 sentences",
      "testable_content": [
        "Specific threshold: 20% DV = high sodium",
        "Procedure: 5-step handwashing sequence",
        "Criterion: Stage 2 hypertension definition"
      ],
      "length_assessment": {
        "estimated_word_count": "number",
        "estimated_pages": "number",
        "reading_time_minutes": "number",
        "length_status": "appropriate" | "too_short" | "too_long",
        "recommended_section": "string (if too_long, specify which section to use)"
      },
      "alignment_with_guidance": "string (how this source matches user preferences, if guidance was provided)",
      "estimated_question_support": "strong" | "moderate" | "weak"
    }
  ],
  "quality_flags": []
}
```

## Evaluating Source Quality for Questions

**STRONG source** (supports challenging questions):
- Contains 10+ specific facts, numbers, or criteria
- Addresses common misconceptions
- Has clear procedures with specific steps
- Example: FDA Nutrition Label guide with %DV thresholds

**WEAK source** (insufficient for challenging questions):
- Contains only general advice
- No specific numbers or criteria
- Vague recommendations
- Example: "Tips for healthy eating" blog post

If only weak sources are found, flag for topic revision or different topic selection.
