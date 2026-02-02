# Act II Refinement Notes - Execution & Workflows

## Key Additions for Tomorrow's Discussion

### 1. Provenance Standards - BEP028
- [BEP028 (BIDS Provenance)](https://github.com/bids-standard/BEP028_BIDSprov/blob/master/bep028spec.md)
- Based on W3C PROV-O ontology
- Defines Activities, Entities, Agents, Environments
- JSON-LD format for machine-readable provenance
- Can be stored in `/prov/` directory or sidecars
- **Key Point**: YODA + BEP028 = complete computational provenance chain

### 2. Dashboard Separation Pattern
**Nipoppy Example:**
- Data layer: `.tsv` files in BIDS hierarchy (YODA-compliant)
- Visualization layer: [Neurobagel digest dashboard](https://digest.neurobagel.org/)
- Upload tracker files → interactive dashboard
- **Principle**: Data remains version-controlled, dashboards consume but don't own

**Other dashboards to mention:**
- BABS processing status tracking
- ReproMan job monitoring
- DataLad-Registry search interface

### 3. YODA-Compliant Workflow Tools

#### BABS (BIDS App Bootstrap)
- [Paper](https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00074/119046)
- [Docs](https://pennlinc-babs.readthedocs.io/)
- Uses DataLad + FAIRly big framework
- HPC-scale (demonstrated on n=2,565 Healthy Brain Network)
- Automatic provenance tracking
- Supports SGE and Slurm
- **Felix Hoffstaedter** co-author (Forschungszentrum Jülich, INM-7)

#### FAIRly big
- [Framework paper](https://www.researchgate.net/publication/355214162_FAIRly_big_A_framework_for_computationally_reproducible_processing_of_large-scale_data)
- DataLad-based, domain-agnostic
- Full audit trail via DataLad
- Used by BABS

#### Nipoppy
- [GitHub](https://github.com/nipoppy/nipoppy)
- [Tutorial](https://repronim.org/resources/tutorials/nipoppy/)
- Lightweight framework for neuroimaging-clinical data
- BIDS + phenotypic data organization
- Integration with DataLad
- Dashboard for processing status via Neurobagel

#### BIDS-flux
- [Docs](https://bids-flux-docs.readthedocs.io/)
- Scalable FAIR data management platform
- Built on BIDS + DataLad
- GitLab for workflow orchestration
- MinIO for object storage
- Containerized BIDSApps
- Multi-site neuroimaging research focus

#### ReproMan
- Already covered in original slides
- Need to emphasize: orchestration across compute environments
- YODA-compliant job specifications

### 4. SciOps Framework (from June 2024 webinar)
Reference: [ReproFlow webinar slides](https://datasets.datalad.org/repronim/artwork/talks/webinar-2024-reproflow/#/)

**Core Principles:**
1. **Be thorough**: Automate provenance information collection
2. **Be efficient**: Automate as much as feasible
3. **Be formal**: Use standardized approaches

**Effort Rebalancing:**
- Current: >80% on data collection/processing
- Goal: >80% upfront planning, automate execution

**ReproFlow Components:**
- **ReproIn/HeuDiConv**: DICOM → BIDS automation
- **ReproStim**: Capture audio/video stimuli presented
- **ReproEvents**: Behavioral event tracking
- **Con/noisseur**: Scanner console input capture
- **ReproMon**: Real-time operator feedback
- **phys2bids**: Physiological data automation

**YODA Connection:**
All of these produce version-controlled outputs that fit into YODA hierarchy

### 5. Proposed Act II Structure

**Act II: Execution & Workflows - The SciOps Way**

1. **The Automation Imperative**
   - 80/20 rule: plan upfront, automate execution
   - SciOps principles (thorough, efficient, formal)
   - Reference to June 2024 webinar

2. **Provenance as First-Class Citizen**
   - BEP028 specification
   - Activities, Entities, Agents
   - `datalad run` → BEP028-compliant records
   - `con/duct` → execution traces
   - `tinuous` → CI/CD provenance

3. **YODA-Compliant Workflow Tools**
   - **ReproMan**: Multi-environment orchestration
   - **BABS**: HPC-scale BIDS Apps (FAIRly big) - Felix Hoffstaedter et al.
   - **Nipoppy**: Clinical-imaging integration with dashboard
   - **BIDS-flux**: Multi-site platform with GitLab orchestration
   - All share: YODA hierarchy + provenance tracking

4. **The Dashboard Pattern**
   - Data ≠ Visualization
   - Data: Version-controlled .tsv files in YODA structure
   - Dashboards: Consume data, provide insights
   - Examples:
     - Nipoppy → Neurobagel digest
     - BABS → processing status
     - DataLad-Registry → dataset search
   - **Principle**: Dashboards are regenerable views, not truth

5. **Complete Capture - ReproFlow Ecosystem**
   - Scanner → ReproIn → BIDS
   - Stimuli → ReproStim → BIDS derivatives
   - Events → ReproEvents → BIDS events.tsv
   - Console → Con/noisseur → metadata
   - Monitor → ReproMon → QC feedback
   - Processing → datalad run + duct → BEP028 prov
   - CI/CD → tinuous → build artifacts

6. **From Execution to Archive**
   - YODA structure enables: re-execution, sharing, composition
   - Every step captured, every input/output tracked
   - "Do not look up" preserved at every level

### 6. Key Messages for Act II

- **Automation ≠ Black Box**: SciOps automates capture, not decisions
- **Provenance Everywhere**: From scanner to publication
- **Separation of Concerns**: Data in YODA, views via dashboards
- **Standard Tools**: Don't write custom scripts, compose standard tools
- **Scale Through Structure**: YODA enables HPC/cloud/local equivalence

## Additional Resources

### Papers to Reference
- [BABS paper (2024)](https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00074/119046) - Hoffstaedter et al.
- [FAIRly big framework](https://www.researchgate.net/publication/355214162_FAIRly_big_A_framework_for_computationally_reproducible_processing_of_large-scale_data)
- [BEP028 spec](https://github.com/bids-standard/BEP028_BIDSprov/blob/master/bep028spec.md)

### Tools Documentation
- [Nipoppy tutorial](https://repronim.org/resources/tutorials/nipoppy/)
- [BABS docs](https://pennlinc-babs.readthedocs.io/)
- [BIDS-flux docs](https://bids-flux-docs.readthedocs.io/)
- [Neurobagel digest](https://digest.neurobagel.org/)

## Questions for Tomorrow
1. Should we create a unified "ReproFlow ecosystem diagram" showing all components?
2. How much detail on each tool vs. overview?
3. Should Felix's BABS work be a detailed case study or just mentioned?
4. Do we need a slide specifically on "data vs. dashboard" separation?
5. How to best visualize the SciOps 80/20 principle?
6. Should we have a comparative slide showing BABS vs. Nipoppy vs. BIDS-flux use cases?
