#!/usr/bin/env python3
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "05_coverage" / "phase04_batch03_A_subjective_queue.csv"
REGISTRY = ROOT / "01_source_inventory" / "phase03_raw_source_registry.csv"
OUT_CSV = ROOT / "codex_lane" / "phase04_batch03_A_subjective_codexA_precheck.csv"
OUT_MD = ROOT / "codex_lane" / "phase04_batch03_A_subjective_scope_precheck.md"

LOGIC_TERMS = [
    "逻辑与思维",
    "辩证思维",
    "创新思维",
    "科学思维",
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
    "中国特色社会主义",
    "文化传承与文化创新",
]
RUBRIC_HINTS = ["分", "答案", "评分", "细则", "给分", "评标", "参考", "等级"]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def clean(text: str, limit: int = 360) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit]


def read_text(path: str) -> str:
    if not path:
        return ""
    p = Path(path)
    if not p.exists() or not p.is_file():
        return ""
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def qno_patterns(qno: str) -> list[str]:
    qno = qno.strip()
    base = re.sub(r"\(.*?\)|（.*?）", "", qno)
    sub = ""
    m = re.search(r"[\(（](.*?)[\)）]", qno)
    if m:
        sub = m.group(1)
    patterns = [qno, qno.replace("(", "（").replace(")", "）")]
    if base:
        patterns.extend([f"{base}.", f"{base}．", f"{base}、", f"{base} "])
    if base and sub:
        patterns.extend([f"{base}({sub})", f"{base}（{sub}）", f"({sub})", f"（{sub}）"])
    return list(dict.fromkeys([p for p in patterns if p]))


def best_snippet(text: str, qno: str) -> str:
    if not text:
        return ""
    candidates = []
    for pat in qno_patterns(qno):
        idx = text.find(pat)
        if idx >= 0:
            start = max(0, idx - 160)
            end = min(len(text), idx + 520)
            candidates.append(text[start:end])
    if candidates:
        return clean(candidates[0], 520)
    hits = []
    for term in LOGIC_TERMS:
        idx = text.find(term)
        if idx >= 0:
            hits.append(text[max(0, idx - 120) : min(len(text), idx + 360)])
    return clean(hits[0], 520) if hits else ""


def term_hits(text: str, terms: list[str]) -> list[str]:
    return [t for t in terms if t in text]


def decide(row: dict[str, str], paper: str, rubric: str, support: str) -> tuple[str, str, str]:
    combined_prompt = " ".join([row.get("excerpt", ""), paper])
    logic_hits = term_hits(combined_prompt + " " + rubric + " " + support, LOGIC_TERMS)
    other_hits = term_hits(combined_prompt, OTHER_BOOK_TERMS)
    rubric_hits = term_hits(rubric, RUBRIC_HINTS)
    support_hits = term_hits(support, RUBRIC_HINTS)

    if other_hits and not logic_hits:
        return "CODEX_A_PRECHECK_SCOPE_OUT_LIKELY", "C-boundary", "other_book_prompt_without_logic_signal"
    if other_hits and logic_hits:
        return "CODEX_A_PRECHECK_BOUNDARY_MIXED", "C-boundary_or_cross_check", "other_book_prompt_with_logic_terms_needs_source_decision"
    if rubric and rubric_hits:
        return "CODEX_A_PRECHECK_RUBRIC_PAIR_CANDIDATE", "A-formal_candidate", "rubric_text_candidate_found"
    if support and support_hits:
        return "CODEX_A_PRECHECK_SUPPORT_PAIR_CANDIDATE", "A-support_candidate", "support_text_candidate_found"
    return "CODEX_A_PRECHECK_NEEDS_SOURCE_OR_VISUAL", "missing_or_inventory_only", "no_rubric_or_support_snippet_found"


