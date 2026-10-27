# The graph: what the notebook is, and the six things a pattern can become

Generic. The model under every other document here. Nothing in it names a domain.

## The paradigm: a labelled property graph

The notebook is a **labelled property graph** that happens to sit at rest as readable markdown. Every other document describes a part of it in its own terms; this is the mapping between them.

| graph | in the notebook |
| --- | --- |
| node | a page |
| primary label | `type:`, stored as the folder the page lives in (`registry.md`) |
| extra labels | tags. A node may carry several, and they nest |
| node properties | frontmatter. **Atomic values only**: a string, a number, a date, or a list of those |
| typed, directed edge | a wikilink inside a named property: `author: "[[Ann]]"` is an edge labelled `author` from this page to Ann |
| untyped edge | a wikilink in prose. It says only *mentions* |
| reverse traversal | backlinks, or a view filtering on `this` |
| unlabelled node | a hub bullet, or a page with no `type:` yet |

**Why a graph and not a database or a class hierarchy.** A relational schema is schema-first: a row cannot exist without its table. A class hierarchy is class-first: an instance is born with its class. A property graph allows an unlabelled node and an untyped edge, and lets labels arrive later. That is the notebook's founding premise - anything worth recording is not yet understood when it is recorded, which is *why* it is being recorded - so classification has to be deferrable:

- capture never blocks on classification (`contract.md` law 1): an unlabelled node is a legal node;
- `/promote` adds a label when the pattern is visible (`promotion.md`);
- the schema check compares declarations against what pages already carry, after the fact. It is **schema-on-read**: it reports, it never gates a write (`contract.md` law 7).

The relational and object readings are still useful, as views of one part: a folder of one type looks like a table, a declaration like a class. Neither is the model.

## Three axes, and which one is one level deep

| axis | mechanism | depth |
| --- | --- | --- |
| **classification** - what a thing is | folder and declaration | **one level, by design.** No folder inside a folder, so no subtypes. If a hierarchy of kinds is ever needed, a nested tag holds it and the folders stay flat |
| **composition by reference** - a has-a to something with identity | links | **unbounded.** A page links to a page that links to a page |
| **composition by value** - a has-a to something without identity | properties | **one level.** A value is atomic; Obsidian has no nested properties, so a value cannot contain a value |
| **ownership** - a part with no existence apart from what owns it | the path: an owner's folder holds what it owns, and a `parent:` link written from it | **unbounded.** An owned page can own pages, to any depth - see "Ownership" below |

So **depth is bought with pages and links**, never with nested values, and never with folders of *kinds*: what a page is stays one level. The one thing folders nest is **ownership** - which instance a part belongs to - and that is a hierarchy of things, not of kinds. A value that would need structure inside it becomes a node of its own, linked to its owner. That is first normal form, and it is the rule the next section applies.

## The six things a pattern can become

When a pattern becomes visible and the user promotes it, it becomes one of six things. Telling them apart is the first thing the promotion gate does (`promotion.md`), and each has one deciding test:

| the material is | it becomes | the deciding test |
| --- | --- | --- |
| things with identity, one page each | an **entity type** | would another page link to one of them and say things about it? |
| a fact binding **three or more** things, or a relationship carrying **properties of its own** | a **relation type** - a reified edge | count the ends; ask whether the relationship itself has a date, a place, a quantity, a condition |
| a relationship between **two** things, with nothing of its own | an **edge** - a declared link field on one end's type | does one end state it about itself? (`contract.md`'s direction test) |
| a **kind** with no identity - any one is as good as another | a **value** - a field holding one of a set of values | could two of them ever be told apart, other than by where or when they turned up? |
| a **part** things play, across types | a **role** - a nested tag | does it cut across folders, so that no one type could hold it? |
| a quality named **across many types, often of a part or a state**, with meaning of its own - while the facts naming it are about something else | an **aspect** - an entity type its occurrences link to inline, read through its backlinks | is it the *subject* of the facts that name it, or only an *index term* in them? |

The tests are about the **shape** of the material, never its meaning, so applying them asserts nothing the notes do not already show (`contract.md` law 3). They are applied only when the user has invoked promotion; noticing that material has one of these shapes is never a reason to raise it (law 2).

### Entity types

The existing case, and `registry.md` is its whole contract. An entity type is **top-level or owned** - its pages either stand alone or belong to a page of another type ("Ownership", below) - and which is a promotion's question too: does a thing of this kind exist apart from what it is part of?

### Relations: when an edge needs to be a node

