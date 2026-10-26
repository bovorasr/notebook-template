---
type: type
declares: entry
folder: Ledger
ledger: periodic
required:
  - type
  - status
defaults:
  status: open
sections:
  - Notes
  - Working notes
log_to: Notes
occasion_only: Working notes
---

# entry

> **The ledger** - one entry per occasion: a day, a session, a visit, a sprint. Append-only and never corrected in place; the only home for what was true only then. See `.claude/notebook/ledger.md`.

> Rename it to what an occasion is called here by changing `declares:`, `folder:` and this file's name. `ledger: periodic` is what makes it the ledger; nothing else needs to know its name. Make it `span` if entries are named things that run in parallel rather than one after another.
