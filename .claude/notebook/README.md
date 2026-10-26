# A notebook system for domains where the categories are part of the discovery

**Domain-neutral, Obsidian-specific.** Two different axes, and it is worth being honest about both: nothing in this folder names a domain, and everything in it assumes an Obsidian vault - wikilinks, frontmatter, Bases, backlinks, the metadata cache and Obsidian's own eventual consistency. A host repository supplies the domain; it does not supply the platform.

## What this is for

A notebook where **some of what you are writing down cannot be classified yet.** Not everything: you arrive with knowledge, and the structure you already know gets declared on day one. An engineer opening a notebook about their portfolio declares a product type immediately, before a single product is recorded, because they know perfectly well that products are a kind of thing.

The difficulty is the rest. Classify *everything* at capture time and you either stop writing or file wrongly; classify nothing and you have a diary you cannot query. This system is the set of moves that let classification arrive **late for the things that need it** while the things you already understand are typed from the start.

**Use it when** some of the categories are part of what is being discovered: a research log, an investigation, a reverse-engineered codebase, a diagnosis, product discovery, a game whose mechanics are the puzzle. Tabula rasa is not a requirement and rarely the reality - you come with knowledge and learn more.

**The exclusion is closure, not knowledge.** Do not reach for this when the domain is *closed* - when no new kind of thing will arrive, and when something that does not fit can be **rejected** rather than kept. Form validation, an order pipeline, a ledger on a fixed chart of accounts: there the hub is a bug and promotion is a migration. The test is not "do I know my types?" but **"when something does not fit, must I keep it?"** If the answer is yes, you need somewhere legitimate to put it, permanently.

## The schema's knownness is a stage, not a property

A notebook's schema is never simply known or unknown. It is always partly settled and still moving, so the layers do not all carry weight at once - the weight shifts:

| stage | what carries it | what the hub is doing |
| --- | --- | --- |
| early | capture, hub - **and whatever types prior knowledge already declared** | the things that knowledge did not anticipate |
| emerging | promotion, firing repeatedly | shrinking in share as sections graduate |
| settled | entities, reference, projection, checks | holding what has not settled, which is never nothing |

The reference layer arrives late and surprises people, because prose accumulates names faster than structure accumulates types, and the gap only becomes visible once there are enough entities for a name to miss one.

**Nothing graduates out of the system.** Parts of it mature at different rates, and the system is the thing that lets them mature separately. The notebook this grew from had, at one moment, fourteen settled types with queries over them - a known schema by any measure - *and* a hub still holding its theories, its unclassified observations and one hand-maintained table. The queries work **because** those types settled. The hub works **because** the rest has not. Both at once is the normal mature state, not a transitional one.

So a settled notebook is not "a database instead". The settled part **is** a database: typed records with queries over them. What this adds, and keeps adding at every stage, is two things a schema does not give you - **a legitimate place for what does not fit**, and **schema change that costs a sentence instead of a migration**.

## The ten layers

| layer | what it does | who defines it |
| --- | --- | --- |
| 1. Capture | arbitrary natural language in, append-only, **never blocks on classification** | generic: `capture.md` |
| 2. Hub | where unclassified observations legitimately live | host supplies the location |
| 3. Entities | typed pages, one per thing: a folder and a `type:`. A relationship binding three or more things is a page too, a relation; a part of one thing is a page it owns, in its folder, to any depth (`graph.md`) | host supplies the type table |
| 4. Ledger | what happened, in order: the occasions themselves | generic: `ledger.md`; host sets the granularity |
| 5. Reference | names onto entities, with *kinds* of mapping | generic: `reference-layer.md` |
| 6. Provenance | where a fact came from, as wikilinks in `source:` that Obsidian indexes as `frontmatterLinks` | generic: `contract.md`, "Frontmatter" |
| 7. Epistemic status | observation vs inference, corrections kept beside what they corrected | generic: `contract.md` |
| 8. Projection | derived output: views, pages rebuilt whole, and ledger entries prepared before they open | generic: `projection.md` |
| 9. Invariants | executable checks that report; the user decides | host supplies the checks |
| 10. Registry | the type system declaring itself: a page per type, a view over them, a check against reality | generic shape, host declares its types |

Promotion — the move from 2 to 3 — is `promotion.md`. Layer 10 is what lets capture interpret input *in the context of the types*; see `registry.md`.

Under all ten is one model: the notebook is a **labelled property graph** - pages are nodes, types and tags are labels, frontmatter holds properties, and links are edges, typed when they sit in a declared field. `graph.md` has the mapping, why a graph is what makes deferred classification legal, and the six things a pattern can become when it is promoted.

## The interface: what a host repository must supply

The generic layer is useless alone. A host specializes it by providing exactly these, and nothing here should need editing to accommodate a domain:

