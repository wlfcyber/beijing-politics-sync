#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import datetime as dt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = dt.datetime.now().strftime("%Y%m%d")
STAMP = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def clean(s: str | None) -> str:
    return " ".join((s or "").replace("\n", " ").split())


def short(s: str | None, n: int = 220) -> str:
    s = clean(s)
    return s if len(s) <= n else s[: n - 1] + "…"


questions = {r["question_id"]: r for r in read_csv(ROOT / "04_merge_audit/merged_subjective_law_questions.csv")}
rubrics = read_csv(ROOT / "04_merge_audit/merged_rubric_atoms_subjective.csv")
materials = read_csv(ROOT / "04_merge_audit/merged_material_atoms_subjective.csv")
pressure_rows = read_csv(ROOT / "10_framework_validation/gptpro_prior_framework_v0_65_question_pressure_test_20260520.csv")
pressure = {r["question_id"]: r for r in pressure_rows}

rubrics_by_q: dict[str, list[dict[str, str]]] = {}
for r in rubrics:
    rubrics_by_q.setdefault(r["question_id"], []).append(r)

materials_by_q: dict[str, list[dict[str, str]]] = {}
for r in materials:
    materials_by_q.setdefault(r["question_id"], []).append(r)


REFERENCE_ONLY = {"CC0040_2024_海淀_一模_19", "CC0162_2025_海淀_一模_18", "CC0311_2026_海淀_二模_18_2", "CC0353_2026_西城_期末_17"}
LOW_FREQ = {"CC0011_2024_丰台_二模_17", "CC0254_2026_丰台_二模_18", "CC0332_2026_石景山_二模_19", "CC0340_2026_西城_一模_17", "RECOVER_2024_东城_一模_19"}
BOUNDARY_OPEN = {"CC0276_2026_房山_二模_17", "RECOVER_2026_西城_二模_18_3", "CC0380_2026_顺义_二模_18_2", "RECOVER_2026_西城_二模_18_2"}
FORCE_SOURCE_CHECK = {"CC0251_2026_丰台_一模_20", "CC0283_2026_朝阳_一模_18"}

BAD_RUBRIC_MARKERS = [
    "学生问题",
    "建议：",
    "教学建议",
    "答题逻辑",
    "字迹",
    "复练",
    "slide",
    "两个大局",
    "识变",
    "主要矛盾",
]


def clean_rubrics_for(qid: str) -> list[dict[str, str]]:
    rows = rubrics_by_q.get(qid, [])
    out: list[dict[str, str]] = []
    for r in rows:
        rid = r["rubric_atom_id"]
        txt = r["rubric_or_answer_phrase"]
        if qid == "CC0277_2026_房山_二模_18":
            suffix = rid.rsplit("_", 1)[-1]
            # Only the law sub-question atoms are allowed. R_07-R_11 are 必修四.
            if suffix.isdigit() and int(suffix) > 6:
                continue
        if qid == "CC0251_2026_丰台_一模_20":
            # Claude Opus source check: only R_01 is the actual scoring text.
            # Keep it even though OCR carried slide labels at the tail.
            if rid.endswith("_01"):
                out.append(r)
            continue
        if any(marker in txt for marker in BAD_RUBRIC_MARKERS):
            continue
        out.append(r)
    return out


def rubric_ids_for(qid: str, max_n: int = 10) -> str:
    return "|".join(r["rubric_atom_id"] for r in clean_rubrics_for(qid)[:max_n])


def rubric_lines_for(qid: str, max_n: int = 8) -> str:
    rows = clean_rubrics_for(qid)[:max_n]
    if not rows:
        return "- 当前无清洗后可用细则原子，需回源。"
    return "\n".join(f"- `{r['rubric_atom_id']}`：{short(r['rubric_or_answer_phrase'], 200)}" for r in rows)


def role_for(qid: str) -> str:
    if qid in REFERENCE_ONLY:
        return "reference_only_locked"
    if qid in LOW_FREQ:
        return "container_only"
    if qid in BOUNDARY_OPEN:
        return "boundary_open_only"
    p = pressure.get(qid, {})
    if qid in FORCE_SOURCE_CHECK or p.get("pass_status") == "PARTIAL_SOURCE_CHECK":
        return "source_check_pending"
    if p.get("pass_status") == "PASS_CANDIDATE":
        return "core_support"
    if p.get("pass_status") == "PARTIAL_LOW_FREQ_CONTAINER":
        return "container_only"
    return "pending"


