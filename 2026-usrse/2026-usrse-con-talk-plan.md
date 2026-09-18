# Talk Plan: Reuse, Compose, Extend, Standardize, Automate
## US-RSE 2026 — 15-minute slot — "AI Assisted Code Development" session
## Monday Oct 19, first session after Plenary

---

## Core identity

**Through-line:** *"AI just arrived. It tends to produce silos. The RSE immune response has a name.
We've been building it for 20 years."*

**Home message:** "Together we can make neuroscience a better science" — earned, not announced.
The five verbs are the *mechanism*, not the slogan.

**Anchor words:** REUSE / COMPOSE / EXTEND / STANDARDIZE / AUTOMATE
Each introduced with a full-bleed word slide, each revisited at its AI failure mode, all five
reunited in Act III.

**Target:** ~93 slides at 6-8/min average = 15 min.
Current deck has 39 slides (several severely overloaded → would run 25+ min).
Lessig move: cut content, add ~60 single-concept transition/beat slides.

---

## Lessig-Method Style Rules (quick reference)

- One idea per slide, always. If you write a second sentence, split the slide.
- Voice ≠ slide text. Slide = anchor word/image; voice = meaning.
- Fast bursts (12-20 slides/min) for timelines and accumulation.
- Hold slides (6-12 s, stop talking) to land key points.
- Every anchor-word appearance must be visually identical (same font, position, weight).
- Do NOT front-load a roadmap. Use rapid burst to flash the five words, then prove each.
- White-on-black = contrast / problem / historical framing.
- One light moment per block max; deliver and immediately move on.
- Target 40-50% image-only slides.

---

## Three-Act Structure

---

### ACT I — The Problem and the Framework (2.5 min, ~18 slides)

**Goal:** establish that AI = silo pressure; the antidote = five verbs; we have 20 years of evidence.

| # | Slide content | Type | Time |
| - | ------------- | ---- | ---- |
| 1 | Title (CON letterhead, QR, logo strip) | Hold | 15 s |
| 2 | "It's 2026. AI writes code." | White-on-black | 5 s |
| 3 | "AI tends to produce silos." | White-on-black | 8 s |
| 4 | Codeberg/Forgejo: "Protecting our FLOSS commons from LLMs" — logo + quote fragment | Image | 5 s |
| 5 | "The antidote has a name." | Transition | 5 s |
| 6-10 | REUSE / COMPOSE / EXTEND / STANDARDIZE / AUTOMATE | **Rapid burst, 1.5 s each** | 8 s |
| 11 | "We've been building this immune system for 20 years." | Hold | 8 s |
| 12 | "It started as an accident." | Transition | 5 s |
| 13 | "2000. A neuroscience grad student joins a Debian developer's lab." | White-on-black | 8 s |
| 14 | [Fernando Perez callback] "Fernando Perez was building IPython in the same community. Same instinct: reuse the ecosystem, not just the code." | 1 slide | 12 s |
| 15-21 | Timeline burst: 2000 / 2005 / 2007 / 2009 / 2013 / 2016 / 2024 — one milestone per slide | **Burst, 2 s each** | 14 s |
| 22 | "Seven milestones. Five verbs. Two decades." | Land | 8 s |

**Fernando Perez placement (slide 14):** one sentence, callback to morning plenary; signals the
talk is in connected intellectual territory without becoming a detour. Move on immediately.

---

### ACT II — The Five Verbs, Proven (8 min, ~55 slides)

Each verb follows the same Lessig ritual:
**WORD** → rule → historical proof burst → current exemplar → AI failure mode → **WORD** (callback)

---

#### REUSE (~2.5 min, 17 slides)

