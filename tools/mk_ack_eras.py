#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Generated with Claude Code 2.1.295 / Claude Opus 5
"""Generate one self-contained acknowledgements fragment per era.

The talk returns to the same people slide again and again as it walks
chronologically, each time with one more era revealed.  Written inline that
would be ~40 KB of generated markup per era in a deck whose whole point is
to stay hand-editable, so each era is a standalone HTML file that the deck
pulls in with an <iframe>.

Why an iframe and not reveal's own external markdown: `data-markdown="x.md"`
is fetched with XMLHttpRequest, which `file://` blocks as cross-origin, so
the slide comes up EMPTY when the deck is opened as a plain file.  The repo's
CLAUDE.md requires every deck to be openable that way.  An <iframe> still
renders under file:// -- only *script* access into it is blocked, which
nothing here needs.  Both were checked under Chromium before choosing.

Each fragment is self-styled, because reveal's CSS does not cross the iframe
boundary.

Each fragment keeps the SECTION STRUCTURE of the full acknowledgements
slide -- Centroids, Collaborators, Affiliated Faculty, Emeritus, the two
project bands, and Funders and in-kind support -- and shows a section
heading only once something is listed under it.  So the slide does not just
accumulate faces, it grows the shape of the final slide.

People move between sections as the talk advances.  Someone who has left is
not dimmed in place: they appear under **Emeritus**, which is where they are
today.  The tier recorded in the store is TODAY's, so the role on the CON
association is what says what they were at the time, and WHEN that role
started is what says from when.  Most of the Emeritus have one association
carrying `marcrel:swd` (software developer) for their whole stay, so they are
Centroids throughout.  Andy Connolly has two: contributor from 2014 and staff
only from 2020, so he moves Collaborators -> Centroids -> Emeritus as the
talk advances.  That is the store's own answer, not an editorial one.

    accent   joined within this era, or named in ACCENT -- ringed
    dim      already on the slide from an earlier era      -- faded back
    (left)   association ended       -- moved to the Emeritus section, NOT faded
    unseen   has not joined yet      -- omitted entirely

Leaving is not a reason to be greyed out.  Emeritus is where someone is
filed today, not a statement that their work mattered less, so the Emeritus
section renders at full strength like every other section.  Fading is used
for one thing only: on an era slide, everyone already introduced steps back
so the people this era is about can be seen.  The final slide
(`ack-now.html`) fades nobody and rings nobody.

Who gets the accent is, by default, whoever arrived in this era.  The store
cannot answer "who worked on THIS era's projects" -- the later project
records name only the PI or the lead (`repronim` names nobody at all, `dandi`
names two people), so deriving the accent from project associations would
grey out most of the people who built the thing.  ACCENT below is the manual
override for that, per era.
"""
import argparse
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
# The record store is vendored as a submodule, so a fresh clone generates the
# same slide without a second checkout living somewhere else on the machine.
# CON_RECORD_STORE still wins, for running against an uncommitted store.
STORE = pathlib.Path(os.environ.get(
    "CON_RECORD_STORE", HERE / "sourcedata/con-site-specific"))
OUT = HERE / "2026-usrse-con-talk"

# The chronology the abstract itself walks, cut into the eras the talk visits.
ERAS = [
    ("2004", "2000–2004", "Debian immersion"),
    ("2008", "2005–2008", "pkg-exppsy · PyMVPA"),
    ("2012", "2009–2012", "NeuroDebian"),
    ("2016", "2013–2016", "DataLad · BIDS"),
    ("2020", "2017–2020", "OpenNeuro · NWB · ReproNim"),
    ("2024", "2021–2024", "DANDI · EMBER · HED"),
    ("2026", "2025–", "STAMPED · ORINOCO-Lite"),
]

# Extra people to ring on a given era's slide, beyond that era's arrivals.
# Keyed by the era's end year, values are display names as they appear in the
# record store.  Use this when an era is about work done by people who were
# already here -- the arrival date cannot say that, and the project records
# are too thin to derive it (see the module docstring).
ACCENT = {
    # "2024": ["John Lee", "Austin Macdonald"],
}

