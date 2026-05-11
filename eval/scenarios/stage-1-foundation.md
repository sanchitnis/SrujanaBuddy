# Stage 1 — Foundation: Test Scenarios

## How to use

Run each scenario by pasting the **Student Input** verbatim into a fresh SrujanaBuddy session.
Evaluate the response against the **Quality Signals**. Mark each as PASS / FAIL / PARTIAL.
Log results in [`eval/data/eval-log-template.md`](../data/eval-log-template.md).

---

## S1-01: Passenger / Management — First session, no aspiration

**Persona**: Persona 3 — Divya (Passenger / CP-8 Management-Consulting)
**Stage**: 1 — Foundation

**Student Input**:
> My professor said I should talk to you. I don't really know why I'm here. I guess I need to figure out what to do after college.

**Expected coaching behaviors**:
1. Does NOT immediately offer a plan or career path.
2. Opens with a gentle exploratory question about what Divya enjoys or finds interesting.
3. Does not mention Stage 2 or portfolio immediately — that is premature.
4. Produces one small, non-threatening next action (e.g., "let's find one thing you enjoyed this week").
5. Keeps the commitment local and short ("by tomorrow" or "by this weekend").
6. Does not compare Divya to peers or to stage expectations.

**Quality signals**:
- [ ] No premature career prescription in the first response
- [ ] At least one open question asked before any advice offered
- [ ] Next action is genuinely achievable for a Passenger within 48 hours
- [ ] No mention of placement, package, or peer comparison
- [ ] Session ends with one evidence artifact named (however small)
- [ ] Checkpoint date is within 1 week

**Common failure modes**:
- F-2: Responding as if Divya is an Achiever — launching into a structured career planning framework
- F-4: Producing a coaching output with a next action Divya has no realistic chance of completing
- F-7: Pushing toward Stage 2 (internship readiness) in session 1

---

## S1-02: Achiever / AI-Technology — Foundation completeness check

**Persona**: Arya (Achiever / CP-1 AI-Technology), but assessed at Stage 1 entry by the coach
**Stage**: 1 — Foundation

**Student Input**:
> I'm in first year BTech CSE. I want to work in AI. I've already started learning Python on my own. I know about machine learning basics from YouTube. What should I do next?

**Expected coaching behaviors**:
1. Acknowledges the self-learning already happening — names it as evidence.
2. Checks depth (not just exposure): asks what she has actually built or practised, not just watched.
3. Does not skip to Stage 2 (internship) without confirming Stage 1 competency.
4. Gives a stretch but realistic next action (e.g., a specific small project, not "do an internship").
5. Links to the AI engineering pathway selector or the foundation stage of a relevant pathway.
6. Evidence artifact is concrete: a project, a notebook, a submission.

**Quality signals**:
- [ ] Self-learning is acknowledged as real evidence
- [ ] Depth-check question asked before prescribing next steps
- [ ] No internship push in Year 1 without Stage 1 milestone confirmed
- [ ] Pathway selector or pathway module referenced (from `references/ai-engineer-pathways.md`)
- [ ] Next action has a specific output, not just "keep learning"
- [ ] Checkpoint within 2 weeks

**Common failure modes**:
- F-1: Treating her as Stage 2-ready when Stage 1 foundation is still being built
- F-9: Generic Python advice not connected to an AI pathway module
- F-6: Slowing her down with excessive caution when she is clearly ready for the next step

---

## S1-03: Explorer / Civil Services — Direction uncertainty at Stage 1

**Persona**: Persona 6 — Sameer (Explorer / CP-5 Civil Services-Policy)
**Stage**: 1 — Foundation

**Student Input**:
> I want to become an IAS officer. But I don't know where to start. There's so much to study. I also like debating and I've joined the debate club. Is all of this useful?

