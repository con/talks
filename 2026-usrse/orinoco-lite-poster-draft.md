# Beyond the Lab Website: Reusing Structured Research Metadata Across Lab Operations

## Presenters

- John Lee, [John.A.Lee@dartmouth.edu](mailto:John.A.Lee@dartmouth.edu), Center for Open Neuroscience, Psychological and Brain Sciences, Dartmouth College, ORCID [0000-0001-5884-4247](https://orcid.org/0000-0001-5884-4247)
- Isaac To, [Isaac.C.To@dartmouth.edu](mailto:Isaac.C.To@dartmouth.edu), Center for Open Neuroscience, Psychological and Brain Sciences, Dartmouth College, ORCID [0000-0002-4740-0824](https://orcid.org/0000-0002-4740-0824)
- Yaroslav O. Halchenko, [yaroslav.o.halchenko@dartmouth.edu](mailto:yaroslav.o.halchenko@dartmouth.edu), Center for Open Neuroscience, Psychological and Brain Sciences, Dartmouth College, ORCID [0000-0003-3456-2493](https://orcid.org/0000-0003-3456-2493)

## Keywords

research information management; metadata reuse; knowledge graphs; semantic interoperability; AI-assisted research

```{=latex}
\newpage
```

## Abstract

We compare two ways to deploy [ORINOCO](https://hub.psychoinformatics.de/orinoco/), a system for collaboratively managing and reusing structured research metadata.
One way uses dedicated services to store records and review changes; the other uses a GitHub repository and pull requests.

Research groups repeatedly need facts about people, projects, and publications for CVs, grant applications, and yearly reporting.
Those facts are scattered across email, spreadsheets, institutional systems, and web pages, so each task begins by recovering what the lab already knows.
Systems such as [ORCID](https://orcid.org) and [SciENcv](https://www.ncbi.nlm.nih.gov/sciencv/) manage specific record types, but research groups still need an open collection they control that brings these records together and describes their relationships.
Such infrastructure improves efficiency and accuracy in lab operations and provides a foundation for lab websites.

Research-information management is an established field [1]-[3].
[CERIF](https://eurocris.org/services/cerif) and systems such as [VIVO](https://vivoweb.org/) model institutional records, while scholarly knowledge graphs connect metadata at global scale [4], [5].
Many use Linked Data: shared identifiers and formally defined terms make relationships machine-readable across independently maintained sources, allowing information to be connected and reused without every system maintaining its own copy.
A schema defines the types of records, their relationships, and the rules used to validate them.
Identifiers such as [ORCID](https://orcid.org) and [DOI](https://www.doi.org/) let a lab connect its records to this broader landscape while describing local roles, relationships, and tools.
This explicit modeling of lab metadata becomes especially valuable with AI: as AI makes it easier to extract and generate candidate content, the harder task is organizing, validating, and reviewing that content so that only trustworthy information enters the lab’s official record.

Our long-time collaborator Michael Hanke and colleagues in the [Psychoinformatics group](https://www.psychoinformatics.de) at the INM-7 Institute of Forschungszentrum Jülich in Germany developed [ORINOCO](https://www.psychoinformatics.de/projects/orinoco/) (Organized Research Information: Ontology-mapping, Curation, Orchestration).
ORINOCO addresses this need at research-group scale through an open, self-hostable set of interoperating components [6].
It is grounded in [LinkML](https://linkml.io/) schemas which provide machine-readable definitions of people, projects, grants, research outputs, and their relationships.
These schemas drive browser-based forms for entering records and a service that validates submissions and stages them for review before they join the lab’s curated collection.
Query and rendering tools can then follow the relationships among approved records and reshape them for websites, reports, catalogs, discovery, and other lab operations.

The [Lab-in-a-Box](https://hub.psychoinformatics.de/lab-in-a-box/) deployment toolkit places ORINOCO alongside other lab-operated services [7].
The Psychoinformatics group website demonstrates how linked records organize pages, related-item lists, backlinks, and graph navigation; the [TRR379](https://www.trr379.de/) research consortium applies the same approach, with schema-generated interfaces accepting records from people and automated processes [6].

At the Center for Open Neuroscience (CON), we are adopting ORINOCO for our lab website and broader research-information needs, retaining its schemas and processing tools while adapting their operation to GitHub-centered collaboration and review in [ORINOCO-Lite](https://github.com/ORINOCO-Lite/orinoco-lite-dev) [8].
Records stored as YAML text files in Git constitute the official collection.
Whether edited directly or prepared automatically from existing lab sources such as our Zotero publication group, all proposed changes are reviewed through pull requests.
A GitHub Action uses ORINOCO components to validate the records and regenerate the website.

For RSEs, the central opportunity is to treat lab metadata as shared infrastructure rather than maintain it separately for each application.
A website provides an immediate and visible use for that infrastructure, but its larger value is an enduring body of curated, structured information that can be reused as the lab’s needs and tools evolve.
```{=latex}
\newpage
```

## Acknowledgments

We thank Michael Hanke, Stephan Heunis and other contributors to DataLad Concepts and the ORINOCO ecosystem for the underlying schemas, services, and implementation patterns, and the broader Center for Open Neuroscience team for motivating operational use cases.

OpenAI Codex assisted with source review, initial drafting, and copy-editing of the Abstract and the Connection to Mission, Goals, and Interests of the US-RSE Community.
The authors selected the scope and framing, verified technical claims against the cited software, and reviewed and approved the final text.

## References

1. euroCRIS.
[Common European Research Information Format (CERIF)](https://eurocris.org/services/cerif).
2. OCLC Research and euroCRIS.
[*Practices and Patterns in Research Information Management: Findings from a Global Survey*](https://doi.org/10.25333/BGFG-D241).
3. [Barcelona Declaration on Open Research Information](https://barcelona-declaration.org/background_and_context/).
4. VIVO and DSpace-CRIS.
Open-source research information systems.
[VIVO](https://vivoweb.org/); [DSpace-CRIS](https://4science.com/open-source/).
5. Open scholarly knowledge graphs.
[OpenAIRE Graph](https://graph.openaire.eu/); [OpenAlex](https://developers.openalex.org/).
6. Research-information schemas, services, and projections.
[DataLad Concepts](https://concepts.datalad.org/); [ORINOCO](https://www.psychoinformatics.de/projects/orinoco/); [ORINOCO documentation](https://hub.psychoinformatics.de/orinoco/); [Psychoinformatics group website](https://www.psychoinformatics.de/); [TRR379 website](https://www.trr379.de/); [TRR379 metadata pool](https://pool.v0.trr379.de/).
7. Lab-in-a-Box.
[Deployment toolkit](https://hub.psychoinformatics.de/lab-in-a-box/liab-deployments); M. Hanke et al., [*Lab in a box: A build-your-own-open-lab software toolkit*](https://doi.org/10.5281/zenodo.20583436), OHBM 2026 poster.
8. ORINOCO-Lite.
[Development repository](https://github.com/con/orinoco-lite-dev); [GitHub Action](https://github.com/con/orinoco-lite-action).

## Connection to Mission, Goals, and Interests of the US-RSE Community

Research software engineers often inherit not only research code, but also the information systems through which groups coordinate their activities and communicate their work to collaborators, funders, institutions, and the public.
Designing those systems as maintainable, reusable infrastructure brings together software architecture, data stewardship, interoperability, governance, and long-term sustainability.
ORINOCO provides a concrete setting in which to make that frequently invisible RSE contribution legible.

This contribution advances US-RSE’s Community, Advocacy, and Resources goals in distinct ways.
It gives RSEs a concrete basis for exchanging approaches across labs and institutions; advocates for metadata modeling and stewardship as consequential RSE work; and presents open models and validation workflows that practitioners can evaluate.
It also highlights the RSE judgment required to connect local needs with community standards and choose an operating model a group can sustain.

The conference theme makes this work particularly timely.
AI can help extract and reorganize information from sources a lab already maintains, but its output becomes operationally useful only when it conforms to explicit models and passes accountable human review.
Designing these boundaries is an RSE responsibility and an important part of building information infrastructure on which conventional and AI-assisted workflows can both rely.
