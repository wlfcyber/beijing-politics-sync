#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "gap_high_confidence_repaired_classification_matrix.csv"
REPAIR = RUN_DIR / "05_reports" / "question_gap_repair_candidates.csv"
TRIAGE = RUN_DIR / "05_reports" / "question_gap_triage.csv"
OUT_MATRIX = RUN_DIR / "04_module_classification" / "raw_marker_review_repaired_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "RAW_MARKER_REVIEW_REPAIRED_COVERAGE_MATRIX.csv"
OUT_REVIEW = RUN_DIR / "05_reports" / "raw_marker_visual_review.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "raw_marker_review_repair_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "raw_marker_review_repaired_blocked_queue.csv"
OUT_GAP_AFTER = RUN_DIR / "05_reports" / "question_gap_after_raw_marker_review.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "raw_marker_review_repair_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}

# Manual source review from original DOCX text, OCR page context, and PDF text
# where available. These are deliberately limited to the 8 rows that were
# previously marked raw_marker_candidate_visual_check.
REVIEW_DECISIONS = {
    ("2024_西城_二模", "1"): {
        "review_result": "true_top_level_question",
        "book_module": "B4_PHILOSOPHY_EXCLUDED",
        "status": "module-boundary-excluded",
        "next_action": "exclude_from_three_target_lines",
        "question_type": "objective",
        "rule_id": "RAW_MARKER_REVIEW_B4_PHILOSOPHY",
        "matched_terms": "马克思主义唯物史观,发展的观点",
        "evidence_type": "original_docx_text",
        "evidence_note": "DOCX direct extraction shows 1． as a top-level objective question.",
        "evidence_text": "1． 人民至上的发展理念是对“现实的人”这一马克思主义唯物史观逻辑起点的继承和发展。以下认识正确的是 ①人民性是马克思主义的本质属性 ②与时俱进是哲学独特的理论品质 ③发展的观点是马克思主义哲学的核心观点 ④坚持人民至上体现了马克思主义历史观和价值观的统一 A．①② B．①④ C．②③ D．③④",
    },
    ("2024_西城_二模", "4"): {
        "review_result": "true_top_level_question",
        "book_module": "B2_ECONOMICS",
        "status": "included",
        "next_action": "future_baodian_intake",
        "question_type": "objective",
        "rule_id": "RAW_MARKER_REVIEW_B2_MARKET_REGULATION",
        "matched_terms": "市场调查,消费者,监管,抽检,评价标准",
        "evidence_type": "original_docx_text",
        "evidence_note": "DOCX direct extraction shows 4． as a top-level objective question.",
        "evidence_text": "4． 某校学生做市场调查，发现不少消费者对上述监测结论有疑虑，总觉得进口奶更安全可靠。同学们拟向相关主管部门提出建议，以下合理的是 ①贯彻落实绿色发展理念，科学宏观调控 ②优化政府治理流程和方式，提高政务服务效能 ③对相关企业持续监管，各个重点环节全覆盖抽检 ④采用科学统一的评价标准体系，对国产奶和进口奶评价 A．①② B．①③ C．②④ D．③④",
    },
    ("2026_丰台_一模", "5"): {
        "review_result": "false_marker",
        "book_module": "",
        "status": "",
        "next_action": "keep_gap_open",
        "question_type": "",
        "rule_id": "RAW_MARKER_FALSE_UN_SDG_LABEL",
        "matched_terms": "性别平等,清洁饮水",
        "evidence_type": "ocr_page_context",
        "evidence_note": "Marker is the UN sustainable-development goal label inside Q19 material, not top-level Q5.",
        "evidence_text": "19.(8分) ... 可持续发展目标 ... 5 性别平等 6清洁饮水和卫生设施 ...",
    },
    ("2026_丰台_一模", "14"): {
        "review_result": "true_top_level_question",
        "book_module": "XB1_EXCLUDED",
        "status": "module-boundary-excluded",
        "next_action": "exclude_from_three_target_lines",
        "question_type": "objective",
        "rule_id": "RAW_MARKER_REVIEW_XB1_INTERNATIONAL",
        "matched_terms": "中非关系,外交关系,零关税,文明互鉴",
        "evidence_type": "ocr_page_context",
        "evidence_note": "OCR page context shows Q14 starts after Q13 answer options and before Q15.",
        "evidence_text": "14 ‘2026年是中国与非洲正式开启外交关系70周年... 中国将于今年5月1日全面实施对非100%税目产品零关税... “中非人文交流年”已拉开大幕... 中非关系新发展 ①彰显中非休戚与共、命运相连的深厚情谊 ②通过政治经济等领域的合作开创新局面 ③以人文交往拓展了国际关系的基本形式 ④通过加强全天候伙伴关系巩固中非同盟 A.12 B.13 C.24 D.84",
    },
    ("2026_丰台_二模", "15"): {
        "review_result": "false_marker",
        "book_module": "",
        "status": "",
        "next_action": "keep_gap_open",
        "question_type": "",
        "rule_id": "RAW_MARKER_FALSE_LIST_ITEM",
        "matched_terms": "加强服务三农检察工作",
        "evidence_type": "pdf_text_page_context",
        "evidence_note": "Marker is item 15 in a list of检察工作任务 on page 1, not top-level Q15.",
        "evidence_text": "最高人民检察院部署16项重点工作任务... 14 加大文物和文化遗产司法保护力度 15 加强服务“三农”检察工作 16 常态化推进矛盾纠纷多元化解",
    },
    ("2026_丰台_期末", "2"): {
        "review_result": "false_marker",
        "book_module": "",
        "status": "",
        "next_action": "keep_gap_open",
        "question_type": "",
        "rule_id": "RAW_MARKER_FALSE_OPTION_UNIT",
        "matched_terms": "二线加强监管",
        "evidence_type": "ocr_page_context",
        "evidence_note": "Marker is option ② in a Hainan free-trade-port objective question, not top-level Q2.",
        "evidence_text": "下列传导正确的是 ①“一线”实施负面清单管理... ②“二线”加强监管—阻断金融风险—防止国家税收流失 ③海南岛内要素自由流通... ④海南自由贸易港全岛封关...",
    },
    ("2026_房山_一模", "1"): {
        "review_result": "true_top_level_question",
        "book_module": "B4_CULTURE",
        "status": "included",
        "next_action": "future_baodian_intake",
        "question_type": "objective",
        "rule_id": "RAW_MARKER_REVIEW_B4_CULTURE_SPIRIT",
        "matched_terms": "伟大建党精神,精神谱系,红色精神",
        "evidence_type": "ocr_page_context",
        "evidence_note": "OCR page context shows top-level Q1 before page 2 Q2.",
        "evidence_text": "坚定信念、艰苦奋斗，实事求是、敢闯新路，依靠群众、勇于胜利 井冈山精神 ... 中国航天精神 特别能吃苦、特别能战斗、特别能攻关、特别能奉献 从伟大精神中汲取奋进力量... 以伟大建党精神为源头的精神谱系是 A.社会主义建设规律的思想引领... B.马克思主义中国化时代化的理论成果... C.中国人民百年奋斗的精神密码... D.解决我国社会主要矛盾的必由之路...",
    },
    ("2026_西城_期末", "15"): {
        "review_result": "true_top_level_question",
        "book_module": "XB1_EXCLUDED",
        "status": "module-boundary-excluded",
        "next_action": "exclude_from_three_target_lines",
        "question_type": "objective",
        "rule_id": "RAW_MARKER_REVIEW_XB1_GLOBAL_GOVERNANCE",
        "matched_terms": "国际调解院,国际争端,全球治理",
        "evidence_type": "ocr_page_context",
        "evidence_note": "OCR page context shows Q15 after Q14 answer options and before 第二部分.",
        "evidence_text": "15 包括中国在内的33个国家签署国际调解院公约，国际调解院正式成立... 国际调解院 ①主张通过对话修复关系，有利于提升全球治理包容性 ②践行联合国和平解决争端原则... ③是首个专门调解国际争端的国际组织... ④适应了国际力量结构的新变化... A.12 B.14 C.28 D.34",
    },
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
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


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    existing = {(row["suite_id"], row["question"]) for row in rows}
    review_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    added_rows: list[dict[str, str]] = []

    repair_rows = [
        row
        for row in load_csv(REPAIR)
        if row["recommended_action"] == "raw_marker_candidate_visual_check"
    ]
    for repair in repair_rows:
        key = (repair["suite_id"], repair["missing_question"])
        decision = REVIEW_DECISIONS[key]
        review_row = {
            "suite_id": repair["suite_id"],
            "question": repair["missing_question"],
            "review_result": decision["review_result"],
            "book_module": decision["book_module"],
            "status": decision["status"],
            "next_action": decision["next_action"],
            "rule_id": decision["rule_id"],
            "matched_terms": decision["matched_terms"],
            "evidence_type": decision["evidence_type"],
            "evidence_note": decision["evidence_note"],
            "raw_marker_text_path": repair["raw_marker_text_path"],
            "evidence_text": compact(decision["evidence_text"], 1200),
        }
        review_rows.append(review_row)
        if decision["review_result"] != "true_top_level_question" or key in existing:
            continue
        year, district, stage = parse_suite(repair["suite_id"])
        new = {field: "" for field in fields}
        new.update(
            {
                "suite_id": repair["suite_id"],
                "year": year,
                "district": district,
                "stage": stage,
                "question": repair["missing_question"],
                "parent_question": "",
                "row_granularity": "question",
                "book_module": decision["book_module"],
                "question_type": decision["question_type"],
                "evidence_source": repair["raw_marker_text_path"],
                "source_types": f"{decision['evidence_type']};raw-marker-review",
                "status": decision["status"],
                "artifact_location": "05_reports/raw_marker_review_repair_audit.csv",
                "decision_reason": json.dumps(
                    {
                        "rule_id": decision["rule_id"],
                        "matched_terms": decision["matched_terms"],
                        "source": "raw_marker_visual_review.csv",
                        "evidence_type": decision["evidence_type"],
                    },
                    ensure_ascii=False,
                ),
                "next_action": decision["next_action"],
                "integration_status": "raw_marker_review_repair",
            }
        )
        added_rows.append(new)
        audit_rows.append(
            {
                "suite_id": repair["suite_id"],
                "question": repair["missing_question"],
                "new_book_module": decision["book_module"],
                "new_status": decision["status"],
                "rule_id": decision["rule_id"],
                "matched_terms": decision["matched_terms"],
                "evidence_type": decision["evidence_type"],
                "evidence_text": compact(decision["evidence_text"], 1200),
            }
        )

    out_rows = rows + added_rows
    write_csv(
        OUT_REVIEW,
        review_rows,
        [
            "suite_id",
            "question",
            "review_result",
            "book_module",
            "status",
            "next_action",
            "rule_id",
            "matched_terms",
            "evidence_type",
            "evidence_note",
            "raw_marker_text_path",
            "evidence_text",
        ],
    )
    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(
        OUT_AUDIT,
        audit_rows,
        [
            "suite_id",
            "question",
            "new_book_module",
            "new_status",
            "rule_id",
            "matched_terms",
            "evidence_type",
            "evidence_text",
        ],
    )
    write_csv(OUT_BLOCKED, [row for row in out_rows if row["status"] == "blocked"], fields)

    resolved_keys = {(row["suite_id"], row["question"]) for row in out_rows}
    added_keys = {(row["suite_id"], row["question"]) for row in added_rows}
    gap_after = []
    for row in load_csv(TRIAGE):
        missing_before = row["missing_if_expected_1_to_21"].split()
        gap_after.append(
            {
                "suite_id": row["suite_id"],
                "missing_after_raw_marker_review": " ".join(
                    q for q in missing_before if (row["suite_id"], q) not in resolved_keys
                ),
                "resolved_by_raw_marker_review": " ".join(
                    q for q in missing_before if (row["suite_id"], q) in added_keys
                ),
                "prior_triage_status": row["triage_status"],
            }
        )
    write_csv(
        OUT_GAP_AFTER,
        gap_after,
        [
            "suite_id",
            "missing_after_raw_marker_review",
            "resolved_by_raw_marker_review",
            "prior_triage_status",
        ],
    )

    status_counts = Counter(row["status"] for row in out_rows)
    target_counts = Counter(
        row["book_module"]
        for row in out_rows
        if row["status"] == "included" and row["book_module"] in TARGET_MODULES
    )
    review_counts = Counter(row["review_result"] for row in review_rows)
    added_counts = Counter(row["book_module"] for row in added_rows)
    remaining_missing = sum(
        len(row["missing_after_raw_marker_review"].split())
        for row in gap_after
        if row["missing_after_raw_marker_review"]
    )

    lines = [
        "# Raw Marker Review Repair Report",
        "",
        f"- input_matrix_rows: {len(rows)}",
        f"- reviewed_raw_marker_rows: {len(review_rows)}",
        f"- added_true_question_rows: {len(added_rows)}",
        f"- output_rows: {len(out_rows)}",
        f"- output_matrix: `{OUT_MATRIX}`",
        f"- output_coverage: `{OUT_COVERAGE}`",
        f"- review_file: `{OUT_REVIEW}`",
        f"- audit_file: `{OUT_AUDIT}`",
        f"- remaining_missing_question_entries_from_prior_gap: {remaining_missing}",
        "",
        "## Review Counts",
        "",
    ]
    for key, value in review_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Added Module Counts", ""])
    for key, value in added_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Status Counts", ""])
    for key, value in status_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Target Included Counts", ""])
    for key in ["B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"]:
        lines.append(f"- {key}: {target_counts.get(key, 0)}")
    lines.extend(
        [
            "",
            "## Governor Note",
            "",
            "- This matrix integrates only raw-marker candidates confirmed as true top-level questions by source review.",
            "- False markers remain gap/open-source-inspection items and are not written into the matrix.",
            "- Final closure remains rejected because blocked rows and unresolved gap entries remain.",
        ]
    )
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(OUT_MATRIX)
    print(OUT_COVERAGE)
    print(OUT_REVIEW)
    print("review_counts", dict(review_counts))
    print("added", len(added_rows), "rows", len(out_rows), "remaining_gap_entries", remaining_missing)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
