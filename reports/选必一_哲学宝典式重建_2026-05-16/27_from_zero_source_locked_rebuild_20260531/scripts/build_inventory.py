#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531")
SEED_AUDIT = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/25_claude_philosophy_aligned_source_audit_20260531/02_audit/AUTOMATED_AUDIT.csv")
OUT_INPUTS = RUN / "01_inputs"

ROOTS = [
    Path("/Users/wanglifei/Desktop/2024模拟题"),
    Path("/Users/wanglifei/Desktop/2025模拟题"),
    Path("/Users/wanglifei/Desktop/2026模拟题"),
    Path("/Users/wanglifei/Desktop/北京高考政治"),
]

EXTS = {".pdf", ".docx", ".doc", ".pptx", ".ppt"}
DISTRICTS = ["东城", "西城", "朝阳", "海淀", "丰台", "石景山", "门头沟", "房山", "通州", "顺义", "昌平", "延庆"]
EXAMS = ["一模", "二模", "期末", "期中"]


def classify_role(path: Path) -> str:
    s = str(path)
    name = path.name
    if any(x in s for x in ["阅卷", "评标", "评分细则", "细则"]):
        return "rubric"
    if "答案" in s or "参考答案" in s:
        return "answer"
    if "试卷" in s or "试题" in s:
        return "paper"
    if "讲评" in s:
        return "review"
    if name.startswith("~$"):
        return "temp"
    return "other"


def infer_year(path: Path) -> str:
    s = str(path)
    m = re.search(r"20(24|25|26)", s)
    return f"20{m.group(1)}" if m else ""


def infer_district(path: Path) -> str:
    s = str(path)
    for d in DISTRICTS:
        if d in s:
            return d
    return ""


def infer_exam(path: Path) -> str:
    s = str(path)
    for d in DISTRICTS:
        m = re.search(fr"{d}(一模|二模|期末|期中)", s)
        if m:
            return m.group(1)
    for e in EXAMS:
        if e in s:
            return e
    return ""


def list_files():
    rows = []
    seen = set()
    for root in ROOTS:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if not p.is_file() or p.suffix.lower() not in EXTS:
                continue
            if p.name.startswith("~$"):
                continue
            real = str(p)
            if real in seen:
                continue
            seen.add(real)
            rows.append({
                "path": real,
                "root": str(root),
                "year": infer_year(p),
                "district": infer_district(p),
                "exam_type": infer_exam(p),
                "role": classify_role(p),
                "suffix": p.suffix.lower(),
                "size": p.stat().st_size,
            })
    return rows


def read_seed_questions():
    rows = list(csv.DictReader(SEED_AUDIT.open(encoding="utf-8-sig")))
    grouped = {}
    for row in rows:
        key = (row["year"], row["district"], row["exam_type"], row["q_no"], row["q_sub"])
        item = grouped.setdefault(key, {
            "year": row["year"],
            "district": row["district"],
            "exam_type": row["exam_type"],
            "q_no": row["q_no"],
            "q_sub": row["q_sub"],
            "entry_count": 0,
            "source_labels": [],
            "seed_paper_paths": set(),
            "seed_rubric_paths": set(),
            "seed_other_paths": set(),
        })
        item["entry_count"] += 1
        item["source_labels"].append(row["source_label"])
        for field, target in [
            ("paper_paths", "seed_paper_paths"),
            ("rubric_paths", "seed_rubric_paths"),
            ("other_paths", "seed_other_paths"),
        ]:
            for part in (row.get(field, "") or "").split(" || "):
                part = part.strip()
                if part:
                    item[target].add(part)
    out = []
    for key, item in grouped.items():
        item["source_labels"] = " || ".join(sorted(set(item["source_labels"])))
        item["seed_paper_paths"] = " || ".join(sorted(item["seed_paper_paths"]))
        item["seed_rubric_paths"] = " || ".join(sorted(item["seed_rubric_paths"]))
        item["seed_other_paths"] = " || ".join(sorted(item["seed_other_paths"]))
        out.append(item)
    out.sort(key=lambda r: (r["year"], r["district"], r["exam_type"], int(r["q_no"] or 0), r["q_sub"]))
    return out


def match_sources(candidates, files):
    by_suite = defaultdict(list)
    for f in files:
        by_suite[(f["year"], f["district"], f["exam_type"])].append(f)
    out = []
    for c in candidates:
        suite_files = by_suite.get((c["year"], c["district"], c["exam_type"]), [])
        roles = defaultdict(list)
        for f in suite_files:
            roles[f["role"]].append(f["path"])
        paper = sorted(roles["paper"])
        rubric = sorted(roles["rubric"])
        answer = sorted(roles["answer"])
        review = sorted(roles["review"])
        if (c["year"], c["district"], c["exam_type"]) == ("2026", "西城", "期末") and not paper:
            hidden_papers = [p for p in rubric + answer if "高三思想政治参考答案.pdf" in p]
            paper.extend(hidden_papers)
        status = "READY_FOR_CARD" if paper and rubric else "SOURCE_GAP"
        if not paper:
            status += "_NO_PAPER"
        if not rubric:
            status += "_NO_RUBRIC"
        out.append({
            **c,
            "match_status": status,
            "matched_papers": " || ".join(paper),
            "matched_rubrics": " || ".join(rubric),
            "matched_answers": " || ".join(answer),
            "matched_reviews": " || ".join(review),
        })
    return out


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    files = list_files()
    candidates = read_seed_questions()
    matches = match_sources(candidates, files)
    write_csv(OUT_INPUTS / "SOURCE_FILE_INVENTORY.csv", files)
    write_csv(OUT_INPUTS / "CANDIDATE_QUESTIONS_FROM_SEED.csv", candidates)
    write_csv(OUT_INPUTS / "QUESTION_SOURCE_MATCH.csv", matches)
    print("files", len(files), Counter(f["role"] for f in files))
    print("candidate_questions", len(candidates), Counter(m["match_status"] for m in matches))


if __name__ == "__main__":
    main()
