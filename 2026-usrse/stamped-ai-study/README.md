# STAMPED example poster — discussion placeholder

An editable **44 × 44 inch** poster adapted from [PR 20](https://github.com/con/talks/pull/20), preserving its layout and institutional artwork.
This is a placeholder for discussion on October 15, 2026, alongside the existing skills proposals: [con/skills#23](https://github.com/con/skills/pull/23), [#24](https://github.com/con/skills/pull/24), and [#26](https://github.com/con/skills/pull/26).

Open [index.html](index.html), view the [PDF preview](exports/pdf-preview.png), or [download the PDF](https://hub.centerforopenneuroscience.org/git-annex-p2phttp/git-annex/40d344f5-0628-494e-82e4-9fab0949ed12/key/MD5E-s694949--7de393e12e04e7a63f89db7c5334b360.pdf).
The [study report](https://github.com/leej3/stamped-ai-research/blob/3db3674d639e63407fa5ac0f9c9012bf48c12727/research/REPORT.md) documents three exploratory paired tasks, including the skills arm's missing-value screening failure.
These results do not establish general skill efficacy or reproduce the proposed ABCD analysis.

## Retrieve and edit

Large assets, the PDF, and preview use git-annex; GitHub displays pointers.
After cloning this branch, use an environment with DataLad and git-annex:

```sh
datalad get 2026-usrse/stamped-ai-study/assets/ \
  2026-usrse/stamped-ai-study/exports/stamped-ai-poster.pdf \
  2026-usrse/stamped-ai-study/exports/pdf-preview.png
```

Edit `index.html` and `poster.css`; preserve the artwork and minimum **32 CSS px / 24 pt** text.
From this directory, with Node/Playwright, uv, Poppler, Inkscape and `rsvg-convert` available:

```sh
uv run --python 3.12 make-logo-qrs.py --check-dir exports/qr-source
node build-poster.cjs --out-dir exports
uv run --python 3.12 verify-pdf.py --review-dir exports
python3 verify-links.py --review-dir exports
```

Retrieve assets first and unlock annexed outputs before replacing them.
The supplied scripts pin their Python dependencies; the builder also supports the bundled Codex Playwright runtime.
Reinspect the PDF after content changes.

## Snapshot and provenance

The existing [PDF audit](exports/pdf-audit.json), [link checks](exports/link-audit.json), and [visual review](exports/agent-visual-review.json) apply to the unchanged exported poster: one 44-inch square page, minimum 24 pt text, 17 link annotations and four QR codes decoded from PDF pixels.
This is agent verification, not author review.
The PDF SHA-256 is `ff238582851dfcf54a7e3be92c955e99644bd09d5eeed34f2c9c0f4ec969f68d`.

The [complete source snapshot and execution records](https://github.com/con/talks/tree/1e96d413e43ca048c7f45674ada9d5f316a68b91/2026-usrse/stamped-ai-study) remain preserved separately, including superseded layouts and retrieval reports.
The QR destinations continue to point to that study's existing branches.
Private transcript payloads remain withheld, and two optional diagnostic images plus two large logs await upload; none is required to view this poster.
[source-manifest.json](source-manifest.json) identifies the original artwork and template.

Composition and prose are CC BY-SA 4.0; scripts are Apache-2.0.
Institutional marks retain their original rights and exceptions in [REUSE.toml](../../REUSE.toml).
