#!/usr/bin/env python3
"""Set up a new notebook from this template: the mechanical half of /setup.

  setup.py <target> [--hub NAME] [--contract NAME]
                    [--ledger TYPE --ledger-folder FOLDER --ledger-kind periodic|span
                     [--log-section S] [--occasion-section S] | --no-ledger]
                    [--skill OLD=NEW ...] [--drop SKILL ...]
                    --assistance LEVEL --consultation LEVEL [--dry-run]

Every choice is a parameter, because the choices are judgement: the /setup
skill asks for them and this carries them out.

One time, one way. It copies what the template's manifest lists, as last
committed - never the working tree - into <target>, a new folder or an
existing repository that is not a notebook yet, and never overwrites a file
there. The template is only read. The manifest lists neither this script nor
the /setup skill, so a notebook has no setup in it to run again. It records
the template's URL and commit, which the update skill starts from.
"""
import argparse, io, json, os, pathlib, re, subprocess, sys, tarfile

TEMPLATE = pathlib.Path(__file__).resolve().parents[1]

MANIFEST = ".claude/notebook/manifest.txt"   # what a notebook gets, and how
SESSION = "CLAUDE.host.md"              # becomes the notebook's CLAUDE.md
CONTRACT = ".claude/skills/_shared/host-contract.md"
LEDGER = "Types/entry.md"
HUB = "Hub.md"
CONFIG = ".scripts/notebook_config.py"

ILLEGAL = set('"*?<>:|\\/[]#^')         # obsidian.md, "Filenames are a Sync constraint"


def published():
    """The template's address every checkout can reach - its origin, when that
    is a URL - or None."""
    url = _git(TEMPLATE, "remote", "get-url", "origin").stdout.decode().strip()
    return url if re.match(r"^[\w+.-]+://|^[\w.-]+@[\w.-]+:", url) else None

def _git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, check=False)

def _filename(kind, name):
    if not name or name[-1] in ". " or ILLEGAL & set(name):
        sys.exit(f"{kind} {name!r}: not a legal filename (obsidian.md) - "
                 f"no {' '.join(sorted(ILLEGAL))}, and no trailing period or space")
    return name

def _ident(kind, name):
    if not re.fullmatch(r"[a-z][a-z0-9-]*", name):
        sys.exit(f"{kind} {name!r}: lowercase letters, digits and hyphens, starting with a letter")
    return name


# ---------------------------------------------------------------- the template
def template():
    """path -> (bytes, mode), from the template's last commit."""
    head = _git(TEMPLATE, "rev-parse", "HEAD").stdout.decode().strip()
    if not head:
        sys.exit(f"not a git repository with a commit: {TEMPLATE}")
    tar = tarfile.open(fileobj=io.BytesIO(_git(TEMPLATE, "archive", "HEAD").stdout))
    files = {m.name: (tar.extractfile(m).read(), m.mode) for m in tar if m.isfile()}
    if SESSION not in files:
        sys.exit(f"{TEMPLATE} is a notebook, not the template: setup has already happened, "
                 "and this script and .claude/skills/setup/ can be deleted")
    return head, files

class Plan:
    """The template's files, being turned into the notebook's: exactly those
    the manifest lists. The rest are the template's own."""

    def __init__(self, files):
        lines = [l.split() for l in files[MANIFEST][0].decode().splitlines()
                 if l.strip() and not l.startswith("#")]
        self.entries = [tuple(f[:2]) for f in lines if f[0] != "choice"]
        # A choice: one file a notebook holds, from the source its setting picks.
        self.picks = {f[1]: f[2] for f in lines if f[0] == "choice" and len(f) >= 3}
        self.all = files
        self.files = {p: v for p, v in files.items() if self.kind(p)}

    def kind(self, path):
        hits = [(len(p), k) for k, p in self.entries
                if path == p or (p.endswith("/") and path.startswith(p))]
        k = max(hits)[1] if hits else None
        return None if k == "own" else k

    def move(self, old, new):
        self.files[new] = self.files.pop(old)

    def drop(self, prefix):
        for p in [p for p in self.files if p == prefix or p.startswith(prefix + "/")]:
            del self.files[p]

    def add(self, path, text):
        self.files[path] = (text.encode(), 0o644)

    def sub(self, path, old, new, count=1):
        """Replace text the template is known to hold. A miss means the
        skeleton changed under this script, which must then change with it."""
        text, mode = self.files[path]
        text = text.decode()
        if old not in text:
            sys.exit(f"setup.py is out of step with the template: {path} no longer contains {old!r}")
        self.files[path] = (text.replace(old, new, count).encode(), mode)

    def resub(self, path, pattern, new):
        text, mode = self.files[path]
        self.files[path] = (re.sub(pattern, new, text.decode(), flags=re.M).encode(), mode)

    def skills(self, kind="skeleton"):
        return sorted({p.split("/")[2] for p in self.files
                       if p.startswith(".claude/skills/") and p.endswith("/SKILL.md")
                       and self.kind(p) == kind})


