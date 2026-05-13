# Leaderboards — Public Student Achievement Celebration

> **This folder contains public leaderboards celebrating student achievements across Srujana stages and courses.**
> **Audience**: Students (for inspiration), coaches (for management), faculty mentors (for strategic overview).

---

## Purpose

Leaderboards in SrujanaBuddy are **not** competitive rankings. They are **celebration catalogs** designed to:

1. **Make invisible learning visible** — students see enterprising ability progress (investigation, pivots, collaboration, reflection) rendered as publicly sharable achievement
2. **Celebrate diverse strengths** — different leaderboard categories highlight different competencies (Investigation Masters, Pivot Artists, Collaboration Heroes, etc.), so every student can be recognized for something
3. **Inspire by example** — peers see real stories of learning, failure, recovery, and progress; builds studio culture
4. **Maintain privacy** — all leaderboards are opt-in; students control whether they appear anonymously or with real names

---

## Current Leaderboards

### 1. GCS Enterprising Ability Leaderboards

**File**: [`gcs-enterprising-ability.md`](gcs-enterprising-ability.md)

**Scope**: Grand Challenge Studio (GCS) — a Stage 3 (Creation) project course for 2nd-sem B.Tech students at REVA SoCSE.

**What's tracked**:
- **6 analytics dimensions** per student, combined into a single **Enterprising Ability Score** (0–100):
  1. Rubric Mastery (5 Growth & Grit rubrics: Pivot, Investigation, Collaboration, Prototype, Reflection)
  2. Sprint Progress (14 weeks of project execution)
  3. Consistency (on-time coaching sessions, no drift)
  4. Evidence Quality (diversity of artifacts logged)
  5. E2E Integration (synergy with 4 linked courses: C Programming, Software Design, IoT, I&E)
  6. Team Collaboration (leadership, communication, conflict resolution)

**8 Leaderboard Categories**:
1. 🔍 **Investigation Masters** — interview count + investigation depth
2. 🔄 **Pivot Artists** — pivots logged + clarity of logic
3. 🤝 **Collaboration Heroes** — conflicts resolved + peer growth
4. 📦 **Builders** — prototype completeness + demo-ability
5. 🧠 **Reflection Sages** — metacognition depth
6. ⚡ **Speed Demons** — velocity (weeks completed / time) + effort consistency
7. 📌 **Consistency Champions** — on-time sessions ≥90%
8. 🎯 **Bold Bets Achieved** — all students who shipped their Bold Bet

**Updated**: Every Friday evening by the GCS coach (after weekly coaching sessions).

**Framework & formulas**: [`references/gcs-enterprising-ability-analytics.md`](../../references/gcs-enterprising-ability-analytics.md)

---

## How to Use as a Coach

### Weekly Update (Friday, ~30 mins)

1. Open each student's profile in `profiles/{full-name}.md`
2. Go to `## GCS Gamification Analytics` section
3. Copy latest data:
   - Rubric levels (Novice/Intermediate/Advanced)
   - Sprint weeks completed
   - Interview count + sources
   - Pivots documented
   - Collaboration moves
   - Prototype status
   - On-time sessions / consistency %
4. Update the relevant leaderboard tabs in `gcs-enterprising-ability.md`
5. Identify **new badge unlocks** and **Bold Bet completions** (celebrate these!)
6. Commit and push
7. **Notify students** (if consented to public leaderboard): *"🔄 Pivot Master badge unlocked!"*

### Identify Students Ready for Next Stage

Review the leaderboard and analytics monthly. Flag students showing **Stage 4 (Enterprise)** signals to faculty mentors:
- 3+ rubrics at Advanced level
- Bold Bet achieved with real user traction
- E2E integration at High across 3+ courses
- Reflection shows venture or research mindset

---

## How to Use as a Student

### Check Your Progress (Anytime)

1. Open your profile in `profiles/{full-name}.md`
2. Go to `## GCS Gamification Analytics`
3. See:
   - **Pentagon radar chart** of your Enterprising Ability Score (visual progress)
   - Rubric mastery levels (Novice → Intermediate → Advanced)
   - Sprint level + weeks completed
   - Badges earned
   - Any public leaderboard ranks (if you consented)

### Appear on Public Leaderboard (Opt-in)

1. In your profile, go to `## GCS Gamification Analytics → Public Leaderboard Consent`
2. Set `Appear on leaderboard: ✅ Yes`
3. Choose: stay anonymous (Anon-XXX) or show your real name
4. Every Friday, if you earned a new badge or rank, you'll appear on the relevant leaderboard

### Share with Your Mentor (Opt-in)

1. In your profile, go to `## GCS Gamification Analytics → Mentor Sharing Consent`
2. Set `Share with mentor: ✅ Yes`
3. Choose what to share: Full profile / Rubric Mastery only / Collaboration log only
4. Your mentor gets a dashboard view of your Enterprising Ability progress

---

## Leaderboard Principles

### ✅ What We Celebrate
- **Investigation depth**: Real research, real interviews, real user insights
- **Pivot clarity**: Documented learning from failure; why you changed direction
- **Collaboration**: Conflict resolved, peer feedback given and received, team grew
- **Prototype reality**: Something that works, that users can actually use
- **Reflection depth**: Learning transferred; connected to personal growth
- **Consistency**: Showing up every week; grit over intensity
- **Ambition**: Attempted something scary; bold bets matter (whether you hit it or learned)

### ❌ What We Don't Rank
- Academic grades
- Output polish (beautiful ≠ useful)
- Brilliance (smart doesn't beat grit)
- Team size (solo is as valid as team)
- Speed alone (fast + shallow loses to slow + deep)

---

## Privacy & Consent

### Three Tiers

1. **Private Profile** (default)
   - Only you see your full analytics
   - Coach sees it during sessions
   - No public leaderboard

2. **Mentor Share** (opt-in)
   - You share with your faculty mentor
   - Mentor can see rubric mastery, Bold Bet progress, collaboration moves
   - Helps mentor guide you toward Stage 4

3. **Public Leaderboard** (opt-in)
   - You appear on public leaderboard(s)
   - Default: anonymous (Anon-001 style)
   - Can opt to show real name
   - Celebrate your achievement publicly

### Change Anytime

You can **opt in, opt out, or switch tiers** anytime. Update your profile → `## GCS Gamification Analytics → [Consent section]`. No judgment; privacy is yours.

---

## Future Leaderboards

This is a template for other project-based courses. Future leaderboards may include:
- **Other course buddies** (any project-heavy course can adopt the gamification system)
- **Internship cohort leaderboards** (Stage 2 Application track)
- **Startup/venture leaderboards** (Stage 4 Enterprise track)
- **Research/publication leaderboards** (Stage 4 Research track)
- **Cross-course badges** (e.g., "Integrated Thinker" for E2E synergy across 5+ courses)

---

## Questions?

- **Coach Q**: How do I update the leaderboard? → See "Weekly Update" section above or [`references/gcs-enterprising-ability-analytics.md`](../../references/gcs-enterprising-ability-analytics.md) → "System-Level Leaderboard Management"
- **Student Q**: How do I get on the leaderboard? → See "Appear on Public Leaderboard" section above
- **Faculty Q**: How do I see my mentee's progress? → Ask your mentee to set `Mentor Sharing Consent: ✅ Yes` in their profile
- **Technical Q**: What's the formula? → [`references/gcs-enterprising-ability-analytics.md`](../../references/gcs-enterprising-ability-analytics.md) has full math

