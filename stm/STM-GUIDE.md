# STM — Sankalpa and Time Management
## Ancient Wisdom + Modern Habit Science for REVA Students

> Skill file: [`.agents/skills/stm/SKILL.md`](../.agents/skills/stm/SKILL.md)

---

## What is a Sankalpa?

In Vedic tradition, **sankalpa** (संकल्प) is more than a goal. It is a sacred commitment — a vow of will and intention that you make to yourself *right now*, with the intention to complete it. The word comes from *sam* (complete, aligned) + *kalpa* (rule, intention): a fully aligned, wholehearted intention.

> "A goal is something you want. A sankalpa is something you commit to completing — starting now."

Crucially: **completing even the smallest task is a fulfilled sankalpa.** Every finished commitment — no matter how tiny — is a kept vow. This is why atomic habits work: the habit is not the action, it is the identity being built through kept commitments.

---

## The STM Core Loop

```
Morning Ritual (5 min)
  → Set 1 Dainika + 2 Tiny Sankalpas
      → Execute (Tatkala: < 2 min = do NOW)
          → Evening Check: Complete? ✅
              → Update Streak
                  → Archive + Celebrate
                      → Weekly Svadhyaya
```

---

## Three Tiers of Sankalpa

### Tier 1 — Tatkala (तत्काल): Instant Sankalpa
**When:** Right now. A task appears and takes less than 2 minutes.  
**Rule:** Do not write it. Do not schedule it. Complete it immediately.  
**Why it matters:** The 2-minute rule (Atomic Habits) builds the neural pathway of *starting and completing*. The Tatkala sankalpa is the atomic unit of commitment culture.

Examples:
- Reply to a WhatsApp message from a professor
- Write one line in your notes
- Close 5 browser tabs you don't need

### Tier 2 — Dainika (दैनिक): Daily Sankalpa
**When:** Set in the morning. Complete by end of today.  
**Rule:** Max 1 big sankalpa + 2 tiny sankalpas per day. No more.  
**Why it matters:** Constraining to 3 items prevents the overwhelm that breaks streaks. Every item should be so small that failing feels harder than doing it.

The **2-minute start test**: Can you *begin* your sankalpa in 2 minutes? If yes, it passes. If no, break it down further.

Examples:
- Big: "Solve 5 data structures problems for 45 minutes after lunch"
- Tiny 1: "Read one page of my textbook"
- Tiny 2: "Open my notes app and type today's date"

### Tier 3 — Saptahika (साप्ताहिक): Weekly Sankalpa
**When:** Set on Sunday evening or Monday morning. Complete this week.  
**Rule:** Max 2 Saptahika sankalpas. Review and update every Sunday in Svadhyaya.  
**Why it matters:** Weekly arc gives medium-term rhythm without overwhelm. It connects daily actions to a larger purpose.

---

## The Streak System

Streaks are borrowed from Duolingo and Snapchat — but rooted in the ancient concept of **Sadhana** (साधना), daily disciplined practice.

**How streaks work:**
- Each day you complete your Dainika sankalpa(s) → streak count +1
- Missing a day breaks the streak — but never permanently

**Sadhana Shield** (streak rescue, once per week):
- Missed yesterday? Do double tiny sankalpas today to restore
- This mirrors the Duolingo streak freeze concept, grounded in the principle that *restart is itself a commitment*

**Streak milestones:**
| Days | What it means |
|------|--------------|
| 3 | The chain is forming — neural pathways priming |
| 7 | Saptahika Siddhi — one full week of kept vows |
| 21 | Popular habit formation marker — behaviour is becoming automatic |
| 66 | Scientific average for habit automaticity (Phillippa Lally, UCL) — this is now identity |

---

## Tiny Wins — Why They Work

From James Clear's *Atomic Habits*: tiny habits are the gateway to identity change. The goal is not the 45-minute study session. The goal is the identity: **"I am someone who completes what I start."**

Each fulfilled sankalpa — no matter how tiny — votes for this identity.

**Design principle for tiny sankalpas:**
1. Make it so small it feels almost too easy
2. Make it **start-able** immediately (not "study for 2 hours" but "open the textbook")
3. Celebrate immediately after completion — not at the milestone, but right now

**Implementation intentions** (from psychology research by Peter Gollwitzer):
Frame every Dainika sankalpa as: *"When [situation], I will [sankalpa] for [duration]."*

Examples:
- *"When I sit down after breakfast, I will solve 2 problems for 20 minutes."*
- *"When my 3 PM class ends, I will read one page of my notes."*
- *"When I feel like scrolling, I will write one sentence in my journal instead."*

---

## Habit Stacking

Once a sankalpa becomes automatic (streak > 21), you can **stack** a new tiny sankalpa on top of it using the existing cue.

Formula: *"After I [existing habit], I will [new sankalpa]."*

Example: *"After I brush my teeth at night, I will write tomorrow's 3 sankalpas."*

---

## STM Workspace Files

