# SrujanaBuddy

An open-source markdown-native AI coaching system for REVA University students.

## What this repository is

SrujanaBuddy is a multi-agent coaching operating system for UG and PG students across streams.
It is designed for action-first coaching in the AI era:
1. Learn-by-doing progression.
2. Career and competency development.
3. Holistic growth across five student life spheres.
4. Better execution and anti-procrastination discipline.
5. Portfolio-first outcomes.

The coach identity in sessions is **SrujanaBuddy**.

## Current implementation status

This repository is migrating in place from the previous SrujanaBuddy baseline to the REVA v1.4 specification.

### Completed in Sprint 1 kickoff
1. Orchestrator identity moved to SrujanaBuddy in [SKILL.md](SKILL.md).
2. Session routing structure updated to 15-agent architecture and 24 required session types.
3. Year-group differentiation added (Year 1, Year 2-3, Final Year, PG).

### In progress (next phases)
1. REVA reference layer and Five Student Spheres standardization.
2. Specialist agent expansion and subject-coach framework.
3. Intake/profile upgrades and psychometric app expansion.
4. GTD Lite runway enforcement, safety routing, metrics, and acceptance audits.

## Core design commitments

These commitments should be interpreted in line with [references/REVA University.md](references/REVA%20University.md), especially `The Strategic Directive: Educate to Enterprise`, `Spiritual and Moral Anchoring: The Gita Perspective and Universal Values`, and `Institutional Profile: REVA University's Vision, Mission, and Objectives`.

1. Aspirations-first coaching.
2. Ask-before-advice conversation flow.
3. AI augments learning, does not replace thinking.
4. Privacy by default and consent-first sharing.
5. Tiered wellbeing support with Manodhara referral for serious concerns.

## Repository structure

```text
SrujanaBuddy/
├── SKILL.md
├── agents/
├── references/
├── intake/
│   └── apps/
├── profiles/
├── gtd/
├── ai-delegation/
├── connectors/
├── COACHING-SESSION-WORKFLOW.md
├── REVA-STUDENT-SYSTEM-SPEC-v1.4.md
└── CONTRIBUTING.md
```

## How to use

1. Load [SKILL.md](SKILL.md) into your AI environment as the master orchestration file.
2. Start a session with a direct request, for example:
   - "Plan my day."
   - "Run weekly review."
   - "Help me prepare for exams."
   - "I need placement readiness coaching."
3. Use the GTD and profile files to track commitments, completions, and progress.

## Key references

1. [REVA-STUDENT-SYSTEM-SPEC-v1.4.md](REVA-STUDENT-SYSTEM-SPEC-v1.4.md)
2. [references/REVA University.md](references/REVA%20University.md)
3. [SKILL.md](SKILL.md)
4. [COACHING-SESSION-WORKFLOW.md](COACHING-SESSION-WORKFLOW.md)
5. [gtd/GTD-GUIDE.md](gtd/GTD-GUIDE.md)
6. [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License. See [LICENSE](LICENSE).
