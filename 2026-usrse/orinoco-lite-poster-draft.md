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

Research groups repeatedly rewrite the same facts about people, affiliations, roles, projects, datasets, instruments, software, grants, and publications. A lab website contains one copy, while grant text, annual reports, CVs, project directories, spreadsheets, and email contain others. These copies drift apart, their provenance is lost, and routine requests become exercises in information recovery. What appears to be a collection of separate communication and administrative tasks is often one metadata-management problem: the group has valuable research information, but no durable way to organize and reuse it.

We addressed this problem by modeling research information once as reviewed records with stable identifiers and explicit relationships, then deriving purpose-specific views from those records. A person's affiliation, role in a project, and connection to an output can support a team page, project history, publication list, CV or biosketch, grant text, funder report, collaborator directory, or graph-based search without being independently re-entered for each task. People can correct a shared record instead of reconciling many copies, while provenance, validation, and review make the resulting information more accountable. In this approach, a lab website is one useful projection of a maintained research-information resource, not the place where the only usable copy of the information lives.

Orinoco provides the schemas and services needed to maintain connected research information and reuse it for different lab tasks. We developed Orinoco Lite, a GitHub Action that makes the same metadata model convenient for labs already working in GitHub by generating a reviewed static website from their records. The website is an entry point to the model, not the limit of what the information can support.

The benefits extend beyond any individual lab. When groups use compatible schemas, stable identifiers, and concepts mapped to shared ontologies, relationships in their independently maintained knowledge graphs can be interpreted across organizational boundaries. Those connections could reveal related projects, shared methods and instruments, reusable datasets and software, linked outputs, and potential collaborators. Labs retain responsibility for their own records while making them connectable within a larger research-information network. Modeling information for local operations can therefore also make it more findable and interoperable across communities.

Structured lab knowledge also changes what people can accomplish with AI assistance. A researcher or RSE preparing an annual report, updating a biosketch, identifying collaborators, or finding every output associated with a grant can ask an assistant to work from reviewed entities and relationships rather than reconstructing facts from prose and email. The assistant could assemble a response with provenance or propose an update to the shared records; schemas, validation, and human review would determine what is accepted. The value lies in the reusable, connected knowledge, while AI provides another way for people to apply it across tasks.

We demonstrated how the same reviewed information can support website publication, reporting, research discovery, and AI-assisted tasks. This approach turns routine metadata maintenance from a recurring recovery exercise into an investment: each reviewed update improves the information available for the lab's next website change, report, proposal, collaboration, or cross-graph query.

```{=latex}
\newpage
```

## Acknowledgments

We thank Michael Hanke and the contributors to DataLad Concepts and the Orinoco ecosystem for the underlying schemas, services, and implementation patterns, and the broader Center for Open Neuroscience team for motivating operational use cases.

OpenAI Codex assisted with source review, initial drafting, and copy-editing of the Abstract and the Connection to Mission, Goals, and Interests of the US-RSE Community. The authors selected the scope and framing, verified technical claims against the cited software and prototype, and will review and approve the final text.

## References

1. DataLad Concepts. "Low-tech" metadata schemas. <https://concepts.datalad.org/>.
2. Hanke, M., Heunis, S., Mönch, C., et al. *Lab in a box: A build-your-own-open-lab software toolkit*. OHBM 2026. Zenodo. <https://doi.org/10.5281/zenodo.20583436>.
3. Orinoco. Self-hostable research-information infrastructure and linked metadata tools. <https://www.psychoinformatics.de/projects/orinoco/>; <https://hub.psychoinformatics.de/orinoco/>.
4. Dump Things Service. Self-hostable research-information storage, validation, and curation service. <https://hub.psychoinformatics.de/orinoco/dump-things-service>.

## Connection to Mission, Goals, and Interests of the US-RSE Community

Research software engineers routinely encounter research information that is important but scattered across websites, documents, spreadsheets, services, and individual memory. Recovering and reconciling that information consumes technical staff time and makes routine communication, reporting, and software maintenance harder. Treating those facts and relationships as governed, reusable data is therefore an RSE concern, not merely a website redesign.

This work supports the US-RSE goals of community, advocacy, and resources by sharing a transferable pattern for turning a common maintenance burden into sustainable research infrastructure. It highlights characteristic RSE contributions: recognizing a hidden systems problem, designing a model around real research activity, preserving provenance, and adding validation and review gates. Compatible models, stable identifiers, and mappings to shared ontologies can also connect independently governed lab graphs, improving discovery and reuse across research communities without requiring every group to use one central system.

The work responds directly to the conference theme, "Advancing Science in the Age of AI," by asking what information people need in order to use AI assistance responsibly. A researcher or RSE should be able to ask for a report, biosketch update, collaborator search, or account of a grant's outputs without requiring an assistant to infer facts from inconsistent prose. Reviewed records and explicit relationships provide that foundation. Provenance, validation, and human approval then offer a practical division of labor: AI can help people retrieve, assemble, and propose updates to research information, while people remain responsible for what becomes an accepted record.