A link carries no properties and joins exactly two pages. A fact that binds more than two things, or a relationship that has properties of its own, cannot be one link. The standard answer in a property graph is to **reify** it: the relationship becomes a node, with a typed edge to each of its ends.

> A neutral example: *Ann attended the review on the 14th, as chair.* Four things - a person, a meeting, an occasion, a role. As links on Ann's page it loses which meeting went with which date; as a property of the meeting it loses who. As one page, `Ann at the review (14th)`, with `attendee: "[[Ann]]"`, `meeting: "[[The review]]"`, `on: "[[<the entry for the 14th>]]"` and `as: chair`, every part stays bound to every other.

The rules for a relation:

- **One page per instance of the fact.** Not one per pair of ends with a list of the rest: that collapses an end into a value and loses the binding the page exists to keep.
- **One typed link per end that has identity**, in a field declared in `links:` (`registry.md`). An end with no identity is a value field instead - see below.
- **The occasion is usually an end.** Where the host has a ledger, the entry for that occasion is a node already; a relation that happened on an occasion links to it. **Name that field for the ledger type it links to** - `entry`, `session`, whatever the host's ledger is called - with the ledger type as its `links:` target, so every relation in a notebook names its occasion the same way. This is how a fact that varies between occasions gets structure without lying: `registry.md` says such a fact is dated prose and not a field, and a relation page tied to its occasion is the same dated statement as a node - true forever, because it says when.
- **The relationship's own properties live on the relation page**: the quantity, the condition, the role played.
- **A quantity is a field, never prose**, even if only one instance has one: a view that counts relations counts pages, so *"two of them"* written in a page's name or prose is counted as one. Declare it optional, with its absence meaning one - a view reads it as `if(<field>, <field>, 1)`.
- **No `source:` of its own is needed.** A relation's provenance is its ends - above all the occasion it links - so `source:` on a relation page would only repeat them. Add it when the fact came from somewhere its ends do not say, such as a document read on that occasion.
- **Each end shows it by an embedded view, not a sentence.** The relation's view has one view per end filtered to the page embedding it - `<end field> == this` - and each end page embeds it once, under the section it belongs in: `![[<the view>.base#<that view>]]`. Every relation naming the page appears there, derived, so **the relation page is the one written copy** and a correction is made once (`contract.md` law 4). An end whose value has pages of its own but is held as a value - a kind - can be shown the same way, with a filter matching the page's name against the field.
- **A sentence on an end page is only for what the fact means there beyond its record** - law 4's "what it means for that page" - never a restatement of the relation's fields.
- **The ledger entry keeps its line.** What was found on an occasion is the ledger's own record (`ledger.md`), not a copy of an entity fact, and a closed entry is never rewritten.
- **The cost, stated:** at rest, the end page's markdown holds an embed line rather than the fact. Anything reading the files still reaches it in one hop, because the relation page links the end in its frontmatter. One copy that cannot drift is worth that.
- **Named from its ends**, as the user would name it: the identity-bearing ends and the occasion, in a pattern the declaration states.
- **A relation page records what the notes state.** Frontmatter reads as settled (`contract.md` law 3), so a relationship the user only guesses at is not a relation page: it stays a guess, in `My reading` on the pages it concerns, until it is stated.
- **Reifying is a promotion.** Capture never invents a relation type to escape law 4's third case (`contract.md`); it fills one only once it is declared (`capture.md`).

### Edges

A two-ended relationship with no properties of its own is a field: `author:`, `found_in:`. Declaring it in `links:` is what makes it a **typed** edge - the check then knows the value must be a link, and to what. Without the declaration, a field holding a link and a field holding plain text are indistinguishable to every tool.

### Values and references

An end of a relationship is either a **reference** - it has identity, other pages say things about it, it gets a page and is linked - or a **value** - it is a kind, and any instance of it is as good as another, so it is written as a plain value.

The test is identity, not importance: *could two of them ever be told apart, other than by where or when they turned up?* If the only thing distinguishing two instances is the relationship they appear in, they have no identity of their own, and the relationship is what carries it.

**A value can become a reference later** without anything else changing: the field's values become links once the kind earns pages. That is deferred classification applied to an edge end, and it is why choosing *value* is never a dead end.

Which values a field may hold is the declaration's prose, not a mechanism. A group field (`reference-layer.md`) is one kind of value field.

**A value field stays a value even where its values have pages of their own.** A kind can have a page - a material, a currency - and still be written as a plain value in a field elsewhere, by an existing convention. Whether a field is an edge is the declaration's to say, in `links:`, not something to infer from whether matching pages exist. So reuse an existing value field as it is used; converting it into an edge is its own promotion (an **edge**, below), done across every type that carries it, never quietly for one new type.

