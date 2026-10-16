#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Center for Open Neuroscience
# SPDX-License-Identifier: Apache-2.0
"""Freeze the completed NARPS worker outputs used by the poster figures.

Run explicitly against existing worker checkouts and coordinator capture records.
This copies no participant images and never reruns or modifies the study.
Rendering the committed snapshot uses render-narps-figures.py and needs no network.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

import nibabel as nib
import nilearn
from nilearn import datasets, image


POSTER = Path(__file__).resolve().parents[1]
SNAPSHOT = POSTER / "data" / "narps-2026-10-15"
REPOSITORY = "https://github.com/leej3/stamped-in-practice"
SUMMARIES = {
    "01": "analysis_summary.json",
    "02": "results.json",
    "03": "summary.json",
    "05": "run_summary.json",
    "06": "analysis_results.json",
    "07": "analysis_results.json",
    "08": "analysis_summary.json",
    "09": "results.json",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(path: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(path), *args], text=True).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers-root", type=Path, required=True)
    parser.add_argument("--capture-root", type=Path, required=True)
    parser.add_argument("--snapshot-utc", required=True,
                        help="UTC cutoff for selecting completed results")
    args = parser.parse_args()
    SNAPSHOT.mkdir(parents=True, exist_ok=True)
    sources: dict[str, dict] = {}
    records = []

    def copy_source(worker: Path, relative: str, destination: str) -> Path:
        src = worker / relative
        dst = SNAPSHOT / destination
        revision = git(worker, "rev-parse", "HEAD")
        if git(worker, "status", "--porcelain", "--", relative):
            raise ValueError(f"Source is not a clean committed file: {src}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        sources[destination] = {
            "sha256": sha256(dst),
            "bytes": dst.stat().st_size,
            "source_repository": REPOSITORY,
            "source_revision": revision,
            "source_path": relative,
            "source_git_object": git(worker, "rev-parse", f"HEAD:{relative}"),
            "source_url": f"{REPOSITORY}/blob/{revision}/{relative}",
            "transformation": "byte-for-byte copy; annex symlinks dereferenced",
        }
        if src.is_symlink():
            sources[destination]["source_annex_key"] = src.readlink().name
        return dst

    for number, filename in SUMMARIES.items():
        run = f"narps-r1-{number}"
        worker = args.workers_root / run
        assignment_path = args.capture_root / run / "launch/native/condition-assignment.json"
        assignment = json.loads(assignment_path.read_text())
        summary_path = copy_source(worker, f"results/{filename}", f"summaries/{run}.json")
        d = json.loads(summary_path.read_text())
        condition = assignment["condition"]
        if number == "01":
            mask, positive = d["voxels_tested"], d["parametric_bonferroni_fwe05_voxels"]
        elif number == "02":
            mask = d["analysis_mask_voxels"]
            positive = d["whole_brain_bonferroni_fwe_voxels_p_lt_0.05"]
        elif number == "03":
            mask, positive = d["analysis_voxels"], d["n_whole_brain_fwer_significant"]
        elif number == "05":
            mask = d["mask_voxels_common_nonzero"]
            positive = d["test"]["positive_whole_brain_fwe_significant_voxels"]
        elif number == "06":
            mask = d["analysis"]["mask_voxels"]
            positive = d["analysis"]["whole_brain_fwe05_voxel_count"]
        elif number == "07":
            mask, positive = d["whole_brain_voxels"], d["significant_positive_whole_brain_voxels"]
        elif number == "08":
            mask, positive = d["n_voxels_tested"], d["significant_voxels_fwe"]
        else:
            mask = d["common_mask_voxels"]
            positive = d["significant_voxels_fwe_p_le_0_05"]
        records.append({
            "run": run,
            "condition": condition,
            "condition_assignment_sha256": sha256(assignment_path),
            "condition_coordinator_revision": assignment["coordinator_commit"],
            "condition_assignment": {
                k: assignment[k] for k in (
                    "condition", "requested_condition", "config_sha256",
                    "additional_prompt_sha256", "supplied_skills_commit"
                )
            },
            "summary": str(summary_path.relative_to(SNAPSHOT)),
            "mask_voxels": mask,
            "positive_whole_brain_fwe_voxels": positive,
            "primary_correction": "Bonferroni" if number in {"01", "02"} else "max-T",
        })

    worker = args.workers_root / "narps-r1-09"
    for filename in (
        "one_sample_t.nii.gz", "common_brain_mask.nii.gz",
        "max_t_fwe_p05_mask.nii.gz", "vmPFC_AAL_medial_orbitofrontal_mask.nii.gz",
    ):
        copy_source(worker, f"results/{filename}", f"maps/{filename}")
    copy_source(worker, "input/sources.json", "participant-map-sources.json")
    copy_source(worker, "scripts/analyze_gain.py", "source-analysis-run09.py")

    # Anatomical context only: a distributed MNI template, not participant anatomy.
    ref = nib.load(SNAPSHOT / "maps/one_sample_t.nii.gz")
    template = image.resample_to_img(
        datasets.load_mni152_template(resolution=2), ref,
        interpolation="continuous", force_resample=True, copy_header=True,
    )
    destination = "maps/anatomical-context.nii.gz"
    nib.save(template, SNAPSHOT / destination)
    sources[destination] = {
        "sha256": sha256(SNAPSHOT / destination),
        "bytes": (SNAPSHOT / destination).stat().st_size,
        "source_url": "https://nilearn.github.io/stable/modules/generated/nilearn.datasets.load_mni152_template.html",
        "source_description": "Nilearn bundled skull-stripped ICBM152 MNI template; anatomical context only",
        "nilearn_version": nilearn.__version__,
        "transformation": "load_mni152_template(resolution=2), continuous resampling to run09 t-map grid",
    }
    result = {
        "result_selection_cutoff_utc": args.snapshot_utc,
        "snapshot_generated_utc": datetime.now(timezone.utc).isoformat(),
        "study": "NARPS Hypothesis 1, AO86 equal-indifference participant gain maps",
        "paper": "https://doi.org/10.1038/s41586-020-2314-9",
        "data": "https://doi.org/10.18112/openneuro.ds001734.v1.0.4",
        "participant_maps": "https://neurovault.org/collections/4932/",
        "n_participants": 54,
        "conditions": ["baseline", "discover-general", "discover-science", "stamped-explicit"],
        "records": records,
        "missing_completed_results": {
            "discover-general": ["narps-r1-04"],
            "stamped-explicit": ["narps-r1-10", "narps-r1-11", "narps-r1-12"],
        },
        "comparison_scope": "Descriptive differences among completed worker analyses of the same 54 participant maps. Mask rules and correction methods differ; these are not causal estimates of condition effects. Failed or incomplete runs are never assigned a zero value.",
        "representative_map_run": "narps-r1-09",
        "representative_map_selection": "A completed run using common nonzero coverage for every participant and a verifiable corrected mask; it is an example, not an average or a condition comparison.",
        "map_display": {
            "statistic": "unthresholded one-sample t; signed colors, clipped at +/- 6",
            "mask": "common nonzero coverage across all 54 participants; no color outside coverage",
            "roi": "AAL SPM12 bilateral Frontal_Med_Orb parcels, intersected with common coverage; descriptive vmPFC localization",
            "corrected": "positive-direction permutation max-T, 10,000 sign flips, whole-brain FWE p <= .05",
            "slice_centers_mni_mm": [-2, 24, -3.599997043609619],
            "orientation": "neurological: left hemisphere on image left in coronal and axial panels",
        },
        "sources": sources,
    }
    (SNAPSHOT / "provenance.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"Snapshotted {len(records)} completed runs and {len(sources)} source files")


if __name__ == "__main__":
    main()
