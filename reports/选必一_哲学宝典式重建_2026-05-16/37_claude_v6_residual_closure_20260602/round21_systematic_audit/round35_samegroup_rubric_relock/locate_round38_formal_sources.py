#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
UNIQUE_CSV = RUN_DIR / "round38_unique_questions.csv"
OUT_JSON = RUN_DIR / "round38_formal_source_locator.json"
OUT_MD = RUN_DIR / "round38_formal_source_locator.md"

ROOTS = [
    Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/texts"),
    Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/12_full_desktop_extract_20260524"),
    Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531/02_source_cards/raw_cards"),
]

KEY_RE = re.compile(r"(20\d{2})(.+?)Q(\d+)(?:\((\d+)\))?$")
FORMAL_FILE_TERMS = ("细则", "评分", "评标", "阅卷", "答案")
FORMAL_CONTENT_TERMS = ("评分细则", "评分标准", "评标", "阅卷细则", "阅卷", "答案变通", "采分", "赋分", "给分", "满分")
REFERENCE_ONLY_TERMS = ("参考答案", "答案及评分参考", "阅卷前参考答案")
DISTRICTS = ("朝阳", "海淀", "西城", "东城", "丰台", "顺义", "通州", "石景山", "房山", "门头沟", "延庆", "昌平")
PHASES = ("思政二模", "一模", "二模", "期中", "期末", "高考", "模拟")


def parse_key(key: str) -> dict:
    m = KEY_RE.match(key)
    if not m:
        raise ValueError(key)
    year, exam, q, sub = m.groups()
    district = next((d for d in DISTRICTS if d in exam), "")
    phase = next((p for p in PHASES if p in exam), "")
    return {"year": year, "exam": exam, "district": district, "phase": phase, "q": q, "sub": sub or ""}


def files() -> list[Path]:
    out: list[Path] = []
    for root in ROOTS:
        if not root.exists():
            continue
        out.extend([p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".txt", ".md"}])
    return out


ALL_FILES = files()


def score_filename(path: Path, year: str, exam: str) -> int:
    name = path.name
    score = 0
    if year in name:
        score += 5
    # Split short district and exam tags so files like 2025朝阳二模细则 match.
    for token in re.findall(r"[\u4e00-\u9fff]+|一模|二模|期中|期末", exam):
        if token and token in name:
            score += 3
    if any(t in name for t in ("细则", "评标", "阅卷")):
        score += 8
    elif "答案" in name:
        score += 2
    if "试卷" in name or "试题" in name:
        score -= 2
    return score


def affinity_ok(path: Path, text: str, parts: dict) -> bool:
    hay = f"{path.name}\n{path.parent.name}\n{text[:4000]}"
    if parts["year"] not in hay:
        return False
    if parts["district"] and parts["district"] not in hay:
        return False
    if parts["phase"] and parts["phase"] not in hay:
        return False
    return True


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def find_question_snippets(text: str, q: str) -> list[str]:
    patterns = [
        rf"(?m)^.*(?:第\s*{q}\s*题|{q}[\.、．)]|{q}（|{q}\().*$",
        rf"(?m)^.*Q\s*{q}(?:\D|$).*$",
    ]
    lines = text.splitlines()
    hit_idxs: list[int] = []
    for idx, line in enumerate(lines):
        compact = line.replace(" ", "")
        if re.search(patterns[0], compact) or re.search(patterns[1], compact):
            hit_idxs.append(idx)
    snippets = []
    for idx in hit_idxs[:5]:
        start = max(0, idx - 4)
        end = min(len(lines), idx + 14)
        snippets.append("\n".join(lines[start:end]))
    return snippets


def content_score(text: str, q: str) -> tuple[int, list[str], str]:
    score = 0
    for term in FORMAL_CONTENT_TERMS:
        if term in text:
            score += 3
    snippets = find_question_snippets(text, q)
    if snippets:
        score += 8
    joined = "\n".join(snippets)
    if any(term in joined for term in FORMAL_CONTENT_TERMS):
        score += 10
    if any(term in joined for term in REFERENCE_ONLY_TERMS) and not any(term in joined for term in ("评分细则", "答案变通", "给分", "赋分", "采分")):
        evidence_type = "reference_only_candidate"
    elif any(term in joined or term in text[:1000] for term in ("评分细则", "评标", "阅卷细则", "答案变通", "给分", "赋分", "采分")):
        evidence_type = "formal_candidate"
    elif snippets:
        evidence_type = "question_candidate"
    else:
        evidence_type = "file_candidate"
    return score, snippets, evidence_type


def locate(row: dict) -> dict:
    key = row["key"]
    parts = parse_key(key)
    candidates = []
    for path in ALL_FILES:
        text = read_text(path)
        if not affinity_ok(path, text, parts):
            continue
        fn_score = score_filename(path, parts["year"], parts["exam"])
        if parts["district"] and parts["district"] in path.name:
            fn_score += 8
        if parts["phase"] and parts["phase"] in path.name:
            fn_score += 5
        if fn_score <= 0:
            fn_score = 1
        c_score, snippets, evidence_type = content_score(text, parts["q"])
        total = fn_score + c_score
        if total < 8:
            continue
        candidates.append(
            {
                "path": str(path),
                "score": total,
                "filename_score": fn_score,
                "content_score": c_score,
                "evidence_type": evidence_type,
                "snippets": snippets[:2],
            }
        )
    candidates.sort(key=lambda x: (-x["score"], x["path"]))
    return {"key": key, "count": row["count"], "candidates": candidates[:8]}


def main() -> None:
    rows = list(csv.DictReader(UNIQUE_CSV.open(encoding="utf-8")))
    located = [locate(row) for row in rows]
    OUT_JSON.write_text(json.dumps(located, ensure_ascii=False, indent=2), encoding="utf-8")
    with OUT_MD.open("w", encoding="utf-8") as f:
        f.write("# Round38 Formal Source Locator\n\n")
        for item in located:
            f.write(f"## {item['key']} ({item['count']} blocks)\n\n")
            if not item["candidates"]:
                f.write("- NO CANDIDATE FOUND\n\n")
                continue
            for cand in item["candidates"][:3]:
                f.write(f"- {cand['evidence_type']} score={cand['score']} `{cand['path']}`\n")
                for snip in cand["snippets"][:1]:
                    safe = snip.strip().replace("```", "'''")
                    f.write(f"\n```text\n{safe[:1600]}\n```\n")
            f.write("\n")
    print(
        json.dumps(
            {
                "questions": len(located),
                "with_candidates": sum(1 for x in located if x["candidates"]),
                "without_candidates": [x["key"] for x in located if not x["candidates"]],
                "outputs": [str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
