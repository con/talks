# STAMPED in Practice poster

An editable **44 × 44 inch** poster about improving STAMPED research skills through the scientific work they produce.
It replaces the earlier behavioral example with the NARPS group-analysis study and presents the intended completed argument, with real example results and open slots for the remaining runs and revisions.

Open [index.html](index.html), inspect the [PDF preview](exports/pdf-preview.png), or retrieve [the PDF](https://hub.centerforopenneuroscience.org/git-annex-p2phttp/git-annex/40d344f5-0628-494e-82e4-9fab0949ed12/key/MD5E-s764394--688be8c06420100b438e1d9ea207036e.pdf).
The [completion plan](completion-plan.md) identifies the evidence needed to finish the poster and changes to data collection that can support it.
No research workers or study protocols are changed by this poster module.

## What is reproducible here

- Scientific figures: saved worker summaries and group maps, input hashes, source revisions and plotting code.
- Outcomes matrix: all three allocated iterations and four conditions, generated from a saved assessment export; open cells remain missing observations.
- Poster: local HTML/CSS, reusable institutional artwork, branded QR generation, a Pixi environment, a pinned browser dependency and PDF/layout checks.

The scientific panel illustrates [run 09](https://github.com/leej3/stamped-in-practice/tree/2ad7c466615141d11b81720ff97d61c2d7c23f73), conditional on the supplied AO86 maps.
The native-analysis variability plot has eight completed runs; it deliberately preserves differing masks and corrections.
Figure provenance is in [data/narps-2026-10-15/provenance.json](data/narps-2026-10-15/provenance.json).
The [assessment data](data/assessment-snapshot.json) retain raw statuses, external validity overrides, missingness, source hashes and separate supplementary judgments.
The exported records are sufficient to regenerate the poster's displayed numbers; full research objects remain linked in the study.

## Retrieve and build

Run from this directory:

```sh
pixi install
pixi run datalad get ../orinoco-lite/assets/con-logo-outlined.svg \
  ../orinoco-lite/assets/con-ccn-dartmouth-letterhead.svg \
  ../orinoco-lite/assets/repronim_logo.svg \
  ../orinoco-lite/assets/orinoco-qr-con.svg assets data figures exports
pixi run setup-browser
pixi run build
pixi run verify
pixi run links
```

The build uses saved local inputs and makes no requests for live study state.
`pixi run build` regenerates figures and the outcomes table, then exports the poster.
Before replacing tracked annexed outputs, run `pixi run git annex unlock assets figures exports/stamped-ai-poster.pdf exports/pdf-preview.png`.
The local `pixi.lock` is preserved on a separate environment snapshot branch, [`codex/env-stamped-poster-narps-20261015`](https://github.com/con/talks/tree/codex/env-stamped-poster-narps-20261015); it is excluded from poster history.
For an exact environment replay, retrieve that snapshot's `pixi.lock` into this directory before `pixi install --locked`.

Institutional marks are reused from the ORINOCO Lite poster.
To change QR destinations, edit `make-logo-qrs.py` and run:

```sh
pixi run python make-logo-qrs.py --check-dir exports/qr-source
```

QR regeneration additionally requires Inkscape and `rsvg-convert`.
Ordinary poster builds use the supplied QR assets and do not require those tools.

## Refresh the evidence deliberately

The assessment export reads allocation and completed judgments from an existing coordinator checkout without changing it:

```sh
pixi run python scripts/export-assessments.py \
  --study /path/to/stamped-in-practice \
  --out data/assessment-snapshot.json
```

Review the export's warnings, validity overlays and source bindings before rebuilding.
A source hash does not by itself establish publication of the original assessment; null source URLs retain that distinction.
The poster's primary judgments remain separate from duplicate and supplementary reviews.
STAMPED cells contain met / partial / unmet counts, not an overall score.
Remaining unavailable, not-checked and not-applicable items remain in the linked export.

The scientific input capture script documents the eight initial worker formats.
Extend its explicit parsers when adding new runs; do not use zero as a missing result or pool incompatible regional estimands.
See [completion-plan.md](completion-plan.md) before adding a common-support comparison.

## Verification and provenance

[HTML audit](exports/html-audit.json), [PDF audit](exports/pdf-audit.json), [link audit](exports/link-audit.json) and [visual review](exports/agent-visual-review.json) describe the current export.
The checks require one 44-inch square page, at least 24-point print text, no layout overflow, clickable PDF links, and all four QR codes decoded from PDF pixels.
These are agent checks; author review remains part of poster preparation.

The original placeholder and superseded verification reports remain in Git history at [efb1b05](https://github.com/con/talks/tree/efb1b059ffdf70d4e13f40cd5085aff6500e5269/2026-usrse/stamped-ai-study).
[source-manifest.json](source-manifest.json) records the inherited layout and artwork.

Composition and prose are CC BY-SA 4.0; scripts are Apache-2.0.
Institutional marks and external scientific inputs retain their own rights, documented in [REUSE.toml](../../REUSE.toml) and the figure provenance.
