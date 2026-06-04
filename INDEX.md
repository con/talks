# INDEX — talks and reusable slides

A catalog of every talk in this repository plus a topic-wise lookup of
*where to copy slides from* when authoring a new deck. Pair this file
with `SOUL.md` (mission/style) and `CLAUDE.md` (authoring workflow).

Slide IDs use the form `<file>#section-<n>[/sub-<m>]` where `n` counts
**top-level `<section>`** elements in the source file (1-based). When a
top-level section has vertical sub-slides, `sub-m` counts those (1-based).
This matches reveal.js's URL-fragment numbering: `#/<n-1>/<m-1>`.


## Per-talk inventory

Shelved drafts and outlines that are not currently being prepared for a
venue live under [`_backdrawer_/`](_backdrawer_/README.md) and are
listed in the *Shelved (backdrawer)* section below the active inventory.
Cross-references in the per-topic lookup point at the shelved path
(`_backdrawer_/<TALK-ID>.html`).

### `2026-usrse-con-talk.html` — *[WiP] Reuse, Compose, Extend, Standardize, Automate: Two Decades of RSEing Open (Neuro)Science at CON*  *(draft)*
- **Venue / date**: US-RSE'26 (proposal-stage draft; title carries a `[WiP]` marker in the tab and on the title slide).
- **Spine**: the five-verb spine (Reuse / Compose / Extend / Standardize / **Automate**) plus a "Reuse, in reverse" coda, an Automate section (with the *meta-automation* handoff), and an HI+AI close.
- **Reusable highlights**:
  - Title slide (per `SOUL.md` §3).
  - "Two decades, five verbs" intro slide (NEW).
  - "When it began for us" verb-tagged timeline (NEW; extension of `2024-distribits-datalad.html` § timeline; Automate milestones include 2007 PyMVPA-with-CI, 2016 ReproIn/HeuDiConv, 2019 dandiset auto-mirroring + con/tinuous).
  - Reuse: NeuroDebian + PyMVPA blocks borrowed from `2022-nih-compcore.html`; **`con/citations-collector`** added as the modern continuation of duecredit.
  - Compose: DataLad sandwich mermaid + extensions diagram from `2024-distribits-datalad.html`; registry stats from `2025-distribits-YODA.html`; small-units table referencing ReproIn / HeuDiConv / NeuroConv / **`con/nwb2bids`** / ReproStim / ReproNim-containers / con/duct.
  - Extend: a NEW "From RUNCMD to BEP028" mermaid summarizing the upstream-lift pattern.
  - Standardize: BIDS slide + BIDS-minder image (from `2023-bids-dicom.html`) + LinkML/concepts.datalad.org bullets.
  - Federated archives slide (DANDI + EMBER + OpenNeuro) with DANDI deep-dive borrowed from `2023-brain-dandi.html`.
  - "Reuse, in reverse" 3-up table (AnnexTube / mykrok / con/serve).
  - **Automate** section (NEW): **4 slides** — opener + "Where we automate" table (CI / con/tinuous / ReproNim-containers / acquisition / archive mirroring / validation / releases) + "Cost: harnesses, harnesses, harnesses → meta-automation via AI" (with `con/skills` / `con/yolo`) + **"The five verbs climb the SciOps ladder"** mapping (5-verbs ↔ SciOps L1–L5; the SciOps paper itself names BIDS / NWB / DataLad / DANDI / brainlife.io as Level-3 exemplars, and reserves Level 5 — Optimizing — for AI-in-the-loop). Hands off into HI+AI.
  - HI+AI section: opener + "Why every layer matters now" (STAMPED + SciOps) + **"HI ↔ AI — every project picks its own policy"** (NEW): 4-stance spectrum table (Reject / Accept-with-disclosure / Spec-driven AI-generated / Autonomous) with OSS exemplars + CON projects + SciOps level + STAMPED principle, citing ICMJE Jan 2026 and melissawm/open-source-ai-contribution-policies. Pointing to `2026-ca-origami-retreat-aicoding.html` as the deeper-dive companion.
  - **MVC mini-section** (NEW): 4 slides — opener + Models + Views + Controllers — placed between HI+AI and the Monday checklist. Models row covers BIDS / NWB / DuckDB-hive layouts + LinkML / pydantic / JSON Schema / SHACL metadata schemas + DataLad storage; Views row includes a dedicated *Schema-driven UIs* row (vjsf → DANDI meditor; shacl-vue → forms and research-group websites; Hanke et al. LinkML workflow ReproTube reference); Controllers row carries the punchline (*pick any cell — Model, View, or Controller — and swap it; the rest still works*). This block is the **seed of the (now shelved) `_backdrawer_/202x-mvc-stack.html` stub**.
  - Standardize section's "Metadata: schemas as first-class citizens" slide (NEW): expanded from a LinkML+concepts.datalad.org one-liner into a multi-language schema overview (LinkML / pydantic / JSON Schema / SHACL); also names **OBC (Open Brain Consent)** as the *consent* layer of standardization.
  - Monday checklist: 6 entries (was 5) — added an Automate take-home pointing at `con/tinuous`.
  - Monday checklist (NEW; 5-action wrap-up).
  - Acknowledgements + Yoda SVG sign-off.
