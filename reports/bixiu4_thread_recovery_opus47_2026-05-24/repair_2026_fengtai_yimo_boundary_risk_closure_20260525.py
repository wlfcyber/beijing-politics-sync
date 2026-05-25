from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent
MATRIX = BASE / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = BASE / "FENGTAI_2026_YIMO_BOUNDARY_RISK_CLOSURE_20260525.md"
REPORT_JSON = BASE / "FENGTAI_2026_YIMO_BOUNDARY_RISK_CLOSURE_20260525.json"


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
        "M0547": {
            h["support"]: "Q19\u9898\u9762\u660e\u786e\u9650\u5b9a\u300a\u5f53\u4ee3\u56fd\u9645\u653f\u6cbb\u4e0e\u7ecf\u6d4e\u300b\uff0c\u6b63\u5f0f\u7b54\u6848\u7248PDF\u6307\u5411\u4eba\u7c7b\u547d\u8fd0\u5171\u540c\u4f53\u3001\u591a\u8fb9\u4e3b\u4e49\u3001\u5168\u7403\u6cbb\u7406\u89c2\u7b49\u56fd\u9645\u653f\u6cbb\u7ecf\u6d4e\u5185\u5bb9\uff1b\u672c\u884c\u4ec5\u4f5c\u6a21\u5757\u8fb9\u754c\u8bb0\u5f55\uff0c\u4e0d\u662f\u5fc5\u4fee\u56db\u4e3b\u89c2\u9898\u8bc4\u5206\u7ec6\u5219\u3002",
            h["evidence"]: "\u6b63\u5f0f\u7b54\u6848\u7248PDF\u9898\u9762+\u6a21\u5757\u8fb9\u754c\uff08\u975e\u5fc5\u4fee\u56db\u8bc4\u5206\u7ec6\u5219\uff09",
            h["misplaced"]: "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u6392\u9664\u884c",
            h["thick"]: "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_FENGTAI_YIMO_Q19_MODULE_BOUNDARY",
        },
        "M0548": {
            h["support"]: "Q20\u9898\u9762\u660e\u786e\u9650\u5b9a\u300a\u6cd5\u5f8b\u4e0e\u751f\u6d3b\u300b\uff0c\u6b63\u5f0f\u7b54\u6848\u7248PDF\u6307\u5411\u5b89\u5168\u4fdd\u969c\u4e49\u52a1\u3001\u4fb5\u6743\u8d23\u4efb\u3001\u53f8\u6cd5\u516c\u6b63\u7b49\u6cd5\u5f8b\u5185\u5bb9\uff1b\u672c\u884c\u4ec5\u4f5c\u6a21\u5757\u8fb9\u754c\u8bb0\u5f55\uff0c\u4e0d\u662f\u5fc5\u4fee\u56db\u4e3b\u89c2\u9898\u8bc4\u5206\u7ec6\u5219\u3002",
            h["evidence"]: "\u6b63\u5f0f\u7b54\u6848\u7248PDF\u9898\u9762+\u6a21\u5757\u8fb9\u754c\uff08\u975e\u5fc5\u4fee\u56db\u8bc4\u5206\u7ec6\u5219\uff09",
            h["misplaced"]: "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u6392\u9664\u884c",
            h["thick"]: "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_FENGTAI_YIMO_Q20_MODULE_BOUNDARY",
        },
        "M0849": {
            h["support"]: "\u5957\u5377\u7ea7\u8bb0\u5f55\u4e0d\u66ff\u4ee3\u9010\u9898\u7ec6\u5219\u6838\u9a8c\u3002Q19/Q20\u5df2\u6309\u6b63\u5f0f\u7b54\u6848\u7248PDF\u9898\u9762\u5b8c\u6210\u6a21\u5757\u8fb9\u754c\u95ed\u5408\uff0c\u4e0d\u8fdb\u5f53\u524d\u5fc5\u4fee\u56db\u54f2\u5b66\u6b63\u6587\u3002",
            h["evidence"]: "SUITE_LEVEL_RECHECKED_MODULE_BOUNDARY",
            h["misplaced"]: "\u4e0d\u9002\u7528",
            h["thick"]: "\u5426\uff1a\u9010\u9898\u56de\u6e90\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_FENGTAI_YIMO_SUITE_LEVEL_RECHECKED",
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
        "suite": "2026\u4e30\u53f0\u4e00\u6a21",
        "rows_updated": touched,
        "docx_changed": False,
        "evidence_boundary": "Q19/Q20 are module-boundary rows from formal answer-edition PDF stems, not philosophy scoring-rubric evidence",
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# FENGTAI_2026_YIMO_BOUNDARY_RISK_CLOSURE_20260525",
        "",
        "Status: `MATRIX_ONLY_CLOSURE_COMPLETE`",
        f"Updated: {now}",
        "",
        "## Scope",
        "",
        "- Suite: `2026\u4e30\u53f0\u4e00\u6a21`.",
        "- Rows updated: `M0547`, `M0548`, `M0849`.",
        "- DOCX changed: `no`.",
        "",
        "## Matrix Action",
        "",
        "- Q19 retained as an international-politics/economy module boundary row.",
        "- Q20 retained as a law module boundary row.",
        "- Suite-level thickening marker closed after row-level boundary review.",
        "- Ordinary answer wording was not promoted to a philosophy scoring rubric.",
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
