---
name: setup
description: Set up a new notebook from this template - asks the choices that shape it (what it is about, where it goes, its hub, its ledger, which skills it keeps) and creates it in its own folder. Runs in the template only; a notebook has no setup in it. Use when the user wants to start a new notebook.
---

# Setup

**One time, one way.** The choices are judgement, so this skill asks for them; `.scripts/setup.py` carries them out and never overwrites anything. Read `.claude/notebook/README.md` first - "The interface" and "Adopting it" - and `.claude/notebook/ledger.md`, "Two kinds, which compose".

## 0. Is this the template?

If there is no `CLAUDE.host.md` at the repository root, this is a notebook: setup has already happened and there is nothing to do. Say so, and that `.scripts/setup.py` and this skill can be deleted if they are here. Stop.

## 1. Ask

One choice at a time, each with a default proposed from what the user has already said. Ask in their domain's words, not the system's: "what do you call a sitting?", not "name the periodic ledger type".

| choice | flag | how it is decided |
| --- | --- | --- |
| where | `<target>` | a new folder, or an existing repository that is not a notebook yet |
| what it is about | - | a phrase; it goes into `CLAUDE.md` in step 3 |
| the hub | `--hub` | what this domain would call the pile of things not yet understood |
| the ledger | `--ledger`, `--ledger-folder`, `--ledger-kind` | what an occasion is here. **periodic** if they come one after another - a day, a session; **span** if they are named and run side by side - an experiment, a case. Setup declares the first ledger; another is declared later with the declare skill. `--no-ledger` only when there are no occasions at all |
| its sections | `--log-section`, `--occasion-section` | where capture logs, and where what was true only then goes. Default `Notes` and `Working notes` |
| the skills | `--skill old=new`, `--drop` | capture renamed to this domain's verb if it has one. Drop `resume` when the only ledger is periodic, `prepare` when no ledger's entries are written before their occasion, `compile` when there is no story to tell, and `open`, `close` and `resume` when there is no ledger |
| the host contract | `--contract` | named for what the notebook is about |
| **the level of assistance** | `--assistance` | how far Claude goes beyond recording. **scribe**: records, and never originates a connection, a reading or a structure - for a notebook where the discovery is the point, a puzzle or an investigation. **advisor**: points out connections and conflicts in its replies, marked as its own, and records them only when asked, under `## Inferred`. **analyst**: points them out and records them unasked under `## Inferred`, and suggests structure whenever it sees the need. At every level structure is made only on the user's word. Ask what they want the notebook to *do for* them; offer scribe where they would rather work things out themselves |
| **the consultation** | `--consultation` | what Claude may read. **closed**: the notes, and what the user says or shows - nothing looked up. **references**: also documents the user names or puts in the notebook. **open**: also the web, reference works and Claude's own knowledge, each cited. Independent of the level of assistance |

**The two choices decide which rules exist in the notebook at all**: it holds the one file of each it chose, and never the others, so ask them plainly and record the answer exactly. Both are named in its `CLAUDE.md`. Changing one later is possible - set it in `.scripts/notebook_config.py`, `upstream.py take` the file, and bring `CLAUDE.md`'s line level - but it is meant as a choice made once.

## 2. Run it

`python3 -I .scripts/setup.py <target> <flags> --dry-run`, show the user what it would write, then run it without `--dry-run`. If it refuses, report why and stop - it refuses to overwrite, to set up a notebook twice, and to write inside the template, and each of those is the user's to resolve.

Commit in the target, exactly the files it wrote: `Set up from notebook-template <sha>`, with the sha it printed, so the notebook records what it came from.

## 3. Fill in what only the host knows

In the target: the TODOs in `CLAUDE.md`, in the host contract and in each skill - above all the domain's epistemic law (README, item 4), which capture obeys from the first note. What the user does not know yet stays a TODO, and say which: a guess written down as a rule is worse than a gap.

Commit that separately, so the notebook's history shows what was decided apart from what was copied.

## 4. Hand over

The rest happens in the notebook, where its own skills and contract load:

- open the folder in Obsidian as a vault, turn off restricted mode, and enable notebook-graph
- open Claude Code there and declare the types already known, with the declare skill - before anything of the kind is recorded (README, "Adopting it")

## Reply

The notebook's path, what was chosen, and what is still TODO. Nothing else.
