# The notebook contract

Generic. The host contract supplies the type table, the hub location, the domain's epistemic law, and the checks; see `README.md`.

Each law below was arrived at by getting it wrong first. Where a case is cited, it happened.

---

## 1. Capture never blocks on classification

An observation is recorded in the words it arrived in, whether or not anyone knows what kind of thing it is. **An observation that cannot be filed goes to the hub and that is the end of it** — do not ask which type it should be, do not invent a folder, do not treat the hub as a staging area that needs clearing.

The hub filling up with one kind of thing is **the signal arriving**, not a mess. In the vault this grew from, evidence of one kind accumulated in the hub for thirty-two days before becoming a type, and those thirty-two days were the system working rather than thirty-two days of debt.

What is not acceptable is losing the observation, or writing it somewhere that contradicts something already recorded.

## 2. Structure changes only on the user's word

The schema changes when the user says so, and on no other trigger. Claude may execute the migration flawlessly and may **not** decide when it happens. It is invoked, not inferred: **`/promote`**. See `promotion.md`. **Whether Claude may *suggest* it, and when, is this notebook's level of assistance** (`assistance.md`, "Structure") - a suggestion is never a trigger, at any level.

**Watch for guards that read as diligence.** This boundary is breached most often by something that looks like quality control: a rule phrased as a safeguard that moves a judgment from the user to Claude - *a type needs several instances before it is worth one*, say, which is a count Claude checks and so a count Claude can fail the user on, when a source can declare a pattern before any of it is filed. The test is not whether a rule sounds careful but **who it lets decide**: a precondition Claude evaluates is a veto, however gently it is worded. Questions that *resolve* an instruction are fine - "did you mean a new type, or this page's real type?" - because the user raised the structure and the answer is theirs either way.

This is an authority boundary, not a politeness. In a notebook whose categories are part of the discovery, **inventing a category is asserting a finding.** The value proposition is that promotion costs the user one sentence instead of an afternoon.

## 3. Structure carries epistemic weight

**A page name is an assertion, a folder is a claim about what kind of thing something is, a tag is the same claim as a folder, and frontmatter reads as settled.** All four read as established regardless of how tentative the thing they encode was.

So an unsettled thing stays in prose, where its hedges survive. Corollaries:

- **A guess promoted to structure stops looking like a guess.** Only an established fact goes in frontmatter; a suspected one stays a marked bullet.
- **Never create a page or a type that asserts a connection the user has not made.** Doing so hands them a structure they did not earn — which is worse if it turns out to be correct.
- **Do not group observations under a new concept because they look related to each other.** Two notes that rhyme stay two notes.
- **A link to a page that does not exist is fine**, because it only repeats a name already used. An invented category is not, because it adds one.
- **Deriving a *field* is not deriving a *fact*.** Structure may be read off accumulated material: if most instances of a kind record a due date, `due:` is a field. That asserts nothing new, because the material is the user's own evidence and naming its shape is description rather than inference. A **value** may never be derived the same way - the instances filed before the field existed need re-checking, not a plausible figure. Applied to names: the *key* `surnames:` is derivable from recorded full names; an *entry* in it, inferred from a marriage nobody wrote down, is not.

File by what the thing **is** in the user's words, not by what it might be **for**.

### The direction test

**Not** *"would this be a spoiler?"* - that question is direction-blind and answers yes for structure the user asked for. If they say *"the murderer is Sam, `/promote` killers"*, the result encodes an enormous spoiler and is entirely legal, because they are the one who knew it. Claude always builds the structure; that is the job. The question is never whether structure is being created, but **which way the knowledge travelled**:

> **Does this tell the user anything they have not already said or read?**

If **no**, Claude is only recording, and the structure may encode the biggest revelation in the domain. If **yes**, Claude is the source. **What Claude may do then - stay silent, say it, record it - is this notebook's level of assistance** (`assistance.md`). At every level, a conclusion Claude originates is never handed over as structure, and never reads as something the notes say.

The test applies where nothing is secret at all, because being the source is the problem rather than spoiling is. What it catches then is **premature closure**: a conclusion handed over as structure. In a research log, an unestablished causal link; in a diagnosis, two symptoms filed under one mechanism; in an investigation, a connection drawn between two people. The user stops looking, and structure does not read like the guess it is. And when Claude is the source, **Claude's error becomes the user's belief** - which is why the mechanisms below matter more than good intentions.

It bites hardest on **associations** - any field that is an edge between things rather than a property of one - because an edge is usually the discovery itself. The operative distinction is not relational versus descriptive:

