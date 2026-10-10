# Plan: community associations as the backbone of the US-RSE'26 CON talk

Status: **in progress.** Written 2026-10-10, state updated 2026-10-10.
See §0 for where things actually stand; the phases in §5 are the plan, §0 is
the truth.

## 0. Current state

Commits so far:

| repo      | commit    | what                                                                  |
| --------- | --------- | --------------------------------------------------------------------- |
| `talks`   | `fe21f2c` | usrse deck adopts the dhmc acknowledgements slide verbatim            |
| `talks`   | `6a5be4f` | one "Funders and in-kind" row, historical order                       |
| `talks`   | `79df3c7` | official PBS and DBIC marks replace the text placeholders             |
| `talks`   | `17f3903` | YOH back among the Centroids; plan state recorded                     |
| `talks`   | `9a5d9fe` | generated project bands replace the hand-placed logo strip            |
| `talks`   | `d22d638` | INCF moves to in-kind; BIDS gets its real mark                        |
| `con.org` | `dd2cad5` | first association schema, harvester, validator (superseded)           |
| `con.org` | `6c18ecf` | defect fixes against the first review                                 |
| `con.org` | `0cf3004` | people and project records extracted, both round-trip clean           |
| `con.org` | `c5840ca` | curated slide selection; decision to adopt the datalad-concepts shape |
| `con.org` | `3d7d5d3` | INCF to in-kind, BIDS logo override                                   |
| `con.org` | *(head)*  | records in the real schema; evidence as JSON-Pointer overlays         |

Phase status:

| # | phase                                              | state                                          |
| - | -------------------------------------------------- | ---------------------------------------------- |
| 0 | branch check, mounts, this plan                    | done                                           |
| 1 | association schema                                 | **done** — see §3, it is not ours              |
| 2 | evidence harvest                                   | PsychoPy and CON converted and validated       |
| 3 | project logos and group photos                     | logos done for the 10-project selection        |
| 4 | `mk_whoweare.py` rewrite (YAML-driven, `--select`) | superseded by `scripts/render_ack_projects.py` |
| 5 | backbone slides from selections                    | acknowledgements band done; rest not started   |
| 6 | playwright verification                            | harness in use throughout                      |

### The finding that reshaped phases 1-2

`ORINOCO-Lite/con-site-specific` is not a future destination — it is a live
corpus of **24 `XYZProject`, 35 `XYZPerson`, 8 `XYZOrganization` and 9
`XYZAgentRole` records for CON**, already carrying `associated_with` with
`object` and `roles`, plus `metadata/overlays/` and `curation-records/`.

Everything the first association schema invented already existed there in
better form, and the one thing missing from it is exactly what we set out to
add: **temporal extent, and provenance of the date.** So the model was
replaced rather than patched — see `con.org:content/associations/SCHEMA.md`,
which is now the reference. §3 below is kept only as the record of what was
tried.

### Defects cleared

1. `psychopy.yaml` corrected (contributor phase to 2018-04-06, Hanke's 2008
   `UNRELEASED` entry attributed to him, the evidence-free `user` claim moved
   to a `pending:` block that is explicitly not asserted).
2. The validator no longer crashes on an empty file, a non-mapping top level,
   or malformed YAML; fault injection confirms nine distinct failures are
   caught and a clean tree exits 0.
3. The bound rule was not just buggy, it was **backwards**: an artifact shows
   the oldest or newest surviving trace, never the event, so a `started` from
   a first commit is an `upper` bound and an `ended` from a last commit a
   `lower` one. Six bounds in the PsychoPy evidence were wrong. The validator
   now enforces direction per slot.
4. `supports: [start]` replaced by a JSON Pointer naming the exact slot, so
   coverage is checked rather than a label trusted.

### Still open

1. **HED has no record anywhere on the site** (`grep` over `content/pages`
   for hedtags / "hierarchical event descriptor" / `>HED<` returns zero). It
   was explicitly asked for on the slide. Fix is to add it to `projects.html`
   under Standards beside BIDS and NWB; commented out in the selection until
   then so the omission is visible.
2. The `xyzrins:` namespace is literally the *demo* namespace, yet all 67
   con-site-specific records use it. Kept for byte-compatibility; needs a
   decision.
