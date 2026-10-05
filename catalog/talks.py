#!/usr/bin/env python3
# /// script
# dependencies = ["pyyaml", "linkml"]
# ///
"""Tooling for talks.yaml (catalog/PLAN.md, D8). DRAFT: only `validate`.

  talks.py validate [TALKS_YAML] [--site CON_SITE_SPECIFIC_CHECKOUT]

Checks TALKS_YAML (default: talks.yaml at the repository root) against the
LinkML schema catalog/talks.schema.yaml (closed: unknown fields are errors),
and then what a schema cannot express: references between entries, files
existing in this repository, unique ids. With --site, people/project/grant
slugs are also looked up in a con-site-specific checkout.
"""
import argparse
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

CATALOG = Path(__file__).resolve().parent
REPO = CATALOG.parent


class Loader(yaml.SafeLoader):
    """Keep dates as written: no timestamp conversion."""


Loader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def load(path):
    # Dates stay strings. A year-only date must be quoted ('2016'):
    # unquoted, YAML reads it as a number, which the schema rejects.
    return yaml.load(Path(path).read_text(), Loader=Loader)


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, msg):
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"warning {where}: {msg}")


def check_schema(cat, rep):
    validator = Validator(str(CATALOG / "talks.schema.yaml"),
                          validation_plugins=[JsonschemaValidationPlugin(closed=True)])
    for r in validator.validate(cat, "TalkCatalog").results:
        rep.error("schema", r.message)


def repo_files():
    out = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                         text=True, check=True).stdout
    return set(out.splitlines())


def check_refs(cat, rep, site=None):
    people = set(cat.get("people") or {})
    organizations = set(cat.get("organizations") or {})
    events = cat.get("events") or {}
    archives = cat.get("video_archives") or {}
    topics = set(cat.get("topics") or {})
    talks = cat.get("talks") or []
    talk_ids = [t.get("id") for t in talks]
    files = repo_files()

    for tid, n in Counter(talk_ids).items():
        if n > 1:
            rep.error(f"talks/{tid}", f"id used {n} times")

    for slug, ev in events.items():
        if ev.get("part_of") and ev["part_of"] not in events:
            rep.error(f"events/{slug}", f"part_of: unknown event {ev['part_of']!r}")
        for o in ev.get("organizers") or []:
            if o not in people | organizations:
                rep.error(f"events/{slug}", f"organizers: unknown person or organization {o!r}")

    youtube = Counter()
    for t in talks:
        w = f"talks/{t.get('id')}"
        for a in t.get("authors") or []:
            if a not in people:
                rep.error(w, f"authors: unknown person {a!r}")
        for d in t.get("derived_from") or []:
            if d not in talk_ids:
                rep.warn(w, f"derived_from: {d!r} has no record in this file")
        slides = t.get("slides") or {}
        for f in [slides.get("source")] + list(slides.get("exports") or []):
            if f and f not in files:
                rep.error(w, f"slides: {f!r} is not tracked in this repository")
        for c in t.get("companions") or []:
            if not any(p.startswith(c.rstrip("/") + "/") for p in files):
                rep.error(w, f"companions: {c!r} has no tracked files")
        if not slides.get("source") and not slides.get("url"):
            rep.error(w, "slides: neither source nor url")
        for h in (t.get("reuse") or {}).get("highlights") or []:
            for tp in h.get("topics") or []:
                if tp not in topics:
                    rep.error(w, f"reuse: unknown topic {tp!r}")
        for i, p in enumerate(t.get("presentations") or []):
            pw = f"{w}/presentations/{i}"
            if p.get("event") not in events:
                rep.error(pw, f"event: unknown event {p.get('event')!r}")
            for pr in p.get("presenters") or []:
                if pr not in people:
                    rep.error(pw, f"presenters: unknown person {pr!r}")
            for r in p.get("recordings") or []:
                youtube[r.get("youtube")] += 1
                for c in r.get("archived_in") or []:
                    a = archives.get(c.get("archive"))
                    if a is None:
                        rep.error(pw, f"archived_in: unknown archive {c.get('archive')!r}")
                    elif a.get("layout") == "collection" and not c.get("channel"):
                        rep.error(pw, f"archived_in: {c['archive']!r} is a collection; channel required")
                    elif a.get("layout") == "single-channel" and c.get("channel"):
                        rep.warn(pw, f"archived_in: {c['archive']!r} is single-channel; channel ignored")
    for vid, n in youtube.items():
        if n > 1:
            rep.warn("talks", f"YouTube id {vid} recorded {n} times")

    if site:
        records = Path(site) / "metadata" / "records"
        known = {cls: {f.stem for f in (records / cls).glob("*.yaml")}
                 for cls in ("XYZPerson", "XYZProject", "XYZGrant")}
        for slug in people:
            if slug not in known["XYZPerson"]:
                rep.warn(f"people/{slug}", "no con-site-specific person record")
        for t in talks:
            for p in t.get("projects") or []:
                if p not in known["XYZProject"]:
                    rep.warn(f"talks/{t.get('id')}", f"projects: no con-site-specific record {p!r}")
            for g in t.get("grants") or []:
                if g not in known["XYZGrant"]:
                    rep.warn(f"talks/{t.get('id')}", f"grants: no con-site-specific record {g!r}")
        # D10 (talk within an author's/presenter's CON membership window) needs
        # dated site-root associations, which con-site-specific does not have yet.


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("talks_yaml", nargs="?", default=str(REPO / "talks.yaml"))
    v.add_argument("--site", help="con-site-specific checkout")
    args = ap.parse_args()

    cat = load(args.talks_yaml)
    rep = Report()
    check_schema(cat, rep)
    if not rep.errors:  # references are only meaningful for a well-formed file
        check_refs(cat, rep, args.site)
    for line in rep.warnings + rep.errors:
        print(line)
    print(f"{args.talks_yaml}: {len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