def main() -> None:
    queue = read_csv(QUEUE)
    registry = read_csv(REGISTRY)
    by_suite: dict[str, list[dict[str, str]]] = {}
    by_source: dict[str, dict[str, str]] = {}
    for r in registry:
        by_suite.setdefault(r["suite_id"], []).append(r)
        by_source[r["source_id"]] = r

    out_rows = []
    for row in queue:
        suite_sources = by_suite.get(row["suite_id"], [])
        paper_source = by_source.get(row["source_id"], {})
        paper_text = read_text(paper_source.get("text_path", ""))
        paper_snippet = best_snippet(paper_text, row["original_qno"]) or clean(row.get("excerpt", ""), 520)

        rubric_snippets = []
        support_snippets = []
        rubric_sources = []
        support_sources = []
        for src in suite_sources:
            role = src.get("source_role", "")
            text = read_text(src.get("text_path", ""))
            if not text:
                continue
            snip = best_snippet(text, row["original_qno"])
            if not snip:
                continue
            if role == "rubric_or_answer":
                rubric_snippets.append(snip)
                rubric_sources.append(src["source_id"])
            elif role == "support_or_lecture":
                support_snippets.append(snip)
                support_sources.append(src["source_id"])

        rubric_snippet = rubric_snippets[0] if rubric_snippets else ""
        support_snippet = support_snippets[0] if support_snippets else ""
        decision, evidence, reason = decide(row, paper_snippet, rubric_snippet, support_snippet)
        out_rows.append(
            {
                "target_id": row["canonical_question_id"],
                "suite_id": row["suite_id"],
                "qno": row["original_qno"],
                "section_scope_from_A": row["section_scope"],
                "question_type": row["question_type"],
                "codexA_precheck_result": decision,
                "evidence_level_precheck": evidence,
                "precheck_reason": reason,
                "paper_source_id": row["source_id"],
                "rubric_source_ids": ";".join(rubric_sources),
                "support_source_ids": ";".join(support_sources),
                "paper_snippet": paper_snippet,
                "rubric_snippet": rubric_snippet,
                "support_snippet": support_snippet,
                "student_permission": "NO_STUDENT_DRAFT",
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = list(out_rows[0].keys())
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_rows)

    counts = Counter(r["codexA_precheck_result"] for r in out_rows)
    evidence_counts = Counter(r["evidence_level_precheck"] for r in out_rows)
    scope_counts = Counter(r["section_scope_from_A"] for r in out_rows)
    boundary_rows = [
        r for r in out_rows if "SCOPE_OUT" in r["codexA_precheck_result"] or "BOUNDARY" in r["codexA_precheck_result"]
    ]
    needs_rows = [r for r in out_rows if r["codexA_precheck_result"] == "CODEX_A_PRECHECK_NEEDS_SOURCE_OR_VISUAL"]

    lines = [
        "# Codex A Phase04 Batch03 Subjective Precheck",
        "",
        "- queue: `05_coverage/phase04_batch03_A_subjective_queue.csv`",
        "- output_csv: `codex_lane/phase04_batch03_A_subjective_codexA_precheck.csv`",
        "- status: internal precheck only; not a fusion decision; not student稿",
        "",
        "## Counts",
        "",
        f"- processed: {len(out_rows)}",
        f"- by precheck_result: {dict(counts)}",
        f"- by evidence_precheck: {dict(evidence_counts)}",
        f"- by section_scope_from_A: {dict(scope_counts)}",
        "",
        "## Boundary Or Mixed Rows For B-Line Challenge",
        "",
    ]
    for r in boundary_rows[:40]:
        lines.append(
            f"- `{r['target_id']}` | {r['suite_id']} | Q{r['qno']} | {r['codexA_precheck_result']} | {r['precheck_reason']} | paper: {clean(r['paper_snippet'], 180)}"
        )
    lines.extend(["", "## Rows Needing More Source Or Visual Recovery", ""])
    for r in needs_rows[:40]:
        lines.append(
            f"- `{r['target_id']}` | {r['suite_id']} | Q{r['qno']} | {r['precheck_reason']} | paper: {clean(r['paper_snippet'], 180)}"
        )
    lines.extend(
        [
            "",
            "## Gate",
            "",
            "- This precheck cannot promote rows by itself.",
            "- ClaudeCode Batch03 A result and later Codex fusion are still required.",
            "- Student稿 remains blocked.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