3. Whether same-pid records merge across stores — decides whether the
   additive `records/XYZOrganization/con.yaml` (pid plus one attribute) is
   legitimate.
4. Whether a handover belongs in `End`'s Trigger slot. The one mapping made
   by interpretation rather than by matching an existing use.
5. Associations still to write: JB ↔ INCF, Dave Kennedy ↔ NITRC, and the
   remaining projects in the slide selection.
6. `published_anchor` from Pelican's `output/*.html` on every person/project
   record; `anchor_id` demoted.

### Evidence already in hand

- `fsl/debian/changelog` bottoms out **2005-12-28** (Hanke); `pyepl`
  **2006-06-18** (YOH) — corroborating the "2005 — pkg-exppsy" line already in
  our decks.
- PsychoPy upstream `4178d2b09`, *"starting to add unit tests (for Yaro ;-) )"*,
  dates the testing push to **2009-10-02 in upstream's own words**; `6048ffd0b`
  credits a butterworth-filter contribution by name; `neurodebian/*` pull
  requests were merged upstream 2015–2018.
- `neurodebian/sphinx/quotes-*.rst`: **50 dated testimonials, 2007–2011**, ten
  from leads of roster projects (Perez/IPython, Peirce/PsychoPy,
  Kleiner/Psychtoolbox, Varoquaux and Thirion/Parietal, Buccigrossi/NITRC).
  Already public at `neuro.debian.net/testimonials.html`, so citable. Extracted
  to `reports/neurodebian-testimonials.json`. **This is the strongest asset
  found for the talk's thesis** — named project leads on the record about what
  NeuroDebian meant to them.
- Dartmouth-side facts verified from primary sources: Haxby directed DBIC from
  January 2008 "until June 2021", Tor Wager "In July of 2021"; Wager is
  "Director, Center for Cognitive Neuroscience and Dartmouth Brain Imaging
  Center"; CON is listed among CCN's Associated Programs.

### Blocked on answers

1. **CON's founding year**, with a citable artifact. The site repo only bounds it
   to "by 2015-07-21". This decides every `actor: yoh` vs `actor: con` call.
2. Canonical location: embedded JSON-LD in `projects.html` (recommended) vs a
   sidecar YAML.
3. Review vehicle: one PR on `con.org` vs per-project commits.
4. `2026-usrse-con-talk-enh` — merge, cherry-pick the Makefile, or drop.
5. Do Dartmouth / PBS / CCN / DBIC / AWS get `support` records? They are neither
   collaborators nor funders in the same sense, and AWS's support is
   per-archive (DANDI, OpenNeuro, EMBER), not to CON.

### Side findings worth acting on separately

- `projects.html` uses `id="dandi"` **three times** (DANDI, EMBER, OpenNeuro).
  Pelican overwrites them so the live page is fine, but it is misleading in
  source — records key off the generated slug instead.
- `dartmouthpbs.org` (PBS Knowledge, built by Cosanlab) describes the Center for
  Open Neuroscience as *"The Center for Open **Science** …"*, and YOH's faculty
  node is empty. Email drafted to Luke Chang; **sent**.
- CCN's staff page lists YOH as "Adjunct and Research Associate Professor"; PBS's
  directory says "Research Professor". Email drafted to Courtney Rogers.

## 1. Goal

Make the talk's thesis — *community matters more in the age of AI, not less* —
visible rather than asserted, by positioning CON's output as dependent on long
ties to many open-source projects.

Mechanically that means:

1. Enrich the CON website with machine-readable metadata about **when and how**
   CON (and Yarik personally) was associated with each community project, with
   provenance for every claim.
2. Derive a reviewable YAML from that, and drive the acknowledgement slide from
   the YAML instead of hand-tuned HTML.
3. Make the acknowledgement slide *selectable*, so the talk can walk its own
   history: start with Yarik + Haxby + Hanke (the PyMVPA / NeuroDebian / DataLad
   cradle), then expand into ReproNim / INCF / OpenNeuro, and so on.

The online reference for the current hand-tuned slide:
<https://datasets.datalad.org/centerforopenneuroscience/talks/2026-dhmc-ieeg.html#/1/2>

## 2. Findings that shape the plan

### 2.1 Branch state — nothing new on any remote

