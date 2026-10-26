---
name: close
description: Close the open ledger entry and commit what it holds, without opening another. For when the user stops for the day.
---

# Close

**Read `.claude/notebook/ledger.md` and follow it.** It has why closing is the natural commit point, and that a ledger entry is never corrected in place.

Then `.claude/skills/_shared/host-contract.md` - this notebook's law, routing and commands.

This file holds **only what that contract cannot know**. If you find yourself
restating a principle from it here, that is the drift the whole layout exists
to prevent - point at it instead.

## Commands

Generic, and they already work - they read the declarations, so they need nothing from this file:

- `python3 -I .scripts/notebook.py close [<name>]` - with no name, the only open entry; it refuses to guess if several are

## TODO: this host supplies

- [ ] the commit message this writes

## Reply

Say briefly what changed and anything you had to guess. Nothing else - except the one line this notebook's level of assistance (`assistance.md`) may allow at the end of an occasion.
