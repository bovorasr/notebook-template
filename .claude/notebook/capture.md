# Capture: the generic contract for a capture skill

Generic. The host's capture skill - whatever the host calls it - reads this from its `SKILL.md` and adds only per-type routing and its own paths.

Capture takes arbitrary natural language and files it in two places: on the pages about what the input names, and on the open ledger entry. It is the hot path: the user is usually mid-activity and entering several in a row, so **capture is fast, append-only, and stops at the notes.** It never runs the projection.

**It is transparent afterwards, not confirming beforehand.** Capture uses judgement and then says what it did - it does not offer its reading back for approval. *"I think that's a sport, is that correct?"* is the wrong shape: it doubles the number of turns, and the user is mid-activity. The reply (step 10) is where anything uncertain surfaces, and the ambiguity table below says when a question is actually warranted - which is rarely.

## Steps

1. **Find out where you are writing.** Read which types are ledgers (`ledger:` in their declarations, `registry.md`) and which of their entries are open. A **periodic** ledger with nothing open stops capture: ask which occasion it is and open it with the host's open skill, then go on. Never invent one, and never write to a closed entry. A **span** ledger with nothing open is ordinary and stops nothing. An **owned** ledger's entries belong to their owner (`ledger.md`): an occasion with someone is open *for them*, and none open for them is ordinary too - but when the input belongs to such an occasion and none is open for whoever it was with, ask; never open one to have somewhere to put it. **The question is only about the entry**: file the rest now - the pages the input concerns, and any other entry open - so an unanswered question loses nothing. A **prepared** entry is not open: never write to it. This is the step that makes knowing the current occasion a question capture asks of the notes, every time, rather than something anyone has to remember.

2. **Name every thing the input touches**, not just the obvious one. One observation usually names several entities — expect a document, two people and a place in a sentence. Work them all out before writing, so nothing is filed against half the subjects; this is internal analysis in a single pass, not a step the user sees.

3. **Look for each one before creating it.** Names shorten, sources rename things, and a second page for something already filed is worse than no page. If it exists under another name, **add the alias** rather than creating a page.

4. **File it where it falls.** Give it a type when one obviously fits — what the thing *is*, not where it was found. When two types fit, pick the one whose required fields can actually be filled; if that does not decide, the type is unclear, and the ambiguity table below says where it goes.

   **An owned type's page has an owner, and the input has to say whose** (`graph.md`, "Ownership"): a page of a type with `parents:` is made under its owner, `notebook.py new <type> <name> --owner <owner>`, never at the top. If the input does not say whose it is, and nothing open does - the session the user is in is with someone - ask, or put it in the hub; never guess an owner, because an owner is a connection the notes would then assert. **An owner is a claim like any other**: where the accounts on file differ about it - which place a thing stood in, say - make the page under the nearest owner they all agree on, or in the hub if none, with each account in `Known`. When a later account disputes the owner a page was made under, say so in the reply, once, as a fact about the notes; moving it is the user's call. And a fact about a part goes on the part's page, not its owner's: the owner reaches it through the view of what it owns.

5. **When nothing fits, write it to the hub and move on.** Do not ask which type it should be, do not invent a folder. See `contract.md` law 1.