`2026-usrse-con-talk` and local `master` are both `789f540`. The branch was
merged and **deleted on GitHub** (a `git fetch gh-con --prune` pruned it).
Divergence of local `master`, as `ahead / behind`:

| remote                               | ahead / behind |
| ------------------------------------ | -------------- |
| `gh-con/master`                      | 4 / 0          |
| `hub-con/master`                     | 4 / 0          |
| `datasets.datalad.org/master`        | 4 / 0          |
| `datasets.datalad.org/synced/master` | 6 / 0          |
| `smaug/master`                       | 6 / 0          |

Zero behind everywhere. `smaug` and `datasets.datalad.org` are ssh remotes, so
those two rows are from the last fetch, not freshly verified.

Loose end: **`2026-usrse-con-talk-enh`** is local-only and unmerged — 6 commits
adding `2026-usrse/Makefile` (md to HTML/PDF) and rewriting
`talk-proposal-draft.md` into ventilated prose. Tip message: *"Claude+I's
attempt to shorten it, not sure I like it yet"*.

### 2.2 What already exists (do not duplicate)

- `2026-usrse/community-slide-spec.md` — tiers 0-4, a `community-slide-data.yaml`
  model with `people[].communities`, and an explicit "mass figures at the bottom"
  intent. This plan **supersedes** it; fold it in rather than keep two specs.
- `ORINOCO-Lite/con-site-specific` is further along than "planned": it already
  has `metadata/records/XYZProject/*.yaml` (25), `XYZPerson` (36),
  `XYZOrganization` (9), `XYZAgentRole` (10), plus `sources/`,
  `curation-records/` and provenance overlays. Associations exist as
  `dlthings:Association` with `roles`, e.g. `bids.yaml` carries
  `object: xyzrins:persons/yaroslav-halchenko, roles: [marcrel:ctb]`.
  **What is missing there is exactly what we want to add: temporal extent and
  provenance-of-the-date.** The YAML below must convert cleanly into these.
- `content/pages/projects.html` already has 31 entries across Software /
  Initiatives / Meetings / Standards / Education / Infrastructure, each a
  `<div class="row">` with an `<h2 id="...">` anchor and `class="centroid"`
  person links. Several wanted additions (BIDS, EMBER, PyMVPA, distribits) are
  already there; INCF and NITRC are under Partners on `whoweare`. So this is as
  much **restructuring** as adding.

### 2.3 Repositories

| path                         | status     | why it is needed                                                 |
| ---------------------------- | ---------- | ---------------------------------------------------------------- |
| `/home/yoh/proj/CON/talks`   | present    | slides, `tools/mk_whoweare.py`, these notes                      |
| `/home/yoh/proj/CON/con.org` | **absent** | the write target; all site enrichment happens here               |
| neurodebian clone (path TBD) | **absent** | `debian/changelog` first-upload dates — the real dating evidence |
| `con-site-specific` clone    | **absent** | shape the YAML to its records so migration is mechanical         |

All three are reachable read-only over the web (github, `neuro.debian.net`, the
copyright extracts), but writes need `con.org` mounted locally.

## 3. Data model

> **Superseded.** The model below was written before
> `con-site-specific`'s records were found. It is kept as the record of what
> was tried and why it was dropped; the live reference is
> `con.org:content/associations/SCHEMA.md`. In short: `phases` was a list of
> associations, `actor` was a reinvention of `Association.object`, `role` was
> already multivalued and IRI-typed, `transitioned_to` is `End`'s Trigger,
> and `supports:` is a JSON Pointer.


### 3.1 Associations are phases, not a start/end pair

The recurring story is **transition**, not a clean stop. PsychoPy is the
archetype: inception-era involvement and the push to add unit testing (recalled
as a Yale hackathon — needs verification), then NeuroDebian packaging, then
offloaded to Debian Med, and we remain users. scikit-learn (SVN to git migration
via NeuroDebian, then veined off) and Jupyter/IPython (via NiPy around 2008, then
Debian/NeuroDebian, drifting to user-only somewhere 2015-2020) follow the same
shape.

So each `(CON <-> project)` record holds a **list of phases**:

