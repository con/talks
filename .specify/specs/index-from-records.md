# Mint `index.html` from CON records

Status: **done** (2026-10-17) for phases 1–4, with these deviations:
records were committed straight to the store's `main` (no PR); talks are
linked to their projects (so they show on project pages); events stay
text (`bibo:presentedAt`) with a `# TODO(event)` comment in each record;
`tools/mk_index.py` also exports `talks.yaml`; the reader was not shared
with `mk_ack_eras.py`, and parity is on the listed entries and their
order (same-date ties may differ), not bytes — the page now also shows
each entry's date and venue. Stage 1 (the `## Chronology` table in
`INDEX.md`, read by `tools/create_index.sh`) was the starting point.

## Goal

Every talk and poster in this repository is a reviewed record in the CON
record store (`sourcedata/con-site-specific`, i.e.
[ORINOCO-Lite/con-site-specific](https://github.com/ORINOCO-Lite/con-site-specific)),
and `index.html` is generated from those records, the same way
[con/centerforopenneuroscience.org](https://github.com/con/centerforopenneuroscience.org)
generates `whoweare` and `projects`. The Chronology table in `INDEX.md`
then goes away: one source of truth, shared with the website.

Success criteria:

1. Every row of today's Chronology table has a record, and both store gates
   pass (`tools/linkml_check.sh`, `tools/validate_records.py`).
2. The new renderer reproduces the current `index.html` **byte for byte**
   from records alone, before anything is deleted.
3. Adding a talk is: add a record (+ evidence) in the store, bump the
   submodule, `datalad run` the renderer. No hand-edited list anywhere.

## How the website did it, and what we do differently

The website (see its `.specify/specs/metadata-flow.md`) went in three steps:

| Commit    | Date       | Step                                                                                                       |
| --------- | ---------- | ---------------------------------------------------------------------------------------------------------- |
| `bfa89fe` | 2026-10-11 | generators + tests, and intermediate extracts (`content/people/*.yaml`, `content/projects/*.yaml`) scraped from the hand-written pages, plus `enrich_*`/`records_from_page.py` to push them into records |
| `a2366f1` | 2026-10-11 | store added as a submodule; `dd6d10d`, `507013c` first renders from records                                |
| `3905d0d` | 2026-10-12 | migration scripts and 104 extract files deleted, after both pages rebuilt byte-identical from records      |

Their pipeline: `scripts/conrecords.py` (plain `yaml.safe_load` over
`metadata/records/XYZ*/`, `CON_RECORD_STORE` override, `write_page()` that
refuses non-well-formed output), one `render_*.py` per page, `make project`
wrapped as `make run-project` = `datalad run --explicit` after a
`check-store-pinned` guard (store pointer must be committed), so history is
paired `store: …` / `[DATALAD RUNCMD] project: …` commits.

**We can go directly.** Their intermediate YAML existed because the data
was locked inside hand-written HTML. Ours is already extracted: the
Chronology table *is* the intermediate, it is small (23 rows), and it was
built for this. So: table → records with a one-off script (not committed,
or committed and removed in the same series, as `3905d0d` did), then the
renderer, then parity, then delete the table.

Lessons carried over from their history:

- Data flows one way (store → generated output). Never fix generated
  `index.html` by hand; fix the record.
- Silent rendering losses happened there (dropped people, wrong order,
  lost anchors). Test for them: count of entries, order, every root deck
  covered.
- Do not cite this repo's *later* generated `index.html` as evidence for a
  record — that would be the records citing themselves. Evidence comes
  from the decks, READMEs, event sites, git history of the decks.

## Modelling (decide first — this is shared data)

The schema (`demo-research-information` + `things-*`) has no Talk, Poster
or Event class. Existing precedent: the SfN 2015/2016 posters are
`XYZPublication` with `kind: bibo:Document`, `generated_by[0].at_time` = the
conference's first day, `generated_by[0].object` = a project, venue only in
the citation text.

Proposal:

| Need                  | Encoding                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| the thing             | `XYZPublication`, pid `xyzrins:publications/talk-<TALK-ID>` / `poster-<stem>`                                                  |
| talk vs. poster       | `kind` + `characterized_by` `dcterms:type`: `bibo:Slideshow` for talks, `fabio:ConferencePoster` for posters (BIBO has no poster); new `XYZBibliographicType` records for both. Re-type the SfN 2015/2016 posters too, or leave them `bibo:Document` (decide) |
| when presented        | `generated_by[0].at_time` — `YYYY`, `YYYY-MM` or `YYYY-MM-DD` (the validator's W3CISO8601 accepts all three), with evidence     |
| where / which event   | now: attribute `bibo:presentedAt` (text). Later, optionally: `XYZActivity` records for events, linked from `generated_by`       |
| host institution      | `generated_by[0].at_location` (IRI, e.g. a ROR), only when meaningful — not for Zoom meetings                                 |
| live slides URL       | attribute `foaf:homepage` = `https://datasets.datalad.org/centerforopenneuroscience/talks/<path>`, also as an `identifiers` entry |
| print PDF of a poster | attribute `dcat:downloadURL` (second link on `index.html`)                                                                     |
| who                   | `attributed_to` with `marcrel:aut` and `marcrel:spk` (presenter); new `XYZAgentRole` record for `marcrel:spk`                  |
| which project         | `generated_by[].object` = the project(s) the talk is about (`datalad`, `bids`, `dandi`, …), else site-root `xyzrins:.`         |
| WiP / not listed      | no record until it is presented; or an attribute the renderer skips (decide)                                                    |

Questions for the store maintainers, before writing 23 records:

1. Are talks wanted in this store at all, and as `XYZPublication`? (The
   alternative, an `XYZActivity` per event, is more correct but is a new
   modelling area.)
2. `fabio:ConferencePoster` / `bibo:Slideshow` as new bibliographic types —
   acceptable vectors?
3. **Side effect on the website**: its project pages list publications
   linked via `generated_by`. Talk records linked to `datalad`, `bids`, …
   would start appearing there. Wanted (probably), or should the website
   renderer filter by `kind`?
4. Existing data issues found on the way, to fix or file: `dcterms:issued`
   values like `2015/10` are not ISO and are not checked by the validator;
   SfN 2015 evidence has `kind: recollection` under `assertions` (rule 3 in
   `docs/metadata-curation.md` says recollections are `pending`).

## Evidence for dates

Every `at_time` needs an assertion in
`sources/curation-evidence/XYZPublication/<slug>.yaml`
(`format: con-association-evidence-v1`; `path`, `value` equal to the record,
`bound`, `kind`, `source`, `locator`, `quote`, `confidence`, `captured`).
From the Chronology table's *Date from* column:

| Date from (Chronology) | Evidence                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| title slide / README   | `kind: publication`, `bound: exact`, `confidence: certain`, locator = file + commit         |
| event program / site   | `kind: publication`, `bound: exact` (or month), `confidence: certain`/`approximate`         |
| git dates only         | `confidence: approximate`, `bound: upper` (presented after the deck was written, roughly); note the commit range. Better: replace with the real day before migrating |

Rows to confirm by a human first: `2024-distribits-datalad-name.html`
(git says 2024-08, INDEX.md says distribits 2024 = April), the two US-RSE'26
posters (session day), and all git-only dates.

## Phases

1. **Store prep** (PR to `ORINOCO-Lite/con-site-specific`)
   - answer the modelling questions above;
   - add `XYZBibliographicType` (Slideshow, ConferencePoster) and
     `XYZAgentRole` (`marcrel:spk`) records;
   - → verify: both gates pass; website renders unchanged (its
     `make project` + diff).
2. **Records** (same or a follow-up PR)
   - one-off script: Chronology rows → `XYZPublication` YAML + evidence
     skeletons; then hand-review each (people, projects, venue text);
   - mechababs (`2026-mcgill-mechababs/slides.html`) gets a record too —
     the renderer can skip it while its content is unpublished, or publish it;
   - → verify: both gates pass; one record per Chronology row
     (count + path set compared by a check script).
3. **Renderer** (this repo)
   - fix `.gitmodules`: `branch = enh-temporal-associations` → `main`
     (the checkout is on `main`, the named branch is 14 commits behind);
   - `tools/conrecords.py`: port the website's reader (`attrs`, `one`,
     `write_page`); move `tools/mk_ack_eras.py` onto it (it has its own
     copies today);
   - `tools/mk_index.py`: records with a talks-repo `foaf:homepage` →
     `index.html`, same HTML/CSS as `create_index.sh` emits today;
   - `Makefile` target `index` + `run-index` (`datalad run --explicit`,
     inputs = store records, output = `index.html`) with the
     `check-store-pinned` guard;
   - pytest tests (`@pytest.mark.ai_generated`): ordering, year grouping,
     poster tag + PDF link, every root `20*.html`/`20*.pdf` covered or
     explicitly excluded, well-formed output;
   - → verify: output byte-identical to the stage-1 `index.html`.
4. **Switch over**
   - delete `tools/create_index.sh` and the Chronology table (leave a
     one-line pointer to the store in `INDEX.md`; per-talk prose stays);
   - update `CLAUDE.md` "Workflow for creating a new deck" (step 9/10:
     add the store record + evidence, bump submodule, `make run-index`)
     and the tools table in `INDEX.md`;
   - → verify: `make run-index` from a clean clone reproduces `index.html`.
5. **Optional, later**
   - event records (`XYZActivity`) and per-talk pages;
   - list CON talks/posters that are *not* in this repo (SfN 2015/2016,
     OHBM…) on `index.html` too, linking out;
   - generate the `INDEX.md` per-talk headings/venue lines from records.

## Not doing

- No intermediate YAML layer in this repo (the table already is one).
- No library dependency (dump-things, linkml) in the renderer — plain YAML,
  as on the website.
- No change to deck files or their URLs.
