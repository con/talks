# mechababs — McGill neuroscience group, 2026-08-11

`slides.md` is the [marp](https://marp.app) source; 16 slides for a 20 min slot, then 10 min discussion.
`slides.html` is the committed self-contained build; open it in a browser to present.

This deck is **marp, not reveal.js** — it does not follow the repo's `beige`/reveal identity, and there is no `<TALK-ID>.html` at the repo root.

## Build

`slides.html` was produced with `datalad run` and marp-cli pinned to 4.5.0, so after editing `slides.md` you can regenerate it with:

```bash
datalad rerun
```

marp does not need to be installed; `npx` fetches it. `google-chrome` is what renders the PDF.
`</dev/null` matters: marp-cli waits on stdin whenever stdin is not a terminal, and `datalad run` hands it a socket that never closes.

```bash
# HTML (self-contained; present from a browser) — this is what `datalad rerun` replays
datalad run -i 2026-mcgill-mechababs/slides.md -o 2026-mcgill-mechababs/slides.html \
  "npx --yes @marp-team/marp-cli@4.5.0 2026-mcgill-mechababs/slides.md -o 2026-mcgill-mechababs/slides.html --html </dev/null"

# PDF (not committed)
cd 2026-mcgill-mechababs
CHROME_PATH=/usr/bin/google-chrome \
  npx --yes @marp-team/marp-cli@4.5.0 slides.md -o slides.pdf --allow-local-files

# live preview while editing
npx --yes @marp-team/marp-cli@4.5.0 -w -s .
```

## No presenter notes

The deck carries none, by choice. The only `<!-- ... -->` comments in `slides.md` are marp layout directives (`_class`, `_paginate`, `_footer`) — do not strip those.
