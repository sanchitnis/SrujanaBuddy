# Course Buddy Builder Agent

## Status

**Internal infrastructure — not student-facing.**
This agent is not routed through `SKILL.md` and is never triggered during student coaching sessions.
It is used by faculty and the REVA core team to build, refresh, and audit course knowledge artefacts.

---

## Purpose

The Course Buddy Builder Agent automates the creation and maintenance of three knowledge artefacts per course:

| Artefact | Format | Used by |
|----------|--------|---------|
| Knowledge wiki | Obsidian Markdown (`knowledge/[CourseCode]-[ShortName]/wiki/`) | Students (self-study), Course Buddy (session context) |
| Practice workbook | Jupyter notebook (`knowledge/[CourseCode]-[ShortName]/workbook.ipynb`) | Students (practice + portfolio evidence) |
| Course Buddy skill | Markdown (`agents/course-buddyes/instances/[CourseCode]-[ShortName]/skill.md`) | SrujanaBuddy (Course Buddy 01-10 routing) |

**Philosophy anchor**: [references/ai-tutor-philosophy.md](../references/ai-tutor-philosophy.md)

**Tool**: [tools/course-buddy-builder/](../tools/course-buddy-builder/)

---

## Operating Modes

### Mode 1 — Build (full pipeline for a new course)

**Trigger**: Faculty or admin runs the builder for a course that has no existing wiki.

**Input**: A completed course descriptor (`tools/course-buddy-builder/templates/course-descriptor.md`).

**Pipeline**:
1. Parse course descriptor YAML frontmatter and Markdown body.
2. Create a NotebookLM notebook named `SrujanaBuddy-[CourseCode]`.
3. Add all sources (URLs, YouTube, PDFs) from the descriptor.
4. Generate: study guide (Markdown), quiz (JSON), flashcards (Markdown), mind map (JSON), audio overview (MP3).
5. Download all artefacts.
6. `wiki_generator.py` → produces Obsidian wiki pages (index, concept pages at 3 levels, glossary, concept-map Mermaid diagram, Obsidian vault stub).
7. `workbook_generator.py` → produces Jupyter notebook (one section per unit, quiz-derived exercises, evidence prompts).
8. `skill_generator.py` → produces Course Buddy skill.md (Socratic protocol, pre-populated mastery tracker, concept dependency map from NLM mind map).
9. Write contribution scaffolding (CONTRIBUTING.md, faculty-notes/README.md, student-contributions/README.md).

**Command**:
```bash
cd tools/course-buddy-builder
python3 build.py --course-file templates/[CourseCode]-descriptor.md --output-dir ../../knowledge/
```

**Output**: `knowledge/[CourseCode]-[ShortName]/` folder with all artefacts.

**Post-build step**: Assign the generated skill to an instance slot in `agents/course-buddyes/instances/` (slots 01-10). Update the student's profile to reference the slot.

---

### Mode 2 — Refresh (update artefacts for an existing course)

**Trigger**: Any of the following:
- F-9 domain gap items logged in `eval/data/IMPROVEMENT-BACKLOG.md` for this course.
- Course syllabus updated (new units, changed outcomes).
- New sources added (new textbook edition, updated lecture notes, new NPTEL playlist).
- Faculty requests a refresh (e.g., after a semester of student feedback).

**Pipeline**: Same as Build, but reuses the existing NotebookLM notebook (does not delete and recreate). Gap topics from `eval_bridge.py` are queried as additional chat questions and appended to the study guide.

**Command**:
```bash
# Step 1: extract gap topics from eval backlog
GAP_TOPICS=$(python3 tools/course-buddy-builder/eval_bridge.py --course-code CSE301)

# Step 2: run refresh with gap topics
python3 tools/course-buddy-builder/build.py \
  --course-file tools/course-buddy-builder/templates/CSE301-descriptor.md \
  --output-dir knowledge/ \
  --refresh \
  --gap-topics "$GAP_TOPICS"
```

**Output**: Updated wiki pages (concept pages re-generated, study guide supplement appended), updated workbook exercises, updated skill mastery tracker pre-population.

---

### Mode 3 — Audit (check existing knowledge artefacts for staleness)

**Trigger**: Quarterly review, or before a new semester begins.

**What to check**:

| Check | Pass condition | Action if fail |
|-------|---------------|----------------|
| Wiki completeness | All concepts from descriptor have a wiki page | Run Mode 1 or update descriptor |
| Wiki currency | All pages updated within the last 180 days | Run Mode 2 (refresh) |
| Workbook openability | `workbook.ipynb` opens without error in Jupyter | Regenerate workbook |
| Skill currency | Skill.md was generated from current descriptor version | Run Mode 1 with same descriptor |
| F-9 backlog | No open F-9 items older than 30 days for this course | Run Mode 2 with gap topics |
| Audio presence | `audio-overview.mp3` exists | Run Mode 2 (audio only flag) |

**Manual audit command** (dry run prints what is stale):
```bash
python3 tools/course-buddy-builder/build.py \
  --course-file tools/course-buddy-builder/templates/CSE301-descriptor.md \
  --output-dir knowledge/ \
  --dry-run
```

