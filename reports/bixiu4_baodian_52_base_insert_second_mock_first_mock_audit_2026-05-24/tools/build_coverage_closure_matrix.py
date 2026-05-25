# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET


RUN = Path(__file__).resolve().parents[1]
INV = RUN / "01_source_inventory"
FUSION = RUN / "04_fusion_audit"
DELIVERY = RUN / "05_delivery"
GOV = RUN / "06_governor_confucius"


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paras: list[str] = []
    for p in root.findall(".//w:p", ns):
        text = "".join(t.text or "" for t in p.findall(".//w:t", ns))
        if text:
            paras.append(text)
    return "\n".join(paras)


def main() -> int:
    inventory = read_csv(INV / "source_suite_inventory.csv")
    accepted = read_jsonl(FUSION / "student_patch_entries.accepted.jsonl")
    blocked = read_jsonl(FUSION / "student_patch_entries.blocked.jsonl")
    res2024 = read_csv(FUSION / "first_mock_2024_queue_resolution.csv")
    prompt_res = read_csv(FUSION / "prompt_gate_resolution.csv")
    weak_res_path = FUSION / "weak_gate_source_repair_resolution.csv"
    weak_res = read_csv(weak_res_path) if weak_res_path.exists() else []
    final_text = docx_text(next(DELIVERY.glob("*.docx")))

    acc_by_suite = Counter(r["source_suite"] for r in accepted)
    block_by_suite: dict[str, Counter] = defaultdict(Counter)
    for r in blocked:
        block_by_suite[r["source_suite"]][r["block_reason"]] += 1
    res_by_suite: dict[str, Counter] = defaultdict(Counter)
    for r in res2024:
        res_by_suite[r["suite"]][r["status"]] += 1
    prompt_resolved_by_suite = Counter(r["source_suite"] for r in prompt_res if r["resolution"] == "resolved_by_final_docx")
    weak_resolved_by_suite = Counter(
        r["source_suite"]
        for r in weak_res
        if r.get("resolution", "").startswith("resolved")
    )

    rows = []
    unresolved_suites = []
    for r in inventory:
        suite = r["suite"]
        mentions = final_text.count(suite)
        accepted_count = acc_by_suite[suite]
        blocks = block_by_suite[suite]
        res = res_by_suite[suite]
        prompt_open = max(0, blocks.get("question_prompt_not_verified", 0) - prompt_resolved_by_suite[suite])
        weak_open = max(0, blocks.get("weak_evidence", 0) - weak_resolved_by_suite[suite])
        unresolved = weak_open + prompt_open
        excluded = blocks.get("culture_boundary", 0) + blocks.get("module_boundary", 0) + res.get("module_boundary_excluded", 0)
        resolved_covered = (
            accepted_count
            + blocks.get("already_in_base_exact_source", 0)
            + res.get("resolved_covered", 0)
            + res.get("resolved_as_misparsed_covered", 0)
        )
        if unresolved:
            closure_status = "OPEN_EVIDENCE_OR_PROMPT_GATE"
            unresolved_suites.append(suite)
        elif resolved_covered or mentions:
            closure_status = "COVERED_OR_PATCHED"
        elif excluded:
            closure_status = "BOUNDARY_EXCLUDED"
        else:
            closure_status = "NO_FINAL_ARTIFACT_EVIDENCE"

        rows.append(
            {
                "suite": suite,
                "year": r["year"],
                "phase": r["phase"],
                "final_docx_suite_mentions": mentions,
                "accepted_insertions": accepted_count,
                "blocked_already_in_base": blocks.get("already_in_base_exact_source", 0),
                "blocked_weak_evidence": blocks.get("weak_evidence", 0),
                "resolved_weak_evidence_by_source_repair": weak_resolved_by_suite[suite],
                "open_weak_evidence_gate": weak_open,
                "blocked_question_prompt_not_verified": blocks.get("question_prompt_not_verified", 0),
                "resolved_question_prompt_by_final_docx": prompt_resolved_by_suite[suite],
                "open_question_prompt_gate": prompt_open,
                "blocked_culture_boundary": blocks.get("culture_boundary", 0),
                "blocked_module_boundary": blocks.get("module_boundary", 0),
                "resolved_2024_covered": res.get("resolved_covered", 0),
                "resolved_2024_misparsed_covered": res.get("resolved_as_misparsed_covered", 0),
                "resolved_2024_module_excluded": res.get("module_boundary_excluded", 0),
                "closure_status": closure_status,
            }
        )

    out_csv = GOV / "COVERAGE_CLOSURE_MATRIX_V2.csv"
    with out_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    status_counts = Counter(r["closure_status"] for r in rows)
    lines = [
        "# COVERAGE_CLOSURE_MATRIX_V2",
        "",
        "This is a suite-level closure matrix for the 35 source suites in this run. It is a governor aid, not a final PASS.",
        "",
        "External-review packet note: direct source bundles are attached for the touched or weak-evidence suites in this repair batch; other suites rely on the accepted base baodian coverage and the lane closure records, not on a full re-upload of all 35 source bundles.",
        "",
        "## Status Counts",
        "",
    ]
    for key, val in status_counts.most_common():
        lines.append(f"- {key}: {val}")
    lines.extend(["", "## Open Evidence Or Prompt Gates", ""])
    if unresolved_suites:
        for suite in sorted(set(unresolved_suites)):
            lines.append(f"- {suite}")
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "## Reading Rule",
            "",
            "- `COVERED_OR_PATCHED`: suite appears in final DOCX or has accepted/base-covered evidence.",
            "- `BOUNDARY_EXCLUDED`: only module/culture boundary items remain.",
            "- `OPEN_EVIDENCE_OR_PROMPT_GATE`: unrepaired weak evidence or missing prompt remains; do not sign final PASS.",
            "- `NO_FINAL_ARTIFACT_EVIDENCE`: no final artifact evidence was found at suite level.",
        ]
    )
    (GOV / "COVERAGE_CLOSURE_MATRIX_V2.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_csv)
    print(GOV / "COVERAGE_CLOSURE_MATRIX_V2.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
