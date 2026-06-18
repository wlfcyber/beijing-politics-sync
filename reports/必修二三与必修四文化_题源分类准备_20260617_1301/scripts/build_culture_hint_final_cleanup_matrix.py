#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "suite_identity_culture_repaired_classification_matrix.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "culture_hint_final_cleanup_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "CULTURE_HINT_FINAL_CLEANUP_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "culture_hint_final_cleanup_audit.csv"
OUT_COMPONENT_AUDIT = RUN_DIR / "05_reports" / "culture_hint_final_component_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "culture_hint_final_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "culture_hint_final_cleanup_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}

TEXTS = {
    "2025_yanqing_answer": RUN_DIR / "02_text_cache" / "texts" / "c0a3990e95796ddd.txt",
    "2025_haidian_yimo_paper": RUN_DIR / "02_text_cache" / "texts" / "7ebce670784d805e.txt",
    "2025_shijingshan_yimo_paper": RUN_DIR / "02_text_cache" / "texts" / "fb8717be46dabe77.txt",
    "2025_xicheng_yimo_paper": RUN_DIR / "02_text_cache" / "texts" / "2542f29bb04e2ae0.txt",
    "2025_xicheng_ermo_paper": RUN_DIR / "02_text_cache" / "texts" / "06c08602a2f5c20b.txt",
    "2025_haidian_ermo_review": RUN_DIR / "02_text_cache" / "texts" / "086cafc0d843cdfd.txt",
    "2025_haidian_ermo_rubric": RUN_DIR / "02_text_cache" / "texts" / "fc56fdd304fde118.txt",
    "2026_dongcheng_yimo_paper": RUN_DIR / "02_text_cache" / "texts" / "0dafc181e82eb031.txt",
    "2026_chaoyang_yimo_paper": RUN_DIR / "02_text_cache" / "texts" / "585b15124610aff7.txt",
    "2026_fengtai_yimo_paper_ocr": RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_一模.txt",
    "2026_fengtai_yimo_rubric": RUN_DIR / "02_text_cache" / "texts" / "26649804f1de31f5.txt",
    "2026_fengtai_qimo_paper_ocr": RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_丰台_期末.txt",
    "2026_fengtai_qimo_rubric": RUN_DIR / "02_text_cache" / "texts" / "dbc93cbfd3a93eff.txt",
    "2026_haidian_yimo_rubric": RUN_DIR / "02_text_cache" / "texts" / "9b5ac8fd0cfe59cb.txt",
}

ANSWER_EVIDENCE: dict[tuple[str, str], tuple[Path, str]] = {
    ("2025_延庆_一模", "1"): (TEXTS["2025_yanqing_answer"], "题号,答案,第一部分共15题"),
    ("2025_延庆_一模", "8"): (TEXTS["2025_yanqing_answer"], "题号,答案,第一部分共15题"),
    ("2025_海淀_一模", "4"): (TEXTS["2025_haidian_yimo_paper"], "参考答案,第一部分,4.A"),
    ("2025_石景山_一模", "4"): (TEXTS["2025_shijingshan_yimo_paper"], "参考答案,第一部分,4. D"),
    ("2025_西城_一模", "4"): (TEXTS["2025_xicheng_yimo_paper"], "参考答案,第一部分,4.D"),
    ("2025_西城_二模", "3"): (TEXTS["2025_xicheng_ermo_paper"], "参考答案,第一部分,3.A"),
    ("2025_西城_二模", "5"): (TEXTS["2025_xicheng_ermo_paper"], "参考答案,第一部分,5.B"),
    ("2026_东城_一模", "3"): (TEXTS["2026_dongcheng_yimo_paper"], "参考答案,第一部分,答案 B A C"),
    ("2026_东城_一模", "9"): (TEXTS["2026_dongcheng_yimo_paper"], "参考答案,题号 9,答案 D"),
    ("2026_朝阳_一模", "3"): (TEXTS["2026_chaoyang_yimo_paper"], "参考答案,第一部分,答案 B A D"),
    ("2026_海淀_一模", "7"): (TEXTS["2026_haidian_yimo_rubric"], "第一部分,7.D,答案"),
}


