# Asking the template for a change

Generic. **A notebook's session never edits the template's repository**, even with a checkout of it at hand. It asks, the way a user asks support: an issue on the template's repository, and the template's side decides and makes the change, generically, for every notebook. The change then comes back with the update (`upstream.md`).

This is the other half of "Changing this folder" (`README.md`): the change arises in a notebook, mid-work, with that notebook's material in view, which is exactly when its names leak into a generic file. Asking instead of editing puts a review between the two.

## The usual way it starts

**With a refused commit.** A generic file was edited - a bug fixed where it showed up - and the guard refused the commit. That edit is the request: `upstream.py diff <file>` shows it, and it becomes the issue's "What would fix it", rewritten in the template's terms. Draft the issue from it first, then undo the edit, as the refusal says. Never get past the guard with `--no-verify`.

## When to ask

When work in a notebook shows that something generic does not fit:

- a bug in a generic script
- a difference the notebook needs that no outlet can hold - a gap the update reports (`upstream.md`, "The outlets")
- a law or a contract that does not hold for this domain, or says something wrong
- an improvement every notebook would want

Not for anything an outlet can hold - a setting, the notebook's own operation or check, a rule for one type. Put that in its outlet instead.

## How

1. **Write it in the template's terms.** Name roles, never this notebook's names (`README.md`, "Name roles, never the host's names"): *a ledger type*, *a generated type*, *the hub*, *a type whose pages are verbatim texts* - not the notebook's types, pages, people or places. Whoever reads the issue sees only what it says, so it must stand on its own.

   **An issue is public: anyone can read it, and it stays readable after an edit.** So it holds no private data of any kind, the domain's or otherwise:
   - the notebook's names, quotes from its notes, and anything its law keeps private
   - people's names, usernames and email addresses
   - paths on someone's machine, hostnames, and links to private repositories or internal systems
   - credentials, tokens and keys
   - anything from an employer or a client: project names, internal terms, data
   - screenshots or pasted output that carry any of the above

   Where a problem can only be shown with real data, say what kind of data it was and reproduce it with placeholders.
2. **Say what was needed and why**, under these headings:
   - **What happened** - the situation, abstractly: what was being done, what the generic layer did, what was expected instead
   - **Where** - the generic file, and the section or function
   - **Why no outlet fits** - or which outlet is missing
   - **What would fix it** - the change proposed, as it would read in the template
   - **How to see it** - a way to reproduce it in a scratch notebook made with setup, in placeholder names
3. **Show the user the draft, and open it when they agree.** The draft is exactly what will be published, so **ask them to check it for private data first** - the check that counts is this one, before the issue exists. The repository is the one `TEMPLATE` names in `.scripts/notebook_config.py`:

   ```bash
   gh issue create --repo <owner>/<repo> --label <bug|enhancement> --title "<the change, in the template's terms>" --body-file <draft>
   ```

4. **Meanwhile, leave the generic file alone** - the guard refuses a commit that changes it. Work around it in an outlet if one fits, or note the gap and carry on. When the template has the change, the update brings it.

## On the template's side

An issue from a notebook is read for **domain leakage first**: a name, a quote, anything private. Edit it out of the issue before anything else is done with it. **An edit does not erase it**: the issue's edit history keeps the earlier text, and copies may already exist, which is why the notebook checks before opening. Then the change is made as any other: generically, tested in the template, and the commit names the issue (`Closes #<n>`). The template's own `CLAUDE.md` has the rest.
