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

Research-information management is an established field. CERIF defines connected entities for interoperable research systems; commercial platforms and open systems such as VIVO and DSpace-CRIS maintain institutional research records; and OpenAIRE and OpenAlex show what connected scholarly metadata can support at global scale. This prior art demonstrates the value of modeling research information, but it also reveals a practical gap. A lab often needs finer-grained operational context, local authority over its records, and an immediate benefit that justifies keeping them current. Institutional-scale services and global discovery graphs do not by themselves provide a lab-scale adoption path.

Orinoco addresses this gap with an open, research-specific model for information a lab creates and uses. It describes people, organizations, projects, grants, datasets, instruments, software, publications, and their relationships as records that can be validated, reviewed, and traced to their sources. The full Orinoco system provides shared services through which a group can curate those records collaboratively and use them in multiple applications. For labs already familiar with GitHub, we developed Orinoco Lite: a GitHub Action that validates reviewed records and generates a static website. In both cases, the lab maintains connected research information once and derives useful outputs from it. The website is an immediately useful output and an incentive to keep the records current, not the boundary of the system.

Once information is maintained as connected records, common lab tasks become different views of shared knowledge. A person's affiliation, project role, and contribution to an output can support a team page, project history, publication list, biosketch, grant narrative, progress report, or collaborator search without being re-entered for each one. A correction improves every view derived from the record; each useful view, in turn, gives the group a reason to keep the record accurate. That feedback loop is central to the adoption model: metadata stewardship becomes part of ordinary lab work rather than a separate documentation obligation.

The local payoff need not produce another information silo. Orinoco records stable identifiers, provenance, and mappings to shared ontologies so that selected records can be interpreted beyond the lab that maintains them. Independently governed graphs could then connect people, organizations, projects, methods, instruments, datasets, software, and outputs. Such connections would support questions that cross organizational boundaries without requiring every group to surrender its data to one central platform.

Reusable research information also provides a better basis for AI-assisted work. A researcher may ask for a draft progress report, a list of potential collaborators, or all products associated with a grant. Searching inconsistent prose forces the assistant to rediscover relationships and guess which facts are current. Reviewed, connected records let it retrieve the relevant information directly, follow relationships across entities, preserve links to sources, and assemble a useful draft. This makes the work more effective and efficient, with results that are easier to verify. An assistant can also propose additions and corrections to those records. AI therefore amplifies both the value of reusable research information and the rate at which it can change. Explicit schemas, provenance, automated checks, and review let a lab benefit from that speed without degrading the quality of its records.

The poster demonstrates the information model, the service-backed system and GitHub workflow, and examples that reuse one set of records for publication, reporting, discovery, and AI-assisted work. Its central claim is simple: a lab website can be a useful product of research-information stewardship instead of the place where research information goes to become stale.

```{=latex}
\newpage
```

## Acknowledgments

We thank Michael Hanke and the contributors to DataLad Concepts and the Orinoco ecosystem for the underlying schemas, services, and implementation patterns, and the broader Center for Open Neuroscience team for motivating operational use cases.

OpenAI Codex assisted with source review, initial drafting, and copy-editing of the Abstract and the Connection to Mission, Goals, and Interests of the US-RSE Community. The authors selected the scope and framing, verified technical claims against the cited software and prototype, and will review and approve the final text.

## References

1. euroCRIS. [Common European Research Information Format (CERIF)](https://eurocris.org/services/cerif).
2. OCLC Research and euroCRIS. [*Practices and Patterns in Research Information Management: Findings from a Global Survey*](https://doi.org/10.25333/BGFG-D241).
3. [Barcelona Declaration on Open Research Information](https://barcelona-declaration.org/background_and_context/).
4. VIVO and DSpace-CRIS. Open-source research information systems. [VIVO](https://vivoweb.org/); [DSpace-CRIS](https://4science.com/open-source/).
5. Open scholarly knowledge graphs. [OpenAIRE Graph](https://graph.openaire.eu/); [OpenAlex](https://developers.openalex.org/).
6. Research-information schemas, services, and projections. [DataLad Concepts](https://concepts.datalad.org/); [Orinoco](https://www.psychoinformatics.de/projects/orinoco/); [Orinoco documentation](https://hub.psychoinformatics.de/orinoco/).

## Connection to Mission, Goals, and Interests of the US-RSE Community

Research software engineers routinely encounter research information that is important but scattered across websites, documents, spreadsheets, services, and individual memory. Recovering and reconciling that information consumes technical staff time and makes routine communication, reporting, and software maintenance harder. Treating those facts and relationships as governed, reusable data is therefore an RSE concern, not merely a website redesign.

This work supports the US-RSE goals of community, advocacy, and resources by translating established research-information and linked-data practices into a lab-scale adoption pattern. A group receives immediate value from maintaining its records while preserving open identifiers, provenance, validation, and review. Compatible models and mappings to shared ontologies can connect independently governed lab graphs, improving discovery and reuse across research communities without requiring every group to use one central system.

The work responds directly to the conference theme, "Advancing Science in the Age of AI," by showing how structured research information makes AI assistance more effective and efficient. Asking an assistant to reconstruct the lab from inconsistent prose repeats the same information-recovery problem at greater speed. Reviewed records and explicit relationships let it retrieve relevant facts, follow connections, preserve sources, and assemble results for the task at hand. The same foundation already serves ordinary scripts, queries, websites, and reports. Reusable research information creates value for a lab; AI amplifies that value.
