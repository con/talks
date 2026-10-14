# STAMPED in Practice: initial study poster

[stamped-ai-poster-initial.svg](stamped-ai-poster-initial.svg) is an editable **44 × 44 inch**
initial poster source with live text and a `3168 × 3168` viewBox.
The [PNG preview](stamped-ai-poster-initial-preview.png) is for screen review.
This layout contains no experiment findings and is awaiting author review.

ABCD data access was not obtained, so the planned scientific result has not been reproduced.
The proposed public-data studies do not resolve that controlled-data access limitation.
The seven-property table distinguishes implementation examples from **PENDING** evidence, effort,
failures, tradeoffs, and gaps.
The study question, dataset, sample size, and metric also remain pending; no general benefit from
skills is demonstrated.

Author order provisionally follows the conference program: John A. Lee, Austin Macdonald, Cody C.
Baker, and Yaroslav O. Halchenko.
Confirm the order before publication.
The descriptive subtitle is provisional; the submitted title remains in the
[accepted abstract](../stamped-abcd-poster-draft.md).

## Edit and regenerate

Edit [build_initial_poster.py](build_initial_poster.py) to change the content or layout
reproducibly, then regenerate the SVG.
The SVG can also be edited directly in a vector editor, but regeneration overwrites those direct
edits.
From this directory:

```bash
python3 build_initial_poster.py
uv run --with cairosvg cairosvg stamped-ai-poster-initial.svg \
  --output-width 1584 --output-height 1584 \
  --output stamped-ai-poster-initial-preview.png
```

The builder uses the Python standard library; preview rendering needs CairoSVG and the Cairo system
library.
With dependencies already cached, add `--offline` to `uv run`.
On Apple Silicon with Homebrew Cairo, prefix the rendering command with
`DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib` if the library is not found.
Local font selection can change text rendering or omit arrow glyphs; visually check a regenerated
preview against the supplied PNG.
The SVG retains its physical dimensions regardless of preview resolution.
Licensing follows the repository's existing [REUSE.toml](../../REUSE.toml) annotations.
