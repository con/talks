# Realistic TODO List for Feb 6 Webinar

**Time available**: 4 days (Feb 2-5)
**Talk duration**: 40-50 min (vs original 30 min = +10-20 min)
**Strategy**: Add accents, references, key figures - NOT major expansion

## Core Concept Refinement

**"Frozen Frontier"** (not just condensation):
- Snapshot at level most useful for current task
- Fit-for-purpose stopping point
- Connection to origin preserved (redo, drill down, verify)
- Work daily at frontier, access depth on demand

## CRITICAL PATH (Must Do - Days 1-2)

### 1. ✅ Update Metadata & QR Code
**Status**: DONE
- Title, abstract, date, QR code all committed

### 2. Add "Frozen Frontier" Concept Slide (NEW - 2 min)
**Location**: After YODA principles overview, before diving into Principle 1
**Content**:
- 1 slide with clear visual
- Title: "YODA Enables Frozen Frontiers"
- Definition: "Snapshot at useful level + link to origin"
- Simple diagram:
  ```
  [Frontier] ← Work here daily (GB, processed, fit-for-purpose)
      ↕ Link (hexsha, DOI, timestamp)
  [Origin]   ← Redo/verify/detail when needed (TB, raw)
  ```
- 3-4 examples (one-liners):
  - Ephys: Work with spike trains (MB), drill to traces (TB)
  - BIDS: Analyze derivatives (GB), verify from raw (DICOM)
  - Papers: Cite via DOI, retrieve exact version
  - Software: Use binary, rebuild from source
- **Time**: 2 min
- **Effort**: 2 hours (create slide + test visual)

### 3. Strengthen Act II: Add Tools Slide (NEW - 3 min)
**Location**: In Principle 3 (Modular Composition) section
**Content**:
- Title: "YODA-Compliant Workflow Tools in the Wild"
- Table format (brief):
  | Tool | Creates Frontier From | Scale | Reference |
  |------|----------------------|-------|-----------|
  | BABS | BIDS → Derivatives | HPC (n=2565) | Hoffstaedter+ 2023 |
  | Nipoppy | Multi-modal → BIDS+pheno | Clinical studies | github.com/nipoppy |
  | BIDS-flux | Multi-site → Harmonized | Federated | GitLab orchestrated |
  | ReproMan | Any env → Job specs | Cross-platform | Already in slides |
- Footer: "All freeze useful frontiers, preserve links to sources"
- **Time**: 3 min to present
- **Effort**: 3 hours (research links, create table, verify)

### 4. Add Dashboard Pattern Slide (NEW - 2 min)
**Location**: In Act II, after workflow tools
**Content**:
- Title: "Dashboards Visualize Frontiers, Don't Own Data"
- Two-column layout:
  - Left: Data Layer (version controlled)
    - `demographics.tsv`
    - `processing-status.tsv`
    - `qc-metrics.tsv`
  - Right: Visualization Layer (regenerable)
    - Neurobagel digest dashboard
    - Upload data → interactive viz
- Key point: "Data = YODA-frozen, Dashboard = ephemeral view"
- Example: Nipoppy workflow
- **Time**: 2 min
- **Effort**: 2 hours (layout, example)

### 5. Add BEP028 Reference (ENHANCE existing - 1 min)
**Location**: In datalad-run provenance section
**Content**:
- After showing datalad run commit message
- Add 1 slide or text block:
  - "Provenance → BEP028 BIDS standard"
  - Activities, Entities, Agents (JSON-LD)
  - "Frozen provenance: know exactly how frontier was created"
  - Link: github.com/bids-standard/BEP028_BIDSprov
- **Time**: 1 min additional
- **Effort**: 1 hour (add text + link to existing slide)

### 6. Update "Take Home Messages" (ENHANCE - same time)
**Location**: Final slides
**Content**:
- Add to existing bullets:
  - "Freeze frontiers at useful levels, preserve links to origins"
  - "Pattern is universal: git, DOIs, timestamps, snapshots"
  - "Dashboards visualize, don't own - data stays in YODA"
- **Time**: No additional (same slide)
- **Effort**: 30 min (edit existing)

## HIGH PRIORITY (Should Do - Day 3)

### 7. Add Software Example: Universal Pattern (NEW - 2 min)
**Location**: In Principle 2 (Portable Environments) or new "Pattern is Universal" slide
**Content**:
- Title: "Frozen Frontiers: Beyond DataLad"
- Examples showing pattern transcends tools:
  - **NeuroDebian**: source → .deb packages (frozen, installable)
  - **reproducible-builds.org**: Same source → identical binary
  - **snapshot.debian.org**: 20PB archive, timestamp retrieval
  - **DOIs**: Paper version frozen, retrievable
