# GCS Enterprising Ability Analytics Framework

> **For coaches, faculty, and students to understand how Srujana Stage 3 (Creation) progress is tracked, scored, and celebrated.**

---

## Overview

The GCS Enterprising Ability analytics system measures student progress along **six dimensions** that directly map to Stage 3 (Creation) competencies and the five Growth & Grit rubric categories. The goal is to make invisible learning visible — through both individual profile tracking and optional public leaderboards.

**Not measured**: Academic grades, attendance, or output polish.  
**Measured**: How well each student learns to innovate, pivot, validate, collaborate, and reflect under real-world constraints.

---

## Six Analytics Dimensions

### 1. Rubric Mastery (0–100 scale)

Each of the five Growth & Grit rubrics progresses through three levels: **Novice → Intermediate → Advanced**.

| Rubric | Novice | Intermediate | Advanced |
|--------|--------|--------------|----------|
| **Evidence of Pivot** | Tried once, failed | Multiple attempts; some reason logged | Pivot sequence with clear data-driven logic |
| **Investigation Depth** | Googled, asked friends | 3–7 interviews; 5–8 sources | 10+ interviews; rich user patterns; contradictions explored |
| **Collaboration** | Attended meetings | Gave/received feedback; minor conflict handled | Resolved real team conflict; elevated teammate idea; learned from criticism |
| **Final Prototype** | Wireframe or sketch | Core logic works; half-demo-able | Fully testable; users can run it independently |
| **Reflection** | "I learned a lot" | Named skill + personal observation | Meta-reflection on own thinking; connected to Srujana journey |

**Score calculation**: 
- Let $n$ = number of rubrics at Advanced, $m$ = number at Intermediate
- Rubric Mastery = $\frac{(n \times 3) + (m \times 1.5)}{5 \times 3} \times 100$ = percentage

**Example**: 2 at Advanced, 2 at Intermediate, 1 at Novice  
$(2 \times 3 + 2 \times 1.5 + 1 \times 0) / 15 = 9 / 15 = 60\%$

---

### 2. Sprint Progress (0–100 scale)

Each week (1–14) is a milestone. A student completes a week when:
- Evidence is logged (sprint log updated)
- Effort signal ≥ 6/10
- Commitment for next week is set

**Score**: $\frac{\text{weeks completed}}{14} \times 100$

**Example**: Week 8 completed, on track  
$8 / 14 = 57\%$

---

### 3. Consistency (0–100 scale)

Anti-drift metric. On-time session means: no 7+ day gap between coaching sessions; effort signal logged; session note captured.

**Score**: $\frac{\text{on-time sessions}}{\text{total sessions}} \times 100$

**Example**: 11 on-time, 1 session had a 10-day gap (still happened, but flagged)  
$11 / 12 = 92\%$

---

### 4. Evidence Quality (0–100 scale)

Diversity and depth of artifacts logged in the sprint log and investigation/pivot logs.

**Artifact types** (max 10):
1. User interview (transcribed or notes)
2. Prototype demo (screenshot, link, or video)
3. Pivot log entry (documented reason)
4. Data analysis or research
5. Design doc (UML, wireframe, spec)
6. Code or technical implementation
7. User testing result (feedback, session notes)
8. Feedback from mentor or peer
9. Market research or competitive analysis
10. Reflection entry or lesson learned

**Score**: $\frac{\text{artifact types logged}}{10} \times 100$

**Example**: 7 types logged (interview, demo, pivot, design doc, code, feedback, reflection)  
$7 / 10 = 70\%$

---

### 5. E2E Integration (0–100 scale)

Depth of synergy with the four linked courses: Advanced C Programming, Software Design, IoT, Innovation & Entrepreneurship.

**Depth scale per course**:
- **Low**: Mentioned or thought about; no deliverable
- **Medium**: One concrete artifact or implementation (e.g., one C function written, UML diagram drawn)
- **High**: Synergy is core to project (e.g., full data structure in C, design drives architecture, IoT is central to product, business model written)

