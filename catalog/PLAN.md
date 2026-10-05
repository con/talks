# Plan: formal talk records (`talks.yaml`) → index.html, the CON website, and Zenodo

Status: **proposal, for review** (2026-10-05; revised after the first review
comments). In this repo nothing is implemented yet. The schema addition for
events is drafted in datalad-concepts (§5.1). This file fixes the target, the
design decisions and the order of work.

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

1. generate `index.html` with a script (no AI). `INDEX.md` is retired:
   `talks.yaml` itself is the inventory, and the slide-reuse hints move into it
   (D6);
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

**Events are records of their own, and talks point to them.**

- A talk is linked to the event(s) it was presented at, the same way a person
  is linked to the group they belong to. Dates, web page, place and nesting
  (conference → session) are properties of the event.
- The link itself is qualified. It can carry *when* (at any precision) and
  *where* (e.g. a room) the talk was given, so pointing at the conference is
  enough (decided).
- That makes events usable beyond talks:
  - the "New Event" issues filed in [con/cierge](https://github.com/con/cierge);
  - an "Events" page on the website later.
- `xyzri` has no event concept, so this needs a minimal schema addition.
  It is **drafted** on the fork `yarikoptic/datalad-concepts`, branch
  `claude/serene-cray-ozqirg` (commits `419c37a` and `db21eb2`, not yet
  pushed; §5.1). It adds:
  - an `XYZEvent` class;
  - an `XYZEventType` classifier;
  - a qualified `presented_at` relation (`XYZPresentation`: event,
    `at_time`, `at_location`, `roles`; short-cut mapping `bibo:presentedAt`),
    from publications and documents to events.
- Route (decided): first a PR against the fork, then upstream
  (psychoinformatics-de). It may later move under the ORINOCO-Lite org.
- Talks use `kind: fabio:Presentation` (decided), in line with
  psychoinformatics-site-specific.
- `catalog/samples/` shows all of this on five real talks. The talks are
  exported to `xyzri` records that validate against the drafted schema (§7).

**So "right away" for the talk records, and "once Event lands" for the
website.**

- Until the `XYZEvent` concept is available to ORINOCO-Lite, an interim
  export would follow what psychoinformatics-site-specific does today (§1.3).
- That means a talk becomes an `XYZPublication` (kind `fabio:Presentation`)
  whose `generated_by.at_location` is a title-only `XYZPublicationVenue` of
  kind `bibo:Conference`.
- It works, but it loses the event's dates, URL, place and nesting.

Why the records are not native `xyzri` from day one:

- **(a) The schema can't express events or recordings yet.** `xyzri`
  (demo-research-information, *UNRELEASED*, pinned by ORINOCO-Lite at
  datalad-concepts `cb6c791`) has no event concept: the draft above is not
  upstream yet. `XYZFile` also has no URL slot.
- **(b) It would bypass review and provenance.** con-site-specific's
  canonical store is *reviewed* records with *machine-provenance overlays*,
  fed by sources and adapters. A hand-kept `xyzri` corpus here would skip
  both.
- **(c) Records here also hold things the website doesn't need.** Spine,
  reusable highlights and story arc are authoring aids for this repo.

**Scope (decided):** talks by **all CON members**, not only Yarik's. For
example, Cody Baker's BBQS STAMPED talk is in scope.

**Membership is dated (D10).** A talk belongs to CON's collection when at
least one author or presenter was a CON member on the presentation date.

- Membership is recorded once, on the person records in con-site-specific,
  as a dated relation to CON.
- When someone leaves, an end date moves them to alumni/emeritus. Their later
  works then fall outside CON's collection automatically.

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

Both parts move into records. Part 2 becomes topic tags on per-talk reuse
highlights. `INDEX.md` can then be retired (D6).

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

**CON membership has no dates.**

- The site root (`XYZProject/site-root.yaml`) lists people through
  `associated_with`, with roles `marcrel:led` or `marcrel:ctb`.
- That list mixes CON staff with outside collaborators; Michael Hanke,
  Satrajit Ghosh and Jean-Baptiste Poline, for example, are `ctb`.
- There is no `started` or `ended` anywhere, and no person record has
  `delegated_by`.

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
  `marcrel:spk` (speaker) role appear nowhere in datalad-concepts or
  con-site-specific. psychoinformatics-site-specific does have such records;
  see below.
- Partial dates are fine: `at_time` is `W3CISO8601`, from `YYYY` up to a
  full datetime.

**How psychoinformatics-site-specific does it today.** This was read from
[ORINOCO-Lite/psychoinformatics-site-specific](https://github.com/ORINOCO-Lite/psychoinformatics-site-specific)
at `780e5fd`.

*Talks:*

- 13 `XYZPublication` records have `kind: fabio:Presentation`. There are also
  `fabio:ConferencePoster` and `bibo:AudioVisualDocument` records.
- Their `XYZBibliographicType` records include:
  - `fabio:Presentation` and `fabio:ConferencePoster`;
  - `bibo:Slideshow` and `bibo:Slide`;
  - `bibo:AudioVisualDocument`;
  - `bibo:Conference`.

*The conference:*

- In one talk, it is
  `generated_by: {object: obo:GSSO_006807, at_location: xyzrins:publication-venues/<uuid>, at_time: '2026-05-08'}`.
  - `obo:GSSO_006807` is an `XYZActivity` record, "Conference presentation
    (activity)".
  - The venue is an `XYZPublicationVenue` with `kind: bibo:Conference` and
    **only a title**.
- The other talks name no event at all.
- So a conference ends up shoe-horned into a publication venue: no dates, no
  URL, no place, no nesting. The draft `XYZEvent` fixes exactly this.

*Group membership with dates:*

- It lives on the **site root** (`xyzrins:.`, the "Psychoinformatics"
  project): `associated_with` lists 27 people.
- The roles are:
  - `marcrel:rtm` (Research team member);
  - Student (`obo:AGRO_00000374`);
  - Research assistant (`obo:ICO_0000080`);
  - Intern;
  - `marcrel:led` (Lead);
  - IT project manager.
- Many of those associations carry `started` and/or `ended` dates; for
  example, 3 research team members have both, and 4 students have `ended`.
- `delegated_by` on person records is used for something else: employers
  (role "Employer", 28 of 59 people) and supervisors.
- This is the precedent for dated CON membership (D10).

*Presenters and events:*

- Talk records mark the presenter with an `attributed_to` role of
  `obo:CRO_0000100` ("Presenter").
- "Distribits 2024" (2024-04-04 to 04-06) and "Distribits 2025"
  (2025-10-23 to 10-25), both in Düsseldorf, are modeled as `XYZProject`
  records. They have `kind: bibo:Conference`, organizers (`marcrel:orm`), and
  are `part_of` a "Distribits" project.
- That is a second existing workaround for the missing event concept.

**con/cierge** (`9881d2d`) is "temporal itemization for the CON roadmap".

- Its only issue template, "New Event", has one required free-text field,
  "Event: drop links and/or describe this event".
- Issues are added to project `con/8`.
- The issues themselves were not read: the repo is not attached to this
  session. Which fields they carry (dates, links, the project's custom
  fields) is still to be checked.

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
- `events`: slug, name, acronym, URL, kind, location, start and end, plus:
  - `part_of`, for nesting (session → conference; series → webinar);
  - an optional link to the con/cierge issue;
  - an optional `zenodo` deposit policy (community, fixed publication date,
    license);
- `topics`: slug, title, and the reusable assets for that topic (the
  "Asset:" lines of today's topic lookup);
- `video_archives`: name, base URL, layout, UI URL template.

They avoid repeating facts. For example, distribits 2024 hosts two of our
talks, and US-RSE'26 hosts a talk plus posters and a BoF. Each registry also
maps onto its own record type later.

**A presentation is the talk's qualified relation to an event.**

- It points at the conference, or at a session within it when the session
  is known.
- It carries the date or datetime of the talk, and optionally a room.
- Presenters are marked by the `obo:CRO_0000100` role on the talk's
  attribution (§5).
- Talk-slot events are not needed.

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
- `xyzrins:events/<event-slug>`, with nested slots at
  `xyzrins:events/<event-slug>/<slot>`;
- `xyzrins:videos/<youtube-id>` for recordings.

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

**D6. INDEX.md is retired**

- `talks.yaml` is the per-talk inventory, and `index.html` is its rendered
  view.
- The editorial reuse notes move into each talk's `reuse:` block (renamed
  from `index:`):
  - `spine` and `notes`;
  - `highlights`, each `{text, slide: '#/<n>/<m>', topics: [...]}`, where
    `slide` is the reveal.js fragment.
- The topic-wise lookup becomes data. Each "steal a slide for X from file §
  section" pointer becomes a topic tag on that talk's highlight, and the
  per-topic "Asset:" lists go into the `topics` registry.
- `index.html` gains a generated "Reusable slides by topic" section, so
  humans keep the lookup. AI authoring reads `talks.yaml` directly.
- After migration:
  - `CLAUDE.md` and `SOUL.md` references move from `INDEX.md` to
    `talks.yaml`;
  - `INDEX.md` is removed (git history keeps it).
- The `reuse:` block stays repo-internal and is never exported.

**D7. Generated files are committed and reproducible**

- `index.html` and the JSON Schema are regenerated with
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

**D10. Whether a talk is a "CON talk" follows dated membership**

- Membership is recorded **once, in con-site-specific**, as dated
  associations on the **site root** (`XYZProject/site-root.yaml`). It follows
  the psychoinformatics precedent:
  `associated_with: [{object: xyzrins:persons/<p>, roles: [marcrel:rtm], started: {at_time}, ended: {at_time}}]`.
  - Roles can be `marcrel:rtm`, a student or intern role, or `marcrel:led`.
  - An `ended` date makes a person alumni/emeritus.
  - `delegated_by` stays for employers and supervisors, as psychoinformatics
    uses it.
- A talk is in CON's collection if at least one author or presenter was a
  member on the presentation date. This is **computed, never stored**.
- Where it is used:
  - `validate` warns about talks that fall outside every membership window;
  - `zenodo push` submits only qualifying talks to community `con`;
  - back-fill (Zenodo ORCID search, Zotero) skips works by former members
    dated after they left, and works dated before a person joined.
- `talks.yaml` does not copy membership dates. Instead,
  `validate --site <con-site-specific checkout>` reads them; without that
  option, the check is skipped.
- Prerequisite in con-site-specific: on the site root, give CON members
  member roles and dates.
- Outside collaborators are listed there today as `marcrel:ctb`. They either
  move elsewhere, or simply stop counting as members because `ctb` is not a
  member role.

---

## 4. Work plan

### Phase 1: schema, seeded records, validation (this repo only; ~1 PR)

1. Write `catalog/talks.schema.yaml` with:
   - classes `TalkCatalog`, `Talk`, `Slides`, `Presentation`, `Recording`,
     `ArchivedCopy`, `ZenodoDeposit`, `ZenodoPolicy`, `Reuse`, `Highlight`,
     `Person`, `Event`, `Topic` and `VideoArchive`;
   - enums `TalkStatus`, `TalkKind`, `SlideFormat`, `EventKind` and `StoryArc`
     (the arcs in SOUL.md §7).

   Generate `talks.schema.json` from it.
2. Seed `talks.yaml` with **every** deck in §8, including `_backdrawer_/` with
   `status: shelved`:
   - move the INDEX.md per-talk prose verbatim into `reuse:` blocks, without
     rewording;
   - turn each topic-lookup pointer into a `topics` tag on the matching
     highlight;
   - move each topic's assets into the `topics` registry;
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
     a `[WiP]` prefix;
   - *(warnings only, with `--site`)* each talk falls inside some author's or
     presenter's CON membership window (D10).
4. Add pre-commit hooks (`check-jsonschema` plus a local `talks.py validate`)
   and `.github/workflows/catalog.yml`.

### Phase 2: generators (~1 PR)

1. `render` writes `index.html`, deterministic and ordered newest first.
   - It keeps the current CSS, which already rhymes with the CON site.
   - It adds event, date, presenters (when they differ from the authors), and
     links to source, live slides, PDF, video and archive copies.
   - It adds a "Reusable slides by topic" section built from the highlights'
     topic tags (D6).
   - It includes subdirectory decks (mechababs), and external talks when they
     have `listed: true`.
   - Drafts and shelved decks are hidden or badged.
   - It embeds **schema.org JSON-LD** (`PresentationDigitalDocument`, `Event`,
     `VideoObject`). This is the first machine-readable projection of the
     records, and it is cheap.
2. Run `render --check` in CI.
3. Update the docs and retire `INDEX.md`:
   - in `CLAUDE.md`, new-deck step 9 becomes "add or extend the `talks.yaml`
     record, then `catalog/talks.py render`", and the step-10 commit bundle
     gains `talks.yaml`;
   - point `CLAUDE.md` and `SOUL.md` references to `INDEX.md` at
     `talks.yaml`;
   - `git rm INDEX.md`;
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

**5A. Event concept in datalad-concepts.**

1. Drafted: commits `419c37a` and `db21eb2` on `yarikoptic/datalad-concepts`,
   branch `claude/serene-cray-ozqirg` (§5.1).
   - Next step: push and open a PR against the fork (decided). After review
     there, propose it upstream (psychoinformatics-de). The ORINOCO-Lite org
     may host it later.
   - The PR description should also cover:
     - the conference-as-`XYZProject` records in psychoinformatics-site-specific
       (migrate them to `XYZEvent`, or let `XYZEvent` point to a project);
     - the `W3CISO8601` anchoring bug (samples README §11) as a separate fix.
2. ORINOCO-Lite pins datalad-concepts through its `things-schemas` submodule,
   at `cb6c791`. Using `XYZEvent` on the site requires:
   - moving that pin to a commit that has the change (the fork branch, until
     upstream accepts it);
   - declaring `xyzri:XYZEvent` in the projection (`pages` or
     `unrendered_classes`), because every record class must be declared.

**5B. Records and adapter.**

1. `talks.py export-things` writes `xyzri` records to a scratch directory for
   review; nothing is committed here. It writes:
   - talks, with `presented_at`;
   - `XYZEvent` records for events and sessions;
   - recordings.

   `catalog/samples/export_sample.py` is the prototype.

   The mapping is in §5. Until 5A is usable, `--interim` emits the
   psychoinformatics-style form instead.
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
   - `XYZBibliographicType` records `fabio:Presentation` and
     `bibo:AudioVisualDocument`;
   - `XYZEventType` records (`bibo:Conference`, `bibo:Workshop`, local
     session/webinar types);
   - `XYZAgentRole` records `obo:CRO_0000100` (Presenter) and `marcrel:orm`.

   The records are copied from psychoinformatics-site-specific where one
   exists there, as the samples do.
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

**5C. Website: talks and events.**

1. Ask ORINOCO-Lite (`www-from-model`) for:
   - a talk page template;
   - an event page template;
   - "Talks" and "Events" sections in `projection.yaml` and the navigation.
2. A talk page embeds the video and lists the slides, archive copies, its
   event, and back-links to persons and projects. An event page lists the
   talks presented there.
3. Decide whether video and archive records live in con-site-specific,
   which is likely if non-talk videos (tutorials) are wanted. If so, the
   `video_archives` registry moves there and talks only reference it.

**5D. Events from con/cierge (later).**

1. Read the con/cierge "New Event" issues and project `con/8` (not yet
   attached to this session) to see which fields they carry.
2. A `cierge` source adapter turns those issues into `XYZEvent` candidates
   for con-site-specific.
3. The `events` entries in `talks.yaml` link to the same issue, so both
   sources resolve to one event PID.
4. At that point the event registry's home moves to con-site-specific, and
   `talks.yaml` only references event slugs.

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

- Phases 1 and 2 are self-contained and immediately useful: `talks.yaml`
  replaces INDEX.md, index.html is correct, and CI checks both.
- Phase 3 needs ReproTube/contube clones and network access.
- Phase 4 can start right after Phase 1.
- 5A is drafted; 5B can start as soon as Phase 1 lands, in interim form
  if needed; 5C waits on 5A; 5D waits on cierge access.
- Phase 6.1 is the only time-critical item, because of the US-RSE deadline.
  6.4 waits for 5B.

---

## 5. Mapping `talks.yaml` → `xyzri`

| `talks.yaml` | With the drafted Event concept (target) | Interim, without it (psychoinformatics-style) |
| --- | --- | --- |
| Talk | `XYZPublication`, `pid: xyzrins:talks/<id>`, `kind: fabio:Presentation`, `title`, `description` | same |
| authors | `attributed_to: [{object: xyzrins:persons/<slug>, roles: [marcrel:aut]}]` | same |
| presenters | role `obo:CRO_0000100` added to the presenter's attribution (presenter-only attribution if not an author) | same |
| projects | `generated_by: [{object: xyzrins:projects/<slug>}]`, as `datalad-joss-2021` does, so the talk is listed on the project page | same |
| topics | `about: [xyzrins:topics/<slug>]` | same |
| derived_from | `derived_from: [{object: xyzrins:talks/<parent>}]` (`EntityMixin`) | same |
| presentation | `presented_at: [{object: xyzrins:events/<event or session>, at_time: <date[time]>}]` (`XYZPresentation`) | `generated_by: [{object: obo:GSSO_006807, at_location: xyzrins:publication-venues/<event>, at_time: <date>}]` |
| session (when known) | `XYZEvent` with `part_of: [<conference>]` | — |
| event | `XYZEvent`: `title`, `kind` (`XYZEventType`, e.g. `bibo:Conference`), `started`/`ended`, `at_location`, web page via `identifiers` or a `foaf:homepage` attribute, `associated_with` organizers (`marcrel:orm`), `part_of` for sub-events | `XYZPublicationVenue`: `title`, `kind: bibo:Conference` (title only) |
| recording | `XYZDocument`: `kind: bibo:AudioVisualDocument`, `generated_by: [{object: <event>, at_time}]`, `derived_from: [{object: <talk>}]` (the event alone doesn't say which talk; §9 Q16), YouTube and archive URLs in `identifiers` | YouTube URL in the talk's `identifiers`, as `zotero-sfqu8qby` does |
| slides: live URL, source @ commit, PDF | `identifiers` (URL notations, as other records do) | same |
| DOI | `identifiers: [{schema_type: dlthings:DOI, notation: 10.5281/…}]` | same |
| `reuse:` block | not exported | not exported |

### 5.1 The drafted schema change

It lives on `yarikoptic/datalad-concepts`, branch `claude/serene-cray-ozqirg`,
in commits `419c37a` and `db21eb2`. The push is pending GitHub access.
Everything is in `src/demo-research-information/unreleased.yaml`.

**`XYZEvent`**

- Declared as `is_a: Thing` with the `ActivityMixin`.
- Exact mapping `schema:Event`; broad mapping `prov:Activity`.
- Slots:
  - `title`;
  - `started` and `ended`;
  - a multivalued `at_location`;
  - `part_of`, with range `XYZEvent`, for nesting;
  - `associated_with`, for organizers, chairs and speakers;
  - `used`, for the slides or poster;
  - `about`, with range `XYZTopic`;
  - `depiction`;
  - `kind`, with range `XYZEventType`.

**`XYZEventType`** is a classifier, e.g. `bibo:Conference`.

**`presented_at`** is a qualified relation: `is_a: influenced_by`, exact
mapping `bibo:presentedAt`, with range **`XYZPresentation`**.

- `XYZPresentation` is an `ActivityInfluence` with `InstantaneousEventMixin`,
  so it has:
  - `object`: the `XYZEvent`;
  - `at_time`;
  - `at_location`;
  - `roles`.
- `presented_at` is multivalued, inlined, and added to `XYZPublication` and
  `XYZDocument`.
- It mirrors `generated_by` → `Generation`. This lets a talk point straight at
  the conference and still state when (and in which room) it was given.

**Recordings need nothing new.** They name their event as the `generated_by`
activity. The samples add `derived_from` the talk, to say which talk was
recorded.

**Examples, each with a committed JSON conversion:**

- `XYZEvent-01-conference`;
- `XYZEvent-03-talk-slot`, showing that nesting works even though it is not
  required;
- `XYZPublication-03-presented-at`: `fabio:Presentation`, presenter role,
  and `presented_at` with `at_time`;
- `XYZDocument-03-recording`.

They come with new validation configs for `XYZEvent` and `XYZDocument`.

**Checks run locally** with linkml 1.11.1 plus the repo's patches, which is
the version ORINOCO-Lite pins:

- `make checkmodel/demo-research-information/unreleased`: lint and all
  generators are clean.
- `checkvalidation`: all valid configs pass.
- Negative checks reject:
  - `presented_at` on an `XYZProject`;
  - an unknown slot on an event;
  - a bare event reference in `presented_at` (it must be a qualified
    object).
- Re-converting the existing examples leaves them unchanged.
- codespell is clean.

**Deliberately not in the minimal change** (later, if needed):

- file URL slots (`dcat:accessURL` and `dcat:downloadURL` on `XYZFile`);
- `duration`;
- narrowing `XYZDocument.distributions` and `XYZDocument.about`;
- an output → grant relation (§9 Q10).

**Data records con-site-specific needs**, with no schema change:

- `XYZEventType`: `bibo:Conference`, `bibo:Workshop`, …;
- `XYZBibliographicType`: the talk kind and `bibo:AudioVisualDocument`;
- `XYZAgentRole`: `obo:CRO_0000100` (Presenter) and `marcrel:orm`.

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
| `kind: talk/webinar/…` | `kind: fabio:Presentation` | `metadata.resource_type.id: presentation` | poster → `poster`; recording → `video` |
| `title` | `title` | `metadata.title` | an event policy may dictate the title, e.g. "as submitted" |
| `description` (Markdown) | `description` | `metadata.description` (HTML) | rendered Markdown → HTML |
| `authors[]` → `people` | `attributed_to` + `marcrel:aut` | `metadata.creators[]`: `person_or_org` with `given_name`, `family_name`, `identifiers: [{scheme: orcid}]`, `affiliations: [{id: <ROR>}]` | default affiliations: CON `ror:04tfhh831` and Dartmouth `ror:049s0rh22` (from `XYZOrganization/con.yaml`); the person registry needs given and family names split |
| `presenters[]` beyond the authors | `obo:CRO_0000100` role on the attribution | `metadata.contributors[]` with role `other`, plus a note in `description` | DataCite has no "speaker" role |
| presentation `date` | `generated_by.at_time` | `metadata.publication_date`, plus `dates: [{type: other, description: presented}]` | an event can fix `publication_date` (US-RSE: 2026-10-19) |
| `event` → `events` | `XYZEvent` (interim: title-only venue) | `custom_fields["meeting:meeting"]`: `title`, `acronym`, `dates`, `place`, `url`, `session` | |
| — (always) plus `events.<e>.zenodo.community` | — | `communities`: `con`, plus the event's (e.g. `usrse26`); a review request on submit | `con` is the sync collection (§9 Q8) |
| `projects[]`, `topics[]` | `generated_by` project / `about` | `metadata.subjects[]` (free keywords) | |
| `grants[]` (new field, slugs = `xyzrins:grants/<slug>`) | not modeled yet: `funded_by` or `characterized_by schema:funding` (§9 Q10) | `metadata.funding[]`: `funder.id` (ROR), `award.number`, `award.title` | con-site-specific `XYZGrant` records lack a funder link; add one there, as a funder `XYZOrganization` with its ROR id |
| `license` (per talk; per export where it differs) | `rules` (things-rules); verify | `metadata.rights: [{id: <SPDX id, lowercased>}]` | must be stated per talk, never inherited (§9 Q9); an event policy (US-RSE: CC-BY-4.0) pre-fills it |
| live slides URL (derived) | `identifiers` / `XYZFile` access URL | `related_identifiers`: `isvariantformof`, scheme `url` | the HTML is a different format of the deposited PDF |
| source in this dataset at a commit | `XYZFile` + git id | `related_identifiers`: `isderivedfrom`, scheme `url`; GitHub blob URL at the commit | |
| `derived_from[]` (lineage) | `derived_from` | `related_identifiers`: `isderivedfrom` (the parent's DOI if it has one, else its URL) | |
| recordings: YouTube, archive copies | recording `XYZDocument` (§5) | `related_identifiers`: `issupplementedby`, resource type `video` | |
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
2. Port it to linkml-map once `export-things` exists (Phase 5B).

**Upstream implications.**

- datalad-concepts needs a recommended way to link an output to its funding
  grant(s), and grant → funder via ROR. Neither is used by any record today.
- con-site-specific person records need ORCIDs and split given/family names
  for creators.

---

## 7. Samples

The example that used to be inline here is replaced by
[`catalog/samples/`](samples/README.md). It has five real talks in the
planned `talks.yaml` format, with each value annotated by its source:

- `2026-usrse-con-talk`;
- `2026-repronim-YODA-BIDS-webinar`;
- `2025-distribits-YODA`;
- `2026-bbqs-stamped`;
- the Zotero-migrated `2016-ohbm-datalad`.

`samples/export_sample.py` is a prototype exporter. It maps them onto 23
`xyzri` records, laid out like con-site-specific.

- All 23 validate against the drafted schema.
- Every person, project, role and type they reference resolves to
  con-site-specific or to the samples.

The samples README lists what they revealed. The decisions still needed are
§9 Q16–Q20.

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
7. ~~Upstream route for the Event change?~~ **Decided:** first a PR against
   `yarikoptic/datalad-concepts`, then upstream. The push is still blocked
   (§10).
8. ~~A CON Zenodo community?~~ **Decided: it exists**, as `con`
   (<https://zenodo.org/communities/con>). It is the collection that talk
   records sync to and from (§6.3).
9. ~~License?~~ **Decided:**
   - the catalog itself (`talks.yaml` and the generated `index.html`) is
     CC-BY 4.0;
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
12. ~~Talk kind?~~ **Decided: `fabio:Presentation`**, in line with
    psychoinformatics.
13. ~~What `presented_at` points to?~~ **Decided: the conference** (or a
    session, when known). Date and time live on the qualified
    `presented_at`, so no talk-slot events are needed.
14. **Long-term home of events.** The proposal is con-site-specific, fed by
    con/cierge and `talks.yaml`. con/cierge needs attaching to a session so
    its issues and project fields can be read.
15. ~~Membership roles?~~ **Checked.** psychoinformatics uses dated
    site-root `associated_with`, with `marcrel:rtm`, student, research
    assistant, intern and `marcrel:led` roles (§1.3). D10 follows that.
    Still open: what happens to the outside collaborators listed as
    `marcrel:ctb` on CON's site root.

From the samples (`catalog/samples/README.md`):

16. **Recording → talk.** When `presented_at` points at a conference, a
    recording `generated_by` that conference does not say which talk it
    shows. Keep `derived_from: <talk>` on the recording (as the samples do),
    or use another relation?
17. **Free-text places.** `at_location` needs an IRI. Options:
    - place IRIs (Wikidata, GeoNames) for cities, with rooms as
      `schema:location` attributes;
    - everything as attributes;
    - a text slot upstream.
18. **Event ↔ project.** `XYZEvent.part_of` accepts only events, so
    distribits 2025 → `projects/distribits` uses `influenced_by` in the
    samples. Should the PR widen `part_of`, or is a series better modeled as
    an `XYZEvent` too?
19. **Fields with no `xyzri` slot yet:** `keywords` (→ `about` + `XYZTopic`
    records?) and `license` (`rules`?). Both are needed for Zenodo.
20. **PIDs and routes.**
    - TALK-IDs contain uppercase letters; check how site paths handle that.
    - Migrated Zotero talks keep `xyzrins:publications/…` PIDs, so talks
      would live under two route prefixes.

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
- con/cierge issues were not read; only its README and issue template were
  (§1.3).
- The datalad-concepts change was validated locally (§5.1). Pushing it to
  `yarikoptic/datalad-concepts` keeps failing with HTTP 403: the Claude
  GitHub App is not installed for that repository. Both commits are ready
  locally.
- psychoinformatics-site-specific facts come from a clone at `780e5fd`.
- The ORINOCO-Lite findings come from `orinoco-lite-dev` HEAD `992c917`.
  The CON downstream pins a different package commit (`1cbebd70`), and its
  `www-from-model` layouts were not inspected, so details of the adapter
  contract may differ slightly.