ROW_RESOLUTIONS: dict[tuple[str, str], dict[str, str]] = {
    ("2024_顺义_二模", "19(1)"): {
        "module": "B2_ECONOMICS",
        "rule_id": "CULTURE_HINT_B2_FULL_SUBQUESTION_NEW_QUALITY_PRODUCTIVE_FORCES",
        "matched_terms": "社会主义基本经济制度,新质生产力,要素参与收入分配,市场经济体制,国有经济,非公有制经济",
        "basis": "第19(1)问设问明确要求从社会主义基本经济制度角度说明新质生产力跃升，细则均为 B2 经济采分点；原 B2 组件升格为整小问，去掉冗余组件行。",
    },
    ("2024_顺义_二模", "19(2)"): {
        "module": "XB1_EXCLUDED",
        "rule_id": "CULTURE_HINT_PARENT_REMAINDER_XB1_AFTER_B3_COMPONENT",
        "matched_terms": "当代国际政治与经济,国际竞争,国家利益,世界多极化,人类命运共同体",
        "basis": "第19(2)问同时限定《政治与法治》和《当代国际政治与经济》；B3 采分点另抽组件，父题余项按 XB1/综合边界关闭。",
    },
    ("2025_东城_期末", "19(2)"): {
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "CULTURE_HINT_B3_STAKEHOLDER_IDENTIFICATION_COMMUNITY_GOVERNANCE",
        "matched_terms": "街道办事处,消防部门,居民,物业,利益相关方",
        "basis": "第19(2)问要求识别电动自行车治理中的利益相关方，答案给出街道办事处、消防部门等公共治理主体，归入 B3 低密度题源；第19(3)仍保留基层自治组件。",
    },
    ("2025_延庆_一模", "1"): {
        "module": "B1_EXCLUDED",
        "rule_id": "CULTURE_HINT_YANQING_Q1_ANSWER_A_REFORM_B1",
        "matched_terms": "答案A,全面深化改革,中国式现代化,制度环境",
        "basis": "答案键显示第1题为 A；正确项落在进一步全面深化改革与中国式现代化制度环境，非 B2/B3/B4_CULTURE 主链。",
    },
    ("2025_延庆_一模", "8"): {
        "module": "B1_EXCLUDED",
        "rule_id": "CULTURE_HINT_YANQING_Q8_ANSWER_C_PARENT_REMAINDER",
        "matched_terms": "答案C,道路自信,新的伟大斗争",
        "basis": "答案键显示第8题为 C，正确项 2/4 指向道路自信和新的伟大斗争；长征精神文化组件已单独入账，父题余项按 B1 边界关闭。",
    },
    ("2025_海淀_一模", "4"): {
        "module": "B1_EXCLUDED",
        "rule_id": "CULTURE_HINT_HAIDIAN_YIMO_Q4_ANSWER_A_SPORT_EDUCATION",
        "matched_terms": "答案A,民族复兴重任,全面育人理念,体育",
        "basis": "答案键显示第4题为 A，正确项为学生担起民族复兴重任、学校树立全面育人理念；不属于 B2/B3/B4_CULTURE 主链。",
    },
    ("2025_海淀_二模", "16"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_HINT_HAIDIAN_ERMO_Q16_PARENT_REMAINDER_B4P",
        "matched_terms": "联系的观点,认识是主体对客体的能动反映,发展的观点,辩证否定",
        "basis": "第16题评标实录明确文化给分点另抽 B4_CULTURE 组件；父题其余知识为联系、认识、发展等哲学余项。",
    },
    ("2025_石景山_一模", "4"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_HINT_SHIJINGSHAN_Q4_ANSWER_D_B4P",
        "matched_terms": "答案D,实事求是,适度原则,改革",
        "basis": "答案键显示第4题为 D，正确项为实事求是与适度原则，归为哲学边界排除。",
    },
    ("2025_西城_一模", "4"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_HINT_XICHENG_YIMO_Q4_PARENT_REMAINDER_AFTER_B2",
        "matched_terms": "答案D,以人民为中心,投资于人,投资于物",
        "basis": "答案键显示第4题为 D；其中经济发展与民生改善良性循环另抽 B2 组件，父题余项按价值/哲学边界关闭。",
    },
    ("2025_西城_二模", "3"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_HINT_XICHENG_ERMO_Q3_PARENT_REMAINDER_AFTER_B2",
        "matched_terms": "答案A,创新尽责形式,高质量发展,绿色动能",
        "basis": "答案键显示第3题为 A；高质量发展和绿色动能组件已入 B2，父题余项按生态实践/一般实践边界关闭。",
    },
    ("2025_西城_二模", "5"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_HINT_XICHENG_ERMO_Q5_PARENT_REMAINDER_AFTER_B2",
        "matched_terms": "答案B,新农人,农创客,价值追求,乡村全面振兴",
        "basis": "答案键显示第5题为 B；乡村振兴和返乡创业经济组件已入 B2，父题余项为人生价值/青年责任等哲学边界。",
    },
    ("2026_东城_一模", "3"): {
        "module": "XB1_EXCLUDED",
        "rule_id": "CULTURE_HINT_DONGCHENG_YIMO_Q3_ANSWER_C_INTERNATIONAL_EXCHANGE",
        "matched_terms": "答案C,国际交流,首都教育育人成效,对外开放",
        "basis": "答案键显示第3题为 C，正确项指向科技教育国际交流与首都教育育人成效，非 B2/B3/B4_CULTURE 主链。",
    },
    ("2026_东城_一模", "9"): {
        "module": "B1_EXCLUDED",
        "rule_id": "CULTURE_HINT_DONGCHENG_YIMO_Q9_PARENT_REMAINDER_AFTER_B3",
        "matched_terms": "答案D,健康学校建设,现代化国家,学校依法履行管理职责",
        "basis": "答案键显示第9题为 D；依法履责/制度治理组件已入 B3，父题余项为健康学校与现代化国家建设的一般边界内容。",
    },
    ("2026_丰台_一模", "21"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_HINT_FENGTAI_YIMO_Q21_PARENT_REMAINDER_AFTER_COMPONENTS",
        "matched_terms": "识变应变求变,系统思维,辩证思维,对外开放,综合运用所学",
        "basis": "第21题为综合题；B2/B3/B4_CULTURE 目标组件另抽，父题余项含哲学思维方法与选必一开放内容，按边界关闭。",
    },
    ("2026_丰台_期末", "16"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_HINT_FENGTAI_QIMO_Q16_PARENT_REMAINDER_AFTER_CULTURE",
        "matched_terms": "矛盾双方,量变质变,联系的观点,主观能动性",
        "basis": "第16题细则明确哲学与文化两个模块；文化角度另抽 B4_CULTURE 组件，父题余项按哲学边界关闭。",
    },
    ("2026_朝阳_一模", "3"): {
        "module": "B4_PHILOSOPHY_EXCLUDED",
        "rule_id": "CULTURE_HINT_CHAOYANG_Q3_ANSWER_D_PARENT_REMAINDER",
        "matched_terms": "答案D,文化自信,传统文化,科技赋能,辩证否定",
        "basis": "答案键显示第3题为 D；文化自信和传统文化科技赋能组件已入 B4_CULTURE，父题余项按辩证否定等哲学边界关闭。",
    },
    ("2026_海淀_一模", "7"): {
        "module": "B1_EXCLUDED",
        "rule_id": "CULTURE_HINT_HAIDIAN_YIMO_2026_Q7_ANSWER_D_HEALTH_EDUCATION",
        "matched_terms": "答案D,健康第一,学校优化健康教育内容和形式,育人生态",
        "basis": "答案键显示第7题为 D，正确项为健康第一理念与学校育人生态，不属于 B2/B3/B4_CULTURE 主链。",
    },
}

