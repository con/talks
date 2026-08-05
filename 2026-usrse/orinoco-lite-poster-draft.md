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
Labs still need a locally governed approach whose immediate value makes curation worthwhile.

Orinoco applies this pattern at research-group scale through an open, self-hostable set of interoperating tools [6].
DataLad Concepts supplies a LinkML model for people, projects, outputs, and their relationships.
Zotero groups and institutional sources can feed incoming areas through source-specific CI adapters; a GitHub-facing tool such as `solidation` could supply another feed [9].
Dump Things validates records and separates incoming proposals from the curated official collection, the lab's operational source of truth for approved metadata.
SHACL-vue supports model-driven entry and review, while `dtc` and `qri` project the collection into websites, reports, catalogs, and other applications.

Lab-in-a-Box provides the service-backed deployment context, including persistent Dump Things and Forgejo among other self-hosted services [7].
The metadata-driven Psychoinformatics website demonstrates one Orinoco projection [6].
Open schemas, software, and interfaces let groups retain custody of their records and choose producers and consumers, which led CON to reuse Orinoco for its website and broader research-information needs.

![](orinoco-metadata-flow.png){width=100%}

*Orinoco's open components turn source-specific metadata feeds into a reviewed lab pool and reusable projections; the callouts show the Lab-in-a-Box service setting and CON's additional GitHub-based deployment.*

At CON, a modeled DataLad publication links DOI and Zotero identifiers to Yaroslav Halchenko and the DataLad project.
`qri` and Hugo turn those relationships into pages, backlinks, and graph navigation, so correcting one record improves every derived view.
For GitHub-oriented labs, we are developing Orinoco Lite: modeled YAML is reviewed in pull requests, a GitHub Action runs Orinoco validation and projection, and Hugo publishes a static website without a persistent metadata service [8].
This changes deployment, not the information model or the possibilities for reuse.

The lab-owned pool need not become a local silo.
ORCID, ROR, DOI, and PROV-O mappings provide explicit join points across independently governed graphs.
When a researcher needs grant outputs, potential collaborators, or a biosketch update, conventional or AI-assisted software can work from reviewed relationships and propose corrections for human approval.

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
