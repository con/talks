# SfN 2026 (poster abstract)

<!--

Abstract (limit: 2,300 characters, including punctuation but not spaces)

Current: 1821, from 

```python
text = """[copy and paste text below]
"""
chars = [char for char in text if char not in ["\n"," "]]
```

-->

Neuroscience increasingly depends on computational pipelines combining code, data, and software environments.
When these components are scattered across repositories, drives, wikis, and notebooks, the record of how final results were produced is incomplete, eroding rigor and reproducibility.
FAIR and FAIR4RS guide discovery and reuse of digital objects but do not prescribe how research objects should be structured so others can re-execute and extend them.

We address this operational gap with STAMPED, a vocabulary and evaluation framework for day-to-day practices that make a research object durable.
Building on the YODA and VAMP traditions from neuroimaging, and on patterns that have independently converged across geophysics, genomics, statistics, and neuroimaging over three decades, we formalize seven principles a research object should satisfy: Self-containment, Tracking, Actionability, Modularity, Portability, Ephemerality, and Distributability, collectively STAMPED.
Each uses RFC-2119 keywords (MUST/SHOULD/MAY) and spans a spectrum from practical minimum to aspirational ideal, so adoption is non-prescriptive and incremental.
Formal LinkML schemas, an interactive compliance checklist, and a worked-example catalog are provided as enabling tools to this end.

We demonstrate STAMPED through two major neuroscience pipelines.
OpenNeuroDerivatives publishes ~850 fMRIPrep/MRIQC outputs from OpenNeuro as DataLad-tracked BIDS-Derivatives datasets distributed via S3 and GitHub.
DANDI Compute, utilizing the Allen Institute for Neural Dynamics electrophysiology pipeline, packages spike-sorting outputs into nested BIDS-derivative units in which each leaf contains the exact code, runtime logs, outputs, and provenance metadata needed to re-execute the analysis, satisfying STAMPED end-to-end.
Mapping these onto STAMPED reveals where each pipeline meets practical minima and where targeted upgrades (pinned container builds, ephemeral re-execution, signed releases) raise operational maturity.
STAMPED gives neuroscientists, reviewers, and AI coding agents a shared language and concrete criteria for building pipelines that others can trust, rerun, and extend.
