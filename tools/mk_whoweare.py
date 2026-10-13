#!/usr/bin/env python3
"""Generate an acknowledgements fragment with all the faces from the CON website.

Reads content/pages/whoweare.html straight from the
con/centerforopenneuroscience.org repository, groups people by the <h2>
tier they live under (Centroids, Collaborators, Affiliated Faculty,
Emeritus, ...), downloads their portraits, and writes a reusable HTML
fragment (con-whoweare.phtml by default) with one row of linked faces per
tier. Each face links back to that person's anchor on the live page.

Usage (from the repository root):

    tools/mk_whoweare.py                        # regenerate fragment + pictures
    tools/mk_whoweare.py --inject 2026-dhmc-ieeg.html
    tools/mk_whoweare.py --no-images            # fragment only, keep pictures

--inject replaces whatever sits between

    <!-- BEGIN con-whoweare -->
    <!-- END con-whoweare -->

in the given deck(s), so decks stay openable as a single file (no build
step, no runtime include) while the fragment remains the single source to
regenerate from.

Portraits are rendered through `object-fit: cover`, so non-square
originals are centre-cropped rather than squashed, and are downscaled on
the way in (--max-size, 0 to keep the originals).

TODO: emit the logo tiers too, so the whole Acknowledgements slide is
generated rather than hand-maintained.  Right now --inject overwrites
everything between the markers, so any logo row added to a deck by hand
is lost on the next run.  Two separate pieces of work:

  * Collaborating projects / Partners.  Both already live on the same
    whoweare page, as <a href=...><img title=...></a> inside
    div#collaborating-projects and the Partners row -- links and titles
    come for free.  They are dropped today because tiers without
    portraits are filtered out in main().  Needs: a second "logo tier"
    renderer (no round crop, no name caption, height-based sizing), a
    way to pick a handful rather than all ~40 projects (--projects
    repronim,openneuro,dandi,datalad?), and the images pulled from
    theme/static/img/3rd/ instead of .../team/.

  * Funders.  NOT on the whoweare page at all -- there is no funders
    section to scrape.  Needs its own source: either a small table in
    this script (logo, href, title, award number) or a funders page on
    the website to parse once one exists.  Award numbers matter here;
    the logos alone are less useful than a link to the award.
"""

import argparse
import html
import os
import shutil
import subprocess
import sys
import urllib.request
from html.parser import HTMLParser

REPO = "con/centerforopenneuroscience.org"
SITE = "https://centerforopenneuroscience.org"
PAGE = "content/pages/whoweare.html"
# Pelican serves theme/static/img/... as /theme/img/...
STATIC_PREFIX = ("/theme/img/", "theme/static/img/")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mk_whoweare.py"})
    with urllib.request.urlopen(req) as r:
        return r.read()


def slugify(name):
    """Anchor id the website generates for a heading: 'Tor D. Wager' -> 'tor_d_wager_'."""
    kept = "".join(c if (c.isalnum() or c.isspace()) else "" for c in name.lower())
    return "_".join(kept.split()) + "_"


class Person:
    def __init__(self, name, anchor):
        self.name = name
        self.anchor = anchor
        self.image = None
        self.position = ""


class WhoWeAreParser(HTMLParser):
    """Linear scan: <h2> opens a tier, <h3> opens a person, the next <img> and
    .position <div> belong to that person."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tiers = []  # [(tier name, [Person, ...]), ...]
        self._collect = None  # 'tier' | 'name' | 'position'
        self._buf = []
        self._person = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h2":
            self._collect, self._buf = "tier", []
        elif tag == "h3":
            self._collect, self._buf = "name", []
            self._person = Person(None, a.get("id"))
        elif tag == "img" and self._person is not None and self._person.image is None:
            self._person.image = a.get("src")
        elif tag == "div" and "position" in a.get("class", "").split():
            self._collect, self._buf = "position", []

    def handle_data(self, data):
        if self._collect:
            self._buf.append(data)

    def handle_endtag(self, tag):
        if self._collect is None:
            return
        text = html.unescape(" ".join("".join(self._buf).split()))
        if tag == "h2" and self._collect == "tier":
            self.tiers.append((text, []))
            self._person = None
        elif tag == "h3" and self._collect == "name":
            self._person.name = text
            self._person.anchor = self._person.anchor or slugify(text)
            if not self.tiers:  # people before any <h2>, shouldn't happen
                self.tiers.append(("", []))
            self.tiers[-1][1].append(self._person)
        elif tag == "div" and self._collect == "position":
            if self._person is not None:
                self._person.position = text
        else:
            return
        self._collect, self._buf = None, []


def shrink(path, max_size):
    """Downscale in place -- these are displayed at ~64px, originals run to ~1MB."""
    if not max_size or not shutil.which("convert"):
        return
    tmp = path + ".tmp" + os.path.splitext(path)[1]
    subprocess.run(
        ["convert", path, "-colorspace", "RGB", "-filter", "Lanczos",
         "-resize", f"{max_size}x{max_size}>", "-colorspace", "sRGB",
         "-quality", "88", "-strip", tmp],
        check=True,
    )
    # re-encoding an already-small portrait can grow it -- keep whichever is smaller
    if os.path.getsize(tmp) < os.path.getsize(path):
        os.replace(tmp, path)
    else:
        os.remove(tmp)


def download_portraits(people, picsdir, ref, max_size):
    """Repo first; fall back to the live site when the blob is a git-annex pointer."""
    os.makedirs(picsdir, exist_ok=True)
    if max_size and not shutil.which("convert"):
        print("WARNING: ImageMagick `convert` not found -- keeping originals", file=sys.stderr)
    for p in people:
        if not p.image:
            continue
        name = os.path.basename(p.image)
        dest = os.path.join(picsdir, name)
        repo_path = p.image.replace(*STATIC_PREFIX, 1) if p.image.startswith(STATIC_PREFIX[0]) else p.image.lstrip("/")
        data = fetch(f"https://raw.githubusercontent.com/{REPO}/{ref}/{repo_path}")
        if len(data) < 512 and b"annex" in data:  # git-annex pointer file, not the image
            data = fetch(SITE + p.image)
            where = "site"
        else:
            where = "repo"
        with open(dest, "wb") as f:
            f.write(data)
        shrink(dest, max_size)
        print(f"  {name:<20} {len(data):>8} -> {os.path.getsize(dest):>7} B  ({where})", file=sys.stderr)


STYLE = """<style>
/* generated by tools/mk_whoweare.py -- tune via the --cww-* variables */
.con-whoweare { --cww-face: 64px; --cww-cell: 92px; --cww-font: 0.30em;
                text-align: center; line-height: 1.15; }
