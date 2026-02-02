# Integrating Frontier Condensation Throughout the Presentation

## Core Message Shift

**Previous framing**: YODA as organizational principles + tools
**New framing**: YODA enables **hierarchical transformation through condensed frontiers**

Every module/subdataset is:
1. A stopping point for complexity growth
2. A transformation to more appropriate form
3. A usable interface (frontier) with links to full source (depth)

**Tagline**: *"Surface you create, depth you preserve"*

## How Frontier Condensation Appears in Each Act

### Act I: YODA Foundation
*Introduce the concept*

**Slide: "YODA Principle 3: Modular Composition" (expand)**
- Current: Just shows submodule hierarchy
- **Add**: Each level is a **condensed frontier**
  - Not just organization
  - Active transformation
  - Size reduction + format appropriateness
  - Examples: TB → GB → MB → KB

**Visual metaphor options**:
- Iceberg: Visible tip (frontier), accessible depth (source)
- Pyramid: Condensed summit, detailed base, connected
- Telescope: Zoom in (drill down) or out (work at frontier)

**Key message**: "Modular ≠ just folders. Modular = hierarchy of transformations."

### Act II: Execution & Workflows (SciOps)
*Show frontier condensation in practice*

**Reorganize around transformation stages:**

#### 1. Data Acquisition Frontiers
- **ReproIn**: DICOM (scanner raw) → BIDS (structured)
  - Same data, more appropriate format
  - Metadata extraction as frontier creation
- **ReproStim**: Video stream → event-synchronized recordings
  - Capture what actually happened (not just planned)
  - Original stimulus files + actual presentation record

#### 2. Processing Frontiers
- **BIDS → Derivatives**: fMRIPrep, MRIQC
  - Multi-hour scans → quality metrics (seconds to review)
  - Volume-by-volume → summary statistics
  - **Dashboard pattern**: Nipoppy tracker .tsv → Neurobagel visualization
    - Data (frontier) = version controlled
    - Dashboard = regenerable view

#### 3. Provenance Frontiers
- **BEP028**: Execution details → structured prov records
  - Full logs → key Activities/Entities/Agents
  - Machine-readable, queryable
- **con/duct**: System calls → execution graph
  - Thousands of operations → flame graph visualization
  - Raw JSON → plotted insights

#### 4. Workflow Tool Comparison (Frontier Condensation Strategies)

**Table/comparison slide:**

| Tool | Source | Frontier | Scale | Approach |
|------|---------|----------|-------|----------|
| **BABS** | Raw BIDS | Derivatives | 1000s subjects, HPC | FAIRly big + DataLad |
| **Nipoppy** | Multi-modal raw | BIDS + phenotype .tsv | Clinical integration | DataLad + Dashboard |
| **BIDS-flux** | Multi-site data | Harmonized datasets | Federated | GitLab + MinIO |
| **ReproMan** | Any compute | Job specs + results | Cross-platform | Environment orchestration |

**Common pattern**: All create frontiers while maintaining source links.

### Act III: Hierarchical Composition (BIDS as YODA Exemplar)
*BIDS as cascade of frontiers*

**Slide: "BIDS Pipeline as Frontier Cascade"**

Show 4-stage transformation:
```
Scanner raw (DICOM, GB/subject)
    ↓ ReproIn
BIDS (NIfTI+JSON, GB/subject) ← Frontier 1
    ↓ fMRIPrep/MRIQC
Derivatives (processed, GB/subject) ← Frontier 2
    ↓ Analysis
Statistical maps (MB/subject) ← Frontier 3
    ↓ Publication
Figures & tables (KB) ← Frontier 4
```

**Each arrow is**:
- Version-controlled transformation (`datalad run` or BEP028)
- Size/complexity reduction
- Format change for next use
- Reversible (can drill down)

**OpenNeuroDerivatives example**:
- Each derivative = frontier
- Each maintains link to raw BIDS (source)
- Multiple analysis groups can create competing frontiers
- Same source, different transformations, all preserved

### Act IV: AI Frontier (Structure Enables Intelligence)
*AI tools as frontier generators*

**Slide: "AI-Generated Frontiers"**

**Traditional problem**:
```
Papers (unstructured) → LLM → Summary (unverifiable)
                              ↓
                         Hallucinations, no links
```

**Structured approach**:
```
Structured corpus (BIDS, DANDI, papers+metadata)
    ↓ AI transformation (NotebookLM, LLMs)
Version-controlled summary ← Frontier
    ├── README-summary.md (condensed)
    └── .datalad/config (links to source)
```

**Examples**:

1. **Literature: dandi-bib**
   - Source: DANDI metadata (API)
   - AI step: Citation discovery via citations-collector
     - Query OpenAlex, CrossRef, DataCite
     - Classify citation types (8 types)
     - Merge preprint/published versions
   - Frontier: citations.tsv + Zotero collection
   - Use: Understand dataset impact, find related work

2. **Quality Control**
   - Source: 1000s of MRIQC metrics (.tsv files)
   - AI step: Anomaly detection
   - Frontier: Flagged subjects with explanations
   - Regenerable as models improve

3. **Meeting Documentation**
   - Source: Zoom recordings (GB, archived locally)
   - AI step: Whisper transcription + summarization
   - Frontier: Minutes with timestamps (KB)
   - Reusable resource: Training, quotes, decision archaeology

**Key difference from RAG**:
- RAG: Query web → synthesize → ephemeral answer
- Structured: Query local corpus → generate frontier → version control → verify

**Slide: "Observability → Insight"**
- duct traces + LLM = "Why did pipeline fail?"
- Bash history + code + LLM = "What actually ran?"
- Zoom + notes + LLM = "What was decided in Q3 about X?"