# Project logos, with the date each project enters the story.  Dates are the
# project `started` in the record store; the band is the one the
# acknowledgements selection puts it in.
BANDS = [
    ("Worked on directly", [
        ("DataLad", "2013-11-01", "pics/con-projects/datalad_logo.png", 42, "https://www.datalad.org/"),
        ("ReproNim", "2016-04-15", "pics/con-projects/repronim_logo.svg", 58, "https://repronim.org/"),
        ("DANDI", "2019-07-24", "pics/con-projects/dandi_logo.png", 49, "https://dandiarchive.org/"),
        ("EMBER", "2024-09-16", "pics/con-projects/ember_logo.png", 58, "https://emberarchive.org/"),
        ("BIDS", "2016-01-01", "pics/bids-logo-wide.png", 42, "https://bids.neuroimaging.io/"),
        ("NWB", "2017-08-03", "pics/con-projects/nwb_logo.png", 30, "https://nwb.org/"),
    ]),
    ("Large communities we take part in", [
        # Debian is where the practice was learned and is still packaged into.
        # Its Open Use logo (the swirl without the word) is explicitly free
        # for anyone, unlike the Official Use one.
        ("Debian", "2005-07-04", "pics/borrowed/debian-openlogo.svg", 46, "https://www.debian.org"),
        # debianmed-mh.svg from people.debian.org/~tille/debian-med/logos/ --
        # the caduceus-in-a-swirl mark, scalable, unlike the med-06.jpg
        # wordmark.  blends.debian.org itself just reuses the Debian swirl.
        ("Debian Med", "2020-02-24", "pics/borrowed/debian-med-logo.svg", 46, "https://blends.debian.org/med/"),
        ("scikit-learn", "2010-03-24", "pics/con-projects/scikit-learn_logo.png", 33, "https://scikit-learn.org/stable/"),
        ("PsychoPy", "2009-06-15", "pics/con-projects/psychopy_logo.png", 33, "https://www.psychopy.org/"),
        ("HCP", "2017-01-01", "pics/con-projects/hcp_logo.png", 33, "https://www.humanconnectome.org/"),
    ]),
]

# Funders and in-kind support, with when each first supported the work.
#
# The award dates are the funders' own, from NIH RePORTER and the NSF award
# API: NSF 1429999 starts 2014-09-01 and NIH's first money is ReproNim/CRNC
# on 2016-04-15.  That ordering is the point -- NSF funded DataLad years
# before NIH funded anything here, and NeuroDebian was never NIH-funded at
# all.
#
# The institutional rows are EDITORIAL, not sourced.  Dartmouth, PBS and DBIC
# date from 2009, when YOH joined Jim Haxby's lab in the PBS department as a
# postdoc (CV: Postdoctoral Fellow, 2009-2012; Hanke was there 2009-2011
# before returning to Germany).  Only the year is sourced -- the month is a
# placeholder, and any date in 2009 lands in the right era.  CCN stays at
# 2015-07 because CON became one of its Associated Programs as a Center, not
# as a postdoc.  INCF's backing for the NIDM and BIDS grassroots work has no
# date in the store either.
FUNDERS = [
    ("Dartmouth College", "2009-01-01", "pics/dartmouth-logo.svg", 62, "https://home.dartmouth.edu/"),
    ("PBS", "2009-01-01", "pics/borrowed/pbs-mark.svg", 60, "https://pbs.dartmouth.edu/"),
    ("CCN", "2015-07-01", "pics/ccn-logo.svg", 46, "https://www.dartmouth.edu/ccn/"),
    ("DBIC", "2009-01-01", "pics/borrowed/dbic-logo.png", 42, "https://www.dartmouth.edu/dbic/"),
    ("NSF", "2014-09-01", "pics/borrowed/nsf1.jpg", 62, "https://www.nsf.gov"),
    ("NIH", "2016-04-15", "pics/borrowed/nih.png", 62, "https://www.nih.gov"),
    ("INCF", "2016-01-01", "pics/borrowed/incf-mark.png", 30, "https://incf.org"),
    ("AWS Open Data", "2019-08-01", "pics/borrowed/aws-mark.png", 44, "https://aws.amazon.com/opendata/open-data-sponsorship-program/"),
]

# Jim Haxby is dated 2015-07-22 in the store because the Center's own record
# is the only association it carries for him -- there is no Haxby-lab or PBS
# project record yet.  But the collaboration starts in 2009, with the postdoc.
# Pin him there until con-site-specific grows a record that says so properly.
EARLIEST_OVERRIDE = {
    "xyzrins:persons/james-haxby": "2009-01-01",
}

