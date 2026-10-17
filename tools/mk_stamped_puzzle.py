#!/usr/bin/env python3
"""Draw the STAMPED object as a jigsaw: one piece per tool.

The argument the picture makes: no single tool hands you a STAMPED research
object.  Each one contributes a piece -- `duct` records what a run cost,
`datalad run` records how it was made, ReproStim records what the participant
actually saw, Open Brain Consent is what makes any of it shareable at all --
and the object is what they add up to.  Which is also why adoption can be
incremental: a piece is useful on its own, and the picture is still an
improvement with gaps in it.

Pieces are laid out on a grid and tiled exactly: every internal edge is drawn
once as a tab and once as the matching blank, so the assembled square has no
seams or overlaps.  Each piece carries the STAMPED letters it supplies, in STAMPED
order; the letters repeat across pieces on purpose, because several tools feed
the same property and that is the point.  They are also deliberately generous:
`datalad run` is Tracked *and* Actionable because the record it writes is
re-runnable, `con/duct` is also Self-contained because the log it leaves holds
the command next to what the command cost, and git-annex is Tracked because
version control over the content is the whole point of it.

Every piece's name is a hyperlink to that tool's own page, and every letter
links to that principle's worked examples, so the picture is itself actionable -- which only works if the decks embed it with
`<object class="dia" data="pics/stamped-puzzle.svg">` rather than `<img>`: an
`<img>` renders the SVG but kills its links.

Writes pics/stamped-puzzle.svg -- vector, so it stays sharp in the decks and
in the PDF export -- plus the build-up stages the US-RSE deck walks through:
stamped-puzzle-frame.svg (the empty outline, "this is the shape of the thing")
and stamped-puzzle-{2016,2020,2024}.svg (the pieces that existed by the end of
that era, the rest still holes).  The stages carry the year each piece arrived
and deliberately carry *no* STAMPED letters: the properties were only named in
2026, so the letters belong to the final picture alone, which is the reveal.

The final stamped-puzzle.svg is frozen -- the MIT STAMPED deck is delivered
against it, so regenerating must leave it byte-identical.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "pics" / "stamped-puzzle.svg"
STAGE_OUT = str(HERE / "pics" / "stamped-puzzle-{}.svg")

# (tool, what piece it contributes, STAMPED letters, url, year it arrived)
#
# The year is the piece's own first appearance, not the grant or the paper:
# DataLad's first commits are 2013, the RUNCMD record 2015, HeuDiConv 2015
# the ReproIn convention that makes the piece automatic 2017, Open Brain Consent 2015, the BIDS
# paper 2016, ReproNim/containers 2019, ReproStim 2020, con/tinuous 2021,
# con/duct 2024.  Used only to decide which stage a piece is already in.
PIECES = [
    ("BIDS / NWB",            "what the files are",        "SA",  "https://bids.neuroimaging.io/", 2016),
    ("HeuDiConv / ReproIn",   "raw → standard",            "AM",  "https://github.com/nipy/heudiconv", 2017),
    ("ReproStim",             "what was actually shown",   "ST",  "https://github.com/ReproNim/reprostim", 2020),
    ("Open Brain Consent",    "permission to share",       "D",   "https://open-brain-consent.readthedocs.io/", 2015),
    ("datalad run",           "how it was made",           "TA",  "https://docs.datalad.org/en/stable/generated/man/datalad-run.html", 2015),
    ("con/duct",              "what it cost",              "STA", "https://github.com/con/duct", 2024),
    ("DataLad / git-annex",   "versioned, composable",     "TMD", "https://www.datalad.org/", 2013),
    ("ReproNim/containers",   "the environment travels",   "PE",  "https://github.com/ReproNim/containers", 2019),
    ("con/tinuous + CI",      "nobody has to remember",    "ST",  "https://github.com/con/tinuous", 2021),
]

# Each stage shows the pieces that existed by the end of that era; the ones new
# since the previous stage get the same red accent the acknowledgement grids use
# for "new in this era", so the two build-ups read as one convention.
STAGES = [2016, 2020, 2024]
GHOST_FILL, GHOST_STROKE = "#faf7f2", "#c6b9a3"
ACCENT = "#c0392b"

COLS, ROWS = 3, 3
W, H = 240, 152          # piece size
PAD = 32                 # room for tabs that stick out of the square
DEPTH = 26               # how far a tab sticks out, in px -- NOT a fraction
                         # of the edge, or the tab on a 240px-wide edge would
                         # cut a third of the way into a 152px-tall piece and
                         # swallow the letter row
FILL = ["#fdf6ec", "#f7ece0"]      # two beiges, checkerboard, theme-matched
STROKE = "#b9a88f"
LETTER = {"S": "#2e7d32", "T": "#c62828", "A": "#1565c0", "M": "#6a1b9a",
          "P": "#ef6c00", "E": "#00838f", "D": "#283593"}
LETTER_NAME = {"S": "Self-contained", "T": "Tracked", "A": "Actionable",
               "M": "Modular", "P": "Portable", "E": "Ephemeral",
               "D": "Distributable"}
# Each letter links to that principle's worked examples, so the picture answers
# "what does Tracked actually mean" without the slide having to.
EXAMPLES = "https://examples.stamped-principles.org/stamped_principles/{}/"

# Tab direction for every internal edge, fixed rather than random so the file
# is reproducible: regenerating must not produce a gratuitous diff.
VTAB = [[1, -1], [-1, 1], [1, -1]]      # [row][internal column edge]
HTAB = [[1, -1, 1], [-1, 1, -1]]        # [internal row edge][column]


def tab(x0, y0, x1, y1, d):
    """Edge from (x0,y0) to (x1,y1); d=0 straight, else a jigsaw tab.

    Built in edge-local coordinates -- u along the edge, p perpendicular --
    so one definition serves all four orientations and the tab on one piece is
    the exact mirror of the blank on its neighbour.
    """
    if not d:
        return f"L {x1:.1f} {y1:.1f} "
    dx, dy = x1 - x0, y1 - y0
    L = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / L, dy / L
    px, py = -uy * d, ux * d        # perpendicular, flipped by tab direction

    def P(a, b):
        """a: fraction along the edge.  b: fraction of DEPTH, perpendicular."""
        return (f"{x0 + ux * a * L + px * b * DEPTH:.1f} "
                f"{y0 + uy * a * L + py * b * DEPTH:.1f}")

    return (
        f"L {P(0.40, 0)} "
        f"C {P(0.47, 0.1)} {P(0.33, 0.8)} {P(0.44, 1.0)} "
        f"C {P(0.50, 1.3)} {P(0.50, 1.3)} {P(0.56, 1.0)} "
        f"C {P(0.67, 0.8)} {P(0.53, 0.1)} {P(0.60, 0)} "
        f"L {P(1.0, 0)} "
    )


def piece_path(c, r):
    x, y = PAD + c * W, PAD + r * H
    top = 0 if r == 0 else -HTAB[r - 1][c]
    right = 0 if c == COLS - 1 else VTAB[r][c]
    bottom = 0 if r == ROWS - 1 else HTAB[r][c]
    left = 0 if c == 0 else -VTAB[r][c - 1]
    return ("M {} {} ".format(x, y)
            + tab(x, y, x + W, y, top)
            + tab(x + W, y, x + W, y + H, right)
            + tab(x + W, y + H, x, y + H, bottom)
            + tab(x, y + H, x, y, left)
            + "Z")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(as_of=None, since=None, letters=True, years=False):
    """One SVG.  as_of=None draws every piece built; otherwise pieces that
    arrived after `as_of` are drawn as holes, and those newer than `since` get
    the red "new in this era" accent."""
    sw, sh = COLS * W + 2 * PAD, ROWS * H + 2 * PAD
    title = ("The STAMPED object, one piece per tool" if as_of is None
             else f"The object as of {as_of} -- the holes are what came later")
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        # 100% rather than {sw}x{sh}: embedded with <object>, the root's own
        # width/height would win over the element's box and the picture would
        # sit undersized in its top-left corner.  viewBox keeps the aspect.
        f'viewBox="0 0 {sw} {sh}" width="100%" height="100%" '
        f'font-family="Source Sans Pro,Helvetica,sans-serif">',
        f"<title>{title}</title>",
        # Link colours are reveal.js's beige theme (--r-link-color and its
        # hover), so a linked name reads as a link on the slide.
        "<style>"
        "a text.name { fill: #8b743d; text-decoration: underline; cursor: pointer; }"
        "a:hover text.name { fill: #b39753; }"
        # The letters keep their STAMPED colours -- they are the colour key for
        # the whole deck -- so a dotted rule is what marks them as links.
        "a text.letter { cursor: pointer; text-decoration: underline dotted; }"
        "a:hover text.letter { text-decoration: underline; }"
        "</style>",
    ]
    # Holes first, built pieces over them: a neighbouring hole drawn later
    # would overdraw the accent edge of the piece that was just added.
    for i, (_, _, _, _, year) in enumerate(PIECES):
        if as_of is not None and year > as_of:
            # The shape still reads, so the audience sees the object is not
            # finished rather than seeing a smaller object.
            out.append(f'<path d="{piece_path(i % COLS, i // COLS)}" '
                       f'fill="{GHOST_FILL}" stroke="{GHOST_STROKE}" '
                       f'stroke-width="1.6" stroke-dasharray="5 5"/>')
    for i, (tool, what, letters_, url, year) in enumerate(PIECES):
        c, r = i % COLS, i // COLS
        cx, cy = PAD + c * W + W / 2, PAD + r * H + H / 2
        if as_of is not None and year > as_of:
            continue
        new_here = since is not None and year > since
        out.append(f'<g><title>{esc(tool)} — {esc(what)}</title>')
        out.append(f'<path d="{piece_path(c, r)}" fill="{FILL[(c + r) % 2]}" '
                   f'stroke="{ACCENT if new_here else STROKE}" '
                   f'stroke-width="{2.8 if new_here else 1.6}"/>')
        # Only the name is the link, not the whole piece: a piece-sized hit box
        # would make the letters and the caption look clickable too.  Both href
        # spellings, since the file is read by SVG1.1 and SVG2 consumers alike.
        out.append(f'<a href="{esc(url)}" xlink:href="{esc(url)}" target="_blank">'
                   f'<text class="name" x="{cx:.0f}" y="{cy - 20:.0f}" '
                   f'text-anchor="middle" font-size="19" font-weight="700">'
                   f'{esc(tool)}</text></a>')
        out.append(f'<text x="{cx:.0f}" y="{cy + 4:.0f}" text-anchor="middle" '
                   f'font-size="15" fill="#666">{esc(what)}</text>')
        if years:
            out.append(f'<text x="{cx:.0f}" y="{cy + 34:.0f}" text-anchor="middle" '
                       f'font-size="17" font-weight="700" '
                       f'fill="{ACCENT if new_here else "#8a7f6d"}">{year}</text>')
        if letters:
            # the letters this piece supplies, spelled out in STAMPED's colours
            n = len(letters_)
            for j, ch in enumerate(letters_):
                lx = cx + (j - (n - 1) / 2) * 26
                lurl = EXAMPLES.format(ch.lower())
                out.append(f'<a href="{lurl}" xlink:href="{lurl}" target="_blank">'
                           f'<title>{ch} — {LETTER_NAME[ch]}: worked examples</title>'
                           f'<text class="letter" x="{lx:.0f}" y="{cy + 36:.0f}" '
                           f'text-anchor="middle" font-size="25" font-weight="700" '
                           f'fill="{LETTER[ch]}">{ch}</text></a>')
        out.append("</g>")
    out.append("</svg>")
    return "\n".join(out) + "\n", sw, sh


def main():
    svg, sw, sh = render()
    OUT.write_text(svg)
    print(f"wrote {OUT.relative_to(HERE)}  ({sw}x{sh}, {len(PIECES)} pieces)")
    # the empty frame: the shape of the object before any of it was built
    frame = pathlib.Path(STAGE_OUT.format("frame"))
    frame.write_text(render(as_of=0)[0])
    print(f"wrote {frame.relative_to(HERE)}  (outline only)")
    for n, year in enumerate(STAGES):
        path = pathlib.Path(STAGE_OUT.format(year))
        path.write_text(render(as_of=year,
                               since=STAGES[n - 1] if n else 0,
                               letters=False, years=True)[0])
        built = sum(1 for p in PIECES if p[4] <= year)
        print(f"wrote {path.relative_to(HERE)}  ({built}/{len(PIECES)} pieces)")


if __name__ == "__main__":
    main()
