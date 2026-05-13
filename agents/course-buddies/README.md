# Course Buddyes Scaffolding

This folder provides dynamic course-buddy provisioning for multiple courses per student, with optional **Enterprising Ability gamification and analytics** for project-based courses like Grand Challenge Studio (GCS).

## Structure
1. instances: named coach slots (e.g. `course-buddy-gcs.md`) plus unassigned stubs (02-10).
2. streams: stream-specific starter templates.

## Provisioning flow
1. Copy a stream template or generic template.
2. Fill course code, name, syllabus outcomes, assessment blueprint.
3. Create a named slot file in `instances/` following the naming convention below.
4. Create a subfolder in `instances/[COURSE-CODE-ShortName]/` with `skill.md` and a `reference/` folder.
5. Update profile and evidence weekly.
6. **(For project courses like GCS)**: Enable gamification analytics in student profile → `## GCS Gamification Analytics`. See [`references/gcs-enterprising-ability-analytics.md`](../references/gcs-enterprising-ability-analytics.md).

## Naming standard
- Slot file: `course-buddy-[slug].md` (e.g. `course-buddy-gcs.md`, `course-buddy-dbms.md`)
- Subfolder: `instances/[COURSE-CODE ShortName]/` with `skill.md` inside
- Profile tracking: student profiles in `profiles/[full-name].md` with course-specific section + optional `## [Course] Gamification Analytics`

## GCS Gamification & Analytics

The Grand Challenge Studio (GCS) course integrates a six-dimensional **Enterprising Ability** analytics system mapped to Srujana Stage 3 (Creation) competencies:

- **6 analytics dimensions**: Rubric Mastery (5 rubrics: Pivot, Investigation, Collaboration, Prototype, Reflection) + Sprint Progress + Consistency + Evidence Quality + E2E Integration + Team Collaboration
- **Composite score**: Weekly updated Enterprising Ability Score (0–100) shown as pentagon radar chart
- **Badge system**: 5 core badges unlock when each rubric reaches Advanced level
- **Narrative arcs**: 4 story roles (Founder / Problem Solver / Change Maker / Researcher); 5 chapters unlock across 14 weeks
- **Public leaderboards**: 8 celebration categories (Investigation Masters, Pivot Artists, Collaboration Heroes, etc.) — opt-in, anonymous by default
- **Privacy by consent**: Private profile → Mentor share → Public leaderboard; all are student-controlled

**For coaches**: Step 10 of the weekly loop includes a **Gamification nudge** (1 min) that celebrates rubric progress and updates profile analytics.

**Full framework**: [`references/gcs-enterprising-ability-analytics.md`](../references/gcs-enterprising-ability-analytics.md)  
**Public leaderboard template**: [`eval/leaderboards/gcs-enterprising-ability.md`](../eval/leaderboards/gcs-enterprising-ability.md)
