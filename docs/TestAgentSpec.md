# SrujanaBuddy Test Agent Specification (TestAgentSpec.md)

This specification defines the multi-level testing agent for SrujanaBuddy.

## Scope Boundaries

### In Scope
1. **Level 1 Testing**: Deterministic verification of YAML frontmatter syntax, checking for broken markdown/file links, and verifying structure of profile/GPS templates.
2. **Level 2 Testing**: Execution of test scenarios (from `eval/scenarios/` and `eval/data/synthetic_test_data.json`) against agents using local mock simulations or optional LLM endpoints.
3. **Level 3 Testing**: Basic loop detection by checking trajectory repeats (if the same file/skill is hit 3+ times in a session).
4. **Synthetic Data Management**: Creating and updating `eval/data/synthetic_test_data.json` with test execution metrics, run history, and dynamic additions based on scope of testing.
5. **Backlog & Reports**: Writing run summaries to `eval/reports/test-report.md` and adding failures to `eval/data/IMPROVEMENT-BACKLOG.md` as open tasks using the standardized template.

### Out of Scope
1. Multi-tenant live web integration.
2. Automated PR commits.
3. Hosting paid AI models directly.

---

## Decisions (Confirmed)
1. **Config-free Mock Mode**: By default, the agent runs in T2-reduced simulation mode if no `LLM_ENDPOINT` or API key is set.
2. **Structured JSON Storage**: Synthetic data is stored in `eval/data/synthetic_test_data.json` to keep prose and data clean, as requested by `AGENTS.md`.
3. **Output Reporting**: Results are written to `eval/reports/test-report.md` with timestamps.

---

## Verification & Acceptance Criteria
1. **AC-1**: Running `test_agent.py --level 1` must perform static analysis and detect invalid YAML frontmatter in any `.agents/skills/*/SKILL.md`.
2. **AC-2**: Running `test_agent.py --level 2 --mock` must execute scenarios against mock templates and output status to console.
3. **AC-3**: Executing any failing test case must result in an open `IMP-YYYY-NNN` entry added to the top of the Active Tasks in `eval/data/IMPROVEMENT-BACKLOG.md`.
4. **AC-4**: A timestamped run metric must be appended to the run history of the synthetic dataset file `eval/data/synthetic_test_data.json`.
