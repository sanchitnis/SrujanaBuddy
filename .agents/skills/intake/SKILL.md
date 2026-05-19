---
name: intake
description: >
  REVA Student Intake Protocol — initialises a new student in SrujanaBuddy and establishes
  coaching readiness across academics, wellbeing, and progression. Covers orientation and
  consent, core data capture, baseline diagnostics, goal setting, and first 30-day plan.
  Includes 9 offline psychometric assessment apps.

  Use when a student is new (no profile exists), when a returning student needs a full
  re-baseline, or when onboarding information is incomplete.

  Trigger on: "new student", "intake", "onboarding", "create my profile", "first session",
  "start coaching", "no profile", "assessment", or any session with an unrecognised mentee.
---

# Student Intake Skill

> Full 5-step workflow: [`intake/intake-protocol.md`](../../intake/intake-protocol.md)

## When to use

- No profile exists in `profiles/` for the current student
- A returning student requests a full re-baseline
- Intake data is partial and needs completion

## Intake outcomes

1. Baseline student profile created at `profiles/<full-name>.md`
2. Academic history and current load captured
3. Personal priorities and constraints explicit
4. Initial risk level and support path assigned
5. First 30-day action plan agreed
6. **Presence bootstrap initiated** — `agents/srujana-presence-agent.md` loaded with collected artifacts (LinkedIn, resume, aspirations draft); scaffolds flagged for session 2 refinement

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

## Profile template

New profiles are created from: [`profiles/_mentee-profile-template.md`](../../profiles/_mentee-profile-template.md)

Save as: `profiles/<full-name>.md` (hyphen-separated, no spaces)
Save aspirations as: `profiles/<full-name>-aspirations.yaml`

## Quick start

```
cd intake/apps && python3 -m http.server 8080
```
Then open `http://localhost:8080` in a browser to run assessments offline.
