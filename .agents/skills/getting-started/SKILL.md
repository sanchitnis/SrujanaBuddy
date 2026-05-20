---
name: getting-started
description: >
  REVA Getting Started Protocol — introduces new students to how SrujanaBuddy works,
  performs intake baselining, initializes aspirations and GPS map artifacts, and nudges
  early adoption of Srujana Presence (personal website + resume + GPS map).

  Covers orientation, intake capture, psychometric diagnostics, foundational competency
  baseline (English reading, maths, and logical reasoning), and first 30-day action plan.
  Includes 12 offline assessment apps.

  Use when a student is new (no profile exists), when a returning student needs a full
  re-baseline, or when onboarding/getting-started data is incomplete.

  Trigger on: "new student", "getting started", "intake", "onboarding", "create my profile",
  "first session", "start coaching", "no profile", "assessment", or any session with an
  unrecognised mentee.
---

# Getting Started Skill

> Full 5-step workflow: [`intake/intake-protocol.md`](../../intake/intake-protocol.md)

## When to use

- No profile exists in `profiles/` for the current student
- A returning student requests a full re-baseline
- Getting-started data is partial and needs completion

## What this skill must do

1. Explain how to use SrujanaBuddy in practical terms (session rhythm, commitments, evidence, review cadence).
2. Perform all current intake tasks.
3. Start Srujana Presence adoption early:
  - Personal website (starter intent)
  - Resume readiness baseline
  - GPS map creation and review rhythm
4. Continue collecting mentee data progressively in later sessions (do not force full completion on day one).

## Getting Started briefing script (first 2-3 minutes)

Use this flow before diagnostics:

1. What SrujanaBuddy does:
  - "We help you decide what you want, build skills for it, and move through weekly commitments."
2. How sessions work:
  - "Each session ends with one commitment, one evidence marker, and one next check date."
3. What the student must maintain:
  - `profiles/<full-name>.md` (living profile)
  - `profiles/<full-name>-aspirations.yaml` (north-star aspirations)
  - `profiles/<full-name>-gps-map.md` (ASCII progress map)
4. Presence nudge:
  - "Within first 2-3 sessions, start your personal website + resume baseline using Srujana Presence flow."

## Intake outcomes

1. Baseline student profile created at `profiles/<full-name>.md`
2. Academic history and current load captured
3. Personal priorities and constraints explicit
4. Initial risk level and support path assigned
5. First 30-day action plan agreed
6. **Presence bootstrap initiated** — `agents/srujana-presence-agent.md` loaded with collected artifacts (LinkedIn, resume, aspirations draft); scaffolds flagged for session 2 refinement
7. **Aspirations bootstrap completed** — first-draft fill of `Templates/StudentAspirationsForm.yaml` saved to `profiles/<full-name>-aspirations.yaml`
8. **GPS map initialized** — first visual goals map saved as `profiles/<full-name>-gps-map.md`
9. **Baseline competencies captured** — English reading comprehension, basic maths, and logical reasoning diagnostic saved in profile notes

## Psychometric apps (offline, no network required)

Run these during Step 3 (Baseline diagnostics). Open locally with any browser.

| # | App | What it measures |
|---|-----|-----------------|
| 1 | [`intake/apps/01-character-strengths.html`](../../intake/apps/01-character-strengths.html) | Character strengths and virtues |
| 2 | [`intake/apps/02-spheres-assessment.html`](../../intake/apps/02-spheres-assessment.html) | Five life spheres balance |
| 3 | [`intake/apps/03-leadership-oa-profile.html`](../../intake/apps/03-leadership-oa-profile.html) | Leadership and organisational awareness |
| 4 | [`intake/apps/04-growth-mindset.html`](../../intake/apps/04-growth-mindset.html) | Growth mindset orientation |
| 5 | [`intake/apps/05-grit-perseverance.html`](../../intake/apps/05-grit-perseverance.html) | Grit and perseverance |
| 6 | [`intake/apps/06-study-habits.html`](../../intake/apps/06-study-habits.html) | Study habits and learning strategies |
| 7 | [`intake/apps/07-time-management-procrastination.html`](../../intake/apps/07-time-management-procrastination.html) | Time management and procrastination patterns |
| 8 | [`intake/apps/08-stress-energy-self-check.html`](../../intake/apps/08-stress-energy-self-check.html) | Stress and energy baseline |
| 9 | [`intake/apps/09-career-interest-mapping.html`](../../intake/apps/09-career-interest-mapping.html) | Career interests and pathway exploration |

## Entry-level competency tests (offline)

Run these in getting-started after psychometric checks (or split over first 2 sessions if student is fatigued).

| # | App | What it measures |
|---|-----|-----------------|
| 10 | [`intake/apps/10-english-reading-comprehension.html`](../../intake/apps/10-english-reading-comprehension.html) | Entry-level reading comprehension and inference |
| 11 | [`intake/apps/11-basic-maths.html`](../../intake/apps/11-basic-maths.html) | Arithmetic and quantitative baseline |
| 12 | [`intake/apps/12-logical-reasoning.html`](../../intake/apps/12-logical-reasoning.html) | Pattern, sequence, and logic baseline |

## Diagnostic scheduling rule

1. If student energy is low or overwhelm is high, do not run all 12 apps in one sitting.
2. Minimum required in first sitting:
  - `08-stress-energy-self-check`
  - one psychometric app of choice
  - one competency app of choice
3. Complete remaining diagnostics in next 1-2 getting-started sessions.

## Profile template

New profiles are created from: [`profiles/_mentee-profile-template.md`](../../profiles/_mentee-profile-template.md)

Save as: `profiles/<full-name>.md` (hyphen-separated, no spaces)
Save aspirations as: `profiles/<full-name>-aspirations.yaml`
Save goals map as: `profiles/<full-name>-gps-map.md`

## Initial Aspirations Bootstrap (getting-started level)

At getting-started, run aspiration capture at beginner depth only.

1. Use REVA's official aspirations structure from `Templates/StudentAspirationsForm.yaml`.
2. Capture first-draft answers even if partial; do not wait for perfect clarity.
3. Save as `profiles/<full-name>-aspirations.yaml`.
4. Generate first GPS visual map using `Templates/StudentGPSMapTemplate.md` and save as `profiles/<full-name>-gps-map.md`.
5. Mark unclear fields for progressive follow-up sessions.
6. Do **not** introduce advanced Swadharma framing at intake; start with aspiration and ikigai basics.

## Srujana Presence nudge protocol

By end of getting-started:

1. Confirm if student has current resume (Yes/No).
2. Confirm if student has any personal web presence (Yes/No).
3. If No for either, set a soft launch commitment in first 30-day plan:
  - Resume baseline draft
  - Personal website baseline draft
4. Explain that GPS map is part of public narrative readiness and should be kept current.

Use: `agents/srujana-presence-agent.md` for implementation in follow-up sessions.

## Quick start

```
cd intake/apps && python3 -m http.server 8080
```
Then open `http://localhost:8080` in a browser to run assessments offline.
