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

People are drawn from the site-root project's associations in
con-site-specific, which carry `started` (and `ended`) dates derived from
the website's own git history.  A person belongs to an era when their
association began at or before that era's end:

    new      joined within this era      -- highlighted
    present  joined earlier, still here  -- normal
    past     association already ended   -- dimmed
    unseen   has not joined yet          -- omitted
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

CSS = """
/* The slide carries the era title, so the fragment does not repeat it --
   it only draws the grid, centred, filling the width it is given. */
html,body{margin:0;padding:0;background:transparent;height:100%;
  font-family:'Source Sans Pro',Helvetica,sans-serif;color:#333;}
body{display:flex;flex-direction:column;justify-content:center;}
.grid{display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-start;
  gap:6px 12px;}
.p{width:92px;text-align:center;text-decoration:none;color:inherit;
  transition:opacity .4s ease;}
.p img{width:62px;height:62px;border-radius:50%;object-fit:cover;
  border:2px solid transparent;display:block;margin:0 auto 2px;}
.p span{display:block;font-size:10.5px;line-height:1.15;}
.new img{border-color:#c0392b;box-shadow:0 0 0 3px rgba(192,57,43,.18);}
.new span{font-weight:700;color:#c0392b;}
.present{opacity:1;}
.past{opacity:.3;filter:grayscale(80%);}
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

    earliest, ended, via = {}, {}, {}
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


def fragment(rows, era_end, era_start, label, sub, pics):
    shown = []
    for r in rows:
        st = r["started"]
        if st is None or st > era_end:
            continue                      # not yet part of the story
        if r["ended"] and r["ended"] <= era_end:
            cls = "past"
        elif st >= era_start:
            cls = "new"
        else:
            cls = "present"
        shown.append((cls, r))
    # Stable chronological order, NOT grouped by state.  Grouping the new
    # arrivals first made every face jump position between eras, which
    # destroys the build-up: the point is that the grid GROWS and the eye
    # can see where.  Sorted by when each person joined, each era appends.
    shown.sort(key=lambda x: (x[1]["started"] or "", x[1]["name"]))

    out = ['<!DOCTYPE html><html><head><meta charset="utf-8">',
           f'<style>{CSS}</style></head><body>',
           '<div class="grid">']
    for cls, r in shown:
        pic = pics.get(r["name"])
        img = (f'<img src="{pic}" alt="{html.escape(r["name"])}"/>' if pic
               else '<img alt=""/>')
        out.append(
            f'<a class="p {cls}" target="_blank" '
            f'href="https://centerforopenneuroscience.org/whoweare" '
            f'title="{html.escape(r["name"])}'
            f'{" — joined " + r["started"] if r["started"] else ""}">'
            f'{img}<span>{html.escape(r["name"])}</span></a>')
    n_new = sum(1 for c, _ in shown if c == "new")
    out.append('</div>')
    out.append(f'<p class="count">{len(shown)} '
               f'{"person" if len(shown) == 1 else "people"}'
               f'{f" &middot; {n_new} new in this era" if n_new else ""}</p>')
    out.append('</body></html>')
    return "\n".join(out), len(shown), n_new


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
