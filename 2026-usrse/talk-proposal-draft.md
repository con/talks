# Reuse, Compose, Extend, Standardize: Two Decades of RSEing Open (Neuro)Science at CON

## Authors

- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0003-3456-2493
- Cody C. Baker \<TODO@TODO\>, Center for Open Neuroscience, ORCID TODO
- Austin Macdonald \<TODO@TODO\>, Center for Open Neuroscience, ORCID TODO
- Isaac To \<TODO@TODO\>, Center for Open Neuroscience, ORCID TODO
- Vadim Melnik \<TODO@TODO\>, Center for Open Neuroscience, ORCID TODO

## Keywords

reuse, modularity, community standards, federation, reproducibility, distributed data management, neuroinformatics, FAIR, open source, research software engineering

## Abstract

For two decades the team of **Center for Open Neuroscience (CON)** has been building an open, and largely domain-agnostic research-software stack — first for neuroimaging, then for neuroscience broadly, now used across various disciplines.
We did it by, at large, repeating four actions: **Reusing** what already exists; **Composing** smaller modules into environments and systems, rather than ship silo-ed monoliths; **Extending** the upstream projects we depend on; and **Standardizing** common "languages" of data we exchanged.
The "Age of AI" doesn't really change anything of that!
It does often help to expedite those actions, but also in turn benefits back from having such modular and transparent structure of the stack to "divide and conquer" the responsibilities, while avoiding duplication of efforts.

In 15 minutes we walk the layers of that stack and, at each, name one concrete thing the audience can start using **right away**:

