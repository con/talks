#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Center for Open Neuroscience
# SPDX-License-Identifier: Apache-2.0
"""Export a dated, public-safe poster snapshot without changing the study.

Usage: python stamped-poster-assessment-export.py --study COORDINATOR --out JSON

Only completed judgments registered in each round ledger are admitted. Raw item
statuses remain intact; the external measurement-validity overlay is separate.
The output contains no transcripts, credentials, native commands or host paths.
"""

import argparse
import collections
import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import Path
from zoneinfo import ZoneInfo


STATUSES = ("met", "partial", "unmet", "not-checked", "not-applicable")
REMOTE = "https://github.com/leej3/stamped-in-practice"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    return result.stdout if result.returncode == 0 else None


def scientific_label(report):
    # Preserve the judge's classification, not whether the tested hypothesis won.
    match = re.search(r"Scientific adequacy:\*?\*?\s*\*?\*?\s*(not supported|qualified|supported|unable to assess|not checked)", report, re.I)
    if match:
        return match.group(1).lower()
    # Judges also label the scientific section's verdict "Adequacy" or
    # "Classification". Restrict these alternatives to that section so a
    # checklist verdict elsewhere cannot be mistaken for scientific adequacy.
    section = re.search(r"^## Scientific[^\n]*\n(.*?)(?=^## |\Z)", report, re.I | re.M | re.S)
    if section:
        match = re.search(r"(?:Adequacy|Classification):\*?\*?\s*\*?\*?\s*(not supported|qualified|supported|unable to assess|not checked)", section[1], re.I)
        if match:
            return match[1].lower()
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", required=True, type=Path,
                        help="Coordinator checkout containing iterations/narps-v1")
    parser.add_argument("--out", required=True, type=Path, help="Destination JSON filename")
    args = parser.parse_args()
    root = args.study.resolve()
    iteration = root / "iterations/narps-v1"
    now = dt.datetime.now(dt.timezone.utc)
    sources = {}
    warnings = []
    head_bytes = git(root, "rev-parse", "HEAD")
    head = head_bytes.decode().strip() if head_bytes else None
    # Read advertised refs without fetching or mutating the live study checkout.
    # Named links are easier to navigate; immutable revisions and file hashes
    # below retain the exact identity verified when the snapshot was exported.
    advertised = git(root, "ls-remote", "--heads", REMOTE + ".git")
    public_branches = {}
    if advertised:
        for line in advertised.decode().splitlines():
            revision, ref = line.split("\t", 1)
            public_branches[ref.removeprefix("refs/heads/")] = revision
    else:
        warnings.append("Public branch advertisement unavailable; no new source links verified")

    def read_source(path, source_id, coordinator_relative=None):
        data = path.read_bytes()
        record = {"sha256": digest(data), "bytes": len(data), "public_url": None}
        if coordinator_relative:
            record["coordinator_path"] = coordinator_relative
            committed = git(root, "show", f"HEAD:{coordinator_relative}")
            record["matches_coordinator_head"] = committed == data
            public_revision = public_branches.get("main")
            published = git(root, "show", f"{public_revision}:{coordinator_relative}") if public_revision else None
            if published == data:
                record["public_url"] = f"{REMOTE}/blob/main/{coordinator_relative}"
                record["public_branch"] = "main"
                record["published_commit"] = public_revision
                record["publication_status"] = "published-branch-source-hash-verified"
        else:
            record["publication_status"] = "not-established-by-this-export"
            judgment_id = source_id.split("/")[0]
            match = re.fullmatch(r"(narps-r\d+-\d+)-judgment-(\d+)", judgment_id)
            branch = f"codex/{match[1]}-judge-{match[2]}-output" if match else None
            revision = public_branches.get(branch)
            if revision and path.name.endswith(("assessment.md", "response.json", "fresh-rerun.json")):
                published = git(path.parent, "show", f"{revision}:{path.name}")
                if published == data:
                    record["public_url"] = f"{REMOTE}/blob/{branch}/{path.name}"
                    record["public_branch"] = branch
                    record["published_commit"] = revision
                    record["publication_status"] = "published-branch-source-hash-verified"
                else:
                    warnings.append(f"{source_id}: advertised output branch does not match source bytes")
        sources[source_id] = record
        return data

    def read_coordinator(name):
        rel = f"iterations/narps-v1/{name}"
        return json.loads(read_source(root / rel, name, rel))

    allocation = read_coordinator("allocation.json")
    disposition = read_coordinator("measurement-disposition-01.json")
    disposition_by_id = {j["judgment_id"]: j for j in disposition["judgments"]}
    # Capture ledgers up front. A late filesystem artifact does not become an
    # outcome unless it was already completed in this captured ledger.
    ledgers = {}
    for planned in allocation["rounds"]:
        name = f"round-{planned['round']}.json"
        if (iteration / name).exists():
            ledgers[planned["round"]] = read_coordinator(name)

    def judgment(run_id, entry):
        jid = f"{run_id}-{entry['judgment_id']}"
        overlay = disposition_by_id.get(jid, {})
        role = overlay.get("role", entry.get("judgment_role"))
        result = {
            "judgment_id": jid, "role": role, "status": entry.get("status"),
            "procedure_sha256": entry.get("procedure_sha256"),
            "assessment_scope": entry.get("assessment_scope"),
            "finished_at": entry.get("finished_at"),
            "science": None, "replay": None, "checklist": None,
        }
        if entry.get("status") != "completed":
            return result
        base = Path(entry["evidence"])
        assessment_dir = base / "judgment"
        response_paths = sorted(assessment_dir.glob("????-??-??-response.json"))
        report_paths = sorted(assessment_dir.glob("????-??-??-assessment.md"))
        replay_paths = sorted(assessment_dir.glob("????-??-??-fresh-rerun.json"))
        source_prefix = jid + "/"
        if len(response_paths) != 1 or len(report_paths) != 1:
            warnings.append(f"{jid}: completed ledger entry lacks one unambiguous response/report pair")
            result["status"] = "completed-artifacts-incomplete"
            return result
        response = json.loads(read_source(response_paths[0], source_prefix + "response.json"))
        report = read_source(report_paths[0], source_prefix + "assessment.md").decode()
        validity = overlay.get("measure_validity", [])
        blocked = {v["measure"]: v["status"] for v in validity
                   if v["status"] in ("unavailable", "invalid")}
        answers = response["responses"]
        raw = collections.Counter(a["status"] for a in answers.values())
        valid = collections.Counter(a["status"] for key, a in answers.items() if key not in blocked)
        unavailable = sum(key in answers and value == "unavailable" for key, value in blocked.items())
        invalid = sum(key in answers and value == "invalid" for key, value in blocked.items())
        total = len(answers)
        result["checklist"] = {
            "version": response.get("checklist_version"),
            "raw_counts": {s: raw[s] for s in STATUSES},
            "comparable_counts": {s: valid[s] for s in STATUSES},
            "total_items": total,
            "applicable_items": total - raw["not-applicable"],
            "comparable_applicable_items": sum(valid.values()) - valid["not-applicable"],
            "unavailable_items": unavailable, "invalid_items": invalid,
            "descriptive_met_numerator": valid["met"],
            "descriptive_met_denominator": sum(valid.values()) - valid["not-applicable"],
            "item_statuses": {key: value["status"] for key, value in sorted(answers.items())},
            "item_validity_overrides": {key: value for key, value in sorted(blocked.items()) if key in answers},
            "raw_retrieval_item": answers.get("stamped-checklist:must/016", {}).get("status"),
            "retrieval_item_validity": blocked.get("stamped-checklist:must/016", "available"),
            "source_id": source_prefix + "response.json",
        }
        dependency = overlay.get("scientific_dependency", {})
        label = scientific_label(report)
        if label is None:
            warnings.append(f"{jid}: scientific adequacy label could not be extracted")
        result["science"] = {
            "reported_adequacy": label,
            "evidence_dependency": dependency.get("status", "no-uncertainty-overlay-recorded"),
            "display_qualifier": "replay evidence unavailable" if dependency.get("status") == "uncertain" else None,
            "source_id": source_prefix + "assessment.md",
        }
        if len(replay_paths) == 1:
            replay = json.loads(read_source(replay_paths[0], source_prefix + "fresh-rerun.json"))
            comparison = replay.get("comparison", {})
            result["replay"] = {
                "raw_status": replay.get("status"),
                "comparable_status": blocked.get("replay", replay.get("status")),
                "validity": blocked.get("replay", "available"),
                "identical_outputs": len(comparison.get("identical", [])) if comparison else None,
                "within_tolerance_outputs": len(comparison.get("within_tolerance", [])) if comparison else None,
                "different_outputs": comparison.get("differing", []),
                "missing_outputs": comparison.get("missing_after_rerun", []),
                "candidate_outputs": sum(len(comparison.get(key, [])) for key in
                    ("identical", "within_tolerance", "differing", "missing_after_rerun")) if comparison else None,
                "host_scope": "same-host",
                "source_id": source_prefix + "fresh-rerun.json",
            }
        native = base / "native/result.json"
        if native.exists():
            native_data = json.loads(read_source(native, source_prefix + "native-result.json"))
            result["assessor_source_commit"] = native_data.get("assessment_pin", {}).get("source_commit")
            result["assessor_environment_commit"] = native_data.get("assessment_pin", {}).get("environment_commit")
        binding_path = base.parent / "retention" / f"{entry['judgment_id']}-output-binding.json"
        result["evidence_binding"] = "pending"
        if binding_path.exists():
            binding_id = source_prefix + "output-binding.json"
            binding = json.loads(read_source(binding_path, binding_id))
            checks = [
                binding.get("outputs", {}).get("response", {}).get("sha256") == sources[source_prefix + "response.json"]["sha256"],
                binding.get("outputs", {}).get("report", {}).get("sha256") == sources[source_prefix + "assessment.md"]["sha256"],
                binding.get("native_result_sha256") == sources.get(source_prefix + "native-result.json", {}).get("sha256"),
            ]
            if overlay.get("native_result_sha256"):
                checks.append(overlay["native_result_sha256"] == sources[source_prefix + "native-result.json"]["sha256"])
            if overlay.get("output_binding_sha256"):
                checks.append(overlay["output_binding_sha256"] == sources[binding_id]["sha256"])
            result["evidence_binding"] = "hashes-match" if all(checks) else "hash-mismatch"
            if not all(checks):
                warnings.append(f"{jid}: retained output binding hash mismatch; do not use as a finalized outcome")
        return result

    rounds = []
    rows = []
    other_judgments = []
    for plan in allocation["rounds"]:
        number = plan["round"]
        ledger = ledgers.get(number)
        by_id = {r["run"]: r for r in ledger["runs"]} if ledger else {}
        round_rows = []
        for assignment in sorted(plan["launch_order"], key=lambda r: r["run"]):
            run_id = assignment["run"]
            run = by_id.get(run_id, {})
            row = {
                "run": run_id, "iteration": number,
                "condition": assignment["condition"], "replicate": assignment["replicate"],
                "status": run.get("status", "planned" if not ledger else "not-started"),
                "worker_result_commit": run.get("worker_head_commit"),
                "worker_finished_at": run.get("finished_at"),
                "worker_elapsed_seconds": run.get("worker_elapsed_seconds"),
                "result_url": f"{REMOTE}/tree/codex/{run_id}" if run.get("worker_head_commit") and public_branches.get(f"codex/{run_id}") == run["worker_head_commit"] else None,
                "result_branch": f"codex/{run_id}",
                "result_branch_verified_commit": public_branches.get(f"codex/{run_id}"),
                "primary": None, "retrieval": None,
                "duplicate_assigned": run_id in plan["duplicate_judgments"],
            }
            for entry in run.get("judgments", []):
                outcome = judgment(run_id, entry)
                if outcome["role"] == "primary":
                    row["primary"] = outcome
                else:
                    other_judgments.append({"run": run_id, **outcome})
            retention = run.get("independent_retention_evidence", {})
            if retention.get("path") and Path(retention["path"]).exists():
                source_id = run_id + "/recipient-check.json"
                receipt = json.loads(read_source(Path(retention["path"]), source_id))
                annex_count = next((receipt[key] for key in ("annex_paths_verified", "annex_paths", "annex_files") if key in receipt), None)
                row["retrieval"] = {
                    "verified": receipt.get("passed", receipt.get("success")),
                    "annex_paths_verified": annex_count,
                    "scope": "coordinator-preservation-of-exact-worker-stop",
                    "worker_delivery_credit": False,
                    "scientific_execution": False,
                    "completed_at": receipt.get("finished_at", receipt.get("completed_at")),
                    "source_id": source_id,
                }
            round_rows.append(row)
        rows.extend(round_rows)
        rounds.append({
            "iteration": number, "status": "recorded-in-progress" if ledger else "planned",
            "final_untuned_evaluation": plan.get("final_untuned_evaluation"),
            "allocated_workers": len(plan["launch_order"]),
            "allocated_primary_judgments": len(plan["launch_order"]),
            "allocated_duplicate_judgments": len(plan["duplicate_judgments"]),
            "skills_commit": ledger.get("skills_commit") if ledger else None,
            "ledger_updated_at": ledger.get("last_updated_at") if ledger else None,
            "workers_finished": sum(row["worker_result_commit"] is not None for row in round_rows),
            "completed_primary_judgments": sum(row["primary"] is not None and row["primary"]["status"] == "completed" for row in round_rows),
        })
    output = {
        "schema_version": 1, "study": "narps", "comparison_id": "narps-v1",
        "snapshot_at_utc": now.isoformat(),
        "snapshot_at_eastern": now.astimezone(ZoneInfo("America/New_York")).isoformat(),
        "coordinator_head": head, "coordinator_url": REMOTE,
        "allocation_sha256": sources["allocation.json"]["sha256"],
        "disposition_sha256": sources["measurement-disposition-01.json"]["sha256"],
        "interpretation": {
            "checklist": "Descriptive item counts, not a combined score or certification. Partial never counts as met. N/A and invalid/unavailable items are excluded only from the explicitly comparable applicable denominator. Not-checked items remain in that denominator and are shown separately.",
            "scientific_adequacy": "Judge support for the scientific analysis is separate from support for the hypothesis. Infrastructure uncertainty flags preserve the raw scientific classification without regrading it.",
            "replay": "Assessor-infrastructure failures are unavailable, not worker failures. Same-host replay does not establish cross-host portability.",
            "retrieval": "Coordinator preservation verifies exact stopped-worker bytes; it is not worker delivery credit or successful scientific execution.",
            "missing": "Missing assessments and future runs are missing observations, never zero scores. Supplementary judgments cannot replace assigned primaries or duplicates.",
            "publication": "Reader links use named branches, verified against advertised remote heads at export. Exact commits and source hashes retain snapshot identity. Branches may later advance. A null public_url means publication of that raw source is not established by this export; result links are independent from assessment publication.",
        },
        "rounds": rounds, "rows": rows, "other_judgments": other_judgments,
        "sources": sources, "warnings": warnings,
    }
    serialized = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if re.search(r"/Users/|/home/|file://", serialized):
        raise RuntimeError("Unexpected host path in public snapshot")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(serialized)
    print(json.dumps({"rows": len(rows), "sources": len(sources),
                      "completed_primary_judgments": sum(r["completed_primary_judgments"] for r in rounds),
                      "warnings": warnings, "snapshot_sha256": digest(serialized.encode())}))


if __name__ == "__main__":
    main()
