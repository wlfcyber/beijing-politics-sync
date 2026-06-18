#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
IN_MATRIX = RUN_DIR / "04_module_classification" / "source_explicit_cleanup_classification_matrix.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
TEXT_DIR = RUN_DIR / "02_text_cache" / "texts"

OUT_MATRIX = RUN_DIR / "04_module_classification" / "suite_identity_culture_repaired_classification_matrix.csv"
OUT_COVERAGE = RUN_DIR / "00_control" / "SUITE_IDENTITY_CULTURE_REPAIRED_COVERAGE_MATRIX.csv"
OUT_AUDIT = RUN_DIR / "05_reports" / "suite_identity_culture_repair_audit.csv"
OUT_BLOCKED = RUN_DIR / "05_reports" / "suite_identity_culture_repaired_blocked_queue.csv"
OUT_REPORT = RUN_DIR / "05_reports" / "suite_identity_culture_repair_report.md"

TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}

SOURCE_SUITE = "2025_海淀_期末"
MIDTERM_SUITE = "2025_海淀_期中"
FINAL_SUITE = "2025_海淀_期末"

MIDTERM_PAPER_NEEDLE = "2025海淀期中/试卷"
MIDTERM_RUBRIC_NEEDLE = "2025海淀期中/细则"
FINAL_PAPER_NEEDLE = "2025海淀期末/试卷"
FINAL_RUBRIC_NEEDLE = "2025海淀期末/细则"


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


def load_candidates() -> list[dict[str, str]]:
    return load_csv(QUESTION_CANDIDATES)


def path_for(candidates: list[dict[str, str]], needle: str) -> str:
    for row in candidates:
        if row.get("suite_id") == SOURCE_SUITE and needle in row.get("file_path", ""):
            return row.get("file_path", "")
    return ""


def snippets_for(candidates: list[dict[str, str]], needle: str, question: str) -> list[dict[str, str]]:
    return [
        row
        for row in candidates
        if row.get("suite_id") == SOURCE_SUITE
        and row.get("question") == question
        and needle in row.get("file_path", "")
    ]


def best_snippet(candidates: list[dict[str, str]], needles: list[str], question: str) -> str:
    pieces = []
    for needle in needles:
        rows = snippets_for(candidates, needle, question)
        rows.sort(key=lambda row: 0 if row.get("source_type") == "paper" else 1)
        for row in rows[:2]:
            pieces.append(row.get("snippet", ""))
    return compact(" ".join(pieces), 1400)


def text_slice(path: Path, start: str, end: str | None = None, limit: int = 1800) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    idx = text.find(start)
    if idx < 0:
        return ""
    end_idx = len(text)
    if end:
        found = text.find(end, idx + len(start))
        if found > idx:
            end_idx = found
    return compact(text[idx:end_idx], limit)


def base_row(fields: list[str], suite_id: str, question: str, module: str, status: str) -> dict[str, str]:
    row = {field: "" for field in fields}
    year, district, stage = suite_id.split("_", 2)
    row.update(
        {
            "suite_id": suite_id,
            "year": year,
            "district": district,
            "stage": stage,
            "question": question,
            "book_module": module,
            "question_type": "objective" if question.split("#", 1)[0].split("(", 1)[0].isdigit()
            and int(question.split("#", 1)[0].split("(", 1)[0]) <= 15
            else "subjective",
            "status": status,
            "next_action": "future_baodian_intake"
            if status == "included"
            else ("exclude_from_three_target_lines" if status == "module-boundary-excluded" else "manual_review_needed"),
            "integration_status": "suite_identity_culture_repair",
        }
    )
    return row