COMPONENTS: list[dict[str, str]] = [
    {
        "suite_id": "2024_顺义_二模",
        "parent_question": "19(2)",
        "component_question": "19(2)#B3_COMPONENT",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "CULTURE_HINT_B3_COMPONENT_NEW_QUALITY_PRODUCTIVE_FORCES_GOVERNMENT",
        "matched_terms": "政治与法治,政府职责,以人民为中心,人民美好生活需要",
        "basis": "第19(2)问明确含《政治与法治》，细则写到“谋划发展新质生产力是政府的职责所在”“以人民为中心的发展理念”等 B3 采分点。",
    },
    {
        "suite_id": "2025_西城_一模",
        "parent_question": "4",
        "component_question": "4#B2_COMPONENT",
        "module": "B2_ECONOMICS",
        "rule_id": "CULTURE_HINT_B2_COMPONENT_INVEST_IN_PEOPLE_AND_THINGS",
        "matched_terms": "投资于人,投资于物,经济发展与民生改善,良性循环",
        "basis": "答案 D 的正确项 4 明确要求将投资于物和投资于人结合，形成经济发展与民生改善良性循环，抽入 B2 组件。",
    },
    {
        "suite_id": "2025_海淀_二模",
        "parent_question": "16",
        "component_question": "16#B4_CULTURE_COMPONENT",
        "module": "B4_CULTURE",
        "rule_id": "CULTURE_HINT_B4C_COMPONENT_MEMORY_CULTURE_FUNCTION",
        "matched_terms": "文化的功能,创造性转化,创新性发展,唐宋八大家",
        "basis": "第16题评标实录明确给出“文化的功能/创造性转化创新性发展（1分）”；题面“唐宋八大家”亦是文化记忆材料。",
    },
    {
        "suite_id": "2026_丰台_一模",
        "parent_question": "21",
        "component_question": "21#B2_COMPONENT",
        "module": "B2_ECONOMICS",
        "rule_id": "CULTURE_HINT_B2_COMPONENT_IDENTIFY_RESPOND_CHANGE_ECONOMY",
        "matched_terms": "高质量发展,统一大市场,未来产业,产业链",
        "basis": "第21题材料与讲评含高质量发展、统一大市场、未来产业等经济内容，抽入 B2 组件。",
    },
    {
        "suite_id": "2026_丰台_一模",
        "parent_question": "21",
        "component_question": "21#B3_COMPONENT",
        "module": "B3_POLITICS_RULE_OF_LAW",
        "rule_id": "CULTURE_HINT_B3_COMPONENT_IDENTIFY_RESPOND_CHANGE_PARTY_LEADERSHIP",
        "matched_terms": "中国共产党领导,党的全面领导,以人民为中心,集中力量办大事",
        "basis": "第21题答案/讲评明确“中国共产党领导是中国特色社会主义的本质特征”等政治与法治采分点，抽入 B3 组件。",
    },
    {
        "suite_id": "2026_丰台_一模",
        "parent_question": "21",
        "component_question": "21#B4_CULTURE_COMPONENT",
        "module": "B4_CULTURE",
        "rule_id": "CULTURE_HINT_B4C_COMPONENT_TRADITIONAL_CULTURE_WISDOM",
        "matched_terms": "中华优秀传统文化,哲学智慧,历史主动精神",
        "basis": "第21题讲评写到“深深根植于中华优秀传统文化的哲学智慧”；按用户提示，综合题中明确文化采分点需单独抽入文化组件。",
    },
    {
        "suite_id": "2026_丰台_期末",
        "parent_question": "16",
        "component_question": "16#B4_CULTURE_COMPONENT",
        "module": "B4_CULTURE",
        "rule_id": "CULTURE_HINT_B4C_COMPONENT_LIUBAI_CHINESE_AESTHETIC_WISDOM",
        "matched_terms": "留白,中华优秀传统文化,美学智慧,审美特质,中华文化",
        "basis": "第16题细则专列文化角度：留白是中华优秀传统文化的美学智慧与审美特质，彰显中华文化独特魅力与精神价值。",
    },
]

