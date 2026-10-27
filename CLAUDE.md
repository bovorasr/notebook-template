# CLAUDE.md

This repository is **the notebook template**, not a notebook. It holds no domain and no notes: a session here works on the generic system that hosts copy, or on the skeletons they fill in. The host's session file is `CLAUDE.host.md`, and nothing in it describes this repository.

## Start here

1. **`README.md`** — what the template is and what each part of it is for.
2. **`.claude/notebook/README.md`** — the system: the ten layers, the eight things a host supplies, and the two sections that govern every change here, **"Changing this folder"** and **"What may and may not appear in this folder"**.
3. **`.claude/notebook/obsidian.md`** — before any rename, any new filename, or any `obsidian` command.

**Do not restate any of it here**, for the reason the system gives: a copy falls out of step.

## Three kinds of file

**`.claude/notebook/manifest.txt` says which files are generic and which are skeletons**; anything it does not list is the template's own - this file, `README.md`, `/setup` - and never reaches a notebook. Setup copies what it lists and the update skill compares by it, so a new file is not shipped until it is listed there.

- **A generic file** must hold for every domain, and names roles, never a host's names. A notebook takes it unchanged and the update skill keeps it level, so it may need an outlet - `upstream.md`, "The outlets" - before a notebook's own version of it can go back to the template's.
- **A choice** - the levels in `.claude/notebook/assistance/` and `consultation/` - is a generic file a notebook takes from the one source it chose. **Each level's file describes only itself**: never another level, never what the others allow, since a notebook holds only its own and rules Claude can read shape what it does. Keep the headings the same across the levels of one choice. The contracts point at `assistance.md` and `consultation.md` where a level decides, and never describe a level themselves; descriptions of all of them, for choosing, live only in `/setup` and `README.md`.
- **A skeleton** stays a skeleton: placeholders and TODOs, never one domain's answers. A notebook adapts a change to one by hand, so say what changed in the commit message plainly enough to adapt from.

**Each generic script opens with a header for a notebook's sessions**: do not edit, and where to extend instead. It is not for this repository, where those files are written. Keep it word for word the same in each Python script, so a change to it is one change; `notebook-graph/main.js` carries its own.

**`/setup` is the one skill meant to run here.** The others are skeletons that happen to load in this repo; run here, they would file into the template's own hub. `/update` has nothing upstream of it here.

**`setup.py` rewrites skeleton text it knows by heart**, and refuses when that text has changed. So after editing a skeleton, run `/setup`'s script with `--dry-run` against a scratch folder; a refusal names the line to bring it level with.

## Bringing in a change worked out in a notebook

Most changes here start in a notebook. They arrive as **issues on this repository**, opened from a notebook's session (`.claude/notebook/requests.md`), or the user brings them over by hand. **Read an issue for domain leakage first** - a notebook's names, quotes from its notes, anything private - and edit it out of the issue before doing anything else with it. Then make the change generically and test it here. The notebook's version is written in its own domain's terms, so **rewrite it generically here; never copy the notebook's file in**. Its specifics may stay only as a case study that says where it came from ("in the notebook this grew from").

**Every change for an issue is tied to it, and the issue is closed when the change is done.** One commit per issue where it can be, holding only that issue's change. Its message names the issue: `Closes #<n>` on the commit that finishes it, `Refs #<n>` on any before. Push it, so GitHub closes the issue from the commit, then check the issue is closed. Leave a short comment on it saying what changed. An issue left open is work not done; an issue closed by hand, with no commit, has no change to show.

## Checks

```
python3 .scripts/vault_check.py
python3 .scripts/types_check.py
python3 .scripts/audit.py
```

The template has no entity pages, so a clean run proves only that the skeleton is consistent. A change to a script is tested against pages made for the purpose, which are deleted before committing.
