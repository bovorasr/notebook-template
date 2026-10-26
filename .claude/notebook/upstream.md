# Upstream: bringing a notebook level with its template

Generic. Specifies **one skill, the update skill**, which the template ships whole because nothing in it is a host's. A notebook takes its generic files from the template once, at setup; the template goes on improving; this brings the improvements in **without losing what the notebook has made its own.** `.scripts/upstream.py` does the mechanical half - fetching, comparing, copying - and decides nothing.

## Three versions, not two

| version | what it is |
| --- | --- |
| **the base** | the template at the commit the notebook's generic files are level with - `TEMPLATE_COMMIT` in `.scripts/notebook_config.py` |
| **the notebook's copy** | what is in the notebook now |
| **the template now** | its newest commit, fetched |

The notebook against the base is **drift**: what the notebook changed. The base against the template now is **upstream**: what the template changed. Comparing the notebook straight with the template now runs the two together, and then nothing can say whether a difference is the notebook's own or something it has not yet taken - which is why the base is recorded at all.

## Drift is expected, in the right place

`.claude/notebook/manifest.txt` sorts every file a notebook gets into two kinds, and drift means something different in each. (A **choice** - `assistance.md`, `consultation.md` - is a generic file whose text comes from the one source the notebook chose; `upstream.py` compares it with that source, and the guard refuses any other source turning up in a notebook.)

- **A skeleton** - the session file, the hub, the skills, the host contract, the config, the ledger's declaration - **is the notebook's own.** It was meant to diverge, and different notebooks are meant to be different. It is never restored; upstream changes to its skeleton are *adapted* into it by hand, in the notebook's own names.
- **A generic file is never edited in a notebook, except by this skill.** So any difference between it and the base is misplaced by definition, which is what makes drift findable at all - and nothing in it is lost, because each kind of difference has somewhere to go:

| a difference that is | goes |
| --- | --- |
| **the domain's material** - its names, its rules, its case studies | to its outlet, below; the generic file goes back to the template's version |
| **an older version** of something the template has since changed | away: the template's version replaces it |
| **a generic improvement made here** | to the template, as an issue (`requests.md`). Until the template has it, it stays, and is reported as drift every time |
| **a difference the notebook needs, with no outlet** | stays, and is reported as **a gap in the template**: say what outlet would have held it, in an issue (`requests.md`). That is a template change, made there first |

### The guard

**What keeps a generic file the template's after that is a check, not a rule.** `upstream.py verify --staged`, installed as the notebook's pre-commit hook, refuses a commit in which a generic file holds text the template never gave it - at the recorded base or any template commit since. So the update's own commits pass, because `take` writes the template's text, and nothing else that touches a generic file does. A notebook's material goes to its outlet instead, and a change meant for every notebook goes to the template first.

Git keeps hooks per checkout, not in the repository, so each checkout installs it: **`.scripts/checkout.py`**, run once in a fresh clone, fetches the template for the guard to compare against and installs the guard, and says so - or that there was nothing to do. Setup runs it for a new notebook, and `notebook.py open` and `close` run it quietly - a session commits after them - so a checkout that lacks the guard gets it before its first commit, whether or not anyone remembered. `status` names a checkout without it. `upstream.py verify`, without `--staged`, checks the working tree the same way.

### The outlets

Each is where a notebook puts what the generic layer cannot know. A generic file points at them; a notebook fills them.

| what | outlet |
| --- | --- |
| the hub's name, pages no tool may touch, group fields, graph additions | `.scripts/notebook_config.py` |
| generated pages, verbatim texts | their type's declaration: `generated: true`, `sections: []` (`registry.md`) - never a list of page names |
| the domain's own audit rules and deferral wording | `AUDIT_DEFERRALS` and `audit_page` in `.scripts/notebook_config.py` |
| operations particular to the domain - how an occasion is named, what carries from one to the next | the notebook's own script beside `notebook.py`, which imports it and never edits it (README, "Where the pieces live") |
| checks particular to the domain | the notebook's own script in `.scripts/` |
| the domain's law, routing to what is not a type | the host contract |
| a rule for one type | that type's declaration, `## Writing to it` (`registry.md`) |
| the notebook's own history in a generic file - an incident, a date, a case study naming its pages | git history, where it stays readable; the template's version keeps the generic telling of the same lesson |

## The runbook

**The notebook's law holds while updating.** The update touches machinery, but reading a generic file to sort its drift can mean reading the domain's material; nothing found there is looked up or remarked on.

**Start from a clean tree.** If the notebook has uncommitted work, ask the user to commit it first - never stash or commit someone's notes for them.

**The notebook's repo rules hold for the update's commits too** - the host contract's "The repo": if it pushes after every commit, so does this.

