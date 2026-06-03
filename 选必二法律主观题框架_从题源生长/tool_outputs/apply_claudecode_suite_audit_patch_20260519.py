#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply ClaudeCode suite-exhaustion audit corrections to the suite corpus."""

from __future__ import annotations

import csv
import json
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
SRC = ROOT / "04_merge_audit/suite_exhaustive_20260519"
OUT = ROOT / "04_merge_audit/suite_exhaustive_claudecode_corrected_20260519"
PACKET = ROOT / "05_reasoner_packets/suite_exhaustive_claudecode_corrected_20260519"
AUDIT = ROOT / "04_merge_audit/claudecode_suite_exhaustion_audit_20260519"

NEW_QID = "RECOVER_2026_朝阳_期末_18_1"
OLD_CC0311 = "CC0311_2026_海淀_二模_18"
NEW_CC0311 = "CC0311_2026_海淀_二模_18_2"

REMOVE_FROM_CORE = {
    "CC0051_2024_海淀_期中_21_1": "downgraded_to_boundary_by_claudecode_audit_same_as_2025_haidian_midterm",
    "RECOVER_2024_顺义_二模_17": "downgraded_to_boundary_by_claudecode_audit_economy_society_main_axis",
}

ID_MAP = {
    "CC0244_2026_东城_期中_18": "CC0244_2026_东城_期末_18",
    "CC0245_2026_东城_期中_18_2": "CC0245_2026_东城_期末_18_2",
    "CC0317_2026_海淀_期中_18": "CC0317_2026_海淀_期末_18",
    "CC0318_2026_海淀_期中_18_2": "CC0318_2026_海淀_期末_18_2",
    "CC0319_2026_海淀_期中_19": "CC0319_2026_海淀_期末_19",
    "CC0353_2026_西城_期中_17": "CC0353_2026_西城_期末_17",
    "CC0364_2026_通州_期中_19_1": "CC0364_2026_通州_期末_19_1",
    OLD_CC0311: NEW_CC0311,
}

STAGE_CORRECT_IDS = set(ID_MAP.values()) - {NEW_CC0311}


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], header: list[str] | None = None):
    path.parent.mkdir(parents=True, exist_ok=True)
    if header is None:
        header = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def replace_ids_in_text(value: str) -> str:
    if not value:
        return value
    for old, new in ID_MAP.items():
        value = value.replace(old, new)
    return value


def normalize_qid(qid: str) -> str:
    return ID_MAP.get(qid, qid)


def append_note(old: str, note: str) -> str:
    old = old or ""
    return (old + " | " if old else "") + note


def new_chaoyang_question(header: list[str]) -> dict:
    material = (
        "网络消费成为人们消费的重要方式。张某系某网络店铺的经营者。一次直播营销中，该店铺主播人员将大叶紫檀木制作的手串宣称为正宗小叶紫檀材质制作，"
        "并承诺“保真”“假一赔十”。侯某观看直播后购买手串1件，支付价款1000元。侯某收到手串后发现不是小叶紫檀材质，遂诉至法院，请求判令张某赔偿十倍价款1万元。"
        "法院认为，主播宣称所售手串系小叶紫檀并明确承诺“保真”“假一赔十”，该承诺构成合同内容；张某交付的手串材质并非小叶紫檀，不符合合同约定；"
        "“假一赔十”的承诺虽高于法定赔偿标准，但属于当事人意思自治，张某应依约履行赔偿义务。法院最终判决张某赔偿侯某1万元。"
    )
    ask = "结合上述案例，运用《法律与生活》知识，说明法院判决的依据。（7分）"
    rubric = (
        "整体作答思路：合同订立（1分）—合同有效（1分）—合同履行（1分）—合同违约（1分）—违约责任承担方式（1分）—法院判决意义（2分）。"
        "1. 合同依法成立：主播宣称手串为小叶紫檀并作出“假一赔十”的承诺，属于要约，内容明确具体且具有订立合同的意思表示；侯某观看直播后购买手串并支付价款，属于承诺，承诺生效后双方买卖合同成立。"
        "2. 合同合法有效：张某与侯某均具有相应民事行为能力，订立合同的意思表示真实，合同内容不违反法律、行政法规的强制性规定，不违背公序良俗，合同依法生效；“假一赔十”的承诺成为合同内容，对张某具有法律约束力。"
        "3. 张某未按照全面、诚信原则履行合同义务。"
        "4. 张某构成违约且需承担违约责任：根据民法典，张某交付的手串为大叶紫檀，与合同约定的小叶紫檀材质不符，构成违约；“假一赔十”是双方约定的违约责任条款，虽高于法定赔偿标准，但属于当事人意思自治，张某应依约履行赔偿义务。"
        "5. 判决的法律意义：该判决制裁了消费欺诈行为，保护了消费者的合法权益，有利于营造良好的网络消费环境，提升消费者的消费安全感与信心。"
    )
    row = {k: "" for k in header}
    row.update(
        {
            "question_id": NEW_QID,
            "year": "2026",
            "district": "朝阳",
            "exam_stage": "期末",
            "source_paper_file": "F0213: /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/试卷/试卷.pdf; F0392 mirror",
            "paper_page": "rendered page_005",
            "question_no": "18",
            "sub_question_no": "1",
            "full_question_text": "18.（15分）网络消费为人们日常生活提供较大便利，已成为人们消费的重要方式。材料一【基本案情】" + material + "（1）" + ask,
            "material_text": material,
            "ask_text": ask,
            "answer_file": "F0212: /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/细则/细则.pdf; F0393 mirror",
            "answer_page": "rendered page_002",
            "answer_text": rubric,
            "rubric_file": "F0212: /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/细则/细则.pdf; F0393 mirror",
            "rubric_page": "rendered page_002",
            "rubric_text": rubric,
            "evidence_type": "marking_rubric",
            "evidence_level": "formal",
            "why_candidate_subjective_law_question": "设问明确要求运用《法律与生活》知识；材料与细则均围绕合同订立、合同效力、合同履行、合同违约、违约责任和消费者权益保护。",
            "why_maybe_not_subjective_law_question": "第18题第（2）问为《逻辑与思维》，但第（1）问已明确拆分为法律与生活。",
            "module_boundary_risk": "选必二",
            "confidence": "high",
            "source_locator": "F0213/F0392 rendered page_005; F0212/F0393 rendered page_002",
            "notes": "Recovered from ClaudeCode suite-exhaustion audit 20260519; original PDFs are OCR-blocked and require OCR_recovered_via_render metadata.",
            "merged_question_id": NEW_QID,
            "codex_question_id_if_matched": "",
            "claudecode_question_id": "MISS_CC_2026_朝阳_期末_18_1",
            "merge_status": "claudecode_recovered_after_suite_audit",
            "merge_decision_reason": "ClaudeCode B found a formal core subjective law question masked by OCR-blocked 2026朝阳期末 files.",
        }
    )
    return row


