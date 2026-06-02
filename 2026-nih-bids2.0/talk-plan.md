# Logistics

- **Venue / series**: NIMH Data Science & Sharing Team — Lunch & Learn
- **Format**: ~30 min talk + Q&A / discussion
- **Audience**: neuroimaging researchers, dataset curators, developers of
  BIDS-aware tools
- **Speaker**: Dr. Yaroslav O. Halchenko (Center for Open Neuroscience, PBS
  Department, Dartmouth College)
- **Deck file**: `2026-nih-bids2.0.html` — to be created by copying
  `../2026-repronim-YODA-BIDS-webinar.html` from the talks repo root, then
  edited from there (see TODO below; the copy must be done on the host since
  the talks/ root is not bind-mounted into this sandbox).

# Abstract

Have you ever wanted something different out of the Brain Imaging Data
Structure (BIDS) standard? Dr. Yaroslav O. Halchenko (leading the Center for
Open Neuroscience at PBS Department of Dartmouth College) will give the NIMH
Data Science & Sharing Team's Lunch & Learn series a half-hour talk on the
past & future of BIDS with a focus on the development of BIDS 2.0, the next
major release of the standard. This presentation and discussion will be
especially interesting to neuroimaging researchers, dataset curators, and
developers of BIDS-aware tools. Attendees can expect an overview of the
overarching agenda guiding BIDS 2.0 together with a tour of how the work is
organized across `github.com/bids-standard/` organization repositories, plus
pointers on how to weigh in or contribute.

# Source materials

- `BIDS.bib` — BibTeX export of our Zotero BIDS bibliography (recommend the
  audience reuse it and contribute):
  https://www.zotero.org/groups/5111637/bids/library

- `nihpp-2309.05768v2.{pdf,md,txt}` — "The Past, Present, and Future of the
  Brain Imaging Data Structure (BIDS)" (Poldrack et al.). The **"Future of
  BIDS"** section (md lines ~861-1000) is the canonical statement of why a
  2.0 is needed: inheritance principle, hierarchical complexity, derivatives
  as inputs, multi-modal data, integration with DICOM/NWB/OME-Zarr,
  governance/funding.
  - `nihpp-2309.05768v2_images/` and `nihpp-2309.05768v2_rawimages/` —
    figures (8 each).

- `BIDS2.0-INCF2024-poster.{odp,pdf,svg}` — INCF 2024 poster summarising the
  *original* (ambitious) BIDS 2.0 agenda. Annexed in this worktree (not
  resolvable from the sandbox); content must be inspected on the host.
  Source: https://docs.google.com/presentation/d/189tCRORhhn1ZzN6DmtK_Wqneui-kaoGiPXh7nzI0WGU/edit

- NSF POSE BIDS talk:
  https://docs.google.com/presentation/d/1x-LdlVGItyX6oINm8URIP5cZWBvQG6bM/edit?usp=sharing
  — useful for **BIDS intro slides**. Companion paper to cite:
  Rokem, Mandava, Cristea, Tambay, Bouchard, Berys-Gonzalez, Connolly
  (2025), "Open-source models for development of data and metadata
  standards", *Patterns*, https://doi.org/10.1016/j.patter.2025.101316 —
  it's the summary of the NSF POSE-funded governance work that ran
  alongside the BIDS intro talk above; **not authored by the speaker**, so
  cite as third-party support (not "our paper").

- **STAMPED Principles** — newly published preprint we should promote
  *whenever YODA comes up* (YODA is a precursor / motivation):
  - Site: https://stamped-principles.org/
  - Preprint: "STAMPED principles for reproducible research objects",
    posted 2026-05-26, MetaArXiv,
    https://doi.org/10.31222/osf.io/f3h82_v1
  - Acronym: **S**elf-containment, **T**racking, **A**ctionability,
    **M**odularity, **P**ortability, **E**phemerality, **D**istributability.
  - Branding repo: https://github.com/stamped-principles/stamped-branding
    (CC-BY-4.0). Downloaded into `assets/stamped/`:
    - `ver-2/name-main+logo_ver-2.{svg,png}` — main lock-up (good for
      section dividers and the "what is STAMPED" slide).
    - `ver-3/name-banner_ver-3.{svg,pdf}` — full horizontal banner (for the
      title slide / footer).
    - `ver-3/name-banner_ver-3_icon-*.png` — eight per-letter principle
      icons (actionable, distributed, ephemeral, modular×2, portable,
      self-contained, tracked) — useful if we want to walk through the
      acronym on one slide.
    - `ver-3/name-favicon+base_ver-3.svg` — compact mark.