# ---------------------------------------------------------------- the choices
def hub(plan, name):
    plan.move(HUB, f"{name}.md")
    plan.sub(f"{name}.md", "# Hub\n", f"# {name}\n")
    plan.sub(CONFIG, 'HUB = "Hub.md"', f'HUB = "{name}.md"')
    plan.sub(SESSION, "| hub | TODO — and set it in `.scripts/notebook_config.py` |",
             f"| hub | `{name}.md` |")

def ledger(plan, typ, folder, kind, log, occasion, skills):
    run = ", ".join(f"`/{skills[s]}`" for s in ("open", "prepare", "resume", "close") if s in skills)
    # Pointing at the declarations keeps the row true as ledgers are declared
    # and retired: the session file must survive a type change (README).
    plan.sub(SESSION, "| ledger | TODO: what an occasion is, and the skills that open and close one |",
             f"| ledger | the types `Types/` declares with `ledger:`" + (f", run by {run}" if run else "")
             + ". TODO: what an occasion is here |")
    if not typ:
        plan.drop(LEDGER)
        return
    new = f"Types/{typ}.md"
    plan.move(LEDGER, new)
    plan.sub(new, "declares: entry", f"declares: {typ}")
    plan.sub(new, "folder: Ledger", f"folder: {folder}")
    plan.sub(new, "ledger: periodic", f"ledger: {kind}")
    plan.sub(new, "  - Notes\n  - Working notes", f"  - {log}\n  - {occasion}")
    plan.sub(new, "log_to: Notes", f"log_to: {log}")
    plan.sub(new, "occasion_only: Working notes", f"occasion_only: {occasion}")
    plan.sub(new, "# entry\n", f"# {typ}\n")
    # The instruction to rename it, now carried out.
    plan.resub(new, r"\n> Rename it to what an occasion is called here.*\n", "")
    plan.add(f"Views/{folder}.base", f"""filters:
  and:
    - type == "{typ}"
views:
  - type: table
    name: {folder}
    order:
      - file.name
      - status
    sort:
      - property: file.name
        direction: DESC
""")

def contract(plan, name):
    new = f".claude/skills/_shared/{name}.md"
    if new != CONTRACT:
        plan.move(CONTRACT, new)
        for p in [SESSION] + [f".claude/skills/{s}/SKILL.md" for s in plan.skills()]:
            plan.sub(p, CONTRACT, new)
    plan.sub(new, "rename this file to what the notebook is about, change the pointer to it "
                  "in `CLAUDE.md` and each skill, and fill in each section", "fill in each section")

def skills(plan, renames, drops):
    """old name -> new name, for every skill the notebook keeps."""
    have = plan.skills()
    for s in list(renames) + drops:
        if s in plan.skills("generic"):
            sys.exit(f"{s} is generic: a notebook takes it as it is, under its own name")
        if s not in have:
            sys.exit(f"no skill {s!r} in the template (skills: {', '.join(have)})")
    for s in drops:
        plan.drop(f".claude/skills/{s}")
    kept = {s: renames.get(s, s) for s in have if s not in drops}
    for old, new in kept.items():
        path = f".claude/skills/{new}/SKILL.md"
        if old != new:
            for p in [p for p in plan.files if p.startswith(f".claude/skills/{old}/")]:
                plan.move(p, p.replace(f"/{old}/", f"/{new}/", 1))
            plan.sub(path, f"name: {old}\n", f"name: {new}\n")
        # Setup was the moment those decided; they are decided.
        plan.resub(path, r" (?:RENAME|DELETE) THIS\b.*$", "")
    return kept

