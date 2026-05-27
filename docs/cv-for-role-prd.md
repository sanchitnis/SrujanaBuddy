# Product Requirements Document (PRD)
## cv-for-role — Student Resume Tailoring Assistant

**Version:** 1.0  
**Date:** 26 May 2026  
**Primary Users:** Students  
**Language:** English  
**Output Format (now):** Markdown (`.md`)  
**Output Format (later):** DOCX (`.docx`)  
**Compliance Baseline:** Indian laws

---

## 1) Inputs Captured from Stakeholder

1. Product name: `cv-for-role`
2. Users: Students
3. Output format: Markdown now, DOCX later
4. Language: English
5. Sources: Accept all sources provided by the user
6. Compliance: Indian laws
7. Include scoring: Yes
8. Include cover letter tone selection: Yes
9. Include interview follow-up rounds: Yes
10. Add additional useful safeguards and requirements: Yes

---

## 2) Purpose

Build a student-first system that converts a student's profile and role/job description into:
- a role-tailored ATS-ready resume,
- a cover letter with selectable tone,
- and interview preparation responses with follow-up rounds,

while enforcing evidence-based claims and Indian legal-compliance guardrails.

---

## 3) Scope

### In Scope (v1)

1. Student master profile creation and reuse.
2. JD/role description ingestion and requirement extraction.
3. Public source links ingestion from user input.
4. User document upload ingestion.
5. Resume generation in Markdown.
6. Cover letter generation in Markdown with tone controls.
7. Interview Q&A generation with multi-round follow-up prompts.
8. Dashboard with Match %, ATS %, and Gap score.
9. Evidence tracing and anti-fabrication checks.
10. Consent and data-handling controls aligned to Indian law baseline.

### Out of Scope (v1)

1. Native DOCX export (planned phase).
2. Non-English generation.
3. Automatic scraping of private or login-gated data.

---


## 4) Core Functional Requirements

### 4.1 Profile Layer

1. Capture structured student profile:
   - Education
   - Skills
   - Projects
   - Internships
   - Certifications
   - Achievements
   - Leadership and extracurricular activities
2. Prompt for measurable outcomes (metrics, impact, scale, frequency).
3. Track profile completeness and missing fields.

### 4.2 Source & Upload Layer

1. Accept all user-provided supported sources.
2. Validate link accessibility (public access check).
3. Ingest uploaded documents and map extracted facts to profile entities.
4. Flag conflicts (dates, titles, timelines, claims) and require user confirmation.
5. Allow per-source include/exclude toggles.

### 4.3 JD Matching & Tailoring

1. Parse JD into:
   - Must-have skills
   - Preferred skills
   - Responsibilities
   - Domain terminology
2. Build requirement-to-evidence mapping.
3. Generate role-tailored bullets only from available evidence.
4. Highlight uncovered requirements and suggest actionable gap closure.

### 4.4 Content Generation

1. Generate ATS-friendly resume in Markdown.
2. Generate cover letter in Markdown with tone selector (for example: formal, concise, confident).
3. Generate interview answer bank:
   - behavioral,
   - role-specific,
   - follow-up deep-dive rounds.

4. **Generate 2-Minute Video Resume Script**
   - Allow any applicant (not just students) to generate a concise, 2-minute video resume script tailored to their experience level and target role.
   - Script structure: introduction, experience summary, key skills, achievements, closing statement.
   - Input prompts for experience level, achievements, and target role.
   - Output: ready-to-record script (approx. 250–300 words) in Markdown.
   - Provide clear instructions for applicants to record their video using the script.
   - Ensure inclusive language for applicants at all experience levels.

### 4.5 Scoring & Feedback Dashboard

1. Match Score (0–100)
2. ATS Keyword Coverage (0–100)
3. Gap Score (0–100)
4. Top improvements list before application submission.

---

## 5) Compliance and Legal Requirements (India Baseline)

1. Consent-first processing for personal data.
2. Purpose limitation (job-application assistance use-case).
3. Data minimization.
4. User ability to access, correct, and request deletion of their data.
5. Reasonable security controls for stored and transmitted data.
6. Source transparency: show what evidence was used for generated outputs.

> Note: final legal language and obligations should be reviewed with legal counsel.

---

## 6) Additional Safeguards (Added)

The system must block, warn, or escalate confirmation for:

1. Fake experience duration or years.
2. Fake company names, job titles, or promotions.
3. Fake projects, publications, or open-source claims.
4. Fake certifications or education credentials.
5. Unverified performance metrics or impact numbers.
6. Plagiarized personal statements.
7. Discriminatory or protected-attribute-biased content.
8. Contradictory timeline claims.
9. Confidential employer data exposure.
10. Any claim without traceable evidence in profile, source, or uploaded content.

---


## 6A) Implementation Plan: Video Resume Script Feature

1. **Requirements & Design**
   - Define script structure: intro, experience, skills, achievements, closing.
   - Make prompts/app flow generic for “applicant” (not just students).
   - Allow input for experience level, key achievements, and target role.

2. **Script Generation Logic**
   - Create a template or script generator (Markdown or Python script).
   - Use applicant’s profile data (if available) or prompt for details.
   - Ensure output is a 2-minute script (approx. 250–300 words).

3. **User Interface/Workflow**
   - Add a section in docs/cv-for-role-prd.md or a new tool in tools/ for video resume script generation.
   - Provide clear instructions for applicants to record their video using the script.

4. **Integration**
   - Link the script generator from relevant documentation (e.g., CV guide).
   - Optionally, add a CLI or web form for easy script generation.

5. **Testing & Review**
   - Test with profiles of varying experience.
   - Review for clarity, brevity, and inclusivity.

---

## 7) Release Plan

### Phase 1 (MVP)

1. Profile + source + upload ingestion.
2. JD parsing and requirement matching.
3. Markdown resume and cover letter generation.
4. Interview Q&A generation with basic follow-up rounds.
5. Scoring dashboard and anti-fabrication checks.

### Phase 2

1. Advanced follow-up interview simulation depth.
2. Better explainability of why each bullet/answer was generated.
3. Snapshot/version support per role application.

### Phase 3

1. DOCX export.
2. Additional language support.

---

## 8) Acceptance Criteria

1. Given a completed student profile and JD, the system generates a role-tailored resume in Markdown.
2. Generated claims are evidence-grounded and traceable to user-provided data.
3. Invalid/private links are flagged and excluded from evidence.
4. Cover letter output changes correctly by selected tone.
5. Dashboard consistently reports Match %, ATS %, and Gap score.
6. Interview module returns both initial and follow-up rounds.
7. User can edit generated content before final export.
8. Data correction/deletion requests are supported in workflow.
9. Conflicting claims trigger confirmation flow before generation.
10. Fabricated or unverifiable claims are blocked or flagged.
