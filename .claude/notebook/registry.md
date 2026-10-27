# The registry: the type system as data

Generic. Layer 10. The host declares its own types; nothing here names one.

## Why prose is not enough

A type table written as prose in a document is read correctly and maintained by nobody. In the notebook this grew from, a type was in use on two pages for **months** while that document was edited three times without ever learning about it - because no mechanism compared what was declared against what existed.

That is the registry's job, and it is not what it first looks like. The value is **not** saving steps during promotion; most of those turned out to have better homes (see `promotion.md`). The value is two things prose cannot do:

- **Capture can interpret input in the context of the types.** Given that the types are known and one of them is a place, a sentence naming a place resolves at write time - no pattern matching, no case rules, no glossary. The hard version is a place whose name is also an ordinary word, which capture handles for free and a retroactive linker cannot. This is the question the retroactive linker can never answer and capture never has to ask.
- **Declared and actual can be compared.** A type in use with no declaration, a required field that pages do not carry, a field nobody declared: all catchable, none visible in prose.

## It has two halves, and only one is written

| | what it holds | who updates it |
| --- | --- | --- |
| **derived** | which types are in use, where their pages live, which fields they actually carry, how often | **nobody** - it is a query |
| **declared** | what the type is *for*, which fields are **required**, its page layout and how to write one, the per-type routing | the promotion skill, at the one moment a human is definitionally present |

**A view is a self-updating table.** That is the whole trick: the registry is not a table anyone maintains, it is a query over pages that each declare themselves. Nothing can drift out of step with a thing it is computed from.

So the declared half is small by construction - judgment only, because everything observable is observed - and it changes only on promotion, which is rare and user-triggered.

## Shape

**A page per type**, in its own folder, declaring itself: in frontmatter, its name in `declares:`, the folder its pages live in, `required:`, `optional:` and `sections:`; in the body, the sentence that tells it from its neighbours and the instructions for writing one. **The declaration is the type's whole contract** - its fields, its page template and its writing rules - so anyone writing a page of the type has exactly one place to read. Then a view over those pages is the table, and a script compares them against the vault.

**A declaration may say what a new instance starts as**, in `defaults:` - a mapping from a required field to its starting value:

```yaml
required:
  - type
  - status
defaults:
  status: <starting value>
```

That is what lets a page be **created from its declaration** rather than assembled by hand and corrected afterwards: page creation reads `required:` and `defaults:`, and the code that makes pages never learns any type's particulars. Without it, a starting value ends up hard-coded in a script for whichever type someone remembered - one type, in the notebook this grew from, while every type declared afterwards would have been created invalid.

**A declaration is the page template too.** `sections:` lists the headings every page of the type has, in order, and page creation writes them:

```yaml
sections:
  - Known
  - <a section particular to this type>
  - My reading
```

Omitted, it is `Known` then `My reading`. Every entity type keeps both, because attribution is structural (`contract.md`); a type adds its own headings around them. **List only the headings every page has.** A section that exists only when there is something to put in it - a verbatim text that some pages have and most do not - is an instruction, below, not a heading created empty on every page. `sections: []` declares a page with no headings at all, for a type whose page is a verbatim text and nothing else.

**And it carries the instructions for writing one.** How content is divided on a page, what belongs in which section, what another page must never defer to this one: that is judgment no field can hold, so it is prose for an agent, in the declaration's body under `## Writing to it`. It is split by the moment it is needed, because each moment is a different act and reads only its own part:

| subsection | read when | holds |
| --- | --- | --- |
| `### On create` | a page of this type is being made | what a new page needs beyond its fields and headings - a companion page, a field to fill from the input |
| `### On update` | anything is written to a page of this type | where each kind of content goes, how it is divided, what is a section of its own |
| `### On link` | **another** page links to or draws on a page of this type | what that other page must carry itself rather than point here for |

`On link` is the one that is easy to miss and the reason the split exists. The writer of a page of some other type would never think to read this type's rules, so a rule about how *others* cite it - "write the fact on the subject's page, never 'see the source'" - has nowhere else to live where it will be read at the moment it applies.

Every subsection is optional, and so is the whole section: a type with nothing particular about writing it has none, and an empty heading is noise. The rules sit on the declaration because it is the one place every writer already reads. Capture reads it before writing (`capture.md` step 6), promotion before moving material onto a page; a skill that restates a type's rules has made a second copy, and the two drift.

**A declaration may say its type is a ledger**, with `ledger: periodic` or `ledger: span` (`ledger.md` has the two kinds), and where in an entry capture writes:

```yaml
ledger: periodic
sections:
  - <the log>
  - <true only of this occasion>
log_to: <the log>
occasion_only: <true only of this occasion>
```

That is how capture finds the ledger without being told, and how the host's word for an occasion - a day, a sitting, a sprint - reaches the generic layer: it is the type's name, declared once. No host document has to explain that its occasions are ledger entries, because the declaration says so. A ledger's `sections:` leave out `Known` and `My reading`, since an entry is a log of an occasion, not a page about a thing.

**A declaration says which of its fields are edges**, in `links:` - a mapping from a field to the type its values link to, or `any`:

```yaml
optional:
  - author
  - found_in
links:
  author: <a type>
  found_in: any
```

A field in `links:` is a **typed edge** (`graph.md`): every value is a quoted wikilink, and the check reports one that is plain text, that does not resolve, or that lands on a page of another type. A field not in `links:` is a property, whatever it happens to hold. `links:` lists fields that are also in `required:` or `optional:`; it says what kind of value a field holds, not whether the field exists.

**A declaration may say its type is a relation**, with `relation: true` - a reified edge, one page per instance of a fact that binds three or more things or carries properties of its own (`graph.md` has when, and why). Its ends are its `links:` fields; its own properties are its other fields:

```yaml
relation: true
required:
  - type
  - <an end>
  - <another end>
links:
  <an end>: <a type>
  <another end>: <a ledger type>
sections:
  - Known
```

A relation page is a record of a fact, not a page about a thing, so it is exempt from carrying `My reading`, as a ledger entry is; `sections:` defaults to `Known` alone. The ends that make it what it is are **required**, because a relation missing an end is not that fact. Its `## Writing to it` says how its pages are named from their ends.

**A declaration may say its type is an aspect**, with `aspect: true` - a quality named across many types, whose occurrences are filed on their own subjects and link it inline (`graph.md`). It tells capture the direction: a page of this type is an **index term** in the facts that name it, so it gets a link from each, never a bullet. Its own pages keep `Known` and `My reading`, for what is about the aspect itself.

**A declaration may say its type is owned**, with `parents:` - the types a page of it may belong to (`graph.md`, "Ownership"). A type with no `parents:` is top-level, as every type is unless it says so; one with them is always owned. Listing the type itself lets it nest to any depth.

```yaml
declares: <a session type>
folder: <Sessions>
parents: [<an owning type>]
identity: date
name: "{date} - <Session> - {name}"
```

### Names

**A type names its pages by a pattern**, in `name:`, from **variables**. Each type sets one, its **identity**, in `identity:` - `name` unless it says otherwise - and everything below a page in its ownership reads the same value: inside one person's folder `{name}` is that person's name everywhere, and inside one session's `{date}` is that session's date. Where a type owns itself and so sets its variable again, the nearest one wins. Without `name:` the pattern is the identity alone, which is how every page was named before.

- **An owned page's name says whose it is** by using the variables above it: `{date} - <Session> - {name}`, not a pointer to its parent. Every variable on the way down makes the name unique across the vault, so a plain `[[link]]` still lands; leaving one out names pages uniquely only among their siblings, and the type check says so.
- **An entity's folder is named by its identity value**, its own page by its pattern - so a person's page can be `<Name> - Bio` inside a folder called `<Name>`, at the cost that every link to it says `[[<Name> - Bio|<Name>]]`, since an alias is not a redirect (`obsidian.md`).
- **`identity: none`** is a type one per owner: its pages have no name of their own, only the variables above them - `{name} - Bio`, `{name} - Prep`. It is always owned.
- `notebook.py new <type> <identity value> --owner <owner>` makes an owned page from all this; the owner is named by its filename or its identity.

**A section may be filled by owned pages**: written `- "<heading>: <owned type>"` in the owner's `sections:` - quoted, or YAML reads it as a mapping - it is created holding an embedded view of the pages of that type the page owns - `parent == this` - instead of being written in by hand. `notebook.py` makes the view, `Views/<folder>.base`, if there is none. This is also where a section promoted to pages of its own ends up (`promotion.md`).

### Buckets

**A type folder may be split into bucket folders, derived from each page's name or a date field** - a ledger by year, or by year and month; numbered sections by their first number - with `buckets:`, one layer per level of folders:

```yaml
buckets:
  - '^(\d{4})'          # 2026/      a regex, matched against the name
  - '{date:MM MMM}'     # 2026/01 Jan/   a date field, with a format
```

- **A regex layer is matched against the page's filename**; its first capture group names the folder, or the whole match where it has none.
- **A field layer, `{<field>:<format>}`, formats a date field** - an ISO date, or the date part of a datetime - as Obsidian's daily notes do: `YYYY`, `YY`, `MMMM` (January), `MMM` (Jan), `MM` (01), `M`, `DD`, `D`, and `[literal text]`. The type check rejects a format it cannot read, as it does a bad regex.
- **Layers apply in order and stop at the first that does not apply** - a name its regex does not match, a field missing or not a date - so the page stays where the last layer left it: legal, and the type check lists it. The two kinds mix freely.
- **Bucket by the name when it already carries the key in an order that sorts; by a field when it does not.** A name whose month is a word sorts its month folders alphabetically, and no regex makes `01 Jan` out of `Jan`. **Never change names to suit folders**: a name is fixed at creation (`ledger.md` law 1), and folders are the convenience.
- **A bucket is a browsing convenience only. The name is the page's whole identity, and never shortens**: `2026/01/2026-01-01`, not `2026/01/01` - as a node it is the full date, a bare link to it stays unique, and changing the buckets later moves pages rather than renaming them.
- **New pages go straight to their bucket**, placed by the fields they are created with, and buckets sit between a type folder and its pages wherever that folder is, an owner's included (`graph.md`, "Ownership").
- **Add, change or remove `buckets:` at any time, then run `notebook.py tree`**: every page moves to where its name and fields now put it - so correcting a date moves its page - an entity that owns pages moving as a unit, and emptied buckets are removed. A move changes no name and no word, so every link still lands - and a closed ledger entry may move (`ledger.md`, "Maintenance is not rewriting").
- **It is the declare skill's, like any change to a declaration**: say what will move and confirm, then edit `buckets:` and run `tree`, and commit the declaration and the moves together - the moves follow from the declaration, and git shows them as pure renames. A page open in Obsidian with unsaved edits can be saved back to its old place, which `tree` warns of when the app is running.