def clean_cc0311_question(row: dict) -> dict:
    legal_material = (
        "材料二 保护知识产权就是保护创新。民法典第440条明确将“可以转让的注册商标专用权、专利权、著作权等知识产权中的财产权”列入可质押权利范围，企业可以质押其核心专利向银行申请贷款。"
        "公司法第48条规定，股东可以用知识产权等可以用货币估价并可以依法转让的非货币财产作价出资。"
        "专利法第15条规定，被授予专利权的单位应当对职务发明创造的发明人或者设计人给予奖励；发明创造专利实施后，应根据其推广应用范围和取得的经济效益给予合理报酬。"
    )
    ask = "结合材料二，运用《法律与生活》知识，分析上述关于知识产权的法律规定是如何助力企业创新与发展的。（8分）"
    ans = (
        "知识产权是财产权的重要组成部分，也是企业重要的无形资产。民法典将知识产权中的财产权纳入可质押权利范围，有利于拓宽企业融资渠道，缓解企业资金压力；"
        "公司法确认知识产权可以作价出资，促进技术要素转化资本，鼓励创业创新；专利法明确对发明人应当给予奖励和合理报酬，尊重创新主体权益，调动员工创新的积极性，激发企业创新的内生动力。"
        "上述法律对知识产权的相关规定，不仅保护了知识产权权利人的合法权益，也促进知识产权的流通使用，为企业发展与创新提供有力法治保障。"
    )
    row = dict(row)
    row["question_id"] = NEW_CC0311
    row["sub_question_no"] = "2"
    row["full_question_text"] = f"18（2）{legal_material}{ask}"
    row["material_text"] = legal_material
    row["ask_text"] = ask
    row["answer_text"] = ans
    row["rubric_text"] = ans
    row["source_locator"] = "F0197:text Q18(2)"
    row["notes"] = append_note(row.get("notes", ""), "claudecode_suite_audit_20260519: split from mixed Q18; logic subquestion removed from core.")
    row["merged_question_id"] = NEW_CC0311
    return row


