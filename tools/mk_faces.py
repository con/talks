#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Generated with Claude Code 2.1.302 / Claude Opus 5
"""Put the people from the acknowledgements onto the project slides.

The acknowledgements slide names everyone once, at the end.  This puts a few
of the same faces in the corner of the slide about the thing they built, so
the people are present while their work is on screen rather than only in a
grid at the end -- and so the final grid is recognition rather than
introduction.

A deck declares who belongs on a slide and nothing else:

    <div class="faces" data-people="john-lee isaac-to yaroslav-halchenko"></div>

then

    tools/mk_faces.py --expand 2026-usrse-con-talk.html

fills every such div with linked, round portraits.  Re-running is idempotent:
the generated children are replaced, the declaration is kept.  So the deck
stays plain static HTML -- no runtime fetch, no build step, works under
file:// and in the PDF export -- while adding somebody to a slide is a
one-word edit plus a re-run.

Keys are portrait slugs (`pics/con-whoweare/john-lee.jpg` -> `john-lee`), and
any unambiguous substring of one works (`isaac`, but not `john`, which matches
both John Lee and John Wodder).  `--list` prints them.

The roster comes from con-whoweare.phtml, which tools/mk_whoweare.py
generates from the live whoweare page -- the same single source
tools/mk_ack_eras.py reads for the acknowledgements grid, so a face on a
project slide, a face in the grid, and the person's record on the website
cannot drift apart.  Each portrait links to that person's anchor on
centerforopenneuroscience.org/whoweare, so somebody reading the deck
afterwards can click a face and find out who it was.

Styling lives in css/custom.css (`.reveal .faces`); size is per-slide via
`style="--face-size:56px"` on the declaration if a crowded slide needs it.
"""

import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
ROSTER_SOURCE = "con-whoweare.phtml"
PORTRAITS = "pics/con-whoweare"
SITE = "https://centerforopenneuroscience.org"

# One <a class="cww-person"> per person, as tools/mk_whoweare.py writes it.
ENTRY = re.compile(
    r'<a class="cww-person" href="([^"]+)"[^>]*title="([^"]*)">'
    r'<img data-src="(' + PORTRAITS + r'/([^"/.]+)\.[A-Za-z]+)" alt="([^"]*)"')

# A declaration is any <div> carrying data-people.  Its generated children are
# <a> elements only, so the body can be sliced to the next </div>.
DECL = re.compile(r'<div[^>]*\bdata-people="([^"]*)"[^>]*>')


class Person:
    def __init__(self, slug, name, title, href, portrait):
        self.slug = slug
        self.name = name
        self.title = title or name
        self.href = href
        self.portrait = portrait


def roster():
    """slug -> Person, from the whoweare fragment plus any stray portrait.

    A portrait with no entry on the website (Ben Dichter is acknowledged here
    and has never been on it) is still usable: it links to the page itself
    rather than to an anchor that does not exist.
    """
    src = (HERE / ROSTER_SOURCE).read_text()
    people = {}
    for href, title, portrait, slug, name in ENTRY.findall(src):
        people[slug] = Person(slug, name, title, href, portrait)
    for f in sorted((HERE / PORTRAITS).iterdir()):
        if f.suffix.lower() in (".jpg", ".jpeg", ".png") and f.stem not in people:
            name = " ".join(w.capitalize() for w in f.stem.split("-"))
            people[f.stem] = Person(
                f.stem, name, name, f"{SITE}/whoweare",
                f"{PORTRAITS}/{f.name}")
    return people


def resolve(key, people):
    if key in people:
        return people[key]
    hits = [p for s, p in sorted(people.items())
            if key in s or key.lower() in p.name.lower()]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        sys.exit(f"mk_faces: no portrait matches {key!r} "
                 f"(try --list)")
    sys.exit(f"mk_faces: {key!r} is ambiguous: "
             f"{', '.join(h.slug for h in hits)}")


def faces(keys, people, indent=""):
    out = []
    for key in keys:
        p = resolve(key, people)
        out.append(
            f'{indent}<a class="face" href="{p.href}" target="_blank"'
            f' title="{p.title}"><img data-src="{p.portrait}"'
            f' alt="{p.name}"/></a>')
    return "\n".join(out)


def expand(deck, people, dry_run=False):
    path = HERE / deck
    s = path.read_text()
    n = 0
    pos = 0
    while (m := DECL.search(s, pos)) is not None:
        keys = m.group(1).split()
        end = s.find("</div>", m.end())
        if end < 0:
            sys.exit(f"{deck}: unclosed faces div at offset {m.start()}")
        body = s[m.end():end]
        if "<div" in body:
            sys.exit(f"{deck}: nested <div> inside a faces declaration at "
                     f"offset {m.start()} -- cannot tell where it ends")
        # Indent the children one step past the declaration itself.
        line = s.rfind("\n", 0, m.start()) + 1
        indent = re.match(r"[ \t]*", s[line:m.start()]).group(0) + "  "
        new = "\n" + faces(keys, people, indent) + "\n" + indent[:-2]
        s = s[:m.end()] + new + s[end:]
        pos = m.end() + len(new)
        n += 1
        print(f"  {' '.join(resolve(k, people).slug for k in keys)}",
              file=sys.stderr)
    if not dry_run:
        path.write_text(s)
    print(f"{'would fill' if dry_run else 'filled'} {n} face row(s) in {deck}",
          file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("people", nargs="*", metavar="KEY",
                    help="print the markup for these people")
    ap.add_argument("--expand", nargs="+", default=[], metavar="DECK.html",
                    help="fill every data-people div in these decks")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list", action="store_true", help="list the keys")
    a = ap.parse_args()

    people = roster()
    if a.list:
        for slug, p in sorted(people.items()):
            print(f"{slug:<40} {p.title}")
        return
    if a.people:
        print('<div class="faces" data-people="'
              + " ".join(resolve(k, people).slug for k in a.people) + '">')
        print(faces(a.people, people, "  "))
        print("</div>")
    for deck in a.expand:
        expand(deck, people, a.dry_run)
    if not a.people and not a.expand:
        ap.error("nothing to do: give people, --expand, or --list")


if __name__ == "__main__":
    main()
