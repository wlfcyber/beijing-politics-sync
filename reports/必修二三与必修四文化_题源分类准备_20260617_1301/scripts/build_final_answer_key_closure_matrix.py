#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "culture_hint_final_cleanup_classification_matrix.csv"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "final_answer_key_closure_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "final_answer_key_closure_audit.csv"
OUT_COMPONENT_AUDIT = RUN_DIR / "05_reports" / "final_answer_key_component_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "final_answer_key_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "final_answer_key_closure_report.md"

YIMO_ANSWER_TEXT = (
    "/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04/"
    "02_extraction/supplemental_answer_sources/2026北京丰台高三一模政治试题有答案_北京高考在线.txt"
)
YIMO_ANSWER_IMAGE = (
    RUN_DIR / "05_reports" / "rendered_evidence" / "2026_fengtai_firstmock_answer_page-09.png"
)
QIMO_ANSWER_VISION = (
    "/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/preprocess_v2_2026-05-03/"
    "supplemental_answer_sources/2026北京丰台高三（上）期末政治_有答案_vision.txt"
)
QIMO_ANSWER_IMAGE = (
    RUN_DIR / "05_reports" / "rendered_evidence" / "2026_fengtai_final_answer_page-10.png"
)
YIMO_PAPER_OCR = RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_一模.txt"
QIMO_PAPER_OCR = RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_期末.txt"


ROW_RESOLUTIONS = {
    ("2026_丰台_一模", "1"): {
        "module": "B1_EXCLUDED",
        "rule_id": "FINAL_KEY_FENGTAI_YIMO_Q1_ANSWER_B_PARENT_REMAINDER",
        "matched_terms": "答案B,党的全面领导,个人奋斗,民族复兴",
        "basis": "补充答案源和渲染答案页显示第1题答案为 B。正确项①为党的全面领导，已另抽 B3 组件；正确项④为个人奋斗融入民族复兴，父题余项按 B1/综合边界关闭。",
        "source_type": "paper+answer_key+rendered_answer_page",
        "source": f"{YIMO_PAPER_OCR} | {YIMO_ANSWER_TEXT} | {YIMO_ANSWER_IMAGE}",
        "evidence_text": "2026丰台一模第1题答案 B；选项①“不忘初心、方得始终，坚持党的全面领导确保中国式现代化行稳致远”；选项④“坚定信仰、志存高远，将个人的奋斗融入国家和民族的伟大复兴之中”。",
    },
    ("2026_丰台_期末", "2"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "FINAL_KEY_FENGTAI_QIMO_Q2_ANSWER_C_PARENT_REMAINDER",
        "matched_terms": "答案C,群众观点,孝亲敬老,传统美德",
        "basis": "渲染答案页显示第2题答案为 C，即②③。③“弘扬孝亲敬老的传统美德”已作为 B4_CULTURE 组件入账；②“坚持群众观点”属于哲学余项，父题余项按 B4_PHILOSOPHY_EXCLUDED 关闭。",
        "source_type": "paper+answer_key+rendered_answer_page",
        "source": f"{QIMO_PAPER_OCR} | {QIMO_ANSWER_VISION} | {QIMO_ANSWER_IMAGE}",
        "evidence_text": "2026丰台期末第2题答案 C；选项②为群众观点，选项③为孝亲敬老传统美德。既有 2#B4_CULTURE_COMPONENT 保留，父题余项关闭为哲学边界。",
    },
    ("2026_丰台_期末", "6"): {
        "module": "XB3_EXCLUDED",
        "rule_id": "FINAL_KEY_FENGTAI_QIMO_Q6_ANSWER_A_PARENT_REMAINDER",
        "matched_terms": "答案A,中国结,中华优秀传统文化,形象思维",
        "basis": "渲染答案页显示第6题答案为 A，即①③。①“中国结传承中华优秀传统文化、承载精神追求”已作为 B4_CULTURE 组件入账；③“运用形象思维”属于选必三余项，父题余项按 XB3_EXCLUDED 关闭。",
        "source_type": "paper+answer_key+rendered_answer_page",
        "source": f"{QIMO_PAPER_OCR} | {QIMO_ANSWER_VISION} | {QIMO_ANSWER_IMAGE}",
        "evidence_text": "2026丰台期末第6题答案 A；选项①为中华优秀传统文化/精神追求，选项③为形象思维。既有 6#B4_CULTURE_COMPONENT 保留，父题余项关闭为选必三边界。",
    },
}