| File | Purpose | Replaces |
|------|---------|---------|
| `_tasks/` | Staging inbox — capture raw tasks before triage | `00-inbox.md` (partial) |
| `00-today-sankalpa.md` | Daily ritual — today's commitments | `00-inbox.md` + `01-next-actions.md` |
| `01-streak-tracker.md` | Active habit streaks with milestone markers | *(new)* |
| `02-weekly-sankalpa.md` | This week's bigger arc commitments | `02-projects.md` (partial) |
| `03-someday-iccha.md` | Deferred wishes (iccha = desire) | `05-someday.md` |
| `04-waiting.md` | Items delegated or pending on others | `04-waiting-for.md` |
| `05-sankalpa-archive.md` | Completed sankalpas — Celebration Hall of Wins | *(new)* |
| `06-weekly-svadhyaya.md` | Weekly self-reflection and reset | `07-weekly-review.md` |

---

## Task Capture and Triage

Before a task can become a sankalpa, it must be **captured and routed**. Writing captures freely — without worrying where they go — protects the quality of your sankalpa list.

`stm/_tasks/` is the **staging inbox**. Write here first. Triage during your morning ritual or at your first free moment.

### Capture

Save any incoming task, obligation, or thought as a new file in `stm/_tasks/`:

```
YYYY-MM-DD-short-title.md
```

Use `stm/_tasks/TEMPLATE-capture.md` as the starting point. Fill only the raw task field. Do not triage at capture time if you are mid-class, mid-meeting, or mid-thought.

### Triage Decision Flow

Work through every `[raw]` file in `_tasks/` during the morning ritual:

```
Incoming capture
  ↓
< 2 min right now?
  YES → Tatkala: complete it NOW — delete the capture file
  NO  ↓
Must happen today?
  YES → Dainika → 00-today-sankalpa.md
        (3/day cap full? → mark [PENDING], triage tomorrow)
  NO  ↓
Must happen this week?
  YES → Saptahika → 02-weekly-sankalpa.md
        (both slots full? → mark [PENDING], review at Svadhyaya)
  NO  ↓
Waiting on someone else?
  YES → Waiting → 04-waiting.md
  NO  ↓
Genuinely want to do someday?
  YES → Iccha → 03-someday-iccha.md
   NO → Discard — hogbidi
```

### Routing Table

| Triage Decision | Route | STM File |
|---|---|---|
| < 2 min right now | Tatkala | Complete immediately — no file |
| Must happen today | Dainika | `00-today-sankalpa.md` |
| Must happen this week | Saptahika | `02-weekly-sankalpa.md` |
| Delegated / waiting | Waiting | `04-waiting.md` |
| Someday / not urgent | Iccha | `03-someday-iccha.md` |
| Cap is full | Pending | Keep in `_tasks/` with `[PENDING]` tag |
| Not worth doing | Discard | Delete the capture file |

### Triage Rules

1. **Capture first, triage second.** Never block writing because you don't know where it goes yet.
2. **The 3/day Dainika cap is enforced at triage.** If the cap is full, the task stays `[PENDING]` — it does not get forced into today.
3. **`_tasks/` is a staging area, not a backlog.** Review all `[raw]` and `[PENDING]` files every Sunday in Svadhyaya. Piling up here is a stress signal.
4. **Write the sankalpa in implementation-intention form** when routing to Dainika or Saptahika: *"When [situation], I will [action] for [duration]."*
5. **Archive after triage.** Move the processed file to `stm/_tasks/.archive/YYYY-MM-DD/`.

> Full folder guide and capture template: [`stm/_tasks/README.md`](../_tasks/README.md)

---

## STM Rules

1. **Max 3 Dainika sankalpas per day** (1 big + 2 tiny). Non-negotiable limit.
2. **Every sankalpa starts with a verb** and includes a time or duration.
3. **Tatkala rule**: Any task < 2 min → complete immediately, do not write it down.
4. **Completion over perfection**: Started + 60% done counts as fulfilled for tiny sankalpas.
5. **Sadhana Shield**: Once per week, miss a day → restore streak by doubling next day.
6. **No guilt, only restart**: Breaking a streak is not failure — continuing after a break is mastery.
7. **Archive wins**: Move completed sankalpas to `05-sankalpa-archive.md` — the hall of wins.
8. **Identity close**: Every session closes with: *"I am someone who completes what I start."*

---

## Student Conventions

- Prefix sankalpas with domain: `[ACA]` academic, `[CAR]` career, `[WLB]` wellbeing, `[SKL]` skill-building
- Tiny sankalpas should take ≤ 15 minutes to complete
- Big Dainika sankalpas should be completable in one focused session (30–90 min max)
- Saptahika sankalpas can span multiple days but must have a clear completion state
- Add evidence links in `05-sankalpa-archive.md` when a win has a portfolio artifact

---

## The STM Identity Statement

> *"Every sankalpa I complete — big or tiny — makes me more of who I am becoming.
> I do not break commitments to myself. When I slip, I restart.
> The restart is itself a fulfilled sankalpa."*

This statement is optionally read at the start of the morning ritual and at the close of weekly Svadhyaya.