def process_questions():
    path = SRC / "merged_subjective_law_questions_suite_exhaustive.csv"
    rows = read_csv(path)
    header = list(rows[0].keys())
    out = []
    removed = []
    for row in rows:
        qid = row["question_id"]
        if qid in REMOVE_FROM_CORE:
            rr = dict(row)
            rr["removal_reason"] = REMOVE_FROM_CORE[qid]
            removed.append(rr)
            continue
        if qid == OLD_CC0311:
            out.append(clean_cc0311_question(row))
            continue
        qid2 = normalize_qid(qid)
        row = {k: replace_ids_in_text(v) for k, v in row.items()}
        row["question_id"] = qid2
        row["merged_question_id"] = qid2
        if qid2 in STAGE_CORRECT_IDS:
            row["exam_stage"] = "期末"
            row["notes"] = append_note(row.get("notes", ""), "claudecode_suite_audit_20260519: exam_stage corrected from 期中 to 期末.")
        out.append(row)
    out.append(new_chaoyang_question(header))
    write_csv(OUT / "merged_subjective_law_questions_claudecode_corrected.csv", out, header)
    write_csv(OUT / "removed_from_core_after_claudecode_audit.csv", removed, header + ["removal_reason"])
    return out, removed, header


def process_material_atoms():
    rows = read_csv(SRC / "merged_material_atoms_subjective_suite_exhaustive.csv")
    header = list(rows[0].keys())
    out = []
    for row in rows:
        qid = row["question_id"]
        if qid in REMOVE_FROM_CORE or qid == OLD_CC0311:
            continue
        row = {k: replace_ids_in_text(v) for k, v in row.items()}
        row["question_id"] = normalize_qid(qid)
        row["material_atom_id"] = replace_ids_in_text(row["material_atom_id"])
        out.append(row)
    out.extend(
        [
            {
                "material_atom_id": f"M_{NEW_CC0311}_01",
                "question_id": NEW_CC0311,
                "material_phrase": "民法典第440条将可转让的知识产权中的财产权列入可质押权利范围，企业可以质押核心专利向银行贷款。",
                "plain_description": "知识产权财产权可以用于质押融资。",
                "subject_or_actor": "企业",
                "action_or_event": "质押知识产权财产权申请贷款",
                "affected_party": "企业/银行",
                "conflict_or_problem": "创新企业融资压力",
                "legal_signal_if_any": "民法典；知识产权；质押权利",
                "possible_relevance_to_answer": "触发知识产权财产权和担保融资助力企业创新。",
                "source_locator": "F0197:text Q18(2)",
                "uncertainty": "claudecode_split_clean_material_atom",
            },
            {
                "material_atom_id": f"M_{NEW_CC0311}_02",
                "question_id": NEW_CC0311,
                "material_phrase": "公司法第48条规定，股东可以用知识产权等非货币财产作价出资。",
                "plain_description": "知识产权可以作价出资并转化为资本要素。",
                "subject_or_actor": "股东/企业",
                "action_or_event": "以知识产权作价出资",
                "affected_party": "企业",
                "conflict_or_problem": "创新成果资本化和企业发展",
                "legal_signal_if_any": "公司法；知识产权；作价出资",
                "possible_relevance_to_answer": "触发知识产权转化资本、促进创新发展。",
                "source_locator": "F0197:text Q18(2)",
                "uncertainty": "claudecode_split_clean_material_atom",
            },
            {
                "material_atom_id": f"M_{NEW_CC0311}_03",
                "question_id": NEW_CC0311,
                "material_phrase": "专利法第15条规定，被授予专利权的单位应当对职务发明创造的发明人或者设计人给予奖励和合理报酬。",
                "plain_description": "专利法保护职务发明创造者的奖励和报酬权益。",
                "subject_or_actor": "单位/发明人/设计人",
                "action_or_event": "给予奖励和合理报酬",
                "affected_party": "创新劳动者",
                "conflict_or_problem": "创新激励和劳动者权益保护",
                "legal_signal_if_any": "专利法；职务发明；奖励报酬",
                "possible_relevance_to_answer": "触发保护创新主体权益、调动创新积极性。",
                "source_locator": "F0197:text Q18(2)",
                "uncertainty": "claudecode_split_clean_material_atom",
            },
        ]
    )
    chaoyang_atoms = [
        ("01", "主播宣称手串为小叶紫檀并承诺“保真”“假一赔十”。", "经营者在直播中作出具体承诺，该承诺构成合同内容。", "张某/主播", "作出商品材质与赔偿承诺", "侯某", "直播购物承诺是否构成合同内容", "合同订立；要约；承诺"),
        ("02", "侯某观看直播后购买手串1件并支付价款1000元。", "消费者作出购买承诺并履行付款，买卖合同成立。", "侯某", "购买并付款", "张某", "买卖合同是否成立", "合同成立；承诺生效"),
        ("03", "张某与侯某均具有民事行为能力，意思表示真实，合同内容不违法且不违背公序良俗。", "合同具备合法有效条件。", "张某/侯某", "订立买卖合同", "双方", "合同是否有效", "合同有效"),
        ("04", "张某交付的手串为大叶紫檀，与合同约定的小叶紫檀材质不符。", "经营者未按约定全面、诚信履行合同义务。", "张某", "交付不符合约定的商品", "侯某", "是否违约", "合同履行；违约责任"),
        ("05", "“假一赔十”的承诺虽高于法定赔偿标准，但属于当事人意思自治，法院判决张某赔偿侯某1万元。", "约定违约责任条款应依约履行，判决保护消费者权益并规范网络消费。", "法院/张某/侯某", "判决依约赔偿", "消费者/网络消费秩序", "违约责任承担及裁判意义", "违约责任；消费者权益"),
    ]
    for suffix, phrase, desc, actor, action, affected, problem, signal in chaoyang_atoms:
        out.append(
            {
                "material_atom_id": f"M_{NEW_QID}_{suffix}",
                "question_id": NEW_QID,
                "material_phrase": phrase,
                "plain_description": desc,
                "subject_or_actor": actor,
                "action_or_event": action,
                "affected_party": affected,
                "conflict_or_problem": problem,
                "legal_signal_if_any": signal,
                "possible_relevance_to_answer": "对应 18(1) 合同/违约/消费者权益评分点。",
                "source_locator": "F0213/F0392 rendered page_005; F0212/F0393 rendered page_002",
                "uncertainty": "OCR_recovered_via_render_claudecode_audit",
            }
        )
    write_csv(OUT / "merged_material_atoms_subjective_claudecode_corrected.csv", out, header)
    return out, header


