# STAMPED in Practice poster

An editable **44 × 44 inch** poster about improving STAMPED research skills through the scientific work they produce.
It replaces the earlier behavioral example with the NARPS group-analysis study and presents the intended completed argument, with real example results and open slots for the remaining runs and revisions.

Open [index.html](index.html), inspect the [PDF preview](exports/pdf-preview.png), or retrieve [the PDF](https://hub.centerforopenneuroscience.org/git-annex-p2phttp/git-annex/40d344f5-0628-494e-82e4-9fab0949ed12/key/MD5E-s892880--c9c8152542986d34d271bc44900ab481.pdf).
The [completion plan](completion-plan.md) identifies the evidence needed to finish the poster and changes to data collection that can support it.
No research workers or study protocols are changed by this poster module.

## What is reproducible here

- Scientific figures: saved worker summaries and group maps, input hashes, source revisions and plotting code.
- Outcomes matrix: all three allocated iterations and four conditions, generated from a saved assessment export; open cells remain missing observations.
- Poster: local HTML/CSS, reusable institutional artwork, branded QR generation, a Pixi environment, a pinned browser dependency and PDF/layout checks.

The scientific panel illustrates [run 09](https://github.com/leej3/stamped-in-practice/tree/codex/narps-r1-09), conditional on the supplied AO86 maps.
The spatial comparison shows corrected-positive agreement across all twelve first-iteration runs, three per condition, on shared coverage.
Group t maps agree to numerical precision; native correction choices account for the displayed difference in positive extent.
Illustrative-map provenance is in [data/narps-2026-10-15/provenance.json](data/narps-2026-10-15/provenance.json).
Spatial source identities, coverage rules and display choices are in [data/narps-spatial/provenance.json](data/narps-spatial/provenance.json); [derived-summary.json](data/narps-spatial/derived-summary.json) contains the regenerated measurements.
The [assessment data](data/assessment-snapshot.json) retain raw statuses, external validity overrides, missingness, source hashes and separate supplementary judgments.
The exported records are sufficient to regenerate the poster's displayed numbers; full research objects remain linked in the study.
Reader-facing links open named branches; exact source revisions and hashes remain in the provenance records.

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
The local `pixi.lock` is preserved on a separate environment snapshot branch, [`codex/env-stamped-poster-spatial-20261016`](https://github.com/con/talks/tree/codex/env-stamped-poster-spatial-20261016); it is excluded from poster history.
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

The original input capture script preserves the illustrative analysis and its initial source summaries.
The spatial extraction separately records all twelve native masks, t maps and corrected-positive maps.
Do not use zero as a missing result or pool incompatible regional estimands.
See [completion-plan.md](completion-plan.md) before extending the spatial comparison to later iterations.

To refresh spatial inputs from completed worker checkouts and their recorded assignments:

```sh
pixi run python scripts/extract-narps-spatial.py \
  --workers-root /path/to/stamped-in-practice-workers/codex \
  --capture-root /path/to/narps-v1
pixi run spatial-map
```

The compact NPZ preserves all twelve native support masks and corrected-positive maps, together with losslessly deduplicated t values on shared support and anatomical context.
Extraction checks participant-map identities, source cleanliness, native geometry, correction semantics, assignment and published result counts.
The renderer verifies the frozen input hash and recomputes both agreement maps and the numerical summary offline.

## Verification and provenance

[HTML audit](exports/html-audit.json), [PDF audit](exports/pdf-audit.json), [link audit](exports/link-audit.json) and [visual review](exports/agent-visual-review.json) describe the current export.
The checks require one 44-inch square page, at least 24-point print text, no layout overflow, clickable PDF links, and all four QR codes decoded from PDF pixels.
These are agent checks; author review remains part of poster preparation.

Earlier designs and verification reports remain in the [poster history](https://github.com/con/talks/commits/codex/stamped-example-poster/2026-usrse/stamped-ai-study).
[source-manifest.json](source-manifest.json) records the inherited layout and artwork.

Composition and prose are CC BY-SA 4.0; scripts are Apache-2.0.
Institutional marks and external scientific inputs retain their own rights, documented in [REUSE.toml](../../REUSE.toml) and the figure provenance.
