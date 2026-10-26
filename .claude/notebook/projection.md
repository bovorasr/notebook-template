# Projection: derived output

Generic. Three kinds, each owned by what writes it for as long as it may still rewrite it (`contract.md` law 8).

| kind | what it is | rebuilt |
| --- | --- | --- |
| **view** | a Bases `.base` file querying the frontmatter — "show me all X" | continuously, by Obsidian |
| **narrative** | a compiled document that reads as prose, overwritten by each build | on demand, by the host's compile skill |
| **entry** | sections of a ledger entry, written before the occasion opens - an interview's questions, a meeting's agenda | while the entry is prepared; never after it opens |

A `.base` file is hand-written and safe to edit; its output is not a file at all. A narrative document is rebuilt whole, so an edit to it is lost at the next build — the host contract should name the generated files explicitly, because this is the rule people break first. An entry is the projection's only until it opens.

## Where a projection writes: a page, or an entry

**A page, overwritten.** A type declared `generated: true`. With `parents:` (`registry.md`) there is one per owner - `identity: none`, named from the owner, `{name} - Prep` - made once with `notebook.py new <type> --owner <owner>` and rewritten whole by each build.

**An entry, prepared.** The output is a ledger entry - often of an ordinary ledger the user then writes in, like the sessions held with someone. Each build for an occasion `notebook.py prepare`s the entry the occasion's variables name and `notebook.py fill`s the sections the ledger declares `prepared:`. Building again before it opens rewrites the same entry; a new occasion gets a new entry; once opened, the entry is the ledger's - append-only, the prepared sections the user's to edit - and no build touches it again (`ledger.md`, "Three states"). So nothing is overwritten that anyone has started writing in, and a history of what was prepared for each occasion is kept by the ledger for free.

**What an entry projection reads is the notes as they stand**, like any projection, and "since the last occasion" is a question the notes answer without git:

- **the owner's previous entry** - the newest of its entries before this one; an entry's name carries its date (`registry.md`, "Names")
- **what came after it** - every ledger's entries dated after that one, which record what each later occasion found, and the pages whose `source:` cites those entries, which are where it was filed
- **what has no date** - material captured with no occasion open is filed without one, so "since" cannot place it. Say how much there is and where, rather than guessing which side of the date it falls

**What it may connect is this notebook's level of assistance** (`assistance.md`, "Projections"); at every level, a connection the notes do not make never reads as one they do.

## A projection reads the registry, never a list of its own

**What exists is the registry's to say.** A projection that enumerates its input types by hand will miss the next one promoted, and miss it silently: it keeps producing confident output from everything it *does* read. In the notebook this grew from, a narrative projection carried a hand-written list of folders; a type was promoted the next day, central to the whole domain, and the projection never read a single one of its fifteen pages. Nothing failed. The account was simply missing a subject.

So a projection **discovers its inputs from the registry**: every declared type, read as story material, except the machinery, which is read deliberately for what it is:

| | read by a projection as |
| --- | --- |
| **declared types** | the material, all of them - a type added tomorrow is included tomorrow |
| **a generated type** | never material. A declaration with `generated: true` holds pages a projection wrote, and a projection that builds on another compounds whatever that one got wrong |
| **the ledger** | *when* things were found, and what is new since the last build. Never its occasion-only working notes |
| **the hub** | material too: anything not yet typed lives there, and an observation waiting for a type is no less part of the account |
| **the registry itself** | never story material. It says what to read; it is not something to report on |

**Prefer a view to re-deriving one.** Where the question a projection needs answered is already a view - everything dated, in order; everything solved; every member of a group - read the view. The view is the query; reconstructing it by hand in the projection is a second copy of the same logic, and the two will drift.

**And the kind of projection is the host's, the inputs are not.** A narrative for one reader, a status board, a weekly digest: the host's compile skill says which kind it is, who reads it, and what shape it takes. It does not say what to read - that is this file and the registry. A compile skill that lists folders has re-acquired the defect above.

## What a projection looks for, and how it reads it

The host's compile skill says **what kind of page to make**. This section is what every such page needs from the notebook, whatever it is for.

**Before building:**

- **Sweep the links.** A projection reads the whole notebook anyway, and it is the one place a dangling link is *content*: something named and not yet filed, which usually belongs in whatever the page calls its open questions. A link dangling because of a typo or a stale rename is different - repair it in the notes first, rather than reporting it.
- **Read the current output.** It says what the last build already covers - and, where the output marks what is new, what has to roll off into the body - and what it already says well.

**Reading the material:**

| it meets | it does |
| --- | --- |
| `## Known` and `## My reading` | keeps them distinguishable in the output - see the epistemic rule below |
| a status field | decides which section a thing belongs in. Read it before reading bodies |
| a date and its precision | orders by it; an undated thing that *says* it is undated is reported as such |
| a verbatim text | **retells and links it, never copies it in** - it is one click away |
| the ledger | newest entries for what is new; older ones only for an occasion, when that occasion adds something; **never** its occasion-only working notes |
| a thing whose instance differs each occasion by a rule | treats it as **worked out once the rule is known**. The instance differing each time is not a loose end; only an unknown rule leaves it open |

**Building:**

- **Incremental is fine; patching is not.** Find what moved since the last build, re-derive the sections it touches, and leave the rest. That is still a build, because the changed sections come from the notes. What is forbidden is editing the output *as a document* - fixing a sentence in it rather than in the page it came from. Rebuild in full when the structure changes, or when most of the notebook has moved.

