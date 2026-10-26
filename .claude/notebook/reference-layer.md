# The reference layer

Generic. The layer most likely to be missing from a notebook system, because it looks like it belongs to the entity layer and does not.

## The problem it solves

Entities have identity: one page per thing. **Names have a many-to-one mapping onto entities, and defining the entity does not define the vocabulary that reaches it.**

Where this came from: a person's page existed, was correct and detailed, and carried four aliases of the form `<short name> <surname>` — and still could not be found from the short name alone, because every alias recorded was another *full* name and nothing mapped the form the prose actually used. The cost was 87 unlinked mentions across 32 pages, and a fact sitting on one of its two pages for days while the other was never reached from it.

The lesson is general: **a notebook's prose uses short, informal, partial and shifting names, and the entity layer records canonical ones.** The gap between them is where facts go missing, and no amount of entity definition closes it.

## The five kinds

Every name must be sorted into exactly one.

| kind | goes | test |
| --- | --- | --- |
| **denotes one entity** | `aliases:` | does this word, alone, always mean this one thing? |
| **denotes a set** | a group field, e.g. `surnames:` | does it mean several things that are related *because* they share it? |
| **genuinely ambiguous** | `ambiguous_names:`, on every candidate | does it mean one of several, with no way to tell? |
| **time-varying** | nowhere — prose, with the transition recorded | did it mean one thing and now mean another? |
| **a common noun** | `common_names:`, on the entity | is the word ordinary vocabulary here, so an occurrence is **not** evidence of reference? |

### A group gets a field only when it cannot get a page

The test, and it keeps the group field rare: **if the group is itself an entity, it does not need one.** Members link to it, and backlinks are the view - a correspondent's letters, a book series, a project all work this way already, for free.

A group field is for a set that **cannot** be a page, because making it one would assert something the domain has not given. A shared family name is the case: the family is a pattern across recorded names, not a thing anyone was told about, so there is nothing to link to and membership has to live in frontmatter instead.

So a group field is the exception, not the template. Reach for a page first.

**An aspect is where this matters most** (`graph.md`): its names are ordinary words - *brass*, *iron* - and its occurrences are filed by an inline link and nothing else, so a missed link is a missed occurrence. Capture makes that call where the referent is known; a converter matching the word cannot, and must not try.

In `graph.md`'s terms a group field is a **value**: the set has no identity the notes have given it, so membership is written as a value on each member rather than as an edge to a node. The same test - could it be a page without asserting something? - decides both.

### A group reference is not a failed alias

A name resolving to five entities is **not** ambiguity to suppress. If they are related *because* they share the name, the collision is the finding — in this lineage, five people sharing a surname is the family tree, and the one entity carrying four surnames was the most informative record in the notebook.

So a group field resolves to the set, deliberately. And it is recorded even when it currently has one member, because a group with one member is a group that may gain a second.

### An alias is a findability claim, not an identity claim

`<short name>` on an entity's page means *this page answers to that word*. It does **not** assert that nothing else answers to it, and it must not quietly settle an open question about identity. In the case above, the entity's own `## My reading` still asked whether the short name referred to one person or two, while the alias made the page reachable — those coexist correctly.

### An alias needs a stated equivalence, not an apparent one

Operationally this is where `contract.md`'s *normalizing is asserting sameness* bites, because `aliases:` **is** the merge mechanism. The test is where the equivalence comes from:

| the equivalence is | example | may Claude record it |
| --- | --- | --- |
| **stated by a source** | a clipping gives a person's pen name | yes - it is a fact to file |
| **apparent from co-occurrence** | two names keep turning up together | no - ask |
| **apparent from similarity** | two spellings look like one word | no - ask, and expect to be wrong |

Derivation (below) stays legal under this because it decomposes names the material **already records in full** - it never merges two separately-recorded things into one.

### Only an established name goes in frontmatter

A *suspected* identity equation stays a marked bullet. This is law 3 of `contract.md` applied to names.

The sharp case: when a name is ambiguous between two entities **and which one is meant is itself an open question**, putting it in either page's frontmatter answers that question invisibly. Leave it out. The check's job is to ask.

## Deriving candidates mechanically

Short forms can be derived from recorded full names, and should be, because doing it by hand means not doing it. What this costs in practice, from one pass in the notebook this grew from over 61 entities producing 93 candidates:

- **Strip honorifics, initials, single letters, ordinals, roman numerals and parentheticals.** Without this the derivation produces `Prof` and `4th` as names.
- **Stop at a prepositional phrase.** `<Name> of <Place>` yields a place as a surname otherwise.
- **A title tells you *which part* of the name you have**, and this is the most useful signal available:
  - titles that precede a **family** name mean the given name is simply not known yet — record the group field, leave `aliases:` empty
  - titles that precede a **given** name mean the opposite
  - titles that do neither reliably should derive nothing at all
