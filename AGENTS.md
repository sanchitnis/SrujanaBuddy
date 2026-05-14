# Project Guidelines

## Code Style
- Prefer minimal, readable edits and preserve existing file structure and tone.
- Default to Markdown-first changes; most of this repository is specification and workflow docs, not executable code.
- Use **JSON or YAML** for structured data with repeating fields: module catalogs, question banks, configuration tables, pathway definitions, and any lookup structure a script will parse. Do not embed these as verbose Markdown lists when a structured format is cleaner.
- Embed `yaml` or `json` fenced code blocks within an `.md` file when data and prose must coexist in a single file. Use standalone `.yaml` / `.json` files when (a) the data exceeds ~15–20 repeating records, (b) it will be consumed by scripts, or (c) separating data from prose significantly aids clarity — then reference the data file from the companion `.md`.
- For `intake/apps/*.html`, keep the apps dependency-free and offline-capable (no network calls, inline CSS/JS in the same HTML file).
- When adding scripts, follow the standards in `CONTRIBUTING.md` (Python 3.10+ preferred, stdlib-first, safe defaults, idempotent behavior).

## Architecture
- `SKILL.md` is the always-loaded routing file (triggers, agent table, session routing, wellbeing thresholds, reference load map).
- `SKILL-context.md` is the companion coaching philosophy file (principles, output formats, guardrails). Load on demand when a session needs full context.
- `SKILL-legacy.md` is the legacy monolithic file — kept for reference but superseded by the core/context split.
- `agents/` contains the specialist coaching agent specifications.
- `references/` contains philosophical and framework foundations used by agents.
- `gtd/` contains the Markdown-native GTD operating system and task lists.
- `ai-delegation/` contains AI delegation specs and task queue templates.
- `intake/` and `profiles/` contain onboarding and mentee profile workflows.
- `connectors/` contains integration specifications (for example calendar audit).
- `tools/` contains standalone scripts and lightweight tools that augment the system (see Tools and Automation policy below).

## Session Initialization and Routing (Single-User Mode)

Each setup is for one individual only. **At every session start**, follow this sequence:

1. **Check for Profile** — scan the `profiles/` directory for any `.md` file that is not `README.md` or `_mentee-profile-template.md`.

2. **If a profile exists**:
   - Identify the mentee by the filename (e.g., `tushar-v.md` -> Tushar).
   - Load `SKILL.md` immediately.
   - Load the student's profile to check coaching context and last session notes.
   - **Greeting**: Start immediately with the name and a short summary of the last **coaching** session (ignore any developer/collaborator sessions): *"Namaste [Name]! Welcome back, da. Last time we [short summary of coaching goals/wins]. Where are we today?"*
   - Skip name request and proceed to **Route session** (Step 4).

3. **If NO profile exists**:
   - Load `SKILL.md` immediately.
   - **Greeting**: *"I am SrujanaBuddy, your AI coaching companion at REVA. This coaching is designed to help you progress toward your aspirations."*
   - Ask for name immediately: *"First things first — what's your name, da?"*
   - Once name is captured, create new profile from `profiles/_mentee-profile-template.md`.
   - Proceed directly to **Intake Protocol** (`intake/intake-protocol.md`).

4. **Route session** based on profile signals or intake progress.

5. **Load agent** specified in `SKILL.md` routing table.

6. **Apply tone and voice** — Bangalore English with Kannada flavour.

## Tools and Automation

Tools, scripts, and small programs are permitted and encouraged in this repository. All tools follow the **T0–T4 Technology Implementation Hierarchy** defined in [references/ai-tutor-philosophy.md](references/ai-tutor-philosophy.md) (Part 6). Summary:

| Tier | What it means | Key required? |
|------|--------------|---------------|
| **T0** | Deterministic — stdlib only, no model | No |
| **T1** | Agent skills — markdown-native, IDE-LLM | No |
| **T2** | Scripts without LLM — rule-based automation | No |
| **T3** | Local / Edge AI — Ollama or Google AI Edge Gallery | No (local) |
| **T4** | Free-tier cloud API — cron/background jobs only; Gemini Flash or Groq free tier | Optional |

**Preference order: T0 → T1 → T2 → T3 → T4.** Use the lowest tier that achieves the goal. T3/T4 keys are always optional — if absent, tools run at T2 level. Paid frontier API keys (OpenAI, Claude, Gemini Pro) are not in scope currently but could be implemented in future.

**In-scope tool categories**:
- Psychometric and self-assessment tools (offline HTML/JS preferred; see `intake/apps/` for the established pattern)
- Live data collectors: email/WhatsApp checking, calendar scraping, RSS/web fetch for opportunity radar
- Simple automation: sending a WhatsApp or email reminder, fetching a deadline, querying a public API
- Local model wrappers: scripts that route a coaching prompt to a local model and return structured output
- Eval runners: scripts that batch-run eval scenarios from `eval/scenarios/` against a local or free-tier model

**Out-of-scope** (do not add):
- Tools that require paid API keys to function at all
- Tools that make heavy batched calls to frontier models as their primary mechanism
- Tools that store or transmit real student PII to any external service

**Placement**: Put all tools in `tools/` with one subfolder per category. Each tool must have a `README.md` or inline header comment explaining: what it does, what it requires, how to run it, and which **tier (T0–T4)** it operates at. See `tools/README.md` for conventions.

## Build and Test
- There is no global build step for the core repository (content is primarily Markdown).
- For local app testing in this repo:
  - `cd intake/apps && python3 -m http.server 8080`
- Validate `SKILL.md` frontmatter before submitting structural changes:
  - `python3 -c "import yaml; c=open('SKILL.md').read(); yaml.safe_load(c.split('---')[1]); print('SKILL.md frontmatter: valid')"`

## Conventions
- Keep guidance aligned with REVA philosophy and Dr. Shyama Raju's vision; do not generalize away core domain intent.
- Prefer small, additive updates over broad rewrites.
- Use "link, don’t embed": point to existing docs instead of duplicating long guidance.
- High-value references for context:
  - Root overview: `README.md`
  - Contribution and developer workflow: `CONTRIBUTING.md`
  - GTD details: `gtd/GTD-GUIDE.md` and `gtd/README.md`
  - AI delegation details: `ai-delegation/AI-DELEGATION-GUIDE.md` and `ai-delegation/README.md`
  - Folder-specific conventions: each folder `README.md`
