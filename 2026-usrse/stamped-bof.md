# Pragmatic practices for reproducible and open science through case stories and principles 

### Session Leaders

```yaml
- Name: Cody C. Baker
  Email: cody.c.baker.phd@gmail.com
  Affiliation: Center for Open Neuroscience, Dartmouth College
  ORCID: https://orcid.org/0000-0002-0829-4790

- Name: Dorota Jarecka
  Email: cody.c.baker.phd@gmail.com
  Affiliation: Gabrieli Laboratory, Massachusetts Institute of Technology
  ORCID: https://orcid.org/0000-0001-8282-2988
```


### Keywords

- Reproducible research
- Open science
- Provenance


### Description for Program

Reproducibility and open science are widely championed in principle yet unevenly practiced.
The gap between aspiration and execution is rarely about willingness.
It is about the day-to-day friction of managing data, code, environments, and provenance across heterogeneous tools, platforms, and collaborators.
Research Software Engineers sit precisely at this gap, translating community standards into workflows that scientists can actually run, share, and reuse.

This Birds of a Feather session brings together RSEs, scientists, and tool builders to exchange pragmatic, battle-tested practices for making research objects reproducible and open.
We will anchor the discussion in concrete case stories drawn from domains including neuroimaging, neurophysiology, statistical computing, and other broad domains, while connecting them to emerging organizing frameworks such as the STAMPED principles (Self-contained, Tracked, Actionable, Modular, Portable, Ephemeral, Distributable).

Topics will include containerization and package management, version control for GB- to TB-scale datasets, cross-platform I/O, workflow portability, and the implications of AI-assisted research for provenance and reproducibility.
We invite RSEs working on or affected by reproducibility infrastructure, whether building tools, supporting scientists, or shaping institutional practice, to join, share what has worked, and help shape a shared vocabulary and toolkit for the community.



### Session Information Abstract

**Topic Summary**  

RSEs are the people who operationalize reproducibility.
They build the pipelines, maintain the environments, and translate community standards into software that scientists can actually run.
Yet the practices that make this work are scattered across domains, tools, and institutions, and rarely shared in one room.
This BoF creates that room.

By pairing emerging organizing frameworks with concrete case stories from working RSEs, the session aims to surface what is already working, where the recurring friction lies, and how the community can converge on shared vocabulary and toolkits without prescribing any single stack.


**Target Audience**   

This BoF is aimed at RSEs and RSE-adjacent practitioners who encounter reproducibility and open science challenges in their daily work, including those building reproducibility infrastructure, RSEs embedded in research groups, tool developers in packaging or data distribution, software-heavy domain scientists, and group leaders shaping reproducibility policy or shared infrastructure.
No specific domain background is required; while several presenters come from neuroscience, the practices discussed apply broadly.
Attendees at any career stage are welcome, whether to actively contribute or simply listen and learn. 


**Format**   

- Start with a few (up to 3-4) short (up to 15 minutes) scheduled presentations
- Open-mic for short (up to 5 minutes) stories / demos about representative projects
- Finish with open panel discussion regarding challenges & sharing known solutions or proposing new ones


**Presenters**  

1. Introduction to STAMPED Principles (Cody Baker, ~15 mins)
2. Package and container management in R (Malcolm Barrett, ~15 mins)
3. Neuroscience data management and analysis through Spyglass (Sam Bray, ~15 mins)
4. Benchmarking cross-platform I/O with cloud-enabled streaming (Ryan Ly, ~5 mins)
5. Neuroimaging with the BIDS study, BABS, and simple2 (Dorota Jarecka, ~5 mins)
6. Assessing pipelines through the Software Gardening Almanack (Dave Bunten, ~5 mins)



### Connection to Mission, Goals, & Interests of US-RSE Community  

**Community**:
- Reproducibility work is often done in isolation, with each lab or RSE solving similar problems with different tools.
- This session creates a venue for RSEs across domains to recognize shared challenges, compare solutions, and form ongoing connections around a common concern.
- The open-mic and panel format is designed specifically to draw out attendees rather than broadcast at them.

**Advocacy**:
- RSEs are the people who turn reproducibility principles into working software, yet this contribution is frequently invisible in research outputs.
- By framing reproducibility as operational maturity that requires sustained RSE effort, the session reinforces the case for RSE roles, time, and recognition within research projects and institutions.

**Resources**:
- Attendees will leave with concrete, field-tested practices and pointers to tooling that addresses container management, large-data versioning, workflow portability, provenance capture, and AI-assisted research.
- The STAMPED principles and accompanying checklist provide a shared vocabulary that RSEs can bring back to their groups for evaluating and incrementally improving existing workflows, without requiring adoption of any particular stack.

**DEI**:
- The session is structured to welcome contributions from RSEs at any career stage and from any domain, with no assumed tooling background.
- Short open-mic slots lower the barrier to participation for newer community members who may not yet be ready to give a full talk.
