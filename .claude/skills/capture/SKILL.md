---
name: capture
description: Record something into the notebook: files it on every page it concerns, and logs it on the open ledger entry. Stops at the notes. Use when the user gives an observation, a correction, or something they learned. RENAME THIS to whatever the domain calls it.
---

# Capture

**Read `.claude/notebook/capture.md` and follow it.** It has the whole procedure: naming what the input touches, looking before creating, writing it on every page framed for each, and when to ask rather than guess.

Then `.claude/skills/_shared/host-contract.md` - this notebook's law, routing and commands.

This file holds **only what that contract cannot know**. If you find yourself
restating a principle from it here, that is the drift the whole layout exists
to prevent - point at it instead.

## Commands

Generic, and they already work - they read the declarations, so they need nothing from this file:

- `python3 -I .scripts/notebook.py new <type> "<Name>" --source X` - creates a page **from its type's declaration**, so it is valid by construction; an owned type's page takes `--owner "<owner>"` and is made in the owner's folder
- `python3 -I .scripts/notebook.py current` - capture's step 1: the open entries, and any ledger that needs one opened first
- `python3 -I .scripts/notebook.py log "<line>"` - the open entry, in its declared `log_to:` section; `--local` for its `occasion_only:` section, `--to <name>` when several are open

## TODO: this host supplies

- [ ] routing to anything that is not a type - a hub table, a cross-index. What belongs to one type goes on its declaration's `## Writing to it` (`registry.md`), not here
- [ ] which inputs route to a different skill instead
- [ ] the phrasings that mean "true only of this occasion" here

## Reply

Say briefly what changed and anything you had to guess. Nothing else.
