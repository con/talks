# Sample talk records, for reviewing `../PLAN.md`

These files show what `PLAN.md` currently proposes. They are applied to a
few real talks, so the design can be reviewed on concrete records before
anything is implemented.

| File | What it is |
| --- | --- |
| `talks.yaml` | Five talks in the planned source format (PLAN §2, §3), plus the `people`, `events`, `video_archives` and `topics` registries. Each value carries a comment naming its source; unknown values are left out. |
| `export_sample.py` | A prototype of `talks.py export-things` (PLAN Phase 5B). It maps `talks.yaml` onto `xyzri` records, following PLAN §5. |
| `xyzri/<Class>/*.yaml` | Its output, laid out like con-site-specific `metadata/records/`. |
| `validate.sh`, `check_refs.py` | Validate `xyzri/` against the schema, then report references that resolve to no record. |

The five talks were picked to cover the shapes the plan must handle:

| Talk | Shape |
| --- | --- |
| `2026-usrse-con-talk` | scheduled; presented in a session; Zenodo record; 5 authors |
| `2026-repronim-YODA-BIDS-webinar` | webinar within a series; `derived_from` another deck; YouTube plus ReproTube copy |
| `2025-distribits-YODA` | conference with known dates; YouTube plus ReproTube copy; event linked to a project |
| `2026-bbqs-stamped` | Google Slides with annexed exports; presenter differs from the author list; Zotero duplicate (`HUPZV3B5`) |
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

- **All 23 records validate.**
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
- the US-RSE presenter and the conference end date;
- the 2016 OHBM presenter and date;
- video titles, which Phase 3's `find-videos` would read from annextube
  `videos.tsv`.

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

### 11. Datetime type

- datalad-concepts' `W3CISO8601` pattern anchors only its first and last
  alternatives (`^…|…|…$`).
- So, for example, `2026-10-19T10:30` without a time zone is accepted.
- That bug predates this work and is worth a separate upstream fix.

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
