---
name: open
description: Open a new ledger entry for a fresh occasion - a day, a session, a visit, a sprint - closing the previous one first. Use when the user says a new one has started.
---

# Open

**Read `.claude/notebook/ledger.md` and follow it.** It has what a ledger entry is and the five laws governing it, above all that it is append-only.

Then `.claude/skills/_shared/host-contract.md` - this notebook's law, routing and commands.

This file holds **only what that contract cannot know**. If you find yourself
restating a principle from it here, that is the drift the whole layout exists
to prevent - point at it instead.

## Commands

Generic, and they already work - they read the declarations, so they need nothing from this file:

- `python3 -I .scripts/notebook.py close "<entry>"` then `python3 -I .scripts/notebook.py open "<name>"` - close first if the previous occasion is over, naming it: a bare `close` closes the only open entry anywhere, which may be another owner's. `close` with nothing open is not an error
- for a ledger owned by an entity, `open "<identity>" --type <ledger> --owner "<owner>"` - one open entry per owner. The owner's page comes first: someone new gets theirs made from its declaration before their entry opens. `open` also opens an entry a projection prepared (`prepare`, `fill`), which from then on is append-only (`ledger.md`, "Three states")
- then show the new entry: open it in the app if the app is running, using the command and the check in `obsidian.md`'s "Showing the user a page" (`ledger.md`, "Lifecycle")

## TODO: this host supplies

- [ ] what an occasion is here, and how its entries are named
- [ ] where its identity comes from, if it is not simply a date
- [ ] the commit this performs

## Reply

Say briefly what changed and anything you had to guess. Nothing else.