6. **Write it on every page it belongs to, framed for each.** Not one sentence copied — one sentence per page, each standing on its own and naming the other. This is the rule most easily got wrong and the one with the worst failure mode; `contract.md` law 4 has the case.

   - **Read the declaration of every type it touches before writing** (`registry.md`): `sections:` for which headings a page has, and `## Writing to it` for how to write them. `On create` for each page being made, `On update` for each page written to, and `On link` for each type that a written page links to or draws on - which is how a rule about citing a source reaches the page doing the citing. The type's rules are more particular than this procedure; where they say more, follow them.
   - **The open entry is one of those pages.** One line framed for the occasion - where it was and what it said - in the declaration's `log_to:` section (`ledger.md` law 3). With several open, it goes on each one the finding belongs to - the day's entry *and* the session with the person it came from. **Belongs to by what was said, not by what it implies**: an entry the finding was made in, with or for, or whose own wording it answers, is routing. That a finding *bears on* an entry only by an inference - it might explain something the entry is pursuing - is a connection, and whether Claude makes it is this notebook's level of assistance (`assistance.md`).
   - **The user's own guess, made during an occasion, is not something the occasion found.** It goes in `My reading` on the page it concerns, marked as theirs and linking the open entry - so it keeps its date - and is not logged in the entry's `log_to:` section, which would put it in someone else's mouth. Only an entry whose type declares a section for the user's own thoughts gets it there too.
   - **A section filled by owned pages is a view, not a place to write** (`registry.md`): never add a bullet under it. What would go there goes on the owned page it is about, and the view shows it.
   - **If the user says it is true only of this occasion**, it goes **only** on the entry, in its `occasion_only:` section, and on no entity page (`ledger.md` law 2). If they don't say, it is general. If it looks occasion-only but they didn't say, file it generally and say in the reply that it can move; don't ask first.
   - **If a page does not exist, create it from its type's declaration** (`registry.md`): every `required:` field set, from the declaration's `defaults:` where it gives one, the type's `sections:` in place, and its `On create` followed. A page created that way is valid by construction - the schema check confirms rather than catches. A required field with no default is one capture must fill from the input, or ask about.
   - **Sort each entity the input names into subject or index term** before writing to it. A **subject** is what the fact is about, and gets the fact on its page, framed for it. An **index term** only describes something in the fact - a material, a currency - and gets **an inline link where the input names it, and nothing on its page**. A page of a type declared `aspect: true` is always an index term, unless the fact is about the aspect itself (`graph.md`). So *"the handle is brass"* is one bullet, on the handle's page, with *brass* linked; the material's page is reached through its backlinks. **An index term with no page yet is linked anyway, and given none**: the dangling link means named, not yet filed (`contract.md`, "Linking"), and the page arrives with the first fact about the thing itself.
   - **A field the declaration lists in `links:` is an edge**, so its value is written as a quoted link - `"[[Target]]"` (`registry.md`) - even when the target has no page yet. A dangling link means *named, not yet filed* (`contract.md`, "Linking"), which is true; a plain value would say the field is not an edge at all. Never create a stub to make the link resolve.
   - **If a declared relation type fits the input** - it states an instance of that fact, every required end present - make the relation page from the declaration, a link to each end, named as its `On create` says, with the user's wording in its `Known` (`graph.md`). **Do not also write the fact as a bullet on the end pages**: each end shows it through the relation's embedded view, so a bullet would be a second copy to drift. If an end page does not embed that view yet, add the embed, once. Write the ledger line as usual, and add a sentence to an end page only for what the fact means there beyond its record. A relation missing an end is not filed as a relation; the bullets carry it, and the reply says which end was missing.
   - **If the input corrects something**, replace the bullet it corrects on **every** page that carried the old claim, so no page holds both readings. A correction is the user putting right **what was recorded** - a mishearing, a slip. **One source disagreeing with another is not one**: both accounts stand, each attributed, and which is right is the user's conclusion (`contract.md` law 5). A source correcting *itself* - telling it differently later - is a second account too, cited to when it was said. **A field holds one value**, so where accounts of it differ, `Known` holds each, attributed and dated, and the field keeps what it had - except where a source revises its own figure, when the field takes the revision and `Known` keeps both.
   - **Every bullet says where it came from.** Where the user names no source, it came from them on this occasion: cite the entry it was told on, keep whose account it is if they say (*Anne mentioned...*), and never supply an occasion they did not give.
   - **If the input adds a name or spelling** for something already filed, add it — never replace what is there.

7. **Keep the user's wording.** Fix an obvious typo only when they are clearly correcting one. Link every other entity the bullet names.

8. **A verbatim text gets its own page** and is embedded where it belongs, so it exists in exactly one place. Keep the text exactly: typos, line breaks, layout, and any bracketed aside the user added, left where they put it. If it has a layout, fence it so a rule of dashes does not become a markdown heading. Then embed it with `![[Title]]` on the page it belongs to.

9. **Verify only when the edit could have broken something.** A plain append cannot break an inbound link and needs no check. A **correction, a rename or a name change** rewrites a page's identity while other pages point at it, and that is where links rot — run the diff-scoped check then, and fix it immediately, while you still know what the link was meant to say.

10. **Reply briefly**: which pages were created or changed, **each as a link the user can click** (`obsidian.md`, "Showing the user a page"), and anything that had to be guessed. Two or three lines while they are working. The links are how the user checks what was written, if they want to, without asking.

    **Capture never opens a page.** It is the hot path and the user is entering several things in a row, so moving their view on every entry would be the opposite of help. Link the pages and leave the view where it is.