All possible because sources are preserved, frontiers are regenerable.

### Act V: The Vision
*Universal frontier condensation*

**Slide: "Every Lab, A Frontier Factory"**

```
Lab operation               Frontier condensation
─────────────────          ─────────────────────
Daily meetings     →       Minutes (KB) + Archive (GB)
Experiments        →       BIDS (GB) + Summaries (MB)
Analysis           →       Figures (KB) + Full results (GB)
Literature review  →       Annotated bib + PDF archive
Grant writing      →       Submitted grant + Research notes
Teaching           →       Lecture slides + Full recordings
```

**Every activity**:
- Creates usable frontier (work at this level)
- Preserves full source (drill down when needed)
- Version controlled (reproducible)
- Transformations automated (SciOps principles)

**Slide: "Pattern Transcends Tools"**

Show comparison table:

| Domain | Tool/Approach | Pattern |
|--------|---------------|---------|
| Code | Git + submodules | Frontier via modularity |
| Software | snapshot.debian.org | Frontier via timestamps |
| Papers | DOI + references | Frontier via citations |
| Data | DataLad + subdatasets | Frontier via git-annex |
| Containers | Docker + layers | Frontier via content addressing |
| Meetings | Zoom + minutes | Frontier via summarization |

**Message**: "Choose tools that fit your domain, but embrace the principles."

**Principles**:
1. Explicit linking (hexsha, DOI, timestamp, hash)
2. Retrievability (can get exact source)
3. Versioning (new versions, don't overwrite)
4. Automation (scripted transformations)
5. Modularity (independent components)

## Visual Consistency Throughout

**Recommended visual motif**: Two-layer diagrams

```
[Frontier Layer]  ← Small, fast, usable
     ⇅
[Source Layer]    ← Large, detailed, preserved
```

Use this pattern in:
- Software compilation slides
- BIDS pipeline slides
- AI summary slides
- Dashboard explanation slides
- Every example

**Color coding**:
- Frontier: Green (ready to use)
- Source: Blue (preserved depth)
- Transformation: Orange arrows
- Links: Dashed lines (bidirectional)

## Key Terminology Consistency

**Use these terms consistently**:

- **Frontier**: The condensed, transformed, usable form
- **Source**: The detailed, raw, original form
- **Condensation**: The transformation process
- **Link**: The version-controlled association (hexsha, DOI, etc.)
- **Drill down**: Going from frontier to source
- **Surface**: Work at the frontier level
- **Depth**: Preserved source accessibility

**Avoid**:
- "Derived data" (too passive)
- "Processed data" (unclear what happened)
- "Summary" (too limited - transformations aren't always summarization)

## Recommended Slide Additions

### New slide: "Frontier Condensation Pattern" (Act II intro)
- Define the concept
- Show the basic diagram
- List examples across domains
- "This pattern appears everywhere YODA succeeds"

### New slide: "Software Example: Reproducible Builds" (Act II)
- NeuroDebian: source → .deb packages
- reproducible-builds.org: Bit-identical binaries
- snapshot.debian.org: 20PB archive (different approach, same principle)
- "Pattern transcends tools"

### New slide: "Literature Example: DANDI Citations" (Act IV)
- Show dandi-bib workflow diagram
- Metadata → BibTeX/RIS → Zotero (automated daily)
- DOI → citation discovery → classified relationships
- "From archive to knowledge graph"

### New slide: "Meeting Archives as Resource" (Act V)
- Personal practice: Archive all Zoom recordings
- Use cases: Decision archaeology, training, quotes
- Frontier (minutes) used daily, source (video) used occasionally
- "Storage cheap, context priceless"

### Enhanced slide: "Dashboard ≠ Data" (Act II)
- Current: Mention dashboards
- **Enhance**: Show data layer vs. visualization layer
- Nipoppy: .tsv (data, version controlled) → Neurobagel (viz, regenerable)
- "Dashboards consume frontiers, don't own them"

## Narrative Thread

**Opening** (Act I): "YODA enables hierarchical transformation"

**Middle** (Act II-III): "Every tool creates frontiers while preserving sources"

**Climax** (Act IV): "AI amplifies structured frontiers, doesn't replace them"

**Resolution** (Act V): "Pattern is universal—embrace principles, choose tools"

**Closing**: "Surface you create, depth you preserve—this is the YODA way"

## Questions for Tomorrow's Refinement

1. Should we make "frontier condensation" an explicit title for a slide section?
2. How much to emphasize non-DataLad examples (snapshot.debian.org, etc.)?
3. Should the meeting archive practice be personal anecdote or general recommendation?
4. Do we need a "frontier condensation anti-patterns" slide?
5. Should we create a visual "frontier condensation cheatsheet" as final slide?

## Integration with Existing Content

**Keep from original slides**:
- YODA principles overview (enhance Principle 3)
- datalad run examples (frame as "frontier generation")
- Container slides (frame as "environment frontiers")
- OpenNeuroDerivatives examples (perfect frontier cascade)

**Reduce/merge from original slides**:
- Detailed git-annex stats (mention briefly)
- Multiple datalad run examples (consolidate)
- Container technology details (focus on concept)

**Add new**:
- Frontier condensation intro slide
- Software examples (NeuroDebian, reproducible-builds, snapshot)
- Literature examples (dandi-bib, citations-collector)
- Meeting archive example
- Universal pattern comparison table
- AI-generated frontiers section

## Backup Slides (if time)

- Deep dive: BEP028 provenance structure
- Deep dive: citations-collector schema (8 types, 11 relationships)
- Deep dive: con/duct execution graphs
- Case study: OpenNeuroDerivatives workflow
- Tutorial: Creating your first frontier with datalad run