- Notes: drafted in support of `2026-usrse/talk-proposal-draft.md`.
  Companion files in `2026-usrse/`. QR code TBD; uncomment the
  `data-src` line in the title slide once the live URL is published.

### `2026-ca-origami-retreat-aicoding.html` — *A few words of intro into AI assisted coding*
- **Venue / date**: CA Origami Retreat 2026.
- **Spine**: AI-coding ladder + spec-driven workflow + CON tools.
- **Reusable highlights**:
  - Title slide with Avogadro Corp book reference (intro hook).
  - "Reality Check" disclaimer slide (idiocracy GIF).
  - YODA-Beyond-Code-and-Data table (traditional vs. expanded YODA scope).
  - `con/serve` "The Vault" mermaid diagram (inbound / hub / outbound).
  - **AI Coding Maturity Ladder** Levels 1–5 (Chat → Mid-loop → In-the-loop →
    On-the-loop → Multi-agent).
  - 5-Stage Development Loop mermaid.
  - Mapping table: Vibe coding vs. Spec-driven vs. Compound engineering.
  - Spec-driven tools ecosystem table (spec-kit / OpenSpec / Compound /
    LAD).
  - AI-assisted projects table (mykrok, AnnexTube, con/serve,
    citations-collector, dandi-cli).
  - Reusable-skills table (con/skills repo).
- Notes: planning notes in `2026-ca-origami-retreat-aicoding/PLAN.md`,
  rendered checkpoint screenshots in the same directory.

### `2026-repronim-YODA-BIDS-webinar.html` — *ReproFlow & YODA: Structure your studies*
- **Venue / date**: ReproNim Webinar, 2026-02-06.
- **Spine**: YODA principle-by-principle deep dive with BIDS framing.
- **Reusable highlights**:
  - The full YODA principles canon (`yoda-principles-reordered.png`).
  - Principle 1: Version control everything — `Why version control?`
    table with PhD Comics 1531; VCS-as-experiment slides; `datalad run`
    walk-through; `datalad rerun`; "datalad runs in the wild" registry
    statistics; `git-annex addcomputed`; `con/duct`.
  - Principle 2: Portable compute environments — software-container
    families; `datalad-container`; `ReproNim/containers`;
    `datalad containers-run`; clean-record CEREBRA/MRIQC.
  - Principle 3: Modular composition — modules-and-layouts ladder;
    BIDS as layout; OpenNeuroDerivatives walkthrough.
  - "Look up you must not!" corollary slide
    (`pics/yoda-do-not-look-up.png`,
    `pics/depends-on-untracked-file.png`).
  - Reality Check / disclaimer slide pattern.
- Notes: companion materials in
  `2026-repronim-YODA-BIDS-webinar/{notes,planning}/`.

### `2025-distribits-YODA.html` — *Pragmatic YODA: principles and their wild life encounters*
- **Venue / date**: distribits 2025, recorded
  <https://www.youtube.com/watch?v=EuKVapscUQ4>.
- **Spine**: same YODA spine as the 2026 ReproNim webinar — older but
  shorter; many slides identical and reused there.
- **Reusable highlights**: see ReproNim entry above; this is the *parent*
  of that deck. Use either as a source for YODA section material.

### `2025-ca-origami-retreat.html` — *A challenge on the way to Neuroscience Nirvana: WORKAROUNDS!*
- **Venue / date**: CA Origami Retreat 2025.
- **Spine**: Nirvana / archives / make-re-use-convenient framing.
- **Reusable highlights**:
  - WordNet "nirvana" definition pre block.
  - "Where data go to die / how data are reincarnated" Q-and-A slides
    (Buddha background).
  - "What makes data re-use INconvenient?" two-slide pair (data bugs;
    ad-hoc data access; opinionated software) with bug / feed-me cartoons.
  - "What allows to make data re-use convenient?" — Standards (BIDS) and
    Validation (BIDS).
  - "What if standard does not (yet) fill the bill?"
  - Closing "talk in BIDS" Nirvana slide.

