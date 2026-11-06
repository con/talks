#!/usr/bin/env python3
"""Generate index.html and talks.yaml from the talk and poster records.

Every talk and poster is an XYZPublication record in the CON record store
(sourcedata/con-site-specific/metadata/records/XYZPublication/), typed
`bibo:Slideshow` or `fabio:ConferencePoster`.  A record is listed when its
`foaf:homepage` points into this repository's published mirror; that URL,
less the mirror prefix, is the path index.html links.  Records without one
(e.g. a deck whose annexed content is not published) are left out.

Authors are the record's attributed_to people, or its `bibo:authorList`
("A; B; C") where some authors have no person record.  Presenters, shown in
bold, are the attributed people with the role marcrel:spk; a talk with none
recorded has all its authors in bold.  People on the CON "who we are" page,
those with a dlthings:tier, link to their entry there.  A dlthings:DOI
identifier is linked after the title.

The data flows one way: fix a record, never the generated files.

Usage (from anywhere): tools/mk_index.py
CON_RECORD_STORE overrides the store location, as for tools/mk_ack_eras.py.
"""
import html
import os
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required")

HERE = pathlib.Path(__file__).resolve().parent.parent
STORE = pathlib.Path(os.environ.get(
    "CON_RECORD_STORE", HERE / "sourcedata/con-site-specific"))
RECORDS = STORE / "metadata/records"
BASE = "https://datasets.datalad.org/centerforopenneuroscience/talks/"
WHOWEARE = "https://centerforopenneuroscience.org/whoweare#"
KINDS = {"bibo:Slideshow": "talk", "fabio:ConferencePoster": "poster"}


def attrs(d, pred):
    return [a["value"] for a in (d.get("attributes") or [])
            if a.get("predicate") == pred]


def one(d, pred):
    v = attrs(d, pred)
    return v[0] if v else None


def person_name(pid, persons):
    d = persons.get(pid)
    if d is None:
        return pid
    return (d.get("display_label") or d.get("formatted_name")
            or f"{d.get('given_name', '')} {d.get('family_name', '')}".strip())


def load_persons():
    persons = {}
    for f in (RECORDS / "XYZPerson").glob("*.yaml"):
        d = yaml.safe_load(f.read_text())
        persons[d["pid"]] = d
    return persons


def whoweare_links(persons):
    """Name -> URL of that person on the page; its anchors are the name, as
    `yaroslav_o_halchenko_`."""
    links = {}
    for pid, d in persons.items():
        if one(d, "dlthings:tier"):
            name = person_name(pid, persons)
            anchor = re.sub(r"[^\w ]", "", name.lower()).replace(" ", "_")
            links[name] = f"{WHOWEARE}{anchor}_"
    return links


def authors_of(d, persons):
    listed = one(d, "bibo:authorList")
    if listed:
        return listed.split("; ")
    return [person_name(a["object"], persons) for a in d.get("attributed_to") or []]


def presenters_of(d, persons):
    return [person_name(a["object"], persons) for a in d.get("attributed_to") or []
            if "marcrel:spk" in (a.get("roles") or [])]


def doi_of(d):
    return next((i["notation"] for i in d.get("identifiers") or []
                 if i.get("schema_type") == "dlthings:DOI"), None)


def is_wip(path):
    """A deck whose <title> starts with [WiP] is not listed yet -- the same
    convention the hand-kept index followed, so dropping the marker from the
    deck is what publishes it."""
    f = HERE / path
    if f.suffix != ".html" or not f.exists():
        return False
    m = re.search(r"<title>\s*(.*?)\s*</title>", f.read_text(errors="replace"), re.S)
    return bool(m) and m.group(1).lower().startswith("[wip]")


