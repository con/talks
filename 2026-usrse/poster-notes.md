# ORINOCO Lite poster

The editable source is [orinoco-lite-poster.html](orinoco-lite-poster.html).
It preserves the title, presenter order and comparison in the [accepted abstract](orinoco-lite-poster-draft.md).
HTML replaces the September SVG as the maintained poster source; the earlier drawing remains in Git history.

## Editing and rebuilding

Open the HTML in a browser to view it, or edit it in any text editor.
Text is ordinary HTML, colors and layout are in the opening `<style>` block, and images have descriptive filenames in `../pics/`.
The browser's **Fit to window** and **Full size** buttons affect viewing only.
The poster keeps the cream, green and navy palette, one title, and a centered CON logo.

HTML/CSS suits this layout because it combines text, screenshots, vector artwork and links without a slide framework.
Marp would still require a custom poster layout; Beamer would be useful for a team that prefers LaTeX authoring.
There is no build step just to open the HTML.

The print canvas remains **48 inches wide by 36 inches high**.
This is the existing draft size; confirm the conference's mounting specification before ordering a print.

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

The public CON footer matched the package and website revisions above, with build timestamp `2026-10-13T02:24:13Z`.
The selected [package checks](https://github.com/ORINOCO-Lite/orinoco-lite-dev/actions/runs/38314624071), [template checks](https://github.com/ORINOCO-Lite/orinoco-lite-template/actions/runs/37829191024), [CON validation](https://github.com/con/dev-centerforopenneuroscience.org/actions/runs/38336534726), and [CON deployment](https://github.com/con/dev-centerforopenneuroscience.org/actions/runs/38336534673) passed.

## Images, links and attribution

All website screenshots were captured on **13 October 2026**.
The poster uses the real pages and existing record values; no form submission was made for a screenshot.
Website screenshots retain the sites' and third parties' notices, represented by the repository's existing `LicenseRef-ThirdPartyMixed` convention rather than a new blanket license claim.
Display frames crop the website screenshots at the bottom; source files retain the captured viewports.

| Poster asset in `../pics/borrowed/` | Source and interpretation |
| --- | --- |
| `orinoco-psychoinformatics-20261013.png` | [Psychoinformatics homepage](https://www.psychoinformatics.de/); an upstream metadata-derived website. |
| `orinoco-con-home-20261013.png` | [CON development homepage](https://dev.centerforopenneuroscience.org/); the tagged CON deployment. |
| `orinoco-con-editor-20261013.png` | [CON's SHACL Vue project editor](https://dev.centerforopenneuroscience.org/edit/?sh%3ANodeShape=xyzri%3AXYZProject&pid=https%3A%2F%2Fconcepts.datalad.org%2Fs%2Fdemo-research-information%2Fns%2Fprojects%2Fdatalad&edit=true); the populated DataLad record, cropped to the form. This is the shared editor as used at CON. |
| `orinoco-con-graph-20261013.png` | [CON graph explorer](https://dev.centerforopenneuroscience.org/explore/); the graph container with all default record types selected. |
| `orinoco-trr379-survey-20261013.png` | [TRR379's DFG survey announcement](https://www.trr379.de/news/2025-dfg-survey/); a public account of an upstream reporting deployment. It is a news-page screenshot, not an image of a personnel PDF. |
| `orinoco-selfhost-components-poster.svg` | [ORINOCO's official artwork](https://hub.psychoinformatics.de/orinoco/artwork), `selfhost_components_no_notes.svg`; Stephan Heunis (2026), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). |

The original ORINOCO diagram was last changed at artwork commit `a1a9a929e02526eaea489ad5817b1c89b259d669`.
Its downloaded SHA256 was `5fc88059db6a4464dac5318f46f869673a96ef5dfaa8448f4c9200a6b5d2394a`, matching the upstream annex key.
The [upstream README](https://hub.psychoinformatics.de/orinoco/artwork/src/commit/384047aa38179ac323aeabfaa617518544b942f3/README.md) provides authorship and licensing.
Inkscape 1.3.2 converted its flowed text to paths using [Nanum Pen Script](https://github.com/google/fonts/tree/main/ofl/nanumpenscript), preserving the artwork and labels while making it render reliably in browsers.
The original editable vector remains available upstream.
The poster's visible caption discloses this adaptation.

The CON logo is the repository's existing `../pics/con-logo_blue_big.svg`.
The four vector QR codes link to the ORINOCO hub, ORINOCO Lite organization, CON development site, and [Stephan Heunis's ReproTube recording](https://datasets.datalad.org/repronim/ReproTube/web/#/channel/DataLad/video/oF98hdaph1k).
The recording is *Information Management at the INM-7*, presented at Distribits on 24 October 2025.

The [Dump Things Service documentation](https://hub.psychoinformatics.de/orinoco/dump-things-service) supports the service explanation.
The service separates incoming submissions from curated records; people and curation tools perform the review and promotion.
The TRR379 reporting example is explicitly attributed to that upstream deployment.

## Changes responding to PR #20

The revised poster pairs the two deployment workflows with website screenshots, uses ORINOCO's own curation graphic, shows the shared SHACL Vue form and CON graph, explains the metadata service, and links Heunis's talk with a QR code.
The earlier bottom sections are replaced by these examples and concise operational guidance.
The Git/submodule/git-annex guidance follows the tagged package's current design: records remain ordinary Git content, submodules select separately maintained components, optional Annex use is confined to site-specific media, and package distributions bundle required upstream rendering assets.

The poster follows the talks repository's CC BY-SA 4.0 license, with separate notices for third-party material.
OpenAI Codex assisted with source review, text, diagrams and layout, as acknowledged on the poster.
