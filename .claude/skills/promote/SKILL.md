---
name: promote
description: Turn a pattern in the notes into structure - an entity type, an aspect, a relation, an edge, a value or a role - working out which from the material's shape, then fitting the pages to it. Calls declare when the type does not exist yet. Also re-types a single page filed as unclassified.
---

# Promote

**Read `.claude/notebook/promotion.md` and follow it.** It has the gate - whose first item is working out which of the six things this pattern is - the runbooks, and the shapes material arrives in. **Then `.claude/notebook/graph.md`** for the six outcomes and their tests: the user names a pattern, never the kind of structure, so telling them apart is this skill's job.

Then `.claude/skills/_shared/host-contract.md` - this notebook's law, routing and commands.

This file holds **only what that contract cannot know**. If you find yourself
restating a principle from it here, that is the drift the whole layout exists
to prevent - point at it instead.

## Commands

Generic, and they already work - they read the declarations, so they need nothing from this file:

- `python3 -I .scripts/notebook.py new <type> "<Name>"` for each page; `--set field=value` fills a field, and writes it as a link when the declaration lists it in `links:`; `--owner "<owner>"` for an owned type
- `python3 -I .scripts/notebook.py clues "<page>"` - what in a page's sections already acts like pages of their own (`promotion.md`, "A section that may be pages of its own")
- `python3 -I .scripts/types_check.py`, `vault_check.py --since HEAD`, then `audit.py <the new folder>`

## TODO: this host supplies

- [ ] where the hub is - see .scripts/notebook_config.py
- [ ] the commands that create a page and verify the links

## Reply

Say briefly what changed and anything you had to guess. Nothing else.
