# Agent-friendly Provenance Capture with `con-duct`

## Presenters

- Austin Macdonald \<austin.s.macdonald@dartmouth.edu\>, Center for Open Neuroscience, Department of Psychological and Brain Sciences, Dartmouth College, ORCID 0000-0002-8124-807X
- Cody C. Baker \<cody.c.baker.phd@gmail.com\>, Center for Open Neuroscience, Department of Psychological and Brain Sciences, Dartmouth College, ORCID 0000-0002-0829-4790
- John A. Lee \<John.A.Lee@dartmouth.edu\>, Center for Open Neuroscience, Department of Psychological and Brain Sciences, Dartmouth College, ORCID 0000-0001-5884-4247
- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Center for Open Neuroscience, Department of Psychological and Brain Sciences, Dartmouth College, ORCID 0000-0003-3456-2493

## Keywords

agentic workflows, provenance, reproducibility, resource monitoring, HPC

## Abstract

Whether trying out a new tool, testing pipelines, or meticulously analyzing data for research, the daily work of RSEs and their agents depends on keeping context lean but relevant.
The terminal outputs of tools and scripts frequently hold the necessary information, but they are
often either invisible (and bloating) in an agent's context window, or forgotten after a human's terminal scrolls past the buffer.

`con-duct` is a lightweight, Python-based command line tool: just use `duct <cmd>` instead of pure `<cmd>` to run a command.
A wrapped run leaves a trail: full stdout and stderr streamed to disk; resource usage sampled across the command's process tree; and a record of the invocation, wall clock time, peak memory, exit code, and system and environment details.
While workflow managers or experiment-tracking systems can produce a richer record, `con-duct` strikes a balance, collecting basic provenance with so little effort it can be used on everything, producing uniform records.

**In daily work**, humans and agents now execute commands side by side.
Using `con-duct`, the full record stays out of the context window until it is needed.
Even better, multiple runs can be filtered and grepped, ready for the questions nobody knew to ask.
When did our tests start having that warning?
Did this run take longer?
`con-duct ls` makes the answers discoverable, filtering on any captured field with a Python expression:
 - `con-duct ls -e "message=='<tag>'"` retrieves runs tagged at capture time with `duct -m "<tag>"`.
 - `con-duct ls -e "exit_code != 0"` lists failures.
 - `con-duct ls -e "peak_rss > 8e9"` finds runs that exceeded a memory budget.

Tools can adopt `con-duct` internally rather than reinventing per-tool monitoring: ReproNim's `containers` [5] and ReproStim [6] both offer it already, and one `con-duct ls` query spans the records from all of them.

**For research**, the record stops being a convenience, and starts being a part of the provenance chain.
Pairing `con-duct` with `datalad` (git-based version control for data)[2] is an easy win for rigor.
`datalad run "duct <cmd> ..."` completes the execution and then commits the diff (including the duct logs).
The invocation results in a **complete** provenance record binding results of running the command, along with `duct` collected logs, and automated commit message with optional specification of inputs and outputs.
On HPC, last month's measured wall time and peak memory are already recorded, and can help inform tomorrow's SLURM request.
**When an expensive job fails**, the bug-report evidence is already on disk, no re-run necessary to file an issue. 

`con-duct` is on PyPI (`pip install con-duct`), conda-forge, registered as `RRID:SCR_025436`, and developed openly [1].

```{=latex}
\newpage
```

## Acknowledgments

We thank the broader ReproNim and OpenNeuro communities for ongoing feedback on `con-duct`'s design and use.
`con-duct`'s resource-monitoring approach is based on brainlife's `smon` [3].

*AI disclosure (per IEEE policy):* Prose in the Abstract and Connection-to-Mission sections was drafted with assistance from Anthropic's Claude; the authors specified the content, edited the text, and verified all technical claims, commands, and references.
The `con-duct` software itself is developed with AI assistance, and with human review of all merged code.

## References

1. `con-duct`. Center for Open Neuroscience. <https://github.com/con/duct>. RRID:SCR_025436.
2. DataLad. <https://www.datalad.org/>. RRID:SCR_003931.
3. brainlife `smon`. <https://github.com/brainlife/abcd-spec/blob/master/hooks/smon>
4. Hoffstaedter, F. `ds000007-mriqc` (duct logs in `logs/duct/`). <https://cerebra.fz-juelich.de/f.hoffstaedter/ds000007-mriqc/src/branch/base/logs/duct/>
5. ReproNim/containers. <https://github.com/ReproNim/containers>. RRID:SCR_018467.
6. ReproStim. <https://github.com/ReproNim/reprostim>. <https://doi.org/10.5281/zenodo.4416842>

## Connection to Mission, Goals, & Interests of US-RSE Community

`con-duct` was built by RSEs at the Center for Open Neuroscience to record provenance for neuroimaging pipelines.
The dev-side payoff (reaching back into outputs that would otherwise be gone) was an unexpected bonus.
As LLM agents take on more of the executing (writing throwaway pipelines, exploring datasets, calling tools), the volume of unrecorded work explodes: more commands, more parallel streams, results produced faster than anyone reads them.
RSEs are the people who decide whether that work remains auditable: who preserve the context, make it discoverable, and keep capture cheap enough that nobody skips the step.
Integrating at the tool level saves each project from building its own monitoring and logging, and keeps the records uniform across tools, so the collection stays queryable as a whole.
