# Promotion: turning accumulated observations into a type

Generic. This is the move from layer 2 (the hub) to layer 3 (entities), and it is a skill: **`/promote`**.

**Promotion is performed on the user's word.** Running it is always their call (`contract.md` law 2): inventing a category is asserting a finding. **Whether, and when, Claude may suggest it is this notebook's level of assistance** (`assistance.md`, "Structure") - and a suggestion is never a trigger.

What accumulation looks like while it is working correctly: one kind of thing piling up in the hub for weeks, with no structure imposed on it. That is the pattern becoming visible.

## The invocation is the signal

**`/promote <what>` dissolves the recognition problem rather than solving it.** Typing it is unambiguous, so Claude never has to judge whether a remark was a trigger - which is the real reason this is a skill and not a rule about reading intent.

That leaves one residual case: a clear structural instruction given in prose, with no command. The test:

> **A signal is about the shape of the notes. An observation is about the domain.**

- *"Deadlines are everywhere in this project"* — a domain observation. Not a signal.
- *"There's a lot of deadline stuff piling up"* — still an observation, about volume. Not a signal.
- *"This deadline stuff needs to be its own thing"* — a signal, and clear enough to run `/promote` on their behalf.

**Claude noticing that the hub holds twenty bullets of one kind is never a signal.** That is Claude's inference, and acting on it is precisely what law 2 forbids.

**A hedged or deferred signal is not a trigger.** Three real cases from the session this was written in:

| what was said | what it was |
| --- | --- |
| "I think timelines are also something probably first class" | hedged, so **not** a trigger — and the user said so in the next breath: "let's not do a timeline refactor yet" |
| "For now here. Same idea: ideate then promote later" | an explicit deferral: the material stays in the hub *by instruction* |
| "Let's try to separate the abstraction, then bootstrap this system into it" | the trigger — phrased nothing like the canonical sentence |

**When the user has made a structural remark and it is unclear whether they mean now, ask.** That is not proposing: they raised the structure, and one short question resolves an instruction rather than originating one. Whether Claude may raise structure where the user has not mentioned it is the level of assistance.

So: run it on an explicit `/promote`, run it on an unambiguous prose instruction, ask when structure was raised but not clearly meant now, and otherwise run nothing - **a suggestion, at any level, is never a trigger.**

## Two operations, not one

Schema change decomposes cleanly, and conflating the halves is what made the earlier version of this document argue with itself:

| | about | needs material |
| --- | --- | --- |
| **declare** | the **type**: that it exists, and its shape | **no** |
| **promote** | **data**: fitting pages to a type already declared | yes, that is the point |

Everything about a type belongs to declare - its declaration, its view, the capture routing that reaches it. Everything about pages belongs to promote - creating them, moving or aggregating material, the index left behind, repointing links, flagging the ordinary words among the new names.

**Promote calls declare when the target type does not exist yet**, so one invocation still carries a thing from unclassified to typed. The split is about which judgments belong where, not about making the user run two commands.

What the decomposition buys, beyond tidiness:

- **A type with no instances is first class.** An engineer opening a notebook declares a product type on day one, before any product exists. That is declare, complete on its own, not a degenerate promotion.
- **Re-typing stops being a special case.** *"This page is actually a <type>"* is promote against an already-declared type. An earlier version of this file carved it out as "not promotion" and had to explain the exception; there is no exception, only promote without declare.
- **The reverse gear splits along the same seam.** Renaming, splitting, merging or retiring a *type* is declare. Moving the *pages* between types is promote. Which is why retiring comes last: the pages must be promoted elsewhere first.

**Both are gated.** Declare proposes a shape and confirms it; promote proposes what will move where and confirms that. Neither writes before the gate. See below. **When one `/promote` calls declare, the two gates are one stop**: the classification, the declaration and the migration go in front of the user together and are confirmed once.

## The gate

**Both operations propose and confirm, which is deliberately the opposite posture from capture.** Capture decides and reports, because it is the hot path. Schema change proposes and confirms, because a wrong shape is paid for over months. Nothing is written before the gate, so an abandoned invocation leaves no trace.