def choose(plan, values):
    """Each choice's file, from the one source the notebook chose - the others
    never reach it (manifest.txt) - and the choice recorded and named."""
    for dest, pattern in plan.picks.items():
        var = re.findall(r"\{(\w+)\}", pattern)[0]
        src = pattern.format(**{var: values[var]})
        if src not in plan.all:
            options = sorted(pathlib.Path(p).stem for p in plan.all
                             if p.startswith(pattern.split("{")[0]) and p.endswith(".md"))
            sys.exit(f"--{var.lower()} {values[var]}: the template has {', '.join(options)}")
        plan.files[dest] = plan.all[src]
        plan.sub(CONFIG, f"{var} = None", f'{var} = "{values[var]}"')
        plan.sub(SESSION, f"<{var.lower()}>", values[var].capitalize())

def renamed(plan, hub_name, ledger_type, contract_name, kept, drops):
    """What this notebook calls each skeleton setup renamed or dropped, so the
    update skill can adapt the template's later changes (upstream.md)."""
    m = {SESSION: "CLAUDE.md"}
    if hub_name != "Hub":
        m[HUB] = f"{hub_name}.md"
    if ledger_type != "entry":
        m[LEDGER] = f"Types/{ledger_type}.md" if ledger_type else None
    if f".claude/skills/_shared/{contract_name}.md" != CONTRACT:
        m[CONTRACT] = f".claude/skills/_shared/{contract_name}.md"
    m.update({f".claude/skills/{old}/": f".claude/skills/{new}/" for old, new in kept.items() if old != new})
    m.update({f".claude/skills/{s}/": None for s in drops})
    body = "".join(f"\n    {json.dumps(k)}: {json.dumps(v) if v else 'None'}," for k, v in m.items())
    plan.sub(CONFIG, "SKELETONS = {}", f"SKELETONS = {{{body}\n}}")

def session(plan, head):
    """Where the notebook came from, for the update skill (upstream.md). No
    path is written: a notebook may be checked out in many places at once
    (obsidian.md), and so may the template - its URL is the same in all."""
    plan.sub(SESSION, "rename this file to `CLAUDE.md`, replacing the template's own, and fill it in",
             "fill this file in")
    url = published()
    if url:
        plan.sub(CONFIG, "TEMPLATE = None", f'TEMPLATE = "{url}"')
    else:
        print("note: the template has no origin every checkout can reach, so TEMPLATE is left "
              "for the update skill to ask")
    plan.sub(CONFIG, "TEMPLATE_COMMIT = None", f'TEMPLATE_COMMIT = "{head}"')
    plan.sub(CONFIG, 'NOT_OURS = {"CLAUDE.md", "CLAUDE.host.md"}   # CLAUDE.host.md is the template\'s own: a notebook has none',
             'NOT_OURS = {"CLAUDE.md"}')
    plan.move(SESSION, "CLAUDE.md")


