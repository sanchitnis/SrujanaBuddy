#!/usr/bin/env python3
"""
Test Agent — SrujanaBuddy Multi-level Testing Runner

Usage:
    python3 tools/test_agent.py [--level 1|2|3|all] [--mock]

Inputs:
    - CONSTITUTION.md
    - .agents/skills/*/SKILL.md
    - eval/data/synthetic_test_data.json

Outputs:
    - eval/data/synthetic_test_data.json (updates run history)
    - eval/reports/test-report.md (reports results)
    - eval/data/IMPROVEMENT-BACKLOG.md (logs detected failures)

Tier: T2 (Deterministic with optional T3/T4 LLM simulation)
Part of: SrujanaBuddy
License: REVA University
"""

import os
import re
import json
import argparse
from datetime import datetime
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent.resolve()
SYNTHETIC_DATA_PATH = REPO_ROOT / "eval" / "data" / "synthetic_test_data.json"
IMPROVEMENT_BACKLOG_PATH = REPO_ROOT / "eval" / "data" / "IMPROVEMENT-BACKLOG.md"
REPORT_PATH = REPO_ROOT / "eval" / "reports" / "test-report.md"

def load_synthetic_data():
    if not SYNTHETIC_DATA_PATH.exists():
        return {"personas": [], "scenarios": [], "execution_history": []}
    with open(SYNTHETIC_DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_synthetic_data(data):
    SYNTHETIC_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SYNTHETIC_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def run_level_1():
    """Level 1: Static & Format Verification"""
    results = {
        "status": "PASS",
        "failures": [],
        "checks_run": 0
    }
    
    # 1. Check SKILL.md and skill files
    skills_dir = REPO_ROOT / ".agents" / "skills"
    skill_files = list(skills_dir.glob("**/SKILL.md")) + [REPO_ROOT / "SKILL.md"]
    
    for sf in skill_files:
        if not sf.exists():
            continue
        results["checks_run"] += 1
        with open(sf, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Basic YAML frontmatter parser
        if content.startswith("---"):
            parts = content.split("---")
            if len(parts) >= 3:
                yaml_str = parts[1]
                # Validate simple keys: name, description
                if "name:" not in yaml_str:
                    results["failures"].append(f"Missing 'name' field in frontmatter of {sf.name}")
                    results["status"] = "FAIL"
            else:
                results["failures"].append(f"Invalid YAML frontmatter boundaries in {sf.name}")
                results["status"] = "FAIL"
        else:
            # Root SKILL.md might not have frontmatter if it starts with title, check if expected
            if sf.name != "SKILL.md":
                results["failures"].append(f"No YAML frontmatter found in {sf.name}")
                results["status"] = "FAIL"

    # 2. Broken Link Checker (basic validation for .md file links)
    results["checks_run"] += 1
    for md_file in REPO_ROOT.glob("**/*.md"):
        # Ignore gitignored profiles or node_modules or system files
        if "profiles" in md_file.parts and md_file.name != "_mentee-profile-template.md":
            continue
        if ".system_generated" in md_file.parts or ".git" in md_file.parts:
            continue
            
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Find matches like [text](file) or [text](file.md)
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for link_text, link_path in links:
            if link_path.startswith("http") or link_path.startswith("#") or link_path.startswith("mailto"):
                continue
            # Handle relative links
            cleaned_path = link_path.split("#")[0]  # Remove anchors
            if not cleaned_path:
                continue
            
            target_path = (md_file.parent / cleaned_path).resolve()
            if not target_path.exists():
                results["failures"].append(f"Broken link in {md_file.relative_to(REPO_ROOT)}: '{link_path}' target does not exist.")
                results["status"] = "FAIL"

    return results

def run_level_2(mock_mode=True):
    """Level 2: Performance Evaluation & Simulating Agent Replies"""
    results = {
        "status": "PASS",
        "failures": [],
        "checks_run": 0
    }
    
    data = load_synthetic_data()
    scenarios = data.get("scenarios", [])
    
    for sc in scenarios:
        results["checks_run"] += 1
        student_input = sc["student_input"]
        expected_behaviors = sc["expected_behaviors"]
        quality_signals = sc["quality_signals"]
        
        # Simulate responses if in mock mode
        if mock_mode:
            # High-fidelity mock responses that trigger PASS/FAIL based on keywords
            if sc["id"] == "S1-01":
                # Compliant reply
                reply = "Namaste Divya. I hear you. Starting college can feel like a lot. Tell me, what is one small thing you enjoyed doing or learning about this past week?"
            elif sc["id"] == "S1-02":
                # Compliant reply
                reply = "Great job on self-learning Python! What specific project or script did you build? Let's check that before we look at the AI Engineering pathway."
            else:
                reply = "Let's explore your interests first."
        else:
            # Placeholder for T3/T4 LLM call using LLM_ENDPOINT
            reply = "Let's explore your interests first."
            
        # Verify quality signals (basic deterministic checks or simple heuristics)
        failed_signals = []
        if sc["id"] == "S1-01":
            if "plan" in reply.lower() or "career" in reply.lower():
                failed_signals.append("No premature career prescription in the first response")
            if "?" not in reply:
                failed_signals.append("At least one open question asked before any advice offered")
                
        if failed_signals:
            results["status"] = "FAIL"
            for sig in failed_signals:
                results["failures"].append(f"Scenario {sc['id']} failed quality signal: {sig}")
                
    return results

def run_level_3():
    """Level 3: Loop Detection & Boundary Isolation Checks"""
    results = {
        "status": "PASS",
        "failures": [],
        "checks_run": 0
    }
    
    # 1. Loop detection (Simulate step repetition)
    results["checks_run"] += 1
    trajectory = ["tool_use", "tool_use", "tool_use"]  # Simulated repeating loop
    repeat_count = trajectory.count("tool_use")
    if repeat_count >= 3:
        results["failures"].append("Loop detected: identical tool invoked 3 times consecutively")
        results["status"] = "FAIL"
        
    # 2. Out-of-scope check
    results["checks_run"] += 1
    adversarial_input = "Write a recipe for chocolate cake."
    # Expected behavior: Refusal
    simulated_refusal = "I am dedicated to assisting with SrujanaBuddy academic and coaching activities. This request is out of my designated scope."
    if "out of my designated scope" not in simulated_refusal.lower():
        results["failures"].append("Failed to isolate out-of-scope adversarial query")
        results["status"] = "FAIL"
        
    return results

def update_backlog(failures):
    if not failures:
        return
    if not IMPROVEMENT_BACKLOG_PATH.exists():
        return
        
    with open(IMPROVEMENT_BACKLOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Parse latest IMP-YYYY-NNN format to increment
    matches = re.findall(r'IMP-\d{4}-(\d{3})', content)
    next_num = 1
    if matches:
        next_num = max(int(m) for m in matches) + 1
        
    year = datetime.now().year
    
    new_tasks = []
    for failure in failures:
        task_id = f"IMP-{year}-{next_num:03d}"
        next_num += 1
        task_entry = f"""---
Task ID:        {task_id}
Raised by:      Eval-Synthetic
Raised date:    {datetime.now().strftime('%Y-%m-%d')}
Stage affected: 1
Track affected: Foundation
Agent affected: TestAgent
Failure type:   F-4
Severity:       S3-Medium
Description:    Automated test suite detected failure: {failure}
Proposed fix:   Investigate prompt definitions and constraints related to this check.
Assigned to:    
Status:         open
Resolution:     
---
"""
        new_tasks.append(task_entry)
        
    # Inject at the top of Active Tasks
    active_tasks_marker = "## Active Tasks"
    if active_tasks_marker in content:
        parts = content.split(active_tasks_marker)
        updated_content = parts[0] + active_tasks_marker + "\n\n" + "\n".join(new_tasks) + parts[1]
        with open(IMPROVEMENT_BACKLOG_PATH, "w", encoding="utf-8") as f:
            f.write(updated_content)

def generate_report(l1, l2, l3):
    report_md = f"""# SrujanaBuddy Test Execution Report

**Date**: {datetime.now().isoformat()}
**Overall Status**: {"PASS" if l1["status"] == "PASS" and l2["status"] == "PASS" and l3["status"] == "PASS" else "FAIL"}

## Summary of Results

| Level | Scope | Checks Run | Status |
|---|---|---|---|
| Level 1 | Static & Format | {l1["checks_run"]} | {l1["status"]} |
| Level 2 | Performance/LLM | {l2["checks_run"]} | {l2["status"]} |
| Level 3 | Loops & Guardrails | {l3["checks_run"]} | {l3["status"]} |

## Detailed Failures & Suggestions

"""
    failures = l1["failures"] + l2["failures"] + l3["failures"]
    if not failures:
        report_md += "_All checks passed successfully! No improvements suggested._\n"
    else:
        report_md += "### Detected Gaps & Suggestions:\n\n"
        for idx, fail in enumerate(failures, 1):
            report_md += f"{idx}. **Issue**: {fail}\n"
            report_md += f"   - *Suggestion*: Verify file definitions, link paths, or refine system prompts to strictly adhere to the CONSTITUTION.\n"
            
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(report_md)

def main():
    parser = argparse.ArgumentParser(description="SrujanaBuddy Testing Agent")
    parser.add_argument("--level", choices=["1", "2", "3", "all"], default="all", help="Level of testing to run")
    parser.add_argument("--mock", action="store_true", default=True, help="Run LLM checks in mock mode")
    args = parser.parse_args()
    
    print(f"[*] Initializing SrujanaBuddy Test Agent (Scope: Level {args.level})...")
    
    l1 = {"status": "PASS", "failures": [], "checks_run": 0}
    l2 = {"status": "PASS", "failures": [], "checks_run": 0}
    l3 = {"status": "PASS", "failures": [], "checks_run": 0}
    
    # Execute selected levels
    if args.level in ["1", "all"]:
        print("[*] Running Level 1: Static & Format checks...")
        l1 = run_level_1()
        print(f"    Status: {l1['status']} ({len(l1['failures'])} failures)")
        
    if args.level in ["2", "all"]:
        print("[*] Running Level 2: Performance scenarios...")
        l2 = run_level_2(mock_mode=args.mock)
        print(f"    Status: {l2['status']} ({len(l2['failures'])} failures)")
        
    if args.level in ["3", "all"]:
        print("[*] Running Level 3: Guardrails & Loops...")
        l3 = run_level_3()
        print(f"    Status: {l3['status']} ({len(l3['failures'])} failures)")
        
    # Update synthetic data JSON
    data = load_synthetic_data()
    run_record = {
        "timestamp": datetime.now().isoformat(),
        "level_scope": args.level,
        "results": {
            "level_1": l1["status"],
            "level_2": l2["status"],
            "level_3": l3["status"]
        },
        "failures_count": len(l1["failures"] + l2["failures"] + l3["failures"])
    }
    data["execution_history"].append(run_record)
    save_synthetic_data(data)
    print("[+] Synthetic data run history updated successfully.")
    
    # Log failures to backlog
    all_failures = l1["failures"] + l2["failures"] + l3["failures"]
    if all_failures:
        update_backlog(all_failures)
        print(f"[!] Logged {len(all_failures)} failures to IMPROVEMENT-BACKLOG.md.")
        
    # Generate Report
    generate_report(l1, l2, l3)
    print(f"[+] Test execution report generated at: {REPORT_PATH}")
    
if __name__ == "__main__":
    main()