- **Declare's gate** puts the type's *declared half* in front of the user: the folder, `required:` and `optional:`, the `sections:` every page has, the `## Writing to it` rules where the type has any, and the sentence that tells this type from its neighbours. That is exactly the half of the registry that cannot be derived (`registry.md`), which is why there is a conversation here and nowhere else.
- **Promote's gate** puts the migration in front of them: which pages will exist, what moves and what stays, where the index goes.

**A type may arrive with no instances at all.** The hub is not the only on-ramp. Two paths lead here and both are legitimate:

| the type comes from | what the gate has to work with |
| --- | --- |
| **accumulated material** - a pattern that became visible | the material: read it, and propose the shape *from* it |
| **prior knowledge** - the user already knows this is a kind of thing | nothing to read, so **elicit** instead of propose |

The second is the normal case for a notebook that is *starting*, and it is not a lesser version of the first. Declaring a type before the first instance means the first instance arrives already having somewhere to go - and the shape can be revised later by the reverse gear, which exists precisely because a declaration made early may be wrong.

So **the gate adapts, and does not insist on material.** With evidence, read it and show the counts. Without, ask: what is one of these, what will its pages carry, what tells it from its neighbours. Do not demand examples before proceeding; the user may not have one yet and may still be right.

**Plurality is expected, not counted - and the user does the expecting.** An earlier version of this section said a type needs plural instances and told Claude to check. That was wrong twice over.

It looks at the wrong evidence: a source can *declare* a pattern before any of it is filed. *"Find the location of each animal and count their spots"* establishes that there are many animals with many spots, so **one instance plus a stated pattern is a perfectly good reason to promote** - and promoting then is better than promoting later, because the second instance arrives already having somewhere to go.

And it is not Claude's call. Whether something is the start of a pattern is a judgment about the domain, which is the user's by law 2. A precondition Claude tests is a precondition Claude can fail the user on, and **"are you sure there will be more?"** is second-guessing the signal rather than executing it.

So: **no count, no threshold, no test.** If they say it is a type, it is a type.

### First: what kind of thing is it?

`/promote <what>` names a pattern, and a pattern can become one of six things: an **entity type**, an **aspect**, a **relation type**, an **edge**, a **value**, or a **role** (`graph.md` has each, and the one test that decides it). **Telling which is the gate's first item**, before any field is proposed, because each leads to a different declaration and a different migration - and the user should not have to know the vocabulary to get the right one. That is what makes `/promote` a deep interface: one word in, and the classification behind it is the gate's job.

So read the material for its **shape**, apply the six tests, and put the outcome in front of the user with the evidence that decided it:

| what the gate shows | read from |
| --- | --- |
| how many things each observation binds | the observations themselves: two ends, or three and more |
| whether the relationship carries its own properties | a date, a place, a quantity, a condition stated with it |
| whether the things have identity | whether any page says something about one of them beyond the relationship it appears in |
| whether it cuts across types | the `type:` of the pages it appears on |
| whether the thing is the **subject** of the facts naming it, or an **index term** in them | what each fact is about: the thing, or something it describes - often a part or a state |
| whether an entity type is **top-level or owned** | whether a thing of this kind exists apart from what it is part of (`graph.md`, "Ownership") |

*"Each of these names a place, an occasion and a kind of thing - three ends, and the kind has no identity of its own. That is a relation with two links and a value field."* Then the user confirms, corrects or redirects, as with every other gate item.

This is executing the invocation, not proposing one: law 2 is unchanged, and the six tests are applied only once the user has invoked promotion. When the shape is genuinely ambiguous between two outcomes, say which two and ask - it is the user's call which reading of their notes is right.

### What the gate reads, and what it may propose

The proposals come from the material, which is the user's own evidence - so reading its shape back to them asserts nothing new. The limits are `contract.md` law 3 and the direction test:

| it reads | it proposes |
| --- | --- |
| a property **each instance states about itself** | a field, with the count as the evidence |
| a property on *most* instances vs one or two | a field vs leaving it prose - **except a quantity on a relation**, which is a field however rarely it appears, because a count over the relation is wrong without it (`graph.md`) |
| frontmatter already used on related pages | reusing an existing key rather than adding one |
| short forms, group names and ordinary words in the prose | which reference kinds apply (`reference-layer.md`) |
| a question the notes could not answer | the view, per `projection.md` |
| basenames that would collide across folders | the hazard, before it is created |
| observations that each bind **three or more** things, or a relationship stated with its own date, place or quantity | a **relation type** (`graph.md`): which ends are links, which are values, and the relationship's own fields |
| a link **each instance states** about one other thing | an **edge**: the field, and its entry in `links:` with the type it points to |
| a kind that recurs with nothing to tell two of them apart | a **value**: the field, and the set of values it holds, in the declaration's prose |
| a part played by pages of **several types** | a **role**: the tag and its nesting |
| a quality named across many types, mostly of parts and states, in facts about other things | an **aspect** (`graph.md`): `aspect: true`, what its page keeps, and its ordinary-word forms |

**Derive the field, never the value**, and **count only what instances say about themselves.** That instances co-mention a third thing is a finding, not a field: *"most of these record a date, want `date:`?"* is legal, *"these all mention the same person, want a field for that?"* is not.

**Required means something breaks without it** - a view filters on it, or a law depends on it. Everything else is optional however often it appears, which keeps a schema check from inventing defects out of fields that simply do not apply.

## The runbooks

Each runs its own gate first - propose, confirm, write nothing - then performs. **Commit before performing either**: both rewrite files across the notebook, and a clean point to return to is the whole recovery story for a migration that dies halfway.

**This holds even when a ledger entry is open with capture not yet committed**, though the host commits once per occasion. Commit what has been captured so far as a checkpoint - *"Checkpoint before promoting <what>"* - then perform; the entry's own commit follows when it closes, as usual. The occasion's history is then two commits instead of one, which costs a line in the log; a migration tangled into an occasion's notes costs the ability to undo either one alone. Say in the gate that the checkpoint will be made, rather than asking.

What each commit holds, in order:

1. **The checkpoint** holds the occasion's capture so far: every tracked page that changed, and every new page. A new file nothing links to - an attachment pasted and never embedded - is not capture; leave it out of the checkpoint and name it in the gate, so the user decides where it goes. Skip the checkpoint when there is nothing to commit.
2. **The migration** is one commit, made **after verification passes** - the schema check, the link check, the anchor pass - and only the files the promotion wrote: the declaration, the view, the new pages, any repointed links. Its message names what was promoted. A failed verification is fixed before the commit, never committed and fixed after.
3. **The occasion's own commit** follows when the entry closes, as usual, and holds whatever is captured after the migration.

Each is pushed the way the host pushes its other commits.

### declare

Four steps, all about the type.

1. **Write the declaration.** A page in the registry's folder stating its folder, `required:`, `optional:`, `sections:`, the `## Writing to it` rules and the sentence agreed at the gate. Give it `common_names:` for **its own name** - a type name is an ordinary word in the domain it describes, by construction (`registry.md`).
2. **Make the view.** One per type is the default (`projection.md`). Run it and check it returns what you expect; an unindexed view answers as though nothing matched, so an empty result means retry before it means wrong.
3. **Refresh the graph view**: rerun the derivation of its colour groups and filter (`graph.md`, "Seeing it"), so the new type shows. It is derived, so this is a command, not a decision.
4. **Route what is not a type, if anything.** Capture reads the new type from its declaration (`capture.md`, "Read the types first"), so no skill is edited for the type itself. Only routing to something that is *not* a type - a hub table that must gain a row, a cross-index - goes in the host contract's "Per-type routing"; most types need none.

Declaring an empty type stops here, and that is a complete piece of work.

### promote

Six steps, all about pages. The type must already be declared - if it is not, declare first.

