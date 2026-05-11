# Getting Started

SrujanaBuddy can be used in three ways based on the technology surface you need.

## 1) Core coaching system (Markdown-first)

Use this when you want the main coaching behavior (`SKILL.md`, `agents/`, `references/`, `gtd/`).

```bash
git clone https://github.com/<owner>/SrujanaBuddy.git
cd SrujanaBuddy
```

Then load `SKILL.md` into your AI environment and start with prompts like:
- `Plan my day`
- `Run weekly review`
- `Help me prepare for exams`

No build step is required for core usage.

## 2) Intake apps (offline HTML apps)

Use this for psychometric/onboarding apps in `intake/apps/`.

Option A: Open any file directly in a browser:
- `intake/apps/01-character-strengths.html`
- `intake/apps/02-spheres-assessment.html`
- ... and so on

Option B: Run a local static server:

```bash
cd intake\apps
python -m http.server 8080
```

Then open `http://localhost:8080`.

## 3) Subject coach builder (Python toolchain)

Use this to generate course knowledge artifacts under `knowledge/`.

```bash
cd tools\subject-coach-builder
pip install -r requirements.txt
notebooklm login
python build.py --course-file templates/course-descriptor.md --output-dir ..\..\knowledge\
```

Notes:
- Requires Python 3.10+.
- `notebooklm login` is needed only for NotebookLM-backed generation.
- For template-only generation (no NotebookLM API calls), add `--skip-notebooklm`.
