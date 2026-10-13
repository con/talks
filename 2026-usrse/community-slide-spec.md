# Community Slide Spec: "CON and the broader community"

## Purpose

A reusable reveal.js slide (or exportable PNG) showing who CON works with, in a tiered
visual that communicates both the names of individuals and the *scale* of the broader
communities they represent. Used in talks to make the "collaboration" message visceral —
real faces, not an org chart.

The slide is intentionally **non-exhaustive at the top and deliberately massive at the bottom**:
the mass-figure tier is what makes the slide land. The audience should feel the crowd.

---

## Separation of concerns

```
community-slide-data.yaml   — the canonical data (who, which tier, community memberships)
community-slide-render.py   — generates the slide image (SVG or PNG) from the YAML
pics/community-slide.svg    — generated output, committed to the repo
```

The YAML is edited by humans; the script is re-run to regenerate the image; the slide
references the image with `<img data-src="pics/community-slide.svg">`. No manual pixel
pushing.

---

## Tier structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  TIER 0 — Apex (1 person)                                                   │
│  ● Yaroslav O. Halchenko  (large circle, center)                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  TIER 1 — CON team  (7 circles, medium-large)                               │
│  James V. Haxby | Isaac To | Austin Macdonald | Cody Baker                 │
│  John Lee | Vadim Melnik                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  TIER 2 — Collaborators  (8 circles, medium)                                │
│  Michael Hanke | Satrajit Ghosh | Chris Markiewicz | Jean-Baptiste Poline  │
│  David N. Kennedy | Joey Hess | Adina Wagner | Franco Pestilli              │
├─────────────────────────────────────────────────────────────────────────────┤
│  TIER 3 — Emeritus  (14 circles, small)                                     │
│  Matteo Visconti di Oleggio Castello | Samuel Nastase | Nikolaas Oosterhof  │
│  Matthew Brett | Kyle Meyer | Benjamin Poldrack | Horea-Ioan Ioanas         │
│  Vanessa Sochat | Soichi Hayashi | Oliver Contier | Jason Gors              │
│  Gergana Alteva | Chris Cheng | John Wodder                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  TIER 4 — Communities  (mass silhouettes + labels, smallest unit figures)   │
│  [BIDS ~600] [ReproNim ~200] [Debian ~1000 DDs] [DataLad] [DANDI/NWB]      │
└─────────────────────────────────────────────────────────────────────────────┘
```

Circle sizes (relative):
- Tier 0: 80 px diameter
- Tier 1: 60 px
- Tier 2: 48 px
- Tier 3: 36 px
- Tier 4: silhouette units ~12 px each, packed in labeled clusters

---

## Data model (community-slide-data.yaml)

```yaml
people:
  - name: Yaroslav O. Halchenko
    tier: 0
    role: Founding Director
    photo: https://centerforopenneuroscience.org/whoweare#yaroslav_o_halchenko_
    communities: [CON, BIDS, ReproNim, Debian, DataLad, DANDI]

  # Tier 1 — CON team
  - name: James V. Haxby
    tier: 1
    role: Co-Director
    photo: https://centerforopenneuroscience.org/whoweare
    communities: [CON]

  - name: Isaac To
    tier: 1
    role: Software Developer
    photo: https://centerforopenneuroscience.org/whoweare
    communities: [CON, DataLad, DANDI]

  - name: Austin Macdonald
    tier: 1
    role: Software Engineer
    photo: https://centerforopenneuroscience.org/whoweare
    communities: [CON, STAMPED, BIDS]

  - name: Cody Baker
    tier: 1
    role: Research Software Engineer
    photo: https://centerforopenneuroscience.org/whoweare
    communities: [CON, NWB, DANDI, STAMPED]

  - name: John Lee
    tier: 1
    role: Research Software Engineer
    photo: https://centerforopenneuroscience.org/whoweare
    communities: [CON, ORINOCO]

  - name: Vadim Melnik
    tier: 1
    role: Software Engineer
    photo: https://centerforopenneuroscience.org/whoweare
    communities: [CON]

  # Tier 2 — Collaborators
  - name: Michael Hanke
    tier: 2
    role: INM-7, Jülich / Magdeburg
    photo: ~  # not on CON site; use INM-7 or public photo
    communities: [DataLad, BIDS, ORINOCO]

  - name: Satrajit Ghosh
    tier: 2
    role: MIT / Harvard Medical School
    photo: ~
    communities: [ReproNim, BIDS, DANDI]

  - name: Chris Markiewicz
    tier: 2
    role: Stanford, Poldrack Lab
    photo: ~
    communities: [BIDS, ReproNim]

  - name: Jean-Baptiste Poline
    tier: 2
    role: McGill University
    photo: ~
    communities: [ReproNim, BIDS]

  - name: David N. Kennedy
    tier: 2
    role: UMass Chan Medical School
    photo: ~
    communities: [ReproNim, BIDS]

  - name: Joey Hess
    tier: 2
    role: Independent / git-annex
    photo: ~
    communities: [Debian, DataLad]

  - name: Adina Wagner
    tier: 2
    role: INM-7, Jülich
    photo: ~
    communities: [DataLad]

  - name: Franco Pestilli
    tier: 2
    role: UT Austin
    photo: ~
    communities: [BIDS, DANDI]

  # Tier 3 — Emeritus (names only; photos optional)
  - name: Matteo Visconti di Oleggio Castello
    tier: 3
  - name: Samuel Nastase
    tier: 3
  - name: Nikolaas Oosterhof
    tier: 3
  - name: Matthew Brett
    tier: 3
  - name: Kyle Meyer
    tier: 3
  - name: Benjamin Poldrack
    tier: 3
  - name: Horea-Ioan Ioanas
    tier: 3
  - name: Vanessa Sochat
    tier: 3
  - name: Soichi Hayashi
    tier: 3
  - name: Oliver Contier
    tier: 3
  - name: Jason Gors
    tier: 3
  - name: Gergana Alteva
    tier: 3
  - name: Chris Cheng
    tier: 3
  - name: John Wodder
    tier: 3

