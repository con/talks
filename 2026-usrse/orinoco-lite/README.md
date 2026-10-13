# ORINOCO Lite poster

The editable source is [../poster.html](../poster.html).
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

The screenshots and large upstream SVG follow the repository's DataLad/git-annex convention. The [poster source assets](https://github.com/con/talks/releases/tag/usrse-2026-10-13-assets) have public download URLs registered with annex, so CI and readers can retrieve them without VPN access or credentials.
That prerelease stores the current and earlier asset versions by their annex keys, with checksums and source notices; it is separate from the four deployment citation tags below.
The existing CON Hub copies remain additional retrieval locations.
With DataLad installed in your project environment, run from the repository root:

```bash
datalad get 2026-usrse/orinoco-lite/assets/
```

Keep `poster.html` beside its `orinoco-lite/` support directory when copying the poster elsewhere.

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
The four website panels use a 1000 × 1220 CSS-pixel viewport, 75% page zoom and device scale 2, yielding 2000 × 2440-pixel images.
The pages retain their full content width; the CON people directory is scrolled to show both Centroids and Collaborators.
The shared editor uses a 2440 × 1190-pixel landscape crop of the populated DataLad project, showing its description, dates and relationships.
It was captured at 75% zoom from a 1600 × 1000 viewport, with the form pane scrolled 310 pixels and a 1220 × 595 crop at (285, 105), at device scale 2.

| Poster asset in `assets/` | Source and interpretation |
| --- | --- |
| `orinoco-psychoinformatics-home-panel-20261013.png` | [Psychoinformatics homepage](https://www.psychoinformatics.de/), including its graph and objectives. |
| `orinoco-psychoinformatics-persons-panel-20261013.png` | [Psychoinformatics people directory](https://www.psychoinformatics.de/persons/). |
| `orinoco-con-home-panel-20261013.png` | [CON development homepage](https://dev.centerforopenneuroscience.org/), including its graph and objectives. |
| `orinoco-con-persons-panel-20261013.png` | [CON people directory](https://dev.centerforopenneuroscience.org/persons/), showing Centroids and Collaborators. |
| `orinoco-con-editor-landscape-20261013.png` | [CON's SHACL Vue project editor](https://dev.centerforopenneuroscience.org/edit/?sh%3ANodeShape=xyzri%3AXYZProject&pid=https%3A%2F%2Fconcepts.datalad.org%2Fs%2Fdemo-research-information%2Fns%2Fprojects%2Fdatalad&edit=true); the populated DataLad record, cropped to its fields. This is the shared editor as used at CON. |
| `orinoco-con-graph-20261013.png` | [CON graph explorer](https://dev.centerforopenneuroscience.org/explore/); the earlier graph capture with all default record types selected. |

The four website panels and editor were captured between 20:34 and 20:37 UTC.
The CON pages identify website revision [`fdf9b7f`](https://github.com/con/dev-centerforopenneuroscience.org/commit/fdf9b7fbc247ae95317146a657475d2bf379a9bf), package [`7c25a98`](https://github.com/ORINOCO-Lite/orinoco-lite-dev/commit/7c25a987d3557fd4e8428d92c687e7feca36255c) (`0.3.0+10.g7c25a98`), built at `2026-10-13T19:56:46Z`.
These live examples postdate the four citation tags above; those tags remain fixed.

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
The five vector QR codes embed the outlined CON mark in its original blue at 42% of the code body width, with a white pad, navy modules, high error correction and a four-module quiet border.
Organization links sit beside their component illustrations, website links beside their screenshot pairs, and the video link beside the ORINOCO heading.
They link to the ORINOCO hub, ORINOCO Lite organization, both group websites, and [Stephan Heunis's ReproTube recording](https://datasets.datalad.org/repronim/ReproTube/web/#/channel/DataLad/video/oF98hdaph1k).
The recording is *Information Management at the INM-7*, presented at Distribits on 24 October 2025.

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
The Lite illustration follows the [tagged design charter](https://github.com/ORINOCO-Lite/orinoco-lite-dev/blob/usrse-2026-10-13/docs/project-design.md#metadata-change-flow).

## Final refresh

After the Vue editing flow is working, choose a public example pull request for viewers to explore.
The current work is in [CON content PR #17](https://github.com/ORINOCO-Lite/con-site-specific/pull/17) and [website PR #22](https://github.com/con/dev-centerforopenneuroscience.org/pull/22).
Once the resulting changes are deployed, select a new coordinated citation snapshot, refresh the screenshots and editor example, and rebuild the poster.
The current tags and captures remain unchanged during this layout revision.

The poster follows the talks repository's CC BY-SA 4.0 license, with separate notices for third-party material.
OpenAI Codex assisted with source review, text, diagrams and layout, as acknowledged on the poster.
