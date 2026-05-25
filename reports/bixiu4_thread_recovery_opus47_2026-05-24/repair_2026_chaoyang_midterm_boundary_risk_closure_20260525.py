from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent
MATRIX = BASE / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = BASE / "CHAOYANG_2026_MIDTERM_BOUNDARY_RISK_CLOSURE_20260525.md"
REPORT_JSON = BASE / "CHAOYANG_2026_MIDTERM_BOUNDARY_RISK_CLOSURE_20260525.json"


def main() -> None:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    h = {
        "id": "matrix_row_id",
        "support": fields[9],
        "evidence": fields[10],
        "misplaced": fields[11],
        "thick": fields[12],
        "status": fields[13],
    }

    updates = {
        "M1277": {
            h["support"]: "\u6559\u5e08\u7248\u9898\u9762\u4e0e\u6b63\u5f0f\u8bc4\u6807/\u7ec6\u5219\u7f13\u5b58\u663e\u793a\uff1aQ16\u5c5e\u300a\u7ecf\u6d4e\u4e0e\u793e\u4f1a\u300b\u7eff\u8272\u91d1\u878d\u3001\u9ad8\u8d28\u91cf\u53d1\u5c55\u3001\u7eff\u8272\u8f6c\u578b\u8303\u56f4\uff1b\u672c\u884c\u4ec5\u4f5c\u6a21\u5757\u8fb9\u754c\u8bb0\u5f55\uff0c\u4e0d\u662f\u5fc5\u4fee\u56db\u4e3b\u89c2\u9898\u8bc4\u5206\u7ec6\u5219\u3002",
            h["evidence"]: "\u6559\u5e08\u7248\u9898\u9762+\u6b63\u5f0f\u8bc4\u6807/\u7ec6\u5219\u7f13\u5b58-\u6a21\u5757\u8fb9\u754c\uff08\u975e\u5fc5\u4fee\u56db\u8bc4\u5206\u7ec6\u5219\uff09",
            h["misplaced"]: "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u6392\u9664\u884c",
            h["thick"]: "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_CHAOYANG_MIDTERM_Q16_MODULE_BOUNDARY",
        },
        "M1278": {
            h["support"]: "\u6559\u5e08\u7248\u9898\u9762\u4e0e\u6b63\u5f0f\u8bc4\u6807/\u7ec6\u5219\u7f13\u5b58\u663e\u793a\uff1aQ17\u5c5e\u300a\u5f53\u4ee3\u56fd\u9645\u653f\u6cbb\u4e0e\u7ecf\u6d4e\u300b\u4eba\u5de5\u667a\u80fd+\u3001\u81ea\u4e3b\u5f00\u653e\u3001\u53d1\u5c55\u5b89\u5168\u8303\u56f4\uff1b\u672c\u884c\u4ec5\u4f5c\u6a21\u5757\u8fb9\u754c\u8bb0\u5f55\uff0c\u4e0d\u662f\u5fc5\u4fee\u56db\u4e3b\u89c2\u9898\u8bc4\u5206\u7ec6\u5219\u3002",
            h["evidence"]: "\u6559\u5e08\u7248\u9898\u9762+\u6b63\u5f0f\u8bc4\u6807/\u7ec6\u5219\u7f13\u5b58-\u6a21\u5757\u8fb9\u754c\uff08\u975e\u5fc5\u4fee\u56db\u8bc4\u5206\u7ec6\u5219\uff09",
            h["misplaced"]: "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u6392\u9664\u884c",
            h["thick"]: "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_CHAOYANG_MIDTERM_Q17_MODULE_BOUNDARY",
        },
    }

    touched: list[str] = []
    for row in rows:
        row_id = row.get(h["id"], "")
        if row_id in updates:
            row.update(updates[row_id])
            touched.append(row_id)

    missing = sorted(set(updates) - set(touched))
    if missing:
        raise RuntimeError(f"missing matrix rows: {missing}")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    now = datetime.now().strftime("%Y-%m-%d %H:%M +08")
    summary = {
        "status": "MATRIX_ONLY_CLOSURE_COMPLETE",
        "updated_at": now,
        "suite": "2026\u671d\u9633\u671f\u4e2d",
        "rows_updated": touched,
        "docx_changed": False,
        "evidence_boundary": "Q16/Q17 are module-boundary rows; teacher-answer wording is not counted as philosophy rubric evidence",
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# CHAOYANG_2026_MIDTERM_BOUNDARY_RISK_CLOSURE_20260525",
        "",
        "Status: `MATRIX_ONLY_CLOSURE_COMPLETE`",
        f"Updated: {now}",
        "",
        "## Scope",
        "",
        "- Suite: `2026\u671d\u9633\u671f\u4e2d`.",
        "- Rows updated: `M1277`, `M1278`.",
        "- DOCX changed: `no`.",
        "",
        "## Matrix Action",
        "",
        "- Q16 retained as an economy module-boundary row.",
        "- Q17 retained as an international-politics/economy module-boundary row.",
        "- Teacher-answer wording was not promoted to a philosophy scoring rubric.",
        "",
        "## ORDER_063 Upload Binding",
        "",
        "- Add this report, JSON sidecar, updated matrix, refreshed risk audit, and refreshed governance files to the future upload scope.",
        "- Upload remains deferred; no push is authorized during active recovery.",
    ]
    REPORT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