1. **Make the folder**, and one page per thing, named as the user names them.
2. **Move the material, do not copy it** - *where it was pooled in one place.* Keep the wording exactly, and watch for text that only made sense in its old position: "recorded separately above", "(same section)", "as mentioned". Name what it meant, now that there is no "above".

   **Where the evidence was scattered across pages instead, nothing moves.** The new pages aggregate it and the original bullets stay, because a fact belongs on every page it concerns (`contract.md` law 4). Deleting them would strip the subject pages to make the new ones look tidy.
3. **Leave an index where the material was.** The old section keeps its explanatory preamble and becomes a list of links, so every existing cross-reference still lands somewhere. Rewrite the preamble if it described itself as holding the detail.
4. **Repoint inbound links.** Anything that linked to a *section* now links the page. Validate the anchors specifically: Obsidian's `unresolvedLinks` does **not** validate the anchor in `[[Page#Heading]]`, so it calls a broken one fine.
5. **Flag the names that are ordinary words.** Every occurrence of the new names in existing prose is now a link candidate, and some are too frequent to link without turning the notebook into noise (`reference-layer.md`).
6. **Verify**: the schema check, the `unresolvedLinks` diff, the `[[Page#Heading]]` anchor pass, any table lint if a table was touched, then the content audit on the new folder.

### The other five outcomes

The two runbooks above are for an **entity type**. The other outcomes of the first gate item use the same gate and the same commit-first rule, with these differences:

- **Relation.** Declare with `relation: true`, its ends in `links:` and as `required:`, its own properties as fields, and in `## Writing to it` how a page is named from its ends (`registry.md`). Then one page per instance of the fact, made from the scattered evidence, with its wording kept on the relation page. Make the view, with one view per end filtered on `this`. Then **the evidence moves**: on each end page, the bullets the relation pages now record are replaced by one embed of that end's view, so the relation page is the only written copy (`contract.md` law 4). A bullet that says more than the relation records keeps the extra as a sentence. Ledger entries are not touched: their lines record the occasion, not a copy (`ledger.md`).
- **Edge.** Add the field to the end type's `optional:` and `links:`. Where existing pages hold the edge as plain text, convert a value to a link only where the target page exists; list the rest for the user rather than creating pages to satisfy the check.
- **Value.** Declare the field on the types that carry it, and the set of values in the declaration's prose. Migrating means writing the field onto the pages that already state it, wording kept in the prose.
- **Aspect.** Declare with `aspect: true`. Where its pages already exist and hold a bullet per occurrence - the inverted shape, from a time before aspects had a name - **re-shaping it is the migration**: for each bullet, decide whether it is about the aspect itself (it stays) or about something the aspect describes. For the second, make sure the fact is on its subject's page, in that page's wording, with the aspect linked inline on the words that name it; then take the bullet off the aspect's page. **Read each one**: whether *brass* in a sentence means the material is a judgement no search can make. Ledger entries are not touched.
- **Role.** Add the tag to the pages that play the part, nesting as agreed. No declaration changes, since `tags:` is universal; the hub or the host contract says what the tag means. A graph view group colouring it is optional, and the user's to make.

### A section that may be pages of its own

A page's section can hold things that act like pages already - a room's section with a block per object in it, which other pages want to link to apart from the room. **Promotion never acts on it unasked.** When `/promote` is reading an entity - promoting its type, re-shaping it, or asked about it directly - it runs `notebook.py clues <page>` and puts any section that passes the test in front of the user, with the evidence. When else Claude may raise it is the level of assistance (`assistance.md`, "Structure").

**The test is the entity test** (`graph.md`): would another page link to part of this section and say things about it? **The clues** are only what the notes already say:

- **links into the section** - `[[<page>#<its heading>]]` from another page means that page is talking about the part, not the whole. The strongest clue.
- **links to the page that mean a part of it** - "the lamp in [[Room]]" links the room and is about the lamp. Weaker: it takes reading the sentence, so report it, never assume it.
- **links only that section makes** - a neighbourhood of its own in the graph
- **the same shape across pages of the type** - every room with headings of its own inside the same section
- **headings of its own inside it** - a run of facts about one thing at a time

