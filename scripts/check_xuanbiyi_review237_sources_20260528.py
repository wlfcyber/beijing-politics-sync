from __future__ import annotations

import csv
import re
from pathlib import Path


RUN_DIR = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/20_review237_verify_final_20260528")
SOURCE_DIR = RUN_DIR / "source_texts"
FULL_CSV = RUN_DIR / "REVIEW237_FULL_PARSED.csv"


def norm(text: str) -> str:
    return re.sub(r"[\s，。、“”‘’：；;,.!！?？（）()《》【】\[\]\"'·\-—/]+", "", text)


def suite_from_question(question: str) -> str:
    m = re.match(r"(20\d{2})([^Q（(——]+)", question)
    if not m:
        return ""
    year = m.group(1)
    rest = m.group(2)
    for district in ["海淀", "丰台", "西城", "东城", "朝阳", "顺义", "门头沟", "延庆", "房山", "石景山", "昌平", "通州"]:
        if district in rest:
            # special 2024 names without year in directory are normalized by source builder.
            exam_type = ""
            if "期中" in rest:
                exam_type = "期中"
            elif "期末" in rest:
                exam_type = "期末"
            elif "一模" in rest:
                exam_type = "一模"
            elif "二模" in rest:
                exam_type = "二模"
            return f"{year}{district}{exam_type}"
    return ""


def longest_found(fragment: str, source_norm: str) -> str:
    f = norm(fragment)
    if not f:
        return ""
    max_len = min(len(f), 30)
    for length in range(max_len, 3, -1):
        for i in range(0, len(f) - length + 1):
            sub = f[i : i + length]
            if sub in source_norm:
                return sub
    return ""


def split_clauses(text: str) -> list[str]:
    if not text:
        return []
    return [c.strip() for c in re.split(r"[；;]", text) if c.strip()]


def main() -> None:
    rows = list(csv.DictReader(FULL_CSV.open(encoding="utf-8")))
    source_cache: dict[str, tuple[str, str]] = {}
    out: list[dict[str, str]] = []
    for row in rows:
        suite = suite_from_question(row["question"])
        source_path = SOURCE_DIR / f"{suite}.txt"
        if suite and source_path.exists():
            if suite not in source_cache:
                text = source_path.read_text(encoding="utf-8", errors="ignore")
                source_cache[suite] = (text, norm(text))
            source_text, source_norm = source_cache[suite]
        else:
            source_text, source_norm = "", ""

        clauses = split_clauses(row.get("missing_clause", ""))
        clause_results = []
        for clause in clauses:
            best = longest_found(clause, source_norm)
            clause_results.append(f"{clause}=>{best or 'NO_SOURCE_MATCH'}")

        sentence_best = longest_found(row.get("sentence", ""), source_norm)
        hit_best = longest_found(row.get("hit", ""), source_norm)

        if row["status"] in {"✅高度匹配", "✅基本匹配"}:
            initial = "ACCEPT_REVIEW_STATUS_NO_PATCH"
        elif clauses and any("NO_SOURCE_MATCH" in x for x in clause_results):
            initial = "PATCH_CANDIDATE_UNSUPPORTED_CLAUSE"
        else:
            initial = "MANUAL_REVIEW_SOURCE_SUPPORT_PRESENT"

        out.append({
            "review_id": row["review_id"],
            "bucket": row["bucket"],
            "core": row["core"],
            "status": row["status"],
            "question": row["question"],
            "suite": suite,
            "source_chars": str(len(source_text)),
            "sentence": row.get("sentence", ""),
            "missing_clause": row.get("missing_clause", ""),
            "sentence_best_source_match": sentence_best,
            "hit_best_source_match": hit_best,
            "missing_clause_source_matches": " | ".join(clause_results),
            "initial_decision": initial,
        })

    fieldnames = list(out[0].keys())
    with (RUN_DIR / "REVIEW237_SOURCE_CHECK.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out)

    counts: dict[str, int] = {}
    for r in out:
        counts[r["initial_decision"]] = counts.get(r["initial_decision"], 0) + 1
    lines = ["# REVIEW237_SOURCE_CHECK_SUMMARY", ""]
    lines += [f"- total_rows: {len(out)}"]
    for k, v in sorted(counts.items()):
        lines.append(f"- {k}: {v}")
    (RUN_DIR / "REVIEW237_SOURCE_CHECK_SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

