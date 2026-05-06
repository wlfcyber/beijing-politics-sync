#!/usr/bin/env python3
"""Normalize Opus Batch03 choice CSV field shifts without changing judgments."""

from __future__ import annotations

import csv
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
RAW = BASE / "claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results.csv"
OUT = BASE / "claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv"
AUDIT = BASE / "claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalization_audit.csv"


def normalize_row(header: list[str], row: list[str]) -> tuple[list[str], str]:
    target_id = row[0] if row else ""
    if len(row) == len(header):
        return row, "unchanged"

    if target_id in {
        "Q-2026东城期末-3",
        "Q-2026东城期末-4",
        "Q-2025顺义一模-3",
    } and len(row) == len(header) + 1:
        fixed = row[:13]
        fixed.append(row[13] + "；" + row[14])
        fixed.extend(row[15:19])
        fixed.append(row[19])
        return fixed, "merged_extra_trap_clause_into_trap_or_boundary"

    if target_id == "Q-2025顺义一模-7" and len(row) == len(header) + 2:
        fixed = row[:13]
        fixed.append("；".join(row[13:16]))
        fixed.extend(row[16:19])
        fixed.extend(row[19:21])
        return fixed, "merged_BCD_option_analysis_into_trap_or_boundary"

    raise ValueError(f"unhandled malformed row for {target_id}: {len(row)} fields")


def main() -> None:
    with RAW.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    fixed_rows: list[list[str]] = []
    audit_rows: list[dict[str, str]] = []
    for line_no, row in enumerate(rows, 2):
        fixed, action = normalize_row(header, row)
        if len(fixed) != len(header):
            raise AssertionError((line_no, row[0] if row else "", len(fixed), len(header)))
        fixed_rows.append(fixed)
        audit_rows.append(
            {
                "line_no": str(line_no),
                "target_id": fixed[0],
                "raw_field_count": str(len(row)),
                "normalized_field_count": str(len(fixed)),
                "action": action,
                "can_enter_fusion": fixed[14],
                "can_enter_student_draft": fixed[15],
            }
        )

    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(fixed_rows)

    with AUDIT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(audit_rows[0]))
        writer.writeheader()
        writer.writerows(audit_rows)

    print(f"wrote {OUT}")
    print(f"wrote {AUDIT}")
    print(f"rows={len(fixed_rows)} fixes={sum(r['action'] != 'unchanged' for r in audit_rows)}")


if __name__ == "__main__":
    main()