### `2024-distribits-datalad.html` — *"What's in the DataLad sandwich" AKA the DataLad ecosystem*
- **Venue / date**: distribits 2024.
- **Spine**: DataLad origin → sandwich layering → ecosystem → CI / health.
- **Reusable highlights**:
  - "When it began for us" timeline (git → PyMVPA → GitHub →
    git-annex → DataLad first commits).
  - First use case: arjlover crawler → website-crawler-born mermaid.
  - "From an email to a proposal" Joey-email screenshot timeline.
  - "More layers to the sandwich" mermaid (datalad → git-annex →
    git-annex-remote-archives → git-annex → git-annex-remote-datalad).
  - DataLad crawler pipeline gitGraph (incoming → processed → master).
  - DataLad realizations & shortcomings checklist.
  - DataLad **extensions** mechanism + extension template + initial
    extension graph.
  - DataLad core "what it is" definition slide with JOSS citation.
  - DataLad Extensions & Their Health (`pics/datalad-extensions.png`).
  - DataLad Handbook overview (3-row table).
  - "DataLad fulfilled original promise of a Data Distribution"
    (`datasets.datalad.org` snapshot).
  - Examples-of-use: OpenNeuro, brainlife, CONP infrastructure use;
    YODA + ReproNim/containers; DANDI alternative view + Dropbox.
  - "DataLad ecosystem" `DataLad-minder.svg` figure.
  - **CI / testing / monitoring stack**: DataLad-all-changes-are-tested,
    extensions tested daily, git-annex daily, daily-status-email,
    `con/tinuous` archives, datalad-installer.
  - Acknowledgements slide with funders + collaborators.

### `2024-distribits-datalad-name.html` — *"What's in the DataLad name" AKA How come DataLad?*
- **Venue / date**: distribits 2024 (lightning).
- **Spine**: just the naming history (datagit → ftf → datalad).
- **Reusable highlights**: name-history single-slide timeline (good
  warm-up / origin-story slide).

### `2023-brain-dandi.html` — *DANDI: distributed archives for neurophysiology data integration*
- **Venue / date**: BRAIN Initiative talk, 2023.
- **Spine**: archive challenge → DANDI ingredients → standards → testing.
- **Reusable highlights**:
  - "Challenge: Develop a BRAIN Initiative Archive" (radial-gradient
    section divider).
  - "Where data go to die" → DANDI born.
  - "What data is in DANDI" `dandi-slide-modalities.svg`.
  - "Data chronology and demographics"
    `20230622-NWB-and-DANDI-tutorial-updates.svg`.
  - "Ingredients needed to build an archive" — People / Standards /
    Technologies / FOSS / Automations.
  - DANDI users by role (submitter / researcher / developer SVGs).
  - DANDI integrates standards (`20210421-INCF-dandischema.svg`).
  - DANDI ecosystem (`DANDI-ecosystem.svg`).
  - **Testing the entire archive**: docker-compose; DataLad-mirroring
    of dandisets; `con/tinuous`; webshots; trivial IO across all
    dandisets (`dandisets-healthstatus.png`).
  - "DANDI ..." final summary bullets (modular FOSS, integrates,
    novel-tech adoption, automated QA).

### `2023-lbl-building-dandi.html` — *Building an Archive for Large-scale Neuroscience Data*
- **Venue / date**: LBL talk, 2023.
- **Spine**: same as `2023-brain-dandi.html` but longer; with a Brief
  Bio section for general-audience framing.
- **Reusable highlights**: see DANDI entries above; this is the larger
  parent deck. Includes:
  - "Brief Bio" slide (Born in Siberia → Ukraine → US trajectory).
  - "Standard for neurophysiology data: NWB" slide.
  - "Standards make DANDI FAIR for People" slide.
  - DANDI schema deeper-dive (`dandi-slide-schema.svg`).

### `2023-bids-dicom.html` — *BIDS 4 DICOM WG-16*
- **Venue / date**: DICOM WG-16 meeting, 2023.
- **Spine**: BIDS as a meta-standard, and where BIDS ↔ DICOM
  collaboration could go.
