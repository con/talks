# CON projects audit — what the US-RSE talk does *not* mention

Source comparison: `gh api orgs/con/repos` (active, non-archived) **vs.**
projects named in `2026-usrse-con-talk.html` and `talk-proposal-draft.md`.
Also covers projects that *were* in older CON talks but dropped from the
current US-RSE deck, plus a few key external/CON-external projects worth
re-considering.

- First sweep: 2026-05-10.
- **Refreshed 2026-05-11** after applying the original recommendations
  1–5 and adding the Automate / SciOps mapping.


## Currently named in the US-RSE deck / proposal

### CON repos and CON-led projects
**con/duct**, **con/serve**, **con/validation**, **con/tinuous**,
**con/skills**, **con/yolo**, **con/citations-collector**,
**con/nwb2bids**, **con/annextube** (AnnexTube),
**registry.datalad.org**, **concepts.datalad.org**,
**open-brain-consent (OBC)** — referenced in the Standardize section
and Acknowledgements; **shub** mirror — visible by URL in the Automate
section but not named as the repo `con/shub`.

### DataLad family + extensions
DataLad core; `git`+`git-annex`; datalad-container, -crawler, -fuse,
-neuroimaging, -next, -osf, -ukbiobank, -xnat, -extension-template;
`datalad run` / `containers-run`; DataLad Handbook.

### Standards & community projects (CON-adjacent)
BIDS, NWB, DANDI, OpenNeuro, EMBER, BIDS-Apps (mriqc, fmriprep),
LinkML, pydantic, JSON Schema, SHACL, HED, vjsf, shacl-vue,
ReproIn, HeuDiConv, NeuroConv, ReproStim, ReproNim/containers,
ReproMan, NeuroDebian, PyMVPA, duecredit, citeproc-py, nwbinspector,
pynwb, zarr, OME-Zarr.

### Frameworks / principles (now load-bearing)
**STAMPED** (per-artifact, Macdonald *et al.* 2026) and **SciOps**
(team-operations CMM, Johnson *et al.* 2024) — mapped to the 5-verb
spine: Reuse / Compose / Extend / Standardize ≈ L3, Automate ≈ L4,
AI-in-the-loop ≈ L5. Plus **YODA**, **FAIR**, and the **AI-coding
ladder** (companion talk).

### External tools / collaborators
brainlife.io, CBRAIN, CONP, Kitware (NWB tooling), MetaCell NWB
Explorer, neurobagel, Datasette, VisiData, Hexagonal Architecture
(Cockburn 2005), GoF Design Patterns, Fowler's PoEAA,
Eric Evans (DDD Smart UI anti-pattern), distribits, ReproTube.


## Status of original recommendations

| # | Project | Status | Where it now appears |
|---|---------|--------|----------------------|
| 1 | `con/tinuous` | **Applied** | Automate § "Where we automate" + timeline (2019 milestone) + Monday checklist |
| 2 | `con/yolo` + `con/skills` | **Applied** | Timeline 2024+ row; Automate § meta-automation slide; HI+AI cross-ref |
| 3 | `con/citations-collector` | **Applied** | Reuse § (continuation of duecredit; feeds dandi-bib) |
| 4 | `con/nwb2bids` | **Applied** | Compose § small-units table + MVC Controllers row |
| 5 | `OBC` (open-brain-consent) | **Applied** | Standardize § "schemas as first-class citizens" + retained in logo strip |
| 6 | `fail2ban` | **Deferred** | Mentioned in `SOUL.md §1` Extend bullet, not in the deck — recommended for the BoF, not the 15-min talk |


## Active CON repos *still* not named (gap list, refreshed)

### Worth a one-liner if space opens up

- **`con/external-services`** — *Registry of external services to use
  for YOUR hosted files*. Direct match for the "Federate, don't
  recentralize" thread; could be a sentence next to `registry.datalad.org`
  in the Compose section.
- **`con/shub`** — *GitHub mirror of `datasets.datalad.org/?dir=/shub`*.
  Currently only visible via a `?dir=/shub` link in the Automate-section
  container-building row; the repo itself isn't named. Quintessential
  Reuse-in-reverse + archive story — could be promoted to a named line.
- **`con/noisseur`** — *Automated verification of entered/displayed
  information*. Concept-stage; cited in `2022-nih-compcore.html` as
  "Beyond ReproIn". A one-line nod under Controllers / acquisition
  would round out the ReproIn / HeuDiConv / ReproStim family.
- **`con/upptime`** — *Uptime of CON websites & services*. Tiny but a
  cheap "View on the operations Model" example for the MVC Views slide.
- **`con/flux`** — *Map of `git`/`git-annex` clones of a repository*.
  Maps to the federation/discovery story; pair with `registry.datalad.org`.