NODES = [
    {
        "id": "LAW_V5_1_N01",
        "name": "一格一答",
        "line": "表格题先数空格，看栏目名；一个空只答一件事。",
        "trigger": "表格、完成下表、参考示例、补充完整、裁判要点。",
        "rule": "每个案例的意义分开写；机制格、理由格、结果格、意义格不能串答案。",
        "sentence": "机制格写程序事实；理由格写规则+事实；意义格写保护谁、规范谁、弘扬什么。",
        "qids": ["CC0077_2025_东城_一模_19", "CC0084_2025_东城_二模_19", "CC0289_2026_朝阳_二模_18", "RECOVER_2025_海淀_二模_18", "RECOVER_2026_通州_一模_20"],
    },
    {
        "id": "LAW_V5_1_N02",
        "name": "分关系·定责任",
        "line": "责任题先判关系：合同、侵权、消费、劳动、相邻。",
        "trigger": "法律责任、判决理由、是否赔偿、是否承担责任、合同成立、违约、侵权。",
        "rule": "先表态，再写关系；混合题分段写，不把合同和侵权糊成一段；法律名称要写全称。",
        "sentence": "某请求应予支持/不支持。甲乙形成某法律关系，某责任成立要满足某条件；材料中某事实符合/不符合条件，所以某方承担/不承担某责任。",
        "qids": ["CC0143_2025_朝阳_一模_19", "CC0305_2026_海淀_一模_18_3", "CC0063_2024_西城_二模_16", "CC0251_2026_丰台_一模_20", "CC0244_2026_东城_期末_18", "CC0002_2024_丰台_一模_17", "CC0200_2025_西城_二模_18"],
    },
    {
        "id": "LAW_V5_1_N03",
        "name": "认产权·抓侵权",
        "line": "创新题先认保护对象，再抓侵害行为。",
        "trigger": "知识产权、著作权、商标、商业秘密、技术秘密、植物新品种、数据、不正当竞争、保护创新。",
        "rule": "创新活力只能放最后，前面必须有具体权利、具体行为、具体司法手段。",
        "sentence": "某成果受法律保护；材料中某主体未经许可/不诚信实施某行为，侵害权利人权益或竞争秩序；法院通过停止侵害、赔偿、惩罚性赔偿、调解或规制恶意诉讼保护创新。",
        "qids": ["CC0229_2026_东城_一模_18", "CC0283_2026_朝阳_一模_18", "CC0103_2025_丰台_一模_19", "CC0137_2025_昌平_二模_20", "CC0206_2025_西城_期末_19"],
    },
    {
        "id": "LAW_V5_1_N04",
        "name": "排维权步骤",
        "line": "维权题排路径、证据、请求、效力。",
        "trigger": "如何维权、调解、仲裁、诉讼、起诉状、举证、公益诉讼、司法确认。",
        "rule": "先判程序阶段；再判主体；最后写证据、请求和法律效力。公益诉讼不能写成个人维权。",
        "sentence": "当事人/公益组织可通过某路径解决纠纷，准备某类证据和诉讼材料；经法院确认的调解或和解协议具有强制执行力。",
        "qids": ["RECOVER_2026_门头沟_一模_18_1", "CC0245_2026_东城_期末_18_2", "CC0125_2025_延庆_一模_19", "CC0150_2025_朝阳_二模_20", "CC0223_2025_顺义_一模_19"],
    },
    {
        "id": "LAW_V5_1_N05",
        "name": "划风险边界",
        "line": "风险题一项风险配一条规则和一项措施。",
        "trigger": "法律风险、法律边界、应对措施、合规、涉嫌违法。",
        "rule": "只看设问触发，不看题材触发；AI 宏观产业影响进开放容器，不进本卡。",
        "sentence": "材料中的某行为存在某法律风险，触碰某法律边界；相关主体应采取某措施，依法划清权利义务边界。",
        "qids": ["CC0277_2026_房山_二模_18", "RECOVER_2025_丰台_二模_19_2", "RECOVER_2026_延庆_一模_18_1", "RECOVER_2026_房山_一模_17_1"],
    },
    {
        "id": "LAW_V5_1_N06",
        "name": "推价值",
        "line": "价值从本案推出，不是最后补口号。",
        "trigger": "意义、价值、作用、认识、如何推动、如何护航。",
        "rule": "每个价值词前面都要有“因为本案……”。消费案不乱写法治国家，摔倒案不乱写市场秩序。",
        "sentence": "因为本案【具体处理】保护了【具体主体】，规范了【具体行为/行业】，所以弘扬了【与本案直接相关的价值】。",
        "qids": ["CC0063_2024_西城_二模_16", "CC0103_2025_丰台_一模_19", "CC0251_2026_丰台_一模_20", "CC0229_2026_东城_一模_18", "CC0143_2025_朝阳_一模_19"],
    },
]


