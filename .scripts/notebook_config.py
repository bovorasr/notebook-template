"""The host's own names. Every generic script here imports this and nothing else
domain-specific. Everything else a script needs from the host - the ledger
among it - is in the type declarations, so it is read from there, not repeated.

See .claude/notebook/README.md, "the interface": these are the parts of it that
the checks need in code rather than in prose.
"""

# The hub: where an observation with no type yet legitimately lives.
HUB = "Hub.md"

# Pages a tool may neither edit nor link to, and whose links are not checked:
# documentation about the notes, which may hold deliberate examples of broken
# syntax. Generated pages need no entry - their type says `generated: true` -
# and nor do verbatim texts, whose type says `sections: []` (registry.md).
NOT_OURS = {"CLAUDE.md", "CLAUDE.host.md"}   # CLAUDE.host.md is the template's own: a notebook has none

# Group fields: a field whose names each denote a set of pages related because
# they share it, never one page (.claude/notebook/reference-layer.md). The
# linker reports these names and never links them.
GROUP_FIELDS = []

# Where the registry's declarations and the views live.
TYPES_DIR = "Types"
VIEWS_DIR = "Views"

# The graph view (`notebook.py graph`, .claude/notebook/graph.md). Groups and
# the filter are derived from the declarations; these are only the host's
# additions. GRAPH_EXTRA is a list of (search query, "#rrggbb") groups placed
# before the derived ones - first match wins - such as tinting one page.
# GRAPH_EXCLUDE is a list of extra filter terms, such as "-file:\"README\"".
GRAPH_EXTRA = []
GRAPH_EXCLUDE = []

# The host's own audit rules (audit.py): what no declaration can say about
# whether a page stands on its own. AUDIT_DEFERRALS adds regexes for wording
# that points at something instead of saying it. audit_page is given a page's
# folder and text and returns its problems, as short strings.
AUDIT_DEFERRALS = []

def audit_page(folder, text):
    return []

# Where this notebook came from (.claude/notebook/upstream.md): the template's
# URL, and the template commit its generic files are level with. Setup writes
# both and the update skill moves the commit; in the template they are None.
# These and SKELETONS stay plain literals: upstream.py reads them without
# running this file. Everything else here may be computed, and a notebook may
# add names of its own that its settings are computed from.
TEMPLATE = None
TEMPLATE_COMMIT = None

# This notebook's two choices, made at setup (.claude/notebook/README.md, item
# 4): its level of assistance and its consultation, held as one file each -
# .claude/notebook/assistance.md and consultation.md - from the template's
# source of that name. Plain literals: upstream.py reads them to know which.
ASSISTANCE = None
CONSULTATION = None

# The template's skeletons this notebook renamed or dropped: the template's
# path -> this notebook's, or None where it was dropped. A folder maps as a
# folder. The update skill adapts a skeleton's changes into the file named here.
SKELETONS = {}
