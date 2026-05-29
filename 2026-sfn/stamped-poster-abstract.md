# SfN 2026 (poster abstract)

<!--

Abstract (limit: 2,300 characters, including punctuation but not spaces)

Current: 2011, from 

```python
text = """[copy and paste text below]
"""
chars = [char for char in text if char not in ["\n"," "]]
```

-->

Neuroscience increasingly depends on computational pipelines combining code, data, and software environments.
When these components are scattered across repositories, shared drives, wikis, and lab notebooks, the record of how results were produced becomes incomplete, eroding rigor, reproducibility, and reusability.
FAIR and FAIR4RS guide discovery and reuse of digital objects but do not prescribe how research objects should be structured so others can re-execute and extend them.

We address this operational gap with STAMPED, a vocabulary and evaluation framework for day-to-day practices that make a research object durable.
The principles that embody this acronym are: Self-containment (one complete retrieval unit), Tracking (content-addressed versioning and provenance for all components), Actionability (machine-executable instructions), Modularity (independent, composable units), Portability (no hidden host coupling), Ephemerality (disposable environments per run), and Distributability (persistent retrievability with explicit licenses).
Each principle uses RFC-2119 keywords (MUST/SHOULD/MAY) and spans a spectrum from practical minimum to aspirational ideal, so adoption is non-prescriptive and incremental.
The principles and checklist requirements are published in formal LinkML schemas.
An interactive compliance checklist app and a catalogue of examples are available from `stamped-principles.org`.

We primarily demonstrate the application of these principles to enhancing the scientific rigor and reproducibility of two major neuroscience pipelines: OpenNeuroDerivatives and DANDI Compute.
OpenNeuroDerivatives publishes ~850 fMRIPrep/MRIQC outputs from OpenNeuro as DataLad-tracked BIDS-Derivatives datasets distributed via S3 and GitHub.
DANDI Compute utilizes Allen Institute spike-sorting pipelines in a BIDS-Study layout where each run is a self-contained derivative bundling code, logs, and output.

Mapping these efforts onto STAMPED reveals where each pipeline meets practical minima and where targeted upgrades (pinned container builds, ephemeral re-execution, signed releases) raise operational maturity.
STAMPED gives neuroscientists, reviewers, and AI coding agents a shared language and concrete criteria for building pipelines that others can trust, rerun, and extend.
