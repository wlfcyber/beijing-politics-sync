from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent
MATRIX = BASE / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = BASE / "SHIJINGSHAN_2026_ERMO_MATRIX_CLOSURE_20260525.md"
REPORT_JSON = BASE / "SHIJINGSHAN_2026_ERMO_MATRIX_CLOSURE_20260525.json"
SCORING_DOCX = "shijingshan_2026_ermo_scoring_extracted_20260525.docx"


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
        "note": fields[14],
        "artifact": "source_artifact",
    }

    support_common = (
        "\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u53c2\u8003\u7b2c17(3)\u9898\u660e\u793a\uff1a"
        "\u6b63\u786e\u4f7f\u75281\u4e2a\u54f2\u5b66\u89c2\u70b9\u6982\u62ec\u4e8c\u8005\u5173\u7cfb\u53ef\u5f971\u5206\uff0c"
        "\u8fd0\u75281\u4e2a\u54f2\u5b66\u89c2\u70b9\u8fdb\u884c\u6b63\u786e\u5206\u6790\u53ef\u5f972-4\u5206\uff0c"
        "\u5e76\u660e\u793a\u53ef\u4ece\u8054\u7cfb\u3001\u77db\u76fe\u3001\u5b9e\u8df5\u4e0e\u8ba4\u8bc6\u5173\u7cfb\u7b49\u89d2\u5ea6\u56de\u7b54\uff1b"
        "\u7b49\u7ea7\u8868\u7ed9\u51fa6-7\u5206\u6c34\u5e73\u63cf\u8ff0\u3002"
    )
    current_docx = (
        "\u5f53\u524dDOCX\u5df2\u5206\u522b\u6536\u201c2026\u77f3\u666f\u5c71\u4e8c\u6a21 \u7b2c17(3)\u9898\u201d"
        "\u8054\u7cfb\u89c2\u70b9\u3001\u77db\u76fe\u89c2\u70b9\u3001\u5b9e\u8df5\u4e0e\u8ba4\u8bc6\u5173\u7cfb\u4e09\u5904\u6b63\u6587\u6761\u76ee\u3002"
    )

    updates = {
        "M0046": {
            h["in_book"]: "\u662f\uff1a\u5df2\u8fdb\u5165\u5f53\u524dDOCX/PDF\u6b63\u6587",
            h["support"]: support_common + current_docx + "\u672c\u884c\u5bf9\u5e94\u8054\u7cfb\u89c2\u70b9\uff1b\u8bc1\u636e\u4e3a\u5bbd\u89d2\u5ea6+\u7b49\u7ea7\u8d4b\u5206\uff0c\u4e0d\u662f\u9010\u70b9\u7ec6\u5219\u3002",
            h["evidence"]: "\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u53c2\u8003-\u5bbd\u89d2\u5ea6+\u7b49\u7ea7\u8d4b\u5206+\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6",
            h["misplaced"]: "\u5426\uff1a\u5df2\u4e0e\u5f53\u524d\u6b63\u6587\u8054\u7cfb\u89c2\u70b9\u843d\u70b9\u5bf9\u9f50",
            h["thick"]: "\u5426\uff1a\u6b63\u5f0f\u8bc4\u5206\u53c2\u8003\u5bbd\u89d2\u5ea6\u5df2\u6838\u9a8c",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_SHIJINGSHAN_ERMO_Q17_3_CURRENT_DOCX_COVERED",
            h["artifact"]: SCORING_DOCX,
        },
        "M0047": {
            h["in_book"]: "\u662f\uff1a\u5df2\u8fdb\u5165\u5f53\u524dDOCX/PDF\u6b63\u6587",
            h["support"]: support_common + current_docx + "\u672c\u884c\u5bf9\u5e94\u77db\u76fe\u89c2\u70b9\uff1b\u8bc1\u636e\u4e3a\u5bbd\u89d2\u5ea6+\u7b49\u7ea7\u8d4b\u5206\uff0c\u4e0d\u662f\u9010\u70b9\u7ec6\u5219\u3002",
            h["evidence"]: "\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u53c2\u8003-\u5bbd\u89d2\u5ea6+\u7b49\u7ea7\u8d4b\u5206+\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6",
            h["misplaced"]: "\u5426\uff1a\u5df2\u4e0e\u5f53\u524d\u6b63\u6587\u77db\u76fe\u89c2\u70b9\u843d\u70b9\u5bf9\u9f50",
            h["thick"]: "\u5426\uff1a\u6b63\u5f0f\u8bc4\u5206\u53c2\u8003\u5bbd\u89d2\u5ea6\u5df2\u6838\u9a8c",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_SHIJINGSHAN_ERMO_Q17_3_CURRENT_DOCX_COVERED",
            h["artifact"]: SCORING_DOCX,
        },
        "M0048": {
            h["in_book"]: "\u662f\uff1a\u5df2\u8fdb\u5165\u5f53\u524dDOCX/PDF\u6b63\u6587",
            h["support"]: support_common + current_docx + "\u672c\u884c\u5bf9\u5e94\u5b9e\u8df5\u4e0e\u8ba4\u8bc6\u5173\u7cfb\uff1b\u8bc1\u636e\u4e3a\u5bbd\u89d2\u5ea6+\u7b49\u7ea7\u8d4b\u5206\uff0c\u4e0d\u662f\u9010\u70b9\u7ec6\u5219\u3002",
            h["evidence"]: "\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u53c2\u8003-\u5bbd\u89d2\u5ea6+\u7b49\u7ea7\u8d4b\u5206+\u5f53\u524dDOCX\u6b63\u6587\u8986\u76d6",
            h["misplaced"]: "\u5426\uff1a\u5df2\u4e0e\u5f53\u524d\u6b63\u6587\u5b9e\u8df5\u4e0e\u8ba4\u8bc6\u843d\u70b9\u5bf9\u9f50",
            h["thick"]: "\u5426\uff1a\u6b63\u5f0f\u8bc4\u5206\u53c2\u8003\u5bbd\u89d2\u5ea6\u5df2\u6838\u9a8c",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_SHIJINGSHAN_ERMO_Q17_3_CURRENT_DOCX_COVERED",
            h["artifact"]: SCORING_DOCX,
        },
        "M0853": {
            h["support"]: "\u5957\u5377\u7ea7\u8bb0\u5f55\u4e0d\u66ff\u4ee3\u9010\u9898\u7ec6\u5219\u6838\u9a8c\u3002\u672c\u8f6e\u5df2\u6838\u9a8cQ17(3)\u6b63\u5f0f\u7b54\u6848\u53ca\u8bc4\u5206\u53c2\u8003\u7684\u54f2\u5b66\u5bbd\u89d2\u5ea6\u4e0e\u7b49\u7ea7\u8868\uff0c\u5e76\u4e0e\u5f53\u524dDOCX\u4e09\u5904\u6b63\u6587\u843d\u70b9\u5bf9\u9f50\u3002",
            h["evidence"]: "SUITE_LEVEL_RECHECKED_FORMAL_SCORING_AND_DOCX",
            h["misplaced"]: "\u4e0d\u9002\u7528",
            h["thick"]: "\u5426\uff1a\u9010\u9898\u56de\u6e90\u5df2\u95ed\u5408",
            h["status"]: "MATRIX_ONLY_CLOSED_20260525_SHIJINGSHAN_ERMO_SUITE_LEVEL_RECHECKED",
            h["artifact"]: SCORING_DOCX,
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
        "status": "MATRIX_ONLY_CLOSURE_COMPLETE",
        "updated_at": now,
        "suite": "2026\u77f3\u666f\u5c71\u4e8c\u6a21",
        "rows_updated": touched,
        "docx_changed": False,
        "evidence_file": SCORING_DOCX,
        "current_docx_entries": [
            "Q17(3) contact-view entry",
            "Q17(3) contradiction-view entry",
            "Q17(3) practice-knowledge entry",
        ],
        "evidence_boundary": "formal scoring reference gives broad philosophy angles and level scoring, not point-by-point scoring rules",
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# SHIJINGSHAN_2026_ERMO_MATRIX_CLOSURE_20260525",
        "",
        "Status: `MATRIX_ONLY_CLOSURE_COMPLETE`",
        f"Updated: {now}",
        "",
        "## Scope",
        "",
        "- Suite: `2026\u77f3\u666f\u5c71\u4e8c\u6a21`.",
        "- Rows updated: `M0046`, `M0047`, `M0048`, `M0853`.",
        "- DOCX changed: `no`.",
        "",
        "## Evidence",
        "",
        f"- Formal scoring source converted for inspection: `{SCORING_DOCX}`.",
        "- Q17(3) scoring text names `contact`, `contradiction`, and `practice-knowledge relation` as optional philosophy angles.",
        "- The same source gives level scoring for correct philosophy use and analysis; it is broad-angle evidence, not point-by-point scoring rules.",
        "- Current DOCX already contains three Q17(3) entries for those same angles, so no new insertion was required.",
        "",
        "## Matrix Action",
        "",
        "- Reclassified the three old weak-evidence rows as current-DOCX covered with formal broad-angle/level-scoring support.",
        "- Closed the suite-level row after row-level source comparison.",
        "- Retained the evidence boundary: broad formal angle evidence supports existing entries, but is not inflated into detailed scoring-rule proof.",
        "",
        "## ORDER_063 Upload Binding",
        "",
        "- Add this report, JSON sidecar, extracted scoring DOCX, updated matrix, refreshed risk audit, and refreshed governance files to the future upload scope.",
        "- Upload remains deferred; no push is authorized during active recovery.",
    ]
    REPORT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