REMOVE_KEYS = {("2024_顺义_二模", "19(1)#B2_COMPONENT")}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def compact(text: str, limit: int = 1200) -> str:
    return re.sub(r"\s+", " ", text or "").strip()[:limit]


def text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def window(path: Path, needles: str, limit: int = 1400) -> str:
    body = text(path)
    terms = [term for term in needles.split(",") if term]
    if not body:
        return ""
    best = 0
    best_score = -1
    for term in terms:
        idx = body.find(term)
        if idx >= 0:
            start = max(0, idx - 250)
            chunk = body[start : start + limit]
            score = sum(1 for t in terms if t and t in chunk)
            if score > best_score:
                best_score = score
                best = start
    if best_score < 0:
        return compact(body[:limit], limit)
    return compact(body[best : best + limit], limit)


def candidate_map() -> dict[tuple[str, str], list[dict[str, str]]]:
    by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in load_csv(QUESTION_CANDIDATES):
        by_key[(row["suite_id"], row["question"])].append(row)
    return by_key


def best_candidate(candidates: dict[tuple[str, str], list[dict[str, str]]], suite_id: str, question: str, terms: str) -> tuple[str, str, str]:
    qs = [question]
    if "(" in question:
        qs.append(question.split("(", 1)[0])
    terms_list = [t.strip("《》 ") for t in terms.split(",") if t.strip()]
    scored: list[tuple[int, dict[str, str]]] = []
    for q in qs:
        for row in candidates.get((suite_id, q), []):
            snippet = row.get("snippet", "")
            score = sum(1 for term in terms_list if term and term in snippet)
            if row.get("source_type") in {"paper", "ocr-cache"}:
                score += 2
            elif row.get("source_type") in {"rubric", "reference-answer", "marking-report"}:
                score += 1
            scored.append((score, row))
    if not scored:
        return "", "", ""
    scored.sort(key=lambda item: item[0], reverse=True)
    row = scored[0][1]
    return row.get("source_type", ""), row.get("run_text_path") or row.get("file_path", ""), compact(row.get("snippet", ""))