def process_ask_atoms():
    rows = read_csv(SRC / "merged_ask_atoms_subjective_suite_exhaustive.csv")
    header = list(rows[0].keys())
    out = []
    for row in rows:
        qid = row["question_id"]
        if qid in REMOVE_FROM_CORE or qid == OLD_CC0311:
            continue
        row = {k: replace_ids_in_text(v) for k, v in row.items()}
        row["question_id"] = normalize_qid(qid)
        row["ask_atom_id"] = replace_ids_in_text(row["ask_atom_id"])
        out.append(row)
    out.append(
        {
            "ask_atom_id": f"A_{NEW_CC0311}_01",
            "question_id": NEW_CC0311,
            "ask_text": "结合材料二，运用《法律与生活》知识，分析上述关于知识产权的法律规定是如何助力企业创新与发展的。（8分）",
            "ask_function_plain": "意义",
            "module_requirement": "法律与生活",
            "requires_material_connection": "yes",
            "requires_value_discussion": "yes",
            "requires_behavior_evaluation": "no",
            "requires_solution_or_measure": "no",
            "student_task_plain": "把三个法律规定分别转成知识产权助力融资、资本化和创新激励的答案句。",
            "source_locator": "F0197:text Q18(2)",
        }
    )
    out.append(
        {
            "ask_atom_id": f"A_{NEW_QID}_01",
            "question_id": NEW_QID,
            "ask_text": "结合上述案例，运用《法律与生活》知识，说明法院判决的依据。（7分）",
            "ask_function_plain": "说明",
            "module_requirement": "法律与生活",
            "requires_material_connection": "yes",
            "requires_value_discussion": "yes",
            "requires_behavior_evaluation": "yes",
            "requires_solution_or_measure": "no",
            "student_task_plain": "判断合同是否成立有效、是否违约、如何承担违约责任，并收束消费者权益和网络消费秩序意义。",
            "source_locator": "F0213/F0392 rendered page_005; F0212/F0393 rendered page_002",
        }
    )
    write_csv(OUT / "merged_ask_atoms_subjective_claudecode_corrected.csv", out, header)
    return out, header


