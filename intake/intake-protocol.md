# REVA Student Intake Protocol

This protocol initializes a student in SrujanaBuddy and establishes coaching readiness across academics, wellbeing, and progression.
Use [references/REVA University.md](references/REVA%20University.md) whenever intake needs to make REVA's institutional values, mission, or student expectations explicit.

## Intake outcomes
1. Baseline student profile is complete.
2. Academic history and current load are captured.
3. Personal priorities and constraints are explicit.
4. Initial risk level and support path are assigned.
5. First 30-day action plan is agreed.

## Intake workflow
1. Orientation and consent
   1. Confirm student consent for coaching and data usage.
   2. Explain support boundaries, confidentiality limits, and escalation conditions.
2. Core data capture
   1. Program, stream, year, semester, section.
   2. Mother tongue — used to set coaching language register (see `SKILL-context.md` → Tone and Voice → Mother Tongue Tone Map).
   3. Personality quick-check — introvert / extrovert / ambivert; confidence baseline 1–10.
   4. Sharing consent and avatar name — captured when name is asked (see `getting-started` SKILL.md → Q4). Two options: real name or avatar name. No partial-sharing option — to limit what is shared, the student deletes specific entries from their course profile log files. Store in `profiles/<full-name>.md` → Identity fields 9–10.
   5. Current subjects and known backlog.
   5. Recent performance indicators and attendance patterns.
   6. Optional pre-existing artifacts — collect before asking duplicate questions:
      - LinkedIn or other social/portfolio URL (GitHub, Behance, personal site)
      - Existing resume — pasted text or described section by section
      - Scanned or photographed handwritten aspiration sheet
      - If any artifact is provided, extract and pre-fill profile fields from it; confirm with mentee rather than re-asking what is already known.
3. Baseline diagnostics
   1. Five Student Spheres quick check.
   2. Study habits and time management snapshot.
   3. Stress, sleep, and energy self-check.
   4. Coaching readiness and preferences:
      - Work style: Do they prefer fast ambitious progress with hard/smart work, or slow fun-oriented completion of simple tasks?
      - Energy state: On a 1-10 scale, how are they feeling right now? (1 = very low, 10 = very high)
      - Overwhelm level: None / Mild / Moderate / High?
      - Clarity: Are they clear on what they want, exploring, or confused?
      - Show-up reliability: Can they commit to showing up consistently for coaching?
      - System readiness: Do they have time, mental capacity, and tech access to engage with the system?
4. Goal and direction setting
   - Guide this section using `The Strategic Directive: Educate to Enterprise` and the student-principles section in [references/REVA University.md](references/REVA%20University.md#L43).
   1. 1 academic goal for 30 days.
   2. 1 habit goal for consistency.
   3. 1 career exploration step.
   4. **Aspirations discovery** (progressive):
      - Start collaborative fill of `Templates/StudentAspirationsForm.yaml` during intake.
      - Do not expect complete form in first session if student is exploring.
      - Save first draft as `profiles/<full-name>-aspirations.yaml` even if partial.
      - Plan to revisit and refine aspirations in session 2, month-end review, and whenever direction clarity shifts.
      - **Note in profile**: Aspirations form is *living* — update every 30-60 days or when student insights shift, not one-time only.
5. Setup and handoff
   1. Create profile from template.
   2. **Populate Coaching Context section** with readiness signals and preferences captured in step 3.
   3. Initialize GTD Lite lists.
   4. Route first session type and assigned coach — **calibrated to coaching context** (e.g., if overwhelmed+low energy, start with wellbeing/grounding, not heavy planning).
   5. Link profile + aspirations file as north-star inputs for the first 30-day plan.
   6. **Document update cadence**: Flag in profile when aspirations and coaching context should be revisited (typically month-end or after significant session).
   7. **Presence bootstrap** — Hand off to `agents/srujana-presence-agent.md`. Feed artifacts already collected in step 2.4 (LinkedIn URL, resume text, aspirations draft) to pre-fill the website and resume scaffolds. Even a partial draft in session 1 is enough — the agent will fill placeholders and flag what is missing. Schedule presence refinement in session 2.

## Risk and escalation
1. Green: normal coaching cadence.
2. Amber: weekly monitoring and faculty mentor visibility.
3. Red: immediate referral per support escalation guide.

## Required artifacts
1. Completed profile file (including Coaching Context section with work style, energy, overwhelm, clarity, show-up reliability).
2. Intake app outputs copied into profile evidence section.
3. First 30-day plan with dated checkpoints — **paced according to coaching context** (not all students same speed).
4. Assigned session type for next interaction — **calibrated to readiness signals**.
5. Aspirations file draft: `profiles/<full-name>-aspirations.yaml` (may be partial at intake; plan refinement sessions).
6. North-star note that maps aspirations to the first 30-day plan.
7. Coach notes on how to adjust session intensity, pacing, and style based on this student's coaching context.

## Service level expectations
1. Intake completion target: 1 guided session.
2. First checkpoint: within 7 days.
3. Progress review: day 30.
