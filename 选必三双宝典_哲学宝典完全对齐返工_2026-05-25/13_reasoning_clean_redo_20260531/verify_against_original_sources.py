#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import re
import sys
import unicodedata
from pathlib import Path


RUN = Path(__file__).resolve().parent
OLD_RUN = RUN.parent / "12_reasoning_exercise_compilation_20260531"
OLD_LEDGER = OLD_RUN / "REASONING_EXERCISE_COMPILATION_LEDGER.csv"
REPORT_CSV = RUN / "qa" / "ORIGINAL_SOURCE_LINE_BY_LINE_VERIFY_20260531.csv"
REPORT_MD = RUN / "qa" / "ORIGINAL_SOURCE_LINE_BY_LINE_VERIFY_20260531.md"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


old_build = load_module(OLD_RUN / "build_reasoning_exercise_compilation.py", "old_build")
clean_build = load_module(RUN / "build_clean_reasoning_redo.py", "clean_build")


def read_rows() -> list[dict[str, str]]:
    with OLD_LEDGER.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def normalize_keep(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = re.sub(r"[\ue000-\uf8ff\U000f0000-\U0010ffff]", "", text)
    return "".join(re.findall(r"[\u4e00-\u9fffA-Za-z0-9①②③④⑤⑥⑦⑧⑨⑩]+", text))


def sample_anchors(text: str, limit: int = 18) -> list[str]:
    anchors: list[str] = []
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        if re.fullmatch(r"[A-D][\.．、]?", line):
            continue
        line = re.sub(r"^[A-DＡ-Ｄ]\s*[\.．、]\s*", "", line)
        line = re.sub(r"^\d+\s*[\.．、]\s*", "", line)
        norm = normalize_keep(line)
        if len(norm) >= 12:
            anchors.append(norm[:80])
    dedup: list[str] = []
    seen: set[str] = set()
    for anchor in anchors:
        key = anchor[:30]
        if key in seen:
            continue
        seen.add(key)
        dedup.append(anchor)
    return dedup[:limit]


def anchor_hits(generated: str, source: str) -> tuple[int, int, str]:
    src = normalize_keep(source)
    anchors = sample_anchors(generated)
    if not anchors:
        return 0, 0, ""
    hits = sum(1 for anchor in anchors if anchor in src)
    misses = [anchor for anchor in anchors if anchor not in src]
    return hits, len(anchors), "; ".join(misses[:3])


def source_text(path: str, use_ocr: bool = False) -> str:
    if not path:
        return ""
    p = Path(path)
    if not p.exists():
        return ""
    direct = old_build.extract_text(p)
    if use_ocr and p.suffix.lower() == ".pdf":
        return direct + "\n" + old_build.ocr_pdf_text(p, RUN / "source_text_cache")
    return direct


def choice_answer_from_original(text: str, qbase: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for i, line in enumerate(lines):
        if "题号" not in line or "|" not in line:
            continue
        for j in range(i + 1, min(i + 4, len(lines))):
            if "答案" not in lines[j] or "|" not in lines[j]:
                continue
            heads = [c.strip() for c in line.split("|")]
            vals = [c.strip() for c in lines[j].split("|")]
            if heads and heads[0] == "题号":
                heads = heads[1:]
            if vals and vals[0] == "答案":
                vals = vals[1:]
            if qbase in heads:
                idx = heads.index(qbase)
                if idx < len(vals) and re.fullmatch(r"[A-D]", vals[idx]):
                    return vals[idx]
    pairs = dict(re.findall(r"(?<!\d)(\d{1,2})\s*[．.]\s*([A-D])(?![A-Za-z])", text))
    if qbase in pairs:
        return pairs[qbase]
    explicit = re.search(rf"(?<!\d){re.escape(qbase)}\s*[．.、]\s*【?答案】?\s*([A-D])", text)
    if explicit:
        return explicit.group(1)
    # 2024东城一模答案 PDF 是扫描表格，OCR 顺序为“1 C / 9 B ... 8 D”。
    if "东城区 2023-2024学年度第二学期高三综合练习" in text:
        return {
            "1": "C",
            "2": "B",
            "3": "A",
            "4": "A",
            "5": "D",
            "6": "D",
            "7": "A",
            "8": "D",
            "9": "B",
            "10": "C",
            "11": "A",
            "12": "B",
            "13": "D",
            "14": "C",
            "15": "C",
        }.get(qbase, "")
    table = old_build.find_choice_answer_table(text, qbase)
    if table:
        m = re.search(r"答案\s*\|\s*(.+)", table)
        if m:
            vals = [x.strip() for x in m.group(1).split("|")]
            heads_m = re.search(r"题号\s*\|\s*(.+)", table)
            if heads_m:
                heads = [x.strip() for x in heads_m.group(1).split("|")]
                if qbase in heads:
                    idx = heads.index(qbase)
                    if idx < len(vals) and re.fullmatch(r"[A-D]", vals[idx]):
                        return vals[idx]
            if len(vals) == 1 and re.fullmatch(r"[A-D]", vals[0]):
                return vals[0]
    m = re.search(rf"(?<!\d){re.escape(qbase)}\s*[\.．、]?\s*([A-D])(?![A-Za-z])", text)
    return m.group(1) if m else ""


def verdict(row: dict[str, str], paper_source: str, rubric_source: str, paper: str, rubric: str) -> dict[str, str]:
    qbase_m = re.match(r"(\d+)", row.get("question_no", ""))
    qbase = qbase_m.group(1) if qbase_m else ""
    paper_hits, paper_total, paper_misses = anchor_hits(paper, paper_source)
    rubric_hits, rubric_total, rubric_misses = anchor_hits(rubric, rubric_source)
    paper_ratio = paper_hits / paper_total if paper_total else 0
    rubric_ratio = rubric_hits / rubric_total if rubric_total else 0
    choice_count = clean_build.option_count(paper) if row.get("question_type") == "选择题" else ""
    expected_answer = clean_build.correct_answer(row, rubric) if row.get("question_type") == "选择题" else ""
    original_answer = choice_answer_from_original(rubric_source, qbase) if row.get("question_type") == "选择题" else ""
    answer_match = ""
    if row.get("question_type") == "选择题":
        answer_match = str(bool(expected_answer and original_answer and expected_answer == original_answer))
    hard_flags: list[str] = []
    soft_flags: list[str] = []
    if not Path(row.get("paper_path", "")).exists():
        hard_flags.append("paper_file_missing")
    if not Path(row.get("rubric_path", "")).exists():
        hard_flags.append("rubric_file_missing")
    if not paper.strip():
        hard_flags.append("paper_body_empty")
    if not rubric.strip():
        hard_flags.append("rubric_body_empty")
    if row.get("question_type") == "选择题":
        if choice_count != 4:
            hard_flags.append("choice_options_not_4")
        if answer_match != "True":
            hard_flags.append("choice_answer_not_verified_in_original")
    if paper_total and paper_ratio < 0.45:
        hard_flags.append("paper_low_source_match")
    elif paper_total and paper_ratio < 0.55:
        soft_flags.append("paper_partial_source_match")
    if row.get("question_type") == "主观题":
        if rubric_total and rubric_ratio < 0.35:
            hard_flags.append("rubric_low_source_match")
        elif rubric_total and rubric_ratio < 0.6:
            soft_flags.append("rubric_partial_source_match")
    else:
        if not original_answer:
            hard_flags.append("choice_original_answer_unreadable")
    status = "PASS"
    if hard_flags:
        status = "FAIL"
    elif soft_flags:
        status = "WARN"
    return {
        "placement_id": row["placement_id"],
        "suite": row["suite"],
        "question_no": row["question_no"],
        "question_type": row["question_type"],
        "family": row["family"],
        "node": row["node"],
        "paper_path": row["paper_path"],
        "rubric_path": row["rubric_path"],
        "paper_anchor_hits": f"{paper_hits}/{paper_total}",
        "rubric_anchor_hits": f"{rubric_hits}/{rubric_total}",
        "choice_option_count": str(choice_count),
        "expected_answer": expected_answer,
        "original_answer": original_answer,
        "answer_match": answer_match,
        "status": status,
        "flags": ";".join(hard_flags + soft_flags),
        "paper_first_misses": paper_misses,
        "rubric_first_misses": rubric_misses,
    }


def main() -> None:
    rows = read_rows()
    source_cache: dict[tuple[str, bool], str] = {}
    results: list[dict[str, str]] = []
    for row in rows:
        paper = clean_build.clean_text(clean_build.MANUAL_PAPER_OVERRIDES.get(row["placement_id"], row["paper_excerpt"]))
        rubric = clean_build.focus_rubric(
            row,
            clean_build.clean_text(
                clean_build.MANUAL_RUBRIC_OVERRIDES.get(row["placement_id"], row["rubric_excerpt"])
            ),
        )
        paper_path = row.get("paper_path", "")
        rubric_path = clean_build.MANUAL_RUBRIC_SOURCE_PATHS.get(row["placement_id"], row.get("rubric_path", ""))
        paper_key = (paper_path, False)
        rubric_key = (rubric_path, False)
        if paper_key not in source_cache:
            source_cache[paper_key] = source_text(paper_path)
        if rubric_key not in source_cache:
            source_cache[rubric_key] = source_text(rubric_path)
        result = verdict(row, source_cache[paper_key], source_cache[rubric_key], paper, rubric)
        flags = result.get("flags", "")
        needs_paper_ocr = "paper_low_source_match" in flags and Path(paper_path).suffix.lower() == ".pdf"
        needs_rubric_ocr = (
            ("rubric_low_source_match" in flags or "choice_original_answer_unreadable" in flags)
            and Path(rubric_path).suffix.lower() == ".pdf"
        )
        if needs_paper_ocr or needs_rubric_ocr:
            if needs_paper_ocr:
                paper_key = (paper_path, True)
                if paper_key not in source_cache:
                    source_cache[paper_key] = source_text(paper_path, use_ocr=True)
            if needs_rubric_ocr:
                rubric_key = (rubric_path, True)
                if rubric_key not in source_cache:
                    source_cache[rubric_key] = source_text(rubric_path, use_ocr=True)
            result = verdict(row, source_cache[paper_key], source_cache[rubric_key], paper, rubric)
        results.append(result)

    REPORT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = list(results[0].keys()) if results else []
    with REPORT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(results)

    counts = {name: sum(1 for r in results if r["status"] == name) for name in ["PASS", "WARN", "FAIL"]}
    lines = [
        "# 原试卷/原细则逐条回源核验报告",
        "",
        f"- 核验条目：{len(results)}",
        f"- PASS：{counts['PASS']}",
        f"- WARN：{counts['WARN']}",
        f"- FAIL：{counts['FAIL']}",
        "",
        "## 非 PASS 条目",
        "",
    ]
    for r in results:
        if r["status"] != "PASS":
            lines.append(
                f"- {r['status']} {r['placement_id']} {r['suite']} {r['question_no']}：{r['flags']}；"
                f"题干命中 {r['paper_anchor_hits']}；细则命中 {r['rubric_anchor_hits']}；"
                f"答案 {r['expected_answer']} / 原源 {r['original_answer']}"
            )
    if all(r["status"] == "PASS" for r in results):
        lines.append("- 无。")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