communities:
  - name: BIDS
    approx_size: 600
    color: "#4a90d9"
    tier: 4

  - name: ReproNim
    approx_size: 200
    color: "#7b68ee"
    tier: 4

  - name: Debian
    approx_size: 1000   # ~1000 Debian Developers; broader community much larger
    color: "#d70751"
    tier: 4

  - name: DataLad
    approx_size: 150
    color: "#f5a623"
    tier: 4

  - name: DANDI / NWB
    approx_size: 300
    color: "#2ecc71"
    tier: 4

  - name: NeuroDebian users
    approx_size: 5000   # estimated active users
    color: "#e67e22"
    tier: 4
```

---

## Visual design notes

### Individual circles (Tiers 0–3)
- Circular crop of headshot photo, border in tier accent color (or neutral grey).
- On hover / on click in a browser: tooltip with name + role + community badges.
- For Tier 3, show name below or on hover only (too small for always-visible labels).
- Source photos: download from centerforopenneuroscience.org/whoweare for Tier 0-1;
  for Tier 2-3 find public photos (conference bios, GitHub avatars, lab pages).
  Store at `pics/people/<firstname-lastname>.jpg` (square crop, min 200×200 px).

### Mass figures (Tier 4)
- Each community rendered as a grid/cluster of small person silhouettes.
- Silhouette count is `min(approx_size, MAX_ICONS)` where MAX_ICONS scales with community
  size (e.g., log-scale: 600 BIDS → 30 icons; 5000 NeuroDebian → 60 icons).
- Label below the cluster: "BIDS (~600 contributors)" in community color.
- Use a simple SVG person path (or Unicode 🧑 at 10pt) repeated in a tight grid.
- The visual effect: the bottom quarter of the slide is a dense crowd of tiny figures,
  making the scale difference between "CON team of 7" and "community of thousands" visceral.

### Layout options
Two candidate layouts — choose one before implementation:

**Option A — Horizontal tiers (pyramid)**
Each tier is a centered row. Rows grow wider with each tier. Bottom tier spans full width.
Simple flexbox or SVG `<g>` per row. Familiar org-chart feeling.

**Option B — Concentric rings**
Yaroslav at center; CON team in a tight inner ring; collaborators in a wider ring;
emeritus in an outer ring; mass silhouettes fill the corners/background.
More visually striking; harder to label; better for a "network" metaphor.

Recommendation: **Option A** for a slide where names must be legible; Option B for a
pure "visual impact" variant that invites closer inspection.

---

## Rendering script sketch (community-slide-render.py)

```python
#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Generated with Claude Code 2.1.273 / Claude Sonnet 4.6
#
# Usage: python community-slide-render.py community-slide-data.yaml pics/community-slide.svg

import sys
import yaml
from pathlib import Path

SLIDE_W, SLIDE_H = 1400, 1050   # matches reveal.js canvas

TIER_CIRCLE_D  = {0: 80, 1: 60, 2: 48, 3: 36}
TIER_LABEL_SZ  = {0: 13, 1: 11, 2: 10, 3:  8}
TIER_Y_CENTERS = {0: 80, 1: 190, 2: 310, 3: 420}  # adjust after sizing
TIER_4_TOP     = 510

MAX_ICONS_BY_SIZE = lambda n: max(8, min(80, int(10 * (n ** 0.4))))

# TODO: implement SVG generation
# Each tier: compute x positions to center the row, emit <image> or <circle> + <text>
# Tier 4: emit packed <path d="M..."/> person silhouettes in labeled bounding boxes
# Output: well-formed SVG at SLIDE_W × SLIDE_H

def main(data_path: str, out_path: str):
    data = yaml.safe_load(Path(data_path).read_text())
    # ... implementation ...
    print(f"TODO: generate {out_path} from {data_path}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
```

---

## Reuse in talks

To include in a reveal.js deck:

```html
<section>
  <h2>CON — and the community we work with</h2>
  <img data-src="pics/community-slide.svg"
       style="width:100%; height:85vh; object-fit:contain;">
</section>
```

For the US-RSE talk, this slide appears in **Act III** immediately after "You are alone."
No speaker notes needed — let the faces and the crowd density carry the message.
The speaker may say: "This is what 'together' actually looks like."

---

## TODOs before the slide can be rendered

- [ ] Download headshots for Tier 0–1 from centerforopenneuroscience.org/whoweare
      → store at `pics/people/<firstname-lastname>.jpg` (square, ≥200 px)
- [ ] Find public headshots for Tier 2 collaborators (conference bios, GitHub avatars)
- [ ] Decide: horizontal tiers (Option A) vs. concentric rings (Option B)
- [ ] Implement `community-slide-render.py` (SVG output preferred for scalability)
- [ ] Tune TIER_Y_CENTERS and icon density after a first render
- [ ] Add DebConf / BIDS meeting / distribits group photos as *separate* "community moment"
      slides (these are distinct from this overview slide — they show real events)