### Aspects: when an entity is a lens

Some entities are named far more often than they are written about. A material, a currency, a mood: *the handle is brass*, *the price was in francs*, *the reply was curt*. Each of those facts is about the handle, the price, the reply - the quality is how it is described, and how someone might later want to look across the notes. It is an **index term** in the fact, not a second **subject** of it.

The four tests, all of which hold for an aspect:

| test | an aspect | what it rules out |
| --- | --- | --- |
| does it cut across many types? | yes | an ordinary entity type, which is one kind of thing |
| does it apply to a **part**, a **state** or a context, not only to a whole thing? | yes - *the handle is brass*, not *the door is brass* | a **role** or a **value**, which classify a whole page |
| does it have meaning of its own, worth a page? | yes - a rule about it, a reading of what it signals | a plain **value**, which has no page |
| are most facts that name it about something else? | **yes** | an ordinary entity, whose facts are about it |

The rules for an aspect:

- **A fact naming an aspect lives on its subject's page, with the aspect linked inline**, on the words that name it: *the handle is [[Brass|brass]]*. That link is the whole of the filing. The aspect's page gets **no bullet** for it, so there is one copy (`contract.md` law 4).
- **The aspect's page holds only what is about the aspect itself**: a rule the source states about it, a pattern in what it seems to mean (marked as the user's reading), how it is told from a neighbour.
- **Its backlinks are the lens.** Obsidian's backlinks pane lists every linked mention with the sentence around it, so the aspect's page shows each occurrence in context without carrying it; an agent gets the same from the link index or a search for the link. A view embedded on the page filtering `file.hasLink(this.file)` gives the same set as a table, and a narrative projection gathers by the same backlinks.
- **Link exactly where it is meant.** An aspect's name is often an ordinary word - *iron* in *ironic*, *the Iron Bridge* - which is why the decision is made at capture, where the referent is known, and never by a converter matching words (`reference-layer.md`). Its `common_names:` say which forms are ordinary.
- **A field holding the aspect is optional**, kept only where a filterable column is wanted (`materials:` on a kind of object). The inline link is what makes the occurrence findable; a field adds a whole-page label, never the context.
- **Declare it with `aspect: true`** (`registry.md`), so capture reads the direction instead of inferring it.
- **The cost, stated:** at rest, the aspect's page does not list its occurrences; they are one hop away, in the backlinks. The occurrences themselves stay readable where they belong, on their subjects' pages.

### Roles

A role is a part a thing plays that cuts across types: a person and an organisation can both be a party to something. It is a **tag** - a second label - never a second folder, and the type stays the primary label.

- **Tags nest** (`#party/plaintiff`), and a view filtering with `file.hasTag("party")` matches every level below it.
- **A tag asserts exactly what a folder does** (`contract.md` law 3): that this thing is a member of this kind. So a role tag is added only by promotion, never by capture deciding something "is" one.
- A role says *what part*, never *when*. If the part is played on an occasion, or with someone, it is a relation.

## Ownership

**A page may be owned by another page, to any depth**: a person owns the sessions held with them, a session owns the actions agreed in it. This is a hierarchy of *instances*, not of kinds - a session is not a kind of person; it is a kind of thing a person has - so classification stays flat, and ownership sits beside it.

**The test: does it exist apart from its owner?** A part does not - a person's bio, a session's actions - and is owned. A thing in its own right that its owner merely holds *for now* is not: an object that moves between rooms has a type of its own, and where it was found on an occasion is dated prose (`registry.md`, "A field holds a standing fact"). Both are nodes; ownership is only right when the part has no existence apart from its owner.

**The path is the truth.** Type folders and entity folders alternate, so the nearest type folder still says what a page is:

```
<Type folder>/
  <entity>/                      named by the entity's identity (registry.md, "Names")
    <its own page>.md            named by its type's pattern
    <Owned type folder>/
      <owned page>.md
  <another entity>.md            owns nothing yet: still a plain file
```

- **A type folder may be split into bucket folders by name or by a date field** - by year, say - between it and its pages (`registry.md`, "Buckets"); they are for browsing, and change nothing above.
- **An entity becomes a folder when its first owned page arrives** (`notebook.py` does it). Its filename does not change, so every link to it still lands.
- **Moving a page to another owner's folder re-parents it.**
- **`parent:` is written from the path** by `notebook.py tree` - and by anything that makes an owned page - as an ordinary link, so the graph, backlinks and views see ownership. Nobody edits it; where it disagrees with the path, the path wins and the check says so.
- **A type is top-level or owned, never both.** A thing that sometimes has an owner and sometimes not is two types.

