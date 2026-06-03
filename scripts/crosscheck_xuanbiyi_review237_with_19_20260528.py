from __future__ import annotations

import csv
from pathlib import Path


RUN_DIR = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/20_review237_verify_final_20260528")
FULL_CSV = RUN_DIR / "REVIEW237_FULL_PARSED.csv"
MD19 = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/19_error_report_patch_20260527/选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_错误核对修正版_20260527.md")


def main() -> None:
    text = MD19.read_text(encoding="utf-8", errors="ignore")
    rows = list(csv.DictReader(FULL_CSV.open(encoding="utf-8")))
    out = []
    for row in rows:
        sentence = row.get("sentence", "")
        question = row.get("question", "")
        # Strip parenthetical suffixes only for a looser question search.
        qkey = question.split("——", 1)[0].split("（", 1)[0].strip()
        out.append({
            "review_id": row["review_id"],
            "bucket": row["bucket"],
            "status": row["status"],
            "question": question,
            "sentence_exact_in_19": "YES" if sentence and sentence in text else "NO",
            "question_key_in_19": "YES" if qkey and qkey in text else "NO",
        })
    with (RUN_DIR / "REVIEW237_19_CROSSCHECK.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)
    counts = {
        "sentence_exact_in_19": sum(1 for r in out if r["sentence_exact_in_19"] == "YES"),
        "question_key_in_19": sum(1 for r in out if r["question_key_in_19"] == "YES"),
    }
    lines = ["# REVIEW237_19_CROSSCHECK_SUMMARY", ""]
    lines += [f"- total_rows: {len(out)}"]
    for k, v in counts.items():
        lines.append(f"- {k}: {v}")
    (RUN_DIR / "REVIEW237_19_CROSSCHECK_SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