## Read the types first

The type system is data (`registry.md`), so **read it before classifying** rather than working from a remembered table. It is what lets input be interpreted *in the context of the types*: given that the types are known, a sentence naming one of them resolves here and now, with no pattern matching and no glossary - including where the name is also an ordinary word.

This is the difference between capture and a retroactive linker. **Capture knows the referent, because the user just named it.** A converter has only a word, which is why it needs a list of words that are ordinary - and why that list is the converter's problem, not a fact capture depends on.

## Routing is not asserting

`contract.md`'s constraints - the direction test, normalizing, law 3 - restrict **creating** structure. They do not restrict **using** it. Filing a statement against types and entities the user has already established is clerical work, and it is the job; nothing in them licenses refusing to file.

| act | licensed by |
| --- | --- |
| **routing** - which existing page and section this belongs to | the user already created the type |
| **asserting** - a new type, an equivalence, an edge the material does not state | nothing: it needs `/promote`, or a question |

So routing "the <thing> is <value>" onto the thing's page and into the field its declaration gives that value is not inference about the domain. It is the system working.

**A fact that binds three or more things, with no relation type declared for it, is filed as bullets** - one on each page it concerns, as step 6 says - and nothing else. Making it a relation page would be inventing a type (`graph.md`), which is promotion's. Once the user has declared one, filling it is routing like any other.

**A role tag is never added by capture.** A tag asserts membership exactly as a folder does (`contract.md` law 3), so it arrives only by promotion. Capture keeps an existing tag on a page it edits, and never adds one.

### When routing is ambiguous

*Is `Apple` a fruit or a surname?* Three cases, and only the middle one has to interrupt:

| the ambiguity | do this | why |
| --- | --- | --- |
| which **type** it is | write it to the hub in their words | free, and honest: the statement survives intact |
| which **existing entity** it refers to | **ask** - even when context makes one likelier, unless the input or the occasion it was said in settles it. Meanwhile it waits in the hub, in their words, naming no one, so an unanswered question loses nothing | guessing writes a *false statement* onto a page |
| which of two **equally valid** homes | pick one and say which in the reply | a true statement in a less useful place is cheap to move |

The asymmetry that sets the threshold: **a misfiled statement is recoverable as long as the wording survives; a misattributed one is not**, because it stops looking like a guess the moment it is on the page. So ask when guessing wrong would put something untrue on a page - not merely whenever there is doubt. Capture is the hot path, and a question mid-burst is expensive.

**Say what was guessed.** Naming it in the reply is cheaper than asking and keeps the correction available.

Routing is also the first thing the registry (layer 10) pays for: with the types described as data, capture can *read* which entities a statement touches and how they map, instead of having the routing written into the skill.

## The user's own conclusions

If the input is the user's guess, theory or conclusion rather than something a source told them, it goes under `## My reading` with its marker, never under `## Known`.

**Keep every hedge, conditional and question mark.** If they say a claim is hedged by a condition, write the condition into the claim. Flattening a hedge silently upgrades a guess to a finding, which is the same error as putting it in frontmatter.

## How far to help, and what to read

**The user owns the interpretation**, whatever else is chosen: record what they observed and what they made of it, as they gave it - their reading even when it looks wrong, unhedged, never replaced by a better one.

**How far Claude goes beyond that is this notebook's level of assistance, `assistance.md`**, and **what Claude may read to file anything is its consultation, `consultation.md`** - both chosen when the notebook was set up and named in `CLAUDE.md`. Read both before capturing: they settle what to do when a connection, a conflict or a gap shows itself while filing.

## Host extension points

A host adds, and only these:

- **per-type routing** — the extra steps for types the domain treats specially: a table that must gain a row, an index to update, a field to set
- **the ledger** - declared in the registry, not told to capture: a type with `ledger:` set, named for what an occasion is here, plus the skills that open and close one (`ledger.md`)
- **what counts as occasion-only** - the phrasings that mean it in this domain; where it goes is step 6
- **the domain's particulars** — beside its two choices (`assistance.md`, `consultation.md`): which sources are closed or preferred here, and what filing may never pre-empt

## If the input is unclear

If it is not clearly an observation, a correction or a conclusion, **ask one short question** instead of guessing.
