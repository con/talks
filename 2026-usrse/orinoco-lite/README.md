# ORINOCO Lite poster

The editable source is [../orinoco-lite_poster.html](../orinoco-lite_poster.html).
It preserves the title, presenter order and comparison in the [accepted abstract](../orinoco-lite-poster-draft.md).

## Editing and rebuilding

Open the HTML in a browser to view it, or edit it in any text editor.
Text is ordinary HTML, colors and layout are in the opening `<style>` block, and images are in `assets/`.
The browser's **Fit to window** and **Full size** buttons affect viewing only.
The poster keeps the cream, green and navy palette and one title.
Each author has a separate line.

There is no build step just to open the HTML.

The print canvas is **44 inches wide by 44 inches high**, the size selected for fabric printing.
The HTML and exported PDF use the same dimensions.

From the repository root, install the browser once and export:

```bash
uv run --with playwright playwright install chromium
uv run --with playwright python 2026-usrse/orinoco-lite/build-poster.py
```

An installed Google Chrome can be used instead, without the browser download:

```bash
uv run --with playwright python 2026-usrse/orinoco-lite/build-poster.py --channel chrome
```

Alternatively, run `make poster` from the conference directory, `2026-usrse/`.
The helper writes `poster.pdf` in this support directory, checks for missing images and overflowing panels, and uses the HTML's exact print dimensions without browser headers or an additional title.
Add `--preview /path/to/preview.png` for a screen preview.
Generated PDFs follow the existing ignore rule.

### Comparing printed text sizes

The opening CSS variable `--body-text` controls the main paragraphs in the third column.
At the fixed print size, one CSS pixel is 0.75 points: `36px` is 27 pt, `34px` is 25.5 pt, and `32px` is 24 pt. The current value remains 36px; captions, labels, introductions, editor copy and headings have their own sizes.

