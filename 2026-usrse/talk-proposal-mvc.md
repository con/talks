# Model–View–Controller at the Stack Scale: Standards, Schemas, and Why Open-Science Infrastructure Composes

## Authors

- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0003-3456-2493](https://orcid.org/0000-0003-3456-2493)

## Keywords

MVC, software architecture, hexagonal architecture, FAIR, metadata schemas, LinkML, SHACL, JSON Schema, pydantic, schema-driven UI, reproducibility, standards

## Abstract

This talk is the architectural companion to a separately submitted, history-arc proposal on two decades of RSEing open neuroscience at the **Center for Open Neuroscience (CON)**.
Where the history talk asks *how did we get here*, this talk asks *why does it compose*, and *what makes standards load-bearing*?
The answer, sharpened over two decades, is that the reusable open-science stack keeps converging on **Model–View–Controller** — not at the level of one app, but at the level of the whole stack.

**Models — layered, standardized, schema-first.**
Dataset-layout models ([BIDS](https://bids.neuroimaging.io/), [YODA](https://github.com/myyoda/poster)) sit on top of per-file formats ([NWB](https://www.nwb.org/), [NGFF / OME-Zarr](https://ngff.openmicroscopy.org/), NIfTI, TSV, Parquet, HDF5, Zarr, DICOM), which sit on top of *metadata schemas* — the heart of this talk: [LinkML](https://linkml.io/), [pydantic](https://docs.pydantic.dev/), [JSON Schema](https://json-schema.org/), [SHACL](https://www.w3.org/TR/shacl/), and [DataLad Concepts](https://concepts.datalad.org/) define one source from which JSON Schema, OWL/SHACL, pydantic classes, and human-readable docs are *generated*.
Underneath everything sits a content-addressed storage model — `git` + `git-annex` + [DataLad](https://www.datalad.org/) — that any HTTP client can read with no service required.

**Views — including ones the Model materializes.**
Archive UIs ([datasets.datalad.org](https://datasets.datalad.org/), [DANDI](https://dandiarchive.org/), [OpenNeuro](https://openneuro.org/), [EMBER](https://emberarchive.org/)), schema-driven editors and websites ([vjsf](https://vjsf.koumoul.com/) powering the DANDI [meditor](https://gui.dandiarchive.org/); [shacl-vue](https://github.com/psychoinformatics-de/shacl-vue) from M. Hanke's group rendering forms *and entire research-group websites* from SHACL shapes — see Hanke *et al.*, [LinkML metadata-driven workflow](https://datasets.datalad.org/repronim/ReproTube/DataLad/web/#/video/oF98hdaph1k?tab=local&wide=1&t=644&q=model&filter=1)), tabular surfaces ([Datasette](https://datasette.io/), [VisiData](https://www.visidata.org/)), programmatic APIs (PyBIDS, pynwb, `datalad.api`, fsspec, FUSE), and long-form narrative (the DataLad Handbook, per-archive docs, the specs themselves) — all derive from the same Model.
*The Model deserves many Views.*

**Controllers — small, single-purpose.**
HeuDiConv, NeuroConv, ReproStim, ReproIn, BIDS-Apps, `datalad run` / `containers-run`, `git-annex` special remotes, [`con/duct`](https://github.com/con/duct), ReproMan.
Validation is itself a recursion: [`con/validation`](https://github.com/con/validation) harmonizes bids-validator (+ HED), pynwb, zarr, nwbinspector, and OME-Zarr into a single validation-result Model that [dandi-cli](https://github.com/dandi/dandi-cli) emits on every release.
*`con/validation` is the type-checker for your validators.*

**The anti-pattern contrast.**
Most academic data infrastructure is a "service-tied UI": a bespoke LIMS / ELN, a "just a Flask app" portal, a Drupal/WordPress data site, a dashboard that *is* the data.
The Model is implicit (whatever the ORM happens to expose); the View is welded to the Controller; the Controller is welded to a running process.
*A bespoke backend dies the day its server stops.*
The design-pattern literature already names this: Evans's **Smart UI** anti-pattern ([DDD](https://www.domainlanguage.com/ddd/), 2003), Fowler's [**Anemic Domain Model**](https://martinfowler.com/bliki/AnemicDomainModel.html) and [**Service Layer**](https://martinfowler.com/eaaCatalog/serviceLayer.html), and GoF's **Adapter / Strategy / Façade** (1994).
The cure is Cockburn's [**Hexagonal Architecture / Ports & Adapters**](https://alistair.cockburn.us/hexagonal-architecture/) (2005) — the domain Model in the centre, UI, DB, and services as interchangeable Adapters around it.
That is MVC at the stack scale.

**Many lenses, one stack.**
MVC is one of six overlapping lenses we keep using — Architectural (MVC), Procedural ([STAMPED](https://stamped-principles.org/); Macdonald *et al.*, 2026), Sharing (FAIR), Compositional (YODA), Purpose (acquisition / archive / analysis / governance), and Maturity ([SciOps](https://arxiv.org/abs/2401.00077) L1–L5; Johnson *et al.*, 2024).
Each picks out a different property of the same artefacts; disagreements between lenses surface real design tensions.

**Punchline.**
Pick any cell — Model, View, or Controller — and swap it; the rest still works.
*That* is why a small RSE centre can reach population scale, why each piece stays small enough to maintain, and why a human or AI agent can pick up the stack cold.
**Take home:** name the M / V / C of your next project before you write it; if any column has one entry, you have a silo.

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

## Connection to Mission, Goals, & Interests of US-RSE Community

US-RSE audiences are fluent in Model–View–Controller from enterprise contexts — and yet that vocabulary is rarely brought to bear on *research* infrastructure, where the dominant idiom is still a bespoke server-rendered portal whose data evaporates the day the grant ends.
This talk gives RSEs a name for what they already feel: that "the View should be derived from the Model, not welded to a backend".
It is the architectural companion to a separately submitted history-arc proposal from the same author; together they offer two complementary views of the same stack — one diachronic, one structural.

The bridging roles US-RSE foregrounds are central to the talk:

- **RSE <-> engineering industry.**
  Sustained collaboration with [Kitware](https://www.kitware.com/) on NWB browse/analyze/visualize tooling; close uptake of Koumoul's `vjsf` (commercial-OSS) for the DANDI metadata editor; and joint design work with [psychoinformatics-de](https://psychoinformatics.de/) (M. Hanke's group) on `shacl-vue`.
  All three are textbook RSE-<->-industry partnerships built around *schemas*, not services.

- **RSE <-> domain scientists.**
  BIDS, NWB, LinkML, and DataLad Concepts are co-designed with the labs that produce the data; the schemas are the contract that lets RSEs and domain scientists negotiate without renegotiating each tool.

- **RSE <-> global RSE community.**
  Hexagonal Architecture, MVC, Adapter/Strategy/Façade — these are the names RSE practitioners across domains already share.
  Reading the open-science stack through those names is the cheapest possible technology-transfer from RSE to research-data engineering.

The talk closes with a concrete three-action Monday checklist that works in any domain: name your M / V / C; pick the cell you would swap within five years; publish your Model as a real artefact.

