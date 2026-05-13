# Review Instructions for Dr. Anand Siddaiah

Welcome, Dr. Anand. This folder contains the updated specifications and agent behaviors for the **Wellness Triage and Crisis Support** integration within SrujanaBuddy.

## Purpose of Review
We have implemented a three-tier support model to ensure students in distress are identified early and routed to **REVA Manodhara** through the **SLCM Portal**.

## Files to Review
1. [wellness-triage-agent.md](wellness-triage-agent.md): The persona and protocol for the "REVA Wellness Guide".
2. [support-escalation-guide.md](support-escalation-guide.md): The overall logic for Tier 1/2/3 classification.
3. [manodhara-referral.md](manodhara-referral.md): The specific bridge to your services.
4. [SKILL.md](SKILL.md): Master routing rules (see Capability #25).
5. [REVA-STUDENT-SYSTEM-SPEC.md](REVA-STUDENT-SYSTEM-SPEC.md): Updates to the "At-Risk Early Warning Module" (§13.28).

## How to Provide Feedback
- Please edit the files in this folder directly. 
- You can change scripts, thresholds, or contact details.
- Once done, the development team will run a "diff" and merge your expert corrections into the main system.

## Key Terminology Used
- **SLCM Portal**: The official referral channel.
- **Energy Score (1-10)**: Our primary distress proxy (≤3 = Crisis, ≤5 = Concern).
- **Red-Flag Indicators**: Explicit keywords and behaviors triggering immediate referral.
