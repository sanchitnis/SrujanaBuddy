Analysis: REVA AI Hub — Current Protocol for the Three Main Coaching Threads

This analysis is based on the source code, data files, prompts, documentation, and agent configurations currently implemented in the repository. The system as it stands is a framework platform — it provides the scaffolding, prompts, gems (custom AI agents), and learning tracks, but the actual conversational AI interactions happen in external tools (Gemini, Claude, ChatGPT) using templates the system supplies. There is no live in-app conversational AI agent yet; the intelligence is in how the system guides students to configure external AI for each use case.



Thread 1: Aspiration Discovery, Milestone Planning \& Soft Skills Buddy

What the current system provides

The system approaches aspiration coaching through a tiered toolkit, not a single conversational flow:



1\. The AI Ascent Pathway (the primary milestone framework) This is the architectural backbone of Thread 1. It is a multi-year progression ladder differentiated by student discipline and role:



CSE/CSA → AI Citizen → AI Creator → AI Maker → AI Orchestrator → AI Systems Architect → AI Researcher (6 stages)

Engineering (non-CS) → same base, diverges at B3 (IoT, structural AI, predictive maintenance)

Commerce \& Management → Commerce Maker → AI Business Intelligence → AI Business Changemaker (3 stages + 2 universal)

Applied Sciences → branches to AI Data Explorer, then AI Researcher

Design \& Architecture → AI for Creative Impact → AI Changemaker

Human-Centered (Law, Liberal Arts, Education) → AI for Impact → AI Changemaker

Faculty → shorter 4-stage path terminating at AI for Impact

Each stage has explicit outcomes, tools, and courses attached. Progress is tracked in localStorage. This functions as the 3–4 year milestone ladder — it is not generated per student, but students self-select into a track and mark stages complete.



2\. Aspirations Coach Agent (primary aspiration buddy) A purpose-built AI agent (aspirations-coach) explicitly tagged for goal-setting, coaching, career, motivation, and personal-development. This is the closest current implementation to a buddy for aspiration discovery. It is an external AI agent skill — students click a link and interact conversationally with it.



3\. Career Guide  separate AI agent skill for professional career guidance, job search, and planning. This supplements the Aspirations Coach for students with near-term employment goals.



4\. Skill Gap Analysis Prompt (Kaizen track) A structured prompt that explicitly asks students to list their current sub-skills and proficiency levels, compares them to industry standards for a target role, identifies the top 3 critical gaps, and recommends resources (book, course, project) per gap. This is the diagnostic entry point for aspiration → gap → plan flow.



5\. Learning Reflection Prompt (Kaizen track) A weekly growth-mindset coaching conversation (sequential questions, awaiting student response to each) that culminates in a "Personal Growth Action Plan." This supports ongoing milestone check-ins.



6\. Goal Setting feature (Kaizen track) Named as a feature in the Kaizen pillar: "AI-assisted goal creation with actionable milestones and progress tracking." Currently referenced in the UI but milestone granularity (yearly/monthly/weekly/daily) is not implemented in-app — it relies on the Aspirations Coach Gem.



