# TODO for ReproNim 2026 Webinar

**Goal**: Adapt 30-min distribits talk → 40-50 min ReproNim webinar
**Strategy**: Add specific accents, references, select figures - NOT major rewrite
**Key concept**: Frozen frontiers - "Surface you create, depth you preserve"

## What We Have

✅ Existing 30-min talk (2025-distribits-YODA.html)
✅ Updated title slide and metadata
✅ QR code generated
✅ Planning notes in 2026-repronim-YODA-BIDS-webinar/
✅ Image: pics/surface-depth-v2.jpg

## Simple TODO List

### 1. Add "Frozen Frontiers" Accent
**Where**: Early in talk, after YODA principles overview
**What**:
- Use pics/surface-depth-v2.jpg image
- Add text: "Surface you create, depth you preserve"
- Concept: Freeze frontier at useful level, preserve link to origin
- Brief examples: spike trains vs traces, derivatives vs DICOM, DOI vs paper
**Time**: +2 min to talk

### 2. Reference Real Projects in "Modular Composition" Section
**Where**: Principle 3 slides
**What**: Add bullet points or brief mentions:
- BABS (Hoffstaedter+ 2024) - HPC scale with FAIRly big
- Nipoppy - clinical-imaging integration
- BIDS-flux - multi-site platform
- "All create frozen frontiers while preserving source links"
**Time**: +1-2 min to talk

### 3. Add Dashboard Pattern Explanation
**Where**: After workflow tools, or in examples section
**What**:
- Data layer (.tsv in YODA) ≠ Visualization layer (dashboard)
- Example: Nipoppy → Neurobagel digest
- "Dashboards visualize frontiers, don't own data"
**Time**: +1-2 min to talk

### 4. Reference BEP028 Provenance
**Where**: In datalad-run provenance section
**What**:
- Add mention after showing run commit
- "BEP028: BIDS standard for provenance (Activities, Entities, Agents)"
- "Frozen provenance - know exactly how frontier was created"
- Link: github.com/bids-standard/BEP028_BIDSprov
**Time**: +1 min to talk

### 5. Add DANDI-bib Example
**Where**: Could be in "real world YODA" examples
**What**:
- Show workflow diagram from github.com/dandi/dandi-bib
- "DANDI metadata → BibTeX/RIS/Zotero (automated)"
- "WiP: citations-collector for citation discovery"
- Example of frozen frontier: archive metadata → structured citations
**Time**: +1-2 min to talk

### 6. Mention Universal Pattern (Not Just DataLad)
**Where**: In summary or throughout examples
**What**: Brief references to:
- NeuroDebian: source → packages
- reproducible-builds.org: bit-identical binaries
- snapshot.debian.org: 20PB archive (different approach, same principle)
- "Pattern is universal, transcends specific tools"
**Time**: +1 min scattered

### 7. Reference Your June 2024 ReproFlow Webinar
**Where**: When discussing ReproFlow components or SciOps
**What**:
- Link to https://datasets.datalad.org/repronim/artwork/talks/webinar-2024-reproflow/#/
- "SciOps principles: Be thorough, efficient, formal"
- "80/20 shift: plan upfront, automate execution"
**Time**: +30 sec

### 8. Update Take-Home Messages
**Where**: Conclusion slide
**What**: Add:
- "Freeze frontiers at useful levels, preserve links to origins"
- "Pattern is universal: git, DOIs, snapshots, timestamps"
- "Dashboards visualize, don't own - keep data in YODA"
**Time**: No additional time

### 9. Optional: Meeting Archive Mention
**Where**: As aside when discussing "what to version control"
**What**:
- "I maintain archive of all Zoom recordings"
- "Frontier: minutes (daily use), Depth: video (when needed)"
- "Storage cheap, context priceless"
**Time**: +30 sec if included

## Estimated Time Additions

- Frozen frontiers intro: 2 min
- Project references: 1-2 min
- Dashboard pattern: 1-2 min
- BEP028 mention: 1 min
- DANDI-bib example: 1-2 min
- Universal pattern: 1 min
- ReproFlow reference: 30 sec
- Total: ~8-11 min

**Result**: 30 min + 10 min = 40 min talk + 10 min Q&A = 50 min total

## What NOT To Do

❌ Rewrite existing sections
❌ Remove content from original talk
❌ Add multiple new complex slides
❌ Create elaborate graphics
❌ Add live demos
❌ Deep technical dives

## Execution Approach

1. Work directly on 2026-repronim-YODA-BIDS-webinar.html
2. Add slides incrementally
3. Enhance existing slides with new text/references
4. Use pics/surface-depth-v2.jpg where appropriate
5. Keep it simple - this is accents, not reconstruction

## Files to Reference

- `notes/act2-refinement-notes.md` - tool references, links
- `notes/frontier-condensation.md` - examples, concepts
- `planning/frontier-condensation-integration.md` - integration ideas
- Original slides: `2025-distribits-YODA.html`

## Key Message Throughout

**"Surface you create, depth you preserve"**
- Work at frozen frontier (appropriate level for task)
- Preserve connection to origin (can always drill down)
- Pattern is universal (many tools implement it)
- YODA makes it explicit and traceable
