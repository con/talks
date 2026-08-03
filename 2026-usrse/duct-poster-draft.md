# Agent-friendly Provenance Capture with `con-duct`

## Presenters

- Austin Macdonald \<austin.s.macdonald@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-8124-807X
- Cody C. Baker \<cody.c.baker.phd@gmail.com\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-0829-4790
- John A. Lee \<John.A.Lee@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0001-5884-4247
- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0003-3456-2493

## Keywords

agentic workflows, provenance, reproducibility, resource monitoring, HPC

## Abstract

Research outputs are only as trustworthy as the record of how they were produced: what was run, against what inputs, producing what outputs, with which resources.
By default, most of that record is ephemeral; `con-duct` is a lightweight wrapper that keeps it.

Anything you can run in a terminal (binaries, shell pipelines, scripts, etc.) passes through `duct` unchanged and leaves a complete trace.
Invoked as `duct <cmd>`, your command runs and produces:
 - full stdout and stderr to disk
 - resource usage sampled across the command's entire process tree
 - a record containing the invocation, wall clock time, peak memory, exit code, and system and environment details

The monitor is standard-library Python needing no elevated privileges, so the same wrapper works on a laptop, in a container, or on an HPC node, for a human at a terminal or an agent calling a tool.
It is POSIX-only: no Windows, and since sampling relies on `ps`, macOS reports some details differently than Linux.

For research, this capture is provenance, and it composes with existing tooling: `datalad run "duct
<cmd> ..."` produces a git commit binding inputs, command, and outputs, with the duct logs alongside.
On HPC, the measured wall time and resource statistics help guide the next job.
Hoffstaedter's `ds000007-mriqc` dataset [4] ships a `logs/duct/` directory alongside its MRIQC outputs, so `con-duct ls` and `con-duct plot` reconstruct the resource picture of a completed neuroimaging quality-control pipeline months after the fact, without re-executing it.

The same capture pays off in daily work, where humans and agents now execute commands side by side.
Because the full record lands on disk rather than in an agent's context, it costs nothing to carry — and it equips a successor, human or agent, to answer questions that weren't known ahead of time:
 - Did we get that warning last time?
 - Did this run take longer?

`con-duct ls` answers from disk, filtering on any captured field with a Python expression:

- `con-duct ls -e "message=='<tag>'"` retrieves runs tagged at capture time with `duct -m "<tag>"`.
- `con-duct ls -e "exit_code != 0"` lists every failure.
- `con-duct ls -e "peak_rss > 8e9"` finds runs that exceeded a memory budget.

And when an expensive job fails, the bug-report evidence — exact command, host, full stderr, and the resource timeline leading up to the failure — is already on disk: file the issue without re-running the job.

`con-duct` is on PyPI (`pip install con-duct`), registered as RRID:SCR_025436, and developed openly [1].

## Acknowledgments

We thank the broader ReproNim and OpenNeuro communities for ongoing feedback on `con-duct`'s design and use.
`con-duct`'s resource-monitoring approach is based on brainlife's `smon` (<https://github.com/brainlife/abcd-spec/blob/master/hooks/smon>).

*AI disclosure (per IEEE policy):* Prose in the Abstract and Connection-to-Mission sections was drafted with assistance from Anthropic's Claude; the authors specified the content, edited the text, and verified all technical claims, commands, and references.
The `con-duct` software itself is developed with AI assistance, with human review of all merged code.

## References

1. `con-duct`. Center for Open Neuroscience. <https://github.com/con/duct>. RRID:SCR_025436.
2. DataLad. <https://www.datalad.org/>. RRID:SCR_003931.
3. brainlife `smon`. <https://github.com/brainlife/abcd-spec/blob/master/hooks/smon>
4. Hoffstaedter, F. `ds000007-mriqc` (duct logs in `logs/duct/`). <https://cerebra.fz-juelich.de/f.hoffstaedter/ds000007-mriqc/src/branch/base/logs/duct/>

## Connection to Mission, Goals, & Interests of US-RSE Community

`con-duct` was built by RSEs at the Center for Open Neuroscience to record provenance for neuroimaging pipelines.
The dev-side payoff (reaching back into outputs that would otherwise be gone) was an unexpected bonus.
As LLM agents take on more of the executing (writing throwaway pipelines, exploring datasets, calling tools), the volume of unrecorded work explodes: more commands, more parallel streams, results produced faster than anyone reads them.
RSEs are the people who decide whether that work remains auditable — who preserve the context, make it discoverable, and keep capture cheap enough that nobody skips the step.

`con-duct` is one small piece of an answer: a wrapper that makes the agent's work, like the human's, leave a trace.