**What promotion does with it is only a move.** It reports the evidence and lets the user decide; it never adds a link the notes do not make, and never connects what they leave apart (`contract.md`, the direction test). If the user agrees:

1. **Part or thing?** A part - with no existence apart from the page - becomes an **owned** type, `parents:` the page's type (`graph.md`, "Ownership"). A thing in its own right that the page holds for now - an object that can move to another room - becomes a **top-level** type, and the section keeps what was true then as dated prose. Declare it either way, with its name pattern.
2. **For each page that has the section**, make one page per block with `notebook.py new <type> <name> --owner <page>` and move the block's text onto it, wording kept. The page becomes a folder when its first owned page arrives; its links still land.
3. **The section becomes a view**: its body is replaced by the embed of the owned pages, and the owner's declaration says so - `- <heading>: <type>` in its `sections:` (`registry.md`).
4. **Links into the section are re-pointed** to the new pages, with their words kept as the alias - maintenance, which a closed ledger entry allows too (`ledger.md`, "Maintenance is not rewriting"). No link is added anywhere.

The reverse gear folds the pages back into the section, the same way round.

**Two steps these lists used to have and no longer need.** Updating a type table in several documents: the declaration *is* the table, and a reader-facing copy is the bug. Adding the folder to the content audit: it derives its categories from the folders holding typed pages, so a new type is audited the moment it exists.

## Why the registry exists, and the test that got it wrong

Kept because the reasoning was instructive about measuring the wrong thing.

This section once set a falsifiable test: *a correct registry shrinks this runbook from nine steps to about three.* The test did its job, and the answer was **no** - three of the four steps it was meant to collapse were fixed without a registry, each by the same move, **put the fact on the thing it describes**:

| the step | was | now |
| --- | --- | --- |
| the type table | several documents to edit | the declaration *is* the table |
| words too common to link | a list inside the checker | `common_names:` on the entity |
| the audit's categories | a list inside the checker | derived from the folders holding typed pages |

So by that measure a registry was barely worth building - and the measure was wrong. **The value of a registry is not ceremony saved during promotion; it is that capture can interpret input in the context of the types.** Given that the types are known, a sentence naming one of them resolves at write time, with no pattern matching and no glossary - including where the name is also an ordinary word, which is the case a retroactive linker cannot do at all. Which is also what makes the one remaining hand-edit - the capture skill's routing - the one that matters, rather than a leftover.

The general lesson survives either way: a registry is a place to put facts that have no home, and most facts turn out to have one. Check which you are holding before building somewhere to put it.

## Re-shaping: the reverse gear

A type can be wrong - too broad, misnamed, or two unlike things sharing a coat. There was no procedure for this, which is why a type covering two unlike pages can sit undisturbed indefinitely.

It is the same migration with the same hazards, so it follows the same gate: **propose, confirm, then perform.** What changes is the first move:

| | the move |
| --- | --- |
| **rename** | rename the declaration and every page's `type:`. The declaration's own name is a filename, so it rewrites inbound links like any rename |
| **split** | agree the two new types at the gate, declare both, re-type each page, and **retire the old declaration last** |
| **merge** | declare the survivor, re-type the absorbed pages, retire the absorbed declaration |
| **retire** | re-type or re-file every page **first**. A declaration with no pages is the schema check's signal, not a tidy end state |

**Retire last, always.** Removing the declaration while pages still claim the type leaves every one of them undeclared, which the check reports as a fault in the pages rather than in the schema - the error points at the wrong place.

**A re-shaping is not a correction to hide.** The old reading of what a type was is part of how the notebook came to understand its domain, same as `contract.md` law 5: say what it used to be and why it changed, on the declaration that survives.

## What promotion must not do

- **Do not promote to clear the hub.** The hub is not a backlog.
- **Do not promote part of a pattern.** If the signal names one concept, move that concept, not the things nearby that look similar.
- **Do not improve the wording while moving it.** The point of moving material is that it survives the move. Rewriting is a separate act, and a later one.
- **Do not lose a wrong reading that was recorded.** Those were kept on purpose (`contract.md` law 5).