CSS = """
/* The slide carries the era title, so the fragment does not repeat it --
   it only draws the grid, centred, filling the width it is given. */
html,body{margin:0;padding:0;background:transparent;height:100%;
  font-family:'Source Sans Pro',Helvetica,sans-serif;color:#333;}
body{display:flex;flex-direction:column;justify-content:center;}
.sec{margin:0 0 10px 0;}
.lbl{display:block;font-size:11.5px;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;opacity:.6;margin:0 0 3px 0;text-align:center;}
.grid{display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-start;
  gap:4px 10px;}
.logos{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;
  gap:0 22px;}
.logos img{display:block;}
.chip{display:inline-block;font-size:15px;font-weight:600;color:#555;
  border:1px solid #cfc6b8;border-radius:4px;padding:4px 10px;}
.p{width:92px;text-align:center;text-decoration:none;color:inherit;
  transition:opacity .4s ease;}
.p img{width:62px;height:62px;border-radius:50%;object-fit:cover;
  border:2px solid transparent;display:block;margin:0 auto 2px;}
.p span{display:block;font-size:10.5px;line-height:1.15;}
.accent img{border-color:#c0392b;box-shadow:0 0 0 3px rgba(192,57,43,.18);}
.accent span{font-weight:700;color:#c0392b;}
.present{opacity:1;}
.dim{opacity:.55;filter:grayscale(60%);}
.count{font-size:13px;color:#777;margin-top:14px;text-align:center;}
"""


# The fragment is dropped into a 1360px iframe and .p cells are 92px wide
# with a 10px gap, so 13 fit on a line.  Left to itself flex-wrap fills each
# line before starting the next, which is how a 15-person Emeritus section
# ends up 13 + 2: one row running the full width of the slide and two
# stragglers underneath.  Capping the grid's width at a balanced
# people-per-row instead gives 8 + 7, which reads as one block.
CELL = 92 + 10          # .p width + .grid column-gap
ROW_MAX = 13            # how many of those fit across the iframe