- **Reuse — Systems and Methods.** CON's Yaroslav's first move (~2005) was *not* writing code: it was joining Debian GNU/Linux efforts, with then a new random German on the Internets, later long-time collaborator Michael Hanke, packaging FSL and PyEPL under the **pkg-exppsy** project — the precursor to [NeuroDebian](https://neuro.debian.net/). The lesson set the tone for everything since! [PyMVPA](http://www.pymvpa.org/) (2007) followed: an early reproducible-analysis library shipped with a full test suite and buildbot CI when neither was common in scientific Python and Python itself was not common; today we'd contribute upstream to scikit-learn / nilearn instead. The same instinct lives on in [duecredit](https://github.com/duecredit/duecredit) — embedded scholarly-credit tracking that did *not* reinvent CSL rendering: we built on [citeproc-py](https://github.com/citeproc-py/citeproc-py) and stayed on as co-maintainers when it needed care. **Take home:** before your next project, do one upstream-search pass; add `pytest` + a one-file CI workflow to one repo this week.
- **Reuse → Extend — distributing software.** Most of what NeuroDebian pioneered now flows through Debian Med, Debian Science, and conda-forge. A successful bridge dissolves into the commons. **Take home:** file an ITP at Debian Med or a conda-forge feedstock for a tool you currently distribute by URL.
- **Compose — data management on common substrate.** [DataLad](https://www.datalad.org/) layers reproducible versioning and distribution on top of `git` and `git-annex` — tech everyone already knows. The same substrate scales out through [registry.datalad.org](https://registry.datalad.org/), which federates DataLad datasets across institutions and clouds and provides discovery over **petabytes** of data with no recentralizing platform. **Take home:** convert one shared-data folder into a DataLad dataset.
- **Compose — small acquisition & compute units.** [ReproStim](https://github.com/ReproNim/reprostim), [HeuDiConv](https://github.com/nipy/heudiconv), [NeuroConv](https://neuroconv.readthedocs.io/), and the [ReproNim/containers](https://github.com/ReproNim/containers) collection each tackle one slice of acquisition-to-pipeline reproducibility. [con/duct](https://github.com/con/duct) is the leanest of them — execution monitoring built on brainlife's `smon` plus ideas from [ReproMan](https://github.com/ReproNim/reproman), after we learned ReproMan itself was too heavy for everyday use. *Resist monoliths, even your own.* **Take home:** wrap your next pipeline run in `duct` or in a `repronim/containers` recipe.
- **Standardize — data and metadata.** [BIDS](https://bids.neuroimaging.io/) and [NWB](https://www.nwb.org/) make data exchangeable across labs and vendors; [LinkML](https://linkml.io/) and [concepts.datalad.org](https://concepts.datalad.org/) extend the same idea to *metadata*. Pragmatism is fine in the meantime: DataLad's `run` started with an ad-hoc RUNCMD format and is being generalized into [BEP028](https://github.com/bids-standard/bids-specification) provenance and a BIDS prov exporter. *Ship pragmatic now, formalize upstream later.* **Take home:** validate one of your datasets against a community standard.
- **Standardize at scale — federated archives.** [DANDI](https://dandiarchive.org/), [EMBER](https://emberarchive.org/), and [OpenNeuro](https://openneuro.org/) put real data online at population scale, all built on the standards above and discoverable through the same federation pattern. *Federation is what lets a small RSE center reach population scale.*
- **Reuse, in reverse — cross-platform tracking.** [AnnexTube](https://github.com/con/annextube) and `mykrok` pull research outputs back from commercial platforms (YouTube, Google) into the same `git`+`git-annex` substrate. *Your data is yours, even when someone else hosts it.*
- **For HI and AI.** All of the above stays self-contained, well-described, and openly shared — equally legible to **HI** (human investigators) and **AI** agents. The "T" of our [STAMPED](https://stamped-principles.org/) principles (Tracked) extends naturally to AI sessions and AI↔human attribution (a thread we will pick up in a separate BoF), but every layer below is what makes AI-era reproducibility tractable rather than aspirational.

We close with a one-slide **Monday checklist** of five concrete actions distilled from above — none requires neuroscience, all work today.

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
13. *BEP028 — BIDS provenance.* <https://github.com/bids-standard/bids-specification>
14. *LinkML.* <https://linkml.io/>; *DataLad Concepts.* <https://concepts.datalad.org/>
15. *AnnexTube.* <https://github.com/con/annextube> (demo: <https://datasets.datalad.org/repronim/ReproTube/web>); *mykrok.* <https://github.com/mykrok/mykrok> (demo: <https://mykrok.github.io/mykrok/>)
16. *STAMPED principles.* <https://stamped-principles.org/>
17. *con/serve — Digital Research Artifact Archive.* <https://con.github.io/serve/>
18. *Distribits — Technologies for distributed data management (conference & community).* <https://www.distribits.live/>
19. *Center for Open Neuroscience.* <https://centerforopenneuroscience.org/>

## Connection to Mission, Goals, & Interests of US-RSE Community

CON is, by construction, a prototypical US-RSE organization: a small team of full-time research software engineers (five "centroids") whose job is to design, ship, and steward open infrastructure used by domain scientists they do not directly report to. Almost everything we build or co-build — pkg-exppsy/NeuroDebian, PyMVPA, DataLad, duecredit, HeuDiConv, NeuroConv, ReproMan, con/duct, registry.datalad.org, BIDS/NWB/LinkML extensions, the STAMPED principles, and now `con/serve` — was scoped from the outset to be **domain-agnostic**, even when first motivated by neuroimaging. RSEs in genomics, geosciences, HPC, and digital humanities already use them; the talk makes those entry points explicit.

The talk's title verbs are also its takeaways for the US-RSE audience:

- **Reuse.** Whenever an upstream existed or could be grown, we joined it: pkg-exppsy/NeuroDebian → Debian, PyMVPA's intent → scikit-learn / nilearn, duecredit → citeproc-py, DataLad → `git`+`git-annex`, con/duct → brainlife's `smon`. The cheapest reproducible thing is the one you didn't have to build.
- **Compose.** `con/duct` is small on purpose; ReproStim / HeuDiConv / NeuroConv / ReproNim-containers each do one job; `registry.datalad.org` federates rather than recentralizes; BIDS, NWB, and LinkML are independent building blocks that can be picked up à la carte.
- **Extend.** When the commons we depend on needed care, we stayed on as maintainers (citeproc-py), generalized our ad-hoc work upstream (RUNCMD → BEP028 + BIDS prov exporter), and pushed packages into Debian Med / Debian Science / conda-forge so others could re-use them in turn.
- **Standardize.** Common tech (`git`), common data standards (BIDS, NWB), and common metadata standards (LinkML, concepts.datalad.org) so RSEs across fields can read each other's work — and so AI agents can too.

We embody the bridging role US-RSE foregrounds:

- **RSE ↔ engineering industry.** Sustained collaboration with **Kitware** on NWB browse/analyze/visualize tooling — a textbook example of an academic RSE center partnering with a non-academic engineering shop.
- **RSE ↔ domain scientists.** Direct co-development with neuroscience labs at Dartmouth, Stanford (OpenNeuro), Allen Institute (NWB/DANDI), and FZ Jülich.
- **RSE ↔ global RSE community.** We help organize [distribits.live](https://www.distribits.live/), bringing DataLad-adjacent practitioners across continents into one room — a model other RSE sub-communities can copy.

For the US-RSE audience the talk offers (a) a concrete, layer-by-layer tour of reusable infrastructure, (b) a working example of a multi-institutional RSE center sustained for over a decade through NIH P41 and collaborator funding, and (c) a Monday checklist that does not assume anything neuroscience-specific.
