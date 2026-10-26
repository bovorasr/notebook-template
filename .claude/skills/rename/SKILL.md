---
name: rename
description: Rename a page and everything named from it - an entity, its folder, and the pages it owns whose names carry its name - with every link following. Use when the user renames a person, a place or anything else with pages under it.
---

# Rename

**Renaming is hard in any system, so it is one command.** `notebook.py rename` works out what a rename touches from the declarations (`.claude/notebook/registry.md`, "Names") and does it through the running app, which rewrites every link (`.claude/notebook/obsidian.md`).

1. `python3 -I .scripts/notebook.py rename "<page>" "<new name>" --dry-run`, and show the user the plan: the pages renamed, the folder, and **the ledger entries kept** - an entry keeps the name it was made with (`.claude/notebook/ledger.md`, law 1), so say the old names are now behind and leave it to them.
2. On agreement, run it without `--dry-run`. It refuses without the running app; say so, and ask the user to open the vault in Obsidian.
3. `python3 -I .scripts/vault_check.py --since HEAD`: a rename is where links rot.

This skill is generic - the template ships it whole and the update keeps it level - so it names no host file and has nothing to fill in.

## Reply

What was renamed, as links, and the entries left with their old names. Nothing else.
