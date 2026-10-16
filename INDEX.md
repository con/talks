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
(`_backdrawer_/<TALK-ID>.html`). Posters are listed in their own
*Posters* section after the talks.

### `2026-reproAI-MIT-STAMPED.html` — *STAMPED principles and their role in the age of AI-driven scientific software development*
- **Venue / date**: [*Neuroimaging, Reproducibility and LLMs: Early promises
  and future question*](https://www.eventbrite.com/e/neuroimaging-reproducibility-and-llms-early-promises-and-future-question-tickets-1999618019324)
  — a ReproNim workshop at MIT (Building 46, Cambridge MA), 2026-10-16,
  09:30–13:00; my slot 11:10–11:40 (25 min + 5 min Q&A).
- **Spine**: hybrid of the *Challenges → Solutions → Take-home* arc
  (`SOUL.md` §7.2) with the AI flavoring of §7.5. Five acts:
  Frame → *What changed* → STAMPED → *What makes it actionable* →
  *Harnesses and skills as shareable artifacts* → Close.
  Parent decks: `2026-repronim-YODA-BIDS-webinar.html` (provenance
  slides) and `2026-ca-origami-retreat-aicoding.html` (AI framing).
- **Thesis**: agents do not fail for lack of intelligence, they fail for
  lack of *structure to act on*; **Actionability** is the load-bearing
  STAMPED property for agents, and **standards are what make it cheap**.
  The next thing owed to the commons is not more code but **shared
  harnesses and skills**.
- **Reusable highlights**:
  - Title slide (per `SOUL.md` §3) — note the logo strip swaps OBC for
    `pics/stamped-yoda.svg` linking to stamped-principles.org.
  - **STAMPED section opener** using `pics/borrowed/stamped-banner_ver-3.svg`
    (the project's own banner: the seven words with icons, 385×100 mm).
    Much stronger than a text-only opener — reuse it in any STAMPED deck.
  - **"Standing on two talks"** two-column credit slide (NEW): the
    ReproNim YODA webinar + [Oscar Esteban's OHBM 2026 AI
    Educational](https://www.nipreps.org/presentations/2026-OHBM-AI-Educational/).
    The *Agent = Model + Harness* formulation is borrowed from it with
    attribution; reuse this slide shape whenever a deck picks up where
    someone else's left off.
  - **"Without structure, the agent has to guess"** (NEW, *the hinge
    slide of the deck*): side-by-side `study_final2/` vs. a BIDS tree,
    with "*Infer.*" repeated down the left column. Domain-agnostic —
    swap the right-hand tree for any standard.
  - **"STAMPED in one table"** (NEW): all seven properties with a third
    column, *what it buys an agent*. The single most portable slide here.
  - **"STAMPED and FAIR do different jobs"** (NEW): sharing vs.
    operational, three-row contrast.
  - **"Actionability is the one that agents live or die on"** (NEW) —
    carries the Clunie "all standards are bad" line into the AI frame.
  - **"…and AI changed *what counts as* actionable"** (NEW, *the pivot
    of the deck*): three-row escalation — *Before* (exact command/API →
    tools and humans who already knew) / *Now* (a procedure described in
    **human language** + scripts where precision matters → **any agent on
    first contact**; the interface moved from syntax to language) /
    *Next* (routines that fire without being asked → **the harness**
    acts). Plus a two-column breakdown: **Skills** (language carries the
    judgement, scripts the precision, one-skill-one-job) and **Routines**
    (Claude Code on the web watching a repo, scheduled agents, CI).
    Punchline: *AI made automation on top of actionability cheap — that
    is the real multiplier.*
  - **"So grade *them* too: a skill is a research object"** (NEW, *the
    recursive turn*): seven-row table mapping each STAMPED property onto
    a skill/automation. Punchline: **good automation and good skills
    pass the STAMPED checklist — that is what makes them reusable beyond
    the author.** Absorbs the checklist / examples / `main.tex` links.
  - Provenance block borrowed from the ReproNim webinar: `datalad run`
    RUNCMD record, "provenance doesn't care who wrote the code" beat
    (from `2026-usrse-con-talk.html`), `con/duct` webshot.
  - **The BIDS→provenance bridge** (NEW, on the BIDS slide): *"a layout
    only tells you **what** the files are"* →
    **standard → `datalad run` → `duct` = what it is → how it was made →
    what it took.** The one-line connective tissue that makes Act III
    read as one argument instead of three tool demos. Steal it verbatim.
  - **"…and *that log is* the provenance you need later"** (NEW):
    `con/duct` reframed for an AI audience — three operator questions
    (OOM? how much to request? what did it print?) answered by the
    trace rather than by recollection. `REPRONIM_USE_DUCT=1` pointer.
  - **"Agent = Model + Harness"** harness-anatomy table (NEW): each
    harness piece (`AGENTS.md` / skills / hooks / MCP / sandbox) mapped
    onto the STAMPED property it satisfies.
  - **"We are already doing this — upstream, in public"** (NEW): the
    [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills)
    contribution table — `skills/bids` ([PR #125](https://github.com/K-Dense-AI/scientific-agent-skills/pull/125), ours, merged),
    `skills/datalad` ([PR #227](https://github.com/K-Dense-AI/scientific-agent-skills/pull/227), Dylan Pulver, merged with our upstream review),
    [PR #265](https://github.com/K-Dense-AI/scientific-agent-skills/pull/265) (Brent McPherson — STAMPED→DataLad command mapping, *open* as of 2026-10-05),
    [issue #217](https://github.com/K-Dense-AI/scientific-agent-skills/issues/217) ("should STAMPED be its own skill?" + where domain skills should live).
  - `con/skills` table, refreshed against the current repo listing.
  - **"Two regimes — and be honest about which one you are in"** (NEW,
    *the thesis slide of the deck*): **A. scaffolded self-verification**
    (executable spec the loop is checked against; tests/validators as
    the oracle — the loop must be able to *fail*; provenance so drift is
    detectable; automated gates before human eyes) vs. **B. small,
    human-reviewable, hand-tried** (a readable diff as a *design
    constraint, not a courtesy*; one concern per change; run it by hand
    before you believe it; reversibility as the safety mechanism).
    Punchline: *the safe size of an AI-assisted work item is set by the
    strength of your verification loop* — and the way out of B is
    **A**ctionable specs + **T**racked provenance + **M**odular units,
    i.e. STAMPED again. Kicker correctly attributes *"less is more"* to
    **Robert Browning, *Andrea del Sarto*, 1855** (Mies van der Rohe
    popularised it and credited Peter Behrens) — reuse the attribution,
    it is almost always got wrong.
  - **"We are not the only ones saying this"** (NEW): the receipts table —
    [DORA 2025](https://dora.dev/insights/balancing-ai-tensions/)
    ("small batches is a critical countermeasure"; "verification is a
    fundamentally different cognitive task than creation"),
    [METR RCT 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
    (19% slower / felt 20% faster — cite for the *perception gap*; METR
    labels it historical),
    [Addy Osmani](https://addyo.substack.com/p/code-review-in-the-age-of-ai)
    ("proof over vibes"),
    [Simon Willison](https://simonwillison.net/2025/Dec/18/code-proven-to-work/)
    ("deliver code you have proven to work"), and Faros telemetry
    (PR size +51%, review time +441%, incidents/PR +243%).
    **The best single slide in the corpus for arguing AI-assisted work
    discipline to a skeptical or an over-enthusiastic audience.**
  - HI ↔ AI 4-stance policy table (trimmed from `2026-usrse-con-talk.html`),
    now prefaced by the regime mapping (*rows 1–2 are regime B; rows 3–4
    are only honest once regime A is built*),
    with the **Autonomous** row now naming real exemplars:
    [Brain Researcher](https://brain-researcher.com/) (Poldrack lab,
    [arXiv:2608.19902](https://arxiv.org/abs/2608.19902)) and
    [K-Dense AI](https://github.com/K-Dense-AI/). Footnote: both are
    *harnesses* — **autonomy is bought with structure, not a bigger
    model**. The same paper supplies the hinge slide's evidence
    footnote (tool-selection accuracy 23.3% → 93.6% across 7 models).
  - 6-item Monday checklist (incl. *size the work to the loop you
    actually have*); canonical Acknowledgements; STAMPED-Yoda closer.
  - **"All three layers, one real artifact — built with AI"** +
    **"So I tried to `rerun` it. Live, on this laptop."** (NEW, 2 slides,
    *the strongest evidence in the deck*): the
    [`dandi/compression-comparisons-t261-study`](https://github.com/dandi/compression-comparisons-t261-study)
    worked example — BIDS-shaped layout, tool and 523 GB data as
    subdatasets pinned by commit, and `[DATALAD RUNCMD]` records whose
    `cmd` **is** a `duct` invocation. Verified counts (2026-10-06):
    1265 commits / 1216 RUNCMD / 1095 wrapping `duct` / 912 cells, 0
    errors / 3838 h recorded compute / 26 `Co-Authored-By: Claude`.
    The second slide reports an **actual rerun from a clean clone**:
    every scientific number (`cr`, `encoded_bytes`, `rmse`,
    `round_trip_ok`, `signal_std`) came back **bit-for-bit** across a
    different machine, kernel and Python patch — and the *one* thing
    that broke was **D**istributable (a `.gitmodules` `url = ../..` that
    resolves only on the author's disk). See `PLAN.md` §4b for the full
    method, and reuse this as the canonical "STAMPED, graded by actually
    being someone else" example.
  - **"Where are *you* on the ladder?"** (NEW): `ai-ladder-skills.png`
    beside a condensed L1–L5 table (*what it looks like* / *the skill you
    have to acquire*). Punchline: **L4–L5 is where a bad harness stops
    being survivable — invest in the harness, not the model.**
    Credit: Jo Van Eyck, *You are Not Ready: Agentic coding in 2026*.
  - **"And the loop that gets you up it"** (NEW): 5-stage mermaid beside
    the **development-model mapping** (vibe coding / spec-driven /
    compound engineering). Punchline: **stage 5 is where a skill is
    born**, and what it writes down is exactly the artifact that must be
    STAMPED. This is the best pairing of the loop with the dev models in
    the corpus — prefer it over the markdown version in
    `2026-ca-origami-retreat-aicoding.html`.
  - **"That was the *individual* ladder. Here is the *team* one."**
    (NEW): the **SciOps maturity figure**,
    `pics/borrowed/neuro-sciops-fig.svg` (derived at authoring time from
    the annexed `pics/borrowed/neuro-sciops.pdf` via `pymupdf`'s
    `get_svg_image(text_as_path=True)`; the source PDF is pure vector, so
    prefer SVG over a raster render — sharper at projector scale and in
    the PDF export, and smaller than the PNG it replaced). **The figure is credited on-slide to the SciOps preprint**
    (Johnson, Nguyen, Dichter, …, Martone, Pestilli, Yatsenko;
    [arXiv:2401.00077](https://arxiv.org/abs/2401.00077)) — reuse it the
    same way; it is not a CON figure. Punchline: *L5 presupposes L3.*
  - **Appendix vertical stack** (skipped in a 25-min delivery): STAMPED
    vs. FAIR, Portable+Ephemeral, the long-form AI-coding ladder,
    BEP028, `con/yolo` + `con/serve`, related-CON-talks table.
- Companion **video playlist** spec: `2026-reproAI-MIT-STAMPED/playlist.md`
  — 8 videos for the ReproNim YouTube channel, with **yt-dlp-verified
  licences** (4 CC-BY on the DataLad channel, 1 ReproNim-own, 3 Standard
  Licence that are linked but never mirrored) and the ReproTube archival
  status (all mirrorable ones *already archived*). Reuse the verification
  one-liner in that file before any future mirroring decision.
- Notes: plan in `2026-reproAI-MIT-STAMPED/PLAN.md` (includes pre-delivery
  TODOs: confirm the workshop's official name, re-check PR #265 state,
  publish the playlist).
  Deck is 41 slides (34 main + 7 appendix); verified rendered with no
  broken images, no console errors, and no slide overflowing the
  1400×1050 canvas by more than ~42px. **34 main slides is well over
  budget for the 25-min slot** — four main-deck slides carry a
  `SKIP CANDIDATE` marker in their `<aside class="notes">`; dropping all
  four lands at 30, still ~2 long. See `PLAN.md` §6 for the cut order.

### `2026-dhmc-ieeg.html` — *Open Neuroscience Infrastructure for Intracranial EEG*
- **Venue / date**: Dartmouth/DH Human Intracranial Electrophysiology
  Consortium (monthly Zoom meeting), 2026-10-09; ~40 min + discussion.
  Planning and audience notes: `2026-dhmc-ieeg/NOTES.md`.
- **Spine**: a *toolbelt, not one solution* tour for an iEEG group
  (macro- now, microelectrodes soon): clinic vs. academia → participants
  and consent → NWB → NWB apps (Neurosift) → archives → BIDS →
  nwb2bids / ReproStim / HED / sync → compute → DataLad → STAMPED →
  take-home checklist. Each block ends with an explicit *ask* of the
  audience.
- **Written in markdown**: every top-level section is one
  `data-markdown` textarea (`----` separators, `.slide:` comments,
  `Note:` speaker notes); only the title and the who-we-are grid stay
  HTML. The header comment explains the convention — copy it for new
  markdown-first decks.
- **Backbone diagrams**: two incrementally-built SVGs,
  `pics/academic-clinician.svg` and `pics/academic-participants.svg`,
  driven by their `.svgtune` files and pre-rendered into
  `pics/*_tuned/`. Detour slides follow the diagram step that
  introduces them and bookend back to it.
- **Reusable highlights**:
  - "Two communities, a thin line of correspondence" — clinic (vendor
    hardware, DICOM, PACS/EHR) vs. academia (NWB, BIDS); DICOM WG-32
    (ephys in DICOM) with the lossy-compression *ask*; "manufacturers do
    not really care about academic standards" + *report gotchas to them*.
  - Participants and consent: "Federally regulated but locally
    managed", *plan the archive deposit in the consent form*.
  - NWB block: one format for all modalities, NWB GUIDE ("TurboTax of
    file conversions"), "Life without NWB"; five live Neurosift
    examples (event-related signals, LFP, spectrograms) on DANDI data —
    "cool stuff is possible only because of boring stuff (standards)".
  - Data Archives: DANDI, EMBER, OpenNeuro, NEMAR, one slide each.
  - BIDS: "Why do we need dataset standards?", BEP032 (microelectrode
    ephys), nwb2bids.
  - ReproStim, Pozu, HED (with HEDit), and LSL/QR-code sync slides.
  - DataLad: "DataLad in one figure", "Why version control?", nesting
    → BIDS study layout → all the way to the paper.
  - "Take Home Weekend Entertainment Checklist from CON" (checkbox list).
  - Acknowledgements grid **frozen** as delivered (see the comment in
    the deck); regenerate a fresh one for new decks with
    `tools/mk_whoweare.py`.

### `2026-mcgill-mechababs/slides.html` — *mechababs: STAMPED execution of BIDS Apps at scale*
- **Venue / date**: McGill neuroscience group, 2026-08-11 (20 min + 10 min discussion).
- **Not a reveal.js deck**: marp source `2026-mcgill-mechababs/slides.md`, built to a self-contained `slides.html` via `datalad run` (marp-cli 4.5.0; `datalad rerun` regenerates it). Lives in its own subdirectory, no root `<TALK-ID>.html`. Slide IDs below do not apply.
- **Spine**: Why (so many datasets) / How (STAMPED, DataLad) / What (BABS, mechababs) / flow + provenance / gaps / BIDS Study + BEP 028 / nipoppy comparison.
- **Reusable highlights**: BABS interface + mechababs config-layer split; output-structure and derivative-details slides; provenance-capture slide; BEP 028 "gaps we have already hit" list.

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

### `2026-brainhack-containers-mashup.html` — *Containers: BrainHack 2026 Mashup*
- **Venue / date**: BrainHack 2026, containers session.
- **Spine**: pointer-pack to container-related talks and materials.
- **Reusable highlights**:
  - Title slide (per `SOUL.md` §3).
  - "Containers — talks to mash up" markdown slide with links to:
    fMRIPrep Bootcamp (Geneva 2024) containers day, QLS612 (McGill 2026)
    containers lecture, BioCore CRG Singularity introduction, ReproNim
    containers tutorial.
- Notes: tiny deck (2 slides — title + pointer list); useful as a
  quick-reference card rather than a standalone presentation.

### `2026-nih-bids2.0.html` — *BIDS 2.0: the past, present, and (realistic) future of the Brain Imaging Data Structure*
- **Venue / date**: NIMH Data Science & Sharing Team Lunch & Learn, 2026-06-02.
- **Spine**: BIDS overview → deprecations in 1.x → inconsistencies →
  modularity (study datasets, YODA, STAMPED) → how to get involved.
- **Reusable highlights**:
  - Title slide (per `SOUL.md` §3).
  - Brief Bio + CON principles `r-stack` (borrowed from `2022-nih-compcore.html`).
  - BIDS citation slide (Gorgolewski et al. 2016) + BIDS 10th birthday
    card iframe (`pics/bids-10th-birthday-card.html`).
  - BIDS Features table (modular composition, consistent folder structure,
    expressive naming, standard formats, documented metadata, BIDS-apps,
    PyBIDS/bids2table/snakebids).
  - BIDS timeline SVG (`pics/borrowed/bids-timeline-2024.svg`) from
    Poldrack et al. Imaging Neuroscience (2024).
  - **Deprecations** deep-dive (NEW): field renames, semantic swaps,
    MAY→MUST tightenings, deprecated suffixes screenshot, "drop the
    shims" takeaway.
  - **Inconsistencies** slide (NEW): `participants.tsv`→`subjects.tsv`,
    singular column names, time units, `.json` dual-purpose, path-vs-URI.
  - **Modularity**: BIDS study `DatasetType` (v1.10.1), nipoppy / Princeton /
    YODA layout overlays, OpenNeuroStudies, YODA→STAMPED transition,
    `pics/stamped-principles-webshot_20260602.png`.
  - BIDS 2.0 card iframe (`pics/bids-2.0-card.html`).
  - "How to get involved" pointers (project board, repos, BEP process,
    Zotero bibliography).
- Notes: companion materials in `2026-nih-bids2.0/` (INCF 2024 poster,
  bibliography, deprecation notes, talk plan).

### `2026-bbqs-stamped` — *Guidelines for Reproducible Research* (STAMPED)  *(Google Slides)*
- **Venue / date**: BBQS (BRAIN Behavior Quantification and
  Synchronization) virtual workshop, 2026-03-11.
- **Presenters**: Cody Baker (Yaroslav Halchenko is just a co-author)
- **Format**: Google Slides (not reveal.js). Archived as
  `2026-bbqs-stamped.pptx` (editable) and `2026-bbqs-stamped.pdf`
  (static). Original at
  <https://docs.google.com/presentation/d/1yC412amV-j3BUfZ8Aq0aPEay93mnvmbo833BfNwuI_8/edit?usp=sharing>.
- Notes: companion `2026-bbqs-stamped/README.md` documents the format
  choice.

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

### `202404xx-NSF-POSE-BIDS.pdf` — *The Brain Imaging Data Structure (BIDS): an open community standard for neuroscience*  *(PDF/ODP)*
- **Venue / date**: NSF POSE (Pathways to Enable Open-Source
  Ecosystems), April 2024. Not a reveal.js deck: LibreOffice source
  `202404xx-NSF-POSE-BIDS.odp` + PDF export, both at the repository
  root. Co-credits slides by Ariel Rokem and Rémi Gau.
- **Spine**: what BIDS is (standard + tools + community) → the
  "Researcher A / Researcher B" re-use story → adoption and community,
  threaded through the BIDS ecosystem figure.

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

## Posters

### `2026-usrse/stamped-ai-study/index.html` — *STAMPED in Practice*

- US-RSE 2026 poster comparing research-skill assistance across three rounds.
- [Editable poster, verified PDF and research evidence](2026-usrse/stamped-ai-study/README.md).


Posters are not reveal.js decks and have no slide IDs. HTML posters
live in their venue directory; `tools/create_index.sh` lists them (with
a *poster* tag) on `index.html` from its hand-maintained `LISTED` array —
add new posters there too.

### `2026-usrse/duct-poster.html` — *Agent-friendly Provenance Capture with `con-duct`*
- **Venue / date**: US-RSE'26 poster session, 2026-10. Presenters:
  Austin Macdonald, Cody C. Baker, John A. Lee, Yaroslav O. Halchenko.
- **Format**: editable HTML at 42×36 in; print PDF
  `2026-usrse/duct-poster.pdf` (annexed). Abstract:
  `2026-usrse/duct-poster-abstract.md`; layout notes:
  `2026-usrse/duct-poster-layout.md`; assets under
  `2026-usrse/duct-poster-assets/` (logos, QR codes, the
  fmriprep-on-ds002785 resource plot).
- **Content**: `duct <cmd>` as near-zero-effort provenance (stdout/err,
  process-tree resource sampling, invocation + environment record);
  `con-duct ls` filtering for humans *and* agents; a chat panel of an
  agent reading duct records; comparison table against workflow
  managers / experiment trackers. The agent-usage patterns that
  `2026-reproAI-MIT-STAMPED.html` and `2026-usrse-con-talk.html` point
  to live here.
- *Asset*: `pics/fmriprep-on-1-subject-of-ds002785__ps-cpu-timepoint.svg`.

### `2026-usrse/orinoco-lite_poster.html` — *Beyond the Lab Website: Reusing Structured Research Metadata Across Lab Operations*
- **Venue / date**: US-RSE'26 poster session, 2026-10.
- **Content**: service-based ORINOCO and GitHub-based ORINOCO Lite,
  with actual websites, metadata editing, graph exploration and funder
  reporting.
- **Format**: editable HTML/CSS, with PDF export through
  `2026-usrse/orinoco-lite/build-poster.py`. Sources, licensing and four
  tagged component revisions: `2026-usrse/orinoco-lite/README.md`.
  Draft text: `2026-usrse/orinoco-lite-poster-draft.md`.

### `2025-sfn-poster-data-standards.pdf` — *The Ecosystem of Standards in Neuroscience: Which Ones Are For You?*
- **Venue / date**: SfN 2025; [Zenodo
  10.5281/zenodo.18333008](https://doi.org/10.5281/zenodo.18333008),
  34 authors led by Oliver Ruebel, CC-BY-4.0 (see `REUSE.toml`). PDF and
  JPG at the repository root.
- **Reuse**: the crops `pics/borrowed/2025-sfn-poster-data-standards_preview.jpg`
  and `pics/borrowed/2025-sfn-poster-data-standards--archives.png` —
  the "standards bring them all together" picture used in
  `2026-dhmc-ieeg.html`.

### `posters/crcns-2022-dataland.pdf` — *DataLad: The Ecosystem for Everyone*
- **Venue / date**: CRCNS 2022 (committed 2022-10-26). Halchenko, Hanke,
  Wagner, Poldrack, Heunis, Szczepanik, Wodder, Moench.
- **Format**: Inkscape SVG source + PDF/PNG renderings, all in
  `posters/` (annexed).

### Poster abstracts in preparation (no poster yet)
- `2026-sfn/stamped-poster-abstract.md` — STAMPED poster abstract for SfN 2026.
- `2026-brain-initiative/stamped-poster-abstract.md` — the same STAMPED
  abstract adapted for the BRAIN Initiative Conference 2026.
- `2026-usrse/stamped-abcd-poster-draft.md` — *STAMPED in Practice:
  Reproducing a Scientific Result Using ABCD Neuroimaging Data* (draft).

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
- `2026-brainhack-containers-mashup.html` — pointer-pack to external
  container talks (fMRIPrep Bootcamp, QLS612, BioCore CRG, ReproNim).
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

### Extend / standards work / BIDS BEPs / BIDS 2.0
- `2026-nih-bids2.0.html` — **best BIDS 2.0 walkthrough**: deprecations
  deep-dive, inconsistencies, modularity (study datasets), how to get
  involved. BIDS Features table, timeline SVG, 10th-birthday card.
- `2023-bids-dicom.html` § BIDS features, § BIDS-minder, § DICOMs-in-BIDS
  workflow, § "All standards are bad, but some are used".
- `2026-dhmc-ieeg.html` § clinic vs. academia (DICOM WG-32 for ephys,
  "manufacturers do not care"), § NWB, § BEP032 microelectrode ephys,
  § nwb2bids, § HED — the **ephys-facing** standards story.
- `2025-sfn-poster-data-standards.pdf` (poster) — the neuro* standards
  landscape on one page.
- `2022-nih-compcore.html` § Microscopy-BIDS citation.
- *Asset*: `pics/BIDS-minder.svg`, `pics/bids-logo-wide.png`,
  `pics/bids-yoda.png`, `pics/bep028-example1.png`,
  `pics/borrowed/bids-timeline-2024.svg`,
  `pics/bids-10th-birthday-card.html`, `pics/bids-2.0-card.html`,
  `pics/borrowed/bids-2-devel_issue57-agenda_20260602.png`,
  `pics/bids-2.0-incf2024-webshottop.png`.

### Standardize / data archives / DANDI / OpenNeuro / federation
- `2023-brain-dandi.html` (whole deck) — best DANDI walkthrough.
- `2023-lbl-building-dandi.html` — extended version.
- `2024-distribits-datalad.html` § DANDI alternative-view slide;
  § OpenNeuro infrastructure use.
- `2026-dhmc-ieeg.html` § Data Archives — one slide each for DANDI,
  EMBER, OpenNeuro, NEMAR; plus § consent ("plan the deposit in the
  consent form") and the five Neurosift streaming examples.
- *Asset*: `pics/dandi-slide-{modalities,services,standards,schema}.svg`,
  `pics/DANDI-{ecosystem,FAIR,users-*}.svg`,
  `pics/dandiarchive-webshots.png`, `pics/dandisets-healthstatus.png`.

### YODA principles + "Look up you must not" + STAMPED
- `2026-reproAI-MIT-STAMPED.html` — **best standalone STAMPED
  treatment in reveal.js**: the seven-property table (with an
  agent-affordance column), the STAMPED-vs-FAIR contrast, the
  Actionability-is-load-bearing slide, and the
  checklist/examples/paper sub-site table.
- `2025-distribits-YODA.html` and `2026-repronim-YODA-BIDS-webinar.html`
  — full YODA spine.
- `2026-nih-bids2.0.html` § Modularity → YODA hierarchy with containers
  slide + YODA→STAMPED transition
  (`pics/stamped-principles-webshot_20260602.png`).
- `2026-bbqs-stamped` (PDF/PPTX) — standalone STAMPED presentation.
- *Asset*: `pics/yoda*.{png,svg}`, `pics/principle-{vcs,computeenv,
  structure}.png`, `pics/depends-on-untracked-file.png`,
  `pics/yoda-hierarchy-with-containers.png`,
  `pics/yoda-do-not-look-up.png`, `pics/yoda-all-the-way-down.png`,
  `pics/stamped-principles-webshot_20260602.png`.

### Worked example: a full STAMPED research object (AI-built)
- `2026-reproAI-MIT-STAMPED.html` § Act III, last two slides —
  [`dandi/compression-comparisons-t261-study`](https://github.com/dandi/compression-comparisons-t261-study):
  BIDS-shaped layout + pinned subdatasets + 1216 `[DATALAD RUNCMD]`
  commits, 1095 of them wrapping `duct`. **The single best "all the
  pieces, on a real study" artifact in the corpus** — use it whenever a
  deck needs to show the layers composing rather than describing them.
- *Rerun evidence*: a clean-clone `datalad rerun` of the 0.5 s smoke cell
  reproduced every scientific value bit-for-bit; only timings and the
  environment record moved. Method and caveats in
  `2026-reproAI-MIT-STAMPED/PLAN.md` §4b.
- *Known defect worth citing*: `.gitmodules` `url = ../..` breaks
  `datalad get` for any outside cloner — a live **D**istributable
  failure, one-line fix. Good teaching material for the checklist.

### Companion video playlists / YouTube licensing / ReproTube
- `2026-reproAI-MIT-STAMPED/playlist.md` — the model for a talk-companion
  playlist: ordered video list, **licences verified with `yt-dlp`** (not
  assumed), an explicit mirror-vs-link rule, and the ReproTube archival
  status of each entry. Copy this file as the template for future decks.
- *Rule of thumb established there*: CC-BY → may be mirrored to ReproTube;
  Standard YouTube Licence → playlist link only, never mirrored.
- *Note*: `con/annextube` is channel-oriented and mirrors each channel's
  own playlists; a curated **cross-channel** playlist has no archival
  representation today. Recommended stance: leave it, the playlist is a
  view and every mirrorable video is already archived per-channel.
- *Asset*: <https://datasets.datalad.org/repronim/ReproTube/channels.tsv>

### Provenance / `datalad run` / `datalad rerun` / RUNCMD → BEP028
- `2025-distribits-YODA.html` and `2026-repronim-YODA-BIDS-webinar.html`
  § Principle 1.
- `2022-nih-compcore.html` § Provenance capture (3 code-block slides).
- `2024-distribits-datalad.html` § DataLad crawler gitGraph.
- `2026-usrse/duct-poster.html` (poster) — `con-duct` run records, for
  humans and agents; the place to point for duct usage patterns.

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
- `2026-reproAI-MIT-STAMPED.html` — **the STAMPED↔AI deck**: "without
  structure the agent has to guess" contrast slide, STAMPED-table
  *what-it-buys-an-agent* column, the **"AI changed what counts as
  actionable"** escalation, Agent=Model+Harness anatomy table, the
  **AI-coding-ladder + 5-stage-loop + dev-model** pair (promoted out of
  the appendix and better laid out than the CA Origami original), the
  **SciOps figure**, and the "skills are the new reusable module" argument.
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

### Actionability in the AI era / automations on top of standards
- `2026-reproAI-MIT-STAMPED.html` § Act II — the three-tier escalation
  (*exact command* → *procedure in human language* → *routines that fire
  unasked*) and the two mechanisms it unlocks: **skills** (human
  language carries judgement, scripts carry precision, modularity still
  applies) and **harness-provided routines** (Claude Code on the web
  watching a repo, scheduled agents, CI beyond tests).
- `2026-reproAI-MIT-STAMPED.html` § "So grade *them* too" — the
  recursive claim that **skills and automations are themselves research
  objects that must pass the STAMPED checklist**, which is what makes
  them reusable beyond their author. Reuse this slide in any deck that
  argues for sharing harnesses rather than hoarding prompts.

### AI work-item sizing / verification loops / review burden
- `2026-reproAI-MIT-STAMPED.html` § "Two regimes" + "We are not the only
  ones saying this" — the thesis and its receipts. Use whenever a deck
  needs to argue *why* AI-assisted work must stay small absent a
  self-checking harness, or to push back on "the model is good enough
  now".
- *External evidence worth keeping at hand*:
  [DORA 2025](https://dora.dev/insights/balancing-ai-tensions/);
  [METR RCT 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/);
  [Addy Osmani, *Code Review in the Age of AI*](https://addyo.substack.com/p/code-review-in-the-age-of-ai);
  [Simon Willison, *Your job is to deliver code you have proven to work*](https://simonwillison.net/2025/Dec/18/code-proven-to-work/);
  [Faros/DORA-2025 telemetry](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025).
- *Aphorism*: "less is more" = Robert Browning, *Andrea del Sarto*, 1855
  — **not** Mies van der Rohe (who credited Peter Behrens). Counter:
  Robert Venturi, "less is a bore" (1966).

### Five verbs ↔ SciOps maturity levels
- *Mapping* (Johnson *et al.*, 2024; <https://arxiv.org/abs/2401.00077>):
  - **L1 Initial** — ad-hoc; no CON verb yet.
  - **L2 Managed** — Compose (lab-local; YODA layout).
  - **L3 Defined** — Reuse / Compose / Extend / Standardize; FAIR data + FAIR workflows. *Paper-cited L3 exemplars*: BIDS, NWB, DataLad / git-annex, DANDI, brainlife.io.
  - **L4 Scalable** — Automate; "SciOps pipelines" (semi-automated continuous workflows).
  - **L5 Optimizing** — Automate × AI; closing the discovery loop.
- *Figure*: `pics/borrowed/neuro-sciops-fig.svg` (vector, converted from
  the annexed `pics/borrowed/neuro-sciops.pdf`) — the five-level ladder
  graphic from the preprint itself. **Always credit Johnson et al.
  on-slide**; it is not a CON figure. Used in
  `2026-reproAI-MIT-STAMPED.html` § "That was the individual ladder.
  Here is the team one."
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
- `2026-bbqs-stamped` (PDF/PPTX) — standalone STAMPED presentation
  co-presented with Cody Baker at the BBQS virtual workshop (2026-03-11).
  Not reveal.js; use the Google Slides original or the `.pptx` export for
  remixing.
- Both STAMPED and SciOps now have entries in `SOUL.md` §5 (canonical
  citations), so any future deck can cite them with one-line consistency.

### Schema-driven UIs / "the Model materializes the View"
- `2026-usrse-con-talk.html` § Standardize → "Metadata: schemas as first-class citizens" (LinkML / pydantic / JSON Schema / SHACL bullets) and § MVC mini-section's Views slide (vjsf → DANDI meditor; shacl-vue → forms + research-group websites).
- `_backdrawer_/202x-mvc-stack.html` *(stub)* § Models → "Metadata: many languages, one idea" and § Views → "Schema-driven UIs: the View that the Model generates".
- *External reference*: M. Hanke et al., **LinkML metadata-driven workflow** —
  on ReproTube: <https://datasets.datalad.org/repronim/ReproTube/DataLad/web/#/video/oF98hdaph1k?tab=local&wide=1&t=644&q=model&filter=1>
  (YouTube id `oF98hdaph1k`, timestamp 644s); cite when borrowing or expanding the schema-driven-UI argument.
- *Suggested screenshots to add later*: DANDI meditor at <https://gui.dandiarchive.org/>; a `shacl-vue`-rendered website (per psychoinformatics-de's deployments).

### Agent skills / harnesses as shareable artifacts
- `2026-reproAI-MIT-STAMPED.html` § Act IV — the canonical treatment:
  harness-anatomy table (`AGENTS.md` / skills / hooks / MCP / sandbox
  ↔ STAMPED properties), the upstream-contribution table, and the
  `con/skills` listing.
- `2026-ca-origami-retreat-aicoding.html` § "Reusable Skills: con/skills"
  — the workflow-level view (compound engineering stage 5).
- *External*: [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills)
  (177 skills, Agent Skills spec, MIT) — CON authored `skills/bids`
  ([PR #125](https://github.com/K-Dense-AI/scientific-agent-skills/pull/125))
  and reviewed `skills/datalad`
  ([PR #227](https://github.com/K-Dense-AI/scientific-agent-skills/pull/227));
  STAMPED→DataLad command mapping is
  [PR #265](https://github.com/K-Dense-AI/scientific-agent-skills/pull/265).
  The open design question — *where should domain skills live?* — is
  [issue #217](https://github.com/K-Dense-AI/scientific-agent-skills/issues/217).
- *External*: [Oscar Esteban, OHBM 2026 AI
  Educational](https://www.nipreps.org/presentations/2026-OHBM-AI-Educational/)
  — "Agent = Model + Harness", `AGENTS.md` as the operational contract,
  grounding-beats-search experiment. Credit it when borrowing.

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

## Repo-level tooling (`tools/`)

Reach for these before writing anything per-talk:

| Tool                         | What it does                                                                                                                                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tools/mkqrcode.py`          | QR-code generation (PNG or SVG), with optional embedded logo and a decode-back verification pass                                                                                                                           |
| `tools/mkqrcode_con`         | Thin wrapper: `mkqrcode.py` with the CON logo and `-c H` error correction — **the branded variant**                                                                                                                        |
| `tools/qrcode_url.sh`        | URL → QR shortcut                                                                                                                                                                                                          |
| `tools/mkpdf.py`             | Headless reveal.js → PDF for **any** deck (Playwright; page size from each deck's own reveal config). Third option next to `README.md`'s manual `?print-pdf` and decktape-in-Docker routes. Derived PDFs are not committed |
| `tools/create_index.sh`      | Regenerates `index.html`: root `20*.html`/`20*.pdf` by year, plus posters and other hand-titled entries from its `LISTED` array                                                                                            |
| `tools/mk_whoweare.py`       | Acknowledgements fragment with all faces from the CON website's who-we-are page (`con-whoweare.phtml`)                                                                                                                     |
| `tools/mk_ack_eras.py`       | Per-era acknowledgements iframes (`2026-usrse-con-talk/ack-*.html`) from the `sourcedata/con-site-specific` record store                                                                                                   |
| `tools/mk_stamped_puzzle.py` | Draws `pics/stamped-puzzle.svg`: the STAMPED object as a jigsaw, one piece per tool                                                                                                                                        |
| `tools/build_preview.py`     | Minimal static site with only the given decks and the files they reference (used by `.github/workflows/preview.yml` PR previews)                                                                                           |
| `tools/copy_pics.sh`         | Picture copying helper                                                                                                                                                                                                     |
| `tools/get_pdf_page_to_png`  | Extract one PDF page as a trimmed, transparent PNG (needs `pdftk`/`pdftoppm`/`convert`)                                                                                                                                    |

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
