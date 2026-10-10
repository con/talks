# Plan: community associations as the backbone of the US-RSE'26 CON talk

Status: **plan only** — nothing implemented. Written 2026-10-10.

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
(<https://chrisproject.org/>), BIDS, INCF, NITRC, scikit-learn, Jupyter
(IPython), **PsychoPy**. Aim at *large* community projects. Cross-check against
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
