# CLAUDE.md

> TODO: rename this file to `CLAUDE.md`, replacing the template's own, and fill it in. It is the host's own, and the template only shows its shape.

An Obsidian vault holding the notes for <what>. The vault is this repository's root, wherever it is checked out; every path here is relative to it.

**This notebook's choices**, made when it was set up - read both files with the contracts, before anything is filed or answered:

- **Assistance: <assistance>** - how far Claude goes beyond recording: `.claude/notebook/assistance.md`
- **Consultation: <consultation>** - what Claude may read: `.claude/notebook/consultation.md`

## Start here

The note-taking system is **generic and lives in `.claude/notebook/`** — it names no domain and this vault is one host of it. Read in this order:

1. **`.claude/notebook/README.md`** — the ten layers, and the eight things a host supplies.
2. **`.claude/notebook/obsidian.md`** — the platform. **Read it before any rename, any new filename, or any `obsidian` command.**
3. **`.claude/skills/_shared/host-contract.md`** — the host contract: this vault's types, domain rules, and per-type routing.

Then the contract for whatever is being done: `capture.md`, `ledger.md`, `promotion.md`, `projection.md`, `registry.md`, `reference-layer.md`.

**Do not restate any of it here.** Anything a host document repeats instead of pointing at falls out of step; that is why this file is short.

**`.claude/notebook/` is the template's, not this vault's**, like every file `.claude/notebook/manifest.txt` calls generic - most of the scripts in `.scripts/` among them, so a bug fix to one is a template change: never edit one here, except with the update skill, which brings them level with the template (`upstream.md`). The guard, a pre-commit hook, refuses a commit that does; a fresh clone installs it with `python3 -I .scripts/checkout.py`. When work here shows the generic system needs changing, never edit the template's repository: ask for the change with an issue on it, written in the template's terms (`.claude/notebook/requests.md`). It comes back with the update skill.

**This file must survive a type change at any time.** It never fixes a classification - no "X is not a type", no "Y is always filed as Z" - because types can be declared, re-shaped or retired whenever the material calls for it (`README.md`, "The interface").

## What this vault supplies

The eight host items, in the README's order. Fill each in with a line or a short table and **no generic explanation**.

| item | here |
| --- | --- |
| type table | `Types/`, a page per type declaring its own fields. `Views/Types.base` is the table; `types_check.py` compares it against the pages |
| per-type page sections | TODO |
| hub | TODO — and set it in `.scripts/notebook_config.py` |
| epistemic law | the two choices above, and the domain's particulars in the host contract's "The domain's law". TODO: the particulars, in a line |
| per-type routing | TODO, in the host contract's "Per-type routing" |
| checks | `.scripts/vault_check.py`, `types_check.py`, `audit.py`; `relink.py` is a migration, not a check. `upstream.py verify` keeps the generic files the template's, and runs as the pre-commit hook |
| ledger | TODO: what an occasion is, and the skills that open and close one |
| paths and tools | TODO |

## Where things stand

> TODO. Keep this as the state a previous session left, **not** a task list the user has agreed to. Date it.