def process_rubric_atoms():
    rows = read_csv(SRC / "merged_rubric_atoms_subjective_suite_exhaustive.csv")
    header = list(rows[0].keys())
    out = []
    for row in rows:
        qid = row["question_id"]
        if qid in REMOVE_FROM_CORE or qid == OLD_CC0311:
            continue
        row = {k: replace_ids_in_text(v) for k, v in row.items()}
        row["question_id"] = normalize_qid(qid)
        row["rubric_atom_id"] = replace_ids_in_text(row["rubric_atom_id"])
        row["related_material_atom_ids"] = replace_ids_in_text(row.get("related_material_atom_ids", ""))
        out.append(row)
    cc0311 = [
        ("01", "知识产权是财产权的重要组成部分，也是企业重要的无形资产。", "确认知识产权的财产权属性和企业无形资产价值。", "M_" + NEW_CC0311 + "_01", "知识产权；财产权；无形资产", "knowledge"),
        ("02", "民法典将知识产权中的财产权纳入可质押权利范围，有利于拓宽企业融资渠道，缓解企业资金压力。", "把民法典质押规则转化为融资助力。", "M_" + NEW_CC0311 + "_01", "民法典；知识产权；质押；融资", "knowledge+material+value"),
        ("03", "公司法确认知识产权可以作价出资，促进技术要素转化资本，鼓励创业创新。", "把公司法作价出资规则转化为创新成果资本化。", "M_" + NEW_CC0311 + "_02", "公司法；作价出资；资本要素", "knowledge+material+value"),
        ("04", "专利法规定对发明人给予奖励和合理报酬，尊重创新主体权益，调动员工创新积极性。", "把专利法奖励报酬规则转化为创新激励。", "M_" + NEW_CC0311 + "_03", "专利法；职务发明；奖励；合理报酬", "knowledge+material+value"),
        ("05", "法律规定保护知识产权权利人合法权益，促进知识产权流通使用，为企业创新发展提供法治保障。", "形成法治保障与企业创新发展的价值收束。", "M_" + NEW_CC0311 + "_01|M_" + NEW_CC0311 + "_02|M_" + NEW_CC0311 + "_03", "知识产权；合法权益；流通使用；法治保障", "knowledge+value"),
    ]
    for suffix, phrase, desc, mats, kws, kmv in cc0311:
        out.append(
            {
                "rubric_atom_id": f"R_{NEW_CC0311}_{suffix}",
                "question_id": NEW_CC0311,
                "rubric_or_answer_phrase": phrase,
                "evidence_type": "teacher_reference_answer",
                "evidence_level": "reference_only",
                "plain_reward_description": desc,
                "related_material_atom_ids": mats,
                "what_expression_is_rewarded": phrase,
                "what_judgment_student_must_make_before_writing": "先判断材料二中的法律规定分别作用于融资、出资、奖励报酬，再转成企业创新发展的意义。",
                "legal_knowledge_or_rule_if_explicit": kws,
                "value_expression_if_explicit": "助力企业创新与发展",
                "knowledge_material_value_type": kmv,
                "can_be_written_without_material": "no",
                "source_locator": "F0197:text Q18(2)",
                "uncertainty": "claudecode_split_reference_only",
            }
        )
    chaoyang = [
        ("01", "合同依法成立：主播宣称手串为小叶紫檀并作出“假一赔十”的承诺，属于要约；侯某观看直播后购买并支付价款，属于承诺，承诺生效后买卖合同成立。", "奖励判断合同订立路径：要约+承诺+买卖合同成立。", "M_" + NEW_QID + "_01|M_" + NEW_QID + "_02", "合同订立；要约；承诺", "", "knowledge+material"),
        ("02", "合同合法有效：双方具有相应民事行为能力，意思表示真实，内容不违反法律法规强制性规定、不违背公序良俗；“假一赔十”的承诺成为合同内容，对张某具有法律约束力。", "奖励判断合同有效条件。", "M_" + NEW_QID + "_03", "合同有效；意思表示真实；公序良俗", "", "knowledge+material"),
        ("03", "张某未按照全面、诚信原则履行合同义务。", "奖励指出合同履行原则被违反。", "M_" + NEW_QID + "_04", "全面履行；诚信原则", "", "knowledge+material"),
        ("04", "张某构成违约且需承担违约责任：交付的大叶紫檀与合同约定的小叶紫檀不符；“假一赔十”是双方约定的违约责任条款，虽高于法定赔偿标准，但属意思自治，张某应依约赔偿。", "奖励事实与违约责任条款匹配。", "M_" + NEW_QID + "_04|M_" + NEW_QID + "_05", "违约；违约责任；意思自治；依约赔偿", "", "knowledge+material"),
        ("05", "判决制裁了消费欺诈行为，保护了消费者的合法权益，有利于营造良好的网络消费环境，提升消费者的消费安全感与信心。", "奖励裁判意义的价值收束，四个维度选二即可。", "M_" + NEW_QID + "_05", "消费欺诈；消费者合法权益；网络消费环境；消费安全感", "保护消费者权益；规范网络消费", "material+value"),
    ]
    for suffix, phrase, desc, mats, kws, value, kmv in chaoyang:
        out.append(
            {
                "rubric_atom_id": f"R_{NEW_QID}_{suffix}",
                "question_id": NEW_QID,
                "rubric_or_answer_phrase": phrase,
                "evidence_type": "marking_rubric",
                "evidence_level": "formal",
                "plain_reward_description": desc,
                "related_material_atom_ids": mats,
                "what_expression_is_rewarded": phrase,
                "what_judgment_student_must_make_before_writing": "先判断合同成立有效，再判断经营者是否按约履行、是否违约及应承担何种违约责任。",
                "legal_knowledge_or_rule_if_explicit": kws,
                "value_expression_if_explicit": value,
                "knowledge_material_value_type": kmv,
                "can_be_written_without_material": "no",
                "source_locator": "F0212/F0393 rendered page_002",
                "uncertainty": "OCR_recovered_via_render_claudecode_audit",
            }
        )
    write_csv(OUT / "merged_rubric_atoms_subjective_claudecode_corrected.csv", out, header)
    return out, header