1. **The type table** — folder, `type:` value, and what goes in it. One row per kind of thing. This is layer 3 and it is the single most domain-specific artifact.
2. **Per-type page layout and writing rules**, declared on each type's page: `sections:` for the headings every page has, and `## Writing to it` for how to write one, split into on create, on update and on link (`registry.md`). A source whose *contents* matter needs somewhere to put them that is not its provenance; a verbatim text needs its embed. Without this declared, a type's pages are shaped by whoever writes the next one.
3. **The hub location** — one file, or one per type. One file has held in practice.
4. **The domain's epistemic law** — two choices made at setup, and the domain's particulars. **How far Claude goes beyond recording** is the level of assistance, `assistance.md`; **what Claude may read** is the consultation, `consultation.md`; a notebook holds the one file of each it chose, and `CLAUDE.md` names both. The host contract adds only what is particular to the domain - which sources the choice means, and whose discovery this is. Capture obeys all of it.
5. **Per-type routing** — the extra steps capture takes for particular types. What belongs to one type - an aggregate page every mention must reach, a field a kind of instance always carries - goes on that type's declaration, in `## Writing to it` (`registry.md`). What the host keeps separately is only routing to something that is not a type: a hub table that must be updated, a cross-index.
6. **The checks** — the executable invariants, as scripts in `.scripts/`, and the command that runs them. See `contract.md` on what makes a good one.
7. **The ledger** — a type declared with `ledger:`, named for what an occasion is here — a day, a sitting, a sprint, a project — and the skills that open and close one. Capture finds it through the registry, so the declaration is the whole of telling it. See `ledger.md`. A notebook with no occasions to speak of is the only case where this is genuinely absent.
8. **Paths and tools** — where the vault is and what talks to it.

**Everything else a host adds goes in an outlet, never in a generic file**: its settings and audit rules in `.scripts/notebook_config.py`, its own operations and checks in scripts of its own beside the generic ones. `upstream.md`, "The outlets", has the table. A generic file a host has edited cannot be brought level with the template without losing the edit, which is why the outlets exist.

**The host's session file must survive a type change at any time.** It is read at the start of every session and nothing updates it, so it holds only what stays true however the schema moves: where things are, what to read, the domain's law, and conventions. It never fixes a classification - *these are not a type*, *X will always be filed as Y* - because classification is deferred by design (`graph.md`), and a line that forbids a promotion is a decision the session file cannot know it is still right about. Where a classification needs recording, it goes on the declaration that makes it, which the reverse gear can change.

## Files here

There are **two kinds of file here and they are used differently**, which is worth knowing before reading any of them.

**Laws and mechanics** - they govern everything and no single skill implements them:

| file | holds |
| --- | --- |
| `obsidian.md` | the platform: filename legality, link resolution, the CLI |
| `contract.md` | the eight laws, the page shape, frontmatter, linking |
| `reference-layer.md` | how names reach entities, and the five kinds |
| `graph.md` | the model: the notebook as a labelled property graph, and the six things a pattern can become |
| `registry.md` | the type system as data: what is derived, what is declared |
| `assistance.md` | this notebook's level of assistance - how far Claude goes beyond recording - one of the template's levels, chosen at setup |
| `consultation.md` | what Claude may read in this notebook - one of the template's choices, made at setup |
| `requests.md` | how a notebook asks the template for a change: an issue in the template's terms, never an edit |

**Skill contracts** - each specifies one or more skills **the host must write**, because this folder ships none:

| file | specifies | which does |
| --- | --- | --- |
| `capture.md` | **1** - the capture skill | files arbitrary input, the hot path |
| `ledger.md` | **3** - open, resume, close | the lifecycle of an occasion |
| `promotion.md` | **2** - declare, promote | the type, and fitting data to it |
| `projection.md` | **2** - the compile and prepare skills | the narrative output, and the entries prepared before an occasion |
| `upstream.md` | **1** - the update skill | bringing a notebook level with the template it came from |

**So ten skills, and none of them are in this folder.** The template ships eight as skeletons and two whole - the update skill, and `/rename`, which `obsidian.md` and `registry.md` specify - because nothing in them is a host's. `manifest.txt` says which files a notebook takes unchanged and which it owns. For the rest, a host reads the contract and writes a thin skill - frontmatter, a line saying which contract to read, and its own paths. The host's skill holds nothing the contract already says; see "Name roles, never the host's names" below for why it does not even get named here.

A host may split a role across several skills where its domain wants the distinction: a capture skill per kind of input, for instance. That is specialization, not a departure.

## Where the pieces live

Claude Code's own layout, named rather than described:

