from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent
MATRIX = BASE / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = BASE / "HAIDIAN_2024_MIDTERM_REMOVED_MISPLACEMENT_CLOSURE_20260525.md"
REPORT_JSON = BASE / "HAIDIAN_2024_MIDTERM_REMOVED_MISPLACEMENT_CLOSURE_20260525.json"


def main() -> None:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    h = {
        "id": "matrix_row_id",
        "in_book": fields[7],
        "support": fields[9],
        "evidence": fields[10],
        "misplaced": fields[11],
        "thick": fields[12],
        "status": fields[13],
        "note": fields[14],
    }

    ids = ["M0965", "M0966", "M0967"]
    support = (
        "\u7b2c18\u9898\u6b63\u5f0f\u8bc4\u5206\u7ec6\u5219\u660e\u786e\u77e5\u8bc6\u677f\u5757\u4e3a"
        "\u300a\u653f\u6cbb\u4e0e\u6cd5\u6cbb\u300b\u57fa\u5c42\u6c11\u4e3b\uff0c\u8bc4\u5206\u89d2\u5ea6\u4e3a"
        "\u515a\u7684\u9886\u5bfc\u3001\u5168\u8fc7\u7a0b\u4eba\u6c11\u6c11\u4e3b\u3001\u57fa\u5c42\u6c11\u4e3b\u3001"
        "\u534f\u5546\u6c11\u4e3b/\u6c11\u4e3b\u51b3\u7b56/\u6c11\u4e3b\u76d1\u7763/\u6c11\u4e3b\u7ba1\u7406\u3001"
        "\u591a\u5143\u4e3b\u4f53\u5171\u5efa\u5171\u6cbb\uff1b\u65e0\u5fc5\u4fee\u56db\u54f2\u5b66\u539f\u7406\u65b9\u6cd5\u8bba\u3002"
        "\u5f53\u524dDOCX\u590d\u6838\u672a\u547d\u4e2d\u201c2024\u6d77\u6dc0\u671f\u4e2d\u201d\uff0c\u8bef\u653e\u6761\u76ee\u5df2\u79fb\u9664\u3002"
    )

    touched: list[str] = []
    for row in rows:
        if row.get(h["id"]) not in ids:
            continue
        row[h["in_book"]] = "\u5426\uff1a\u8bef\u653e\u6761\u76ee\u5df2\u79fb\u9664\uff0c\u4e0d\u8fdb\u5f53\u524d\u5fc5\u4fee\u56db\u54f2\u5b66\u6b63\u6587"
        row[h["support"]] = support
        row[h["evidence"]] = "\u6b63\u5f0f\u8bc4\u5206\u7ec6\u5219\u53cd\u8bc1+\u5f53\u524dDOCX\u65e0\u547d\u4e2d"
        row[h["misplaced"]] = "\u5df2\u79fb\u9664\uff1a\u65e7DOCX\u8bef\u653e\u4e0d\u518d\u4f5c\u4e3a\u5f53\u524d\u6b63\u6587\u843d\u70b9"
        row[h["thick"]] = "\u5426\uff1a\u6a21\u5757\u8fb9\u754c\u5df2\u95ed\u5408"
        row[h["status"]] = "MATRIX_ONLY_CLOSED_20260525_HAIDIAN_MIDTERM_Q18_REMOVED_MISPLACEMENT"
        row[h["note"]] = "\u5f53\u524dDOCX\u6587\u672c\u590d\u6838\uff1a2024\u6d77\u6dc0\u671f\u4e2d\u547d\u4e2d0\u6b21\uff1b\u4fdd\u7559\u8fb9\u754c\u8bb0\u5f55\uff0c\u4e0d\u6062\u590d\u6b63\u6587\u3002"
        touched.append(row[h["id"]])

    missing = sorted(set(ids) - set(touched))
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
        "suite": "2024\u6d77\u6dc0\u671f\u4e2d",
        "rows_updated": touched,
        "docx_changed": False,
        "docx_hits_after_removal": 0,
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# HAIDIAN_2024_MIDTERM_REMOVED_MISPLACEMENT_CLOSURE_20260525",
        "",
        "Status: `MATRIX_ONLY_CLOSURE_COMPLETE`",
        f"Updated: {now}",
        "",
        "## Scope",
        "",
        "- Suite: `2024\u6d77\u6dc0\u671f\u4e2d`.",
        "- Rows updated: `M0965`, `M0966`, `M0967`.",
        "- DOCX changed: `no`.",
        "",
        "## Evidence",
        "",
        "- Q18 formal scoring source is a politics-and-law grassroots-democracy item, not a compulsory-book-four philosophy item.",
        "- Current DOCX text check found `0` hits for `2024\u6d77\u6dc0\u671f\u4e2d`; the old misplaced entries remain removed.",
        "",
        "## Matrix Action",
        "",
        "- Kept the rows as boundary records but removed the active misplaced-risk flag by marking them as removed, not active placements.",
        "- No DOCX insertion or render was required.",
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