def split_list(v: str) -> list[str]:
    return [x for x in (v or "").split(";") if x]


def join_list(items):
    return ";".join([x for x in items if x])


def process_matrix(question_rows):
    rows = read_csv(SRC / "suite_exhaustion_matrix.csv")
    header = list(rows[0].keys())
    out = []
    for row in rows:
        y, d, s = row["year"], row["district"], row["exam_stage"]
        qids = [normalize_qid(x) for x in split_list(row["question_ids_in_suite_exhaustive_core"]) if x not in REMOVE_FROM_CORE]
        if OLD_CC0311 in row["question_ids_in_suite_exhaustive_core"]:
            qids = [NEW_CC0311 if x == OLD_CC0311 else x for x in qids]
        row["question_ids_in_suite_exhaustive_core"] = join_list(qids)
        row["core_question_count"] = str(len(qids))
        if y == "2024" and d == "海淀" and s == "期中":
            row["suite_status"] = "midterm_boundary_no_core_after_claudecode_audit"
            row["boundary_or_blocked_case_ids"] = join_list(split_list(row["boundary_or_blocked_case_ids"]) + ["CC0051_2024_海淀_期中_21_1_DOWNGRADED_TO_BOUNDARY"])
            row["notes"] = "ClaudeCode audit: Q21(1) is 法治知识/良法 boundary; same口径 as 2025海淀期中."
        elif y == "2024" and d == "顺义" and s == "二模":
            row["suite_status"] = "boundary_not_core_after_claudecode_audit"
            row["boundary_or_blocked_case_ids"] = join_list(split_list(row["boundary_or_blocked_case_ids"]) + ["RECOVER_2024_顺义_二模_17_DOWNGRADED_TO_BOUNDARY"])
            row["notes"] = "ClaudeCode audit: Q17 main axis is 经济社会发展/产权制度改革; not core法律与生活."
        elif y == "2026" and d == "朝阳" and s == "期中":
            true_mid = dict(row)
            true_mid.update(
                {
                    "source_file_ids": "F0209;F0210;F0211;F0389;F0390;F0391",
                    "paper_file_ids": "F0211;F0391",
                    "rubric_or_answer_file_ids": "F0209;F0210;F0389;F0390",
                    "suite_status": "no_law_subjective_confirmed",
                    "question_ids_in_suite_exhaustive_core": "",
                    "core_question_count": "0",
                    "boundary_or_blocked_case_ids": "",
                    "notes": "True 2026朝阳期中 only; ClaudeCode confirmed no 法律与生活 subjective.",
                }
            )
            out.append(true_mid)
            term = dict(row)
            term.update(
                {
                    "exam_stage": "期末",
                    "source_file_ids": "F0212;F0213;F0392;F0393",
                    "paper_file_ids": "F0213;F0392",
                    "rubric_or_answer_file_ids": "F0212;F0393",
                    "suite_status": "has_suite_exhaustive_core_rows_after_claudecode_recovery",
                    "question_ids_in_suite_exhaustive_core": NEW_QID,
                    "core_question_count": "1",
                    "boundary_or_blocked_case_ids": "UNCERTAIN_2026_朝阳_期末_18_2_LOGIC",
                    "notes": "New independent 2026朝阳期末 suite split from old 朝阳期中 row; Q18(1) recovered via rendered pages.",
                }
            )
            out.append(term)
            continue
        elif y == "2026" and d == "海淀" and s == "期中":
            true_mid = dict(row)
            true_mid.update(
                {
                    "source_file_ids": "F0214;F0215;F0394;F0395",
                    "paper_file_ids": "F0215;F0394",
                    "rubric_or_answer_file_ids": "F0214;F0395",
                    "suite_status": "no_law_subjective_confirmed",
                    "question_ids_in_suite_exhaustive_core": "",
                    "core_question_count": "0",
                    "boundary_or_blocked_case_ids": "",
                    "notes": "True 2026海淀期中 only; ClaudeCode confirmed no 法律与生活 subjective.",
                }
            )
            out.append(true_mid)
            term = dict(row)
            term.update(
                {
                    "exam_stage": "期末",
                    "source_file_ids": "F0216;F0217;F0396;F0397",
                    "paper_file_ids": "F0217;F0397",
                    "rubric_or_answer_file_ids": "F0216;F0396",
                    "suite_status": "has_suite_exhaustive_core_rows_after_stage_correction",
                    "question_ids_in_suite_exhaustive_core": "CC0317_2026_海淀_期末_18;CC0318_2026_海淀_期末_18_2;CC0319_2026_海淀_期末_19",
                    "core_question_count": "3",
                    "boundary_or_blocked_case_ids": "",
                    "notes": "2026海淀期末 split from mislabeled期中 row.",
                }
            )
            out.append(term)
            continue
        elif y == "2026" and d in {"东城", "西城", "通州"} and s == "期中":
            row["exam_stage"] = "期末"
            row["suite_status"] = "has_suite_exhaustive_core_rows_after_stage_correction"
            row["notes"] = "ClaudeCode audit: this row was mislabeled as 期中; source paths show it is 期末."
        elif y == "2026" and d == "丰台" and s == "期中":
            row["exam_stage"] = "期末"
            row["suite_status"] = "mixed_boundary_only_after_stage_correction"
            row["boundary_or_blocked_case_ids"] = "UNCERTAIN_2026_丰台_期末_18_MIXED"
            row["notes"] = "ClaudeCode audit: actual suite is 2026丰台期末; Q18 remains mixed boundary, not core."
        elif y == "2026" and d == "石景山" and s == "期中":
            row["suite_status"] = "not_independent_suite_stage_mapping_conflict"
            row["notes"] = "ClaudeCode audit: no independent 2026石景山期中 suite; this is an artifact of期末 mapping."
        out.append(row)
    write_csv(OUT / "suite_exhaustion_matrix_claudecode_corrected.csv", out, header)
    return out, header


