from __future__ import annotations

import csv
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
RISK_CSV = RECOVERY / "MATRIX_EVIDENCE_RISK_AUDIT_20260525.csv"
OUT_CSV = RECOVERY / "CHOICE_QUESTION_BOUNDARY_ADJUDICATION_20260525.csv"
OUT_MD = RECOVERY / "CHOICE_QUESTION_BOUNDARY_ADJUDICATION_20260525.md"

BOUNDARY_SENTENCE = "边界：本行为选择题官方答案键/正确项链条，只用于选择题知识触发与错项辨析，不作为主观题稳定评分触发或评分细则证据。"
EVIDENCE_SUFFIX = "；选择题边界已明示"
STATUS_SUFFIX = "_CHOICE_CHAIN_BOUNDARY_CONFIRMED"


def backup(path: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target = path.with_name(f"{path.stem}_backup_before_choice_boundary_adjudication_{stamp}{path.suffix}")
    shutil.copy2(path, target)
    return target


def load_choice_risk_ids() -> set[str]:
    with RISK_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return {
            row["row_id"]
            for row in reader
            if "OBJECTIVE_KEY_ONLY_IN_BODY_BOUNDARY" in row.get("risks", "")
        }


def main() -> None:
    target_ids = load_choice_risk_ids()
    matrix_backup = backup(MATRIX)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    changed = []
    for row in rows:
        row_id = row.get("matrix_row_id", "")
        if row_id not in target_ids:
            continue
        if "非主观题评分细则" not in row.get("题型或模块判断", ""):
            row["题型或模块判断"] = (row.get("题型或模块判断", "") + "；选择题正确项链条（非主观题评分细则）").strip("；")
        if BOUNDARY_SENTENCE not in row.get("细则支持原理", ""):
            row["细则支持原理"] = row.get("细则支持原理", "") + " " + BOUNDARY_SENTENCE
        if "选择题边界已明示" not in row.get("证据等级", ""):
            row["证据等级"] = row.get("证据等级", "") + EVIDENCE_SUFFIX
        row["是否误放"] = "否：选择题链条已明示边界"
        if not row.get("是否需补厚", "").startswith("否"):
            row["是否需补厚"] = "否：仅作选择题正确项/错项辨析链条，不扩写为主观题评分点。"
        if STATUS_SUFFIX not in row.get("当前处理", ""):
            row["当前处理"] = row.get("当前处理", "") + STATUS_SUFFIX
        note = row.get("备注", "")
        if "选择题边界复核" not in note:
            append = "2026-05-25选择题边界复核：官方答案键只支撑正确项链条和错项辨析，不支撑主观题稳定评分触发。"
            row["备注"] = f"{note}；{append}" if note else append
        changed.append(row)

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    out_fields = ["matrix_row_id", "题源", "年份", "阶段", "题号", "宝典节点", "证据等级", "当前处理", "source_artifact"]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for row in changed:
            writer.writerow({field: row.get(field, "") for field in out_fields})

    suites = Counter(row.get("题源", "") for row in changed)
    lines = [
        "# CHOICE_QUESTION_BOUNDARY_ADJUDICATION_20260525",
        "",
        "Status: `CHOICE_CHAIN_BOUNDARY_DISCLOSED`",
        "",
        "## Result",
        "",
        f"- Rows adjudicated: `{len(changed)}`.",
        f"- Matrix backup: `{matrix_backup}`.",
        f"- CSV ledger: `CHOICE_QUESTION_BOUNDARY_ADJUDICATION_20260525.csv`.",
        "",
        "## Rule Applied",
        "",
        "- Choice-question official answer keys can support correct-option chains and wrong-option analysis.",
        "- They do not support main-question stable scoring triggers.",
        "- The repaired rows now explicitly state that boundary in the matrix, evidence level, and processing note.",
        "",
        "## Suites",
        "",
    ]
    for suite, count in suites.most_common():
        lines.append(f"- `{suite}`: `{count}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- No row in this batch was upgraded to formal main-question rubric evidence.",
            "- External GPTPro and Claude Opus review gates remain `real_call_pending`.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"CHOICE_BOUNDARY_ROWS={len(changed)}")
    print(f"OUT_CSV={OUT_CSV}")
    print(f"OUT_MD={OUT_MD}")


if __name__ == "__main__":
    main()