.con-whoweare .cww-tier { margin: 0 0 6px 0; }
.con-whoweare .cww-label { display: block; font-size: 0.38em; font-weight: bold;
                           letter-spacing: 0.08em; text-transform: uppercase;
                           opacity: 0.65; margin-bottom: 2px; }
.con-whoweare .cww-faces { display: flex; flex-wrap: wrap;
                           justify-content: center; align-items: flex-start; }
.con-whoweare .cww-person { display: inline-block; width: var(--cww-cell);
                            margin: 0 2px 2px 2px; text-decoration: none;
                            color: inherit; }
.con-whoweare .cww-person img { width: var(--cww-face); height: var(--cww-face);
                                object-fit: cover; object-position: center top;
                                border-radius: 50%; display: block;
                                margin: 0 auto 2px auto; border: 0; box-shadow: none; }
.con-whoweare .cww-person span { display: block; font-size: var(--cww-font);
                                 overflow-wrap: break-word; }
.con-whoweare .cww-person:hover img { outline: 2px solid currentColor; }
</style>
"""


def render(tiers, picsdir, ref):
    out = [
        f"<!-- GENERATED by tools/mk_whoweare.py from {REPO}@{ref}:{PAGE} -- do not edit by hand -->",
        STYLE.rstrip(),
        '<div class="con-whoweare">',
    ]
    for tier, people in tiers:
        out.append(f'  <div class="cww-tier"><span class="cww-label">{html.escape(tier)}</span>')
        out.append('	<div class="cww-faces">')
        for p in people:
            title = f"{p.name} — {p.position}" if p.position else p.name
            img = os.path.join(picsdir, os.path.basename(p.image))
            out.append(
                f'	  <a class="cww-person" href="{SITE}/whoweare#{p.anchor}" target="_blank"'
                f' title="{html.escape(title, quote=True)}">'
                f'<img data-src="{img}" alt="{html.escape(p.name, quote=True)}"/>'
                f"<span>{html.escape(p.name)}</span></a>"
            )
        out.append("	</div>")
        out.append("  </div>")
    out.append("</div>")
    return "\n".join(out) + "\n"


BEGIN, END = "<!-- BEGIN con-whoweare -->", "<!-- END con-whoweare -->"


def inject(deck, fragment):
    with open(deck) as f:
        s = f.read()
    try:
        head, rest = s.split(BEGIN, 1)
        _, tail = rest.split(END, 1)
    except ValueError:
        sys.exit(f"{deck}: no {BEGIN} ... {END} markers to fill in")
    with open(deck, "w") as f:
        f.write(f"{head}{BEGIN}\n{fragment}{END}{tail}")
    print(f"injected into {deck}", file=sys.stderr)


def check_anchors(tiers):
    live = fetch(SITE + "/whoweare").decode("utf-8", "replace")
    missing = [p.name for _, people in tiers for p in people if f'id="{p.anchor}"' not in live]
    if missing:
        print(f"WARNING: anchors not found on the live page: {', '.join(missing)}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", default="master", help="git ref of the website repo (default: master)")
    ap.add_argument("--outfile", default="con-whoweare.phtml")
    ap.add_argument("--picsdir", default="pics/con-whoweare")
    ap.add_argument("--inject", nargs="*", default=[], metavar="DECK.html")
    ap.add_argument("--no-images", action="store_true", help="only regenerate the fragment")
    ap.add_argument("--max-size", type=int, default=512, metavar="PX",
                    help="downscale portraits to fit PX (0 keeps the originals; default: 512)")
    ap.add_argument("--no-check-anchors", action="store_true")
    args = ap.parse_args()

    src = fetch(f"https://raw.githubusercontent.com/{REPO}/{args.ref}/{PAGE}").decode("utf-8")
    parser = WhoWeAreParser()
    parser.feed(src)
    # tiers without portraits are the logo sections (Collaborating projects, Partners)
    tiers = [(t, ps) for t, ps in parser.tiers if any(p.image for p in ps)]
    for tier, people in tiers:
        print(f"{tier}: {len(people)}", file=sys.stderr)

    if not args.no_check_anchors:
        check_anchors(tiers)
    if not args.no_images:
        download_portraits([p for _, ps in tiers for p in ps], args.picsdir, args.ref, args.max_size)

    fragment = render(tiers, args.picsdir, args.ref)
    with open(args.outfile, "w") as f:
        f.write(fragment)
    print(f"wrote {args.outfile}", file=sys.stderr)
    for deck in args.inject:
        inject(deck, fragment)


if __name__ == "__main__":
    main()