def add_row(
    out_rows: list[dict[str, str]],
    audit_rows: list[dict[str, str]],
    fields: list[str],
    *,
    suite_id: str,
    question: str,
    module: str,
    status: str,
    row_granularity: str,
    evidence_source: str,
    source_types: str,
    rule_id: str,
    matched_terms: str,
    basis: str,
    evidence_text: str,
    parent_question: str = "",
    next_action: str | None = None,
) -> None:
    row = base_row(fields, suite_id, question, module, status)
    row.update(
        {
            "parent_question": parent_question,
            "row_granularity": row_granularity,
            "evidence_source": evidence_source,
            "source_types": source_types,
            "artifact_location": str(OUT_AUDIT.relative_to(RUN_DIR)),
            "decision_reason": json.dumps(
                {
                    "rule_id": rule_id,
                    "matched_terms": matched_terms,
                    "basis": basis,
                    "source": str(OUT_AUDIT.relative_to(RUN_DIR)),
                },
                ensure_ascii=False,
            ),
        }
    )
    if next_action is not None:
        row["next_action"] = next_action
    out_rows.append(row)
    audit_rows.append(
        {
            "suite_id": suite_id,
            "question": question,
            "parent_question": parent_question,
            "row_granularity": row_granularity,
            "book_module": module,
            "status": status,
            "rule_id": rule_id,
            "matched_terms": matched_terms,
            "basis": basis,
            "evidence_source": evidence_source,
            "source_types": source_types,
            "evidence_text": evidence_text,
        }
    )


