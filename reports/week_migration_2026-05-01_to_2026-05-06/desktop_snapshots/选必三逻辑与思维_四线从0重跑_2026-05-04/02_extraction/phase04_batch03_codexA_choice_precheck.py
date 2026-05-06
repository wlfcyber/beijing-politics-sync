#!/usr/bin/env python3
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "05_coverage" / "phase04_batch03_B_choice_queue.csv"
REGISTRY = ROOT / "01_source_inventory" / "phase03_raw_source_registry.csv"
OUT_CSV = ROOT / "codex_lane" / "phase04_batch03_B_choice_codexA_precheck.csv"
OUT_MD = ROOT / "codex_lane" / "phase04_batch03_B_choice_scope_answer_precheck.md"

LOGIC_TERMS = [
    "逻辑与思维",
    "科学思维",
    "辩证思维",
    "创新思维",
    "超前思维",
    "分析与综合",
    "思维抽象",
    "思维具体",
    "推理",
    "假言",
    "三段论",
    "联言",
    "选言",
    "归纳",
    "类比",
    "演绎",
]
OTHER_BOOK_TERMS = [
    "经济与社会",
    "哲学与文化",
    "政治与法治",
    "当代国际政治与经济",
    "法律与生活",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def read_text(path: str) -> str:
    if not path:
        return ""
    p = Path(path)
    if not p.exists() or not p.is_file():
        return ""
    return p.read_text(encoding="utf-8", errors="ignore")


def clean(text: str, limit: int = 420) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit]


def qno_patterns(qno: str) -> list[str]:
    qno = qno.strip()
    return list(
        dict.fromkeys(
            [
                qno,
                f"{qno}.",
                f"{qno}．",
                f"{qno}、",
                f"{qno} ",
                f"{qno}􀆰",
            ]
        )
    )


def best_snippet(text: str, qno: str) -> str:
    if not text:
        return ""
    for pat in qno_patterns(qno):
        idx = text.find(pat)
        if idx >= 0:
            return clean(text[max(0, idx - 120) : min(len(text), idx + 700)], 700)
    return ""


def option_coverage(snippet: str) -> str:
    marks = []
    for mark in ["A", "B", "C", "D"]:
        if re.search(rf"({mark}[\.．、]|{mark}．|{mark}􀆰)", snippet):
            marks.append(mark)
    for mark in ["①", "②", "③", "④"]:
        if mark in snippet:
            marks.append(mark)
    return "".join(marks) if marks else "not_detected"


def detect_answer(texts: list[str], qno: str) -> str:
    joined = "\n".join(texts)
    escaped = re.escape(qno)
    patterns = [
        rf"{escaped}\s*[\.．、]?\s*([ABCD])",
        rf"{escaped}\s*[:：]\s*([ABCD])",
        rf"{escaped}\s*题\s*([ABCD])",
    ]
    for pat in patterns:
        m = re.search(pat, joined)
        if m:
            return m.group(1)
    return ""


def hits(text: str, terms: list[str]) -> list[str]:
    return [t for t in terms if t in text]


def main() -> None:
    queue = read_csv(QUEUE)
    registry = read_csv(REGISTRY)
    by_suite: dict[str, list[dict[str, str]]] = {}
    by_source: dict[str, dict[str, str]] = {}
    for r in registry:
        by_suite.setdefault(r["suite_id"], []).append(r)
        by_source[r["source_id"]] = r

    out = []
    for row in queue:
        suite_sources = by_suite.get(row["suite_id"], [])
        paper_src = by_source.get(row["source_id"], {})
        paper_text = read_text(paper_src.get("text_path", ""))
        paper_snippet = best_snippet(paper_text, row["original_qno"]) or clean(row.get("excerpt", ""), 700)

        answer_texts = []
        answer_sources = []
        source_snippets = []
        for src in suite_sources:
            role = src.get("source_role", "")
            if role not in {"paper", "rubric_or_answer", "support_or_lecture"}:
                continue
            text = read_text(src.get("text_path", ""))
            if not text:
                continue
            if role != "paper":
                answer_texts.append(text)
                answer_sources.append(src["source_id"])
                snip = best_snippet(text, row["original_qno"])
                if snip:
                    source_snippets.append(f"{src['source_id']}: {snip}")

        detected_answer = detect_answer(answer_texts + [paper_text], row["original_qno"])
        option_status = option_coverage(paper_snippet)
        logic_hits = hits(paper_snippet, LOGIC_TERMS)
        other_hits = hits(paper_snippet, OTHER_BOOK_TERMS)

        if other_hits and not logic_hits:
            result = "CODEX_A_CHOICE_SCOPE_OUT_LIKELY"
        elif not detected_answer:
            result = "CODEX_A_CHOICE_NEEDS_ANSWER_SOURCE"
        elif option_status == "not_detected" or not all(m in option_status for m in ["A", "B", "C", "D"]):
            result = "CODEX_A_CHOICE_NEEDS_FULL_OPTIONS_VISUAL"
        else:
            result = "CODEX_A_CHOICE_ANSWER_OPTIONS_CANDIDATE"

        out.append(
            {
                "target_id": row["canonical_question_id"],
                "suite_id": row["suite_id"],
                "qno": row["original_qno"],
                "section_scope_from_A": row["section_scope"],
                "codexA_choice_precheck_result": result,
                "detected_answer": detected_answer,
                "option_coverage": option_status,
                "logic_term_hits": ";".join(logic_hits),
                "other_book_hits": ";".join(other_hits),
                "paper_source_id": row["source_id"],
                "answer_source_ids_checked": ";".join(answer_sources),
                "paper_snippet": paper_snippet,
                "answer_source_snippet": clean(" || ".join(source_snippets), 700),
                "student_permission": "NO_STUDENT_DRAFT",
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = list(out[0].keys())
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out)

    counts = Counter(r["codexA_choice_precheck_result"] for r in out)
    scope_counts = Counter(r["section_scope_from_A"] for r in out)
    answer_counts = Counter(r["detected_answer"] or "missing" for r in out)
    option_counts = Counter(r["option_coverage"] for r in out)

    lines = [
        "# Codex A Phase04 Batch03 Choice Precheck",
        "",
        "- queue: `05_coverage/phase04_batch03_B_choice_queue.csv`",
        "- output_csv: `codex_lane/phase04_batch03_B_choice_codexA_precheck.csv`",
        "- status: internal precheck only; not a fusion decision; not student稿",
        "",
        "## Counts",
        "",
        f"- processed: {len(out)}",
        f"- by precheck_result: {dict(counts)}",
        f"- by section_scope_from_A: {dict(scope_counts)}",
        f"- by detected_answer: {dict(answer_counts)}",
        f"- by option_coverage: {dict(option_counts)}",
        "",
        "## Rows Needing B-Line Challenge",
        "",
    ]
    for r in out:
        if r["codexA_choice_precheck_result"] != "CODEX_A_CHOICE_ANSWER_OPTIONS_CANDIDATE":
            lines.append(
                f"- `{r['target_id']}` | {r['suite_id']} | Q{r['qno']} | {r['codexA_choice_precheck_result']} | answer={r['detected_answer'] or 'missing'} | options={r['option_coverage']} | paper: {clean(r['paper_snippet'], 180)}"
            )
    lines.extend(
        [
            "",
            "## Gate",
            "",
            "- This precheck cannot promote rows by itself.",
            "- Choice rows require full question/options plus reliable answer source and trap analysis before entering evidence fusion.",
            "- Student稿 remains blocked.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