SAMPLE_RUNS = {
    "CC0077_2025_东城_一模_19": {
        "entry": "一格一答，叠加排维权步骤、推价值",
        "judgment": "先数空格和栏目；案件一写解决机制，案件二和案件三分别写意义，不能合并。",
        "layer": "案件一：装修合同纠纷进入诉讼程序，法官释法析理促成赔偿；案件二：医院培训协议、柳某提前离职和仲裁驳回返还请求；案件三：顾氏三兄弟事实照料孤寡老人，申请遗产管理并获适当分配。",
        "answer": "案件一的解决机制可写调解、诉讼调解或诉讼，因为该案已进入诉讼程序，并通过法院出具调解书方式化解纠纷。柳某与医院案的意义应分两层：对劳动者而言，有利于树立权利和义务相统一的法治意识，督促劳动者依法依约履行义务；对医院而言，有利于维护用人单位合法权益，构建和谐劳动关系。顾氏三兄弟案也要单独分层：从制度看，遗产管理制度有利于维护公民合法财产权利和继承秩序；从价值看，对事实扶养人给予适当遗产分配，有利于弘扬社会主义核心价值观和敬老扶弱的中华优秀传统美德。",
        "risk": "漏写顾氏三兄弟案就直接丢掉表格后半题；每个案例意义必须分开。",
    },
    "CC0143_2025_朝阳_一模_19": {
        "entry": "起手表态 + 分关系·定责任 + 推价值",
        "judgment": "王某请求应支持；先写合同成立，再写合同可撤销/撤销请求，再写《消费者权益保护法》下欺诈赔偿。",
        "layer": "付款出票是合同成立；页面优惠与实际票价差额、技术搭售 10 元红包、无法知悉且无法拒绝，是欺诈和意思表示不真实；法院支持请求。",
        "answer": "王某的诉讼请求应予支持。王某通过平台购买机票并付款，机票已经出票，双方合同成立；但合同成立不等于合同当然有效。A 公司通过技术手段擅自搭售 10 元外卖红包，使王某不能清楚知悉费用细节且无法拒绝，属于欺诈，使消费者在违背真实意思的情况下订立合同，王某有权请求人民法院撤销该合同。依据《消费者权益保护法》，经营者提供商品或者服务有欺诈行为的，应按照消费者要求增加赔偿；因此法院支持王某退款和惩罚性赔偿请求。该判决有利于维护消费者知情权、自主选择权和公平交易权，规范在线文旅平台经营行为。",
        "risk": "《消费者权益保护法》必须写全称；不能只写“保护法”；不能漏合同可撤销和请求撤销合同。",
    },
    "CC0229_2026_东城_一模_18": {
        "entry": "认产权·抓侵权，叠加排维权步骤、推价值",
        "judgment": "法院用调解、惩罚性赔偿、规制恶意诉讼三种司法手段守护创新。",
        "layer": "专利权归属纠纷以调解减少内耗；植物新品种侵权以惩罚性赔偿提高成本；恶意诉讼以驳回谴责维护司法与创新秩序。",
        "answer": "人民法院坚持以事实为根据、以法律为准绳，发挥司法裁判导向作用。案例一中，法院通过诉讼调解化解专利权归属纠纷，提高纠纷解决效率，让创新主体回归研发。案例二中，法院对故意侵害植物新品种权行为适用惩罚性赔偿，提高侵权违法成本，保护知识产权。案例三中，法院驳回并谴责恶意诉讼，规制滥用诉权行为，维护司法秩序和创新环境。",
        "risk": "不要只写新质生产力，要逐案写司法手段。",
    },
    "CC0277_2026_房山_二模_18": {
        "entry": "划风险边界；仅处理 18(1) 法律子题",
        "judgment": "这是风险—边界—措施题；只引用 R_01-R_06，哲学 R_07-R_11 不进法律答案。",
        "layer": "虚假负面数据文章；上传核心代码；AI 图案商用。",
        "answer": "数字员工生成虚假负面数据文章，可能构成商业诋毁并侵犯相关公司的名誉权，应履行审核义务、依法经营。将公司核心代码上传公共 AI 平台，可能造成商业秘密泄露，应完善保密措施并与平台签订保密协议。数字员工设计图案直接用作商业用途，可能侵犯他人著作权或外观设计权，应进行权利审核并取得必要授权。",
        "risk": "这是跨模块题，法律答案只做 18(1)；不要把联系、发展、扬弃等哲学细则拿来支撑法律框架。",
    },
    "RECOVER_2026_门头沟_一模_18_1": {
        "entry": "排维权步骤，叠加开放容器的公益公共利益写法",
        "judgment": "环境公益诉讼题先判适格主体、多元解纷和司法确认强制执行力。",
        "layer": "公益组织起诉；法院审查首份和解协议不足以保护公共利益；技术论证后达成调解协议；调解书履行并跟踪修复。",
        "answer": "从诉讼主体看，公益社会组织依法提起环境民事公益诉讼，目的在于维护生态环境公共利益。从纠纷解决方式看，本案通过和解、司法调解、诉讼等多元方式消除损害风险。从法律效力看，经人民法院依法确认有效的和解或调解协议具有强制执行效力，法院持续跟踪修复履行，有助于切实维护生态环境公共利益。",
        "risk": "不能写成个人维权或普通生态意义。",
    },
    "CC0305_2026_海淀_一模_18_3": {
        "entry": "起手表态 + 分关系·定责任",
        "judgment": "支持原告诉讼请求；分隐私权侵权链和消费欺诈链两段写。",
        "layer": "包间活动具有私密性，公开监控和聊天信息侵害隐私权；夸大治疗功效诱导消费，损害知情权并构成欺诈。",
        "answer": "原告诉讼请求应予支持。任何组织或者个人不得以刺探、侵扰、泄露、公开等方式侵害他人的隐私权；商家公开包厢监控录像和聊天信息，构成对消费者隐私权的侵害，应承担停止侵权、赔礼道歉等侵权责任。经营者应保护消费者知情权，提供真实全面信息，不得作虚假或者引人误解的宣传；赵某夸大治疗功效诱导消费，构成欺诈，应退款并承担惩罚性赔偿责任。",
        "risk": "设问仍待 OCR 回补，正式宝典前必须补真实设问。",
    },
    "CC0063_2024_西城_二模_16": {
        "entry": "推价值，叠加分关系·定责任",
        "judgment": "意义来自首单支持、加购不支持的权利保护与权利边界。",
        "layer": "首单合理消费，应支持惩罚性赔偿；后续明知问题仍大量加购，超出正常生活需要，不支持；判决平衡食品安全和经营秩序。",
        "answer": "经营者应依法、诚信经营，保护消费者合法权益。人民法院支持甲就首单购买行为适用食品安全法中的惩罚性赔偿请求，打击违法生产经营行为，维护消费者合法权益。同时，民事主体行使民事权利不能超过正当界限，不得滥用民事权利损害他人合法权益；甲的加购行为超出正常生活消费需要，法院不支持其就加购部分提出的惩罚性赔偿请求，有利于引导消费者依法、诚信、理性维权。该判决平衡了保证食品安全和维护生产经营秩序两种价值取向。",
        "risk": "不能只写保护消费者；必须写权利边界和理性维权。",
    },
    "CC0251_2026_丰台_一模_20": {
        "entry": "起手表态 + 分关系·定责任 + 推价值",
        "judgment": "被告不承担赔偿责任；仅 R_01 可用，其余教学反思和复练题不得进证据。",
        "layer": "公共场所安全保障义务有合理限度；现场无影响通行客观因素；原告完全民事行为能力且自身未尽注意义务。",
        "answer": "人民法院以事实为根据、以法律为准绳作出判决。依据民法典，公共场所经营者、管理者因过错造成他人损害的，应承担侵权责任。本案中，被告安全保障义务应保持在合理限度内，且证据表明事发现场不存在影响原告通行的客观因素；原告作为完全民事行为能力人，摔倒系自身未尽安全注意义务所致，因此被告无过错，不应承担赔偿责任。该判决有利于平衡双方权利义务，明确公共场所经营者、管理者安全保障义务边界，倡导安全文明出行和自我负责的安全责任意识，弘扬社会主义核心价值观。",
        "risk": "不要写市场秩序、优化营商环境；ask_text 需回源补真实设问。",
    },
    "CC0283_2026_朝阳_一模_18": {
        "entry": "认产权·抓侵权 + 排维权步骤 + 推价值",
        "judgment": "当前材料字段疑似装入答案，需回源；按清洗后 rubric 先作临时样章。",
        "layer": "调解降低诉讼成本；惩罚性赔偿提高侵权成本；规制不诚信诉讼；整合司法手段护航新质生产力。",
        "answer": "人民法院通过特邀第三方调解，高效化解知识产权纠纷，既维护当事人合法权益，又降低诉讼成本、提高纠纷解决效率。针对故意侵权行为，法院适用惩罚性赔偿规定，提高侵权违法成本，维护公平竞争的市场秩序。依据民法公平、诚信等基本原则，法院谴责并规制不诚信诉讼行为，保障诉讼秩序和经营秩序，避免“假维权”拖垮“真创新”。通过整合调解、惩罚、规制等司法手段，法院保护知识产权人的合法权益，兼顾社会公共利益，为新质生产力发展提供稳定、可预期的法治环境。",
        "risk": "这题必须先回源，因为设问/材料字段和 rubric 口径不一致。",
    },
    "CC0103_2025_丰台_一模_19": {
        "entry": "认产权·抓侵权 + 推价值",
        "judgment": "意义分企业、市场、司法、社会四层；法治中国建设要写，但必须有铺垫。",
        "layer": "技术秘密侵权；2 倍惩罚性赔偿和 6.4 亿判赔；停止侵害、迟延履行金等开创探索；典型案例示范。",
        "answer": "本案判决维护原告方合法权益，严惩侵害技术秘密行为，保护知识产权。法院适用 2 倍惩罚性赔偿，提高侵权成本，规范市场竞争秩序，营造公平市场环境，以法治力量鼓励创新。作为人民法院保护科技创新典型案例，本案为同类案件提供范例，有利于提升审判质量和效率、增强司法公信力；它还引导公民和企业依法办事，增强民众法治信仰，推动法治中国建设。",
        "risk": "不能裸写法治中国建设；要接在企业、市场、司法三层之后。",
    },
}


