# pdfdeck: talks that exist only as PDF

`pdfdeck.html?talk=<TALK-ID>` presents `<TALK-ID>.pdf` as a reveal.js deck.
Nothing is generated per talk: there are no page images and no per-talk HTML.
The viewer paints each slide from the PDF with pdf.js, which fetches only the
parts it needs through HTTP range requests.

| Key                 | Does                                             |
| ------------------- | ------------------------------------------------ |
| Left / Right        | previous / next section                          |
| Up / Down           | previous / next frame within the section         |
| Space / Shift+Space | next / previous PDF page, through everything     |
| `o`                 | overview: one column per section                 |
| `t`                 | the list of sections                             |

Links in the PDF stay clickable, and the URL tracks the position, so a slide
can be linked to (`...?talk=<TALK-ID>#/3/2`).

## How a PDF becomes a deck

- **Sections** come from [`sections.yaml`](sections.yaml), `page: title` per
  talk. Each section is a column of the deck, and moving between sections is
  animated. A talk with no entry is one column.
- **Frames** come from the PDF: beamer gives all overlays of a frame the same
  page label, so consecutive equal labels are one slide, and its later pages
  are reveal.js fragments, which swap instantly as they did on stage. A PDF
  without usable labels has one slide per page.

- **Events**, such as a workshop, are a folder of PDFs with one record:
  `?talk=<EVENT>/<LECTURE>` shows `<EVENT>/<LECTURE>.pdf`, and `?talk=<EVENT>`
  opens on the first lecture. The lectures are the `sections.yaml` entries named
  `<EVENT>/<LECTURE>`, in file order, each with a `title:` next to its pages, and
  they are listed above the sections (`t`).

`model.js` holds this logic, `viewer.js` the browser side.

## Adding a talk

1. Copy the PDF to `<TALK-ID>.pdf` at the repository root (it goes to the annex).
2. Add its sections to `sections.yaml`.
3. Add its record, as for any talk (`CLAUDE.md`, step 10), with
   `foaf:homepage` set to `.../pdfdeck.html?talk=<TALK-ID>` and
   `dcat:downloadURL` to `.../<TALK-ID>.pdf`. Title, venue and date shown by the
   viewer come from `talks.yaml`, which is generated from that record.

For an event, put the PDFs in `<EVENT>/`, give each its `sections.yaml` entry,
and add one record with `foaf:homepage` set to `.../pdfdeck.html?talk=<EVENT>`,
without `dcat:downloadURL`, as there is no single PDF to download.

The viewer needs a web server, as browsers refuse to `fetch` from `file://`:
`python3 -m http.server`, or `npm start`.

## Tests

```sh
uv run --with pytest --with pyyaml --with playwright --with pymupdf playwright install chromium-headless-shell
uv run --with pytest --with pyyaml --with playwright --with pymupdf pytest tests/
```

`tests/test_pdfdeck_e2e.py` drives the viewer in Chromium over generated PDFs
whose pages are solid colours, so it reads back which page is really on screen.
`tests/pdfdeck_model.test.mjs` covers `model.js`, and `tests/test_pdfdeck.py`
runs those and checks `sections.yaml` against `talks.yaml` and the PDFs.

## Vendored

`3rd-party/pdfjs` is `pdfjs-dist` 6.4.299 and `3rd-party/js-yaml` is `js-yaml`
4.1.0, from npm. The two pdf.js modules are renamed from `.mjs` to `.js`, as
module scripts need a JavaScript content type and that is what the published
mirror is known to send for `.js`.
