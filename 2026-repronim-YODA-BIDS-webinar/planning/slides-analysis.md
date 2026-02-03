# Slides Structure Analysis & Change Plan

## Current Slide Structure (from 2025-distribits-YODA.html)

### Section 1: Intro
- Title slide (UPDATED ✓)
- Acknowledgements
- "A YODA principle a day..."
- YODA principles overview (poster image)

### Section 2: Principle 1 - Version Control Everything
- Why version control?
- VCS allows experiment
- datalad run examples
- datalad rerun
- datalad-usage-registry
- git-annex addcomputed
- con/duct examples
- Summary of Principle 1

### Section 3: Principle 2 - Portable Compute Environments
- Obstacles to sharing environments
- Software containers solution
- Container families (Docker, Singularity)
- datalad-container extension
- ///repronim/containers
- containers-run examples
- Summary of Principle 2

### Section 4: Principle 3 - Modular Composition
- We deal with modules
- Global layouts (FHS, XDG)
- Project layouts
- YODA's Layout
- BIDS examples (nipoppy, princeton, yoda)
- Why git submodules
- When to use submodules
- datasets.datalad.org scale proof
- YODA all the way down
- YODA from raw data to paper
- ReproNim/containers workflow
- ReproMan reference
- OpenNeuroDerivatives example
- "Do not look up" principle
- Corollaries
- Summary of Principle 3

### Section 5: Take Home Messages
- More on YODA via DataLad
- Summary bullets
- Thank you

## Change Plan - Map TODO Items to Sections

### ✅ TODO #1: Add "Frozen Frontiers" Intro (NEW SLIDE)
**Location**: After YODA principles overview (after line 124), before Principle 1
**Action**: INSERT new slide
**Content**:
```html
<section>
  <h2>YODA Enables Frozen Frontiers</h2>
  <img src="pics/surface-depth-v2.jpg" style="width:80%"/>
  <h3>"Surface you create, depth you preserve"</h3>
  <ul>
    <li>Freeze frontier at level useful for current task</li>
    <li>Preserve connection to origin (redo, verify, drill down)</li>
    <li>Work daily at frontier, access depth on demand</li>
  </ul>
  <small>
    <strong>Examples:</strong>
    Ephys: spike trains (MB) ↔ traces (TB) •
    BIDS: derivatives (GB) ↔ DICOM (scanner raw) •
    Papers: DOI cite ↔ exact version •
    Software: binary ↔ source
  </small>
</section>
```
**Estimate**: +2 min

### ✅ TODO #4: Reference BEP028 Provenance (ENHANCE EXISTING)
**Location**: After "Result: automated record" slide (around line 229-260)
**Action**: ADD new slide after git show example
**Content**:
```html
----

### Frozen Provenance: BEP028

**[BEP028](https://github.com/bids-standard/BEP028_BIDSprov)**: BIDS Extension for Provenance

- W3C PROV-based standard for neuroimaging workflows
- Captures: **Activities** (what ran), **Entities** (inputs/outputs), **Agents** (tools)
- JSON-LD format (machine-readable, queryable)
- `datalad run` provenance → can map to BEP028 records

**Frozen provenance**: Know exactly how each frontier was created

<small>
Link: [github.com/bids-standard/BEP028_BIDSprov](https://github.com/bids-standard/BEP028_BIDSprov/blob/master/bep028spec.md)
</small>
```
**Estimate**: +1 min

### TODO #6: Universal Pattern Mentions (ENHANCE EXISTING)
**Location**: In Principle 2 (containers) or add small slide
**Action**: ADD bullets to existing summary slide or create small new slide
**Content**: Add to Principle 2 summary:
```
- Pattern transcends specific tools:
  - **NeuroDebian**: source → .deb packages
  - **reproducible-builds.org**: bit-identical binaries
  - **snapshot.debian.org**: 20PB archive (timestamp-based)
  - **DOIs**: frozen paper versions
```
**Estimate**: +1 min scattered

### ✅ TODO #2: Reference Real Projects (ENHANCE EXISTING)
**Location**: In Principle 3 section, around "YODA from raw data to paper"
**Action**: ADD new slide showing tools
**Content**:
```html
----

### YODA-Compliant Workflow Tools in Practice

Real-world tools creating frozen frontiers:

- **[BABS](https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00074/119046)** (Hoffstaedter+ 2024): BIDS → Derivatives at HPC scale
  - Uses FAIRly big framework + DataLad
  - Demonstrated on n=2,565 (Healthy Brain Network)

- **[Nipoppy](https://github.com/nipoppy/nipoppy)**: Multi-modal → BIDS + phenotypic
  - Clinical-imaging integration
  - Dashboard via Neurobagel

- **[BIDS-flux](https://bids-flux-docs.readthedocs.io/)**: Multi-site → Harmonized
  - GitLab orchestration + MinIO storage
  - Federated research platform

All freeze useful frontiers while preserving source links
```
**Estimate**: +2 min

