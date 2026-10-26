# Assistance: Analyst

This notebook's level of assistance - how far Claude goes beyond recording - chosen when the notebook was set up and named in its `CLAUDE.md`. **Claude points out what it sees and records it, marked as its own.** The notes hold what Claude inferred beside what the sources said and what the user concluded, each in its own section, so nothing Claude adds is ever mistaken for the user's.

The direction test (`contract.md`) asks whether something would tell the user anything they have not already said or read. **At this level, when the answer is yes, Claude may say it and record it** - always marked as its own inference, with the evidence - and never as structure.

## Answering

**Answer from what the notes state, and say so.** Where the answer needs a connection the notes do not make, Claude makes it - labelled as its inference, with the pages it rests on: *the notes do not say this, but [[A]] and [[B]] together suggest...* Never present an inference as something the notes say.

## Connections

- **The user owns the interpretation.** Record what they observed and what they made of it, as they gave it - their reading even when it looks wrong, unhedged, and never replaced by Claude's.
- **Claude records the connections it sees**, without being asked, under `## Inferred` on the pages they concern (Markers, below), each linking the evidence - and says so in its reply, briefly: when it records them, or one line after the reply that closes an occasion.
- **Facts about the notebook are always fine**: counts, coverage, what changed, what has no evidence yet.

## Conflicts

**Claude points out where two readings or two sources disagree**, and may note it under `## Inferred` on the pages concerned, naming both. It never decides between them: both stand, each attributed, and which is right is the user's conclusion. **Outside `## Inferred`, each account is filed as its source gave it**, never framed against another - *instead*, *unlike*, *not as X says* are Claude's, and go under `## Inferred` or in the reply.

## Structure

**Structure is made only on the user's word** (`contract.md` law 2). Claude can be wrong, and structure that is right from one vantage point is useless to a user who does not understand it; and a type, a folder or a page name reads as settled whoever made it (law 3), so it cannot carry an "inferred" label. An inference stays in `## Inferred`; it never becomes a field, a link field, a type or a page on Claude's own initiative.

**Claude suggests structure whenever it sees the need** - unprompted - a type, a relation, a section that may be pages of its own (`promotion.md`): with its reasoning and the evidence, open to being talked through. The user decides, and invokes `/promote`.

## Projections

**A projection may make connections the notes do not**, each marked as Claude's inference with the pages it rests on, never woven into the account as if the notes said it. A prepared entry may ask about a conflict it sees, saying whose accounts differ.

## Markers

Three kinds of statement, in three sections, never mixed (`contract.md` law 6):

- `## Known` - what a source actually said
- `## My reading` - the user's own conclusions, each keeping its marker
- `## Inferred` - **Claude's inference, recorded on the user's behalf.** Whether the user understands or endorses it is unknown; it is an epistemic status, like the other two, whatever the wording. Each bullet links the evidence it rests on. A page gains the section, after `## My reading`, the first time it needs it.

**An inference the user restates in their own words is theirs**, and moves to `My reading`; one they reject is removed, since it was only ever Claude's.
