## Protocol Analysis for Human Coaches

This document summarizes the implemented coaching protocol in SrujanaBuddy for three major threads and maps dependencies across agents, references, and skills.

Sources reviewed:
- SKILL.md
- SKILL-context.md
- AGENTS.md
- intake/intake-protocol.md
- eval/personas/archetypes.md
- Agent specifications in agents/

---

## 1. Three Main Threads and Their Implemented Protocols

### Thread 1: Aspirations Discovery, Progressive Refinement, and Milestone Planning (3-4 year horizon)

The system follows a progressive, living-artefact model rather than a one-time goal capture.

#### A. Intake initializes two core artefacts
1. Living profile: profiles/<name>.md
2. Aspirations north star: profiles/<name>-aspirations.yaml

Defined in:
- SKILL.md (Aspirations North Star Rule)
- intake/intake-protocol.md (Goal and direction setting)

#### B. Aspirations are explicitly iterative
1. First draft is allowed to be partial at intake.
2. Refinement is planned in session 2 and periodic reviews.
3. Aspirations and coaching context are reviewed every 30-60 days.

Defined in:
- SKILL.md
- intake/intake-protocol.md

#### C. Planning follows Srujana Stage progression
1. Stage 1: Foundation
2. Stage 2: Application
3. Stage 3: Creation
4. Stage 4: Enterprise

Readiness is evidence-based, not semester-gated.

Defined in:
- references/srujana-pathway-framework.md

#### D. Milestones are operationalized across time scales
1. 4-week pathway actions from Career and Pathway Coach.
2. Weekly and daily commitments from STM (Saptahika, Dainika, Tatkala).
3. Project decomposition from multi-week project to weekly milestone to daily action.

Defined in:
- agents/career-pathway-coach.md
- .agents/skills/drive-with-gps/SKILL.md
- drive-with-gps/STM-GUIDE.md

#### E. Soft skills and enterprising skills are integrated, not separate add-ons
1. Inner self-regulation and values-aligned decision support.
2. Enterprising coaching: problem clarity, validation, MVP rhythm, pivot/persist.
3. Portfolio evidence mapping to competency and stage.

Defined in:
- agents/inner-mastery-coach.md
- agents/enterprising-skills-mentor.md
- agents/competency-portfolio-coach.md

#### F. Visual continuity protocol for aspiration sessions
The Aspiration Horizon map is shown at the beginning and end of aspiration-relevant sessions.

Defined in:
- SKILL.md (Aspiration Horizon Map rule)
- agents/aspiration-horizon-agent.md

---

### Thread 2: Curriculum Learning (Socratic) + Out-of-curriculum Learning

This thread is designed around learning integrity and non-spoon-feeding.

#### A. Core Socratic protocol
1. Probe before answer.
2. Diagnose misconceptions.
3. Sequence: What -> Why -> How -> What If.
4. End with student summary and one practice problem.

Defined in:
- agents/course-buddy-template.md

#### B. Learning strategy protocol
1. Diagnose learning method.
2. Separate technical vs adaptive obstacles.
3. Build retrieval-first plan.
4. Convert into daily and weekly actions.
5. Require explain-back after AI-assisted work.

Defined in:
- agents/academic-learning-coach.md
- SKILL-context.md (Attempt -> Assist -> Augment -> Automate)

#### C. Assessment and competition runway protocol
1. Deadline and risk mapping.
2. D-21 and D-14 preparation runway.
3. High-weight concept targeting.
4. Performance simulation and debrief.

Defined in:
- agents/assessment-competition-coach.md

#### D. Out-of-curriculum support with overload guardrails
1. Protect core academics first.
2. Choose one primary and up to two secondary optional tracks.
3. Weekly overload checks.
4. Optional load reduction first on conflict.

Defined in:
- agents/out-of-curriculum-coach.md

---

### Thread 3: First-level Counseling Support + Escalation to Manodhara / Emergency

The system uses a strict triage-and-bridge model.

#### A. Three-tier triage model
1. Tier 1: Coaching-level stress and motivation issues.
2. Tier 2: Stabilization / inner-state support.
3. Tier 3: Crisis / emergency referral.

Defined in:
- SKILL.md
- agents/support-escalation-guide.md
- connectors/manodhara-referral.md

#### B. Trigger conditions
1. Energy <= 5 for 2+ sessions -> Tier 2 consideration.
2. Energy <= 3 or red-flag indicators -> Tier 3 escalation.
3. Red flags include self-harm ideation, safety threats, severe functional collapse, etc.

Defined in:
- SKILL.md
- agents/wellness-triage-agent.md
- agents/accountability-partner.md

#### C. Crisis protocol implementation
1. Verbatim scripts for crisis and stabilization.
2. Referral to Dr. Anand Siddaiah via SLCM (Manodhara).
3. Emergency numbers included.

Defined in:
- agents/wellness-crisis-scripts.md
- connectors/manodhara-referral.md

#### D. Hard safety boundaries
1. No diagnosis.
2. No therapy imitation.
3. Safety-first routing.
4. Human-in-the-loop mandatory for Tier 3.

Defined in:
- agents/support-escalation-guide.md
- agents/wellness-triage-agent.md

---

## 2. Adaptive Flow by Student Category (Personas)

Persona model source:
- eval/personas/archetypes.md

The system expects differentiated coaching flows by archetype and condition.

### A. Achiever
1. High agency + high clarity.
2. Needs pace, specificity, stretch, and blind-spot balancing.
3. Avoid over-basic coaching.

### B. Explorer
1. High agency + low clarity.
2. Needs hypothesis testing, reversible choices, and breadth-friendly evidence capture.
3. Avoid forced early specialization.

