# The host contract

> TODO: rename this file to what the notebook is about, change the pointer to it in `CLAUDE.md` and each skill, and fill in each section. It is the one file every skill that files anything reads, so it holds **only what `.claude/notebook/` cannot know**. Anything it restates instead of pointing at will drift.

Read by every skill. Change it here, not in each skill.

Every path below is relative to the repository's root, which is the vault.

## The domain's law

The stance is this notebook's two choices, named in `CLAUDE.md`: how far Claude goes (`.claude/notebook/assistance.md`) and what it may read (`.claude/notebook/consultation.md`). This section holds only the domain's particulars - nothing either file already says.

- TODO: which sources the consultation choice means here - the ones closed, the documents that count, the ones to prefer or distrust
- TODO: whose discovery this is, and what filing may never pre-empt, with the case that taught it if there is one

## One page per thing

Each type is declared on its own page in `Types/`; `Views/Types.base` is the table and `types_check.py` compares it against the pages. **There is no copy of the table here**, and there should never be one: a copy is what drifts.

- TODO: how to choose a type when two fit, in this domain's terms - what a thing *is*, not where it was found
- TODO: any basenames two folders share on purpose, and the link form that disambiguates them (`obsidian.md`)

## Per-type routing

What capture owes beyond the entity pages, **for what is not a type**. Anything particular to one type goes on its declaration's `## Writing to it` (`registry.md`), never here.

- TODO: a hub table that must gain a row, a cross-index, a check to run after a kind of edit

## What stays in the hub

- TODO: which sections the hub keeps, and which embed a view instead of keeping a list

## What is true only of one occasion

- TODO: the phrasings that mean it here. Where it goes is the ledger's `occasion_only:` section (`ledger.md`)

## Where replies are read

- TODO: where the user reads replies - a terminal inside Obsidian, or somewhere else - and what makes a page link there (`obsidian.md`, "Showing the user a page")

## The commands

| job | command |
| --- | --- |
| does this name already resolve | `python3 -I .scripts/vault_check.py --check "<Name>"` |
| create a typed page | `python3 -I .scripts/notebook.py new <type> "<Name>" --source X` |
| log on the open entry | `python3 -I .scripts/notebook.py log "<line>"` |
| what this edit broke | `python3 -I .scripts/vault_check.py --since HEAD` |
| does each page stand on its own | `python3 -I .scripts/audit.py <the folders touched>` |

## The repo

- TODO: where it is pushed, and when. One commit per occasion is `ledger.md` law 4
- TODO: what must never be pushed or rewritten

## Settled

Decisions the user has made that belong to no one type. A decision about a type goes on its declaration instead, where the reverse gear can change it.

- TODO, or nothing yet

## Generated pages

- TODO: which pages a projection writes, so nobody hand-edits them. Their type declares `generated: true`, which keeps the tools off them too
