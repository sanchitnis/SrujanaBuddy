# tools — Lightweight Scripts and Automation

Primary audience: contributors, faculty mentors, and technically inclined students.

## Purpose

This folder contains standalone scripts, small programs, and lightweight tools that augment SrujanaBuddy without requiring frontier AI model access. The core coaching system is Markdown-native and AI-agnostic. Tools in this folder extend it with useful automation — collecting live information, running psychometric assessments, sending reminders, or running eval scenarios against local models.

---

## Tool Constraints Policy

Every tool in this folder must satisfy **at least one** of the following:

| Constraint | What it means |
|-----------|--------------|
| **C1 — No AI API calls** | The tool does its job with no calls to paid or rate-limited AI APIs |
| **C2 — Free-tier compatible** | If it calls an AI API, it works fully within the free tier (Gemini Flash free, Groq free, etc.) and degrades gracefully when rate-limited |
| **C3 — Local model compatible** | Designed to work with an on-device model (Google AI Edge Gallery, Ollama, llama.cpp, or equivalent) — no external API required |

A tool that requires a paid API key to function at all does **not** belong in this folder.

---

## Folder structure (by category)

```
tools/
├── README.md                         ← this file
│
├── psychometric/                     ← self-assessment and psychometric tools (offline-first)
│   └── (see intake/apps/ for the established HTML/JS pattern)
│
├── live-data/                        ← tools that fetch live information from the outside world
│   └── (e.g. email check, WhatsApp status, calendar fetch, opportunity radar scraper)
│
├── messaging/                        ← tools that send or check messages on behalf of the student
│   └── (e.g. WhatsApp reminder sender, email digest, deadline alert)
│
├── eval-runner/                      ← tools that batch-run eval scenarios against a model
│   └── (e.g. run eval/scenarios/*.md prompts against a local Gemma model; produce a quality report)
│
└── local-model/                      ← wrappers and helpers for on-device model inference
    └── (e.g. Ollama prompt wrapper, AI Edge Gallery integration helper)
```

---

## How to add a tool

1. Choose or create the right subfolder (see categories above).
2. Write the tool. Follow the standards in [`CONTRIBUTING.md`](../CONTRIBUTING.md): Python 3.10+ preferred, stdlib-first, safe defaults, idempotent behavior.
3. At the top of every tool file, include a header comment with:
   - **What it does** (one sentence)
   - **Constraint satisfied** (C1 / C2 / C3 — at least one)
   - **Requirements** (Python version, any pip packages, any API keys needed and where to get them)
   - **How to run** (exact command)
   - **Example output** (a short sample)
4. If the tool is an HTML/JS offline app, follow the `intake/apps/` pattern: dependency-free, inline CSS/JS, no network calls.
5. If the tool sends messages or accesses accounts, include a `--dry-run` flag that prints what would be sent without sending it.

---

## In-scope tool categories (examples)

| Category | Examples |
|---------|---------|
| Psychometric / self-assessment | Character strengths quiz, sphere balance self-rating, Srujana stage self-assessment |
| Live data collection | Opportunity radar: fetch internship deadlines from REVA portal or Internshala; fetch exam dates; check email for mentor replies |
| Messaging | Send a WhatsApp reminder for a coaching checkpoint; send an email digest of this week's GTD actions |
| Eval runner | Batch-run `eval/scenarios/*.md` prompts against a local Gemma model; output a quality report with pass/fail per scenario |
| Local model wrapper | Wrap a Ollama or AI Edge Gallery call to a coaching prompt; return a structured coaching output for manual review |

---

## Out-of-scope (do not add here)

- Tools that require a paid API key to function at all
- Tools that batch-call frontier models as their primary mechanism
- Tools that store or transmit real student PII to any external service
- Scripts that modify any file outside the `tools/` folder without an explicit `--write` flag and user confirmation

---

## Related

| File | Relationship |
|------|-------------|
| [`intake/apps/`](../intake/apps/) | Established pattern for offline HTML/JS psychometric tools |
| [`eval/`](../eval/) | The eval framework that eval-runner tools target |
| [`connectors/`](../connectors/) | Integration *specifications* (prose); `tools/` is where the actual implementations go |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Code standards that all tools must follow |
| [`AGENTS.md`](../AGENTS.md) | Tools and Automation policy (the authoritative constraint definition) |