- **Some entries are not names.** A description (`<Someone>'s father`, `a general of the <Unit>`), or a collective of several individuals, decomposes into nonsense. Skip them explicitly, by name, with the reason recorded.
- **Expect to review a handful by hand.** In that pass, 70 derivations were right and about five were junk. Derive, then show the user the ones that are judgement calls rather than facts — unusual name orders, possible middle names, anything where the convention rather than the evidence decided it.

Derivation is additive. It never rewrites what is already recorded.

## What the check must do

Three classes, and only the first two are convertible:

| finding | action |
| --- | --- |
| an unlinked alias in prose | offer to link it to its entity |
| an unlinked group name in prose | **report only, never convert** - see below |
| an unlinked ambiguous name | **ask which entity is meant**; never pick |

It must handle possessives and inflections, because the possessive form is exactly what slips past — the original failure was the word `<name>'s`.

Report before converting. The first run over an established notebook will be long, and a bulk rewrite of prose is not a thing to do unreviewed.

### The converter is a migration, and its output is a metric

Worth stating because it is easy to file this among the standing checks and then run it forever. It has exactly **two** legitimate triggers:

1. **After a promotion.** A new type makes old prose linkable: the moment a kind of thing gets pages, every mention of one already written becomes a candidate. That backfill is real work and it is finite.
2. **As a measurement of capture.** And this is the part that matters: **capture knows the referent.** When the user says *"<the thing> is in <the place>"*, nothing has to be inferred - the entity was just named, so the link can be written then, exactly, with no pattern matching and no glossary involved.

So after a promotion's backfill is done, **a non-zero result is a defect report on the capture skill**, not a maintenance task. It means capture wrote prose where it should have written a link. Applying the links fixes the symptom; the number trending back up is the thing to investigate.

Which also explains why the noise problem belongs to the converter alone. Retroactive linking has to guess from a word; capture never does.

**A group name is reported, not linked**, and the first run of such a check showed why more sharply than the argument did. Two of the most frequent group names in that notebook were not being used as group names at all: one surname appeared on 35 pages, almost always as part of a *place* name that happens to share it, and another on 9 pages where it was nearly always a **colour**. Converting either would have linked a place or a colour to a family. A surname in prose is usually already inside a linked full name anyway, so the link adds nothing and risks a lot. Report it, and let the group's view answer the question.

**A name claimed by more than one page is refused, not guessed.** The same run found four basenames living in two folders on purpose - a thing and the problem it poses - where the converter had been silently linking whichever the directory walk reached first. Refusing is the only correct behaviour, and the host contract already says to write such a link's path by hand.

### `ambiguous_names:` - recorded symmetrically, resolving nothing

The problem this solves was found by building the check rather than by reasoning about it. A genuinely ambiguous name is **deliberately absent** from every page's frontmatter - that is law 3, keeping an open question open - so nothing in the notebook knows the name exists. A check scanning the alias vocabulary never looks for it, and the class returns zero candidates forever. *The rule that protects the question also hides it.*

In the notebook this grew from: one given name shared by two people, where which of them it refers to in a particular context is itself unsolved. It is in neither page's `aliases:`, correctly - and so **109 plain-text mentions across 41 pages were invisible to the check**, more than the name that prompted the whole exercise.

The fix is to record the *ambiguity* rather than the resolution, **on every candidate page**:

```yaml
# on each of the pages the name might mean
ambiguous_names:
  - <the name they share>
```

Why this is not the error it resembles:

- **It asserts the opposite claim.** An alias says *"this word means this page."* This says *"this word refers to me among others, and is not safe to resolve."* Each page can say that truthfully on its own, and saying it settles nothing.
- **It is symmetric**, so no page is privileged. An ambiguity recorded on one side only would be a resolution wearing a disguise.
- **It needs no new mechanism.** It is frontmatter, so the check already walks it, a view can query it, and there is no vault-level file to drift out of step with the pages.

**The validation rule:** a name in `ambiguous_names:` on **fewer than two** pages is not ambiguous - it is an alias that has not been promoted, or a leftover from a question since settled. The check should say so.

What the check then does with it: **ask.** It may report the mentions and name the candidates; it may never pick, and it may never convert. That is the whole point of the class.

### `common_names:` - the glossary, kept on the entities

The state that is easiest to leave in code, and should not be. Some entity names are also ordinary words in the domain: a place named for what it is, a material, a tool whose name is the noun for it. Their occurrences in prose are constant and mostly **not** references, so a checker that treats every one as a candidate produces noise forever.

