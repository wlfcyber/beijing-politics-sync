#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "twenty_question_structure_accepted_classification_matrix.csv"
GAP_BEFORE = RUN_DIR / "05_reports" / "question_gap_after_twenty_question_structure_review.csv"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "raw_source_inspection_repaired_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "RAW_SOURCE_INSPECTION_REPAIRED_COVERAGE_MATRIX.csv"
OUT_REVIEW = RUN_DIR / "05_reports" / "raw_source_inspection_review.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "raw_source_inspection_repair_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "raw_source_inspection_repaired_blocked_queue.csv"
OUT_GAP_AFTER = RUN_DIR / "05_reports" / "question_gap_after_raw_source_inspection.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "raw_source_inspection_repair_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


REVIEW_DECISIONS = {
    ("2024_西城_一模", "5"): {
        "review_result": "true_top_level_question_original_docx",
        "decision_note": "Original DOCX shows Q5 between Q4 and Q6; prior extraction missed the visible marker.",
        "rows": [
            {
                "question": "5",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B3_POLITICS_RULE_OF_LAW",
                "status": "included",
                "question_type": "objective",
                "next_action": "future_baodian_intake",
                "rule_id": "RAW_SOURCE_REVIEW_B3_JUDICIAL_ORGANS",
                "matched_terms": "司法机关,以事实为根据,以法律为准绳,定分止争,司法救助",
                "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/西城一模/试卷/试卷.docx",
                "source_types": "original_docx_text;raw-source-inspection",
                "evidence_type": "original_docx_text",
                "evidence_text": "法律不是冰冷的，司法工作也是做群众工作。综合上述信息，可以看到司法机关坚持以事实为根据、以法律为准绳，在定分止争中传递司法善意、展现司法担当、促进社会和谐。",
            }
        ],
    },
    ("2024_西城_一模", "20"): {
        "review_result": "accepted_absent_actual_19_question_structure",
        "decision_note": "Original DOCX second part contains Q16-Q19 only; no top-level Q20 marker was found.",
        "rows": [],
        "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/西城一模/试卷/试卷.docx",
        "evidence_type": "original_docx_text",
        "evidence_text": "第二部分 本部分共4题，共55分。Top-level questions end at 19．（31分）; no 20． marker appears before the answer-card notice.",
    },
    ("2024_西城_一模", "21"): {
        "review_result": "accepted_absent_actual_19_question_structure",
        "decision_note": "Original DOCX second part contains Q16-Q19 only; no top-level Q21 marker was found.",
        "rows": [],
        "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/西城一模/试卷/试卷.docx",
        "evidence_type": "original_docx_text",
        "evidence_text": "第二部分 本部分共4题，共55分。Top-level questions end at 19．（31分）; no 21． marker appears before the answer-card notice.",
    },
    ("2024_西城_二模", "15"): {
        "review_result": "true_top_level_question_original_docx",
        "decision_note": "Original DOCX shows Q15 before the second-part heading; prior extraction missed this top-level objective item.",
        "rows": [
            {
                "question": "15",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB3_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "RAW_SOURCE_REVIEW_XB3_ABSTRACTION_ASSOCIATION",
                "matched_terms": "表象,联想,类推,思维抽象",
                "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/西城二模/试卷/试卷.docx",
                "source_types": "original_docx_text;raw-source-inspection",
                "evidence_type": "original_docx_text",
                "evidence_text": "15．一个“间”字，画出一幅场景：两扇门的门缝中有一个月亮。以下分析正确的是：表象是文字发明之源；古人运用联想和类推；思维具体提纯为思维抽象。",
            }
        ],
    },
    ("2024_西城_二模", "20"): {
        "review_result": "accepted_absent_actual_19_question_structure",
        "decision_note": "Original DOCX second part says four questions and lists Q16-Q19 only.",
        "rows": [],
        "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/西城二模/试卷/试卷.docx",
        "evidence_type": "original_docx_text",
        "evidence_text": "第二部分 本部分共4题，共55分。Top-level subjective questions are 16．, 17．, 18．, 19．; no 20． marker appears.",
    },
    ("2024_西城_二模", "21"): {
        "review_result": "accepted_absent_actual_19_question_structure",
        "decision_note": "Original DOCX second part says four questions and lists Q16-Q19 only.",
        "rows": [],
        "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/西城二模/试卷/试卷.docx",
        "evidence_type": "original_docx_text",
        "evidence_text": "第二部分 本部分共4题，共55分。Top-level subjective questions are 16．, 17．, 18．, 19．; no 21． marker appears.",
    },
    ("2024_顺义_二模", "9"): {
        "review_result": "true_top_level_question_hidden_number_original_docx",
        "decision_note": "Original DOCX places this State Secrets Law objective item between Q8 and Q10; the leading number was lost in extraction.",
        "rows": [
            {
                "question": "9",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B3_POLITICS_RULE_OF_LAW",
                "status": "included",
                "question_type": "objective",
                "next_action": "future_baodian_intake",
                "rule_id": "RAW_SOURCE_REVIEW_B3_STATE_SECRETS_LAW",
                "matched_terms": "保守国家秘密法,党的领导,总体国家安全观,法律保障",
                "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/顺义思政二模/试卷/试卷.docx",
                "source_types": "original_docx_text;raw-source-inspection",
                "evidence_type": "original_docx_text",
                "evidence_text": "新修订的《中华人民共和国保守国家秘密法》自2024年5月1日起施行。条文涉及坚持中国共产党对保守国家秘密工作的领导、保密科技研究和总体国家安全观相关判断。",
            }
        ],
    },
    ("2024_顺义_二模", "14"): {
        "review_result": "true_top_level_question_hidden_number_original_docx",
        "decision_note": "Original DOCX places this BRICS objective item between Q13 and Q15; the leading number was lost in extraction.",
        "rows": [
            {
                "question": "14",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB1_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "RAW_SOURCE_REVIEW_XB1_BRICS_GLOBAL_GOVERNANCE",
                "matched_terms": "金砖国家,国家利益,全球治理,国际组织",
                "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/顺义思政二模/试卷/试卷.docx",
                "source_types": "original_docx_text;raw-source-inspection",
                "evidence_type": "original_docx_text",
                "evidence_text": "金砖国家是新兴市场与发展中国家间的合作机制，金砖合作机制走过18年的历程，越来越多志同道合的伙伴参与其中。下列说法正确的是：国家利益、全球治理、国际组织等判断。",
            }
        ],
    },
    ("2024_顺义_二模", "21"): {
        "review_result": "accepted_absent_actual_20_question_structure",
        "decision_note": "After the already accepted hidden Q20 span, original DOCX has no reliable top-level Q21 marker.",
        "rows": [],
        "evidence_source": "/Users/wanglifei/Desktop/2024模拟题/顺义思政二模/试卷/试卷.docx",
        "evidence_type": "original_docx_text",
        "evidence_text": "Original-paper review previously accepted hidden Q20; no top-level Q21 marker appears after the Q20 span.",
    },
    ("2026_丰台_一模", "5"): {
        "review_result": "true_top_level_question_ocr_marker",
        "decision_note": "OCR page context shows a top-level marker rendered as 、5. before the quantum communication item.",
        "rows": [
            {
                "question": "5",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B4_PHILOSOPHY_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "RAW_SOURCE_REVIEW_B4_PHILOSOPHY_QUANTUM_COMMUNICATION",
                "matched_terms": "具体联系,认识,实践,意识具有直接现实性",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_一模.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "、5.量子通信是怎么实现“加密”的？量子通信的核心技术是量子密钥分发。选项涉及新的具体联系、认识深化、客观条件、意识具有直接现实性。",
            }
        ],
    },
    ("2026_丰台_一模", "9"): {
        "review_result": "true_top_level_question_ocr_marker",
        "decision_note": "OCR page context shows a top-level Q9 marker before the lantern-riddle logic item.",
        "rows": [
            {
                "question": "9",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB3_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "RAW_SOURCE_REVIEW_XB3_EXTENSION_RELATION",
                "matched_terms": "外延,属种关系,联言判断",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_一模.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "9. 元宵节猜灯谜题，围绕谜面、谜目和谜底设置判断，选项涉及外延、属种关系和联言判断。",
            }
        ],
    },
    ("2026_丰台_二模", "15"): {
        "review_result": "true_top_level_question_ocr_i_marker",
        "decision_note": "OCR rendered the top-level Q15 marker as I5.; the full objective item is visible after Q14.",
        "rows": [
            {
                "question": "15",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB1_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "RAW_SOURCE_REVIEW_XB1_GLOBAL_TRADE",
                "matched_terms": "全球货物贸易,国际竞争,绿色产品,贸易强国",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_二模.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "I5.2025年我国继续保持全球货物贸易第一大国地位，其中的含“新”量、含“绿”量和含“智”量不断提升。选项涉及国际竞争、货物贸易、绿色产品、贸易强国。",
            }
        ],
    },
    ("2026_丰台_期末", "2"): {
        "review_result": "true_top_level_question_mixed_keep_blocked",
        "decision_note": "OCR page context shows the Q2 objective item, but answer/module split is mixed between governance/public service and traditional virtue culture.",
        "rows": [
            {
                "question": "2",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "UNKNOWN_OR_MIXED",
                "status": "blocked",
                "question_type": "objective",
                "next_action": "manual_choice_module_split_or_answer_key_needed",
                "rule_id": "RAW_SOURCE_REVIEW_MIXED_B3_B4_CULTURE_ELDERLY_SERVICES",
                "matched_terms": "基本公共服务,群众观点,孝亲敬老,社会治理",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_期末.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "加装智能呼叫设备、手机培训班、养老驿站等适老化改造。选项同时涉及差异化基本公共服务、群众观点、孝亲敬老传统美德和社会治理方式。",
            }
        ],
    },
    ("2026_丰台_期末", "6"): {
        "review_result": "true_top_level_question_mixed_keep_blocked",
        "decision_note": "OCR page context now locates the Q6 span, but the item mixes B4 culture and XB3 thinking-method options.",
        "rows": [
            {
                "question": "6",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "UNKNOWN_OR_MIXED",
                "status": "blocked",
                "question_type": "objective",
                "next_action": "manual_choice_module_split_or_answer_key_needed",
                "rule_id": "RAW_SOURCE_REVIEW_MIXED_B4_CULTURE_XB3_CHINESE_KNOT",
                "matched_terms": "中华优秀传统文化,精神追求,形象思维,抽象思维",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_期末.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "〕.中国结是我国传统的手工艺品，造型独特、色彩多样、内涵丰富。选项同时涉及中华优秀传统文化、民族精神支柱、形象思维和抽象思维。",
            }
        ],
    },
    ("2026_丰台_期末", "7"): {
        "review_result": "true_top_level_question_ocr_marker",
        "decision_note": "OCR page context shows Q7 after the Chinese-knot item and before Q8.",
        "rows": [
            {
                "question": "7",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B3_POLITICS_RULE_OF_LAW",
                "status": "included",
                "question_type": "objective",
                "next_action": "future_baodian_intake",
                "rule_id": "RAW_SOURCE_REVIEW_B3_LOCAL_LEGISLATION",
                "matched_terms": "森林法,北京市人大常委会,地方立法权,法治化",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_期末.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "7为实施好《中华人民共和国森林法》...北京市第十六届人民代表大会常务委员会审议通过《北京市实施〈中华人民共和国森林法〉办法》。选项涉及地方立法权、制度化法治化。",
            }
        ],
    },
    ("2026_丰台_期末", "12"): {
        "review_result": "true_top_level_question_hidden_number_ocr",
        "decision_note": "OCR page context places this industrial-coordination objective item between Q11 and Q13; the leading number was lost.",
        "rows": [
            {
                "question": "12",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B2_ECONOMICS",
                "status": "included",
                "question_type": "objective",
                "next_action": "future_baodian_intake",
                "rule_id": "RAW_SOURCE_REVIEW_B2_JJJ_INDUSTRIAL_CHAIN",
                "matched_terms": "京津冀产业协同,产业链供应链,区域产业布局,科技创新",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_期末.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "京津冀产业协同正在加快“集链成群”。“共绘一张图”“共建一批园”“共造一辆车”。选项涉及产业链供应链、区域产业布局、科技创新和物流成本。",
            }
        ],
    },
    ("2026_房山_一模", "5"): {
        "review_result": "true_top_level_question_ocr_s_marker",
        "decision_note": "OCR rendered Q5 as S.; full item is visible after Q4 and before Q6.",
        "rows": [
            {
                "question": "5",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB3_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "RAW_SOURCE_REVIEW_XB3_FORMAL_LOGIC_ALL_GAMES",
                "matched_terms": "思维运行方式,三段论,矛盾关系,矛盾律",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_房山_一模.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "S.第十五届全运会，是粤港澳三地首次联合承办的大型体育赛事。选项涉及思维运行方式、三段论、矛盾关系和矛盾律。",
            }
        ],
    },
    ("2026_房山_一模", "8"): {
        "review_result": "true_top_level_question_hidden_number_ocr",
        "decision_note": "OCR page context shows the item between Q7 and Q9; the leading Q8 marker was lost.",
        "rows": [
            {
                "question": "8",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B3_POLITICS_RULE_OF_LAW",
                "status": "included",
                "question_type": "objective",
                "next_action": "future_baodian_intake",
                "rule_id": "RAW_SOURCE_REVIEW_B3_PARTY_ROOT_PURPOSE",
                "matched_terms": "党员干部,根本宗旨,为民造福,依法执政",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_房山_一模.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "“吃水不忘挖井人”的故事，讲述毛泽东发现群众饮水困难，带领干部群众挖井。选项包括党员干部要践行根本宗旨、传承红色文化基因、坚定马克思主义信仰、依法执政。",
            }
        ],
    },
    ("2026_房山_一模", "21"): {
        "review_result": "accepted_absent_actual_20_question_structure",
        "decision_note": "OCR shows second part has five questions and top-level Q16-Q20 only; no Q21 span appears before the answer-card notice.",
        "rows": [],
        "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_房山_一模.txt"),
        "evidence_type": "ocr_page_context",
        "evidence_text": "本部分共5题，共55分。OCR line review shows Q16, Q17, Q18, Q19 and 20.(10分), followed by the answer-card notice; no top-level Q21 appears.",
    },
    ("2026_西城_一模", "12"): {
        "review_result": "true_top_level_question_original_docx",
        "decision_note": "Original DOCX shows Q12 '读数看经济' before Q13.",
        "rows": [
            {
                "question": "12",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "B2_ECONOMICS",
                "status": "included",
                "question_type": "objective",
                "next_action": "future_baodian_intake",
                "rule_id": "RAW_SOURCE_REVIEW_B2_DEMAND_GDP_GROWTH",
                "matched_terms": "GDP增长,消费,投资,出口,三大需求",
                "evidence_source": "/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026西城一模/试卷/试卷.docx",
                "source_types": "original_docx_text;raw-source-inspection",
                "evidence_type": "original_docx_text",
                "evidence_text": "12．读数看经济。题面呈现2016-2025年我国三大需求对国内生产总值增长的贡献率和拉动变化，选项围绕消费、投资、出口判断。",
            }
        ],
    },
    ("2026_西城_一模", "14"): {
        "review_result": "true_top_level_question_original_docx",
        "decision_note": "Original DOCX shows Q14 as a logic-judgment item about Beijing Central Axis heritage information.",
        "rows": [
            {
                "question": "14",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB3_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "RAW_SOURCE_REVIEW_XB3_QUANTIFIER_JUDGMENT",
                "matched_terms": "判断必然为真,有些,所有,逻辑判断",
                "evidence_source": "/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026西城一模/试卷/试卷.docx",
                "source_types": "original_docx_text;raw-source-inspection",
                "evidence_type": "original_docx_text",
                "evidence_text": "14．北京中轴线是中华文明规范理念的杰出范例。根据《北京中轴线文化遗产保护条例》获得若干信息，要求判断“下列判断必然为真的是”，选项为“有些/所有”等量项判断。",
            }
        ],
    },
    ("2026_西城_期末", "9"): {
        "review_result": "true_top_level_question_ocr_marker",
        "decision_note": "OCR page context shows a top-level marker rendered as 9: before the digital-technology syllogism item.",
        "rows": [
            {
                "question": "9",
                "parent_question": "",
                "row_granularity": "question",
                "book_module": "XB3_EXCLUDED",
                "status": "module-boundary-excluded",
                "question_type": "objective",
                "next_action": "exclude_from_three_target_lines",
                "rule_id": "RAW_SOURCE_REVIEW_XB3_SYLLOGISM",
                "matched_terms": "判断,三段论推理,大前提,小前提,结论",
                "evidence_source": str(RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_西城_期末.txt"),
                "source_types": "ocr_page_context;raw-source-inspection",
                "evidence_type": "ocr_page_context",
                "evidence_text": "9:数字技术是驱动发展方式变革的关键力量。有同学作出四个判断，要求选取三个依次作为大前提、小前提、结论，形成一个三段论推理。",
            }
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


def compact(text: str, limit: int = 1000) -> str:
    return re.sub(r"\s+", " ", text or "").strip()[:limit]


def split_missing(text: str) -> list[str]:
    return [item.strip() for item in re.split(r"[;\s]+", text or "") if item.strip()]


def main() -> int:
    matrix_rows = load_csv(IN_MATRIX)
    fields = list(matrix_rows[0].keys())
    existing = {(row["suite_id"], row["question"]) for row in matrix_rows}

    prior_gaps = {
        row["suite_id"]: split_missing(row.get("missing_after_twenty_question_structure_review", ""))
        for row in load_csv(GAP_BEFORE)
    }
    expected = {(suite_id, q) for suite_id, questions in prior_gaps.items() for q in questions}
    decisions = set(REVIEW_DECISIONS)
    if expected != decisions:
        missing = sorted(expected - decisions)
        extra = sorted(decisions - expected)
        raise SystemExit(f"review decisions do not match remaining gaps; missing={missing}; extra={extra}")

    review_fields = [
        "suite_id",
        "missing_question",
        "review_result",
        "added_matrix_rows",
        "resolved_gap",
        "evidence_type",
        "evidence_source",
        "evidence_text",
        "decision_note",
    ]
    audit_fields = [
        "suite_id",
        "question",
        "new_book_module",
        "new_status",
        "row_granularity",
        "question_type",
        "rule_id",
        "matched_terms",
        "evidence_type",
        "evidence_source",
        "evidence_text",
    ]

    review_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    added_rows: list[dict[str, str]] = []
    resolved: set[tuple[str, str]] = set()
    absent_structure_resolved: set[tuple[str, str]] = set()

    for key in sorted(REVIEW_DECISIONS):
        suite_id, missing_question = key
        decision = REVIEW_DECISIONS[key]
        decision_rows = decision.get("rows", [])
        evidence_source = decision.get("evidence_source", "")
        evidence_type = decision.get("evidence_type", "")
        evidence_text = decision.get("evidence_text", "")
        if decision_rows:
            evidence_source = decision_rows[0]["evidence_source"]
            evidence_type = decision_rows[0]["evidence_type"]
            evidence_text = " | ".join(row["evidence_text"] for row in decision_rows)
        else:
            absent_structure_resolved.add(key)

        review_rows.append(
            {
                "suite_id": suite_id,
                "missing_question": missing_question,
                "review_result": decision["review_result"],
                "added_matrix_rows": str(len(decision_rows)),
                "resolved_gap": "yes",
                "evidence_type": evidence_type,
                "evidence_source": evidence_source,
                "evidence_text": compact(evidence_text, 1400),
                "decision_note": decision["decision_note"],
            }
        )
        resolved.add(key)

        for decision_row in decision_rows:
            new_key = (suite_id, decision_row["question"])
            if new_key in existing:
                raise SystemExit(f"refusing duplicate matrix key {new_key}")
            year, district, stage = parse_suite(suite_id)
            new = {field: "" for field in fields}
            new.update(
                {
                    "suite_id": suite_id,
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
                    "artifact_location": "05_reports/raw_source_inspection_repair_audit.csv",
                    "decision_reason": json.dumps(
                        {
                            "rule_id": decision_row["rule_id"],
                            "matched_terms": decision_row["matched_terms"],
                            "source": "raw_source_inspection_review.csv",
                            "evidence_type": decision_row["evidence_type"],
                            "parent_missing_question": missing_question,
                        },
                        ensure_ascii=False,
                    ),
                    "next_action": decision_row["next_action"],
                    "integration_status": "raw_source_inspection_repair",
                }
            )
            added_rows.append(new)
            audit_rows.append(
                {
                    "suite_id": suite_id,
                    "question": decision_row["question"],
                    "new_book_module": decision_row["book_module"],
                    "new_status": decision_row["status"],
                    "row_granularity": decision_row["row_granularity"],
                    "question_type": decision_row["question_type"],
                    "rule_id": decision_row["rule_id"],
                    "matched_terms": decision_row["matched_terms"],
                    "evidence_type": decision_row["evidence_type"],
                    "evidence_source": decision_row["evidence_source"],
                    "evidence_text": compact(decision_row["evidence_text"], 1400),
                }
            )

    out_rows = matrix_rows + added_rows
    gap_rows = []
    prior_missing_count = 0
    remaining_missing_count = 0
    for suite_id in sorted(prior_gaps):
        before = prior_gaps[suite_id]
        prior_missing_count += len(before)
        resolved_here = [q for q in before if (suite_id, q) in resolved]
        absent_here = [q for q in resolved_here if (suite_id, q) in absent_structure_resolved]
        added_here = [q for q in resolved_here if (suite_id, q) not in absent_structure_resolved]
        after = [q for q in before if (suite_id, q) not in resolved]
        remaining_missing_count += len(after)
        gap_rows.append(
            {
                "suite_id": suite_id,
                "missing_after_raw_source_inspection": ";".join(after),
                "resolved_by_raw_source_inspection": ";".join(resolved_here),
                "matrix_rows_added_for_questions": ";".join(added_here),
                "accepted_absent_structure_questions": ";".join(absent_here),
                "unresolved_reason": "" if not after else "raw_source_inspection_unresolved",
            }
        )

    write_csv(OUT_REVIEW, review_rows, review_fields)
    write_csv(OUT_AUDIT, audit_rows, audit_fields)
    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(OUT_BLOCKED, [row for row in out_rows if row["status"] == "blocked"], fields)
    write_csv(
        OUT_GAP_AFTER,
        gap_rows,
        [
            "suite_id",
            "missing_after_raw_source_inspection",
            "resolved_by_raw_source_inspection",
            "matrix_rows_added_for_questions",
            "accepted_absent_structure_questions",
            "unresolved_reason",
        ],
    )

    status_counts = Counter(row["status"] for row in out_rows)
    included_modules = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    duplicate_keys = len(out_rows) - len({(row["suite_id"], row["question"]) for row in out_rows})
    blocked_count = sum(1 for row in out_rows if row["status"] == "blocked")
    excluded_count = sum(1 for row in out_rows if row["status"] == "module-boundary-excluded")
    included_count = sum(1 for row in out_rows if row["status"] == "included")
    reference_count = sum(1 for row in out_rows if row["status"] == "reference-only")

    report = f"""# Raw Source Inspection Repair Report

Generated from `{IN_MATRIX.name}`.

## Scope

- Reviewed remaining missing-question entries: {len(review_rows)}
- Added matrix rows: {len(added_rows)}
- Accepted absent-structure gap entries: {len(absent_structure_resolved)}
- Remaining missing-question entries: {remaining_missing_count}

## Matrix Counts

- Rows: {len(out_rows)}
- Status counts: {dict(status_counts)}
- Included module counts: {dict(included_modules)}
- Included rows: {included_count}
- Module-boundary-excluded rows: {excluded_count}
- Blocked rows: {blocked_count}
- Reference-only rows: {reference_count}
- Duplicate `(suite_id, question)` keys: {duplicate_keys}

## Decisions

- `2024_西城_一模`: Q5 added as `B3_POLITICS_RULE_OF_LAW`; Q20/Q21 accepted absent because the paper ends at Q19.
- `2024_西城_二模`: Q15 added as `XB3_EXCLUDED`; Q20/Q21 accepted absent because the paper ends at Q19.
- `2024_顺义_二模`: Q9 added as `B3_POLITICS_RULE_OF_LAW`; Q14 added as `XB1_EXCLUDED`; Q21 accepted absent after the already accepted Q20 span.
- `2026_丰台_一模`: Q5 added as `B4_PHILOSOPHY_EXCLUDED`; Q9 added as `XB3_EXCLUDED`.
- `2026_丰台_二模`: Q15 added as `XB1_EXCLUDED`.
- `2026_丰台_期末`: Q2 and Q6 added as `UNKNOWN_OR_MIXED` blocked rows; Q7 added as `B3_POLITICS_RULE_OF_LAW`; Q12 added as `B2_ECONOMICS`.
- `2026_房山_一模`: Q5 added as `XB3_EXCLUDED`; Q8 added as `B3_POLITICS_RULE_OF_LAW`; Q21 accepted absent because the paper ends at Q20.
- `2026_西城_一模`: Q12 added as `B2_ECONOMICS`; Q14 added as `XB3_EXCLUDED`.
- `2026_西城_期末`: Q9 added as `XB3_EXCLUDED`.

## Note

This closes the visible question-number gap ledger but does not close the run: two newly found questions remain blocked as mixed objective items, and the whole matrix still has {blocked_count} blocked rows.

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
