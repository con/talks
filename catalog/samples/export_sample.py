#!/usr/bin/env python3
# /// script
# dependencies = ["pyyaml"]
# ///
"""PROTOTYPE of `talks.py export-things` (PLAN.md §5, Phase 5B).

Maps the sample talks.yaml onto datalad-concepts `xyzri` records, laid out
like con-site-specific (`<out>/<Class>/<file>.yaml`). It targets the
demo-research-information schema *with* the drafted `XYZEvent` /
`XYZPresentation` additions (yarikoptic/datalad-concepts,
branch claude/serene-cray-ozqirg).

Usage: export_sample.py talks.yaml OUTDIR
"""
import re
import sys
from pathlib import Path

import yaml

LIVE_BASE = "https://datasets.datalad.org/centerforopenneuroscience/talks/"
ZOTERO_GROUP = "6197458"  # con-site-specific sources/zotero/source.yaml

EVENT_KINDS = {
    "conference": "bibo:Conference",
    "workshop": "bibo:Workshop",
    "session": "xyzrins:event-types/session",
    "webinar": "xyzrins:event-types/webinar",
    "webinar-series": "xyzrins:event-types/webinar-series",
}
# classifier records the export needs; copied from psychoinformatics-site-specific
# where a record exists there, otherwise label only
CLASSIFIERS = [
    ("XYZBibliographicType", {
        "pid": "fabio:Presentation", "display_label": "Presentation",
        "description": "A set of slides containing text, tables or figures, designed to "
        "communicate ideas or research results, for projection and viewing by an "
        "audience at a conference, symposium, seminar, lecture, workshop or other "
        "gatherings, typically embodied in a particular manifestation format such as "
        "a SlideShare or PowerPoint slideshow."}),
    ("XYZBibliographicType", {
        "pid": "bibo:AudioVisualDocument", "display_label": "Audio-visual document",
        "description": "An audio-visual document; film, video, and so forth."}),
    ("XYZAgentRole", {
        "pid": "obo:CRO_0000100", "name": "Presenter",
        "description": "Oral presentation intended to present information or teach "
        "people about a particular subject, such as a talk or poster presentation at "
        "a conference."}),
    ("XYZEventType", {"pid": "bibo:Conference", "display_label": "Conference"}),
    ("XYZEventType", {"pid": "bibo:Workshop", "display_label": "Workshop"}),
    ("XYZEventType", {"pid": "xyzrins:event-types/session", "display_label": "Session"}),
    ("XYZEventType", {"pid": "xyzrins:event-types/webinar", "display_label": "Webinar"}),
    ("XYZEventType", {"pid": "xyzrins:event-types/webinar-series",
                      "display_label": "Webinar series"}),
]


def date(v):
    # YAML parses 2026-10-19 into a date and 2016 into an int; xyzri wants strings
    return None if v is None else str(v)


def ident(notation):
    return {"notation": notation, "schema_type": "dlthings:Identifier"}


def filename(pid):
    if pid.startswith("xyzrins:"):
        return pid.split("/", 1)[1].replace("/", "-")
    return re.sub(r"[:_]", "-", pid).lower()


def event_pid(slug):
    return f"xyzrins:events/{slug}"


def export_event(slug, ev):
    rec = {"pid": event_pid(slug), "schema_type": "xyzri:XYZEvent", "title": ev["name"]}
    if ev.get("kind"):
        rec["kind"] = EVENT_KINDS[ev["kind"]]
    if ev.get("part_of"):
        rec["part_of"] = [event_pid(ev["part_of"])]
    if ev.get("start") is not None:
        rec["started"] = {"at_time": date(ev["start"]), "schema_type": "dlthings:Start"}
    if ev.get("end") is not None:
        rec["ended"] = {"at_time": date(ev["end"]), "schema_type": "dlthings:End"}
    attrs = []
    if ev.get("url"):
        attrs.append({"predicate": "foaf:homepage", "value": ev["url"]})
    # free-text places have no slot (`at_location` takes an IRI); see samples/README.md
    for key in ("location", "room"):
        if ev.get(key):
            attrs.append({"predicate": "schema:location", "value": ev[key]})
    if attrs:
        rec["attributes"] = [dict(a, schema_type="dlthings:AttributeSpecification")
                             for a in attrs]
    if ev.get("project"):
        rec["influenced_by"] = [{"object": f"xyzrins:projects/{ev['project']}",
                                 "schema_type": "xyzri:XYZInfluence"}]
    return "XYZEvent", rec


