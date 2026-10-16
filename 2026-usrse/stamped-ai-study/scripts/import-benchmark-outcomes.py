#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Import a committed benchmark summary and render its four poster rows."""
from __future__ import annotations

import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("experiments/retained-round-reporting/pooled/poster-outcomes.json")
CONFIG = SOURCE.parent.parent / "poster-pool.json"
COPY = ROOT / "data/benchmark-outcomes.json"
BINDING = ROOT / "data/benchmark-outcomes-source.json"
START = "<!-- BENCHMARK_OUTCOMES_START -->"
END = "<!-- BENCHMARK_OUTCOMES_END -->"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_rows(summary):
    rows = []
    for row in summary["conditions"]:
        science = f'{row["science"]["supported"]}/{row["scientific_n"]}' if row["scientific_n"] else "—"
        replay = f'{row["replay_matched_n"]}/{row["replay_executed_n"]}' if row["replay_executed_n"] else "—"
        score = (f'{row["checklist_mean_met_percent"]:.1f}%<br>n={row["checklist_n"]}'
                 if row["checklist_n"] else "—")
        rows.append(f'<tr><th>{escape(row["label"])}</th><td>{row["assigned_runs"]}</td><td>{science}</td><td>{replay}</td><td>{score}</td></tr>')
    if len(rows) != 4:
        raise ValueError("Expected four assistance conditions")
    return "\n".join("                " + row for row in rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark", type=Path)
    args = parser.parse_args()
    if args.benchmark:
        benchmark = args.benchmark.resolve()
        source = benchmark / SOURCE
        summary = json.loads(source.read_text())
        paths = [SOURCE, CONFIG, Path("scripts/summarize_poster_outcomes.py")]
        for row in summary["sources"]:
            relative = Path(row["path"])
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError("Summary source escapes its experiment directory")
            path = CONFIG.parent / relative
            if digest(benchmark / path) != row["sha256"]:
                raise ValueError("Summary input changed: " + str(path))
            paths.append(path)
        if digest(benchmark / CONFIG) != summary["config_sha256"]:
            raise ValueError("Summary configuration changed")
        if digest(benchmark / "scripts/summarize_poster_outcomes.py") != summary["generator_sha256"]:
            raise ValueError("Summary generator changed")
        subprocess.run(["git", "-C", str(benchmark), "ls-files", "--error-unmatch", "--", *map(str, paths)], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["git", "-C", str(benchmark), "diff", "--quiet", "HEAD", "--", *map(str, paths)], check=True)
        revision = subprocess.check_output(["git", "-C", str(benchmark), "rev-parse", "HEAD"], text=True).strip()
        COPY.parent.mkdir(parents=True, exist_ok=True)
        COPY.write_bytes(source.read_bytes())
        BINDING.write_text(json.dumps({
            "schema_version": 1,
            "repository": "https://github.com/leej3/stamped-in-practice",
            "branch": "codex/stamped-poster-analysis", "revision": revision,
            "source": SOURCE.as_posix(), "sha256": digest(COPY),
            "scope": "Display copy; aggregation and run-level evidence remain in the benchmark.",
        }, indent=2) + "\n")
    binding = json.loads(BINDING.read_text())
    if digest(COPY) != binding["sha256"]:
        raise ValueError("Poster outcome display copy changed")
    summary = json.loads(COPY.read_text())
    rows = table_rows(summary)
    rounds = summary["retained_rounds"]
    description = "Rounds " + ", ".join(map(str, rounds)) + f'; {sum(row["assigned_runs"] for row in summary["conditions"])} research runs.'
    html_path = ROOT / "index.html"
    html = html_path.read_text()
    block = START + "\n" + rows + "\n                " + END
    rendered, count = re.subn(re.escape(START) + ".*?" + re.escape(END), lambda _: block, html, flags=re.S)
    if count != 1:
        raise ValueError("Expected one benchmark outcome table")
    rendered, count = re.subn(r'(<span id="retained-rounds">).*?(</span>)', lambda m: m[1] + description + m[2], rendered)
    if count != 1:
        raise ValueError("Expected one retained-round description")
    if args.benchmark:
        html_path.write_text(rendered)
    elif rendered != html:
        raise ValueError("Poster table differs from its benchmark summary; reimport it")
    print(json.dumps({"verified_condition_rows": 4, "retained_rounds": rounds, "benchmark_revision": binding["revision"]}))


if __name__ == "__main__":
    main()
