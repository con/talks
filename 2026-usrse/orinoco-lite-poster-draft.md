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

Ask a research group to update its website, prepare a funder report, assemble a collaborator list, revise a biosketch, or account for every output from a grant, and the same problem appears: the facts exist, but not in a form that can be reused. They have been copied among email, spreadsheets, CVs, proposals, manuscript acknowledgments, institutional systems, and web pages. Each new task begins by recovering, reconciling, and rewriting what the lab already knows. The website is not the problem; it is one visible symptom of treating research information as scattered prose rather than shared infrastructure.

Research-information management is an established field [1]-[3]. CERIF defines connected entities for interoperable research systems; commercial platforms and open systems such as VIVO and DSpace-CRIS maintain institutional research records; and OpenAIRE and OpenAlex show what connected scholarly metadata can support at global scale [1], [4], [5]. This prior art demonstrates the value of modeling research information, but it also reveals a practical gap. A lab often needs finer-grained operational context, local authority over its records, and an immediate benefit that justifies keeping them current. Institutional-scale services and global discovery graphs address many research-information needs, but they do not by themselves give an individual lab a practical, locally governed path for maintaining the finer-grained context it uses day to day.

Orinoco is an open, self-hostable ecosystem for maintaining and reusing structured research information [6]. Its research-specific model represents people, organizations, projects, grants, datasets, instruments, software, publications, and their relationships as records that can be validated, reviewed, and traced to their sources. The full system provides shared services through which a group can curate those records collaboratively and use them in multiple applications. Its service-backed components also provide the research-information layer of Lab-in-a-Box, a broader self-hostable toolkit for research data, metadata, collaboration, and publication [7]. The metadata-driven Psychoinformatics group website is a working example and inspired our adaptation [6]. For labs already familiar with GitHub, we are developing Orinoco Lite: a GitHub Action that keeps human-readable YAML records under pull-request review, validates them, and generates a static Hugo website [8]. In both cases, the lab maintains connected research information once and derives useful outputs from it. The website is an immediately useful output and an incentive to keep the records current, not the boundary of the system.

Once information is maintained as connected records, common lab tasks become different views of shared knowledge. A person's affiliation, project role, and contribution to an output can support a team page, project history, publication list, biosketch, grant narrative, progress report, or collaborator search without being re-entered for each one. A correction improves every view derived from the record; each useful view, in turn, gives the group a reason to keep the record accurate. That feedback loop is central to the adoption model: metadata stewardship becomes part of ordinary lab work rather than a separate documentation obligation.

The local payoff need not produce another information silo. Stable identifiers, provenance, and mappings to shared ontologies allow selected Orinoco records to be interpreted beyond the lab that maintains them. Independently governed graphs could therefore support questions across organizational boundaries without requiring every group to surrender its data to one central platform.

These same records provide a better basis for AI-assisted work. An assistant responding to a researcher's request can retrieve reviewed facts, follow relationships, preserve sources, and assemble a verifiable draft without first having to recover and reconcile the relevant information from inconsistent prose; it can also propose structured corrections for review. AI therefore amplifies both the value of reusable research information and the rate at which it can change, making explicit schemas, provenance, automated checks, and review increasingly important. The poster demonstrates the information model through its service-backed and GitHub-based implementations and shows how one record set supports multiple lab tasks. Its central claim is simple: a lab website can be a useful product of research-information stewardship instead of the place where research information goes to become stale.

```{=latex}
\newpage
```

## Acknowledgments

We thank Michael Hanke, Stephan Heunis and other contributors to DataLad Concepts and the Orinoco ecosystem for the underlying schemas, services, and implementation patterns, and the broader Center for Open Neuroscience team for motivating operational use cases.

OpenAI Codex assisted with source review, initial drafting, and copy-editing of the Abstract and the Connection to Mission, Goals, and Interests of the US-RSE Community. The authors selected the scope and framing, verified technical claims against the cited software, and reviewed and approved the final text.

## References

1. euroCRIS. [Common European Research Information Format (CERIF)](https://eurocris.org/services/cerif).
2. OCLC Research and euroCRIS. [*Practices and Patterns in Research Information Management: Findings from a Global Survey*](https://doi.org/10.25333/BGFG-D241).
3. [Barcelona Declaration on Open Research Information](https://barcelona-declaration.org/background_and_context/).
4. VIVO and DSpace-CRIS. Open-source research information systems. [VIVO](https://vivoweb.org/); [DSpace-CRIS](https://4science.com/open-source/).
5. Open scholarly knowledge graphs. [OpenAIRE Graph](https://graph.openaire.eu/); [OpenAlex](https://developers.openalex.org/).
6. Research-information schemas, services, and projections. [DataLad Concepts](https://concepts.datalad.org/); [Orinoco](https://www.psychoinformatics.de/projects/orinoco/); [Orinoco documentation](https://hub.psychoinformatics.de/orinoco/); [Psychoinformatics group website](https://www.psychoinformatics.de/).
7. Lab-in-a-Box. [Deployment toolkit](https://hub.psychoinformatics.de/lab-in-a-box/liab-deployments); M. Hanke et al., [*Lab in a box: A build-your-own-open-lab software toolkit*](https://doi.org/10.5281/zenodo.20583436), OHBM 2026 poster.
8. Orinoco Lite. [Development repository](https://github.com/con/orinoco-lite-dev); [GitHub Action](https://github.com/con/orinoco-lite-action).

## Connection to Mission, Goals, and Interests of the US-RSE Community

Research software engineers often inherit not only research code, but also the information systems through which groups communicate their work to collaborators, funders, institutions, and the public. Designing those systems as maintainable, reusable infrastructure brings together software architecture, data stewardship, interoperability, governance, and long-term sustainability. Orinoco provides a concrete setting in which to make that frequently invisible RSE contribution legible.

This contribution advances US-RSE's Community, Advocacy, and Resources goals in distinct ways. It gives RSEs a concrete basis for comparing approaches across labs and institutions; advocates for metadata modeling and stewardship as consequential RSE work; and contributes open resources, including shared models, validation workflows, and service-backed and GitHub-based implementations, that practitioners can evaluate and adapt. It also highlights the RSE judgment required to connect local needs with community standards and choose an operating model a group can sustain.

The conference theme makes this foundation more urgent. AI assistance can increase both the demand for research information and the rate at which proposed changes are produced. Trustworthy sources, inspectable transformations, and accountable review therefore become more important, not less. The contribution is not simply an AI-enabled website; it is an example of RSEs creating governed information infrastructure on which conventional software and AI-assisted work can both rely.
