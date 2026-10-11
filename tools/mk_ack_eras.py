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
today.  While they were still staff they appear under Centroids, because all
fourteen of the current Emeritus carry `marcrel:swd` (software developer) on
their CON association -- the tier recorded in the store is today's, and the
role is what says what they were at the time.

    new      joined within this era      -- highlighted
    present  joined earlier, still here  -- normal
    (left)   association ended           -- moved to the Emeritus section
    unseen   has not joined yet          -- omitted entirely
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
STORE = pathlib.Path(os.environ.get(
    "CON_RECORD_STORE", "/home/yoh/proj/orinoco-lite/con-site-specific"))
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

# Project logos, with the date each project enters the story.  Dates are the
# project `started` in the record store; the band is the one the
# acknowledgements selection puts it in.
BANDS = [
    ("Worked on directly", [
        ("DataLad", "2013-11-01", "pics/con-projects/datalad_logo.png", 42),
        ("ReproNim", "2016-04-15", "pics/con-projects/repronim_logo.svg", 58),
        ("DANDI", "2019-07-24", "pics/con-projects/dandi_logo.png", 49),
        ("EMBER", "2024-09-16", "pics/con-projects/ember_logo.png", 58),
        ("BIDS", "2016-01-01", "pics/bids-logo-wide.png", 42),
        ("NWB", "2017-08-03", "pics/con-projects/nwb_logo.png", 30),
    ]),
    ("Large communities we take part in", [
        # Debian is where the practice was learned and is still packaged into.
        # Its Open Use logo (the swirl without the word) is explicitly free
        # for anyone, unlike the Official Use one.
        ("Debian", "2005-07-04", "pics/borrowed/debian-openlogo.svg", 46),
        # The blend has no mark of its own -- blends.debian.org/med uses the
        # same swirl -- so it appears as text rather than a second swirl.
        ("Debian Med", "2020-02-24", None, 0),
        ("scikit-learn", "2010-03-24", "pics/con-projects/scikit-learn_logo.png", 33),
        ("PsychoPy", "2009-06-15", "pics/con-projects/psychopy_logo.png", 33),
        ("HCP", "2017-01-01", "pics/con-projects/hcp_logo.png", 33),
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
# The institutional rows are EDITORIAL, not sourced: Dartmouth, PBS, CCN and
# DBIC have supported the work in kind for longer than CON has existed, and
# 2015-07 is simply when the Center they host was founded.  INCF's backing
# for the NIDM and BIDS grassroots work has no date in the store either.
FUNDERS = [
    ("Dartmouth College", "2015-07-01", "pics/dartmouth-logo.svg", 62),
    ("PBS", "2015-07-01", "pics/borrowed/pbs-mark.svg", 60),
    ("CCN", "2015-07-01", "pics/ccn-logo.svg", 46),
    ("DBIC", "2015-07-01", "pics/borrowed/dbic-logo.png", 42),
    ("NSF", "2014-09-01", "pics/borrowed/nsf1.jpg", 62),
    ("NIH", "2016-04-15", "pics/borrowed/nih.png", 62),
    ("INCF", "2016-01-01", "pics/borrowed/incf-mark.png", 30),
    ("AWS Open Data", "2019-08-01", "pics/borrowed/aws-mark.png", 44),
]

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
.new img{border-color:#c0392b;box-shadow:0 0 0 3px rgba(192,57,43,.18);}
.new span{font-weight:700;color:#c0392b;}
.present{opacity:1;}
.past{opacity:.45;filter:grayscale(70%);}
.count{font-size:13px;color:#777;margin-top:14px;text-align:center;}
"""


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

    earliest, ended, via, isdev = {}, {}, {}, {}
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
                # while they were still active
                if "marcrel:swd" in (a.get("roles") or []):
                    isdev[pid] = True
                if not st:
                    # Deliberately undated on the site root: the founding
                    # director predates the website, so his association has
                    # no start by design.  He is present from the first era.
                    # assignment, not setdefault: fail2ban already set 2005
                    # for him and the point is that he precedes all of it
                    earliest[pid] = "0000"
                    via[pid] = "founding"
                en = (a.get("ended") or {}).get("at_time")
                # a person can have several site-root associations (a gap);
                # only the LAST one ending means they are gone
                if en and not any(
                        (b.get("object") == pid and not b.get("ended"))
                        for b in (proj.get("associated_with") or [])):
                    ended[pid] = en
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
            "swd": isdev.get(pid, False),
        })
    return rows


def portraits_from_deck():
    """name -> existing portrait path, read out of the deck itself.

    The record store names portraits `persons/<slug>/portrait.ext`, but this
    repo already carries them under short hand-chosen names
    (pics/con-whoweare/yarik.jpg).  Reusing those avoids copying 33 more
    binaries into a DataLad dataset to say the same thing, and keeps the
    fragments consistent with the full acknowledgements slide.

    Paths get `../` because an iframe resolves relative to the FRAGMENT,
    which lives one directory down.
    """
    deck = (HERE / "2026-usrse-con-talk.html").read_text()
    return {name: "../" + src for src, name in
            re.findall(r'data-src="(pics/con-whoweare/[^"]+)" alt="([^"]+)"', deck)}


def logo_or_text(name, src, h):
    """A band entry.  Not everything has a mark -- Debian Med uses Debian's."""
    if src:
        return (f'<img src="../{src}" alt="{html.escape(name)}" '
                f'title="{html.escape(name)}" style="height:{h}px"/>')
    return f'<span class="chip" title="{html.escape(name)}">{html.escape(name)}</span>'


def fragment(rows, era_end, era_start, label, sub, pics):
    """One era's slide: the full slide's sections, with only what exists yet.

    A section heading appears the moment something is listed under it and not
    before, so the shape of the final acknowledgements slide assembles over
    the talk rather than arriving all at once.
    """
    # Which section is each person in, as of this era?
    sections = {"Centroids": [], "Collaborators": [],
                "Affiliated Faculty": [], "Emeritus": []}
    n_new = 0
    for r in rows:
        st = r["started"]
        if st is None or st > era_end:
            continue                       # not yet part of the story
        if r["ended"] and r["ended"] <= era_end:
            sec, cls = "Emeritus", "past"
        else:
            tier = r["tier"]
            # The store records TODAY's tier.  Everyone currently Emeritus
            # carries marcrel:swd on their CON association, i.e. they were
            # staff -- so while still active they belong under Centroids.
            if tier == "Emeritus":
                tier = "Centroids" if r["swd"] else "Collaborators"
            sec = tier if tier in sections else "Collaborators"
            cls = "new" if st >= era_start else "present"
        if cls == "new":
            n_new += 1
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
        out.append('<div class="grid">')
        for cls, r in group:
            pic = pics.get(r["name"])
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
        for name, since, src, h in live:
            out.append(logo_or_text(name, src, h))
        out.append('</div></div>')

    live_f = [x for x in FUNDERS if x[1] <= era_end]
    if live_f:
        out.append('<div class="sec">')
        out.append('<span class="lbl">Funders and in-kind support</span>')
        out.append('<div class="logos">')
        for name, since, src, h in live_f:
            out.append(logo_or_text(name, src, h))
        out.append('</div></div>')

    out.append('</body></html>')
    return "\n".join(out), shown_total, n_new


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    rows = load()
    pics = portraits_from_deck()
    missing = sorted({r["name"] for r in rows} - set(pics))
    if missing:
        print(f"no portrait for {len(missing)}: {missing}", file=sys.stderr)
    prev = "0000"
    print(f"{'era':12s} {'people':>7s} {'new':>4s}  file")
    for end, label, sub in ERAS:
        frag, n, n_new = fragment(rows, end + "-12-31", prev + "-01-01",
                                  label, sub, pics)
        f = OUT / f"ack-{end}.html"
        if a.write:
            OUT.mkdir(parents=True, exist_ok=True)
            f.write_text(frag)
        print(f"  {label:10s} {n:7d} {n_new:4d}  {f.relative_to(HERE)}"
              f"  ({len(frag)//1024}K)")
        prev = str(int(end) + 1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
