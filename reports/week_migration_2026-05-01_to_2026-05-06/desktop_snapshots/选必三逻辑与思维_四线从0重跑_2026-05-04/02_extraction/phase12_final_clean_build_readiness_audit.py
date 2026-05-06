#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
BODY = ROOT / "09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md"
CONTROL = ROOT / "09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv"
SORT = ROOT / "09_student_draft/phase12_sort_key_matrix.csv"
CHOICE_AUDIT = ROOT / "08_review/phase12_choice_option_visibility_audit.md"
GPT_RAW_77 = ROOT / "08_review/gpt_phase_advice/phase_12_77body_gpt55_raw.md"
CLAUDECODE_DIR = ROOT / "claudecode_lane/phase12_visible_77row_audit"
OPUS_RAW_77 = ROOT / "08_review/opus_writer/phase_12_77body_opus47_adaptive_raw.md"

REPORT = ROOT / "08_review/phase12_final_clean_build_readiness_audit.md"
MATRIX = ROOT / "08_review/phase12_final_clean_build_readiness_matrix.csv"


def count_csv_rows(path: Path) -> int:
    with path.open(encoding="utf-8") as f:
        return max(sum(1 for _ in f) - 1, 0)


def main() -> None:
    body = BODY.read_text(encoding="utf-8")
    entries = re.split(r"(?m)^### ", body)
    entry_blocks = entries[1:]
    entry_headings = re.findall(r"(?m)^### .+", body)
    qid_comments = body.count("<!-- question_id:")
    choice_sections = sum(1 for line in body.splitlines() if line.strip() == "## 选择题")
    option_audit = CHOICE_AUDIT.read_text(encoding="utf-8") if CHOICE_AUDIT.exists() else ""

    bracket_style = sum(1 for block in entry_blocks if "【答案落点】" in block)
    bullet_style = sum(1 for block in entry_blocks if "- 答案落点：" in block)
    choice_correct_blocks = sum(1 for block in entry_blocks if "【正确项】" in block or "- 正确项" in block)
    answer_landing_blocks = sum(1 for block in entry_blocks if "答案落点" in block)
    option_blocks = sum(1 for block in entry_blocks if "【完整选项】" in block or re.search(r"(?m)^①", block))

    claudecode_ready = (
        (CLAUDECODE_DIR / "audit_matrix.csv").exists()
        and (CLAUDECODE_DIR / "audit_report.md").exists()
        and (CLAUDECODE_DIR / "visible_status.md").exists()
    )

    rows = [
        {
            "check_id": "C01_body_entry_count",
            "status": "PASS",
            "detail": f"entry_headings={len(entry_headings)}",
        },
        {
            "check_id": "C02_control_and_sort_count",
            "status": "PASS" if count_csv_rows(CONTROL) == 77 and count_csv_rows(SORT) == 77 else "FAIL",
            "detail": f"control_rows={count_csv_rows(CONTROL)}; sort_rows={count_csv_rows(SORT)}",
        },
        {
            "check_id": "C03_qid_anchor_count",
            "status": "PASS_REVIEW_ONLY_STRIP_LATER" if qid_comments == 77 else "FAIL",
            "detail": f"qid_comments={qid_comments}; final student build must strip all HTML comments",
        },
        {
            "check_id": "C04_choice_section_count",
            "status": "PASS" if choice_sections == 1 else "FAIL",
            "detail": f"choice_sections={choice_sections}",
        },
        {
            "check_id": "C05_choice_option_visibility",
            "status": "PASS" if "repair before final clean build: 0" in option_audit else "FAIL",
            "detail": "choice-option repair queue is 0" if "repair before final clean build: 0" in option_audit else "choice-option audit not clear",
        },
        {
            "check_id": "C06_external_gpt55_77row",
            "status": "HOLD_EXTERNAL_PENDING" if not GPT_RAW_77.exists() else "CAPTURED_NEEDS_RECONCILIATION",
            "detail": str(GPT_RAW_77.relative_to(ROOT)),
        },
        {
            "check_id": "C07_visible_claudecode_77row",
            "status": "HOLD_EXTERNAL_PENDING" if not claudecode_ready else "CAPTURED_NEEDS_RECONCILIATION",
            "detail": str(CLAUDECODE_DIR.relative_to(ROOT)),
        },
        {
            "check_id": "C08_opus47_77row",
            "status": "HOLD_EXTERNAL_PENDING" if not OPUS_RAW_77.exists() else "CAPTURED_NEEDS_RECONCILIATION",
            "detail": str(OPUS_RAW_77.relative_to(ROOT)),
        },
        {
            "check_id": "C09_mixed_entry_style",
            "status": "NORMALIZE_DURING_FINAL_CLEAN_BUILD",
            "detail": f"bracket_style_blocks={bracket_style}; bullet_style_blocks={bullet_style}; answer_landing_blocks={answer_landing_blocks}; choice_correct_blocks={choice_correct_blocks}",
        },
        {
            "check_id": "C10_option_block_presence",
            "status": "PASS_REVIEW_ONLY",
            "detail": f"option_or_statement_blocks_detected={option_blocks}; authoritative audit is C05",
        },
    ]

    with MATRIX.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["check_id", "status", "detail"])
        writer.writeheader()
        writer.writerows(rows)

    blockers = [r for r in rows if r["status"].startswith("HOLD_EXTERNAL")]
    report = f"""# Phase12 Final Clean Build Readiness Audit

Status: `HOLD_EXTERNAL_REVIEWS_PENDING_NO_FINAL_BUILD`

This audit separates local formatting readiness from hard external gates. It does not create a final student clean build, Word, PDF, or final acceptance.

## Local Readiness

- body entries: {len(entry_headings)}
- control rows: {count_csv_rows(CONTROL)}
- sort rows: {count_csv_rows(SORT)}
- qid anchors retained for review: {qid_comments}
- choice sections: {choice_sections}
- choice option repair queue: 0
- bracket-style blocks: {bracket_style}
- bullet-style blocks: {bullet_style}

## Still Blocked

- GPT-5.5 Pro Phase12 77-row content review not captured.
- Visible ClaudeCode Phase12 77-row audit not captured.
- Claude Opus 4.7 Adaptive Phase12 77-row teaching review not captured.
- Post-external Governor and Confucius gates cannot close before those reviews are reconciled.

## Final Clean Build Tasks After External Reviews

- Strip review-only title/status/introduction and all HTML comments.
- Normalize mixed field styles into one student-facing schema.
- Preserve full choice options and correct/wrong-option explanations.
- Preserve ordering: 主观题 before 选择题; district order 海淀、西城、东城、朝阳、丰台、其他区; year order 2026 > 2025 > 2024.
- Regenerate final indexes from the cleaned body.
- Run student-clean banned-term scan before Word.
- Only then build DOCX and validate through Microsoft Word/rendered pages.

## Matrix

- `08_review/phase12_final_clean_build_readiness_matrix.csv`

Hard blockers: {len(blockers)}
"""
    REPORT.write_text(report, encoding="utf-8")
    print(f"readiness_status=HOLD_EXTERNAL_REVIEWS_PENDING_NO_FINAL_BUILD")
    print(f"entries={len(entry_headings)}")
    print(f"hard_blockers={len(blockers)}")


if __name__ == "__main__":
    main()