### ✅ TODO #3: Dashboard Pattern (NEW SLIDE)
**Location**: After tools slide in Principle 3
**Action**: INSERT new slide
**Content**:
```html
----

### Dashboards Visualize Frontiers, Don't Own Data

<div style="display: flex; justify-content: space-between;">
<div style="width: 45%;">
<h4>Data Layer (YODA)</h4>
<small>Version controlled, source of truth</small>
<pre>
study/
├── tabular/
│   ├── demographics.tsv
│   ├── processing-status.tsv
│   └── qc-metrics.tsv
└── README.md
</pre>
</div>

<div style="width: 45%;">
<h4>Visualization Layer</h4>
<small>Regenerable, ephemeral</small>
<ul>
  <li>Neurobagel digest dashboard</li>
  <li>Upload .tsv files</li>
  <li>Interactive exploration</li>
  <li>Can rebuild anytime</li>
</ul>
</div>
</div>

**Example**: [Nipoppy](https://github.com/nipoppy/nipoppy) → [Neurobagel](https://digest.neurobagel.org/)

**Principle**: Dashboards consume frontiers, don't own them
```
**Estimate**: +2 min

### ✅ TODO #5: DANDI-bib Example (NEW SLIDE)
**Location**: Could go in Principle 3 examples or in "real world YODA" section
**Action**: INSERT new slide
**Content**:
```html
----

### Example: DANDI Citations as Frozen Frontier

**Project**: [github.com/dandi/dandi-bib](https://github.com/dandi/dandi-bib)

**Workflow** (automated daily):
1. DANDI Archive metadata (source)
2. → BibTeX/RIS generation (transformation)
3. → Zotero public collection (frontier)

**Work in Progress** ([citations-collector](https://github.com/con/citations-collector)):
- DOI → Citation discovery (OpenAlex, CrossRef, DataCite)
- Classify citation types (8 types: Publication, Preprint, Protocol, Thesis...)
- Classify relationships (11 types: Cites, Uses, IsDocumentedBy...)
- Fetch open-access PDFs

**Archive metadata (source) → Structured citations (frozen frontier)**

<small>
Workflow diagram: [github.com/dandi/dandi-bib#workflow](https://github.com/dandi/dandi-bib?tab=readme-ov-file#workflow)
</small>
```
**Estimate**: +2 min

### TODO #7: ReproFlow Webinar Reference (MENTION)
**Location**: When mentioning ReproFlow components or in intro
**Action**: ADD brief reference
**Content**: Add to existing ReproFlow slide:
```
Reference: [ReproNim Webinar June 2024](https://datasets.datalad.org/repronim/artwork/talks/webinar-2024-reproflow/#/)
- **SciOps principles**: Be thorough, efficient, formal
- **80/20 shift**: Plan upfront, automate execution
```
**Estimate**: +30 sec

### ✅ TODO #8: Update Take-Home Messages (ENHANCE)
**Location**: Conclusion section (around line 793+)
**Action**: MODIFY existing bullets
**Content**: Add to existing take-homes:
```
- **Freeze frontiers** at useful levels, preserve links to origins
- **Pattern is universal**: git, DOIs, snapshots, timestamps (not just DataLad)
- **Dashboards visualize**, don't own - keep data in YODA
- Observability (provenance) + reproducibility = trustworthy science
```
**Estimate**: No additional time

### TODO #9: Meeting Archive (OPTIONAL MENTION)
**Location**: In "what to version control" section or as aside
**Action**: ADD bullet or brief mention
**Content**: Add to version control examples:
```
- Meeting recordings: I maintain archive of all Zoom meetings
  - Frontier: minutes (daily use, KB)
  - Depth: video (when needed, GB)
  - Storage cheap, context priceless
```
**Estimate**: +30 sec if included

## Sections Needing Review/Update

### Potentially Outdated:
1. **Line 311-327**: "datalad-usage-registry" stats from 2021
   - **Action**: Update date reference or note it's historical snapshot

2. **Line 323-326**: "Side-topic: update on git-annex/DataLad stats"
   - Shows 2025-10-21 stats
   - **Action**: Keep as-is (recent enough) or note as "Oct 2024"

3. **Line 353-361**: References to distribits 2024
   - **Action**: Keep as references to prior work

4. **Line 697-703**: ReproMan reference to distribits 2024
   - **Action**: Keep, but could add reference to recent work

### Sections to Potentially Condense:
1. Multiple datalad-run examples could be consolidated
2. Container families details (Docker/Singularity) - keep brief
3. git-annex addcomputed section - could shorten

## Implementation Order

1. ✅ Add frozen frontiers intro slide (after YODA principles)
2. ✅ Add BEP028 reference (after datalad run example)
3. Add universal pattern mentions (in Principle 2 summary)
4. ✅ Add tools table slide (in Principle 3)
5. ✅ Add dashboard pattern slide (after tools)
6. ✅ Add DANDI-bib example (in Principle 3 or examples)
7. Add ReproFlow webinar reference (when mentioning ReproFlow)
8. ✅ Update take-home messages (conclusion)
9. Optionally add meeting archive mention

## Time Check

Original: ~30 min
New additions:
- Frozen frontiers: +2 min
- BEP028: +1 min
- Tools table: +2 min
- Dashboard pattern: +2 min
- DANDI-bib: +2 min
- Universal pattern: +1 min
- ReproFlow ref: +30 sec
- Meeting archive: +30 sec (optional)

Total additions: ~11 min
Result: ~41 min talk + Q&A

## Next Steps

1. Create implementation plan with exact line numbers
2. Make changes incrementally
3. Test slides render correctly
4. Practice timing
