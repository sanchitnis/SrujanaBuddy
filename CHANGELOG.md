# Changelog

All notable changes to the Hitaishin are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html):
- **Major** (x.0.0): Significant philosophical or architectural changes
- **Minor** (0.x.0): New agents, new connectors, new reference files
- **Patch** (0.0.x): Corrections, clarifications, small improvements

---

## [Unreleased] - 2026-05-07

### Added - REVA v1.4 migration foundations
- `references/reva-values-anchor.md` - REVA coaching value baseline and learning integrity checks.
- `references/srujana-pathway-framework.md` - Stage 1-4 pathway and evidence progression model.
- `references/student-year-group-modes.md` - Year-group routing defaults.
- `references/dopamine-stewardship-student.md` - Daily and weekly dopamine protocol.
- `references/gtd-lite-student-edition.md` - D-14, D-21, D-3 and no-zero-day policy.
- `agents/academic-learning-coach.md` - learning strategy specialist agent.
- `agents/course-coach-template.md` - dynamic course-coach template.
- `agents/assessment-competition-coach.md` - assessments and competitions specialist.
- `agents/career-pathway-coach.md` - multi-path career planning specialist.
- `agents/competency-portfolio-coach.md` - competency evidence mapping specialist.
- `agents/out-of-curriculum-coach.md` - optional track governance specialist.
- `agents/enterprising-skills-mentor.md` - enterprise and MVP coaching specialist.
- `agents/support-escalation-guide.md` - tiered support and referral specialist.
- `agents/faculty-mentor-coordination-agent.md` - mentor prep/debrief and share controls.
- `agents/academic-history-agent.md` - academic record history specialist.
- `agents/personal-website-builder-agent.md` - student website planning specialist.
- `gtd/03-runway-calendar.md` - student runway and red-zone tracker.
- `gtd/opportunity-radar.md` - rolling opportunities tracker.
- `connectors/manodhara-referral.md` - three-tier escalation and referral protocol.
- `intake/apps/04-growth-mindset.html` - offline mindset baseline app.
- `intake/apps/05-grit-perseverance.html` - offline grit baseline app.
- `intake/apps/06-study-habits.html` - offline study habits app.
- `intake/apps/07-time-management-procrastination.html` - offline procrastination profile app.
- `intake/apps/08-stress-energy-self-check.html` - offline stress-energy app.
- `intake/apps/09-career-interest-mapping.html` - offline career interest mapping app.
- `REVA-IMPLEMENTATION-TRACKER-v1.4.md` - migration progress tracker.
- `REVA-METRICS-TRACKER-v1.4.md` - success metrics tracking grid.

### Changed
- `SKILL.md` migrated to SrujanaBuddy identity, 15-agent routing, 24 session types, year-group modes, and REVA guardrails.
- `README.md` replaced with REVA product framing and migration status.
- `COACHING-SESSION-WORKFLOW.md` replaced with REVA 24-session operational workflow.
- `references/five-spheres-framework.md` replaced with Five Student Spheres framework.
- `references/daily-thread.md`, `references/weekly-rhythm.md`, `references/yearly-strategy.md` replaced with clean REVA-compatible rhythm docs.
- `references/README.md`, `agents/README.md`, `intake/README.md`, `gtd/README.md`, `connectors/README.md` updated for REVA artifact discovery.
- `intake/intake-protocol.md` extended with REVA student onboarding addendum.
- `profiles/_mentee-profile-template.md` extended with REVA student profile fields.
- `gtd/GTD-GUIDE.md` extended with REVA GTD Lite runway policy.
- `agents/accountability-partner.md`, `agents/integral-life-coach.md`, `agents/inner-mastery-coach.md` extended with REVA student-mode addendums.

---

## [2.0.0] — 2026-04

### Added — Coaching Lifecycle (Intake System)
- `intake/intake-protocol.md` — Complete 3-stage onboarding: Deep Interview (6 modules) → Psychometrics → Synthesis session
- `intake/apps/01-character-strengths.html` — 30-question VIA-adapted Character Strengths assessment with REVA values-aligned interpretations and Markdown export
- `intake/apps/02-spheres-assessment.html` — 50-question Five Spheres Balance Wheel with radar chart visualisation and Integral Balance Score (see REVA-STUDENT-SYSTEM-SPEC for Panchakosha rewrite roadmap)
- `intake/apps/03-leadership-oa-profile.html` — 40-question Organizational Attitude profile with Saboteur identification and REVA-specific antidotes
- `profiles/_mentee-profile-template.md` — Comprehensive living mentee document: psychometrics → sessions → breakthroughs → coaching hypothesis

