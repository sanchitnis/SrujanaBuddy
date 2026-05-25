# Contributing to SrujanaBuddy

First, thank you. This project exists to serve REVA University students, and every improvement makes a genuine difference to the people who use it.

This guide is for all three types of contributors. Read the section that applies to you.

---

## Before You Contribute

### Understand the spirit

This is not a generic productivity tool with Indian branding. Every design decision flows from the specific context of REVA students: their aspirations, the Educate to Enterprise vision of Dr. P. Shyama Raju, the Panchakosha model of holistic development, and the Brahmacharya Ashrama stage of disciplined learning and preparation for life.

**Before suggesting any change, ask**: Does this serve REVA students in the Educate to Enterprise vision, or am I generalising for a broader audience? (Both are valid, but they're different projects.)

### Ground rules

1. **Philosophical accuracy matters more than coaching elegance.** A technically sophisticated coaching question that misrepresents Advaita or the Organizational Attitude framework does more harm than good.

2. **The user's dignity is non-negotiable.** Nothing in this system should make a student feel inadequate for not having an active optional contribution pathway or a perfect daily practice. The coaching is demanding but never shaming.

3. **Less is more.** The temptation in coaching systems is to add more questions, more frameworks, more agents. Resist. A smaller system that is deeply used is better than a comprehensive one that overwhelms.

4. **Credit sources.** If you adapt from Kegan, Heifetz, Seligman, or any other framework — say so. Intellectual honesty is a REVA Universal Value (Ethics pillar).

---

## For Domain Experts

### What counts as domain expertise here

- REVA faculty, staff, mentors, and students with deep familiarity with REVA's pedagogy and Dr. Shyama Raju's vision
- Professional coaches (ICF-credentialed preferred — PCC or above)
- Scholars of Advaita Vedanta, the Bhagavad Gita, or related Indian traditions (Vivekananda, Aurobindo)
- Positive psychologists, organisational behaviourists, or leadership researchers with relevant expertise

### How to contribute as a domain expert

**Option 1: Open a GitHub Issue**

The lowest-friction way to contribute. Label your issue with one of:
- `philosophy-accuracy` — something is philosophically incorrect or misleading
- `coaching-methodology` — a coaching protocol needs improvement
- `reva-authenticity` — something doesn't align with REVA's philosophy or Dr. Shyama Raju's vision
- `missing-content` — an important domain, concept, or framework is absent
- `enhancement` — something correct that could be made richer

Describe:
- What the current content says
- What is inaccurate or missing
- What it should say instead (with your reasoning and any sources)

**Option 2: Submit a Pull Request**

If you want to write the improvement directly:

1. Fork the repository
2. Create a branch: `git checkout -b domain/[brief-description]`
3. Make your changes — **only to files in** `references/`, `agents/`, or `intake/intake-protocol.md`
4. Add a comment at the top of any changed section explaining your rationale
5. Submit a PR with label `domain-review`

**Pull Request checklist for domain contributions**:
- [ ] Changes are philosophically grounded (cite source if possible)
- [ ] Language is accessible to any REVA student or faculty member
- [ ] Nothing has been removed without explanation
- [ ] REVA philosophical terminology is used accurately (see Glossary in `references/README.md`)
- [ ] Changes tested by asking Claude to coach using the modified file


### Editorial and Design Principles for Skills and Guardrails

#### Skill/Guardrail Separation

Every agent or skill in this repository must encode its core behavior directly in its `SKILL.md` file. Shared guardrails (philosophy, safety, or practice profile) live in the orchestrator or agent-level context files. **If a skill's correct output depends on a guardrail catching a mistake the skill would have made, that's a design smell.**

**Rule of thumb:** If a test passes only because a guardrail fired, add the behavior to the skill directly. Guardrails are the safety net, not the primary scaffold.

**Examples:**
- If a coaching skill covers a domain (e.g., career planning), it must handle all relevant sub-cases (e.g., entrepreneurship, research, placements) in its own checklist or logic, not rely on a global override.
- If a date or calculation must be business-day aware, encode the rule in the skill, not just in a shared fallback.

#### Provenance and Tagging

Attach provenance tags or citations to key numbers, formulas, or decisions—not just to paragraphs. E.g., `[source: Gita 2.47]` next to a principle, or `[verify: REVA policy]` on a load-bearing rule. Tags on surrounding prose get lost; tags on the critical item do not.

#### Decline Pathways

If the right answer to a category of question is "I decline to answer/compute," bake that into the skill as a hard gate. State the gate plainly, make it default-on, and narrow any exemptions in sub-bullets—not the other way around.

#### Workflow Discipline

- **Read the orchestrator and agent context files before editing any skill.** The practice profile, integrations, and shared guardrails shape what the skill should say and omit.
- **Bump the version on material changes.** Patch bumps for behavior additions; minor bumps for new skills or required inputs.
- **Run all validators and linters before submitting.**
- **Do not remove shared guardrails.** The net stays; the goal is a skill that doesn't need the net, not a system without one.

### The editorial process for philosophical changes

Any change to `references/REVA University.md`, `references/reva-values-anchor.md`, or to the core frameworks in `references/five-spheres-framework.md` goes through a two-reviewer process before merging. This protects the philosophical integrity of the system.

Reviewers are drawn from a standing panel of REVA faculty, mentors, and credentialed coaches. If you'd like to be on the review panel, open an Issue with label `reviewer-volunteer`.

---

## For General Users (REVA Students and Faculty)

You don't need to know how to code to contribute meaningfully.

### Share your experience

The most valuable contributions from users are:
- "This coaching question landed exactly right — here's why"
- "This framing of Svadharma doesn't align with REVA's Gita perspective or Dr. Shyama Raju's vision"
- "I needed coaching on [topic] and the system didn't have it"
- "This psychometric question doesn't make sense in an Indian student context"

Open a GitHub Issue with label `user-experience`. You don't need technical details — just describe what happened and what would have been more useful.

### Share a session transcript (with consent)

If you've had a particularly valuable or revealing coaching session, consider sharing a lightly anonymised transcript as an Issue or Discussion. These become invaluable for improving the agents' coaching protocols.

### Suggest Powerful Questions

Each agent has a **Powerful Questions Library**. If you've been asked (by a coach, a mentor, or in a REVA coaching context) a question that really shifted your thinking — share it as an Issue with label `powerful-question`. Include:
- The question
- The context it was asked in
- What made it powerful

---

## For Developers

### Repository setup

```bash
# Clone
git clone https://github.com/sanchitnis/srujanabuddy.git
cd srujanabuddy

# No build step required for the core skill (all Markdown)
# For the psychometric apps:
cd intake/apps
open 01-character-strengths.html  # macOS
# or
python3 -m http.server 8080       # then visit localhost:8080
```

### Branch naming conventions

| Type | Format | Example |
|------|--------|---------|
| New feature | `feature/[description]` | `feature/gmail-connector` |
| Bug fix | `fix/[description]` | `fix/sphere-scoring-normalisation` |
| Domain content | `domain/[description]` | `domain/ramdas-dasabodha-depth` |
| Documentation | `docs/[description]` | `docs/developer-setup-guide` |
| Scripts | `scripts/[description]` | `scripts/gtd-weekly-summary` |

### Where developers can contribute

**High priority:**

| Area | Description | Skills needed |
|------|-------------|---------------|
| `scripts/` (new folder) | GTD automation scripts | Python or Node.js |
| `intake/apps/` | Psychometric app improvements | Vanilla JS, HTML/CSS |
| `connectors/` | New MCP connector specs + testing | Claude API, MCP |
| CI/CD | GitHub Actions to validate SKILL.md frontmatter | YAML, Actions |

**Medium priority:**

| Area | Description |
|------|-------------|
| Obsidian plugin | Native GTD dashboard for Obsidian users |
| Mobile web app | Responsive companion app for GTD + Sankalpa tracking |
| API integration | Claude API wrapper for autonomous agent runs |
| Supabase schema | Database schema for multi-mentee coaching practices |

### Adding scripts

Scripts belong in a new `scripts/` folder (not yet created). Create it with your first PR.

Conventions for scripts:
- **Language**: Python 3.10+ preferred; Node.js 18+ acceptable; bash for simple utilities
- **No external dependencies** unless absolutely necessary (prefer stdlib)
- **Documented inputs/outputs** in the script's docstring or leading comment
- **Safe defaults**: scripts that modify GTD files must create backups first
- **Idempotent**: running twice should not corrupt data

Script template:
```python
#!/usr/bin/env python3
"""
[Script name] — [One-line description]

Usage:
    python3 scripts/[name].py [--args]

Inputs:
    - gtd/00-inbox.md (reads)
    
Outputs:
    - gtd/01-next-actions.md (appends)
    - Console summary

Dependencies: None (stdlib only)

Part of: SrujanaBuddy
License: MIT
"""

import argparse
import shutil
from pathlib import Path
from datetime import date

GTD_DIR = Path(__file__).parent.parent / "gtd"

def backup_file(filepath: Path) -> Path:
    """Create a timestamped backup before modifying any GTD file."""
    backup = filepath.with_suffix(f".{date.today().isoformat()}.bak")
    shutil.copy2(filepath, backup)
    return backup

def main():
    # ... implementation
    pass

if __name__ == "__main__":
    main()
```

### Improving the psychometric apps

The three HTML apps in `intake/apps/` are intentionally dependency-free. Keep them that way.

When modifying:
- Test in Chrome, Firefox, and Safari before submitting
- Verify the clipboard export still produces valid Markdown
- Don't add any network calls (the apps must work completely offline)
- Keep all CSS within the `<style>` tag, all JS within `<script>`

### Validating SKILL.md

The `SKILL.md` file's YAML frontmatter must be valid. A GitHub Action (to be added) will validate this automatically. Until then, validate manually:

```bash
python3 -c "
import yaml, sys
with open('SKILL.md') as f:
    content = f.read()
# Extract frontmatter between --- delimiters
fm = content.split('---')[1]
yaml.safe_load(fm)
print('SKILL.md frontmatter: valid')
"
```

### Pull Request checklist for code contributions

- [ ] No breaking changes to existing file formats (GTD, agent files, profile template)
- [ ] New scripts have docstrings and usage examples
- [ ] HTML apps tested in Chrome + Firefox
- [ ] No new external dependencies introduced without discussion
- [ ] README for the affected folder updated
- [ ] `SKILL.md` agent roster / file index updated if new files added

---

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) v2.1.

Additionally, given the community this serves:
- Respect the philosophical traditions referenced — engage with them seriously, not as cultural decoration
- Disagreements about philosophical interpretation are welcome as Issues, not in PR comments
- REVA serves students across many streams and backgrounds; contributions should be accessible across that diversity

---

## Recognition

All contributors are acknowledged in the project's [CONTRIBUTORS.md](CONTRIBUTORS.md) file.

Domain experts who make significant philosophical contributions will be listed with their credentials and area of expertise (with their consent).

---

## Questions?

Open a GitHub Discussion (not an Issue) for open-ended questions about the project's direction, design philosophy, or how to approach a contribution you're considering.

*Sada Saavdhan* — always alert, always engaged.
