# STAMPED in Practice: Reproducing a Scientific Result on ABCD Neuroimaging Study

## Authors

- John A. Lee <John.A.Lee@dartmouth.edu>, Dartmouth College, ORCID 0000-0001-5884-4247
- Austin Macdonald <Austin.S.Macdonald@dartmouth.edu>, Dartmouth College, ORCID 0000-0002-8124-807X
- Yaroslav O. Halchenko <Yaroslav.O.Halchenko@dartmouth.edu>, Dartmouth College, ORCID 0000-0003-3456-2493

## Keywords

STAMPED, reproducibility, research objects, neuroimaging, provenance, AI-assisted science

## Abstract

The scientific value of a computational finding depends on whether others can understand how it was produced, inspect its evidence, and re-execute or extend the analysis.
Code alone is insufficient: data, parameters, software environments, execution context, and provenance must also be identifiable and recoverable.
AI-assisted tools can reduce software-development effort, but their high-volume, nondeterministic output makes explicit context, provenance, and reviewable intermediate states increasingly important.
STAMPED (<https://stamped-principles.org>) defines seven properties for organizing these materials as a durable research object.

We used STAMPED to assess an existing analysis presented at OHBM 2025 on age-dependent bias in cortical morphometry tools using Adolescent Brain Cognitive Development (ABCD) Study data (https://abcdstudy.org).
We reworked the analysis to more closely align with the ideals laid out in the STAMPED principles.
We made extensive use of AI in the development, testing, and documentation of the work, helping to assess how such practices interact with the application of the principles.

Given an analysis pipeline and a chosen set of tools, we created a research object more closely aligned with the principles:

- **Self-contained:** Everything needed to understand and run the study was available within one research-object boundary, eliminating the need to look elsewhere for context (supported by DataLad and git-annex).
- **Tracked:** Results were linked to their inputs, transformations, execution context, and scientific meaning so their provenance could be inspected (recorded with Git, DataLad run records, `con-duct`, and NIDM/PROV).
- **Actionable:** Procedures and expected outputs were encoded as executable, testable operations instead of instructions requiring interpretation (implemented through BIDS, tested BIDS Apps, Pixi tasks, manifests, validation commands, and Datalad run records).
- **Modular:** Data, environments, operations, and results retained distinct identities so components could be reviewed, updated, and reused independently (organized as versioned DataLad subdatasets).
- **Portable:** Software dependencies and interfaces were separated from site-specific configuration so execution could move across systems (supported by locked Pixi environments, exact Apptainer images, and standard interfaces).
- **Ephemeral:** Fresh, disposable execution tested whether results followed from the declared research object rather than accumulated machine state (tested with BABS, Slurm, and clean-installation replay with `datalad rerun` and alike).
- **Distributable:** Exact permitted research states remained persistently retrievable under explicit licensing and access rules, supporting reuse while protecting controlled data (implemented through Git/annex siblings and separate access boundaries).

Collectively, the decisions on how to implement the principles provide a worked example of how to use STAMPED to guide choices about research-object boundaries, provenance, execution, validation, and distribution.
The worked example exposes the effort, evidence, and tradeoffs involved, giving RSEs an implementation pattern they can adapt across domains.
Although we demonstrate the approach through a scientific reproduction, such an effort is more convenient if integrated from the start of the analysis.


## Acknowledgments

We thank the authors of the STAMPED principles and the developers and communities behind DataLad, BIDS, BABS, ReproNim, NIDM, Pixi, Apptainer, and `con-duct`.

AI-assisted content disclosure: This submission was prepared with assistance from OpenAI Codex (GPT-5, accessed August 2026).
The system helped synthesize repository evidence and draft the Abstract and Connection to Mission sections.
The authors reviewed the source evidence, edited the text, and remain responsible for all claims.

## References

1. Macdonald A, Baker CC, To I, Halchenko YO.
*STAMPED principles for reproducible research objects*.
May 2026.
<https://github.com/stamped-principles/stamped-paper>
2. Lee JA.
*STAMPED-dl_morphometrics_biases: an ideal-oriented reconstruction of a neuroimaging analysis*.
2026.
<https://github.com/STAMPED-dl-morphometrics-biases/STAMPED-dl_morphometrics_biases>
3. Nielson DM, Lee JA, Earl E, Moraczewski D, Pereira F. *Age dependent volume estimation biases in recon-all clinical and recon-any*.
OHBM 2025 poster.
<https://doi.org/10.17605/OSF.IO/P3KNS>
4. Halchenko YO, et al. DataLad: distributed system for joint management of code, data, and their relationship.
*Journal of Open Source Software*.
2021;6(63):3262.
<https://doi.org/10.21105/joss.03262>
5. Zhao C, et al. A reproducible and generalizable software workflow for analysis of large-scale neuroimaging data collections using BIDS Apps.
*Imaging Neuroscience*. 2024;2:imag-2-00074.
<https://doi.org/10.1162/imag_a_00074>
6. Center for Open Neuroscience.
*con-duct: a lightweight wrapper for monitoring command execution*.
RRID:SCR_025436.
<https://github.com/con/duct>

## Connection to Mission, Goals, & Interests of US-RSE Community

Research software engineers help determine whether a computational result is merely produced once or becomes a durable scientific contribution.
STAMPED gives RSEs and researchers a shared vocabulary for the properties that make this difference: coherent research-object boundaries, exact identities, executable procedures, independent components, explicit environments, clean execution, and persistent distribution.
This case study translates those properties into a concrete implementation and shows how they can be designed into an analysis from the beginning rather than added after publication.

The project also addresses the conference theme, "Advancing Science in the Age of AI," by shifting attention from what AI can do to what evidence AI-assisted work leaves behind.
Using STAMPED as a shared point of reference, the poster invites RSEs to compare how their teams record decisions, divide responsibility, and evaluate AI-assisted work, and to consider how those expectations could become community review criteria and institutional practice across research domains.
