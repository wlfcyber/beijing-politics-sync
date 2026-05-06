#!/usr/bin/env python3
"""Audit whether Phase12 choice entries visibly carry all four option units."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
BODY = BASE / "09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md"
CONTROL = BASE / "09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv"
AUDIT_CSV = BASE / "08_review/phase12_choice_option_visibility_audit.csv"
AUDIT_MD = BASE / "08_review/phase12_choice_option_visibility_audit.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def parse_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", text, re.M))
    sections: dict[str, str] = {}
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
        sections[title] = body
    return sections


def option_status(text: str) -> tuple[str, str]:
    circled = {d: (d in text) for d in ["①", "②", "③", "④"]}
    abcd = {d: bool(re.search(rf"(^|[\\s【（(]){d}[．.、:：)]", text, re.M)) for d in ["A", "B", "C", "D"]}
    has_correct = "正确项" in text or "正确选项" in text
    has_trap = "错项" in text or "陷阱" in text
    if all(circled.values()):
        return "four_statement_units_visible", "①②③④ all visible in current body"
    if all(abcd.values()):
        return "abcd_options_visible", "A/B/C/D option markers visible in current body"
    if has_correct and has_trap:
        return "answer_and_trap_visible_but_full_options_missing", "has correct/trap analysis but not all four option units"
    return "choice_entry_needs_source_option_repair", "choice entry does not visibly carry all four options"


def main() -> None:
    rows = [row for row in read_csv(CONTROL) if row["question_type_group"] == "选择题"]
    sections = parse_sections(BODY.read_text(encoding="utf-8"))
    out_rows: list[dict[str, str]] = []
    for row in rows:
        text = sections.get(row["visible_title"], "")
        status, note = option_status(text)
        out_rows.append(
            {
                "order": row["order"],
                "question_id": row["question_id"],
                "visible_title": row["visible_title"],
                "district": row["district"],
                "year": row["year"],
                "exam_stage": row["exam_stage"],
                "option_visibility_status": status,
                "final_clean_build_action": "keep" if status in {"four_statement_units_visible", "abcd_options_visible"} else "repair_before_final_clean_build",
                "note": note,
            }
        )

    AUDIT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_CSV.open("w", newline="", encoding="utf-8") as f:
        fields = [
            "order",
            "question_id",
            "visible_title",
            "district",
            "year",
            "exam_stage",
            "option_visibility_status",
            "final_clean_build_action",
            "note",
        ]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_rows)

    counts = Counter(row["option_visibility_status"] for row in out_rows)
    repair_rows = [row for row in out_rows if row["final_clean_build_action"] == "repair_before_final_clean_build"]
    status = "CHOICE_OPTION_VISIBILITY_AUDIT_DONE_NO_REPAIR_QUEUE" if not repair_rows else "CHOICE_OPTION_VISIBILITY_AUDIT_DONE_FINAL_REPAIR_REQUIRED"
    parts = [
        "# Phase12 Choice Option Visibility Audit",
        "",
        f"Status: `{status}`",
        "",
        "用户此前要求选择题统一显示四个选项。本审计只检查当前 77-row review-only 正文的选择题选项可见性，不授权 Word/PDF/final。",
        "",
        "## Counts",
        "",
        f"- choice rows: {len(out_rows)}",
    ]
    for key, value in counts.items():
        parts.append(f"- {key}: {value}")
    parts.extend(
        [
            f"- repair before final clean build: {len(repair_rows)}",
            "",
            "## Repair Queue",
            "",
        ]
    )
    if repair_rows:
        for row in repair_rows:
            parts.append(f"- 第{row['order']}条：{row['visible_title']} | {row['option_visibility_status']}")
    else:
        parts.append("- none")
    parts.extend(
        [
            "",
            "## Rule",
            "",
            "- 最终学生 clean build 前，选择题必须统一恢复完整选项或完整 ①②③④ 选项单位。",
            "- 当前 review-only 正文仍可继续外部审查，但不得据此生成 Word。",
        ]
    )
    AUDIT_MD.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(dict(counts))
    print(f"repair_rows={len(repair_rows)}")


if __name__ == "__main__":
    main()