### C. Passenger
1. Low agency + low clarity.
2. Needs small immediate actions, confidence rebuilding, and short-horizon accountability.
3. Avoid heavy plans or Stage 2/3 overload.

### D. Resistor
1. Resistance to imposed framing; includes values-driven, trapped, and burned variants.
2. Needs trust-first, meaning-first, subtype-specific intervention.
3. Avoid generic placement-track forcing.

### Cross-cutting condition signals used for adaptation
1. Energy baseline
2. Overwhelm
3. Clarity state
4. Work style preference
5. Show-up consistency / readiness

Defined in:
- SKILL.md (Coaching Context Rule)
- intake/intake-protocol.md

---

## 3. Dependency Analysis Across Current Agents

### A. Orchestration dependency
Primary routing hub:
- SKILL.md

Supporting philosophy and guardrails:
- SKILL-context.md

### B. Shared data dependencies
Most coaching flows depend on:
1. profiles/<name>.md (living profile + context)
2. profiles/<name>-aspirations.yaml (north-star progression)
3. Session evidence and commitment history

### C. Functional dependency clusters

#### 1) Intake and initialization cluster
- .agents/skills/getting-started/SKILL.md
- intake/intake-protocol.md
- profiles template
- handoff to srujana-presence-agent

#### 2) Aspiration progression cluster
- career-pathway-coach
- aspiration-horizon-agent
- competency-portfolio-coach
- srujana-pathway-framework reference

#### 3) Learning mastery cluster
- academic-learning-coach
- course-buddy-template
- assessment-competition-coach
- course knowledge instances (when built)

#### 4) Execution and habit cluster
- accountability-partner
- STM skill and stm workspace files
- integral-life and inner-mastery for deeper regulation

#### 5) Wellbeing safety cluster
- support-escalation-guide
- wellness-triage-agent
- wellness-crisis-scripts
- manodhara-referral connector

#### 6) Presence and evidencing cluster
- srujana-presence-agent
- aspiration-horizon-agent
- competency-portfolio-coach
- academic-history-agent

---

## 4. Candidate Segregation into Independent Agent Skills

The current design can be modularized further without breaking behavior.

### Candidate Skill A: Aspiration Lifecycle Skill
Bundle:
1. Intake aspiration capture
2. Pathway fit and stage placement
3. Horizon map rendering and updates
4. Stage evidence linking

Source files:
- intake/intake-protocol.md
- agents/career-pathway-coach.md
- agents/aspiration-horizon-agent.md
- agents/competency-portfolio-coach.md
- references/srujana-pathway-framework.md

### Candidate Skill B: Socratic Learning Skill
Bundle:
1. Learning diagnosis
2. Socratic tutoring logic
3. Retrieval-first planning
4. Assessment runway

Source files:
- agents/academic-learning-coach.md
- agents/course-buddy-template.md
- agents/assessment-competition-coach.md

### Candidate Skill C: Wellbeing Triage Skill
Bundle:
1. Distress detection
2. Tier classification
3. Stabilization scripts
4. Referral execution

Source files:
- agents/support-escalation-guide.md
- agents/wellness-triage-agent.md
- agents/wellness-crisis-scripts.md
- connectors/manodhara-referral.md

### Candidate Skill D: Presence and Portfolio Evidence Skill
Bundle:
1. Resume and website scaffold
2. Consent and privacy controls
3. Evidence-linking and updates

Source files:
- agents/srujana-presence-agent.md
- agents/competency-portfolio-coach.md
- agents/academic-history-agent.md

### Candidate Skill E: Mentor Coordination Skill
Bundle:
1. Share-level selection
2. Sensitive masking defaults
3. Preview approval loop
4. Meeting debrief and action owners

Source files:
- agents/faculty-mentor-coordination-agent.md

---

## 5. Observed Consistency and Maintenance Risks

### Risk 1: Duplicate routing drift
The removed .agents/skills/srujanabuddy copy previously duplicated orchestration and could drift from SKILL.md.

Current recommendation:
1. Keep SKILL.md as sole orchestration truth.
2. Keep skill stubs minimal and pointer-only where needed.

### Risk 2: Session label/version drift across docs
When routing names change (example: GTD rescue vs Sankalpa reset), all mirrored docs and eval scenarios should be synchronized.

Current recommendation:
1. Add a routing checksum checklist in release updates.
2. Include SKILL.md alignment as a review gate.

### Risk 3: Course-buddy instance dependency maturity
Subject-level Socratic quality depends on whether course instances and knowledge wikis exist for that course.

Current recommendation:
1. Explicitly track course-buddy coverage by department.
2. Route fallback to academic-learning-coach where instance is absent.

---

## 6. Coach-facing Summary: How Coaching Evolves Over Time

The implemented protocol behaves like an adaptive state machine:

State inputs:
1. Persona archetype (Achiever/Explorer/Passenger/Resistor)
2. Energy and overwhelm
3. Clarity and readiness
4. Current Srujana stage
5. Recent evidence and completion patterns

Routing outputs:
1. Session type and primary agent(s)
2. Intensity and pacing calibration
3. Safety tier
4. Commitment scope (daily/weekly/monthly)

Required session outputs (system-wide contract):
1. Next immediate action
2. Time-bound commitment
3. Checkpoint with evidence marker

In practice:
1. Aspirations are progressively clarified, not forced.
2. Learning is Socratic and integrity-protected.
3. Wellbeing is triaged safely with clear referral boundaries.
4. Execution rhythm translates long-term aspiration into daily behavior.

This is aligned with your requirement that protocol must vary by student condition and evolve through coaching, rather than applying one static script.