- **Reusable highlights**:
  - "Brief Bio" (variant).
  - BIDS-Steering iframe slide.
  - "Standard for neural datasets: BIDS" with the 2016 BIDS Sci Data
    citation (canonical citation slide).
  - "BIDS ..." features bullets, including "you've seen one BIDS dataset
    you've seen them all".
  - BIDS-minder upstream-images slide
    (`bids-standard.github.io/.../BIDS-minder.svg`).
  - DICOM ↔ BIDS chronology (1982 DICOM → 2014 BIDS).
  - Clunie MICCAI 2017 5-image fragments (data is in `pics/2017-Clunie-*.png`).
  - **"All standards are 'Bad', but some are used"** — recurring
    rhetorical slide.
  - DICOMs in BIDS workflow (sourcedata, .json sidecars, BEP019, PR#1450).

### `2023-brain-dandi-imgdatasrc.html` — short DANDI talk
- Tiny deck (86 lines), title-only template; safe to ignore as source.

### `2022-nih-compcore.html` — *An Integrated and Trusted Scientific and Statistical Computing Core*
- **Venue / date**: NIH SSCR pitch, 2022.
- **Spine**: trust → noise → human IO → standards → FOSS distribution
  → data management → archive → all the projects in one walk.
- **Reusable highlights**:
  - Yarik-goal cartoon (`pics/yarik-goal.svg`) — the "north star".
  - "Brief Bio" slide (canonical version; reused in 2023 talks).
  - CON principles (`con-principles.png`) — used in title slides.
  - **"Integration & Trust Tiers"** ladder (Social / Data acquisition /
    Methods/Analytics / Software systems / Data management / Services).
  - "Trust is largely a social aspect" framing slides.
  - "How can we minimize unexplained variance?" — minimize-human-IO
    bullets, simulations, assertions, peer-review, provenance, re-use.
  - **3rd-party / "God-is-at-the-computer"** slide (recursive trust).
  - Phantom QA / Nuisance study figure (F1000 2020 citation).
  - **ReproNim 5 steps** (`pics/repronim-5steps.png`,
    <http://5steps.repronim.org>).
  - OBC (Open Brain Consent) born-in-2014 slide; outcomes; OBC tools.
  - "Challenge: minimize human IO to understand data" → BIDS → BIDS-Apps.
  - **ReproIn / HeuDiConv** sequence-naming → automated BIDS slides.
  - **Beyond ReproIn**: ReproStim / ReproEvents / con/noisseur.
  - "Challenge 2007: no ML framework" → **PyMVPA** features /
    classification / searchlight / hyperalignment / TRANSFusion;
    PyMVPA-on-phone deployment punchline.
  - **NeuroDebian** born-2009 slide; integration figure;
    user-perspective figure; `nd_overview.svg` developer view; benefits
    bullets (Conda-Forge / Fedora / Gentoo handoff,
    "Containerization comes for free").
  - **DataLad-in-one-figure** (`pics/datalad_process_tuned/00base_preview.png`).
  - Provenance capture: 3-step `datalad run` / `datalad containers-run`
    / `datalad rerun` code blocks.
  - **Extend DataLad** extensions overview.
  - DataLad CI / health (testing-extensions / git-annex daily /
    `con/tinuous` archive).
  - "In DataLad We Trust" + decentralized RDM citation.
  - **DANDI**-section duplicate (modalities / services / standards /
    schema / "Webshots of all dandisets").
  - Closing "Integrated and Trusted" bullet manifesto.
- This deck is the **richest single source** of reusable CON-history
  material — borrow heavily for any retrospective talk.

### `2022-tx-big-neuroscience.html` — *Towards the Big Data Neuroscience Nirvana*
- **Venue / date**: ACNN Workshop 2022 (Texas).
- **Spine**: Nirvana / archives / making re-use convenient + DataLad CI
  health quick tour.
- **Reusable highlights**: prototype of the Nirvana arc later refined in
  `2025-ca-origami-retreat.html`. Includes "Big Data" section, the
  largest-Git-repo / `datasets.datalad.org` snapshot, the for-users /
  for-developers slide pair, and DataLad / extensions / git-annex daily
  validation triplet.

### `0000-zoom-background.html` — Zoom background slide template
- Not a talk; layout source for sharing CON banner during Zoom.

## Shelved (backdrawer)

Outline-only stubs and parked drafts. See
[`_backdrawer_/README.md`](_backdrawer_/README.md) for the convention
(filenames preserved so the published URL still works on revival,
symlink-into-root pattern for live preview, `git mv` to promote back to
active status).

### `_backdrawer_/202x-mvc-stack.html` — *[WiP] MVC at the stack scale: what makes the open-(neuro)science stack compose*  *(shelved stub)*
- **Status**: **Shelved in `_backdrawer_/`** — outline-only stub, no
  venue lined up. The MVC framing lives on as a 4-slide mini-section
  inside `2026-usrse-con-talk.html`. If revived: `git mv` the file back
  to the root, rename to `<YYYY>-<venue>-mvc-stack.html`, drop the
  `[WiP]` prefix, and regenerate the QR code (the URL changes with the
  filename).
- **Spine**: re-reads the four CON verbs as Model–View–Controller at
  the *stack* scale.
- **Authoring seed**: the 4-slide MVC mini-section inside
  `2026-usrse-con-talk.html` is the seed; promote each row into its own
  slide here, plus borrow visuals from the per-topic lookup below.
- **Section openers in place**:
  - "One thesis, two parts" — explicit MVC-at-stack-scale claim.
  - "Why 'at the stack scale' is the new word" — classical-vs-stack-MVC contrast.
  - **Models**: Dataset layout / Per-file / Metadata / Storage (4 stub slides).
  - **Views**: Browse-the-archive humans / Tabular ad-hoc / Programmatic / External services / **Schema-driven UIs** (vjsf → DANDI meditor; shacl-vue → forms + research-group websites) / Long-form narrative.
  - **Controllers**: Acquisition→layout / Reproducible execution / Logistics / Data→derivative / **Validation — and a recursive Standardize moment** (the latter is now the most fleshed-out slide: con/validation harmonizes bids-validator + HED + pynwb + zarr + nwbinspector + OME-Zarr; deployed in dandi-cli; VisiData for triage).
  - **Contrast: the "service-tied UI" pattern** section (NEW): four slides walking through the academic anti-pattern (LIMS / ELN / "just a Flask app"), naming the design-pattern literature (Smart UI [Evans], Anemic Domain Model [Fowler], Hexagonal / Ports & Adapters [Cockburn 2005], Adapter / Strategy / Façade [GoF], Service Layer [PoEAA]), and showing CON's static-first contrast (datasets.datalad.org as plain `nginx`, schema-driven UIs, JAMstack-style decks). Includes a "if your project dies when the server is down for a week..." heuristic.
  - **One stack, many lenses** section: a table of six lenses (Architectural / Procedural / Sharing / Compositional / Purpose / Maturity) mapping to MVC / STAMPED / FAIR / YODA / project-purpose / AI-ladder. Captured as a recurring framing in `SOUL.md` §1.
  - "Three things to do this week" closer.
- TODO markers in-file flag what to fill in.

## Topic-wise lookup

Use these as a fast "where do I steal a slide for X?" cheat sheet.

### Reuse / upstream contribution / NeuroDebian
- `2022-nih-compcore.html` § "NeuroDebian from user perspective", § "Under-the-hood for a NeuroDebian developer", § Overall benefits.
- `2024-distribits-datalad.html` § "git-annex is built and tested daily", § datalad-installer, § acknowledgements.
- *Asset*: `pics/neurodebian*.{png,svg}`, `pics/nd_overview.svg`,
  `pics/neuropy_history.svg`.

### Compose / DataLad ecosystem / sandwich layering
- `2024-distribits-datalad.html` § Sandwich mermaid, § Extensions
  template, § DataLad ecosystem (`DataLad-minder.svg`), § "DataLad for
  developers".
- `2022-nih-compcore.html` § Provenance + extensions list.
- *Asset*: `pics/DataLad-minder.svg`, `pics/datalad-extensions.png`,
  `pics/tall-burger.png`, `pics/datalad_process_tuned/`.

### Compose / small acquisition+compute units (HeuDiConv / ReproStim /
ReproNim-containers / con/duct / ReproMan)
- `2022-nih-compcore.html` § ReproIn / HeuDiConv / Beyond-ReproIn.
- `2025-distribits-YODA.html` § "datalad-container", § "ReproNim/
  containers" walkthrough, § ReproMan reference.
- `2026-repronim-YODA-BIDS-webinar.html` § same Principle 2 section.
- `2025-distribits-YODA.html` § con/duct; § "datalad runs in the wild";
  § `git-annex addcomputed`.
- *Asset*: `pics/webshot-repronim-containers.png`,
  `pics/repronim-containers-{workflow,show,yoda-lower}.png`,
  `pics/webshot-con-duct.png`, `pics/screenshot-duct-*.png`,
  `pics/duct-mriqc-cerebra.png`, `pics/borrowed/reproin-logo.jpg`.

### Extend / standards work / BIDS BEPs
- `2023-bids-dicom.html` § BIDS features, § BIDS-minder, § DICOMs-in-BIDS
  workflow, § "All standards are bad, but some are used".
- `2022-nih-compcore.html` § Microscopy-BIDS citation.
- *Asset*: `pics/BIDS-minder.svg`, `pics/bids-logo-wide.png`,
  `pics/bids-yoda.png`, `pics/bep028-example1.png`.

### Standardize / data archives / DANDI / OpenNeuro / federation
- `2023-brain-dandi.html` (whole deck) — best DANDI walkthrough.
- `2023-lbl-building-dandi.html` — extended version.
- `2024-distribits-datalad.html` § DANDI alternative-view slide;
  § OpenNeuro infrastructure use.
- *Asset*: `pics/dandi-slide-{modalities,services,standards,schema}.svg`,
  `pics/DANDI-{ecosystem,FAIR,users-*}.svg`,
  `pics/dandiarchive-webshots.png`, `pics/dandisets-healthstatus.png`.

### YODA principles + "Look up you must not"
- `2025-distribits-YODA.html` and `2026-repronim-YODA-BIDS-webinar.html`
  — full YODA spine.
- *Asset*: `pics/yoda*.{png,svg}`, `pics/principle-{vcs,computeenv,
  structure}.png`, `pics/depends-on-untracked-file.png`,
  `pics/yoda-hierarchy-with-containers.png`,
  `pics/yoda-do-not-look-up.png`, `pics/yoda-all-the-way-down.png`.

### Provenance / `datalad run` / `datalad rerun` / RUNCMD → BEP028
- `2025-distribits-YODA.html` and `2026-repronim-YODA-BIDS-webinar.html`
  § Principle 1.
- `2022-nih-compcore.html` § Provenance capture (3 code-block slides).
- `2024-distribits-datalad.html` § DataLad crawler gitGraph.

### CI / con/tinuous / daily-tested git-annex / health dashboards
- `2024-distribits-datalad.html` § three-image stack of
  PR-test screenshots; daily-status email iframe; `con/tinuous`.
- `2023-brain-dandi.html` § identical CI slides re-used for DANDI.
- `2022-nih-compcore.html` § "PART of an answer: AUTOMATION" + 3
  testing slides.
- *Asset*: `pics/con-tinuous-{github,term,term-dandi-cli}.png`,
  `pics/datalad-extensions.png`, `pics/datalad-git-annex.png`,
  `pics/webshot-datalad-installer.png`,
  `pics/datalad-daily-status-email-subject.png`,
  `embed/datalad_git-annex_daily.html`.

### Trust / accountability / variance / phantom QA / OBC
- `2022-nih-compcore.html` § "Trust is largely social", § Nuisance
  study, § ReproNim 5 steps, § OBC born/outcomes/tools.
- *Asset*: `pics/god-is-at-the-computer.jpg`,
  `pics/MRI-scanner.png`, `pics/f1000-webshot-20200930*.png`,
  `pics/repronim-5steps.png`, `pics/OBC_LogoCheck.svg`,
  `pics/obc-{main,ultimate,tools}.png`.

### PyMVPA / "we ported the intent upstream"
- `2022-nih-compcore.html` § PyMVPA Features → searchlight →
  hyperalignment → TRANSFusion → "phone deployment".
- *Asset*: `pics/pymvpa*.png/svg`,
  `pics/pymvpa_logo_fromfusionposter.svg`,
  `pics/pymvpa_on_phone.jpg`,
  `pics/uniform_analysis.svg`.

### "Make re-use convenient" / Nirvana framing
- `2025-ca-origami-retreat.html` — full deck.
- `2022-tx-big-neuroscience.html` — original.
- `2023-brain-dandi.html` § "Where data go to die".

### AI angle / HI+AI / AI-coding ladder / con/serve
- `2026-ca-origami-retreat-aicoding.html` — full deck.
- `2026-repronim-YODA-BIDS-webinar.html` § hand-off to AI talk
  (Appendix-style slide referenced from the AI talk's "Previously on…").
- *Asset*: `pics/borrowed/ai-ladder-skills.png`,
  `pics/borrowed/2026-ai-intensifies.png`,
  `pics/surface-depth-v2.jpg`, `pics/borrowed/idiocracy-fixed.gif`.

### MVC framing / "why the stack composes"
- `2026-usrse-con-talk.html` § "Why it composes — MVC at the stack scale" (4-slide mini-section: opener + Models + Views + Controllers table).
- `_backdrawer_/202x-mvc-stack.html` *(stub)* — the standalone deck spun out of that mini-section.
- *Asset*: re-uses existing tables; no new images required for the seed.
  When deepening the standalone talk, borrow `pics/DataLad-minder.svg`
  (storage model), `pics/BIDS-minder.svg` (dataset-layout model), and
  the controllers screenshots from
  `2025-distribits-YODA.html` / `2026-repronim-YODA-BIDS-webinar.html`.

### Validation harmonization (con/validation)
- `2026-usrse-con-talk.html` § MVC mini-section's Controllers row
  ("Validation *(and harmonization)*") names `con/validation` as the
  harmonizer for bids-validator (+ HED) / pynwb / zarr / nwbinspector /
  OME-Zarr / LinkML validators, deployed in dandi-cli.
- `_backdrawer_/202x-mvc-stack.html` § Controllers/"Validation — and a recursive
  Standardize moment" — the long-form treatment: *con/validation is the
  type-checker for your validators*; once results are one Model, Views
  are easy (dashboards, VisiData on the validation TSV).
- *External*: <https://github.com/con/validation>;
  deployed in <https://github.com/dandi/dandi-cli>.

### Automate / harness / meta-automation
- `2026-usrse-con-talk.html` § Automate (3 slides: opener, "Where we
  automate" table, "Cost: harnesses, harnesses, harnesses → meta-
  automation via AI"). Cites con/tinuous as the canonical CI-archival
  example (highly modular, fits con/serve's archival mission).
- *Older talks with reusable CI/automation slides*:
  - `2024-distribits-datalad.html` § "DataLad: all changes are tested",
    "extensions tested daily", "git-annex daily", `con/tinuous` archive,
    `datalad-installer`.
  - `2022-nih-compcore.html` § "PART of an answer: AUTOMATION" + the
    same three testing slides.
  - `2023-brain-dandi.html` § "Dandisets converted into DataLad and
    pushed to GitHub", "Webshots of all dandisets", "Testing trivial
    IO across all dandisets".
- *Asset*: `pics/con-tinuous-{github,term,term-dandi-cli}.png`,
  `pics/datalad-extensions.png`, `pics/datalad-git-annex.png`,
  `pics/datalad-daily-status-email-subject.png`,
  `embed/datalad_git-annex_daily.html`,
  `pics/dandiarchive-webshots.png`,
  `pics/dandisets-healthstatus.png`.
- *Meta-automation framing*: harness maintenance is the place where AI
  assistance becomes most viable for a small RSE center; pair with
  `con/skills` and `con/yolo` (per `2026-ca-origami-retreat-aicoding.html`).

### HI ⇄ AI policy spectrum (per-project AI-acceptance)
- `2026-usrse-con-talk.html` § "HI ↔ AI — every project picks its own policy" (in the HI+AI section): a 4-row spectrum table mapping policy stance ↔ OSS exemplars ↔ CON project ↔ SciOps level ↔ STAMPED property:
  - **Reject** — Zig, Krita, Clojure, QEMU; `git-annex` (Joey Hess's "Feb 30" satirical policy).
  - **Accept with disclosure** — NumPy, Kubernetes, Linux, Django; **DataLad / DANDI** with `Co-Authored-By` trailers, `@pytest.mark.ai_generated`.
  - **Spec-driven AI-generated** — **AnnexTube**, **mykrok**, **con/citations-collector**, parts of **dandi-cli**.
  - **Autonomous** — **con/skills** + **con/yolo** workflows.
  Common ground per [ICMJE Jan 2026](https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html): AI cannot be author, humans retain responsibility, disclosure mandatory.
- *External survey*: [`melissawm/open-source-ai-contribution-policies`](https://github.com/melissawm/open-source-ai-contribution-policies) — community-maintained catalog of declared OSS policies; the three+one bucket framework (Accept / Restrict / Reject / Ongoing) is what the slide's 4-stance spectrum is built on.
- *SOUL.md §1* names this as a recurring framing — use it for any deck that touches AI contributions.

### Backend-coupled "service-tied UI" anti-pattern / Hexagonal contrast
- `_backdrawer_/202x-mvc-stack.html` § "Contrast: the 'service-tied UI' pattern"
  (4 slides): the anti-pattern in academia, design-pattern names
  (Smart UI / Anemic Domain Model / Hexagonal-Ports-Adapters / Adapter /
  Strategy / Façade / Service Layer), CON's static-first counter-pattern.
- *Citations*: Cockburn, *Hexagonal Architecture*, 2005
  <https://alistair.cockburn.us/hexagonal-architecture/>; Evans,
  *Domain-Driven Design*, 2003 (Smart UI anti-pattern); Fowler,
  *Patterns of Enterprise Application Architecture*
  (<https://martinfowler.com/eaaCatalog/serviceLayer.html>; Anemic
  Domain Model: <https://martinfowler.com/bliki/AnemicDomainModel.html>);
  Gamma, Helm, Johnson, Vlissides (GoF), *Design Patterns*, 1994
  (Adapter / Strategy / Façade).
- Use this slide block when an audience is more enterprise-software-
  literate than data-archive-literate, or when a critic asks
  "why don't you just build a portal?".

### Five verbs ↔ SciOps maturity levels
- *Mapping* (Johnson *et al.*, 2024; <https://arxiv.org/abs/2401.00077>):
  - **L1 Initial** — ad-hoc; no CON verb yet.
  - **L2 Managed** — Compose (lab-local; YODA layout).
  - **L3 Defined** — Reuse / Compose / Extend / Standardize; FAIR data + FAIR workflows. *Paper-cited L3 exemplars*: BIDS, NWB, DataLad / git-annex, DANDI, brainlife.io.
  - **L4 Scalable** — Automate; "SciOps pipelines" (semi-automated continuous workflows).
  - **L5 Optimizing** — Automate × AI; closing the discovery loop.
- *Slide anchors*: `2026-usrse-con-talk.html` § Automate's 4th slide ("The five verbs climb the SciOps ladder"); `_backdrawer_/202x-mvc-stack.html` § Many-lenses Maturity row (now spells out all 5 levels); `2026-usrse-con-talk.html` § HI+AI's updated SciOps bullet (STAMPED = per-artifact, SciOps = team-operations).
- *SOUL.md §7* explicitly lists the verb→level mapping; cite it from any future deck that wants to talk about maturity.
- *Practical implication*: when you name one of the 5 verbs in a slide, mention which SciOps level it corresponds to — CMM language travels well to RSE audiences.

### Multi-dimensional framings ("many lenses, one stack")
- `_backdrawer_/202x-mvc-stack.html` § "One stack, many lenses" — table of six
  lenses (Architectural / Procedural / Sharing / Compositional / Purpose
  / Maturity) with example axes:
  - Architectural → MVC (this talk's spine)
  - Procedural → **STAMPED** — Self-containment, Tracking, Actionability, Modularity, Portability, Ephemerality, Distributability (Macdonald et al. 2026, [stamped-paper](https://github.com/stamped-principles/stamped-paper))
  - Sharing → FAIR
  - Compositional → YODA
  - Purpose → acquisition / curation / archive / analysis / governance / sharing / training
  - Maturity → **SciOps** five-level CMM (Johnson et al. 2024, [arXiv:2401.00077](https://arxiv.org/abs/2401.00077)) + AI-coding ladder L1–L5 for the agentic-readiness sub-axis.
  Use this slide when a talk needs to triangulate several patterns at
  once instead of pitching one.
- *SOUL.md §1* names this as a recurring framing — read it before
  writing a talk that compares projects/properties along multiple axes.
- Both STAMPED and SciOps now have entries in `SOUL.md` §5 (canonical
  citations), so any future deck can cite them with one-line consistency.

### Schema-driven UIs / "the Model materializes the View"
- `2026-usrse-con-talk.html` § Standardize → "Metadata: schemas as first-class citizens" (LinkML / pydantic / JSON Schema / SHACL bullets) and § MVC mini-section's Views slide (vjsf → DANDI meditor; shacl-vue → forms + research-group websites).
- `_backdrawer_/202x-mvc-stack.html` *(stub)* § Models → "Metadata: many languages, one idea" and § Views → "Schema-driven UIs: the View that the Model generates".
- *External reference*: M. Hanke et al., **LinkML metadata-driven workflow** —
  on ReproTube: <https://datasets.datalad.org/repronim/ReproTube/DataLad/web/#/video/oF98hdaph1k?tab=local&wide=1&t=644&q=model&filter=1>
  (YouTube id `oF98hdaph1k`, timestamp 644s); cite when borrowing or expanding the schema-driven-UI argument.
- *Suggested screenshots to add later*: DANDI meditor at <https://gui.dandiarchive.org/>; a `shacl-vue`-rendered website (per psychoinformatics-de's deployments).

### CON identity / acknowledgements / funders
- `2024-distribits-datalad.html` final acknowledgements slide is the
  canonical layout: software → some-slides-origin → Funders → Collaborators.
- `2022-nih-compcore.html` § "Trust ladder" CON banner.
- *Asset*: `pics/con-{principles,ack-*,webshot-*,logo_*}.{png,svg}`,
  `pics/con-ccn-dartmouth-letterhead.svg`,
  `pics/borrowed/{nih,nsf*,bmbf_2020,binc,erdf,cbbs_logo,LSA-Logo,fzj_logo,
  hbp_logo,conp_logo,vbc_logo,repronim_logo,openneuro_logo,cbrain_logo,
  brainlife_logo,dandi_logo,bannerthanks}.{png,svg,jpg}`.

### Speaker bio / "Brief Bio" slides
- `2022-nih-compcore.html`, `2023-bids-dicom.html`,
  `2023-lbl-building-dandi.html` — three near-identical versions of
  Yarik's bio + CON-principles `r-stack`.

### Title / opening hook archetypes
- `2025-ca-origami-retreat.html` opens with "WORKAROUNDS!" reveal.
- `2026-repronim-YODA-BIDS-webinar.html` opens with Reality-Check GIF.
- `2024-distribits-datalad.html` opens with QR code + logo strip
  (canonical template).

### Closing slides
- "Save your questions for the panel discussion" / "Let me know what to
  fix":
  `2024-distribits-datalad.html`, `2025-distribits-YODA.html`,
  `2026-ca-origami-retreat-aicoding.html` ("Let the AI agents be with
  you", with the Yoda SVG as a sign-off).

## How to use this index

1. **Pick a story arc** from `SOUL.md` §7.
2. Walk the per-talk list above for the arc's parent deck — its slide
   anchors are your "free" content.
3. For each section of the new deck, consult the *topic-wise lookup* to
   pull supporting slides from sibling decks rather than re-creating
   them.
4. When you copy a slide, update relative `data-src` paths only if the
   new deck lives in a subdirectory (it shouldn't — keep new decks at
   the repo root).
5. Add the new deck to this index when committed.
