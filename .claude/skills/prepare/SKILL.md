---
name: prepare
description: Prepare the next entry of a ledger before its occasion starts - the questions for an interview, the agenda for a meeting - from what the notes gained since the last one. DELETE THIS if no ledger here prepares its entries.
---

# Prepare

**Read `.claude/notebook/projection.md` ("Where a projection writes: a page, or an entry") and `.claude/notebook/ledger.md` ("Three states") and follow them.** They have what a prepared entry is, what "since the last occasion" means in the notes, and why the entry is the projection's only until it opens.

Then `.claude/skills/_shared/host-contract.md` - this notebook's law, routing and commands.

This file holds **only what that contract cannot know**. If you find yourself
restating a principle from it here, that is the drift the whole layout exists
to prevent - point at it instead.

## Commands

Generic, and they already work - they read the declarations, so they need nothing from this file:

- `python3 -I .scripts/notebook.py prepare "<identity>" --type <ledger> --owner "<owner>"` - makes the entry, or finds the one prepared before; refused once it has opened
- `python3 -I .scripts/notebook.py fill "<entry>" "<section>" --file <draft>` - each section the ledger lists as `prepared:`, rewritten whole
- `/open` - when the occasion starts; from then on the entry is append-only

## TODO: this host supplies

- [ ] which ledger it prepares, and who owns its entries
- [ ] what goes in each prepared section, and how it is phrased
- [ ] the commit it makes

## Reply

Say briefly what was prepared, as a link, and anything you had to guess. Nothing else.