MIDTERM_ROWS = [
    ("1", "B2_ECONOMICS", "included", "question", "MIDTERM_Q1_B2_ANSWER_C", "国有企业,民营企业,产业链,商业航天", "答案 C 对应民营企业与产业链协同，知识归入《经济与社会》。"),
    ("2", "B2_ECONOMICS", "included", "question", "MIDTERM_Q2_B2_ANSWER_A", "消费,市场需求,差异化产品", "答案 A 对应消费需求与企业经营，归入《经济与社会》。"),
    ("3", "B2_ECONOMICS", "included", "question", "MIDTERM_Q3_B2_ANSWER_C", "二次元经济,消费市场,地区经济增长点", "答案 C 对应消费新空间和地区经济发展，归入《经济与社会》。"),
    ("4", "B2_ECONOMICS", "included", "question", "MIDTERM_Q4_B2_SERVICE_MARKET_ACCESS", "市场准入,服务业,非公有制经济", "题干围绕服务业市场准入和非公经济活力，归入《经济与社会》。"),
    ("5", "B2_ECONOMICS", "included", "question", "MIDTERM_Q5_B2_MEDICAL_INSURANCE", "医保,社会保障,共济账户", "题干围绕医保个人账户与社会保障服务，归入《经济与社会》。"),
    ("6", "B2_ECONOMICS", "included", "question", "MIDTERM_Q6_B2_ELDERLY_SERVICE_SUPPLY", "养老服务,民营企业,养老供给", "题干围绕养老服务供给和民营企业参与，归入《经济与社会》。"),
    ("7", "B3_POLITICS_RULE_OF_LAW", "included", "question", "MIDTERM_Q7_B3_PARTY_BUILDING_GOVERNANCE", "流动党支部,党员先锋,首都治理", "题干主干是党建引领基层治理，归入《政治与法治》。"),
    ("8", "B3_POLITICS_RULE_OF_LAW", "included", "question", "MIDTERM_Q8_B3_NPC_SUPERVISION", "全国人大常委会,执法检查,法律贯彻", "题干主干是人大监督和法治实施，归入《政治与法治》。"),
    ("9", "B3_POLITICS_RULE_OF_LAW", "included", "question", "MIDTERM_Q9_B3_ETHNIC_UNITY", "民族团结,铸牢中华民族共同体意识,对口支援", "答案 D 对应民族团结和民族政策相关内容，归入《政治与法治》。"),
    ("10", "B3_POLITICS_RULE_OF_LAW", "included", "question", "MIDTERM_Q10_B3_NETWORK_VIOLENCE_GOVERNANCE", "网络暴力治理,法规,政府,社会公平正义", "题干围绕网络暴力信息治理规定和多主体法治治理，归入《政治与法治》。"),
    ("11", "B3_POLITICS_RULE_OF_LAW", "included", "question", "MIDTERM_Q11_B3_GRASSROOTS_RULE_OF_LAW", "法律指引,基层治理法治化,协商民主", "题干围绕基层治理法治化与协商民主，归入《政治与法治》。"),
    ("12", "B1_EXCLUDED", "module-boundary-excluded", "question", "MIDTERM_Q12_B1_NATIONAL_SECURITY", "中国梦,国家安全,民族复兴", "题干主干为国家安全与中国梦，非本次三条目标线。"),
    ("13", "XB1_EXCLUDED", "module-boundary-excluded", "question", "MIDTERM_Q13_XB1_PARENT_PUBLIC_DIPLOMACY", "公共外交,外国游客,东方大国形象", "第 13 题整题含入境游经济与公共外交，先将外交余项排除，并另抽 B2 组件。"),
    ("14", "XB1_EXCLUDED", "module-boundary-excluded", "question", "MIDTERM_Q14_XB1_HEAD_OF_STATE_DIPLOMACY", "元首外交,人类命运共同体,上合组织", "题干主干为中国特色大国外交，非本次三条目标线。"),
    ("15", "XB1_EXCLUDED", "module-boundary-excluded", "question", "MIDTERM_Q15_XB1_APEC_ENERGY", "APEC,国际能源合作", "题干主干为国际组织与国际合作，非本次三条目标线。"),
    ("16(1)", "B2_ECONOMICS", "included", "subquestion", "MIDTERM_Q16_1_B2_COFFEE_MARKET", "经济与社会,市场前景,消费偏好,产品创新", "第 16 题第 (1) 问明确要求运用《经济与社会》知识。"),
    ("16(2)", "B2_ECONOMICS", "included", "subquestion", "MIDTERM_Q16_2_B2_COFFEE_EXPORT", "经济角度,企业经营,供应链,国际国内两个市场", "第 16 题第 (2) 问要求从经济角度提出企业出海建议，抽入 B2。"),
    ("17", "B2_ECONOMICS", "included", "question", "MIDTERM_Q17_B2_GAZELLE_ENTERPRISE", "经济与社会,财政补贴,税收优惠,融资支持", "第 17 题明确要求运用《经济与社会》知识说明政策促进企业发展。"),
    ("18", "B3_POLITICS_RULE_OF_LAW", "included", "question", "MIDTERM_Q18_B3_GRASSROOTS_DEMOCRACY", "基层民主,居民自治,党的领导,民主协商", "第 18 题材料与答案均指向基层民主和社区治理，归入《政治与法治》。"),
    ("19", "B3_POLITICS_RULE_OF_LAW", "included", "question", "MIDTERM_Q19_B3_PARTY_DISCIPLINE", "政治与法治,中国共产党,全面从严治党,全面依法治国", "第 19 题明确要求运用《政治与法治》知识分析党纪处分条例修订。"),
    ("20", "B2_ECONOMICS", "included", "question", "MIDTERM_Q20_B2_GRAIN_COMPENSATION", "经济与社会,共同富裕,区域协调,乡村振兴", "第 20 题明确要求运用《经济与社会》知识说明横向利益补偿机制意义。"),
    ("21(1)", "XB2_EXCLUDED", "module-boundary-excluded", "subquestion", "MIDTERM_Q21_1_XB2_MARRIAGE_LAW", "法治知识,民法典,婚姻家庭", "第 21 题第 (1) 问为法律知识余项，非目标线。"),
    ("21(2)", "XB1_EXCLUDED", "module-boundary-excluded", "subquestion", "MIDTERM_Q21_2_XB1_CHINA_DIPLOMACY", "中国外交,和平与发展,独立自主", "第 21 题第 (2) 问为《当代国际政治与经济》余项，非目标线。"),
]