def export_talk(t, archives):
    pid = t.get("pid") or f"xyzrins:talks/{t['id']}"
    rec = {"pid": pid, "schema_type": "xyzri:XYZPublication",
           "kind": "fabio:Presentation", "title": t["title"]}
    if t.get("description"):
        rec["description"] = " ".join(t["description"].split())

    presenters = {p for pr in t.get("presentations", []) for p in pr.get("presenters", [])}
    attributions = []
    for a in t.get("authors", []):
        roles = ["marcrel:aut"] + (["obo:CRO_0000100"] if a in presenters else [])
        attributions.append({"object": f"xyzrins:persons/{a}", "roles": roles})
    for p in sorted(presenters - set(t.get("authors", []))):
        attributions.append({"object": f"xyzrins:persons/{p}", "roles": ["obo:CRO_0000100"]})
    rec["attributed_to"] = [dict(a, schema_type="dlthings:Attribution") for a in attributions]

    if t.get("projects"):
        rec["generated_by"] = [{"object": f"xyzrins:projects/{p}",
                                "schema_type": "dlthings:Generation"} for p in t["projects"]]
    if t.get("derived_from"):
        rec["derived_from"] = [{"object": f"xyzrins:talks/{d}",
                                "schema_type": "dlthings:Derivation"} for d in t["derived_from"]]

    presented = []
    for pr in t.get("presentations", []):
        q = {"object": event_pid(pr["event"]), "schema_type": "xyzri:XYZPresentation"}
        if pr.get("date") is not None:
            q["at_time"] = date(pr["date"])
        presented.append(q)
    if presented:
        rec["presented_at"] = presented

    ids = []
    slides = t.get("slides", {})
    if slides.get("source"):
        ids.append(LIVE_BASE + slides["source"])
    if slides.get("url"):
        ids.append(slides["url"])
    ids += [LIVE_BASE + e for e in slides.get("exports", [])]
    if t.get("zenodo", {}).get("record"):
        ids.append(f"https://zenodo.org/records/{t['zenodo']['record']}")
    if t.get("zotero"):
        ids.append(f"zotero:group:{ZOTERO_GROUP}:item:{t['zotero']}")
    rec["identifiers"] = [ident(i) for i in ids]
    out = [("XYZPublication", rec)]

    # recordings: one XYZDocument per video, generated by the presentation's event
    for pr in t.get("presentations", []):
        for r in pr.get("recordings", []):
            vid = r["youtube"]
            v = {"pid": f"xyzrins:videos/{vid}", "schema_type": "xyzri:XYZDocument",
                 "kind": "bibo:AudioVisualDocument"}
            gen = {"object": event_pid(pr["event"]), "schema_type": "dlthings:Generation"}
            if pr.get("date") is not None:
                gen["at_time"] = date(pr["date"])
            v["generated_by"] = [gen]
            # the event alone does not say *which* talk was recorded (a conference
            # has many); see samples/README.md
            v["derived_from"] = [{"object": pid, "schema_type": "dlthings:Derivation"}]
            urls = [f"https://www.youtube.com/watch?v={vid}"]
            for c in r.get("archived_in", []):
                a = archives[c["archive"]]
                urls.append(a["video_url"].format(base=a["base"], channel=c["channel"], id=vid))
            v["identifiers"] = [ident(u) for u in urls]
            out.append(("XYZDocument", v))
    return out


def main(src, outdir):
    cat = yaml.safe_load(Path(src).read_text())
    records = list(CLASSIFIERS)
    records += [export_event(s, e) for s, e in cat["events"].items()]
    for t in cat["talks"]:
        records += export_talk(t, cat["video_archives"])
    for cls, rec in records:
        f = Path(outdir) / cls / f"{filename(rec['pid'])}.yaml"
        f.parent.mkdir(parents=True, exist_ok=True)
        rec.setdefault("schema_type", f"xyzri:{cls}")
        f.write_text(yaml.safe_dump(rec, sort_keys=True, allow_unicode=True, width=78))
    print(f"wrote {len(records)} records to {outdir}")


if __name__ == "__main__":
    main(*sys.argv[1:])
