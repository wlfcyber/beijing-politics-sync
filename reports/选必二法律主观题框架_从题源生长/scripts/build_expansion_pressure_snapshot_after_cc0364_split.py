#!/usr/bin/env python3
"""Create a coverage snapshot after CC0364 split and codebook v1.1."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
QUESTIONS = ROOT / "04_merge_audit" / "merged_subjective_law_questions.csv"
CODEBOOK = ROOT / "08_codebook" / "provisional_codebook_v1_1_after_cc0364_split_20260519.csv"
OPEN = ROOT / "08_codebook" / "transfer_open_container_after_cc0364_split_20260519.csv"
OUT_CSV = ROOT / "10_framework_validation" / "framework_v1_1_after_cc0364_split_pressure_snapshot_20260519.csv"
OUT_MD = ROOT / "10_framework_validation" / "framework_v1_1_after_cc0364_split_pressure_snapshot_20260519.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def split_ids(value: str) -> list[str]:
    return [p.strip() for p in (value or "").split("|") if p.strip()]


def main() -> None:
    questions = read_csv(QUESTIONS)
    code_rows = read_csv(CODEBOOK)
    open_rows = read_csv(OPEN)

    core_by_qid: dict[str, list[str]] = defaultdict(list)
    for row in code_rows:
        for qid in split_ids(row["supporting_question_ids"]):
            core_by_qid[qid].append(row["code_id"])

    open_by_qid: dict[str, list[str]] = defaultdict(list)
    reject_by_qid: dict[str, list[str]] = defaultdict(list)
    for row in open_rows:
        dest = reject_by_qid if row["status"] == "reject_core" else open_by_qid
        for qid in split_ids(row["question_ids"]):
            dest[qid].append(row["container_id"] or row["source_decision_id"])

    output = []
    for q in questions:
        qid = q["question_id"]
        evidence_level = q.get("evidence_level", "")
        if qid in core_by_qid:
            status = "CORE_CODEBOOK_SUPPORT"
            matched = "|".join(core_by_qid[qid])
            note = "Codebook v1.1 has core support after CC0364 split; still requires sentence-level pressure test."
        elif evidence_level == "reference_only" or qid in reject_by_qid:
            status = "REFERENCE_OR_REJECT_NON_CORE"
            matched = "|".join(reject_by_qid.get(qid, []))
            note = "Not core support; reference_only or rejected by dual-model adjudication."
        elif qid in open_by_qid:
            status = "OPEN_CONTAINER_ONLY"
            matched = "|".join(open_by_qid[qid])
            note = "Kept as open container or transfer-only; does not support core codebook."
        else:
            status = "NO_EXPANSION_SUPPORT_YET"
            matched = ""
            note = "No dual-model expansion support after current round; keep pending for later source check."
        output.append(
            {
                "question_id": qid,
                "year": q.get("year", ""),
                "district": q.get("district", ""),
                "exam_stage": q.get("exam_stage", ""),
                "question_no": q.get("question_no", ""),
                "evidence_level": evidence_level,
                "expansion_status": status,
                "matched_code_or_container": matched,
                "ask_text": q.get("ask_text", ""),
                "note": note,
            }
        )

    fields = list(output[0].keys())
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)

    counts = Counter(row["expansion_status"] for row in output)
    md = [
        "# Framework v1.1 After CC0364 Split Pressure Snapshot",
        "",
        "This is a coverage snapshot, not final framework validation.",
        "",
        f"- total questions: {len(output)}",
        f"- core codebook support: {counts['CORE_CODEBOOK_SUPPORT']}",
        f"- open-container only: {counts['OPEN_CONTAINER_ONLY']}",
        f"- reference/rejected non-core: {counts['REFERENCE_OR_REJECT_NON_CORE']}",
        f"- source-check pending: 0",
        f"- no expansion support yet: {counts['NO_EXPANSION_SUPPORT_YET']}",
        "",
        "## Status Counts",
        "",
        "| status | count |",
        "|---|---:|",
    ]
    for status, count in counts.most_common():
        md.append(f"| {status} | {count} |")
    md.extend(["", "## Remaining Non-Core / Pending Rows", ""])
    for row in output:
        if row["expansion_status"] != "CORE_CODEBOOK_SUPPORT":
            md.append(f"- `{row['question_id']}` — {row['expansion_status']} — {row['matched_code_or_container'] or 'none'}")
    md.extend(
        [
            "",
            "## Gate",
            "",
            "CC0364 is no longer source-check pending. The next required step is a sentence-level all-65 pressure test. This snapshot still does not authorize framework_v2 or final handbook regeneration.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(md), encoding="utf-8")

    print(f"Wrote {OUT_CSV}")
    print(dict(counts))


if __name__ == "__main__":
    main()
