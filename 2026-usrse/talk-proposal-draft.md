# Reuse, Compose, Extend, Standardize, Automate: Two Decades of RSEing Open (Neuro)Science at CON

## Authors

- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0003-3456-2493](https://orcid.org/0000-0003-3456-2493)
- Cody Baker \<cody.c.baker.phd@gmail.com\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0002-0829-4790](https://orcid.org/0000-0002-0829-4790)
- Austin Macdonald \<austin@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0002-8124-807X](https://orcid.org/0000-0002-8124-807X)
- Isaac To \<Isaac.C.To@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0002-4740-0824](https://orcid.org/0000-0002-4740-0824)
- Vadim Melnik \<vmelnik@docsultant.com\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0009-0007-3981-0798](https://orcid.org/0009-0007-3981-0798)

## Keywords

reuse, modularity, community standards, federation, reproducibility, distributed data management, neuroinformatics, FAIR, open source

```{=latex}
\newpage
```

## Abstract

For two decades the team of the **Center for Open Neuroscience (CON)** has been building an open, largely domain-agnostic research-software stack — first for neuroimaging, then for neuroscience broadly, and now used well beyond.
The story traces back to 2000, when Yaroslav joined the lab of a Debian developer ([Barak A. Pearlmutter](https://www.bcl.hamilton.ie/~barak/)) as a graduate student.
That immersion introduced open-source practices for **reuse** of existing tools while developing new neurophysiological analysis methods.
Debian's compositional pattern instilled the discipline of integrating reused components to **compose** powerful systems, while sharing the maintenance burden with the broader community.

Those practices encouraged **extending** the distribution with our own packages and contributing to upstream projects we depended on daily ([Fail2Ban](https://github.com/fail2ban/fail2ban), [PyEPL](https://pyepl.sourceforge.net/), and others).
Joining forces with like-minded but geographically distant collaborators — notably Michael Hanke — elevated all three actions to the next level.
In 2005 we formed a team to package FSL and PyEPL under the **pkg-exppsy** project, which became [NeuroDebian](https://neuro.debian.net/), used by thousands to this day.
Recognizing the potential of machine learning for neural data — and the absence of good practice in then-existing implementations — we initiated [PyMVPA](http://www.pymvpa.org/) (2007): an early reproducible-analysis library shipped with a test suite, CI, documentation, tutorials, and a "traveling school" before any of that was common in scientific Python.
We contributed upstream to scikit-learn and ultimately sunsetted PyMVPA in favor of newer libraries.

We soon saw the same compositional gap in scientific *data* management.
[DataLad](https://www.datalad.org/) (2013) was created to provide data versioning and distribution on top of `git` and `git-annex`, extendable via the [DataLad extensions](https://github.com/datalad/datalad-extension-template).
The distributed nature of git unlocked a wide range of data-management workflows for science while reusing the `git-annex` data-logistics layer.
Today, [datasets.datalad.org](https://datasets.datalad.org) aggregates thousands of datasets from many sources, and we lead or contribute to national archives — [DANDI](https://dandiarchive.org/), [EMBER](https://emberarchive.org/), and [OpenNeuro](https://openneuro.org/) — all built on shared standards and accessible via DataLad.
Then [registry.datalad.org](https://registry.datalad.org/) federates DataLad datasets across institutions, clouds, and projects, providing discovery of **petabytes** of data without central platform. `git` and `git-annex` have effectively become our **standard** mechanism for working with *all* digital research artifacts — code, data, containers — across these venues.
Seeing the need for common "data languages" in neuroscience, we co-founded or joined community efforts on [BIDS](https://bids.neuroimaging.io/), [NWB](https://www.nwb.org/), and [NGFF / OME-Zarr](https://ngff.openmicroscopy.org/) to make data exchangeable across labs and vendors, serving on Steering and Technical advisory boards and bridging to industry standards such as DICOM.

The compositional pattern permeates our project portfolio.
For data acquisition we composed a toolbelt of small utilities — [ReproStim](https://github.com/ReproNim/reprostim), [HeuDiConv](https://github.com/nipy/heudiconv), [NeuroConv](https://neuroconv.readthedocs.io/), [con/nwb2bids](https://github.com/con/nwb2bids), and [ReproNim/containers](https://github.com/ReproNim/containers) — each tackling one slice of acquisition-to-pipeline reproducibility, glued together by [YODA](https://github.com/myyoda/poster) ("look up you must not"), which generalized into the [STAMPED Principles](https://stamped-principles.org/). We keep building generic small tools while reusing — and heavily contributing to, or taking over maintainership of upstream projects: e.g. [duecredit](https://github.com/duecredit/duecredit) using [citeproc-py](https://github.com/citeproc-py/citeproc-py), which we now co-maintain, and [con/duct](https://github.com/con/duct) based-on brainlife's `smon` after learning [ReproMan](https://github.com/ReproNim/reproman) was too heavy for everyday use.
Every cycle returns to standardization efforts that improve reuse and cross-pollination across projects.

Given our team size, scaling to this many projects is impossible without **automation**.
Since the early days we practice software- and data-level unit and integration testing, performance benchmarking, CI/CD with [con/tinuous](https://github.com/con/tinuous) archiving logs and artifacts across PRs and builds, daily testing of `git-annex` and DataLad extensions, auto-rebuilt ReproNim containers, automated MRI/stimuli/aux data acquisition, and auto-mirrored dandisets — among many others.

All of these actions, from reuse to automation, map directly onto the operational-maturity climb of the **SciOps Capability Maturity Model** ([Johnson *et al.*, 2024](https://arxiv.org/abs/2401.00077)), which we actively advocate.
They lift teams beyond *Level 3* — where Johnson *et al.* themselves cite BIDS, NWB, DataLad / git-annex, DANDI, and brainlife.io as canonical exemplars — through *Level 4 (Scalable)* SciOps pipelines and toward *Level 5 (Optimizing)*, the AI-in-the-loop pinnacle.

In 15 minutes (talk + Q&A) we draw on two decades of CON operation to present the projects and products that together stand behind our long-standing slogan:

*"Together we can make neuroscience a better science!"*

```{=latex}
\newpage
```

## References

1. *DataLad: distributed system for joint management of code, data, and their relationship.* Halchenko et al. JOSS 2021. <https://doi.org/10.21105/joss.03262>
2. *The Brain Imaging Data Structure (BIDS).* Gorgolewski et al. Sci. Data 2016. <https://doi.org/10.1038/sdata.2016.44>
3. *Neurodata Without Borders (NWB).* <https://www.nwb.org/>
4. *DANDI Archive.* <https://dandiarchive.org/>
5. *OpenNeuro: An open resource for sharing of neuroimaging data.* Markiewicz et al. eLife 2021. <https://elifesciences.org/articles/71774>
6. *EMBER Archive.* <https://emberarchive.org/>
7. *ReproNim: A center for reproducible neuroimaging computation.* <https://www.repronim.org/> (NIH NIBIB P41 EB019936)
8. *PyMVPA.* <http://www.pymvpa.org/>
9. *NeuroDebian.* Halchenko & Hanke. Front. Neuroinform. 2012. <https://doi.org/10.3389/fninf.2012.00022>
10. *duecredit — automated scholarly credit tracking.* <https://github.com/duecredit/duecredit>; *citeproc-py.* <https://github.com/citeproc-py/citeproc-py>
11. *con/duct — small process-execution monitor.* <https://github.com/con/duct>
12. *DataLad Registry.* <https://registry.datalad.org/>
13. *con/tinuous — CI-log and artifact archival across GitHub Actions / Travis / AppVeyor.* <https://github.com/con/tinuous>
14. *YODA principles.* Hanke, Meyer, Visconti di Oleggio Castello, Poldrack & Halchenko. 2018 OHBM poster. <https://github.com/myyoda/poster>
15. *NGFF / OME-Zarr — Next-generation file format for bioimaging.* <https://ngff.openmicroscopy.org/>
16. *Reproducible acquisition toolbelt:* [ReproIn](https://reproin.repronim.org/); [HeuDiConv](https://heudiconv.repronim.org/); [NeuroConv](https://neuroconv.readthedocs.io/); [ReproStim](https://github.com/ReproNim/reprostim); [ReproNim/containers](https://github.com/ReproNim/containers); [con/nwb2bids](https://github.com/con/nwb2bids).
17. *STAMPED principles for reproducible research objects.* A. Macdonald, C. C. Baker, I. To, Y. O. Halchenko. 2026. <https://stamped-principles.org/>; sources: <https://github.com/stamped-principles/stamped-paper>. STAMPED = **S**elf-containment, **T**racking, **A**ctionability, **M**odularity, **P**ortability, **E**phemerality, **D**istributability.
18. *SciOps: Achieving Productivity and Reliability in Data-Intensive Research.* E. C. Johnson, T. T. Nguyen, B. K. Dichter, F. Zappulla, M. Kosma, K. Gunalan, **Y. O. Halchenko**, S. Q. Neufeld, K. Ratan, N. J. Edwards, S. Ressl, S. R. Heilbronner, M. Schirner, P. Ritter, B. Wester, S. Ghosh, M. E. Martone, F. Pestilli, D. Yatsenko. 2024. <https://arxiv.org/abs/2401.00077> — a five-level Capability Maturity Model for rigorous scientific operations.
19. *Distribits — Technologies for distributed data management (conference & community).* <https://www.distribits.live/>
20. *Center for Open Neuroscience.* <https://centerforopenneuroscience.org/>

```{=latex}
\newpage
```

## Connection to Mission, Goals, & Interests of US-RSE Community

CON is, by construction, a prototypical US-RSE organization: a small team of full- and part-time research software engineers ("centroids") and contractors whose job is to design, ship, and steward open infrastructure used by domain scientists they do not directly report to.
Many of the projects we build or co-maintain — DataLad, duecredit, con/duct, ReproMan, registry.datalad.org, the STAMPED principles, and others — were scoped from the outset to be **domain-agnostic**, even when first motivated by neural-science use cases.
RSEs in genomics, geosciences, HPC, and digital humanities already use them; the talk makes those entry points explicit.

The talk's title verbs are also its takeaways for the US-RSE audience across scientific domains.

- *The most efficient and reproducible thing is the one you didn't have to build yourself.*
- *Federation lets small projects reach national and international scales of reuse.*
- *Resist monoliths, even your own.*

We embody the bridging role US-RSE foregrounds:

- **RSE -- engineering industry.**
  Sustained collaboration with **Kitware** on Neurodata Without Borders (NWB) browsing, analysis, and visualization tooling — a textbook example of an academic RSE center partnering with a non-academic engineering shop.
  Participation in industry-standard working groups (DICOM) further aligns our academic standardization efforts with industrial ones.

- **RSE -- domain scientists.**
  Direct co-development with neuroscience labs at Dartmouth, Stanford (OpenNeuro), McGill (Neurobagel, Nipoppy), MIT McGovern Institute (DANDI, ReproNim), Allen Institute (AIND pipelines / NWB / DANDI), and FZ Jülich INM-7.

- **RSE -- global RSE community.**
  We help organize [distribits.live](https://www.distribits.live/), bringing DataLad-adjacent practitioners across continents into one room — a model other RSE sub-communities can copy.

For the US-RSE audience the talk offers

- (a) a concrete tour of reusable and modular infrastructure,
- (b) a working example of a multi-institutional RSE center sustained for over a decade through NSF, NIH, and collaborator funding, and
- (c) a toolbelt of dedicated utilities whose adoption — directly or through AI-agentic interfaces — can boost the audience's efficiency and reproducibility.
