#!/usr/bin/env python3
"""Build the Phase11D combined source-verified review draft.

This is a mechanical artifact builder. It only combines entries that already
contain the four required student-facing headings; source notes and review
headers are intentionally left out of the combined body.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUTS = [
    ROOT / "09_student_draft/phase11D_seed_source_verified_08_V2_REVIEW_ONLY.md",
    ROOT / "09_student_draft/phase11D_batch02_source_verified_05_REVIEW_ONLY.md",
    ROOT / "09_student_draft/phase11D_batch03_source_verified_05_REVIEW_ONLY.md",
    ROOT / "09_student_draft/phase11D_batch04_source_verified_11_REVIEW_ONLY.md",
]
OUT_MD = ROOT / "09_student_draft/phase11D_combined_source_verified_29_REVIEW_ONLY.md"
OUT_CSV = ROOT / "09_student_draft/phase11D_combined_source_verified_29_index.csv"
REQUIRED = ["【材料触发点】", "【设问】", "【为什么能想到】", "【答案落点】"]


def extract_entries(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^##\s+(.+)$", text))
    rows: list[dict[str, str]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        title = match.group(1).strip()
        chunk = text[start:end].strip()
        if all(h in chunk for h in REQUIRED):
            rows.append({"title": title, "source_file": path.name, "body": chunk})
    return rows


def main() -> int:
    rows: list[dict[str, str]] = []
    for path in INPUTS:
        rows.extend(extract_entries(path))

    body_lines = [
        "# 选必三《逻辑与思维》Phase11D 四要件源核合并候选稿",
        "",
        "本稿由 Phase11D seed、Batch02、Batch03、Batch04 合并生成，共 29 条。它只用于四线审稿和后续成品化，不是终稿，不授权 Word/PDF/final。",
        "",
        "---",
        "",
    ]
    for row in rows:
        body_lines.append(row["body"])
        body_lines.append("")
        body_lines.append("---")
        body_lines.append("")

    OUT_MD.write_text("\n".join(body_lines).rstrip() + "\n", encoding="utf-8")

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["order", "title", "source_file"])
        writer.writeheader()
        for order, row in enumerate(rows, 1):
            writer.writerow({"order": order, "title": row["title"], "source_file": row["source_file"]})

    print(f"entries={len(rows)}")
    print(f"wrote={OUT_MD}")
    print(f"wrote={OUT_CSV}")
    return 0 if len(rows) == 29 else 1


if __name__ == "__main__":
    raise SystemExit(main())
