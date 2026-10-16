# Build and verify the poster

Start with the [poster introduction](README.md) for downloads and interpretation.
This page covers editing, exact scientific sources, environment replay and verification.

## Scientific sources and display copies

The [benchmark figure workflow](https://github.com/leej3/stamped-in-practice/blob/codex/stamped-poster-analysis/scripts/POSTER-FIGURES.md) contains the scientific generators, frozen inputs, root Pixi environment, derived results and provenance.
This poster retains display copies and a [source binding](figures/benchmark-source.json), including the exact benchmark revision and SHA-256 values.
Overview links begin with guides on `main`; direct technical links open the named research branches.
The guides explain their role, while exact source revisions remain in the provenance.

The group map shows formal round-two run 09: a one-sample group test on 54 participant maps, 9,999 sign-flip permutations and whole-brain FWE correction.
The spatial comparison uses all 48 analyses from rounds two and three, twelve per condition, on 168,285 shared tested voxels.
Every run retains its native corrected decisions and coverage; the source repository preserves masks, scientific code, reports and capture identities.

The compact outcomes table pools the retained operational assessments from all three rounds: 72 original research runs, 70 primary scientific judgments and 68 valid primary checklists.
Native replay counts distinguish full selected-output matches from observed executions.
The [benchmark summary](https://github.com/leej3/stamped-in-practice/tree/codex/stamped-poster-analysis/experiments/retained-round-reporting/pooled) retains all grades, denominators, partial matches and separate round summaries.
The [outcomes](data/benchmark-outcomes.json), [checklist index](data/benchmark-checklists.json) and [source binding](data/benchmark-outcomes-source.json) identify the exact imported reports.
The table’s linked checklist scores average each valid primary response’s met-item count divided by all 31 checklist items, matching the app’s denominator.
Each condition mean links to its individual filled checklists, with exact original JSON responses alongside them.
The app rounds individual scores to integers; pooled means use the unrounded fractions and display one decimal.
Four unavailable checklists remain unscored; their retained responses are accessible with exclusion reasons.
The complete table includes 21 observed native reruns: 13 full selected-output matches, five partial matches and three nonzero exits.
Round-specific results and every original judgment remain retrievable.

The progression chart shows each condition across the three rounds, with separate panels for scientific adequacy and mean evaluated checklist items met.
Each point summarizes designated primary judgments from six assigned fresh workers; science has 5–6 available judgments and the checklist has 4–6 per condition and round.
Scientific proportions have 95% Wilson intervals, conditional on independent runs with a common within-group probability.
The checklist panel shows each available run, connected means and ± one sample standard deviation, describing between-run spread rather than uncertainty in a mean.
Its denominator is evaluated items (met + partial + unmet), excluding unchecked and not-applicable items; this differs from the table’s all-31-item app measure.
The chart uses the same retained judgments as the table, with exact denominators in the linked round data.
Neither bar type accounts for missing judgments, assessor uncertainty, shared infrastructure or the adaptive protocol; these are descriptive comparisons, not causal effects.
Only the STAMPED condition receives the revised research-skill bundle; the other conditions retain their assigned instructions.
The baseline label is “No supplied research skills”: common task instructions, software resources and runtime system skills remain available to all conditions.

The seven concise definitions follow the [STAMPED paper](https://github.com/stamped-principles/stamped-paper/blob/main/main.tex), including component and change provenance, versioned environment specifications, persistent retrieval and explicit licenses.
A spectrum note distinguishes incremental improvement from a single compliance threshold.

The poster focuses on the scientific results and skill-development experiment.
Original reporting failures, additive extraction corrections and infrastructure diagnostics remain in the benchmark's linked reporting record.
The final guidance example explicitly identifies the STAMPED research-loop skill's environment-recipe clarification and the condition that received it.
The methodological lesson pairs assessment without prescribing with bounded repairs that let the experiment advance.

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

`pixi run build` verifies the scientific display copies and outcome table against their bindings, then exports the local HTML/CSS poster. It does not regenerate scientific analyses or request live study data. Before replacing annexed exports, run `pixi run git annex unlock exports/stamped-ai-poster.pdf exports/pdf-preview.png`. The exact validated `pixi.lock` is preserved separately on [`codex/env-poster-uncertainty-20261016`](https://github.com/con/talks/tree/codex/env-poster-uncertainty-20261016). For an exact environment replay, retrieve its `2026-usrse/stamped-ai-study/pixi.lock` here before `pixi install --locked`.

To import a new committed benchmark export:

```sh
pixi run git annex unlock figures
pixi run python scripts/import-benchmark-figures.py --benchmark /path/to/stamped-in-practice
pixi run python scripts/import-benchmark-outcomes.py --benchmark /path/to/stamped-in-practice
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
The retrieval audit records fresh full-payload checks for the current PDF, preview and changed figure assets, alongside earlier checks for unchanged assets.
Checks require one 44-inch square page, at least 24-point print text, no layout overflow, clickable PDF links, and four QR codes decoded from PDF pixels.
These are agent checks; author review remains part of poster preparation.

Earlier designs remain in the [poster history](https://github.com/con/talks/commits/codex/stamped-example-poster/2026-usrse/stamped-ai-study).
[source-manifest.json](source-manifest.json) records the inherited layout and artwork.
Composition and prose are CC BY-SA 4.0; scripts are Apache-2.0.
Institutional marks and external scientific inputs retain their own rights, documented in [REUSE.toml](../../REUSE.toml) and the benchmark provenance.
