#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
BODY = ROOT / "09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md"
REPORT = ROOT / "08_review/phase12_preclean_metadata_cleanup_report.md"
ACTIONS = ROOT / "08_review/phase12_preclean_metadata_cleanup_actions.csv"
BACKUP = ROOT / "audit/phase12_expanded_body_FROM_362_REVIEW_ONLY_before_preclean_metadata_cleanup.md"


def main() -> None:
    original = BODY.read_text(encoding="utf-8")
    BACKUP.parent.mkdir(parents=True, exist_ok=True)
    if not BACKUP.exists():
        BACKUP.write_text(original, encoding="utf-8")

    actions: list[dict[str, str]] = []
    out: list[str] = []
    prev_line = None
    previous_nonblank = ""
    qid_comments_in_entry: set[str] = set()

    for lineno, line in enumerate(original.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("### "):
            qid_comments_in_entry.clear()

        is_qid_comment = stripped.startswith("<!-- question_id:") and stripped.endswith("-->")
        if is_qid_comment and (prev_line == line or stripped in qid_comments_in_entry):
            actions.append(
                {
                    "line": str(lineno),
                    "action": "remove_duplicate_qid_comment_in_entry",
                    "detail": stripped,
                }
            )
            continue

        if stripped == "## 选择题" and previous_nonblank == "## 选择题":
            actions.append(
                {
                    "line": str(lineno),
                    "action": "remove_duplicate_section_heading",
                    "detail": stripped,
                }
            )
            continue

        out.append(line)
        prev_line = line
        if is_qid_comment:
            qid_comments_in_entry.add(stripped)
        if stripped:
            previous_nonblank = stripped

    cleaned = "\n".join(out) + "\n"
    BODY.write_text(cleaned, encoding="utf-8")

    with ACTIONS.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["line", "action", "detail"])
        writer.writeheader()
        writer.writerows(actions)

    before_entries = sum(1 for line in original.splitlines() if line.startswith("### "))
    after_entries = sum(1 for line in cleaned.splitlines() if line.startswith("### "))
    before_qid_comments = original.count("<!-- question_id:")
    after_qid_comments = cleaned.count("<!-- question_id:")
    before_choice_sections = sum(1 for line in original.splitlines() if line.strip() == "## 选择题")
    after_choice_sections = sum(1 for line in cleaned.splitlines() if line.strip() == "## 选择题")

    report = f"""# Phase12 Preclean Metadata Cleanup Report

Status: `REVIEW_ONLY_METADATA_CLEANUP_DONE_NO_FINAL_AUTHORIZATION`

This cleanup only removes duplicated review metadata from the 77-row review-only body. It does not change knowledge content, answer judgments, option text, or trap explanations. It does not authorize Word/PDF/final.

## Files

- body: `09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md`
- backup: `audit/phase12_expanded_body_FROM_362_REVIEW_ONLY_before_preclean_metadata_cleanup.md`
- action log: `08_review/phase12_preclean_metadata_cleanup_actions.csv`

## Counts

- entry headings before: {before_entries}
- entry headings after: {after_entries}
- question_id comments before: {before_qid_comments}
- question_id comments after: {after_qid_comments}
- duplicate qid comments removed: {before_qid_comments - after_qid_comments}
- choice section headings before: {before_choice_sections}
- choice section headings after: {after_choice_sections}
- duplicate choice section headings removed: {before_choice_sections - after_choice_sections}

## Gate

Still blocked before final student build:

- external GPT-5.5 Pro 77-row review
- visible ClaudeCode 77-row audit
- Claude Opus 4.7 Adaptive teaching review
- post-external Governor and Confucius gates
- final clean Markdown and Word/PDF validation
"""
    REPORT.write_text(report, encoding="utf-8")
    print(f"actions={len(actions)}")
    print(f"entries={after_entries}")
    print(f"qid_comments={after_qid_comments}")
    print(f"choice_sections={after_choice_sections}")


if __name__ == "__main__":
    main()
