# STAMPED in Practice poster

An editable **44 × 44 inch** poster about improving STAMPED research skills through the scientific work they produce.
The blue banner states the experiment; the left column introduces STAMPED, the centre shows the NARPS scientific example, and the right connects condition-level outcomes to the study's research objects.

Open [index.html](index.html), inspect the [PDF preview](exports/pdf-preview.png), or retrieve [the PDF](https://hub.centerforopenneuroscience.org/git-annex-p2phttp/git-annex/40d344f5-0628-494e-82e4-9fab0949ed12/key/MD5E-s838462--d8ef321e58eda856e01de66965ab01d9.pdf).
The [completion plan](completion-plan.md) identifies the evidence needed to fill the pooled comparison and guide subsequent data collection.

## Scientific figures belong to the benchmark

The [benchmark figure workflow](https://github.com/leej3/stamped-in-practice/blob/codex/stamped-poster-analysis/scripts/POSTER-FIGURES.md) contains the scientific generators, frozen inputs, root Pixi environment, derived results and provenance.
This poster retains display copies and a [source binding](figures/benchmark-source.json), including the exact benchmark revision and SHA-256 values.
Reader-facing links open named branches; exact revisions remain in the provenance.

The group map illustrates development run 09, conditional on the supplied AO86 participant maps.
The spatial comparison includes twelve development runs, three per condition, on shared coverage.
Group t maps agree to numerical precision; native correction choices account for the displayed difference in positive extent.
These development examples remain useful while the compact outcomes table reserves space for eligible benchmark iterations pooled by condition.
No comparison averages have been inserted yet.

## Retrieve and build

Run from this directory:

```sh
pixi install
pixi run datalad get ../orinoco-lite/assets/con-logo-outlined.svg \
  ../orinoco-lite/assets/con-ccn-dartmouth-letterhead.svg \
  ../orinoco-lite/assets/repronim_logo.svg \
  ../orinoco-lite/assets/orinoco-qr-con.svg assets figures exports
pixi run setup-browser
pixi run build
pixi run verify
pixi run links
```

`pixi run build` verifies the scientific display copies against their binding, then exports the local HTML/CSS poster. It does not regenerate scientific analyses or request live study data. Before replacing annexed exports, run `pixi run git annex unlock exports/stamped-ai-poster.pdf exports/pdf-preview.png`. The exact validated `pixi.lock` is preserved separately on [`codex/env-stamped-poster-contained-20261016`](https://github.com/con/talks/tree/codex/env-stamped-poster-contained-20261016). For an exact environment replay, retrieve its `2026-usrse/stamped-ai-study/pixi.lock` here before `pixi install --locked`.

To import a new committed benchmark export:

```sh
pixi run git annex unlock figures
pixi run python scripts/import-benchmark-figures.py --benchmark /path/to/stamped-in-practice
pixi run build
```

The importer checks every source recorded in the benchmark export manifest and requires those files to match its committed revision.
Scientific regeneration and input refresh happen through the benchmark's documented root tasks.
The historical poster-side scientific pipeline remains in Git history; it is no longer a second source of truth.

Institutional marks are reused from the ORINOCO Lite poster.
To change QR destinations, edit `make-logo-qrs.py` and run `pixi run python make-logo-qrs.py --check-dir exports/qr-source`.
QR regeneration additionally requires Inkscape and `rsvg-convert`; ordinary builds use the supplied QR assets.

## Verification and provenance

[HTML audit](exports/html-audit.json), [PDF audit](exports/pdf-audit.json), [link audit](exports/link-audit.json), [retrieval audit](exports/retrieval-audit.json) and [visual review](exports/agent-visual-review.json) describe the current export.
Checks require one 44-inch square page, at least 24-point print text, no layout overflow, clickable PDF links, and four QR codes decoded from PDF pixels.
These are agent checks; author review remains part of poster preparation.

Earlier designs remain in the [poster history](https://github.com/con/talks/commits/codex/stamped-example-poster/2026-usrse/stamped-ai-study).
[source-manifest.json](source-manifest.json) records the inherited layout and artwork.
Composition and prose are CC BY-SA 4.0; scripts are Apache-2.0.
Institutional marks and external scientific inputs retain their own rights, documented in [REUSE.toml](../../REUSE.toml) and the benchmark provenance.
