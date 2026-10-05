#!/usr/bin/env python3
"""Report references in the sample records that resolve to no record.

Usage: check_refs.py SAMPLE_RECORDS_DIR [CON_SITE_SPECIFIC_RECORDS_DIR]
"""
import sys
from pathlib import Path

import yaml

REF_KEYS = {"object", "kind", "roles", "part_of"}


def pids(root):
    docs = (yaml.safe_load(f.read_text()) for f in Path(root).rglob("*.yaml"))
    return {d["pid"] for d in docs if isinstance(d, dict) and "pid" in d}


def refs(node, key=None):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from refs(v, k)
    elif isinstance(node, list):
        for v in node:
            yield from refs(v, key)
    elif key in REF_KEYS and isinstance(node, str):
        yield key, node


known = pids(sys.argv[1])
if len(sys.argv) > 2:
    known |= pids(sys.argv[2])
missing = {}
for f in sorted(Path(sys.argv[1]).rglob("*.yaml")):
    for key, ref in refs(yaml.safe_load(f.read_text())):
        if ref not in known:
            missing.setdefault(ref, []).append(f"{f.parent.name}/{f.name}:{key}")
for ref, where in sorted(missing.items()):
    print(f"unresolved  {ref}  <- {', '.join(where)}")
print(f"{len(missing)} unresolved reference(s)")
