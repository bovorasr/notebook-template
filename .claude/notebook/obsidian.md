# Obsidian: the platform

Generic. The platform is a dependency, not a variable - this file names its constraints rather than abstracting them. A host supplies only its own scripts. **The vault is the repository's root, and a notebook may be checked out in many places at once**, so no path to it is written down anywhere: a script derives it from its own location, and the vault's name - the `<vault>` below - is that folder's name, read where the command runs.

## Filenames are a Sync constraint, not a preference

**Filenames may not contain** `" * ? < > : | \ / [ ] # ^`, and may not end in a period or a space. macOS and git accept some of these; **Obsidian Sync rejects them and Windows cannot store them.**

So a title needing one of those characters keeps it in the `# H1` and gets a sanitized filename. **The H1 is allowed to differ from the filename for exactly this reason** - a page whose title contains a colon keeps the colon in its heading and takes a sanitized filename.

**The same characters break `[[wikilinks]]`, and a slash is the worst of them**, because Obsidian reads `[[A/b]]` as a folder path: it looks like a working link while pointing at nothing. Link to the page's real filename and let `aliases:` carry its other names.

## `aliases:` is not a redirect

Verified against the app on 2026-10-21: a bare `[[Alias]]` does **not** resolve, even with that alias in the target's frontmatter. It lands in `unresolvedLinks` and `getFirstLinkpathDest` returns null.

What an alias buys is **findability** - the quick switcher and autocomplete reach the page by that name, and autocomplete then inserts the piped form. So link the real filename, write `[[Real name|the other name]]` when the other name should show, and treat `aliases:` as an index rather than a rewrite. **Add to it; never rewrite it**, because dropping one loses findability and nothing a link check can see.

`reference-layer.md` governs *which* names belong there.

## Renaming has to rewrite inbound links

Leaving the old name in `aliases:` does **not** keep old links alive, which follows directly from the rule above. `obsidian rename` rewrites them on disk; `git mv` plus a hand-written sweep does not, and doing it by hand is what produced, in the notebook this grew from, a clobbered-alias bug here.

**`rename` needs "Automatically update internal links" on** (Settings → Files and links). With it on, the command completes instantly and unattended. With it **off**, Obsidian raises a dialog and the command blocks until someone clicks it - so check `app.vault.getConfig('alwaysUpdateLinks')` before scripting a rename, and if it is false, say a dialog is coming rather than hanging silently.

## Moving a file keeps its links; renaming one does not

A link names a file, not a path, so **moving a file between folders leaves every link to it working** - which is what lets an entity become a folder when its first owned page arrives, and lets a page move to another owner, without any link changing (`graph.md`, "Ownership"). Only the *name* is what links say. So a rename goes through the app, and a move need not: `notebook.py rename` renames the pages through `obsidian rename` and the folders on disk, and refuses without the running app.

**Folders for browsing never shorten a name.** Obsidian's own daily notes do it this way - a date format like `YYYY/MM/YYYY-MM-DD` puts each note in year and month folders and still names it by its full date - and buckets follow the same rule (`registry.md`, "Buckets"): the folders are for browsing, the name stays the whole identity, and a bare link to it stays unique.

Two pages sharing a filename in different folders - every owner's `2026-09-09` - make a bare link ambiguous, and Obsidian then links by the shortest unique path. That is why owned pages are named from the variables above them (`registry.md`, "Names"): unique names keep links bare.

## The CLI is a call into the running app, not a file tool

Obsidian ships an official CLI, enabled in Settings → General. **Think of it as a server in front of the UI.** Every command asks the running app, so it answers about *app state*, which is not what is on disk. Three consequences, each of which has already caused a wrong answer:

- **It is eventually consistent with disk.** Edit a file with Write or python and the app needs a moment to reindex; meanwhile `obsidian read` may serve the *editor's buffer* for a file open in a tab, which is how a verified-good edit read back as missing. **Never confirm your own write through the CLI** - read the file. Conversely a dirty buffer can save over an external edit, so prefer writing through the CLI for files the user may have open.
- **It is stateful.** Commands fall back to the *active file* when `file=`/`path=` is omitted, and the active file is whatever was last focused. **Always pass `file=` or `path=` explicitly**; never rely on the active file.
- **It needs the app.** A command launches Obsidian if it is closed, so anything that must work headless belongs in a script.

A newly written file is subject to the first point: **a query returning nothing may mean "not indexed yet", so retry before believing it.**

## Ask Obsidian, not a parser

Where those caveats do not bite, the CLI is authoritative in a way that parsing files is not, because it applies Obsidian's own link resolution and reads the live metadata cache. A hand-rolled parser has been wrong about this more than once - `find -name '*?*'` treats `?` as a wildcard and matches everything, and a naive `\[\[(...)\]\]` regex mis-parses the escaped pipe in `[[Target\|label]]`.

