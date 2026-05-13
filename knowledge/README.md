# knowledge — AI-Native Course Knowledge Base

## Purpose

This folder contains the generated knowledge artefacts for all courses processed by the
[Course Buddy Builder](../tools/course-buddy-builder/README.md).

Each course gets its own subfolder:

```
knowledge/
  [CourseCode]-[ShortName]/          e.g. CSE301-DSA/
    wiki/                            Obsidian-format knowledge wiki
      index.md                       Course overview, unit links, NLM audio embed
      [concept-slug].md              One page per key concept (3 levels: Beginner/Intermediate/Advanced)
      glossary.md                    All key terms
      concept-map.md                 Mermaid dependency graph + NLM mind map JSON
      .obsidian/app.json             Minimal Obsidian vault config (open folder as vault, no setup)
    workbook.ipynb                   Jupyter practice workbook (quiz exercises, evidence prompts)
    flashcards.md                    Markdown flashcards (from NotebookLM)
    audio-overview.mp3               NotebookLM audio overview podcast
    faculty-notes/                   Faculty annotations (no PR needed; do not edit generated base)
      README.md
    student-contributions/           Student-authored improvements (reviewed before merge)
      README.md
    CONTRIBUTING.md                  Contribution guide for this course
  instances/                         Generated Course Buddy skills (assign to agent slots 01-10)
    [CourseCode]-[ShortName]/
      skill.md
```

---

## Philosophy

This knowledge base is built on the [REVA AI Tutor Philosophy](../references/ai-tutor-philosophy.md):

- **Short and readable**: No concept page should require more than 15 minutes of reading.
- **Multi-level**: Every concept has Beginner / Intermediate / Advanced sections.
- **Bidirectional**: Students contribute; faculty curate. The wiki improves from the bottom up.
- **Self-improving**: Eval feedback (F-9 domain gaps) triggers targeted wiki refreshes.
- **Evidence-linked**: Every concept connects to Srujana portfolio evidence types.
- **Living**: There is no "v1.0 done" — only the current best state.

---

## How to use the wiki (students)

### Option A — In Obsidian (recommended)
1. Download [Obsidian](https://obsidian.md) (free desktop app, no account needed).
2. Open Obsidian → "Open folder as vault" → select `knowledge/[CourseCode]-[ShortName]/wiki/`.
3. Start at `index.md`. Navigate via wikilinks (`[[concept]]`).
4. The graph view shows concept dependencies visually.

### Option B — In any Markdown viewer
All pages are plain Markdown and render correctly in GitHub, VS Code, or any Markdown preview.
Wikilinks (`[[concept-slug]]`) will appear as bracketed text; follow them manually.

### Option C — In Jupyter (for the workbook)
```bash
pip install notebook
jupyter notebook knowledge/[CourseCode]-[ShortName]/workbook.ipynb
```

---

## How to use the workbook (students)

1. Open `workbook.ipynb` in Jupyter (or JupyterLab, or VS Code with the Jupyter extension).
2. Work through each unit section sequentially.
3. Read the concept overview, then attempt the exercise **before** reading the answer.
4. Fill in the "My Notes" cell after each exercise.
5. Complete the "Evidence Prompt" cell — note the completed exercise in your Srujana portfolio.

For STEM courses: code cells have a starter stub. Write your solution, run the cell, check your output.
For non-STEM courses: markdown cells have a structured prompt. Write your analysis directly in the cell.

---

## How to contribute (students)

1. Create a file in `knowledge/[CourseCode]-[ShortName]/student-contributions/` named `[concept-slug]-[your-reva-id].md`.
2. Include: your explanation, a worked example, and a note on what you found confusing and how you resolved it.
3. Open a pull request targeting `main`. The course faculty will review.
4. If accepted, your name is added to the concept page. This is Srujana Stage 2-3 evidence — add it to your portfolio.

---

## How to contribute (faculty)

### To add annotations without touching generated pages
Create files in `knowledge/[CourseCode]-[ShortName]/faculty-notes/` — no PR needed. Direct commit.
These appear in the wiki as supplemental context and do not affect the generated base.

### To edit a generated wiki page
Edit the Markdown file directly and commit. You are the course owner.

### To update AI-derived sections (study guide, quiz, flashcards, concept map, audio)
Run a refresh:
```bash
cd tools/course-buddy-builder
python3 build.py --course-file templates/[CourseCode]-descriptor.md \
                 --output-dir ../../knowledge/ \
                 --refresh
```

### To add a gap topic (from student confusion or eval feedback)
```bash
# Extract F-9 gap topics from eval backlog automatically:
GAP=$(python3 tools/course-buddy-builder/eval_bridge.py --course-code [CourseCode])

# Run refresh with those topics:
python3 tools/course-buddy-builder/build.py \
  --course-file templates/[CourseCode]-descriptor.md \
  --output-dir ../../knowledge/ \
  --refresh --gap-topics "$GAP"
```

---

## How to add a new course

1. Copy `tools/course-buddy-builder/templates/course-descriptor.md` to a new file named `[CourseCode]-descriptor.md` in the same folder.
2. Fill in all frontmatter fields and unit breakdown sections.
3. Run the builder:
   ```bash
   python3 tools/course-buddy-builder/build.py \
     --course-file tools/course-buddy-builder/templates/[CourseCode]-descriptor.md \
     --output-dir knowledge/
   ```
4. Assign the generated skill (`knowledge/instances/[CourseCode]-[ShortName]/skill.md`) to an available Course Buddy slot (`agents/course-buddyes/instances/course-buddy-NN.md`).

---

## Feedback loop: eval → refresh

When SrujanaBuddy logs an **F-9** (domain gap) failure for a course in the eval backlog,
the `eval_bridge.py` script extracts the gap topic and feeds it into the builder's refresh pipeline.
This closes the loop: a student question the coach couldn't answer well becomes enriched wiki content.

```
Student session → F-9 logged in IMPROVEMENT-BACKLOG → eval_bridge.py → build.py --refresh → updated wiki
```

---

## Related files

| File | Role |
|------|------|
| [references/ai-tutor-philosophy.md](../references/ai-tutor-philosophy.md) | Governing philosophy |
| [agents/course-buddy-builder.md](../agents/course-buddy-builder.md) | Builder agent spec (Build / Refresh / Audit modes) |
| [tools/course-buddy-builder/README.md](../tools/course-buddy-builder/README.md) | Tool documentation |
| [eval/data/IMPROVEMENT-BACKLOG.md](../eval/data/IMPROVEMENT-BACKLOG.md) | F-9 gap source |
| [agents/course-buddyes/](../agents/course-buddyes/) | Generated skill instance slots |
