# CLAUDE.md — guidance for authoring & curating CON talks

This file is loaded automatically when you (Claude / Claude Code) work in
this repository. It complements:

- **`SOUL.md`** — *what* CON talks are about, voice, visual style, fixed
  metadata, citation conventions, and the recurring story arcs.
- **`INDEX.md`** — *which slides exist already* and how to find them per
  topic and per talk.

Read both before authoring or editing a deck. Treat them as the source of
truth for cross-talk decisions.


## Repository layout (relevant subset)

```
README.md                 — repo overview, build/PDF instructions
SOUL.md                   — mission, voice, visual identity, references
INDEX.md                  — talk-by-talk catalog + topic lookup
CLAUDE.md                 — this file: how to author & curate
LICENSE                   — CC-BY-SA
gulpfile.js, package.json — npm/gulp setup for `npm start` live reload
css/custom.css            — small site-wide CSS overrides
reveal.js/                — vendored reveal.js (do not modify)
reveal.js-mermaid-plugin/ — vendored mermaid plugin
pics/                     — all images (canonical assets are listed in SOUL §4)
pics/borrowed/            — third-party images
3rd-party/                — third-party PDFs cited in slides
embed/                    — small HTML iframes referenced by some decks
posters/                  — poster sources (separate flow)
2026-usrse/               — venue-specific drafts: proposal, BoF/poster templates,
                            lineage diagrams
2026-ohbm-ossig/          — OHBM Open Science Room submission
2026-repronim-YODA-BIDS-webinar/ — companion notes/planning to that deck
2026-ca-origami-retreat-aicoding/ — planning + per-slide screenshots for that deck
_backdrawer_/             — shelved talk prototypes / outline-only stubs
                            (see _backdrawer_/README.md for the convention)
<TALK-ID>.html            — top-level reveal.js decks
```

`<TALK-ID>` follows `<YYYY>-<venue>-<short-topic>` (or with a trailing
`-name`/`-aicoding` for sub-decks at the same venue). The published mirror
is `https://datasets.datalad.org/centerforopenneuroscience/talks/<TALK-ID>.html`.

The repo is a [DataLad](https://datalad.org/) dataset (note `.datalad/`,
`.gitattributes`); commit binary assets via DataLad if introducing new
ones. For text-only edits to existing HTML, plain `git` is fine.


## Workflow for creating a new deck

1. **Decide the arc** (`SOUL.md` §7) — Origin/Stack/Today, Challenges/
   Solutions/Take-home, YODA-principle-a-day, Nirvana, AI-ladder, or
   Reuse/Compose/Extend/Standardize. Copy the spine, then customize.
2. **Pick the parent deck** for that arc from `INDEX.md` (e.g. for a
   data-archives talk, start from `2023-brain-dandi.html` or
   `2023-lbl-building-dandi.html`).
3. **Create `<TALK-ID>.html`** at the repository root. Use the parent
   deck as a starting point — `cp` it and edit, or assemble fresh from
   the title-slide template in `SOUL.md` §3.
4. **Set the standard reveal.js header** with theme `beige`, the four
   plugins (Markdown / Highlight / Notes / Mermaid), `1400×1050` canvas,
   and the `Reveal.initialize` block matching `SOUL.md`.
5. **Title slide**: CON letterhead → title → social handles → CON/PBS/
   CCN/Dartmouth affiliations → QR code (see "QR codes" below) → venue
   + date + live-slides URL → logo strip with the Ukraine ribbon last.
6. **Pull reusable slides** by copying full `<section>` elements from
   the talk file referenced in `INDEX.md`. Adjust hyperlinks but keep
   `data-src="pics/..."` paths verbatim — all decks share the `pics/`
   tree.
7. **End with**:
   - one or more "Take-home" / "Monday checklist" slides;
   - an Acknowledgements slide (the canonical layout is in
     `2024-distribits-datalad.html`);
   - a final "Thank you!" slide. Yoda-SVG sign-off is appropriate when
     the deck has YODA flavoring.
8. **Test** the deck by opening it in a browser. For a development
   loop, `npm install` then `npm start` per `README.md`.
9. **Update `INDEX.md`** with the new deck (per-talk entry + any
   topic-lookup additions).
10. **Commit** the new deck *and* the QR code *and* the `INDEX.md`
    update together. Use the repo's git workflow (DataLad-managed).

### QR codes

The live-slides URL is **fully determined by the deck filename**:

```
https://datasets.datalad.org/centerforopenneuroscience/talks/<TALK-ID>.html
```

so the QR code can (and should) be generated **at deck-creation time**
— do not wait for "after publishing". The same URL is already hard-coded
into the title-slide template, and every older deck in the corpus
follows this convention (e.g.
`pics/2024-distribits-datalad-qrcode.png`,
`pics/2025-distribits-YODA-qrcode.png`,
`pics/2026-repronim-YODA-BIDS-webinar-qrcode.png` — open any of them
side-by-side with the title slide of the matching `*.html` deck to
confirm).

Save as `pics/<TALK-ID>-qrcode.png` and reference it from the title
slide `<img>`. The repo's already-generated QR PNGs were produced with
the `qrcode` Python package (which also installs a `qr` CLI). Install
once with `uv` (do **not** forget `--with pillow` — without it `qr`
fails at import-time with `ModuleNotFoundError: No module named 'PIL'`):

