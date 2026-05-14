---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 26px;
    padding: 40px 60px;
    color: #1a1a2e;
  }
  section.lead {
    text-align: center;
    justify-content: center;
    background: linear-gradient(135deg, #1a237e 0%, #283593 60%, #3949ab 100%);
    color: #ffffff;
  }
  section.lead h1 { color: #ffffff; font-size: 52px; }
  section.lead h2 { color: #c5cae9; font-size: 32px; font-weight: 300; }
  section.lead p { color: #e8eaf6; }
  section.lead blockquote {
    background: transparent;
    border-left: 5px solid rgba(255,255,255,0.4);
    color: #e8eaf6;
  }
  section.track {
    background: #f3f4f6;
  }
  section.demo-slide {
    background: #fafafa;
    border-top: 6px solid #3949ab;
  }
  section.cta {
    background: linear-gradient(135deg, #0d47a1 0%, #1565c0 100%);
    color: white;
  }
  section.cta h1, section.cta h2, section.cta li { color: white; }
  h1 { color: #1a237e; font-size: 40px; margin-bottom: 0.3em; }
  h2 { color: #283593; font-size: 30px; }
  h3 { color: #3949ab; font-size: 24px; }
  blockquote {
    border-left: 5px solid #3949ab;
    background: #e8eaf6;
    padding: 0.6em 1.2em;
    border-radius: 4px;
    font-style: italic;
    color: #1a237e;
  }
  table { font-size: 22px; width: 100%; }
  th { background: #3949ab; color: white; }
  tr:nth-child(even) { background: #e8eaf6; }
  .chat-student {
    background: #e3f2fd;
    border-radius: 12px;
    padding: 0.5em 1em;
    margin: 0.4em 0;
    border-left: 3px solid #1976d2;
    font-size: 22px;
  }
  .chat-buddy {
    background: #e8f5e9;
    border-radius: 12px;
    padding: 0.5em 1em;
    margin: 0.4em 0;
    border-left: 3px solid #388e3c;
    font-size: 22px;
  }
  .placeholder {
    background: #fff9c4;
    border: 2px dashed #f9a825;
    padding: 1em;
    border-radius: 8px;
    text-align: center;
    color: #6d4c41;
    font-size: 20px;
  }
  footer { font-size: 16px; color: #9e9e9e; }
---

<!-- _class: lead -->

#

> **आचार्यात् पादमादत्ते पादं शिष्यः स्वमेधया ।**
> **पादं सब्रह्मचारिभ्यः पादं कालक्रमेण च ॥**

---

<!-- _class: lead -->

# SrujanaBuddy
## REVA University's AI Coaching Companion

**A Leadership Demonstration**
May 14, 2026 · First Floor Boardroom, Admin Block

*Augmenting Faculty Mentoring at Scale*

---

# Agenda

| Time | Session |
|------|---------|
| 15 min | **Software 3.0 & Agent Skills** — The Revolution in Plain Language |
| 5 min | **SrujanaBuddy** — Architecture & Coach Identity |
| 15 min | **Live Demo** — Student Experience Walkthrough |
| 15 min | **Feedback & Q&A** |
| 10 min | **Action Planning** — Beta Testers & Next Steps |

> *You choose which demo scenarios to see — pick from 10 real student situations.*

---

# Part 1: Software 3.0 & Agent Skills

## The Revolution — In Plain Language

*For non-technical leadership: what changed, and why it matters now*

---

# How Software Evolved

<div class="mermaid">
timeline
    title The Evolution of Software
    1960 onwards : Software 1.0 — Rule-Based
              : Programmer writes every instruction
              : Rigid. Predictable. No judgement.
    2010 onwards : Software 2.0 — Learning from Data
              : Neural networks trained on examples
              : Flexible patterns. Still no language.
    2025 onwards  : Software 3.0 — Language-First Intelligence
              : You describe what you want in plain language
              : AI reasons, plans, and acts
</div>

> *We moved from "tell the computer every step" to "describe the goal and the AI figures out the steps."*

---

# The Analogy — In Simple Terms

<div class="mermaid">
graph LR
    A["📋 Software 1.0\nPrinted Procedure Manual\nFollow exact steps only"] --> B["🎓 Software 2.0\nLearned by Example\nShowed 10,000 cases; found patterns"] --> C["🧠 Software 3.0\nExpert Consultant\nDescribe the problem.\nThey figure out the approach."]

    style A fill:#ffcdd2,stroke:#c62828,color:#000
    style B fill:#fff9c4,stroke:#f9a825,color:#000
    style C fill:#c8e6c9,stroke:#2e7d32,color:#000
</div>

### The shift:
- **Old:** You tell the computer every step. It breaks if one step changes.
- **New:** You describe intent. The AI reasons. It adapts.

---

<!-- _class: track -->

# What Are "Agent Skills"?

<div class="mermaid">
flowchart TB
    subgraph AI["🧠 Large Language Model (The Brain)"]
        direction TB
        LLM["Reasoning Engine\nUnderstands language, context, intent"]
    end

    subgraph SKILL["📋 Agent Skill (The Role)"]
        direction TB
        S1["Identity: Who am I?"]
        S2["Rules: How do I behave?"]
        S3["Tools: What can I use?"]
        S4["Domain: What do I know?"]
    end

    subgraph ACTION["⚡ Output"]
        O1["Coaching conversation"]
        O2["Document review"]
        O3["Task planning"]
        O4["Data analysis"]
    end

    SKILL --> AI --> ACTION
</div>

> **An Agent Skill = Instructions that give the AI a specific role, domain knowledge, and behavioural rules.**
> Like giving a brilliant generalist a detailed job description.

---

# One Model. Infinite Specialists.

<div class="placeholder">
🖼️ INFOGRAPHIC PLACEHOLDER: Show one brain → 15 specialist hats (coach, auditor, researcher, admin, mentor...)
</div>

### Why this is revolutionary:
- **No new software** to install or maintain
- **No new servers** — runs in the tools you already use (GitHub Copilot, VS Code, Gemini)
- **Instantly update** expertise by editing a text file
- **Any domain** — the same approach works for coaching, legal review, research, admin

> *You are not buying software. You are writing role descriptions for an AI that already exists.*

---

<!-- _class: track -->

# T.R.A.C.K — Automation Across REVA

<div class="mermaid">
mindmap
  root((T.R.A.C.K))
    T[Teaching & Learning]
      Course coaching for each subject
      Exam prep and study plans
      Learning-to-learn coaching
      Anti-brain-rot guardrails
    R[Research]
      PhD scholar guidance
      Literature review assistant
      Materials synthesis protocols
      Publication planning
    A[Administration]
      MOU review with legal checks
      AAA Audit document review
      NAAC evidence collection
      Faculty coordination
    C[Consulting & Products]
      Startup mentoring
      Industry project coaching
      Portfolio and competency building
      GCS gamification engine
    K[Kaizen]
      Weekly review protocols
      Faculty mentoring insights
      Continuous improvement loops
      Early warning dashboards
</div>

---

# T.R.A.C.K — Real Examples Today

| Domain | What an Agent Skill Can Do |
|--------|---------------------------|
| **Teaching (T)** | Coach a student through exam panic at 11pm — no faculty needed |
| **Research (R)** | Guide a PhD scholar on materials synthesis from published papers |
| **Administration (A)** | Review an MOU against REVA's legal checklist — flag gaps instantly |
| **Consulting (C)** | Score a student's startup idea across 6 Enterprising dimensions |
| **Kaizen (K)** | Run weekly coaching reviews and flag at-risk students to faculty |

<div class="placeholder">
🖼️ MEME PLACEHOLDER: "It's not about replacing faculty — it's about giving faculty superpowers."
(Suggest: Professor with Iron Man suit)
</div>

---

# The Key Insight for Leadership

<div class="mermaid">
flowchart LR
    A["❌ Old Model\n1 Faculty : 60 Students\nPersonalized guidance = impossible"] --> B["✅ New Model\n1 Faculty + SrujanaBuddy\n= 1 Faculty : 60 Students\nwith personalized coaching at scale"]

    style A fill:#ffcdd2,stroke:#c62828,color:#000
    style B fill:#c8e6c9,stroke:#2e7d32,color:#000
</div>

### SrujanaBuddy is not a chatbot.
It is a **coaching operating system** — 160 files, 15,000 lines of REVA-specific coaching intelligence — built on Agent Skills technology.

> *The same platform that can coach students can review MOUs, guide PhD research, support NAAC audits, and run Kaizen reviews. Same technology. Different skill files.*

---

# Part 2: SrujanaBuddy

## Architecture & Coach Identity

---

# What Is SrujanaBuddy?

<div class="mermaid">
graph TB
    SB["SrujanaBuddy\nAI Coaching Companion\nfor REVA Students"]

    SB --> C1["📚 Shiksha\nAcademic Coaching\nSubject mastery, exam prep"]
    SB --> C2["🧠 Antarmana\nInner Mastery\nFocus, discipline, motivation"]
    SB --> C3["👥 Sangha\nTeam & Relationships\nLeadership, collaboration"]
    SB --> C4["🌿 Seva\nContribution\nNCC, NSS, open source"]
    SB --> C5["💪 Sharira\nEnergy & Wellbeing\nSleep, stress, recovery"]

    style SB fill:#1a237e,color:#ffffff
    style C1 fill:#e3f2fd,color:#000
    style C2 fill:#f3e5f5,color:#000
    style C3 fill:#e8f5e9,color:#000
    style C4 fill:#fff9c4,color:#000
    style C5 fill:#fce4ec,color:#000
</div>

*Five Spheres (Panchakosha) — whole-person coaching, not just grades.*

---

# Architecture: How It Routes

<div class="mermaid">
flowchart TD
    START([Student says 'hi']) --> PROFILE{Profile exists?}

    PROFILE -- Yes --> GREET["Greet by name\n+ Last coaching session summary"]
    PROFILE -- No --> INTAKE["Start Intake Protocol\nCapture aspirations north star"]

    GREET --> CONTEXT["Load Coaching Context\nEnergy · Clarity · Overwhelm signals"]
    INTAKE --> CONTEXT

    CONTEXT --> ROUTE{Route Session}

    ROUTE --> A1["Academic Learning Coach"]
    ROUTE --> A2["Wellbeing Triage Agent"]
    ROUTE --> A3["Career Pathway Coach"]
    ROUTE --> A4["Accountability Partner"]
    ROUTE --> A5["Enterprising Skills Mentor"]
    ROUTE --> A6["... 10 more specialists"]

    style START fill:#1a237e,color:#fff
    style GREET fill:#c8e6c9,color:#000
    style INTAKE fill:#fff9c4,color:#000
    style ROUTE fill:#3949ab,color:#fff
</div>

---

# 15 Specialist Agents

| # | Agent | Who It Serves |
|---|-------|--------------|
| 1 | Academic Learning Coach | Study strategy, subject mastery |
| 2 | Course Buddy (per subject) | Per-course deep coaching |
| 3 | Assessment & Competition Coach | Exams, hackathons, competitions |
| 4–5 | Accountability + GTD Partner | Daily/weekly execution discipline |
| 6 | Inner Mastery Coach | Focus, discipline, dopamine regulation |
| 7 | Integral Life Coach | Whole-person balance |
| 8 | Career & Pathway Coach | Job/internship/GATE/startup direction |
| 9 | Competency & Portfolio Coach | Portfolio for placements and admissions |
| 10 | Out-of-Curriculum Coach | Certifications, personal projects |
| 11 | Enterprising Skills Mentor | GCS, startup ideas, venture readiness |
| 12–15 | Support, Faculty Coord, History, Website | Safety, escalation, evidence, presence |

---

# The Srujana Pathway

<div class="mermaid">
graph LR
    S1["🌱 Stage 1\nFoundation\nStudy habits · GTD\nCampus integration\nYear 1"]
    S2["🔨 Stage 2\nApplication\nIndustry projects\nInternships · Skills\nYear 2–3"]
    S3["🛠️ Stage 3\nCreation\nProducts · Papers\nPortfolio · GCS\nYear 3–4"]
    S4["🚀 Stage 4\nEnterprise\nVentures · Research\nImpact · Leadership\nFinal / PG"]

    S1 --> S2 --> S3 --> S4

    style S1 fill:#e3f2fd,stroke:#1976d2,color:#000
    style S2 fill:#e8f5e9,stroke:#388e3c,color:#000
    style S3 fill:#fff9c4,stroke:#f9a825,color:#000
    style S4 fill:#fce4ec,stroke:#c62828,color:#000
</div>

*Readiness-based progression, not semester-gated. Evidence-first.*

---

# Part 3: Live Demo

## 10 Student Scenarios — You Choose

*Select any scenario below. We will walk through it live.*

---

# Choose Your Demo

| # | Student | Situation | What You'll See |
|---|---------|-----------|-----------------|
| 1 | **Riya** — 1st yr CSE | Exam panic, blank brain | Wellbeing triage · Calm Queen reset |
| 2 | **Arjun** — 3rd yr CSE | AI vs Startup dilemma | Career coaching · Svadharma discovery |
| 3 | **Keerthi** — 2nd yr ECE | Wants to learn ML | Out-of-curriculum coach · AI pathways |
| 4 | **Vikram** — 4th yr CSE | Placement panic, weak portfolio | Portfolio rescue · 6-week plan |
| 5 | **Sneha** — MBA 1 | "I don't know my strengths" | Five Spheres · strengths discovery |
| 6 | **Rohit** — 3rd yr ISE | Personal website, paralysed | Personal website agent · step-by-step |
| 7 | **Ananya** — 3rd yr CSE | Startup idea → GCS score | Enterprising mentor · 6-dim GCS score |
| 8 | **Faizan** — 1st yr Mech | Missed 3 weeks, family crisis | Wellbeing first · academic re-entry |
| 9 | **Priya** — 4th yr CSE | GATE + PhD ambition | Research pathway · GATE 2027 plan |
| 10 | **Suresh** — 2nd yr Civil | Wrong branch, demotivated | Svadharma navigator · pivot framing |

---

<!-- _class: demo-slide -->

# Demo A — Wellbeing First: Riya's Story
### *1st Year · Exam Week · 3/10 energy · 2 days no sleep*

<div class="chat-student">
💬 Riya: "hi i dont know what to do i have 3 exams in 2 days and i cant study anything my brain is just blank"
</div>

<div class="chat-buddy">
🤖 SrujanaBuddy: "Aye Riya, seri — I hear you, da. Blank brain during exam week is the worst feeling, no? Before we do anything else — quick check-in first. On a scale of 1 to 10, how are you feeling right now?"
</div>

**What happened:**
- ✅ Wellbeing check BEFORE any study plan
- ✅ Calm Queen Reset (4-4-6 breathing)
- ✅ 3-subject priority triage → 2-hour micro-plan
- ✅ Session close with anonymized log consent

> *Faculty insight: Student reached out at 10 PM. No faculty available. SrujanaBuddy held the space.*

---

<!-- _class: demo-slide -->

# Demo B — Career Clarity: Arjun's Dilemma
### *3rd Year · AI/ML track vs co-founding a startup*

<div class="chat-student">
💬 Arjun: "i like AI and i've been doing some ML projects but my friend wants me to co-found a startup... i honestly don't know which is better"
</div>

<div class="chat-buddy">
🤖 SrujanaBuddy: "Arjun, this is actually a really good problem to have — it means you have options. Most 3rd years are still figuring out what they even want. So respect, da. When you were doing those ML projects — what was the feeling? 'I love this work itself' or 'I love what I can build with this'?"
</div>

**The outcome:** Arjun realized his answers pointed to the startup — and the startup was in AI. The paths weren't in conflict. He needed to see it clearly.

> *Socratic coaching — SrujanaBuddy never told him the answer. He found it himself.*

---

<!-- _class: demo-slide -->

# Demo C — Portfolio Rescue: Vikram's 6-Week Plan
### *4th Year · Placements in 6 weeks · 7 GitHub projects, 5 unfinished*

<div class="chat-buddy">
🤖 SrujanaBuddy: "Let me give you the honest portfolio audit: Current state: 7 projects, 2 usable, 5 dead weight. Target state in 6 weeks: 3 strong projects + 1 standout you can talk about for 15 minutes. Your bottleneck is not CGPA — it's projects + communication. That's fixable."
</div>

**6-week rescue plan generated:**
- Week 1–2: Triage + polish one project
- Week 3–4: Build one focused new project
- Week 5: Practice interview narration
- Week 6: Mock interview dry run

<div class="placeholder">
🖼️ IMAGE PLACEHOLDER: Before/after GitHub profile screenshot (mock-up)
</div>

---

<!-- _class: demo-slide -->

# Demo D — Startup & GCS Score: Ananya's Idea
### *3rd Year · Campus gig marketplace app · 30 student interviews done*

**GCS 6-Dimension Live Scoring:**

| Dimension | Ananya's Signal | Score |
|-----------|----------------|-------|
| Problem Intelligence | Two clear sub-problems identified | 4/5 |
| Solution Design | V1 scoped to 3 features only | 4/5 |
| Execution | 30 interviews before building | 5/5 |
| Market Awareness | REVA-first, then expand | 3/5 |
| Team & Resources | Solo founder currently | 2/5 |
| Impact | Real student economic pain point | 4/5 |

**Coaching nudge:** "Go to 5/5 on Problem Intelligence: quantify — '73% of students missed a job due to discovery lag.' That one number changes how people hear your pitch."

---

<!-- _class: demo-slide -->

# Demo E — Strengths Discovery: Sneha's Revelation
### *MBA 1st Year · "Everyone else knows what they want"*

<div class="chat-buddy">
🤖 SrujanaBuddy: "Sneha, you love *invisible architecture* — the systems behind the scenes that make things work. You're not doing it for recognition. You're doing it for the satisfaction of the system working. That's operations intelligence + process design + systems thinking."
</div>

**Five Spheres Snapshot — built in one session:**

| Sphere | Signal |
|--------|--------|
| 🧠 Intellectual | Systems thinker, loves structured complexity |
| 🤝 Social | Facilitator energy — enables others to show up |
| 🎯 Action | Satisfaction from plan → execution → silent success |
| 💬 Communication | Low-ego communicator |
| 🌱 Growth | Exploration mode — appropriate for Stage 1→2 |

> *"Oh wow. I never thought of 'organizing the fest' as a strength."*

---

<!-- _class: demo-slide -->

# Demo F — The Tough One: Suresh's Reframe
### *2nd Year Civil · "I hate my branch. I was always into tech."*

<div class="chat-buddy">
🤖 SrujanaBuddy: "You're learning Python on your own, without anyone asking you to. That's self-directed learning. And 'the maths of how buildings are designed' — you know what field sits exactly at that intersection? Computational Civil Engineering. People in it write Python to simulate building stress, model earthquake impact, optimize structural design."
</div>

**What SrujanaBuddy did NOT do:**
- ❌ Did not tell him to "just study harder"
- ❌ Did not escalate unnecessarily
- ❌ Did not dismiss the branch mismatch

**What it DID:**
- ✅ Wellbeing check first
- ✅ Reframed the branch — not wrong, just wrong frame
- ✅ Specific career path: Computational Civil + BIM + Digital Twins

---

# 6 AI Engineer Career Pathways

*Already built into SrujanaBuddy — ready to deploy*

<div class="mermaid">
graph TD
    ASSESS["5-Question Self-Assessment"]
    ASSESS --> P1["Pathway 1\nAI-Native Builder\n6–9 months"]
    ASSESS --> P2["Pathway 2\nAI Systems Engineer\n9–15 months"]
    ASSESS --> P3["Pathway 3\nData Science & Analytics\n6–9 months"]
    ASSESS --> P4["Pathway 4\nML Research Analyst\n12–18 months"]
    ASSESS --> P5["Pathway 5\nAI Product Leader\n4–6 months"]
    ASSESS --> P6["Pathway 6\nAI Security & Governance\n9–12 months"]

    style ASSESS fill:#1a237e,color:#fff
    style P1 fill:#e3f2fd,color:#000
    style P2 fill:#e8f5e9,color:#000
    style P3 fill:#fff9c4,color:#000
    style P4 fill:#fce4ec,color:#000
    style P5 fill:#f3e5f5,color:#000
    style P6 fill:#ffccbc,color:#000
</div>

*48 modules · 8 categories · evidence-based progression · free audit resources*

---

# Part 3: What SrujanaBuddy Delivers

---

# For Students

<div class="mermaid">
graph LR
    S["Student\n'I need help'"] --> B["SrujanaBuddy\nAvailable 24/7"]
    B --> W["Wellbeing check\nbefore task work"]
    B --> G["Personalized\nweekly coaching"]
    B --> P["Portfolio &\ncompetency tracking"]
    B --> C["Career pathway\nclarity"]
    B --> E["Enterprising skills\n& GCS scoring"]

    style S fill:#e3f2fd,color:#000
    style B fill:#1a237e,color:#fff
</div>

- **Always available** — 11 PM exam panic? Handled.
- **Culturally resonant** — Bangalore English, Kannada flavour, peer energy
- **Privacy-first** — consent-based sharing, student controls their data
- **Anti-substitution** — AI augments thinking; explain-back rule enforced

---

# For Faculty

| Before SrujanaBuddy | After SrujanaBuddy |
|--------------------|-------------------|
| Repetitive "where to start" questions | Students arrive with a plan |
| No visibility until exam failures | Early warning dashboard signals |
| 60 students, 30 minutes each = impossible | AI handles routine; faculty handle advanced |
| Mentoring minutes undocumented | Structured session logs (consent-based) |
| Subject coaching bottleneck | 10+ course coaches available per semester |

<div class="placeholder">
🖼️ INFOGRAPHIC PLACEHOLDER: Faculty time freed up → deep mentoring, research collaboration
</div>

---

# For REVA as an Institution

<div class="mermaid">
mindmap
  root((REVA Advantage))
    Differentiation
      AI-native student experience
      Visible Srujana pathway evidence
      Portfolio-first graduates
    Mission Alignment
      Educate to Enterprise
      Panchakosha holistic development
      Indian wisdom tradition anchored
    Measurability
      GCS scores and progression
      Competency evidence collection
      At-risk early warning signals
    Scalability
      Markdown-native — no new infra
      Internal open source model
      Faculty as contributors
</div>

---

# Privacy, Safety & Guardrails

<div class="mermaid">
flowchart TD
    CHECK["Wellbeing Signal Detected"]
    CHECK --> L1["Tier 1 — Light coaching\nStudent briefly off\nHandle within session"]
    CHECK --> L2["Tier 2 — Support coaching\nConsistent stress signals\nGentle referral to REVA counsellor"]
    CHECK --> L3["Tier 3 — Escalation\nCrisis language detected\nImmediate faculty + Manodhara referral"]

    style CHECK fill:#283593,color:#fff
    style L1 fill:#c8e6c9,color:#000
    style L2 fill:#fff9c4,color:#000
    style L3 fill:#ffcdd2,color:#000
</div>

- **Student controls sharing** — 3 tiers of mentor visibility
- **Consent-based leaderboards** — opt-in only
- **Anti-brain-rot rule** — AI never writes essays or code for submission
- **Explain-back requirement** — student must be able to explain AI-assisted output

---

# The Numbers

| Metric | Value |
|--------|-------|
| Files in system | ~160 |
| Lines of coaching intelligence | ~15,000 |
| Specialist agents | 15 |
| AI Engineer pathways | 6 |
| Demo student personas | 10 |
| Domains covered | Learning · Career · Life Skills · Wellbeing · Enterprise |
| Infrastructure required | None — runs on existing IDE + GitHub |
| New software to install | None |

<div class="placeholder">
🖼️ MEME PLACEHOLDER: "No new servers. No new licenses. Just a text file that makes the AI brilliant."
(Suggest: "We have technology at home" meme — the technology is already here)
</div>

---

# What Makes SrujanaBuddy Different

<div class="mermaid">
quadrantChart
    title Coaching Solutions Comparison
    x-axis Scalable --> Personalised
    y-axis Generic --> REVA-Specific
    quadrant-1 Ideal Zone
    quadrant-2 Generic & Personalised
    quadrant-3 Generic & Scalable
    quadrant-4 Specific but Limited
    SrujanaBuddy: [0.85, 0.9]
    Generic Chatbot: [0.9, 0.1]
    Human Faculty: [0.1, 0.85]
    Commercial EdTech: [0.7, 0.3]
</div>

*SrujanaBuddy occupies the ideal zone: scalable AND REVA-specific AND personalised.*

---

# Part 4: Action Planning

## Beta Testers, Contributors & Next Steps

---

<!-- _class: cta -->

# The Ask — Be Part of History

> *"The best way to predict the future is to create it."* — Alan Kay

### We are looking for:

**Faculty Beta Testers (2–3 volunteers)**
- Use SrujanaBuddy alongside your existing mentoring
- Provide weekly feedback on student outcomes
- Help identify subject-specific coaching gaps

**Student Beta Testers (5–10 volunteers)**
- Commit to weekly coaching sessions for one semester
- Share anonymized progress signals (with consent)
- Help evolve the system through real use

**Faculty Contributors (1–2 per course)**
- Help build Course Buddy instances for your subject
- Co-author subject-specific knowledge base entries
- Become internal open source maintainers at REVA

---

# How to Contribute — No Tech Skills Needed

<div class="mermaid">
flowchart LR
    F["Faculty / Student\nContributor"] --> C1["🗣️ Talk to SrujanaBuddy\nReport what works / what doesn't"]
    F --> C2["📝 Edit a Markdown file\nUpdate coaching scripts, question banks"]
    F --> C3["🏫 Build a Course Buddy\nCoaching spec for your subject"]
    F --> C4["📊 Review student signals\nValidate coaching recommendations"]

    style F fill:#1a237e,color:#fff
    style C1 fill:#e3f2fd,color:#000
    style C2 fill:#e8f5e9,color:#000
    style C3 fill:#fff9c4,color:#000
    style C4 fill:#fce4ec,color:#000
</div>

> **This is a Markdown-native system. If you can write an email, you can contribute.**
> The system lives on GitHub — every change is versioned, reviewed, and attributed.

---

# Rollout Roadmap

<div class="mermaid">
gantt
    title SrujanaBuddy Rollout Plan
    dateFormat YYYY-MM-DD
    section v1.5 (Now)
    General coaching live          :done, 2026-05-14, 2026-05-31
    10 AI Engineer pathways        :done, 2026-05-14, 2026-05-31
    Demo & feedback loop           :active, 2026-05-14, 2026-06-30

    section v1.6 (Q3 2026)
    Faculty beta cohort (3 faculty)  :2026-06-01, 2026-07-31
    Student beta cohort (10 students):2026-06-01, 2026-07-31
    Course Buddy instances (3 courses):2026-07-01, 2026-08-31

    section v2.0 (Q4 2026)
    Faculty dashboards               :2026-09-01, 2026-11-30
    GCS leaderboard (opt-in)         :2026-09-01, 2026-11-30
    REVA-wide rollout consideration  :2026-10-01, 2026-12-31
</div>

---

# Identify 2–3 Courses for v1.6

| Course Type | Why It Fits | Effort |
|-------------|-------------|--------|
| **Capstone Project** | Students need ongoing coaching, not one-off advice | Medium |
| **Research Methods / Dissertation** | Structured guidance is repeatable and scalable | Medium |
| **Internship Prep** | Clear milestones, portfolio checkpoints, placement coaching | Low |
| **AI/ML Foundation** | Already have AI Engineer pathway modules built | Low |
| **Life Skills / Soft Skills** | Five Spheres framework maps directly | Low |

> *Which courses would benefit most from 24/7 coaching support for your students?*

---

# Action Planning — Today's Commitments

| Who | Action | By When |
|-----|--------|---------|
| Faculty volunteers | Confirm beta testing interest | Today |
| Student nominees | Identify 5–10 beta testers | This week |
| Course selection | Nominate 2–3 courses for v1.6 | This week |
| Core team | Schedule onboarding session | Next week |
| All | Share this presentation | Today — GitHub link |

<div class="placeholder">
🖼️ IMAGE PLACEHOLDER: QR code linking to this presentation on GitHub
(URL: github.com/[org]/SrujanaBuddy/review/srujanabuddy-leadership-demo-v1.0.md)
</div>

---

<!-- _class: cta -->

# Before We Open the Floor

### Quick show of hands:

1. **Which demo scenario did you find most relevant to your students?**

2. **Which T.R.A.C.K domain outside coaching interests you most?**
   *(Teaching / Research / Administration / Consulting / Kaizen)*

3. **Who wants to be a beta tester — faculty or student nominator?**

> *Your answers will shape v1.6 priorities.*

---

# Q&A

<div class="placeholder">
🖼️ IMAGE PLACEHOLDER: "No question is too basic" — open floor graphic
</div>

### Anticipate these questions:

| Question | Short Answer |
|----------|-------------|
| "Is student data safe?" | Student-controlled, consent-based, no PII to external services |
| "Does it replace faculty?" | No — it handles routine so faculty handle advanced |
| "What if AI gives wrong advice?" | Faculty escalation triggers; all advice is explainable |
| "How much does it cost?" | Zero infrastructure cost — runs on existing tools |
| "Who maintains it?" | REVA contributors — internal open source model |
| "Is it ready now?" | 15,000 lines live; demo logs validated; beta-ready |

---

<!-- _class: lead -->

# ❝

> *"Education is not the filling of a pail,*
> *but the lighting of a fire."*
> — W.B. Yeats

**SrujanaBuddy exists to light that fire —**
**one student, one session, one small win at a time.**

---

<!-- _class: lead -->

# Thank You

**SrujanaBuddy — REVA University AI Coaching System**

📂 This presentation: `review/srujanabuddy-leadership-demo-v1.0.md`
🌐 Repository: `github.com/[org]/SrujanaBuddy`
📧 Core team: [add contact]

*Built with Markdown · Versioned on GitHub · Open for REVA contributors*

---

# Appendix: Full Demo Index

*Reference for facilitator — jump to any scenario as requested*

| File | Student | Key Capability |
|------|---------|---------------|
| [riya-sharma.md](../eval/demos/riya-sharma.md) | Riya — Exam panic | Wellbeing triage, Calm Queen |
| [arjun-patel.md](../eval/demos/arjun-patel.md) | Arjun — Career dilemma | Svadharma, pathway mapping |
| [keerthi-reddy.md](../eval/demos/keerthi-reddy.md) | Keerthi — Wants ML | Out-of-curriculum, AI pathways |
| [vikram-nair.md](../eval/demos/vikram-nair.md) | Vikram — Placement | Portfolio rescue, GTD |
| [sneha-kulkarni.md](../eval/demos/sneha-kulkarni.md) | Sneha — MBA strengths | Five Spheres, strengths |
| [rohit-joshi.md](../eval/demos/rohit-joshi.md) | Rohit — Website | Personal website agent |
| [ananya-rao.md](../eval/demos/ananya-rao.md) | Ananya — Startup | GCS scoring, 6 dimensions |
| [mohammed-faizan.md](../eval/demos/mohammed-faizan.md) | Faizan — Crisis re-entry | Wellbeing → academic plan |
| [priya-venkatesh.md](../eval/demos/priya-venkatesh.md) | Priya — GATE + PhD | Research pathway |
| [suresh-babu.md](../eval/demos/suresh-babu.md) | Suresh — Wrong branch | Svadharma reframe |