- **An edge each instance states is safe to make a field.** Every document names its own author, so `author:` only writes down what is already written. So does provenance.
- **An edge visible only by comparing instances is a finding, and never a field Claude derives.** Whether Claude may point it out is the level of assistance. *"Four of six invoices record a due date"* licenses `due:`, because each of the four says so. *"Five of six documents from one place mention the same person"* licenses nothing at all - that is a pattern across the material, and noticing it is the user's.

Which is law 3's field-versus-value rule one level up: derive from what instances **say**, never from what they **collectively imply**.

**Making a pattern findable is not asserting what it means**, and this is the refinement that keeps a group field legal. A field recording family names derives from names each page already states, so creating it is description - and the resulting view, five people under one surname, makes a pattern *visible*. Announcing that the pattern is a family tree is a different act - an inference, which only the level of assistance can license, and then only marked as Claude's.

A near-miss worth keeping: when that field was built in the notebook this grew from, the user had already said the shared surnames were a real connection. Had they not, building it and presenting it as the family tree would have handed them the relationship - the same structure, spoiling, purely because they had not got there yet. So the test is not only about what Claude creates but about **when**: an index is safe, a reading of it is an inference, and the ordering of those two is the whole difference.

### Normalizing is asserting sameness

The second mechanism, and the one that makes Claude the source most easily.

Mapping two surface forms onto one entity **claims they denote the same thing**. Where a domain obfuscates - variant spellings, a codename, a partial name, two terms for what may or may not be one phenomenon - **the obfuscation may be the thing being worked out**, and removing it hands over the answer. A clear case is easy to spot; an obscure one is not, and the obscure ones are exactly where the discovery lives.

And **Claude may simply be wrong.** That is the stronger objection, because it does not depend on the domain having secrets at all:

- a false equivalence **resolves**, so it never appears in `unresolvedLinks` and no link check can see it - like the same-folder-first trap, it has to be prevented rather than detected
- it reads as structure rather than as the guess it is
- and it destroys the distinction it merged, which may have been the finding

So **equivalence is the user's to assert.** Claude may record that two forms occur together; it may not record that they are one thing. Rulings in the notebook this grew from were all this same call: two names that might be one thing stay two pages until the user merges them; a word that merely *contains* an entity's name is not that entity; and a given name shared by two people was deliberately left out of both their frontmatter, because which of them it refers to is an open question.

The legitimate case looks different, and the difference is visible: an equivalence is recordable when **the material states it** - a clipping that gives a person's pen name is a source saying the two names are one person, which is a fact to file rather than an inference to draw.

## 4. Reference must terminate

A graph of pure edges holds no content. Something has to be the node with the words in it - so **where a fact terminates is what decides whether it is written once or written twice**, and that is a property of the schema rather than a preference.

| the fact | where it lives | what each subject page does |
| --- | --- | --- |
| **has its own node** - a document, a verbatim text, or a reified fact type (a relation, `graph.md`) | at that node | states what the fact means *for that page*, and links the node - or, for a relation, **embeds a view** of the relations it is an end of, which shows the fact on the page without a second written copy |
| **has no node, one subject** | a bullet on that page | nothing further |
| **has no node, several subjects** | nowhere else, so in all of them | states it in full, framed for that page, naming the others |

**Count only subjects.** A page the fact merely names as an **index term** - an aspect (`graph.md`), such as the material something is made of - is not a subject of it: it gets the link, inline where the fact names it, and no copy. A fact about one thing that mentions an aspect has one home.

The third case is denormalized because it has no alternative: there is no node to point at, so a pointer would point at nothing. One observation about two things becomes two sentences, not one sentence copied - here a manual and the machine it describes are the two subjects:

```markdown
# <Source>.md, under "What it says"
- Chapter 3: the pump must be primed before first use (see [[<Subject>]]).

# <Subject>.md, under "Known"
- Must be primed before first use (see [[<Source>|<Source>, chapter 3]]).
```

**Claude may not reify a fact to escape the third case.** If a fact type existed - say the statements in a manual were themselves first class - then "the pump must be primed" would be a page with its own provenance, and both the manual and the pump would link it. That is a perfectly good design, and `graph.md` gives its shape: a **relation type**, one page per instance of the fact with a typed link to each end. But creating that type is a **promotion**, so it belongs to the user and to `/promote` (law 2). Until they make it, duplication is not a choice Claude gets to avoid by inventing a node.

**The invariant across all three cases: no page is a bare pointer.** Every page says something in its own words; the link is an attribution, or a route to more, and never a substitute for the content that page needs. That is what this law is really protecting, and it is why reifying a fact does not actually remove the obligation - a reified fact still leaves each subject page owing the fact. **An embedded view discharges it**: it puts the content on the page, not a route to it, so it is not a bare pointer. What a relation's end page still owes in its own words is only what the fact means *there* beyond its record (`graph.md`).

