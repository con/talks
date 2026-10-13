# ORINOCO Lite poster

The editable source is [orinoco-lite-poster.html](orinoco-lite-poster.html).
It preserves the title, presenter order and comparison in the [accepted abstract](orinoco-lite-poster-draft.md).
HTML replaces the September SVG as the maintained poster source; the earlier drawing remains in Git history.

## Editing and rebuilding

Open the HTML in a browser to view it, or edit it in any text editor.
Text is ordinary HTML, colors and layout are in the opening `<style>` block, and images have descriptive filenames in `../pics/`.
The browser's **Fit to window** and **Full size** buttons affect viewing only.
The poster keeps the cream, green and navy palette and one title.
The centered CON logo is about twice the previous width, and each author has a separate line.

HTML/CSS suits this layout because it combines text, screenshots, vector artwork and links without a slide framework.
Marp would still require a custom poster layout; Beamer would be useful for a team that prefers LaTeX authoring.
There is no build step just to open the HTML.

The print canvas is **44 inches wide by 44 inches high**, the size selected for fabric printing.
The HTML and exported PDF use the same dimensions.

From the repository root, install the browser once and export:

```bash
uv run --with playwright playwright install chromium
uv run --with playwright python 2026-usrse/build-orinoco-poster.py
```

An installed Google Chrome can be used instead, without the browser download:

```bash
uv run --with playwright python 2026-usrse/build-orinoco-poster.py --channel chrome
```

Alternatively, run `make poster` from this directory.
The helper writes `orinoco-lite-poster.pdf`, checks for missing images and overflowing panels, and uses the HTML's exact print dimensions without browser headers or an additional title.
Add `--preview /path/to/preview.png` for a screen preview.
Generated PDFs follow the existing ignore rule.

### Comparing printed text sizes

The opening CSS variables `--body-text` and `--workflow-text` control the main paragraphs and workflow details.
At the fixed print size, one CSS pixel is 0.75 points: `36px` is 27 pt, `34px` is 25.5 pt, and `32px` is 24 pt. The current values remain 36px and 34px respectively; captions, labels, introductions and headings have their own sizes.

