# AI Engineer Career Pathways
*Source: AIEngineer-interview-university (CC-BY-SA-4.0, sanchitnis / jwasham). Adapted for REVA University student context. deeplearning.ai course links are free to audit at time of writing.*
# AI Engineer Career Pathways
## A Microlearning-Based Achievement Guide for REVA Students

> **Source**: Adapted from [AIEngineer-interview-university](https://github.com/sanchitnis/AIEngineer-interview-university) by sanchitnis (CC-BY-SA-4.0), with REVA student context applied.
>
> **For**: Career Pathway Coach — use this file to guide students targeting AI engineering roles.
>
> **Philosophy**: Each pathway is structured as four achievement levels that mirror the Srujana Pathway stages. A student advances when they produce the stage milestone evidence — progression is readiness-based, not semester-gated.

---

## How to Choose Your Pathway — 5-Question Self-Assessment

Ask the student these five questions. Tally the letters and map to a pathway.

| # | Question | A | B | C | D | E | F |
|---|----------|---|---|---|---|---|---|
| 1 | When I imagine myself at work in 5 years, I see myself... | Shipping AI-powered products fast | Training and deploying ML models at an AI lab | Analysing data and building dashboards/models | Reading papers and doing experiments | Setting product direction for an AI team | Defending systems from AI-powered attacks |
| 2 | My favourite part of a CS project is... | Building something users can actually use | Getting the model to work better | Finding patterns in data | Understanding why something works mathematically | Defining what should be built and why | Finding vulnerabilities before others do |
| 3 | I am most comfortable with... | APIs, tools, building quickly | Python, PyTorch, training loops | Excel/SQL, statistics, visualisation | Proofs, papers, mathematical derivations | Strategy, communication, product specs | Security, networking, threat modelling |
| 4 | My immediate goal is... | Get a software/product job with AI skills | Join an AI lab or ML team | Join a data analytics/science team | Publish research or pursue a master's/PhD | Lead AI projects as a PM or consultant | Work in cybersecurity with AI specialisation |
| 5 | I am willing to spend how long on this pathway? | 6–9 months | 9–15 months | 6–9 months | 12–18 months | 4–6 months | 9–12 months |

**Tally**: Mostly **A** → Pathway 1 · Mostly **B** → Pathway 2 · Mostly **C** → Pathway 3 · Mostly **D** → Pathway 4 · Mostly **E** → Pathway 5 · Mostly **F** → Pathway 6

---

## Module Library

Full module definitions (48 modules across 8 categories) are in **[ai-engineer-modules.yaml](ai-engineer-modules.yaml)** — each entry has `key_concepts`, `resources`, `time_estimate`, and `completion_evidence`.

Module code prefixes: `ML-CS` · `ML-MATH` · `ML-AI` · `ML-BUILD` · `ML-DEEP` · `ML-HUMAN` · `ML-CAREER` · `ML-CYBER`

---

## Pathways

---

### Pathway 1 — AI-Native Builder
> *"I want to build products and systems using AI tools and LLMs as my primary accelerants."*

**Who this is for**: Product engineers, technical founders, and full-stack developers who build with AI, not just alongside it.

**Total estimated time**: 6–9 months

---

#### Stage 1 — Foundation
*Goal: Become a capable Python developer who can work with AI tools fluently and understands how to build with a spec.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CS-01 | Python Fluency | 1–2 weeks |
| ML-CS-03 | Git & GitHub | 3–5 days |
| ML-CS-04 | Linux / Terminal Basics | 2–3 days |
| ML-BUILD-01 | AI-native SDLC & Spec-Driven Development | 3–5 days |
| ML-BUILD-02 | AI Coding Tools | 3–5 days |
| ML-HUMAN-01 | Communication & Storytelling | 1 week (baseline) |
| ML-HUMAN-03 | Ethics & Responsibility in AI | 3–5 days |
| ML-CAREER-01 | GitHub Portfolio & Open Source | 1 day setup |

**Stage milestone**: Build one small AI-assisted project (e.g. a CLI tool or script) using spec-driven development with a coding assistant; push it to a public GitHub repo with a clean README.

---

#### Stage 2 — Application
*Goal: Build and ship real AI-powered features using LLM APIs, RAG, and cloud infrastructure.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CS-06 | Databases & SQL Basics | 1 week |
| ML-AI-05 | Prompting Techniques | 3–5 days |
| ML-AI-06 | RAG — Retrieval-Augmented Generation | 1–2 weeks |
| ML-BUILD-03 | Full-Stack Basics for AI Apps | 1–2 weeks |
| ML-BUILD-04 | Product Engineering with AI | 1–2 weeks |
| ML-BUILD-06 | Cloud Fundamentals | 1–2 weeks |
| ML-CAREER-03 | Coding Interview Preparation (begin) | ongoing |

**Stage milestone**: Ship a deployed AI product feature — a RAG chatbot or LLM-powered tool — accessible via a public URL, with at least one graceful fallback for model failure.

---

#### Stage 3 — Creation
*Goal: Design and build complete AI product systems; understand production constraints.*

| Module | Topic | Time |
|--------|-------|------|
| ML-BUILD-05 | Systems Architecture for AI Products | 2–3 weeks |
| ML-AI-07 | LLM Agents & Agentic Systems | 2–3 weeks |
| ML-BUILD-09 | Vector Databases & Embeddings | 3–5 days |
| ML-BUILD-08 | MLOps & AI Infrastructure (production basics) | 2–3 weeks |
| ML-HUMAN-02 | Critical Thinking & Problem Framing | ongoing |
| ML-CAREER-06 | Showcase Project — Build & Deploy | 2–4 weeks |

**Stage milestone**: A deployed AI system with a documented architecture diagram, observable logging, and a public showcase project on HuggingFace Spaces or cloud.

---

#### Stage 4 — Enterprise
*Goal: Interview-ready and placement-ready for AI-native builder roles.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CAREER-03 | Coding Interview Preparation (complete) | ongoing |
| ML-CAREER-04 | AI System Design Interview Prep | 2–4 weeks |
| ML-CAREER-02 | Resume & LinkedIn for AI Roles | 3–5 days |
| ML-BUILD-07 | Data Engineering on the Cloud (optional depth) | 2–3 weeks |
| ML-HUMAN-04 | Collaboration & Team Engineering | ongoing |

**Stage milestone**: Interview-ready portfolio (3+ deployed projects); can whiteboard 2 AI system designs; 100+ LeetCode problems solved; tailored resume reviewed by mentor.

**Target roles**: Product Engineer (AI), Full-Stack AI Engineer, AI Startup Founding Engineer, Technical Co-founder

---

### Pathway 2 — AI Systems Engineer
> *"I want to build the AI systems themselves — train models, fine-tune LLMs, architect agentic pipelines."*

**Who this is for**: Engineers who want to work directly on AI systems at labs or AI-first companies.

**Total estimated time**: 9–15 months

---

#### Stage 1 — Foundation
*Goal: Build the mathematical and CS foundations required for deep AI engineering work.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CS-01 | Python Fluency | 1–2 weeks |
| ML-CS-02 | Data Structures & Algorithms | 4–6 weeks |
| ML-CS-03 | Git & GitHub | 3–5 days |
| ML-CS-04 | Linux / Terminal Basics | 2–3 days |
| ML-MATH-01 | Linear Algebra for ML | 2–3 weeks |
| ML-MATH-02 | Calculus & Optimization | 2 weeks |
| ML-MATH-03 | Probability & Statistics | 2–3 weeks |
| ML-MATH-04 | Information Theory | 3–5 days |
| ML-HUMAN-03 | Ethics & Responsibility in AI | 3–5 days |

**Stage milestone**: Implement PCA from scratch; implement gradient descent from scratch; solve 30+ LeetCode problems; write a 1-page explanation of cross-entropy loss and KL divergence without referencing notes.

---

#### Stage 2 — Application
*Goal: Understand and apply the full modern ML stack; work with LLMs and build RAG systems.*

| Module | Topic | Time |
|--------|-------|------|
| ML-AI-01 | Machine Learning Fundamentals | 3–4 weeks |
| ML-AI-02 | Deep Learning Foundations | 3–4 weeks |
| ML-AI-03 | Transformers & Attention | 1–2 weeks |
| ML-AI-04 | Large Language Models & Generative AI | 2–3 weeks |
| ML-AI-05 | Prompting Techniques | 3–5 days |
| ML-AI-06 | RAG | 1–2 weeks |
| ML-BUILD-08 | MLOps & AI Infrastructure (basics) | 2 weeks |
| ML-CAREER-05 | Kaggle & ML Competitions (begin) | ongoing |

**Stage milestone**: Train a CNN on a real dataset; build a working RAG system; fine-tune a HuggingFace model; achieve a public Kaggle score on any competition.

---

#### Stage 3 — Creation
*Goal: Own the deep technical stack — agentic systems, fine-tuning, data curation, distillation.*

| Module | Topic | Time |
|--------|-------|------|
| ML-AI-07 | LLM Agents & Agentic Systems | 2–3 weeks |
| ML-AI-08 | LLM Fine-tuning (LoRA, QLoRA, RLHF) | 2–3 weeks |
| ML-AI-09 | LLM Evaluation | 1 week |
| ML-DEEP-01 | Knowledge Distillation | 1–2 weeks |
| ML-DEEP-02 | Data Collection & Curation | 1–2 weeks |
| ML-DEEP-03 | Synthetic Data Generation | 1 week |
| ML-DEEP-04 | Multi-Agent AI Systems | 1–2 weeks |
| ML-BUILD-09 | Vector Databases & Embeddings | 3–5 days |
| ML-CAREER-01 | GitHub Portfolio & Open Source (active contribution) | ongoing |

**Stage milestone**: Fine-tune a 7B model using QLoRA on a custom dataset; run a distillation experiment; build a 3-agent system; curate a 500+ example dataset with a data card.

---

#### Stage 4 — Enterprise
*Goal: Interview-ready for AI Engineer roles at AI labs and AI-first companies.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CAREER-02 | Resume & LinkedIn for AI Roles | 3–5 days |
| ML-CAREER-03 | Coding Interview Preparation (complete) | ongoing |
| ML-CAREER-04 | AI System Design Interview Prep | 2–4 weeks |
| ML-BUILD-08 | MLOps & AI Infrastructure (production depth) | 2–3 weeks |
| ML-BUILD-07 | Data Engineering on the Cloud | 2–3 weeks |
| ML-CS-05 | Design Patterns | 1–2 weeks |

**Stage milestone**: Can design an end-to-end ML system on a whiteboard; 100+ LeetCode problems; fine-tuning and evaluation project on GitHub; Kaggle medal or a deployed open-source model on HuggingFace.

**Target roles**: AI Engineer, ML Engineer, LLM Engineer, Research Engineer, AI Infrastructure Engineer

---

### Pathway 3 — Data Science & Analytics
> *"I want to work with data — build models, generate insights, and drive decisions."*

**Who this is for**: Fresh CS students interested in data-driven roles at product companies, banks, e-commerce, healthcare, and consulting.

**Total estimated time**: 6–9 months

---

#### Stage 1 — Foundation
*Goal: Python + data manipulation + statistical foundations.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CS-01 | Python Fluency (focus on pandas/NumPy) | 1–2 weeks |
| ML-CS-06 | Databases & SQL Basics | 1 week |
| ML-CS-03 | Git & GitHub | 3–5 days |
| ML-MATH-01 | Linear Algebra for ML | 2–3 weeks |
| ML-MATH-03 | Probability & Statistics | 2–3 weeks |
| ML-HUMAN-03 | Ethics & Responsibility in AI | 3–5 days |

**Stage milestone**: Clean and analyse a real dataset with Python (pandas + matplotlib); write 10 SQL queries on the same dataset; explain the Central Limit Theorem to a peer.

---

#### Stage 2 — Application
*Goal: Apply ML to real problems; deploy data pipelines; work with cloud data tools.*

| Module | Topic | Time |
|--------|-------|------|
| ML-AI-01 | Machine Learning Fundamentals | 3–4 weeks |
| ML-CS-02 | Data Structures & Algorithms (focus on arrays, sorting, graphs) | 2–3 weeks |
| ML-BUILD-06 | Cloud Fundamentals | 1–2 weeks |
| ML-BUILD-07 | Data Engineering on the Cloud | 2–3 weeks |
| ML-CAREER-05 | Kaggle & ML Competitions (begin) | ongoing |

**Stage milestone**: Build an end-to-end ML pipeline on a cloud data warehouse; enter and complete a Kaggle competition; deploy a simple Streamlit dashboard from a cloud data source.

---

#### Stage 3 — Creation
*Goal: Move beyond basic ML; incorporate deep learning and language/embedding techniques.*

| Module | Topic | Time |
|--------|-------|------|
| ML-AI-02 | Deep Learning Foundations (intro: neural nets + basic CNN) | 2–3 weeks |
| ML-AI-06 | RAG & Embeddings (for text/document analytics) | 1–2 weeks |
| ML-BUILD-09 | Vector Databases & Embeddings | 3–5 days |
| ML-BUILD-03 | Full-Stack Basics for AI Apps | 1–2 weeks |
| ML-HUMAN-01 | Communication & Storytelling (data storytelling focus) | 1 week |
| ML-CAREER-06 | Showcase Project — Build & Deploy | 2–4 weeks |

**Stage milestone**: Deploy a data science project that includes a semantic search or text analytics component; Kaggle public notebook with 10+ upvotes; present findings to a non-technical audience.

---

#### Stage 4 — Enterprise
*Goal: Interview-ready for data science and analytics engineering roles.*

| Module | Topic | Time |
|--------|-------|------|
| ML-BUILD-08 | MLOps & AI Infrastructure (basic: experiment tracking + model serving) | 2 weeks |
| ML-CAREER-04 | AI System Design Interview Prep (focus: recommendation and search) | 2–4 weeks |
| ML-CAREER-02 | Resume & LinkedIn for Data Science Roles | 3–5 days |
| ML-CAREER-03 | Coding Interview Preparation (SQL + Python focus) | 4 weeks |

**Stage milestone**: Interview-ready: 3+ projects deployed; SQL + Python interview readiness; can design a recommendation system or fraud detection pipeline on a whiteboard.

**Target roles**: Data Scientist, Analytics Engineer, ML Engineer (product companies), Data Analyst (AI-powered), Business Intelligence Engineer

---

### Pathway 4 — ML Research Analyst
> *"I want to understand AI deeply — publish research, pursue a master's/PhD, or join a research team."*

**Who this is for**: Students aiming for graduate school, research internships, or research engineering roles.

**Total estimated time**: 12–18 months

---

#### Stage 1 — Foundation
*Goal: Strong mathematical and theoretical CS foundations — the bedrock of research.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CS-01 | Python Fluency | 1–2 weeks |
| ML-CS-02 | Data Structures & Algorithms | 4–6 weeks |
| ML-MATH-01 | Linear Algebra for ML | 2–3 weeks |
| ML-MATH-02 | Calculus & Optimization | 2 weeks |
| ML-MATH-03 | Probability & Statistics | 2–3 weeks |
| ML-MATH-04 | Information Theory | 3–5 days |
| ML-HUMAN-03 | Ethics & Responsibility in AI | 3–5 days |

**Stage milestone**: Implement backpropagation from scratch; derive cross-entropy loss from MLE first principles; solve 30+ LeetCode problems; read and summarise one seminal ML paper (AlexNet or Attention Is All You Need).

---

#### Stage 2 — Application
*Goal: Understand the full modern ML stack and begin working with the research literature.*

| Module | Topic | Time |
|--------|-------|------|
| ML-AI-01 | Machine Learning Fundamentals | 3–4 weeks |
| ML-AI-02 | Deep Learning Foundations | 3–4 weeks |
| ML-AI-03 | Transformers & Attention | 1–2 weeks |
| ML-AI-04 | Large Language Models & Generative AI | 2–3 weeks |
| ML-CAREER-05 | Kaggle & ML Competitions | ongoing |

**Seminal papers to read** (required):
- [Attention Is All You Need — Vaswani et al. 2017](https://arxiv.org/abs/1706.03762)
- [BERT — Devlin et al. 2018](https://arxiv.org/abs/1810.04805)
- [GPT-3 — Brown et al. 2020](https://arxiv.org/abs/2005.14165)
- [InstructGPT (RLHF) — Ouyang et al. 2022](https://arxiv.org/abs/2203.02155)
- [AlexNet — Krizhevsky et al. 2012](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)

**Stage milestone**: Train a Transformer from scratch (Karpathy's nanoGPT); write a 1-page critique of one seminal paper; achieve a Kaggle public score on any competition.

---

#### Stage 3 — Creation
*Goal: Run experiments, replicate results, evaluate models, and produce research artefacts.*

| Module | Topic | Time |
|--------|-------|------|
| ML-AI-08 | LLM Fine-tuning | 2–3 weeks |
| ML-AI-09 | LLM Evaluation | 1 week |
| ML-DEEP-01 | Knowledge Distillation | 1–2 weeks |
| ML-BUILD-08 | MLOps (experiment tracking with W&B/MLflow) | 2 weeks |
| ML-HUMAN-01 | Communication & Storytelling (research writing focus) | 1 week |
| ML-CAREER-01 | GitHub Portfolio (research repos and replication projects) | ongoing |

**Stage milestone**: Replicate the results of one published paper (even at small scale); write a 3-page research-style report with method, results, and limitations; contribute to an open-source ML project.

---

#### Stage 4 — Enterprise
*Goal: Ready for research internships, grad school applications, or research engineering roles.*

| Module | Topic | Time |
|--------|-------|------|
| ML-DEEP-02 | Data Collection & Curation | 1–2 weeks |
| ML-DEEP-03 | Synthetic Data Generation | 1 week |
| ML-DEEP-04 | Multi-Agent AI Systems | 1–2 weeks |
| ML-CAREER-02 | Resume for Research Roles | 3–5 days |
| ML-CAREER-04 | AI System Design Interview (research engineering) | 2–4 weeks |

**Stage milestone**: Statement of purpose drafted for top 3 target programs; research portfolio with replication study, fine-tuning experiment, and a novel (small) research contribution; active GitHub with ML research repos.

**Target roles**: Research Engineer, ML Research Intern, Research Scientist (entry), Graduate School (M.Tech / MS / PhD), AI Research Analyst

---

### Pathway 5 — AI Product & Strategy
> *"I want to lead AI products — define what gets built, why, and for whom."*

**Who this is for**: Students who want to work as AI Product Managers, AI Consultants, or strategy leads. Lighter technical depth; stronger product, communication, and systems-thinking emphasis.

**Total estimated time**: 4–6 months

---

#### Stage 1 — Foundation
*Goal: Become AI-literate at a level that enables confident product leadership.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CS-01L | Python Lite for Non-Engineers | 3–5 days |
| ML-AI-05 | Prompting Techniques | 3–5 days |
| ML-HUMAN-03 | Ethics & Responsibility in AI | 3–5 days |
| ML-HUMAN-01 | Communication & Storytelling | 1 week (baseline) |
| ML-HUMAN-02 | Critical Thinking & Problem Framing | ongoing |

**Recommended reading**: [AI for Everyone — Andrew Ng (Coursera, free to audit)](https://www.deeplearning.ai/courses/ai-for-everyone/)

**Stage milestone**: Complete AI for Everyone; build one simple prompt-based tool using an LLM API; write a 1-page "AI opportunity brief" for a real problem in any domain.

---

#### Stage 2 — Application
*Goal: Learn how AI features are designed and evaluated; develop product intuition for AI.*

| Module | Topic | Time |
|--------|-------|------|
| ML-BUILD-04 | Product Engineering with AI | 1–2 weeks |
| ML-BUILD-01 | AI-native SDLC & Spec-Driven Development | 3–5 days |
| ML-AI-07 | LLM Agents (conceptual: what agents can and cannot do) | 1 week |
| ML-HUMAN-04 | Collaboration & Team Engineering | ongoing |

**Stage milestone**: Write a complete product spec for an AI-powered feature (user story → acceptance criteria → technical design → evaluation plan); present it to a peer in a 10-minute mock review.

---

#### Stage 3 — Creation
*Goal: Design end-to-end AI products and lead cross-functional teams building them.*

| Module | Topic | Time |
|--------|-------|------|
| ML-AI-06 | RAG (conceptual: when and why to use it) | 3–5 days |
| ML-BUILD-05 | Systems Architecture for AI Products (conceptual) | 1–2 weeks |
| ML-CAREER-06 | Showcase Project (product spec + prototype) | 2–3 weeks |
| ML-HUMAN-01 | Communication: Executive storytelling + stakeholder management | ongoing |

**Stage milestone**: One end-to-end AI product case study: problem brief → user research → product spec → architecture diagram → evaluation plan → go-to-market brief. Presentable to a non-technical panel.

---

#### Stage 4 — Enterprise
*Goal: Interview-ready for AI Product Manager and AI strategy roles.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CAREER-04 | AI System Design Interview (product design track) | 2–3 weeks |
| ML-CAREER-02 | Resume & LinkedIn for PM/Strategy Roles | 3–5 days |
| ML-HUMAN-03 | Ethics: AI governance and responsible product decisions | 3–5 days |

**Stage milestone**: Can run a 45-minute product design interview for an AI feature; portfolio of 2–3 product case studies; LinkedIn profile with a clear AI product leadership narrative.

**Target roles**: AI Product Manager, AI Strategy Consultant, Technical Product Manager (AI), AI Program Manager, Chief of Staff (AI-first companies)

---

### Pathway 6 — Cybersecurity & AI
> *"I want to specialise at the intersection of AI and security — building and defending AI-powered systems."*

**Who this is for**: Students interested in cybersecurity careers who want to leverage AI for threat detection, or who want to defend AI systems from adversarial attack and misuse.

**Total estimated time**: 9–12 months

---

#### Stage 1 — Foundation
*Goal: Solid CS fundamentals + security mindset + Python.*

| Module | Topic | Time |
|--------|-------|------|
| ML-CS-01 | Python Fluency | 1–2 weeks |
| ML-CS-02 | Data Structures & Algorithms | 4–6 weeks |
| ML-CS-03 | Git & GitHub | 3–5 days |
| ML-CS-04 | Linux / Terminal Basics | 2–3 days |
| ML-CS-07 | Networking Fundamentals | 1 week |
| ML-CYBER-01 | Computer Security Fundamentals | 1–2 weeks |
| ML-HUMAN-03 | Ethics & Responsibility in AI | 3–5 days |

**Stage milestone**: Perform a basic OWASP review on a sample web application; write a threat model for a simple AI-powered system; solve 30+ LeetCode problems.

---

#### Stage 2 — Application
*Goal: Apply ML to security problems; build anomaly detection and classification systems.*

| Module | Topic | Time |
|--------|-------|------|
| ML-MATH-03 | Probability & Statistics | 2–3 weeks |
| ML-AI-01 | Machine Learning Fundamentals | 3–4 weeks |
| ML-CYBER-02 | ML for Security (anomaly detection, intrusion detection) | 2–3 weeks |
| ML-AI-05 | Prompting Techniques | 3–5 days |
| ML-BUILD-06 | Cloud Fundamentals | 1–2 weeks |

**Stage milestone**: Build a fraud or network intrusion detection system on a public dataset; document the false positive/negative tradeoff; deploy a basic detection API.

---

#### Stage 3 — Creation
*Goal: Understand adversarial AI and LLM-specific security threats; build defensive tooling.*

| Module | Topic | Time |
|--------|-------|------|
| ML-AI-04 | Large Language Models & Generative AI | 2–3 weeks |
| ML-CYBER-03 | Adversarial ML & Robustness | 1–2 weeks |
| ML-CYBER-04 | LLM Security & Prompt Injection | 1 week |
| ML-AI-07 | LLM Agents (security angle: sandboxing, privilege separation) | 1–2 weeks |
| ML-CAREER-06 | Showcase Project (security + AI angle) | 2–4 weeks |

**Stage milestone**: Demonstrate an FGSM adversarial attack and a defence; demonstrate a prompt injection attack and two mitigations; build and deploy a security-focused AI tool as a showcase project.

---

#### Stage 4 — Enterprise
*Goal: Interview-ready for cybersecurity roles with AI specialisation.*

| Module | Topic | Time |
|--------|-------|------|
| ML-BUILD-08 | MLOps & AI Infrastructure (security-focused: monitoring + threat detection logging) | 2 weeks |
| ML-CAREER-04 | AI System Design Interview (security system design track) | 2–4 weeks |
| ML-CAREER-02 | Resume & LinkedIn for Cybersecurity + AI Roles | 3–5 days |
| ML-CAREER-03 | Coding Interview Preparation | ongoing |

**Stage milestone**: Can design a fraud detection pipeline or LLM security architecture on a whiteboard; showcase project deployed; responsible disclosure brief written for one discovered vulnerability (simulated environment only).

**Target roles**: AI Security Engineer, ML Security Researcher, Threat Detection Engineer, Red Team AI Specialist (authorised testing contexts), Security Data Scientist

---

## Cross-Pathway Module Map

`●` = required · `○` = optional / recommended

| Module | P1 Builder | P2 Systems | P3 Data | P4 Research | P5 Product | P6 Security |
|--------|:----------:|:----------:|:-------:|:-----------:|:----------:|:-----------:|
| ML-CS-01 Python | ● | ● | ● | ● | | ● |
| ML-CS-01L Python Lite | | | | | ● | |
| ML-CS-02 DSA | ○ | ● | ● | ● | | ● |
| ML-CS-03 Git | ● | ● | ● | ● | | ● |
| ML-CS-04 Linux | ● | ● | | | | ● |
| ML-CS-05 Design Patterns | | ● | | | | |
| ML-CS-06 SQL | ● | | ● | | | |
| ML-CS-07 Networking | | | | | | ● |
| ML-MATH-01 Linear Algebra | | ● | ● | ● | | |
| ML-MATH-02 Calculus | | ● | | ● | | |
| ML-MATH-03 Probability | | ● | ● | ● | | ● |
| ML-MATH-04 Info Theory | | ● | | ● | | |
| ML-AI-01 ML Fundamentals | | ● | ● | ● | | ● |
| ML-AI-02 Deep Learning | | ● | ● | ● | | |
| ML-AI-03 Transformers | | ● | | ● | | |
| ML-AI-04 LLMs | | ● | | ● | | ● |
| ML-AI-05 Prompting | ● | ● | | | ● | ● |
| ML-AI-06 RAG | ● | ● | ● | | ○ | |
| ML-AI-07 Agents | ● | ● | | | ○ | ● |
| ML-AI-08 Fine-tuning | | ● | | ● | | |
| ML-AI-09 Evaluation | | ● | | ● | | |
| ML-BUILD-01 SDLC | ● | | | | ● | |
| ML-BUILD-02 AI Coding Tools | ● | | | | | |
| ML-BUILD-03 Full-Stack | ● | | ● | | | |
| ML-BUILD-04 Product Eng | ● | | | | ● | |
| ML-BUILD-05 Architecture | ● | | | | ● | |
| ML-BUILD-06 Cloud | ● | | ● | | | ● |
| ML-BUILD-07 Data Eng | ○ | ● | ● | | | |
| ML-BUILD-08 MLOps | ● | ● | ● | ● | | ● |
| ML-BUILD-09 Vector DBs | ● | ● | ● | | | |
| ML-DEEP-01 Distillation | | ● | | ● | | |
| ML-DEEP-02 Data Curation | | ● | | ● | | |
| ML-DEEP-03 Synthetic Data | | ● | | ● | | |
| ML-DEEP-04 Multi-Agent | | ● | | ● | | |
| ML-HUMAN-01 Communication | ● | | | ● | ● | |
| ML-HUMAN-02 Critical Thinking | ● | | | | ● | |
| ML-HUMAN-03 Ethics | ● | ● | ● | ● | ● | ● |
| ML-HUMAN-04 Collaboration | ● | | | | ● | |
| ML-CAREER-01 GitHub | ● | ● | | ● | | |
| ML-CAREER-02 Resume | ● | ● | ● | ● | ● | ● |
| ML-CAREER-03 Coding Interview | ● | ● | ● | | | ● |
| ML-CAREER-04 System Design | ● | ● | ● | ● | ● | ● |
| ML-CAREER-05 Kaggle | | ● | ● | ● | | |
| ML-CAREER-06 Showcase Project | ● | | ● | | ● | ● |
| ML-CYBER-01 Security Basics | | | | | | ● |
| ML-CYBER-02 ML for Security | | | | | | ● |
| ML-CYBER-03 Adversarial ML | | | | | | ● |
| ML-CYBER-04 LLM Security | | | | | | ● |

---

## Coach Usage Notes

1. **Pathway selection**: Use the 5-question self-assessment at the top. If a student scores across multiple pathways, ask: *"Which matters more — building fast, or understanding deeply?"* Builder → P1. Deep understanding → P2.

2. **Stage transitions**: Progress when the student can produce the stage milestone evidence — not by calendar time. Use the milestone as a coaching checkpoint, not a syllabus gate.

3. **Combining pathways**: A student may start on P3 (Data Science) and transition to P2 (AI Systems) after Stage 2. The cross-pathway module map makes shared modules visible — no duplication needed.

4. **REVA curriculum integration**: Most REVA CS students already have partial credit for ML-CS-01, ML-CS-02, ML-MATH-01, and ML-MATH-03 by Year 2. Encourage them to treat coursework as their Foundation stage — and focus coaching energy on what comes after.

5. **USR/Jagruti integration**: ML-CYBER-02 (fraud/anomaly detection for social systems), ML-AI-07 (agentic systems for community service), and ML-BUILD-04 (AI product features for real users) all have natural USR applications. Encourage students to find community problems they can solve with their skills.

6. **Internship readiness signal**: Stage 2 completion of any pathway = internship-ready. Stage 3 completion = competitive placement and research program readiness.

7. **Ethics note**: All security and adversarial ML modules (ML-CYBER-03, ML-CYBER-04) are scoped to controlled, ethical, and authorised environments only — consistent with REVA's Universal Values (Ethics, Ownership, Involvement, Commitment).

---

*Source: AIEngineer-interview-university (CC-BY-SA-4.0, sanchitnis / jwasham). Adapted for REVA University student context. deeplearning.ai course links are free to audit at time of writing.*
