# eval — Testing, Evaluation, and Continuous Improvement

Primary audience: SrujanaBuddy core team, faculty mentors, and system contributors.

## Purpose

This folder provides the infrastructure to validate, test, and continuously improve SrujanaBuddy.
It is **internal infrastructure** — students do not interact with this folder directly.

Three activities happen here:

1. **Synthetic testing** — run test personas through stage scenarios to verify coaching quality before changes go live.
2. **Feedback collection** — gather anonymized observations from real students and faculty mentors to surface gaps and failures.
3. **Improvement governance** — log improvement tasks, triage them, and assign them to the right collaborators through the VC-chaired Improvement Board.

---

## Folder map

```
eval/
├── README.md                          ← this file
├── eval-agent.md                      ← agent spec for running eval sessions and audits
├── improvement-board.md               ← governance charter, meeting cadence, stakeholder roles
│
├── personas/
│   └── archetypes.md                  ← 4 student archetypes × 8 career paths; 12 sample personas
│
├── scenarios/
│   ├── stage-1-foundation.md          ← test scenarios for Stage 1 coaching validation
│   ├── stage-2-application.md         ← test scenarios for Stage 2 coaching validation
│   ├── stage-3-creation.md            ← test scenarios for Stage 3 coaching validation
│   └── stage-4-enterprise.md          ← test scenarios for Stage 4 (all 3 tracks)
│
├── feedback/
│   ├── student-feedback-template.md   ← anonymized feedback form for students (< 5 min)
│   └── mentor-feedback-template.md    ← feedback form for faculty and industry mentors
│
└── data/
    ├── eval-log-template.md           ← per-session quality log with pass/fail signal checklist
    └── IMPROVEMENT-BACKLOG.md         ← live log of improvement tasks raised from eval/feedback
```

---

## How to run a synthetic eval session

1. Choose a persona from [`personas/archetypes.md`](personas/archetypes.md).
2. Choose a scenario from the relevant stage file in [`scenarios/`](scenarios/).
3. Open a fresh SrujanaBuddy session. Paste the scenario's **Student Input** verbatim.
4. Evaluate the response against the **Quality Signals** listed in the scenario.
5. Fill in one row of [`data/eval-log-template.md`](data/eval-log-template.md).
6. If any quality signal fails, raise an improvement task in [`data/IMPROVEMENT-BACKLOG.md`](data/IMPROVEMENT-BACKLOG.md).

---

## How to process real feedback

1. A student or mentor completes the relevant form in [`feedback/`](feedback/).
2. A core team member reads the response, anonymizes any identifying details (replace names/roll numbers with generic IDs), and logs the relevant observation in [`data/IMPROVEMENT-BACKLOG.md`](data/IMPROVEMENT-BACKLOG.md).
3. The Improvement Board reviews all new backlog items at each quarterly session (see [`improvement-board.md`](improvement-board.md)).

---

## Governing principle

All evaluation data and all improvement decisions must be traceable to the same chain used in coaching:

> **Observation → Gap → Improvement Task → Action → Evidence of Resolution**

---

## Related files

| File | Role |
|------|------|
| [`references/srujana-pathway-framework.md`](../references/srujana-pathway-framework.md) | Defines the four stages that scenarios and personas are built around |
| [`SKILL.md`](../SKILL.md) | Master orchestration — the primary target of quality improvement |
| [`agents/README.md`](../agents/README.md) | Active agent roster — agents are also eval targets |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | How domain experts and community members submit improvements |