Add `--font-proof` to the build command to also produce `orinoco-font-proof.pdf`, a US Letter comparison of 27, 25.5 and 24 pt in the poster's font and colors.
Print it at **Actual size / 100%**, check the two-inch rule, and compare from the intended reading distance, around one metre.
Browser fit-to-window scaling is not a useful test of printed legibility.
[PosterNerd recommends](https://www.posternerd.com/tutorials/customer-questions) at least 24 pt for text and 36 pt for headings.
If reducing the body text, try 25.5 pt first and rebuild to check the resulting layout.

The screenshots and large upstream SVG follow the repository's DataLad/git-annex convention.
Their registered download URLs on the existing CON Hub allow retrieval without Hub credentials or an additional Git remote, provided the Hub is reachable from your network.
Downloads currently succeed over VPN but return HTTP 403 outside it, leaving GitHub's asset-availability check blocked.
Passing that check requires publishing these assets to the existing public datasets mirror or making the Hub externally accessible.
With DataLad installed in your project environment, run from the repository root:

```bash
datalad get pics/borrowed/orinoco-*
```

Copying the HTML elsewhere also requires its referenced `pics/` assets.

## Tagged CON snapshot

All four repositories have the annotated citation tag **`usrse-2026-10-13`**.
These are the mutually selected revisions of the CON deployment, not four independently chosen versions.
The dated tags retain the poster snapshot without changing package or template semantic versions.
Each tag annotation records all four full revisions.

| Component | Tagged source | Commit |
| --- | --- | --- |
| Package | [orinoco-lite-dev](https://github.com/ORINOCO-Lite/orinoco-lite-dev/tree/usrse-2026-10-13) | `de4d13c6ea67865b0c89990a58b7847b83e8f6ad` |
| Template | [orinoco-lite-template](https://github.com/ORINOCO-Lite/orinoco-lite-template/tree/usrse-2026-10-13) | `1e44846e8d8e5d17f333138c2fbd9e54d57c7468` |
| CON content | [con-site-specific](https://github.com/ORINOCO-Lite/con-site-specific/tree/usrse-2026-10-13) | `e61781ccd01f5ee5adbbf76eca2aa44463e2d276` |
| Website | [dev-centerforopenneuroscience.org](https://github.com/con/dev-centerforopenneuroscience.org/tree/usrse-2026-10-13) | `c1b1e201faae7e8d7cd2a522cc2964f14db971d6` |

When the citation tags were selected, the public CON footer matched the package and website revisions above, with build timestamp `2026-10-13T02:24:13Z`.
The selected [package checks](https://github.com/ORINOCO-Lite/orinoco-lite-dev/actions/runs/38314624071), [template checks](https://github.com/ORINOCO-Lite/orinoco-lite-template/actions/runs/37829191024), [CON validation](https://github.com/con/dev-centerforopenneuroscience.org/actions/runs/38336534726), and [CON deployment](https://github.com/con/dev-centerforopenneuroscience.org/actions/runs/38336534673) passed.

## Images, links and attribution

All website screenshots were captured on **13 October 2026**.
The poster uses the real pages and existing record values; no form submission was made for a screenshot.
Website screenshots retain the sites' and third parties' notices, represented by the repository's existing `LicenseRef-ThirdPartyMixed` convention rather than a new blanket license claim.
The two homepage overviews use a 900 × 960 CSS-pixel viewport, 75% page zoom and device scale 2, yielding 1800 × 1920-pixel images.
The centered pages retain their full content width and are displayed without additional cropping.
The shared editor frame crops the screenshot at the bottom to show its form controls and example record fields at a readable size; its source retains the captured viewport.

| Poster asset in `../pics/borrowed/` | Source and interpretation |
| --- | --- |
| `orinoco-psychoinformatics-overview-20261013.png` | [Psychoinformatics homepage](https://www.psychoinformatics.de/); an upstream metadata-derived website. |
| `orinoco-con-home-overview-20261013.png` | [CON development homepage](https://dev.centerforopenneuroscience.org/); the live CON deployment captured at 14:55 UTC. |
| `orinoco-con-editor-20261013.png` | [CON's SHACL Vue project editor](https://dev.centerforopenneuroscience.org/edit/?sh%3ANodeShape=xyzri%3AXYZProject&pid=https%3A%2F%2Fconcepts.datalad.org%2Fs%2Fdemo-research-information%2Fns%2Fprojects%2Fdatalad&edit=true); the populated DataLad record, cropped to the form. This is the shared editor as used at CON. |
| `orinoco-con-graph-20261013.png` | [CON graph explorer](https://dev.centerforopenneuroscience.org/explore/); the graph container with all default record types selected. |

The refreshed CON homepage capture shows website revision [`d64e994`](https://github.com/con/dev-centerforopenneuroscience.org/commit/d64e99466b5bcb54bf19cb95301f90190f6ff5b2), built at `2026-10-13T14:33:14Z`, with the same tagged package revision `de4d13c`.
It postdates the four citation tags above; those tags remain fixed.

The first column restores `../pics/borrowed/orinoco-selfhost-components-poster.svg`, the official ORINOCO component illustration.
The diagram is Stephan Heunis's `selfhost_components_no_notes.svg`, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), from the [ORINOCO artwork repository](https://hub.psychoinformatics.de/orinoco/artwork).
Its source revision is `a1a9a929e02526eaea489ad5817b1c89b259d669`; Inkscape 1.3.2 outlined its flowed text using Nanum Pen Script.
The second column uses `../pics/borrowed/orinoco-lite-components-poster.svg`, an adaptation by the poster authors under the same CC BY 4.0 terms.
It keeps the original schema, SHACL Vue, processing and output artwork in place, substitutes GitHub pull requests and Git-backed YAML records for Forgejo and Dump Things, and adds the Lite change flow.
The shared App is identified only on the editor-to-GitHub connection; it is outside the records-to-build path.
The catalog, website and annual report are illustrative output types, not claims that CON has implemented each application.
The earlier TRR379 news-page screenshot remains a reference asset and is not an image of the personnel PDF.

The Lite adaptation is a self-contained SVG with editable text labels.
Its reproducible source is `make-component-diagram.py`; run `python3 2026-usrse/make-component-diagram.py` from the repository root to regenerate it.
The script preserves the original source illustration and never writes through an annex symlink.
After changing it, use the repository's normal annex workflow to save the regenerated asset, then rebuild the poster.

The CON logo is `../pics/con-logo-outlined.svg`, copied from the dev site's outlined logo so its lettering does not depend on installed fonts.
The Dartmouth seal is displayed from `../pics/con-ccn-dartmouth-letterhead.svg` with an SVG view fragment; `object-fit: fill` preserves the cropped view instead of the letterhead's intrinsic aspect ratio.
Psychological and Brain Sciences is credited as text beside the seal; the ReproNim mark is `../pics/borrowed/repronim_logo.svg`.
These existing institutional marks retain their respective notices.
The Psychoinformatics mark is `../pics/borrowed/psychoinformatics_logo.svg`, from the group's [official artwork](https://hub.psychoinformatics.de/www/www.psychoinformatics.de/src/commit/810dfbc307471ed4bbc8cba0c9609f14aa7b5327/artwork/psychoinformatics.svg).
Its [source copyright notice](https://hub.psychoinformatics.de/www/www.psychoinformatics.de/src/commit/810dfbc307471ed4bbc8cba0c9609f14aa7b5327/content/pages/copyright.rst) credits Michael Hanke and Alex Waite, 2014–2016, under CC BY-SA 4.0.
For this copy, Inkscape converted the original Passion One glyphs to paths so the logo does not depend on an installed font; its geometry and colors are preserved.
The four vector QR codes embed the complete CON mark with a white pad, high error correction and a four-module quiet border.
They link to the ORINOCO hub, ORINOCO Lite organization, CON development site, and [Stephan Heunis's ReproTube recording](https://datasets.datalad.org/repronim/ReproTube/web/#/channel/DataLad/video/oF98hdaph1k).
The recording is *Information Management at the INM-7*, presented at Distribits on 24 October 2025.

Regenerate and check the logo QR codes with:

```bash
uv run 2026-usrse/make-logo-qrs.py --check-dir /tmp/con-qr-checks
```

The generator uses Inkscape and `rsvg-convert`, keeps the artwork vector-based, and verifies decoded destinations at screen and print sizes, including rotation and slight blur.

The [Dump Things Service documentation](https://hub.psychoinformatics.de/orinoco/dump-things-service) supports the service explanation.
The service separates incoming submissions from curated records; people and curation tools perform the review and promotion.
The TRR379 reporting example is explicitly attributed to that upstream deployment.

## Architecture and reader-facing structure

The overview illustrations share their component positions so the two deployments can be compared visually.
The original service illustration appears unchanged; the Lite adaptation maps Forgejo to GitHub pull requests and service storage to YAML records in Git.
Its arrows show proposals reaching pull requests, reviewers merging them into the accepted records, and Actions building reusable outputs from those records.
The two illustrations span their columns, with the homepage screenshots and explanatory text paired immediately below.
The shared editor appears in the third column, alongside the value of validation within a group and ontologies and identifiers across groups.
The lower workflows describe the corresponding submission, review, acceptance and rendering stages.
The third column closes with the common objective rather than a separate operational checklist.

The [tagged design charter](https://github.com/ORINOCO-Lite/orinoco-lite-dev/blob/usrse-2026-10-13/docs/project-design.md#metadata-change-flow) and its editing, review and authentication contracts support the Lite flow.
“No services for your lab to deploy” refers to using GitHub and the shared curation App.
The App provides authenticated GitHub operations for static editing and review pages; it is outside the build and public reading paths and stores no metadata.
It can be self-hosted, but a downstream need not operate it.
Transient build-time use of Dump Things is deliberately omitted from the high-level deployment comparison.

Upstream curation occurs outside the storage service and may be performed by people or automation; the poster does not identify Forgejo as a universal review interface.
The Psychoinformatics deployment's [update workflow](https://github.com/ORINOCO-Lite/www-from-model/blob/31d7b254c93a4a65613632fd6e1df71b32a20fd0/.forgejo/workflows/update-from-pool.yaml) and [publication workflow](https://github.com/ORINOCO-Lite/www-from-model/blob/31d7b254c93a4a65613632fd6e1df71b32a20fd0/.forgejo/workflows/deploy.yml) support the stated Forgejo role.
Upstream uses `query-things` for selection and joining; the tagged Lite package implements that projection in its own code.
Both reuse `www-from-model` templates and graph generation, with Hugo rendering the site.

The poster retains the accepted abstract's comparison and broader metadata-reuse objective.
Its introductory text explains the use case before the component names, and the paired component artwork complements the detailed workflows below.
The Git/submodule/git-annex guidance remains scoped to the current design: ordinary Git for records, pinned components, and optional Annex for large site-specific media.

The poster follows the talks repository's CC BY-SA 4.0 license, with separate notices for third-party material.
OpenAI Codex assisted with source review, text, diagrams and layout, as acknowledged on the poster.
