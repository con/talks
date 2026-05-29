# Agent-friendly Provenance Capture with `con-duct`

## Presenters

- Austin Macdonald \<austin.s.macdonald@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-8124-807X
- Cody C. Baker \<cody.c.baker.phd@gmail.com\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-0829-4790
- Isaac To \<Isaac.C.To@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-4740-0824
- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0003-3456-2493

## Keywords

agentic workflows, provenance, reproducibility, resource monitoring, HPC

## Abstract

Agents and humans now routinely execute commands side-by-side, whether developing workflows, exploring datasets, invoking analysis tools, or chaining outputs through pipelines.
The outputs of those commands are often worth keeping, whether to refer back to, to compare against, or to hand to a successor.
By default they vanish the moment the terminal scrolls or the agent's context rolls over.

In development and exploration, this is a context problem.
A command's full stdout, its exit status, how long it took, and the resources used are exactly the breadcrumbs a successor (human or agent) needs to pick up where the last one left off, and the cost of capturing them is small enough that there is no reason not to.
 - Did we get that warning last time we ran that command?
 - Did this run take longer?

For research outputs the stakes change.
Capture becomes provenance: a record of what was run, against what inputs, producing what outputs, with which resources.
The same recording does double duty on HPC, where the measured wall time and peak memory from earlier runs are the cheapest possible input to the next SLURM request, replacing the usual guesswork.

`con-duct` closes both halves of the loop with the same wrapper.
`con-duct run` (or `duct` for convenience) handles the capture:
 - Invoked as `duct -m "searchable message/tag" <cmd>`, it streams full stdout and stderr to disk, polls the process group for resource usage at a configurable interval, and writes metadata recording the command, environment, wall clock time, peak RSS, and exit code.
 - Capture is automatic and identical whether the runner is a human in a terminal or an agent calling out via tool use.
 - The core monitor depends only on the Python standard library and needs no elevated privileges, so it works the same on a laptop, inside a container, or on an HPC compute node (`--mode current-session` for SLURM-tracked sessions).

The companion `con-duct ls` provides discovery:
Its `-e` flag takes a Python expression over any captured field, so a later agent or human can retrieve runs by whatever dimension turns out to matter:
 - `con-duct ls -e "message=='<tag>'"` retrieves runs by their `-m` tag.
 - `con-duct ls -e "re.search('fmriprep', command)"` matches the command string against a regex.
 - `con-duct ls -e "exit_code != 0"` lists all failures.
 - `con-duct ls -e "peak_rss > 8e9"` finds runs that exceeded a memory budget.
 - `con-duct ls -e "wall_clock_time > 3600 and hostname=='cluster-node-7'"` narrows to long runs on a specific host.

From any match, the full captured stdout, stderr, and resource samples are recoverable on disk, even when no one knew at runtime that those outputs would be needed.
Aggregated across runs, the resource statistics, exit codes, and wall times surface patterns: performance issues, a regression in runtime, a flaky exit under specific inputs.
The same wrapper composes with DataLad: `datalad run "duct <cmd> ..."` produces a git commit binding inputs, command, and outputs with the duct logs alongside.
MRIQC is a neuroimaging quality-control pipeline, a typical HPC workload.
Hoffstaedter's `ds000007-mriqc` dataset ships a `logs/duct/` directory alongside its MRIQC outputs (<https://cerebra.fz-juelich.de/f.hoffstaedter/ds000007-mriqc/src/branch/base/logs/duct/>), so `con-duct ls` and `con-duct plot` reproduce the resource picture of a completed `mriqc` run months after the fact, without re-executing the pipeline.

`con-duct` is available on PyPI (`pip install con-duct`), registered as RRID:SCR_025436, and developed openly at <https://github.com/con/duct>.

## Acknowledgments

We thank the broader ReproNim and OpenNeuro communities for ongoing feedback on `con-duct`'s design and use.
`con-duct`'s resource-monitoring approach is based on brainlife's `smon` (<https://github.com/brainlife/abcd-spec/blob/master/hooks/smon>).

*AI-assisted content disclosure (per IEEE policy).* This submission was prepared with assistance from Anthropic's Claude (model: `claude-opus-4-7`, accessed via the Claude Code CLI in May 2026).
The AI system contributed to drafting prose in the Abstract and Connection-to-Mission sections. The human authors specified the content, edited the prose, and verified all technical claims, command examples, figures, and references.
The `con-duct` software described in this work was also developed with assistance from the multiple agents used by the authors for code generation, refactoring, and review. All merged code was reviewed by the human authors.

## References

1. `con-duct`. Center for Open Neuroscience. <https://github.com/con/duct>. RRID:SCR_025436.
2. DataLad. <https://www.datalad.org/>. RRID:SCR_003931.
3. brainlife `smon`. <https://github.com/brainlife/abcd-spec/blob/master/hooks/smon>
4. Hoffstaedter, F. `ds000007-mriqc`. <https://cerebra.fz-juelich.de/f.hoffstaedter/ds000007-mriqc>

## Connection to Mission, Goals, & Interests of US-RSE Community

Maturing conventions, increasingly capable tooling, and the arrival of AI agents bring rigor, reproducibility, reusability, and efficiency within closer reach than ever.
US-RSE represents the researchers and engineers who build, maintain, and sustain the software that turns that potential into practice.
`con-duct` was built by RSEs at the Center for Open Neuroscience for precisely that audience: a small, dependency-light tool that captures what a command actually did, so the next person (or agent) can pick up where the last one left off without rerunning.
That is the day-to-day texture of research-software work: handing off enough context for someone else to act, and doing it cheaply enough that nobody skips the step.

The conference theme, *Advancing Science in the Age of AI*, sharpens this concern.
As LLM agents take on more of the executing (writing throwaway pipelines, exploring datasets, calling tools), RSEs are the people who decide whether that work remains auditable.
`con-duct` is one small piece of an answer: a wrapper that makes the agent's work, like the human's, leave a trace.

The project is openly developed at <https://github.com/con/duct>, registered (RRID:SCR_025436), and composes with the broader ecosystem of RSE-built tools we depend on (DataLad, BIDS, fmriprep, ReproNim/containers), rather than reinventing them.
We hope to find collaborators at US-RSE working on adjacent pieces of this puzzle.