def evidence_for(suite_id: str, question: str, terms: str, candidates: dict[tuple[str, str], list[dict[str, str]]]) -> tuple[str, str, str]:
    if (suite_id, question) in ANSWER_EVIDENCE:
        answer_path, answer_terms = ANSWER_EVIDENCE[(suite_id, question)]
        source_type, source, q_text = best_candidate(candidates, suite_id, question, terms)
        a_text = window(answer_path, answer_terms, limit=900)
        combined = compact((q_text + " " + a_text).strip(), 1800)
        return "paper+answer_key", f"{source} | {answer_path}", combined

    manual: list[Path] = []
    if suite_id == "2025_延庆_一模":
        manual = [TEXTS["2025_yanqing_answer"]]
    elif suite_id == "2025_海淀_一模":
        manual = [TEXTS["2025_haidian_yimo_paper"]]
    elif suite_id == "2025_石景山_一模":
        manual = [TEXTS["2025_shijingshan_yimo_paper"]]
    elif suite_id == "2025_西城_一模":
        manual = [TEXTS["2025_xicheng_yimo_paper"]]
    elif suite_id == "2025_西城_二模":
        manual = [TEXTS["2025_xicheng_ermo_paper"]]
    elif suite_id == "2025_海淀_二模":
        manual = [TEXTS["2025_haidian_ermo_review"], TEXTS["2025_haidian_ermo_rubric"]]
    elif suite_id == "2026_东城_一模":
        manual = [TEXTS["2026_dongcheng_yimo_paper"]]
    elif suite_id == "2026_朝阳_一模":
        manual = [TEXTS["2026_chaoyang_yimo_paper"]]
    elif suite_id == "2026_丰台_一模":
        manual = [TEXTS["2026_fengtai_yimo_rubric"], TEXTS["2026_fengtai_yimo_paper_ocr"]]
    elif suite_id == "2026_丰台_期末":
        manual = [TEXTS["2026_fengtai_qimo_rubric"], TEXTS["2026_fengtai_qimo_paper_ocr"]]
    elif suite_id == "2026_海淀_一模":
        manual = [TEXTS["2026_haidian_yimo_rubric"]]

    chunks = [(path, window(path, terms)) for path in manual]
    chunks = [(path, chunk) for path, chunk in chunks if chunk]
    if chunks:
        path, chunk = max(chunks, key=lambda item: sum(1 for term in terms.split(",") if term and term in item[1]))
        return "verified_text_cache", str(path), chunk
    return best_candidate(candidates, suite_id, question, terms)


