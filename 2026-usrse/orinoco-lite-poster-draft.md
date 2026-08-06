# Beyond the Lab Website: Reusing Structured Research Metadata Across Lab Operations

## Presenters

- John Lee <[leej3@dartmouth.edu](mailto:leej3@dartmouth.edu)>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0001-5884-4247](https://orcid.org/0000-0001-5884-4247)
- Isaac To <[Isaac.C.To@dartmouth.edu](mailto:Isaac.C.To@dartmouth.edu)>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0002-4740-0824](https://orcid.org/0000-0002-4740-0824)
- Yaroslav O. Halchenko <[yaroslav.o.halchenko@dartmouth.edu](mailto:yaroslav.o.halchenko@dartmouth.edu)>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0003-3456-2493](https://orcid.org/0000-0003-3456-2493)

## Keywords

research information management; metadata reuse; knowledge graphs; semantic interoperability; AI-assisted research

```{=latex}
\newpage
```

## Abstract

Research groups repeatedly need the same facts to update a website, prepare a funder report, assemble a collaborator list, revise a biosketch, or account for a grant's outputs.
Those facts are scattered across email, spreadsheets, CVs, proposals, institutional systems, and web pages, so each task begins by recovering what the lab already knows.
A website is one visible symptom of treating research information as disconnected documents rather than shared infrastructure.

Research-information management is an established field [1]-[3].
CERIF, VIVO, and DSpace-CRIS model institutional records, while OpenAIRE and OpenAlex demonstrate connected scholarly metadata at global scale [1], [4], [5].
A lab-scale system should complement these resources by preserving global identifiers while maintaining the local roles, relationships, tools, and emerging work needed for day-to-day operations.
ORCID, ROR, DOI, and explicit mappings to terms in PROV-O provide possible connection points between local records and independently governed graphs.
AI can reduce the effort of maintaining this information by extracting candidate facts, reconciling identifiers, helping researchers query reviewed relationships, or drafting schema-conforming additions.
The schema constrains what kinds of records and relationships can be proposed, validation identifies malformed submissions, and human reviewers decide what enters the official record.

Orinoco implements this pattern at research-group scale through an open, self-hostable set of interoperating components [6].
DataLad Concepts supplies LinkML schemas: machine-readable definitions of people, projects, grants, research outputs, and their relationships.
Source-specific adapters transform metadata feeds, such as Zotero groups or institutional exports, into model-conforming candidate records; an adapter around GitHub data or CON's activity-report tool, `solidation`, could provide another feed [9].
The `dtc` command-line client submits and retrieves these records through Dump Things.
Dump Things validates records against the shared model and separates incoming submissions from the curated official collection.
SHACL-vue uses the same model to generate browser-based forms for entering, editing, and viewing records.
For reuse, `qri` follows relationships and reshapes approved records for particular consumers, while Hugo turns them into the public website and graph navigation.
The same approved knowledge can support reports, catalogs, discovery, and other lab operations.
Together, these components give the group an operational source of truth under local control while allowing feeds to remain authoritative for source-specific observations.
Open schemas and interfaces let a lab inspect each transformation, replace a feed or consumer, and connect selected records to information maintained elsewhere.

![](orinoco-metadata-flow.png){width=100%}

*Orinoco's open components turn source-specific metadata feeds into a reviewed lab pool and reusable projections; the callouts show the Lab-in-a-Box service setting and CON's additional GitHub-based deployment.*

Lab-in-a-Box is the broader self-hosted lab-service toolkit; its deployment workflows include persistent Dump Things and Forgejo among other services [7].
This arrangement keeps facilities for contributing, curating, storing, and reusing research information continuously available.
The Psychoinformatics website shows how the resulting knowledge can be presented: a scheduled workflow retrieves approved records and generates public pages, related-item lists, backlinks, and graph navigation [6].
The website is one maintained representation of that knowledge, not its source.

CON chose to reuse Orinoco's model and processing components while coordinating them through our own code rather than adopting the same long-running service topology.
We are developing Orinoco Lite as an additional deployment option for labs whose collaboration and review already happen in GitHub [8].
The modeled YAML records in Git are the canonical source, proposed changes are reviewed in pull requests, and a GitHub Action starts the necessary Orinoco components temporarily.
The Action starts Dump Things to validate the records, uses `dtc` to submit and retrieve them, uses `qri` to prepare website content and graph data, and invokes Hugo to build a static lab website.
GitHub Pages hosts the result, so the deployed website does not depend on a continuously running metadata service.

This deployment fits CON because GitHub already supplies identity, review, automation, and hosting, while Orinoco supplies the shared model, validation, and reusable processing components.
Orinoco Lite relocates the review and deployment boundary while preserving the modeled records as reusable inputs.
Metadata feeds can run in CI and propose repository updates for review rather than writing directly to accepted records.
It is therefore another way to operate the Orinoco approach, not a separate research-information system.

We invite RSEs to combine semantic models with constrained AI: use AI to propose structured records and relationships, validate those proposals, and keep human curators responsible for approval.
Curating knowledge once as shared metadata can make websites, reporting, discovery, and collaboration more efficient without sacrificing provenance or local control.

```{=latex}
\newpage
```

## Acknowledgments

We thank Michael Hanke, Stephan Heunis and other contributors to DataLad Concepts and the Orinoco ecosystem for the underlying schemas, services, and implementation patterns, and the broader Center for Open Neuroscience team for motivating operational use cases.

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
[DataLad Concepts](https://concepts.datalad.org/); [Orinoco](https://www.psychoinformatics.de/projects/orinoco/); [Orinoco documentation](https://hub.psychoinformatics.de/orinoco/); [Psychoinformatics group website](https://www.psychoinformatics.de/).
7. Lab-in-a-Box.
[Deployment toolkit](https://hub.psychoinformatics.de/lab-in-a-box/liab-deployments); M. Hanke et al., [*Lab in a box: A build-your-own-open-lab software toolkit*](https://doi.org/10.5281/zenodo.20583436), OHBM 2026 poster.
8. Orinoco Lite.
[Development repository](https://github.com/con/orinoco-lite-dev); [GitHub Action](https://github.com/con/orinoco-lite-action).
9. Center for Open Neuroscience.
[`solidation`: Produce activity reports from GitHub](https://github.com/con/solidation).

## Connection to Mission, Goals, and Interests of the US-RSE Community

Research software engineers often inherit not only research code, but also the information systems through which groups communicate their work to collaborators, funders, institutions, and the public.
Designing those systems as maintainable, reusable infrastructure brings together software architecture, data stewardship, interoperability, governance, and long-term sustainability.
Orinoco provides a concrete setting in which to make that frequently invisible RSE contribution legible.

This contribution advances US-RSE's Community, Advocacy, and Resources goals in distinct ways.
It gives RSEs a concrete basis for exchanging approaches across labs and institutions; advocates for metadata modeling and stewardship as consequential RSE work; and contributes open models and validation workflows that practitioners can evaluate and adapt across service-backed and GitHub-based deployments.
It also highlights the RSE judgment required to connect local needs with community standards and choose an operating model a group can sustain.

The conference theme makes this foundation more urgent.
AI assistance can increase both the demand for research information and the rate at which proposed changes are produced.
Trustworthy sources, inspectable transformations, and accountable review therefore become more important, not less.
The contribution is not simply an AI-enabled website; it is an example of RSEs creating governed information infrastructure on which conventional software and AI-assisted work can both rely.