7\. Planning Resources (CS Market Forecast 2026–29) Provides market-level context (India's CS job market trends, talent-crunch roles, survival strategies) to anchor a student's aspirations against real-world opportunities.



Protocol flow by student condition

Student Condition	Current System Flow

First-year, no clear direction	Directed to Get Started → AI Ascent Pathway → selects track → sees full stage map as 3–4 year ladder → clicks Aspirations Coach Gem to open a conversational session

Mid-program, has a vague goal	Skill Gap Analysis prompt (Kaizen) → identifies gaps vs. target role → feeds results into Aspirations Coach Gem for refinement

Motivated with a specific target	Career Guide Gem + Planning Resources (market forecast) → grounds aspiration in market reality → Aspirations Coach Gem for milestone breakdown

Weekly progress review	Learning Reflection Prompt → produces Personal Growth Action Plan

Gaps vs. requirement

The aspiration discovery is not progressively conversational within the platform — it depends on external Gem sessions that are not persisted back into the hub.

Soft skills / enterprising skills (communication, leadership, entrepreneurial mindset) are named in the Kaizen track description but have no dedicated agent or structured path. The Consulting track's Simulation Scenarios prompt does develop decision-making and persuasion skills indirectly.

Milestone granularity (yearly → monthly → weekly → daily) is conceptually present in the AI Ascent stages but not configurable per student within the app.

The AI Ascent progress tracker (localStorage) does not feed back into a personalized coaching session.

Thread 2: Socratic Learning Buddy (Curriculum + Extra-Curricular Topics)

What the current system provides

1\. AI Tutor Activation Prompt (primary Socratic learning agent) This is the central Thread 2 implementation. Located in the Kaizen track (/track/kaizen/ai-tutor), it is a carefully engineered prompt template that students copy into any AI tool. It explicitly configures:



A 10-step personalized roadmap from the student's current level

A resource list (documentation, key concepts, project ideas)

A Knowledge Check (3 open-ended questions to test foundational understanding — not closed questions)

An ELI5 version of the hardest concept

Crucially: "Set up a Socratic Dialogue where you help me solve a small starter problem without giving me the direct code" — this is the explicit Socratic mode constraint

This prompt requires students to fill in \[Target Skill], \[Current Level], and \[Goal]. It works for both curriculum topics and personal interests outside the curriculum since the topic is student-defined.



2\. Course System with Module-Level Tracking (curriculum backbone) The portal (/portal/courses) provides enrolled courses with modules, materials (PPT, PDF, video, link, doc), and assignments with submission + grading status. The Docusaurus knowledge base publishes course syllabi with Bloom's taxonomy-aligned outcomes (e.g., AI Foundations: CO1 L2 → CO2 L3 → CO3 L5 → CO4 L6). This is the curriculum state that the AI Tutor should — but currently does not — automatically read.



3\. Differentiated Learning by Ascent Track (persona-based protocol) The AI Ascent Pathway determines what the Socratic learning looks like per persona:



CSE/CSA students at A2 level: the AI Tutor prompt focuses on spec-driven agentic coding with Cursor/Kiro — Socratic dialogue centers on architecture decisions and debugging, not giving code directly

Commerce students at M2: Socratic dialogue applied to business scenarios, financial analysis decisions, marketing strategy choices

Sciences students at C2: AI-assisted data analysis with Python-light, Socratic questioning around research hypothesis formation

Design students at E2: Socratic dialogue about generative design choices in Midjourney/Spline

4\. Student Engagement Tools prompt (for faculty-led sessions) Enables faculty to design Socratic classroom activities — AI acts as a "personified concept" or "historical figure" that students must engage through dialogue, "AI-powered discussion starters," and team-based synthesis. This is the classroom-level Socratic layer managed by faculty.



5\. Assessment Design prompt (maintaining Socratic integrity) The AI-Ready Assessment Design explicitly includes designing "Socratic Prompts" for students to use with AI tutors for specific topics, plus rubrics that evaluate "Human Insight" and "Critical Verification of AI Content." This creates the accountability layer so the Socratic method is not circumvented.



6\. Academic Integrity Policy (structural Socratic enforcement) The Student Guidelines explicitly prohibit submitting AI-generated content as original work and using AI to fabricate data. This policy forces students to use the AI tutor as a Socratic partner rather than an answer machine. The disclosure framework (minor vs. substantial use) is the behavioral reinforcement.



7\. Supporting Artifacts for specific topics



PyLingo Claude Artifact: gamified interactive Python learning (curriculum and extra-curricular)

Fourier Transform Explainer: interactive visual for STEM signal processing

Learning with YouTube Gem: extracts insights from external educational video content

Protocol flow by student condition

Student Condition	Current System Flow

Stuck on a curriculum assignment	Portal → enrolled course → module materials → copy AI Tutor prompt → paste into Gemini/Claude with \[Target Skill] = specific topic, \[Current Level] = current, \[Goal] = understand this concept for the assignment → Socratic dialogue initiated

Wants to learn outside curriculum	AI Ascent Pathway → identifies next stage tools (e.g., LangChain for A3) → AI Tutor prompt with that tool as \[Target Skill]

Faculty-structured session	Student Engagement prompt used by faculty → class works with AI as "personified concept" → students critique/debate AI output

Progress validation	"After completing a module with your AI tutor, try explaining the concept to a colleague or building a small 'Hello World' project" (explicit instruction in AITutor.tsx)

Gaps vs. requirement

No live in-app Socratic agent — interaction occurs in external tools; there is no session memory or curriculum-state awareness

The AI Tutor prompt does not read the student's current course status (enrolled modules, grades, assignment due dates) to auto-contextualize the Socratic dialogue

For extra-curricular topics, there is no differentiation in the Socratic approach based on whether the student is at F1 vs. A3 level (the template is the same)

Verification of mastery ("explain to a colleague or build a Hello World") is instructional text, not tracked

Thread 3: Counselling Support (First-Level Issues, Manodhara, Emergency)

What the current system provides

1\. REVA Heartbreak Navigator Gem (primary first-level counselling agent) This is the most developed counselling component. It is a live AI agent skill specifically built for REVA community members dealing with relationship break-ups, dating violence, and similar personal emotional challenges. It is:



Featured on the main Resources page as "Specialized AI support for wellbeing and relationship challenges on campus"

Tagged: wellbeing, student-support, mental-health, reva-specific

Built on a RAG (Retrieval-Augmented Generation) pipeline according to the research project entry: "Development of the RAG pipeline and fine-tuning of the emotional support agent for student wellbeing"

The backend research project lists LLM + RAG + Mental Health as its technology stack — this indicates domain-specific fine-tuning on REVA context

2\. Heartbreak Navigator Backend Research Project This is an active R\&D project (status: completed in 2024) by Dr. Sanjay Chitnis and Amit Kumar in AI \& ML department. The description: "Development of the RAG pipeline and fine-tuning of the emotional support agent for student wellbeing." This suggests the Gem is backed by domain-specific knowledge — likely REVA counselling policies, resource contacts, and wellbeing frameworks.



3\. Academic framework positioning The Staff AI Procedures and Student Guidelines emphasize that "AI is a support tool — not a replacement for human judgment." This is the de-escalation boundary for Thread 3: the system explicitly positions AI as first-level support, not clinical intervention.



Current protocol for Thread 3 (inferred from system design)

The Heartbreak Navigator Gem operates as a first-level emotional support layer:



Student initiates a AI agent skill conversation about a personal/relationship issue

The RAG pipeline retrieves relevant REVA-specific context (counselling resources, support policies)

The Gem provides empathetic first-level guidance

For issues beyond first-level scope, the expectation is referral to human services — but this referral pathway (to Manodhara or emergency services) is not yet implemented in the current frontend code

Critical gaps vs. requirement

Requirement	Current Status

First-level counselling for general issues	Partially met — Heartbreak Navigator Gem covers relationship/emotional issues

Manodhara integration	Not present in current codebase — no link, contact, or routing to REVA's Manodhara service

Emergency situation protocol	Absent — no crisis detection, no emergency escalation pathway, no hotline integration

Breadth of counselling issues (beyond heartbreak)	Limited — the current Gem is relationship-specific; academic stress, family issues, mental health crises have no dedicated agent

Differentiation by student persona	None — the same Gem is available to all; no persona-aware first-contact protocol

Cross-Cutting Observation: How Persona-Based Protocol Differentiation Currently Works

The system's primary differentiation mechanism is the AI Ascent Track selection at /get-started. This is where the coach/student interaction diverges:



Persona	Track	Thread 1 Aspiration Path	Thread 2 Learning Mode	Thread 3 Counselling

CSE 1st year	A	F1→F2→A1 (build apps without code)	Coding-focused Socratic (spec-driven, no direct code)	Heartbreak Navigator

CSE 3rd year	A3/A4	Full 6-stage ladder visible; AI Researcher as capstone	LangChain/API Socratic dialogue	Heartbreak Navigator

Commerce student	C	M1→M2→M3 (business automation focus)	Business scenario Socratic, financial decision-making	Heartbreak Navigator

Sciences student	D	C2 Data Explorer branch	Python-light + Jupyter Socratic, research hypothesis	Heartbreak Navigator

Law/Liberal Arts	F	D2 AI for Impact, D3 Changemaker	Domain-specific AI tools, policy analysis discussion	Heartbreak Navigator

Faculty	Faculty track	4-stage path (AI Citizen→Impact)	Teaching-focused: pedagogy, assessment design	Same as students

The critical observation: Thread 3 has zero persona differentiation — every student, regardless of condition, reaches the same single counselling gem. Threads 1 and 2 have track-based differentiation built into the framework but the differentiation is about learning content, not about coaching style or depth based on the student's current psychological or motivational condition.



Summary for the Expert Coach

What works well in the current system:



The AI Ascent Pathway provides a coherent 3–4 year milestone framework differentiated by discipline — it is the clearest operationalization of Thread 1's long-horizon planning

The Socratic mode is explicitly encoded in the AI Tutor prompt ("without giving the direct code") — the intention is correct

The Heartbreak Navigator Gem represents a serious investment in Thread 3 with an actual RAG-backed counselling agent

The Kaizen track's Learning Reflection + Skill Gap Analysis prompts form a functional weekly coaching loop

What needs to be built for the vision to be fully realized:



Thread 1: A conversational in-app aspiration discovery flow that progressively elicits goals (rather than requiring students to navigate to an external Gem), persists across sessions, and generates personalized milestone plans (yearly → monthly → weekly → daily)

Thread 2: Linking the AI Tutor to the student's actual course enrollment status so the Socratic dialogue is automatically contextualized to their current curriculum standing

Thread 3: A protocol layer that: (a) extends counselling coverage beyond relationship issues, (b) integrates Manodhara as a human escalation pathway, and (c) implements emergency detection with immediate routing — the RAG infrastructure already built for the Heartbreak Navigator is the right foundation to expand from