# ---------------------------------------------------------------- run
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--hub", default="Hub")
    ap.add_argument("--contract", default="host-contract")
    ap.add_argument("--ledger")
    ap.add_argument("--ledger-folder")
    ap.add_argument("--ledger-kind", choices=("periodic", "span"))
    ap.add_argument("--log-section", default="Notes")
    ap.add_argument("--occasion-section", default="Working notes")
    ap.add_argument("--no-ledger", action="store_true")
    ap.add_argument("--skill", action="append", default=[], metavar="OLD=NEW")
    ap.add_argument("--drop", action="append", default=[], metavar="SKILL")
    ap.add_argument("--assistance", required=True, metavar="LEVEL",
                    help="how far Claude goes beyond recording: one of the template's levels")
    ap.add_argument("--consultation", required=True, metavar="LEVEL",
                    help="what Claude may read: one of the template's choices")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if a.no_ledger == bool(a.ledger):
        sys.exit("say what the ledger is - --ledger, --ledger-folder and --ledger-kind - or --no-ledger")
    if a.ledger and not (a.ledger_folder and a.ledger_kind):
        sys.exit("--ledger needs --ledger-folder and --ledger-kind")
    if a.ledger:
        if _ident("ledger type", a.ledger) == "type":
            sys.exit("ledger type 'type' is the registry's own")
        if _filename("ledger folder", a.ledger_folder) in ("Types", "Views") or a.ledger_folder.startswith("."):
            sys.exit(f"ledger folder {a.ledger_folder!r}: that folder is machinery, not a ledger's")
        for s in (a.log_section, a.occasion_section):
            if not s.strip() or "\n" in s or s.startswith("#"):
                sys.exit(f"section {s!r}: one line of heading text, without the #")
    _filename("hub", a.hub)
    _filename("contract", a.contract)
    renames = {}
    for r in a.skill:
        old, _, new = r.partition("=")
        renames[old] = _ident("skill", new)

    target = pathlib.Path(a.target).expanduser().resolve()
    if target == TEMPLATE or TEMPLATE in target.parents:
        sys.exit(f"the notebook goes outside the template: {target}")
    if (target / ".claude/notebook").exists():
        sys.exit(f"{target} is already a notebook. Setup is one time; there is nothing to do")

    head, files = template()
    url = published()
    if url:
        # The notebook records this commit, and its updates and guard fetch it
        # from the published template, so it has to be there already.
        _git(TEMPLATE, "fetch", "-q", "origin")
        if not _git(TEMPLATE, "branch", "-r", "--contains", head).stdout.strip():
            sys.exit(f"the template's last commit, {head[:7]}, is not on {url} yet: push it first. "
                     "The notebook records it, and fetches its updates from there")
    plan = Plan(files)
    kept = skills(plan, renames, a.drop)
    contract(plan, a.contract)
    hub(plan, a.hub)
    ledger(plan, a.ledger, a.ledger_folder, a.ledger_kind, a.log_section, a.occasion_section, kept)
    choose(plan, {"ASSISTANCE": a.assistance, "CONSULTATION": a.consultation})
    renamed(plan, a.hub, a.ledger, a.contract, kept, a.drop)
    session(plan, head)

    clash = sorted(p for p in plan.files if (target / p).exists())
    if clash:
        sys.exit(f"{target} already has files setup would write, and it never overwrites:\n  "
                 + "\n  ".join(clash))
    if not a.ledger and {"open", "close", "resume"} & set(kept):
        print("note: with no ledger, open, close and resume have nothing to act on - --drop them")
    if _git(TEMPLATE, "status", "--porcelain").stdout.strip():
        print(f"note: the template has uncommitted changes, and they are not copied")

    print(f"{'would set up' if a.dry_run else 'setting up'} {target}  from the template at {head[:7]}")
    for p in sorted(plan.files):
        print(f"  {p}")
    if a.dry_run:
        return

    for p, (data, mode) in plan.files.items():
        out = target / p
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        os.chmod(out, mode & 0o777)
    if _git(target, "rev-parse", "--is-inside-work-tree").returncode != 0:
        _git(target, "init", "-q")
        print("git init")
    # The template, kept in the notebook's repo for the guard to compare against
    # (upstream.md, "The guard"); then the guard itself.
    _git(target, "fetch", "-q", "--no-tags", url or str(TEMPLATE), "HEAD")
    _git(target, "update-ref", "refs/template/head", "FETCH_HEAD")
    sys.stdout.flush()
    for cmd in (["checkout.py"], ["notebook.py", "graph"]):
        subprocess.run([sys.executable, "-I", str(target / ".scripts" / cmd[0]), *cmd[1:]], check=True)
    print(f"template {head}  - recorded in {CONFIG}; name it in the first commit")


if __name__ == "__main__":
    main()
