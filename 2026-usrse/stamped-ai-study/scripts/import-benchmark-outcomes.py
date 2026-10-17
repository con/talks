#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Import committed summaries and render linked primary checklist scores."""
from __future__ import annotations

import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("experiments/retained-round-reporting/pooled/poster-outcomes.json")
CONFIG = SOURCE.parent.parent / "poster-pool.json"
COPY = ROOT / "data/benchmark-outcomes.json"
BINDING = ROOT / "data/benchmark-outcomes-source.json"
CHECKLIST_SOURCE = Path("experiments/narps-poster/checklists/index.json")
CHECKLIST_COPY = ROOT / "data/benchmark-checklists.json"
FIGURE_MANIFEST = Path("experiments/narps-poster/figures/poster-figure-manifest.json")
START = "<!-- BENCHMARK_OUTCOMES_START -->"
END = "<!-- BENCHMARK_OUTCOMES_END -->"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_rows(summary, checklists):
    rows = []
    runs = checklists["runs"]
    if len(runs) != 72 or len({run["run_id"] for run in runs}) != 72:
        raise ValueError("Expected one checklist slot for each of 72 research runs")
    for row in summary["conditions"]:
        group = [run for run in runs if run["condition"] == row["condition"]]
        if any(sum(run["round"] == number for run in group) != 6 for number in summary["retained_rounds"]):
            raise ValueError("Expected six assigned runs per condition and round")
        valid = []
        for run in group:
            score = run["evaluated_met_percent"]
            if score is None:
                if run["checklist_valid"] or run["app_url"] is not None or run["app_all_items_met_percent"] is not None:
                    raise ValueError("Unavailable checklist must not carry a score link")
                continue
            url = urlsplit(run["app_url"])
            if not run["checklist_valid"] or url.scheme != "https" or url.netloc != "checklist.stamped-principles.org":
                raise ValueError("Expected a valid primary checklist app URL")
            if not run["evaluated_count"] or abs(score - 100 * run["met_count"] / run["evaluated_count"]) > 1e-9:
                raise ValueError("Evaluated-item score and counts disagree")
            if run["all_item_count"] != 31 or abs(run["app_all_items_met_percent"] - 100 * run["met_count"] / 31) > 1e-9:
                raise ValueError("App score and all-item counts disagree")
            valid.append(run)
        if len(valid) != row["checklist_n"] or abs(sum(run["evaluated_met_percent"] for run in valid) / len(valid) - row["checklist_mean_met_percent"]) > 1e-9:
            raise ValueError("Individual scores do not reproduce the original condition summary")
        aggregate, = [item for item in checklists["conditions"] if item["condition"] == row["condition"]]
        mean = aggregate["app_all_items_mean_met_percent"]
        if aggregate["checklist_n"] != len(valid) or abs(mean - sum(run["app_all_items_met_percent"] for run in valid) / len(valid)) > 1e-9:
            raise ValueError("App-score mean differs from the exported individual scores")
        url = urlsplit(aggregate["checklist_list_url"])
        if (url.scheme != "https" or url.netloc != "github.com" or not url.fragment
                or url.path != "/leej3/stamped-in-practice/tree/codex/stamped-poster-analysis/experiments/narps-poster/checklists"):
            raise ValueError("Expected a condition checklist list in the benchmark")
        science = f'{row["science"]["supported"]}/{row["scientific_n"]}' if row["scientific_n"] else "—"
        replay = f'{row["replay_matched_n"]}/{row["replay_executed_n"]}' if row["replay_executed_n"] else "—"
        label = escape(f'{row["label"]}: mean app score {mean:.1f}% across {len(valid)} primary checklists; open the checklist list', quote=True)
        score = f'<a href="{escape(aggregate["checklist_list_url"], quote=True)}" title="{label}" aria-label="{label}">{mean:.1f}%</a><br>n={len(valid)}'
        rows.append(f'<tr><th scope="row">{escape(row["label"])}</th><td>{row["assigned_runs"]}</td><td>{science}</td><td>{replay}</td><td>{score}</td></tr>')
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
        figure_manifest = json.loads((benchmark / FIGURE_MANIFEST).read_text())
        checklist_entry, = [row for row in figure_manifest["sources"] if row["path"] == CHECKLIST_SOURCE.as_posix()]
        if digest(benchmark / CHECKLIST_SOURCE) != checklist_entry["sha256"]:
            raise ValueError("Checklist export differs from the benchmark figure manifest")
        subprocess.run(["git", "-C", str(benchmark), "ls-files", "--error-unmatch", "--", str(CHECKLIST_SOURCE), str(FIGURE_MANIFEST)], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["git", "-C", str(benchmark), "diff", "--quiet", "HEAD", "--", str(CHECKLIST_SOURCE), str(FIGURE_MANIFEST)], check=True)
        COPY.parent.mkdir(parents=True, exist_ok=True)
        COPY.write_bytes(source.read_bytes())
        CHECKLIST_COPY.write_bytes((benchmark / CHECKLIST_SOURCE).read_bytes())
        BINDING.write_text(json.dumps({
            "schema_version": 2,
            "repository": "https://github.com/leej3/stamped-in-practice",
            "branch": "codex/stamped-poster-analysis", "revision": revision,
            "source": SOURCE.as_posix(), "sha256": digest(COPY),
            "checklists": {"source": CHECKLIST_SOURCE.as_posix(), "sha256": digest(CHECKLIST_COPY),
                           "manifest": FIGURE_MANIFEST.as_posix(), "manifest_sha256": digest(benchmark / FIGURE_MANIFEST)},
            "scope": "Display copy; aggregation and run-level evidence remain in the benchmark.",
        }, indent=2) + "\n")
    binding = json.loads(BINDING.read_text())
    if digest(COPY) != binding["sha256"]:
        raise ValueError("Poster outcome display copy changed")
    if digest(CHECKLIST_COPY) != binding["checklists"]["sha256"]:
        raise ValueError("Poster checklist display copy changed")
    summary = json.loads(COPY.read_text())
    rows = table_rows(summary, json.loads(CHECKLIST_COPY.read_text()))
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
