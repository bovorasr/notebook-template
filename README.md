# A notebook template

A note-taking system for domains where **some of what you write down cannot be classified yet** — a research log, an investigation, a reverse-engineered codebase, a diagnosis, product discovery. It is an Obsidian vault, and the system is deliberately Obsidian-specific: wikilinks, frontmatter, Bases, the metadata cache.

It grew out of one notebook about one game, which is why the laws below cite cases rather than assert principles. Every one of them was arrived at by getting it wrong first.

It is built to be run by [Claude Code](https://claude.com/claude-code): the rules in `.claude/notebook/` are written for an agent to follow, and the skills in `.claude/skills/` are how you drive it - you say what you found, and the notebook files it.

**Start at `.claude/notebook/README.md`** — the ten layers, and the eight things a host supplies.

## What you need

- **[Claude Code](https://claude.com/claude-code)**, to run the skills.
- **[Obsidian](https://obsidian.md)** (desktop), with its **CLI enabled** - Settings → General. The scripts ask the running app what it knows - its link resolution, its metadata cache - and renaming a page goes through it so every link follows. Without the app they fall back to parsing the files themselves, and say so.
- **Python 3.9 or later**, standard library only.
- **git**, and a **GitHub** account with the **[GitHub CLI](https://cli.github.com)** (`gh`) signed in: a notebook fetches updates from the template's repository, and asks it for changes by opening issues there.
- Optional: Obsidian's **Terminal** community plugin, to read Claude's replies inside Obsidian with page links you can click (`.claude/notebook/obsidian.md`, "Showing the user a page").

## What is here

| | |
| --- | --- |
| `.claude/notebook/` | **the system.** Its laws and mechanics, the contracts the skills follow, the README, and `manifest.txt` - which files a notebook takes unchanged and which it owns. Copied in unchanged; nothing here names a domain |
| `.claude/notebook/assistance/`, `consultation/` | **the levels a notebook chooses from at setup** - how far Claude goes, what it may read. One file of each reaches a notebook, as `assistance.md` and `consultation.md`; the rest never do |
| `.claude/skills/` | **eight skeletons**, one per specified skill, and `_shared/host-contract.md`, the host contract's skeleton. Each is a line naming its contract and a TODO list of what you supply. And `update` and `rename`, shipped whole |
| `.scripts/` | **the operations and the checks** - `notebook.py` (create a page from its declaration, open / resume / close / log a ledger entry, derive the graph view), three checks, a migration (`relink.py`) and `upstream.py`, the update skill's comparisons. All import `notebook_config.py` and nothing else host-specific |
| `Types/`, `Views/` | the ledger's declaration, to rename, and `Types.base`, the registry's own view |
| `.obsidian/` | the notebook-graph plugin, and the graph view's display defaults |
| `CLAUDE.host.md`, `Hub.md` | skeletons of the session file and the hub. `CLAUDE.host.md` becomes your `CLAUDE.md` |
| `CLAUDE.md`, `.claude/skills/setup/`, `.scripts/setup.py` | the template's own: its session file, and `/setup`. None of them is copied into a notebook |

## Adopting it

1. **Fork this repository**, and turn on **Issues** in your fork (Settings → General → Features; GitHub turns them off on forks). Your notebooks are set up from your fork, fetch their updates from it, and open their requests for changes on it - so the template is yours to change, and nothing you write reaches anyone else.
2. **Clone your fork**, and open Claude Code in it.
3. **Run `/setup`.**

`/setup` asks what the notebook is about, where it goes, what to call its hub and its ledger, which skills to keep, and two choices that decide which rules the notebook holds at all - **how far Claude goes beyond recording** (scribe, advisor, analyst) and **what it may read** (closed, references, open) - then creates it in its own folder and fills in what you can already say. The template is never changed. The steps are in `.claude/notebook/README.md`, "Adopting it" - one list, so the two cannot disagree.

## Updating a notebook

**Run `/update` in the notebook.** It fetches the template, works out what has drifted in the notebook's generic files since the commit setup recorded, moves anything domain-specific to where it belongs, and then offers what the template has gained, as features to choose from (`.claude/notebook/upstream.md`). A notebook older than `/update` brings it in first: `upstream.md`, "A notebook older than the update skill".

**After that, a pre-commit hook keeps the generic files the template's**, so later updates have no drift to sort: `upstream.py fetch` and `upstream.py update` take the generic half, and `/update` is needed only when a skeleton changed upstream and has to be adapted by hand.

## Changing the template

**Your fork is yours.** Change it however you like; your notebooks pick up the changes with `/update`. When work in a notebook shows something generic does not fit, the notebook's session does not edit the template - it opens an issue on your fork, written in the template's terms, and you make the change there (`.claude/notebook/requests.md`). To take improvements from this repository, merge them into your fork the usual way.

## The one rule about this folder

`.claude/notebook/` is generic and `.claude/skills/`, `CLAUDE.md` and your host contract are not. **Generic content belongs in the generic layer; host files keep only what it cannot know.**

That boundary was swept several times while this was being written, and the leaks were never where expected: domain terms first, then pretending the platform was interchangeable, then host skill names, then the *spec examples* quietly filling with one domain's rooms and people, then principles stated only inside a skill. The useful test is narrow — **does this sentence depend on my domain?** — and the useful habit is running it as a grep rather than trusting that it reads fine.

Once you have adopted it, your host files are yours and will diverge. That is the point. `.claude/notebook/` is not: it stays the template's, and a change to it is made here first and brought into each host with `/update` (`.claude/notebook/README.md`, "Changing this folder").

## Status

A personal project, shared as it is. It is used daily, and it changes when use shows something wrong - but there is no support, no roadmap and no promise that an issue or a pull request will be answered. Fork it and make it yours.

## License

[MIT No Attribution](LICENSE): use it, change it, sell it, ship it, for anything, with no conditions - not even keeping the copyright notice. It comes with no warranty, and no one who wrote it is liable for anything it does.