```
CLAUDE.md                              read at session start; points here, then adds the host's eight items
.claude/notebook/                      this folder, copied in unchanged
.claude/skills/<name>/SKILL.md         one per skill; `name:` and `description:` frontmatter, and the
                                       description is what decides whether the skill triggers
.claude/skills/_shared/<host>.md       the host contract, read by every skill that files anything;
                                       the template ships a skeleton as host-contract.md
.scripts/                              the operations and the checks, with paths derived from the script's own location
.scripts/notebook_config.py            the host's settings, and the outlet for its own audit rules
.scripts/<host>.py                     the host's own operations - how an occasion is named, say - importing
                                       notebook.py and never editing it; its own checks beside them
Views/*.base                           one Bases view per entity type; Types.base is the registry's own
.obsidian/plugins/notebook-graph/      gives every local graph the colour groups the registry derives (graph.md)
```

A skill reads shared material by naming its path and nothing more - there is no include mechanism, so a `SKILL.md` says *"read `.claude/notebook/capture.md` first"* and that is the whole coupling. Which is also why duplication drifts: anything a host contract restates instead of pointing at will fall out of step.

## Adopting it

**Run `/setup` in the template.** Setup is one time and one way. Its renames are mechanical but what they rename *to* is judgement, so the skill asks the choices and `.scripts/setup.py` carries them out: in a folder of its own, from the template's last commit, never overwriting a file. The template is only read, and neither the skill nor the script is copied, so a notebook has no setup in it to run again. Every skeleton marks what it leaves to the host with a TODO.

`/setup` does the first three steps; the rest happen in the notebook.

1. **Get the files**: this folder, the skeletons, `Types/`, `Views/Types.base`, the hub, `.scripts/` and `.obsidian/plugins/notebook-graph/`. `CLAUDE.host.md` becomes `CLAUDE.md`; the template's own `CLAUDE.md` and `README.md` are about the template and stay behind.
2. **Name things what this domain calls them.** The hub's file, and `HUB` in `.scripts/notebook_config.py`. The first ledger: its type, folder, kind and sections, with a view over it - more can be declared later. The host contract's file, and every pointer to it. Each skill's folder and `name:`, and the skills not wanted removed: `resume` if only one entry is ever open, `compile` if there is no story to tell.
3. **Write what only the host knows:**
   - `CLAUDE.md` - the eight host items, each a line or a table row pointing somewhere. It must survive a type change (above)
   - the host contract - the domain's law, routing to what is not a type, the hub's sections, the repo's rules
   - each skill's TODOs - its commit message, and what this domain calls an occasion
4. **Open the folder in Obsidian** and enable the notebook-graph plugin. Run `notebook.py graph` after declaring types, so both graph views show them.
5. **Declare the first types** with the declare skill - before anything of the kind exists, where prior knowledge already knows it is a kind of thing.
6. **Build the checks before you need them.** An unenforced convention survives about as long as the session that wrote it.

## Changing this folder

**A change to the generic layer is made in the template first, as though no host existed, and reaches a host through the update skill.** Never the other way round, and never by copying files blind.

- **A host asks for it; it never makes it.** Its session opens an issue on the template's repository, in the template's terms (`requests.md`), and the change is made here.
- **Write it in the template, generically.** The change usually arises in a host, mid-work, with that host's material in view - which is exactly when its names slip into the examples. So write it from the template's side: placeholders in anything a reader will copy, and a host's specifics only in a case study that says where it came from (below). A change that cannot be written without the host's names is not generic yet.
- **Test it in the template on its own.** Its checks and its scripts, against its own pages.
- **Then bring it into each host with the update skill** (`upstream.md`). It sorts out what the host's copy has picked up before it takes anything, so nothing is overwritten unseen. Otherwise a host's copy of this folder is never edited in place and never copied back: what a host learns goes into the template rewritten, and returns as the generic version. A copy in either direction carries whatever the source has picked up, and a host's copy picks things up because agents work in it.
- **A diff between the two copies is evidence, not a procedure.** It says where they differ; whether a difference is generic is the test below, applied each time.

## What may and may not appear in this folder

Several sweeps have been needed to keep this clean - for domain terms, for pretending Obsidian was interchangeable, for host skill names, and for spec examples. The rules that prevent another:

- **Name roles, never the host's names.** "The capture skill", not `/note`. A host renames freely, and a generic page that states its name is wrong the moment it does.
- **This folder may name its own skills.** `/promote` belongs to the system, so prescribing it here is a recommendation rather than an assumption.
- **Two kinds of example, and they have opposite rules.** A **case study** - the narrative that gives a law its force - keeps its specifics and says where they came from ("in the notebook this grew from"). A **spec example** - a frontmatter block, a syntax fragment, anything a reader will copy - takes **placeholders**, never a real name, because a concrete name in a spec reads as part of the spec. Sweeps kept being needed here and this distinction is why: the case studies were fine every time, and the spec examples quietly filled up with one domain's rooms and people.
- **Obsidian is not abstracted.** Name `unresolvedLinks`, `![[...]]`, Bases and the metadata cache directly. The platform is a dependency, not a variable.

The test of whether the separation is clean: **a change to the generic system should never require editing the host's contract, and a new entity type should never require editing this folder.**