def load_entries():
    persons = load_persons()
    entries = []
    for f in sorted((RECORDS / "XYZPublication").glob("*.yaml")):
        d = yaml.safe_load(f.read_text())
        kind = KINDS.get(d.get("kind"))
        url = one(d, "foaf:homepage")
        if kind is None or not url or not url.startswith(BASE):
            continue
        path = url[len(BASE):]
        if is_wip(path):
            continue
        pdf = one(d, "dcat:downloadURL")
        presenters = presenters_of(d, persons)
        doi = doi_of(d)
        entries.append({
            "date": str(d["generated_by"][0]["at_time"]),
            "kind": kind,
            "title": d["title"],
            "path": path,
            "url": url,
            **({"pdf": pdf} if pdf else {}),
            **({"doi": doi} if doi else {}),
            "venue": one(d, "bibo:presentedAt"),
            "authors": authors_of(d, persons),
            **({"presenters": presenters} if presenters else {}),
            "pid": d["pid"],
        })
    # Newest first.  Dates are YYYY, YYYY-MM or YYYY-MM-DD; padding with
    # "-00" puts a month-only date after the known days of that month (an
    # unknown day is not a late one).  Ties go by path.
    entries.sort(key=lambda e: e["path"])
    entries.sort(key=lambda e: (e["date"] + "-00-00")[:10], reverse=True)
    return entries


def check_coverage(entries):
    """A root deck without a record would silently drop off the index."""
    listed = {e["path"] for e in entries}
    # A PDF shown through pdfdeck.html is listed by its viewer path.
    listed |= {e["pdf"][len(BASE):] for e in entries if "pdf" in e}
    for f in sorted(HERE.glob("20*.html")) + sorted(HERE.glob("20*.pdf")):
        if f.name not in listed and not is_wip(f.name):
            print(f"WARNING: {f.name} has no talk record in {RECORDS}",
                  file=sys.stderr)


def check_presenters(entries):
    """A presenter missing from the author list would silently lose the bold."""
    for e in entries:
        for p in e.get("presenters", []):
            if p not in e["authors"]:
                print(f"WARNING: {e['pid']}: presenter {p} is not among its authors",
                      file=sys.stderr)


def author_html(name, bold, links):
    text = html.escape(name)
    if name in links:
        text = f'<a href="{html.escape(links[name])}">{text}</a>'
    return f"<strong>{text}</strong>" if name in bold else text


def render(entries, links=None):
    esc = html.escape
    links = links or {}
    items, year = [], None
    for e in entries:
        if e["date"][:4] != year:
            if year is not None:
                items.append("      </ul>")
            year = e["date"][:4]
            items += [f"      <h2>{year}</h2>", '      <ul class="talks">']
        extra = ""
        if e["kind"] != "talk":
            extra += f' <span class="kind">{esc(e["kind"])}</span>'
        if "pdf" in e:
            extra += (f' (<a class="alt" href="{esc(e["pdf"][len(BASE):])}">'
                      f'PDF</a>)')
        if "doi" in e:
            extra += (f' (<a class="alt" href="https://doi.org/{esc(e["doi"])}">'
                      f'DOI</a>)')
        bold = e.get("presenters") or (e["authors"] if e["kind"] == "talk" else [])
        authors = ", ".join(author_html(a, bold, links) for a in e["authors"])
        meta = " &middot; ".join(
            [esc(x) for x in (e["date"], e["venue"]) if x]
            + [f'<a class="alt file" href="{esc(e["path"])}">{esc(e["path"])}</a>'])
        items.append(
            f'        <li><a href="{esc(e["path"])}">{esc(e["title"])}</a>{extra}'
            f' <span class="authors">{authors}</span>'
            f' <span class="meta">{meta}</span></li>')
    if year is not None:
        items.append("      </ul>")
    return TEMPLATE.replace("@ITEMS@", "\n".join(items))


TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CON Talks</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700" rel="stylesheet" type="text/css">
  <style>
    /* Loose visual rhyme with https://centerforopenneuroscience.org/ */
    :root {
      --con-blue: #87AADE;
      --con-dark: #38434C;
      --con-text: #333;
      --con-muted: #777;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      font-weight: 400;
      color: var(--con-text);
      background: #fff;
      line-height: 1.5;
    }
    header {
      background: var(--con-blue);
      color: #fff;
      padding: 2em 1em;
    }
    header .inner { max-width: 960px; margin: 0 auto; }
    header h1 {
      margin: 0;
      font-weight: 600;
      font-size: 2em;
    }
    header h1 a { color: #fff; text-decoration: none; }
    header p {
      margin: 0.25em 0 0 0;
      font-weight: 300;
      font-size: 1.1em;
      opacity: 0.95;
    }
    main {
      max-width: 960px;
      margin: 0 auto;
      padding: 2em 1em 4em 1em;
    }
    main h2 {
      font-weight: 600;
      color: var(--con-dark);
      border-bottom: 2px solid var(--con-blue);
      padding-bottom: 0.25em;
      margin-top: 1.75em;
    }
    ul.talks {
      list-style: none;
      padding: 0;
      margin: 0.5em 0;
    }
    ul.talks li {
      padding: 0.5em 0;
      border-bottom: 1px solid #eee;
    }
    ul.talks a {
      color: var(--con-dark);
      text-decoration: none;
      font-weight: 600;
    }
    ul.talks a.alt { font-weight: 400; }
    ul.talks .kind {
      font-size: 0.75em;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #fff;
      background: var(--con-blue);
      border-radius: 3px;
      padding: 0.05em 0.4em;
      vertical-align: middle;
    }
    ul.talks a:hover { color: var(--con-blue); text-decoration: underline; }
    ul.talks .authors {
      display: block;
      font-size: 0.9em;
    }
    ul.talks .authors a { color: inherit; font-weight: 400; }
    ul.talks .authors strong, ul.talks .authors strong a { font-weight: 700; }
    ul.talks .meta {
      display: block;
      font-size: 0.9em;
      color: var(--con-muted);
      overflow-wrap: anywhere;
    }
    ul.talks .file { font-family: 'Source Code Pro', monospace; }
    footer {
      background: var(--con-dark);
      color: #fff;
      padding: 1.5em 1em;
      font-size: 0.9em;
    }
    footer .inner { max-width: 960px; margin: 0 auto; }
    footer a { color: var(--con-blue); }
  </style>
</head>
<body>
  <header>
    <div class="inner">
      <h1><a href="https://centerforopenneuroscience.org/">Center for Open Neuroscience</a></h1>
      <p>Talks, slide decks &amp; posters</p>
    </div>
  </header>
  <main>
    <p>Slides and posters from talks and workshops by CON people. This location is also a <a href="https://datasets.datalad.org/?dir=/centerforopenneuroscience/talks">DataLad dataset (git/git-annex repository)</a> so you can datalad clone it to get all the sources and materials. Also as data: <a href="talks.yaml">talks.yaml</a>. Presenters are in bold; where it is not recorded who gave a talk, all its authors are.</p>
@ITEMS@
  </main>
  <footer>
    <div class="inner">
      Auto-generated by <code>tools/mk_index.py</code> from the talk records in <a href="https://github.com/ORINOCO-Lite/con-site-specific">con-site-specific</a>.
    </div>
  </footer>
</body>
</html>
"""


def main():
    entries = load_entries()
    if not entries:
        sys.exit(f"No talk records found in {RECORDS}")
    check_coverage(entries)
    check_presenters(entries)
    (HERE / "index.html").write_text(render(entries, whoweare_links(load_persons())))
    header = ("# Generated by tools/mk_index.py from the XYZPublication records in\n"
              "# sourcedata/con-site-specific -- do not edit; fix the records.\n")
    (HERE / "talks.yaml").write_text(header + yaml.safe_dump(
        entries, sort_keys=False, allow_unicode=True, width=88))
    print(f"Wrote index.html and talks.yaml with {len(entries)} entries.")


if __name__ == "__main__":
    main()