- Message: "Pattern is ancient, tools evolve"
- **Time**: 2 min
- **Effort**: 2 hours (slide creation)

### 8. Add DANDI-bib Example (NEW - 2 min)
**Location**: In Act III or IV (could be "real-world YODA" example)
**Content**:
- Title: "Example: DANDI Citations as Frozen Frontier"
- Show workflow diagram (already exists on GitHub)
- DANDI metadata → BibTeX/RIS → Zotero (automated daily)
- WiP: DOI → citation discovery → classified relationships
- Point: "Archive metadata (source) → structured citations (frontier)"
- Link: github.com/dandi/dandi-bib
- **Time**: 2 min
- **Effort**: 2 hours (grab diagram, simplify for slide)

### 9. Add SciOps 80/20 Slide (NEW - 1 min)
**Location**: Start of Act II (Workflows)
**Content**:
- Reference to June 2024 webinar
- Simple visual: Pie chart shift
  - Before: 80% execution, 20% planning
  - After: 80% planning/automation, 20% execution
- "Automate frontier creation, focus on science"
- **Time**: 1 min
- **Effort**: 1 hour (simple visual)

### 10. Enhance "Modular Composition" Slide (ENHANCE - same time)
**Location**: YODA Principle 3 existing slide
**Content**:
- Add text to existing slide:
  - "Each level = frozen frontier for next level"
  - "Do not look up = freeze dependencies explicitly"
  - Example annotation on existing diagram
- **Time**: No additional
- **Effort**: 1 hour (enhance existing)

## MEDIUM PRIORITY (If Time - Day 4)

### 11. Add Meeting Archive Example (NEW or MENTION - 30 sec)
**Location**: In "unrealized YODA" section or as aside
**Content**:
- Brief mention: "Personal practice: archive all Zoom meetings"
- Frontier: minutes (KB), Source: recordings (GB)
- Use cases: decision archaeology, training, quotes
- "Storage cheap, context priceless"
- **Time**: 30 sec mention
- **Effort**: 30 min (add to existing slide as bullet)

### 12. Add Brief AI Frontier Mention (ENHANCE - 1 min)
**Location**: In conclusion or "future" section
**Content**:
- Add to existing content:
  - "AI tools can generate frontiers: summaries, QC reports, anomaly detection"
  - "But: AI output also frozen and version controlled"
  - "Structure enables verification, not just generation"
- **Time**: 1 min
- **Effort**: 1 hour (add to existing slide)

### 13. Update Acknowledgments (ENHANCE - same time)
**Location**: Existing acknowledgments slide
**Content**:
- Add logos/mentions if not already present:
  - ReproNim, BIDS, OpenNeuro, DANDI
  - Ensure ReproFlow components visible
- **Time**: No additional
- **Effort**: 30 min (check and update)

## LOW PRIORITY (Only If Ahead)

### 14. Create Visual Consistency
**Content**:
- Use two-layer diagram motif where appropriate
- Color coding: Frontier (green), Source (blue), Links (dashed)
- **Effort**: 3-4 hours (risky, cosmetic)

### 15. Add Backup Slides
**Content**:
- Detailed BEP028 structure
- BABS case study
- citations-collector schema
- **Effort**: 2 hours per backup slide

### 16. Practice Demos (RISKY)
**Content**:
- Live datalad run?
- Show dashboard?
- Navigate subdatasets?
- **Risk**: High (demos fail, eat time)
- **Recommendation**: Skip or use screenshots

## EXPLICIT NON-GOALS

❌ **Don't do** (time sinks):
- Complete rewrite of any section
- Deep technical dives into tools
- Custom graphics/animations
- Multiple demos
- New research/reading
- Expanding examples beyond bullet points

✅ **Do instead**:
- Enhance existing slides with new language
- Add 1-2 sentence references
- Use existing diagrams from projects
- Screenshots not demos
- Cite, don't explain in depth

## Time Budget Summary

**Critical path** (Must do): ~11 hours
- Frozen frontier slide: 2h
- Tools table: 3h
- Dashboard pattern: 2h
- BEP028 reference: 1h
- Update take-homes: 0.5h
- Buffer: 2.5h

**High priority** (Should do): ~9 hours
- Universal pattern: 2h
- DANDI-bib example: 2h
- SciOps 80/20: 1h
- Enhance modular slide: 1h
- Buffer: 3h