- **BIDS 2.0 GitHub project board**:
  https://github.com/orgs/bids-standard/projects/10 — compiles issues
  (mostly from `bids-2-devel`, some from `bids-specification`) organising
  progress toward 2.0, plus a "BIDS 3.0" column for items deferred beyond
  2.0.

- **`bids-standard/bids-2-devel`** — dedicated issue repository. As of
  the 2026-06-01 sync: 94 issues total (81 open, 13 closed) and 2 PRs (both
  old infrastructure). Many issues were migrated from `bids-specification`
  as items not addressable inside the 1.x series. Top labels by count:
  `metadata` (23), `consistency` (13), `impact: high` (11),
  `folder-structure` (11), `entities` (10), `suffixes` (8),
  `modularity` (5), `auto-migrate` (3).

- **`bids-standard/bids-specification`** with label `bids-2.0`:
  - Open PRs (3): [`bids-specification#1821`](https://github.com/bids-standard/bids-specification/issues/1821) (singular TSV columns, units +
    `migrate_plural_columns`), [`bids-specification#1809`](https://github.com/bids-standard/bids-specification/issues/1809) (flex BIDS layout —
    [`bids-2-devel#54`](https://github.com/bids-standard/bids-2-devel/issues/54)), [`bids-specification#1775`](https://github.com/bids-standard/bids-specification/issues/1775) (umbrella "BIDS-2.0").
  - Merged: [`bids-specification#2400`](https://github.com/bids-standard/bids-specification/issues/2400) (controlled vocab for age units).
  - Open issue: [`bids-specification#2155`](https://github.com/bids-standard/bids-specification/issues/2155) — inheritance principle deep-dive (Lestropie).

- **`bids-standard/bids-utils`** — planned home of `bids-utils migrate`
  (analogue of `2to3` for smoothing 1.x→2.0 upgrades / deprecations) and
  related migration tooling.

- **`bids-standard/bids-examples`** —
  https://github.com/bids-standard/bids-examples — curated valid BIDS
  datasets. Heavily used to test schema/tooling changes; the talk should
  advocate that the audience contribute more examples (especially modality
  combos that would catch 2.0 migrations).

- **OpenNeuroStudies** — https://github.com/OpenNeuroStudies/OpenNeuroStudies
  — concrete demonstrator of the `DatasetType: study` composition pattern
  (multiple OpenNeuro datasets composed into a study); reference it on the
  "what 1.x delivered" slide.

## Local data dumps

`Makefile` + `scripts/fetch_repo.py` + `scripts/fetch_project.py` pull
issues/PRs/labels/comments from the three sources above as YAML under
`data/`, so the deck (and this plan) can be regenerated from a fresh snapshot
with `make sync`. See `scripts/README.md` for prerequisites — `gh auth login`
must be done by you (the scripts deliberately don't touch the dev token).

**Open issue with the project-board fetch**: the dev token in this sandbox
lacks the `read:project` scope, so `data/project-10/items.yaml` currently
holds an `error:` placeholder. When you run `make sync-project` on the host
under your `gh auth login` (as a member of `bids-standard`), it should
populate. If not, generate a classic PAT with `read:project` and re-run.

Do not edit `data/*.yaml` by hand — `make sync` overwrites them.

# Overall presentation plan

The deck reuses the structure of `2026-repronim-YODA-BIDS-webinar.html`
(reveal.js). Target ~30 minutes ≈ 12-15 content slides + intro/closing.
**Wherever YODA is mentioned, promote the STAMPED preprint and show its
banner.**

| #  | Slide                              | Key points                                                                                                                                              |
|---:|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Title                              | Title, speaker, CON affiliation, NIMH L&L date. STAMPED banner in footer as branding.                                                                   |
|  2 | Who I am / what CON does           | One-line CON + DataLad + ReproNim links; transition to "let me tell you what's happening in BIDS-land".                                                 |
|  3 | BIDS at ~10                        | Hook: BIDS turns 10. Quick "what is BIDS" recap (reuse one slide from the NSF POSE deck). Cite Rokem et al. 2025 *Patterns* paper (NSF POSE governance summary).                  |
|  4 | The Past/Present/Future paper      | Reference Poldrack et al. preprint as the canonical map of where 1.x landed and where 2.0 is heading.                                                   |
|  5 | What 1.x already delivered         | Recent wins: schema/sidecar overloads; DatasetType `study` (composition) → [`bids-2-devel#59`](https://github.com/bids-standard/bids-2-devel/issues/59) (demo on OpenNeuroStudies); inheritance docs PR [`bids-specification#1834`](https://github.com/bids-standard/bids-specification/issues/1834); plus past deprecations during 1.x (see notes).            |
|  6 | The "standards vs software" wrinkle | In semver, adding a feature is a minor bump. In a standard, even an optional addition exerts pressure on every tool. Frame as why 2.0 must be **paced and scope-bounded** — bundle breaking changes into one well-trailed release rather than trickling them as optional bumps that tools silently fail to implement. |
|  7 | Originally: ambitious BIDS 2.0     | Summary of INCF 2024 poster goals (composition, derivatives-as-inputs, multi-modal hierarchies, formal data model). Pull figures from poster.           |
|  8 | Now: realistic 2.0                 | Tighter scope — consistency (e.g. `participants.tsv`→`subjects.tsv`, singular TSV columns, MUST-summarise, deprecations deprecated) + tooling (`bids-utils migrate`, PR #1775 functional patches). Distil cross-modality divergences (see notes). |
|  9 | State of play — by the numbers     | Counts from `make sync` data: open bids-2-devel issues, bids-2.0-labelled PRs in bids-specification, project board columns.                             |
| 10 | Featured open threads              | 3-5 concrete items the audience can engage with (e.g. inheritance [`bids-specification#2155`](https://github.com/bids-standard/bids-specification/issues/2155), singular TSV [`bids-specification#1821`](https://github.com/bids-standard/bids-specification/issues/1821), flex layout [`bids-specification#1809`](https://github.com/bids-standard/bids-specification/issues/1809)).                                        |
| 11 | What's in scope for 2.0 vs 3.0     | Treat 3.0 as a closing note only — acknowledge that we *are* thinking about 3.0, but the talk's spine is the slimmer 2.0. Reference the project board "BIDS 3.0" column for deferrals.   |
| 12 | YODA → STAMPED                     | YODA as the precursor pattern → STAMPED preprint as the formalisation. Show banner + per-letter icons. Encourage citing the preprint.                   |
| 13 | How to get involved                | Project board, `bids-2-devel`, `bids-specification`, `bids-utils`, `bids-examples` (advocate contributing more valid examples), BEP process, Zotero group, monthly maintainer call.                                  |
| 14 | Acknowledgments + Q&A              | Maintainers, funders (BRAIN Initiative), the community.                                                                                                 |

## Per-slide notes

### Slide 5 — what 1.x already delivered

- BIDS has "always been v1" — `bids-specification/src/CHANGES.md` records
  the entire history under the 1.x major; there is no prior major release.
  The argument for a real 2.0 is that we should make that step properly
  rather than continuing to accrete minor bumps forever.
- BUT 1.x has not been free of breakage either: across 1.0 → 1.11 the spec
  accumulated **~20** distinct deprecations / renames / removals /
  behavioural changes (formal deprecation mechanism only landed in 1.4.1 via
  [`bids-specification#634`](https://github.com/bids-standard/bids-specification/pull/634)
  — earlier breakages were outright renames). Three themes worth calling
  out: field renames (`Unit`→`Units`, `T2star`→`T2starw`, etc.); semantic
  swaps under stable names (e.g. `PhaseEncodingDirection` `x/y/z`→`i/j/k`;
  BIDS URIs replacing raw-relative paths in `IntendedFor`/`Sources`); and
  the schema-format swap (prose → YAML) that reshaped every downstream tool
  without a `[BREAKING]` tag. Full timeline + PR refs in
  `notes-1x-deprecations.md`.
- **Promote `DatasetType: study`** as a 1.x-era win for composition, with
  https://github.com/OpenNeuroStudies/OpenNeuroStudies as the demonstrator
  (multiple OpenNeuro datasets composed under one study root).

### Slide 8 — modality divergences worth distilling

Examples of inconsistency across modalities that 2.0 could (and should)
flatten:

- Mixing of **column definitions** for `.tsv` files alongside metadata
  definitions inside `.json` sidecars (the dual purpose of the same
  sidecar field).
- Multiple, modality-specific indexing files. The "sticks-out" case is
  `samples.tsv` (microscopy) —
  [`bids-specification#2283`](https://github.com/bids-standard/bids-specification/issues/2283)
  — which doesn't fit the otherwise-uniform `<entity>.tsv` indexing
  pattern.
- (Add more as we mine `data/bids-specification/issues-bids-2.0.yaml`.)

### Slide 8/9 — migration mechanism (PR #1775)

Besides `bids-utils migrate`, the *spec* repo itself demonstrates *how* to
land sweeping 2.0 changes:
[`bids-specification#1775`](https://github.com/bids-standard/bids-specification/pull/1775)
introduces "functional patches" — scripts that perform major text-level
sweeps over the spec (e.g. replacing `participants` with `subjects`):

- Patch script example:
  https://github.com/bids-standard/bids-specification/pull/1775/files#diff-a0b511b2ce4b2b01d7db2e671a257160a1e810b89d926c073dfd3b02bb9fe055
- Initial migration for `participants.tsv` → `subjects.tsv`:
  https://github.com/bids-standard/bids-specification/pull/1775/files#diff-b81290f4f0476f7197f66bf34cab9f750df9401d7aaa05caf78732e542c97181R43

The pitch: PR #1775 is the **proof of concept** that 2.0 changes can be
applied mechanically across the spec text and (by analogy) across user
datasets — paired with `bids-examples` as the test corpus.

### Closing — 2.0 vs 3.0 framing

Decision: **3.0 lives in the closing note only.** The spine of the talk is
"slimmer 2.0, soon"; 3.0 is acknowledged as on-the-horizon but explicitly
out of scope. Project board "BIDS 3.0" column is the artefact to point at
for what's deferred.

## Open questions to settle before cutting slides

- Do we want a live "demo" slide (e.g. running `bids-utils migrate` on a
  sample dataset) or keep it purely narrative for a 30-min slot?

# Refined content sections (for slide bullets)

## What is the goal behind BIDS 2.0

### Originally: ambitious

Source: INCF 2024 poster (pulls slide content from there once
host-accessible). High-level themes from Poldrack et al. "Future of BIDS":
- Refine / replace **inheritance principle** for clearer semantics
  (especially TSV files, which the principle does not currently define
  well).
- Address **hierarchical complexity**: the immutable raw-data hierarchy
  (dataset → subject → (session) → modality) does not accommodate
  multi-modal derivatives or model outputs spread across files.
- **Derivatives as inputs**: allow BIDS Apps to consume other Apps' outputs
  → enables DAG-of-Apps pipelines.
- **Existing toolchains**: define round-trip conversions (or annotation
  layers) so legacy software stacks can participate without reformatting
  everything.
- **Cross-standard integration**: closer coordination with DICOM, NWB,
  OME-Zarr to stop duplicating effort.
- **Governance / funding**: foundation-like support for BIDS as it scales.

### Current: realistic

Smaller consistency-focused changes to set a sustainable base, automated by
`bids-utils migrate` (analogue of `2to3`). Examples already on the table:

- `participants.tsv` → `subjects.tsv` (`bids-2-devel` & `bids-specification`
  threads — confirm exact issue # once data is synced).
- Singular TSV column names — [`bids-specification#1821`](https://github.com/bids-standard/bids-specification/issues/1821) (units,
  `migrate_plural_columns`).
- Summarisation promoted from RECOMMENDED to **MUST**.
- Flex layout / inheritance reform per [`bids-2-devel#54`](https://github.com/bids-standard/bids-2-devel/issues/54) →
  [`bids-specification#1809`](https://github.com/bids-standard/bids-specification/issues/1809).
- DatasetType `study` for dataset composition ([`bids-2-devel#59`](https://github.com/bids-standard/bids-2-devel/issues/59)).

The pitch: ship a **migrate-able** 2.0 now to establish a better base for
3.0's more drastic changes.

## What has happened already in 1.x

Concrete wins to call out:

- DANDI alignment / large-dataset issue raised in
  [`bids-2-devel#65`](https://github.com/bids-standard/bids-2-devel/issues/65), largely solved via docs PR
  [`bids-specification#1834`](https://github.com/bids-standard/bids-specification/issues/1834).
- More consistent schema and sidecar **overloads** (specific PRs to itemise
  from the YAML dump once available).
- DatasetType `study` for composition ([`bids-2-devel#59`](https://github.com/bids-standard/bids-2-devel/issues/59)).
- Recent merge: controlled vocabulary for age units —
  [`bids-specification#2400`](https://github.com/bids-standard/bids-specification/issues/2400).

TODO: cross-check the YAML dump for any other 1.x ENH labels worth showing.

## "Backward compatibility" — standard vs software

Working title for the slide; rename later.

- In software, **adding** a feature is a *minor* version bump under semver.
  Users can opt into it or ignore it.
- In a standard, even an **optional** addition exerts pull on every tool to
  implement support — otherwise validators, parsers, and downstream pipelines
  diverge.
  - Example: refining inheritance for TSV files. Spec can call it a minor
    revision; tool developers may not even notice, and now BIDS datasets in
    the wild are "valid by spec" but invalid by behaviour.
- Not unique to BIDS: see DICOM and vendor-specific tags, delayed adoption
  of standardised mechanisms (clock-time sync apparatus, etc.).
- Implication for 2.0: prefer **breaking + migrate-able** over **optional +
  drift-prone**. Hence the focus on `bids-utils migrate` and on raising
  RECOMMENDED → MUST.

## STAMPED promotion plan

Every mention of YODA in this deck must be followed by a STAMPED callout:

- One-line: "YODA's conventions are now formalised as **STAMPED** — a
  preprint laying out 7 principles for reproducible research objects".
- Show banner (`assets/stamped/ver-3/name-banner_ver-3.svg`) on the YODA
  slide.
- Link: https://stamped-principles.org/ (preprint
  https://doi.org/10.31222/osf.io/f3h82_v1).
- If we have a "principles" slide, use the per-letter icons from
  `assets/stamped/ver-3/name-banner_ver-3_icon-*.png`.

# TODOs

Grouped by stage. Tick as we go.

## Data / tooling

- [x] `Makefile` + `scripts/` to dump `bids-2-devel` issues + PRs,
      `bids-specification` issues+PRs with `bids-2.0` label, and ProjectV2
      #10 items as YAML under `data/`. *(Done; project-10 fetch needs a
      `read:project`-scoped token from the host — see "Local data dumps".)*
- [ ] After `make sync` lands, scan `data/bids-2-devel/issues.yaml` for
      top labels and counts to seed the "by the numbers" slide.
- [ ] From `data/bids-specification/prs-bids-2.0.yaml`, write a one-line
      summary of each open PR (titles already in this plan; flesh out
      bullets once bodies are available).
- [ ] From `data/project-10/items.yaml`, list what is allocated to
      "BIDS 2.0" vs "BIDS 3.0" columns.
- [ ] Confirm the exact issue/PR numbers backing
      `participants.tsv`→`subjects.tsv` and `summarisation MUST`.

## Slides (deferred — do not start until plan is approved)

- [ ] On the host: `cp 2026-repronim-YODA-BIDS-webinar.html
      .git-meta/worktrees/2026-nih-bids2.0/2026-nih-bids2.0/2026-nih-bids2.0.html`
      (the talks/ root is not visible from inside the sandbox, so the copy
      has to happen there).
- [ ] Strip YODA-webinar-specific slides; keep the chrome (title,
      footer, transitions, CSS).
- [ ] Wire STAMPED banner + favicon into the deck shell.
- [ ] Build slides 1-14 per the table above.
- [ ] On every YODA slide, add the STAMPED callout (line + banner + link).
- [ ] Pull selected figures from `nihpp-2309.05768v2_images/` (e.g. BEP
      timeline, schema diagram) onto the past/present slides.
- [ ] Embed 1-2 panels from the INCF 2024 poster on the "originally
      ambitious" slide (requires host-side access to the annexed file).
- [ ] Add an "involvement" slide with QR codes for: project board,
      bids-2-devel, BIDS.bib Zotero library, BIDS monthly call.

## Content / fact-checking

- [ ] Verify "BIDS turns 10" framing against the Poldrack et al. timeline
      (paper covers BEPs through 2019-2024 — confirm exact founding year).
- [ ] Confirm STAMPED preprint authorship and whether the speaker is on
      the author list (affects how to phrase the plug — "our preprint" vs
      "a related preprint").
- [ ] Decide whether to include a slide on **funding/governance** (paper
      section 9-ish) — relevant to NIMH audience but might bloat a 30-min
      talk.
- [ ] Pick a citation style for in-slide references and stick to it.

## Logistics

- [ ] Get the exact date, room/Zoom link, and pre-talk blurb from the
      NIMH L&L organisers; insert on title slide.
- [ ] Decide on a discussion-prompt slide (one or two open questions the
      audience can chew on during Q&A).
- [ ] Send a follow-up email post-talk linking deck + STAMPED preprint +
      project board.

# Open issues with this worktree (operational, not for the audience)

- The talks/ working tree is not bind-mounted into the sandbox we're
  developing in, so we cannot read existing sibling HTML decks, the annexed
  poster, or run `git` from here. Anything requiring those has to be done
  host-side; see TODOs above.
- `gh` inside this sandbox uses a read-only PAT — fine for `make sync` data
  pulls, but any pushes / PRs need to be run on the host with the user's own
  auth.