```yaml
project: psychopy
phases:
  - role: contributor          # contributor | maintainer | packager | founder | user | steering
    via: direct                # direct | neurodebian | datalad | repronim | dandi | ...
    start: 2009-??             # ISO 8601, partial allowed
    end: ~                     # null = ongoing
    status: transitioned       # active | transitioned | user-only | dormant
    note: initiated unit testing
    provenance:
      - source: https://...
        kind: recollection     # debian-changelog | copyright-extract | site-git-history |
                               # publication | recollection
        confidence: unverified # certain | approximate | unverified
```

**Rule: no date without at least one `provenance` entry.** Recollections are
recorded as recollections and flagged for human confirmation, never silently
promoted to fact.

### 3.2 AI-contribution stance

Researched rather than invented. The draft `ai-contribution-policy.yml` standard
defines four stance values verbatim; the 281-policy landscape study adds
`encouraged` as a distinct category (7.1% of projects actively promote AI use,
against 76.2% permit and 14.9% forbid). Combined, with one honest addition:

| value               | meaning                                | informal term  |
| ------------------- | -------------------------------------- | -------------- |
| `encouraged`        | policy actively promotes AI assistance | "AI embracing" |
| `unrestricted`      | permitted, no disclosure expected      |                |
| `disclosed-allowed` | permitted if disclosed and attested    | "AI cautious"  |
| `restricted`        | allowed only in stated circumstances   |                |
| `prohibited`        | not accepted                           | "AI averse"    |
| `unstated`          | **no published policy**                | —              |

`unstated` is non-negotiable: it is the majority case and must never be
collapsed into either extreme.

