# Automatic Question Generation Workflow

I'll execute the workflow to generate a quiz about probate based on the California Courts reference material.

## Workflow Detection

**Input Analysis:**
- Reference material provided: ✓ (PDF file path)
- Sample questions provided: ✗
- Additional prompts: ✗

**Selected Path:** Path B (Source Materials Provided)
- Skip SOURCE_DISCOVERY and DOMAIN_EXPERT
- Start with QUESTION_WRITER
- No SAMPLE_QUESTION_EXTRACTOR needed

---

## Step 1: Analyzing Reference Material

First, I need to examine the probate.pdf file to understand the scope and identify testable content.

**Request:** Please provide the contents of the PDF file at `/Users/WuYung-Hsuan/Desktop/coding-stuff/AI-Externalities_Batch-AQG/reference_materials/probate.pdf` so I can analyze it and generate appropriate questions.

**Note:** Since I cannot directly access local file systems, I need you to either:
1. Paste the text content of the PDF here, OR
2. Upload the PDF file to this conversation, OR
3. Provide the text/content from the PDF

Once I have the reference material content, I will proceed through the remaining workflow steps:
- QUESTION_WRITER → Generate 12-15 candidate questions across Bloom's levels
- PSYCHOMETRIC_REVIEWER → Evaluate and select best 9 questions
- CURRICULUM_DESIGNER → Derive learning objectives and familiarity quiz
- CONSISTENCY_AGENT → Format final output

Please provide the PDF content so I can continue with the generation process.