| Slide | Content | Type |
| ----- | ------- | ---- |
| REUSE | Full-bleed word, hold 3 s | Anchor |
| "The cheapest reproducible thing is the one you didn't have to build." | Rule | Land |
| NeuroDebian logo | Historical | 2 s |
| "Born by joining Debian. Not forking it." | Beat | 5 s |
| PyMVPA logo | Historical | 2 s |
| "2007. Full test suite. CI. Tutorials. Before it was common." | Beat | 8 s |
| logos burst: duecredit / con/duct / citations-collector | Current exemplars | 6 s |
| "One upstream search pass saves a thousand local fixes." | Land | 8 s |
| **[REUSE/SPDX beat]** | | |
| REUSE logo + "Debian DEP-5 → REUSE spec: machine-readable licensing and copyright, per file." | One slide | 8 s |
| "`/introduce-reuse-compliance` — we reuse the standard and automate its adoption." | One slide (link to github.com/con/skills) | 8 s |
| "What if AI attribution worked the same way?" | White-on-black, transition | 6 s |
| `SPDX-FileContributor: assisted-by-ai: Claude Code 2.1 / Claude Sonnet 4.6` | Code slide, hold | 10 s |
| "File-level AI provenance that survives redistribution. We filed the issue." | Beat (fsfe/reuse-website#127) | 8 s |
| **[TODO: % AI commits graphic]** — see note below | Placeholder | — |
| "Agents don't search. They generate." | White-on-black AI beat | 8 s |
| "Reuse requires asking 'does this exist?' before the first keystroke." | Hold | 8 s |
| REUSE | Callback, 1.5 s | Anchor |

**Notes on REUSE/SPDX beat:**
- The REUSE spec (reuse.software) is Debian DEP-5 inspired — fits the talk's lineage perfectly.
- `/introduce-reuse-compliance` (github.com/con/skills) is a Lessig-style proof point: we don't
  just adopt standards, we automate their adoption. Bridges to AUTOMATE without spelling it out.
- The SPDX AI provenance proposal (fsfe/reuse-website#127) is the forward-looking moment: the
  same Reuse-the-standard discipline applied to the open problem of AI attribution at the
  artifact level (survives git history loss; machine-readable; same SPDX grammar). It also
  previews the STANDARDIZE section's "shared grammar for HI and AI" argument. One slide showing
  the actual proposed header syntax (`SPDX-FileContributor: assisted-by-ai: ...`) makes it
  concrete without requiring explanation.

**TODO — % AI commits graphic:**
Generate a visualization of the git log showing what fraction of commits (by time or count)
carry a `Co-Authored-By: Claude Code` trailer. A stacked area or bar chart over time — showing
the progression from 0% to current — would be a striking one-slide visual for the talk: CON
walks the walk on transparent AI attribution. Suggested approach:
```bash
git log --format="%ad %s" --date=short | ...  # annotate lines with Co-Authored-By presence
```
Could also show the split between `assisted-by-ai` (Claude co-authored) vs. `generated-by-ai`
(fully agent-driven) once the SPDX convention is adopted. This slide would land in the REUSE
section just before or just after the SPDX beat.

*Cut from current deck:* "Today we'd contribute upstream" (S4.5) — collapse to logos burst above.
*Cut:* "Reuse-in-reverse" section (S9) — fold into REUSE or drop for time.

---

#### COMPOSE (~1.5 min, 10 slides)

| Slide | Content | Type |
| ----- | ------- | ---- |
| COMPOSE | Anchor, hold 3 s | |
| "Sandwich, don't silo." | Rule | |
| DataLad sandwich mermaid | Diagram, hold 15 s | |
| DataLad extensions graph mermaid | Diagram, hold 10 s | |
| registry.datalad.org screenshot | "Federate, don't recentralize." | 10 s |
| "AI generates glue. Nobody owns the glue." | White-on-black AI beat | 8 s |
| "Deliberate interfaces outlast generated adapters." | Hold | 8 s |
| COMPOSE | Callback, 1.5 s | |

*Cut from current deck:* "Small acquisition & compute units" table (S5.5) — too long; con/duct
appears already in REUSE logos burst.

---

#### EXTEND (~1.5 min, 10 slides)

| Slide | Content | Type |
| ----- | ------- | ---- |
| EXTEND | Anchor, hold 3 s | |
| "Ship pragmatic now. Formalize upstream later." | Rule | |
| RUNCMD → BEP028 → BIDS standard mermaid | Diagram, hold 15 s | |
| Logos burst: Debian/Med / BIDS Steering / NWB+Kitware | 3 slides, 3 s each | |
| "AI extends by adding. It rarely stays to maintain." | White-on-black AI beat | |
| "Staying on as maintainer is the non-automatable contribution." | Hold | |
| EXTEND | Callback, 1.5 s | |

---

#### STANDARDIZE (~2.5 min, 18 slides)

This is the conceptual heart of the talk. Introduce MVC here as the *why* that makes all the
prior Reuse and Compose choices pay off. The general argument comes first — standards are the
shared grammar that makes AI work governable and composable — then ORINOCO-Lite as one worked
example of that argument in practice.

**Ordering principle:** general → specific. The audience must grasp "standards = AI's framing
layer" before they hear about ORINOCO-Lite; otherwise ORINOCO-Lite looks like a niche metadata
project rather than an instance of a broadly applicable pattern.

| Slide | Content | Type |
| ----- | ------- | ---- |
| STANDARDIZE | Anchor, hold 3 s | |
| "All standards are bad. Some are used." — Clunie, MICCAI 2017 | Rule + humor, hold 5 s | |
| BIDS-minder SVG | Diagram | 15 s |
| "You've seen one BIDS dataset, you've seen them all." | Land | 8 s |
| NWB logo + one-liner | 3 s | |
| **MVC slide** — "Standards as Model. Reuse+Compose follow." | Hold 20 s — the architectural insight |
|   M = LinkML/BIDS/NWB schemas — machine-readable, deterministically validatable, FAIR-enabling | sub-beat | |
|   C = the ecosystem of tools that operate on M (BIDS-Apps, DataLad, HeuDiConv…) | sub-beat | |
|   V = lab website, reports, discovery — use-case-specific views | sub-beat | |
| "Same M → endless C and V. This is why standards compound." | Land | |
| **[AI general beat — BEFORE ORINOCO-Lite]** | | |
| "Without standards, AI produces cacophony at scale." | White-on-black AI beat | 8 s |
| "Standards are the framing and validation layer for any AI endeavor." | Hold | 10 s |
| "STAMPED encodes what makes a research object reproducible — for HI and AI alike." | STAMPED webshot (`stamped-principles-webshot_20260602.png`) | 10 s |
| **ORINOCO-Lite — one instance of the pattern** | Transition | 5 s |
| LinkML logo + "LinkML — schemas that compose. Built 2 hours north, at LBNL." | Geographic hook | 8 s |
| ORCID / ROR / DOI / PROV-O logos burst | "Reused identifiers — not invented" | 6 s |
| ORINOCO → ORINOCO-Lite flow: INM-7 Jülich → CON, GitHub-native | Diagram or 2 slides | 10 s |
| "AI drafts candidate records. Schema validates. Humans curate via PR." | Land — HI+AI with standards doing the work | Hold 10 s |
| **[Poster call-out]** "Posters: ORINOCO-Lite · STAMPED · con/duct. Come find us." | 1 slide, light tone | 10 s |
| STANDARDIZE | Callback, 1.5 s | |

**Notes on MVC placement:**
- MVC belongs here, inside STANDARDIZE, not as a standalone section at the end.
- The three sub-beats (M/C/V) can each be a full-bleed slide with one large letter and one
  example (M = BIDS, C = HeuDiConv, V = lab website) — Lessig-style one-idea-per-slide.
- The MVC insight *retroactively justifies* the Reuse and Compose sections: once there is a
  shared M, Reuse and Compose are not just good hygiene — they become architecturally necessary.

**Notes on ORINOCO-Lite:**
- Frame as CON reusing ORINOCO (Michael Hanke / INM-7 Jülich) and composing with GitHub
  Actions/Pages — a live instance of the general Reuse+Compose+Standardize pattern.
- The ORINOCO-Lite AI beat is *one specific instance* of the general claim made two slides
  earlier ("standards are the framing/validation layer"): here the schema validates AI-generated
  metadata records before they enter the curated pool. The schema is doing the work; ORINOCO-Lite
  demonstrates it concretely.
- The LinkML geographic detail (LBNL, 2 h north of San Jose) is a light moment; one aside only.
- Do NOT frame ORINOCO-Lite as "the HI+AI model" — frame it as "here is what it looks like
  when you apply the general pattern to lab knowledge management."

*Cut from current deck:* the "Metadata: schemas as first-class citizens" overloaded table (S7.4)
— the MVC slide + ORINOCO-Lite replaces this more concisely.
*Cut from current deck:* "Federated archives, built on the standards" 4-row dense table (S8.1)
— replaced by the Act III logo burst.
*Keep from current deck:* DANDI modalities SVG (S8.2) and DANDI ecosystem SVG (S8.3) — move
these into Act III's evidence burst or cut entirely (DANDI appears via logo anyway).

---

#### AUTOMATE (~2 min, 14 slides)

Two distinct AI beats here: (1) testing as the review layer that scales with agent output;
(2) provenance — con/duct, con/tinuous, and `datalad run` as the tools that track *what the
agent actually did*, making AI-assisted work reproducible and auditable, not just fast.

| Slide | Content | Type |
| ----- | ------- | ---- |
| AUTOMATE | Anchor, hold 3 s | |
| "If a human has to remember it, it's already broken." | Rule | |
| Burst: con/tinuous archives / daily git-annex / auto-rebuilt containers / auto-mirrored dandisets | 4 slides, 2 s each | |
| **"The tests don't know the code was AI-generated."** | Land — RSE take-home line 1 | Hold 10 s |
| "Agent-rate output demands agent-rate review." | White-on-black AI beat | |
| **[Provenance beat — con/duct + con/tinuous + datalad run]** | | |
| "con/duct watches every process. AI agents included." | White-on-black | 6 s |
| con/duct screenshot (`pics/webshot-con-duct.png`) | "Wall time. CPU. Memory. Per task. Per agent." | 8 s |
| "con/tinuous archives every run. AI-assisted runs included." | Beat | 6 s |
| "`datalad run` records every transformation. Agent-written or hand-written." | Beat | 6 s |
| **"Provenance doesn't care who wrote the code."** | Land — RSE take-home line 2 | Hold 10 s |
| con/skills + con/yolo (one slide) | "We also automate the harness. AI assists the harness." | 10 s |
| "AI is expensive. Shared harnesses — and shared logs — amortize the cost." | Hold | |
| AUTOMATE | Callback, 1.5 s | |

**Why con/duct + con/tinuous + `datalad run` belong here (not just as tool names):**
- con/duct: monitors resource usage of any process — including agentic AI runs. When AI is
  expensive (tokens, GPU, wall time), con/duct makes the cost visible and comparable across runs.
  This is "we use this daily with AI" made concrete.
- con/tinuous: archives CI logs including runs of AI-generated or AI-assisted code. The archive
  is the audit trail. If an agent introduced a regression, the log is there.
- `datalad run`: records provenance of every computation, whether the script was hand-crafted or
  agent-generated. The abstraction holds regardless of who (or what) produced the code.
Together these form a **pragmatic provenance stack** that works with or without AI but becomes
load-bearing when AI is in the loop — because you need to know what the agent actually did.

*Cut from current deck:* "Where we automate" 7-row table (S10.2) — replace with 4-slide burst.
*Cut from current deck:* "Five verbs climb the SciOps ladder" table (S10.4) — drop from talk;
mention SciOps verbally if time allows.

---

### ACT III — The Synthesis (3.5 min, ~27 slides)

**Goal:** reunite the five verbs, make the collaboration argument visceral (people, not diagrams),
point to formalizations others are building, land the home message.

| # | Slide | Type | Time |
| - | ----- | ---- | ---- |
| 1 | REUSE / COMPOSE / EXTEND / STANDARDIZE / AUTOMATE — all five, one slide | Hold 6 s | Reunion |
| 2 | "These are not 20-year-old advice." | White-on-black | 6 s |
| 3 | "They are the load-bearing structure for the age of AI." | Hold | 10 s |
| 4 | "AI makes going alone tempting." | White-on-black | 5 s |
| 5 | "Fast. Flexible. Free of dependencies." | Beat, hold 4 s | |
| 6 | **"You are alone."** | White-on-black, large, hold 8 s — emotional pivot | |
| **[Community photos burst — the emotional counter-argument]** | | |
| 7 | Photo: Yaroslav alone, early 2000s | 3 s — "It starts here" |
| 8 | Photo: Yaroslav + Michael Hanke / first collaborators | 3 s |
| 9 | Photo: small group — NeuroDebian / early BIDS meeting | 3 s |
| 10 | Photo: larger community — DebConf / distribits / OHBM open science | 3 s |
| 11 | Photo: biggest community moment available | 3 s |
| 12 | **"Together."** | White-on-black, hold 6 s — callback; earns the closer | |
| 13 | "A hundred agentic projects reinventing the same infrastructure…" | Build | 5 s |
| 14 | "…is a hundred times the debt." | White-on-black, hold 8 s | |
| 15 | "One collaborative ecosystem." | Transition | 5 s |
| 16-21 | Logo burst: DANDI / BIDS / DataLad / OpenNeuro / NWB / EMBER | 2 s each = 12 s | Evidence |
| 22 | HI↔AI policy spectrum (4-stance table: Reject / Disclose / Spec-driven / Autonomous) | Hold 20 s — only complex slide in Act III | |
| **[Networked Intelligence — others formalizing the same intuition]** | | |
| 23 | "Others are formalizing this too." | Transition | 5 s |
| 24 | Paper: "Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science" — title + arXiv:2607.13220 | 1 slide, hold 8 s | |
| 25 | **"Scale the connections, not just the agents."** | Land — paraphrase of paper's core claim | Hold 8 s |
| 26 | "The principles don't change. The urgency does." | Land | 10 s |
| 27 | "Together we can make neuroscience a better science." + Yoda SVG | Hold 8 s | Closer |
| 28 | QR + slides URL + "Thank you!" | Hold | |

**Notes on community photos (slides 7–11):**
- The sequence is the argument: collaboration is not a diagram, it is people. Show the actual
  people. The arc from "alone" (slide 6) through the photos to "Together." (slide 12) is the
  emotional center of the talk — more persuasive than any logo burst.
- Photo sourcing: DebConf group photos (Debian community), BIDS inaugural meeting or steering
  committee, distribits group photo, OHBM open science room crowd, or ReproNim workshop.
  All should be candid/real, not posed stock photos.
- The photos need no captions or speaker narration — just land them in silence or near-silence.
  Let the faces do the work. Hold each 2-3 s and move on.
- The progression (1 person → 2 people → ~10 people → ~50 people → hundreds) mirrors the talk's
  entire argument: Reuse scales through people, not code.
- **TODO:** identify 4-5 specific photos (file paths or sources) to use here. May need permission
  check for conference/group photos.

**Notes on Networked Intelligence paper (slides 23–25):**
- arXiv:2607.13220 — "Networked Intelligence: Active Shared Context Graphs for Human-AI Team
  Science." Proposes Mycelium: an active shared workspace routing findings across human+AI teams.
- The paper's core claim: "Scale the connections, not just the agents." This is the academic
  formalization of what CON has been practicing for 20 years — and what the five verbs enable.
- Frame it as convergence, not citation: "Others are now formalizing the intuition we've been
  building infrastructure for." This positions CON as ahead of the curve without claiming priority.
- One slide for the title/authors/arXiv ID; one slide for the single key phrase. Do not
  summarize the paper. The phrase is enough.

**Monday checklist:** spoken aside on slide 27 or 28 — no separate section.
"Your Monday: one upstream search. One `datalad run`. One CI job."

*Cut from current deck:* standalone "Monday Checklist" section (S13) — carried as spoken aside.
*Cut from current deck:* standalone MVC section (S12) — folded into STANDARDIZE above.

---

## Summary of Changes to Current Deck

| Current state | Action | Reason |
| ------------- | ------ | ------ |
| MVC section (S12, 3 slides) after checklist | **Move into STANDARDIZE** — 3-4 single-idea slides | Architecturally belongs there; arrives too late at current position |
| "Federated archives" dense table (S8.1) | **Replace** with Act III logo burst | Table is undeliverable Lessig-style; burst is more powerful |
| "Reuse-in-reverse" section (S9) | **Cut or fold** last bullet into REUSE | Orphaned; can't afford 2 slides on this in 15 min |
| "HI↔AI policy table" (S11.3) — 70 s overload | **Move to Act III** hold 20 s, let audience read | Best original slide; deserves synthesis position |
| "Five verbs climb SciOps ladder" table (S10.4) | **Cut** from talk body | Valuable but too dense; verbal mention in AUTOMATE AI beat |
| Timeline slide (S3.2) — 9 bullets, ~50 s | **Replace** with Act I burst (7 slides, 2 s each) | One milestone = one slide |
| AI section as standalone chapter (S11) | **Dissolve** into each verb's own AI beat | Woven AI is structurally stronger than appended chapter |
| "Where we automate" 7-row table (S10.2) | **Replace** with 4-slide burst | Undeliverable at Lessig pace |
| "Metadata: schemas" overloaded table (S7.4) | **Replace** with MVC slides + ORINOCO-Lite | More concrete, more Lessig-friendly |

---

## New Slides Needed (not in current corpus)

All are single-concept; most are text-only or one-logo. No new images required except ORINOCO-Lite.

1. "It's 2026. AI writes code." (white-on-black)
2. "AI tends to produce silos." (white-on-black)
3. Codeberg/Forgejo logo + quote fragment
4. "The antidote has a name." (transition)
5. Fernando Perez callback sentence (Act I)
6. Timeline burst: 7 individual milestone slides (replacing the one dense slide)
7. Per-verb AI failure mode slides (white-on-black): REUSE / COMPOSE / EXTEND / STANDARDIZE / AUTOMATE — 5 slides
7b. REUSE/SPDX beat: REUSE logo slide; `/introduce-reuse-compliance` slide; "What if AI attribution worked the same way?" transition; `SPDX-FileContributor: assisted-by-ai:` code slide; "We filed the issue" beat — 5 slides
7c. **TODO:** % AI commits over time graphic (1 slide — needs git log analysis; see REUSE section note)
8. MVC: M/C/V as 3 individual Lessig slides (one letter + one example each)
9. "Same M → endless C and V. This is why standards compound." (land)
10. ORINOCO-Lite pivot + LinkML logo + "2 hours north, at LBNL" (1-2 slides)
11. ORCID/ROR/DOI/PROV-O logos burst (4 slides, 2 s each)
12. ORINOCO → ORINOCO-Lite flow (1-2 slides)
13. "AI generates candidate records. Humans curate via PR." (land)
14. Poster call-out: "ORINOCO-Lite · STAMPED · con/duct — come find us." (1 slide, light)
15. "Fast. Flexible. Free of dependencies." (collapsed from 3 to 1, Act III build)
16. "You are alone." (white-on-black, Act III pivot)
17. Community photos burst — 4-5 slides (Act III emotional counter-argument); **TODO: source photos**
18. "Together." (white-on-black callback, Act III)
19. "One collaborative ecosystem." (transition)
20. Five-word reunion slide (all five verbs, Act III)
21. "These are not 20-year-old advice." (white-on-black)
22. "Others are formalizing this too." (transition, Act III)
23. Networked Intelligence paper title slide (arXiv:2607.13220)
24. "Scale the connections, not just the agents." (land, Act III)

**Total new slides: ~30.** Combined with trimmed existing slides → target ~100 total.

**Outstanding TODOs before slides can be finalized:**
- [ ] Source 4-5 community photos (DebConf, BIDS meeting, distribits, OHBM) — check permissions
- [ ] Generate % AI commits over time graphic from `git log` (see REUSE section note)
- [ ] Confirm which REUSE/SPDX header syntax to show (`SPDX-FileContributor: assisted-by-ai:`)
- [ ] QR code for talk URL (currently placeholder in title slide)

---

## Anchor Phrase Placement

| Phrase | Where | How |
| ------ | ----- | --- |
| REUSE/COMPOSE/EXTEND/STANDARDIZE/AUTOMATE | Act I burst + each section opener/callback + Act III reunion | Identical template every appearance |
| "The cheapest reproducible thing is the one you didn't have to build." | REUSE rule slide | Land |
| "Sandwich, don't silo." | COMPOSE rule slide | Land |
| "All standards are bad. Some are used." | STANDARDIZE — Clunie quote | Light moment, hold 5 s |
| "Same M → endless C and V." | MVC synthesis slide | Land |
| "Standards are the framing and validation layer for any AI endeavor." | STANDARDIZE AI beat (general) | Hold — the architectural claim |
| "AI drafts candidate records. Schema validates. Humans curate via PR." | STANDARDIZE/ORINOCO-Lite | Land — standards doing the work in practice |
| **"The tests don't know the code was AI-generated."** | AUTOMATE land slide 1 | Hold 10 s — RSE take-home |
| "Agent-rate output demands agent-rate review." | AUTOMATE AI beat | White-on-black |
| **"Provenance doesn't care who wrote the code."** | AUTOMATE land slide 2 | Hold 10 s — the reproducibility claim |
| **"You are alone."** | Act III pivot | White-on-black, long hold — emotional center |
| "Together we can make neuroscience a better science." | Closing slide only | Earned by the argument; not announced |

---

## Asset Sources (per-verb)

| Verb | Primary source slides |
| ---- | --------------------- |
| REUSE | `2022-nih-compcore.html` NeuroDebian + PyMVPA; `pics/neurodebian_logo_web_banner.png`; `pics/pymvpa_logo_fromfusionposter.svg` |
| COMPOSE | `2024-distribits-datalad.html` DataLad sandwich + extensions mermaid; `pics/datalad-registry-stats-20251021.png` |
| EXTEND | `2026-usrse-con-talk.html` S6.3 RUNCMD→BEP028 mermaid (keep); S6.2 logos (condense) |
| STANDARDIZE | `pics/BIDS-minder.svg`; `2023-bids-dicom.html` "all standards are bad"; `pics/stamped-principles-webshot_20260602.png`; new ORINOCO-Lite slides |
| AUTOMATE | `2024-distribits-datalad.html` CI screenshots; `2026-ca-origami-retreat-aicoding.html` con/skills+con/yolo |
| AI beats | `2026-ca-origami-retreat-aicoding.html` HI↔AI policy table (move to Act III) |

---

## Notes for Delivery

- **Session context:** first talk after the Plenary (Fernando Perez / Jupyter). The room will
  be full and fresh. Anchor to the morning talk in Act I slide 14 — one sentence, then move.
- **Spectrum of AI attitudes:** the audience contains AI skeptics and enthusiasts. Slide 4
  (Codeberg framing) validates the skeptics without alienating the enthusiasts. The through-line
  ("the antidote has a name") is neutral on AI enthusiasm level.
- **STAMPED, ORINOCO-Lite, con/duct posters:** announced once in STANDARDIZE (slide "Poster
  call-out"), not mentioned again. Light, warm, specific. con/duct also appears substantively
  in AUTOMATE's provenance beat — the poster call-out is not its only mention.
- **con/duct + con/tinuous + `datalad run` as daily AI tools:** the provenance beat in AUTOMATE
  is the talk's most concrete "we actually use this with AI, today" moment. Don't bury it. The
  two land slides ("tests don't know" and "provenance doesn't care") carry equal weight.
- **Humor moments:** (a) "Born by joining Debian. Not forking it." — dry, accurate, RSEs get it;
  (b) "All standards are bad. Some are used." — Clunie attribution is the joke; (c) "LinkML —
  built 2 hours north, at LBNL." — local color; (d) "You are alone." — the long pause IS the
  joke, don't add words.
- **Closing:** say the closing line slowly. Stop. Let the Yoda SVG sit. Do not move to the
  thank-you slide until the line has landed.
