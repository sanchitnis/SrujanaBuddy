# CV-for-Role Plugin — Skill Specification

## Overview
Comprehensive resume tailoring assistant for applicants (students or experienced professionals). Generates:
- ATS-ready resume (Markdown)
- Cover letter with tone selection
- Interview Q&A (multi-round)
- Scoring dashboard (Match %, ATS %, Gap score)
- 2-minute video resume script

---

## Skills

### 1. generate-resume
- **Inputs:** Applicant profile, job description (JD), supporting documents/links
- **Output:** Markdown resume tailored to the role, evidence-based, ATS-friendly
- **Flow:**
  1. Ingest applicant profile and JD
  2. Extract requirements and map to profile evidence
  3. Generate resume with only verifiable claims
  4. Highlight missing requirements

### 2. generate-cover-letter
- **Inputs:** Applicant profile, target role, tone (formal, concise, confident, etc.)
- **Output:** Markdown cover letter in selected tone
- **Flow:**
  1. Ingest profile and target role
  2. Prompt for tone
  3. Generate cover letter accordingly

### 3. generate-interview-qa
- **Inputs:** Applicant profile, target role
- **Output:** Interview Q&A bank (behavioral, role-specific, follow-up rounds)
- **Flow:**
  1. Ingest profile and role
  2. Generate initial and follow-up questions/answers

### 4. generate-scoring-dashboard
- **Inputs:** Profile, JD, resume, cover letter
- **Output:** Dashboard with Match %, ATS %, Gap score, improvement suggestions
- **Flow:**
  1. Analyze generated content
  2. Compute scores and suggest improvements

### 5. generate-video-resume-script
- **Inputs:** Applicant name, experience, achievements, target role, skills, motivation, reflection
- **Output:** 2-minute video resume script (Markdown)
- **Flow:**
  1. Prompt for required details
  2. Generate script using template

---

## Compliance & Safeguards
- Consent-first data handling
- Evidence-based claims only
- Block/warn on unverifiable or fabricated claims
- Indian legal compliance
- User can edit generated content before export

---

## Example Usage
- See PRD in docs/cv-for-role-prd.md for detailed requirements and flows.

---

## Implementation Notes
- All skills must use inclusive language (applicant, not just student)
- Modular: each skill can be invoked independently
- CLI and Markdown integration supported
- Data processed locally (T0/T2 preferred)
