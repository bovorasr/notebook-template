# The ledger

Generic. A record of **what happened, in order**, as distinct from the entity layer's knowledge at rest. A daily note, a session log, a project logbook, a lab notebook's dated entry: all the same shape.

The host **declares** it: a type with `ledger:` set (`registry.md`), named for what an occasion is here - a day, a sitting, a visit, a sprint, a project - and the skills that open and close one. Capture writes to the open entry (`capture.md` step 1), and **fails loudly when there is none** rather than inventing it.

## Why it cannot be derived from the entity pages

The entity layer is organized by subject, which destroys three things. Only the ledger can answer:

- **order** - what came before what, and what I believed at the time
- **co-occurrence** - these findings arrived together, in one sitting
- **conditions** - the state of the world while they did, which may never be true again

A notebook with no ledger can tell you everything known about a thing and nothing about how it came to be known. In a discovery domain that reasoning trail is most of the value, which is the same argument as law 5.

## It is a subject, not an exception to law 4

A finding's entity bullet says *this is true of X*. Its ledger entry says *on occasion N, here is where I found it*. Same observation, two subjects, each framed for its own page - exactly law 4's third case, with **the occasion as one of the subjects**. So the duplication needs no special licence, and the ledger entry is usually one line: where it was and what it said. The full statement lives on the entity pages.

## Its own five laws

1. **Append-only, and never corrected in place.** This is where law 5 lands. On an entity page a correction *replaces* the bullet, because that page states what is true. On the ledger it must not, because the ledger states what *happened* - and what happened includes believing the wrong thing at the time. **The ledger is where an overturned reading survives.** Correct the entity pages; leave the ledger alone.

   **An entry's identity is fixed when it is created.** If the scheme that named it is later corrected - an anchor adjusted, a numbering fixed - existing entries keep the names they were created with, because renaming them rewrites what the record said at the time. Say the names are now off and let the user decide; do not tidy them.

2. **It is the only home for what was true only then.** A condition holding for one occasion has no entity page, because it is not true of the entity in general. The standing fact *that* something varies belongs on the entity's page; the value it had this time belongs only here. Writing such a value to an entity page states something false.

3. **Entries are framed for the occasion.** Not a copy of the entity bullet - a line that makes the finding findable in sequence and lines it up against the conditions above it.

4. **It is the unit of diff.** One commit per occasion makes the notebook's history readable as *what changed this session*, which is also what lets a narrative projection be read as a diff rather than re-read as a document. Where occasions overlap - a visit inside a day - closing one commits everything written so far, named for the entry closed, since the pages they share cannot be split between them; the one still open carries on in later commits. What was written while no entry of its own was open goes with the next close. The one exception is a promotion run while an entry is open: it checkpoints the capture so far first, so the migration is its own commit (`promotion.md`, "The runbooks").

5. **No tool backfills it.** A converter that rewrites prose across the notebook - a linker, a reformatter - must exclude the ledger, except for maintenance (below), and law 4 is the sharper reason why: rewriting a closed entry changes *its diff*, so the record of what that occasion changed is no longer what the occasion wrote. Capture links an entry as it writes it; nothing goes back. The same applies to generated pages and verbatim texts: **a tool does not edit a page it does not own.** The one thing that may touch a closed entry is **maintenance**, below.

### Maintenance is not rewriting

The five laws protect **what the entry says** - what was found, what was believed, in the words written at the time. They do not require a closed entry to break when the notebook around it changes. A record whose image has gone missing or whose links point at nothing has not been preserved; it has been damaged by standing still.

**The test: would someone reading the entry learn anything that could not have been known on that occasion?** If not, the change is maintenance, and it is allowed. If so, it is rewriting history, and it is not.

**And it cuts both ways: maintenance is lossless.** Think of a paper journal being digitised - re-attaching the scanned photos to the transcribed page is fine, because afterwards you can still tell exactly how the day went and what was thought, no more and no less. A change that loses any of that - a dropped image, a line no longer readable as it was - fails the test just as surely as one that adds what was learned later.

**A closed entry is closed to reclassification.** What it named, and how it classified it - which words it linked, and to what - was fixed when it closed. Maintenance keeps that working as the notebook changes around it; it never adds a classification the entry did not make, even a correct one. That is what reclassifying is, and it belongs to the entity pages and to later entries.

| maintenance - allowed | rewriting - never |
| --- | --- |
| an attachment renamed, its embed following the rename | a fact, finding or correction learned later |
| a link updated so it still resolves after a page is renamed, re-typed or promoted - the words as written kept, as the alias | a guess restated as what it later turned out to be |
| an existing link **repointed** so it lands on the same thing it always meant, when a type is declared or re-shaped and the page it pointed at moves or splits | **any new link on a plain word**, even to the right page - linking "brass" to the material, or "the person in the photo" to whoever they later proved to be, classifies the entry after it closed |
| repairing what fails to render: invalid frontmatter, a broken embed | rewording, reordering, tidying for style |
| moving an entry into the bucket its name puts it in, or out of one (`registry.md`, "Buckets") - its name and words unchanged | renaming an entry to suit a new folder |

- **The words stay.** Maintenance adds or repairs links and file references around the text; it never changes the text a reader sees.
- **It is its own commit**, named as maintenance, never folded into an occasion's commit. The occasion's diff then still shows exactly what that occasion wrote, and the maintenance shows as what it was.
- **A discovery about an earlier entry goes in the entry for the day it was made**, linking back: *"the person in the photo in [[<earlier entry>]] is [[<Person>]]"*, written in a later entry, links back to the earlier one and to the person. The earlier entry keeps "the person in the photo" as written, and the entity pages carry the identification from then on.
- **The entry's own name is not maintenance.** Renaming an entry rewrites its identity, which law 1 fixes at creation.

