# Brain Initiative Meeting 2026 (poster abstract)

<!--

A brief abstract of the work you will present in your poster. Abstracts should be a written description of less than 350 words and include plain text with no additional information (ex., symbols, graphs, charts, pictures, etc.).  

BONUS:
- If you would like to be considered for Scholar Spotlight, and you meet the criteria above, prepare a 350-word or less statement.
- The theme of the 2026 BRAIN Initiative Conference is Inventing the Future. Describe the ways your research uniquely contributes to the future of neuroscience and/or will help revolutionize our understanding of the brain. 

-->

Neuroscience increasingly depends on the interplay of code, data, and computational environments, yet the record of how they were used together is often incomplete, scattered across repositories, wikis, and notebooks, or lost entirely.
This fragmentation undermines rigor, reproducibility, reusability, and efficiency in BRAIN Initiative pipelines that routinely span multiple institutions, archives, and compute platforms.
Existing frameworks such as FAIR and FAIR4RS govern discovery and interoperability of digital objects, but do not specify how research objects should be structured and managed so they can be re-executed, extended, and audited.
The community lacks a shared vocabulary for this operational layer.

Building on the YODA and VAMP traditions from neuroimaging, and on patterns that have independently converged across geophysics, genomics, statistics, and neuroimaging over three decades, we formalize seven principles a research object should satisfy: Self-containment, Tracking, Actionability, Modularity, Portability, Ephemerality, and Distributability, collectively STAMPED.
Each uses RFC-2119 keywords (MUST/SHOULD/MAY) and spans a spectrum from practical minimum to aspirational ideal, so adoption is non-prescriptive and incremental.
Formal LinkML schemas, an interactive compliance checklist, and a worked-example catalog are enabling tools to this end.

We demonstrate STAMPED through three BRAIN-funded exemplars.
OpenNeuroDerivatives reorganized derivative neuroimaging datasets so they exist as independent units that reference raw inputs as subdatasets rather than nesting under them, removing an upward dependency that previously violated Self-containment, Modularity, and Portability.
DANDI Compute, utilizing the Allen Institute for Neural Dynamics electrophysiology pipeline, packages spike-sorting outputs into nested BIDS-derivative units in which each leaf contains the exact code, runtime logs, outputs, and provenance metadata needed to re-execute the analysis, satisfying STAMPED end-to-end.
These adoptions show that STAMPED provides a tool-agnostic, incrementally adoptable vocabulary that lets researchers, reviewers, collaborators, and emerging AI agents evaluate and improve the operational maturity of computational neuroscience.
By making research objects re-executable and inspectable by construction, STAMPED converts reproducibility from an aspiration into a measurable property of everyday neuroscience practice.



### Scholar Spotlight statement

The future of neuroscience will be defined less by any single experimental technique than by our ability to compose and trust pipelines that span instruments, datasets, archives, and AI systems.
BRAIN Initiative investments have produced an extraordinary substrate for this future: OpenNeuro, DANDI, EMBER, ReproNim, and the derivative ecosystems they anchor.
Yet the rate at which these resources can compound depends on whether each research object they hold can be opened, rerun, extended, and reused without rediscovery. Today, too much of that work is repeated. STAMPED targets exactly this bottleneck.

By naming seven operational properties of a research object, Self-containment, Tracking, Actionability, Modularity, Portability, Ephemerality, and Distributability, we give the community a shared vocabulary that did not previously exist.
Researchers can now describe what their pipelines do and do not guarantee; reviewers can ask precise questions; collaborators can hand off work without losing context; and infrastructure projects such as DANDI Compute and OpenNeuroDerivatives can declare and verify the properties they enforce.
Each principle is a spectrum starting at what many labs already do, so adoption is incremental rather than gatekept.

STAMPED is also designed for the moment neuroscience is now entering, in which AI coding agents and autonomous research systems participate in analysis.
When an agent modifies code, generates a script, or proposes a hypothesis, those actions become part of the scientific record and must be Tracked alongside human contributions.
When a specification can be regenerated into an implementation at near-zero cost by an AI assistant, the specification itself becomes the research object, and STAMPED tells us what that specification must satisfy to remain accountable.
Without such principles, AI acceleration risks producing results that are fast but not introspectable.
By formalizing these principles and providing schemas, checklists, and worked examples openly, we aim to make every BRAIN-funded pipeline a durable, composable, and auditable contribution to the next decade of neuroscience, an invitation to invent that future together rather than rebuild it apart.