Add `--font-proof` to the build command to also produce `font-proof.pdf` in this directory, a US Letter comparison of 27, 25.5 and 24 pt in the poster's font and colors.
Print it at **Actual size / 100%**, check the two-inch rule, and compare from the intended reading distance, around one metre.
Browser fit-to-window scaling is not a useful test of printed legibility.
[PosterNerd recommends](https://www.posternerd.com/tutorials/customer-questions) at least 24 pt for text and 36 pt for headings.
If reducing the body text, try 25.5 pt first and rebuild to check the resulting layout.

The screenshots and large SVGs follow the repository's DataLad/git-annex convention. The [refreshed poster source assets](https://github.com/con/talks/releases/tag/usrse-2026-10-13-r2-assets) have public download URLs registered with annex, so CI and readers can retrieve them without VPN access or credentials.
That prerelease stores the 13 October captures, the updated 14 October editor view, and two component illustrations by their annex keys, with checksums and source notices.
The [earlier asset release](https://github.com/con/talks/releases/tag/usrse-2026-10-13-assets) preserves previous versions; the existing CON Hub copies remain additional retrieval locations.
These asset releases are separate from the four deployment citation tags below.
With DataLad installed in your project environment, run from the repository root:

```bash
datalad get 2026-usrse/orinoco-lite/assets/
```

Keep `orinoco-lite_poster.html` beside its `orinoco-lite/` support directory when copying the poster elsewhere.

## Tagged CON snapshot

All four repositories have the annotated citation tag **`usrse-2026-10-13-r2`**.
The earlier `usrse-2026-10-13` tags remain unchanged.
These are the mutually selected revisions of the CON deployment, not four independently chosen versions.
The dated tags retain the poster snapshot without changing package or template semantic versions.
Each tag annotation records all four full revisions.

| Component | Tagged source | Commit |
| --- | --- | --- |
| Package | [orinoco-lite-dev](https://github.com/ORINOCO-Lite/orinoco-lite-dev/tree/usrse-2026-10-13-r2) | `94c3178f830d54f483b6a0e99c8a286f5f0aa5b7` |
| Template | [orinoco-lite-template](https://github.com/ORINOCO-Lite/orinoco-lite-template/tree/usrse-2026-10-13-r2) | `84677de0144a87bdda38fc3318d09f066221ea62` |
| CON content | [con-site-specific](https://github.com/ORINOCO-Lite/con-site-specific/tree/usrse-2026-10-13-r2) | `2ab2f87fb08f094a5049d57c44d2dbd78cbe3147` |
| Website | [dev-centerforopenneuroscience.org](https://github.com/con/dev-centerforopenneuroscience.org/tree/usrse-2026-10-13-r2) | `f54d790c4ad7924684857e2733eb6af19b544e98` |

The public CON footer matched the package and website revisions above, with build timestamp `2026-10-13T23:37:53Z`.
The website selects the tagged template in `.copier-answers.yml`, CON content through its `site-specific` gitlink, and package revision in `pixi.toml`.
The citation tags fix these four source revisions; the website does not commit a `pixi.lock`, so they do not freeze every resolved dependency.
The selected [package engineering checks](https://github.com/ORINOCO-Lite/orinoco-lite-dev/actions/runs/38465299575), [package application checks](https://github.com/ORINOCO-Lite/orinoco-lite-dev/actions/runs/38465299593), [template checks](https://github.com/ORINOCO-Lite/orinoco-lite-template/actions/runs/38470378312), and [CON deployment](https://github.com/con/dev-centerforopenneuroscience.org/actions/runs/38485223963) passed.
[Website PR #24 validation](https://github.com/con/dev-centerforopenneuroscience.org/actions/runs/38485223966) also passed on Linux and macOS.

## Images, links and attribution

The website and graph screenshots were captured on **13 October 2026**; the editor view was updated on **14 October 2026**.
The poster uses the real pages and existing record values; no form submission was made for a screenshot.
Website screenshots retain the sites' and third parties' notices, represented by the repository's existing `LicenseRef-ThirdPartyMixed` convention rather than a new blanket license claim.
The four website panels use a 1000 × 1220 CSS-pixel viewport, 75% page zoom and device scale 2, yielding 2000 × 2440-pixel images.
The pages retain their full content width and start at the top; the CON people directory shows both Centroids and Collaborators.
The shared editor uses a 1440 × 730-pixel crop of Horea-Ioan Ioanas’s existing association with CON’s project record.
It shows the Person record type and an open role picker with controlled vocabulary choices.
It was captured on 14 October at 13:15:07 UTC, at 80% zoom from a 1600 × 1100 viewport, with a 720 × 365 crop at (680, 450), at device scale 2.
Only the existing association form and its role picker were opened; no selections or record values were changed.

| Poster asset in `assets/` | Source and interpretation |
| --- | --- |
| `orinoco-psychoinformatics-home-panel-20261013.png` | [Psychoinformatics homepage](https://www.psychoinformatics.de/), including its graph and objectives. |
| `orinoco-psychoinformatics-persons-panel-20261013.png` | [Psychoinformatics people directory](https://www.psychoinformatics.de/persons/). |
| `orinoco-con-home-panel-20261013.png` | [CON development homepage](https://dev.centerforopenneuroscience.org/), including its graph and objectives. |
| `orinoco-con-persons-panel-20261013.png` | [CON people directory](https://dev.centerforopenneuroscience.org/persons/), showing Centroids and Collaborators. |
| `orinoco-con-editor-typed-20261014.png` | [CON’s SHACL Vue project editor](https://dev.centerforopenneuroscience.org/edit/?sh%3ANodeShape=dlthings%3AThing&pid=xyzrins%3A.&edit=true); the Person record type and controlled role choices in an existing project association. This is the shared editor as used at CON. |
| `orinoco-con-graph-20261013.png` | [CON graph explorer](https://dev.centerforopenneuroscience.org/explore/); all default record types selected. |

The 13 October captures were taken between 23:49:29 and 23:50:59 UTC for this snapshot.
The updated editor view was checked against the same deployed website and package revisions.
The graph image is a 1312 × 1300-pixel capture of the live graph with its default record types.
The CON pages identify website revision [`f54d790`](https://github.com/con/dev-centerforopenneuroscience.org/commit/f54d790c4ad7924684857e2733eb6af19b544e98), package [`94c3178`](https://github.com/ORINOCO-Lite/orinoco-lite-dev/commit/94c3178f830d54f483b6a0e99c8a286f5f0aa5b7) (`0.3.0+12.g94c3178`), built at `2026-10-13T23:37:53Z`.
The CON captures match the four citation tags above.
The editor links to SHACL Vue source commit [`41a2fe3`](https://hub.psychoinformatics.de/orinoco/shacl-vue/src/commit/41a2fe388ef3e2698deeadd6f24bb270cbe49d44); this identifies its source despite the placeholder timestamp in its version label.

The first column uses `assets/orinoco-selfhost-components-poster.svg`, the official ORINOCO component illustration.
The diagram is Stephan Heunis's `selfhost_components_no_notes.svg`, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), from the [ORINOCO artwork repository](https://hub.psychoinformatics.de/orinoco/artwork).
Its source revision is `a1a9a929e02526eaea489ad5817b1c89b259d669`; Inkscape 1.3.2 outlined its flowed text using Nanum Pen Script.
The second column uses `assets/orinoco-lite-components-poster.svg`, an adaptation by the poster authors under the same CC BY 4.0 terms.
It keeps the original schema, SHACL Vue, processing and output artwork in place, substitutes GitHub pull requests and Git-backed YAML records for Forgejo and Dump Things, and adds the Lite change flow.
The shared App is identified only on the editor-to-GitHub connection; it is outside the records-to-build path.
The catalog, website and annual report are illustrative output types, not claims that CON has implemented each application.

The Lite adaptation is a self-contained SVG with editable text labels.
Its reproducible source is `make-component-diagram.py`; run `python3 2026-usrse/orinoco-lite/make-component-diagram.py` from the repository root to regenerate it.
The script preserves the original source illustration and never writes through an annex symlink.
After changing it, use the repository's normal annex workflow to save the regenerated asset, then rebuild the poster.

The CON logo is `assets/con-logo-outlined.svg`, copied from the dev site's outlined logo so its lettering does not depend on installed fonts.
The Dartmouth seal is displayed from `assets/con-ccn-dartmouth-letterhead.svg` with an SVG view fragment; `object-fit: fill` preserves the cropped view instead of the letterhead's intrinsic aspect ratio.
Psychological and Brain Sciences is credited as text beside the seal; the ReproNim mark is `assets/repronim_logo.svg`.
These institutional marks retain their respective notices.
The Dartmouth and ReproNim assets are copies of the repository’s shared originals, which remain in `pics/` for other talks.
The Psychoinformatics mark is `assets/psychoinformatics_logo.svg`, from the group's [official artwork](https://hub.psychoinformatics.de/www/www.psychoinformatics.de/src/commit/810dfbc307471ed4bbc8cba0c9609f14aa7b5327/artwork/psychoinformatics.svg).
Its [source copyright notice](https://hub.psychoinformatics.de/www/www.psychoinformatics.de/src/commit/810dfbc307471ed4bbc8cba0c9609f14aa7b5327/content/pages/copyright.rst) credits Michael Hanke and Alex Waite, 2014–2016, under CC BY-SA 4.0.
For this copy, Inkscape converted the original Passion One glyphs to paths so the logo does not depend on an installed font; its geometry and colors are preserved.
The eight vector QR codes embed the outlined CON mark in its original blue at 42% of the code body width, with a white pad, navy modules, high error correction and a four-module quiet border.
Organization links sit beside their component illustrations, website links beside their screenshot pairs, the video link beside the ORINOCO heading, and the GitHub workflow link beside the editor.
The graph-explorer QR sits beside its description, and the online-poster QR sits beside the authors in the top bar.
They link to the ORINOCO hub, ORINOCO Lite organization, both group websites, [CON’s graph explorer](https://dev.centerforopenneuroscience.org/explore/), the [poster on Zenodo](https://doi.org/10.5281/zenodo.22834595), [editor-generated pull requests](https://github.com/con/dev-centerforopenneuroscience.org/pulls?q=is%3Apr+head%3Acuration%2Fshacl-vue-), and [Stephan Heunis's ReproTube recording](https://datasets.datalad.org/repronim/ReproTube/web/#/channel/DataLad/video/oF98hdaph1k).
The poster link uses Zenodo’s all-versions DOI so it follows the latest published version.
The recording is *Information Management at the INM-7*, presented at Distribits on 24 October 2025.

Every screenshot is also a direct link to the page it depicts.
The component illustrations link to their respective projects, and the CON, Dartmouth, Psychological and Brain Sciences, ReproNim and Psychoinformatics marks or labels link to their websites.
These links are available in the HTML and exported PDF.

Regenerate and check the logo QR codes with:

```bash
uv run 2026-usrse/orinoco-lite/make-logo-qrs.py --check-dir /tmp/con-qr-checks
```

The generator uses Inkscape and `rsvg-convert`, keeps the artwork vector-based, and verifies decoded destinations at screen and print sizes, including rotation and slight blur.

The [TRR379 reporting example](https://www.trr379.de/news/2025-dfg-survey/) is explicitly attributed to that upstream deployment.

## Reader-facing structure

The first two columns compare deployment choices through corresponding component illustrations, homepage and people-directory screenshots, and brief introductions.
A shared editor spans both columns below them.
The third column connects local reuse, shared meanings through ontologies, and structured context for AI, closing with the common ORINOCO vision.
The poster retains the accepted abstract's comparison and broader metadata-reuse objective.

The component drawings retain their original technical labels as visual discussion aids.
The Lite illustration follows the [tagged design charter](https://github.com/ORINOCO-Lite/orinoco-lite-dev/blob/usrse-2026-10-13-r2/docs/project-design.md#metadata-change-flow).

## GitHub workflow examples

The editor section and QR code link to [all website pull requests from SHACL Vue](https://github.com/con/dev-centerforopenneuroscience.org/pulls?q=is%3Apr+head%3Acuration%2Fshacl-vue-).
The search matches branches beginning with `curation/shacl-vue-` and includes open and closed proposals, so readers can follow the workflow as it improves.
[Website PR #24](https://github.com/con/dev-centerforopenneuroscience.org/pull/24) and its companion [CON metadata PR #18](https://github.com/ORINOCO-Lite/con-site-specific/pull/18) remain one completed example.

## Connections through global identifiers

The diagram compares CON’s records with independently published JOSS metadata for the DataLad paper.
[CON’s Yaroslav Halchenko record](https://github.com/ORINOCO-Lite/con-site-specific/blob/2ab2f87fb08f094a5049d57c44d2dbd78cbe3147/metadata/records/XYZPerson/yaroslav-halchenko.yaml) contains ORCID `0000-0003-3456-2493`.
[CON’s DataLad publication record](https://github.com/ORINOCO-Lite/con-site-specific/blob/2ab2f87fb08f094a5049d57c44d2dbd78cbe3147/metadata/records/XYZPublication/datalad-joss-2021.yaml) identifies the paper by DOI `10.21105/joss.03262` and credits Yaroslav with the MARC author role, `marcrel:aut`.
The [JOSS publisher record](https://joss.theoj.org/papers/10.21105/joss.03262) independently lists the same DOI and author ORCID; this was checked on 14 October 2026.

Solid arrows show the author relationship within each collection; dashed lines show where the shared external identifiers permit matching across collections.
The diagram illustrates matching opportunities supported by actual records, not an implemented automatic graph merge or a live query to JOSS.
ORCID and DOI identify entities; MARC describes the meaning of CON’s author role.
The publisher is not asserted to use MARC internally.

The poster follows the talks repository's CC BY-SA 4.0 license, with separate notices for third-party material.
OpenAI Codex assisted with source review, text, diagrams and layout, as acknowledged on the poster.
