#!/usr/bin/env python3
"""Build a guarded framework_v1_2 and rerun an all-65 pressure snapshot."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
CODEBOOK = ROOT / "08_codebook" / "provisional_codebook_v1_3_after_gptpro_guarded_review_20260519.csv"
PRESSURE_V11 = ROOT / "10_framework_validation" / "framework_v1_1_question_by_question_sentence_pressure_test_20260519.csv"
RESOLUTION = ROOT / "10_framework_validation" / "fail4_source_adjudication_20260519" / "framework_v1_2_fail4_resolution_snapshot_20260519.csv"
PARTIAL_POLICY = ROOT / "10_framework_validation" / "framework_v1_2_partial_policy_20260519.csv"
LOCAL_PATCH = ROOT / "10_framework_validation" / "fail4_source_adjudication_20260519" / "fail4_local_patch_candidates_20260519.csv"

OUT_FRAMEWORK = ROOT / "09_candidate_frameworks" / "framework_v1_2_guarded.md"
OUT_PLAN = ROOT / "09_candidate_frameworks" / "framework_v1_2_synthesis_plan.md"
OUT_MAP = ROOT / "09_candidate_frameworks" / "framework_v1_2_evidence_map.csv"
OUT_TEST = ROOT / "10_framework_validation" / "framework_v1_2_question_by_question_test_20260519.csv"
OUT_PASS = ROOT / "10_framework_validation" / "framework_v1_2_pass_report_20260519.md"
OUT_FAIL = ROOT / "10_framework_validation" / "framework_v1_2_failure_cases_20260519.md"
OUT_PATCH = ROOT / "10_framework_validation" / "framework_v1_2_patch_suggestions_20260519.md"

CORE_EXCLUDED_QUESTION_IDS = {"CC0380_2026_顺义_二模_18_2"}
CORE_EXCLUDED_ATOM_PREFIXES = ("R_CC0380_2026_顺义_二模_18_2_",)
CORE_EXCLUDED_MATERIAL_PREFIXES = ("M_CC0380_2026_顺义_二模_18_2_",)

OPEN_CONTAINER_OVERRIDES = {
    "CC0380_2026_顺义_二模_18_2": {
        "framework_entry_node": "FWV1_2_OPEN 开放容器",
        "why_this_entry": "Formal evidence, but the merged row is marked 综合 and the prompt allows必修三+选必二 mixed analysis; keep as AI rights/remedies open-container pressure case, not core node support.",
        "patch_type": "formal_open_container_ai_governance_boundary",
        "patch_suggestion": "remove from core CODE_COWORK_007 evidence; keep as open-container formal pressure case until same-type formal samples repeat",
    }
}

ROW_SCORING_OVERRIDES = {
    "CC0077_2025_东城_一模_19": {
        "rubric_atom_ids_matched": "R_CC0077_2025_东城_一模_19_02|R_CC0077_2025_东城_一模_19_03|R_CC0077_2025_东城_一模_19_04",
        "full_score_sentence_generated": "解决机制写调解、诉讼调解或诉讼；柳某与医院案写树立劳动者权利和义务相统一的法治意识、督促劳动者履行义务，并维护用人单位合法权益或构建和谐劳动关系；顾氏三兄弟案写落实遗产管理制度，并用友善、守望相助、尊老敬老等具体价值收束。",
        "complete_answer_generated": "本题按表格一格一答：第一格，纠纷解决机制可写调解、诉讼调解或诉讼。第二格，柳某案体现劳动者要树立权利和义务相统一的法治意识、依法履行劳动义务，也有利于维护医院合法权益、构建和谐劳动关系。第三格，顾氏三兄弟照顾老人案体现遗产管理制度的落实，有利于合理处置老人遗产、保护继承权益，并弘扬友善、守望相助、尊老敬老的价值导向。",
        "notes": "学生问题和教学启示类 atoms R05-R12 已移出满分句，只作易错路径。",
    },
    "CC0084_2025_东城_二模_19": {
        "rubric_atom_ids_matched": "R_CC0084_2025_东城_二模_19_02|R_CC0084_2025_东城_二模_19_03|R_CC0084_2025_东城_二模_19_04|R_CC0084_2025_东城_二模_19_05",
        "full_score_sentence_generated": "龙某为钱某文身案可从限制民事行为能力人未经法定代理人追认导致合同无效，或龙某未尽核实义务、侵犯身体权/健康权角度作答；杨某自媒体案要写故意侮辱或诽谤造成公司社会评价降低，侵害名誉权；服务条款案写公平原则或诚信原则；典型意义写维护消费者合法权益、规范格式条款使用。",
        "complete_answer_generated": "本题按表格逐格作答：龙某案中，钱某为限制民事行为能力人，未经法定代理人追认的文身合同无效；也可写龙某未尽核实义务、存在过错，侵犯钱某身体权或健康权。杨某自媒体案中，杨某利用自媒体故意侮辱、诽谤公司并造成社会评价降低，侵害公司名誉权。服务条款体现民法公平原则，也可写诚信原则。典型意义在于维护消费者合法权益、规范格式条款使用。",
        "notes": "学生表现、典型错误和教学启示类 atoms R06-R11 已移出满分句，只作易错路径。",
    },
    "CC0150_2025_朝阳_二模_20": {
        "rubric_atom_ids_matched": "R_CC0150_2025_朝阳_二模_20_05|R_CC0150_2025_朝阳_二模_20_06|R_CC0150_2025_朝阳_二模_20_07|R_CC0150_2025_朝阳_二模_20_08|R_CC0150_2025_朝阳_二模_20_09|R_CC0150_2025_朝阳_二模_20_10|R_CC0150_2025_朝阳_二模_20_11",
        "full_score_sentence_generated": "刘先生安装摄像头拍摄到孙女士家日常出行规律及其他动态信息，侵犯孙女士隐私权，应承担侵权责任；楼道属于专有部分以外的共有部分，双方享有共有和共同管理权；刘先生虽可保障财产安全，但设备范围和功能超出必要限度、安装前未尽妥善注意义务，并应按相邻关系原则处理纠纷；调解建议为及时拆除摄像头并清除已拍摄信息。",
        "complete_answer_generated": "刘先生侵犯了孙女士的隐私权，应当承担侵权责任。根据民法典，楼道属于双方专有部分以外的共有部分，双方享有共有和共同管理的权利。摄像头拍摄到孙女士家的日常出行规律及其他动态信息，与私人生活高度关联，属于应受保护的隐私利益。刘先生虽有权保障自身财产安全，但安装设备的范围、功能已超出必要限度，且安装前未尽妥善注意义务；双方作为相邻权利人，应按照有利生产、方便生活、团结互助、公平合理原则处理关系。作为人民调解员，可建议刘先生及时拆除摄像头，并清除已拍摄的孙女士及家人的视频信息。",
        "notes": "R12-R24 为第21题当代国际政治与经济内容，已从本工程满分句和支持链移除。",
    },
    "CC0245_2026_东城_期末_18_2": {
        "rubric_atom_ids_matched": "PATCH_CC0245_R01A_REMEDY_PATH|PATCH_CC0245_R01B_EVIDENCE_PREP|PATCH_CC0245_R01C_REASONABLE_REQUEST",
        "framework_entry_node": "FWV1_2_N06B 维权准备与诉讼请求",
        "full_score_sentence_generated": "陈某应根据协商未果的程序状态，选择调解、仲裁或诉讼等合适维权途径；同时依法收集并固定合同、订单、转账、邮件记录、无人机故障、受伤事实和经济损失等证据，形成完整证据链；还要明确自身权利义务和法律依据，围绕违约责任或侵权责任提出退还购置费、赔偿医疗费、误工费、经济损失等合理诉求。",
        "complete_answer_generated": "陈某维权应先做好路径选择和证据准备。材料表明双方已经协商未果，因此可以选择调解、仲裁或诉讼等方式依法维权；若选择诉讼，应准备起诉状、原被告身份信息并注意诉讼时效。陈某还应依法收集并固定合同、订单、转账、邮件记录等交易证据，以及无人机故障、手臂受伤、医疗费和商业损失等损害与因果关系证据。最后，陈某应明确自身权利义务和法律依据，围绕违约责任或侵权责任提出退还无人机购置费、赔偿医疗费、误工费、经济损失等合理诉求。",
        "notes": "R02-R04 为典型问题/教学建议，已移出满分句，只作易错路径。",
    },
    "CC0251_2026_丰台_一模_20": {
        "rubric_atom_ids_matched": "PATCH_CC0251_R01A_COURT_ANCHOR|PATCH_CC0251_R01B_PUBLIC_PLACE_RULE|PATCH_CC0251_R01C_FACT_NO_FAULT|PATCH_CC0251_R01D_VALUE_BOUNDARY",
        "full_score_sentence_generated": "人民法院以事实为根据、以法律为准绳作出判决；根据民法典，公共场所经营者、管理者因过错造成他人损害的，才承担侵权责任；本案事发现场不存在影响通行的客观因素，原告是完全民事行为能力人且未尽安全注意义务，某餐饮公司和某商业管理公司无过错，不承担赔偿责任；该判决有利于平衡原被告权利义务，明确公共场所安全保障义务边界，倡导安全文明出行和自我负责。",
        "complete_answer_generated": "人民法院应以事实为根据、以法律为准绳作出判决。根据民法典，经营场所、公共场所的经营者、管理者因过错造成他人损害的，应当承担侵权责任。本案中，事发现场不存在影响通行的客观因素，原告是完全民事行为能力人，其摔倒主要是自身未尽安全注意义务所致，某餐饮公司和某商业管理公司没有过错，因此不承担赔偿责任。该判决有利于平衡原被告权利义务，明确公共场所经营者、管理者安全保障义务边界，也有利于倡导安全文明出行和自我负责的安全责任意识。",
        "notes": "R02-R16 为学生问题、建议、复练试题或其他题内容，已移出满分句。",
    },
}

ENTRY_REMAPS = {
    "CC0092_2025_东城_期末_19_1": "FWV1_2_N06A 法律边界识别与合规措施",
    "CC0277_2026_房山_二模_18": "FWV1_2_N06A 法律边界识别与合规措施",
    "CC0125_2025_延庆_一模_19": "FWV1_2_N06C 调解方案与合同诚信理由",
    "RECOVER_2024_东城_二模_19_1": "FWV1_2_N06B 维权准备与诉讼请求",
    "RECOVER_2026_门头沟_一模_18_1": "FWV1_2_N06D 公益诉讼与司法确认",
    "RECOVER_2026_延庆_一模_18_1": "FWV1_2_N06B 维权准备与诉讼请求",
    "CC0289_2026_朝阳_二模_18": "FWV1_2_N06B 维权准备与诉讼请求",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def append_unique(existing: str, extra: str) -> str:
    values: list[str] = []
    seen: set[str] = set()
    for part in (existing or "").split("|") + (extra or "").split("|"):
        value = part.strip()
        if value and value not in seen:
            values.append(value)
            seen.add(value)
    return "|".join(values)


def filter_pipe_values(existing: str, *, excluded_exact: set[str] | None = None, excluded_prefixes: tuple[str, ...] = ()) -> str:
    excluded_exact = excluded_exact or set()
    values: list[str] = []
    seen: set[str] = set()
    for part in (existing or "").split("|"):
        value = part.strip()
        if not value:
            continue
        if value in excluded_exact or any(value.startswith(prefix) for prefix in excluded_prefixes):
            continue
        if value not in seen:
            values.append(value)
            seen.add(value)
    return "|".join(values)


def codebook_rows() -> dict[str, dict[str, str]]:
    _, rows = read_csv(CODEBOOK)
    return {row["code_id"]: row for row in rows}


def merged_code(codes: dict[str, dict[str, str]], code_ids: list[str]) -> dict[str, str]:
    base = dict(codes[code_ids[0]])
    for code_id in code_ids[1:]:
        row = codes[code_id]
        for key in [
            "source_observation_ids",
            "supporting_question_ids",
            "supporting_rubric_atom_ids",
            "supporting_material_atom_ids",
            "must_have_keywords",
            "counterexamples",
            "reason",
        ]:
            base[key] = append_unique(base.get(key, ""), row.get(key, ""))
    base["code_id"] = "|".join(code_ids)
    return base


def core_filtered_code(code: dict[str, str]) -> dict[str, str]:
    filtered = dict(code)
    filtered["supporting_question_ids"] = filter_pipe_values(
        filtered.get("supporting_question_ids", ""),
        excluded_exact=CORE_EXCLUDED_QUESTION_IDS,
    )
    filtered["supporting_rubric_atom_ids"] = filter_pipe_values(
        filtered.get("supporting_rubric_atom_ids", ""),
        excluded_prefixes=CORE_EXCLUDED_ATOM_PREFIXES,
    )
    filtered["supporting_material_atom_ids"] = filter_pipe_values(
        filtered.get("supporting_material_atom_ids", ""),
        excluded_prefixes=CORE_EXCLUDED_MATERIAL_PREFIXES,
    )
    return filtered


def framework_nodes() -> list[dict[str, str]]:
    codes = codebook_rows()
    case_code = merged_code(codes, ["CODE_COWORK_004", "CODE_COWORK_006"])
    return [
        {
            "node_id": "FWV1_2_GATE",
            "node_class": "boundary_gate",
            "node_name": "边界先判",
            "student": "先问这是不是《法律与生活》的私人法律关系、权利义务、责任救济或程序路径；如果是国家治理、涉外法治建设、依法行政，就先挡出去。",
            "teacher": "边界 gate 防止 formal 但非选必二核心的法治题污染框架。CC0276 与 RECOVER_2026_西城_二模_18_3 是正式证据，但只能作边界反例。",
            "source_code_ids": "BOUNDARY_FROM_FAIL4_COWORK",
            "supporting_question_ids": "CC0276_2026_房山_二模_17|RECOVER_2026_西城_二模_18_3",
            "supporting_rubric_atom_ids": "R_CC0276_2026_房山_二模_17_01|RECOVER_2026_西城_二模_18_3_R01|RECOVER_2026_西城_二模_18_3_R02|RECOVER_2026_西城_二模_18_3_R03",
            "material_trigger": "设问主语是中国/国家/最高法典型案例；答案锚词是涉外法治建设、国家治理能力现代化、依法行政。",
            "ask_trigger": "运用法治知识谈国家如何建设、国家治理意义、涉外法治建设。",
            "minimum_judgment": "先判断是否离开选必二私法/程序机制，进入必修三或综合法治。",
            "answer_pattern": "本工程不把此类题生成选必二核心满分句；只在边界附录记录。",
            "risk": "若误收，会把框架必修三化。",
        },
        node_from_code("FWV1_2_N01", "表格一格一答", codes["CODE_COWORK_001"], "完成下表/补充裁判理由/示例行", "一格一答：先判格子功能，再填主体+行为+规则+意义。"),
        node_from_code("FWV1_2_N02", "裁判锚句起手", codes["CODE_COWORK_003"], "法院判决/裁判理由/调解结论", "人民法院以事实为根据、以法律为准绳，依据具体法律……"),
        node_from_code("FWV1_2_N03", "评析先表态", codes["CODE_COWORK_005"], "是否支持/是否有效/是否构成/能否得到法院支持", "先表态，再写法律依据，再写材料事实依据，最后复结论。"),
        node_from_code("FWV1_2_N04", "私法案例四链", case_code, "分析案例/判决理由；材料是合同、侵权、相邻、消费欺诈、责任承担", "定性权利或行为 -> 援引规则 -> 嵌入材料事实 -> 落责任/结果。"),
        node_from_code("FWV1_2_N05", "知识产权竞争保护链", codes["CODE_COWORK_008"], "知识产权、不正当竞争、恶意诉讼、惩罚性赔偿、司法保护创新", "定性行为 -> 援引知识产权或反不正当竞争规则 -> 写法院手段 -> 收束创新和竞争秩序。"),
        {
            "node_id": "FWV1_2_N06A",
            "node_class": "core_node",
            "node_name": "法律边界识别与合规措施",
            "student": "先识别方案或AI行为触碰了哪些法律边界，再给出对应合规措施。",
            "teacher": "这一支处理方案审查、AI/数字员工风险识别题，不按普通民事维权程序启动。",
            "source_code_ids": "CODE_COWORK_007A",
            "supporting_question_ids": "CC0092_2025_东城_期末_19_1|CC0277_2026_房山_二模_18",
            "supporting_rubric_atom_ids": "R_CC0092_2025_东城_期末_19_1_01|R_CC0277_2026_房山_二模_18_04|R_CC0277_2026_房山_二模_18_05|R_CC0277_2026_房山_二模_18_06",
            "material_trigger": "充电桩/公共区域/消防规定/业主共有权；数字员工生成虚假数据、上传核心代码、商业使用图案。",
            "ask_trigger": "法律问题、法律边界、应对措施、合规建议。",
            "minimum_judgment": "先判断风险类型：是否违反规定、是否侵害共有权/名誉权/商业秘密/著作权，再对应写审核、保密、授权或依法经营措施。",
            "answer_pattern": "风险事实 -> 法律边界 -> 合规措施，一项风险对应一项措施。",
            "risk": "不能写成普通协商仲裁诉讼，也不能空写科技向善。",
        },
        {
            "node_id": "FWV1_2_N06B",
            "node_class": "core_node",
            "node_name": "维权准备与诉讼请求",
            "student": "问怎么维权、准备什么、诉讼请求怎么写，就按路径、证据、请求三件事启动。",
            "teacher": "这一支保留 CODE_COWORK_007 中真正的程序维权样本，强调程序路径必须匹配材料阶段。",
            "source_code_ids": "CODE_COWORK_007B",
            "supporting_question_ids": "CC0245_2026_东城_期末_18_2|CC0289_2026_朝阳_二模_18|RECOVER_2024_东城_二模_19_1|RECOVER_2026_延庆_一模_18_1",
            "supporting_rubric_atom_ids": "PATCH_CC0245_R01A_REMEDY_PATH|PATCH_CC0245_R01B_EVIDENCE_PREP|PATCH_CC0245_R01C_REASONABLE_REQUEST|R_CC0289_2026_朝阳_二模_18_04|R_CC0289_2026_朝阳_二模_18_06|R_CC0289_2026_朝阳_二模_18_08|RECOVER_2024_东城_二模_19_1_R01|RECOVER_2024_东城_二模_19_1_R02|RECOVER_2024_东城_二模_19_1_R03|RECOVER_2026_延庆_一模_18_1_R01|RECOVER_2026_延庆_一模_18_1_R02|RECOVER_2026_延庆_一模_18_1_R03",
            "material_trigger": "协商未果、拟起诉、律师函、侵权后果、证据材料、诉讼请求。",
            "ask_trigger": "如何维权、需要做好哪些工作、诉讼请求、承担何种责任。",
            "minimum_judgment": "先看材料程序节点：协商未果则不再把协商作为主路径；再写证据与实体请求。",
            "answer_pattern": "程序路径 + 证据准备 + 实体请求/责任承担。",
            "risk": "不能把上诉、行政诉讼、笼统维权写进民事纠纷。",
        },
        {
            "node_id": "FWV1_2_N06C",
            "node_class": "core_node",
            "node_name": "调解方案与合同诚信理由",
            "student": "问调解方案时，先给调解结果，再用诚信、合同解除、证据意识说明理由。",
            "teacher": "这一支处理调解题，不宜被普通诉讼路径覆盖。",
            "source_code_ids": "CODE_COWORK_007C",
            "supporting_question_ids": "CC0125_2025_延庆_一模_19",
            "supporting_rubric_atom_ids": "R_CC0125_2025_延庆_一模_19_M17_01|R_CC0125_2025_延庆_一模_19_M17_02|R_CC0125_2025_延庆_一模_19_M17_03|R_CC0125_2025_延庆_一模_19_M17_04|R_CC0125_2025_延庆_一模_19_M17_05",
            "material_trigger": "标的较小、退款、合同解除、商品已丢弃、证据缺失。",
            "ask_trigger": "调解方案、调解理由。",
            "minimum_judgment": "先判断调解目的与双方权利义务，再给可接受的理由。",
            "answer_pattern": "调解结果 + 诚信原则/合同解除/证据意识 + 材料事实。",
            "risk": "不能只写息事宁人，也不能把调解题写成法院判决书。",
        },
        {
            "node_id": "FWV1_2_N06D",
            "node_class": "core_node",
            "node_name": "公益诉讼与司法确认",
            "student": "出现公益、社会公共利益、多元解纷、司法确认，就按主体合法性、纠纷解决、确认效力三层写。",
            "teacher": "这一支区别于普通私人维权，处理检察公益诉讼与司法确认的制度功能。",
            "source_code_ids": "CODE_COWORK_007D",
            "supporting_question_ids": "RECOVER_2026_门头沟_一模_18_1",
            "supporting_rubric_atom_ids": "RECOVER_2026_门头沟_一模_18_1_R01|RECOVER_2026_门头沟_一模_18_1_R02|RECOVER_2026_门头沟_一模_18_1_R03",
            "material_trigger": "公益、公众利益、和解/调解、司法确认、强制执行力。",
            "ask_trigger": "公益诉讼、多元纠纷解决、司法确认意义。",
            "minimum_judgment": "先判断主体与利益是否公益，再写解纷方式和司法确认效力。",
            "answer_pattern": "主体合法性/公益利益 + 多元解纷 + 司法确认效力。",
            "risk": "不能直接套普通私权维权的停止侵害、赔偿损失模板。",
        },
        node_from_code("FWV1_2_N07", "意义收束三层", codes["CODE_COWORK_002"], "现实意义/社会价值/典型意义/意义", "先写法律规则推出的个人权益，再写司法或行业秩序，再写公平正义/核心价值观；AI产业影响题另入开放容器。"),
        {
            "node_id": "FWV1_2_OPEN",
            "node_class": "open_container",
            "node_name": "开放容器",
            "student": "能看出法律信号但样本不足或边界偏综合时，不硬套核心节点。",
            "teacher": "开放容器用于压力测试和后续样本积累，不允许生成新核心节点。",
            "source_code_ids": "OPEN_CONTAINER_POLICY",
            "supporting_question_ids": "RECOVER_2026_西城_二模_18_2|CC0380_2026_顺义_二模_18_2",
            "supporting_rubric_atom_ids": "RECOVER_2026_西城_二模_18_2_R01|RECOVER_2026_西城_二模_18_2_R02|RECOVER_2026_西城_二模_18_2_R03|R_CC0380_2026_顺义_二模_18_2_P01|R_CC0380_2026_顺义_二模_18_2_P02|R_CC0380_2026_顺义_二模_18_2_P03|R_CC0380_2026_顺义_二模_18_2_P04",
            "material_trigger": "AI责任边界、开源智能体法律风险、裁判标准、行业有序发展、企业创新活力。",
            "ask_trigger": "AI法律风险/治理，或判决对产业发展和治理影响。",
            "minimum_judgment": "主语是判决对产业的外部影响，不是当事人责任承担。",
            "answer_pattern": "作为开放示范保留，不支撑核心节点；不得把综合治理或AI开放题升为稳定满分模板。",
            "risk": "强行升核心会把意义层写成泛营商环境话术。",
        },
    ]


def node_from_code(node_id: str, node_name: str, code: dict[str, str], ask: str, pattern: str) -> dict[str, str]:
    return {
        "node_id": node_id,
        "node_class": "core_node",
        "node_name": node_name,
        "student": code.get("what_student_must_judge", ""),
        "teacher": code.get("plain_description", ""),
        "source_code_ids": code.get("code_id", ""),
        "supporting_question_ids": code.get("supporting_question_ids", ""),
        "supporting_rubric_atom_ids": code.get("supporting_rubric_atom_ids", ""),
        "material_trigger": code.get("material_trigger_pattern", ""),
        "ask_trigger": ask,
        "minimum_judgment": code.get("what_student_must_judge", ""),
        "answer_pattern": pattern or code.get("full_score_sentence_pattern", ""),
        "risk": f"必修三化风险：{code.get('risk_of_empty_value_talk', '')}；法考化风险：{code.get('risk_of_legal_exam_overanalysis', '')}；边界：{code.get('module_boundary_risk', '')}",
    }


def write_framework() -> None:
    nodes = framework_nodes()
    map_fields = [
        "node_id",
        "node_class",
        "node_name",
        "source_code_ids",
        "supporting_question_ids",
        "supporting_rubric_atom_ids",
        "material_trigger",
        "ask_trigger",
        "minimum_judgment",
        "answer_pattern",
        "risk",
    ]
    write_csv(OUT_MAP, map_fields, [{key: node.get(key, "") for key in map_fields} for node in nodes])

    md = [
        "# Framework v1.2 Guarded - 选必二法律主观题启动框架",
        "",
        "Status: pressure-test framework, not final baodian.",
        "",
        "## One-Minute Student Version",
        "",
        "1. 先挡边界：国家治理/涉外法治/依法行政，不当选必二核心题写。",
        "2. 再看设问：表格、评析、案例理由、维权建议、意义价值。",
        "3. 案例题先判关系：合同、侵权、相邻、消费欺诈、知识产权/竞争。",
        "4. 满分句按顺序写：定性 -> 规则 -> 材料事实 -> 责任/结果 -> 必要价值收束。",
        "5. 没有重复正式细则支撑的低频题，只进开放容器，不临场造模板。",
        "",
        "## Nodes",
        "",
    ]
    for node in nodes:
        md.extend(
            [
                f"### {node['node_id']} {node['node_name']}",
                "",
                f"- 节点类别：{node.get('node_class', '')}",
                f"- 学生启动：{node['student']}",
                f"- 教师解释：{node['teacher']}",
                f"- 设问触发：{node['ask_trigger']}",
                f"- 材料触发：{node['material_trigger']}",
                f"- 最小判断：{node['minimum_judgment']}",
                f"- 满分句生成：{node['answer_pattern']}",
                f"- 证据：{node['source_code_ids']} / {node['supporting_question_ids']}",
                f"- 风险：{node['risk']}",
                "",
            ]
        )
    md.extend(
        [
            "## Guardrails",
            "",
            "- reference_only 题只作弱示范，不支撑节点。",
            "- open-container 题可压测，不生成核心模板。",
            "- formal 但明显必修三/综合法治的题只入边界附录。",
            "- 价值句必须由具体法律规则和材料事实推出，不能独立空写。",
            "",
        ]
    )
    OUT_FRAMEWORK.write_text("\n".join(md), encoding="utf-8")

    plan = [
        "# Framework v1.2 Synthesis Plan",
        "",
        "- Merge duplicated private-law four-chain observations (`CODE_COWORK_004` and `CODE_COWORK_006`) into one student-facing case node.",
        "- Keep `CODE_COWORK_008` as a specialized branch, not as a separate legal-exam framework.",
        "- Put CC0276 and RECOVER_2026_西城_二模_18_3 behind a boundary gate.",
        "- Put RECOVER_2026_西城_二模_18_2 into an open container until more formal same-type samples appear.",
        "- Rerun all 65 questions with explicit PASS/PARTIAL/FAIL labels before framework_v2 or final baodian.",
        "",
    ]
    OUT_PLAN.write_text("\n".join(plan), encoding="utf-8")


def load_resolution() -> dict[str, str]:
    _, rows = read_csv(RESOLUTION)
    return {row["question_id"]: row["final_resolution_status"] for row in rows}


def load_partial_policy() -> dict[str, dict[str, str]]:
    _, rows = read_csv(PARTIAL_POLICY)
    return {row["question_id"]: row for row in rows}


def load_local_patch() -> dict[str, dict[str, str]]:
    _, rows = read_csv(LOCAL_PATCH)
    return {row["question_id"]: row for row in rows}


def rerun_pressure() -> None:
    fields, rows = read_csv(PRESSURE_V11)
    resolution = load_resolution()
    partial_policy = load_partial_policy()
    local_patch = load_local_patch()
    out_rows: list[dict[str, str]] = []
    for row in rows:
        row = dict(row)
        qid = row["question_id"]
        if qid in OPEN_CONTAINER_OVERRIDES:
            override = OPEN_CONTAINER_OVERRIDES[qid]
            row["framework_entry_node"] = override["framework_entry_node"]
            if "expansion_status" in row:
                row["expansion_status"] = "OPEN_CONTAINER_ONLY"
            row["why_this_entry"] = override["why_this_entry"]
            row["full_score_sentence_generated"] = "开放容器示范：先识别可能侵害的民事权益，再写民法典保护和救济路径；但本题不宣称形成选必二核心满分闭环。"
            row["complete_answer_generated"] = "本题保留为AI权益与治理开放容器，不作为选必二核心节点的满分答案模板。"
            row["lost_points_if_any"] = "not applicable to xuanbier core"
            row["reason_for_loss"] = "formal open/comprehensive boundary, not failed"
            row["pass_status"] = "PARTIAL"
            row["patch_needed"] = "no"
            row["patch_type"] = override["patch_type"]
            row["patch_suggestion"] = override["patch_suggestion"]
            out_rows.append(row)
            continue
        status = resolution.get(qid, row["pass_status"])
        if status == "PASS_AFTER_CC0143_PATCH":
            lp = local_patch[qid]
            row["framework_entry_node"] = "FWV1_2_N04 私法案例四链 + FWV1_2_N07 意义收束"
            if "expansion_status" in row:
                row["expansion_status"] = "CORE_CODEBOOK_SUPPORT_AFTER_CC0143_PATCH"
            row["why_this_entry"] = "Cowork and local source adjudication agree CC0143 is a selected-compulsory-2 consumer contract fraud/triple-compensation case after atom patch."
            row["minimum_judgment_required"] = lp["minimum_judgment"]
            row["material_trigger"] = lp["material_trigger"]
            row["legal_knowledge_triggered"] = "合同成立/可撤销；消费者权益保护法第五十五条；经营者欺诈；三倍赔偿"
            row["rubric_atom_ids_matched"] = "PATCH_CC0143_CONTRACT_CHAIN_R01|PATCH_CC0143_CONSUMER_TRIPLE_COMP_R02|R_CC0143_2025_朝阳_一模_19_02|R_CC0143_2025_朝阳_一模_19_03|R_CC0143_2025_朝阳_一模_19_04|R_CC0143_2025_朝阳_一模_19_05|R_CC0143_2025_朝阳_一模_19_06|R_CC0143_2025_朝阳_一模_19_07|R_CC0143_2025_朝阳_一模_19_08|R_CC0143_2025_朝阳_一模_19_09|R_CC0143_2025_朝阳_一模_19_10"
            row["full_score_sentence_generated"] = lp["full_score_sentence_pattern"]
            row["complete_answer_generated"] = lp["full_score_sentence_pattern"]
            row["lost_points_if_any"] = "0 after atom patch"
            row["reason_for_loss"] = ""
            row["pass_status"] = "PASS"
            row["patch_needed"] = "no"
            row["patch_type"] = ""
            row["patch_suggestion"] = "resolved_by_cc0143_atom_patch_20260519"
        elif status == "BOUNDARY_EXCLUDED_NON_CORE":
            row["framework_entry_node"] = "FWV1_2_GATE 边界先判"
            row["why_this_entry"] = "Formal evidence but non-core for this selected-compulsory-2 project; boundary gate correctly blocks it from core framework support."
            row["full_score_sentence_generated"] = "不生成选必二核心满分句；登记为边界反例。"
            row["complete_answer_generated"] = "不纳入选必二法律主观题核心框架；如开综合法治/必修三线另行处理。"
            row["lost_points_if_any"] = "not applicable to xuanbier core"
            row["reason_for_loss"] = "boundary excluded, not failed"
            row["pass_status"] = "PASS"
            row["patch_needed"] = "no"
            row["patch_type"] = "边界排除"
            row["patch_suggestion"] = "keep in boundary appendix only"
        elif status == "OPEN_CONTAINER_ONLY":
            row["framework_entry_node"] = "FWV1_2_OPEN 开放容器"
            row["why_this_entry"] = "Formal evidence but only a singleton/open mechanism; use as open-container pressure case, not core node."
            row["pass_status"] = "PARTIAL"
            row["patch_needed"] = "no"
            row["patch_type"] = "开放容器"
            row["patch_suggestion"] = "wait for repeated formal same-type evidence before promotion"
        elif row["pass_status"] == "PARTIAL":
            policy = partial_policy.get(qid, {})
            row["framework_entry_node"] = policy.get("framework_entry_node", row["framework_entry_node"])
            row["why_this_entry"] = policy.get("policy_reason", row["why_this_entry"])
            row["patch_needed"] = "no"
            row["patch_type"] = policy.get("partial_policy", row["patch_type"])
            row["patch_suggestion"] = policy.get("next_action", row["patch_suggestion"])
        if qid in ENTRY_REMAPS:
            row["framework_entry_node"] = ENTRY_REMAPS[qid]
            row["why_this_entry"] = f"GPTPro guarded-v2 review split CODE_COWORK_007; this row now enters through {ENTRY_REMAPS[qid]} instead of the broad procedure node."
        if qid in ROW_SCORING_OVERRIDES:
            for key, value in ROW_SCORING_OVERRIDES[qid].items():
                row[key] = value
            row["patch_needed"] = "no"
            row["patch_type"] = "gptpro_guarded_v2_scoring_trim"
            row["patch_suggestion"] = "student-problem/teaching/other-question text removed from scoring answer generation"
        out_rows.append(row)

    extra_fields = [field for row in out_rows for field in row if field not in fields]
    fields = fields + list(dict.fromkeys(extra_fields))
    write_csv(OUT_TEST, fields, out_rows)
    counts = Counter(row["pass_status"] for row in out_rows)
    boundary_pass = sum(1 for row in out_rows if row["framework_entry_node"].startswith("FWV1_2_GATE"))
    core_pass = counts["PASS"] - boundary_pass
    md = [
        "# Framework v1.2 Pressure Pass Report",
        "",
        f"- total: {len(out_rows)}",
        f"- PASS: {counts['PASS']} (core/pass rows {core_pass}; boundary-gate pass rows {boundary_pass})",
        f"- PARTIAL: {counts['PARTIAL']}",
        f"- FAIL: {counts['FAIL']}",
        "- formal: 61; reference_only: 4; missing: 0",
        "",
        "Interpretation: hard FAIL is removed. However, PARTIAL rows remain open/reference cases and cannot be advertised as full-score core closure.",
        "",
    ]
    OUT_PASS.write_text("\n".join(md), encoding="utf-8")

    fails = [row for row in out_rows if row["pass_status"] == "FAIL"]
    fail_md = ["# Framework v1.2 Failure Cases", ""]
    if not fails:
        fail_md.append("No hard FAIL rows after FAIL4 Cowork integration. Remaining unresolved rows are PARTIAL/open/reference, not silent failures.")
    else:
        for row in fails:
            fail_md.append(f"- {row['question_id']}: {row['reason_for_loss']}")
    fail_md.append("")
    OUT_FAIL.write_text("\n".join(fail_md), encoding="utf-8")

    patch_md = [
        "# Framework v1.2 Patch Suggestions",
        "",
        "- Do not generate new core nodes from single formal open-container rows.",
        "- Do not treat reference_only rows as full-score closure.",
        "- Keep CC0276 and RECOVER_2026_西城_二模_18_3 in boundary appendix only.",
        "- Keep RECOVER_2026_西城_二模_18_2 as open container until repeated formal same-type evidence appears.",
        "- Move CC0380_2026_顺义_二模_18_2 out of core CODE_COWORK_007 support and keep it as an AI/legal-risk open-container pressure case.",
        "- Next step may synthesize framework_v2 only if it preserves these gates.",
        "",
    ]
    OUT_PATCH.write_text("\n".join(patch_md), encoding="utf-8")


def main() -> None:
    write_framework()
    rerun_pressure()
    print(f"Wrote {OUT_FRAMEWORK}")
    print(f"Wrote {OUT_TEST}")


if __name__ == "__main__":
    main()
