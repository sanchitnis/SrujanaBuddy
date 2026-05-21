# agents - Specialist Coaching Layer

Primary audience: coaching designers and reviewers.

## Purpose

Each file in this folder defines one specialist coaching role used by the orchestrator.
The master routing logic in SKILL.md selects one or more agents per session type.

## Active roster (REVA v1.4)

| Agent file | Domain |
|-----------|--------|
| academic-learning-coach.md | Learning strategy and mastery |
| course-buddy-template.md | Course-specific Socratic tutoring template |
| assessment-competition-coach.md | Exams, vivas, competitions, hackathons |
| drive-with-gps.md | Goal Plan Sankalpa — GPS map, commitment tracking, Sankalpa execution |
| inner-mastery-coach.md | Emotional regulation and soft-skill growth |
| integral-life-coach.md | Sphere balance and values alignment |
| career-pathway-coach.md | Multi-path career planning and placement readiness |
| competency-portfolio-coach.md | Competency evidence and portfolio mapping |
| out-of-curriculum-coach.md | Optional tracks with overload control |
| enterprising-skills-mentor.md | Venture readiness and MVP execution |
| support-escalation-guide.md | Triage, escalation, and referral routing |
| faculty-mentor-coordination-agent.md | Mentor preparation, debrief, and share packets |
| academic-history-agent.md | Achievement and record history maintenance |
| srujana-presence-agent.md | Personal website and resume with digital presence scaffolding |
| aspiration-horizon-agent.md | Visual Pathway Map — aspirational horizon view; displayed at start and end of career, aspiration, and review sessions |
| organizational-attitude-builder.md | Leadership behavior and team contribution |

## Eval and improvement infrastructure

The following agent is internal infrastructure used by the core team, not by students in coaching sessions.

| Agent file | Domain |
|-----------|--------|
| [../eval/eval-agent.md](../eval/eval-agent.md) | Persona simulation, session audit, feedback synthesis, improvement backlog |
| [course-buddy-builder.md](course-buddy-builder.md) | Build, refresh, and audit AI-native knowledge wikis and workbooks per course (faculty-facing; not student-facing) |

See [`eval/README.md`](../eval/README.md) for the full evaluation and continuous improvement framework.

## Agent output contract

Every agent-guided session should end with:
1. Next action now.
2. Time-bound commitment.
3. Checkpoint and evidence marker.

## Safety and quality expectations

1. Ask before advice.
2. Distinguish technical from adaptive issues.
3. Keep core academics protected in trade-offs.
4. Enforce learning integrity for AI-assisted work.
5. Do not provide clinical diagnosis.
