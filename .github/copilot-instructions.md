# Copilot Instructions — SrujanaBuddy Repository

## Tone: Bangalore English with Kannada flavour

All student-facing coaching content in this repository uses **Bangalore English with Kannada flavour** as the default register. When generating or editing session scripts, prompts, check-in flows, challenge cards, onboarding dialogues, or any student-facing coaching text, apply this tone.

**Use naturally (not in every sentence):**
- English: "da", "yaar", "guru", "machcha", "no?", "only", "itself"
- Kannada flavour: "seri" (okay), "correct-aa?" (is that right?), "shuru maadu" (let's begin), "ond nimisha" (one moment), "thumba" (very/a lot), "hogbidi" (let it go)

**Peer energy, not teacher energy.** Short punchy sentences. Celebrate small wins loudly. Challenge with warmth.

**Switch to professional formal English for:** faculty escalation messages, institutional documents, YAML frontmatter, and philosophy reference files.

Full tone spec: [`SKILL-context.md`](../SKILL-context.md) → `## Tone and Voice`

## Repository purpose

SrujanaBuddy is a markdown-native AI coaching operating system for REVA University students. It is **not** a software codebase — most files are Markdown specs, YAML data, and coaching workflow documents.

- Do not suggest code refactors or linting fixes on `.md` files
- Do not add docstrings, comments, or type annotations unless asked
- Prefer small additive edits; preserve the existing structure and tone of each file
- For structured data (question banks, module catalogs, pathway tables), prefer YAML or JSON over verbose Markdown lists
- Follow the T0→T4 technology tier hierarchy defined in `references/ai-tutor-philosophy.md` for any tool or automation suggestions

## Key files
- `SKILL.md` — routing core (always-loaded)
- `SKILL-context.md` — coaching philosophy and tone (load on demand)
- `agents/` — specialist agent specs
- `profiles/` — student profiles (named `full-name.md`, hyphen-separated)
- `references/` — philosophy and framework foundations
