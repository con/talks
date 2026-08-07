# STAMPED Principles: Pragmatic practices for reproducible science


## Presenters

- Cody C.Baker <cody.c.baker.phd@gmail.com>, Center for Open Neuroscience, Psychological and Brain Sciences, Dartmouth College, ORCID [0000-0002-0829-4790](https://orcid.org/0000-0002-0829-4790)
- Austin Macdonald <Austin.S.Macdonald@dartmouth.edu>, Center for Open Neuroscience, Psychological and Brain Sciences, Dartmouth College, ORCID [0000-0002-8124-807X](https://orcid.org/0000-0002-8124-807X)
- John A. Lee <John.A.Lee@dartmouth.edu>, Center for Open Neuroscience, Psychological and Brain Sciences, Dartmouth College, ORCID [0000-0001-5884-4247](https://orcid.org/0000-0001-5884-4247)
- Yaroslav O. Halchenko <Yaroslav.O.Halchenko@dartmouth.edu>, Center for Open Neuroscience, Psychological and Brain Sciences, Dartmouth College, ORCID [0000-0003-3456-2493](https://orcid.org/0000-0003-3456-2493)

## Keywords

Reproducible research - Open science - Provenance

## Abstract

Neuroscience increasingly depends on the interplay of code, data, and computational environments, yet the record of how they were used together is often incomplete, scattered across repositories, wikis, and notebooks, or lost entirely.
This fragmentation undermines rigor, reproducibility, reusability, and efficiency in BRAIN Initiative pipelines that routinely span multiple institutions, archives, and compute platforms.
Existing frameworks such as FAIR and FAIR4RS govern discovery and interoperability of digital objects, but do not specify how research objects should be structured and managed so they can be re-executed, extended, and audited.
The community lacks a shared vocabulary for this operational layer.

Building on the YODA and VAMP traditions from neuroimaging, and on patterns that have independently converged across geophysics, genomics, statistics, and neuroscience over three decades, we formalize seven principles a research object should satisfy: Self-containment, Tracking, Actionability, Modularity, Portability, Ephemerality, and Distributability, collectively STAMPED.
Each spans a spectrum from practical minimum to aspirational ideal, so adoption is non-prescriptive and incremental. 
Formal LinkML schemas, an interactive compliance checklist, and the curated collection of examples are provided as enabling tools to this end.

We demonstrate STAMPED through two major neuroscience pipelines.
OpenNeuroDerivatives reorganized derivative neuroimaging datasets so they exist as independent Ephemeral units that reference raw inputs as subdatasets rather than nesting under them, removing an upward dependency that previously violated Self-containment, Modularity, and Portability.
DANDI Compute, utilizing the Allen Institute for Neural Dynamics electrophysiology pipeline, packages spike-sorting outputs into nested BIDS-derivative units in which each leaf contains the exact code, runtime logs, outputs, and provenance metadata needed to re-execute the analysis, satisfying STAMPED end-to-end.

These adoptions show that STAMPED provides a tool-agnostic, incrementally adoptable vocabulary that lets researchers, reviewers, collaborators, and emerging AI agents evaluate and improve the operational maturity of computational neuroscience.
By making research objects re-executable and inspectable by construction, STAMPED converts reproducibility from an aspiration into a measurable property of everyday neuroscience practice.

## References

Austin Macdonald, Cody Baker, Isaac To, Yaroslav O. Halchenko, “STAMPED principles for reproducible research objects”, 26-May-2026. [Online]. Available: osf.io/preprints/metaarxiv/f3h82_v1. 
Michelle Barker, et al. Introducing the FAIR Principles for research software. Scientific Data, 9(1):622, October 2022. ISSN 2052-4463.
Michael Hanke, et al. YODA: YODA’s organigram on data analysis, 2018. Slides.
Alessio P Buccino, Arjun Sridhar, David Feng, Karel Svoboda, Joshua H Siegle (2026). Efficient and reproducible pipelines for spike sorting large-scale electrophysiology data. eLife, 15:RP110170.
Michael Hanke. What is DataLad and what can it do for you? 2023. https://files.inm7.de/mih/pres/talks/whatisdatalad_2023.html#/