**Score**: $\frac{\text{(# courses at High)} \times 3 + \text{(# courses at Medium)} \times 1.5}{\text{4 courses} \times 3} \times 100$

**Example**: C Programming (High), Software Design (High), IoT (Low), I&E (Medium)  
$(2 \times 3 + 1 \times 1.5) / 12 = 7.5 / 12 = 62.5\%$

---

### 6. Team Collaboration (0–100 scale)

LCC observations logged: Leadership, Communication, Collaboration signals captured each week.

**Score**: $\frac{\text{LCC entries logged}}{14} \times 100$ (by Week 14)

**Interim** (e.g., Week 8): $\frac{\text{LCC entries}}{8} \times 100$

**Example**: Week 8, 6 LCC entries logged  
$6 / 8 = 75\%$

---

## Enterprising Ability Score (Composite)

**Weighted average of all six dimensions:**

$$\text{Enterprising Ability} = (0.25 \times \text{Rubric Mastery}) + (0.20 \times \text{Sprint Progress}) + (0.15 \times \text{Consistency}) + (0.15 \times \text{Evidence Quality}) + (0.15 \times \text{E2E Integration}) + (0.10 \times \text{Team Collaboration})$$

**Range**: 0–100  
**Updated**: Weekly, after each coaching session

**Example calculation** (Week 8):
- Rubric Mastery: 60%
- Sprint Progress: 57%
- Consistency: 92%
- Evidence Quality: 70%
- E2E Integration: 62.5%
- Team Collaboration: 75%

$$\text{Score} = (0.25 \times 60) + (0.20 \times 57) + (0.15 \times 92) + (0.15 \times 70) + (0.15 \times 62.5) + (0.10 \times 75)$$
$$= 15 + 11.4 + 13.8 + 10.5 + 9.375 + 7.5 = 67.6$$

---

## Engagement Intensity Modifiers

Students can opt into higher engagement levels. This changes the leaderboard multiplier (not the score itself, but visibility):

| Intensity | Definition | Leaderboard multiplier |
|-----------|-----------|----------------------|
| **Solo Studio** | Student works; coach supports as needed | 1.0× |
| **Team Studio** | Multi-person team; coach tracks intra-team dynamics | 1.0× |
| **Mentored Studio** | Faculty or peer mentor involved | 1.0× |
| **Bold Studio** | Student picks a scary Bold Bet; coach checks in 2x/week | 1.5× |

**Effect**: A Bold Studio student with score 60 is visible as "60 × 1.5 = 90 in intensity-adjusted rank" for leaderboard purposes (optional feature; defaults to raw scores).

---

## Narrative Arcs and Chapters

Students pick one of four roles at Week 1. As they progress, they unlock narrative chapters:

| Chapter | Week | Arc narrative |
|---------|------|---------------|
| Chapter 1: Discovery | 2 | "I found a problem. I talked to people." |
| Chapter 2: Hypothesis | 4 | "I think I know how to solve it." |
| Chapter 3: First Test | 7 | "I built something and tested it. It worked / didn't." |
| Chapter 4: Pivot or Confirm | 10 | "I learned [X]. Changing course / staying the course." |
| Chapter 5: Resolution | 14 | "Here's what I built. Here's what I learned." |

Students see this narrative in their profile alongside scores. It makes abstract progress concrete and memorable.

---

## Badge System

Five core badges (one per rubric). Badges unlock when a rubric reaches **Advanced** level.

| Badge | Rubric | Unlock criteria | Icon |
|-------|--------|-----------------|------|
| Pivot Master | Evidence of Pivot | 2+ documented pivots with clear logic | 🔄 |
| Deep Diver | Investigation Depth | 10+ interviews / 6+ data sources | 📚 |
| Team Hero | Collaboration | Resolved one real conflict + elevated teammate idea | 🤝 |
| Builder | Final Prototype | Fully working demo; user can use independently | 📦 |
| Sage | Reflection | Meta-reflection; connects learning to personal growth | 🧠 |

**Display**: Shown in student profile and leaderboards (if public). Celebrated in chat when unlocked ("🔄 Badge: Pivot Master").

---

## Leaderboard Categories

Eight separate leaderboards celebrate different strengths. Each student can appear in multiple. No single "rank #1".

1. **Investigation Masters** — interview count + depth
2. **Pivot Artists** — pivots + clarity of logic
3. **Collaboration Heroes** — conflict resolved + feedback quality
4. **Builders** — prototype completeness + user testability
5. **Reflection Sages** — depth of metacognition
6. **Speed Demons** — velocity (weeks completed / time elapsed) + consistent effort
7. **Consistency Champions** — on-time sessions (≥90% required)
8. **Bold Bets Achieved** — all students who shipped their Bold Bet (any rank)

**Participation**: Optional. Default is private profile; students must consent to appear on public leaderboards.

---

## Srujana Stage Mapping

### GCS = Minimum Stage 3 Gateway

Every student who completes GCS (Week 14 with Effort ≥ 6 average) demonstrates **Stage 3 (Creation)** competency:
- Problem validated through user research
- Prototype built and tested
- Iteration based on feedback
- Reflection on learning

**Profile mark**: Srujana Stage = "3-creation" (in their profile)

### Stage 3 → Stage 4 Signal

Students showing these signals qualify for **Stage 4 (Enterprise)** consideration:
- Bold Bet achieved (MVP users, real traction, or validated market signal)
- 3+ rubrics at Advanced (suggesting readiness for higher complexity)
- E2E integration at High across 3+ courses (suggesting systems thinking)
- Reflection shows evidence of enterprise mindset ("How do I scale this?", "What's the market play?")

**Profile mark** (if observed): Srujana Stage = "3-creation → 4-venture" (potential).

Faculty mentors can review these students for **Stage 4 venture track** or **research publication track** (via references/srujana-pathway-framework.md).

---

## Coach Integration

### Weekly Coaching Loop Update

During step 10 (Gamification nudge), the coach:
1. Reviews student's profile → `## GCS Gamification Analytics`
2. Calculates or observes latest rubric levels
3. Celebrates any badge unlocks
4. Nudges lagging rubrics: *"Investigation is still Novice — let's push it this week"*
5. Updates all six scores and Enterprising Ability composite
6. Logs any narrative chapter unlocks
7. Flags if Bold Bet ambition has quietly shrunk

### After Session

Coach updates profile with:
- Week completed (yes/no)
- Effort signal (1–10)
- Rubric levels for this week (if changed)
- Any new evidence artifacts (interview count, pivot logged, etc.)
- Consistency streak (if unbroken)
- LCC observations (one per week, rotated)

All data lands in the student's `## GCS Gamification Analytics` section.

---

## Faculty Mentor View (Optional Future)

If a student consents to mentor sharing, faculty can see a **simplified dashboard**:

```
Student: [Name] | Week: 8/14 | Enterprising Ability: 68/100

Rubric Mastery (pentagon):
- Evidence of Pivot: ●●◯ (Intermediate)
- Investigation Depth: ●●● (Advanced)
- Collaboration: ●●◯ (Intermediate)
- Final Prototype: ●●◯ (Intermediate)
- Reflection: ●◯◯ (Novice)

Sprint Progress: ████████░░░░░░ (57%)
Consistency: ██████████████░░ (92%)

Key blocker: [From latest session]
Next milestone: [From sprint log]
Recommended mentor action: [Coach note]
```

---

## System-Level Leaderboard Management

**Location**: `eval/leaderboards/gcs-enterprising-ability.md`  
**Frequency**: Updated every Friday evening  
**Data source**: Student profiles (`profiles/[full-name].md` → `## GCS Gamification Analytics`)  

**Weekly update checklist**:
- [ ] Extract data from all student profiles (those with consent)
- [ ] Recalculate all six dimensions
- [ ] Rank students in each of 8 leaderboard categories
- [ ] Identify new badge unlocks; celebrate them
- [ ] Flag students reaching Stage 4 signals for faculty review
- [ ] Commit changes; notify students of new badges/achievements
- [ ] Archive previous week's snapshot (optional, for trend analysis)

---

## Privacy and Consent Model

### Tiers

1. **Private Profile** (default)
   - Only student sees their profile
   - Coach sees during sessions
   - No data on public leaderboard

2. **Mentor Share** (opt-in)
   - Student consents → data goes to faculty mentor
   - Mentor can see Rubric Mastery, collaboration moves, Bold Bet status
   - Useful for faculty to guide Stages 3→4 progression

3. **Public Leaderboard** (opt-in)
   - Student consents → anonymized entry on leaderboard
   - Can choose to show real name (or stay Anon-XXX)
   - Celebrates achievement publicly

### Workflow

**Session**: *"Your rubric just reached Advanced — that's a badge! Want to show this on the public leaderboard, or keep it private for now?"*

Student decides anytime; can change consent in their profile `## GCS Gamification Analytics → Public Leaderboard Consent`.

---

## Measuring Success

By end of semester, the system succeeds if:

1. ✅ **Rubric progression visible**: All 5 rubrics tracked; most students reach Intermediate in ≥2 rubrics; some reach Advanced
2. ✅ **Sprints completed**: ≥80% of students complete Week 14 with effort ≥6
3. ✅ **Investigation depth**: Average interview count ≥8 per team; rich diversity of sources
4. ✅ **Pivots captured**: ≥50% of students show 1+ documented pivot with logic
5. ✅ **Team signals strong**: Collaboration entries logged consistently; conflicts surfaced and resolved constructively
6. ✅ **Prototype quality**: ≥70% of students can demo something functional to a real user by Week 14
7. ✅ **Leaderboard celebrated**: ≥40% of students opt-in to public sharing; celebrate different achievement types (not just top 1)
8. ✅ **Stage 4 signals emerging**: ≥5% of students show Stage 4 (Enterprise) readiness; flagged for venture or research track
9. ✅ **Reflection depth**: By Week 14, ≥60% of students show genuine metacognition and learning transfer
10. ✅ **Engagement sustained**: Consistency ≥80% on average; minimal mid-semester dropoff

---

## Troubleshooting

| Issue | Root cause | Fix |
|-------|-----------|-----|
| Rubric stuck at Novice after Week 8 | Student hasn't attempted to improve; coach asking surface-level questions | Inject tactical suggestion; coach deeper probe next session |
| Consistency drops suddenly | Student hit blocker or personal emergency | Run Recovery Sprint; escalate to faculty if 2 consecutive weeks low |
| No pivots documented | Student hasn't failed or tested; all planning, no execution | Challenge them with a fail-fast activity; reframe "pivot" as learning |
| E2E integration zero | Student didn't connect GCS to other courses | E2E prompt each week; give concrete example linking current sprint to C programming / Design |
| Low reflection quality | Student rushes close-of-session reflection | Slow down session end; ask follow-up: *"But what does that teach you about yourself?"* |
| No one opting into leaderboard | Students nervous about comparison | Start with anonymous option; celebrate first badge; show that categories are diverse (not just "best") |

---

## Appendix: Analytics Profile Template

This is what gets filled in `profiles/[full-name].md → ## GCS Gamification Analytics`:

```yaml
gcs_stage: 3-creation  # or 3-creation → 4-venture if Stage 4 signals show
current_week: 8
enterprising_ability_score: 68

rubric_mastery:
  evidence_of_pivot: intermediate
  investigation_depth: advanced
  collaboration: intermediate
  final_prototype: intermediate
  reflection: novice
  mastery_count: 1  # number at advanced

sprint_level: 8
weeks_completed: [1, 2, 3, 4, 5, 6, 7, 8]
on_track: true

engagement:
  intensity: team-studio
  total_sessions: 9
  on_time_sessions: 8
  consistency_score: 89%

evidence_artifacts:
  count: 7
  types_logged: [interview, demo, pivot, design, code, feedback, reflection]

e2e_integrations:
  adv_c: medium
  software_design: high
  iot: low
  innovation_ie: medium
  total_score: 62.5%

narrative:
  role: the-founder
  chapter: chapter-3
  story: "Tested hypothesis with 8 users; found core assumption wrong; pivoting"

badges:
  - pivot-master
  - deep-diver-progress (7/10 interviews)

mentor_share_consent: true
public_leaderboard_consent: false
```

