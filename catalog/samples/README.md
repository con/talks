# Sample talk records, for reviewing `../PLAN.md`

These files show what `PLAN.md` currently proposes. They are applied to a
few real talks, so the design can be reviewed on concrete records before
anything is implemented.

| File | What it is |
| --- | --- |
| `talks.yaml` | Five talks in the planned source format (PLAN §2, §3), plus the `people`, `events`, `video_archives` and `topics` registries. Each value carries a comment naming its source; unknown values are left out. |
| `../talks.schema.yaml` | **Draft** LinkML schema for `talks.yaml` (PLAN D2). It is the only schema file; no generated JSON is stored. |
| `../talks.py` | **Draft** tool (PLAN D8). Only `validate` exists so far: JSON Schema checks plus checks a schema cannot express (references, tracked files, unique ids, and con-site-specific slugs with `--site`). |
| `export_sample.py` | A prototype of `talks.py export-things` (PLAN Phase 5B). It maps `talks.yaml` onto `xyzri` records, following PLAN §5. |
| `xyzri/<Class>/*.yaml` | Its output, laid out like con-site-specific `metadata/records/`. |
| `validate.sh`, `check_refs.py` | Validate `talks.yaml` (via `../talks.py validate`), then the `xyzri/` records against the drafted schema, then report references in `xyzri/` that resolve to no record. |

The five talks were picked to cover the shapes the plan must handle:

| Talk | Shape |
| --- | --- |
| `2026-usrse-con-talk` | scheduled; presented in a session; Zenodo record; 5 authors |
| `2026-repronim-YODA-BIDS-webinar` | webinar within a series; `derived_from` another deck; YouTube plus ReproTube copy |
| `2025-distribits-YODA` | conference with known dates; YouTube plus ReproTube copy; event linked to a project |
| `2026-bbqs-stamped` | Google Slides with annexed exports; presenter differs from the author list; Zotero duplicate (`HUPZV3B5`); recording archived on contube (a single-channel archive) |
| `2016-ohbm-datalad` | a talk migrated from Zotero (`7AHRXD2X`) that keeps its existing site PID |

## Regenerate and validate

```bash
python3 export_sample.py talks.yaml xyzri
./validate.sh <datalad-concepts checkout> [<con-site-specific checkout>]
```

`validate.sh` needs a datalad-concepts checkout with the drafted schema:

- the repo is `yarikoptic/datalad-concepts`, branch `claude/serene-cray-ozqirg`
  (commits `419c37a` and `db21eb2`);
- it must be switched to local imports (`make imports-local`);
- linkml 1.11.1 must be installed (the version ORINOCO-Lite pins), with the
  repo's `tools/patch_linkml` applied.

Result at the time of writing:

- **`talks.yaml`: 0 errors.** The 4 warnings are `derived_from` parents that
  have no record in the sample.
  - `talks.py` validates it directly against the LinkML schema (closed).
  - Deliberately broken copies are rejected for each of these:
    - an unknown field;
    - a bad date;
    - a bad YouTube id;
    - a bad enum value;
    - a missing title;
    - an unknown person or event;
    - an untracked slide file;
    - a collection archive without a channel;
    - an unquoted year;
    - a license outside the `License` enum;
    - an unknown organizer;
    - a malformed DOI.
- **All 23 `xyzri` records validate.**
- With con-site-specific given, every person, project, role and type
  reference resolves.
- The only unresolved references are four `derived_from` parents
  (`xyzrins:talks/2022-nih-compcore` and others). Those talks are not in this
  sample.

## What the samples show (input for finalizing PLAN.md)

### 1. `presented_at` → conference is enough for the talk itself

- `presented_at` is now a qualified relation:
  `{object: <event>, at_time, at_location, roles}`.
- So the date of the talk sits on the relation, at whatever precision is
  known: `2026-10-19`, or `2016` for the OHBM talk.
- A session is added only when it is known: US-RSE's
  "AI Assisted Code Development" is an `XYZEvent` that is `part_of` the
  conference.

### 2. A recording needs its own link to the talk

- A recording is `generated_by` its event.
- When that event is a whole conference (distribits 2025), the conference
  alone does not say *which* talk the video shows.
- The exporter therefore also writes `derived_from: <talk>` on the recording.
- The alternative would be a talk-slot event per recorded talk.
- **To decide.**

### 3. Free-text places have no slot

- `at_location` takes an IRI.
- Some places are only known as text: "Düsseldorf, Germany (Haus der
  Universität)", "Geneva, Switzerland", "Willow Glen Room".
- The exporter falls back to `attributes: [{predicate: schema:location,
  value: …}]`.
- The options are:
  - accept that fallback;
  - use place IRIs (e.g. Wikidata, GeoNames) for cities and keep rooms as
    attributes;
  - add a text slot upstream.
- **To decide.**

### 4. Linking an event to a project

- `XYZEvent.part_of` only accepts events. So `distribits-2025` is linked to
  `xyzrins:projects/distribits` through `influenced_by` instead.