def material_core(qid: str) -> str:
    atoms = [short(a["material_phrase"], 90) for a in materials_by_q.get(qid, [])[:5]]
    return "；".join(atoms) if atoms else short(questions.get(qid, {}).get("material_text", ""), 300)


def write_evidence_map() -> None:
    rows = []
    for n in NODES:
        for qid in n["qids"]:
            role = role_for(qid)
            rows.append(
                {
                    "node_id": n["id"],
                    "node_name": n["name"],
                    "question_id": qid,
                    "evidence_level": questions.get(qid, {}).get("evidence_level", ""),
                    "pass_status": pressure.get(qid, {}).get("pass_status", ""),
                    "role_in_node": role,
                    "clean_rubric_atom_ids": rubric_ids_for(qid),
                    "cleaning_note": "CC0277 only law sub-question atoms; CC0251 only R_01; teaching reflections/cross-module atoms filtered.",
                }
            )
    write_csv(
        ROOT / f"09_candidate_frameworks/framework_v5_1_evidence_map_{TODAY}.csv",
        rows,
        ["node_id", "node_name", "question_id", "evidence_level", "pass_status", "role_in_node", "clean_rubric_atom_ids", "cleaning_note"],
    )


def write_batch_plan() -> None:
    rows = []
    for r in pressure_rows:
        qid = r["question_id"]
        if qid in REFERENCE_ONLY:
            batch = "reference_only锁死"
            action = "只作参考，不进核心、不进句库。"
        elif qid in LOW_FREQ:
            batch = "低频formal容器"
            action = "可教，不升核心。"
        elif qid in BOUNDARY_OPEN:
            batch = "边界/开放容器"
            action = "作为刹车题，不进私法核心。"
        elif qid in FORCE_SOURCE_CHECK or r["pass_status"] == "PARTIAL_SOURCE_CHECK":
            batch = "先回源补设问/清洗题面"
            action = "补真实设问、页码和题干后再定。"
        elif r["pass_status"] == "PASS_CANDIDATE":
            batch = "核心扩展候选"
            action = "V5.1 样章返工后进入35题扩展。"
        else:
            batch = r["pass_status"]
            action = r.get("pressure_notes", "")
        rows.append(
            {
                "question_id": qid,
                "evidence_level": r["evidence_level"],
                "old_pass_status": r["pass_status"],
                "v5_1_batch": batch,
                "v5_1_action": action,
                "primary_node_old": r["primary_node"],
            }
        )
    write_csv(
        ROOT / f"09_candidate_frameworks/v5_1_batch_plan_{TODAY}.csv",
        rows,
        ["question_id", "evidence_level", "old_pass_status", "v5_1_batch", "v5_1_action", "primary_node_old"],
    )


