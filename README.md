# Slides for the talks from CON people

This repository contains the raw sources for talks and workshops done by CON people.
Its content is based on the [DataLad handbook](http://handbook.datalad.org) and others, and its technical backbone is [reveal.js](https://github.com/hakimel/reveal.js/).


**Slides** are written in HTML and are within this root folder.

**Casts** are remotely executed code casts, mostly written with [autorunrecord](https://pypi.org/project/autorunrecord/) in the [book](https://github.com/datalad-handbook/book) itself.

Casts can be executed using the tool ``cast_live`` found in ``tools/`` with the following invocation:

```sh
tools/cast_live casts/<cast-of-your-choice> 
```

``cast_live`` may not work on your system. It has only been used on Linux-based systems so far. Please file an issue if you encounter problems.
A number of casts from previous workshops can be found in ``casts/``. To find out how to create casts on your own machine, check out the [contributing instructions for the book for casts](http://handbook.datalad.org/en/latest/contributing.html#directives), or write them by hand - everything that starts within a ``run '<code here>'`` statement is executed on ``Enter``, everything within a ``say '<note>'`` is written to your private terminal as a note.
Note that ``cast_live`` may configure your keyboard layout to ``en-us``. If you are usually using a different keyboard layout, e.g., German, reset it using ``setxkbmap de``.

## DataLad/git-annex

If cloning from anywhere else than https://datasets.datalad.org copy of this dataset, you might need to add its content-containing git-annex via

```sh
git remote add --fetch datasets.datalad.org https://datasets.datalad.org/centerforopenneuroscience/talks/.git
```

to get access to the files stored on this remote (I didn't bother adding it as auto-enabling git-annex type=git remote yet).

## Advice for creating presentations

- ``clone`` the repository to your local computer and ``datalad get`` all subdatasets (``datalad get -n -r .``).
- For simple use cases such as viewing presentations it should suffice to open any raw ``.html`` in a browser of your choice. In this scenario, you *may* be able to generate a PDF from your slides by opening the presentation in a recent version of Chrome or Chromium, and append ``?print-pdf`` to the URL. Afterwards, you may be able to print to PDF from your browser.
  - **Gotcha:** the query string must come *before* the ``#`` fragment. reveal.js tests ``window.location.search``, so ``deck.html?print-pdf`` and ``deck.html?print-pdf#/4`` both work, but ``deck.html#/4?print-pdf`` **silently does nothing** -- the whole ``#/4?print-pdf`` is the hash, and ``search`` stays empty. Since normal navigation leaves a ``#/<slide>`` in the URL bar, appending ``?print-pdf`` to what you are looking at is exactly the case that fails. (``?view=print`` works too.)
  - In the print dialog set **Margins: None** and **Background graphics: on**, and choose a landscape paper size. Chrome's dialog cannot adopt the deck's own page size, so slides end up letterboxed on A4/Letter with white bands -- fine for sharing, not pixel-perfect. ``tools/mkpdf.py`` below avoids this.
- For more use cases and more reliable PDF exports, use [reveal.js's full setup](https://revealjs.com/installation/#full-setup). This requires a working installation of [Node.js](https://nodejs.org/):
 
```sh
# in the root dataset:
npm install
# to create a local npm server that automatically refreshes presentations
npm start
``` 
- A reliable method to export PDFs from a running npm server is ``decktape``. To generate PDFs from HTML run
```
docker run --rm -t --net=host -v `pwd`:/slides astefanutti/decktape http://localhost:8000/<presentation-of-your-choice.html> slides.pdf -s  1024x768
```
- More options, e.g., exports of individual slide screenshots, are in decktape's [documentation](https://github.com/astefanutti/decktape)
- If you have neither Docker nor a running npm server, ``tools/mkpdf.py`` exports any deck in this repo headlessly, straight from the ``.html`` file, needing only [uv](https://docs.astral.sh/uv/):
```sh
uv run --with playwright playwright install chromium   # once
uv run --with playwright python tools/mkpdf.py <presentation-of-your-choice.html>
```
  It writes ``<presentation>.pdf`` next to the deck (override with ``-o``). Page size is taken from the deck's own reveal ``width``/``height`` config, so 4:3 and 16:9 decks both come out right with no flags. Use ``--wait`` to give mermaid-heavy decks longer to render. **Do not commit the generated PDFs** -- they are derived artifacts; the live HTML is what gets shared.
- The tool [directpoll](https://directpoll.com/) works fantastic for virtual talks. See [#34](https://github.com/datalad-handbook/course/issues/34) or the template talk for info on how to use it
- We have made good experiences with live code demonstrations. The ``tools/cast_live`` script is used for this. It is highly advised to test whether this script works on your set-up beforehand! 

## License

CC-BY-SA: You are free to

   - share - copy and redistribute the material in any medium or format
   - adapt - remix, transform, and build upon the material for any purpose, even commercially

under the following terms:

   - Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

   - ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

### Not everything here is ours

Slides quote the world: screenshots of web pages and papers, figures,
cartoons, funder logos. Those are **not** covered by the CC-BY-SA above —
they belong to their original rights holders, and this repository cannot
and does not relicense them. The CC-BY-SA applies to the slides, diagrams
and text authored here.

Our own *code* is not under the slide license either: the helper scripts
in `tools/` and the CI workflows under `.github/` are **Apache-2.0**,
since Creative Commons licenses are not meant for software.

Which is which is recorded per-file, machine-readably, following the
[REUSE specification](https://reuse.software/):

| Where                                     | What                                                                            |
| ----------------------------------------- | ------------------------------------------------------------------------------- |
| `REUSE.toml`                              | per-path copyright and license annotations, with comments explaining each group  |
| `LICENSES/`                               | full license texts                                                              |
| `LICENSES/LicenseRef-ThirdPartyMixed.txt` | marker for third-party material whose provenance could not be reconstructed     |
| `LICENSES/LicenseRef-ThirdPartyLogo.txt`  | marker for third-party logos and trademarks (nominative use only)               |

The two `LicenseRef-*` entries are **markers, not license grants**. They
record "this is someone else's, and we could not determine whose" rather
than pretending to ownership — their `SPDX-FileCopyrightText` is
`NOASSERTION` for exactly that reason. If you want to reuse one of those
files, track down the original rights holder.

One caveat on that `NOASSERTION`: it reads as intended in `REUSE.toml` and
in this document, but `reuse spdx` currently emits it wrapped as
`FileCopyrightText: <text>SPDX-FileCopyrightText: NOASSERTION</text>`
rather than as the bare SPDX sentinel. An SBOM consumer may therefore treat
it as a literal copyright string instead of "unknown". Read `REUSE.toml` as
the authoritative statement.

Known provenance *is* recorded where we have it — for example the YODA
artwork (from [myyoda/poster](https://github.com/myyoda/poster), © 2018
Michael Hanke and Kyle Meyer, CC-BY-4.0) and the carrot/ReproNim-containers
artwork adapted from Michael Hanke's *"Carrots! Not sticks!"*
([slides](https://hedgedoc.psychoinformatics.de/edfuJiNaSNufM4trL8_HhA#/),
CC-BY per the author). Corrections and additions are very welcome —
please open an issue or a PR.

Check compliance with:

```sh
uvx --from 'reuse==6.2.0' reuse lint
```

(The version is pinned to match `.pre-commit-config.yaml`; the counts below
are version-dependent.)

#### Caveat: `reuse lint` only sees about half of this repository

[REUSE specification 3.3](https://reuse.software/spec-3.3/) excludes
"Symlinks and files with no data (zero-byte)" from *Covered Files*, and
`reuse` implements that by skipping every symlink unconditionally. This is
a git-annex dataset, so **282 of its tracked files are symlinks** — most of
`pics/` — and the linter neither checks nor counts them. Together with the
submodules, the license files and `REUSE.toml` itself, which the spec also
excludes, only **300 files out of roughly 590 tracked** are actually
checked. A green `300 / 300` from `reuse lint` therefore means "the 300
files it looks at are fine", not "the repository is fully covered".

The annotations in `REUSE.toml` still describe the annexed files correctly;
they are simply not machine-verified here. Upstream has been aware of this
since 2022 — see [reuse-tool#627](https://codeberg.org/fsfe/reuse-tool/issues/627)
and the long-stalled draft [PR #764](https://codeberg.org/fsfe/reuse-tool/pulls/764),
which needs a specification change before it can land.