def boundary_table():
    rows = read_csv(SRC / "boundary_mixed_or_blocked_cases.csv")
    header = list(rows[0].keys())
    extra = []
    template = {k: "" for k in header}
    for qid, reason in REMOVE_FROM_CORE.items():
        r = dict(template)
        r.update(
            {
                "case_id": qid + "_DOWNGRADED_TO_BOUNDARY",
                "year": "2024",
                "district": "海淀" if "海淀" in qid else "顺义",
                "exam_stage": "期中" if "海淀" in qid else "二模",
                "question_no": "21" if "海淀" in qid else "17",
                "sub_question_no": "1" if "海淀" in qid else "",
                "boundary_status": "downgraded_from_core_after_claudecode_audit",
                "reason": reason,
                "evidence_level": "formal" if "海淀" in qid else "reference_only",
                "recommended_action": "exclude_from_core_reasoner_packet; keep as boundary audit evidence only",
                "source_locator": "see removed_from_core_after_claudecode_audit.csv",
            }
        )
        extra.append(r)
    r = dict(template)
    r.update(
        {
            "case_id": "UNCERTAIN_2026_朝阳_期末_18_2_LOGIC",
            "year": "2026",
            "district": "朝阳",
            "exam_stage": "期末",
            "question_no": "18",
            "sub_question_no": "2",
            "boundary_status": "non_law_subquestion_removed",
            "reason": "第18(2)问明确运用《逻辑与思维》知识，不进入法律主观题核心。",
            "evidence_level": "formal",
            "recommended_action": "exclude_from_core_reasoner_packet",
            "source_locator": "F0213/F0392 rendered page_006; F0212/F0393 rendered page_002",
        }
    )
    extra.append(r)
    rows = [{k: replace_ids_in_text(v) for k, v in row.items()} for row in rows] + extra
    write_csv(OUT / "boundary_mixed_or_blocked_cases_claudecode_corrected.csv", rows, header)
    return rows, header