```bash
uv tool install qrcode --with pillow
```

Then for each new deck:

```bash
TALK_ID=2026-usrse-con-talk
URL=https://datasets.datalad.org/centerforopenneuroscience/talks/${TALK_ID}.html
qr "$URL" > pics/${TALK_ID}-qrcode.png
```

The default output is a ~490×490 1-bit PNG, which is what the older
title slides reference. `qrencode` from your distro works too if it's
installed.

The PNG itself is binary; commit it via DataLad
(`datalad save -m '+ qrcode for <TALK-ID>' pics/<TALK-ID>-qrcode.png`).

### Subdirectory conventions

- Companion notes (planning, per-slide screenshots, companion
  TODO files) live in a directory matching the deck name without the
  `.html` extension, e.g. `2026-ca-origami-retreat-aicoding/`.
- Long-running drafts of submissions, BoFs, posters, etc. live under
  the venue directory (e.g. `2026-usrse/`).
- Do **not** introduce a new top-level subdirectory just for one talk.

## Workflow for curating / editing existing decks

- **Small fix** (typo, link rot): edit in place, commit a focused diff.
- **Adding a new slide**: prefer copying a similarly-structured slide
  from a sibling deck (consult `INDEX.md`) over inventing layout from
  scratch. Reveal.js's section-vertical structure is touchy; cargo-cult
  carefully.
- **Updating a citation**: keep the small/`<small>` blockstyle from
  `SOUL.md` §5; bold the speaker's name; link the DOI directly.
- **Refreshing a screenshot**: drop into `pics/` with a date suffix
  (e.g. `datasets.datalad.org-20251021.png`). Don't delete the older
  one — older decks still reference it.
- **Yanking a slide for reuse**: copy the *entire* `<section>...</section>`
  block, then walk through any `class="fragment"`, `data-fragment-index`,
  `data-transition` attributes — they are usually fine but occasionally
  need to be adjusted to fit the new local context.

## Authoring conventions to match the existing corpus

- **Use `data-src` for `<img>`**, not `src`. Reveal.js lazy-loads on
  approach.
- **Reveal markdown sub-decks** — use them for content-heavy sections:
  ```html
  <section data-markdown
           data-separator="^\n----\n"
           data-vertical="^\n---\n">
    <textarea data-template>… markdown …</textarea>
  </section>
  ```
- **Mermaid diagrams** — wrap in `<div class="mermaid"><pre>…</pre></div>`
  and stay within widely-supported flavors (`flowchart`, `gitGraph`,
  `graph TB|LR`). Newer decks set theme variables per-diagram.
- **Speaker notes** — `<aside class="notes">…</aside>`. Fine to be
  long; press `s` to view in reveal.js.
- **Section dividers** — soft radial gradient
  (`<section data-background-gradient="radial-gradient(white, #f7dfd3)">`)
  for "Challenge:" intros.
- **No new CSS files** — augment `css/custom.css` if you must, but
  inline-style most layout tweaks (matching the existing decks).
- **No emojis** in slide text unless the deck already uses them
  (the corpus does not, except in occasional small flourishes).

## What goes where in this folder

| If you're producing… | Put it in… |
| --- | --- |
| New slide deck | `<TALK-ID>.html` at repo root |
| QR code image for the deck | `pics/<TALK-ID>-qrcode.png` |
| Per-deck planning notes / screenshots | `<TALK-ID>/` directory |
| Venue-specific submission docs (PRD, BoF, poster, abstract) | `<venue-dir>/` (e.g. `2026-usrse/`) |
| New reusable image | `pics/` (or `pics/borrowed/` if third-party) |
| New citation PDF | `3rd-party/` |

## Don't do these

- Don't switch the reveal.js theme. **`beige`** is the visual identity.
- Don't introduce a build step in a deck (each `<TALK-ID>.html` must be
  openable as a single file).
- Don't move or rename existing `<TALK-ID>.html` files — published live
  links depend on the URL. The one exception is shelving an outline-only
  stub that never went out: `git mv <TALK-ID>.html _backdrawer_/`,
  update its INDEX.md entry into the *Shelved (backdrawer)* section,
  and (if previously cited externally) update those refs. Filename does
  not change — promotion back to active status is just `git mv` in
  reverse.
- Don't add a new top-level subdirectory for slides; keep decks at the
  root and notes in a sibling directory named after the deck.
- Don't `git rm` historical assets from `pics/` — older talks reference
  them.
- Don't write new English-language documentation files at the root
  unprompted. The three docs (`SOUL.md`, `INDEX.md`, `CLAUDE.md`) plus
  the existing `README.md` are intentional. Use `<TALK-ID>/PLAN.md`,
  `TODO.md`, etc., per existing companion-notes convention.

## When the user says "draft a talk for X"

A reasonable flow:

1. Skim `SOUL.md` to anchor on style.
2. Pick the arc (`SOUL.md` §7) and parent deck (`INDEX.md`).
3. Search `INDEX.md`'s topic-lookup for matching reusable slides.
4. Produce `<TALK-ID>.html` (and the companion `<TALK-ID>/PLAN.md` if
   the deck warrants one).
5. Update `INDEX.md` with the new talk's entry.
6. Surface a list of slides borrowed (with source `<file>:<section>`
   pointers) so the user can sanity-check sourcing.