**Medium priority** (If time): ~3 hours
- Meeting archive: 0.5h
- AI mention: 1h
- Acknowledgments: 0.5h
- Buffer: 1h

**Total realistic estimate**: ~20-25 hours over 4 days = 5-6 hours/day

## Daily Plan Suggestion

**Day 1 (Feb 2 - Today)**: Planning complete ✅
- Review materials (done)
- Decide on structure
- Commit to critical path items

**Day 2 (Feb 3)**: Critical path execution
- Frozen frontier slide (2h)
- Tools table (3h)
- Dashboard pattern (2h)
- = 7 hours

**Day 3 (Feb 4)**: Finish critical + start high priority
- BEP028 reference (1h)
- Update take-homes (0.5h)
- Universal pattern (2h)
- DANDI-bib example (2h)
- SciOps 80/20 (1h)
- = 6.5 hours

**Day 4 (Feb 5)**: Polish + practice
- Enhance modular slide (1h)
- Medium priority items (2h)
- Practice full talk 2x (2h)
- Timing adjustments (1h)
- = 6 hours

**Day 5 (Feb 6)**: Delivery day
- Final review (30 min)
- Setup check (30 min)
- Deliver webinar (50 min)
- Q&A

## Talk Structure & Timing (40-50 min)

**Intro** (3 min)
- Title slide
- YODA principles overview
- **NEW**: Frozen frontier concept (2 min)

**Act I: Principle 1 - Version Control** (8 min)
- Existing content (6 min)
- **ENHANCE**: BEP028 mention (1 min)
- con/duct, tinuous (1 min)

**Act II: Principle 2 - Portable Environments** (6 min)
- Existing containers content (4 min)
- **NEW**: Universal pattern examples (2 min)

**Act III: Principle 3 - Modular Composition** (12 min)
- **ENHANCE**: Frozen frontiers language (no add time)
- **NEW**: Tools table (3 min)
- **NEW**: Dashboard pattern (2 min)
- Existing OpenNeuroDerivatives (4 min)
- Existing YODA hierarchy (3 min)

**Act IV: Real-World Examples** (8 min)
- **NEW**: SciOps 80/20 (1 min)
- **NEW**: DANDI-bib example (2 min)
- Existing ReproFlow components (3 min)
- **ENHANCE**: AI frontier mention (1 min)
- Existing other examples (1 min)

**Conclusion** (3 min)
- **ENHANCED**: Take-home messages (2 min)
- Thank you / questions (1 min)

**Total**: ~40 min talk + 10 min Q&A = 50 min

**Expansion from original**:
- Original: ~30 min
- New content: +10 min
  - Frozen frontier: 2 min
  - Tools table: 3 min
  - Dashboard: 2 min
  - DANDI-bib: 2 min
  - SciOps 80/20: 1 min
  - Various enhancements: ~1 min
- Net: 40 min talk

## Success Criteria

✅ **Must achieve**:
1. Introduce "frozen frontier" concept clearly
2. Show pattern universality (not just DataLad)
3. Connect to current ReproNim ecosystem (BABS, Nipoppy, etc.)
4. Emphasize observability (provenance, dashboards)
5. Fit in 40-50 min total

✅ **Nice to achieve**:
1. Live demo or compelling figure
2. Personal anecdote (meeting archives)
3. AI frontier angle
4. Visual consistency

✅ **Don't need**:
1. Complete rewrite
2. Deep technical dives
3. Novel research
4. Perfect polish

## Risk Mitigation

**If running behind**:
- Skip medium priority items
- Use bullet points instead of full slides
- Mention tools by name only (no details)
- Drop demos entirely

**If ahead of schedule**:
- Add backup slides
- Improve visuals
- Practice more
- Add medium priority items

## Decision Points for Tomorrow Morning

1. **Approve critical path?** (6 items, ~11 hours)
2. **Which high priority items?** (All 4? Pick 2-3?)
3. **Any medium priority must-haves?** (Probably meeting archives)
4. **Visual consistency worth it?** (Probably not, time sink)
5. **Demos or screenshots?** (Screenshots safer)
6. **Daily schedule realistic?** (Adjust as needed)

## Files to Track Progress

Create daily progress files:
- `TODO-day2-progress.md`
- `TODO-day3-progress.md`
- `TODO-day4-progress.md`

Check off items as completed, note blockers, adjust plan.

---

**Bottom line**: Focused enhancements (10 min new content) leveraging existing structure, not a rewrite. Achievable in 4 days with clear daily goals.
