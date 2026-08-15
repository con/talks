# mechababs — McGill neuroscience group, 2026-08-11

`slides.md` is the [marp](https://marp.app) source; 16 slides for a 20 min slot, then 10 min discussion.

This deck is **marp, not reveal.js** — it does not follow the repo's `beige`/reveal identity, and there is no `<TALK-ID>.html` at the repo root. Only the source is kept here; build the HTML or PDF locally.

## Build

marp does not need to be installed; `npx` fetches it. `google-chrome` is what renders the PDF.

```bash
cd 2026-mcgill-mechababs

# HTML (self-contained; present from a browser)
npx --yes @marp-team/marp-cli@latest slides.md -o slides.html --html

# PDF
CHROME_PATH=/usr/bin/google-chrome \
  npx --yes @marp-team/marp-cli@latest slides.md -o slides.pdf --allow-local-files

# live preview while editing
npx --yes @marp-team/marp-cli@latest -w -s .
```

## No presenter notes

The deck carries none, by choice. The only `<!-- ... -->` comments in `slides.md` are marp layout directives (`_class`, `_paginate`, `_footer`) — do not strip those.
