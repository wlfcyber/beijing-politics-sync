from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
MD = RUN / "09_delivery" / "选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md"
MATRIX = RUN / "08_review" / "role_reviews" / "all_question_rubric_point_repair_matrix_20260504.csv"
OUT_MD = RUN / "08_review" / "role_reviews" / "redword_reverse_source_trace_audit_20260504.md"
OUT_CSV = RUN / "08_review" / "role_reviews" / "redword_reverse_source_trace_suspects_20260504.csv"

RED_RE = re.compile(r'<span style="color:#c00000">(.*?)</span>')
QUESTION_RE = re.compile(r"^###\s+\d+\.\s+(.+?)\s*$")
BAD_CONTEXT_HINTS = (
    "框架落点：",
    "**本题命中框架**",
    "- 时代背景：",
    "- 理论：",
    "- 经济全球化：",
    "- 政治多极化：",
    "- 中国：",
    "- 联合国：",
    "框架归类：",
)


def norm(text: str) -> str:
    return re.sub(r"\s+", "", text.replace("、", "").replace("，", "").replace("；", "")).strip()


def split_terms(value: str) -> list[str]:
    out: list[str] = []
    for raw in re.split(r"[;；]", value or ""):
        item = raw.strip(" ；;，,。")
        if item:
            out.append(item)
    return out


def term_is_sourced(span: str, allowed_terms: list[str]) -> bool:
    s = norm(span)
    if not s:
        return True
    for term in allowed_terms:
        t = norm(term)
        if not t:
            continue
        if s in t or t in s:
            return True
    return False


def load_allowed_terms() -> dict[str, list[str]]:
    allowed: dict[str, list[str]] = defaultdict(list)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            q = row["question"]
            for term in split_terms(row.get("red_scoring_terms", "")):
                if term not in allowed[q]:
                    allowed[q].append(term)
    return allowed


def main() -> None:
    text = MD.read_text(encoding="utf-8")
    allowed_by_q = load_allowed_terms()
    current_q = ""
    in_training_loop = False
    total_red = 0
    question_red = 0
    suspect_rows: list[dict[str, str]] = []
    bad_context_count = 0
    unsourced_count = 0
    framework_red_count = 0

    for lineno, line in enumerate(text.splitlines(), 1):
        if line.strip() == "## 按题训练闭环":
            in_training_loop = True
            current_q = ""
            continue
        if line.startswith("## ") and line.strip() != "## 按题训练闭环":
            if in_training_loop and not QUESTION_RE.match(line):
                current_q = ""
            if line.strip() == "## 六桶术语积累复盘":
                in_training_loop = False
        match = QUESTION_RE.match(line)
        if match:
            current_q = match.group(1)

        spans = RED_RE.findall(line)
        if not spans:
            continue
        total_red += len(spans)

        if not current_q:
            framework_red_count += len(spans)
            continue

        question_red += len(spans)
        allowed_terms = allowed_by_q.get(current_q, [])
        bad_context = any(hint in line for hint in BAD_CONTEXT_HINTS)
        for span in spans:
            sourced = term_is_sourced(span, allowed_terms)
            if bad_context or not sourced:
                if bad_context:
                    bad_context_count += 1
                if not sourced:
                    unsourced_count += 1
                suspect_rows.append(
                    {
                        "line": str(lineno),
                        "question": current_q,
                        "red_span": span,
                        "reason": ("bad_context;" if bad_context else "") + ("not_in_question_source_terms" if not sourced else ""),
                        "line_text": line,
                    }
                )

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames = ["line", "question", "red_span", "reason", "line_text"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(suspect_rows)

    verdict = "PASS" if not suspect_rows else "NEEDS_FIX"
    lines = [
        "# Redword Reverse Source Trace Audit",
        "",
        "time: 2026-05-04 21:33 CST",
        f"verdict: `{verdict}`",
        "",
        "## Scope",
        "",
        "- Checks every red span inside `按题训练闭环` against that question's `red_scoring_terms` in `all_question_rubric_point_repair_matrix_20260504.csv`.",
        "- Separately rejects red spans in framework-only contexts such as `本题命中框架`, `框架落点`, and numbered `框架归类` headings.",
        "- Red spans in the front six-bucket index and six-bucket review are counted as framework-level red terms, not question-specific redwords.",
        "",
        "## Counts",
        "",
        f"- total red spans in Markdown: {total_red}",
        f"- question-loop red spans audited: {question_red}",
        f"- framework-level red spans outside question-loop: {framework_red_count}",
        f"- bad-context red spans: {bad_context_count}",
        f"- unsourced question red spans: {unsourced_count}",
        f"- suspect rows: {len(suspect_rows)}",
        "",
        "## Decision",
        "",
    ]
    if suspect_rows:
        lines.append("FAIL: see `redword_reverse_source_trace_suspects_20260504.csv`.")
    else:
        lines.append("PASS: no red span in the question loop appears in a framework-only context, and every audited question-loop red span traces back to that question's recorded scoring terms.")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(OUT_MD)
    print(OUT_CSV)
    print(verdict)


if __name__ == "__main__":
    main()
