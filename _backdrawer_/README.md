# `_backdrawer_/` — shelved talk prototypes

A parking spot for talk **drafts, prototypes, and outlines** that are not
currently being prepared for a venue but should not be lost — either
because the spine is reusable, the title may be picked up later, or the
deck embodies a framing we may revisit.

Decks here are **not linked** from `INDEX.md`'s active inventory in the
usual way; instead, `INDEX.md` lists them under a dedicated *backdrawer*
section so the catalog stays honest about what is live vs. parked.

## Convention

- Files keep their original name (`<TALK-ID>.html`, etc.). Do **not**
  rename — when/if the deck is revived, the same filename can move back
  to the repository root and its published URL
  (`https://datasets.datalad.org/centerforopenneuroscience/talks/<TALK-ID>.html`)
  works again without rebuilding QR codes or rewriting external links.
- While actively editing a shelved deck (e.g. previewing through
  `npm start`), symlink it into the top directory so the asset paths
  (`pics/...`, `reveal.js/...`, `css/...`) resolve:
  ```bash
  ln -s _backdrawer_/202x-mvc-stack.html .
  # edit / preview as usual
  rm 202x-mvc-stack.html   # remove the symlink when done
  ```
  Don't commit the symlink.
- When promoting a shelved deck to active status, **move** the file back
  to the root (`git mv _backdrawer_/<TALK-ID>.html <TALK-ID>.html`) and
  update its `INDEX.md` entry from the backdrawer block back into the
  main per-talk inventory.

## Currently parked

- `202x-mvc-stack.html` — *MVC at the stack scale: what makes the open-
  (neuro)science stack compose*. Outline-only stub. The MVC framing is
  also carried as a 4-slide mini-section inside
  `../2026-usrse-con-talk.html` (HI+AI → MVC → Monday checklist), which
  remains live; the standalone deck was shelved when no venue picked it
  up.
