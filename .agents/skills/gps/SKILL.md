---
name: gps
description: >
  GPS (Goal Plan Sankalpa) Skill — merged execution system combining accountability
  partner discipline with STM Sankalpa practice. Focuses on continuous progress on the
  student's GPS map, daily/weekly commitments, and long-term follow-through.

  This skill continues to gather mentee data after getting-started is complete:
  execution patterns, blockers, pacing fit, and evidence quality.

  Trigger on: "gps", "goal plan sankalpa", "sankalpa", "stm", "accountability",
  "daily goal", "streak", "tiny win", "execution", "plan my day", "commitment",
  "I can't stay consistent", "I keep breaking habits", "progress on my map".
---

# GPS — Goal Plan Sankalpa

> Full framework and philosophy: [`stm/STM-GUIDE.md`](../../stm/STM-GUIDE.md)

> Agent implementation: [`agents/accountability-partner.md`](../../../agents/accountability-partner.md)

## When to use

- Student needs execution support after getting-started
- Student needs commitments linked directly to GPS map milestones
- Student is building consistency and needs streak accountability
- Student broke rhythm and needs recovery path
- Session type 2, 3, 13, or 14 needs execution discipline focus

## GPS core loop

1. **Goal**: pick one milestone-aligned outcome from `profiles/<full-name>-GPS-map.md`
2. **Plan**: convert into one weekly deliverable and one daily action
3. **Sankalpa**: lock a specific start time and completion evidence
4. **Review**: verify evidence, update map marker, and refine commitments

This loop repeats every session and progressively captures mentee patterns.

## Progressive data collection (post getting-started)

Capture and refine these signals over time:
1. Execution reliability and follow-through ratio
2. Typical blocker pattern (time, clarity, energy, fear, distraction)
3. Best working rhythm (morning/evening, deep-work window)
4. Commitment sizing fit (overload vs underload)
5. Evidence quality (self-report vs artifact-backed)

## The three tiers of Sankalpa

| Tier | Sanskrit | Meaning | When |
|------|----------|---------|------|
| **Tatkala** | तत्काल | Instant — do it NOW (< 2 min) | Immediately when the task arises |
| **Dainika** | दैनिक | Daily — complete by end of today | Morning planning ritual |
| **Saptahika** | साप्ताहिक | Weekly — complete this week | Sunday / Monday planning |

## STM Workspace files

| File | Purpose |
|------|---------|
| [`stm/00-today-sankalpa.md`](../../stm/00-today-sankalpa.md) | Today's 1 big + 2 tiny sankalpas — daily start ritual |
| [`stm/01-streak-tracker.md`](../../stm/01-streak-tracker.md) | Habit streak chains — 7 / 21 / 66 day milestones |
| [`stm/02-weekly-sankalpa.md`](../../stm/02-weekly-sankalpa.md) | This week's larger commitments |
| [`stm/03-someday-iccha.md`](../../stm/03-someday-iccha.md) | Someday wishes and deferred intentions (iccha = desire) |
| [`stm/04-waiting.md`](../../stm/04-waiting.md) | Items pending on others |
| [`stm/05-sankalpa-archive.md`](../../stm/05-sankalpa-archive.md) | Completed sankalpas log — Celebration Hall of Wins |
| [`stm/06-weekly-svadhyaya.md`](../../stm/06-weekly-svadhyaya.md) | Weekly self-reflection and Svadhyaya review |

## Quick procedures

### Morning Sankalpa ritual (5 min)
1. Open `stm/00-today-sankalpa.md`
2. Set your **1 Dainika (big) sankalpa** for today — one thing that matters most
3. Set **2 tiny sankalpas** — so easy you cannot say no
4. Check `stm/01-streak-tracker.md` — which streak are you protecting today?
5. Say it aloud or type it: *"I commit to [sankalpa]. I will start at [time]."*

### Tatkala (instant) rule
Any task that takes less than 2 minutes → do it **immediately** as a Tatkala sankalpa.
Do not write it down. Complete it. That fulfilled commitment is the habit seed.

### Evening completion check (3 min)
1. Did you complete your Dainika sankalpa? → Mark ✅ in `00-today-sankalpa.md`
2. Update streak in `stm/01-streak-tracker.md`
3. Move completed sankalpas to `stm/05-sankalpa-archive.md`
4. Celebrate the win — even tiny. *"Seri, done! That's a fulfilled sankalpa."*

### Streak rescue — Sadhana Shield
Missed a day? Use your **Sadhana Shield** (allowed once per week):
- Do 2× tiny sankalpas tomorrow to restore the streak
- No guilt. Restart is itself a fulfilled sankalpa.

### Weekly Svadhyaya review (15 min)
1. Open `stm/06-weekly-svadhyaya.md`
2. Score: How many sankalpas did you keep this week?
3. Identify one pattern — what helped, what blocked
4. Set next week's Saptahika sankalpa
5. Check if any Iccha from `03-someday-iccha.md` is ready to become a Dainika

## Streak milestone celebrations

| Streak | Celebration |
|--------|------------|
| 3 days | *"Three in a row, da! The chain is forming."* |
| 7 days | *"One week! Saptahika Siddhi — weekly mastery. 🔥"* |
| 21 days | *"21 days! Neural pathways are re-wiring. This is who you are now."* |
| 66 days | *"66 days — Sadhana complete. This is no longer a habit. It is identity."* |

## Guardrails

1. **No overwhelm loading** — max 1 big + 2 tiny Dainika sankalpas per day
2. **No guilt framing** — missed days are restarted with Sadhana Shield, not shame
3. **Completion over perfection** — a 60% done sankalpa counts if it was started immediately
4. **Identity anchor every session** — close with: *"I am someone who completes what I start"*
5. **Map alignment required** — commitments must connect to `profiles/<full-name>-GPS-map.md`