**Reading it:**

| want | how |
| --- | --- |
| a page's direct children of one type | an embedded view filtered `parent == this` - a section the owner's type fills with owned pages embeds it (`registry.md`) |
| everything below a page, at any depth | `file.inFolder(this.file.folder)` |
| what a page is | its `type:`, as everywhere |

What a declaration says about it - `parents:`, `identity:`, the name pattern, sections filled by owned pages - is `registry.md`. An owned ledger, one per owner, is `ledger.md`. Renaming an owner is `notebook.py rename`, and it needs the running app (`obsidian.md`).

## Seeing it: the graph view

Obsidian's graph view draws the edges and, left alone, hides the labels - which is why a notebook of any size looks like spaghetti there. Its **colour groups** are how the labels show: a group colours every node a search matches. So the graph view is configured **from the registry**, never by hand:

| in the graph | from |
| --- | --- |
| one colour group per type, `[type:/^<name>$/]` - the type property, anchored, so two types sharing a folder still differ | each declaration's name |
| a relation's pages read as small connectors between their ends | the relation type's own colour group |
| an aspect is a hub, its spokes the things it describes - the lens, drawn | the aspect type's group |
| machinery filtered out of the view: ledgers, generated pages, the registry, the views, the hub | `ledger:`, `generated: true`, and the host's paths |
| a host's own additions, such as tinting one page | the host's config, placed before the derived groups |

- **Pin each type's colour** with `graph_color:` on its declaration (`registry.md`). An unpinned type gets a colour fixed by its name, moved past any colour already taken, and the derivation says so: pinning is what keeps it, since a palette shared by many types cannot stay collision-free by hashing alone.
- **Derived, so kept current by the workflow**: declaring or re-shaping a type ends by rerunning the derivation (`promotion.md`), and the schema check reports, as a browse, a type with no group or a group for no type.
- **The edges stay untyped in the picture.** A typed `author:` link, a provenance link and a prose mention all draw as the same line; arrows show direction and nothing more. The labels are what the graph can show, and they are most of what it needed.
- **The local graph** from any page, at depth 1 or 2, is the readable view - and Obsidian gives it **no defaults**: each local-graph pane keeps its own settings and starts with no colour groups (tested 2026-10-25). So the notebook ships a small Obsidian plugin, `notebook-graph` (`.obsidian/plugins/`), that copies the global graph's colour groups and filter into every local graph as it opens, and again whenever the derivation reruns. A local graph opened fresh also starts from the notebook's **local defaults** - depth, forces, display - kept in the plugin's `data.json`, since nothing global can set a local graph's depth; they are applied once, and from then on the pane's settings are the user's. The global graph's display and forces ship in `.obsidian/graph.json`; the derivation never touches them. It relies on the graph's internal options, not a public API; if an update breaks it, local graphs go back to uncoloured and nothing else is affected.

## What Obsidian can and cannot do with this

Tested on 2026-10-25 against Obsidian 1.14.4. Recheck after a major release.

| it can | it cannot |
| --- | --- |
| filter, sort and show a link-valued property as a column | **put properties on an edge.** A link is bare, which is why relations are pages |
| list formulas: `map`, `filter`, `reduce`, `unique`, `flat`, `join`; `split` on strings | **nest a property.** Objects in frontmatter are not supported, so values are atomic |
| custom table summaries over a column (counts, totals) | **group a row under several values.** Grouping by a list groups by the *whole list*: a page holding `[a, b]` lands in an `a, b` group, not in both |
| `file.hasTag("a")`, matching nested tags at every level | - |
| colour graph nodes by any search, including `tag:` (graph view groups) | type an edge in the graph: every link draws the same |
| query a group by a property, `[type:/^<type>$/]` - anchored, or it matches substrings | - |
| set the graph's groups and filter through the running app (`obsidian eval`, the graph plugin's `options` and `saveOptions()`), pushed live to an open graph view | match a folder with a bare `path:<Folder>`: it is a substring, and also catches a page elsewhere with the folder's name in its own - quote it with the slash, `path:"<Folder>/"` |
| `file.hasLink(this.file)` in an embedded view: the pages linking the page doing the embedding | - |
| filter an **embedded** view on `this` - the page doing the embedding: `<field> == this`, `<field>.contains(this.file.name.lower())` | evaluate `this` from the CLI: `base:query` has no embedding page |

And one tooling limit: `obsidian base:query` returns the flat rows of a view and **ignores its grouping and summaries**, which render only in the app. A check that needs a grouped answer computes it from the rows.