def make_component_row(fields: list[str], parent: dict[str, str], component: dict[str, str], candidates: dict[tuple[str, str], list[dict[str, str]]]) -> tuple[dict[str, str], dict[str, str]]:
    source_type, source, evidence_text = evidence_for(component["suite_id"], component["parent_question"], component["matched_terms"], candidates)
    row = {field: "" for field in fields}
    row.update(parent)
    row.update(
        {
            "question": component["component_question"],
            "parent_question": component["parent_question"],
            "row_granularity": "culture_component" if component["module"] == "B4_CULTURE" else "target_component",
            "book_module": component["module"],
            "question_type": parent.get("question_type", ""),
            "evidence_source": source,
            "source_types": source_type,
            "status": "included",
            "artifact_location": str(OUT_COMPONENT_AUDIT.relative_to(RUN_DIR)),
            "decision_reason": json.dumps(
                {
                    "rule_id": component["rule_id"],
                    "matched_terms": component["matched_terms"],
                    "basis": component["basis"],
                    "source": OUT_COMPONENT_AUDIT.name,
                    "user_rule": "题目和细则中的文化部分必须抽离；民族精神属于文化。",
                },
                ensure_ascii=False,
            ),
            "next_action": "future_baodian_intake_culture_component"
            if component["module"] == "B4_CULTURE"
            else "future_baodian_intake_target_component",
            "integration_status": "culture_hint_final_component_extraction",
        }
    )
    audit = {
        "suite_id": component["suite_id"],
        "parent_question": component["parent_question"],
        "component_question": component["component_question"],
        "question_type": parent.get("question_type", ""),
        "book_module": component["module"],
        "status": "included",
        "rule_id": component["rule_id"],
        "matched_terms": component["matched_terms"],
        "basis": component["basis"],
        "evidence_source_type": source_type,
        "evidence_source": source,
        "evidence_text": evidence_text,
    }
    return row, audit


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    candidates = candidate_map()
    row_by_key = {(row["suite_id"], row["question"]): row for row in rows}

    missing = [key for key in ROW_RESOLUTIONS if key not in row_by_key]
    missing += [(c["suite_id"], c["parent_question"]) for c in COMPONENTS if (c["suite_id"], c["parent_question"]) not in row_by_key]
    if missing:
        raise SystemExit(f"missing required rows: {sorted(set(missing))}")

    out_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    removed_rows: list[dict[str, str]] = []

    for row in rows:
        key = (row["suite_id"], row["question"])
        if key in REMOVE_KEYS:
            removed_rows.append(row)
            continue
        original = dict(row)
        if key in ROW_RESOLUTIONS:
            resolution = ROW_RESOLUTIONS[key]
            module = resolution["module"]
            status = "included" if module in TARGET_MODULES else "module-boundary-excluded"
            source_type, source, evidence_text = evidence_for(key[0], key[1], resolution["matched_terms"], candidates)
            row = dict(row)
            row.update(
                {
                    "book_module": module,
                    "status": status,
                    "evidence_source": source or row.get("evidence_source", ""),
                    "source_types": source_type or row.get("source_types", ""),
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
                    "next_action": "future_baodian_intake"
                    if status == "included"
                    else "exclude_from_three_target_lines",
                    "integration_status": "culture_hint_final_cleanup",
                }
            )
            audit_rows.append(
                {
                    "suite_id": key[0],
                    "question": key[1],
                    "operation": "resolve_original_row",
                    "prior_book_module": original.get("book_module", ""),
                    "prior_status": original.get("status", ""),
                    "new_book_module": module,
                    "new_status": status,
                    "rule_id": resolution["rule_id"],
                    "matched_terms": resolution["matched_terms"],
                    "basis": resolution["basis"],
                    "evidence_source_type": source_type,
                    "evidence_source": source,
                    "evidence_text": evidence_text,
                }
            )
        out_rows.append(row)

    for removed in removed_rows:
        audit_rows.append(
            {
                "suite_id": removed.get("suite_id", ""),
                "question": removed.get("question", ""),
                "operation": "remove_redundant_component",
                "prior_book_module": removed.get("book_module", ""),
                "prior_status": removed.get("status", ""),
                "new_book_module": "",
                "new_status": "superseded",
                "rule_id": "CULTURE_HINT_REMOVE_REDUNDANT_B2_COMPONENT_AFTER_FULL_SUBQUESTION",
                "matched_terms": "19(1)#B2_COMPONENT",
                "basis": "2024 顺义二模 19(1) 已升格为整小问 B2 included，原组件行不再重复计数。",
                "evidence_source_type": removed.get("source_types", ""),
                "evidence_source": removed.get("evidence_source", ""),
                "evidence_text": removed.get("decision_reason", ""),
            }
        )

    existing_keys = {(row["suite_id"], row["question"]) for row in out_rows}
    component_audit_rows: list[dict[str, str]] = []
    for component in COMPONENTS:
        key = (component["suite_id"], component["component_question"])
        if key in existing_keys:
            continue
        parent = row_by_key[(component["suite_id"], component["parent_question"])]
        row, audit = make_component_row(fields, parent, component, candidates)
        out_rows.append(row)
        component_audit_rows.append(audit)
        existing_keys.add(key)

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
                "# Culture Hint Final Cleanup Report",
                "",
                f"- input_matrix: `{IN_MATRIX.relative_to(RUN_DIR)}`",
                f"- output_matrix: `{OUT_MATRIX.relative_to(RUN_DIR)}`",
                f"- output_coverage: `{OUT_COVERAGE.relative_to(RUN_DIR)}`",
                f"- original blocked rows resolved or remainder-closed: {len(ROW_RESOLUTIONS)}",
                f"- redundant component rows removed: {len(removed_rows)}",
                f"- component rows added: {len(component_audit_rows)}",
                f"- output rows: {len(out_rows)}",
                f"- status counts: " + "; ".join(f"{k} {v}" for k, v in status_counts.most_common()),
                f"- target included counts: B2_ECONOMICS {module_counts['B2_ECONOMICS']}; B3_POLITICS_RULE_OF_LAW {module_counts['B3_POLITICS_RULE_OF_LAW']}; B4_CULTURE {module_counts['B4_CULTURE']}",
                f"- row granularity counts: " + "; ".join(f"{k} {v}" for k, v in granularity_counts.most_common()),
                f"- duplicate matrix keys: {len(duplicates)}",
                f"- audit blank evidence rows: {blank_evidence}",
                "",
                "## Still Blocked",
                "",
                "The remaining blocked rows require a reliable answer key or manual choice split before closure:",
                "",
                *[
                    f"- {row['suite_id']} {row['question']}: {row['next_action']}"
                    for row in blocked
                ],
                "",
                "## User Rule Applied",
                "",
                "- Philosophy/culture mixed questions were rechecked against both question text and scoring/rubric text.",
                "- Explicit culture points, including `民族精神` and `中华优秀传统文化`, were extracted as B4_CULTURE components instead of being swallowed by philosophy remainders.",
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