NEW_COMPONENTS = [
    {
        "suite_id": "2026_丰台_一模",
        "parent_question": "1",
        "component_question": "1#B3_COMPONENT",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "FINAL_KEY_B3_COMPONENT_PARTY_LEADERSHIP_Q1",
        "matched_terms": "党的全面领导,中国式现代化,行稳致远",
        "basis": "第1题答案 B 的正确项①明确“坚持党的全面领导确保中国式现代化行稳致远”，属于必修三党的领导采分点；该组件供后续 B3 宝典接手。",
        "source_type": "paper+answer_key+rendered_answer_page",
        "source": f"{YIMO_PAPER_OCR} | {YIMO_ANSWER_TEXT} | {YIMO_ANSWER_IMAGE}",
        "evidence_text": "2026丰台一模第1题答案 B；正确项①“不忘初心、方得始终，坚持党的全面领导确保中国式现代化行稳致远”。",
    }
]


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def module_status(module: str) -> str:
    return "included" if module in {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"} else "module-boundary-excluded"


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    by_key = {(row["suite_id"], row["question"]): row for row in rows}

    missing = [key for key in ROW_RESOLUTIONS if key not in by_key]
    missing += [(item["suite_id"], item["parent_question"]) for item in NEW_COMPONENTS if (item["suite_id"], item["parent_question"]) not in by_key]
    if missing:
        raise SystemExit(f"missing required rows: {sorted(set(missing))}")

    out_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []

    for row in rows:
        key = (row["suite_id"], row["question"])
        if key in ROW_RESOLUTIONS:
            original = dict(row)
            resolution = ROW_RESOLUTIONS[key]
            status = module_status(resolution["module"])
            row = dict(row)
            row.update(
                {
                    "book_module": resolution["module"],
                    "source_types": resolution["source_type"],
                    "evidence_source": resolution["source"],
                    "status": status,
                    "artifact_location": str(OUT_AUDIT.relative_to(RUN_DIR)),
                    "decision_reason": json.dumps(
                        {
                            "rule_id": resolution["rule_id"],
                            "matched_terms": resolution["matched_terms"],
                            "basis": resolution["basis"],
                            "source": OUT_AUDIT.name,
                            "prior_book_module": original.get("book_module", ""),
                            "prior_status": original.get("status", ""),
                        },
                        ensure_ascii=False,
                    ),
                    "next_action": "future_baodian_intake" if status == "included" else "exclude_from_three_target_lines",
                    "integration_status": "final_answer_key_closure",
                }
            )
            audit_rows.append(
                {
                    "suite_id": key[0],
                    "question": key[1],
                    "operation": "resolve_blocked_parent_with_answer_key",
                    "prior_book_module": original.get("book_module", ""),
                    "prior_status": original.get("status", ""),
                    "new_book_module": resolution["module"],
                    "new_status": status,
                    "rule_id": resolution["rule_id"],
                    "matched_terms": resolution["matched_terms"],
                    "basis": resolution["basis"],
                    "evidence_source_type": resolution["source_type"],
                    "evidence_source": resolution["source"],
                    "evidence_text": resolution["evidence_text"],
                }
            )
        out_rows.append(row)

    existing_keys = {(row["suite_id"], row["question"]) for row in out_rows}
    component_audit_rows: list[dict[str, str]] = []
    for component in NEW_COMPONENTS:
        key = (component["suite_id"], component["component_question"])
        if key in existing_keys:
            continue
        parent = by_key[(component["suite_id"], component["parent_question"])]
        row = {field: "" for field in fields}
        row.update(parent)
        row.update(
            {
                "question": component["component_question"],
                "parent_question": component["parent_question"],
                "row_granularity": "target_component",
                "book_module": component["module"],
                "source_types": component["source_type"],
                "evidence_source": component["source"],
                "status": "included",
                "artifact_location": str(OUT_COMPONENT_AUDIT.relative_to(RUN_DIR)),
                "decision_reason": json.dumps(
                    {
                        "rule_id": component["rule_id"],
                        "matched_terms": component["matched_terms"],
                        "basis": component["basis"],
                        "source": OUT_COMPONENT_AUDIT.name,
                        "user_rule": "客观题有可靠答案键后，正确项中的目标模块必须抽成组件；题目和细则中的文化部分仍单独抽离。",
                    },
                    ensure_ascii=False,
                ),
                "next_action": "future_baodian_intake_target_component",
                "integration_status": "final_answer_key_component_extraction",
            }
        )
        out_rows.append(row)
        existing_keys.add(key)
        component_audit_rows.append(
            {
                "suite_id": component["suite_id"],
                "parent_question": component["parent_question"],
                "component_question": component["component_question"],
                "question_type": parent.get("question_type", ""),
                "book_module": component["module"],
                "status": "included",
                "rule_id": component["rule_id"],
                "matched_terms": component["matched_terms"],
                "basis": component["basis"],
                "evidence_source_type": component["source_type"],
                "evidence_source": component["source"],
                "evidence_text": component["evidence_text"],
            }
        )

    key_counts = Counter((row["suite_id"], row["question"]) for row in out_rows)
    duplicates = [key for key, count in key_counts.items() if count > 1]
    if duplicates:
        raise SystemExit(f"duplicate matrix keys: {duplicates[:20]}")

    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(
        OUT_AUDIT,
        audit_rows,
        [
            "suite_id",
            "question",
            "operation",
            "prior_book_module",
            "prior_status",
            "new_book_module",
            "new_status",
            "rule_id",
            "matched_terms",
            "basis",
            "evidence_source_type",
            "evidence_source",
            "evidence_text",
        ],
    )
    write_csv(
        OUT_COMPONENT_AUDIT,
        component_audit_rows,
        [
            "suite_id",
            "parent_question",
            "component_question",
            "question_type",
            "book_module",
            "status",
            "rule_id",
            "matched_terms",
            "basis",
            "evidence_source_type",
            "evidence_source",
            "evidence_text",
        ],
    )

    blocked = [row for row in out_rows if row.get("status") == "blocked"]
    write_csv(OUT_BLOCKED, blocked, fields)

    status_counts = Counter(row["status"] for row in out_rows)
    module_counts = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    granularity_counts = Counter(row["row_granularity"] for row in out_rows)
    blank_evidence = sum(1 for row in audit_rows + component_audit_rows if not row.get("evidence_text"))

    OUT_REPORT.write_text(
        "\n".join(
            [
                "# Final Answer Key Closure Report",
                "",
                f"- input_matrix: `{IN_MATRIX.relative_to(RUN_DIR)}`",
                f"- output_matrix: `{OUT_MATRIX.relative_to(RUN_DIR)}`",
                f"- output_coverage: `{OUT_COVERAGE.relative_to(RUN_DIR)}`",
                f"- blocked parent rows resolved with answer keys: {len(audit_rows)}",
                f"- target component rows added: {len(component_audit_rows)}",
                f"- output rows: {len(out_rows)}",
                "- status counts: " + "; ".join(f"{k} {v}" for k, v in status_counts.most_common()),
                f"- target included counts: B2_ECONOMICS {module_counts['B2_ECONOMICS']}; B3_POLITICS_RULE_OF_LAW {module_counts['B3_POLITICS_RULE_OF_LAW']}; B4_CULTURE {module_counts['B4_CULTURE']}",
                "- row granularity counts: " + "; ".join(f"{k} {v}" for k, v in granularity_counts.most_common()),
                f"- duplicate matrix keys: {len(duplicates)}",
                f"- audit blank evidence rows: {blank_evidence}",
                "",
                "## Closed Rows",
                "",
                "- `2026_丰台_一模 Q1`: answer B; B3 party-leadership component added; parent remainder closed as B1 boundary.",
                "- `2026_丰台_期末 Q2`: answer C; existing culture component retained; parent remainder closed as B4 philosophy boundary.",
                "- `2026_丰台_期末 Q6`: answer A; existing culture component retained; parent remainder closed as XB3 boundary.",
                "",
                "## Remaining Blocked",
                "",
                f"- blocked rows: {len(blocked)}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(OUT_REPORT)
    print(f"rows={len(out_rows)} blocked={len(blocked)} components_added={len(component_audit_rows)} blank_evidence={blank_evidence}")
    print("status", dict(status_counts))
    print("targets", {k: module_counts[k] for k in ["B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"]})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
