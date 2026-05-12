# Course Coaches Scaffolding

This folder provides dynamic course-coach provisioning for up to 10 courses per student.

## Structure
1. instances: named coach slots (e.g. `course-coach-gcs.md`) plus unassigned stubs (02-10).
2. streams: stream-specific starter templates.

## Provisioning flow
1. Copy a stream template or generic template.
2. Fill course code, name, syllabus outcomes, assessment blueprint.
3. Create a named slot file in `instances/` following the naming convention below.
4. Create a subfolder in `instances/[COURSE-CODE-ShortName]/` with `skill.md` and a `reference/` folder.
5. Update mastery and evidence weekly.

## Naming standard
- Slot file: `course-coach-[slug].md` (e.g. `course-coach-gcs.md`, `course-coach-dbms.md`)
- Subfolder: `instances/[COURSE-CODE ShortName]/` with `skill.md` inside
- Profile tracking: student profiles in `profiles/[full-name].md` with course-specific section
