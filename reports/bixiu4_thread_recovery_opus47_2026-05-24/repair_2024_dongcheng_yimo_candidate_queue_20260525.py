from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent
MATRIX = BASE / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = BASE / "DONGCHENG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = BASE / "DONGCHENG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"
RENDER_DIR = "dongcheng_2024_yimo_source_pages_20260525"


def main() -> None:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    if not fields:
        raise RuntimeError("matrix header missing")

    h = {
        "id": "matrix_row_id",
        "source": fields[2],
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
        "artifact": "source_artifact",
    }

    updates: dict[str, dict[str, str]] = {
        "M0137": {
            h["in_book"]: "\u5426\uff1a\u65e7\u884c\u4e3a\u9898\u53f7\u8bef\u5207\uff1b\u771f\u6b63\u5bf9\u5e94\u7684\u7b2c21\u9898\u5df2\u5728\u5f53\u524dDOCX/PDF\u6b63\u6587\u8986\u76d6",
            h["node"]: "\u7cfb\u7edf\u4f18\u5316\u7684\u65b9\u6cd5 / \u6574\u4f53\u4e0e\u90e8\u5206\uff08\u7b2c21\u9898\u5df2\u8986\u76d6\uff09",
            h["support"]: "\u6e90\u5377\u7b2c4\u9898\u662f\u9009\u62e9\u9898\uff0c\u800c\u65e7\u884c\u6240\u6307\u201c\u4e09\u5708\u8054\u52a8/\u9996\u90fd\u90fd\u5e02\u5708\u201d\u5c5e\u7b2c21\u9898\u4e3b\u89c2\u9898\u3002\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u6807\u51c6\u7b2c21\u9898\u660e\u793a\u53ef\u4ece\u4ee5\u4eba\u6c11\u4e3a\u4e2d\u5fc3\u3001\u7cfb\u7edf\u4f18\u5316\u3001\u73b0\u4ee3\u5316\u4ea7\u4e1a\u4f53\u7cfb\u7b49\u89d2\u5ea6\u56de\u7b54\uff1b\u5f53\u524dDOCX\u5df2\u6536\u201c2024\u4e1c\u57ce\u4e00\u6a21 \u7b2c21\u9898\u201d\u7cfb\u7edf\u4f18\u5316\u6761\u76ee\u3002",
            h["evidence"]: "\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u6807\u51c6+\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6",
            h["misplaced"]: "\u5df2\u5254\u9664\uff1a\u65e7\u884c\u9898\u53f7\u8bef\u5207\uff0c\u4e0d\u4f5c\u4e3a\u7b2c4\u9898\u6b63\u6587\u843d\u70b9",
            h["thick"]: "\u5426\uff1a\u8bef\u5207\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_DONGCHENG_YIMO_Q4_MISCUT_TO_Q21",
            h["artifact"]: f"{RENDER_DIR}\\paper_page_02.png;{RENDER_DIR}\\answer_page_01.png",
        },
        "M0138": {
            h["in_book"]: "\u662f\uff1a\u5df2\u8fdb\u5165\u5f53\u524dDOCX/PDF\u6b63\u6587",
            h["node"]: "\u77db\u76fe\u666e\u904d\u6027\u4e0e\u7279\u6b8a\u6027\uff1b\u4ef7\u503c\u5224\u65ad\u4e0e\u4ef7\u503c\u9009\u62e9",
            h["support"]: "\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u6807\u51c6\u7b2c16\u9898\u660e\u793a\u53ef\u4ece\u8054\u7cfb\u3001\u53d1\u5c55\u3001\u4e2d\u534e\u6587\u5316\u7b49\u89d2\u5ea6\u56de\u7b54\uff1b\u5f53\u524dDOCX\u5df2\u6536\u201c2024\u4e1c\u57ce\u4e00\u6a21 \u7b2c16\u9898\u201d\u4e24\u5904\u6b63\u6587\u6761\u76ee\uff0c\u5206\u522b\u627f\u63a5\u77db\u76fe\u666e\u7279\u548c\u4ef7\u503c\u5224\u65ad\u843d\u70b9\u3002",
            h["evidence"]: "\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u6807\u51c6\u7b49\u7ea7\u63cf\u8ff0+\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6",
            h["misplaced"]: "\u5426\uff1a\u5df2\u4e0e\u73b0\u6709\u6b63\u6587\u843d\u70b9\u5bf9\u9f50",
            h["thick"]: "\u5426\uff1a\u5df2\u8986\u76d6",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_DONGCHENG_YIMO_Q16_DOCX_COVERED",
            h["artifact"]: f"{RENDER_DIR}\\answer_page_01.png",
        },
        "M0190": {
            h["in_book"]: "\u662f\uff1a\u5df2\u8fdb\u5165\u5f53\u524dDOCX/PDF\u6b63\u6587",
            h["node"]: "\u8054\u7cfb/\u77db\u76fe\u666e\u7279/\u4ef7\u503c\u89c2/\u6587\u5316\u7ebf",
            h["support"]: "\u5f53\u524dDOCX\u5df2\u6536\u201c2024\u4e1c\u57ce\u4e00\u6a21 \u7b2c16\u9898\u201d\u4e24\u5904\u6b63\u6587\u6761\u76ee\uff1b\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u6807\u51c6\u4e3a\u5f00\u653e\u7b49\u7ea7\u8bc4\u5206\uff0c\u53ef\u4ece\u8054\u7cfb\u3001\u53d1\u5c55\u3001\u4e2d\u534e\u6587\u5316\u7b49\u89d2\u5ea6\u56de\u7b54\u3002",
            h["evidence"]: "\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u6807\u51c6+\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6",
            h["misplaced"]: "\u5426\uff1a\u8986\u76d6\u5df2\u6838\u5b9a",
            h["thick"]: "\u5426\uff1a\u672c\u8f6e\u4e0d\u65b0\u589e",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_DONGCHENG_YIMO_Q16_DOCX_COVERED",
            h["artifact"]: f"{RENDER_DIR}\\answer_page_01.png",
        },
        "M0247": {
            h["in_book"]: "\u5426\uff1a\u9009\u62e9\u9898\u5ba2\u89c2\u7b54\u6848\u952e\u8fb9\u754c\uff0c\u4e0d\u4f5c\u4e3a\u4e3b\u89c2\u9898\u7ec6\u5219\u8fdb\u6b63\u6587",
            h["node"]: "\u4e0d\u5165\u5b9d\u5178\u6b63\u6587",
            h["support"]: "\u6e90\u5377\u7b2c1\u9898\u4e3a\u9009\u62e9\u9898\uff0c\u5b98\u65b9\u7b54\u6848\u952e\u4e3aC\u3002\u65e7Codex A\u5907\u6ce8\u6f02\u5230\u540e\u7eed\u8bb2\u8bc4/PPT\u7247\u6bb5\uff0c\u4e0d\u80fd\u4f5c\u4e3aQ1\u4e3b\u89c2\u9898\u8bc4\u5206\u7ec6\u5219\u3002",
            h["evidence"]: "\u5b98\u65b9\u7b54\u6848\u952e+\u9898\u9762\uff1b\u9009\u62e9\u9898\u8fb9\u754c\u5df2\u660e\u793a",
            h["misplaced"]: "\u5df2\u5254\u9664\uff1a\u65e7\u5019\u9009\u5907\u6ce8\u6f02\u79fb",
            h["thick"]: "\u5426\uff1a\u5ba2\u89c2\u9898\u8fb9\u754c\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_DONGCHENG_YIMO_Q1_CHOICE_BOUNDARY",
            h["artifact"]: f"{RENDER_DIR}\\paper_page_01.png;{RENDER_DIR}\\answer_page_01.png",
        },
        "M0248": {
            h["in_book"]: "\u5426\uff1a\u9009\u62e9\u9898\u5ba2\u89c2\u7b54\u6848\u952e\u8fb9\u754c\uff0c\u4e0d\u4f5c\u4e3a\u4e3b\u89c2\u9898\u7ec6\u5219\u8fdb\u6b63\u6587",
            h["node"]: "\u4e0d\u5165\u5b9d\u5178\u6b63\u6587",
            h["support"]: "\u6e90\u5377\u7b2c2\u9898\u4e3a\u9009\u62e9\u9898\uff0c\u5b98\u65b9\u7b54\u6848\u952e\u4e3aB\u3002\u65e7Codex A\u5907\u6ce8\u6f02\u5230\u540e\u7eed\u8bb2\u8bc4/PPT\u7247\u6bb5\uff0c\u4e0d\u80fd\u4f5c\u4e3aQ2\u4e3b\u89c2\u9898\u8bc4\u5206\u7ec6\u5219\u3002",
            h["evidence"]: "\u5b98\u65b9\u7b54\u6848\u952e+\u9898\u9762\uff1b\u9009\u62e9\u9898\u8fb9\u754c\u5df2\u660e\u793a",
            h["misplaced"]: "\u5df2\u5254\u9664\uff1a\u65e7\u5019\u9009\u5907\u6ce8\u6f02\u79fb",
            h["thick"]: "\u5426\uff1a\u5ba2\u89c2\u9898\u8fb9\u754c\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_DONGCHENG_YIMO_Q2_CHOICE_BOUNDARY",
            h["artifact"]: f"{RENDER_DIR}\\paper_page_01.png;{RENDER_DIR}\\answer_page_01.png",
        },
        "M0249": {
            h["in_book"]: "\u5426\uff1a\u65e7\u5019\u9009\u9898\u53f7\u8bef\u5207\uff1b\u7b2c4\u9898\u672c\u8eab\u4e3a\u9009\u62e9\u9898\uff0c\u771f\u6b63\u4e3b\u89c2\u9898\u94fe\u6761\u4e3a\u7b2c21\u9898\u4e14\u5df2\u5165\u6b63\u6587",
            h["node"]: "\u4e0d\u65b0\u589e\uff1b\u7b2c21\u9898\u5df2\u5728\u7cfb\u7edf\u4f18\u5316\u8282\u70b9\u8986\u76d6",
            h["support"]: "\u6e90\u5377\u7b2c4\u9898\u4e3a\u9009\u62e9\u9898\uff0c\u5b98\u65b9\u7b54\u6848\u952e\u4e3aA\u3002\u65e7\u5907\u6ce8\u4e2d\u201c\u4e09\u5708\u8054\u52a8/\u9996\u90fd\u90fd\u5e02\u5708\u201d\u5c5e\u7b2c21\u9898\u4e3b\u89c2\u9898\uff1b\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u6807\u51c6\u7b2c21\u9898\u660e\u793a\u7cfb\u7edf\u4f18\u5316\u7b49\u89d2\u5ea6\uff0c\u5f53\u524dDOCX\u5df2\u6536\u7b2c21\u9898\u7cfb\u7edf\u4f18\u5316\u6761\u76ee\u3002",
            h["evidence"]: "\u5b98\u65b9\u7b54\u6848\u952e+\u6b63\u5f0f\u8bc4\u5206\u6807\u51c6+\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6",
            h["misplaced"]: "\u5df2\u5254\u9664\uff1aQ4\u5019\u9009\u5b9e\u4e3aQ21\u8bef\u5207",
            h["thick"]: "\u5426\uff1a\u8bef\u5207\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_DONGCHENG_YIMO_Q4_CHOICE_AND_Q21_COVERED",
            h["artifact"]: f"{RENDER_DIR}\\paper_page_02.png;{RENDER_DIR}\\answer_page_01.png",
        },
        "M0250": {
            h["in_book"]: "\u5426\uff1a\u5957\u5377\u7ea7\u62bd\u53d6\u6f02\u79fb\uff0c\u4e0d\u4f5c\u4e3a\u72ec\u7acb\u8fdb\u6b63\u6587\u6761\u76ee",
            h["node"]: "SUITE_LEVEL_REVIEW_CLOSED",
            h["support"]: "\u8be5\u884c\u4e3a\u8bb2\u8bc4/PPT\u7247\u6bb5\u7684\u5957\u5377\u7ea7\u805a\u5408\uff0c\u4e0d\u662f\u5355\u4e00\u53ef\u91c7\u5206\u9898\u3002\u672c\u8f6e\u9010\u9898\u88c1\u51b3\uff1aQ1/Q2/Q4\u4e3a\u9009\u62e9\u9898\u5ba2\u89c2\u7b54\u6848\u952e\u8fb9\u754c\uff1bQ16\u548cQ21\u5df2\u6709\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6\u3002",
            h["evidence"]: "\u9010\u9898\u56de\u6e90\u88c1\u51b3+\u5f53\u524dDOCX\u6b63\u6587\u5bf9\u9f50",
            h["misplaced"]: "\u4e0d\u9002\u7528\uff1a\u5957\u5377\u62bd\u53d6\u884c\u5df2\u62c6\u89e3",
            h["thick"]: "\u5426\uff1a\u5957\u5377\u805a\u5408\u884c\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_DONGCHENG_YIMO_SUITE_EXTRACTION_CLOSED",
            h["artifact"]: f"{RENDER_DIR}\\paper_page_01.png;{RENDER_DIR}\\paper_page_02.png;{RENDER_DIR}\\answer_page_01.png",
        },
        "M0817": {
            h["in_book"]: "\u5957\u5377\u6709\u6700\u7ec8DOCX\u63d0\u53ca\u6216\u95ed\u5408\u8bb0\u5f55",
            h["node"]: "SUITE_LEVEL_SUMMARY_CLOSED",
            h["support"]: "\u5957\u5377\u7ea7\u8bb0\u5f55\u4e0d\u66ff\u4ee3\u9010\u9898\u7ec6\u5219\u6838\u9a8c\u3002\u672c\u8f6e\u5df2\u5b8c\u6210Q1/Q2/Q4\u9009\u62e9\u9898\u8fb9\u754c\u88c1\u51b3\uff0cQ16/Q21\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6\u6838\u5b9a\u3002",
            h["evidence"]: "SUITE_LEVEL_RECHECKED_SOURCE_RENDER_AND_DOCX",
            h["misplaced"]: "\u4e0d\u9002\u7528",
            h["thick"]: "\u5426\uff1a\u9010\u9898\u56de\u6e90\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_DONGCHENG_YIMO_SUITE_LEVEL_RECHECKED",
            h["artifact"]: f"{RENDER_DIR}\\paper_page_01.png;{RENDER_DIR}\\paper_page_02.png;{RENDER_DIR}\\answer_page_01.png",
        },
    }

    touched: list[str] = []
    for row in rows:
        row_id = row.get(h["id"], "")
        if row_id not in updates:
            continue
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
        "status": "MATRIX_ONLY_REPAIR_COMPLETE",
        "updated_at": now,
        "suite": "2024\u4e1c\u57ce\u4e00\u6a21",
        "rows_updated": touched,
        "docx_changed": False,
        "source_renders": [
            f"{RENDER_DIR}/paper_page_01.png",
            f"{RENDER_DIR}/paper_page_02.png",
            f"{RENDER_DIR}/answer_page_01.png",
        ],
        "decisions": [
            "Q1 and Q2 are objective choice-question answer-key boundaries, not main-question rubric insertions.",
            "Old Q4 candidate was a row-slicing error: the source Q4 is a choice question, while the three-circle rubric text belongs to Q21 already covered in DOCX.",
            "Q16 and Q21 remain covered by current DOCX body entries; no DOCX insertion was needed.",
            "Suite-level row was downgraded to a closed summary after row-level source review.",
        ],
    }

    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# DONGCHENG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525",
        "",
        "Status: `MATRIX_ONLY_REPAIR_COMPLETE`",
        f"Updated: {now}",
        "",
        "## Scope",
        "",
        "- Suite: `2024\u4e1c\u57ce\u4e00\u6a21`.",
        "- Rows updated: `M0137`, `M0138`, `M0190`, `M0247`, `M0248`, `M0249`, `M0250`, `M0817`.",
        "- DOCX changed: `no`.",
        "",
        "## Source Review",
        "",
        f"- Rendered source pages: `{RENDER_DIR}/paper_page_01.png`, `{RENDER_DIR}/paper_page_02.png`, `{RENDER_DIR}/answer_page_01.png`.",
        "- Q1: source paper shows a choice question; official answer key is `C`; old production note drifted into later lecture/PPT material and was removed as a body candidate.",
        "- Q2: source paper shows a choice question; official answer key is `B`; old production note drifted into later lecture/PPT material and was removed as a body candidate.",
        "- Q4: source paper shows a choice question; official answer key is `A`; the old candidate text about three-circle linkage belongs to Q21, not Q4.",
        "- Q16: official answer/scoring standard allows philosophy/culture angles; current DOCX already carries Q16 body entries.",
        "- Q21: official answer/scoring standard names system optimization and related angles; current DOCX already carries the Q21 system-optimization body entry.",
        "",
        "## Matrix Action",
        "",
        "- Closed Q1/Q2/Q4 candidate rows as objective-key or row-slicing boundaries.",
        "- Closed Q16 current-body comparison rows against current DOCX coverage.",
        "- Closed Qunknown and suite-level rows as source-reviewed summaries, not independent body insertions.",
        "- No ordinary reference answer was promoted to a scoring-rule source; answer-key rows remain labeled as objective-choice boundaries.",
        "",
        "## ORDER_063 Upload Binding",
        "",
        "- Add this repair report, JSON sidecar, render evidence directory, updated matrix, refreshed risk audit, and refreshed Governor/Confucius/status files to the future final upload scope.",
        "- Upload remains deferred until all active Beijing politics lines reach a terminal or user-approved blocker state and the pre-push secret scan passes.",
    ]
    REPORT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