**Running it:**

- **Never two at once.** Both rewrite the same file, and the slower one overwrites the newer page with a staler read.
- **One per burst of capture, not one per entry.** The page only has to be right when someone reads it.
- **It is a snapshot.** It reads the notebook once, at the start; anything entered while it works lands in the next build, and the page must not claim to cover it.
- **If it ran in the background, re-read the output before touching it** - the file on disk is newer than anything the foreground remembers writing.
- **Show it when it is done.** A narrative build opens its output in the app if the app is running (`obsidian.md`, "Showing the user a page"), because someone asked for it in order to read it. A build that ran in the background does not open it. The user handed it off so they could carry on undisturbed, so the report is relayed with a link and the user opens it when they choose.

## The rule that drives entity granularity

**No view can enumerate bullets.** This is the practical test of whether something should be a page or a line:

> If *"show me all the X"* is a question you expect to ask, then each X is a page.

Where this came from: six documents of the same kind had accumulated as a run of bullets on one page — "a second letter…", "the next one…" — and the question could not be answered at all, because there was nothing to query. They became one page each with an index, and the index holds the standing facts about the kind rather than a bullet per instance.

So this is a promotion trigger in its own right, and it is a *question-shaped* one rather than a volume-shaped one. The signal is a question the notebook cannot answer, not a section getting long.

## One view per type

The default is one `.base` per entity type, filtering on `type:`. Add a view whenever a **cross-cutting** question appears — one that selects on a field rather than a type, or on a group reference rather than an identity. Those are the interesting ones, because a cross-cutting view is a hypothesis about the domain written as a query.

A view that silently returns nothing is worse than no view. Bases filter expressions fail quietly rather than erroring, so **test a new one with `obsidian base:query path="Views/X.base" view="Name" format=md`** and checking it returns the rows you expect, rather than trusting the syntax. Note also that Obsidian is eventually consistent with disk and may not have indexed a file written a moment ago, so a query returning nothing should be retried before it is believed.

### Bases, as tested

Verified against Obsidian 1.14.4 on 2026-10-22. The field names below are placeholders; the *expressions* are the ones that were verified. Filters sit at the top level for the whole base, or under a single view.

```yaml
filters:
  and:
    - type == "<type>"
    - file.hasProperty("<field>")
views:
  - type: table
    name: More than one value
    filters:
      and:
        - <field>.length > 1
    order: [file.name, <field>]
    sort:
      - property: file.name
        direction: ASC
```

What works on a list-valued property: `<field>.contains("<value>")`, `<field>.length > 1`, and the explicit `note.<field>.length > 1`. A column only appears if it is named in `order:`.

**A sort on a formula only applies when the formula is a column.** A view sorted by `formula.key` with `key` absent from `order:` comes back in filename order, with no error. Verified 2026-10-23. So a computed sort key - a date assembled from separate year, month and day fields, say - has to be shown; put it last.

What else held, in the same test: a partial date split across numeric fields sorts correctly through a key like `if(year, year, 99999) * 10000 + if(month, month, 0) * 100 + if(day, day, 0)`, which puts a year-only record first in its year and a record with no year after everything dated. Sorting on the fields directly does not: an empty field sorts last within its group. A weekday is a formula too, `date(<y-mm-dd string>).format("dddd")` - there is no `padStart`, so pad with `if(month < 10, "0", "")`. And **a base cannot show a page's body**: `file.content`, `file.body` and `file.text` do not exist, so anything a table must show is a property, and a link written inside a text property is not registered as a link.

**The trap that cost the most:** a newly written `.base` is not queryable until Obsidian has indexed it, and an unindexed or stale file answers *as though the filter matched nothing*. Four filter syntaxes looked broken this way and all four were correct. So a query returning no rows means "retry", not "wrong syntax" - and a filter is only disproved after the file has settled.

## Narrative projection

The compile step turns the entity layer into something read start to finish. It has rules the entity pages do not:

- **It has an audience and a shape**, which the host's compile skill defines — who reads it, what it includes and leaves out, how it orders.
- **It is re-derived, never patched.** Every section comes from the notes, so editing the output as a document makes it a third source of truth that drifts from the pages it summarizes. Re-deriving only the sections that changed is still a build - see "Building" above.
- **It carries the epistemic split through.** An inference must still read as an inference after compilation; a compile that flattens "My guess" into prose asserts things the notebook does not know.

  In prose that means **the verbs carry it.** "The clipping names him" is something a source said; "she reads the mark as a signature", "her guess is", "she suspects" are hers. Where a long stretch is the user's own reasoning, say so **once at its top** and let it run, rather than marking every sentence. And it runs both ways: never launder an inference into a fact, and never hand a source's fact to the user as though they worked it out.

- **What it connects is the level of assistance** (`assistance.md`, "Projections"), and at every level a connection the notes do not make never reads as one they do. A narrative is the easiest place to commit the direction test's error, because a good story wants its threads tied.
- **It never refers to the notebook from outside it.** No "the notes say", "the record shows", "according to the file". State the thing. And state a *gap* just as directly - "no year is given", "who they were is unknown", "where it was found went unrecorded" - because gaps are information and must survive compilation. Only the pointing at a file goes.
- **It is behind by design.** Capture does not update it, because capture is the hot path. The host decides how far behind is acceptable; the compile is a separate, deliberate act.

Offer a rebuild when the notebook has moved on substantially. Never run it unasked mid-capture, and do not nag.
