# PLAN — `2026-reproAI-MIT-STAMPED.html`

**Venue**: [*Neuroimaging, Reproducibility and LLMs: Early promises and
future question*](https://www.eventbrite.com/e/neuroimaging-reproducibility-and-llms-early-promises-and-future-question-tickets-1999618019324)
— a ReproNim workshop, MIT Building 46, 43 Vassar Street, Cambridge MA —
**Friday, 2026-10-16**, 09:30–13:00
**Slot**: 11:10–11:40, 25 min talk + 5 min Q&A (first after the coffee break)
**Title**: *STAMPED principles and their role in the age of AI-driven
scientific software development*
(Dave's original framing — "STAMPED and how coding is transformed and
the new scientific framework for code/software development" — kept as
the speaker-note gloss, not on the slide.)

**Live URL / QR**:
`https://datasets.datalad.org/centerforopenneuroscience/talks/2026-reproAI-MIT-STAMPED.html`
→ `pics/2026-reproAI-MIT-STAMPED-qrcode.png` (generated at authoring time)

---

## 1. Thesis

> Agents do not fail for lack of intelligence. They fail for lack of
> **structure to act on**. The same properties that made a research
> object reusable by a human — STAMPED — are what make it *actionable*
> by an agent. And the next thing we owe the commons is not more code:
> it is **shared harnesses and skills** that encode how to act on
> standardized objects.

Three claims, in order:

1. **What changed**: the bottleneck moved from *writing* code to
   *verifying and situating* it. Agent-rate output demands agent-rate
   review — which only provenance and standards can supply.
2. **What did not change**: STAMPED (and YODA before it) already named
   the properties. **Actionability** is the load-bearing one for agents,
   and **standards are what make Actionability cheap** — they are the
   scaffolding *and* the shared vocabulary across HI ⇄ AI.
3. **What is next**: harnesses and skills become first-class, shareable,
   *modular* research artifacts. We are already contributing them
   (BIDS + DataLad skills upstream); the field should treat this as
   infrastructure work, not as prompt-hoarding.

## 2. Arc

Hybrid of `SOUL.md` §7 arc 2 (Challenges → Solutions → Take-home) with
the AI-ladder flavor of arc 5. Parent decks for layout/slide theft:

| Parent | What is borrowed |
| ----------------------------------------- | -------------------------------------------------------------------------- |
| `2026-repronim-YODA-BIDS-webinar.html`    | Title-slide shape, `datalad run`/`rerun` record, `con/duct` slides, "Look up you must not", YODA-beyond-code-and-data |
| `2025-distribits-YODA.html`               | Same YODA spine (grandparent)                                              |
| `2026-ca-origami-retreat-aicoding.html`   | Reality-Check GIF, AI-coding ladder (→ appendix), `con/skills` table, Thank-you closer |
| `2026-usrse-con-talk.html`                | HI ⇄ AI policy table, "provenance doesn't care who wrote the code" beat, Acknowledgements |
| `2026-nih-bids2.0.html`                   | YODA → STAMPED transition, `stamped-principles-webshot_20260602.png`       |
| `2024-distribits-datalad.html`            | Canonical Acknowledgements layout                                          |

**External credit (explicit, on-slide):**
[Oscar Esteban, *Using LLMs in Neuroimaging Research: LLMs for Coding*,
OHBM 2026 Educational](https://www.nipreps.org/presentations/2026-OHBM-AI-Educational/)
— the "Agent = Model + Harness" formulation, `AGENTS.md` as the
operational contract, and the grounding-beats-search result. This talk
deliberately picks up *where Oscar's leaves off*: he showed how to build
the harness; this one argues about **what the harness stands on** and
**how harnesses themselves get shared**.

## 3. Slide-by-slide (34 main slides + 7-slide appendix, for 25 min)

### Act 0 — Frame (≈2 min)

1. **Title slide** — standard `SOUL.md` §3 template, QR, logo strip.
2. **Reality Check** — `idiocracy-fixed.gif` disclaimer.
   *(borrowed: aicoding deck §Reality Check)*
3. **Previously on… / standing on two talks** — ReproNim YODA webinar
   (mine) + Oscar's OHBM AI Educational (his). States the hand-off.

### Act I — What actually changed (≈4 min)

4. **"It's 2026. Agents write the code."** — black beat slide.
5. **The bottleneck moved** — writing → verifying + situating.
   `2026-ai-intensifies.png` (HBR) as the visual.
6. **Without structure, agents go wild** — the central claim slide.
   Left column: what an agent sees in an ad-hoc `~/data/study_final2/`.
   Right column: what it sees in a BIDS dataset. Same model, different
   affordances.
7. **This has a name** — YODA (2018) → STAMPED (2026).
   `pics/stamped-yoda.svg` / `pics/yoda-principles-reordered.png`.

### Act II — STAMPED, and what AI did to Actionability (≈7 min)

7b. **Section opener** — the STAMPED banner
    (`pics/borrowed/stamped-banner_ver-3.svg`, the project's own artwork:
    the seven words with their icons) replacing the former text-only
    opener, with the "whoever, *or whatever*, picks it up next" line as a
    fragment underneath.
8. **STAMPED in one table** — all seven, one line each, from
   <https://stamped-principles.org/>. Third column: *what it buys an
   agent*. Paper + preprint DOI cited.
9. **Actionability is the one that agents live or die on** — and
   standards are what make it cheap. "You've seen one BIDS dataset…"
   lands twice as hard for a model that would otherwise *infer*.
10. **…and AI changed what counts as actionable** (NEW — the slide the
    talk now pivots on). A three-row escalation:
    - *Before*: an exact command / API / documented CLI. Tools and
      humans-who-already-knew could act; everything else stayed a
      paragraph in the Methods.
    - *Now*: a procedure **described in human language**, with scripts
      dropped in where precision matters → **any agent, on first
      contact**. The interface moved from *syntax* to *language*.
    - *Next*: routines that fire **without being asked** → the
      **harness** acts (CI, PR monitors, scheduled agents).
    Then two columns: **(1) Skills** — language carries the judgement,
    scripts carry the precision, one skill one job (modularity still
    applies); **(2) Routines** — Claude Code on the web watching a repo,
    scheduled agents, CI that does more than run tests.
    *Punchline:* AI did not only make more things actionable — it made
    **automation on top of actionability cheap**, and that is the real
    multiplier.
11. **So grade *them* too: a skill is a research object** (NEW — the
    recursive turn). Seven-row table mapping every STAMPED property onto
    a skill/automation (S: carries its own references, not "see our
    wiki"; T: `metadata.version` + history; A: runnable, not only prose;
    M: one skill one job; P: no hardcoded paths; E: fresh sandbox;
    D: published, not pasted into chat).
    *Punchline:* **good automation and good skills pass the STAMPED
    checklist — that is precisely what makes them reusable beyond the
    person who wrote them.** Footer carries the checklist / examples /
    principles / `main.tex` links (absorbed from the old
    "Operationalized, not aspirational" slide).

### Act III — What makes it actionable in practice (≈6 min)

12. **Standards = the agent's grammar** — BIDS as the worked example.
    `BIDS-minder.svg`; the schema is *data an agent queries*, the
    validator is the type-checker. *(marked SKIP CANDIDATE in-file)*
    **Ends with the explicit jump into the next two slides**: *"a layout
    only tells you what the files are — it says nothing about how they
    came to be, or what it cost."*
    **Standard → `datalad run` → `duct` = what it is → how it was made →
    what it took.** Three layers, and an agent needs all three. This is
    the connective tissue Act III previously lacked.
13. **Tracking: `datalad run`** — the RUNCMD commit record.
14. **Provenance doesn't care who wrote the code** — AI-written or
    hand-written, same record shape; the tests don't know either.
15. **`con/duct`** — self-contained execution logs.
    *(marked SKIP CANDIDATE in-file — the next slide carries the argument)*
16. **…and that log IS the provenance you need later** — three operator
    questions answered by the trace rather than by recollection;
    `REPRONIM_USE_DUCT=1`.
17. **All three layers, one real artifact — built with AI** (NEW): the
    [`dandi/compression-comparisons-t261-study`](https://github.com/dandi/compression-comparisons-t261-study)
    worked example, which *is* the BIDS→run→duct bridge in one object.
    Left: the BIDS-shaped, YODA-composed layout (tool and 523 GB data as
    **subdatasets pinned by commit**). Right: a real `[DATALAD RUNCMD]`
    record whose `cmd` **is** a `duct` invocation, so every cell commits
    its own resource trace beside its own results.
    Verified counts (read from the repo 2026-10-06): **1265 commits ·
    1216 `[DATALAD RUNCMD]` · 1095 of those wrapping `duct` · 912 cells,
    0 errors · 3838 h of recorded compute, peak RSS 120 GB · 26
    `Co-Authored-By: Claude` trailers.**
18. **So I tried to `rerun` it. Live, on this laptop.** (NEW) — the
    receipt. See §4b below for what actually happened.

### Act IV — Harnesses, the two ladders, and shared skills (≈8 min)

19. **Agent = Model + Harness** — credited to Oscar's OHBM deck.
    Anatomy table: `AGENTS.md` / skills / hooks / MCP / sandbox, each
    mapped onto the STAMPED property it satisfies.
20. **Where are *you* on the ladder?** (NEW, promoted from the appendix)
    `ai-ladder-skills.png` beside a condensed L1–L5 table (what it looks
    like / the skill you have to acquire). L3 is the 2–3-month tax
    nobody skips and is where reusable skills get extracted.
    *Punchline:* **L4–L5 is exactly where a bad harness stops being
    survivable — invest in the harness, not the model.**
    Credit: Jo Van Eyck, *You are Not Ready: Agentic coding in 2026*.
21. **And the loop that gets you up it** (NEW, promoted): the 5-stage
    mermaid beside the **development-model mapping** — vibe coding
    (2→3→4, knowledge evaporates) / spec-driven (1→2→3→4→2…) /
    compound engineering (…→**5**→1+2…, each cycle cheaper).
    *Punchline:* **stage 5 is where a skill is born** — and what it
    writes down is exactly the artifact slide 11 said must be STAMPED.
22. **That was the *individual* ladder. Here is the *team* one.** (NEW)
    The SciOps maturity figure, converted from
    `pics/borrowed/neuro-sciops.pdf` → `pics/borrowed/neuro-sciops-fig.svg`
    (**vector**; the source PDF is pure vector — 0 rasters, 203 drawing
    ops, text already outlined — so SVG keeps it sharp at any projector
    scale and in the PDF export, and at 403 KB is *smaller* than the
    439 KB raster it replaced).
    **Figure explicitly credited to the SciOps preprint**
    (Johnson, Nguyen, Dichter, …, Martone, Pestilli, Yatsenko;
    arXiv:2401.00077, 2024) — *not* presented as this talk's own.
    The preprint names BIDS / NWB / DataLad / DANDI / brainlife.io as
    its own L3 exemplars and reserves L5 for AI+human-in-the-loop.
    *Punchline:* **L5 presupposes L3 — no closed-loop discovery on top
    of `study_final2/`.**
23. **Everyone is rebuilding the same private harness** — the silo
    failure mode, at machine speed. *(marked SKIP CANDIDATE in-file)*
24. **We are already doing this — upstream, in public** — the
    `K-Dense-AI/scientific-agent-skills` contribution table.
25. **`con/skills`** — our own domain-agnostic set.

### Act V — The honest thesis, and close (≈6 min)

26. **Two regimes — and be honest about which one you are in** (NEW —
    *the thesis slide*). Claim: **the safe size of an AI-assisted work
    item is set by the strength of your verification loop, and nothing
    else.**
    - **A. Scaffolded self-verification** — an executable spec the loop
      is checked against (spec-kit / OpenSpec / LAD); tests and
      validators as the *oracle* (the loop must be able to **fail**);
      provenance so drift is detectable; automated gates before human
      eyes. *Only then* are large autonomous batches defensible.
    - **B. Small, human-reviewable, hand-tried** — a diff a human can
      actually read is a **design constraint, not a courtesy**; one
      concern per change; **run it by hand before you believe it**;
      cheap to back out. *Not a lesser mode — the correct default until
      A is actually built.*
    - *Punchline:* there is no third regime where large unverified agent
      output ships safely; and the way out of B is not a better model
      but **A**ctionable specs, **T**racked provenance, **M**odular
      units — STAMPED again.
    - Kicker, correctly attributed: *"Well, less is more"* — Robert
      Browning, *Andrea del Sarto*, **1855**; later Mies van der Rohe's
      motto, and he credited Peter Behrens rather than claiming it.
27. **We are not the only ones saying this** (NEW — the receipts;
    marked SKIP CANDIDATE, ideal to hold for Q&A). See §4 below.
28. **HI ⇄ AI: every project picks its own policy** — 4-row table.
    The *Autonomous* row now names real exemplars:
    [**Brain Researcher**](https://brain-researcher.com/) (Poldrack lab;
    arXiv:2608.19902) and [**K-Dense AI**](https://github.com/K-Dense-AI/)
    (whose skills library we contribute to). Footnote makes the point
    that both are **harnesses** — *autonomy is bought with structure,
    not with a bigger model*. ICMJE Jan 2026 + melissawm catalog.
    Now prefaced with the regime mapping: **rows 1–2 live in regime B;
    rows 3–4 are only honest once regime A is actually built.**
29. **Monday checklist** — 6 actions (added: *size the work to the loop
    you actually have, and say so out loud so nobody mistakes B for A*).
30. **Acknowledgements** — canonical layout.
31. **Thank you** — STAMPED/Yoda sign-off.

### Appendix (vertical sub-deck, skipped live)

- **STAMPED vs. FAIR** — different jobs (demoted from Act II).
- **Portable + Ephemeral** — `datalad containers-run` +
  ReproNim/containers (demoted from Act III).
- **AI coding ladder, the long version** — per-level detail, time costs,
  the "don't start at L5" warning.
- **BEP028** — provenance lifted into a community standard.
- **`con/yolo`** (ephemerality + portability applied to the agent itself)
  and **`con/serve`**.
- **Related CON talks** table.

## 4. External evidence used (and where)

| Claim on a slide | Source |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Structure beats scale: tool-selection 23.3% → 93.6% across 7 models | Chen, …, Poldrack, *Bringing analytic rigor to agentic AI for science*, [arXiv:2608.19902](https://arxiv.org/abs/2608.19902), 2026 — footnote on the hinge slide |
| SciOps maturity figure + L3 exemplars + L5 = AI-in-the-loop       | Johnson *et al.*, [arXiv:2401.00077](https://arxiv.org/abs/2401.00077), 2024 — credited on-slide    |
| Agent = Model + Harness; `AGENTS.md` as contract; grounding wins  | [Oscar Esteban, OHBM 2026 Educational](https://www.nipreps.org/presentations/2026-OHBM-AI-Educational/) |
| AI coding maturity ladder L1–L5                                   | [Jo Van Eyck, *You are Not Ready: Agentic coding in 2026*](https://www.youtube.com/watch?v=6W_-YWHKwZ4) |
| Autonomous-stance exemplars                                       | [brain-researcher.com](https://brain-researcher.com/), [K-Dense AI](https://github.com/K-Dense-AI/) |
| AI cannot be an author                                            | [ICMJE, Jan 2026](https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html) |

### Backing for the two-regimes thesis (slide 27)

| Source | What it supplies |
| ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [DORA 2025](https://dora.dev/insights/balancing-ai-tensions/) (Google Cloud)                  | AI adoption raises throughput **and** delivery instability; *"working in small batches is a critical countermeasure to the risks of AI-assisted development"*; *"verification is a fundamentally different cognitive task than creation"* |
| [METR RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), 2025    | 16 experienced OSS devs, 246 real issues on repos they maintain: **19% slower** with AI while estimating **20% faster**. METR now labels it historical — cite it for the *perception gap*, not as a current benchmark |
| [Addy Osmani](https://addyo.substack.com/p/code-review-in-the-age-of-ai)                      | *"Proof over vibes"*; verification is the bottleneck; *break agent output into digestible commits*; no PR without tests or a demo |
| [Simon Willison](https://simonwillison.net/2025/Dec/18/code-proven-to-work/)                  | *"Your job is to deliver code you have proven to work"*; the skill is instructing **and then confidently verifying**; a model cannot take accountability |
| [Faros telemetry](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025) (~22k devs) | PR size **+51%**, median time in review **+441%**, incidents per PR **+243%** |

Attribution note for the kicker: *"less is more"* first appears in
Robert Browning's *Andrea del Sarto* (1855) — **not** Mies van der Rohe,
who adopted it as a motto and himself credited Peter Behrens
(AEG turbine factory façade, ~1907). The common misattribution to Mies
is worth getting right on a slide in a deck that otherwise insists on
sourcing. Robert Venturi's *"Less is a bore"* (1966) is the standard
rebuttal if anyone wants the counter-aphorism.

## 4b. The rerun experiment (slide 18) — what was actually done

Run on 2026-10-06, from a clean clone, by someone who is not the author.

**It worked, and the science came back bit-for-bit.**

| | |
| --------------------- | ------------------------------------------------------------------------------------------- |
| Cell chosen           | `42dc5cfa` — `synthetic-tiny__blosc-zstd-level_3-shuffle_byte` |
| Why that one          | `duct` recorded it at **0.5 s / 9 MB RSS**; its only input is a config file in the tool submodule, so none of the 523 GB source data is needed. *The record told me which cells were cheap — that is itself the argument for `duct`.* |
| Setup                 | `uv tool install datalad`; `uv venv envs/compbench`; `uv pip install './code/compression-comparisons-tools[pipeline]' con-duct` |
| Command               | `datalad rerun 42dc5cfa` |
| Result                | `run(ok)` — wall clock **0.549 s**, peak RSS **7.8 MB** |
| **Identical**         | `cr` 1.5142911224682944 · `encoded_bytes` 5283 · `rmse` 0.0 · `round_trip_ok` true · `signal_std` 706.6094860217612 |
| **Differed**          | `encode_time_s` / `decode_time_s` and their derived `*_xrt` — *as they must* |
| **Also differed**     | `manifest.json`: timestamp, originating commit, kernel 6.12→7.1, python 3.13.15→3.13.5 |

### The one STAMPED failure, and it is a real one

`datalad get code/compression-comparisons-tools` **fails for any outside
cloner**. `.gitmodules` carries `url = ../..`, which git resolves against
the superproject URL to `https://github.com/` — not a repository. It worked
on the author's disk (`datalad-url = /home/yoh/proj/dandi/compression-comparisons`)
and nowhere else. Worked around by cloning
`https://github.com/dandi/compression-comparisons` into place by hand.

- **S, T, A, M held. D did not.**
- One-line fix: `url = ../compression-comparisons`.
- This is the honest payoff of the whole deck: *you do not find that by
  reading your own repo; you find it by being someone else.* Present it as
  a finding, not a gotcha.

**Caveat to state out loud:** I reproduced a 0.5-second smoke cell, not a
17-hour production cell. The claim is "the mechanism works end to end",
not "the whole 3838-hour study was re-verified".

## 4c. Companion video playlist (ReproNim channel)

A deliverable in its own right, specified in [`playlist.md`](playlist.md):
an 8-video playlist for the [ReproNim channel](https://www.youtube.com/@repronim)
collecting every video the talk references, so the audience can follow them
from one place.

Metadata (title, channel, date, duration, **licence**) was read from YouTube
with `yt-dlp` on 2026-10-06 — licences are verified, not assumed, because
they decide what may be mirrored:

- **4 videos are CC-BY** (all on the DataLad channel: Pragmatic YODA,
  DataLad-Registry, git-annex-is-complete, compute-on-demand) → mirrorable.
- **1 is ReproNim's own** (the YODA webinar).
- **3 are Standard YouTube Licence** (Jo Van Eyck; Simon Willison ×2) →
  **linked, never mirrored.**

**ReproTube status: nothing outstanding.** Checked against
<https://datasets.datalad.org/repronim/ReproTube/> on 2026-10-06 — all five
mirrorable videos are *already archived* under their own channels, and the
archive is syncing current (a 2026-10-05 ReproNim video is present).

One open design item, not urgent: `con/annextube` models **channels** and
mirrors each channel's own playlists; it has no notion of a curated
**cross-channel** playlist. Recommended default is to leave it — every
mirrorable video is already archived, and the playlist is a *view*
("dashboards visualise, don't own"). The alternative — a small annextube
feature storing an ordered id list plus symlinks into existing per-channel
dirs, skipping licence-forbidden videos — is written up in `playlist.md`.

## 4d. PDF export

Use the repo-level helper (**not** talk-specific): `tools/mkpdf.py`,
documented in `../README.md` alongside the manual `?print-pdf` and
decktape-via-Docker routes.

```bash
uv run --with playwright playwright install chromium   # once
uv run --with playwright python tools/mkpdf.py 2026-reproAI-MIT-STAMPED.html
```

Verified 2026-10-06: **41 pages for 41 slides**, 9.4 MB, SVGs stay
vector, mermaid and slide backgrounds render. Also checked against
`2024-distribits-datalad.html` (16:9, 45 pages) to confirm the page size
really is taken from each deck's own config rather than hardcoded.

Do **not** commit the PDF — it is a derived artifact and the live HTML is
the thing to share. Generate on demand for anyone wanting an offline copy.

## 4e. Workshop cross-references

**Cross-references.** Six one-line pointers to the other talks in the
session are embedded in the deck, each marked `<!-- workshop-xref -->`:
program orientation on *Standing on two talks*, and one each on the
actionability-escalation, skill-is-a-research-object, `datalad run`,
`Agent = Model + Harness` and stage-5-loop slides. They carry first
names and a few words of topic only &mdash; no times, no verbatim
titles. `grep -n workshop-xref` to find or drop them.

The full program, learning objectives, per-session mapping and spoken
hand-off lines live in **`SCHEDULE.local.md`**, which is *not committed*
(`*.local.md` is in `.gitignore`) because it holds other people's
unpublished material.

## 5. Links discipline

Per `~/.claude/CLAUDE.md` §Slides: every issue/PR/repo/paper reference
on a slide is a real `<a href>`; every count links to the live filter
that produces it (e.g. "177 skills" → the repo's `skills/` tree; "15.2%
of DataLad repos carry RUNCMD" → the usage dashboard). A one-liner on
the first content-dense slide tells the audience counts are links.

## 6. Open TODOs before delivery

- [ ] Skim the one co-presenter deck that was shared (link in
      `SCHEDULE.local.md` §4) and align vocabulary &mdash; it is not
      publicly readable, so it could not be checked automatically.
- [ ] Re-read the `workshop-xref` lines once the running order is final;
      three of them say "next" / "this morning" and would be wrong if
      the order changes.
- [ ] PR #265 may merge before Oct 16 — re-check its state and flip the
      slide's "open" badge if so.
- [ ] Optional: webshot of `K-Dense-AI/scientific-agent-skills`
      `skills/bids/SKILL.md` for slide 20 (currently text + links only).
- [ ] Optional: refresh the DataLad usage-registry RUNCMD percentage.
- [ ] `pics/borrowed/neuro-sciops-fig.svg` is **derived** from the annexed
      `pics/borrowed/neuro-sciops.pdf`. Regenerate with:
      `uv run --with pymupdf python -c "import pymupdf; open('pics/borrowed/neuro-sciops-fig.svg','w').write(pymupdf.open('pics/borrowed/neuro-sciops.pdf')[0].get_svg_image(text_as_path=True))"`
- [ ] Publish the companion YouTube playlist on the ReproNim channel —
      see [`playlist.md`](playlist.md) for the ordered list, verified
      licences, the creation recipe, and the ReproTube archival status.
      Then backfill the playlist URL into this file, `playlist.md`,
      `INDEX.md` and the deck's appendix.
- [ ] Optionally report the `.gitmodules` `url = ../..` bug upstream on
      `dandi/compression-comparisons-t261-study` (one-line fix). Doing so
      *before* the talk would be a nice "and it is already fixed" beat;
      leaving it lets the slide stand as a live example. Speaker's call.
- [ ] Timing: **34 main slides for 25 min — this is now well over budget.**
      Four slides carry a `SKIP CANDIDATE` note in their
      `<aside class="notes">`; dropping all four lands at 30, which is
      still ~2 slides long. In priority order: "We are not the only ones
      saying this" (hold for Q&A — it is the single best Q&A asset in
      the deck), the BIDS-minder slide, the con/duct webshot, and
      "everyone is rebuilding the same private harness". If more must
      go, the *rerun* slide (18) can be delivered verbally over slide 17
      in three sentences — but it is the most persuasive slide in Act III,
      so cut it last.
