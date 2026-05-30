# Model–View–Controller at the Stack Scale: Standards, Schemas, and Why Open-Science Infrastructure Composes

## Authors

- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0003-3456-2493](https://orcid.org/0000-0003-3456-2493)

## Keywords

MVC, software architecture, hexagonal architecture, FAIR, metadata schemas, LinkML, SHACL, JSON Schema, pydantic, schema-driven UI, reproducibility, standards

```{=latex}
\newpage
```

## Abstract

This talk is the architectural companion to a separately submitted, history-arc proposal on two decades of RSEing open neuroscience at the **Center for Open Neuroscience (CON)**.
Where the history talk asks *how did we get here*, this talk asks *why does it compose*, and *what makes standards load-bearing*?
The answer, sharpened over two decades of building and re-building infrastructure, is that the reusable open-science stack keeps converging on **Model–View–Controller** — not at the level of one application, but at the level of the whole stack.

The **Models** are layered and schema-first.
Dataset-layout models ([BIDS](https://bids.neuroimaging.io/), [YODA](https://github.com/myyoda/poster)) sit on top of per-file formats ([NWB](https://www.nwb.org/), [NGFF / OME-Zarr](https://ngff.openmicroscopy.org/), NIfTI, TSV, Parquet, HDF5, Zarr, DICOM), which in turn rest on the *metadata schemas* that are the heart of this talk.
[LinkML](https://linkml.io/), [pydantic](https://docs.pydantic.dev/), [JSON Schema](https://json-schema.org/), [SHACL](https://www.w3.org/TR/shacl/), and [DataLad Concepts](https://concepts.datalad.org/) provide a single source from which JSON Schema, OWL/SHACL, pydantic classes, and human-readable docs are *generated* rather than maintained in parallel.
Beneath everything sits a content-addressed storage model — `git` + `git-annex` + [DataLad](https://www.datalad.org/) — that any HTTP client can read with no running service required.

A well-defined Model deserves many **Views**, and several of those Views the Model itself materializes.
Archive UIs ([datasets.datalad.org](https://datasets.datalad.org/), [DANDI](https://dandiarchive.org/), [OpenNeuro](https://openneuro.org/), [EMBER](https://emberarchive.org/)), schema-driven editors and websites ([vjsf](https://vjsf.koumoul.com/) powering the DANDI [meditor](https://gui.dandiarchive.org/); [shacl-vue](https://github.com/psychoinformatics-de/shacl-vue) from M. Hanke's group rendering forms — and entire research-group websites — from SHACL shapes, as documented in Hanke *et al.*'s [LinkML metadata-driven workflow](https://datasets.datalad.org/repronim/ReproTube/DataLad/web/#/video/oF98hdaph1k?tab=local&wide=1&t=644&q=model&filter=1)), tabular surfaces ([Datasette](https://datasette.io/), [VisiData](https://www.visidata.org/)), programmatic APIs (PyBIDS, pynwb, `datalad.api`, fsspec, FUSE), and long-form narrative (the DataLad Handbook, per-archive docs, the specs themselves) all derive from the same Model — so when the Model evolves, every View follows for free.

The **Controllers** stay small and single-purpose.
HeuDiConv, NeuroConv, ReproStim, ReproIn, BIDS-Apps, `datalad run` / `containers-run`, `git-annex` special remotes, [`con/duct`](https://github.com/con/duct), and ReproMan each do one slice of the acquisition-to-pipeline work and then compose.
Validation is itself a recursion of the same idea: [`con/validation`](https://github.com/con/validation) harmonizes bids-validator (+ HED), pynwb, zarr, nwbinspector, and OME-Zarr into a single validation-result Model that [dandi-cli](https://github.com/dandi/dandi-cli) emits on every release — `con/validation` is, in effect, the type-checker for your validators.

Most academic data infrastructure does the opposite of all this.
The dominant pattern is a "service-tied UI" — a bespoke LIMS or ELN, a "just a Flask app" portal, a Drupal/WordPress data site, a dashboard that *is* the data — in which the Model is implicit (whatever the ORM happens to expose), the View is welded to the Controller, and the Controller is welded to a running process.
*A bespoke backend dies the day its server stops.*
The design-pattern literature already names this trap: Evans's **Smart UI** anti-pattern ([DDD](https://www.domainlanguage.com/ddd/), 2003), Fowler's [**Anemic Domain Model**](https://martinfowler.com/bliki/AnemicDomainModel.html) and [**Service Layer**](https://martinfowler.com/eaaCatalog/serviceLayer.html), and GoF's **Adapter / Strategy / Façade** (1994).
The cure has a name too — Cockburn's [**Hexagonal Architecture / Ports & Adapters**](https://alistair.cockburn.us/hexagonal-architecture/) (2005), with the domain Model in the centre and the UI, DB, and services as interchangeable Adapters around it — which is exactly MVC at the stack scale.

MVC is one of six overlapping lenses we keep using on the same stack: Architectural (MVC), Procedural ([STAMPED](https://stamped-principles.org/); Macdonald *et al.*, 2026), Sharing (FAIR), Compositional (YODA), Purpose (acquisition / archive / analysis / governance), and Maturity ([SciOps](https://arxiv.org/abs/2401.00077) L1–L5; Johnson *et al.*, 2024).
Each picks out a different property of the same artefacts, and disagreements between lenses are where real design tensions surface.

The punchline is operational: pick any cell — Model, View, or Controller — and swap it; the rest still works.
*That* is why a small RSE centre can reach population scale, why each piece stays small enough to maintain, and why a human or AI agent can pick up the stack cold.
**Take home:** name the M / V / C of your next project before you write it; if any column has one entry, you have a silo.

```{=latex}
\newpage
```

## References

1. *The Brain Imaging Data Structure (BIDS).* Gorgolewski *et al.* Sci. Data 2016. <https://doi.org/10.1038/sdata.2016.44>; <https://bids.neuroimaging.io/>
2. *YODA — modular, look-up-you-must-not data organization.* <https://github.com/myyoda/poster>
3. *Neurodata Without Borders (NWB).* <https://www.nwb.org/>
4. *NGFF / OME-Zarr — next-generation file formats for bioimaging.* <https://ngff.openmicroscopy.org/>
5. *LinkML — a linked-data modelling language.* <https://linkml.io/>
6. *pydantic — data validation using Python type hints.* <https://docs.pydantic.dev/>
7. *JSON Schema.* <https://json-schema.org/>
8. *SHACL — Shapes Constraint Language.* W3C Recommendation. <https://www.w3.org/TR/shacl/>
9. *DataLad Concepts — metadata schema definitions for DataLad-managed datasets.* <https://concepts.datalad.org/>
10. *DANDI Archive.* <https://dandiarchive.org/>; DANDI metadata editor (meditor) at <https://gui.dandiarchive.org/>; *vjsf — Vue JSON Schema Form.* <https://vjsf.koumoul.com/>
11. *OpenNeuro.* Markiewicz *et al.* eLife 2021. <https://elifesciences.org/articles/71774>; <https://openneuro.org/>
12. *EMBER Archive.* <https://emberarchive.org/>
13. *DataLad: distributed system for joint management of code, data, and their relationship.* Halchenko *et al.* JOSS 2021. <https://doi.org/10.21105/joss.03262>; <https://www.datalad.org/>
14. *shacl-vue — SHACL-driven Vue forms and websites.* M. Hanke's group, psychoinformatics-de. <https://github.com/psychoinformatics-de/shacl-vue>; M. Hanke *et al.*, *LinkML metadata-driven workflow*, ReproTube: <https://datasets.datalad.org/repronim/ReproTube/DataLad/web/#/video/oF98hdaph1k?tab=local&wide=1&t=644&q=model&filter=1>
15. *con/validation — a harmonized schema and CLI for validation results across BIDS, NWB, Zarr, OME-Zarr, nwbinspector, HED, etc.* <https://github.com/con/validation>
16. *dandi-cli — DANDI command-line client; harnesses con/validation across format validators.* <https://github.com/dandi/dandi-cli>
17. *Datasette — an open-source multi-tool for exploring and publishing data.* Simon Willison. <https://datasette.io/>
18. *VisiData — a terminal interface for exploring and arranging tabular data.* <https://www.visidata.org/>
19. *STAMPED principles for reproducible research objects.* A. Macdonald, C. C. Baker, I. To, Y. O. Halchenko. 2026. <https://stamped-principles.org/> — **S**elf-containment, **T**racking, **A**ctionability, **M**odularity, **P**ortability, **E**phemerality, **D**istributability.
20. *SciOps: Achieving Productivity and Reliability in Data-Intensive Research.* E. C. Johnson *et al.* (incl. Y. O. Halchenko). 2024. <https://arxiv.org/abs/2401.00077> — five-level Capability Maturity Model for rigorous scientific operations.
21. A. Cockburn. *Hexagonal Architecture (Ports & Adapters).* 2005. <https://alistair.cockburn.us/hexagonal-architecture/>
22. E. Evans. *Domain-Driven Design: Tackling Complexity in the Heart of Software.* Addison-Wesley, 2003 — "Smart UI" anti-pattern (Ch. 4).
23. M. Fowler. *Anemic Domain Model.* <https://martinfowler.com/bliki/AnemicDomainModel.html>; *Service Layer*, *Patterns of Enterprise Application Architecture*. <https://martinfowler.com/eaaCatalog/serviceLayer.html>
24. E. Gamma, R. Helm, R. Johnson, J. Vlissides. *Design Patterns: Elements of Reusable Object-Oriented Software.* Addison-Wesley, 1994 — Adapter, Strategy, Façade.
25. *Center for Open Neuroscience.* <https://centerforopenneuroscience.org/>

```{=latex}
\newpage
```

## Connection to Mission, Goals, & Interests of US-RSE Community

US-RSE audiences are fluent in Model–View–Controller from enterprise contexts, and yet that vocabulary is rarely brought to bear on *research* infrastructure, where the dominant idiom is still a bespoke server-rendered portal whose data evaporates the day the grant ends.
This talk gives RSEs a name for what they already feel — that the View should be derived from the Model, not welded to a backend — and a vocabulary for arguing it in their own organisations.
It is the architectural companion to a separately submitted, history-arc proposal from the same author; together they offer two complementary readings of the same stack, one diachronic and one structural, and either stands alone.

The bridging roles that US-RSE foregrounds are central to the talk.
On the **RSE <-> engineering industry** axis, the talk draws on sustained collaboration with [Kitware](https://www.kitware.com/) on NWB browse/analyze/visualize tooling, close uptake of Koumoul's commercial-OSS `vjsf` for the DANDI metadata editor, and joint design work with [psychoinformatics-de](https://psychoinformatics.de/) (M. Hanke's group) on `shacl-vue` — three textbook industry partnerships built around *schemas*, not services.
On the **RSE <-> domain scientists** axis, BIDS, NWB, LinkML, and DataLad Concepts are co-designed with the labs that produce the data, and the schemas are the explicit contract that lets RSEs and domain scientists negotiate once instead of renegotiating each tool.
On the **RSE <-> global RSE community** axis, Hexagonal Architecture, MVC, and Adapter/Strategy/Façade are names RSE practitioners across domains already share; reading the open-science stack through those names is the cheapest possible technology-transfer from RSE practice to research-data engineering.

The talk closes with a concrete three-action Monday checklist that works in any domain: name your M / V / C; pick the cell you would swap within five years; publish your Model as a real, citable artefact.
