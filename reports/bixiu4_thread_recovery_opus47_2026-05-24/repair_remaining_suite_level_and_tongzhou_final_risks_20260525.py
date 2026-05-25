from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent
MATRIX = BASE / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = BASE / "REMAINING_SUITE_LEVEL_AND_TONGZHOU_FINAL_RISK_CLOSURE_20260525.md"
REPORT_JSON = BASE / "REMAINING_SUITE_LEVEL_AND_TONGZHOU_FINAL_RISK_CLOSURE_20260525.json"


SUITE_ROWS = [
    "M0814",
    "M0816",
    "M0818",
    "M0820",
    "M0823",
    "M0824",
    "M0826",
    "M0827",
    "M0829",
    "M0832",
    "M0834",
    "M0839",
    "M0842",
]


def main() -> None:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    h = {
        "id": "matrix_row_id",
        "question": fields[5],
        "type": fields[6],
        "in_book": fields[7],
        "node": fields[8],
        "support": fields[9],
        "evidence": fields[10],
        "misplaced": fields[11],
        "thick": fields[12],
        "status": fields[13],
        "note": fields[14],
    }

    suite_support = (
        "\u5957\u5377\u7ea7\u8bb0\u5f55\u4ec5\u4f5c\u8986\u76d6\u6458\u8981\uff0c\u4e0d\u66ff\u4ee3\u9010\u9898\u7ec6\u5219\u6838\u9a8c\uff0c"
        "\u4e5f\u4e0d\u5355\u72ec\u652f\u6301\u65b0\u589e\u6b63\u6587\u6761\u76ee\u3002\u5f53\u524d\u98ce\u9669\u5ba1\u8ba1\u4e2d\u8be5\u5957\u5377\u65e0\u9700\u8981"
        "\u518d\u7531\u5957\u5377\u7ea7\u884c\u89e6\u53d1\u7684\u6b63\u6587\u8865\u539a\u9879\uff1b\u82e5\u540e\u7eed\u91cd\u5f00\uff0c\u5fc5\u987b\u56de\u5230\u5177\u4f53\u9898\u53f7\u548c\u6b63\u5f0f\u8bc4\u5206\u6765\u6e90\u3002"
    )

    touched_suite: list[str] = []
    touched_tongzhou = False
    for row in rows:
        row_id = row.get(h["id"], "")
        if row_id in SUITE_ROWS:
            row[h["support"]] = suite_support
            row[h["evidence"]] = "SUITE_LEVEL_SUMMARY_RECHECKED_NO_OPEN_ROW_RISK"
            row[h["misplaced"]] = "\u4e0d\u9002\u7528"
            row[h["thick"]] = "\u5426\uff1a\u5957\u5377\u7ea7\u6458\u8981\u884c\u5df2\u964d\u7ea7\u4e3a\u95ed\u5408\u8bb0\u5f55"
            row[h["status"]] = "MATRIX_ONLY_CLOSED_20260525_SUITE_LEVEL_SUMMARY_DOWNGRADED"
            row[h["note"]] = "\u672c\u884c\u4ec5\u4fdd\u7559\u4e3a\u5957\u5377\u6458\u8981\uff1b\u4e0d\u7528\u4e8e\u4ee3\u66ff\u9010\u9898\u8bc1\u636e\u6216\u751f\u6210\u6b63\u6587\u3002"
            touched_suite.append(row_id)
        elif row_id == "M1471":
            row[h["in_book"]] = "\u5426\uff1a\u6b63\u5f0f\u7ec6\u5219\u4ec5\u7ed9\u5bbd\u89d2\u5ea6\u601d\u7ef4\u63d0\u793a\uff0c\u4e0d\u5f3a\u884c\u8fdb\u5165\u5177\u4f53\u77db\u76fe\u8282\u70b9\u6b63\u6587"
            row[h["support"]] = "\u6b63\u5f0f\u7ec6\u5219\u7b2c21\u9898\u5bbd\u6cdb\u5217\u51fa\u79d1\u5b66\u601d\u7ef4\u3001\u8fa9\u8bc1\u601d\u7ef4\u3001\u77db\u76fe\u89c2\u7b49\u89d2\u5ea6\uff1b\u56e0\u672a\u843d\u5230\u5177\u4f53\u77db\u76fe\u8282\u70b9\u6216\u53ef\u62c6\u5206\u91c7\u5206\u70b9\uff0c\u672c\u8f6e\u4ec5\u4f5c\u5bbd\u89d2\u5ea6\u8fb9\u754c\u8bb0\u5f55\uff0c\u4e0d\u628a\u5bbd\u8bcd\u5f3a\u884c\u653e\u5165\u6b63\u6587\u3002",
            row[h["evidence"]] = "\u6b63\u5f0f\u8bc4\u5206\u7ec6\u5219\u5bbd\u89d2\u5ea6-\u8fb9\u754c\u95ed\u5408"
            row[h["misplaced"]] = "\u5426\uff1a\u5bbd\u89d2\u5ea6\u8fb9\u754c\u8bb0\u5f55"
            row[h["thick"]] = "\u5426\uff1a\u5bbd\u89d2\u5ea6\u4e0d\u5f3a\u884c\u5165\u6b63\u6587\uff1b\u540e\u7eed\u82e5\u8981\u65b0\u589e\u987b\u91cd\u5f00\u5177\u4f53\u7ec6\u5219\u843d\u70b9"
            row[h["status"]] = "MATRIX_ONLY_CLOSED_20260525_TONGZHOU_FINAL_Q21_BROAD_TERM_BOUNDARY"
            row[h["note"]] = "\u4fdd\u7559\u4e3a\u6b63\u5f0f\u7ec6\u5219\u5bbd\u89d2\u5ea6\u8fb9\u754c\uff0c\u4e0d\u4f5c\u4e3a\u5f53\u524d\u6b63\u6587\u8865\u539a\u9879\u3002"
            touched_tongzhou = True

    missing_suite = sorted(set(SUITE_ROWS) - set(touched_suite))
    if missing_suite or not touched_tongzhou:
        raise RuntimeError(f"missing suite rows={missing_suite}, tongzhou={touched_tongzhou}")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    now = datetime.now().strftime("%Y-%m-%d %H:%M +08")
    summary = {
        "status": "MATRIX_ONLY_RISK_QUEUE_CLOSED",
        "updated_at": now,
        "suite_level_rows_closed": touched_suite,
        "tongzhou_final_row_closed": "M1471",
        "docx_changed": False,
        "evidence_boundary": "suite-level rows remain summaries only; Tongzhou final Q21 broad thinking angle is not forced into body",
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# REMAINING_SUITE_LEVEL_AND_TONGZHOU_FINAL_RISK_CLOSURE_20260525",
        "",
        "Status: `MATRIX_ONLY_RISK_QUEUE_CLOSED`",
        f"Updated: {now}",
        "",
        "## Scope",
        "",
        f"- Suite-level summary rows closed: `{len(touched_suite)}`.",
        "- Tongzhou Final broad-angle row closed: `M1471`.",
        "- DOCX changed: `no`.",
        "",
        "## Matrix Action",
        "",
        "- Downgraded suite-level rows to closed summaries that cannot replace row-level evidence or trigger body insertions.",
        "- Closed 2026 Tongzhou Final Q21 broad thinking-angle row as a boundary record only; broad terms were not forced into a concrete contradiction node.",
        "- No ordinary reference answer was promoted to scoring-rule evidence.",
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
