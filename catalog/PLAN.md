# Plan: formal talk records (`talks.yaml`) → INDEX.md, index.html, and the CON website

Status: **proposal, for review** (2026-10-05). Nothing below is implemented
yet. This file fixes the target, the design decisions and the order of work.

## The goal

Replace the hand-curated catalog in `INDEX.md` with formal records for
every CON talk. Each record says where the talk can be found:

- as **sources** in this DataLad dataset;
- **rendered**, at <https://datasets.datalad.org/centerforopenneuroscience/talks/>
  or elsewhere;
- as **video**: on YouTube, and as annextube backups in
  [ReproTube](https://datasets.datalad.org/repronim/ReproTube/) and
  [contube](https://datasets.datalad.org/centerforopenneuroscience/contube/).

From those records we then:

1. generate `INDEX.md` and `index.html` with a script (no AI);
2. write a guide that humans and an AI skill follow to add and update
   records (shacl-vue forms later);
3. sync them into
   [ORINOCO-Lite/con-site-specific](https://github.com/ORINOCO-Lite/con-site-specific),
   which holds [datalad-concepts](https://concepts.datalad.org) `xyzri:`
   records, so talks show up on the CON website (preview:
   <https://dev.centerforopenneuroscience.org/>);
4. keep each talk's **Zenodo** deposit (DOI, creators, funders, conference,
   related links) in sync both ways, through a crosswalk between the records
   and the Zenodo REST API (§6). The crosswalk does not go through
   `CITATION.cff` or `.zenodo.json`.

---

## 0. Recommendation in brief

**`talks.yaml` is an authoring-friendly *source* with its own small LinkML
schema.** Its slots and identifiers are chosen to map one-to-one onto
datalad-concepts. It reaches con-site-specific **through an ORINOCO-Lite
source adapter**, the same way Zotero and `con/dump-research-info` already
do. We do not hand-write `xyzri:` records in this repo.

The answer to "eventually or right away?" is **eventually, in two tiers**:

- **Tier A, possible as soon as `talks.yaml` exists.** Export each talk as
  an `XYZPublication` with `kind: bibo:Slideshow`, with URLs (live slides,
  YouTube, DOI) as `identifiers` and the event as
  `generated_by.at_location` plus `at_time`. That is exactly how
  con-site-specific *already* stores talks that came in from Zotero (e.g.
  `XYZPublication/zotero-sfqu8qby.yaml`, the 2013 NeuroDebian talk, with a
  YouTube URL as an identifier). `XYZPublication` is rendered today. This
  tier needs no schema or theme change; it only adds one data record (the
  `bibo:Slideshow` type, §5).
- **Tier B, after a small upstream datalad-concepts addition.** This adds a
  real event record, file/URL distributions, recordings as their own
  documents, and a "talks" section on the site.

Why the records are not native `xyzri` from day one:

- **(a) The schema can't express events or recordings yet.** `xyzri`
  (demo-research-information, *UNRELEASED*, pinned by ORINOCO-Lite at
  datalad-concepts `cb6c791`) has no event, presentation or recording
  class, and `XYZFile` has no URL slot.
- **(b) It would bypass review and provenance.** con-site-specific's
  canonical store is *reviewed* records with *machine-provenance overlays*,
  fed by sources and adapters. A hand-kept `xyzri` corpus here would skip
  both.
- **(c) Records here also hold things the website doesn't need.** Spine,
  reusable highlights and story arc feed `INDEX.md` only.

**Scope (decided):** talks by **all CON members**, not only Yarik's. For
example, Cody Baker's BBQS STAMPED talk is in scope. The `people` registry
covers the whole team.

**Identifiers are shared from day one**, so the later sync is cheap:

- person slugs = `xyzrins:persons/<slug>`;
- project slugs = `xyzrins:projects/<slug>`;
- ORCID and GitHub handles;
- DOIs;
- YouTube ids.

**Zenodo** is a third projection of the same records, alongside `xyzri` and
the schema.org JSON-LD in `index.html`.

- It uses the **Zenodo (InvenioRDM) REST API directly, per talk**, not
  `CITATION.cff` or `.zenodo.json`. Those two describe *one deposit per
  repository release*, and CFF cannot express funders, conference details or
  rich relations.
- Sync is plan/apply: render, diff against the live record, update a draft.
  The records own the descriptive metadata; Zenodo owns record ids, DOIs,
  versions and file checksums.
- The talks crosswalk comes first, because the US-RSE slides are due on
  Zenodo by 2026-10-21. It is then lifted to a generic
  **`xyzri` ↔ Zenodo/DataCite** crosswalk, usable for publications, software
  and datasets as well (§6).

---

## 1. Review findings

### 1.1 This repository (`con/talks`)

**`INDEX.md` mixes two different things:**

1. a *per-talk inventory*:
   - catalog data: title, venue, date, format, presenters, a few video
     links;
   - editorial notes: spine, reusable highlights, companion directories;
2. a *topic-wise lookup*, an editorial map of where to borrow slides from
   across decks.

Only part 1 belongs in records. Part 2 stays hand-written (see D6).

**`index.html` exists already.** It is the landing page at
`datasets.datalad.org/.../talks/`. `tools/create_index.sh` builds it from
`ls 20*.html 20*.pdf` plus each deck's `<title>`. As a result:

- there are no dates, venues or videos;
- `2026-bbqs-stamped` shows up as a title;
- `2026-mcgill-mechababs/slides.html`, which lives in a subdirectory, is
  missing.

**HTML metadata cannot be the source of truth.** `<meta name="description">`
is often copy-pasted and stale:

- `2025-ca-origami-retreat.html` says "…ACNN_Workshop_2022";
- `2023-brain-dandi.html` says "a talk at LBL";
- both distribits 2024 decks say "distribits.live/ 2004".

**Sources also disagree.** For US-RSE'26:

- the program lists 5 authors;
- `2026-usrse/2026-usrse-con-talk-abstract.md` lists 6 (plus John A. Lee);
- Vadim Melnik's ORCID is known in the abstract but "TBD" in `SOUL.md` §8.

Records must be the place where such questions get decided.

**Talk "shapes" the schema must cover** (all present today):

| Shape | Example |
| --- | --- |
| reveal.js deck at the root | most talks |
| marp deck in a subdirectory, built with `datalad run` | `2026-mcgill-mechababs/` |
| Google Slides original plus annexed `.pptx`/`.pdf` exports | `2026-bbqs-stamped` (presented by Cody Baker, Yarik a co-author) |
| shelved stub | `_backdrawer_/202x-mvc-stack.html` |
| not a talk | `0000-zoom-background.html` |
| CON talks with slides **outside** this repo, already referenced from decks | ReproNim webinars of 2020 and 2024 under `datasets.datalad.org/repronim/artwork/talks/`, and Google Slides (§8) |

**Lineage between decks is real and already written down, in prose.** A new
`<TALK-ID>.html` is usually a fork of an older deck. For example,
`2026-repronim-YODA-BIDS-webinar` comes from `2025-distribits-YODA`, and
`2023-brain-dandi` from `2023-lbl-building-dandi`. This becomes a
`derived_from` relation.

**Video links are scattered.** Known so far:

- `EuKVapscUQ4`: `2025-distribits-YODA`, in its title slide and in INDEX.md;
- `1XbTbJ_P2x0`: the ReproNim webinar, linked from the AI-coding and BIDS
  2.0 decks.

Two ReproTube URL forms are in use:

- `ReproTube/web/#/channel/<chan>/video/<id>`, the collection UI;
- `ReproTube/DataLad/web/#/video/<id>`, the per-channel UI.

**Event metadata at session level is available for US-RSE'26:**

- the date is Mon 2026-10-19;
- the session is "AI Assisted Code Development", in the Willow Glen Room;
- a **Zenodo deposit** is mandated, so the slides will get a DOI. DOIs are
  therefore first-class identifiers for a talk.

US-RSE'26 also sets rules for that deposit
(`2026-usrse/USRSE26_AuthorCameraReady+ZenodoGuidance.md`):

- it goes into community `usrse26`;
- resource type is "Presentation";
- publication date is fixed to 2026-10-19;
- ORCIDs are requested;
- slides are due by **2026-10-21**;
- the license is "leave default CC-BY 4.0". This repo's `LICENSE` is
  CC-BY-SA 4.0, but individual talks and materials may carry their own
  licenses (decided, §9 Q9).

So events impose deposit policy, and this crosswalk must handle it.

The talk abstract is already deposited as
<https://zenodo.org/records/22783262>. It is listed in CON's Zenodo
community **`con`** (<https://zenodo.org/communities/con>), which is the
collection that talk records sync to and from (decided, §9 Q8 and Q11).
Both URLs come from Yarik; this session could not fetch them (§10).

**Every older deck already has a slot for a slides DOI.** Each one carries a
commented-out `Slides: DOI 10.5281/zenodo.6346849 (Scan the QR code)`
block. It was inherited from the DataLad-course template; the DOI and the
HHU QR image belong to that course, not to these talks.

**Dates** can be seeded from `git log --diff-filter=A` per deck (§8). These
are lower bounds only, so the schema must allow partial dates.

**Infrastructure:**

- `.pre-commit-config.yaml` exists, used only by snapper on one file;
- there is no `.github/` and no CI;
- helper scripts live in `tools/`.

### 1.2 con-site-specific and the ORINOCO-Lite pipeline

Read from con-site-specific, `ORINOCO-Lite/orinoco-lite-dev` (HEAD
`992c917`) and `con/dev-centerforopenneuroscience.org`.

**Records:**

- They live in `metadata/records/<Class>/<slug>.yaml` and use PIDs of the
  form `xyzrins:<collection>/<slug>`.
- Collections today: `persons/`, `projects/`, `publications/`, `topics/`,
  `grants/`, `organizations/` and `source-adapters/<id>/v<n>`.
- Records are hand-editable ("direct human edits are ordinary Git
  commits").
- Machine provenance goes into mirrored overlays under
  `metadata/overlays/machine-provenance-annotations/`, with
  `pav:importedFrom` and `pav:importedBy`.

**Schema and validation:**

- The schema is ORINOCO-Lite's `things-schemas` submodule at datalad-concepts
  `cb6c791`. That is the same commit as the `yarikoptic/datalad-concepts`
  checkout used for this review.
- Validation is LinkML: `linkml==1.11.1` plus dump-things-service, which
  converts each record to TTL.
- SHACL ships only for the shacl-vue `/edit/` page.

**Sources and adapters:**

- Each source has `sources/<id>/source.yaml`, which the adapter owns.
  Optional `policy/`, `evidence/` and `content/` subdirectories sit next
  to it.
- Reviewed dispositions (`accept`, `reject` or `defer`, plus a
  `github-comment:<id>` review link) are stored per PID in
  `curation-records/<id>.yaml`.
- Each adapter has an identity record, `XYZInstrument/source-adapter-<id>-v<n>.yaml`.

**Adapter mechanics (current package):**

- The entry point is `extensions/source-adapters/<id>/review.py::build_candidate_plan()`
  in the *downstream* site repo.
- CON's existing `source.yaml` files still name `metadata_adapter.py` and
  `candidates.py`, from an older layout.
- It runs through the `curation-review.yml` workflow, triggered by
  `workflow_dispatch` or a `/curation submit` comment, and is wrapped in
  `datalad run`.
- A plan holds at most 225 candidates.
- **The source revision is not pinned in `source.yaml`.** It is recorded in
  a `Curation-Source: {commit, repository, source_roots: {path: tree-sha}}`
  commit trailer.
- **The downstream may only have the gitlinks `site-specific` and
  `sourcedata/www-from-model`.** So `con/talks` cannot be a submodule; the
  adapter fetches it at a revision.

**Rendering:**

- Rendered by default: `XYZDataset`, `Objective`, `Topic`, `Project`,
  `Person`, `Publication` and `Instrument`.
- **`XYZActivity`, `XYZDocument` and `XYZFile` are "unrendered"**: valid
  records with no pages.
- The route is the PID minus `xyzrins:`, so `xyzrins:talks/<TALK-ID>` would
  be served at `/talks/<TALK-ID>/`.
- A `site-specific/projection.yaml` can replace the default class → template
  map. CON has none yet.
- Menus are set in `tool.orinoco.site.navigation`.
- Layouts come from the `www-from-model` submodule, which was not checked out
  in this review.

**Talks are already in the store.** 34 `XYZPublication` records carry
`kind: bibo:Document`, imported from Zotero. The Zotero snapshot
(`sources/zotero/content/snapshot.json`, fetched 2026-08-26) has no item of
Zotero type `presentation`. Talks and posters are `document` items, and
only the free-text `extra` field says which is which.

Items whose `extra` field says they are talks:

| Zotero key | On site as | Year | Title (abbreviated) | `extra` says | Material (item `url`) |
| --- | --- | --- | --- | --- | --- |
| `5Z7A6KRC` | `zotero-5z7a6krc` | 2015 | Overview of statistical evaluation techniques adopted by publicly available MVPA… | OHBM, Honolulu. Talk | `pymvpa.org/files/OHBM2015_Halchenko.pdf` |
| `ABZE6DSN` | `zotero-abze6dsn` | 2015 | Clustering cortical searchlights based on shared representational geometry | Oral presentation, OHBM, Honolulu | — |
| `4J5D6V7H` | `zotero-4j5d6v7h` | 2016 | Resources for practicing PR4NI – pragmatic cursory overview | OHBM, Tutorials, Geneva. Talk | `pymvpa.org/files/OHBM2016_Halchenko_resources.pdf` |
| `7AHRXD2X` | `zotero-7ahrxd2x` | 2016 | DataLad – decentralized data distribution… | OHBM, Geneva. Talk | `pymvpa.org/files/OHBM2016_Halchenko_datalad.pdf` |
| `QHQKTYYQ` | `zotero-qhqktyyq` | 2016 | DueCredit – automagically collect citations… | OHBM, Geneva. Talk | — |
| `M5E9BT5H` | `zotero-m5e9bt5h` | 2018 | ReproIn: automatic generation of shareable, version-controlled BIDS datasets… | Poster and talk, OHBM, Singapore | — |
| `7U85ZJ95` | `zotero-7u85zj95` | 2018 | Variability of the Neuroimaging Results Across OS, and How to Avoid it | Talk, annual meeting of the Biological Psychiatry | — |
| `HUPZV3B5` | **not on site** | 2026-03 | Guidelines for Reproducible Research (STAMPED) | Talk, Virtual BBQS Workshop | YouTube `8NTWKHer5Zo` |

- `HUPZV3B5` is this repo's `2026-bbqs-stamped`. It sits in the Zotero
  "External" collection, which the site's Zotero source does not include.
  This is how that talk's video id became known.
- Three items do not state a type in `extra`. They need a human decision:
  - `SFQU8QBY` (2013, NeuroDebian; its only URL is YouTube `WhUrTRuMoFs`);
  - `HYWV9D2A` (2010, Cognitive Neuroscience Society annual meeting,
    Montreal);
  - `QLTPV7JM` (2014, CRCNS PI meeting, Tempe).
- The other 19 meeting-related `document` items say "Poster". They are out
  of scope for talks (§9 Q3).

This makes **ownership and dedup between Zotero and `talks.yaml`** a real
design point (D9).

**Join keys for people:** only 2 of 35 person records carry an ORCID
(`xyzri:ORCID`). 33 carry a GitHub handle (`creator: rrid:SCR_002630`).

### 1.3 datalad-concepts `xyzri` (demo-research-information/unreleased)

**A talk deck fits `XYZDocument` best.**

- It has `distributions`, `part_of`, `kind` (an `XYZBibliographicType`),
  `attributed_to`, `generated_by`, `derived_from` and `about`.
- But it is unrendered, and its `distributions` is not narrowed to
  `XYZFile`.

**`XYZPublication` is rendered**, and it has `kind`, `about` (an
`XYZTopic`), `attributed_to`, `generated_by` and `derived_from`. But it has
**no `distributions` and no `part_of`**.

**An event would have to be an `XYZActivity`.**

- That gives `name`, a `part_of` limited to `XYZActivity`, and `started`/`ended`
  as `{at_time, at_location}`, plus `associated_with` and `used`.
- It cannot be `part_of` a project; for example, `distribits-2024` cannot be
  part of `projects/distribits`.
- It has no title and no direct location.

**Other gaps:**

- There is **no URL slot** for files or distributions. The `landing_page`
  slot exists only in demo-research-assets. Records put URLs into
  `identifiers` or `attributes` with `foaf:homepage`.
- `bibo:Slideshow`, `bibo:AudioVisualDocument`, `bibo:presentedAt` and the
  `marcrel:spk` (speaker) role appear **nowhere** yet.
- Partial dates are fine: `at_time` is `W3CISO8601`, from `YYYY` up to a
  full datetime.

### 1.4 annextube (video backups)

These findings come from reading the `con/annextube` code. The live archives
could not be fetched from this session (§10).

**Single-channel archives:**

- Video directories are named `{year}/{month}/{date}_{sanitized_title}`, so
  **a path cannot be derived from a video id**.
- `videos/videos.tsv` (in git, not annex) maps the id to the path. Its
  columns include `video_id`, `title`, `published_at`, `duration`,
  `source_url`, `path`, and the first line of `description`. Full
  descriptions are in `videos/video_fulldescriptions.json`.
- Each video directory holds `metadata.json`, `video.mkv` (annex `addurl`),
  captions and `comments.json`.

**Collections** such as ReproTube:

- have one subdataset per channel, named after the @handle (e.g. `DataLad/`);
- have a top-level `channels.tsv`;
- share one `web/`.

**Web routes:**

- `#/channel/<channel_dir>/video/<id>[?t=<sec>]` in a collection;
- `#/video/<id>` in a single-channel archive.

So the **UI URL *can* be derived** from the base, channel and id.

**Reverse links already exist.** A per-video `extra_metadata.json` with
`related_resources: [{url, title, relation_type, resource_type_general,
resource_type}]` (DataCite vocabulary, e.g. `IsSupplementedBy`) is merged
into `metadata.json`. It is shown in the UI as "Related Resources". This
lets a video page link back to its slides.

**There is no query CLI and no JSON-LD.** Discovery means reading
`channels.tsv` and `videos.tsv`, either from a `datalad clone` (no annexed
content needed) or over HTTPS.

---

## 2. Record model (conceptual)

```
Talk  (the work = a slide deck; id = TALK-ID = deck filename stem)
 ├─ authors[]          → Person         credit for the content
 ├─ projects[]/topics[]→ Project / Topic (con-site-specific slugs)
 ├─ derived_from[]     → Talk (lineage) | URL
 ├─ grants[]           → Grant (con-site-specific slugs; for Zenodo `funding`)
 ├─ license            per talk (and per export where it differs); no default
 │                     inherited from the repo LICENSE
 ├─ slides             source path in this dataset; rendered URL (derived);
 │                     exports (PDF/PPTX); original (e.g. Google Slides)
 ├─ zenodo             record id, DOI, concept DOI (owned by Zenodo; §6)
 └─ presentations[]    each delivery (usually one)
      ├─ event         → Event
      ├─ date, session, presenters[] → Person (may differ from authors)
      ├─ commit        optional: dataset state "as presented"
      └─ recordings[]  YouTube id (+ optional start/end offsets)
           └─ archived_in[] → VideoArchive + channel dir
```

Three small **registries** live in the same file, next to the talks:

- `people`: slug, name, ORCID, GitHub handle;
- `events`: slug, name, acronym, URL, kind, location, start and end, plus
  an optional `zenodo` deposit policy (community, fixed publication date,
  license);
- `video_archives`: name, base URL, layout, UI URL template.

They avoid repeating facts. For example, distribits 2024 hosts two of our
talks, and US-RSE'26 hosts a talk plus posters and a BoF. Each registry also
maps onto its own record type later.

---

## 3. Design decisions

Each decision comes with a recommendation; veto or adjust any of them in
review.

**D1. Format and location**

- `talks.yaml` sits at the repo root. It is one mapping with the keys
  `people`, `events`, `video_archives` and `talks` (a list).
- The schema, tooling and guide go in `catalog/`, which also holds this plan.
- Rejected alternatives:
  - per-talk files: they scatter the registries, and not every talk has a
    companion directory;
  - JSON: harder to hand-edit.

**D2. LinkML schema**

- The schema is `catalog/talks.schema.yaml`.
- Its `slot_uri`s point at the dlthings, schema.org, DCTERMS or PROV terms
  that the adapter will emit.
- `gen-json-schema` produces `catalog/talks.schema.json`, which is committed.
  Validation then runs through the `check-jsonschema` pre-commit hook, so
  there is no heavy LinkML dependency in CI.
- `gen-shacl` is used later for shacl-vue (Phase 4).

**D3. Identifiers**

| What | Identifier |
| --- | --- |
| Talk | `id` = TALK-ID; it is already the key of the published URL; never reused |
| Talk hosted elsewhere | an `id` in the same `<YYYY>-<venue>-<topic>` style, plus explicit URLs |
| Person, project | con-site-specific slugs |
| Video | the bare YouTube id |
| Slide deposit | DOI |

Exported PIDs:

- `xyzrins:talks/<TALK-ID>`;
- `xyzrins:events/<event-slug>`;
- and in Tier B, `xyzrins:videos/<youtube-id>`.

People carry `orcid` and `github` where known. We should backfill ORCIDs into
con-site-specific person records; 33 of 35 lack one.

**D4. Store minimal facts and derive URLs**

Derived in one place, the renderer:

- the live deck URL:
  `https://datasets.datalad.org/centerforopenneuroscience/talks/<source path>`;
- YouTube URLs;
- archive UI URLs.

Explicit `url:` fields are only for what cannot be derived: Google Slides,
external hosting and event pages. If an archive UI changes its routing, one
template changes.

**D5. Dates and states**

- Partial dates are allowed: `2023`, `2023-06` or `2023-06-14`.
- `status` is one of `draft`, `scheduled`, `given` or `shelved`.
- `kind` is one of `talk`, `lightning`, `webinar`, `keynote`, `tutorial` or
  `template`.
- `0000-zoom-background` becomes `kind: template` and is never listed.

**D6. INDEX.md is half generated**

- The per-talk inventory is rewritten between
  `<!-- BEGIN GENERATED from talks.yaml -->` and `<!-- END GENERATED -->`.
- The intro, the slide-ID convention, the topic-wise lookup and "How to use
  this index" stay hand-written.
- Spine, highlights and notes move verbatim into each record's `index:`
  block. That block is repo-internal and never exported.
- Turning the topic lookup into data is a possible follow-up, not part of
  this plan.

**D7. Generated files are committed and reproducible**

- `INDEX.md`, `index.html` and the JSON Schema are regenerated with
  `datalad run uv run catalog/talks.py render`, following the mechababs
  `datalad rerun` precedent.
- CI and pre-commit run `render --check` and fail on drift.

**D8. Tooling**

- There is one script, `catalog/talks.py`, in stdlib Python plus PyYAML, with
  PEP 723 inline dependencies so `uv run` needs no setup.
- Its subcommands are `validate`, `render [--check]`, `find-videos` and
  `export-things`.
- Only `find-videos` and `validate --online` use the network, and neither
  runs in the per-PR CI path.
- `tools/create_index.sh` becomes a shim that calls `render`.

**D9. Dedup with Zotero**

- `talks.yaml` owns *talks* from now on.
- A record may carry `zotero: <item key>`. The talks adapter then either
  reuses that publication PID or the Zotero site policy excludes the item, so
  the website never shows a talk twice.
- To migrate the Zotero-held talks (§1.2 table):
  - add a `talks.yaml` record carrying `zotero: <key>`;
  - the talks adapter **keeps the existing PID**
    (`xyzrins:publications/zotero-<key>`), so site URLs stay stable;
  - in Zotero, change the item's type to `presentation`, so the Zotero
    source can exclude talks by type rather than by a hand-kept list.
- Until migrated, these talks stay as they are (§9 Q2).

---

## 4. Work plan

### Phase 1: schema, seeded records, validation (this repo only; ~1 PR)

1. Write `catalog/talks.schema.yaml` with:
   - classes `TalkCatalog`, `Talk`, `Slides`, `Presentation`, `Recording`,
     `ArchivedCopy`, `ZenodoDeposit`, `ZenodoPolicy`, `Person`, `Event` and
     `VideoArchive`;
   - enums `TalkStatus`, `TalkKind`, `SlideFormat`, `EventKind` and `StoryArc`
     (the arcs in SOUL.md §7).

   Generate `talks.schema.json` from it.
2. Seed `talks.yaml` with **every** deck in §8, including `_backdrawer_/` with
   `status: shelved`:
   - move the INDEX.md prose verbatim into `index:` blocks, without rewording;
   - fill dates from git and the title slides, partial where unsure;
   - add the known videos;
   - add the people from SOUL.md §8 and the US-RSE abstract.
3. `catalog/talks.py validate` checks the JSON Schema plus these repo
   invariants:
   - every root `20*.html` and every known subdirectory deck has a record,
     and every record's source path exists (checked via `git ls-files`, so
     annexed files without content pass);
   - references to `people`, `events` and `video_archives` resolve;
   - YouTube ids are unique unless deliberately shared;
   - *(warnings only)* non-draft root decks have a QR code
     `pics/<TALK-ID>-qrcode.png`;
   - *(warnings only)* the HTML `<title>` matches the record title, ignoring
     a `[WiP]` prefix.
4. Add pre-commit hooks (`check-jsonschema` plus a local `talks.py validate`)
   and `.github/workflows/catalog.yml`.

### Phase 2: generators (~1 PR)

1. `render` rewrites the INDEX.md generated block (D6).
   - The output is deterministic and ordered newest first.
   - Each entry gives title, status, event and date, and presenters if they
     differ from the authors.
   - Each entry links the source, live slides, PDF, video and archive copies,
     followed by the spine, highlights and notes.
2. `render` also writes `index.html`.
   - It keeps the current CSS, which already rhymes with the CON site.
   - It adds event, date and links.
   - It includes subdirectory decks (mechababs), and external talks when they
     have `listed: true`.
   - Drafts and shelved decks are hidden or badged.
   - It embeds **schema.org JSON-LD** (`PresentationDigitalDocument`, `Event`,
     `VideoObject`). This is the first machine-readable projection of the
     records, and it is cheap.
3. Run `render --check` in CI.
4. Update the docs:
   - in `CLAUDE.md`, new-deck step 9 becomes "add or extend the `talks.yaml`
     record, then `catalog/talks.py render`", and the step-10 commit bundle
     gains `talks.yaml`;
   - `README.md` gets one paragraph.

### Phase 3: videos, YouTube and annextube (~1 PR plus external PRs)

1. Fill the `video_archives` registry:
   - `reprotube`: a collection; `channel` is required.
   - `contube`: its layout must be confirmed (§9 Q4).
2. `talks.py find-videos` reads `channels.tsv`, `*/videos/videos.tsv` and
   `video_fulldescriptions.json`.
   - It reads from a local `datalad clone`, with no annex content needed, or
     over HTTPS.
   - It proposes matches:
     - a YouTube id already in a record → an archived copy;
     - a title similar to a talk's title, published near a presentation date;
     - a speaker's name in the title or full description.
   - It prints **proposed YAML** for a human or the skill to accept. It never
     edits `talks.yaml` silently.
3. `@centeropenneuro` has no annextube archive yet.
   - Preferred: back it up into contube, so contube becomes the index (one
     mechanism).
   - Fallback: a one-off `yt-dlp --flat-playlist -J`, outside CI.
4. `validate --online` runs on a schedule, not per PR. It checks that each
   archived id is present in that archive's `videos.tsv` and that YouTube ids
   still resolve.
5. Add back-links from the archives:
   - `talks.py` emits `extra_metadata.json` snippets of the form
     `related_resources: [{url: <live slides>, relation_type:
     IsSupplementedBy, resource_type_general: Text, resource_type: Slides}]`;
   - they are committed to ReproTube and contube in their own PRs;
   - a video page then links to its deck.

### Phase 4: guide for humans and an AI skill (~1 PR, can follow Phase 1)

1. `catalog/README.md` is the field guide. It covers:
   - each field (the table is generated from the schema, so it cannot drift);
   - one example per talk shape (§1.1);
   - when to create a new talk versus add a new presentation of an existing
     one;
   - how to record lineage, partial dates, co-presenters, Zenodo DOIs and
     Zotero keys.
2. `.claude/skills/talk-record/SKILL.md` is a deterministic procedure. Given a
   TALK-ID:
   - read the title slide (venue/date line, `<title>`, authors);
   - read the `git log` dates, the companion directory and the
     `20YY-<venue>/` docs;
   - run `find-videos`;
   - draft the record;
   - run `validate` and `render`;
   - **list every field that was inferred rather than read**, for a human to
     confirm.
3. Later, shacl-vue data entry from `gen-shacl` output. Either it edits
   `talks.yaml` directly, or (more likely) it edits the exported Things
   records in the ORINOCO-Lite editor. File this as an ORINOCO-Lite issue
   rather than build it here.

### Phase 5: con-site-specific and the website (cross-repo)

**5A. Tier A, no schema change.**

1. `talks.py export-things` writes `xyzri` records to a scratch directory
   (§5, column A) for review. Nothing is committed here.
2. In con-site-specific, add:
   - `sources/talks/source.yaml`, modeled on `sources/dump-research-info/`:
     ```yaml
     contract_version: 1
     id: talks
     repository: con/talks
     source_roots: [talks.yaml]
     provenance_identity: xyzrins:source-adapters/talks/v1
     decision_cache: site-specific/curation-records/talks.yaml
     ```
   - `XYZInstrument/source-adapter-talks-v1.yaml`;
   - `XYZBibliographicType/slideshow.yaml` (`pid: bibo:Slideshow`);
   - optionally `XYZAgentRole` `marcrel:spk`;
   - `policy/` holding the person mapping (if slugs ever diverge) and the
     Zotero dedup list (D9).
3. In the downstream site repo, add
   `extensions/source-adapters/talks/review.py`.
   - It reuses `export-things` logic: the adapter imports it, or vendors a
     pinned copy.
   - It fetches `con/talks` at a commit. The commit is recorded through the
     `Curation-Source` trailer, and the overlays carry
     `pav:importedFrom: https://github.com/con/talks/blob/<sha>/talks.yaml#<TALK-ID>`.
4. Result: talks are listed on the existing person and project pages, and
   possibly at `/talks/<id>/` through PID routing. That last point is
   inferred; check it with a build.

**5B. Tier B, richer model.**

1. Propose the minimal `xyzri` additions in §5 upstream
   (psychoinformatics-de/datalad-concepts), with this catalog as the
   motivating use case.
2. Ask ORINOCO-Lite (`www-from-model`) for a talk page template and a "talks"
   section in `projection.yaml` and the navigation. The talk page would
   embed the video and list the slides, archive copies and back-links to
   persons and projects.
3. Decide whether video and archive records live in con-site-specific, which
   is likely if non-talk videos (tutorials) are wanted. If so, the
   `video_archives` registry moves there and talks only reference it.

### Phase 6: Zenodo crosswalk and sync (details in §6)

1. **Pilot: the US-RSE'26 talk, due 2026-10-21.** This can run right after
   Phase 1, or by hand before Phase 1 if needed.
   - `talks.py zenodo render 2026-usrse-con-talk` emits InvenioRDM record
     JSON.
   - The target is the existing abstract record
     <https://zenodo.org/records/22783262>. US-RSE asks for slides to be
     added "as a revision", which means a **new version** of that record,
     staying in communities `usrse26` and `con`.
   - `zenodo diff` and `zenodo push --sandbox` run against
     `sandbox.zenodo.org`, then `push` creates the new-version draft for a
     human to publish.
   - The PDF is exported with decktape under `datalad run`.
   - The record id, version DOI and concept DOI are written back into
     `talks.yaml`.
2. **Generalize to every talk that has a `zenodo:` block.**
   - Add `zenodo pull`, which writes back DOIs and reports drift when someone
     edited the record on Zenodo.
   - Add a CI workflow, `zenodo-sync.yml`. On a push it runs a dry-run diff
     and posts it; on `workflow_dispatch` with `apply` it pushes. The token
     lives in the `ZENODO_TOKEN` secret.
   - A new record is never published automatically: DOIs are permanent.
3. **Back-fill from community `con`.**
   - List the records of the `con` community and match them to
     `talks.yaml` by DOI, then by title and date.
   - Propose `zenodo:` blocks for matches, and new talk records for
     unmatched `presentation` records.
   - Additionally, search by member ORCIDs for deposits that are not in the
     community, and propose adding them to it.
   - Dedup against Zotero's "CON Zenodo/OSF DOIs" collection, which
     con-site-specific already ingests (D9).
4. **Lift the crosswalk to `xyzri` ↔ Zenodo** (§6.4). It would be an
   ORINOCO-Lite export projection plus a `zenodo` source adapter, so the
   same mapping serves publications, software (`XYZInstrument`) and datasets.

**Order and dependencies:**

- Phases 1 and 2 are self-contained and immediately useful: a correct
  INDEX.md and index.html, plus CI.
- Phase 3 needs ReproTube/contube clones and network access.
- Phase 4 can start right after Phase 1.
- 5A can start as soon as Phase 1 lands; 5B waits on upstream.
- Phase 6.1 is the only time-critical item, because of the US-RSE deadline.
  6.4 waits for 5A.

---

## 5. Mapping `talks.yaml` → `xyzri`

| `talks.yaml` | A: today (renders as a publication) | B: target (needs upstream additions) |
| --- | --- | --- |
| Talk | `XYZPublication`, `pid: xyzrins:talks/<id>`, `kind: bibo:Slideshow`, `title`, `description` | `XYZDocument` (`distributions` narrowed to `XYZFile`, `about` narrowed to `XYZTopic`), or `XYZPublication` gaining `distributions` |
| authors | `attributed_to: [{object: xyzrins:persons/<slug>, roles: [marcrel:aut]}]` | same |
| projects | `generated_by: [{object: xyzrins:projects/<slug>}]`, as `datalad-joss-2021` does, so the talk is listed on the project page | same |
| topics | `about: [xyzrins:topics/<slug>]` | same |
| derived_from | `derived_from: [{object: xyzrins:talks/<parent>}]` (`EntityMixin`) | same |
| presentation (event, date) | an extra `generated_by` entry `{at_time: <date>, at_location: <event IRI>}`, as publications use a venue | an activity for the talk slot: `part_of` the event, `associated_with` presenters (`marcrel:spk`), `used` the talk; the talk gets `presented_at` (`bibo:presentedAt`) |
| event | only an IRI (the event URL) | **`XYZEvent`** (new): `title`, `at_location`, `started`/`ended`, `kind` from a new `XYZEventType` (`bibo:Conference`, `bibo:Workshop`, webinar…), `part_of` an `XYZEvent` or `XYZProject` (distribits) |
| slides: live URL, source @ commit, PDF | `identifiers` (URL notations, as Zotero-derived records do) | `XYZFile` per artifact, with new `access_url` (`dcat:accessURL`) and `download_url` (`dcat:downloadURL`) slots; git blob id in `identifiers`; PDF `derived_from` the HTML |
| DOI | `identifiers: [{schema_type: dlthings:DOI, notation: 10.5281/…}]` | same |
| recording | YouTube URL in the talk's `identifiers`, as `zotero-sfqu8qby` does | `XYZDocument` with `kind: bibo:AudioVisualDocument`, `generated_by` the talk-slot activity; one `XYZFile` per recording, with every copy (YouTube, ReproTube, contube) as access URLs; an optional `duration` (`schema:duration`) |
| presenters ≠ authors | lost (only authors survive) | `associated_with` with `marcrel:spk` on the talk-slot activity |
| `index:` block | not exported | not exported |

**Proposed upstream changes for B**, all in
`demo-research-information/unreleased.yaml`:

1. a new `XYZEvent` class plus an `XYZEventType` classifier;
2. a `presented_at` slot;
3. `access_url` and `download_url` on `XYZFile`;
4. on `XYZDocument`, narrow `distributions` and `about`, and add `depiction`;
5. optionally, `duration`.

**Data records** (no schema change): `bibo:Slideshow` and
`bibo:AudioVisualDocument` as `XYZBibliographicType`; `marcrel:spk` (and
`marcrel:orm`, `marcrel:vdg`) as `XYZAgentRole`.

---

## 6. Zenodo crosswalk and two-way sync

### 6.1 Why the REST API rather than CITATION.cff or `.zenodo.json`

**Granularity.** `CITATION.cff` and `.zenodo.json` drive Zenodo's GitHub
integration, which makes **one deposit per repository release**. We want
**one deposit per talk**, with new versions when a deck is updated.

**Expressiveness.** CFF has no funding field and no conference block, and
its relation types are poor.

The current InvenioRDM record API covers what the records hold:

- `creators` with ORCID and ROR affiliations;
- `funding` as a funder ROR plus an award number and title, accepted even
  when the award is in no registry;
- `related_identifiers` with DataCite relation types;
- `subjects`;
- `dates` with types;
- the `custom_fields["meeting:meeting"]` conference block: title, acronym,
  dates, place, url, session;
- `communities` and `rights`.

The legacy deposit API (`upload_type`, `conference_*`, `grants:
[{id: "<funder>::<award>"}]`) remains a fallback. Its grants must already
exist in the award registry.

**Optional extra.** A *single* `CITATION.cff` for the repository as a whole
(the "CON talks collection") could later be **generated** from `talks.yaml`,
but it is never a source.

> The InvenioRDM field names above come from knowledge of the API rather than
> from reading it in this session. Verify them against the Zenodo REST docs
> and `sandbox.zenodo.org` before the pilot.

### 6.2 Crosswalk: `talks.yaml` (and its `xyzri` image) → Zenodo record

| Record field | `xyzri` (§5) | Zenodo InvenioRDM | Notes |
| --- | --- | --- | --- |
| `kind: talk/webinar/…` | `kind: bibo:Slideshow` | `metadata.resource_type.id: presentation` | poster → `poster`; recording → `video` |
| `title` | `title` | `metadata.title` | an event policy may dictate the title, e.g. "as submitted" |
| `description` (Markdown) | `description` | `metadata.description` (HTML) | rendered Markdown → HTML |
| `authors[]` → `people` | `attributed_to` + `marcrel:aut` | `metadata.creators[]`: `person_or_org` with `given_name`, `family_name`, `identifiers: [{scheme: orcid}]`, `affiliations: [{id: <ROR>}]` | default affiliations: CON `ror:04tfhh831` and Dartmouth `ror:049s0rh22` (from `XYZOrganization/con.yaml`); the person registry needs given and family names split |
| `presenters[]` beyond the authors | `marcrel:spk` (Tier B) | `metadata.contributors[]` with role `other`, plus a note in `description` | DataCite has no "speaker" role |
| presentation `date` | `generated_by.at_time` | `metadata.publication_date`, plus `dates: [{type: other, description: presented}]` | an event can fix `publication_date` (US-RSE: 2026-10-19) |
| `event` → `events` | `at_location` (A) / `XYZEvent` (B) | `custom_fields["meeting:meeting"]`: `title`, `acronym`, `dates`, `place`, `url`, `session` | |
| — (always) plus `events.<e>.zenodo.community` | — | `communities`: `con`, plus the event's (e.g. `usrse26`); a review request on submit | `con` is the sync collection (§9 Q8) |
| `projects[]`, `topics[]` | `generated_by` project / `about` | `metadata.subjects[]` (free keywords) | |
| `grants[]` (new field, slugs = `xyzrins:grants/<slug>`) | Tier B: `funded_by` or `characterized_by schema:funding` (§9 Q10) | `metadata.funding[]`: `funder.id` (ROR), `award.number`, `award.title` | con-site-specific `XYZGrant` records lack a funder link; add one there, as a funder `XYZOrganization` with its ROR id |
| `license` (per talk; per export where it differs) | `rules` (things-rules); verify | `metadata.rights: [{id: <SPDX id, lowercased>}]` | must be stated per talk, never inherited (§9 Q9); an event policy (US-RSE: CC-BY-4.0) pre-fills it |
| live slides URL (derived) | `identifiers` / `XYZFile` access URL | `related_identifiers`: `isvariantformof`, scheme `url` | the HTML is a different format of the deposited PDF |
| source in this dataset at a commit | `XYZFile` + git id | `related_identifiers`: `isderivedfrom`, scheme `url`; GitHub blob URL at the commit | |
| `derived_from[]` (lineage) | `derived_from` | `related_identifiers`: `isderivedfrom` (the parent's DOI if it has one, else its URL) | |
| recordings: YouTube, archive copies | identifiers / Tier B video document | `related_identifiers`: `issupplementedby`, resource type `video` | |
| talk page on the CON website | — | `related_identifiers`: `isdescribedby` | once Phase 5 exists |
| deposited files | `distributions` → `XYZFile` | `files`: the PDF exported with decktape via `datalad run` (optionally also `.pptx`) | |
| `zenodo.{record, doi, concept_doi}` | `identifiers: [{schema_type: dlthings:DOI}]` | read back from the API | owned by Zenodo; never hand-edited except to seed |

### 6.3 Sync semantics ("automagically", but safely)

**Ownership.**

- `talks.yaml` owns all descriptive metadata.
- Zenodo owns:
  - record and concept ids, and the DOIs;
  - version history;
  - file checksums;
  - community review state.

**The Zenodo-side collection is community `con`.** Every talk deposit is
submitted there, in addition to any event community. `zenodo pull` also
reports `con` records that have no `talks.yaml` record, and the reverse.

**Plan/apply commands.**

- `zenodo render <id>` produces deterministic JSON.
- `zenodo diff <id>` normalizes the live record and diffs it against the
  render.
- `zenodo push <id>`:
  - creates a draft, or edits the published record's metadata;
  - uploads files only when they changed;
  - **never publishes unless `--publish` is given**.
- `zenodo pull` writes back DOIs and ids. Any other drift, such as a
  community curator editing the record, is reported for a human to resolve.

**File-change detection without downloading anything.** This repo uses the
`MD5E` annex backend, so the PDF's annex key already contains its md5.
Comparing it with Zenodo's file checksum decides between "metadata-only
edit" and "new version".

**After a push**, `git annex registerurl` adds the Zenodo file URL to the
PDF's key. The dataset then knows Zenodo as another content source, which is
the DataLad-native back-link.

**DOI before the talk.** Reserving the DOI on the draft makes it available
before the talk. The title slide can then show it again, reviving the
template's commented-out "Slides: DOI … (Scan the QR code)" slot. The QR
code stays on the live URL, per `CLAUDE.md`.

**Automation.**

- The CI dry-run diff runs on every change to `talks.yaml`.
- Applying requires explicit dispatch.
- Tests run against the sandbox.
- The token holds only the deposit scopes.

### 6.4 Lifting the crosswalk to the concepts level

The talks crosswalk is the first instance of a general need: `xyzri` records
↔ Zenodo, and more broadly DataCite, which also covers OSF and institutional
repositories.

**Where it belongs.**

- Export side: an **ORINOCO-Lite projection**.
- Import side: a **`zenodo` source adapter**. It searches by member ORCIDs
  and communities, and proposes `XYZPublication` / `XYZInstrument` /
  `XYZDataset` candidates through the usual curation review.

**How it would be written.** Describe the needed subset of the Zenodo record
schema in LinkML, then express the crosswalk declaratively as a
**linkml-map** transformation spec. That gives a reviewable mapping artifact
instead of code, and an inverse spec for the import side.

**Order.**

1. Write the talks crosswalk first, as plain Python in `catalog/talks.py`.
   Structure it field by field, mirroring the §6.2 table.
2. Port it to linkml-map once the Tier A `xyzri` export exists.

**Upstream implications.**

- datalad-concepts needs a recommended way to link an output to its funding
  grant(s), and grant → funder via ROR. Neither is used by any record today.
- con-site-specific person records need ORCIDs and split given/family names
  for creators.

---

## 7. Example `talks.yaml` (target shape)

Values marked `VERIFY` are not confirmed yet. The abstract and highlights are
abbreviated.

```yaml
people:
  yaroslav-halchenko: {name: Yaroslav O. Halchenko, orcid: 0000-0003-3456-2493, github: yarikoptic}
  cody-baker:         {name: Cody Baker, orcid: 0000-0002-0829-4790}
  austin-macdonald:   {name: Austin Macdonald, orcid: 0000-0002-8124-807X}
  isaac-to:           {name: Isaac To, orcid: 0000-0002-4740-0824}
  vadim-melnik:       {name: Vadim Melnik, orcid: 0009-0007-3981-0798}

events:
  usrse-2026:
    name: "US-RSE'26: Research Software Engineers Conference"
    acronym: US-RSE'26
    url: https://us-rse.org/usrse26/
    kind: conference
    start: 2026-10-19                    # VERIFY full span
    zenodo:                              # deposit policy imposed by the event
      community: usrse26
      publication_date: 2026-10-19
      license: CC-BY-4.0                 # community default; see §9 Q9
  distribits-2025:
    name: distribits 2025
    url: https://distribits.live/
    kind: conference
    start: 2025-10                       # VERIFY exact days and location
  bbqs-2026-workshop:
    name: BBQS virtual workshop
    kind: workshop
    online: true
    start: 2026-03-11

video_archives:
  reprotube:
    title: ReproTube
    base: https://datasets.datalad.org/repronim/ReproTube
    layout: collection
    video_url: "{base}/web/#/channel/{channel}/video/{id}"

talks:
- id: 2026-usrse-con-talk
  title: "Reuse, Compose, Extend, Standardize, Automate: Two Decades of RSEing Open (Neuro)Science at CON"
  kind: talk
  status: scheduled
  # program lists 5 authors; the abstract also lists john-a-lee: decide here
  authors: [yaroslav-halchenko, cody-baker, austin-macdonald, isaac-to, vadim-melnik]
  description: >-
    …abstract from 2026-usrse/2026-usrse-con-talk-abstract.md…
  projects: [neurodebian, pymvpa, datalad, bids, dandi, con-duct, con-tinuous, yoda]
  arc: reuse-compose-extend-standardize
  derived_from: [2024-distribits-datalad, 2022-nih-compcore, 2025-distribits-YODA]
  license: CC-BY-4.0                     # per talk; matches the US-RSE deposit policy
  grants: []                             # xyzrins:grants/<slug>; the deck's Acknowledgements
                                         # shows only NIH/NSF/BMBF logos, no award numbers
  slides:
    format: revealjs
    source: 2026-usrse-con-talk.html     # live URL is derived from this
    exports: [2026-usrse-con-talk.pdf]   # decktape, produced with `datalad run`
  zenodo:                                # filled in by `talks.py zenodo pull`
    record: 22783262                     # the abstract deposit (communities usrse26, con)
    # doi / concept_doi: pulled from the record; not copied by hand
  companions: [2026-usrse/]
  presentations:
  - event: usrse-2026
    date: 2026-10-19
    session: AI Assisted Code Development (Willow Glen Room)
    presenters: [yaroslav-halchenko]
  index:                                 # INDEX.md only; never exported
    spine: >-
      the five-verb spine (Reuse / Compose / Extend / Standardize / Automate) …
    highlights:
    - Title slide (per `SOUL.md` §3).
    - '"Two decades, five verbs" intro slide (NEW).'

- id: 2025-distribits-YODA
  title: "Pragmatic YODA: overview of YODA principles and their wild life encounters"
  kind: talk
  status: given
  authors: [yaroslav-halchenko]
  projects: [yoda, datalad, con-duct, reproman]
  arc: yoda-principle-a-day
  slides: {format: revealjs, source: 2025-distribits-YODA.html}
  presentations:
  - event: distribits-2025
    date: 2025-10                        # VERIFY exact day
    presenters: [yaroslav-halchenko]
    recordings:
    - youtube: EuKVapscUQ4
      archived_in: [{archive: reprotube, channel: DataLad}]

- id: 2026-bbqs-stamped
  title: "Guidelines for Reproducible Research (STAMPED)"
  kind: talk
  status: given
  authors: [cody-baker, yaroslav-halchenko]
  slides:
    format: google-slides
    url: https://docs.google.com/presentation/d/1yC412amV-j3BUfZ8Aq0aPEay93mnvmbo833BfNwuI_8/
    exports: [2026-bbqs-stamped.pdf, 2026-bbqs-stamped.pptx]
  companions: [2026-bbqs-stamped/]
  presentations:
  - event: bbqs-2026-workshop
    date: 2026-03-11
    presenters: [cody-baker]
```

**Tier-A export of `2025-distribits-YODA`** (sketch; the `schema_type` of
inlined objects is omitted for brevity):

```yaml
pid: xyzrins:talks/2025-distribits-YODA
schema_type: xyzri:XYZPublication
kind: bibo:Slideshow
title: 'Pragmatic YODA: overview of YODA principles and their wild life encounters'
attributed_to:
- {object: xyzrins:persons/yaroslav-halchenko, roles: [marcrel:aut]}
generated_by:
- {object: xyzrins:projects/yoda}
- {object: xyzrins:projects/datalad}
- {at_time: '2025-10', at_location: 'https://distribits.live/'}     # the presentation
identifiers:
- {notation: 'https://datasets.datalad.org/centerforopenneuroscience/talks/2025-distribits-YODA.html'}
- {notation: 'https://www.youtube.com/watch?v=EuKVapscUQ4'}
- {notation: 'https://datasets.datalad.org/repronim/ReproTube/web/#/channel/DataLad/video/EuKVapscUQ4'}
```

---

## 8. Seed inventory (what Phase 1 encodes)

Dates in *italics* are the date each deck was first committed (`git log
--diff-filter=A`). They are lower bounds, not event dates. "?" means unknown
or still to be verified.

| TALK-ID | Event / kind | Date | Format | Known video |
| --- | --- | --- | --- | --- |
| `2026-usrse-con-talk` | US-RSE'26, AI Assisted Code Development; 5–6 authors | 2026-10-19 | reveal.js (draft) | — (Zenodo record 22783262, abstract) |
| `2026-mcgill-mechababs` | McGill neuroscience group | 2026-08-11 | marp, in a subdirectory | ? |
| `2026-bbqs-stamped` | BBQS virtual workshop; presenter Cody Baker | 2026-03-11 | Google Slides + `.pptx`/`.pdf` | YouTube `8NTWKHer5Zo` (from Zotero `HUPZV3B5`) |
| `2026-brainhack-containers-mashup` | BrainHack 2026, containers | *2026-06-11* | reveal.js (2 slides) | ? |
| `2026-nih-bids2.0` | NIMH DSST Lunch & Learn | 2026-06-02 | reveal.js | ? |
| `2026-ca-origami-retreat-aicoding` | CA Origami Retreat 2026 | *2026-02-24* | reveal.js | ? |
| `2026-repronim-YODA-BIDS-webinar` | ReproNim Webinar | 2026-02-06 | reveal.js | YouTube `1XbTbJ_P2x0`; ReproTube `ReproNim` |
| `2025-distribits-YODA` | distribits 2025 | *2025-10-21* | reveal.js | YouTube `EuKVapscUQ4`; ReproTube `DataLad` |
| `2025-ca-origami-retreat` | CA Origami Retreat 2025 | *2025-02-27* | reveal.js | ? |
| `2024-distribits-datalad` | distribits 2024 | *2024-03-29* (event 2024-04) | reveal.js | ? |
| `2024-distribits-datalad-name` | distribits 2024, lightning | 2024-04? (added *2024-08-14*) | reveal.js | ? |
| `2023-brain-dandi` | BRAIN Initiative talk | *2023-06-27* | reveal.js | ? |
| `2023-brain-dandi-imgdatasrc` | short DANDI talk | *2023-06-29* | reveal.js | ? |
| `2023-bids-dicom` | DICOM WG-16 meeting | *2023-06-14* | reveal.js | ? |
| `2023-lbl-building-dandi` | LBL talk | *2023-04-09* | reveal.js | ? |
| `2022-tx-big-neuroscience` | ACNN Workshop 2022 (Texas) | *2022-09-15* | reveal.js | ? |
| `2022-nih-compcore` | NIH SSCC pitch | *2022-09-12* | reveal.js | ? |
| `202x-mvc-stack` | shelved stub | — | reveal.js, `_backdrawer_/` | — |
| `0000-zoom-background` | template, not a talk | — | reveal.js | — |

**External candidates** (slides hosted elsewhere and referenced from our
decks; §9 Q2):

| Talk | Date | Slides | Video |
| --- | --- | --- | --- |
| ReproNim webinar, "Version control your data and computation using containers, DataLad and ReproMan…" | 2020-06-05 | Google Slides | YouTube `ix3lC6HGo-Q` |
| ReproNim webinar, "Reproducible Execution of Data Collection/Processing" | 2020 | `repronim/artwork/talks/webinar-2020-reprocomp/` | YouTube `dwBtrpI2iS0` |
| ReproNim webinar, ReproFlow | 2024-06 | `repronim/artwork/talks/webinar-2024-reproflow/` | ? |

Talks already recorded in Zotero: the eight items in the §1.2 table, plus
the three whose type is not stated. Migrate them per D9.

---

## 9. Open questions

1. ~~Whose talks?~~ **Decided: all CON members.** `con/talks` holds the
   records for every CON talk, including talks whose slides live
   elsewhere.
2. **How far back, and in what order?** Proposed order:
   1. this repo's decks;
   2. the eight Zotero talks (§1.2), keeping their PIDs (D9);
   3. the three Zotero items of unstated type, after a human decides;
   4. ReproNim-artwork and Google Slides talks (§8).

   Confirm, or reorder.
3. **Posters and BoFs?** `posters/`, `2026-usrse/*poster*`, `2026-sfn/` and
   `2026-brain-initiative/` could use the same schema with `kind: poster` or
   `kind: bof`. Now, or later?
4. **contube layout.** Is contube a single-channel archive of
   `@centeropenneuro`, or a collection? This decides its URL template.
   Should `@centeropenneuro` be added there if it isn't already?
5. **"As presented" pinning.** Create git tags `talk/<TALK-ID>/<date>` at
   delivery time, or is the optional `commit:` field enough?
6. **Zotero dedup policy (D9).** For an overlapping talk, should the talks
   adapter reuse the Zotero PID, or should Zotero exclude the item?
7. **Upstream route for Tier B.** File the `XYZEvent` / `presented_at` /
   file-URL proposal as a datalad-concepts issue now, or after Tier A shows
   the website side working?
8. ~~A CON Zenodo community?~~ **Decided: it exists**, as `con`
   (<https://zenodo.org/communities/con>). It is the collection that talk
   records sync to and from (§6.3).
9. ~~License?~~ **Decided:**
   - the catalog itself (`talks.yaml` and the generated `INDEX.md` /
     `index.html`) is CC-BY 4.0;
   - each talk states its own `license`, and an export or material can
     differ from it;
   - nothing is inherited from the repo `LICENSE`.

   Still open: how a deposited PDF states the terms of borrowed images
   (`pics/borrowed/`).
10. **Funding linkage.** Should talks list `grants` explicitly, as slugs of
    con-site-specific `XYZGrant` records, or inherit them from their projects?
    Either way, grant records need funder ROR links for Zenodo `funding`, and
    datalad-concepts needs a recommended output → grant relation.
11. ~~The US-RSE Zenodo record?~~ **Known:**
    <https://zenodo.org/records/22783262> (abstract). The pilot adds the
    slides as a new version (Phase 6.1).

---

## 10. Review notes and limits

- The network policy of the session that produced this plan blocked
  `datasets.datalad.org`, `zenodo.org`, `www.youtube.com` and
  `dev.centerforopenneuroscience.org`. As a result:
  - the annextube findings come from reading code, not from inspecting
    ReproTube or contube;
  - the Zenodo field names in §6 come from memory and must be checked
    against the API;
  - the video ids in this plan come only from this repo and from the Zotero
    snapshot in con-site-specific; none were looked up;
  - no content of those sites is assumed.
- Implementing Phases 3 and 6 needs these hosts allowed:
  - `datasets.datalad.org`;
  - `zenodo.org` and `sandbox.zenodo.org`;
  - `www.youtube.com`;
  - `dev.centerforopenneuroscience.org`.
- The ORINOCO-Lite findings come from `orinoco-lite-dev` HEAD `992c917`.
  The CON downstream pins a different package commit (`1cbebd70`), and its
  `www-from-model` layouts were not inspected, so details of the adapter
  contract may differ slightly.
