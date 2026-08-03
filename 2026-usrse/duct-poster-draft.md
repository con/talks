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
By default, that record is ephemeral, gone when the terminal scrolls or the agent's context rolls over.

`con-duct` is a lightweight, standard-library Python wrapper: anything you can run in a terminal (binaries, shell pipelines, scripts, etc.) runs unchanged as `duct <cmd>`.

Every wrapped run leaves a complete trace: full stdout and stderr streamed to disk; resource usage sampled across the command's entire process tree; and a record of the invocation, wall clock time, peak memory, exit code, and system and environment details.

**For research**, capture is provenance: `datalad run "duct <cmd> ..."` binds inputs, invocation, and outputs into a git commit, with the duct logs alongside [2].
On HPC, yesterday's measured wall time and peak memory size tomorrow's SLURM request.

**In daily work**, humans and agents now execute commands side by side.
The full record lands on disk, not in an agent's context: free to carry, and ready for the questions nobody knew to ask.
Did we get that warning last time?
Did this run take longer?
`con-duct ls` answers from disk, filtering on any captured field with a Python expression:
 - `con-duct ls -e "message=='<tag>'"` retrieves runs tagged at capture time with `duct -m "<tag>"`.
 - `con-duct ls -e "exit_code != 0"` lists every failure.
 - `con-duct ls -e "peak_rss > 8e9"` finds runs that exceeded a memory budget.

**When an expensive job fails**, the bug-report evidence is already on disk (invocation, host, full stderr, resource timeline).
File the issue; skip the re-run.

`con-duct` is on PyPI (`pip install con-duct`), registered as RRID:SCR_025436, and developed openly [1].

```{=latex}
\newpage
```

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
RSEs are the people who decide whether that work remains auditable: who preserve the context, make it discoverable, and keep capture cheap enough that nobody skips the step.

`con-duct` is one small piece of an answer: a wrapper that makes the agent's work, like the human's, leave a trace.
