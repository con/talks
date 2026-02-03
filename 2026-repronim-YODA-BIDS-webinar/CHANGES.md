# Changes Made to Slides

## Summary

Adapted 30-min distribits talk to 40-50 min ReproNim webinar by adding focused accents and references. Total additions: ~10-11 min of new content.

## New Slides Added

### 1. Frozen Frontiers Concept (After YODA Principles Overview)
**Location**: Line ~125 (after YODA poster, before Principle 1)
**Content**:
- Uses pics/surface-depth-v2.jpg image
- "Surface you create, depth you preserve" tagline
- Definition and principles
- Brief examples: ephys, BIDS, papers, software
**Time**: +2 min

### 2. BEP028 Provenance (After datalad run Example)
**Location**: Line ~286 (after git show example, before rerun)
**Content**:
- BEP028: BIDS Extension Proposal for Provenance
- W3C PROV-based: Activities, Entities, Agents
- JSON-LD format
- "Frozen provenance" concept
- Link to spec
**Time**: +1 min

### 3. YODA-Compliant Tools in Practice (Before "raw data to paper")
**Location**: Line ~717 (in Principle 3, before hierarchy diagram)
**Content**:
- BABS (Hoffstaedter+ 2024) - HPC scale with FAIRly big
- Nipoppy - clinical-imaging + Neurobagel dashboard
- BIDS-flux - multi-site, GitLab orchestration
- All create frozen frontiers with source links
**Time**: +2 min

### 4. Dashboard Pattern (After Tools)
**Location**: Line ~735 (after tools, before hierarchy)
**Content**:
- Two-column layout: Data layer vs Visualization layer
- Data: .tsv in YODA (version controlled, source of truth)
- Viz: Neurobagel dashboard (regenerable, ephemeral)
- Example: Nipoppy → Neurobagel
- Principle: "Dashboards consume frontiers, don't own them"
**Time**: +2 min

### 5. DANDI-bib Citation Example (After OpenNeuroDerivatives)
**Location**: Line ~837 (before "common principle" section)
**Content**:
- github.com/dandi/dandi-bib project
- Workflow: metadata → BibTeX/RIS → Zotero (automated daily)
- WiP: citations-collector (DOI → citation discovery)
- 8 citation types, 11 relationships
- Archive metadata (source) → structured citations (frontier)
**Time**: +2 min

## Enhanced Existing Slides

### 6. Principle 2 Summary (Portable Environments)
**Location**: Line ~566
**Added**:
- Universal pattern examples beyond containers
- NeuroDebian: source → .deb packages
- reproducible-builds.org: bit-identical binaries
- snapshot.debian.org: 20PB archive
- "Pattern transcends specific tools"
**Time**: +1 min scattered

### 7. Take-Home Messages
**Location**: Line ~925
**Added bullets**:
- "Freeze frontiers at useful levels, preserve links to origins"
- "Pattern is universal: git, DOIs, snapshots, timestamps"
- "Dashboards visualize, don't own - keep data in YODA"
- "Observability (provenance, BEP028) + reproducibility = trustworthy science"
**Time**: No additional (same slide)

### 8. ReproFlow Webinar Reference
**Location**: Line ~110 (introductory section)
**Added**:
- Link to June 2024 ReproNim webinar
- SciOps principles: Be thorough, efficient, formal
- 80/20 shift: Plan upfront, automate execution
**Time**: +30 sec (reference only)

## Content Review Notes

### Kept As-Is (Still Relevant)
- datalad-usage-registry examples (historical data points)
- distribits 2024 references (prior work citations)
- git-annex addcomputed section
- con/duct examples
- All YODA principle explanations
- OpenNeuroDerivatives examples

### Not Outdated (Recent Enough)
- DataLad registry stats (Oct 2024)
- distribits 2024 talks (recent conference)

### Optional Future Additions (Not Done)
- Meeting archive personal practice (decided not to add - keep talk general)
- Detailed ReproFlow component breakdown (not in original, would add too much)
- AI frontier examples (mentioned in abstract, not expanded)
- More SciOps detail (referenced, not expanded)

## Time Budget

**Original talk**: ~30 min
**New content**:
- Frozen frontiers intro: 2 min
- BEP028 reference: 1 min
- Tools table: 2 min
- Dashboard pattern: 2 min
- DANDI-bib example: 2 min
- Universal pattern: 1 min
- ReproFlow ref: 30 sec
- **Total**: ~10.5 min

**Result**: ~40-41 min talk + 10 min Q&A = 50 min total

## Files Modified

- `2026-repronim-YODA-BIDS-webinar.html` - main slides file
- All changes follow the plan in `TODO.md`
- Uses existing image: `pics/surface-depth-v2.jpg`

## Key Themes Added

1. **Frozen Frontiers** - central organizing concept
2. **Universality** - pattern transcends DataLad/git
3. **Real Projects** - BABS, Nipoppy, BIDS-flux, dandi-bib
4. **Provenance Standards** - BEP028 specification
5. **Dashboard Pattern** - separation of data and visualization
6. **Observability** - provenance + reproducibility

## What Was NOT Done

✅ Did not rewrite existing sections
✅ Did not remove content
✅ Did not add complex demos
✅ Did not create new graphics (used existing surface-depth image)
✅ Did not add deep technical dives
✅ Kept changes focused and incremental

## Next Steps

1. Test slides render correctly
2. Practice timing through full talk
3. Verify all links work
4. Check image loads (pics/surface-depth-v2.jpg)
5. Practice transitions between new and existing content
