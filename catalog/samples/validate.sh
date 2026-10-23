#!/bin/bash
# Validate the samples (PLAN.md §7):
#  1. samples/talks.yaml against the draft talks schema
#     (catalog/talks.py validate: JSON Schema generated from
#     catalog/talks.schema.yaml + references, files, ids);
#  2. the exported xyzri records against the demo-research-information
#     schema with the drafted XYZEvent / XYZPresentation additions;
#  3. references in the exported records.
#
# Usage: validate.sh DATALAD_CONCEPTS_CHECKOUT [CON_SITE_SPECIFIC_CHECKOUT]
#
# DATALAD_CONCEPTS_CHECKOUT: yarikoptic/datalad-concepts at branch
#   claude/serene-cray-ozqirg, switched to local imports (`make imports-local`),
#   with linkml installed and patched (`tools/patch_linkml`).
# Requires: pyyaml, jsonschema, linkml (linkml-validate).
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
schema="$1/src/demo-research-information/unreleased.yaml"
rc=0
echo "== talks.yaml"
python3 "$here/../talks.py" validate "$here/talks.yaml" ${2:+--site "$2"} || rc=1
echo "== xyzri records"
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
echo "== xyzri references"
python3 "$here/check_refs.py" "$here/xyzri" ${2:+"$2/metadata/records"} || rc=1
exit $rc