---

## Input Contract

### Required fields in course descriptor frontmatter

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `course_code` | string | Yes | University course code (folder key) |
| `course_name` | string | Yes | Full course name |
| `short_name` | string | Yes | Short identifier (used in file names) |
| `stream` | string | Yes | CSE / ECE / MBA / BCA / MCA / MTECH / PHD / other |
| `semester` | int | Yes | 1-8 (UG) or 1-4 (PG) |
| `instructor` | string | No | Course instructor name |
| `notebooklm_sources.urls` | list | No | Web URLs to add as NLM sources |
| `notebooklm_sources.files` | list | No | Relative paths to PDF/DOCX files |
| `textbooks` | list | No | Textbook entries with title/authors/edition/isbn |

### Required sections in course descriptor body

| Section | Required | Notes |
|---------|----------|-------|
| `# Unit Breakdown` | Yes | Must contain `## Unit N —` subsections |
| Each unit must have | Yes | Numbered outcome lines + `- [ ]` concept checkboxes |
| `# Assessment Blueprint` | No | Used in skill mastery tracker context |
| `# Srujana Evidence Mapping` | No | Used in workbook evidence prompts |

---

## Output Contract

| Artefact | Path | When available |
|----------|------|----------------|
| Wiki index | `knowledge/[CODE]-[SHORT]/wiki/index.md` | Always |
| Concept pages | `knowledge/[CODE]-[SHORT]/wiki/[concept-slug].md` | Always |
| Glossary | `knowledge/[CODE]-[SHORT]/wiki/glossary.md` | Always |
| Concept map | `knowledge/[CODE]-[SHORT]/wiki/concept-map.md` | Always |
| Obsidian vault stub | `knowledge/[CODE]-[SHORT]/wiki/.obsidian/app.json` | Always |
| Workbook | `knowledge/[CODE]-[SHORT]/workbook.ipynb` | Always (requires nbformat) |
| Flashcards | `knowledge/[CODE]-[SHORT]/flashcards.md` | When NLM available |
| Audio overview | `knowledge/[CODE]-[SHORT]/audio-overview.mp3` | When NLM available |
| Course Buddy skill | `knowledge/instances/[CODE]-[SHORT]/skill.md` | Always |
| CONTRIBUTING.md | `knowledge/[CODE]-[SHORT]/CONTRIBUTING.md` | Always |
| faculty-notes/README | `knowledge/[CODE]-[SHORT]/faculty-notes/README.md` | Always |
| student-contributions/README | `knowledge/[CODE]-[SHORT]/student-contributions/README.md` | Always |

---

## Constraint

**C2 — Free-tier compatible.**
The NotebookLM access uses `notebooklm-py` (unofficial Python client) with Google's free tier. No paid API key is required. Auth is done via browser cookie (one-time `notebooklm login`). Heavy usage may be rate-limited — use `--skip-notebooklm` for C1-compatible template-only output.

---

## Failure modes and mitigations

| Failure | Detection | Mitigation |
|---------|-----------|------------|
| NLM auth expired | `notebooklm-py` raises auth error | Run `notebooklm login` to refresh cookies |
| NLM rate limit | HTTP 429 response | Reduce batch size; retry after cooldown; or use `--skip-notebooklm` |
| Course descriptor parse error | YAML `safe_load` exception | Fix frontmatter syntax; validate with `python3 -c "import yaml; yaml.safe_load(open('descriptor.md').read().split('---')[1])"` |
| nbformat not installed | ImportError | `pip install nbformat`; workbook skipped gracefully |
| PDF source not found | File not found warning | Check path relative to course descriptor file |
| Mind map JSON malformed | JSON decode error | NLM mind map skipped; concept deps fall back to unit-order list |

---

## Integration with SKILL.md

The generated skill files are **student-facing** via the Course Buddy 01-10 routing in `SKILL.md`.

After running the builder for a course:
1. Copy (or symlink) `knowledge/instances/[CODE]-[SHORT]/skill.md` to `agents/course-buddyes/instances/course-buddy-NN.md` where NN is an available slot.
2. The SKILL.md Course Buddy routing block will load the wiki index from `knowledge/[CODE]-[SHORT]/wiki/index.md` as supplemental context when the student requests a session for that course.

The builder itself is **never triggered by a student session** — only by faculty or admin.

---

## Related files

| File | Role |
|------|------|
| [tools/course-buddy-builder/](../tools/course-buddy-builder/) | Implementation (Python scripts) |
| [tools/course-buddy-builder/templates/course-descriptor.md](../tools/course-buddy-builder/templates/course-descriptor.md) | Input template |
| [references/ai-tutor-philosophy.md](../references/ai-tutor-philosophy.md) | Governing philosophy |
| [knowledge/README.md](../knowledge/README.md) | Output folder conventions |
| [agents/course-buddyes/_course-buddy-instance-template.md](course-buddyes/_course-buddy-instance-template.md) | Skill template used by skill_generator.py |
| [eval/data/IMPROVEMENT-BACKLOG.md](../eval/data/IMPROVEMENT-BACKLOG.md) | F-9 gap source for refresh pipeline |