Two framings worth borrowing from that literature, because they fit the talk:
**verification over detection** (attest "I ran the tests, I understand this
change"; never try to answer "was this AI?", which is unanswerable) and
**disclosure over bans** — the bans are what close contribution pathways that
took thirty years to open.

### 3.3 Projects carry a stance; people carry quotes

A project's stance is a published fact with a URL. A *person's* stance, absent a
public statement, is an inference about a named individual that would end up on a
public website and a conference slide, attached to people whose collaboration the
talk celebrates. Getting that wrong damages exactly the ties the talk is about.

- **Projects** — `ai_contribution_stance` from the enum, with `source_url` and a
  `captured` date (policies change fast; the landscape study tracked 196
  policy-change commits). No policy found means `unstated`.
- **People** — no scale. A list of *stated positions*:
  `{stance, scope, quote, source_url, date}`, where `scope` records what they
  were speaking for (their project, their lab, contributions they accept).
  No public statement means the field is **absent**, not `prohibited`.

Named examples still needing a citable artifact before they go in: Dimitri
Yatsenko / DataJoint and Satrajit Ghosh. Check whether the SciOps maturity model
paper already cited in these decks (arXiv 2401.00077; Johnson, ..., Halchenko,
..., Yatsenko) carries a usable statement, rather than asserting from reputation.

CON is the one case where we *are* the authority: declaring CON's own stance —
possibly by adopting `ai-contribution-policy.yml` in CON repos — is both honest
and a talk beat.

### 3.4 Where the canonical data lives

Proposal (**decision 1 below**): a hidden
`<script type="application/ld+json">` inside each project's existing
`div.row` in `content/pages/projects.html`, keyed to the anchor id. Invisible on
the page, machine-readable, and shaped 1:1 onto the `XYZProject` /
`dlthings:Association` records in `con-site-specific`. The slide-facing YAML is
then **derived** from the site, with a round-trip check, so the site stays the
single source.

## 4. Project roster to cover

Wanted additions, beyond what `projects.html` already lists: Debian, Debian
Med / Debian Science blends, distribits, PyMVPA, EMBER, Kitware, ChRIS
(<https://chrisproject.org/>), BIDS, **NWB**, **HED**, INCF, NITRC,
scikit-learn, Jupyter (IPython), **PsychoPy**.

NWB and HED are not optional: NWB is the format the whole DANDI/EMBER side
rests on, and HED is the annotation layer NEMAR already searches by. Both are
standards bodies we sit inside rather than tools we merely use, which is the
distinction the `roles` field exists to carry (`steering` vs `user`). Aim at *large* community projects. Cross-check against
<https://centerforopenneuroscience.org/projects> and
<https://centerforopenneuroscience.org/whoweare#partners_>.

Most associations arrived either **through NeuroDebian** (PsychoPy,
Psychtoolbox-3, scikit-learn, Jupyter) or through **multiple vehicles over time**
(OpenNeuro: originally via DataLad, later also ReproNim and DANDI) — the `via`
field exists to make that legible.

## 5. Phases and success criteria

### Phase 1 — model

Implement the schema above; add a JSON Schema and a validator.

*Success:* every record validates; **no date and no stance without a source**;
`reports/associations-review.md` lists every `recollection` / `unstated` entry at
the top, so the human review pass is short and targeted.

### Phase 2 — harvest, with provenance

Sources: site git history (first commit adding each `<h2 id="...">` gives "listed
on the CON site since"); neurodebian `debian/changelog` first entries; the
copyright extracts at `https://neuro.debian.net/debian/extracts/<pkg>/copyright`;
each project's CONTRIBUTING / AI policy file for the stance.

*Success:* zero invented dates; the "transitioning" pattern is visible as phases
for PsychoPy, scikit-learn and Jupyter; each unverified item names the specific
artifact to check next (a changelog entry, a mailing-list thread, a commit).

### Phase 3 — photos and contributor listings

Group photos (distribits, Debian, BIDS) come from Yarik; contributor montages
generated where a public API exists. Mention `con/tributors` (built with
Vanessa Sochat of USRSE, still used by DataLad and others) as our own
contribution to this problem.

*Success:* every project row can render either a logo, a group photo, or a
contributor montage — no empty cells on the slide.

### Phase 4 — rework `tools/mk_whoweare.py`

Site -> reviewable `con-community.yaml` -> renderer. New capabilities: project
tiers alongside people tiers; row balancing (equal-ish widths when a tier wraps);
and **selection**, so a slide is specified as e.g.
`--select yoh,haxby,hanke +pymvpa,neurodebian,datalad`. Stance may drive an
optional visual channel, off by default.

*Success:* regeneration **reproduces the current hand-tuned slide**. Today it
would not — a `--inject` run destroys the Funders tier, the commented-out
self-portrait, the logo rows and the `--cww-face` / `--cww-cell` overrides. Any
remaining deviation must be explained, not overwritten.

### Phase 5 — slides

Regenerate the acknowledgement slide from YAML; produce the staged backbone
progression for the talk.

### Phase 6 — verification (playwright)

- **Website**: render every touched page before and after; hidden metadata must
  change the rendering by **zero pixels**. Sharp and falsifiable.
- **Deck**: the three-way comparison already built for `2026-dhmc-ieeg` —
  slide structure (position, transitions, fragments, objects, images), rendered
  text, and per-slide pixels. Remember to strip per-slide `data-transition`
  attributes before measuring, or bookend slides get captured mid-animation.

## 6. Open decisions

1. **Canonical location** — embedded JSON-LD in the site HTML (recommended: the
   site stays the single source, YAML is derived and round-trip-checked), or a
   sidecar YAML in the site repo with the HTML untouched?
   potentially could be done within con-site-specific and then reflected within con.org in its current form (until orinoco-lite is finished) done by claude, not scripted I guess.
2. **Review vehicle** — one PR on `con.org` carrying the review table, or
   per-project commits so entries can be accepted piecemeal?
3. **`2026-usrse-con-talk-enh`** — merge, cherry-pick the Makefile only, or
   leave it?

## 7. Sources

- OSS AI-Contribution Policy standard (stance enum; **early-stage**: schema
  v0.1, 21 catalogue entries, AI-assisted drafting per its own README) —
  <https://github.com/dapper-agent/oss-ai-contribution-policy>
- Hora, Robbes & Zacchiroli, *"We Permit the Use of AI, but [...]": The Landscape
  of AI Policies in Popular Open Source Projects*, arXiv:2609.07542 —
  <https://arxiv.org/html/2609.07542>
- Robles & German, *You can contribute if you... An Empirical Framework of AI
  Contribution Policies in OSS*, arXiv:2609.07919 —
  <https://arxiv.org/pdf/2609.07919>
- *AI Policy, Disclosure, and Human in the Loop: How Are Contribution Guidelines
  Adapting to GenAI?*, arXiv:2605.16706 — <https://arxiv.org/html/2605.16706>

Adopt the *vocabulary* from the first; do not depend on the project itself.