- psychoinformatics-site-specific models "Distribits 2024" and
  "Distribits 2025" as **`XYZProject`** records. Those have `kind:
  bibo:Conference`, `started`/`ended`, organizers (`marcrel:orm`), and are
  `part_of` a "Distribits" project.
- The datalad-concepts PR should therefore address both:
  - letting `XYZEvent.part_of` (or another slot) point to a project;
  - suggesting that such conference-as-project records migrate to
    `XYZEvent`.

### 5. Presenters

- Presenters are marked with the role `obo:CRO_0000100` ("Presenter") on the
  talk's `attributed_to`, as psychoinformatics does.
- Talks have no other way to record who presented, so this is the only place
  presenters live.
- A presenter who is not an author gets a presenter-only attribution.
- If one deck is given several times by different people, the per-occasion
  presenter is lost. The talk-slot event would carry it if ever needed.

### 6. Fields `talks.yaml` has that `xyzri` cannot take yet

- **`keywords`.** There is no slot. They could become `about` → `XYZTopic`
  records, but con-site-specific has only one topic today.
- **`license`.** `rules` might be the place, but that is unverified.
- Both are needed for Zenodo (PLAN §6). The exporter drops them for now.

### 7. The sources disagree, and the records must decide

- **US-RSE'26 authors:** the program lists 5; the abstract adds John A. Lee.
- **BBQS:** Zotero `HUPZV3B5` lists only Cody Baker; INDEX.md lists Cody
  Baker as presenter and Yarik as co-author.
- **Vadim Melnik's ORCID:** "TBD" in `SOUL.md`; given in the US-RSE abstract.

### 8. Facts still missing (left out rather than guessed)

- the day of the YODA talk within distribits 2025 (2025-10-23 to 2025-10-25);
- the US-RSE presenter;
- the 2016 OHBM presenter and date.

The US-RSE end date and place now come from the Zenodo record (see below).

### 9. PIDs and routes

- New talks get `xyzrins:talks/<TALK-ID>`. A TALK-ID can contain uppercase
  letters (`2025-distribits-YODA`); check whether the site generator
  lowercases paths.
- The migrated Zotero talk keeps `xyzrins:publications/zotero-7ahrxd2x`, so
  talks would live under two route prefixes. Either accept that, or add
  redirects.

### 10. Event types

- `bibo:Conference` and `bibo:Workshop` exist.
- Session, webinar and webinar series use local types
  (`xyzrins:event-types/…`).

### 11. Year-only dates must be quoted in `talks.yaml`

- YAML reads `2016` as a number, so it fails the schema's string date
  pattern.
- Write `'2016'`. Full and month dates (`2026-10-19`, `2025-10`) need no
  quotes.

### 12. Datetime type in datalad-concepts

- datalad-concepts' `W3CISO8601` pattern anchors only its first and last
  alternatives (`^…|…|…$`).
- So, for example, `2026-10-19T10:30` without a time zone is accepted.
- That bug predates this work and is worth a separate upstream fix.

## Changes after review (2026-10-05)

**Nothing Zenodo-specific in `talks.yaml`.**

- An event's `collection` (`url`, `publication_date`, `license`, `due`) says
  where and how it gathers materials, e.g. the Zenodo community `usrse26`.
- A talk's `deposits` (`url`, `doi`, `concept_doi`) lists its records in any
  repository.
- The top-level `collections` names CON's own community (`con`).
- The platform follows from the URL.

**Identifiers live in the schema.**

- `License` and `EventKind` are enums whose values carry `meaning`
  identifiers, such as `spdxlic:CC-BY-4.0` or `bibo:Conference`.
- `export_sample.py` takes event-type PIDs from there.

**Organizers.**

- An `organizations` registry (CON, `ror: 04tfhh831`) and
  `events.<e>.organizers` were added.
- distribits 2025 lists CON, as the `[user]` comment records. In `xyzri`
  this becomes `associated_with: [{object: ror:04tfhh831, roles:
  [marcrel:orm]}]`; see PLAN §5.2.
- distribits 2025 now links to its edition page,
  `https://www.distribits.live/events/2025-distribits/`.

**`reuse:`** is explained in the schema: authoring notes, formerly
INDEX.md, never exported.

## Verified against live sources (2026-10-05)

These were fetched by a helper session in the "Default Cloud Environment",
which has network access. This session's environment blocks those hosts.

### Zenodo record 22783262 (the US-RSE'26 abstract)

**Identity:**

- DOI `10.5281/zenodo.22783262`; concept DOI `10.5281/zenodo.22783261`.
- Communities: `usrse26` and `con`.
- `resource_type: presentation`; `license: cc-by-4.0`.

**Fields of `GET /api/records/<id>` used by the crosswalk** (PLAN §6):

- `metadata.creators[]`: `{name: "Family, Given", affiliation, orcid}`;
- `metadata.meeting`: `{title, acronym, dates, place, url}`;
- `metadata.grants[]`: `{code, internal_id: "<funder DOI>::<code>", funder: {name, doi, acronym}, title, program}`;
- `metadata.related_identifiers[]`: `{identifier, relation, resource_type, scheme}`;
- `metadata.custom`: `{"code:codeRepository": "https://github.com/con/talks"}`;
- `metadata.version`.