def node_md(n: dict[str, object]) -> str:
    qids = n["qids"]  # type: ignore[index]
    assert isinstance(qids, list)
    return f"""## {n['id']}：{n['name']}

学生先记：{n['line']}

触发词：{n['trigger']}

动作铁律：{n['rule']}

满分句骨架：{n['sentence']}

支持题号：{', '.join(qids)}
"""


def sample_md(qid: str, idx: int) -> str:
    q = questions[qid]
    s = SAMPLE_RUNS[qid]
    return f"""## 样章 {idx}：{qid}

题源：{q.get('year')} {q.get('district')} {q.get('exam_stage')} 第 {q.get('question_no')} 题

证据等级：{q.get('evidence_level')}；V5.1 角色：{role_for(qid)}

设问：{clean(q.get('ask_text')) or '设问待回源补正；当前样章仅作动作卡校准。'}

### 一、框架入口

{s['entry']}

### 二、材料分层

{s['layer']}

### 三、最小必要判断

{s['judgment']}

### 四、清洗后细则原子

{rubric_lines_for(qid)}

### 五、考场版满分答案

{s['answer']}

### 六、易错刹车

{s['risk']}
"""


def write_docs() -> None:
    framework = f"""# 选必二《法律与生活》主观题框架 V5.1：六张动作卡 + 起手铁律

生成时间：{STAMP}

本稿根据 GPTPro 对策、Claude Opus 4.7 复核和 Codex 内部零基础学生压测修订。V5 的七张卡降并为：**六张并列动作卡 + 一条通用起手铁律**。

## 首屏口诀

圈主体 → 抓行为 → 认设问、选卡 → 先表态 → 摆规则、配事实 → 收责任或价值。

## 通用起手铁律

凡设问出现“是否支持 / 能否得到支持 / 是否有效 / 是否构成 / 判决理由 / 评析”，答案第一句必须先表态：

- 某请求应予支持 / 不予支持。
- 某行为构成 / 不构成侵权、违约、欺诈、不正当竞争。
- 某合同成立、有效、无效或可撤销。
- 法院题可写：人民法院以事实为根据、以法律为准绳。不要写反。

表态后，立刻进入六张卡之一写规则、材料、责任或价值。

## 六张动作卡

{chr(10).join(node_md(n) for n in NODES)}

## 开放容器清单

看到这些信号，先停手，不要套合同侵权劳动模板：

- 低频 formal 容器：CC0011 生态保护、CC0254 法治德治结合、CC0332 校园欺凌惩教、CC0340 绿色发展、RECOVER_2024_东城_一模_19 诉讼时效。
- 边界题：CC0276 涉外法治、RECOVER_2026_西城_二模_18_3 国家治理能力现代化、CC0380 开源智能体综合治理。
- AI 宏观影响：RECOVER_2026_西城_二模_18_2 只进开放容器。
- reference_only：CC0040、CC0162、CC0311、CC0353 锁死参考，不支撑核心。

开放容器三句法：制度或规则是什么；材料中怎么体现；它发挥什么具体作用。
"""
    (ROOT / f"09_candidate_frameworks/framework_v5_1_action_card_candidate_{TODAY}.md").write_text(framework, encoding="utf-8")

    student = f"""# 选必二法律主观题 V5.1 学生一页纸

生成时间：{STAMP}

## 20 秒启动

圈主体 → 抓行为 → 认设问、选卡 → 先表态 → 摆规则、配事实 → 收责任或价值。

## 先圈四样

- 主体：谁和谁、谁受损、谁裁判。
- 行为：签、买、付、退、用、传、抓取、辞退、搭售、调解、起诉、判决。
- 请求：支持吗、赔吗、有效吗、构成吗、怎么维权。
- 尾词：表格、判决理由、法律责任、保护创新、如何维权、法律风险、意义。

## 先表态

判决/评析/是否题，第一句先写结论。法院题可以写“人民法院以事实为根据、以法律为准绳”，不要写反。

## 六张动作卡

1. 一格一答：表格题一个空只答一件事，每个案例意义分开写。
2. 分关系·定责任：先判合同、侵权、消费、劳动、相邻，再写规则、事实、责任。
3. 认产权·抓侵权：先判保护对象，再抓侵害行为，最后写司法保护创新。
4. 排维权步骤：写路径、证据、请求、效力；公益诉讼先写公共利益和适格主体。
5. 划风险边界：一项风险、一条规则、一项措施；AI 宏观影响进容器。
6. 推价值：每个价值词前面都要有“因为本案……”，价值从本案推出。

## 最小规则句库

- 消费欺诈：经营者应真实全面告知，不得虚假宣传、强制搭售、欺诈消费者；依据《消费者权益保护法》，欺诈可退赔并承担惩罚性赔偿。
- 隐私权：不得以刺探、侵扰、泄露、公开等方式侵害他人隐私权，公开私密空间信息应承担侵权责任。
- 技术秘密/商业秘密：未经许可获取、披露、使用他人技术信息，构成商业秘密侵害或不正当竞争，可停止侵害、赔偿并适用惩罚性赔偿。
- 调解：依法自愿调解能节约诉讼成本、缓和对立、保留合作可能，减少纠纷对生活经营或创新的干扰。
- 公益诉讼：公共利益受损风险 → 适格主体起诉 → 法院审查协议是否足以保护公共利益 → 调解书/判决履行 → 持续监督修复。
- 责任边界：先看有没有法定义务、过错、损害和因果关系；该支持就支持，该限制就限制，不能把所有损失都推给对方。

## 禁止

- 不能不表态直接分析。
- 不能把法律名称写简称、写错。
- 不能跨格写大段。
- 摔倒案、继承案等不要乱写“优化营商环境”“市场秩序”。
- 没有材料铺垫，不要裸写“法治社会、法治中国、全面依法治国”。
"""
    (ROOT / f"11_final_framework/framework_v5_1_student_one_page_{TODAY}.md").write_text(student, encoding="utf-8")

    samples = f"# V5.1 十题样章：清洗后版本\n\n生成时间：{STAMP}\n\n"
    for i, qid in enumerate(SAMPLE_RUNS, 1):
        samples += sample_md(qid, i) + "\n"
    (ROOT / f"10_framework_validation/framework_v5_1_first10_sample_runs_{TODAY}.md").write_text(samples, encoding="utf-8")

    csv_rows = []
    for qid, s in SAMPLE_RUNS.items():
        q = questions[qid]
        csv_rows.append(
            {
                "question_id": qid,
                "year": q.get("year", ""),
                "district": q.get("district", ""),
                "exam_stage": q.get("exam_stage", ""),
                "question_no": q.get("question_no", ""),
                "role": role_for(qid),
                "framework_entry": s["entry"],
                "minimum_judgment": s["judgment"],
                "clean_rubric_atom_ids": rubric_ids_for(qid),
                "full_score_answer": s["answer"],
                "risk_warning": s["risk"],
            }
        )
    write_csv(
        ROOT / f"10_framework_validation/framework_v5_1_first10_sample_runs_{TODAY}.csv",
        csv_rows,
        ["question_id", "year", "district", "exam_stage", "question_no", "role", "framework_entry", "minimum_judgment", "clean_rubric_atom_ids", "full_score_answer", "risk_warning"],
    )

    baodian = f"""# 选必二法律主观题满分宝典 V5.1 十题样章版

生成时间：{STAMP}

## 第一部分：学生框架

{student}

## 第二部分：十题逐题运行

{samples}

## 当前状态

V5.1 已吸收 Claude Opus 复核硬问题，完成样章返工和证据清洗，但仍是十题样章版。下一步应先用干净题面重新做零基础压测，再扩展 35 道核心题。
"""
    (ROOT / f"12_final_baodian/选必二法律主观题满分宝典_v5_1_十题样章_{TODAY}.md").write_text(baodian, encoding="utf-8")


