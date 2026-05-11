# The SrujanaBuddy AI Tutor Philosophy

## Anchoring philosophy for AI-native knowledge wikis and workbooks

---

## Part 1 — The Original Manifesto (Allen B. Downey, 2010, updated 2016)

Source: [greenteapress.com/wp/textbook-manifesto](https://greenteapress.com/wp/textbook-manifesto/)

The core thesis is disarmingly simple:

> **Students should read and understand textbooks.**

Downey observes that the entire textbook ecosystem — authors chasing authority, publishers demanding coverage, professors wanting a course-in-a-box — conspires to produce books that no one actually reads. A 1000-page doorstop is not a learning tool. The remedy is the opposite of every current convention:

### Downey's Nine Principles

| # | Principle | What it means in practice |
|---|-----------|--------------------------|
| D1 | **Short** | 140 pages per semester (10 pages/week). Anything beyond that does not get read. |
| D2 | **Readable** | Written for actual students, not imaginary well-prepared ones from 50 years ago. |
| D3 | **Free** | No $300 textbook that students don't buy anyway. Free licensing so anyone can use, improve, fork. |
| D4 | **Concept-first** | Teach ideas, not just procedures. Students should understand *why*, not just *how*. |
| D5 | **Reading quizzes** | Short comprehension checks after each chapter force the author to notice when material is unclear. |
| D6 | **Fix the book when students fail** | If a few students misunderstand, blame the students. If most do, fix the book. |
| D7 | **No publisher required** | Distribution is solved. Authors write; platforms distribute. |
| D8 | **Opinions allowed** | A book with no personality is a book with no readers. Take positions. |
| D9 | **Iterative improvement** | Books are never finished. Treat them as living software: version, patch, improve. |

---

## Part 2 — The REVA AI-Era Extension

The original manifesto addresses the written textbook. At REVA University, we extend it to the AI era: a world where learning resources can be bidirectional, self-improving, multi-modal, and deeply connected to the student's own portfolio of evidence.

The REVA extension is built on Dr. Shyama Raju's directive: **"Educate to Enterprise"** — knowledge must not just be understood, it must become capability, and capability must become evidence, and evidence must become enterprise.

### The Six REVA Extensions

| # | Extension | What it adds beyond Downey |
|---|-----------|---------------------------|
| R1 | **Bidirectional** | Students are contributors, not just consumers. Every wiki page can receive student annotations, corrections, and examples. Faculty curate; students co-author. The book improves from the bottom up. |
| R2 | **Self-improving** | Evaluation feedback (domain gaps found during coaching eval) automatically flags sections for review. A failing student question is a failing wiki section. The Refresh pipeline closes this loop. |
| R3 | **Multi-level** | The same concept is presented at three levels: Beginner (plain language, analogy), Intermediate (formal definition, worked example), Advanced (edge cases, research connections). One wiki, three entry points. |
| R4 | **AI-native enrichment** | NotebookLM is a first-class step, not an afterthought. Audio overviews, flashcards, mind maps, quizzes, and study guides are generated programmatically and embedded in the wiki from day one. |
| R5 | **Evidence-linked** | Every concept in the wiki is tagged to at least one Srujana Pathway evidence type. Understanding alone does not count; evidence of application does. The workbook converts knowledge into portfolio-ready artefacts. |
| R6 | **Living document with provenance** | Every change is version-controlled. Contributions are attributed. The wiki tracks who added what, when, and why. A student contribution that enters the main wiki is itself a portfolio evidence item. |

---

## Part 3 — What This Means for the Knowledge Wiki and Workbook System

### The Knowledge Wiki (Obsidian-format Markdown)

- Short, readable pages — no page should require more than 15 minutes of uninterrupted reading.
- Every page has a `level:` tag (beginner / intermediate / advanced) in its YAML frontmatter.
- Wikilinks (`[[concept]]`) make the dependency graph navigable, not just linear.
- Every page embeds or links to the NotebookLM-generated artefact most relevant to it (flashcard, mind map node, quiz question).
- A `student-contributions/` subfolder accepts student additions without touching the generated base; faculty promote accepted contributions to the main wiki via pull request.
- A `faculty-notes/` subfolder accepts faculty annotations without modifying generated pages.

### The Workbook (Jupyter Notebook)

- One notebook per course, divided into units.
- Each unit: learning objective (markdown cell) → concept explanation (markdown) → worked example (code or text) → practice problem pulled from NotebookLM quiz JSON → student notes cell → evidence prompt ("What Srujana evidence does this generate? Where will you record it?")
- STEM courses: code cells are pre-stubbed with problem setup; student fills the solution.
- Non-STEM courses: markdown cells are pre-structured prompts; student fills analysis.
- The workbook is never static. The Refresh pipeline updates practice problems from new quiz generations.

### The Course Coach Skill (Socratic tutor)

- Generated from the course descriptor using the Socratic template.
- Pre-populated with the concept dependency map extracted from the NotebookLM mind map.
- Mastery tracker pre-filled from unit outcomes.
- The coach references wiki pages and workbook units during sessions — not just raw syllabus text.

---

## Part 4 — Contribution Ladder

| Level | Who | What they can do | How it enters the main wiki |
|-------|-----|------------------|-----------------------------|
| Student (observer) | Any enrolled student | Read, annotate in personal Obsidian vault | N/A |
| Student (contributor) | Any student | Add to `student-contributions/` subfolder | Faculty review → PR merge |
| Student (author) | Students whose contributions are merged | Named attribution on the wiki page | Automatic on merge |
| Faculty (annotator) | Course faculty | Add to `faculty-notes/` subfolder | Immediate (no review needed) |
| Faculty (editor) | Course owner | Edit main wiki pages directly | Direct commit |
| Builder (automated) | `build.py --refresh` | Regenerate AI-derived sections | Committed by the faculty running the refresh |

---

## Part 5 — Governing Principles (Summary)

1. If a student cannot understand a page in 15 minutes, the page is too long or too complex. Fix it.
2. If an eval session logs an F-9 domain gap for a concept, that concept's wiki page is flagged for refresh within one sprint.
3. Every piece of content must have a clear level (`beginner / intermediate / advanced`). Mixed-level pages must be split.
4. Audio, flashcard, and quiz artefacts are generated, not optional. They are part of the definition of "complete" for any course wiki.
5. A student's accepted wiki contribution is evidence. It must be linkable from their Srujana portfolio.
6. The wiki is never finished. There is no "v1.0 done" — only the current best state.

---

## Part 6 — Technology Implementation Hierarchy (System-wide)

This section governs technology choices across the **entire SrujanaBuddy system** — not only the Course Coach Builder, but every tool, script, app, and integration.

The guiding principle: **prefer the simplest tier that achieves the goal**. Move to a higher tier only when a lower tier genuinely cannot do the job.

### The Five Tiers

| Tier | Label | What it is | API key needed? |
|------|-------|------------|-----------------|
| T0 | **Deterministic** | Pure Python / JS / HTML, stdlib only, no model. Template filling, offline scoring, static HTML apps (`intake/apps/` pattern). | No |
| T1 | **Agent Skills** | Markdown-native Copilot skills — interactive coaching sessions, daily conversational use. No script involved; the LLM is the IDE. | No |
| T2 | **Scripts (no LLM)** | Rule-based automation — RSS fetch, calendar audit, gap extraction, file transforms. Deterministic output; no language model needed. | No |
| T3 | **Local / Edge AI** | Prompts needing language understanding — REVA-hosted LLM (when available) or a Gemma-class model running on a mobile phone (Google AI Edge Gallery) or laptop (Ollama). All T3 scripts read `LLM_ENDPOINT`; swap backends with zero code change. | No (local) |
| T4 | **Free-tier Cloud API** | Unattended background / cron jobs only — e.g., nightly wiki refresh, batch eval runs. Acceptable: Gemini Flash free tier, Groq free tier. Must include a stdlib daily quota guard (`.quota/daily.json`). Paid frontier keys (OpenAI paid, Claude, Gemini Pro) are not in scope currently but could be implemented in future. | Optional |

**Preference order: T0 → T1 → T2 → T3 → T4**

### "Optional" Means Reduced Mode, Not Failure

API keys (T4) and local model endpoints (T3) are always **optional**. If they are not configured, the tool operates at T2 level and logs `[reduced mode] LLM not configured — running without AI enrichment`. T0/T1/T2 always work with zero configuration.

Example: the opportunity radar at T2 surfaces raw RSS articles; at T3 it also summarises and ranks them by relevance to the student's Srujana pathway. Both modes are useful. A student should never see a hard error because a key is missing.

**Standard environment variables** (never hard-code these values):

| Variable | Purpose | Default |
|----------|---------|--------|
| `LLM_ENDPOINT` | Local model base URL | `http://localhost:11434` (Ollama standard) |
| `LLM_MODEL` | Local model name | `gemma3:4b` |
| `GEMINI_API_KEY` | Gemini Flash free-tier key | *(unset — optional)* |
| `GROQ_API_KEY` | Groq free-tier key | *(unset — optional)* |

### Six Design Rules

1. **Declare the tier** in every tool's `README.md` or inline header comment: `# Tier: T2`.
2. **T3/T4 tools degrade gracefully** to T2 via a `--skip-llm` flag or when no endpoint/key is found in the environment.
3. **No hard-coded model names or API keys** — always read from environment variables listed above.
4. **T4 cron tools must check a quota guard** before any API call — a stdlib JSON counter at `.quota/daily.json` is sufficient; no extra library needed.
5. **T3 mobile tools must document one-time setup** in their `README.md`: the app name, the model file to download, and estimated device requirements.
6. **No tool may require a paid API key to function at all** — if a design requires one, redesign the feature.

---

*This philosophy governs the design and maintenance of the entire SrujanaBuddy system — knowledge wikis, workbooks, coaching agents, intake apps, and automation scripts. See [tools/course-coach-builder/README.md](../tools/course-coach-builder/README.md) for the Course Coach Builder implementation.*