def grid_width(n):
    """max-width that splits n cells into even rows, or None if one row does."""
    if n <= ROW_MAX:
        return None
    rows = -(-n // ROW_MAX)          # ceil
    per_row = -(-n // rows)          # ceil
    return per_row * CELL


def attrs(d, pred):
    return [a["value"] for a in (d.get("attributes") or [])
            if a.get("predicate") == pred]


def one(d, pred):
    v = attrs(d, pred)
    return v[0] if v else None


def load():
    """Each person, with the EARLIEST dated association anywhere in the store.

    Taking only the site-root associations would date everyone from 2015-07,
    because that is when whoweare.html starts -- so the Debian, pkg-exppsy
    and PyMVPA eras would show one person each.  The collaborations are older
    than the Center and the project records say so: Hanke on PyMVPA from
    2007-05-24 and NeuroDebian from 2009-03-28, YOH on Fail2Ban from 2005.
    The earliest date across every project is the honest "since when we have
    been working together".

    `ended` is taken ONLY from the site-root association, because leaving one
    project is not leaving the Center.
    """
    R = STORE / "metadata/records"
    people = {}
    for f in (R / "XYZPerson").glob("*.yaml"):
        d = yaml.safe_load(f.read_text())
        people[d["pid"]] = (f.stem, d)

    earliest, ended, via, swd_since = {}, {}, {}, {}
    for f in sorted((R / "XYZProject").glob("*.yaml")):
        proj = yaml.safe_load(f.read_text())
        for a in (proj.get("associated_with") or []):
            pid = a.get("object")
            if pid not in people:
                continue
            st = (a.get("started") or {}).get("at_time")
            if st and (pid not in earliest or st < earliest[pid]):
                earliest[pid] = st
                via[pid] = f.stem
            if f.stem == "site-root":
                # marcrel:swd on the CON association says they were staff,
                # which is what decides where a current-Emeritus person sits
                # while they were still active.  A person can hold several
                # site-root associations, and the staff one need not be the
                # first -- Andy Connolly contributed from 2014 and was hired
                # in 2020 -- so keep WHEN it starts, not just whether it
                # exists.  Undated means from the beginning.
                if "marcrel:swd" in (a.get("roles") or []):
                    w = st or "0000"
                    if pid not in swd_since or w < swd_since[pid]:
                        swd_since[pid] = w
                if not st:
                    # Deliberately undated on the site root: the founding
                    # director predates the website, so his association has
                    # no start by design.  He is present from the first era.
                    # assignment, not setdefault: fail2ban already set 2005
                    # for him and the point is that he precedes all of it
                    earliest[pid] = "0000"
                    via[pid] = "founding"
                en = (a.get("ended") or {}).get("at_time")
                # a person can have several site-root associations (a gap,
                # or a contributor and a staff stretch side by side); they are
                # gone only once every one of them has ended, and the date is
                # the last of those ends
                if en and not any(
                        (b.get("object") == pid and not b.get("ended"))
                        for b in (proj.get("associated_with") or [])):
                    ended[pid] = max(en, ended.get(pid, ""))

    for pid, when in EARLIEST_OVERRIDE.items():
        if pid in people and (pid not in earliest or when < earliest[pid]):
            earliest[pid] = when
            via[pid] = "editorial"

    rows = []
    for pid, (slug, d) in people.items():
        if pid not in earliest and one(d, "dlthings:tier") is None:
            continue
        rows.append({
            "slug": slug,
            "name": d.get("display_label") or one(d, "dlthings:formatted_name") or slug,
            "tier": one(d, "dlthings:tier"),
            "started": earliest.get(pid),
            "ended": ended.get(pid),
            "via": via.get(pid),
            "swd_since": swd_since.get(pid),
        })
    return rows


PORTRAIT_SOURCE = "con-whoweare.phtml"


def portraits():
    """name -> existing portrait path, from the shared whoweare fragment.

    The record store names portraits `persons/<slug>/portrait.ext`, but this
    repo already carries them under the whoweare page's own filenames, which
    are the same slugs (pics/con-whoweare/yaroslav-halchenko.jpg).  Reusing
    those avoids copying 35 more binaries into a DataLad dataset to say the
    same thing.

    Read from con-whoweare.phtml -- which tools/mk_whoweare.py generates from
    the live whoweare page, and which names the downloaded files -- rather than
    from a deck.  Decks now EMBED the fragments this script writes, so scraping
    one for portraits would be circular.

    Paths get `../` because an iframe resolves relative to the FRAGMENT,
    which lives one directory down.

    Returns two maps.  The first is by display name, scraped from the
    fragment.  The second is by record slug, from whatever is actually in
    pics/con-whoweare/, and covers anyone the whoweare page does not list --
    Ben Dichter is acknowledged here and has never been on the site.  To add
    such a person, drop pics/con-whoweare/<record-slug>.<ext> beside the
    scraped ones; no code change needed.
    """
    src = (HERE / PORTRAIT_SOURCE).read_text()
    by_name = {name: "../" + p for p, name in
               re.findall(r'data-src="(pics/con-whoweare/[^"]+)" alt="([^"]+)"', src)}
    by_slug = {f.stem: "../" + f.relative_to(HERE).as_posix()
               for f in sorted((HERE / "pics/con-whoweare").iterdir())
               if f.suffix.lower() in (".jpg", ".jpeg", ".png")}
    return by_name, by_slug


def logo_or_text(name, src, h, url=None):
    """A band entry.  Not everything has a mark -- Debian Med uses Debian's.

    Everything is a link: people follow a deck afterwards and click the logos,
    and the repo's slide rules require counts and marks to be navigable.
    target=_top so a click inside the iframe navigates the whole page rather
    than loading a site into an 880px box with no way back out.
    """
    n = html.escape(name)
    inner = (f'<img src="../{src}" alt="{n}" title="{n}" style="height:{h}px"/>'
             if src else f'<span class="chip" title="{n}">{n}</span>')
    if not url:
        return inner
    return f'<a href="{html.escape(url)}" target="_top" title="{n}">{inner}</a>'


def fragment(rows, era_end, era_start, label, sub, pics, by_slug, accent=True):
    """One era's slide: the full slide's sections, with only what exists yet.

    A section heading appears the moment something is listed under it and not
    before, so the shape of the final acknowledgements slide assembles over
    the talk rather than arriving all at once.
    """
    # Which section is each person in, as of this era?
    sections = {"Centroids": [], "Collaborators": [],
                "Affiliated Faculty": [], "Emeritus": []}
    ringed = set(ACCENT.get(era_end[:4], ()))
    n_accent = 0
    for r in rows:
        st = r["started"]
        if st is None or st > era_end:
            continue                       # not yet part of the story
        if r["ended"] and r["ended"] <= era_end:
            sec = "Emeritus"               # where they are filed, nothing more
        else:
            tier = r["tier"]
            # The store records TODAY's tier.  A current-Emeritus person
            # counts as staff for the eras from their marcrel:swd association
            # onwards, and as a contributor before it -- so someone who
            # contributed for years before being hired is not retroactively
            # made a Centroid.
            swd = r["swd_since"]
            if tier == "Emeritus":
                tier = ("Centroids" if swd is not None and swd <= era_end
                        else "Collaborators")
            sec = tier if tier in sections else "Collaborators"
        # Emphasis is decided for everyone alike, Emeritus included.
        if not accent:
            cls = "present"                # the final slide: no ring, no fade
        elif st >= era_start or r["name"] in ringed:
            cls = "accent"
            n_accent += 1
        else:
            cls = "dim"
        sections[sec].append((cls, r))
    for v in sections.values():
        v.sort(key=lambda x: (x[1]["started"] or "", x[1]["name"]))

    out = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
           f'<style>{CSS}</style></head><body>']
    shown_total = 0
    for sec in ("Centroids", "Collaborators", "Affiliated Faculty", "Emeritus"):
        group = sections[sec]
        if not group:
            continue                       # heading stays hidden until filled
        shown_total += len(group)
        out.append('<div class="sec">')
        out.append(f'<span class="lbl">{html.escape(sec)}</span>')
        w = grid_width(len(group))
        out.append(f'<div class="grid" style="max-width:{w}px;margin:0 auto">'
                   if w else '<div class="grid">')
        for cls, r in group:
            pic = pics.get(r["name"]) or by_slug.get(r["slug"])
            img = (f'<img src="{pic}" alt="{html.escape(r["name"])}"/>' if pic
                   else '<img alt=""/>')
            since = f' \u2014 since {r["started"]}' if r["started"] != "0000" else ""
            out.append(
                f'<a class="p {cls}" target="_blank" '
                f'href="https://centerforopenneuroscience.org/whoweare" '
                f'title="{html.escape(r["name"])}{since}">'
                f'{img}<span>{html.escape(r["name"])}</span></a>')
        out.append('</div></div>')

    for band_label, items in BANDS:
        live = [x for x in items if x[1] <= era_end]
        if not live:
            continue
        out.append('<div class="sec">')
        out.append(f'<span class="lbl">{html.escape(band_label)}</span>')
        out.append('<div class="logos">')
        for name, since, src, h, url in live:
            out.append(logo_or_text(name, src, h, url))
        out.append('</div></div>')

    live_f = [x for x in FUNDERS if x[1] <= era_end]
    if live_f:
        out.append('<div class="sec">')
        out.append('<span class="lbl">Funders and in-kind support</span>')
        out.append('<div class="logos">')
        for name, since, src, h, url in live_f:
            out.append(logo_or_text(name, src, h, url))
        out.append('</div></div>')

    out.append('</body></html>')
    return "\n".join(out), shown_total, n_accent


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    rows = load()
    pics, by_slug = portraits()
    missing = sorted(r["name"] for r in rows
                     if r["name"] not in pics and r["slug"] not in by_slug)
    if missing:
        print(f"no portrait for {len(missing)}: {missing}", file=sys.stderr)
    prev = "0000"
    print(f"{'era':12s} {'people':>7s} {'ring':>4s}  file")
    for end, label, sub in ERAS:
        frag, n, n_new = fragment(rows, end + "-12-31", prev + "-01-01",
                                  label, sub, pics, by_slug)
        f = OUT / f"ack-{end}.html"
        if a.write:
            OUT.mkdir(parents=True, exist_ok=True)
            f.write_text(frag)
        print(f"  {label:10s} {n:7d} {n_new:4d}  {f.relative_to(HERE)}"
              f"  ({len(frag)//1024}K)")
        prev = str(int(end) + 1)

    # Same final state, with nobody ringed and nobody faded.  Both only mean
    # something inside the US-RSE deck's seven-era build-up; in a deck that
    # just wants the acknowledgements once (the MIT STAMPED talk) a ring reads
    # as an unexplained highlight and a fade as a slight.
    last = ERAS[-1][0]
    frag, n, _ = fragment(rows, last + "-12-31", "9999-01-01",
                          ERAS[-1][1], ERAS[-1][2], pics, by_slug, accent=False)
    f = OUT / "ack-now.html"
    if a.write:
        f.write_text(frag)
    print(f"  {'current':10s} {n:7d} {'-':>4s}  {f.relative_to(HERE)}"
          f"  ({len(frag)//1024}K)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
