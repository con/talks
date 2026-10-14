# STAMPED in Practice: final poster source

This editable **44 × 44 inch** poster follows the layout, cream/navy/green palette, and original artwork from [con/talks PR 20](https://github.com/con/talks/pull/20), pinned to `8a15964ed5cbcd07b04d1f325e848c788e672b05`.
Open [index.html](index.html) after retrieving its assets, or use the [verified direct PDF download](https://hub.centerforopenneuroscience.org/git-annex-p2phttp/git-annex/40d344f5-0628-494e-82e4-9fab0949ed12/key/MD5E-s694949--7de393e12e04e7a63f89db7c5334b360.pdf).
The [PDF preview](exports/pdf-preview.png), [PDF audit](exports/pdf-audit.json), and [agent visual review](exports/agent-visual-review.json) describe this exact export.
The visual review is by agents; it does not claim human review or conference publication.

## Checked snapshot and scope

All three pairs have finished.
Actual-data checks and fresh direct command replays pass in all six arms.
Task 03's skills arm **fails the required case-insensitive N/A screening** in 2 of 15 synthetic cases; the actual dataset contained no such tokens.
The poster separates **Data checks**, **Replay**, and **Screening** and retains the explicit failure paragraph.
These results do not establish general skill efficacy, independent infrastructure, or ABCD reproduction.
The trials shared an account, host, and caches; the coordinator supplied inputs and performed later replay and curation.

[results-data.json](results-data.json) is the final checked snapshot, with precise values and source digests.
Only display values are rounded.
The [study and assessments](https://github.com/leej3/stamped-ai-research/tree/codex/stamped-poster-study/research) provide the full evidence.
[results-placeholder.json](results-placeholder.json) is a superseded, unused layout proposal.

The confirmed author order is **John A. Lee, Austin Macdonald, Cody C. Baker, Yaroslav O. Halchenko**, with the Dartmouth/CON affiliation. The poster retains ReproNim support, truthful Codex assistance disclosure, and the ABCD access/scope limitation.
The submitted title remains in HTML metadata and [source-manifest.json](source-manifest.json); the face subtitle describes the public mixed-gambles study.

## Retrieve the deliverables

The PDF, raster exports, large institutional SVGs, and superseded initial PNG use git-annex.
GitHub tree pages display pointers for these files.
Use DataLad and git-annex from a project-local Pixi environment:

```sh
git clone --branch codex/stamped-usrse-poster https://github.com/con/talks.git
cd talks
pixi run --manifest-path /path/to/environment/pixi.toml git annex init --no-autoenable
pixi run --manifest-path /path/to/environment/pixi.toml datalad get \
  2026-usrse/stamped-ai-study/assets/ \
  2026-usrse/stamped-ai-study/exports/stamped-ai-poster.pdf \
  2026-usrse/stamped-ai-study/exports/pdf-preview.png
```

[public-retrieval.json](exports/public-retrieval.json) records fresh anonymous full-byte downloads, byte lengths, and SHA-256 checks.
A [fresh network clone](exports/fresh-retrieval.json) retrieved all 54 available annex objects through DataLad with credentials disabled and an initially empty object store; every byte length and SHA-256 matched, and all three institutional assets matched their source hashes.
All [14 printed destinations](exports/link-audit.json) also passed anonymous HTTP checks after the delivery branch was pushed.
The PDF is **694,949 bytes**, SHA-256 `ff238582851dfcf54a7e3be92c955e99644bd09d5eeed34f2c9c0f4ec969f68d`.
Public URLs are registered only after the downloaded bytes match.
The superseded initial PNG is retrievable from its pinned earlier Git commit.
Two optional QR test rasters, `exports/qr-source/qr-skills-210px.png` and `exports/qr-source/qr-study-177px.png`, still await upload: the public endpoints returned empty bodies, which failed integrity checks.
The final PDF, preview, institutional assets, and all four QR crops from the actual PDF are verified independently of those diagnostic rasters.

## Edit, build, and verify

Edit `index.html` and `poster.css`; `template.css` retains the reference layout.
Keep all visible poster text at **32 CSS px / 24 pt or larger**.
Shorten text instead of shrinking it.
Preserve the existing checked result snapshot when rebuilding this delivery.

From this directory, with Node, Playwright/cached Chromium, uv, Poppler, Inkscape, and `rsvg-convert` available:

```sh
uv run --python 3.12 make-logo-qrs.py --check-dir exports/qr-source
node build-poster.cjs --out-dir exports --check-only
node build-poster.cjs --out-dir exports
uv run --python 3.12 verify-pdf.py --review-dir exports
python3 verify-links.py --review-dir exports
```

The Python verification dependencies are pinned in the scripts.
`CODEX_NODE_MODULES` can select an existing Playwright installation; the builder also supports the bundled Codex runtime.
No browser download or scientific analysis is automatic.
Retrieve annexed assets before rebuilding, and unlock an annexed output with `git annex unlock -- PATH` before replacing it; never write through a locked annex symlink.
The module intentionally versions its reproducible PDF despite the conference directory's general generated-PDF ignore rule.
Its scoped storage rules preserve binary annex storage and large SVG thresholds without requiring MagicMime.

The HTML audit checks the full print canvas, regions, text size, image loading, and every image link.
The PDF audit checks one 44-inch square page, minimum 24 pt inspectable text, 17 link annotations covering 14 destinations, and all four QR codes decoded from the actual 150 dpi PDF raster both upright and rotated.
The source QR report contains 42 decoding checks per code.
Inspect the latest PDF preview after any poster-content change; the current agent review applies only to its recorded hashes.
`verify-links.py` checks public destination availability after the branch is pushed; it does not establish scientific validity or annex payload integrity.

[update-results.py](update-results.py) is preserved for a separately approved future snapshot refresh:

```sh
python3 update-results.py --study-root /absolute/stamped-ai-research --require-complete
```

It reads checked evaluator artifacts and stopped-arm status; it does not run studies.
A refresh requires new export audits and visual review.
No scientific computation was performed for this source handoff.

## Artwork, links, and licenses

The four QRs point to the poster branch, study branch, skills branch, and CON site.
Every figure, QR, and institutional logo remains clickable.
[source-manifest.json](source-manifest.json) records the exact original CON, Dartmouth, and ReproNim asset hashes and the template revision.
The artwork paths, aspect ratios, and colors were preserved; the marks were not redrawn.

The HTML/CSS adaptation and new prose/QR composition follow **CC BY-SA 4.0**.
The new build, update, and verification scripts retain **Apache-2.0** headers.
The original CON artwork retains the repository's existing attribution.
Dartmouth artwork remains Dartmouth's institutional property, and ReproNim retains `NOASSERTION` with `LicenseRef-ThirdPartyLogo`.
Those marks are not offered under a new CC grant; the PDF and its full-poster renderings retain these exceptions.
See [REUSE.toml](../../REUSE.toml) and the existing [institutional-mark notice](../../LICENSES/LicenseRef-ThirdPartyLogo.txt).
REUSE skips annex symlinks, so asset hashes and these specific annotations supplement lint.

Raw logs and native transcripts remain withheld pending separate coordinator review and publication authorization.
Local captures are preserved; this handoff does not claim a complete public log archive or independently worker-produced infrastructure.
The running final delivery capture is incomplete until the worker stops and will be curated separately afterward.
No blanket license is granted over quoted raw records.

## Superseded initial layout

The earlier [SVG](stamped-ai-poster-initial.svg), [builder](build_initial_poster.py), and [preview](stamped-ai-poster-initial-preview.png) are retained unchanged as **superseded initial layout** artifacts.
Use the HTML and final exports above for this delivery.