1. **Fetch.** `upstream.py fetch`. If the notebook has no `TEMPLATE`, ask the user for the template's address - the one every checkout can reach, not a path on one machine, since `record` keeps it as `TEMPLATE`. The fetched template is kept in the notebook's repo as `refs/template/head`, apart from its own branches, and the address in its git config as `notebook.template`.
2. **Find the base.** `upstream.py status`, which ends with the candidate base: the commits inside every matching file's range. With a recorded base, that is it. Without one - a notebook older than the record - `status` gives, per file, the range of template commits it is level with (*from* the commit that made it so, *until* the next to change it), or the nearest commit when it matches none. The base is a commit inside every matching file's range, leaving out the update's own files, which `status` marks: a notebook older than the update took them at the newest commit, so they say nothing about the base. Nor does a file that matches no commit. The notebook's own history - a commit saying what it last brought in - is evidence too. Show the user what it found and agree a base before going on: parts of an old notebook may predate the template itself.
3. **Level the generic files.** For each drifted file, `upstream.py diff <file> --at <base>`, and sort every difference by the table above. Show the user the plan in plain words, grouped: what goes back to the template's version, what moves to which outlet, what is a generic improvement to carry upstream, what is a gap. On agreement, move each piece of the domain's material into its outlet, then `upstream.py take <file> --at <base>`.
   - A difference **gone from the template since** - a skip list a later version derives instead - goes the same way as the rest: to the template's version, if what replaced it covers the notebook's case.
   - Where a piece of the domain's material needs an outlet only a later template commit has, take that later version for the file, and say so: the leveling and the update meet there.
   - **A notebook older than part of the generic layer** may lack a generic file the others import - `missing here` in `status` - and the config they read. Take the missing file at the commit that reproduces what the notebook's own scripts did, which is usually the base but not always: read what it does, because a version that quietly does less - stops excluding something, say - passes every check. Make `.scripts/notebook_config.py` from the template's skeleton, at the commit whose outlets the leveling needs, with this notebook's values in it.
   - A file taken ahead of the base shows in `status` as `ahead: level with <commit>`. That is expected, and step 5 brings everything else up to meet it.
   - **Fill in `SKELETONS`** in the config if it is empty and the notebook renamed or dropped any skeleton - the session file, the hub, the ledger's declaration, the host contract, a skill. Setup writes it; a notebook older than setup has to have it worked out, and step 5 depends on it. A skill follows the same contract as the skeleton it came from - the `.claude/notebook/` file it says to read - which narrows the match; where several share a contract, the skeleton's match is the general one the others specialise or call.
   - **A notebook's own script that copies generic code** - an operations script written before `notebook.py` existed, say - is the notebook's, not drift. Report the duplication and ask whether to rebuild it on the generic one (the outlet above); never rebuild it unasked.
   - Run the notebook's checks before and after. Their findings should be the same, apart from what the plan said would change; a difference nobody predicted means something was lost. **The checks are not everything a generic file does**: compare what the rest produce too - a migration's dry run, the graph view derived (`notebook.py graph --print` against `.obsidian/graph.json`).
   - `upstream.py record <base>`, so the next steps compare from it. Commit: `Level the generic layer with notebook-template <base>`.
4. **Offer what is upstream.** `upstream.py log` lists the template's commits since the base, each file marked generic, skeleton or the template's own. Group them into **features** - what the notebook would gain, in plain words, not commit subjects. A commit touching only the template's own files reaches no notebook; leave it out without asking. Ask which to bring in.
   - **A feature that changes generic files is taken up to a commit, not picked out of one**: the base is a single commit every generic file is level with, so skipping one means stopping before it, and the rest waits for the next update. A feature that only changes skeletons can be skipped freely.
5. **Bring them in.**
   - **Generic files**: `upstream.py take <file> --at <commit>`.
   - **Skeletons**: `upstream.py skeleton` shows what changed in each since the base - `--to <commit>` when stopping short of the newest - renames followed, and the notebook's own file it goes into (`SKELETONS`). Make the same change there - a new config name with its default, a new section in the host contract, a new step in a skill - in the notebook's names, never the skeleton's placeholders. **A skeleton's diff shows what changed in the skeleton, not in what a notebook filled it with**: a removed TODO may stand for a value every filled-in file wrote its own way. Read the commit message for what the change is for, and carry that through the notebook's files - including those no skeleton maps to. `status` names config entries the template has and the notebook lacks.
6. **Check, record, guard, commit.** Run the checks. `upstream.py record <commit>`, then `checkout.py` if `status` says this checkout has no guard. Commit: `Update from notebook-template <base>..<commit>`, naming the features brought in and the ones left.

## After the first update

With the guard in place, the generic files cannot have drifted, so there is nothing to sort: `upstream.py fetch`, then `upstream.py update` takes every generic file up to the newest commit (or `--to <commit>`), records it, and lists the skeletons left to adapt. With none, commit as it says and the update is done, no skill needed. With some, adapt them as step 5 says, check, and commit.

Offering features (step 4) still applies when the user wants to stop short of the newest commit: `update --to <commit>`.

## Reply

What was leveled, what was brought in, what was left and why, and every gap in the template found on the way, each drafted as an issue for the user to open (`requests.md`).

## A notebook older than the update skill

It has no `upstream.py` to run. Run the notebook's checks first and keep their output, with everything else step 3 will compare - a migration's dry run, the derived graph, any verbose listing - since this is the first change. Then bring `upstream.py` in - a new file, so nothing is overwritten - and let it bring the rest:

The template's URL is the address every checkout can reach, since it becomes `TEMPLATE`. Updating only up to an earlier commit, add `--at <commit>` to each `take`.

```bash
git fetch <template URL> HEAD && git show FETCH_HEAD:.scripts/upstream.py > .scripts/upstream.py
python3 -I .scripts/upstream.py fetch <template URL>
python3 -I .scripts/upstream.py take .claude/notebook/upstream.md
python3 -I .scripts/upstream.py take .claude/notebook/manifest.txt
python3 -I .scripts/upstream.py take .claude/skills/update/SKILL.md
python3 -I .scripts/upstream.py take .scripts/checkout.py
```

Install the guard with `python3 -I .scripts/checkout.py`, so nothing but the template's text reaches a generic file from here on, this commit included. Then commit these on their own - `Bring in the update skill from notebook-template <the commit taken>` - before anything else: they are the update's own machinery, not the user's notes. Then run the update skill from step 2.
