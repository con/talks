#!/bin/bash
# Validate the sample xyzri records (PLAN.md §5) against the
# demo-research-information schema that has the drafted XYZEvent /
# XYZPresentation additions, then check that references resolve.
#
# Usage: validate.sh DATALAD_CONCEPTS_CHECKOUT [CON_SITE_SPECIFIC_CHECKOUT]
#
# DATALAD_CONCEPTS_CHECKOUT: yarikoptic/datalad-concepts at branch
#   claude/serene-cray-ozqirg, switched to local imports (`make imports-local`),
#   with linkml installed and patched (`tools/patch_linkml`).
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
schema="$1/src/demo-research-information/unreleased.yaml"
rc=0
for d in "$here"/xyzri/*/; do
    cls="$(basename "$d")"
    for f in "$d"*.yaml; do
        out="$(linkml-validate -s "$schema" -C "$cls" "$f" 2>&1)" || true
        if [ "$(echo "$out" | tail -n1)" = "No issues found" ]; then
            echo "ok    $cls/$(basename "$f")"
        else
            echo "FAIL  $cls/$(basename "$f")"; echo "$out" | sed 's/^/      /'; rc=1
        fi
    done
done
python3 "$here/check_refs.py" "$here/xyzri" ${2:+"$2/metadata/records"} || rc=1
exit $rc