**Expected coaching behaviors**:
1. Validates the aspiration (IAS) without immediately asking him to commit permanently to it.
2. Names the debate club as genuine Stage 1 evidence (communication, argumentation).
3. Reduces the overwhelm by scoping: one study area to begin with, not a complete UPSC plan.
4. Does not give a full 2-year preparation timeline in session 1.
5. Helps him frame his current activity (debates, reading newspapers) as a working hypothesis.
6. Next action is small, specific, and tests the aspiration without requiring full commitment.

**Quality signals**:
- [ ] Aspiration validated without demanding permanence
- [ ] Debate club named as existing Stage 1 evidence
- [ ] Overwhelm addressed explicitly — scope narrowed, not expanded
- [ ] No complete 2-year plan produced in session 1
- [ ] Next action tests the aspiration (e.g., "read and summarise one editorial this week")
- [ ] Door left open to revisit the aspiration if it changes

**Common failure modes**:
- F-2: Treating an Explorer like an Achiever — producing a complete UPSC preparation roadmap immediately
- F-3: Ignoring the debate club evidence and focusing only on study
- F-7: Setting a month-long commitment in session 1 with a Passenger-prone student

---

## S1-04: Resistor / Social Enterprise — System skepticism at Stage 1

**Persona**: Persona 12 — Deepak (Resistor / CP-6 Social Enterprise)
**Stage**: 1 — Foundation

**Student Input**:
> I don't really believe in this coaching stuff. I know what I want to do — I want to work in rural education. But everyone just talks about placements and packages. I'm not here for that.

**Expected coaching behaviors**:
1. Validates the pushback immediately — does NOT defend the system or argue.
2. Asks about his vision for rural education — gets curious before giving anything.
3. Does not use placement, industry, or package language in this session.
4. Connects "Educate to Enterprise" to social enterprise and rural impact — not commercial startup.
5. Names what he already knows or has done as real Stage 1 evidence.
6. Produces one next action that honors his actual direction, not a standard career coaching action.

**Quality signals**:
- [ ] No defense of the institutional coaching system in the first response
- [ ] Exploratory question about his vision asked before any advice
- [ ] Zero placement/package/industry language in the response
- [ ] "Educate to Enterprise" reframed toward social contribution
- [ ] His existing knowledge or experience named as evidence
- [ ] Next action is toward his stated direction, not toward standard Stage 1 activities

**Common failure modes**:
- F-3: Ignoring his stated values and defaulting to a standard Stage 1 action plan
- F-5: Implicitly devaluing rural education as a career path
- F-2: Treating him as a Passenger (low agency) rather than a Resistor (different agenda)

---

## S1-05: Passenger / Health Sciences — Academic survival at Stage 1

**Persona**: Persona 10 — Rahul (Passenger / CP-7 Health Sciences)
**Stage**: 1 — Foundation

**Student Input**:
> I just need to pass my exams. I'm struggling with pharmacology. Can you help me study?

**Expected coaching behaviors**:
1. Starts with the stated need (pharmacology, exam readiness) — does NOT redirect immediately to career.
2. Uses retrieval-first learning protocol (Academic Learning Coach pattern): identify gaps, build practice blocks, not just re-reading.
3. Does not push optional or Stage 2+ activities in this session.
4. One small additional action (not mandatory) offered at the end — shadowing a ward round, reading one case study — as an invitation, not a requirement.
5. Commitment is low-bar and academic: specific study session for pharmacology, not a career plan.

**Quality signals**:
- [ ] Session opens with the stated need (pharmacology) not a career question
- [ ] Retrieval-first or active recall method suggested (not "read the textbook again")
- [ ] No Stage 2+ push in this session
- [ ] Optional extra action offered as invitation, not instruction
- [ ] Commitment is realistic: one study block, one practice test
- [ ] Checkpoint within 48 hours (Passenger needs short loops)

**Common failure modes**:
- F-7: Pushing Rahul toward research or extracurricular activities when he needs academic support
- F-2: Treating him like an Achiever with a career planning response instead of a study plan
- F-6: Over-caution that produces no useful study method — only encouragement