def write_decision() -> None:
    decision = f"""# V5.1 修订决策记录

生成时间：{STAMP}

## 触发来源

- GPTPro：V4 不修补，退回学生动作卡重写。
- Claude Opus：V5 架构 CONDITIONAL_PASS，但十题样章漏分、证据映射污染，未清洗前不得进入 35 核心扩展。
- Codex 内部零基础学生：V5 能让学生不空不乱，但缺最小法律规则句库。

## 已执行修订

1. 七张卡降并为“六张并列动作卡 + 起手表态铁律”。
2. `先判后证` 不再是并列入口，而是所有判决/评析/是否题的第一句规则。
3. `切责成链` 改为 `分关系·定责任`。
4. `护创新` 改为 `认产权·抓侵权`。
5. `走救济` 改为 `排维权步骤`。
6. `补价值` 改为 `推价值`，并新增“因为本案……”强制句式。
7. 清洗 CC0277：仅 R_01-R_06 可作法律证据；哲学 R_07-R_11 删除。
8. 清洗 CC0251：仅 R_01 可作本题证据；教学反思、复练题、必修一话术删除。
9. RECOVER_2026_西城_二模_18_2 从核心降为 AI 宏观开放容器。
10. 低频 formal 和边界题物理列入开放容器。
11. CC0077、CC0143、CC0103 样章按 Claude 指出漏分点返工。

## 未关闭

- CC0077、CC0277、CC0305 等设问字段仍需回源补正。
- CC0283、CC0251 因源字段/教学反思污染被标记为 source_check_pending。
- V5.1 仍未完成 35 核心题扩展和全量宝典。
"""
    (ROOT / f"09_candidate_frameworks/v5_1_revision_decision_{TODAY}.md").write_text(decision, encoding="utf-8")


