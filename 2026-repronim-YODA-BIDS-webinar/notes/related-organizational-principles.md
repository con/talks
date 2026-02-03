# Related Organizational Principles & Frameworks for Data Science

Research findings on principles similar to YODA, with focus on composition, reuse, and modularity.

## Overview

Multiple frameworks and principles have emerged for organizing data science and computational research projects, each with different emphases but sharing core goals of reproducibility, modularity, and reuse.

## 1. FAIR Principles (2016)

**Source**: [Nature Scientific Data](https://www.nature.com/articles/sdata201618) • [GO FAIR](https://www.go-fair.org/fair-principles/)

**Focus**: Data findability, accessibility, interoperability, reuse

**Core Principles**:
- **Findable**: Data with rich metadata, unique identifiers
- **Accessible**: Data retrievable via standard protocols
- **Interoperable**: Data uses standard formats, vocabularies
- **Reusable**: Data with clear usage licenses, provenance

**Key Differences from YODA**:
- FAIR focuses on **data sharing and discoverability** at archive/repository level
- YODA focuses on **project organization and workflow** during research
- FAIR is about "what" to preserve, YODA is about "how" to organize

**Relationship**: YODA-organized projects facilitate FAIR compliance. [Yoda RDM platform](https://vu.nl/en/about-vu/more-about/yoda-simplify-your-research-data-management) explicitly implements FAIR via YODA structure.

## 2. Cookiecutter Data Science (DrivenData)

**Source**: [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) • [GitHub](https://github.com/drivendataorg/cookiecutter-data-science)

**Focus**: Standardized project templates for data science

**Core Principles** (from "10 Rules of Reliable Data Science"):
1. Data is immutable
2. Notebooks for exploration, pipelines for replication
3. Analysis is a DAG (Directed Acyclic Graph)
4. Build from environment
5. Keep secrets and configuration out of version control
6. Be conservative in changing default folder structure
7. Default structure focuses on **modularity**: separate data, models, code, reports
8. Unix philosophy: chain together best tools for task

**Directory Structure**:
```
project/
├── data/
│   ├── raw/         (immutable)
│   ├── interim/     (transformed)
│   └── processed/   (final datasets)
├── models/
├── notebooks/
├── src/
└── reports/
```

**Similarities to YODA**:
- Immutable data principle
- Clear separation of concerns (modular)
- Version control everything (code at minimum)
- Build from environment (portable)

**Differences**:
- Cookiecutter: flat hierarchy, ML/analytics focus
- YODA: nested subdatasets, general research focus
- Cookiecutter: less emphasis on data versioning
- YODA: git-annex/DataLad for large data management

## 3. Noble (2009) - Computational Biology Organization

**Source**: [PLOS Computational Biology](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424) • [Noble's page](https://noble.gs.washington.edu/papers/noble2009quick.html)

**Focus**: Day-to-day organization of computational experiments

**Core Principles**:
1. **Top-level logical organization**: data/, results/, doc/, src/, bin/
2. **Chronological at next level**: results/2024-01-15-experiment/
3. **Logical below that**: By sample, condition, method
4. **Document everything**: Lab notebook (electronic)
5. **Organize by project**: Each project self-contained

**Key Insights**:
- "Someone unfamiliar with your project should be able to look at your computer files and understand in detail what you did and why"
- Use relative paths (portability)
- Separate data (fixed) from results (computational experiments)
- Driver scripts record parameters and methods

**Similarities to YODA**:
- Logical, hierarchical organization
- Self-contained projects (modularity)
- Documentation as first-class citizen
- Separation of data and results

**Differences**:
- Noble: chronological results tracking
- YODA: version control-centric (every change tracked)
- Noble: single project scope
- YODA: composable multi-project via subdatasets

## 4. Research Compendium

**Source**: [The Turing Way](https://book.the-turing-way.org/reproducible-research/compendia/) • [Gentleman & Temple Lang 2007](https://biostats.bepress.com/bioconductor/paper2/)

**Focus**: Bundling all research artifacts for reproducibility

**Core Principles**:
1. **Self-contained**: All digital materials in one place
2. **Standardized organization**: Conventions many use
3. **Reusable without author**: Complete standalone package
4. **Transparent**: Easy to understand relationships between files

**Typical Structure**:
```
compendium/
├── data/           (raw and processed)
├── analysis/       (scripts, notebooks)
├── paper/          (manuscript files)
└── README.md       (entry point)
```

**Extensions**:
- **rrtools** (R): Functions to create research compendia
- Often packaged as language-specific packages (R packages, Python packages)

**Similarities to YODA**:
- All materials together
- Self-contained and portable
- Standard structure aids understanding
- Focus on reproducibility

**Differences**:
- Research compendium: single study focus
- YODA: supports multi-study composition via submodules
- Research compendium: may use package managers for dependencies
- YODA: uses containers + DataLad for dependencies

## 5. Workflow Management Systems

**Source**: [SC'23 Workshop](https://dl.acm.org/doi/10.1145/3624062.3626283) • [ORNL Best Practices](https://www.ornl.gov/publication/toward-designing-effective-exascale-scientific-computing-workflows-experiences-and-best)

**Focus**: Orchestration of computational pipelines

**Examples**: Nextflow, Snakemake, CWL, WDL, Prefect, Airflow

**Core Principles**:
1. **Task modularity**: Atomic, self-contained modules
2. **Execution/logic decoupling**: Config separate from code
3. **DAG representation**: Dependencies explicit
4. **Reproducibility**: Capture environment, parameters, provenance
5. **Checkpoint-restart**: Handle failures gracefully

**Key Capabilities**:
- Resource allocation and scheduling
- Dependency management
- Provenance tracking
- Container integration
- Parallel execution

**Relationship to YODA**:
- Workflow systems **implement** computational steps
- YODA provides **organizational structure** for inputs/outputs
- Complementary: YODA = file organization, Workflows = execution orchestration
- Example: `datalad run` integrates workflow execution with YODA structure

## 6. MLOps Tools & Principles

**Source**: [DVC vs MLflow comparison](https://censius.ai/blogs/dvc-vs-mlflow) • [Metaflow comparison](https://medium.com/geekculture/comparing-metaflow-mlflow-and-dvc-e84be6db2e2)

**Examples**: DVC, MLflow, Weights & Biases, Neptune.ai, Metaflow

**Core Principles**:
1. **Experiment tracking**: Parameters, metrics, artifacts
2. **Model versioning**: Track model lineage
3. **Data versioning**: Track dataset changes (DVC focus)
4. **Pipeline management**: Define, execute, track pipelines
5. **Reproducibility**: Environment + code + data = result

**Comparison**:

| Tool | Focus | Versioning | Integration |
|------|-------|------------|-------------|
| **DVC** | Data + pipelines | Git-like for data | Extends Git |
| **MLflow** | Experiments + models | Model registry | Framework-agnostic |
| **Metaflow** | Production workflows | Built-in | AWS/Netflix-oriented |
| **YODA/DataLad** | Research data | git-annex | Scientific research |

**Similarities to YODA**:
- Version control for data (DVC, DataLad)
- Pipeline/DAG representation
- Provenance tracking
- Environment management

**Differences**:
- MLOps: ML/model lifecycle focus
- YODA: General research focus, any domain
- MLOps: Often cloud/production-oriented
- YODA: Local-first, federated approach

## 7. Good Enough Practices in Scientific Computing

**Source**: [Software Carpentry](https://carpentries-lab.github.io/good-enough-practices/02-data_management.html) • [Wilson et al. 2017](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)

**Focus**: Minimum viable reproducibility practices

**Core Principles**:
1. **Data management**:
   - Save raw data
   - Create analysis-friendly data
   - Record all steps from raw to final
2. **Software**:
   - Put everything in version control
   - Make requirements and dependencies explicit
3. **Collaboration**:
   - Create overview of project
   - Create shared public workspace
4. **Project organization**:
   - Put each project in its own directory
   - Put text documents in version control
   - Put raw data in version control (or reference location)
5. **Manuscripts**:
   - Write in plain text (Markdown, LaTeX)
   - Keep track of changes

**Philosophy**:
- "Good enough" is better than perfect (which is never achieved)
- Practices should be **actually adoptable** by working scientists
- Incremental improvement over current practices

**Similarities to YODA**:
- Everything under version control
- Project-level organization
- Track all transformations
- Plain text preferred

**Differences**:
- Good Enough: pragmatic minimum
- YODA: more comprehensive framework
- Good Enough: permissive about tools
- YODA: opinionated about DataLad/git-annex

## 8. Modular Data Science Principles (2024-2025)

**Source**: [LinkedIn Guide](https://www.linkedin.com/pulse/building-modular-data-science-project-practical-guide-adonye-brown-dbygf) • [DEV Community](https://dev.to/dare_johnson/how-to-implement-code-modularity-in-data-science-and-machine-learning-projects-1fgm)

**Emerging Principles** (based on 2024 DORA Report):
- Elite teams with modular architectures deploy **973x more frequently**
- Change failure rates **5x lower** than monolithic approaches

**Key Practices**:
1. **Interface standardization**: APIs as contracts between modules
2. **Separation of concerns**: Data, processing, visualization separate
3. **Dependency injection**: External dependencies passed in, not hard-coded
4. **Independent testing**: Each module testable in isolation
5. **Loose coupling**: Modules interact through well-defined interfaces
6. **High cohesion**: Each module focused on single responsibility

**Similarities to YODA**:
- Modularity as core principle
- Clear interfaces (submodule boundaries)
- Independent components
- Testable units

**Differences**:
- Modular DS: code/software architecture focus
- YODA: data + code organization focus
- Modular DS: deployment/production concerns
- YODA: research lifecycle concerns

## 9. Reproducible Builds (Software)

**Source**: [reproducible-builds.org](https://reproducible-builds.org/)

**Focus**: Bit-identical binaries from same source

**Core Principles**:
1. **Deterministic builds**: Same input → same output
2. **Build environment captured**: OS, tools, dependencies versioned
3. **Source availability**: Complete source preserved
4. **Verification**: Anyone can rebuild and verify

**Relevance to Research**:
- Extends reproducibility to **compilation step**
- Source code (frontier) vs binary (frontier) both preserved
- Shows reproducibility patterns transcend domains

## Comparison Matrix

| Framework | Domain | Modularity | Composition | Reuse | Data Versioning | Tool-Specific |
|-----------|--------|------------|-------------|-------|-----------------|---------------|
| **YODA** | Research (any) | ✓✓✓ Subdatasets | ✓✓✓ Git submodules | ✓✓✓ | ✓✓✓ git-annex | DataLad-centric |
| **FAIR** | Data archives | ✗ | ✗ | ✓✓✓ Focus | ○ Metadata | Tool-agnostic |
| **Cookiecutter DS** | Data science/ML | ✓✓ Directories | ○ Flat | ✓ Templates | ○ Recommended | Tool-agnostic |
| **Noble 2009** | Comp biology | ✓ Directories | ○ Single project | ✓ Principles | ✗ | Tool-agnostic |
| **Research Compendium** | Academic research | ✓ Bundled | ○ Packages | ✓✓ Standalone | ○ Varies | Language packages |
| **DVC** | ML/data science | ✓ Pipelines | ✓ Git-like | ✓✓ | ✓✓✓ Focus | Git + DVC |
| **MLflow** | ML experiments | ○ | ○ | ✓ Models | ✓ Limited | MLflow-specific |
| **Good Enough** | General science | ✓ Basic | ○ | ✓ | ○ | Tool-agnostic |

**Legend**:
- ✓✓✓ = Core feature, deeply supported
- ✓✓ = Well supported
- ✓ = Supported
- ○ = Partially supported or recommended
- ✗ = Not a focus

## Key Insights

### 1. Convergent Evolution
Despite emerging independently, these frameworks share core patterns:
- **Hierarchy**: Organized nested structure
- **Separation**: Data ≠ code ≠ results ≠ documentation
- **Immutability**: Raw data never modified
- **Provenance**: Track how results were created
- **Portability**: Avoid absolute paths, hard-coded dependencies

### 2. Domain Specialization
Different domains emphasize different aspects:
- **ML/Data Science** (DVC, MLflow): Model versioning, experiment tracking
- **HPC/Scientific Computing** (Workflow systems): Scalability, resource management
- **Open Science** (FAIR, Research Compendium): Sharing, discoverability
- **General Research** (YODA, Noble): Project organization, daily workflow

### 3. Tool vs. Principle Distinction
- **Principles** (YODA, FAIR, Noble): Can be implemented with various tools
- **Tools** (DataLad, DVC, MLflow): Specific software implementing principles
- **Templates** (Cookiecutter): Concrete instantiation of principles

### 4. Complementarity, Not Competition
Most frameworks are **complementary**:
- YODA + FAIR: Structure projects → share via FAIR
- YODA + Workflow systems: Organize → execute pipelines
- YODA + DVC: Same goals, different implementation (DataLad vs DVC)
- Noble + Cookiecutter: Manual principles → automated templates

### 5. The "Frozen Frontier" Pattern Appears Everywhere
Different terminology, same concept:
- **YODA**: Frozen frontiers (surface you create, depth you preserve)
- **Cookiecutter**: Data pipeline stages (raw → interim → processed)
- **Noble**: data/ (fixed) vs results/ (experimental)
- **Research Compendium**: Bundled artifacts with source links
- **DVC**: Data versions with pipeline stages
- **Reproducible Builds**: Source → binary with provenance

All share: **Condensed working form + preserved source + explicit transformation**

## Notable Gaps

What YODA emphasizes that others often don't:
1. **Multi-study composition**: Subdatasets as first-class concept
2. **"Do not look up" principle**: Explicit no-dependency-on-parent rule
3. **Scale via modularity**: From single file to 8000+ subdatasets (datasets.datalad.org)
4. **Nested version control**: Full git trees at every level, not just top
5. **Federated, not centralized**: No required central authority

What others emphasize that YODA doesn't explicitly:
1. **Discovery/search** (FAIR): Metadata standards for cross-archive search
2. **Deployment** (MLOps): Production serving, monitoring, A/B testing
3. **Team collaboration** (modern DS tools): Real-time sharing, cloud notebooks
4. **Domain specifics** (Cookiecutter variants): Field-specific templates

## Recommendations for Your Talk

### Positioning YODA Among Frameworks

1. **YODA is not alone**: Part of broader movement toward reproducible, organized research
2. **YODA's unique contribution**: Hierarchical composition + frozen frontiers at scale
3. **Pattern transcendence**: Show examples (NeuroDebian, snapshot.debian.org, DOIs) prove pattern is universal
4. **Complementarity**: YODA + BIDS, YODA + workflow systems, YODA + FAIR all work together

### Potential Slide

**"YODA in Context: Organizational Principles Landscape"**

```
Research Organization Principles (2009-2025)

Noble 2009: "Quick Guide to Organizing Computational Biology Projects"
├─ Core: Logical hierarchy, document everything
└─ Impact: Influential, widely cited

FAIR 2016: "Findable, Accessible, Interoperable, Reusable"
├─ Core: Data sharing standards
└─ Impact: Policy requirement (NIH, EU)

Cookiecutter DS 2016+: "Standardized data science templates"
├─ Core: Automated project structure
└─ Impact: Widely adopted in industry

YODA 2018: "YODAs Organigram on Data Analysis"
├─ Core: Modular composition + frozen frontiers
└─ Impact: Neuroimaging, git-annex community

Research Compendium: "All materials bundled for reproducibility"
├─ Core: Self-contained packages
└─ Impact: R community, The Turing Way

MLOps Tools 2018+: "DVC, MLflow, Metaflow, ..."
├─ Core: Experiment tracking, model lifecycle
└─ Impact: ML/AI industry standard

Common Thread: Version control + modularity + reproducibility
YODA's Unique: Hierarchical composition at scale + frozen frontiers
```

### Key Talking Point

> "The pattern is ancient—from software packages to academic citations—but YODA makes it explicit and composable. We're not inventing something new; we're formalizing what works and making it scale from single files to thousands of datasets."

## References

All sources linked throughout this document. Key papers:
- [Noble 2009 - PLOS Comp Biol](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)
- [Wilkinson 2016 - FAIR Principles](https://www.nature.com/articles/sdata201618)
- [Wilson 2017 - Good Enough Practices](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)
- [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/)
- [Research Compendia - Turing Way](https://book.the-turing-way.org/reproducible-research/compendia/)