**Duplication is a cost, paid only where it is necessary.** Every written copy has to be kept in step by hand, and a copy that drifts breaks nothing a check can see. So a fact is written once wherever the schema gives it a node, and shown elsewhere by embedding; it is written on several pages only in the third case above, where there is nothing to embed.

Where this came from: the contract used to say one wikilink was enough, because Obsidian's backlinks pane gives the other direction. That was wrong - **a backlink gives you the link, not the content** - and it hollowed out a whole category. An audit found source pages listing who had consulted them and not a word of what they said.

**A page about a source shows the source.** The commonest way this law fails is not a missing bullet but a whole category hollowing out: pages about sources fill with *provenance* - where it was found, what it cost, who consulted it - while the sources' own content scatters onto the pages of the things they mention. Every fact is somewhere, and the source is unreadable from its own page.

So a type whose instances *say things* needs a section for what they say, kept separate from the facts about the object - that is the page-layout item in `README.md`'s interface, declared on the type's own page (`registry.md`). The test is whether someone opening the page can read what the source told them **without following a link.**

A **verbatim text** is the clearest case one: it lives at its own node, is embedded once with `![[...]]` and retold nowhere, while the pages it concerns still state what it says *for them*.

The cost of case three is a consistency burden, and it is real: a fact written on only one of its two pages is invisible to every check that looks at links, because nothing is broken. It is only safe with law 7 behind it.

### A dated record has two dates

Worth separating, because conflating them loses one of them silently. **A source has the date it was made; what it describes has the date it happened**, and they are usually not the same:

| | carries | example |
| --- | --- | --- |
| the **record** | its own date | a clipping published on the 11th |
| the **event** | the date it occurred | the thing it reports, four days earlier |

So a timeline needs **both as separate entries**, citing the same source. A row about the clipping is about the clipping; the event's row is about the event. Drop the second and the event has no date anywhere, while the notes look complete - the source is filed, the date is recorded, and the one that matters is missing.

This is also why the two live in different places: the record is a page of a source type and carries its publication date; the happening is a page of an event type and carries the date it happened. A type that confuses them produces pages dated by when someone wrote about them.

**And the event's date is derived from the source, so it is the user's to add.** "Four days ago" plus a dated clipping is arithmetic, but the result is a *value* (law 3), and in a domain where the timeline is load-bearing, a computed date entering it is exactly what the rule against deriving values exists to prevent.

## 5. Corrections keep what they corrected

A correction **replaces** the bullet it corrects, on every page that carried it, so a page never holds both readings at once. But the *overturned reading itself* is kept in the record, and the ledger is where it survives: an entity page states what is true, so a correction replaces the bullet there, while the ledger states what *happened* and is never corrected in place. See `ledger.md`.

In the vault this grew from, one puzzle was read wrongly twice before it was solved, and both wrong readings are still recorded, because the evidence that overturned them is the valuable part. A notebook that silently overwrites its mistakes loses the reasoning trail, which in a discovery domain is most of the content.

### A skill's copy of a domain rule is a cache, and the notes win

Where a skill encodes a rule *of the domain* - how to read a code, how to convert one scheme to another, what a marking means - it holds a copy of something the notes own. The user refines such rules as they learn, and they refine them **in the notes**.

So: **read the rule fresh from the notes before applying it, and where the notes and the skill disagree, the notes win** - saying so in the reply rather than silently following either. A skill that trusts its own copy is wrong the first time the user learns something, and wrong *invisibly*, because it keeps producing confident output.

Same shape as a stale type table or a reader-facing copy of a contract: a second copy of a fact that nothing compares. The difference is that a domain rule has to be restated in a skill to be usable at all, so the fix is not deduplication but **deference**.

## 6. Observation and inference never share a section

| section | holds | rule |
| --- | --- | --- |
| `## Known` | what the source actually said | one bullet per fact. Append; replace only to correct |
| `## My reading` | the user's own conclusions, each keeping its marker | never put one of these in `## Known`, or a fact here |

Whether a page has a section for **Claude's** inferences, and what it is called, is this notebook's level of assistance (`assistance.md`, "Markers"). Where it has none, Claude's inferences are not recorded at all.

**Never drop a marker to make a line read better.** A clean sentence that reads as a fact from the source is the single failure this separation exists to prevent, and it is produced by editing for style rather than by any decision to mislead.

