# placements-and-internships

Optional placements and internships support plugin for SrujanaBuddy.

## Tier

**Tier: T2** — rule-based automation, no LLM required.

## Constraint

**C1 — No AI API calls.**

## Requirements

- Python 3.10+
- No extra pip packages

## Why this is a plugin

- It is **not required** for the core SrujanaBuddy install or launch flow.
- It lives in its own folder with its own manifest and entrypoint.
- Users who do not need placements/internships support can ignore it completely.

## How to run

From the repository root:

```bash
python3 tools/live-data/placements-and-internships/placements_and_internships.py --category placement --tag engineering
```

Show internships only:

```bash
python3 tools/live-data/placements-and-internships/placements_and_internships.py --category internship
```

JSON output for further processing:

```bash
python3 tools/live-data/placements-and-internships/placements_and_internships.py --format json --limit 5
```

## Container usage

No extra installation is required inside the container beyond Python itself:

```bash
docker run --rm -v "$PWD":/workspace -w /workspace python:3.12-slim \
  python tools/live-data/placements-and-internships/placements_and_internships.py --category internship --tag engineering
```

If the repository is mounted elsewhere, pass `--repo-root /path/to/repo` or set `SRUJANABUDDY_REPO_ROOT`.

## Data sources

- `knowledge/internship-portals.json`
- `knowledge/placement-portals.json`
- `docs/placements-and-internships-guidance.md`
