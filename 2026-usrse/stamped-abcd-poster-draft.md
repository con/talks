# STAMPED in Practice: Reproducing a Scientific Result on ABCD Neuroimaging Study

## Authors

- John A. Lee <John.A.Lee@dartmouth.edu>, Dartmouth College, ORCID 0000-0001-5884-4247
- Austin Macdonald <Austin.S.Macdonald@dartmouth.edu>, Dartmouth College, ORCID 0000-0002-8124-807X
- Yaroslav O. Halchenko <Yaroslav.O.Halchenko@dartmouth.edu>, Dartmouth College, ORCID 0000-0003-3456-2493

## Keywords

STAMPED, reproducibility, research objects, neuroimaging, provenance, AI-assisted science

## Abstract

RSEs routinely encounter computational analyses whose code is available but whose data, parameters, software environments, execution context, and provenance are difficult to reconstruct.
This missing context makes analyses harder to review, maintain, transfer, and extend.
AI-assisted tools can accelerate development, testing, and documentation, but their high-volume and nondeterministic output further complicate these tasks and heightens the need for explicit context and reviewable intermediate states.
STAMPED (https://stamped-principles.org) defines seven properties for organizing these materials as a durable and more useful research object [1].
The framework complements the established FAIR (Findable, Accessible, Interoperable, and Reusable) principles by focusing on the organization and execution of computational research objects [7].

This poster presents our application of STAMPED to an existing analysis presented at OHBM 2025 on age-dependent bias in cortical morphometry tools using Adolescent Brain Cognitive Development (ABCD) Study data (https://abcdstudy.org) [3].
We use the principles to guide improvements to the research object surrounding the analysis [2].
We use AI extensively in development, testing, and documentation, making the reconstruction a practical test of the STAMPED vision for AI-assisted research.

Following a review of the original analysis, we use a coordinated set of tools to improve the research object across the seven properties: DataLad and git-annex for composition and versioned state [4]; Git, DataLad run records, con-duct, and NIDM/PROV for provenance [4,6]; tested BIDS Apps and Pixi tasks for executable interfaces [5]; Apptainer, BABS, and Slurm for portable, fresh execution [5]; and persistent Git/annex siblings with separate access boundaries for distribution [4].
We show how these tools work in concert to make the data, environments, operations, and results more FAIR and STAMPED.

Collectively, the decisions on how to implement the principles provide a worked example of how to use STAMPED to guide choices about research-object boundaries, provenance, execution, validation, and distribution.
The poster reports the practical details of this process: the effort and judgment required, problems encountered, tradeoffs made, evidence produced, and interactions among principles and tools.
It invites RSEs to consider which parts apply to their own shared or domain-specific challenges.
Although we demonstrate the approach through a scientific reproduction, such an effort is more convenient if integrated from the start of the analysis.

The poster reports the practical details of this process: the effort and judgment required, problems encountered, tradeoffs made, evidence produced, and interactions among principles and tools.
In doing so, it shows why these practices are easier to incorporate during study design than to add retrospectively.
It invites RSEs to compare these experiences with their own shared or domain-specific challenges.

```{=latex}
\newpage
```

## Acknowledgments

We thank the authors of the STAMPED principles and the developers and communities behind DataLad, BIDS, BABS, ReproNim, NIDM, Pixi, Apptainer, and `con-duct`.

AI-assisted content disclosure: This submission was prepared with assistance from OpenAI Codex (GPT-5, accessed August 2026).
The system helped synthesize repository evidence and draft the Abstract and Connection to Mission sections.
The authors reviewed the source evidence, edited the text, and remain responsible for all claims.

## References

1. Macdonald A, Baker CC, To I, Halchenko YO; *STAMPED principles for reproducible research objects*; May 2026; [preprint](https://github.com/stamped-principles/stamped-paper)

2. Lee JA; *STAMPED-dl_morphometrics_biases: an ideal-oriented reconstruction of a neuroimaging analysis*; 2026; [repository](https://github.com/STAMPED-dl-morphometrics-biases/STAMPED-dl_morphometrics_biases)

3. Nielson DM, Lee JA, Earl E, Moraczewski D, Pereira F; *Age dependent volume estimation biases in recon-all clinical and recon-any*; OHBM 2025 poster; [doi:10.17605/OSF.IO/P3KNS](https://doi.org/10.17605/OSF.IO/P3KNS)

4. Halchenko YO, et al.; DataLad: distributed system for joint management of code, data, and their relationship; *Journal of Open Source Software*; 2021;6(63):3262; [doi:10.21105/joss.03262](https://doi.org/10.21105/joss.03262)

5. Zhao C, et al.; A reproducible and generalizable software workflow for analysis of large-scale neuroimaging data collections using BIDS Apps; *Imaging Neuroscience*; 2024;2:imag-2-00074; [doi:10.1162/imag_a_00074](https://doi.org/10.1162/imag_a_00074)

6. Center for Open Neuroscience; *con-duct: a lightweight wrapper for monitoring command execution*; RRID:SCR_025436; [repository](https://github.com/con/duct)

7. Wilkinson MD, Dumontier M, Aalbersberg IJ, et al.; *The FAIR Guiding Principles for scientific data management and stewardship*; *Scientific Data*; 2016;3:160018; [doi:10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)

## Connection to Mission, Goals, & Interests of US-RSE Community

Research software engineers help determine whether a computational result is merely produced once or becomes a durable scientific contribution.
STAMPED gives RSEs and researchers a shared vocabulary for the properties that make this difference: coherent research-object boundaries, exact identities, executable procedures, independent components, explicit environments, clean execution, and persistent distribution [1].
This poster grounds that vocabulary in a practical implementation, showing how RSE decisions about provenance, execution, validation, and distribution shape the reviewability and reuse of computational research across domains.

The project also addresses the conference theme, “Advancing Science in the Age of AI,” by shifting attention from what AI can do to what evidence AI-assisted work leaves behind.
The poster invites RSEs to compare how their teams bound context, record decisions, divide work between automation and human reviewers, and evaluate AI-assisted outputs.
These comparisons can help identify shared expectations for reviewing AI-assisted research and inform longer-term community and institutional practices.
