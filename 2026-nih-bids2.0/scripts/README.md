# BIDS 2.0 GitHub state dumper

Helpers used by `Makefile` in the parent directory.

## Prerequisites

- Python 3.10+ with `PyYAML` (`pip install pyyaml`)
- `gh` CLI authenticated for `github.com`:
  - either run `gh auth login`,
  - or export `GH_TOKEN` (a classic PAT with `read:project` for the Project
    fetch, or a fine-grained PAT with org Projects "Read" permission).

The scripts deliberately do **not** source any token themselves; they rely on
whatever `gh` already has configured.

## Usage

```
make sync                # all three sources
make sync-bids-2-devel   # bids-standard/bids-2-devel
make sync-bids-spec      # label:bids-2.0 items in bids-standard/bids-specification
make sync-project        # ProjectV2 #10 of org bids-standard
make clean               # rm -rf data/
```

Outputs land under `../data/`:

```
data/
  bids-2-devel/issues.yaml
  bids-2-devel/prs.yaml
  bids-specification/issues-bids-2.0.yaml
  bids-specification/prs-bids-2.0.yaml
  project-10/items.yaml
  fetched-at.txt
```

Re-running `make sync` overwrites everything; the dumps are idempotent.

## Caveats

- The Project fetch requires extra scope. If the token lacks it, `items.yaml`
  is written with an `error:` field and an empty `items:` list — `make` still
  exits 0 so the rest of the pipeline keeps working.
- `gh issue list` / `gh pr list` cap at `--limit 1000`; if the repos grow past
  that, switch to paginated REST API.
- Reactions, avatar URLs, and GitHub node IDs are stripped intentionally to
  keep the YAML human/LLM readable.
