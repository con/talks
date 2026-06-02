#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Yaroslav Halchenko <yaroslav.o.halchenko@dartmouth.edu>
# SPDX-License-Identifier: MIT
#
# Generated with Claude Code 2.1.159 / Claude Opus 4.7
"""Dump an organisation ProjectV2 (new GitHub Projects) to YAML.

Usage:
    fetch_project.py <org> <project_number> <outpath>

Requires `gh` CLI auth with read:project (or the equivalent in a fine-grained
PAT: organization "Projects" -> Read). Without it the project query returns
null and this script writes an empty/error placeholder so the rest of the
pipeline can keep going.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml


QUERY = """
query($org: String!, $number: Int!, $cursor: String) {
  organization(login: $org) {
    projectV2(number: $number) {
      title
      url
      number
      fields(first: 50) {
        nodes {
          ... on ProjectV2FieldCommon { id name dataType }
          ... on ProjectV2SingleSelectField {
            id name dataType options { id name }
          }
        }
      }
      items(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          type
          fieldValues(first: 30) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                field { ... on ProjectV2FieldCommon { name } }
                name
              }
              ... on ProjectV2ItemFieldTextValue {
                field { ... on ProjectV2FieldCommon { name } }
                text
              }
              ... on ProjectV2ItemFieldNumberValue {
                field { ... on ProjectV2FieldCommon { name } }
                number
              }
              ... on ProjectV2ItemFieldDateValue {
                field { ... on ProjectV2FieldCommon { name } }
                date
              }
              ... on ProjectV2ItemFieldIterationValue {
                field { ... on ProjectV2FieldCommon { name } }
                title
              }
              ... on ProjectV2ItemFieldLabelValue {
                field { ... on ProjectV2FieldCommon { name } }
                labels(first: 20) { nodes { name } }
              }
            }
          }
          content {
            __typename
            ... on Issue {
              number title state url
              repository { nameWithOwner }
              labels(first: 20) { nodes { name } }
            }
            ... on PullRequest {
              number title state url isDraft merged
              repository { nameWithOwner }
              labels(first: 20) { nodes { name } }
            }
            ... on DraftIssue { title body }
          }
        }
      }
    }
  }
}
"""


def run_gh_graphql(query: str, variables: dict[str, Any]) -> dict:
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for k, v in variables.items():
        if v is None:
            continue
        flag = "-F" if isinstance(v, int) else "-f"
        cmd += [flag, f"{k}={v}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        sys.stderr.write(
            f"gh graphql failed: stderr: {result.stderr}\n"
        )
        sys.exit(result.returncode)
    return json.loads(result.stdout)


def slim_field_value(fv: dict) -> dict | None:
    field = fv.get("field") or {}
    name = field.get("name")
    if not name:
        return None
    if "name" in fv and fv["name"] is not None and "options" not in field:
        # single-select
        return {"field": name, "value": fv["name"]}
    if "text" in fv and fv["text"] is not None:
        return {"field": name, "value": fv["text"]}
    if "number" in fv and fv["number"] is not None:
        return {"field": name, "value": fv["number"]}
    if "date" in fv and fv["date"] is not None:
        return {"field": name, "value": fv["date"]}
    if "title" in fv and fv["title"] is not None:
        return {"field": name, "value": fv["title"]}
    if "labels" in fv:
        return {
            "field": name,
            "value": [l["name"] for l in fv["labels"]["nodes"]],
        }
    return None


def slim_content(c: dict | None) -> dict:
    if not c:
        return {"type": "Unknown"}
    t = c.get("__typename")
    out: dict[str, Any] = {"type": t}
    if t in ("Issue", "PullRequest"):
        out.update({
            "repo": (c.get("repository") or {}).get("nameWithOwner"),
            "number": c.get("number"),
            "title": c.get("title"),
            "state": c.get("state"),
            "url": c.get("url"),
            "labels": [l["name"] for l in (c.get("labels") or {}).get("nodes", [])],
        })
        if t == "PullRequest":
            out["isDraft"] = c.get("isDraft")
            out["merged"] = c.get("merged")
    elif t == "DraftIssue":
        out.update({"title": c.get("title"), "body": c.get("body")})
    return out


def slim_item(node: dict) -> dict:
    fvs = []
    for fv in (node.get("fieldValues") or {}).get("nodes", []):
        s = slim_field_value(fv)
        if s:
            fvs.append(s)
    return {
        "content": slim_content(node.get("content")),
        "fields": fvs,
    }


def fetch_all_items(org: str, number: int) -> dict:
    cursor: str | None = None
    items: list[dict] = []
    meta: dict[str, Any] = {}
    fields: list[dict] = []
    while True:
        data = run_gh_graphql(QUERY, {"org": org, "number": number, "cursor": cursor})
        proj = (data.get("data") or {}).get("organization", {}).get("projectV2")
        if proj is None:
            return {
                "error": (
                    "projectV2 returned null — your gh token lacks 'read:project' "
                    "scope (or fine-grained PAT 'Projects' permission) for "
                    f"org {org}. The project is at "
                    f"https://github.com/orgs/{org}/projects/{number}"
                ),
                "items": [],
            }
        if not meta:
            meta = {
                "title": proj.get("title"),
                "url": proj.get("url"),
                "number": proj.get("number"),
            }
            fields = [
                {
                    "name": f.get("name"),
                    "dataType": f.get("dataType"),
                    "options": [o["name"] for o in (f.get("options") or [])] or None,
                }
                for f in (proj.get("fields") or {}).get("nodes", [])
                if f.get("name")
            ]
        page = proj["items"]
        for n in page["nodes"]:
            items.append(slim_item(n))
        if page["pageInfo"]["hasNextPage"]:
            cursor = page["pageInfo"]["endCursor"]
        else:
            break
    return {**meta, "fields": fields, "items": items}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("org")
    ap.add_argument("number", type=int)
    ap.add_argument("outpath")
    args = ap.parse_args()

    sys.stderr.write(f"Fetching project {args.org}/{args.number}...\n")
    data = fetch_all_items(args.org, args.number)
    if "error" in data:
        sys.stderr.write(f"  WARNING: {data['error']}\n")
    else:
        sys.stderr.write(f"  -> {len(data['items'])} items\n")

    outpath = Path(args.outpath)
    outpath.parent.mkdir(parents=True, exist_ok=True)
    with outpath.open("w", encoding="utf-8") as f:
        yaml.safe_dump(
            data,
            f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=100000,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
