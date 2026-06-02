#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Generated with Claude Code 2.1.159 / Claude Opus 4.7
"""Dump issues and PRs of a GitHub repo to YAML for offline summarisation.

Usage:
    fetch_repo.py <owner/repo> <outdir> [--label LABEL]

Requires `gh` CLI to be authenticated (run `gh auth login` or set GH_TOKEN).
Writes:
    <outdir>/issues<-suffix>.yaml
    <outdir>/prs<-suffix>.yaml
where <-suffix> is "-<label>" if --label was given, else empty.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


ISSUE_FIELDS = (
    "number,title,state,labels,author,assignees,createdAt,updatedAt,closedAt,"
    "body,comments,url"
)
PR_FIELDS = (
    "number,title,state,labels,author,assignees,createdAt,updatedAt,closedAt,"
    "mergedAt,body,comments,reviews,url,isDraft,mergedBy,headRefName,baseRefName"
)


def run_gh(args: list[str]) -> Any:
    """Run gh CLI and return parsed JSON output."""
    cmd = ["gh", *args]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        sys.stderr.write(
            f"gh failed: {' '.join(cmd)}\nstderr: {result.stderr}\n"
        )
        sys.exit(result.returncode)
    return json.loads(result.stdout) if result.stdout.strip() else []


def slim_user(u: Any) -> str | None:
    """Reduce a user object to just the login (or None)."""
    if not u:
        return None
    if isinstance(u, dict):
        return u.get("login") or u.get("name")
    return str(u)


def slim_label(lbl: Any) -> str:
    if isinstance(lbl, dict):
        return lbl.get("name", "")
    return str(lbl)


def slim_comment(c: dict) -> dict:
    return {
        "author": slim_user(c.get("author")),
        "createdAt": c.get("createdAt"),
        "body": c.get("body", ""),
    }


def slim_review(r: dict) -> dict:
    return {
        "author": slim_user(r.get("author")),
        "state": r.get("state"),
        "submittedAt": r.get("submittedAt"),
        "body": r.get("body", ""),
    }


def slim_issue(it: dict) -> dict:
    return {
        "number": it["number"],
        "title": it.get("title", ""),
        "state": it.get("state"),
        "url": it.get("url"),
        "author": slim_user(it.get("author")),
        "assignees": [slim_user(a) for a in it.get("assignees") or []],
        "labels": [slim_label(l) for l in it.get("labels") or []],
        "createdAt": it.get("createdAt"),
        "updatedAt": it.get("updatedAt"),
        "closedAt": it.get("closedAt"),
        "body": it.get("body", ""),
        "comments": [slim_comment(c) for c in it.get("comments") or []],
    }


def slim_pr(pr: dict) -> dict:
    out = slim_issue(pr)
    out["mergedAt"] = pr.get("mergedAt")
    out["mergedBy"] = slim_user(pr.get("mergedBy"))
    out["isDraft"] = pr.get("isDraft")
    out["headRefName"] = pr.get("headRefName")
    out["baseRefName"] = pr.get("baseRefName")
    out["reviews"] = [slim_review(r) for r in pr.get("reviews") or []]
    return out


def dump_yaml(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(
            data,
            f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=100000,
        )


def fetch_issues(repo: str, label: str | None) -> list[dict]:
    args = [
        "issue", "list",
        "--repo", repo,
        "--state", "all",
        "--limit", "1000",
        "--json", ISSUE_FIELDS,
    ]
    if label:
        args += ["--label", label]
    raw = run_gh(args)
    return [slim_issue(it) for it in raw]


def fetch_prs(repo: str, label: str | None) -> list[dict]:
    args = [
        "pr", "list",
        "--repo", repo,
        "--state", "all",
        "--limit", "1000",
        "--json", PR_FIELDS,
    ]
    if label:
        args += ["--label", label]
    raw = run_gh(args)
    return [slim_pr(pr) for pr in raw]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("repo", help="owner/repo, e.g. bids-standard/bids-2-devel")
    ap.add_argument("outdir", help="output directory")
    ap.add_argument("--label", default=None, help="only items with this label")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    suffix = f"-{args.label}" if args.label else ""

    sys.stderr.write(f"Fetching issues for {args.repo}"
                     f"{f' (label={args.label})' if args.label else ''}...\n")
    issues = fetch_issues(args.repo, args.label)
    sys.stderr.write(f"  -> {len(issues)} issues\n")
    dump_yaml(issues, outdir / f"issues{suffix}.yaml")

    sys.stderr.write(f"Fetching PRs for {args.repo}"
                     f"{f' (label={args.label})' if args.label else ''}...\n")
    prs = fetch_prs(args.repo, args.label)
    sys.stderr.write(f"  -> {len(prs)} PRs\n")
    dump_yaml(prs, outdir / f"prs{suffix}.yaml")

    return 0


if __name__ == "__main__":
    sys.exit(main())
