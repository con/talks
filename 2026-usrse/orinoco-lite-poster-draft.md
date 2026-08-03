# Beyond the Lab Website: Reusing Structured Research Metadata Across Lab Operations

## Presenters

- John Lee <[leej3@dartmouth.edu](mailto:leej3@dartmouth.edu)>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0001-5884-4247](https://orcid.org/0000-0001-5884-4247)
- Isaac To <[Isaac.C.To@dartmouth.edu](mailto:Isaac.C.To@dartmouth.edu)>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0002-4740-0824](https://orcid.org/0000-0002-4740-0824)
- Yaroslav O. Halchenko <[yaroslav.o.halchenko@dartmouth.edu](mailto:yaroslav.o.halchenko@dartmouth.edu)>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID [0000-0003-3456-2493](https://orcid.org/0000-0003-3456-2493)

## Keywords

research metadata; research information management; lab operations; metadata reuse; AI agents

```{=latex}
\newpage
```

## Abstract

Research groups repeatedly rewrite the same facts about people, affiliations, roles, projects, datasets, instruments, software, grants, and publications. A lab website contains one copy, while grant text, annual reports, CVs, project directories, spreadsheets, and email contain others. These copies drift apart, the evidence behind them is lost, and routine requests become exercises in information recovery. The website is often treated as a communications problem, but the recurring burden points to a broader data-modeling problem: the group has valuable research information, yet no durable way to organize and reuse it.

We explore a different operating principle: model research information once as reviewed records with stable identifiers and explicit relationships, then generate purpose-specific views from those records. Reusable facts remain separate from destination-specific prose and visual presentation. A person's affiliation, role in a project, and connection to an output can therefore support a team page, a project history, a publication list, a CV or biosketch, grant boilerplate, a funder or annual report, a collaborator directory, and graph-based discovery without being independently re-entered for each use. A correction to the shared record can propagate to every projection; validation can reject malformed records or broken relationships; and version history can preserve who changed what and why. The lab website becomes one visible use of an operational research-information resource rather than the only place where its contents can be recovered.

The Center for Open Neuroscience (CON) website provides a concrete demonstration. Its modeled records connect an organization, people, projects, instruments, and publications, while human-authored narrative, branding, media, and legacy URLs remain under the lab's control. The current vertical slice generates entity pages, collection lists, forward links, backlinks, filters, and a navigation graph from the same records. Identical inputs produce byte-identical site manifests; adding a metadata record adds its page and graph connections without adding a route, index, or template; and invalid records, dangling relationships, and route conflicts stop publication. This is a deliberately small proof rather than a completed migration, but it shows how maintaining a website can simultaneously improve the lab's reusable operational knowledge without displacing editorial judgment.

Orinoco supplies schemas and components for capturing, validating, connecting, curating, and projecting this information. A service-backed deployment supports collaborative curation and reuse by multiple tools. In Orinoco Lite, we package the same model-to-website workflow as a GitHub Action for labs already familiar with GitHub, complementing the broader ecosystem with a convenient path to a reviewed static site.

The value grows in the age of AI. An agent asked to find collaborators, assemble a progress report, update a project page, or draft a biosketch can work from explicit entities, identifiers, and relationships instead of scraping uncertain prose or searching old email. It can propose a structured change rather than silently invent a new copy. Schemas, provenance, deterministic checks, and human review remain the publication boundary. Well-modeled metadata turns a ubiquitous administrative pain point into reusable lab infrastructure: each website update can make future reporting, discovery, communication, and agent-assisted work easier rather than adding another isolated source of truth.

```{=latex}
\newpage
```

## Acknowledgments

We thank Michael Hanke and the contributors to DataLad Concepts and the Orinoco ecosystem for the underlying schemas, services, and implementation patterns, and the broader Center for Open Neuroscience team for the website and metadata use case.

OpenAI Codex assisted with source review, initial drafting, and copy-editing of the Abstract and the Connection to Mission, Goals, and Interests of the US-RSE Community. The authors selected the scope and framing, verified technical claims against the cited software and prototype, and will review and approve the final text.

## References

1. DataLad Concepts. "Low-tech" metadata schemas. <https://concepts.datalad.org/>.
2. Hanke, M., Heunis, S., Mönch, C., et al. *Lab in a box: A build-your-own-open-lab software toolkit*. OHBM 2026. Zenodo. <https://doi.org/10.5281/zenodo.20583436>.
3. Orinoco. Self-hostable research-information infrastructure and linked metadata tools. <https://www.psychoinformatics.de/projects/orinoco/>; <https://hub.psychoinformatics.de/orinoco/>.
4. Dump Things Service. Self-hostable research-information storage, validation, and curation service. <https://hub.psychoinformatics.de/orinoco/dump-things-service>.
5. Center for Open Neuroscience. Orinoco Lite CON prototype and static preview. <https://github.com/leej3/centerforopenneuroscience.org/tree/orinoco-lite>; <https://leej3.github.io/centerforopenneuroscience.org/>.

## Connection to Mission, Goals, and Interests of the US-RSE Community

Research software engineers routinely encounter research information that is important but scattered across websites, documents, spreadsheets, services, and individual memory. Recovering and reconciling that information consumes technical staff time and makes routine communication, reporting, and software maintenance harder. Treating those facts and relationships as governed, reusable data is therefore an RSE concern, not merely a website redesign.

This work supports the US-RSE goals of community, advocacy, and resources by sharing a transferable pattern for turning a common maintenance burden into sustainable research infrastructure. It highlights characteristic RSE contributions: recognizing a hidden systems problem, designing a model around real research activity, preserving provenance, separating reusable data from presentation, adding validation and review gates, and choosing an operating boundary that a lab can maintain. The reusable GitHub workflow is intended to make these practices approachable to smaller teams without requiring them to operate the underlying components.

The work also responds directly to the conference theme, "Advancing Science in the Age of AI." Agents become more useful and less error-prone when they can retrieve explicit records and relationships instead of inferring facts from inconsistent prose. At the same time, faster generation makes accountable review more important. Structured proposals, deterministic validation, provenance, and human approval offer a practical division of labor: agents can help retrieve, assemble, and update research information, while people remain responsible for what becomes an accepted public record.
