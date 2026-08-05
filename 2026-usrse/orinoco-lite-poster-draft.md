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
Those facts are dispersed across email, spreadsheets, CVs, proposals, acknowledgments, institutional systems, and web pages, so each task begins by recovering and reconciling what the lab already knows.
A website is one visible symptom of treating research information as scattered prose rather than shared infrastructure.

Research-information management is an established field [1]-[3].
CERIF, VIVO, and DSpace-CRIS model institutional records, while OpenAIRE and OpenAlex demonstrate connected scholarly metadata at global scale [1], [4], [5].
Research groups still need a practical way to maintain finer-grained operational context under local governance, with an immediate return that makes curation worthwhile.

Orinoco brings this approach to the scale of a research group [6].
LinkML schemas from DataLad Concepts describe people, organizations, projects, grants, datasets, instruments, software, publications, and their relationships, with identifiers and provenance that keep records traceable.
The service-backed Orinoco stack uses SHACL-vue and Dump Things for collaborative curation and supplies the research-information layer of Lab-in-a-Box [7]; its metadata-driven Psychoinformatics group website demonstrates the model in use and inspired our adaptation [6].
For labs already working in GitHub, we are developing Orinoco Lite: human-readable YAML is reviewed in pull requests, a GitHub Action validates it, `qri` projects its relationships, and Hugo publishes a static website [8].
Both paths maintain the same reusable model through review processes that fit different lab operations.

![](orinoco-metadata-flow.png){width=100%}

*Solid arrows show the working record-to-website path; the dashed arrow marks prospective reuse of modeled scope by `solidation`, whose GitHub-to-report path already works independently.*

At CON, a YAML record for a DataLad publication includes its DOI and Zotero item identifiers and links the publication to Yaroslav Halchenko and the DataLad project.
`qri` and Hugo use those relationships to generate publication, person, and project pages, related items, backlinks, and graph navigation.
The website makes curation visibly useful: correcting one record improves every derived view.

The model also supplies context to source-specific tools rather than replacing them.
CON's `solidation` combines YAML lists of repositories and members with current GitHub activity to produce a Markdown project-health report [9].
It could draw that scope from modeled relationships among people, projects, and repositories while GitHub remains authoritative for activity.

Shared identifiers such as ORCID, ROR, and DOI, together with explicit mappings to PROV-O, provide connection points for linking selected records across independently governed lab graphs and could support questions that cross organizational boundaries.
When a researcher asks for grant outputs, potential collaborators, or a biosketch update, an assistant can follow reviewed relationships, preserve sources, and propose structured corrections for human review.
The website provides the immediate payoff; the governed record can also support reporting, cross-lab discovery, and AI-assisted work without creating another copy of the lab's knowledge.

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
It gives RSEs a concrete basis for comparing approaches across labs and institutions; advocates for metadata modeling and stewardship as consequential RSE work; and contributes open resources, including shared models, validation workflows, and service-backed and GitHub-based implementations, that practitioners can evaluate and adapt.
It also highlights the RSE judgment required to connect local needs with community standards and choose an operating model a group can sustain.

The conference theme makes this foundation more urgent.
AI assistance can increase both the demand for research information and the rate at which proposed changes are produced.
Trustworthy sources, inspectable transformations, and accountable review therefore become more important, not less.
The contribution is not simply an AI-enabled website; it is an example of RSEs creating governed information infrastructure on which conventional software and AI-assisted work can both rely.
