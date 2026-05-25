from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent
MATRIX = BASE / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = BASE / "HAIDIAN_2024_YIMO_MATRIX_CLOSURE_20260525.md"
REPORT_JSON = BASE / "HAIDIAN_2024_YIMO_MATRIX_CLOSURE_20260525.json"


def main() -> None:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    h = {
        "id": "matrix_row_id",
        "in_book": fields[7],
        "node": fields[8],
        "support": fields[9],
        "evidence": fields[10],
        "misplaced": fields[11],
        "thick": fields[12],
        "status": fields[13],
        "artifact": "source_artifact",
    }

    scoring = (
        "2024\u5404\u533a\u6a21\u62df\u9898\\2024\u5404\u533a\u4e00\u6a21\\2024\u6d77\u6dc0\u4e00\u6a21\\"
        "\u7ec6\u5219\\2024\u6d77\u6dc0\u4e00\u6a21\u7ec6\u5219.docx"
    )
    support_q16 = (
        "\u6b63\u5f0f\u7ec6\u5219\u7b2c16\u9898\u660e\u793a\u53ef\u4ece\u53d1\u6325\u4e3b\u89c2\u80fd\u52a8\u6027\u3001"
        "\u8054\u7cfb\u7684\u89c2\u70b9\u3001\u53d1\u5c55\u7684\u89c2\u70b9\u3001\u5b9e\u8df5\u7684\u89c2\u70b9\u3001"
        "\u6c11\u65cf\u7cbe\u795e\u7b49\u89d2\u5ea6\u4f5c\u7b54\uff1b\u5f53\u524dDOCX\u5df2\u6536"
        "\u201c2024\u6d77\u6dc0\u4e00\u6a21 \u7b2c16\u9898\u201d\u4e3b\u89c2\u80fd\u52a8\u6027\u3001\u8054\u7cfb\u3001"
        "\u53d1\u5c55\u3001\u5b9e\u8df5\u7b49\u6b63\u6587\u6761\u76ee\u3002\u8be5\u8bc1\u636e\u662f\u6b63\u5f0f\u7ec6\u5219"
        "\u5bbd\u89d2\u5ea6\uff0c\u4e0d\u662f\u9010\u70b9\u7ec6\u5219\u3002"
    )

    updates = {
        "M0200": {
            h["in_book"]: "\u662f\uff1a\u5df2\u8fdb\u5165\u5f53\u524dDOCX/PDF\u6b63\u6587",
            h["node"]: "\u4e3b\u89c2\u80fd\u52a8\u6027/\u8054\u7cfb/\u53d1\u5c55/\u5b9e\u8df5/\u6c11\u65cf\u7cbe\u795e",
            h["support"]: support_q16,
            h["evidence"]: "\u6b63\u5f0f\u7ec6\u5219-\u5bbd\u89d2\u5ea6+\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6",
            h["misplaced"]: "\u5426\uff1a\u5df2\u4e0e\u5f53\u524dQ16\u6b63\u6587\u843d\u70b9\u5bf9\u9f50",
            h["thick"]: "\u5426\uff1a\u6b63\u5f0f\u7ec6\u5219\u5bbd\u89d2\u5ea6\u5df2\u6838\u9a8c",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_HAIDIAN_2024_YIMO_Q16_DOCX_COVERED",
            h["artifact"]: scoring,
        },
        "M0299": {
            h["in_book"]: "\u5426\uff1aQ17\u9898\u7ec4\u4e0d\u65b0\u589e\uff1bQ17(2)\u8bef\u653e\u6761\u76ee\u5df2\u4eceDOCX\u79fb\u9664",
            h["node"]: "Q17(2)\u5e94\u8def\u7531\u9009\u5fc5\u4e09\u5206\u6790\u4e0e\u7efc\u5408\uff1bQ17(1)\u7ecf\u6d4e\uff1bQ17(3)\u653f\u6cbb\u4e0e\u6cd5\u6cbb",
            h["support"]: "\u6b63\u5f0f\u7ec6\u5219\u663e\u793aQ17(2)\u4e3a\u5206\u6790\u4e0e\u7efc\u5408\u601d\u7ef4\u65b9\u6cd5\uff0cQ17(1)\u5c5e\u7ecf\u6d4e\u7ebf\uff0cQ17(3)\u5c5e\u653f\u6cbb\u4e0e\u6cd5\u6cbb\u7ebf\uff1b\u65e7DOCX\u7cfb\u7edf\u89c2\u5ff5\u8bef\u653e\u5df2\u5728Batch02\u79fb\u9664\u3002",
            h["evidence"]: "\u5f3a\u7ec6\u5219+\u6a21\u5757\u8fb9\u754c+\u5df2\u79fb\u9664\u8bef\u653e",
            h["misplaced"]: "\u5df2\u79fb\u9664\uff1a\u65e7Q17(2)\u7cfb\u7edf\u89c2\u5ff5\u6761\u76ee\u4e0d\u518d\u4fdd\u7559\u4e3a\u5fc5\u4fee\u56db\u6b63\u6587",
            h["thick"]: "\u5426\uff1a\u5f53\u524d\u54f2\u5b66\u5b9d\u5178\u4e0d\u8865",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_HAIDIAN_2024_YIMO_Q17_MISPLACED_REMOVED",
            h["artifact"]: scoring,
        },
        "M0821": {
            h["support"]: "\u5957\u5377\u7ea7\u8bb0\u5f55\u4e0d\u66ff\u4ee3\u9010\u9898\u7ec6\u5219\u6838\u9a8c\u3002\u672c\u8f6e\u5df2\u6838\u9a8cQ16\u6b63\u5f0f\u7ec6\u5219\u5bbd\u89d2\u5ea6\u4e0e\u5f53\u524dDOCX\u591a\u8282\u70b9\u8986\u76d6\uff0c\u5e76\u786e\u8ba4Q17\u8bef\u653e\u5df2\u79fb\u9664\u4e14\u4e0d\u5c5e\u5fc5\u4fee\u56db\u6b63\u6587\u8865\u5145\u8303\u56f4\u3002",
            h["evidence"]: "SUITE_LEVEL_RECHECKED_FORMAL_SCORING_AND_DOCX",
            h["misplaced"]: "\u4e0d\u9002\u7528",
            h["thick"]: "\u5426\uff1a\u9010\u9898\u56de\u6e90\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_HAIDIAN_2024_YIMO_SUITE_LEVEL_RECHECKED",
            h["artifact"]: scoring,
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
        "suite": "2024\u6d77\u6dc0\u4e00\u6a21",
        "rows_updated": touched,
        "docx_changed": False,
        "evidence_boundary": "Q16 has formal broad-angle scoring support and current DOCX body coverage; Q17 is a removed module-boundary misplacement",
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# HAIDIAN_2024_YIMO_MATRIX_CLOSURE_20260525",
        "",
        "Status: `MATRIX_ONLY_CLOSURE_COMPLETE`",
        f"Updated: {now}",
        "",
        "## Scope",
        "",
        "- Suite: `2024\u6d77\u6dc0\u4e00\u6a21`.",
        "- Rows updated: `M0200`, `M0299`, `M0821`.",
        "- DOCX changed: `no`.",
        "",
        "## Evidence",
        "",
        "- Formal scoring source: `2024\u6d77\u6dc0\u4e00\u6a21\u7ec6\u5219.docx`.",
        "- Q16 scoring source gives broad philosophy/culture angles, including subjectivity, contact, development, practice, and national spirit.",
        "- Current DOCX already contains Q16 body entries across those philosophy nodes.",
        "- Q17(2) is an analysis/synthesis thinking-method item; old system-view placement was removed earlier and remains excluded from this philosophy body.",
        "",
        "## Matrix Action",
        "",
        "- Reclassified Q16 as current-DOCX covered with formal broad-angle support.",
        "- Closed Q17 as a removed module-boundary misplacement without triggering the active misplaced-risk flag.",
        "- Closed the suite-level row after row-level source review.",
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