**A ledger's `prepared:` lists the sections a projection writes** into an entry before it opens (`ledger.md`, `projection.md`).

**A declaration may pin its colour in the graph view**, with `graph_color: "#rrggbb"`. The graph's colour groups are derived from the declarations (`graph.md`, "Seeing it"); a pinned colour is what keeps a type's colour stable and distinct, so pin it when the type is declared.

**A declaration may say its pages are generated**, with `generated: true` - written by a projection and rebuilt whole - a hand edit is lost at the next build - and never by capture (`contract.md` law 8). A generated type is never material for another projection (`projection.md`), and it is exempt from the `Known` / `My reading` layout, since a projection's output declares its own.

**Some fields belong to every type, and no declaration lists them.** `aliases:`, `source:`, `ambiguous_names:`, `common_names:` and `tags:` are the contract's - provenance, the reference layer and roles (`graph.md`) apply to anything that can be named. A declaration lists only what is *particular* to its type; re-listing the universal ones on every type page is a second copy of the contract that nothing compares, and the schema check permits them without being told.

A **group** field is different: which set a thing belongs to is particular to its type, so it is declared where it applies.

**A field holds a standing fact.** Frontmatter reads as settled, so a property that varies by occasion cannot be a field without stating something false the next time it changes. Where a thing is found, if that moves between occasions, is the clear case: as a field it asserts a permanent location; as **dated prose** - "found in <place> on <date>" - it stays true forever. That is `ledger.md`'s law that a value true only then belongs to the ledger, applied to schema design. So before declaring a field, ask whether its value can change between occasions; if it can, it is prose.

**Required means something breaks without it.** Not "would be nice": a field is required when a view filters on it or a law depends on it. Anything else is optional, however often it appears - which keeps the requirement list honest and short, and keeps a check from inventing defects out of fields that simply do not apply.

**The type pages are plain markdown**, so a skill reads them with no application running. The view is a convenience over them, not the source.

**Exclude the folder from the content audit.** The type system is machinery, and "does this page stand on its own" is the wrong question for it - the same reason the ledger is excluded.

## The blind spot: optional is indistinguishable from unpopulated

`required:` is checkable - a view filters on it, so its absence is a defect. **`optional:` is not**, and that is where a type system quietly stops describing reality. A field listed as optional covers two different states with no way to tell them apart:

- **does not apply** - a picture whose subject is genuinely unknown has no `depicts:`, correctly
- **nobody filled it in** - the field applies and the page predates the convention, or capture skipped it

In the notebook this grew from, measured on the day the registry was built: `depicts:` on 1 of 14 pictures, `date:` on **0 of 9** events, and the field a colour's reverse edge depends on present on **5 of 118** pages that name a colour. Each is permitted by the declaration and none is visible as a problem.

The consequence is worth stating because it is easy to miss: the last of those means you can navigate from the aggregate page to everything it collects, and **not back**. The edge exists in one direction only, and the glossary suppresses the prose link partly on the grounds that the frontmatter carries it.

**The mitigation is prose, not a sentinel.** Where an absence is worth knowing about, *state it* on the page - "no date is given for it anywhere in the notes" - rather than inventing a frontmatter value to mean "checked, nothing there". A stated absence is readable, survives a schema change, and is already how a narrative projection is told to report a gap: say *"no year is given"* directly rather than referring to the notes.

That does not close the blind spot - a check still cannot tell the two states apart mechanically - but it closes it for the cases anyone cared about, which is the part that matters. The five eras in this lineage have no dates and now say so, including the user's own hedge that it may change.

So a check can report **fill rates** and must not report them as defects - that is `contract.md` law 7's "a browse, not a defect list", applied to schema. Deciding which absences are real is domain judgment, and the useful output is the rate plus the question, not a count to drive to zero.

## Which of the six a pattern is

A declaration is one of four shapes - an entity type, an aspect (`aspect: true`), a relation type (`relation: true`), or a ledger - and a field on any of them is a property, an edge (`links:`) or a group. Which of those a pattern becomes, and the tag that is the remaining possibility, is decided at the promotion gate by `graph.md`'s six tests, not here.

## What it does not fix

**Classification judgment.** Where a thing and the problem it poses share a name, the registry says both types exist and cannot say which one a sentence means. That stays a judgment, and `capture.md` says to ask when guessing wrong would put something untrue on a page.