FINAL_ROWS = [
    ("1", "B4_CULTURE", "included", "question", "FINAL_Q1_B4_CULTURE_CENTRAL_AXIS", "历史文化,中华文明,民族精神,中轴线", "答案 A 对应历史文化承载与中华文明连续性；民族精神按文化处理。"),
    ("2", "XB3_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q2_XB3_SCENE_MIGRATION", "场景迁移,辩证思维整体性", "答案 C 对应迁移和辩证思维整体性，文化材料不等于文化采分点。"),
    ("3", "B4_CULTURE", "included", "question", "FINAL_Q3_B4_GAME_TRADITIONAL_CULTURE", "非遗文化,传统文化,中国故事,中国文化独特魅力", "答案 B 对应讲好中国故事和展现传统文化独特魅力，归入文化。"),
    ("4", "B4_PHILOSOPHY_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q4_B4P_AI_CULTURE_HARMONY", "主观能动性,科技与文化的和鸣", "答案 C 的知识落点是主观能动性；题面文化场景不单独形成文化采分点。"),
    ("5", "B4_PHILOSOPHY_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q5_B4P_DESERT_CONTROL", "主观能动性,量变质变,革命热情与科学态度", "答案 D 的知识落点为哲学方法论，非文化目标线。"),
    ("6", "B4_PHILOSOPHY_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q6_B4P_HOOKES_LAW", "真理,矛盾,实践与认识", "答案 B 的知识落点为认识论和矛盾观，非文化目标线。"),
    ("7", "B4_PHILOSOPHY_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q7_B4P_PEOPLE_VALUE", "价值标准,群众路线", "答案 A 的知识落点为价值观和群众路线，非文化目标线。"),
    ("8", "XB3_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q8_XB3_LOGIC_REASONING", "逻辑与思维,推理,概念关系", "题干为《逻辑与思维》客观题，非目标线。"),
    ("9", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q9_XB2_NATURAL_FRUITS", "民法典,天然孳息,所有权,用益物权", "题干为法律与生活物权题，非目标线。"),
    ("10", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q10_XB2_CONTRACT", "民法典,买卖合同,保证金", "题干为法律与生活合同题，非目标线。"),
    ("11", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q11_XB2_LITIGATION_PASSENGER", "民法典,诉讼,上诉,赔偿责任", "题干为法律与生活诉讼和侵权责任题，非目标线。"),
    ("12", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q12_XB2_INHERITANCE", "继承,遗产,法定继承,仲裁", "题干为法律与生活继承题，非目标线。"),
    ("13", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q13_XB2_LABOR_DISPUTE", "劳动者,劳动法,法院,劳动权益保护", "题干主干为劳动争议法律问题，非目标线。"),
    ("14", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q14_XB2_COPYRIGHT", "著作权,传统蜡染图案,举证,调解", "答案落点为著作权和诉讼程序，传统纹样只是案情材料。"),
    ("15", "B3_POLITICS_RULE_OF_LAW", "included", "question", "FINAL_Q15_B3_SOCIAL_GOVERNANCE_SHORT_VIDEO", "行业内容管理公约,社会治理法治化", "答案 D 指向平台行业公约和社会治理法治化，抽入《政治与法治》。"),
    ("16", "B4_PHILOSOPHY_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q16_PARENT_B4P_REMAINDER", "联系观点,发展观点,哲学与文化混合", "第 16 题哲学与文化混合；文化组件另行抽出，父项余项按哲学边界排除。"),
    ("17(1)", "XB3_EXCLUDED", "module-boundary-excluded", "subquestion", "FINAL_Q17_1_XB3_SCIENTIFIC_THINKING", "科学思维,客观性", "第 17 题第 (1) 问明确要求科学思维知识，非目标线。"),
    ("17(2)", "B4_PHILOSOPHY_EXCLUDED", "module-boundary-excluded", "subquestion", "FINAL_Q17_2_B4P_PERPETUAL_MOTION", "发展观点,对立统一,追求真理", "第 17 题第 (2) 问为哲学角度，非文化目标线。"),
    ("18", "XB3_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q18_XB3_INNOVATIVE_THINKING_LIBRARY", "创新思维,逆向思维,联想思维", "第 18 题设问和细则均要求创新思维，公共文化空间为材料场景，不单独形成文化采分点。"),
    ("19", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q19_PARENT_XB2_LAND_RIGHTS", "法治知识,财产权,用益物权,不动产登记", "第 19 题设问为法治知识；经济意义组件另抽入 B2。"),
    ("20", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q20_XB2_TORT_LIABILITY", "民法典,侵权责任,产品责任,危险动物", "第 20 题为法律与生活侵权责任题，非目标线。"),
    ("21", "XB2_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q21_PARENT_XB2_NONCOMPETE", "法律与生活,竞业限制,劳动合同,知识产权", "第 21 题设问为《法律与生活》；经济效果组件另抽入 B2。"),
    ("22", "B4_PHILOSOPHY_EXCLUDED", "module-boundary-excluded", "question", "FINAL_Q22_PARENT_INTEGRATED_REMAINDER", "质量互变规律,价值观,中国梦,人类命运共同体", "第 22 题为综合短文题；B3 与文化目标组件另抽，余项不并入目标线。"),
]

COMPONENT_ROWS = [
    ("2025_海淀_期中", "13#B2_COMPONENT", "13", "B2_ECONOMICS", "MIDTERM_Q13_B2_COMPONENT_INBOUND_TOURISM", "入境游,经济动能,旅游消费", "第 13 题答案 A 同时含入境游经济动能与公共外交；经济动能部分抽入 B2。", [MIDTERM_PAPER_NEEDLE, MIDTERM_RUBRIC_NEEDLE]),
    ("2025_海淀_期末", "16#B4_CULTURE_COMPONENT", "16", "B4_CULTURE", "FINAL_Q16_B4_CULTURE_COMPONENT_TCM_FASHION", "中华优秀传统文化,创造性转化,创新性发展,文化创新", "第 16 题题干与细则明确中医药文化和传统文化双创，应抽入文化组件。", [FINAL_PAPER_NEEDLE, FINAL_RUBRIC_NEEDLE]),
    ("2025_海淀_期末", "19#B2_COMPONENT", "19", "B2_ECONOMICS", "FINAL_Q19_B2_COMPONENT_LAND_RIGHTS_ECONOMIC_EFFECT", "优化资源配置,增加农民收入,乡村振兴,共同富裕", "第 19 题虽为法治知识题，但答案/细则明确给出资源配置、农民收入、乡村振兴和共同富裕等 B2 效果。", [FINAL_PAPER_NEEDLE, FINAL_RUBRIC_NEEDLE]),
    ("2025_海淀_期末", "21#B2_COMPONENT", "21", "B2_ECONOMICS", "FINAL_Q21_B2_COMPONENT_MARKET_FAIRNESS", "市场公平竞争,推动社会创新,人才资源合理配置,公平公正市场环境", "第 21 题虽为法律与生活题，但答案明确给出维护市场公平竞争和优化人才资源配置等经济效果。", [FINAL_PAPER_NEEDLE, FINAL_RUBRIC_NEEDLE]),
    ("2025_海淀_期末", "22#B4_CULTURE_COMPONENT", "22", "B4_CULTURE", "FINAL_Q22_B4_CULTURE_COMPONENT_YUGONG_SPIRIT", "中华优秀传统文化,中华民族精神,愚公精神", "第 22 题细则明列中华优秀传统文化、中华民族精神；民族精神属于文化，必须抽入文化组件。", [FINAL_PAPER_NEEDLE, FINAL_RUBRIC_NEEDLE]),
    ("2025_海淀_期末", "22#B3_COMPONENT", "22", "B3_POLITICS_RULE_OF_LAW", "FINAL_Q22_B3_COMPONENT_PARTY_PEOPLE", "中国共产党的领导,坚持党的领导,坚持以人民为中心", "第 22 题细则可选知识包含党的领导和以人民为中心，抽入必修三组件。", [FINAL_PAPER_NEEDLE, FINAL_RUBRIC_NEEDLE]),
]


def main() -> int:
    rows = load_csv(IN_MATRIX)
    fields = list(rows[0].keys())
    candidates = load_candidates()

    contaminated = [row for row in rows if row.get("suite_id") == SOURCE_SUITE]
    out_rows = [row for row in rows if row.get("suite_id") != SOURCE_SUITE]
    audit_rows: list[dict[str, str]] = []

    source_paths = {
        MIDTERM_PAPER_NEEDLE: path_for(candidates, MIDTERM_PAPER_NEEDLE),
        MIDTERM_RUBRIC_NEEDLE: path_for(candidates, MIDTERM_RUBRIC_NEEDLE),
        FINAL_PAPER_NEEDLE: path_for(candidates, FINAL_PAPER_NEEDLE),
        FINAL_RUBRIC_NEEDLE: path_for(candidates, FINAL_RUBRIC_NEEDLE),
    }

    for old in contaminated:
        audit_rows.append(
            {
                "suite_id": old.get("suite_id", ""),
                "question": old.get("question", ""),
                "parent_question": old.get("parent_question", ""),
                "row_granularity": old.get("row_granularity", ""),
                "book_module": old.get("book_module", ""),
                "status": old.get("status", ""),
                "rule_id": "REMOVED_CONTAMINATED_2025_HAIDIAN_MIXED_SUITE",
                "matched_terms": "",
                "basis": "旧 2025_海淀_期末 行同时混入 2025 海淀期中与 2025 海淀期末来源，整组移除后按真实文件身份重建。",
                "evidence_source": old.get("evidence_source", ""),
                "source_types": old.get("source_types", ""),
                "evidence_text": old.get("decision_reason", ""),
            }
        )

    for question, module, status, granularity, rule_id, terms, basis in MIDTERM_ROWS:
        parent = question.split("(", 1)[0] if "(" in question else ""
        needles = [MIDTERM_PAPER_NEEDLE, MIDTERM_RUBRIC_NEEDLE]
        evidence_source = " | ".join(path for path in (source_paths[MIDTERM_PAPER_NEEDLE], source_paths[MIDTERM_RUBRIC_NEEDLE]) if path)
        add_row(
            out_rows,
            audit_rows,
            fields,
            suite_id=MIDTERM_SUITE,
            question=question,
            module=module,
            status=status,
            row_granularity=granularity,
            evidence_source=evidence_source,
            source_types="paper|rubric",
            rule_id=rule_id,
            matched_terms=terms,
            basis=basis,
            evidence_text=best_snippet(candidates, needles, parent or question),
            parent_question=parent,
        )

    for question, module, status, granularity, rule_id, terms, basis in FINAL_ROWS:
        parent = question.split("(", 1)[0] if "(" in question else ""
        needles = [FINAL_PAPER_NEEDLE, FINAL_RUBRIC_NEEDLE]
        evidence_source = " | ".join(path for path in (source_paths[FINAL_PAPER_NEEDLE], source_paths[FINAL_RUBRIC_NEEDLE]) if path)
        if question == "22":
            evidence_text = (
                text_slice(TEXT_DIR / "b960993a71bd93ca.txt", "22. 阅读材料", "参考答案", 1400)
                + " "
                + text_slice(TEXT_DIR / "4b22b6c78aaddb3e.txt", "22.(9分)", "16.(8分)守正", 1400)
            )
            evidence_text = compact(evidence_text, 1800)
        else:
            evidence_text = best_snippet(candidates, needles, parent or question)
        add_row(
            out_rows,
            audit_rows,
            fields,
            suite_id=FINAL_SUITE,
            question=question,
            module=module,
            status=status,
            row_granularity=granularity,
            evidence_source=evidence_source,
            source_types="paper|rubric",
            rule_id=rule_id,
            matched_terms=terms,
            basis=basis,
            evidence_text=evidence_text,
            parent_question=parent,
        )

    for suite_id, question, parent, module, rule_id, terms, basis, needles in COMPONENT_ROWS:
        evidence_source = " | ".join(source_paths.get(needle, "") for needle in needles if source_paths.get(needle, ""))
        if parent == "22":
            evidence_text = (
                text_slice(TEXT_DIR / "b960993a71bd93ca.txt", "22. 阅读材料", "参考答案", 1200)
                + " "
                + text_slice(TEXT_DIR / "4b22b6c78aaddb3e.txt", "22.(9分)", "16.(8分)守正", 1600)
            )
            evidence_text = compact(evidence_text, 1800)
        else:
            evidence_text = best_snippet(candidates, needles, parent)
        add_row(
            out_rows,
            audit_rows,
            fields,
            suite_id=suite_id,
            question=question,
            module=module,
            status="included",
            row_granularity="target_component",
            evidence_source=evidence_source,
            source_types="paper|rubric",
            rule_id=rule_id,
            matched_terms=terms,
            basis=basis,
            evidence_text=evidence_text,
            parent_question=parent,
            next_action="future_baodian_intake_target_component",
        )

    duplicate_keys = len(out_rows) - len({(row["suite_id"], row["question"]) for row in out_rows})
    if duplicate_keys:
        dupes = Counter((row["suite_id"], row["question"]) for row in out_rows)
        repeated = [key for key, count in dupes.items() if count > 1][:20]
        raise SystemExit(f"duplicate keys after repair: {repeated}")

    write_csv(OUT_MATRIX, out_rows, fields)
    write_csv(OUT_COVERAGE, out_rows, fields)
    write_csv(
        OUT_AUDIT,
        audit_rows,
        [
            "suite_id",
            "question",
            "parent_question",
            "row_granularity",
            "book_module",
            "status",
            "rule_id",
            "matched_terms",
            "basis",
            "evidence_source",
            "source_types",
            "evidence_text",
        ],
    )
    write_csv(OUT_BLOCKED, [row for row in out_rows if row["status"] == "blocked"], fields)

    status_counts = Counter(row["status"] for row in out_rows)
    included_counts = Counter(row["book_module"] for row in out_rows if row["status"] == "included")
    granularity_counts = Counter(row["row_granularity"] for row in out_rows)
    suite_counts = Counter(row["suite_id"] for row in out_rows if row["suite_id"] in {MIDTERM_SUITE, FINAL_SUITE})
    remaining_blocked = status_counts.get("blocked", 0)

    report = f"""# Suite Identity + Culture Component Repair Report

Generated from `{IN_MATRIX.name}`.

## Scope

- Removed contaminated `2025_海淀_期末` rows: {len(contaminated)}
- Rebuilt `2025_海淀_期中` rows: {suite_counts.get(MIDTERM_SUITE, 0)}
- Rebuilt `2025_海淀_期末` rows: {suite_counts.get(FINAL_SUITE, 0)}
- Explicit target components added: {len(COMPONENT_ROWS)}
- Remaining blocked rows: {remaining_blocked}

## Matrix Counts

- Rows: {len(out_rows)}
- Status counts: {dict(status_counts)}
- Included module counts: {dict(included_counts)}
- Row granularity counts: {dict(granularity_counts)}
- Duplicate `(suite_id, question)` keys: 0

## User Rule Applied

- Mixed philosophy/culture or integrated questions must not be swallowed as one undifferentiated row.
- Cultural content is extracted when the question or rubric explicitly gives cultural knowledge/material hooks.
- `民族精神` is treated as `B4_CULTURE`.

## Deliverables

- `{OUT_AUDIT.relative_to(RUN_DIR)}`
- `{OUT_MATRIX.relative_to(RUN_DIR)}`
- `{OUT_COVERAGE.relative_to(RUN_DIR)}`
- `{OUT_BLOCKED.relative_to(RUN_DIR)}`
"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