- **`datalad-installer`** — was in `2024-distribits-datalad.html` § "To
  provide peace to developers and users for deployment". Concrete
  Reuse / distribution / multi-platform evidence; not load-bearing
  for the US-RSE story but a natural Acknowledgements name.

### Long-running maintenance work, not in the talk

- **`fail2ban`** — Halchenko is co-maintainer; canonical "we stayed
  on as upstream maintainer" example. *In `SOUL.md` but not the deck.*
  Recommended for a BoF / longer talk, not the 15-min US-RSE slot.
- **`psychtoolbox-3-debian`** — long-running Debian-Med packaging;
  same audience-fit call as fail2ban.

### Mentioned in older talks, dropped from this one (deliberate)

- **PyMVPA-on-phone** punchline (`2022-nih-compcore.html`) — the
  "12.5 hours to happy time" deployment-pain story that motivated
  NeuroDebian. Cut for length; appropriate to drop.
- **Phantom QA / Nuisance study** (Cheng & Halchenko, F1000 2020) —
  excellent Trust/Variance content for an NIH audience, but off-topic
  for US-RSE. Keep in references only.
- **Decentralized RDM** (Hanke *et al.*, Neuroforum 2021) — cited in
  SOUL.md §5 canonical citations, not in the deck.

### CON-internal / niche — probably keep skipping

`CONveyor`, `catenate`, `cierge`, `communitator`, `con-intro`,
`demos`, `docflow`, `duct-gallery`, `ference`, `fscacher`,
`git-annex-log-stats`, `journals`, `jsdownloader`, `job`,
`liab-deployments`, `mind_2018`, `opfvta-reexecution`, `quest`,
`scripts`, `serve-liab`, `serve-actions`,
`serve-wayback-archive-demo`, `shell-chronicle`, `solidation`,
`sparkle-tools`, `taxonomy-site-sandbox`, `tents`, `tinuous-inception`,
`tinuous-template`, `tinuum`, `try-aind-1`, `tube`, `tributors`,
`vandermeerlab-to-bids`, `versations`, `visidata-demos`,
`work-history-data`. Some are namedrop-worthy if a future slide is
already on the topic (e.g. `visidata-demos` if a VisiData live demo
gets added; `vandermeerlab-to-bids` if BEP-032 comes up).


## What's gained since the first sweep (2026-05-10 → 2026-05-11)

Beyond the audit-driven additions (1)–(5), the deck has grown three
substantial pieces that didn't exist in the first sweep and that
*were* the chief reason the audit asked for con/tinuous etc.:

- **5-verb spine with Automate** — Reuse / Compose / Extend /
  Standardize / **Automate** now appears in the title, spine slide,
  timeline, every section, the Monday checklist, and the sign-off.
- **A full Automate section** — 4 slides: opener + "Where we
  automate" + "Cost: harnesses → meta-automation via AI" + **"The
  five verbs climb the SciOps ladder"** (the new SciOps L1–L5
  mapping slide, with the L3 exemplar list — BIDS / NWB / DataLad /
  DANDI / brainlife.io — that Johnson *et al.* themselves call out).
- **SciOps + STAMPED as load-bearing references** — STAMPED is
  cited canonically (Macdonald, Baker, To & Halchenko, 2026, with
  the full Self-containment / Tracking / Actionability / Modularity /
  Portability / Ephemerality / Distributability expansion); SciOps
  is cited canonically (Johnson *et al.*, 2024) and framed as the
  *team-level* maturity ladder complementing STAMPED's *per-artifact*
  properties. The proposal abstract weaves the 5-verb ↔ SciOps L1–L5
  mapping into the framing paragraph.

These together — not the individual project namedrops — are the
substantive shift the audit needed to acknowledge.


## Updated recommendation summary

The list of project namedrops to *still* add is now short and
optional. In priority order (each is a single line):

1. **`con/shub`** — promote from a `?dir=/shub` URL to a named repo
   line in the Automate section's container-building row. One word
   change, very on-spine (Reuse-in-reverse + archive). *Recommend
   doing this.*
2. **`con/external-services`** — one cell in the Compose section
   right after `registry.datalad.org`, framing it as a "federation
   registry, plain text, no service required". *Recommend.*
3. **`datalad-installer`** — one line in Acknowledgements (or in the
   Reuse → Extend distribution bullet). *Marginal.*
4. **`con/noisseur`** — drop in only if the Compose § acquisition
   row needs more concreteness. *Skip for 15-min US-RSE.*
5. **`con/upptime`** / **`con/flux`** — fine to skip; cheap mentions
   if the MVC Views slide opens up. *Skip.*
6. **`fail2ban`** / **`psychtoolbox-3-debian`** — save for the BoF.

The audit no longer recommends anything that materially changes the
talk's shape; (1)–(2) are the only worthwhile micro-edits.
