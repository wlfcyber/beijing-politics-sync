from __future__ import annotations

import csv
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
RISK_CSV = RECOVERY / "MATRIX_EVIDENCE_RISK_AUDIT_20260525.csv"
OUT_CSV = RECOVERY / "REMAINING_IN_BODY_NON_RUBRIC_EVIDENCE_BOUNDARIES_20260525.csv"
OUT_MD = RECOVERY / "REMAINING_IN_BODY_NON_RUBRIC_EVIDENCE_BOUNDARIES_20260525.md"
STATUS_SUFFIX = "_DISCLOSED_NON_RUBRIC_EVIDENCE_BOUNDARY"


def backup(path: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target = path.with_name(f"{path.stem}_backup_before_remaining_non_rubric_boundaries_{stamp}{path.suffix}")
    shutil.copy2(path, target)
    return target


def load_remaining() -> list[dict[str, str]]:
    with RISK_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return [
            row
            for row in reader
            if row.get("in_book", "").startswith("是")
            and "IN_BODY_WEAK_OR_REFERENCE_EVIDENCE" in row.get("risks", "")
        ]


def update_matrix(target_ids: set[str]) -> Path:
    backup_path = backup(MATRIX)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    for row in rows:
        if row.get("matrix_row_id") not in target_ids:
            continue
        if STATUS_SUFFIX not in row.get("当前处理", ""):
            row["当前处理"] = row.get("当前处理", "") + STATUS_SUFFIX
        row["是否误放"] = "否：保留为已明示的非细则证据边界"
        if "非细则证据边界" not in row.get("是否需补厚", ""):
            row["是否需补厚"] = row.get("是否需补厚", "") + "；非细则证据边界，若要升为正式评分触发需补正式细则/评标/评分文件。"
        note = row.get("备注", "")
        append = "2026-05-25复核：未找到可升级为逐点评分细则的来源；继续在审计中保留风险，不包装为闭合证据。"
        if "未找到可升级为逐点评分细则" not in note:
            row["备注"] = f"{note}；{append}" if note else append
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return backup_path


def main() -> None:
    remaining = load_remaining()
    target_ids = {row["row_id"] for row in remaining}
    backup_path = update_matrix(target_ids)

    out_fields = ["row_id", "suite", "question", "node", "evidence_level", "risks", "support_text", "source_artifact"]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for row in remaining:
            writer.writerow({field: row.get(field, "") for field in out_fields})

    suites = Counter(row.get("suite", "") for row in remaining)
    lines = [
        "# REMAINING_IN_BODY_NON_RUBRIC_EVIDENCE_BOUNDARIES_20260525",
        "",
        "Status: `NON_RUBRIC_EVIDENCE_BOUNDARIES_REMAIN_OPEN`",
        "",
        "## Summary",
        "",
        f"- Remaining in-body non-rubric evidence rows: `{len(remaining)}`.",
        f"- Matrix backup: `{backup_path}`.",
        f"- CSV ledger: `REMAINING_IN_BODY_NON_RUBRIC_EVIDENCE_BOUNDARIES_20260525.csv`.",
        "",
        "## Boundary Decision",
        "",
        "- These rows are not treated as formal scoring-rubric evidence.",
        "- They remain visible in the audit queue because the available source is a teacher/reference broad angle or material wording, not a point-by-point scoring rule.",
        "- They are not marked as final acceptance blockers for file creation, but they block any claim that every in-body row has point-by-point formal rubric closure.",
        "",
        "## Suites",
        "",
    ]
    for suite, count in suites.most_common():
        lines.append(f"- `{suite}`: `{count}`")
    lines.extend(["", "## Rows", ""])
    lines.append("| row | suite | question | node | evidence |")
    lines.append("|---|---|---|---|---|")
    for row in remaining:
        lines.append(
            "| {row_id} | {suite} | {question} | {node} | {evidence} |".format(
                row_id=row.get("row_id", ""),
                suite=row.get("suite", "").replace("|", "/"),
                question=row.get("question", "").replace("|", "/"),
                node=row.get("node", "").replace("|", "/"),
                evidence=row.get("evidence_level", "").replace("|", "/"),
            )
        )
    lines.extend(
        [
            "",
            "## External Gates",
            "",
            "- GPTPro web external review: `real_call_pending`.",
            "- Claude Opus web/app external review: `real_call_pending`.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"REMAINING_IN_BODY_NON_RUBRIC_ROWS={len(remaining)}")
    print(f"OUT_CSV={OUT_CSV}")
    print(f"OUT_MD={OUT_MD}")


if __name__ == "__main__":
    main()
