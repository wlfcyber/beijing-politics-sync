from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

import apply_p0_thickness_batch01_20260525 as helper
from docx import Document


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "P1_SUBJECTIVE_CANDIDATE_INSPECTION_20260526.md"


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M +08")


def main() -> int:
    queue_path = ROOT / "THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.csv"
    rows: list[dict[str, str]] = []
    with queue_path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row["priority"] == "P1" and row["question_kind"] == "subjective" and int(row["answer_chars"]) < 120:
                rows.append(row)
            if len(rows) >= 30:
                break

    doc = Document(str(helper.current_docx()))
    blocks = helper.entry_blocks(doc)
    lines = [
        "# P1 Subjective Candidate Inspection 20260526",
        "",
        f"Updated: {now()}",
        "",
        "Selection: first 30 current P1 subjective rows with answer length under 120 chars.",
        "",
    ]
    for idx, row in enumerate(rows, 1):
        excerpt = row["answer_excerpt"]
        matches = [
            block
            for block in blocks
            if block["heading"] == row["heading"]
            and excerpt in str(block.get("fields", {}).get("answer", ""))
        ]
        lines.extend(
            [
                f"## {idx}. {row['queue_id']} {row['heading']}",
                "",
                f"- why chars: `{row['why_chars']}`",
                f"- answer chars: `{row['answer_chars']}`",
                f"- match count: `{len(matches)}`",
                f"- old answer excerpt: {excerpt}",
                "",
            ]
        )
        if matches:
            fields = matches[0]["fields"]
            lines.extend(
                [
                    f"**Material**: {fields.get('material', '')}",
                    "",
                    f"**Question**: {fields.get('question', '')}",
                    "",
                    f"**Why**: {fields.get('why', '')}",
                    "",
                    f"**Answer**: {fields.get('answer', '')}",
                    "",
                ]
            )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(str(OUT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
