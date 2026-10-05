# Orinoco Lite poster

The editable source is [orinoco-lite-poster.svg](orinoco-lite-poster.svg).
It preserves the title and presenter order of the [submitted abstract](orinoco-lite-poster-draft.md).
The draft leads with the deployment comparison requested by the reviewers, followed by the GitHub curation design, observed results and next evaluation steps.

## Editing and export

Open the SVG in Inkscape or another SVG editor.
The title, comparison, diagram, results and footer have named layers.
Text remains editable text, and the CON logo and QR code are embedded vectors with no linked image dependencies.
The SVG is kept in ordinary Git so GitHub reviewers and a fresh clone can read the complete source without fetching Annex content.

Use the text tool to revise text and adjust its line breaks.
The font is Arial with Helvetica and generic sans-serif fallbacks; check the layout after font substitution or substantial text changes.
The provisional canvas is **48 inches wide by 36 inches high**.
This is a draft choice, not a verified conference mounting requirement; confirm the accepted-presenter instructions before printing.

Export a PDF in the editor, or run from this directory:

```bash
rsvg-convert --format pdf --output orinoco-lite-poster.pdf \
  orinoco-lite-poster.svg
```

The PDF is a generated preview and follows this directory's existing PDF ignore rule.
The initial export was checked as one 48-by-36-inch page with searchable text and visually inspected for layout.
The QR code points to the public Orinoco Lite development repository.

## Results and claim boundaries

The approximately 390-word poster describes a development case study, using a **9 September 2026** snapshot:

- The CON downstream at [commit `ee2e568`](https://github.com/con/dev-centerforopenneuroscience.org/commit/ee2e56839f5b3e0ffb42437a3918387b95ed2d75) selects package `0.3.0rc5` and template `v0.3.0rc3`.
- Fresh frozen validation/build checks reported **224 canonical records** and **193 projected pages**.
  These are counts of different artifacts, not a conversion ratio or a usability result.
- Its [validation](https://github.com/con/dev-centerforopenneuroscience.org/actions/runs/34319183393) and [Pages deployment](https://github.com/con/dev-centerforopenneuroscience.org/actions/runs/34319183434) succeeded.
- The operating comparison follows the [ORINOCO components](https://hub.psychoinformatics.de/orinoco), [metadata service](https://hub.psychoinformatics.de/orinoco/dump-things-service), and [Orinoco Lite design charter](https://github.com/ORINOCO-Lite/orinoco-lite-dev/blob/9417f90cb8989555cf71f41d9f982970c8402828/docs/project-design.md).

The curation diagram describes the intended integrated workflow.
At the snapshot, CON's automated source-import/review workflow was not yet wired into the default branch, and complete authenticated curation had not been exercised in this review.
The poster marks CON integration and App hardening as ongoing work.
It does not assert enforced GitHub branch protections or a completed security assessment of the private deployment configuration.

Broader reuse is explicitly future work: the review did not demonstrate a CON report/CV workflow or measure editing time, error reduction, maintenance cost or independent adoption.
Before finalizing the poster, update the snapshot if the release or dataset changes and review the text, acknowledgments and physical dimensions.

## Attribution

The embedded CON logo comes from [the existing vector artwork](../pics/con-logo_blue_big.svg).
The poster follows the talks repository's CC BY-SA 4.0 license and acknowledges the ORINOCO and DataLad contributors named in the abstract.
The footer discloses OpenAI Codex assistance with draft text, diagram and layout and retains the draft's author-review status.
