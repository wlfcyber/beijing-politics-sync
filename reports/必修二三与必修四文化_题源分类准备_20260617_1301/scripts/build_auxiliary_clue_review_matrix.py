#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "raw_marker_review_repaired_classification_matrix.csv"
REPAIR = RUN_DIR / "05_reports" / "question_gap_repair_candidates.csv"
GAP_BEFORE = RUN_DIR / "05_reports" / "question_gap_after_raw_marker_review.csv"
OUT_MATRIX = RUN_DIR / "04_module_classification" / "auxiliary_clue_repaired_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "AUXILIARY_CLUE_REPAIRED_COVERAGE_MATRIX.csv"
OUT_REVIEW = RUN_DIR / "05_reports" / "auxiliary_clue_source_review.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "auxiliary_clue_repair_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "auxiliary_clue_repaired_blocked_queue.csv"
OUT_GAP_AFTER = RUN_DIR / "05_reports" / "question_gap_after_auxiliary_clue_review.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "auxiliary_clue_repair_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}

# Manual source review for the six auxiliary-only clues. Each decision below
# requires original-paper DOCX text or OCR page context; rubric-only clues do
# not create new rows.
REVIEW_DECISIONS = {
    ("2024_顺义_二模", "6"): {
        "review_result": "true_top_level_question_hidden_number",
        "rows": [
            {
                "question": "6",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB3_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "AUX_REVIEW_XB3_FORMAL_LOGIC",
                "matched_terms": "形式逻辑,逻辑思维能力,复合判断,排中律",
                "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/顺义思政二模/试卷/试卷.docx",
                "source_types": "original_docx_text;auxiliary-clue-review",
                "evidence_type": "original_docx_text",
                "evidence_note": "DOCX direct extraction shows a top-level objective question between Q5 and Q7; visible question number is missing in extracted text.",
                "evidence_text": "在生活和工作中，有些听起来似乎有道理，但仔细想起来，又疑窦丛生，这就需要学习形式逻辑，提升逻辑思维能力。下列观点和逻辑分析正确的是 A 法定继承第一顺位继承人中的子女... B 若a=b，则ac=bc... C 刑法第二十条规定...该判断属于复合判断 D “服务员同志...” ... 违反了排中律",
            }
        ],
    },
    ("2024_顺义_二模", "20"): {
        "review_result": "true_top_level_question_hidden_number",
        "rows": [
            {
                "question": "20",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B1_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "subjective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "AUX_REVIEW_B1_PARTY_THEORY_MIXED",
                "matched_terms": "科学理论的政党,中华民族伟大复兴,马克思主义中国化时代化,中国共产党的领导",
                "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/顺义思政二模/试卷/试卷.docx",
                "source_types": "original_docx_text;auxiliary-clue-review",
                "evidence_type": "original_docx_text",
                "evidence_note": "DOCX direct extraction shows a top-level subjective question after Q19; visible question number is missing in extracted text.",
                "evidence_text": "(10分)拥有科学理论的政党，才拥有真理的力量；科学理论指导的事业，才拥有光明的前途。 （1）我们如期完成脱贫攻坚、全面建成小康社会的历史任务...完成下表。（2分） 结合材料，综合运用所学，谈谈对实现中华民族伟大复兴需要“不断谱写马克思主义中国化时代化新篇章”的认识。（8分）",
            }
        ],
    },
    ("2026_丰台_一模", "7"): {
        "review_result": "true_top_level_question_ocr_hyphen_marker",
        "rows": [
            {
                "question": "7",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB3_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "AUX_REVIEW_XB3_SCIENTIFIC_THINKING",
                "matched_terms": "四诊法,科学的思维方法",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_一模.txt"),
                "source_types": "ocr_page_context;auxiliary-clue-review",
                "evidence_type": "ocr_page_context",
                "evidence_note": "OCR page context shows Q7 as '7-四诊法...' after Q6 and before Q8.",
                "evidence_text": "7-四诊法是中医诊断的基本方法，包括望诊、闻诊、问诊、切诊四种诊察手段。四诊法的应用体现了科学的思维方法。下列认识正确的是... A.12 B.14 C.23 D.34",
            }
        ],
    },
    ("2026_丰台_期末", "6"): {
        "review_result": "source_not_found_keep_gap_open",
        "rows": [],
        "evidence_note": "Rubric clue mentions Q6, but primary OCR/PDF text review did not locate a reliable top-level Q6 span. Kept open.",
        "evidence_type": "rubric_clue_only_unaccepted",
        "evidence_text": "较少数学生的字迹太过潦草。 7,检察院的”监察权”,检察院的监管职能,检察院的判决以事实 为......公平公正。",
    },
    ("2026_丰台_期末", "9"): {
        "review_result": "true_top_level_question_hidden_number",
        "rows": [
            {
                "question": "9",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B3_POLITICS_RULE_OF_LAW",
                "status": "included",
                "question_type": "objective",
                "next_action": "future_baodian_intake",
                "rule_id": "AUX_REVIEW_B3_CPPCC",
                "matched_terms": "人民政协,政协委员,科学讲堂",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_期末.txt"),
                "source_types": "ocr_page_context;auxiliary-clue-review",
                "evidence_type": "ocr_page_context",
                "evidence_note": "OCR page context places this objective question after Q8; the leading top-level number is absent in OCR text.",
                "evidence_text": "全国政协创新开展“委员科学讲堂”活动，来自科研、教育界的政协委员走进校园、社区、企业，围绕前沿科技、基础科学、航天探索等话题开展讲座，揭开前沿科技的神秘面纱，回应群众学习科学的迫切需求。这体现了人民政协 ①通过政治协商，拓宽了与群众的沟通渠道 ②发挥人才优势，为科技强国建设贡献力量 ③弘扬科学精神，形成崇尚科学的社会氛围 ④履行文化职能，搭建普及科学知识的平台 A.12 B.14 C.23 D.34",
            }
        ],
    },
    ("2026_房山_一模", "17"): {
        "review_result": "true_top_level_question_split_subquestions",
        "rows": [
            {
                "question": "17(1)",
                "parent_question": "17",
                "row_granularity": "subquestion",
                "book_module": "XB2_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "subjective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "AUX_REVIEW_XB2_CIVIL_LEGAL_RELATIONSHIP",
                "matched_terms": "民事法律关系,AI幻觉,民事主体资格",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_房山_一模.txt"),
                "source_types": "ocr_page_context;auxiliary-clue-review",
                "evidence_type": "ocr_page_context",
                "evidence_note": "OCR page context shows Q17(1) as a legal Life question; split from the B3 law subquestion.",
                "evidence_text": "17(9分) AI幻觉造成损失谁买单? 某AI模型系A公司研发... (1)结合材料，运用“民事法律关系”知识，辨析“AI幻觉造成损失谁买单”。(3分)",
            },
            {
                "question": "17(2)",
                "parent_question": "17",
                "row_granularity": "subquestion",
                "book_module": "B3_POLITICS_RULE_OF_LAW",
                "status": "included",
                "question_type": "subjective",
                "next_action": "future_baodian_intake",
                "rule_id": "AUX_REVIEW_B3_SUPREME_COURT_RULE_OF_LAW",
                "matched_terms": "法治知识,最高人民法院工作报告,案例写入报告",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_房山_一模.txt"),
                "source_types": "ocr_page_context;auxiliary-clue-review",
                "evidence_type": "ocr_page_context",
                "evidence_note": "OCR page context shows Q17(2) asks the significance of inclusion in the Supreme People's Court work report; split as B3 rule-of-law content.",
                "evidence_text": "该案例写入2026年最高人民法院工作报告。(2)结合材料，运用法治知识，分析该案例写入最高人民法院工作报告的意义。(6分)",
            },
        ],
    },
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def parse_suite(suite_id: str) -> tuple[str, str, str]:
    parts = suite_id.split("_")
    return (
        parts[0] if len(parts) > 0 else "",
        parts[1] if len(parts) > 1 else "",
        parts[2] if len(parts) > 2 else "",
    )


def compact(text: str, limit: int = 900) -> str:
    return re.sub(r"\s+", " ", text).strip()[:limit]


def read_prior_gaps() -> dict[str, list[str]]:
    gaps: dict[str, list[str]] = {}
    if not GAP_BEFORE.exists():
        return gaps
    for row in load_csv(GAP_BEFORE):
        missing = [
            item.strip()
            for item in re.split(r"[;\s]+", row.get("missing_after_raw_marker_review", ""))
            if item.strip()
        ]
        gaps[row["suite_id"]] = missing
    return gaps


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    existing = {(row["suite_id"], row["question"]) for row in rows}
    repair_rows = {
        (row["suite_id"], row["missing_question"]): row
        for row in load_csv(REPAIR)
        if (row["suite_id"], row["missing_question"]) in REVIEW_DECISIONS
    }

    review_fields = [
        "suite_id",
        "question",
        "review_result",
        "added_matrix_rows",
        "candidate_source_types",
        "best_candidate_file",
        "best_candidate_snippet",
        "evidence_type",
        "evidence_note",
        "evidence_text",
    ]
    audit_fields = [
        "suite_id",
        "question",
        "new_book_module",
        "new_status",
        "row_granularity",
        "rule_id",
        "matched_terms",
        "evidence_type",
        "evidence_text",
    ]

    review_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    added_rows: list[dict[str, str]] = []
    resolved_parent_questions: set[tuple[str, str]] = set()

    for key, decision in REVIEW_DECISIONS.items():
        repair = repair_rows.get(key)
        if not repair:
            raise SystemExit(f"missing repair candidate for {key}")
        decision_rows = decision.get("rows", [])
        review_rows.append(
            {
                "suite_id": key[0],
                "question": key[1],
                "review_result": decision["review_result"],
                "added_matrix_rows": str(len(decision_rows)),
                "candidate_source_types": repair.get("candidate_source_types", ""),
                "best_candidate_file": repair.get("best_candidate_file", ""),
                "best_candidate_snippet": compact(repair.get("best_candidate_snippet", ""), 500),
                "evidence_type": decision.get("evidence_type", decision_rows[0]["evidence_type"] if decision_rows else ""),
                "evidence_note": decision.get("evidence_note", "; ".join(row["evidence_note"] for row in decision_rows)),
                "evidence_text": compact(decision.get("evidence_text", " | ".join(row["evidence_text"] for row in decision_rows)), 1200),
            }
        )
        if decision_rows:
            resolved_parent_questions.add(key)

        for decision_row in decision_rows:
            new_key = (key[0], decision_row["question"])
            if new_key in existing:
                continue
            year, district, stage = parse_suite(key[0])
            new = {field: "" for field in fields}
            new.update(
                {
                    "suite_id": key[0],
                    "year": year,
                    "district": district,
                    "stage": stage,
                    "question": decision_row["question"],
                    "parent_question": decision_row["parent_question"],
                    "row_granularity": decision_row["row_granularity"],
                    "book_module": decision_row["book_module"],
                    "question_type": decision_row["question_type"],
                    "evidence_source": decision_row["evidence_source"],
                    "source_types": decision_row["source_types"],
                    "status": decision_row["status"],
                    "artifact_location": "05_reports/auxiliary_clue_repair_audit.csv",
                    "decision_reason": json.dumps(
                        {
                            "rule_id": decision_row["rule_id"],
                            "matched_terms": decision_row["matched_terms"],
                            "source": "auxiliary_clue_source_review.csv",
                            "evidence_type": decision_row["evidence_type"],
                            "parent_missing_question": key[1],
                        },
                        ensure_ascii=False,
                    ),
                    "next_action": decision_row["next_action"],
                    "integration_status": "auxiliary_clue_review_repair",
                }
            )
            added_rows.append(new)
            audit_rows.append(
                {
                    "suite_id": key[0],
                    "question": decision_row["question"],
                    "new_book_module": decision_row["book_module"],
                    "new_status": decision_row["status"],
                    "row_granularity": decision_row["row_granularity"],
                    "rule_id": decision_row["rule_id"],
                    "matched_terms": decision_row["matched_terms"],
                    "evidence_type": decision_row["evidence_type"],
                    "evidence_text": compact(decision_row["evidence_text"], 1200),
                }
            )

    out_rows = rows + added_rows
    write_csv(OUT_REVIEW, review_rows, review_fields)
    write_csv(OUT_AUDIT, audit_rows, audit_fields)
    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)

    blocked_rows = [row for row in out_rows if row["status"] == "blocked"]
    write_csv(OUT_BLOCKED, blocked_rows, fields)

    gap_rows = []
    prior_gaps = read_prior_gaps()
    for suite_id in sorted(prior_gaps):
        missing_after = [
            q
            for q in prior_gaps[suite_id]
            if (suite_id, q) not in resolved_parent_questions
        ]
        resolved = [
            q
            for q in prior_gaps[suite_id]
            if (suite_id, q) in resolved_parent_questions
        ]
        gap_rows.append(
            {
                "suite_id": suite_id,
                "missing_after_auxiliary_clue_review": ";".join(missing_after),
                "resolved_by_auxiliary_clue_review": ";".join(resolved),
            }
        )
    write_csv(
        OUT_GAP_AFTER,
        gap_rows,
        [
            "suite_id",
            "missing_after_auxiliary_clue_review",
            "resolved_by_auxiliary_clue_review",
        ],
    )

    status_counts = Counter(row["status"] for row in out_rows)
    included_modules = Counter(
        row["book_module"] for row in out_rows if row["status"] == "included"
    )
    gap_remaining = sum(
        1
        for row in gap_rows
        for item in row["missing_after_auxiliary_clue_review"].split(";")
        if item.strip()
    )
    duplicate_keys = len(out_rows) - len({(row["suite_id"], row["question"]) for row in out_rows})

    report = f"""# Auxiliary Clue Source Review Repair Report

Generated from `{IN_MATRIX.name}`.

## Scope

- Reviewed auxiliary-only clues: {len(REVIEW_DECISIONS)}
- Added matrix rows: {len(added_rows)}
- Unaccepted auxiliary clues: 1 (`2026_丰台_期末` Q6, primary source not found)

## Matrix Counts

- Rows: {len(out_rows)}
- Status counts: {dict(status_counts)}
- Included module counts: {dict(included_modules)}
- Duplicate `(suite_id, question)` keys: {duplicate_keys}
- Remaining question-gap entries: {gap_remaining}

## Decisions

- `2024_顺义_二模` Q6: accepted as top-level hidden-number question; classified `XB3_EXCLUDED`.
- `2024_顺义_二模` Q20: accepted as top-level hidden-number question; classified `B1_EXCLUDED`.
- `2026_丰台_一模` Q7: accepted as top-level OCR hyphen-marker question; classified `XB3_EXCLUDED`.
- `2026_丰台_期末` Q6: not accepted; rubric clue only, no reliable primary-source span located.
- `2026_丰台_期末` Q9: accepted as top-level hidden-number question; classified `B3_POLITICS_RULE_OF_LAW`.
- `2026_房山_一模` Q17: accepted and split into Q17(1) `XB2_EXCLUDED` plus Q17(2) `B3_POLITICS_RULE_OF_LAW`.

## Deliverables

- `{OUT_REVIEW.relative_to(RUN_DIR)}`
- `{OUT_AUDIT.relative_to(RUN_DIR)}`
- `{OUT_MATRIX.relative_to(RUN_DIR)}`
- `{OUT_COVERAGE.relative_to(RUN_DIR)}`
- `{OUT_BLOCKED.relative_to(RUN_DIR)}`
- `{OUT_GAP_AFTER.relative_to(RUN_DIR)}`
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
