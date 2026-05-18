# stm/_tasks — STM Task Capture Inbox

This folder is a **staging area** for incoming tasks. It is not a to-do list.

Write here now. Triage later. Route to the right STM file. Archive the capture.

---

## What Goes Here

Any task, commitment, or obligation that arrives and cannot be triaged immediately:

- Assignment announced in class
- Task mentioned in a WhatsApp message
- Thought that surfaces mid-day
- Action item from a meeting
- Coach-suggested item (from SrujanaBuddy session)

---

## Capture File Naming

```
YYYY-MM-DD-short-title.md
```

Examples:
```
2026-05-18-os-lab-submission.md
2026-05-18-email-prof-sharma.md
2026-05-18-update-linkedin.md
```

Use `TEMPLATE-capture.md` as the starting point.

---

## The Triage Workflow

Triage happens during your **morning ritual** (while setting Dainika sankalpas) or at your first free moment. Work through every `[raw]` file in this folder:

```
Open capture file
  ↓
Ask: Can I do this in < 2 minutes right now?
  YES → Tatkala: complete it now. Delete the capture file.
  NO  ↓
Ask: Does this need to happen today?
  YES → Dainika: add to 00-today-sankalpa.md
        (check 3/day cap first — if full, mark [PENDING] and come back tomorrow)
  NO  ↓
Ask: Does this need to happen this week?
  YES → Saptahika: add to 02-weekly-sankalpa.md (max 2)
        (if both slots full, mark [PENDING] and route to Iccha or next Svadhyaya)
  NO  ↓
Ask: Am I waiting on someone else for this?
  YES → Waiting: add to 04-waiting.md. Note who and by when.
  NO  ↓
Ask: Is this something I genuinely want to do someday?
  YES → Iccha: add to 03-someday-iccha.md
   NO → Discard the capture. Let it go. Hogbidi.
```

After routing, update the capture file status to `triaged` and move it to `.archive/`.

---

## Routing Quick Reference

| Triage Answer | Route To | STM File |
|---|---|---|
| < 2 min right now | Tatkala | Complete immediately — no file |
| Must happen today | Dainika | `00-today-sankalpa.md` |
| Must happen this week | Saptahika | `02-weekly-sankalpa.md` |
| Delegated / waiting | Waiting | `04-waiting.md` |
| Someday / not urgent | Iccha | `03-someday-iccha.md` |
| Overflow (caps full) | Pending | Keep in `_tasks/` with `[PENDING]` tag; review at Svadhyaya |
| Not worth doing | Discard | Delete the capture file |

---

## Key Rules

1. **Capture first, triage second.** Never block writing because you don't know where it goes yet.
2. **3/day Dainika cap is enforced here** — at triage, not later. If the cap is full, the task does not go into today; it stays `[PENDING]` until tomorrow or Svadhyaya.
3. **This folder is a staging area, not a backlog.** If items pile up here without triage, they go stale. Review all `[raw]` and `[PENDING]` files every Sunday in Svadhyaya.
4. **Tatkala items do not need a capture file.** If you can do it in 2 minutes, do it — no file, no triage.
5. **Archive after triage.** Move the processed file to `.archive/YYYY-MM-DD/`.

---

## Folder Structure

```
stm/_tasks/
  README.md               ← this file
  TEMPLATE-capture.md     ← copy this for each new capture
  YYYY-MM-DD-title.md     ← your active raw captures
  .archive/
    YYYY-MM-DD/           ← triaged captures moved here
```

---

## Svadhyaya Review (Weekly)

Every Sunday in `06-weekly-svadhyaya.md`, scan this folder:
- How many items were captured this week?
- Any `[PENDING]` items that can now be routed?
- Any pattern in what's piling up? (stress signal — discuss with coach)
