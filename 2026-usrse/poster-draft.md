# Agent-friendly Provenance Capture with `con-duct`

## Presenters

- Austin Macdonald \<austin.s.macdonald@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-8124-807X
- Cody C. Baker \<cody.c.baker.phd@gmail.com\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-0829-4790
- Isaac To \<Isaac.C.To@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0002-4740-0824
- Yaroslav O. Halchenko \<yaroslav.o.halchenko@dartmouth.edu\>, Department of Psychological and Brain Sciences, Dartmouth College / Center for Open Neuroscience, ORCID 0000-0003-3456-2493

## Keywords

agentic workflows, provenance, reproducibility, resource monitoring, HPC

## Abstract

Agents and humans now routinely execute commands side-by-side.
Whether developing workflows, exploring datasets, invoking analysis tools, or chaining outputs through pipelines, the outputs of tool usage are critical information.
The provenance problem of agent-driven work cuts two ways: command outputs need to be *captured* automatically as they happen, and need to be *operable on* later, by the originating agent, a successor agent, or the human reviewer.

Three inefficiencies recur that `con-duct` can help with.
 - An agent runs `cmd | grep ...`; the unfiltered stdout is gone.
 - An agent pipes to an ad-hoc `/tmp/` file with no metadata; nobody can find it again.
 - A human runs a command and copy-pastes a slice of output into an agent's context; the agent operates on only what the human chose to share, and the rest is, again, gone.

`con-duct` closes both halves of the loop with the same wrapper.
`con-duct run` (or `duct` for convenience) handles the capture:
 - Invoked as `duct -m "tag" <cmd>`, it streams full stdout and stderr to disk, polls the process group for resource usage at a configurable interval, and writes metadata recording the command, environment, wall clock time, peak RSS, and exit code.
 - Capture is automatic and identical whether the runner is a human in a terminal or an agent calling out via tool use.
 - The core monitor depends only on the Python standard library and needs no elevated privileges, so it works the same on a laptop, inside a container, or on an HPC compute node (`--mode current-session` for SLURM-tracked sessions).

The companion `con-duct ls` provides discovery:
Its `-e` flag takes a Python expression over any captured field, so a later agent or human can retrieve runs by whatever dimension turns out to matter:
 - `con-duct ls -e "message=='<tag>'"` — by the `-m` tag attached at runtime.
 - `con-duct ls -e "re.search('fmriprep', command)"` — by a regex over the command string.
 - `con-duct ls -e "exit_code != 0"` — all failures.
 - `con-duct ls -e "peak_rss > 8e9"` — runs that exceeded a memory budget.
 - `con-duct ls -e "wall_clock_time > 3600 and hostname=='cluster-node-7'"` — long runs on a specific host.

From any match, the full captured stdout, stderr, and resource samples are recoverable on disk — even when no one knew at runtime that those outputs would be needed.
Aggregated across runs, the resource statistics, exit codes, and wall times surface patterns: a tool that OOMs near four hours, a regression in runtime, a flaky exit under specific inputs.

For research outputs where provenance is the point, the same wrapper composes with DataLad: `datalad run -m "..." "duct <cmd> ..."` produces a git commit binding inputs, command, and outputs with the duct logs alongside.
On HPC this matters twice over — resource usage from prior runs directly informs what to request for the next SLURM job, replacing the usual guesswork.
A public MRIQC dataset (`ds000007-mriqc`) ships its `logs/duct/` directory, so `con-duct ls` and `con-duct plot` reproduce the resource picture of a completed `fmriprep` run months after the fact, without re-executing the pipeline.

`con-duct` is available on PyPI (`pip install con-duct`), registered as RRID:SCR_025436, and developed openly at <https://github.com/con/duct>.

## Acknowledgments

We thank the broader Center for Open Neuroscience and DataLad communities for ongoing feedback on `con-duct`'s design and use.

*AI-assisted content disclosure (per IEEE policy).* This submission was prepared with assistance from Anthropic's Claude (model: `claude-opus-4-7`, accessed via the Claude Code CLI in May 2026).
The AI system contributed to drafting prose in the Abstract and Connection-to-Mission sections; the human authors specified the content, edited the prose, and verified all technical claims, command examples, figures, and references.
The `con-duct` software described in this work was also developed with substantial assistance from the same Claude model family across multiple sessions during 2024–2026, used by the authors for code generation, refactoring, and review; all merged code was reviewed by the human authors before commit.

## References

*(to finalize; candidates below)*

1. `con-duct` — Center for Open Neuroscience. <https://github.com/con/duct>. RRID:SCR_025436.
2. Macdonald, A. *An intro-duct-tion to con-duct.* DataLad blog, 2024. <https://blog.datalad.org/posts/intro-duct-tion/>
3. DataLad — Halchenko, Y. O. et al. <https://www.datalad.org/>
4. brainlife `smon`. <https://github.com/brainlife/abcd-spec/blob/master/hooks/smon>
5. ReproNim / ReproMan. <https://github.com/ReproNim/reproman>
6. Esteban, O. et al. *fMRIPrep: a robust preprocessing pipeline for functional MRI.* Nature Methods, 2019.
7. `ds000007-mriqc` (Hoffstaedter / cerebra.fz-juelich.de). <https://cerebra.fz-juelich.de/f.hoffstaedter/ds000007-mriqc>
8. *con/demos sfn-2025: duct + DataLad demo.* <https://github.com/con/demos/tree/main/sfn-2025>

## Connection to Mission, Goals, & Interests of US-RSE Community

*(< 300 words — to draft next.)*