## Lifecycle

A ledger entry has a lifecycle, and its controls are **skills**, which the host names and points back here:

| operation | what it does | host examples |
| --- | --- | --- |
| **prepare** | create the entry a projection writes before the occasion starts, or find it again (below) | a prep step the day before |
| **open** | create the entry for a new occasion and make it active - or make active the one prepared for it | `/<open> <n>`, `/today` |
| **resume** | make an existing entry active again | `/resume <name>` |
| **close** | mark it finished, and checkpoint | end of a day or a sprint |

**Close is the natural commit point**, which is law 4 above: one commit per occasion, and the narrative projection rebuilt against it if the domain has one.

**Open and resume show the entry.** Once the entry is active, open it in the app if the app is running (`obsidian.md`, "Showing the user a page"). It is the page the user is about to work in, and they should not have to go looking for it. Close does not open anything: it links the entry it closed, since the occasion is over and the user has moved on.

### Three states: prepared, open, closed

| state | who writes it | how it gets there |
| --- | --- | --- |
| **prepared** | a projection, into the sections the ledger lists as `prepared:` (`registry.md`), as often as it is run: preparing the same occasion again - the same variables, so the same name - finds the entry it made and rewrites it | `notebook.py prepare`, then `notebook.py fill <entry> <section>` |
| **open** | the ledger's, append-only like any entry. What the projection wrote is now the user's as much as the rest, and no projection touches it again | `notebook.py open`, which opens a prepared entry, or makes an open one directly |
| **closed** | nothing, as ever | `notebook.py close` |

**Most ledgers never prepare**: an entry made by `open` starts open, as every entry did before prepared existed. Preparing is for an occasion a projection writes the top of - the questions to ask, the agenda - before it starts. How a host wires it is the host's: a prep skill run ahead and `/open` when the occasion begins, or one skill that prepares and opens at once.

**Capture never writes to a prepared entry**: it is not active yet, so capture's first step does not list it as open (`notebook.py current` shows it apart).

### A ledger owned by an entity

A ledger type with `parents:` (`registry.md`) is **one ledger per owner**: the sessions held with each person, each in that person's folder (`graph.md`, "Ownership"). Everything above holds per owner:

- **A periodic owned ledger has at most one open entry per owner** - `notebook.py open` refuses a second until the first is closed - and none at all is ordinary: an owner with no occasion going on needs nothing opened, so capture does not ask about one.
- **Its entries are named from the variables above them** - `{date} - <Session> - {name}` - and, by law 1, keep the name they were made with even when their owner is renamed.
- **An entry may own pages of its own** - the actions agreed in a session - and becomes a folder when the first arrives, its filename unchanged.
- **The owner's page comes first**: an entry is made under it, so a session with someone new starts by making their page (capture, from its declaration), then opening the entry. The entry can then be the page's `source:` from the first fact on.
- **An occasion with several owners is an entry for each** - a session held with two people at once is one in each of their ledgers, each naming who else was there in its `occasion_only:` section - since an entry has one owner, and what each person said is theirs.
- **A prepared entry may be moved while nothing has happened on it.** Law 1 fixes an entry's name when it is made because the name records an occasion; a prepared entry records none yet. If the occasion moves, prepare the new one and delete the old while it is still prepared. Once opened, law 1 holds.

### Two kinds, which compose

| kind | identity | how many active | "active" means |
| --- | --- | --- | --- |
| **periodic** | a date or a sequence number | exactly one | the current one - today's, or the latest |
| **span** | a named thing with a duration | any number | explicitly open |

They compose, and this is the case that matters: a notebook can have today's entry *and* two open experiments active at once, and one finding is logged to all three. A domain with a single periodic ledger is the degenerate case, not the general one.

### The active set is state, and must be recorded rather than derived

With one periodic ledger, derivation seems to get by - *"the current one is the highest-numbered"* - until the latest occasion is over and the next has not begun, when the highest-numbered entry is finished and nothing is current. It breaks for good as soon as a second can be open, because nothing on disk says which project you are in.

So record it, and **frontmatter on the entry is the place**: `status: open` on a span entry makes the active set a query rather than a state file, visible in the vault and answerable by a view, with nothing to drift out of step. A periodic entry carries the flag too: its date says *which* occasion it was, not whether that occasion is still going on.

### What capture does with it

**Capture reads the active set; it never derives it** - its first step. And it distinguishes two failures that look alike:

- a **periodic** ledger with nothing active is an error - ask which occasion, never invent one
- a **span** ledger with nothing open is ordinary, and not an error at all
- an **owned** ledger with nothing open for an owner is ordinary too; when something said belongs to an occasion with someone, and none is open for them, ask - never open one to have somewhere to put it

## The hub is a queue; the ledger is a log

They are different axes and an observation can need both:

| | the hub | the ledger |
| --- | --- | --- |
| an observation goes there because | its **type** is not known yet | it is **scoped to one occasion** |
| its contents | are supposed to leave, by promotion | never leave |
| it empties | eventually, when a type arrives | never, and should not |

So a hub section filling up is a signal (law 1). A ledger growing without bound is not a signal at all - it is the ledger working.