| job | command |
| --- | --- |
| does a link resolve | `obsidian unresolved verbose counts` |
| the authoritative link-health answer | `obsidian eval code="JSON.stringify(app.metadataCache.unresolvedLinks)"` |
| what links here / from here | `obsidian backlinks file="X"` / `obsidian links file="X"` |
| pages nothing links to | `obsidian orphans` |
| search with surrounding lines | `obsidian search:context query="X"` |
| a page's frontmatter | `obsidian properties file="X"` |
| run a view | `obsidian base:query path="Views/X.base" format=md` |
| how long a page is | `obsidian wordcount path="X"` |
| rename, rewriting inbound links | `obsidian rename file="Old" name="New"` |
| arbitrary JS against the app | `obsidian eval code="1+1"` |

`file=` resolves by name, `path=` is exact; quote values with spaces. The `base:*` commands take `path=` only, so a bare `file="Tasks"` does not find `Views/Tasks.base`. `obsidian append` only appends to the end of a file, which is why appending under a named heading stays a script's job.

Prefer `search:context` over hand-rolled `find`/`grep`: shell globbing and regex escaping have produced confident wrong answers twice in the notebook this grew from.

## Showing the user a page

There are two ways to do it. **Which one a skill uses is the contracts' decision**: capture links (`capture.md` step 10), opening a ledger entry opens it (`ledger.md`, "Lifecycle"), and a narrative build opens its output (`projection.md`, "Running it"). This section covers how.

### Link it in the reply

**Any reply that names a page links it**, unprompted, so that looking at what was written is one click rather than a request. These rules are for replies read in a terminal running inside Obsidian (the Terminal community plugin). That plugin turns a vault path into a link that opens the page in the app, and it does so by two regexes. A host whose replies are read somewhere else says so in its contract, along with what makes a link there. Checked against the plugin's source on 2026-10-22:

- **Write the vault-relative path in parentheses, `.md` included**: `(Folder/Page name.md)`. Spaces are fine inside the parentheses. A bare path linkifies only if it has no spaces, and a period straight after it breaks the match.
- **The path must be exact.** It is looked up as a literal path, not resolved like a wikilink, and a path that does not exist renders silently as plain text. So get it right rather than guess.
- **A filename containing `)` cannot match**, because the parenthesized form stops at the first `)`. For those, use a percent-encoded URI on its own or at the end of a sentence: `obsidian://open?file=<name>`, where the name is the bare page name with no folder and no `.md`, encoded with `quote(name, safe='')`. This form resolves like a wikilink, so where two pages share a basename it may open the wrong one. The path form has no such problem.
- **Never write a markdown link.** `[label](obsidian://...)` renders verbatim in the terminal, brackets and all.
- **Only `.md` files outside dot folders can be links.** A `.base`, a script, or anything under `.claude/` or `.scripts/` is named as plain text and not dressed up as a link.

### Open it in the app

```bash
ps -axco comm= | grep -qx Obsidian && obsidian vault="<vault>" open path="<vault-relative path>"
```

- **Only when the app is already running.** A CLI call launches Obsidian if it is closed (above), and a page the user did not ask to see is no reason to start the app. So check the process list rather than the CLI. The check above is macOS's; `pgrep` can miss the app under a sandbox where `ps` does not.
- **Pass `vault=` and `path=` both**, since the CLI is stateful. `path=` takes a filename with parentheses as it is.
- **`vault=` finds a vault by its folder's name alone**, so a clone or a second checkout with the same name is answered by whichever the app has registered. The scripts check first - `app.vault.adapter.basePath` must be this folder - and treat the app as not running otherwise; a command typed by hand checks the same way: `obsidian vault="<vault>" eval code=app.vault.adapter.basePath`.
- **Opening moves the user's view**, so it is for a page they are about to work in or have just asked to have built. It never happens on the hot path, and it never comes from a background job.
- Verified 2026-10-23: the command prints `Opened: <path>`, and the page becomes the active markdown leaf.

### Open it for editing, at a heading

For a page the user is about to type into. `open` keeps whatever mode the pane was in, which may be reading view, so switch **that file's leaf** to its edit mode and then jump to the heading:

```bash
obsidian vault="<vault>" open path="<path>" && obsidian vault="<vault>" eval code="(async()=>{const leaf=app.workspace.getLeavesOfType('markdown').find(l=>l.view?.file?.path==='<path>');if(!leaf)return 'no leaf';const before=leaf.view.getMode();if(before!=='source')await leaf.view.setMode(leaf.view.editMode);leaf.view.setEphemeralState({subpath:'#<heading>'});return before})()"
```

- **`getMode()` is `preview` or `source`.** `source` means editing, whether Live Preview or source view. `setMode(view.editMode)` switches to editing and keeps the user's own choice between those two, so nothing needs checking first: the call is a no-op when the pane is already editing.
- **Find the leaf by `view.file.path`**, never the active view, which can be the Terminal pane.
- **Verify in a second call**: `getMode()` and the cursor line, read back from the same leaf. Verified 2026-10-24: a pane in `preview` came back `source`, Live Preview kept, the cursor on the heading's line.
