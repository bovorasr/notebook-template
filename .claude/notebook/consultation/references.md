# Consultation: References

What Claude may read in this notebook, chosen when it was set up and named in its `CLAUDE.md`. **The notes, what the user says or shows, and the documents the user names or puts in the notebook.** The host contract names the domain's particulars - which documents count, and where they are kept.

## What may be read

- **The notebook itself**, every page of it.
- **What the user says, and what they show** in the session.
- **Documents the user names or puts in the notebook**: a file in it, an attachment, a document or link they point at. Naming it is what brings it in.

**Never the web beyond what the user named, and never Claude's own memory of the domain** - not to answer a question, not to check a fact, not to fill a gap.

## Bringing in a source

The user brings a document in by naming it or adding it. Claude reads what was named, and may point out that a named document seems to cover a question - but does not go looking for new ones.

## Citing

**Every fact from a document is cited to it** - in the page's `source:` and on the bullet, with where in it, as closely as it can be given - and filed under `## Known`, as what that document says. A document read is never written as the user's own observation.

**A source read to answer a question is quoted in the reply, not filed.** It is filed - in `## Known`, cited as above - when the user asks for it to be noted, or gives it as something to record.

## What Claude already knows

**Claude's knowledge of the domain is not a source here.** Where it would answer something neither the notes nor a named document does, nothing answers it yet - say so. General knowledge outside the domain - how to read a date, what a word means - is fine.
