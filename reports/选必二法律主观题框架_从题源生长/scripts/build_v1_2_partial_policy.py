#!/usr/bin/env python3
"""Classify v1.1 PARTIAL rows after FAIL4 resolution.

The goal is not to promote these rows. It is to prevent framework synthesis
from treating reference-only or singleton open-container rows as core support.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
PRESSURE = ROOT / "10_framework_validation" / "framework_v1_1_question_by_question_sentence_pressure_test_20260519.csv"
OUT_CSV = ROOT / "10_framework_validation" / "framework_v1_2_partial_policy_20260519.csv"
OUT_MD = ROOT / "10_framework_validation" / "framework_v1_2_partial_policy_20260519.md"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def policy_for(row: dict[str, str]) -> tuple[str, str, str]:
    qid = row["question_id"]
    if row["evidence_level"] == "reference_only":
        return (
            "reference_only_demo_not_core",
            "no",
            "May be used only as a weak classroom demo; cannot support a codebook or framework node.",
        )
    if qid == "CC0011_2024_丰台_二模_17":
        return (
            "formal_open_container_institutional_value",
            "no",
            "Formal evidence, but current support is a singleton/open value mechanism; keep as validation material, not core support.",
        )
    if qid == "CC0061_2024_西城_一模_18":
        return (
            "formal_open_container_family_value_after_split",
            "no",
            "Procedure micro-items and family-value reasoning are split; do not force into private-law core until repeated support appears.",
        )
    if qid in {
        "CC0254_2026_丰台_二模_18",
        "RECOVER_2026_房山_一模_17_1",
    }:
        return (
            "formal_open_container_after_source_patch",
            "no",
            "Source-checked formal atoms are usable for boundary testing, but not yet enough for a stable core node.",
        )
    if row["expansion_status"] == "OPEN_CONTAINER_ONLY":
        return (
            "formal_open_container_singleton_or_low_frequency",
            "no",
            "Keep in open container; it can pressure-test the framework but cannot create an unsupported node.",
        )
    return (
        "partial_pending_manual_review",
        "no",
        "Do not use as core support until separately adjudicated.",
    )


def main() -> None:
    _, rows = read_csv(PRESSURE)
    partials = [row for row in rows if row["pass_status"] == "PARTIAL"]
    fields = [
        "question_id",
        "year",
        "district",
        "exam_stage",
        "question_no",
        "evidence_level",
        "expansion_status",
        "framework_entry_node",
        "partial_policy",
        "core_codebook_use",
        "policy_reason",
        "next_action",
    ]
    out_rows = []
    for row in partials:
        policy, core_use, reason = policy_for(row)
        next_action = (
            "exclude from framework-node evidence; keep as weak demo"
            if row["evidence_level"] == "reference_only"
            else "keep as open-container pressure case during framework synthesis"
        )
        out_rows.append(
            {
                "question_id": row["question_id"],
                "year": row["year"],
                "district": row["district"],
                "exam_stage": row["exam_stage"],
                "question_no": row["question_no"],
                "evidence_level": row["evidence_level"],
                "expansion_status": row["expansion_status"],
                "framework_entry_node": row["framework_entry_node"],
                "partial_policy": policy,
                "core_codebook_use": core_use,
                "policy_reason": reason,
                "next_action": next_action,
            }
        )
    write_csv(OUT_CSV, fields, out_rows)

    counts = Counter(row["partial_policy"] for row in out_rows)
    md = [
        "# Framework v1.2 PARTIAL Policy",
        "",
        "This file prevents PARTIAL rows from being mistaken for core framework evidence.",
        "",
        f"- PARTIAL rows: {len(out_rows)}",
        f"- reference_only demos: {sum(1 for row in out_rows if row['evidence_level'] == 'reference_only')}",
        f"- formal open-container rows: {sum(1 for row in out_rows if row['evidence_level'] == 'formal')}",
        "",
        "## Counts",
        "",
    ]
    for key, value in sorted(counts.items()):
        md.append(f"- {key}: {value}")
    md.extend(
        [
            "",
            "## Gate",
            "",
            "These rows may be used to pressure-test framework_v2, but none may create a new core node unless separately supported by formal repeated evidence and a new cross-validation record.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {OUT_CSV}")
    print(f"Rows: {len(out_rows)}")


if __name__ == "__main__":
    main()