There is no `custom_fields` key in this serialization.

**What `zenodo diff` would already report against `talks.yaml`:**

- **Creators.** There are 6, including John A. Lee, matching the abstract
  (the program lists 5). Vadim Melnik is entered as `"Vadim, Melnik"`, with
  family and given name swapped.
- **Publication date.** It is `2026-09-16`, the abstract upload date. The
  US-RSE guidance says to set `2026-10-19`.
- **Grants.** Five are listed: DANDI `2R24MH117295-06`, OpenNeuro
  `2R24MH117179-06`, EMBER `1R24MH136632-01`, ReproNim `5P41EB019936-09`,
  NSF `1912266`. con-site-specific holds DANDI and OpenNeuro under
  *other award years* (`1R24MH117295-01A1`, `5R24MH117179-07`). So grants
  must be matched on the core project number (`R24MH117295`), not the full
  award code. ReproNim and NSF have no record there.

**Community `con` holds 3 records:**

- this talk abstract;
- a poster, "The Ecosystem of Standards in Neuroscience: Which Ones Are For
  You?" (2025-11-11, record 18333008);
- a dataset (Haxby et al. 2001, record 1203329).

### annextube archives

**ReproTube `channels.tsv`** has `channel_dir`s `DataLad` and `ReproNim`, as
the URL templates assume.

**The three sample videos are present:**

| Video | Archive | Title | Published | Duration | Status |
| --- | --- | --- | --- | --- | --- |
| `EuKVapscUQ4` | DataLad | 'Yaroslav Halchenko: "Pragmatic YODA: …"' | 2025-11-12 | 1702 s | downloaded |
| `1XbTbJ_P2x0` | ReproNim | "YODA: Structure your studies, observable and reproducible they become" | 2026-02-06 | 3656 s | `metadata_only` |
| `8NTWKHer5Zo` | contube | "Guidelines for Reproducible Research (STAMPED)" | 2026-03-30 | 2915 s | `metadata_only` |

- `8NTWKHer5Zo` is from the channel "CON: Center for Open Neuroscience". Its
  description says "CON member Cody Baker presented".
- **`published_at` is the upload date, not the talk date.** The distribits
  talk (2025-10-23 to 25) was uploaded 2025-11-12, and the BBQS talk
  (2026-03-11) on 2026-03-30. Never use it as a presentation date.

**contube is a single-channel archive.**

- It has no `channels.tsv` (404), and its `videos/videos.tsv` holds 32
  videos from 16 YouTube channels, CON's among them.
- Its `channel.json` describes "Brainhack-AMX", not CON. That looks like a
  contube/annextube bug worth reporting.

**A name search over the two ReproTube `videos.tsv` files** (what Phase 3's
`find-videos` does) finds:

| Video | Title | Published | What it matches |
| --- | --- | --- | --- |
| `Mkb7qpYaL7o` | 'Yaroslav Halchenko: "What's in the DataLad sandwich?" AKA DataLad "ecosystem"' | 2024-04-09 | `2024-distribits-datalad` |
| `_McJ1BtLsiQ` | "Isaac To, Yaroslav Halchenko: DataLad-Registry, …" | 2024-04-09 | a CON talk at distribits 2024 |
| `ix3lC6HGo-Q` | "ReproNim Webinar: Containers" | 2020-06-07 | external candidate (PLAN §8) |
| `dwBtrpI2iS0` | "ReproNim Webinar: Reproducible Execution of Data Collection/Processing" | 2020-12-04 | external candidate (PLAN §8) |
| `SZ96Q6pwJzQ` | "SciOps from ReproNim/ ReproFlow" | 2024-06-16 | the 2024 ReproFlow webinar |
| `pVrjRRrmKbY` | "Introduction to DataLad" | 2021-03-26 | — |

It also finds panels and an unconference session from distribits 2024 and
2025.

### Published talks listing and dev site

- `datasets.datalad.org/centerforopenneuroscience/talks/` lists the same 16
  entries as `index.html`. There is no `2026-mcgill-mechababs/` entry.
- The dev site's navigation is: People, Projects, Publications, Datasets,
  Instruments, Explore. There are no Talks or Events sections yet.

## CON membership: the shape only (no records written)

psychoinformatics-site-specific records group membership on its site root
(`xyzrins:.`) through dated associations:

- 27 people are listed;
- roles include `marcrel:rtm` (Research team member), Student (`obo:AGRO_00000374`),
  Research assistant (`obo:ICO_0000080`), Intern and `marcrel:led`;
- many associations carry `started` and/or `ended` dates.

`delegated_by` is used there for employers and supervisors, not for group
membership.

The CON equivalent would be dated entries on con-site-specific
`XYZProject/site-root.yaml`:

```yaml
associated_with:
- object: xyzrins:persons/<person>
  roles: [marcrel:rtm]
  started: {at_time: "<YYYY-MM-DD>"}
  ended: {at_time: "<YYYY-MM-DD>"}   # present once the person has left → alumni
  schema_type: dlthings:Association
```

The dates must come from CON's own records, so none are filled in here.