**And an inference never enters a record of what a source literally said.** Not a verbatim cell in a table, not a full-text page, not an evidence column - and never a field a projection reads as settled, because a guess does not change a status. Those are recordings; an inference about them belongs beside them, not inside them.

Markers distinguish the kinds of inference — in this lineage, `My guess:` worded as a question and `My synthesis:` worded as a statement. **Keep every hedge, conditional and question mark**; the hedge is data about confidence, and flattening it is a silent upgrade of a guess to a finding. If the user says a claim is hedged by something, write the condition into the claim.

## 7. Checks report; they do not fix, and they do not accumulate allowlists

Three properties worth preserving exactly:

- **Diff-scope the lint.** Report what *stopped* being true since the last commit, not everything that is currently untrue. Deliberate exceptions then stay quiet forever with nobody maintaining an allowlist, because they are not new. This is the single most valuable trick here.
- **Two kinds of check, and only one may gate.** A **gate** reports a defect - a link that stopped resolving, a type in use that nothing declares, a malformed table row - and exits non-zero, so anything may refuse to proceed on it. A **browse** reports a state - thin pages, link candidates, fill rates - and **always exits zero**, because it describes the notebook rather than faulting it. A browse that exits non-zero tells every caller the notebook is broken when it is not, and the first thing to gate on it will refuse a healthy commit.
- **Counts are a browse, not a defect list.** A thin page is usually thin because little is known, which is information rather than a problem. Never drive such a number to zero — that means writing content the source never gave.

Ask Obsidian, not a file parser: link health is `app.metadataCache.unresolvedLinks` via `obsidian eval`, and a hand-rolled parser has been wrong about it more than once. A check may ask a question it cannot answer (*"this name is ambiguous between two entities — which?"*) and should, rather than guessing.

## 8. A projection owns what it writes only while it may still rewrite it

An overwriting projection always may, so **an edit to its output is lost at the next build** - change the inputs, which live elsewhere. A projection that prepares a ledger entry may rewrite it only until the entry opens; from then on the entry is the ledger's, append-only like any other, and its prepared sections are the user's to edit like the rest (`projection.md`, `ledger.md`). Query configuration *over* the data is not generated output and is safe to edit. Say in the host contract which pages a projection overwrites, by name.

---

## The page

```markdown
---
type: <type>
aliases:
  - <other name this page answers to>
source:
  - "[[Where it was seen]]"
---

# <Name>

## Known

- One fact per bullet, in the user's words, linking every other entity named.

## My reading

- <marker>: a conclusion, still marked.
```

- Add `> one line` under the title when a page needs a summary. Optional.
- A verbatim text gets its own page and is pulled in with `![[Title]]`, so it exists in exactly one place.

## Frontmatter

Always `type:`. Then, where they apply: `aliases:`, any group-reference field, `ambiguous_names:` and `common_names:` (all four in `reference-layer.md`), `source:`, `tags:` for a role (`graph.md`), and whatever the host's type table requires per type.

**A field its declaration lists in `links:` is an edge**, and holds wikilinks under the same rules as provenance below (`registry.md`). A field not listed there is a property, and a link inside it is an accident the check will not see.

**Provenance holds wikilinks, and a frontmatter wikilink is a real graph edge.** Obsidian indexes `[[...]]` in frontmatter as `frontmatterLinks`: a resolved one appears in `resolvedLinks`, in the backlinks pane and in `obsidian backlinks`, and a dangling one lands in `unresolvedLinks` exactly like one in the body - meaning *named, not yet filed*. Three rules, each of which has cost something:

- **Quote it**: `- "[[Target]]"`. Bare `- [[Target]]` is a nested sequence, not a link.
- **One entry per thing.** A compound string is two entries.
- **Single-quote a value containing double quotes.** An unescaped inner quote is invalid YAML, and **when the YAML fails the whole block is dropped** — `type:`, `aliases:` and provenance vanish together while the page still looks fine, and the entity silently leaves every view. Have a check ask Obsidian for the parsed frontmatter rather than parsing the file itself: a dropped block is invisible to a parser and obvious in the metadata cache.

## Linking

- Name another entity with a link, never a prose pointer.
- **Where two folders hold the same basename, link the full path.** Obsidian resolves a bare `[[Name]]` **same-folder-first**, so the identical text means different targets depending on which page it sits on. It lands in `resolvedLinks` either way, so `unresolvedLinks` never mentions it and no link check can see the mistake. Write `[[Folder/Name|Name]]`.
- A link to a nonexistent page means *named, not yet filed*. Never create a stub to silence one, which quietly asserts the thing exists, and never strip one to tidy up.
