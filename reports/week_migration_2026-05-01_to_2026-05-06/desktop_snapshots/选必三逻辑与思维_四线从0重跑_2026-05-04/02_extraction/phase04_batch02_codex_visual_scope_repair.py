#!/usr/bin/env python3
"""
Phase04 Batch02 Codex A visual/scope repair.

This script does not claim final fusion. It registers supplemental raw answer
sources reopened for this run, records visually recovered questions, and writes
addendum matrices for Lane B/GPT review.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVERAGE = ROOT / "05_coverage"
CONFLICTS = ROOT / "06_conflicts"
EXTRACTION = ROOT / "02_extraction"

AFTER_B1 = COVERAGE / "phase04_control_base_status_after_laneB_batch01.csv"
VISUAL_PATCH = COVERAGE / "phase04_batch02_codex_visual_scope_repair_addendum.csv"
SUPP_LEDGER = EXTRACTION / "supplemental_answer_sources" / "phase04_batch02_supplemental_source_ledger.csv"
REPORT = CONFLICTS / "phase04_batch02_codex_visual_scope_repair.md"


FIELDS = [
    "target_id",
    "suite",
    "qno",
    "source_locator",
    "question_type",
    "section_scope",
    "codexA_result",
    "evidence_level",
    "visual_status",
    "answer_status",
    "rubric_status",
    "reasoning_or_thinking_node",
    "logical_or_method_form",
    "rule_slogan",
    "trap_or_boundary",
    "can_enter_fusion_before_laneB",
    "can_enter_student_draft",
    "blocker_reason",
    "notes",
]


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def existing_ids() -> set[str]:
    with AFTER_B1.open(newline="", encoding="utf-8") as f:
        return {row["canonical_question_id"] for row in csv.DictReader(f)}


def main() -> None:
    ids = existing_ids()

    supplemental_sources = [
        {
            "supplemental_source_id": "SUPP-2026丰台一模-北京高考在线-有答案",
            "suite": "2026丰台一模",
            "local_pdf": str(
                EXTRACTION
                / "supplemental_answer_sources"
                / "2026北京丰台高三一模政治试题有答案_北京高考在线.pdf"
            ),
            "local_text": str(
                EXTRACTION
                / "supplemental_answer_sources"
                / "2026北京丰台高三一模政治试题有答案_北京高考在线.txt"
            ),
            "source_url": "https://cdn.gaokzx.com/zixunzhan/2026%E5%8C%97%E4%BA%AC%E4%B8%B0%E5%8F%B0%E9%AB%98%E4%B8%89%E4%B8%80%E6%A8%A1%E6%94%BF%E6%B2%BB%E8%AF%95%E9%A2%98%20%E6%9C%89%E7%AD%94%E6%A1%881775093347093.pdf",
            "source_page": "https://www.gaokzx.com/gk/shitiku/154050.html",
            "use_boundary": "raw supplemental answer source reopened for this run; no old conclusions inherited",
        },
        {
            "supplemental_source_id": "SUPP-2025海淀二模-北京高考在线-试题及答案",
            "suite": "2025海淀二模",
            "local_pdf": str(
                EXTRACTION
                / "supplemental_answer_sources"
                / "2025北京海淀高三二模政治试题及答案.pdf"
            ),
            "local_text": str(
                EXTRACTION
                / "supplemental_answer_sources"
                / "2025北京海淀高三二模政治试题及答案.txt"
            ),
            "source_url": "download gated/unknown direct PDF; landing page listed below",
            "source_page": "https://www.gaokzx.com/gk/shitiku/139893.html",
            "use_boundary": "answer table only; question/options still from current run render page_04",
        },
    ]

    rows = [
        {
            "target_id": "Q-2026丰台一模-4",
            "suite": "2026丰台一模",
            "qno": "4",
            "source_locator": "042 render_page_02::Q4; SUPP-2026丰台 answer table page9",
            "question_type": "选择题",
            "section_scope": "思维",
            "codexA_result": "A_VISUAL_RECOVERED_NEEDS_LANEB",
            "evidence_level": "B-choice-signal",
            "visual_status": "VISUAL_CONFIRMED_RENDER_AND_SUPPLEMENTAL_TEXT",
            "answer_status": "answer_confirmed_A_from_supplemental_key",
            "rubric_status": "no_formal_rubric",
            "reasoning_or_thinking_node": "综合思维",
            "logical_or_method_form": "综合思维：功能性与艺术性融为一体",
            "rule_slogan": "材料把多个要素合成一个整体功能，即综合思维",
            "trap_or_boundary": "④把现代研究的最速降线理论倒置成古人迁移使用，不能入选；①是实践智慧边界项，②为选必三核心项",
            "can_enter_fusion_before_laneB": "no",
            "can_enter_student_draft": "no",
            "blocker_reason": "newly recovered from visual suite scan; requires Lane B independent verification",
            "notes": "Original control base had only Q18(2) plus UNPARSED-PAPER for this suite; Q4 must be added to in-scope candidate pool.",
        },
        {
            "target_id": "Q-2026丰台一模-7",
            "suite": "2026丰台一模",
            "qno": "7",
            "source_locator": "042 render_page_02::Q7; SUPP-2026丰台 answer table page9",
            "question_type": "选择题",
            "section_scope": "思维",
            "codexA_result": "A_VISUAL_RECOVERED_NEEDS_LANEB",
            "evidence_level": "B-choice-signal",
            "visual_status": "VISUAL_CONFIRMED_RENDER_AND_SUPPLEMENTAL_TEXT",
            "answer_status": "answer_confirmed_B_from_supplemental_key",
            "rubric_status": "no_formal_rubric",
            "reasoning_or_thinking_node": "发散思维与聚合思维;超前思维;科学思维方法",
            "logical_or_method_form": "发散聚合结合;超前思维",
            "rule_slogan": "多方案诊治先发散再聚合，诊疗预判需超前思维",
            "trap_or_boundary": "②把病症病因必然联系误挂充分条件假言推理；③完全归纳在现实诊断中不可强作唯一保证",
            "can_enter_fusion_before_laneB": "no",
            "can_enter_student_draft": "no",
            "blocker_reason": "newly recovered from visual suite scan; requires Lane B independent verification",
            "notes": "Answer B=①④. This is a direct 思维方法 choice question and must not remain hidden under suite visual blocker.",
        },
        {
            "target_id": "Q-2026丰台一模-8",
            "suite": "2026丰台一模",
            "qno": "8",
            "source_locator": "042 render_page_03::Q8; SUPP-2026丰台 answer table page9",
            "question_type": "选择题",
            "section_scope": "推理",
            "codexA_result": "A_VISUAL_RECOVERED_NEEDS_LANEB",
            "evidence_level": "B-choice-signal",
            "visual_status": "VISUAL_CONFIRMED_RENDER_AND_SUPPLEMENTAL_TEXT",
            "answer_status": "answer_confirmed_C_from_supplemental_key",
            "rubric_status": "no_formal_rubric",
            "reasoning_or_thinking_node": "充分条件假言推理",
            "logical_or_method_form": "P -> Q; 否定后件式有效",
            "rule_slogan": "只要P就Q：否后可否前，否前/肯后不可推",
            "trap_or_boundary": "①否定前件无效；④肯定后件无效；③为官方答案项，需 Lane B 说明其存在量词前提",
            "can_enter_fusion_before_laneB": "no",
            "can_enter_student_draft": "no",
            "blocker_reason": "newly recovered from visual suite scan; answer source is supplemental key; requires Lane B independent verification",
            "notes": "Official supplemental key gives Q8=C=②③. Because ③ has existential presupposition risk, this row especially needs B-line reasoning audit.",
        },
        {
            "target_id": "Q-2026丰台一模-9",
            "suite": "2026丰台一模",
            "qno": "9",
            "source_locator": "042 render_page_03::Q9; SUPP-2026丰台 answer table page9",
            "question_type": "选择题",
            "section_scope": "推理",
            "codexA_result": "A_VISUAL_RECOVERED_NEEDS_LANEB",
            "evidence_level": "B-choice-signal",
            "visual_status": "VISUAL_CONFIRMED_RENDER_AND_SUPPLEMENTAL_TEXT",
            "answer_status": "answer_confirmed_D_from_supplemental_key",
            "rubric_status": "no_formal_rubric",
            "reasoning_or_thinking_node": "概念外延关系;联言判断",
            "logical_or_method_form": "概念关系辨析;联言判断识别",
            "rule_slogan": "外延关系看范围，联言判断看同时断定多个支判断",
            "trap_or_boundary": "A把种属关系误判全同；B把整体与组成部分误作属种；C OCR字形不清，需回图核字",
            "can_enter_fusion_before_laneB": "no",
            "can_enter_student_draft": "no",
            "blocker_reason": "newly recovered from visual suite scan; requires Lane B independent verification",
            "notes": "Answer D. This is a direct formal-logic choice question.",
        },
        {
            "target_id": "Q-2025海淀二模-12",
            "suite": "2025海淀二模",
            "qno": "12",
            "source_locator": "008 render_page_04::Q12; SUPP-2025海淀二模 answer table page9",
            "question_type": "选择题",
            "section_scope": "思维",
            "codexA_result": "A_VISUAL_RECOVERED_ANSWER_FOUND_NEEDS_LANEB",
            "evidence_level": "B-choice-signal",
            "visual_status": "VISUAL_CONFIRMED_RENDER_AND_SUPPLEMENTAL_TEXT",
            "answer_status": "answer_confirmed_D_from_supplemental_key",
            "rubric_status": "no_formal_rubric",
            "reasoning_or_thinking_node": "超前思维;风险收益平衡;长期发展",
            "logical_or_method_form": "超前思维关注长期发展",
            "rule_slogan": "耐心资本看长期、看趋势、看风险收益平衡",
            "trap_or_boundary": "①把耐心资本直接说成新事物生命力过强；②消除矛盾错误；③④构成答案",
            "can_enter_fusion_before_laneB": "no",
            "can_enter_student_draft": "no",
            "blocker_reason": "Codex A found supplemental answer source after Batch01; requires Lane B independent verification before fusion",
            "notes": "This was B-only/blocked because original 008 text layer failed. Full options were visually recovered earlier; answer D is from reopened supplemental answer PDF.",
        },
        {
            "target_id": "Q-2025海淀二模-13",
            "suite": "2025海淀二模",
            "qno": "13",
            "source_locator": "008 render_page_04::Q13; SUPP-2025海淀二模 answer table page9",
            "question_type": "选择题",
            "section_scope": "推理",
            "codexA_result": "A_VISUAL_RECOVERED_ANSWER_FOUND_NEEDS_LANEB",
            "evidence_level": "B-choice-signal",
            "visual_status": "VISUAL_CONFIRMED_RENDER_AND_SUPPLEMENTAL_TEXT",
            "answer_status": "answer_confirmed_C_from_supplemental_key",
            "rubric_status": "no_formal_rubric",
            "reasoning_or_thinking_node": "三段论;概念划分;选言判断",
            "logical_or_method_form": "三段论有效式",
            "rule_slogan": "大前提+小前提+结论，概念项位置不能乱",
            "trap_or_boundary": "A分类混杂；B充分条件过强；D把国际关系三形式作不相容穷尽选言",
            "can_enter_fusion_before_laneB": "no",
            "can_enter_student_draft": "no",
            "blocker_reason": "Codex A found supplemental answer source after Batch01; requires Lane B independent verification before fusion",
            "notes": "Answer C. This row must be added to 推理题型 archive after B-line confirmation.",
        },
    ]

    for row in rows:
        row["already_in_batch01_control_base"] = "yes" if row["target_id"] in ids else "no"

    write_csv(SUPP_LEDGER, supplemental_sources, list(supplemental_sources[0].keys()))
    write_csv(VISUAL_PATCH, rows, FIELDS + ["already_in_batch01_control_base"])

    report_lines = [
        "# Phase04 Batch02 Codex Visual/Scope Repair",
        "",
        "Status: `A_PATCH_READY_FOR_GPT_AND_LANEB_REVIEW`.",
        "",
        "This file is not a student draft and not a final fusion decision.",
        "",
        "## Supplemental Sources Registered",
        "",
    ]
    for source in supplemental_sources:
        report_lines.append(
            f"- `{source['supplemental_source_id']}` | {source['suite']} | {source['use_boundary']} | local_text=`{source['local_text']}`"
        )

    report_lines.extend(
        [
            "",
            "## Addendum Rows",
            "",
            f"- total addendum rows: {len(rows)}",
            f"- rows already in Batch01 control base: {sum(1 for r in rows if r['already_in_batch01_control_base'] == 'yes')}",
            f"- new rows not in Batch01 control base: {sum(1 for r in rows if r['already_in_batch01_control_base'] == 'no')}",
            "",
            "### New Or Repaired In-Scope Rows",
            "",
        ]
    )
    for row in rows:
        report_lines.append(
            f"- `{row['target_id']}` | {row['section_scope']} | {row['answer_status']} | {row['reasoning_or_thinking_node']} | in_batch01={row['already_in_batch01_control_base']}"
        )

    report_lines.extend(
        [
            "",
            "## Critical Notes",
            "",
            "- `2026丰台一模` had been represented in Batch01 only by `Q18(2)` plus a suite-level visual blocker. Visual reading and supplemental answer source show at least `Q4/Q7/Q8/Q9` are selected-compulsory-three relevant and must enter Batch02 B-line verification.",
            "- `2025海淀二模 Q12/Q13` now have both visually recovered options and supplemental answer-table pairing. They remain blocked from fusion until Lane B independently verifies the reopened source and classification.",
            "- No addendum row has `can_enter_fusion_before_laneB=yes`; this is deliberately conservative.",
        ]
    )
    REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"wrote {VISUAL_PATCH}")
    print(f"wrote {SUPP_LEDGER}")
    print(f"wrote {REPORT}")


if __name__ == "__main__":
    main()
