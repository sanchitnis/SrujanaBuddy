# SrujanaBuddy Project Instructions (GEMINI.md)

## Persona Routing
- **Default (Mentee):** By default, assume the user is a **mentee**. Stop reading this file and immediately load `SKILL.md` to proceed with the coaching and support workflow.
- **Contributor:** If the user is explicitly identified as a **contributor**, proceed with the technical mandates and workflows defined in the rest of this file.

---

This file contains foundational mandates, architectural patterns, and development workflows for the SrujanaBuddy project. All contributors and AI agents must adhere to these standards.

## Project Overview
SrujanaBuddy is an AI-augmented student support and coaching ecosystem designed for REVA University. It utilizes a multi-agent architecture to provide academic, career, and personal growth guidance.

## Core Principles
- **Student-Centricity:** All agents and workflows must prioritize the student's holistic development.
- **Agentic Automation:** Leverage AI agents for specialized tasks (coaching, history tracking, triage).
- **STM Framework:** Adhere to Sankalpa and Time Management (STM) principles for student commitment culture, streaks, and habit formation. GTD lists in `gtd/` are legacy; the active execution workspace is `drive-with-gps/`.

## Architectural Patterns
- **Multi-Agent System:** Specialized agents reside in the `agents/` directory.
- **Protocol-Driven:** Standardized protocols for intake (`intake/`) and evaluation (`eval/`).
- **Knowledge Base:** Centralized references and pathways in the `knowledge/` and `references/` directories.

## Technology & AI Standards
- **Markdown-Native:** The core system is Markdown-native and AI-agnostic. All logic, agent instructions, and user data should be stored in `.md` files to ensure readability and portability.
- **API Token Management:** 
    - **Never hard-code** API keys or tokens. 
    - Always use environment variables (e.g., `LLM_ENDPOINT`, `LLM_MODEL`). 
    - Paid frontier API keys (OpenAI, Claude, etc.) must remain **optional**. Tools must provide a functional fallback or "reduced mode" when keys are absent.
- **Model Usage (Local vs. Frontier):**
    - **Local Models (Tier 3):** Prioritize local execution using tools like Ollama or llama.cpp for privacy and offline accessibility.
    - **Frontier Models (Tier 4):** Use for heavy batch processing or high-reasoning tasks. These are considered secondary to the local-first approach.
    - **Zero-Config Tiers:** T0-T2 (templates, scripts, regex) must always work without any AI configuration.

## Conventions
- **Documentation:** Use Markdown (`.md`) for agent definitions, workflows, and guides.
- **File Naming:** Use kebab-case for filenames (e.g., `academic-learning-coach.md`).
- **Templates:** Utilize templates provided in `profiles/`, `gtd/projects/`, and `agents/course-buddyes/` for consistency.

## Workflows
- **Coaching Sessions:** Follow the workflow defined in `COACHING-SESSION-WORKFLOW.md`.
- **Task Management:** Use the STM system in `drive-with-gps/` for tracking daily sankalpas, streaks, and weekly Svadhyaya. Legacy GTD lists are in `gtd/`.
- **Evaluation:** Regularly update trackers in `REVA-IMPLEMENTATION-TRACKER.md` and related files.

## Tools
- Python scripts in `tools/` are used for building course buddyes and generating wiki/workbook content. Ensure `requirements.txt` is updated when adding dependencies.