def update_control() -> None:
    note = f"""

## STEP_78_V5_1_CLAUDE_PATCH_APPLIED ({STAMP})

- 已读取 Claude Opus 复核：`06_open_observations/claude_opus_v5_action_card_counter_review_20260521.md`。
- 已按 Claude 硬问题生成 V5.1：六张动作卡 + 起手表态铁律。
- 已清洗 CC0277/CC0251 脏细则，降级 AI 宏观和低频容器，返工 CC0077/CC0143/CC0103 样章。
- 新文件：
  - `09_candidate_frameworks/framework_v5_1_action_card_candidate_{TODAY}.md`
  - `09_candidate_frameworks/framework_v5_1_evidence_map_{TODAY}.csv`
  - `09_candidate_frameworks/v5_1_batch_plan_{TODAY}.csv`
  - `11_final_framework/framework_v5_1_student_one_page_{TODAY}.md`
  - `10_framework_validation/framework_v5_1_first10_sample_runs_{TODAY}.md`
  - `12_final_baodian/选必二法律主观题满分宝典_v5_1_十题样章_{TODAY}.md`
- 当前仍不声明最终 PASS：必须做干净题面零基础压测和 35 道核心扩展。
"""
    for rel in ["PROGRESS.md", "governor_board.md", "TODO.md"]:
        p = ROOT / rel
        p.write_text(p.read_text(encoding="utf-8") + note, encoding="utf-8")


def main() -> None:
    write_evidence_map()
    write_batch_plan()
    write_docs()
    write_decision()
    update_control()
    print("built V5.1 artifacts for", TODAY)


if __name__ == "__main__":
    main()
