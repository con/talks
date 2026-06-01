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
Five actions — **Reuse**, **Compose**, **Extend**, **Standardize**, and **Automate** — carried us here, and we expect them to keep us productive as AI agents enter the workflow.

The story traces back to 2000, when [Yaroslav](https://centerforopenneuroscience.org/whoweare#yaroslav_o_halchenko_) joined the lab of a Debian developer ([Barak A. Pearlmutter](https://www.bcl.hamilton.ie/~barak/)) as a graduate student.
That immersion introduced open-source practices for **reuse** of existing tools while developing new neurophysiological analysis methods.
Debian's compositional pattern instilled the discipline of integrating reused components to **compose** powerful systems, while sharing the maintenance burden with the broader community.
Those practices encouraged **extending** the distribution with our own packages and contributing to upstream projects we depended on daily (e.g., [Fail2Ban](https://github.com/fail2ban/fail2ban)).
Joining forces with like-minded but geographically distant collaborators, notably [Michael Hanke](https://www.psychoinformatics.de/persons/michael-hanke/), elevated all three actions to the next level.
In 2005 we formed a team to package FSL and PyEPL under the **pkg-exppsy** project, which became [NeuroDebian](https://neuro.debian.net/), used by thousands to this day.
Recognizing the potential of machine learning for neural data, and the absence of good practice in then-existing implementations, we initiated [PyMVPA](http://www.pymvpa.org/) (2007): an early reproducible-analysis library with a full test suite, CI, and tutorials before any of that was common in scientific Python.

To close the same compositional gap in scientific *data* management, [DataLad](https://www.datalad.org/) (2013) was created to provide data versioning and distribution on top of `git` and [`git-annex`](https://git-annex.branchable.com/).
Today, [datasets.datalad.org](https://datasets.datalad.org) aggregates thousands of datasets from many sources. National archives we lead or participate in ([DANDI](https://dandiarchive.org/), [EMBER](https://emberarchive.org/), and [OpenNeuro](https://openneuro.org/)) are built on shared standards and accessible via DataLad.
[registry.datalad.org](https://registry.datalad.org/) then federates DataLad datasets across institutions, clouds, and projects, providing discovery of **petabytes** of data without any central platform.
In effect, `git` and `git-annex` have become our **standard** for managing *all* digital research artifacts — code, data, containers — across these venues.
Seeing the need to **standardize** common "data languages" in neuroscience, we co-founded or joined community efforts on [BIDS](https://bids.neuroimaging.io/), [NWB](https://www.nwb.org/), and [NGFF / OME-Zarr](https://ngff.openmicroscopy.org/) — serving on their advisory boards and bridging to industry standards such as DICOM.

Given our team size, scaling to this many projects is impossible without **automation**.
Since the early days we practice software- and data-level unit and integration testing, performance benchmarking, CI/CD with [con/tinuous](https://github.com/con/tinuous) archiving logs and artifacts across PRs and builds, daily testing of `git-annex` and DataLad extensions, auto-rebuilt ReproNim containers, automated MRI/stimuli/aux data acquisition, and auto-mirrored dandisets, among many others.

The "Age of AI" doesn't make this list optional — it *amplifies* every entry.
AI lets teams move faster than ever while generating an explosion of divergent approaches, drifting styles, and under-reviewed output.
**Reuse** seemingly becomes unnecessary when an agent confidently writes new code instead of finding a robust upstream;
**Compose** appears effortless when AI generates ad-hoc adapters between misaligned components.
Such practices are a recipe for fragile systems.
**Standardize** remains the main protection against cacophonies of APIs and data formats, and **Automate**d testing and review the only viable defense at agent-rate output.

AI makes going it alone tempting, you can move fast, you have all the flexibility to do whatever you want, and you have fewer dependencies and supply-chain risks.
But even simple code bloats over time to cover all possible cases, security requires many eyes and iterations to harden, collaboration is still more efficient in the long term.
The five actions pay off most when invested in *common* projects, *shared* standards, and *joint* maintainership — a hundred isolated agentic projects reinventing the same infrastructure is far worse than one collaborative ecosystem.

This talk walks through ongoing CON projects through those five lenses — alongside our AI adoption — to show how a small RSE team can scale productively through the "Age of AI" in service of our long-standing call:

```{=latex}
\begin{flushright}
\textit{``Together we can make neuroscience a better science!''}
\end{flushright}
```

```{=html}
<p style="text-align: right; font-style: italic;">"Together we can make neuroscience a better science!"</p>
```

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

CON is, by construction, a prototypical US-RSE organization: a small team of full- and part-time research software engineers ("centroids") and contractors who design, ship, and steward open infrastructure for domain scientists they do not directly report to.
Much of the portfolio named in the abstract was scoped to be **domain-agnostic** from the outset and is already used by RSEs in genomics, geosciences, HPC, and digital humanities; the talk makes those entry points explicit.

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
