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

## Module Library — Shared Microlearning Topics

Modules are atomic learning units shared across multiple pathways. Each module has a code, key concepts, a primary resource, a time estimate, and a completion evidence criterion.

---

### ML-CS: CS Foundations

#### ML-CS-01: Python Fluency
- **Key concepts**: Variables, functions, classes, file I/O, list comprehensions, error handling, NumPy arrays, pandas DataFrames
- **Primary resource**: [Python for Everybody — Coursera (free to audit)](https://www.coursera.org/specializations/python) · [Real Python](https://realpython.com/) · [Exercism Python track](https://exercism.org/tracks/python)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Solve 10 LeetCode Easy problems in Python; write a pandas data-cleaning script on a real dataset

#### ML-CS-01L: Python Lite for Non-Engineers
- **Key concepts**: Variables, functions, loops, using AI libraries without deep programming knowledge
- **Primary resource**: [AI Python for Beginners — deeplearning.ai (free short course)](https://www.deeplearning.ai/short-courses/ai-python-for-beginners/)
- **Time estimate**: 3–5 days
- **Completion evidence**: Complete the course; write a short script that calls an LLM API and prints a response

#### ML-CS-02: Data Structures & Algorithms
- **Key concepts**: Big-O analysis, arrays, linked lists, stacks, queues, hash tables, trees (BST, heap), graphs (BFS, DFS), sorting (merge, quick), dynamic programming basics
- **Primary resource**: [Coding Interview Patterns (book)](https://geni.us/q7svoz) · [LeetCode (arrays, trees, graphs tags)](https://leetcode.com/) · [CS50 Harvard (YouTube)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- **Time estimate**: 4–6 weeks (parallel with other study — 2–3 problems/day)
- **Completion evidence**: Solve 50 LeetCode problems (Easy: 30, Medium: 20) with Python; implement a BST and a hash table from scratch

#### ML-CS-03: Git & GitHub
- **Key concepts**: Clone, branch, commit, merge, pull request, GitHub Actions (CI/CD basics), GitHub profile README
- **Primary resource**: [Learn Git Branching (interactive)](https://learngitbranching.js.org/) · [GitHub Skills](https://skills.github.com/)
- **Time estimate**: 3–5 days
- **Completion evidence**: Have a GitHub profile with a README; make one pull request to any open-source project (documentation counts)

#### ML-CS-04: Linux / Terminal Basics
- **Key concepts**: Navigation (cd, ls, mkdir), file manipulation, grep, pipes, environment variables, SSH, virtual environments (venv/conda)
- **Primary resource**: [Linux Command Line Basics — LabEx (free)](https://labex.io/tutorials/practice-linux-commands-hands-on-labs-398420)
- **Time estimate**: 2–3 days
- **Completion evidence**: Set up a Python virtual environment from the command line; write a bash script that automates a repetitive task

#### ML-CS-05: Design Patterns
- **Key concepts**: Strategy, singleton, factory, observer, decorator, adapter — with Python examples; SOLID principles
- **Primary resource**: [Head First Design Patterns (book)](https://www.amazon.com/Head-First-Design-Patterns-Freeman/dp/0596007124) · [Bob Martin SOLID (video)](https://www.youtube.com/watch?v=TMuno5RZNeE)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Refactor a personal project to use at least two design patterns; explain SOLID to a peer

#### ML-CS-06: Databases & SQL Basics
- **Key concepts**: SQL SELECT/JOIN/GROUP BY, relational vs. NoSQL tradeoffs, SQLite with Python, basic schema design
- **Primary resource**: [Mode Analytics SQL Tutorial (free)](https://mode.com/sql-tutorial/) · [SQLite + Python quickstart](https://docs.python.org/3/library/sqlite3.html)
- **Time estimate**: 1 week
- **Completion evidence**: Write 10 SQL queries on a real dataset (e.g. Kaggle); design and query a 3-table schema

#### ML-CS-07: Networking Fundamentals
- **Key concepts**: TCP/IP, HTTP/HTTPS, DNS, REST APIs, OSI model basics, SSL/TLS, sockets
- **Primary resource**: [Khan Academy — Computers and the Internet](https://www.khanacademy.org/computing/code-org/computers-and-the-internet) · [TCP/IP Explained (YouTube)](https://www.youtube.com/watch?v=e5DEVa9eSN0)
- **Time estimate**: 1 week
- **Completion evidence**: Explain how an HTTPS request works end-to-end; write a Python script that makes a REST API call and handles errors

---

### ML-MATH: Mathematics for AI

#### ML-MATH-01: Linear Algebra for ML
- **Key concepts**: Vectors, matrices, dot product, matrix multiplication, eigenvalues/eigenvectors, SVD, PCA (geometric intuition), orthogonality
- **Primary resource**: [Essence of Linear Algebra — 3Blue1Brown (YouTube)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2ZAgoSIREkZe0o) · [MIT 18.06 Gilbert Strang (OCW)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Implement PCA from scratch with NumPy; explain what happens geometrically during matrix multiplication

#### ML-MATH-02: Calculus & Optimization
- **Key concepts**: Partial derivatives, gradients, chain rule → backpropagation, gradient descent variants (SGD, Adam), convex vs. non-convex optimization, learning rate scheduling
- **Primary resource**: [Khan Academy — Multivariable Calculus](https://www.khanacademy.org/math/multivariable-calculus) · [CS231n Optimization Notes](https://cs231n.github.io/optimization-1/)
- **Time estimate**: 2 weeks
- **Completion evidence**: Implement gradient descent on a quadratic function; derive the chain rule for a 2-layer neural network by hand

#### ML-MATH-03: Probability & Statistics
- **Key concepts**: Probability distributions (Gaussian, Bernoulli, Categorical), Bayes' theorem, MLE and MAP estimation, hypothesis testing, A/B testing, Central Limit Theorem, confidence intervals
- **Primary resource**: [Khan Academy — Statistics and Probability](https://www.khanacademy.org/math/statistics-probability) · [Think Stats — free book (Allen Downey)](https://greenteapress.com/thinkstats2/)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Run an A/B test analysis on a real dataset; implement MLE for a Gaussian from scratch

#### ML-MATH-04: Information Theory
- **Key concepts**: Entropy, cross-entropy loss (why it works for classification), KL divergence (used in VAEs, RLHF, distillation), mutual information
- **Primary resource**: [Visual Information Theory — Chris Olah (blog)](https://colah.github.io/posts/2015-09-Visual-Information/)
- **Time estimate**: 3–5 days
- **Completion evidence**: Explain cross-entropy loss intuitively; derive the KL divergence formula and name two places it appears in modern ML

---

### ML-AI: AI/ML Core

#### ML-AI-01: Machine Learning Fundamentals
- **Key concepts**: Supervised learning (linear regression, logistic regression, SVM, decision trees, gradient boosting), unsupervised learning (k-means, PCA), bias-variance tradeoff, regularisation, cross-validation, feature engineering, evaluation metrics
- **Primary resource**: [Hands-On ML with Scikit-Learn (book)](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) · [Machine Learning Specialisation — Andrew Ng (Coursera, free to audit)](https://www.coursera.org/specializations/machine-learning-introduction)
- **Time estimate**: 3–4 weeks
- **Completion evidence**: Build an end-to-end ML pipeline (data → model → evaluation) for a real dataset; achieve a Kaggle public score on any beginner competition

#### ML-AI-02: Deep Learning Foundations
- **Key concepts**: Neural network forward/backward pass, activation functions, loss functions, weight initialisation, batch normalisation, dropout, training techniques (Adam, gradient clipping), CNNs, RNNs, LSTMs
- **Primary resource**: [Deep Learning Specialisation — Andrew Ng (Coursera)](https://www.deeplearning.ai/courses/deep-learning-specialization/) · [fast.ai Practical Deep Learning (free)](https://course.fast.ai/) · [Deep Learning book — Goodfellow et al. (free online)](https://www.deeplearningbook.org/)
- **Time estimate**: 3–4 weeks
- **Completion evidence**: Implement a 2-layer neural network with backprop from scratch using NumPy; train a CNN on CIFAR-10 with >80% accuracy

#### ML-AI-03: Transformers & Attention
- **Key concepts**: Self-attention (Q, K, V, scaled dot-product), multi-head attention, positional encoding, encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5), residual connections, layer normalisation
- **Primary resource**: [Illustrated Transformer — Jay Alammar (blog)](https://jalammar.github.io/illustrated-transformer/) · [Attention Is All You Need — Vaswani et al. 2017 (paper)](https://arxiv.org/abs/1706.03762) · [Neural Networks: Zero to Hero — Karpathy (YouTube)](https://karpathy.ai/zero-to-hero.html)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Implement scaled dot-product attention in PyTorch; explain the difference between encoder-only and decoder-only architectures with a use-case example

#### ML-AI-04: Large Language Models & Generative AI
- **Key concepts**: LLM architecture overview, pre-training objectives, scaling laws, tokenisation, instruction tuning, RLHF, ChatGPT alignment, GPT vs. BERT families, context windows, temperature and sampling
- **Primary resource**: [Generative AI with LLMs — Coursera (deeplearning.ai)](https://www.deeplearning.ai/courses/generative-ai-with-llms/) · [HuggingFace NLP Course (free)](https://huggingface.co/learn/nlp-course/) · [LLM Course — Maxime Labonne (free GitHub)](https://github.com/mlabonne/llm-course)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Load and query a HuggingFace model; explain RLHF to a non-technical peer; describe how ChatGPT differs from base GPT

#### ML-AI-05: Prompting Techniques
- **Key concepts**: Zero-shot, few-shot, chain-of-thought (CoT), self-consistency, structured output/JSON mode, function calling/tool use, system prompts, prompt injection risks
- **Primary resource**: [ChatGPT Prompt Engineering for Developers — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) · [Building Systems with ChatGPT API — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/)
- **Time estimate**: 3–5 days
- **Completion evidence**: Build a chain-of-thought prompt that solves a multi-step reasoning problem; demonstrate function calling with the OpenAI or Anthropic API

#### ML-AI-06: RAG — Retrieval-Augmented Generation
- **Key concepts**: When to use RAG vs. fine-tuning, document loading and chunking, embedding models, vector databases (Pinecone, ChromaDB, Weaviate), similarity search, retrieval pipeline, re-ranking, evaluation of RAG quality
- **Primary resource**: [LangChain: Chat with Your Data — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/) · [Building & Evaluating Advanced RAG — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) · [Vector Databases from Embeddings to Applications — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Build a working RAG chatbot over a custom PDF/document set; evaluate retrieval quality with at least 10 test queries

#### ML-AI-07: LLM Agents & Agentic Systems
- **Key concepts**: The agentic loop (Observe → Think → Act), ReAct pattern, tool use, planning strategies (Plan-and-Execute, Tree of Thought), memory architectures (in-context, external vector store), multi-agent orchestration, error recovery, human-in-the-loop
- **Primary resource**: [AI Agents in LangGraph — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) · [Multi AI Agent Systems with crewAI — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) · [Building Effective Agents — Anthropic blog](https://www.anthropic.com/research/building-effective-agents) · [HuggingFace Agents Course (free)](https://huggingface.co/learn/agents-course/)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Build a 2-tool agent that completes a multi-step task; demonstrate error recovery when a tool fails

#### ML-AI-08: LLM Fine-tuning (LoRA, QLoRA, RLHF)
- **Key concepts**: When to fine-tune vs. RAG, supervised fine-tuning (SFT), instruction tuning dataset formats, LoRA (low-rank adapters), QLoRA (quantised LoRA for consumer GPUs), DPO as RLHF alternative, evaluation after fine-tuning
- **Primary resource**: [Finetuning Large Language Models — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/) · [LlamaFactory (GitHub)](https://github.com/hiyouga/LLaMA-Factory) · [Unsloth (GitHub)](https://github.com/unslothai/unsloth)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Fine-tune a small open-source LLM (e.g. Llama or Mistral 7B) using QLoRA on a custom dataset of at least 500 examples; compare outputs before and after fine-tuning

#### ML-AI-09: LLM Evaluation
- **Key concepts**: Golden test sets, automatic metrics (BLEU, ROUGE, METEOR — limitations), LLM-as-judge, RAGAS for RAG evaluation, human evaluation design, model cards, hallucination detection, task completion rate
- **Primary resource**: [Evaluating and Debugging Generative AI — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/evaluating-debugging-generative-ai/) · [Building & Evaluating Advanced RAG — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)
- **Time estimate**: 1 week
- **Completion evidence**: Build an evaluation harness with at least 20 test cases for an LLM feature; use an LLM-as-judge to score outputs automatically

---

### ML-BUILD: Building & Infrastructure

#### ML-BUILD-01: AI-native SDLC & Spec-Driven Development
- **Key concepts**: Spec-driven development (write the spec before the code), AI-native SDLC stages (Problem → Spec → AI-assisted design → AI-assisted implementation → Testing → Iteration), TDD with AI, version control workflows
- **Primary resource**: [Specification by Example — Martin Fowler](https://martinfowler.com/bliki/SpecificationByExample.html) · [How to Use GitHub Copilot Effectively](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)
- **Time estimate**: 3–5 days
- **Completion evidence**: Write a complete spec for a small project before writing any code; demonstrate a working feature built spec-first with AI assistance

#### ML-BUILD-02: AI Coding Tools
- **Key concepts**: Effective use of GitHub Copilot, Cursor, Claude Code — prompt patterns, spec-driven prompting, reviewing AI-generated code critically, knowing when to override AI suggestions
- **Primary resource**: [Claude Code Best Practices — Anthropic blog](https://www.anthropic.com/engineering/claude-code-best-practices) · [Cursor AI Editor — Getting Started](https://www.cursor.com/docs) · [GitHub Copilot Quickstart](https://docs.github.com/en/copilot/quickstart)
- **Time estimate**: 3–5 days (ongoing skill)
- **Completion evidence**: Build a small feature using an AI coding tool from a written spec; annotate 3 cases where you corrected AI-generated code and explain why

#### ML-BUILD-03: Full-Stack Basics for AI Apps
- **Key concepts**: FastAPI (build a REST ML inference endpoint), Streamlit / Gradio (rapid ML demo UIs), SQLite/PostgreSQL basics for storing model outputs, Docker for packaging
- **Primary resource**: [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) · [Streamlit docs — quickstart](https://docs.streamlit.io/get-started) · [Gradio quickstart](https://www.gradio.app/guides/quickstart) · [Docker for Developers (YouTube)](https://www.youtube.com/watch?v=fqMOX6JJhGo)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Deploy an ML model behind a FastAPI endpoint with a Streamlit UI; Dockerise the project

#### ML-BUILD-04: Product Engineering with AI
- **Key concepts**: Product thinking (user needs → spec → shipped feature), AI feature design (confidence scores, fallbacks, graceful degradation, streaming responses), A/B testing AI features, evaluation before launch, LLM API integration (OpenAI, Anthropic, Gemini APIs), structured outputs, function calling
- **Primary resource**: [Shape Up — Basecamp (free)](https://basecamp.com/shapeup) · [OpenAI API Quickstart](https://platform.openai.com/docs/quickstart) · [Anthropic API Docs](https://docs.anthropic.com/)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Build one AI-powered product feature end-to-end (user need → spec → shipped) with at least one graceful fallback for model failure

#### ML-BUILD-05: Systems Architecture for AI Products
- **Key concepts**: Architectural thinking, software architecture patterns (monolith, microservices, event-driven), AI system design (recommendation engine, semantic search, LLM chatbot at scale), designing for observability, idempotency in LLM pipelines, schema design for AI-generated content
- **Primary resource**: [System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer) · [Building LLM Applications for Production — Chip Huyen](https://huyenchip.com/2023/04/11/llm-engineering.html) · [Emerging Architectures for LLM Applications — a16z](https://a16z.com/emerging-architectures-for-llm-applications/)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Design (on paper/diagram) two AI system architectures: one RAG chatbot at scale, one recommendation engine; explain key tradeoffs

#### ML-BUILD-06: Cloud Fundamentals
- **Key concepts**: Pick one provider (AWS/GCP/Azure), compute (VMs, containers, serverless), storage (object storage, data lakes), networking basics, IAM and least-privilege, pricing models (on-demand, spot)
- **Primary resource**: [AWS Cloud Practitioner Essentials (free, official)](https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/) · [GCP Fundamentals — Coursera](https://www.coursera.org/learn/gcp-fundamentals)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Deploy a FastAPI ML app to one cloud provider; set up an IAM role with least-privilege access

#### ML-BUILD-07: Data Engineering on the Cloud
- **Key concepts**: Data pipelines (ingest → transform → load), dbt for data transformation, Apache Airflow for orchestration, Kafka basics, data lake vs. data warehouse vs. lakehouse, cloud-specific tools (S3/Glue/BigQuery/Dataflow)
- **Primary resource**: [Data Engineering Zoomcamp — DataTalks.Club (free)](https://github.com/DataTalksClub/data-engineering-zoomcamp) · [Fundamentals of Data Engineering — Reis & Housley (book)](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Build a data pipeline that ingests a public dataset, transforms it with dbt, and loads it into a cloud data warehouse; add a scheduled Airflow DAG

#### ML-BUILD-08: MLOps & AI Infrastructure
- **Key concepts**: ML pipelines (data → training → evaluation → deployment as reproducible pipeline), experiment tracking (MLflow, Weights & Biases), model serving (BentoML, TorchServe, Ray Serve), inference optimisation (quantisation, batching), model monitoring (drift detection), feature stores, CI/CD for ML
- **Primary resource**: [MLOps Zoomcamp — DataTalks.Club (free)](https://github.com/DataTalksClub/mlops-zoomcamp) · [MLflow docs](https://mlflow.org/docs/latest/index.html) · [Weights & Biases docs](https://docs.wandb.ai/) · [Designing ML Systems — Chip Huyen (book)](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Set up an MLflow experiment tracking run for a training job; deploy a model to a REST endpoint with basic monitoring (request logging + latency tracking)

#### ML-BUILD-09: Vector Databases & Embeddings
- **Key concepts**: What embeddings are, cosine similarity, FAISS, Pinecone, ChromaDB, Weaviate — comparison, indexing strategies (HNSW, IVF), hybrid search (dense + sparse), practical limits of vector search
- **Primary resource**: [Vector Databases Explained — Pinecone](https://www.pinecone.io/learn/vector-database/) · [Understanding and Applying Text Embeddings — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/google-cloud-vertex-ai/)
- **Time estimate**: 3–5 days
- **Completion evidence**: Build a semantic search engine over a document collection using any vector database; benchmark retrieval quality with 10 sample queries

---

### ML-DEEP: Deep Technical

#### ML-DEEP-01: Knowledge Distillation
- **Key concepts**: Response distillation (train student on teacher outputs), feature distillation (match internal representations), LoRA-based distillation, hard vs. soft labels, KL divergence as distillation loss, speculative decoding, self-distillation
- **Primary resource**: [Distilling Step-by-Step paper (Hsieh et al., 2023)](https://arxiv.org/abs/2212.10535) · [Orca paper (Microsoft)](https://arxiv.org/abs/2306.02707) · [HuggingFace TRL — KTO and DPO trainers](https://huggingface.co/docs/trl/)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Run a response-distillation experiment: use a large model to generate training data, then fine-tune a smaller model on it; compare outputs

#### ML-DEEP-02: Data Collection & Curation
- **Key concepts**: Web scraping at scale (Common Crawl, Scrapy), crowdsourcing (Scale AI, Appen), programmatic labelling (Snorkel weak supervision), deduplication (MinHash/LSH, semantic dedup), quality filtering (perplexity, classifier-based), toxicity and PII filtering, data mixture and weighting, data cards
- **Primary resource**: [Argilla — open-source annotation platform](https://argilla.io/) · [HuggingFace Datasets library](https://huggingface.co/docs/datasets/) · [DataComp benchmark](https://www.datacomp.ai/)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Curate a dataset of at least 500 examples with quality filtering applied; write a data card documenting source, filtering criteria, and known biases

#### ML-DEEP-03: Synthetic Data Generation
- **Key concepts**: LLM-based generation (self-instruct, persona-driven, backtranslation), Constitutional AI (CAI), code + test generation, reward model filtering, diversity sampling, human spot-checking
- **Primary resource**: [Self-Instruct paper (Wang et al., 2022)](https://arxiv.org/abs/2212.09561) · [Constitutional AI paper (Anthropic, 2022)](https://arxiv.org/abs/2212.08073)
- **Time estimate**: 1 week
- **Completion evidence**: Generate a synthetic instruction dataset of at least 200 examples using an LLM; apply one quality filtering step; demonstrate diversity using embedding visualisation

#### ML-DEEP-04: Multi-Agent AI Systems
- **Key concepts**: Orchestrator-subagent patterns, peer collaboration between agents, parallelism for independent subtasks, structured communication protocols, error recovery in multi-agent pipelines, evaluation at the task level
- **Primary resource**: [LangGraph documentation](https://langchain-ai.github.io/langgraph/) · [AutoGen — Microsoft](https://microsoft.github.io/autogen/) · [Multi AI Agent Systems with crewAI — deeplearning.ai (free)](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Build a 3-agent system where a supervisor orchestrates two specialist agents; demonstrate the system completing a multi-step research-and-synthesis task

---

### ML-HUMAN: Human Skills & Ethics

#### ML-HUMAN-01: Communication & Storytelling
- **Key concepts**: Pyramid Principle (structured communication), technical writing for engineers, presenting ML results to non-technical stakeholders, public speaking basics
- **Primary resource**: [How to Speak — MIT Patrick Winston (YouTube)](https://www.youtube.com/watch?v=Unzc731iCUY) · [Technical Writing for Engineers — Google (free)](https://developers.google.com/tech-writing)
- **Time estimate**: Ongoing (1 week to baseline, then practice)
- **Completion evidence**: Give a 5-minute presentation of a technical project to a non-technical audience; write a project README that a first-year student can follow

#### ML-HUMAN-02: Critical Thinking & Problem Framing
- **Key concepts**: First principles thinking, cognitive biases in technical decision-making (Kahneman System 1 vs. 2), OODA loop, problem framing before solution generation, adaptive vs. technical challenges (Heifetz)
- **Primary resource**: [Thinking, Fast and Slow — Daniel Kahneman (book)](https://www.amazon.com/Thinking-Fast-Slow-Daniel-Kahneman/dp/0374533555) · [First Principles Thinking — Wait But Why](https://waitbutwhy.com/2015/11/the-cook-and-the-chef-musks-secret-sauce.html)
- **Time estimate**: Ongoing
- **Completion evidence**: Write a one-page "problem brief" for a real challenge — articulating root cause, assumptions, and constraints before proposing any solution

#### ML-HUMAN-03: Ethics & Responsibility in AI
- **Key concepts**: Bias and fairness in ML, AI harms and societal impact, responsible AI practices, the alignment problem (basic), OWASP Top 10 for LLMs (prompt injection, data poisoning), GDPR basics for ML engineers
- **Primary resource**: [AI Ethics — fast.ai](https://ethics.fast.ai/) · [Weapons of Math Destruction — Cathy O'Neil (book)](https://www.amazon.com/Weapons-Math-Destruction-Increases-Inequality/dp/0553418815) · [Responsible AI Practices — Google](https://ai.google/responsibility/responsible-ai-practices/)
- **Time estimate**: 3–5 days
- **Completion evidence**: Conduct a bias audit on a public ML model (e.g. a sentiment classifier); write a 1-page reflection on one real-world AI harm case

#### ML-HUMAN-04: Collaboration & Team Engineering
- **Key concepts**: Psychological safety (Google Project Aristotle), giving and receiving feedback (Radical Candor), non-violent communication, the five dysfunctions of a team, code review etiquette
- **Primary resource**: [Google Project Aristotle — rework.withgoogle.com](https://rework.withgoogle.com/print/guides/5721312655835136/) · [Radical Candor — Kim Scott](https://www.radicalcandor.com/)
- **Time estimate**: Ongoing
- **Completion evidence**: Conduct or participate in a structured code review; document a retrospective from a team project

---

### ML-CAREER: Portfolio & Career

#### ML-CAREER-01: GitHub Portfolio & Open Source
- **Key concepts**: Profile README, pinned repositories (3–5 strong projects), consistent commit history, open-source contribution (even documentation), README quality
- **Primary resource**: [How to Build an AI Portfolio — Towards Data Science](https://towardsdatascience.com/how-to-build-a-data-science-portfolio-5f566517c79c) · [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- **Time estimate**: Ongoing (set up in 1 day, maintain always)
- **Completion evidence**: GitHub profile with at least 3 pinned projects; 1 merged pull request to any public repo

#### ML-CAREER-02: Resume & LinkedIn for AI Roles
- **Key concepts**: Lead with projects not job titles, quantify ML impact (e.g. "Reduced latency by 40% via INT8 quantisation"), show your stack explicitly, AI-specific resume tips (Kaggle rankings, HuggingFace models, open-source contributions), LinkedIn optimisation
- **Primary resource**: [Tech Interview Handbook — Resume Guide](https://www.techinterviewhandbook.org/resume/guide)
- **Time estimate**: 3–5 days (then update after every project)
- **Completion evidence**: A tailored resume reviewed by at least one peer or mentor; LinkedIn profile with an "About" section that includes AI tech stack

#### ML-CAREER-03: Coding Interview Preparation
- **Key concepts**: LeetCode patterns (sliding window, two pointers, BFS/DFS, DP), time and space complexity analysis, communicating approach before coding, Python idioms for interviews
- **Primary resource**: [LeetCode](https://leetcode.com/) · [Coding Interview Patterns book](https://geni.us/q7svoz) · [NeetCode patterns (YouTube)](https://www.youtube.com/@NeetCode)
- **Time estimate**: 4–8 weeks (2–3 problems/day)
- **Completion evidence**: Solve 100 LeetCode problems (Easy: 50, Medium: 40, Hard: 10); complete 3 mock interviews (Pramp or similar)

#### ML-CAREER-04: AI System Design Interview Prep
- **Key concepts**: ML system design framework (Problem scoping → Data → Modelling → Evaluation → Deployment → Monitoring), classic design problems (recommendation engine, semantic search, LLM chatbot at scale, fraud detection), ML-specific tradeoffs (latency vs. accuracy, cost vs. quality)
- **Primary resource**: [Designing Machine Learning Systems — Chip Huyen (book)](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) · [ML System Design Template — Chip Huyen (free)](https://huyenchip.com/machine-learning-systems-design/toc.html) · [Machine Learning System Design Interview book](https://www.amazon.com/Machine-Learning-System-Design-Interview/dp/1736049127)
- **Time estimate**: 2–4 weeks
- **Completion evidence**: Design 3 ML systems on paper using the framework; present one design in a mock system design interview setting

#### ML-CAREER-05: Kaggle & ML Competitions
- **Key concepts**: Competition lifecycle, feature engineering under a leaderboard, Kaggle notebooks, ensemble methods, reading winning solutions, community learning
- **Primary resource**: [Kaggle](https://www.kaggle.com/) · [How to Win a Kaggle Competition (blog)](https://towardsdatascience.com/how-to-win-a-kaggle-competition-8a7dce0ae1ef)
- **Time estimate**: Ongoing (enter at least 1 competition per semester)
- **Completion evidence**: At least one Kaggle competition submission with a public leaderboard score; one Kaggle notebook published with at least 10 upvotes

#### ML-CAREER-06: Showcase Project — Build & Deploy
- **Key concepts**: End-to-end project: data → model/system → API → UI → deployed and publicly accessible; clean README, architecture diagram, honest limitations section
- **Primary resource**: [HuggingFace Spaces — host demos for free](https://huggingface.co/spaces)
- **Time estimate**: 2–4 weeks
- **Completion evidence**: One deployed, publicly accessible AI project on HuggingFace Spaces or a cloud provider; GitHub repo with README, architecture diagram, and demo link

---

### ML-CYBER: Cybersecurity & AI

#### ML-CYBER-01: Computer Security Fundamentals
- **Key concepts**: Threat models, attack surfaces, OWASP Top 10, network security (firewalls, VPNs, TLS), OS-level security (privilege separation, sandboxing), common vulnerabilities (SQL injection, XSS, buffer overflow), security mindset
- **Primary resource**: [MIT 6.858 Computer Systems Security (YouTube playlist)](https://www.youtube.com/watch?v=GqmQg-cszw4&index=1&list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh) · [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Perform a basic OWASP Top 10 security review on a web application; write a 1-page threat model for a simple AI system

#### ML-CYBER-02: ML for Security
- **Key concepts**: Anomaly detection (isolation forest, autoencoders), intrusion detection systems (IDS) with ML, fraud detection pipelines, network traffic classification, malware classification with embeddings, false positive management
- **Primary resource**: [Anomaly Detection with Scikit-Learn](https://scikit-learn.org/stable/modules/outlier_detection.html) · [Fraud Detection datasets — Kaggle](https://www.kaggle.com/search?q=fraud+detection)
- **Time estimate**: 2–3 weeks
- **Completion evidence**: Build a fraud or anomaly detection model on a public dataset (e.g. Kaggle Credit Card Fraud); achieve >90% recall at a meaningful precision; document the false positive tradeoff

#### ML-CYBER-03: Adversarial ML & Robustness
- **Key concepts**: Adversarial examples (FGSM, PGD attacks), model robustness evaluation, certified defences, data poisoning attacks, model stealing/inversion attacks, robustness benchmarks (RobustBench)
- **Primary resource**: [Adversarial Robustness Toolbox (IBM, GitHub)](https://github.com/Trusted-AI/adversarial-robustness-toolbox) · [CleverHans library](https://github.com/cleverhans-lab/cleverhans)
- **Time estimate**: 1–2 weeks
- **Completion evidence**: Implement an FGSM attack on a trained image classifier; demonstrate that adversarial training improves robustness; present results as a table

#### ML-CYBER-04: LLM Security & Prompt Injection
- **Key concepts**: Prompt injection (direct and indirect), jailbreaking techniques, LLM vulnerabilities (OWASP Top 10 for LLMs), insecure output handling, data exfiltration via LLMs, mitigation strategies (input validation, output filtering, privilege separation in agentic systems)
- **Primary resource**: [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) · [LLM Security — learnprompting.org](https://learnprompting.org/docs/prompt_hacking/intro)
- **Time estimate**: 1 week
- **Completion evidence**: Demonstrate a prompt injection attack on a simple LLM application (in a controlled, ethical setting); implement and document two mitigations; write a 1-page security brief for the application

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
