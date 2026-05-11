# SrujanaBuddy Improvement Board
## Governance Charter

---

## Purpose

The Improvement Board is the governance body responsible for reviewing evaluation findings, triaging improvement tasks, assigning implementation work, and ensuring that SrujanaBuddy continuously improves in alignment with REVA University's vision and Dr. P. Shyama Raju's philosophy of "Educate to Enterprise."

The Board translates raw observations — from synthetic eval sessions, real student feedback, and mentor observations — into prioritized, actionable improvement tasks that are implemented by the core contributor community.

---

## Chair

**Vice Chancellor, REVA University**

The VC chairs all quarterly Board sessions and holds final authority on:
- Changes to the philosophical and values layer (`references/REVA University.md`, `references/reva-values-anchor.md`)
- Changes to the core Srujana Pathway framework
- Decisions to deprecate or substantially restructure any coaching agent
- Decisions to expand or contract the scope of the system

---

## Standing Members

| Constituency | Role on the Board | Notes |
|-------------|------------------|-------|
| **Students** | 2 student representatives (one UG, one PG) — rotating annually | Must have used SrujanaBuddy in at least one full academic session; nominated by student body |
| **REVA Leaders** | Dean of Student Affairs + one additional REVA leadership representative | Institutional alignment, resource allocation |
| **Faculty Mentors** | 2 faculty members — one from STEM stream, one from non-STEM | Domain accuracy review; coaching protocol feedback |
| **Manodhara** | 1 Manodhara counsellor representative | Wellbeing escalation review; safety and mental health signal accuracy |
| **REVA NEST** | 1 REVA NEST advisor | Startup and venture track accuracy; incubation pathway feedback |
| **Domain Experts / Coaches** | 1 external credentialed coach or domain expert (invited; may rotate) | Coaching methodology quality; philosophical grounding |

Quorum: VC (or designated chair) + at least 4 of the 6 constituent groups represented.

---

## Meeting Cadence

| Meeting type | Frequency | Agenda |
|-------------|-----------|--------|
| Quarterly Review | Every 3 months | All new backlog items reviewed; S1 and S2 items triaged and assigned; S3 items batched; progress on previous quarter reviewed |
| Ad Hoc — Critical (S1) | As needed, within 48 hours of S1 item raised | Single-item review; VC or designate chairs; immediate assignment |
| Annual Retrospective | Once per year | Full system review; assess whether agents and frameworks remain REVA-aligned; assess emerging domains not yet covered |

---

## Improvement Task Format

Every improvement task logged in [`data/IMPROVEMENT-BACKLOG.md`](data/IMPROVEMENT-BACKLOG.md) must follow this format:

```
Task ID:       IMP-YYYY-NNN (e.g. IMP-2026-001)
Raised by:     [Student / Mentor / Eval-Synthetic / Eval-Audit / Board]
Raised date:   YYYY-MM-DD
Stage affected: [1 / 2 / 3 / 4 / All]
Track affected: [Foundation / Application / Creation / Research / Venture / Career / All]
Agent affected: [agent filename or "SKILL.md" or "Framework" or "All"]
Failure type:  [F-1 through F-10 from eval-agent.md, or "Philosophy" or "Domain" or "New Feature"]
Severity:      [S1-Critical / S2-High / S3-Medium / S4-Low]
Description:   [2–5 sentences: what the problem is, where it was observed, what the impact is]
Proposed fix:  [1–3 sentences: what change would resolve this; or "Unknown — board to determine"]
Assigned to:   [person or team; blank until assigned at Board meeting]
Status:        [open / in-progress / resolved / deferred / rejected]
Resolution:    [blank until resolved; then: what was changed, in which file, on what date]
```

---

## Triage and Severity Tiers

| Tier | Criteria | Response |
|------|---------|---------|
| **S1 — Critical** | Escalation failure (F-10); values violation (F-5, two or more); safety or dignity concern | Ad hoc meeting within 48 hours; fix before next student use |
| **S2 — High** | Coaching quality failure affecting multiple archetypes or stages (F-1, F-2, F-3 consistently); significant domain error (F-9) in a core pathway | Agenda item at next quarterly meeting; assigned at that meeting |
| **S3 — Medium** | Isolated coaching quality failure in a specific scenario; domain gap in a specialist area | Batched with other S3 items; quarterly review; community contributor may implement |
| **S4 — Low** | Acceptable-tier session with minor improvement potential; style or tone feedback; optional enhancement | Someday backlog; implemented only if a contributor volunteers |

---

## Escalation Pathway (Between Meetings)

1. **Any core team member** can raise an S1 item at any time by directly contacting the Chair and Dean of Student Affairs.
2. **Manodhara representative** can escalate any wellbeing or safety concern outside the standard meeting cycle.
3. **Student representatives** can request an ad hoc meeting if they observe a pattern that warrants immediate attention.
4. For all other items: log in the backlog and wait for the next quarterly session.

---

## Implementation Responsibility

The Board assigns but does not implement. Implementation is done by:
- Core contributor team (REVA faculty and student contributors listed in `CONTRIBUTORS.md`)
- Domain experts identified in `CONTRIBUTING.md` (for philosophical and domain-accuracy changes)
- REVA technology team (for any tooling or infrastructure changes, if applicable)

All implementations must follow the contribution standards in [`CONTRIBUTING.md`](../CONTRIBUTING.md).
All merged changes must be verified against at least one eval scenario before the Board meeting at which the resolution is reported.

---

## Stakeholder Representation — Why These Six

| Group | Why they are on the Board |
|-------|--------------------------|
| Students | The primary beneficiaries of the system; their lived experience of coaching quality is irreplaceable |
| REVA Leaders | Institutional alignment and stewardship of REVA's values; resource and policy authority |
| Faculty Mentors | Domain accuracy and pedagogical quality; they see the gap between what the system produces and what a human expert would say |
| Manodhara | The only constituency that can assess whether wellbeing signals are being handled correctly; a system that fails here fails fundamentally |
| REVA NEST | The venture and startup ecosystem of REVA; their feedback is essential for Stage 4 venture track accuracy |
| Domain Experts / Coaches | External credentialing and methodological integrity; ensures the coaching practices are grounded in evidence and ethical professional standards |

---

## Principles

1. **No permanent membership below Chair**: All non-Chair members rotate to keep the Board fresh and student-representative.
2. **Evidence first**: Every improvement decision must be traceable to at least one observation (eval log, feedback form, or Board member direct observation).
3. **Improvement traceability**: Every resolved improvement task must name the file changed, the change made, and the eval scenario used to verify the fix.
4. **Philosophical changes require the Chair**: No change to the values layer or Srujana framework is implemented without the VC's explicit approval.
5. **Speed on S1**: A system that fails on safety or values is worse than no system. S1 items are addressed in 48 hours.
