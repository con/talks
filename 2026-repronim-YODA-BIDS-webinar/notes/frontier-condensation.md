# Frontier Condensation: Modular Composition as Hierarchical Transformation

## The Core Concept

Modular composition in YODA isn't just about organizing files—it's about creating **condensed frontiers** at each level of the hierarchy. Each module/subdataset serves as:

1. **A stopping point** ("stopping the bleeding" of data/complexity growth)
2. **A transformation** (extraction, compilation, summarization)
3. **A usable interface** for the next level up
4. **A versioned link** back to the full source

This pattern appears across all domains of computation and science, and YODA+version control makes it explicit and traceable.

## The Pattern

```
Original Source (large, raw, detailed)
        ↓
   [Transformation]
        ↓
Condensed Frontier (smaller, processed, appropriate)
        ↓
   [Used by next level]
```

**Key insight**: The frontier is version-controlled and maintains exact association with its source, allowing bidirectional traversal:
- **Forward**: Use the condensed form (efficient)
- **Backward**: Retrieve exact original (reproducible)

## Examples Across Domains

### 1. Neuroscience - Electrophysiology

**Source**: Terabytes of continuous high-sampling-rate recordings (30 kHz, weeks of data)

**Transformation**: Spike detection and sorting

**Frontier**:
- Spike times (timestamps, milliseconds precision)
- Cluster assignments (which neuron)
- Average waveforms
- **Size reduction**: 1000x-10000x smaller

**YODA implementation**:
```
study/
├── raw-ephys/          (subdataset: TB of continuous data)
└── derivatives/
    └── spike-sorted/   (subdataset: spike trains, MB-GB)
        └── .datalad/
            └── config  (links to exact raw-ephys hexsha)
```

Work with spike trains daily, drill down to raw traces when needed.

### 2. Software Development - Compilation

**Source**: Human-readable source code (text files, with comments, dependencies)

**Transformation**: Compilation and linking

**Frontier**:
- Platform-specific binaries (x86_64, ARM, etc.)
- Optimized for execution
- Stripped of debug symbols (often)
- **Size**: Often smaller, always more appropriate for deployment

**Real-world examples**:

**NeuroDebian** (http://neuro.debian.net):
- Source: Upstream neuroimaging software repositories
- Frontier: Debian packages (.deb) for easy installation
- Maintains links to exact source versions
- Distribution across Debian releases (stable, testing, unstable)

**Reproducible Builds** (https://reproducible-builds.org/):
- Takes source → binary transformation to next level
- Goal: Bit-for-bit identical binaries from same source
- Eliminates timestamps, build paths, randomness
- Enables verification: different builders get identical results
- **Frontier condensation + verifiability**

**Snapshot Archive** (https://snapshot.debian.org/):
- Different approach to preservation (not git-based)
- Archives every version of every Debian package
- ~20PB of historical builds
- Can retrieve exact binary from specific timestamp
- **Shows pattern is universal, not DataLad/git-specific**

**YODA/DataLad implementation**:
```
software-project/
├── src/                (subdataset: source code)
├── dependencies/       (subdatasets: libraries)
└── releases/
    └── v1.2.3/        (subdataset: compiled binaries)
        └── .datalad/
            └── config  (links to exact src hexsha)
```

Distribute binaries, but can always rebuild from exact source. Reproducible-builds ensures same source → same binary.

### 3. Neuroimaging - BIDS Pipeline

**Multi-stage transformation cascade:**

**Stage 1: DICOM → BIDS**
- Source: Scanner raw (DICOM, proprietary formats, ~GB per subject)
- Frontier: Organized BIDS (NIfTI, JSON sidecars)
- Reduction: Similar size, but structured and standardized

**Stage 2: BIDS → Preprocessed**
- Source: Raw BIDS
- Frontier: Preprocessed (fMRIPrep, MRIQC outputs)
- Transformation: Motion correction, normalization, quality metrics
- Reduction: Similar size, but ready for analysis

**Stage 3: Preprocessed → Analysis**
- Source: Preprocessed volumes
- Frontier: Statistical maps, ROI timecourses
- Reduction: Massive (GB → MB)

**Stage 4: Analysis → Publication**
- Source: All statistical maps
- Frontier: Select figures and tables
- Reduction: Extreme (GB → KB)

**YODA implementation**:
```
study/
├── inputs/
│   └── raw-bids/           (subdataset: DICOM → BIDS)
├── derivatives/
│   ├── mriqc/              (subdataset: QC metrics)
│   ├── fmriprep/           (subdataset: preprocessed)
│   └── analysis-2025/      (subdataset: stats)
└── paper/                  (subdataset: figures, manuscript)
    └── .datalad/
        └── config          (links to all source subdatasets)
```

Paper cites exact versions of all upstream data.

### 4. Data Analysis - Summary Statistics

**Source**:
- Individual subject measurements (1000s of subjects × 100s of variables)
- Full timeseries data
- Raw questionnaires

**Transformation**: Aggregation and statistical analysis

**Frontier**:
- Summary statistics (means, SDs, correlations)
- Demographic tables
- Group-level plots
- **Size reduction**: 10000x typical

**Example**:
- Source: 5000 subjects × 200 brain regions × 1200 timepoints = 1.2 billion datapoints
- Frontier: Correlation matrix (200×200) + summary stats = ~40k values

**YODA implementation**:
```
cohort-study/
├── subjects/
│   ├── sub-0001/          (subdataset)
│   ├── sub-0002/          (subdataset)
│   └── ...
└── group-analysis/        (subdataset)
    ├── summary-stats.tsv  (condensed frontier)
    ├── figures/
    └── .datalad/
        └── config         (links to all subject subdatasets)
```

### 5. AI/ML - Embeddings and Indices

**Source**: Full text corpus (billions of tokens, TB)

**Transformation**: Embedding generation, vector indexing

**Frontier**:
- Vector embeddings (dense representations)
- Similarity indices
- **Size**: Often smaller, always faster to query

**Example**:
- Source: 1M documents, 500 words each = 500M tokens
- Frontier: 1M × 768-dim embeddings = ~3GB dense vectors
- Query time: milliseconds vs. hours

**YODA implementation**:
```
knowledge-base/
├── documents/             (subdataset: full text)
└── embeddings/           (subdataset: vectors)
    ├── index.faiss
    ├── metadata.json     (which model, when created)
    └── .datalad/
        └── config        (links to exact documents hexsha)
```

When embedding model improves, regenerate from same source.

### 6. Meeting Documentation

**Source**:
- Full Zoom recording (hours, GB)
- Complete audio transcript
- Chat logs
- Shared screens

**Transformation**: Human curation + AI assistance

**Frontier**:
- Meeting minutes (key decisions, action items)
- Summary document
- **Size reduction**: 1000x (2 GB video → 2 KB notes)

**Real-world practice**:
- Maintain local archive of all Zoom meetings with recordings
- Becomes **reusable resource** for:
  - Clarifying decisions made months ago
  - Training new team members
  - Extracting quotes for papers/grants
  - Understanding evolution of ideas
- Most common use: minutes
- Occasional use: full video review
- **Frontier (minutes) + Source (video) both valuable**

**YODA implementation**:
```
lab-meetings/
├── 2026-02-01/
│   ├── recording/        (subdataset: video, audio)
│   │   ├── zoom-recording.mp4
│   │   └── transcript.txt
│   └── notes/           (subdataset: summary)
│       ├── minutes.md   (frontier)
│       └── .datalad/
│           └── config   (links to recording subdataset)
```

Read minutes daily, watch recording when clarification needed. Archive never deleted—storage cheap, context priceless.

### 7. Genomics - Reference to Variants

**Source**: Full genomes (3 billion base pairs per individual, ~200 GB BAM files)

**Transformation**: Variant calling against reference

**Frontier**:
- VCF files (only differences from reference)
- **Size reduction**: 1000x (200 GB → 200 MB)

**YODA implementation**:
```
genomics-study/
├── reference/            (subdataset: reference genome)
├── alignments/
│   └── sample-001.bam   (subdataset: full alignment)
└── variants/
    └── sample-001.vcf   (subdataset: condensed frontier)
        └── .datalad/
            └── config   (links to alignments + reference)
```

### 8. Literature - From Papers to Citations Database

**Real-world example: DANDI Archive Citations**

**Project**: https://github.com/dandi/dandi-bib + https://github.com/con/citations-collector

**Source Layer 1**: DANDI Archive metadata
- 1000s of neuroscience datasets
- Dataset DOIs, descriptions, contributors

**Frontier 1**: Structured bibliography
- **Transformation**: Daily GitHub Actions workflow (3:22 AM UTC)
- Fetch metadata from DANDI API → Generate BibTeX/RIS files
- Sync to public Zotero collection
- **Output**: `dandi.bib`, `dandi.ris`, Zotero library
- Use case: Easy citation of DANDI datasets

**Source Layer 2**: Academic citation databases
- OpenAlex, DataCite, CrossRef, OpenCitations

**Frontier 2**: Citation discovery (WiP)
- **Transformation**: `citations-collector` queries with dataset DOIs
- Discovers papers citing DANDI datasets
- Merges preprint/published versions
- Classifies citation types (8 types defined in schema):
  - Publication, Preprint, Protocol, Thesis, Book, Software, Dataset, Other
- Classifies citation relationships (11 types):
  - Cites, CitesAsDataSource, Uses, IsDocumentedBy, Reviews, etc.
- Fetches open-access PDFs
- **Output**: TSV file + Zotero subcollection
- Use case: Understand dataset impact, discover related work

**Schema**: https://github.com/con/citations-collector/blob/master/schema/citations.yaml

**Workflow visualization**: https://github.com/dandi/dandi-bib#workflow

**YODA-style organization**:
```
dandi-bib/
├── scripts/           (transformation code)
├── outputs/
│   ├── dandi.bib     (frontier: bibliography)
│   ├── dandi.ris
│   └── citations.tsv (frontier: citation graph)
└── .github/workflows/ (automation: daily updates)
```

**Key insight**: Automated transformation from archive metadata → structured citations → queryable knowledge. Zotero serves as "dashboard" - regenerable view of version-controlled data.

### 9. Simulation - From Runs to Figures

**Source**: Massive simulation output (timesteps, spatial grids, TB)

**Transformation**: Post-processing, visualization

**Frontier**:
- Key summary metrics over time
- Select visualizations
- **Size reduction**: 10000x typical

**Example**: Climate model
- Source: 100 years × 365 days × 24 hours × global grid = PB
- Frontier: Annual averages for key regions = GB

**YODA implementation**:
```
climate-model/
├── runs/
│   └── scenario-RCP85/  (subdataset: raw output)
└── analysis/
    └── temperature-trends/ (subdataset: condensed)
        ├── regional-means.nc
        └── .datalad/
            └── config    (links to runs)
```

## The YODA+Git Advantage

### 1. Exact Association
Every frontier knows its exact source via git hexsha:
```bash
# Which exact version of raw data produced this derivative?
git submodule status derivatives/spike-sorted
# a3f9d1c2... derivatives/spike-sorted (v1.2.0)

# What raw data version does it link to?
cd derivatives/spike-sorted
git submodule status
# 7b8e4a5d... ../raw-ephys (heads/main)
```

### 2. Reproducible Regeneration
If processing improves, regenerate frontier from **exact same source**:
```bash
# Update processing code
git commit -m "Improved spike detection algorithm"

# Regenerate from exact same raw data
datalad run -m "Reprocess with improved algorithm" \
  --input raw-ephys \
  --output derivatives/spike-sorted-v2 \
  spike_sort_v2.py
```

### 3. Multiple Frontiers from Same Source
Different use cases need different condensations:
```
raw-ephys/              (source: TB)
├── spike-sorted/       (frontier 1: spike trains, MB)
├── lfp-filtered/       (frontier 2: LFP bands, GB)
└── spectrograms/       (frontier 3: power spectra, GB)
```

All link to same source, all independently version controlled.

### 4. Frontier of Frontiers
Meta-analyses work on condensed data:
```
meta-analysis/
├── study-001/summary-stats/    (frontier of a frontier)
├── study-002/summary-stats/
└── aggregated/                 (frontier of frontiers)
```

Can still drill down to individual subject in study-001.

## The Pattern is Universal, Not Tool-Specific

**Critical insight**: Frontier condensation is a **general pattern**, not limited to DataLad/git:

### Different Approaches to the Same Pattern

**Git/DataLad approach**:
- Explicit submodule references (hexsha)
- Distributed, federated
- Local clone contains full history

**Debian snapshot.debian.org approach**:
- Centralized archive of all package versions
- ~20PB of historical builds
- Timestamp-based retrieval
- Different mechanism, same goal: exact source retrieval

**Container registries (Docker Hub, etc.)**:
- Layer-based content addressing
- Tag → specific image hash
- Multi-stage builds as frontier cascade

**Data repositories (Zenodo, Figshare)**:
- DOI → specific version
- Can't update published versions (new DOI instead)
- Less granular than git, but same principle

**Academic citations**:
- DOI/ISBN as "permanent" identifier
- Reference list links papers together
- Different granularity than code, same graph structure

### What Matters: The Principles

1. **Explicit linking**: Frontier knows its source (hexsha, DOI, timestamp, hash)
2. **Retrievability**: Can get exact source when needed
3. **Versioning**: Changes create new versions, don't overwrite
4. **Automation**: Transformations are scripted/repeatable
5. **Modularity**: Components can be used independently

**YODA/DataLad advantages**:
- Fine-grained (file-level) tracking
- Distributed (no central chokepoint)
- Unified interface across domains
- Computational provenance (`datalad run`)

**But**: The conceptual pattern predates and transcends any specific tool.

**Message for slides**: "Pattern is ancient, tools evolve—choose what fits your domain, but embrace the principles."

## Dashboard Pattern Revisited

Dashboards are **visualization frontiers**:

**Source**: .tsv files, JSON metadata (YODA-structured data)

**Transformation**: Web rendering, interactive visualization

**Frontier**: Dashboard UI (ephemeral, regenerable)

**Key**: Dashboard is not the source of truth
- Data remains version-controlled
- Dashboard can be regenerated anytime
- Multiple dashboards can visualize same data

**Example: Nipoppy**
```
study/
├── tabular/
│   ├── demographics.tsv       (data: version controlled)
│   ├── processing-status.tsv  (data: version controlled)
│   └── qc-metrics.tsv         (data: version controlled)
└── dashboards/
    └── neurobagel-config.json (points to tabular/)
    # Dashboard runs separately, reads from tabular/
```

## AI-Generated Frontiers

With LLMs, we can create new types of condensed frontiers:

### NotebookLM-style Summaries
**Source**: Full dataset with README, code, results

**Transformation**: LLM analysis

**Frontier**:
- Executive summary
- Key findings document
- FAQ about the dataset

**YODA pattern**:
```bash
datalad run -m "Generate AI summary with NotebookLM" \
  --input . \
  --output ai-summary/README-summary.md \
  generate_summary.py --model=notebooklm
```

The summary is version controlled and links to exact dataset version.

### Anomaly Detection Frontiers
**Source**: 1000s of QC metrics across subjects

**Transformation**: AI-based outlier detection

**Frontier**:
- List of flagged subjects
- Anomaly explanations
- Confidence scores

**Regenerable**: As models improve, re-scan same data.

## Benefits of Frontier Condensation

1. **Cognitive Load Reduction**: Work with appropriate level of detail
2. **Performance**: Query/process smaller, transformed data
3. **Sharing**: Distribute condensed forms, source on demand
4. **Privacy**: Share aggregates while controlling access to raw data
5. **Specialization**: Different teams work at different frontiers
6. **Reproducibility**: Exact links enable verification
7. **Flexibility**: Multiple frontiers from same source
8. **Evolvability**: Regenerate as methods improve

## Anti-Pattern: Orphaned Frontiers

Without version control + modularity:

```
❌ final_analysis_v3.xlsx         (source unknown)
❌ paper_figure_2_revised.png     (which data? which code?)
❌ summary_stats_march.csv        (from which subjects?)
```

**Problems**:
- Can't verify results
- Can't reproduce with updated methods
- Can't trace back to source
- Frontiers become truth (dangerous!)

## Best Practices

1. **Always link frontier to source** (subdataset references)
2. **Document transformation** (`datalad run` or BEP028 provenance)
3. **Version control both** (source and frontier as separate modules)
4. **Make frontiers regenerable** (script the transformation)
5. **Test bidirectional traversal** (can you get from frontier to source and back?)
6. **Don't delete sources** (storage is cheap, lost provenance isn't)
7. **Multiple frontiers OK** (different condensations for different uses)
8. **Dashboards consume, don't own** (data in version control, viz is ephemeral)

## Slides Integration

This concept should appear in:

1. **Act II**: When discussing modularity and "do not look up"
2. **Act III**: BIDS as cascade of frontiers (DICOM → BIDS → derivatives → paper)
3. **Act IV**: AI summaries as condensed frontiers with deep links
4. **Examples throughout**: Every real-world case is frontier condensation

**Visual metaphor**:
- Iceberg: Tip (frontier) is visible/usable, mass below (source) is accessible
- Pyramid: Condensed summit, detailed base, but connected
- Tree: Leaves (frontiers) are visible, roots (sources) provide depth

**Yoda wisdom**: *"Surface you create, depth you preserve"*