That makes it a fact about the entity, so it belongs on the entity:

```yaml
# on the entity whose own name is an ordinary word
common_names:
  - <that name>
```

It is a **list of names, not a flag on the page**, because an entity can have one name that is ordinary and another that is not: an entity aliased with an abbreviation that is also a common word needs that form excluded while its full name stays matchable. Marking the page would lose that, and the same shape as `aliases:` and `ambiguous_names:` means the checker reads all three the same way.

Three things follow, and the third is the one that matters:

- **It replaces a hardcoded exclusion list.** Left in the checker, the glossary was 70 string literals in a script, in the notebook this grew from - invisible in the notebook, unqueryable, and edited by hand on every promotion. On the pages it is ordinary frontmatter the checker reads like everything else.
- **It is declared at creation**, when whoever makes the page can see at once that the word is ordinary. Classifying at entry is exact; classifying a corpus afterwards is guesswork.
- **It is what makes case-insensitive matching safe.** Without it, matching must be case-sensitive, and that is why a common-noun *object* goes unlinked: a person's name is always capitalised, so page name and prose form agree, while "the magnifying glass" mid-sentence never matches `Magnifying glass`. In the notebook this grew from that was **24 mentions invisible against 1 matched**. With the glossary, the names not in it can be matched case-insensitively and written `[[Page|as written]]`, and the listed ones are simply never candidates.

**A glossary entry is a judgment, and a wrong one is invisible.** This is the failure mode to design against, because it does not look like a failure: an entity wrongly listed is simply never linked, nothing breaks, no check fires, and its references stay prose forever.

The case that proved it, in the notebook this grew from: a motif with its own page was listed as common out of caution when symbols became a type. Seventeen mentions were suppressed - a necklace, a weathervane, a coat of arms - every one a genuine reference, for months, with the system reporting itself clean. In that domain the word essentially always meant the motif; the entry encoded a *fear* rather than an observation.

So the test for an entry is empirical, not cautious - but it has **two** clauses, and the second is easy to miss:

1. **Do occurrences of this word refer to the entity?** If they mostly do not, it belongs in the glossary.
2. **Would linking one add a path that does not already exist?** If the entity aggregates its own evidence, or an edge is carried by frontmatter, the link is redundant and the entry stands *even though clause 1 says the word is referential.*

Clause 2 is why an entity whose page already collects its own evidence can belong in the glossary even when the word does refer to it: clause 1 alone would licence linking every occurrence, and in the notebook this grew from that was hundreds of occurrences of one word against a page that already listed them. The link would add noise and no navigation. An **aspect** is the opposite case: its page keeps no list, so the inline link capture writes is the only path to an occurrence (`graph.md`). **A glossary entry can mean "not a reference" or "a reference you do not need to follow", and the two look identical from the checker's side.**

A checker can prompt the re-reading - a listed name that other pages keep linking *anyway* is one the glossary may be fighting - but it cannot decide either clause, so it reports.

The extreme case is worth seeing, because it is not an exception: **the type pages of the registry are entities whose names are, by construction, the generic words of the domain.** A page called `place` in a notebook about places. They declare `common_names:` like anything else - and that is the point. A folder rule in the checker would have been a special case standing in for the mechanism.

**Who the glossary is for: the converter, not capture.** Capture never needs it, because it knows the referent from the user's own sentence and reads the types (`registry.md`). The glossary exists because a retroactive linker has only a word to go on. That is worth keeping straight, or it looks like a weakness in the system when it is a property of one tool in it.

**Where the glossary does not belong: in the prose.** A per-occurrence marker - `^<name>` - would work mechanically and fails on the hot path: capture succeeds because the user writes naturally, and any syntax they must remember mid-activity is abandoned within a week. It would also be invisible to the application, so it buys nothing where the notes are actually read.

**And not in an external index either.** These are documents under continuous edit, so anything keyed to a position in them is stale on the next keystroke. Note why a wikilink escapes that: the edge is stored *inside the text, at the position*, so an edit moves it rather than invalidating it. That is the property that makes a side index unnecessary rather than merely awkward.

## It generalizes across types

This is the test of whether the abstraction is real rather than a feature of one type. It holds:

- punctuation and spelling variants of a place or document name are **aliases**
- a phrase like "the middle ones" is a **group**
- an object referred to by a bare noun throughout the prose is an **alias** that was never recorded

Outside this lineage the same five kinds appear as brand versus generic drug name, nickname versus legal name, module versus package name, a role like "the defendant" versus a person, and a job title that changes hands.

**Implement it for every type, not the first one.** A reference layer defined for one type is the same incompleteness as a check that covers one folder.