def write_jsonl(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def copy_reasoner_packet_files():
    PACKET.mkdir(parents=True, exist_ok=True)
    mapping = {
        "merged_subjective_law_questions_claudecode_corrected.csv": "merged_subjective_law_questions_for_reasoners_claudecode_corrected.csv",
        "merged_material_atoms_subjective_claudecode_corrected.csv": "merged_material_atoms_subjective_for_reasoners_claudecode_corrected.csv",
        "merged_ask_atoms_subjective_claudecode_corrected.csv": "merged_ask_atoms_subjective_for_reasoners_claudecode_corrected.csv",
        "merged_rubric_atoms_subjective_claudecode_corrected.csv": "merged_rubric_atoms_subjective_for_reasoners_claudecode_corrected.csv",
        "suite_exhaustion_matrix_claudecode_corrected.csv": "suite_exhaustion_matrix_for_reasoners_claudecode_corrected.csv",
        "boundary_mixed_or_blocked_cases_claudecode_corrected.csv": "boundary_mixed_or_blocked_cases_for_reasoners_claudecode_corrected.csv",
        "suite_exhaustion_report_claudecode_corrected.md": "suite_exhaustion_report_for_reasoners_claudecode_corrected.md",
    }
    for src_name, dst_name in mapping.items():
        shutil.copy2(OUT / src_name, PACKET / dst_name)
    shutil.copy2(AUDIT / "claudecode_suite_exhaustion_audit_report.md", PACKET / "claudecode_suite_exhaustion_audit_report_for_reasoners.md")
    shutil.copy2(AUDIT / "claudecode_missed_core_candidates.csv", PACKET / "claudecode_missed_core_candidates_for_reasoners.csv")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    PACKET.mkdir(parents=True, exist_ok=True)
    questions, removed, q_header = process_questions()
    materials, _ = process_material_atoms()
    asks, _ = process_ask_atoms()
    rubrics, _ = process_rubric_atoms()
    matrix, _ = process_matrix(questions)
    boundaries, _ = boundary_table()

    write_jsonl(OUT / "merged_subjective_law_questions_claudecode_corrected.jsonl", questions)

    q_counter = Counter(r["evidence_level"] for r in questions)
    status_counter = Counter(r["suite_status"] for r in matrix)
    core_by_suite = defaultdict(int)
    for q in questions:
        core_by_suite[(q["year"], q["district"], q["exam_stage"])] += 1
    now = datetime.now(timezone(timedelta(hours=8))).isoformat()
    counts = {
        "generated_at": now,
        "source_corpus": str(SRC),
        "claudecode_audit": str(AUDIT),
        "question_count": len(questions),
        "material_atom_count": len(materials),
        "ask_atom_count": len(asks),
        "rubric_atom_count": len(rubrics),
        "evidence_level_counts": dict(q_counter),
        "removed_from_core_count": len(removed),
        "added_core_question_ids": [NEW_QID],
        "renamed_question_ids": ID_MAP,
        "stage_corrected_question_ids": sorted(STAGE_CORRECT_IDS),
        "suite_matrix_rows": len(matrix),
        "suite_status_counts": dict(status_counter),
        "non_independent_stage_conflict_rows": [r for r in matrix if r["suite_status"] == "not_independent_suite_stage_mapping_conflict"],
        "true_no_law_subjective_suites": [
            f"{r['year']}-{r['district']}-{r['exam_stage']}"
            for r in matrix
            if r["suite_status"] in {"no_law_subjective_confirmed", "midterm_boundary_no_core_after_claudecode_audit"}
        ],
    }
    (OUT / "suite_exhaustive_claudecode_corrected_counts.json").write_text(json.dumps(counts, ensure_ascii=False, indent=2), encoding="utf-8")

    report = f"""# Suite Exhaustive Corpus — ClaudeCode Corrected 2026-05-19

Generated at: {now}

This corpus supersedes `suite_exhaustive_20260519` for downstream reasoner packets.

## Corrections Applied

- Added `RECOVER_2026_朝阳_期末_18_1` from ClaudeCode missed-core audit; evidence level formal; source recovered from rendered pages F0213/F0392 and F0212/F0393.
- Removed from core and moved to boundary audit:
  - `CC0051_2024_海淀_期中_21_1`
  - `RECOVER_2024_顺义_二模_17`
- Split `CC0311_2026_海淀_二模_18` into core-only `CC0311_2026_海淀_二模_18_2`; logic subquestion removed from core.
- Corrected seven mislabeled 2026 term rows from `期中` to `期末`.
- Split true 2026 朝阳期中 / 朝阳期末 and true 2026 海淀期中 / 海淀期末 in the suite matrix.
- Preserved OCR/source blockers as audit risks; OCR-recovered entries are tagged in notes/uncertainty fields.

## Counts

- Core questions: {len(questions)}
- Evidence levels: {dict(q_counter)}
- Material atoms: {len(materials)}
- Ask atoms: {len(asks)}
- Rubric atoms: {len(rubrics)}
- Removed from core: {len(removed)}
- Boundary/blocked cases: {len(boundaries)}

## Current Downstream Gate

This corrected corpus may be used to rebuild reasoner packets. GPT-5.5 Pro / Claude Opus outputs created from older 53/56/66-row packets remain superseded.

Remaining blocker before final framework: OCR/source blockers in ClaudeCode audit should remain visible, especially 2026 丰台期末 mixed case and 2026 西城期末 formal rubric OCR.
"""
    (OUT / "suite_exhaustion_report_claudecode_corrected.md").write_text(report, encoding="utf-8")

    packet = f"""# Reasoner Input Packet — Suite Exhaustive ClaudeCode Corrected 2026-05-19

Use only the corrected files in this folder.

Core question count: {len(questions)}
Evidence levels: {dict(q_counter)}
Material atoms: {len(materials)}
Ask atoms: {len(asks)}
Rubric atoms: {len(rubrics)}

Key correction: ClaudeCode audit returned `FINAL_JUDGMENT: FAIL` for the previous 66-row package. This packet applies the required hard fixes before any GPT-5.5 Pro / Claude Opus open observation.

Still forbidden:
- no framework yet;
- no codebook until dual observations are rerun from this corrected packet;
- no reference_only-only core support;
- no use of removed boundary rows as core framework evidence.
"""
    (PACKET / "REASONER_INPUT_PACKET_CLAUDECODE_CORRECTED.md").write_text(packet, encoding="utf-8")

    copy_reasoner_packet_files()
    print(json.dumps(counts, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
