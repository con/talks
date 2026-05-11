# Reuse, Compose, Extend, Standardize, Automate: Two Decades of RSEing Open (Neuro)Science at CON

## Authors

- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0003-3456-2493
- Cody Baker \<cody.c.baker.phd@gmail.com\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-0829-4790
- Austin Macdonald \<austin@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-8124-807X
- Isaac To \<Isaac.C.To@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-4740-0824
- Vadim Melnik \<vmelnik@docsultant.com\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0009-0007-3981-0798

## Keywords

reuse, modularity, community standards, federation, reproducibility, distributed data management, neuroinformatics, FAIR, open source, research software engineering

## Abstract

For two decades the team of the **Center for Open Neuroscience (CON)** has been building an open, largely domain-agnostic research-software stack — first for neuroimaging, then for neuroscience broadly, and now used well beyond.
We did it by repeating five actions: **Reuse** what already exists; **Compose** small modules into environments and systems instead of shipping silo-ed monoliths; **Extend** the upstream projects we depend on; **Standardize** the "languages" of data we exchange; and **Automate** everything we can — because nothing scales without it, and the harness itself is now another thing AI helps us maintain.
These five verbs are not just our private taxonomy: they map directly onto the operational-maturity climb described by the **SciOps Capability Maturity Model** (Johnson *et al.*, [arXiv:2401.00077](https://arxiv.org/abs/2401.00077), 2024) — Reuse/Compose/Extend/Standardize are the practices of *Level 3 (Defined)*, where Johnson *et al.* themselves cite BIDS, NWB, DataLad/git-annex, DANDI, and brainlife.io as canonical exemplars; Automate is *Level 4 (Scalable)* with its "SciOps pipelines"; and AI-in-the-loop is *Level 5 (Optimizing)*, the pinnacle Johnson *et al.* reserve for "closing the discovery loop with the assistance of artificial intelligence".
Architecturally the result is a familiar pattern lifted to the *stack* scale — **Model–View–Controller**: layered, standardized **models** (BIDS / NWB layouts; [LinkML](https://linkml.io/) / [pydantic](https://docs.pydantic.dev/) / [JSON Schema](https://json-schema.org/) / [SHACL](https://www.w3.org/TR/shacl/) for metadata; `git`+`git-annex`+DataLad as a content-addressed storage model); a plurality of interchangeable **views** — including ones the *Model itself materializes*: archive UIs (datasets.datalad.org, DANDI, OpenNeuro), schema-driven editors and websites ([vjsf](https://vjsf.koumoul.com/) for the DANDI meditor; [shacl-vue](https://github.com/psychoinformatics-de/shacl-vue) from M. Hanke's group rendering forms *and entire research-group websites* from SHACL), tabular surfaces ([Datasette](https://datasette.io/), [VisiData](https://www.visidata.org/)), programmatic APIs, and the DataLad Handbook; and small, single-purpose **controllers** (HeuDiConv, NeuroConv, ReproStim, `datalad run`, `con/duct`, BIDS-Apps, `con/validation`).
The "Age of AI" doesn't change any of that — it expedites the actions, and in turn benefits from a modular, transparent stack that lets humans and agents "divide and conquer" without duplicating effort.

In 15 minutes (talk + Q&A) we walk the layers of that stack — drawing on slides distilled from a decade of CON talks at distribits, ReproNim, NIH, OHBM, BIDS/DICOM and NWB/DANDI venues — and at each layer name one concrete thing the audience can start using **right away**:

- **Reuse — joining instead of writing.**
  Yaroslav's first move (~2005) was *not* writing code: it was joining Debian, packaging FSL and PyEPL with Michael Hanke under the **pkg-exppsy** project that became [NeuroDebian](https://neuro.debian.net/).
  [PyMVPA](http://www.pymvpa.org/) (2007) followed — an early reproducible-analysis library shipped with a full test suite and buildbot CI before either was common in scientific Python; today we contribute upstream to scikit-learn / nilearn instead of maintaining a parallel toolbox.
  The same instinct lives on in [duecredit](https://github.com/duecredit/duecredit) (we built on [citeproc-py](https://github.com/citeproc-py/citeproc-py) and stayed on as co-maintainers when it needed care) and in [con/duct](https://github.com/con/duct), built on brainlife's `smon` after we learned [ReproMan](https://github.com/ReproNim/reproman) was too heavy for everyday use.
  *The cheapest reproducible thing is the one you didn't have to build.*
  **Take home:** before your next project, do one upstream-search pass; add `pytest` + a one-file CI workflow to one repo this week.

- **Reuse → Extend — distributing software.**
  Most of what NeuroDebian pioneered now flows through Debian Med, Debian Science, and conda-forge; a successful bridge dissolves into the commons.
  **Take home:** file an ITP at Debian Med, or open a conda-forge feedstock, for a tool you currently distribute by URL.

- **Compose — data management on a common substrate.**
  [DataLad](https://www.datalad.org/) layers reproducible versioning and distribution on top of `git` and `git-annex` — tech everyone already knows — and extends modularly via the [DataLad extensions](https://github.com/datalad/datalad-extension-template) mechanism.
  The same substrate scales out through [registry.datalad.org](https://registry.datalad.org/), which federates DataLad datasets across institutions and clouds and provides discovery over **petabytes** of data with no recentralizing platform.
  **Take home:** convert one shared-data folder into a DataLad dataset.

- **Compose — small acquisition & compute units.**
  [ReproStim](https://github.com/ReproNim/reprostim), [HeuDiConv](https://github.com/nipy/heudiconv), [NeuroConv](https://neuroconv.readthedocs.io/), and the [ReproNim/containers](https://github.com/ReproNim/containers) collection each tackle one slice of acquisition-to-pipeline reproducibility, glued together by [YODA](https://github.com/myyoda/poster) ("look up you must not").
  *Resist monoliths, even your own.*
  **Take home:** wrap your next pipeline run in `duct` or in a `repronim/containers` recipe.

- **Extend — staying upstream.**
  When the commons we depend on need care, we stay: as Debian/Debian-Med maintainers; as citeproc-py co-maintainers; as BIDS Steering Group members.
  We generalize ad-hoc work upstream too: DataLad's `RUNCMD` provenance format is being lifted into [BEP028](https://github.com/bids-standard/bids-specification) (BIDS provenance) plus a BIDS prov exporter.
  *Ship pragmatic now, formalize upstream later.*

- **Standardize — data and metadata.**
  [BIDS](https://bids.neuroimaging.io/) and [NWB](https://www.nwb.org/) make data exchangeable across labs and vendors; [LinkML](https://linkml.io/), [pydantic](https://docs.pydantic.dev/), [JSON Schema](https://json-schema.org/), and [SHACL](https://www.w3.org/TR/shacl/) extend the same idea to *metadata* — and turn the schema into a *generator*: the DANDI [meditor](https://gui.dandiarchive.org/) builds its editor UI from JSON Schema via [vjsf](https://vjsf.koumoul.com/); [`shacl-vue`](https://github.com/psychoinformatics-de/shacl-vue) from M. Hanke's group renders forms *and entire research-group websites* from SHACL shapes (see Hanke et al., *LinkML metadata-driven workflow*, [ReproTube](https://datasets.datalad.org/repronim/ReproTube/DataLad/web/#/video/oF98hdaph1k?tab=local&wide=1&t=644&q=model&filter=1)).
  **Take home:** publish your model as a real artifact (LinkML / pydantic / JSON Schema), not as "what the code happens to accept"; validate one of your datasets against a community standard.

- **Standardize at scale — federated archives.**
  [DANDI](https://dandiarchive.org/), [EMBER](https://emberarchive.org/), and [OpenNeuro](https://openneuro.org/) put real data online at population scale, all built on the standards above and discoverable through the same federation pattern.
  *Federation is what lets a small RSE center reach population scale.*

- **Reuse, in reverse — pulling content back from platforms.**
  [AnnexTube](https://github.com/con/annextube) and [mykrok](https://github.com/mykrok/mykrok) pull research outputs back from commercial platforms (YouTube, Google) into the same `git` + `git-annex` substrate.
  *Your data is yours, even when someone else hosts it.*

- **Automate — without it, nothing of the above scales.**
  Every layer in this talk works only because we automate the boring part: PR-level CI on every DataLad change; daily-tested `git-annex` against DataLad; [con/tinuous](https://github.com/con/tinuous) archiving CI logs and artifacts before they expire; auto-rebuilt [ReproNim/containers](https://github.com/ReproNim/containers); ReproIn / HeuDiConv driving DICOM → BIDS at the scanner; ReproStim auto-recording all stimuli; dandisets auto-mirrored into DataLad on GitHub with webshots and trivial-IO sweeps; con/validation + dandi-cli running the full multi-validator gauntlet on every release.
  In SciOps terms (Johnson *et al.*, 2024), this is *Level 4 (Scalable)* — what the paper calls "SciOps pipelines": semi-automated continuous workflows across experimental design, collection, processing, analysis, and dissemination.
  The cost is real — *those harnesses are themselves code that someone maintains* — and that is the moment AI becomes the most viable way forward: as the **meta-automation** of harness maintenance ([con/skills](https://github.com/con/skills), [con/yolo](https://github.com/con/yolo)), pushing a small RSE center from L4 toward *Level 5 (Optimizing)*.
  **Take home:** automate one repetitive chore (CI matrix, daily smoke test, release script) this week — *and* write down who maintains the automation.

- **For HI and AI.**
  All of the above stays self-contained, well-described, and openly shared — equally legible to **HI** (human investigators) and **AI** agents.
  Our [STAMPED](https://stamped-principles.org/) principles (Self-containment, **T**racking, Actionability, Modularity, Portability, Ephemerality, Distributability — Macdonald, Baker, To & Halchenko, 2026) name exactly the operational properties this requires *per research object*; **SciOps** (Johnson *et al.*, 2024) names the matching team-level maturity ladder.
  The two are complementary: STAMPED describes the *artifact*, SciOps the *operations* around it.
  The AI-coding maturity ladder (companion talk) works only on top of versioned, modular, standardized artifacts — i.e. at least SciOps L3 — and AI is what turns the L4→L5 gap from "requires a consortium" into "feasible for a small RSE center", making AI-era reproducibility tractable rather than aspirational.
  **Different projects need different AI-acceptance policies**, and we show a four-stance spectrum — *Reject* (e.g. `git-annex` upstream contributions — pure HI), *Accept-with-disclosure* (DataLad / DANDI — HI commits with `Co-Authored-By` trailers and `@pytest.mark.ai_generated`), *Spec-driven AI-generated* (AnnexTube, mykrok, con/citations-collector, parts of dandi-cli), *Autonomous* (con/skills + con/yolo for triage/PR-review).
  Common ground across all four (per [ICMJE 2026](https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html)): AI cannot be an author; humans retain full responsibility; AI use must be disclosed in the artifact itself.
  STAMPED *Tracking* is what makes that mechanical rather than aspirational.
  Survey of declared OSS stances: [`melissawm/open-source-ai-contribution-policies`](https://github.com/melissawm/open-source-ai-contribution-policies).

- **Why it composes — MVC at the stack scale.**
  The five verbs above keep producing the same shape: layered standardized **models**, many interchangeable **views**, and small single-purpose **controllers**.
  Pick any cell — Model, View, or Controller — and swap it out; the rest still works.
  *That* is what lets a small RSE center reach population scale, what keeps each piece small enough to maintain, and what lets agents pick up the stack cold.
  **Take home:** name the M / V / C of your next project before you start writing it; if any column has only one entry, you have a silo.

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
14. *LinkML.* <https://linkml.io/>; *pydantic.* <https://docs.pydantic.dev/>; *JSON Schema.* <https://json-schema.org/>; *SHACL.* <https://www.w3.org/TR/shacl/>; *DataLad Concepts.* <https://concepts.datalad.org/>
14a. *Schema-driven UIs.* *vjsf — Vue JSON Schema Form*, <https://vjsf.koumoul.com/> (powering the DANDI metadata editor at <https://gui.dandiarchive.org/>); *shacl-vue*, M. Hanke's group at psychoinformatics-de, <https://github.com/psychoinformatics-de/shacl-vue>; M. Hanke et al., *LinkML metadata-driven workflow*, ReproTube <https://datasets.datalad.org/repronim/ReproTube/DataLad/web/#/video/oF98hdaph1k?tab=local&wide=1&t=644&q=model&filter=1>
15. *AnnexTube.* <https://github.com/con/annextube> (demo: <https://datasets.datalad.org/repronim/ReproTube/web>); *mykrok.* <https://github.com/mykrok/mykrok> (demo: <https://mykrok.github.io/mykrok/>)
16. *STAMPED principles for reproducible research objects.* A. Macdonald, C. C. Baker, I. To, Y. O. Halchenko. 2026. <https://stamped-principles.org/>; sources: <https://github.com/stamped-principles/stamped-paper>. STAMPED = **S**elf-containment, **T**racking, **A**ctionability, **M**odularity, **P**ortability, **E**phemerality, **D**istributability.
16a. *SciOps: Achieving Productivity and Reliability in Data-Intensive Research.* E. C. Johnson, T. T. Nguyen, B. K. Dichter, F. Zappulla, M. Kosma, K. Gunalan, **Y. O. Halchenko**, S. Q. Neufeld, K. Ratan, N. J. Edwards, S. Ressl, S. R. Heilbronner, M. Schirner, P. Ritter, B. Wester, S. Ghosh, M. E. Martone, F. Pestilli, D. Yatsenko. 2024. <https://arxiv.org/abs/2401.00077> — a five-level Capability Maturity Model for rigorous scientific operations; the operational-maturity companion to STAMPED.
16b. *AI use by authors and peer reviewers.* International Committee of Medical Journal Editors (ICMJE) Recommendations, January 2026 update. <https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html> — AI cannot be listed as an author; authors retain full responsibility; AI use must be disclosed.
16c. *Open-source AI contribution policies.* M. Weber Mendonça (curator), community-maintained catalog. <https://github.com/melissawm/open-source-ai-contribution-policies> — surveys declared OSS-project policies under four buckets: Accept / Restrict / Reject / Ongoing. Concrete exemplars (NumPy, Kubernetes, Linux, Django, Zig, Krita, Clojure, QEMU).
17. *con/serve — Digital Research Artifact Archive.* <https://con.github.io/serve/>
18. *Distribits — Technologies for distributed data management (conference & community).* <https://www.distribits.live/>
19. *Center for Open Neuroscience.* <https://centerforopenneuroscience.org/>

## Connection to Mission, Goals, & Interests of US-RSE Community

CON is, by construction, a prototypical US-RSE organization: a small team of full-time research software engineers (five "centroids") whose job is to design, ship, and steward open infrastructure used by domain scientists they do not directly report to.
Almost everything we build or co-build — pkg-exppsy/NeuroDebian, PyMVPA, DataLad, duecredit, HeuDiConv, NeuroConv, ReproMan, con/duct, registry.datalad.org, BIDS/NWB/LinkML extensions, the STAMPED principles, and now `con/serve` — was scoped from the outset to be **domain-agnostic**, even when first motivated by neuroimaging.
RSEs in genomics, geosciences, HPC, and digital humanities already use them; the talk makes those entry points explicit.

The talk's title verbs are also its takeaways for the US-RSE audience:

- **Reuse.**
  Whenever an upstream existed or could be grown, we joined it: pkg-exppsy/NeuroDebian → Debian, PyMVPA's intent → scikit-learn / nilearn, duecredit → citeproc-py, DataLad → `git`+`git-annex`, con/duct → brainlife's `smon`.
  The cheapest reproducible thing is the one you didn't have to build.

- **Compose.**
  `con/duct` is small on purpose; ReproStim / HeuDiConv / NeuroConv / ReproNim-containers each do one job; `registry.datalad.org` federates rather than recentralizes; BIDS, NWB, and LinkML are independent building blocks that can be picked up à la carte.

- **Extend.**
  When the commons we depend on needed care, we stayed on as maintainers (citeproc-py), generalized our ad-hoc work upstream (RUNCMD → BEP028 + BIDS prov exporter), and pushed packages into Debian Med / Debian Science / conda-forge so others could re-use them in turn.

- **Standardize.**
  Common tech (`git`), common data standards (BIDS, NWB), and common metadata standards (LinkML, concepts.datalad.org) so RSEs across fields can read each other's work — and so AI agents can too.

- **Automate.**
  Nothing in this stack scales without it: CI on every PR; daily-tested `git-annex` and DataLad extensions; con/tinuous CI-log archival; auto-rebuilt ReproNim containers; ReproIn/HeuDiConv at the scanner; auto-mirrored dandisets; con/validation + dandi-cli on every release.
  This is SciOps Level 4 ("SciOps pipelines") in practice.
  The harness is itself code we maintain — and the meta-automation step (using AI to maintain *it*) is the most viable way for a small RSE center to approach SciOps Level 5 (Optimizing).

We embody the bridging role US-RSE foregrounds:

- **RSE ↔ engineering industry.**
  Sustained collaboration with **Kitware** on NWB browse/analyze/visualize tooling — a textbook example of an academic RSE center partnering with a non-academic engineering shop.

- **RSE ↔ domain scientists.**
  Direct co-development with neuroscience labs at Dartmouth, Stanford (OpenNeuro), Allen Institute (NWB/DANDI), and FZ Jülich.

- **RSE ↔ global RSE community.**
  We help organize [distribits.live](https://www.distribits.live/), bringing DataLad-adjacent practitioners across continents into one room — a model other RSE sub-communities can copy.

For the US-RSE audience the talk offers (a) a concrete, layer-by-layer tour of reusable infrastructure, (b) a working example of a multi-institutional RSE center sustained for over a decade through NIH P41 and collaborator funding, and (c) a Monday checklist that does not assume anything neuroscience-specific.
