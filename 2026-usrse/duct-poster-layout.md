# con/duct poster — layout plan (proposed)

Status: everything here is *proposed* until we hear the accepted-poster format from US-RSE (announced after acceptance, per the template).
The abstract (`duct-poster-draft.md`) is the submission; this file is our head start on the artifact itself.

## Organizing idea

One property, four moments.
The property: capture is unconditional and complete — anything you can run in a terminal passes through `duct` unchanged and leaves a full trace (stdout, stderr, resource timeline, metadata).
The cases: four moments where someone wishes that trace existed, each told as a small story (problem → command → real artifact → payoff).

## Sketch (landscape, ~4 columns)

```
+--------------------------------------------------------------------------+
| TITLE: Agent-friendly Provenance Capture with con-duct                   |
| authors / CON / Dartmouth          [QR: repo]  [QR: live poster/slides]  |
+--------------------+-----------------------------------------------------+
| SUMMARY (col 1)    | CASE 1: Provenance for the record                   |
|                    |   datalad run "duct mriqc ..."                      |
| terminal ──> duct  |   real ds000007-mriqc logs; con-duct plot figure    |
|   └─> 4 files:     |   payoff: resource picture months later, no rerun   |
|   stdout stderr    +-----------------------------------------------------+
|   info.json        | CASE 2: Size the next SLURM job                     |
|   usage.jsonl      |   last run's wall time + peak RSS -> next request   |
|                    |   payoff: measured numbers replace guesswork        |
| "anything passes   +-----------------------------------------------------+
|  through": binary, | CASE 3: The agent ran it; you can still audit it    |
|  pipeline, script, |   duct -m "tag" <cmd>  ...  con-duct ls -e "..."    |
|  whole process     |   payoff: exit codes + stderr are checkable;        |
|  tree              |   successor (human or agent) picks up the thread    |
|                    +-----------------------------------------------------+
| install: pip       | CASE 4: File the bug without re-running             |
| RRID, links        |   ls -e "exit_code != 0"; attach stderr + timeline  |
|                    |   payoff: expensive failure reported same day       |
+--------------------+-----------------------------------------------------+
| honesty box: when NOT to duct (tight loops; tty caveat) | acknowledgments |
+--------------------------------------------------------------------------+
```

Column count and case order are proposed; cases are modular panels, so reordering or dropping one is cheap.

## Case stories (each panel: problem → command → artifact → payoff)

1. **Provenance for the record** (the anchor case).
   Artifact: `con-duct plot` figure rendered from the real `ds000007-mriqc` duct logs, plus the `datalad run` one-liner.
2. **Size the next SLURM job.**
   Artifact: side-by-side of a guessed `#SBATCH --mem` versus the measured peak RSS from `info.json`.
3. **Agent-led, human-auditable.**
   Artifact: a short transcript excerpt — agent wraps a run with `-m`, later session retrieves it with `con-duct ls -e`, human spot-checks stderr.
4. **File the bug without re-running.**
   Artifact: the four log files annotated as "the complete attachment"; a resource timeline showing the RSS ramp before the failure.

## Honesty box (small, bottom)

- Sub-second commands: no samples land, four files still do — tight dev loops are not worth wrapping.
- Programs that check `isatty()` take their non-interactive path under duct (documented, with workarounds, in the README).
- POSIX-only (no Windows); `ps`-based sampling differs somewhat on macOS.
- `ps` numbers are approximate; exact accounting (cgroups, SLURM integration — con/duct#130) is planned.

## Assets needed (all generatable before acceptance)

- [ ] `con-duct plot` PNG from real ds000007-mriqc logs (fetch the `logs/duct/` dir from cerebra.fz-juelich.de)
- [ ] summary-panel diagram (terminal → duct → four files); mermaid or hand-drawn SVG
- [ ] agent-transcript excerpt for Case 3 (can be a real Claude Code session using the duct skill)
- [ ] QR codes (repo; live poster URL once known)