### Added — GTD Task Management System
- `gtd/GTD-GUIDE.md` — Complete GTD framework adapted for REVA student context with Panchakosha tagging, Sankalpa alignment, and AI delegation layer
- `gtd/00-inbox.md` — Capture inbox template
- `gtd/01-next-actions.md` — Sphere-organised next actions with full tag system
- `gtd/02-projects.md` — Multi-step project index with Sankalpa traceability
- `gtd/04-waiting-for.md` — Delegated items tracker including AI agent queue
- `gtd/05-someday.md` — Deferred aspirations organised by sphere
- `gtd/07-weekly-review.md` — Integrated GTD + Svadhyaya weekly review template
- `gtd/projects/_project-template.md` — Full project file template with phase planning, AI delegation, and reflection log

### Added — AI Delegation Architecture
- `ai-delegation/AI-DELEGATION-GUIDE.md` — Master guide: philosophy, Human-AI division of labour, decision matrix, ethical principles
- `ai-delegation/agent-research.md` — Research Agent: structured brief format, output template, quality log, active task queue
- `ai-delegation/agent-drafting.md` — Drafting Agent: five content templates, voice calibration notes, active task queue
- `ai-delegation/agent-planning.md` — Planning Agent: project plan + weekly time-block output templates
- `ai-delegation/agent-inbox-review.md` — Inbox Agent + Review Agent: batch processing, pattern detection, coaching session prep

### Added — Documentation (GitHub Open Source)
- `README.md` — Project landing page with Quick Start for all three audiences, repository map, philosophical foundation, roadmap
- `references/README.md` — Domain expert guide: what to review, contribution style guide, glossary of 20 key terms
- `agents/README.md` — Coaching methodology guide: ICF alignment check, REVA authenticity review, how to add new agents
- `intake/README.md` — Three-audience guide: users (getting started), domain experts (reviewing), developers (extending apps)
- `profiles/README.md` — User and coach guide: creating profiles, privacy, version control, `.gitignore` setup
- `gtd/README.md` — User and developer guide: GTD basics, REVA student adaptations, Obsidian integration, programmatic parsing
- `ai-delegation/README.md` — Developer guide: current architecture, Phase 1–4 roadmap, Claude API integration examples, Supabase schema, ethical architecture
- `connectors/README.md` — Developer guide: connector file structure, 5 connectors roadmap with MCP details, privacy considerations
- `CONTRIBUTING.md` — Contribution guide for all three audiences with PR checklists, branch naming, script template
- `LICENSE` — MIT with frameworks attribution and psychometric disclaimer
- `.gitignore` — Personal data protection for profiles and GTD personal files
- `CHANGELOG.md` — This file

### Updated — SKILL.md
- Added 4 new session types: Intake & Onboarding, GTD Processing Session, AI Delegation Session, Coach-Initiated Task Injection
- Added Complete File Index table covering all 33 files across all folders

---

## [1.0.0] — 2026-04

### Added — Initial Release
- `SKILL.md` — Master intelligence layer with 7 session types and 6-agent routing
- `references/reva-values-anchor.md` — REVA philosophical foundation: Panchakosha model, Gita Perspective (Dr. Shyama Raju), Universal Values, USR/Jagruti, Educate to Enterprise
- `references/five-spheres-framework.md` — Panchakosha holistic development model with Purusharthas mapping
- `references/daily-thread.md` — Five-zone 24-hour rhythm with Brahma Muhurta protocol and Minimum Viable Day
- `references/weekly-rhythm.md` — Seven-day Svadhyaya architecture with full Sunday review protocol
- `references/yearly-strategy.md` — Two-day Annual Vision Retreat template
- `references/modern-coaching-frameworks.md` — ICF, PERMA, VIA, Heifetz, Frankl, Kegan, Chamine with REVA alignment notes
- `references/spg-contribution-tracker.md` — Adult SPG: selection framework, health assessment, India's priority domains
- `agents/svadharma-navigator.md` — Purpose, calling, VIA strengths integration, three-phase coaching protocol
- `agents/integral-life-coach.md` — Five-sphere balance, time audit, Aurobindo's Integral Yoga applied
- `agents/organizational-attitude-builder.md` — Vivekananda's five Organizational Attitude components, Heifetz adaptive leadership overlay
- `agents/inner-mastery-coach.md` — Mood diagnosis, Saboteur scan, Frankl meaning scan, five inner mastery practices
- `agents/paristhiti-jnana-analyst.md` — Four-layer situational reading, India's macro context, strategic response protocol
- `agents/accountability-partner.md` — Weekly check-in protocol, Sankalpa honoured rate, WOOP framework, CLEAR delegation
- `connectors/calendar-audit.md` — Google Calendar Five-Sphere time audit, meeting quality classification, Organizational Attitude meeting check

---

## Versioning Notes

**What triggers a Major version bump:**
- Fundamental change to the Panchakosha holistic development model
- New primary philosophical tradition added to the foundation
- Complete redesign of the agent architecture
- Breaking changes to GTD file formats (requiring migration)

**What triggers a Minor version bump:**
- New coaching agent added
- New psychometric app added
- New connector added
- Significant new reference file
- New folder/area of functionality

**What triggers a Patch version bump:**
- Corrections to philosophical claims
- Improved coaching questions
- Clarifications in any file
- Bug fixes in HTML apps
- Documentation improvements
