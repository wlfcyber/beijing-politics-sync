#!/usr/bin/env python3
"""Phase11D four-element gate for review-only Markdown drafts.

The gate is intentionally conservative. It catches the exact failure class that
made the bad Word unacceptable: fake prompts, production-instruction answer
landings, missing four-element structure, and blocked-source rows leaking into
student-facing text.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "09_student_draft/phase11D_student_body_REWRITE_REVIEW_ONLY.md"
OUT_DIR = ROOT / "08_review/phase11D_four_element_gate"

REQUIRED_HEADINGS = ["【材料触发点】", "【设问】", "【为什么能想到】", "【答案落点】"]

FORBIDDEN_PHRASES = [
    "本题要求结合材料说明其体现的思维方法",
    "本题要求依据材料判断正确选项",
    "本题要求识别或运用",
    "卷面要把",
    "先写",
    "要写",
    "本题需要",
    "设问要求",
    "采分点",
    "细则要求",
    "v7漏了",
    "关键词最稳",
    "因此做选择题时先圈材料动作，再看选项是否把方法、主体、关系或作用说准",
    "先翻译逻辑结构，再套本题型最小规则，最后判断能否必然推出",
    "参考答案",
    "答案写",
    "评标",
    "可从",
    "A-formal",
    "B-choice-signal",
    "PASS",
]


def split_entries(text: str) -> list[tuple[str, str]]:
    """Return (title, body) chunks beginning at markdown H2/H3 entries."""
    matches = list(re.finditer(r"(?m)^#{2,4}\s+(.+)$", text))
    if not matches:
        return [("WHOLE_DOCUMENT", text)]
    entries: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        title = match.group(1).strip()
        body = text[start:end].strip()
        if any(h in body for h in REQUIRED_HEADINGS):
            entries.append((title, body))
    return entries


def section_text(body: str, heading: str) -> str:
    start = body.find(heading)
    if start < 0:
        return ""
    start += len(heading)
    next_positions = [body.find(h, start) for h in REQUIRED_HEADINGS if body.find(h, start) >= 0]
    end = min(next_positions) if next_positions else len(body)
    return body[start:end].strip()


def assess(title: str, body: str) -> dict[str, str]:
    missing = [h for h in REQUIRED_HEADINGS if h not in body]
    forbidden_hits = [p for p in FORBIDDEN_PHRASES if p in body]
    prompt = section_text(body, "【设问】")
    answer = section_text(body, "【答案落点】")
    trigger = section_text(body, "【材料触发点】")

    fake_prompt = any(p in prompt for p in FORBIDDEN_PHRASES[:3])
    meta_answer = any(p in answer for p in FORBIDDEN_PHRASES[3:14])
    blocked_leak = "BLOCKED_NEEDS_SOURCE" in body and not title.startswith("BLOCKED")
    too_short_answer = len(answer) < 25 and "选 " not in answer and "选" not in answer
    no_quote_or_signal = len(trigger) < 12

    status = "PASS"
    reasons: list[str] = []
    if missing:
        status = "FAIL"
        reasons.append("missing_headings=" + ";".join(missing))
    if forbidden_hits:
        status = "FAIL"
        reasons.append("forbidden=" + ";".join(forbidden_hits[:6]))
    if fake_prompt:
        status = "FAIL"
        reasons.append("fake_prompt")
    if meta_answer:
        status = "FAIL"
        reasons.append("meta_answer_instruction")
    if blocked_leak:
        status = "FAIL"
        reasons.append("blocked_source_leak")
    if too_short_answer:
        status = "WARN" if status == "PASS" else status
        reasons.append("answer_too_short")
    if no_quote_or_signal:
        status = "WARN" if status == "PASS" else status
        reasons.append("trigger_too_thin")

    return {
        "title": title,
        "status": status,
        "reasons": " | ".join(reasons),
        "missing_count": str(len(missing)),
        "forbidden_count": str(len(forbidden_hits)),
        "answer_chars": str(len(answer)),
        "trigger_chars": str(len(trigger)),
    }


def main() -> int:
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if not in_path.exists():
        print(f"input_missing={in_path}")
        return 2

    text = in_path.read_text(encoding="utf-8")
    rows = [assess(title, body) for title, body in split_entries(text)]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = in_path.stem
    out_csv = OUT_DIR / f"{stem}_four_element_gate.csv"
    out_md = OUT_DIR / f"{stem}_four_element_gate.md"

    fields = ["title", "status", "reasons", "missing_count", "forbidden_count", "answer_chars", "trigger_chars"]
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    counts = {key: sum(1 for r in rows if r["status"] == key) for key in ["PASS", "WARN", "FAIL"]}
    verdict = "PASS_FOR_REVIEW_ONLY" if counts["FAIL"] == 0 else "FAIL_REPAIR_REQUIRED"
    lines = [
        "# Phase11D Four Element Gate",
        "",
        f"Input: `{in_path}`",
        f"Verdict: `{verdict}`",
        "",
        f"- entries: {len(rows)}",
        f"- PASS: {counts['PASS']}",
        f"- WARN: {counts['WARN']}",
        f"- FAIL: {counts['FAIL']}",
        "",
        "This gate is mechanical and conservative. It does not authorize Word/PDF/final.",
        "",
        "## Failures And Warnings",
        "",
    ]
    for row in rows:
        if row["status"] != "PASS":
            lines.append(f"- {row['status']}: {row['title']} | {row['reasons']}")
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {out_csv}")
    print(f"wrote {out_md}")
    print(f"verdict={verdict}")
    return 0 if counts["FAIL"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
