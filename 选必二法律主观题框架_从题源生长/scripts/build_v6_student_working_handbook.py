from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
CORE_CSV = ROOT / "12_final_baodian" / "question_by_question_framework_runs_v5_9_27core65guard_20260521.csv"
NONCORE_CSV = ROOT / "12_final_baodian" / "non_core_guardrails_v5_9_20260521.csv"
OUT = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_学生可用工作稿_20260521.md"
FUSION_OUT = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_攻击审查融合工作稿_20260521.md"
PLAN_OUT = ROOT / "09_candidate_frameworks" / "framework_v6_student_working_rebuild_plan_20260521.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def norm(text: str) -> str:
    return " ".join((text or "").replace("\r", "\n").split())


def short(text: str, limit: int = 220) -> str:
    text = norm(text)
    return text if len(text) <= limit else text[:limit].rstrip() + "..."


def bullets_from_bank(text: str) -> list[str]:
    parts = [norm(p) for p in (text or "").split(" | ")]
    return [p for p in parts if p]


def primary_card(row: dict[str, str]) -> str:
    entry = row.get("framework_entry_nodes", "")
    first = entry.split("；")[0].strip()
    return first.replace("主卡=", "") or "未定"


def combined(row: dict[str, str]) -> str:
    return " ".join(
        norm(row.get(k, ""))
        for k in [
            "ask_text",
            "material_trigger",
            "minimum_judgment",
            "must_have_keywords",
            "full_score_sentence_bank",
            "rewrite_cautions",
        ]
    )


QUESTION_BATTLEFIELD_OVERRIDES = {
    "CC0002_2024_丰台_一模_17": "实体责任战场",
    "CC0025_2024_朝阳_二模_17": "劳动用工战场",
    "CC0045_2024_海淀_二模_19": "价值收束战场",
    "CC0054_2024_石景山_一模_17": "合同成立与履行战场",
    "CC0063_2024_西城_二模_16": "消费交易战场",
    "CC0103_2025_丰台_一模_19": "创新竞争战场",
    "CC0125_2025_延庆_一模_19": "程序救济战场",
    "CC0143_2025_朝阳_一模_19": "消费交易战场",
    "CC0150_2025_朝阳_二模_20": "实体责任战场",
    "CC0181_2025_海淀_期末_21": "劳动用工战场",
    "CC0200_2025_西城_二模_18": "实体责任战场",
    "CC0206_2025_西城_期末_19": "创新竞争战场",
    "CC0223_2025_顺义_一模_19": "价值收束战场",
    "CC0229_2026_东城_一模_18": "创新竞争战场",
    "CC0238_2026_东城_二模_19": "创新竞争战场",
    "CC0244_2026_东城_期末_18": "程序救济战场",
    "CC0373_2026_顺义_一模_18": "劳动用工战场",
    "RECOVER_2025_海淀_二模_18": "表格补全战场",
    "RECOVER_2026_通州_一模_20": "表格补全战场",
    "RECOVER_2024_东城_二模_19_1": "程序救济战场",
    "RECOVER_2024_东城_二模_19_2": "程序救济战场",
    "RECOVER_2025_丰台_二模_19_2": "创新竞争战场",
    "RECOVER_2026_延庆_一模_18_1": "程序救济战场",
    "RECOVER_2026_房山_一模_17_1": "AI 风险边界战场",
    "RECOVER_2026_西城_二模_18_1": "AI 风险边界战场",
    "RECOVER_2026_门头沟_一模_18_1": "程序救济战场",
    "RECOVER_2026_朝阳_期末_18_1": "合同成立与履行战场",
}


def battlefield(row: dict[str, str]) -> str:
    if row.get("question_id") in QUESTION_BATTLEFIELD_OVERRIDES:
        return QUESTION_BATTLEFIELD_OVERRIDES[row["question_id"]]
    text = combined(row)
    ask = norm(row.get("ask_text", ""))
    pcard = primary_card(row)
    if "表格" in text or "补充完整" in text or "完成下表" in text or primary_card(row) == "一格一答":
        return "表格补全战场"
    if (
        pcard == "排维权步骤"
        or "撰写起诉状" in ask
        or "维权成功" in ask
        or "做好哪些工作" in ask
        or "可提出哪些诉讼请求" in ask
        or "若主持人" in ask
        or "如何进行调解" in ask
        or "公益诉讼" in text
    ):
        return "程序救济战场"
    if any(k in text for k in ["商标", "知识产权", "植物新品种", "商业秘密", "不正当竞争", "混淆", "创新", "司法建议"]):
        return "创新竞争战场"
    if any(k in text for k in ["劳动", "竞业", "从属性", "用人单位", "劳动者"]):
        return "劳动用工战场"
    if any(k in text for k in ["消费者", "欺诈", "知情权", "自主选择权", "惩罚性赔偿", "经营者"]):
        return "消费交易战场"
    if any(k in text for k in ["合同", "要约", "承诺", "履行", "违约", "中标"]):
        return "合同成立与履行战场"
    if any(k in text for k in ["AI", "人工智能", "算法", "智能体", "幻觉", "生成式"]):
        return "AI 风险边界战场"
    if pcard == "推价值" or any(k in ask for k in ["意义", "价值", "社会价值"]):
        return "价值收束战场"
    return "实体责任战场"


BATTLEFIELD_ORDER = [
    "表格补全战场",
    "合同成立与履行战场",
    "消费交易战场",
    "劳动用工战场",
    "实体责任战场",
    "创新竞争战场",
    "程序救济战场",
    "AI 风险边界战场",
    "价值收束战场",
]


BATTLEFIELD_RULES = {
    "表格补全战场": {
        "signal": "材料里出现表格、笔记、横线、示例行、完成下表。",
        "judge": "先判断每个空格的功能：问机制、理由、证据、结果、意义，还是权利名称。",
        "first": "本格要补的是……，因此只写与该格对应的……。",
        "bad": "把整道题写成一篇法治作文，三个格子用同一段话回答。",
        "fix": "先写格子功能，再一格一句；问证据就写证据，问意义才写价值。",
    },
    "合同成立与履行战场": {
        "signal": "付款、报价、中标、承诺、履约、违约、合同是否成立。",
        "judge": "先判断双方是否形成合同关系，以及关键行为是否满足要约、承诺或履行条件。",
        "first": "双方围绕……形成/未形成合同关系，关键在于……是否构成……。",
        "bad": "只说双方要诚信，没判断合同是否成立、谁违约。",
        "fix": "先判合同关系，再写规则条件和材料事实，最后落违约责任或判决意义。",
    },
    "消费交易战场": {
        "signal": "消费者、经营者、虚假宣传、隐瞒收费、质量瑕疵、退款赔偿。",
        "judge": "先判断经营者是否侵犯消费者知情权、自主选择权、公平交易权，是否构成欺诈。",
        "first": "经营者的……行为损害消费者……权利，依法应承担……责任。",
        "bad": "只写消费者要维权，没写经营者违反了哪项义务。",
        "fix": "经营者义务 + 消费者权利 + 材料欺诈事实 + 退款或惩罚性赔偿。",
    },
    "劳动用工战场": {
        "signal": "派单、签到、平台管理、报酬结算、竞业限制、解除劳动关系。",
        "judge": "先判断是否形成劳动关系或竞业限制是否合理，不能只看协议名称。",
        "first": "判断双方是否存在劳动关系，应看人格、经济和组织从属性，而不能只看……。",
        "bad": "把平台协议名称当结论，直接说不是劳动关系。",
        "fix": "用三从属性回扣材料，再落劳动者权益或用人单位边界。",
    },
    "实体责任战场": {
        "signal": "法院判决、是否支持请求、侵权、损害、过错、因果、相邻关系、好意同乘。",
        "judge": "先表态谁的请求能否支持，再把材料事实塞进责任构成条件。",
        "first": "某方请求应/不应支持，因为本案中……符合/不符合……责任构成。",
        "bad": "只讲故事经过，最后突然说法院公正。",
        "fix": "表态句 + 规则条件 + 材料事实 + 责任结果，每一段只解决一个争点。",
    },
    "创新竞争战场": {
        "signal": "作品、商标、植物新品种、商业秘密、数据、混淆宣传、创新保护。",
        "judge": "先认保护对象，再抓侵害行为，最后落权利人权益和竞争秩序。",
        "first": "本案保护对象是……，某方未经许可/混淆/不当利用……，构成……。",
        "bad": "只喊保护创新，没有写保护对象和侵害行为。",
        "fix": "保护对象 + 侵害行为 + 法律后果 + 创新/竞争秩序价值。",
    },
    "程序救济战场": {
        "signal": "如何维权、证据、诉讼请求、起诉状、调解、仲裁、公益诉讼。",
        "judge": "先判当前问的是路径、证据、请求、效力还是起诉状结构。",
        "first": "当事人应围绕……收集证据，提出……请求，并通过……路径维权。",
        "bad": "用实体责任替代程序动作，漏写证据和请求。",
        "fix": "证据 -> 请求 -> 路径 -> 效力；起诉状题按诉讼请求、事实与理由、证据写。",
    },
    "AI 风险边界战场": {
        "signal": "AI、算法、智能体、生成式、平台、自动回复、数字治理。",
        "judge": "先三分流：具体民事权利风险、综合治理边界、其他模块转出。",
        "first": "本题若落在《法律与生活》，应先处理……权利风险和……责任边界。",
        "bad": "一看到 AI 就写数字中国或把所有 AI 都写成侵权。",
        "fix": "具体权利风险写权利和救济；综合治理只写法律层最低句；逻辑/必修三另开模块。",
    },
    "价值收束战场": {
        "signal": "意义、价值、典型案例、司法之力、社会效果。",
        "judge": "先写本案法律处理，再从处理推出保护对象、规范对象、社会效果。",
        "first": "本案通过……处理，保护了……，规范了……，有利于……。",
        "bad": "裸写公平正义、和谐社会、法治中国。",
        "fix": "本案处理 -> 保护谁 -> 规范谁 -> 推出什么价值，不写脱离案件的空话。",
    },
}


NONCORE_RULES = {
    "source_check_pending": {
        "name": "SOURCE-CHECK 回源保分区",
        "use": "只按问法保最低分方向；正式课堂使用前必须回原题和细则。",
        "danger": "最怕学生把最低三句当闭合满分答案。",
    },
    "low_frequency_container": {
        "name": "低频规则保分区",
        "use": "能训练三句保分，但不抬成高频母题。",
        "danger": "最怕把低频法条包装成总框架。",
    },
    "reference_only_locked": {
        "name": "REFERENCE-ONLY 练笔区",
        "use": "只借表达，不借结论，不支撑核心节点。",
        "danger": "最怕把普通参考答案冒充评分细则。",
    },
    "boundary_open_container": {
        "name": "边界开放区",
        "use": "先写法律层最低句，其他模块另开段，不硬塞私法模板。",
        "danger": "最怕必修三化或宏观治理化。",
    },
    "excluded_logic_boundary": {
        "name": "转出区",
        "use": "主任务属于其他模块时，法律只保留边界提醒。",
        "danger": "最怕拿法律框架硬答逻辑题。",
    },
}


def md_table(rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
    out = []
    out.append("| " + " | ".join(str(rows[0][i]) for i in range(len(widths))) + " |")
    out.append("| " + " | ".join("---" for _ in widths) + " |")
    for row in rows[1:]:
        out.append("| " + " | ".join(str(row[i]) for i in range(len(widths))) + " |")
    return out


def three_sentence_floor(row: dict[str, str], bank: list[str]) -> list[str]:
    if len(bank) >= 3:
        return bank[:3]
    answer = norm(row.get("clean_exam_answer") or row.get("complete_answer_generated"))
    chunks = [p.strip("；。 ") for p in answer.replace("。", "。\n").splitlines() if p.strip()]
    return (bank + chunks)[:3]


def noncore_applicability(row: dict[str, str]) -> tuple[str, str]:
    kind = row.get("audit_category", "")
    text = " ".join(norm(row.get(k, "")) for k in ["source_label", "minimum_sentence_1", "minimum_sentence_2", "minimum_sentence_3", "student_category"])
    if kind == "reference_only_locked":
        return "只适用于练习表达和思路迁移。", "不适用于正式细则满分答案，不支撑核心框架节点。"
    if kind == "boundary_open_container":
        return "只适用于原设问允许写《法律与生活》法律层时。", "不适用于原题主要考必修三、选必一、逻辑或宏观治理整题作答。"
    if kind == "excluded_logic_boundary":
        return "只适用于题中另有独立法律小问时。", "不适用于逻辑推理主任务。"
    if kind == "low_frequency_container":
        return "适用于原设问正好问该低频规则、制度或法律功能时。", "不适用于高频合同/侵权/劳动/知产母题，不得抬为核心模板。"
    if "表格" in text or "补" in text:
        return "适用于原设问也是补表、补笔记、补法律术语时。", "不适用于问意义、原因或建议的整段答案。"
    if "风险" in text or "AI" in text or "智能" in text:
        return "适用于原设问问法律风险、法律边界或合规措施时。", "不适用于宏观治理、哲学方法或技术伦理主任务。"
    if "意义" in text or "价值" in text:
        return "适用于原设问问意义、价值、作用时。", "不适用于问是否支持、责任依据或诉讼请求的题。"
    if "怎么办" in text or "维权" in text or "请求" in text or "证据" in text:
        return "适用于原设问问维权准备、证据、请求或路径时。", "不适用于只问实体责任成立与否的题。"
    return "适用于原设问与本卡最低三句主题一致时。", "不适用于设问功能不同的题，尤其不能把三句背成万能答案。"


def append_core_question(lines: list[str], row: dict[str, str]) -> None:
    bf = battlefield(row)
    rule = BATTLEFIELD_RULES[bf]
    bank = bullets_from_bank(row.get("full_score_sentence_bank", ""))
    keywords = [k.strip() for k in row.get("must_have_keywords", "").replace("、", "|").replace("，", "|").split("|") if k.strip()]

    lines.append(f"### 核心题 {row.get('display_index')}: {row.get('year')} {row.get('district')} {row.get('exam_stage')} 第{row.get('question_no')}题")
    lines.append("")
    lines.append(f"- 题号证据：`{row.get('question_id')}`；证据等级：`{row.get('evidence_level')}`。")
    lines.append(f"- 所属战场：**{bf}**。")
    lines.append(f"- 设问：{norm(row.get('ask_text'))}")
    lines.append("")
    lines.append("#### 1. 陌生题第一眼怎么启动")
    lines.append("")
    lines.append(f"1. 先识别信号：{rule['signal']}")
    lines.append(f"2. 先做判断：{row.get('student_first_judgment_v5_5') or rule['judge']}")
    lines.append(f"3. 第一笔句子：{rule['first']}")
    lines.append("")
    lines.append("#### 2. 三句保底答案")
    lines.append("")
    for idx, sent in enumerate(three_sentence_floor(row, bank), 1):
        lines.append(f"{idx}. {sent}")
    lines.append("")
    lines.append("这三句不是最终满分答案，但能保证你先踩住方向：第一句判争点，第二句写规则，第三句把材料事实落进去。")
    lines.append("")
    lines.append("#### 3. 材料一句话")
    lines.append("")
    lines.append(short(row.get("material_trigger", ""), 520))
    lines.append("")
    lines.append("#### 4. 这题争什么")
    lines.append("")
    lines.append(short(row.get("minimum_judgment", ""), 360))
    lines.append("")
    lines.append("#### 5. 材料翻译表")
    lines.append("")
    table_rows = [
        ["材料事实/信号", "翻译成法律语言", "对应得分句"],
        [short(row.get("material_trigger", ""), 90), short(row.get("minimum_judgment", ""), 90), short(bank[0] if bank else row.get("complete_answer_generated", ""), 90)],
    ]
    if len(bank) > 1:
        table_rows.append(["第二个关键事实", "第二个规则条件或价值落点", short(bank[1], 90)])
    if len(bank) > 2:
        table_rows.append(["最后落点", "责任、程序或价值收束", short(bank[-1], 90)])
    lines.extend(md_table(table_rows))
    lines.append("")
    lines.append("#### 6. 满分句零件")
    lines.append("")
    for item in bank[:8]:
        lines.append(f"- {item}")
    if not bank:
        lines.append(f"- {short(row.get('complete_answer_generated', ''), 260)}")
    lines.append("")
    if keywords:
        lines.append("必带关键词：" + "、".join(keywords[:12]))
        lines.append("")
    lines.append("#### 7. 完整考场版答案")
    lines.append("")
    answer = norm(row.get("clean_exam_answer") or row.get("complete_answer_generated"))
    for part in [p.strip() for p in answer.split(" | ") if p.strip()]:
        lines.append(part)
        lines.append("")
    lines.append("#### 8. 错法改法")
    lines.append("")
    lines.append(f"- 错法：{rule['bad']}")
    lines.append(f"- 改法：{rule['fix']}")
    caution = norm(row.get("rewrite_cautions"))
    if caution:
        lines.append(f"- 本题特别提醒：{caution}")
    lines.append("")
    lines.append("#### 9. 迁移提醒")
    lines.append("")
    lines.append(f"以后看到类似的 {rule['signal']}，先进入“{bf}”；如果题目不是这个信号，就不要硬套本题答案。")
    lines.append("")


def build_plan(core: list[dict[str, str]], noncore: list[dict[str, str]]) -> str:
    bcnt = Counter(battlefield(r) for r in core)
    ncnt = Counter(r.get("audit_category", "") for r in noncore)
    lines: list[str] = []
    lines.append("# V6 学生可用工作稿重构计划")
    lines.append("")
    lines.append("## 总裁定")
    lines.append("")
    lines.append("V5.9 不再按“证据安全即合格”处理。V6 的目标是学生启动闭环：判题门、材料翻译、满分句、错法改法。")
    lines.append("")
    lines.append("## 不变底线")
    lines.append("")
    lines.append("- 证据底座仍为 65 题，formal / reference_only / missing = 61 / 4 / 0。")
    lines.append("- 27 strict core 才进入闭合满分训练。")
    lines.append("- 38 非核心只作保分、边界、回源、参考、转出索引。")
    lines.append("- reference_only 不得单独支撑核心节点。")
    lines.append("")
    lines.append("## 核心重排统计")
    lines.append("")
    for key in BATTLEFIELD_ORDER:
        if bcnt[key]:
            lines.append(f"- {key}: {bcnt[key]} 题。")
    lines.append("")
    lines.append("## 非核心分区统计")
    lines.append("")
    for key, count in sorted(ncnt.items()):
        lines.append(f"- {NONCORE_RULES.get(key, {}).get('name', key)}: {count} 题。")
    lines.append("")
    lines.append("## 下一步")
    lines.append("")
    lines.append("GPTPro、Claude Opus、本地 student-agent、Codex A 攻击审查已落盘并合并。下一步是用本 V6 融合工作稿做裸题盲测：隐藏 question_id、category、core/guard 标签，只给材料和设问。")
    lines.append("")
    return "\n".join(lines)


def build_handbook(core: list[dict[str, str]], noncore: list[dict[str, str]]) -> str:
    by_battle: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in core:
        by_battle[battlefield(row)].append(row)
    noncore_by_kind: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in noncore:
        noncore_by_kind[row.get("audit_category", "")].append(row)

    lines: list[str] = []
    lines.append("# 选必二《法律与生活》主观题满分训练宝典 V6")
    lines.append("")
    lines.append("副标题：学生可用工作稿")
    lines.append("")
    lines.append("生成时间：2026-05-21")
    lines.append("")
    lines.append("## 开卷第一页：你到底要做什么")
    lines.append("")
    lines.append("法律主观题不是背法条，也不是写法治大作文。它只考一件事：")
    lines.append("")
    lines.append("```text")
    lines.append("把材料里的生活冲突，翻译成法律判断。")
    lines.append("主体 -> 行为 -> 争点 -> 规则 -> 材料事实 -> 责任/程序/价值")
    lines.append("```")
    lines.append("")
    lines.append("所以你拿到题，先别急着写。先问自己三句：")
    lines.append("")
    lines.append("1. **这题争什么？** 谁的请求、谁的行为、哪个权利义务在冲突。")
    lines.append("2. **哪个事实决定结果？** 材料里哪句话能触发法律规则。")
    lines.append("3. **最后落到哪里？** 责任、效力、救济、证据，还是价值。")
    lines.append("")
    lines.append("## 一页速记：30 秒判题门")
    lines.append("")
    lines.append("| 先看 | 问自己 | 进入哪里 | 第一笔怎么写 |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| 设问问是否支持、是否有效、是否构成 | 要不要先表态？ | 实体责任/合同/消费/劳动 | 某请求应/不应支持，因为…… |")
    lines.append("| 设问问理由、依据、评析 | 哪个规则 + 哪个事实？ | 对应责任战场 | 依据……规则，材料中……，所以…… |")
    lines.append("| 设问问怎么办、维权、请求 | 要证据、请求、路径还是效力？ | 程序救济战场 | 当事人应围绕……收集证据，提出……请求。 |")
    lines.append("| 设问是表格、补全、笔记 | 每格要什么功能？ | 表格补全战场 | 本格问……，只需写…… |")
    lines.append("| 设问问意义、价值、作用 | 价值从哪个法律处理推出？ | 价值收束战场 | 本案通过……保护了……，规范了……。 |")
    lines.append("| 材料有 AI、治理、逻辑、开放问 | 是不是纯法律核心题？ | AI 边界/转出区 | 若落在法律层，应先处理……权利风险。 |")
    lines.append("")
    lines.append("## 一二三四五总图")
    lines.append("")
    lines.append("- **一件事**：用法律把生活冲突处理成一个明确结果。")
    lines.append("- **两条线**：事实规则线 + 价值收束线。")
    lines.append("- **三问**：判什么、凭什么、怎么得分。")
    lines.append("- **四步**：圈主体、抓行为、定争点、落结果。")
    lines.append("- **五类材料世界**：交易用工、财产家庭、人身侵权、创新竞争、程序公共/新技术。")
    lines.append("")
    lines.append("## 主体法律动作积累页")
    lines.append("")
    lines.extend(md_table([
        ["主体", "一出现先想", "可直接写的句子"],
        ["法院/仲裁委", "支持或不支持请求，理由必须是事实 + 规则", "人民法院/仲裁机构应以事实为根据、以法律为准绳，结合双方关系、行为性质和法律后果作出处理。"],
        ["经营者", "真实、诚信、提示说明、不得欺诈", "经营者应依法诚信经营，真实全面提供商品或服务信息，保障消费者知情权、自主选择权和公平交易权。"],
        ["消费者", "依法、诚信、有证据地维权", "消费者依法享有维权权利，但应遵循诚信原则，不得滥用权利损害经营者合法权益。"],
        ["用人单位/平台", "管理控制、报酬支付、组织从属性、依法解除", "判断是否形成劳动关系，不能只看协议名称，应结合人格、经济和组织从属性。"],
        ["劳动者", "如实说明、遵守纪律、商业秘密边界", "劳动者应遵守劳动纪律和职业道德，履行与劳动合同直接相关的如实说明义务。"],
        ["权利人/创新主体", "保护对象、侵害行为、市场秩序", "权利人依法享有知识产权或竞争利益，未经许可使用、混淆、泄密等行为应承担相应责任。"],
        ["AI/平台企业", "提示、审核、保密、责任边界", "平台和企业应对算法、数据、作品和用户权益尽到必要提示、审核、保密和合规义务。"],
        ["当事人", "证据、请求、路径", "当事人维权应选择适当纠纷解决路径，围绕合同、付款、损害、因果关系和请求收集证据。"],
    ]))
    lines.append("")
    lines.append("## 情境触发翻译词典")
    lines.append("")
    lines.extend(md_table([
        ["材料信号", "法律翻译", "不能乱写成"],
        ["付款、报价、中标、承诺、履约", "要约、承诺、合同成立、违约责任", "诚信原则大作文"],
        ["虚假宣传、费用不清、质量瑕疵", "知情权、自主选择权、公平交易权、欺诈、惩罚性赔偿", "消费者情绪投诉"],
        ["派单、签到、奖惩、结算、业务组成", "人格从属性、经济从属性、组织从属性、劳动关系", "平台协议名称决定一切"],
        ["受伤、隐私、名誉、相邻妨害", "侵权行为、损害、过错/无过错、因果关系、权利边界", "只讲故事"],
        ["作品、商标、植物新品种、商业秘密", "保护对象、未经许可、混淆、泄密、不正当竞争", "只喊保护创新"],
        ["起诉状、证据、仲裁、调解", "诉讼请求、事实与理由、举证、程序效力", "实体责任一锅炖"],
        ["AI、算法、智能体、生成式", "具体民事权利风险、责任边界、合规义务、必要时转出", "数字中国宏观作文"],
        ["意义、价值、典型案例", "本案法律处理 -> 保护对象 -> 规范对象 -> 社会效果", "公平正义空话"],
    ]))
    lines.append("")
    lines.append("## 三型答案骨架")
    lines.append("")
    lines.append("同一套法律知识，落到卷面上有三种产品。先判断是哪一种产品，再动笔。")
    lines.append("")
    lines.extend(md_table([
        ["答案类型", "适用设问", "考场骨架"],
        ["判断型", "是否支持、是否有效、是否构成、判决依据", "先表态：……应/不应支持。再写规则：依据……。再嵌材料：本案中……。最后落结果：所以……。"],
        ["意义型", "意义、价值、作用、典型案例", "先写本案处理：法院/法律通过……。再写保护谁：保护……权益。再写规范谁：规范……行为/秩序。最后写价值：引导……。"],
        ["表格型", "完成下表、补充笔记、补全裁判理由", "先看示例行和空格功能。每格只写一个功能：机制/理由/证据/结果/意义。不能把整篇答案塞进一个格。"],
    ]))
    lines.append("")
    lines.append("## 题级禁用词总表")
    lines.append("")
    lines.append("法律题最可怕的不是不会写，而是把隔壁题的满分词搬过来。本表是 V6 新增的刹车。")
    lines.append("")
    lines.extend(md_table([
        ["题号", "本题能写", "本题禁写或慎写", "为什么"],
        ["CC0002 好意同乘", "维护双方合法权益", "不要迁移到知识产权意义题", "好意同乘减责强调双方权益平衡，知识产权意义题的权利主体不同。"],
        ["CC0103 科技创新典型案例", "营造公平的市场环境、维护原告方合法权益", "优化营商环境、维护双方/公民/被告合法权益", "细则明文把这些列为错误表达。"],
        ["CC0206 不正当竞争", "营商环境、法治化营商环境", "不要套 CC0103 的禁词规则", "本题细则奖励营商环境表达。"],
        ["CC0150 隐私相邻", "隐私权、共有部分、共同管理、相邻关系", "隐私权写错字、周边外交、人类命运共同体", "前者是细则硬词，后者是跨模块污染。"],
        ["CC0244 无人机维权", "合同责任与侵权责任分段写", "把违约要件和侵权要件糊成一段", "细则要求违约和侵权不要混同。"],
        ["CC0289 非核心补全题", "三选一权利保护、举证责任、相邻关系", "必修三/全面依法治国大段", "非核心保分卡必须防必修三化。"],
    ]))
    lines.append("")
    lines.append("## 满分句工厂")
    lines.append("")
    lines.append("一段高分答案通常由六种句子拼成。不要每题都写六句，但缺了关键句就会丢分。")
    lines.append("")
    lines.extend(md_table([
        ["句子零件", "模板", "用途"],
        ["表态句", "某请求应/不应支持；某行为构成/不构成……", "给阅卷人一个明确判断"],
        ["争点句", "本案争点在于……是否触发……规则并产生……后果。", "把材料故事压成法律问题"],
        ["规则句", "依据相关法律，判断……应看……条件。", "写出法律知识而非情绪判断"],
        ["材料句", "本案中，材料显示……，符合/不符合上述条件。", "把材料塞进规则"],
        ["落点句", "因此，某方应承担……责任/通过……路径维权。", "回到责任、程序、效力、救济"],
        ["价值句", "该处理有利于保护……，规范……，引导……。", "只从本案推出价值，不空喊"],
    ]))
    lines.append("")
    lines.append("## 九个战场：看到什么，先打哪一仗")
    lines.append("")
    for key in BATTLEFIELD_ORDER:
        rule = BATTLEFIELD_RULES[key]
        count = len(by_battle.get(key, []))
        if not count:
            continue
        lines.append(f"### {key}（{count} 题）")
        lines.append("")
        lines.append(f"- 题目信号：{rule['signal']}")
        lines.append(f"- 第一判断：{rule['judge']}")
        lines.append(f"- 第一笔句：{rule['first']}")
        lines.append(f"- 常见错法：{rule['bad']}")
        lines.append(f"- 改法：{rule['fix']}")
        lines.append("")
    lines.append("## 易混题对照框")
    lines.append("")
    lines.append("这几组题必须并排学。它们表面相似，但评分口径不同。")
    lines.append("")
    lines.extend(md_table([
        ["易混组", "A 题怎么写", "B 题怎么写", "刹车句"],
        ["CC0103 vs CC0206", "CC0103 写技术秘密、严惩侵权、营造公平市场环境，禁写优化营商环境。", "CC0206 写混淆、虚假宣传、不正当竞争、营商环境。", "看到科技创新典型案例先查禁词；看到混淆宣传再写营商环境。"],
        ["CC0002 vs 通州一模20 vs CC0251", "好意同乘是无偿搭载、无故意或重大过失、依法减责。", "文体活动/公共场所要写自甘风险、安全保障义务、过错边界。", "减责、免责、不担责不是同一套要件。"],
        ["CC0181 vs CC0373", "CC0181 解释竞业限制为什么既保护商业秘密又限制过度。", "CC0373 先拆平等就业和竞业限制两个诉求。", "单考点题不要写成复合两问；复合两问不能漏一问。"],
        ["CC0244 第1问 vs 第2问", "第1问写合同成立、违约、侵权或产品责任。", "第2问写证据准备、请求设计、维权路径。", "先拆问号，每问至少一段。"],
    ]))
    lines.append("")
    lines.append("## 27 道核心题逐题训练")
    lines.append("")
    lines.append("以下 27 题才是本稿的闭合满分训练区。每题先训练启动，再训练答案，不把后台证据标签放到学生前台。")
    lines.append("")
    for key in BATTLEFIELD_ORDER:
        rows = by_battle.get(key, [])
        if not rows:
            continue
        lines.append(f"## {key}")
        lines.append("")
        for row in sorted(rows, key=lambda r: int(r.get("display_index") or 999)):
            append_core_question(lines, row)
    lines.append("## 38 道非核心保分索引")
    lines.append("")
    lines.append("这 38 题不是废题，也不是核心满分模板。它们的作用是保边界、保低频、保回源、保不误收。学生只按下面纪律使用。")
    lines.append("")
    for key, rows in sorted(noncore_by_kind.items()):
        meta = NONCORE_RULES.get(key, {"name": key, "use": "", "danger": ""})
        lines.append(f"### {meta['name']}（{len(rows)} 题）")
        lines.append("")
        lines.append(f"- 怎么用：{meta['use']}")
        lines.append(f"- 最大风险：{meta['danger']}")
        lines.append("")
        for row in rows:
            lines.append(f"#### {row.get('title_with_id')}")
            lines.append("")
            lines.append(f"- 证据等级：`{row.get('evidence_level')}`；学生标签：{row.get('student_category')}。")
            applicable, not_applicable = noncore_applicability(row)
            lines.append(f"- 适用设问：{applicable}")
            lines.append(f"- 不适用设问：{not_applicable}")
            lines.append("- 最低可写三句：")
            for i in range(1, 4):
                sent = norm(row.get(f"minimum_sentence_{i}", ""))
                if sent:
                    lines.append(f"  {i}. {sent}")
            lines.append(f"- 禁止写法：{row.get('do_not_write')}")
            lines.append(f"- 背诵状态：{row.get('memorization_status')}")
            lines.append("")
    lines.append("## 六大陷阱专项练")
    lines.append("")
    lines.extend(md_table([
        ["陷阱", "学生会怎么错", "框架怎么刹车"],
        ["多小问漏问", "只答第一个问号", "先拆问号，每个问号至少一段"],
        ["表格格子错位", "每个格都写同一段法治话", "先判格子功能，再一格一句"],
        ["AI 宏观化", "写数字中国、技术伦理、治理现代化", "先三分流：具体民事风险、综合治理、转出模块"],
        ["价值空泛化", "公平正义、社会和谐一套到底", "本案处理 -> 保护谁 -> 规范谁 -> 社会效果"],
        ["source-check 当满分", "把最低三句当闭合答案", "按问法保分，正式使用前回源"],
        ["reference_only 误升核心", "普通参考答案当正式细则背", "只借表达，不借结论"],
    ]))
    lines.append("")
    lines.append("## 教师后台证据说明")
    lines.append("")
    lines.append("- 本工作稿仍继承当前 65 题底座：61 formal、4 reference_only、0 missing。")
    lines.append("- 27 核心题使用 formal 证据进入闭合训练。")
    lines.append("- 38 非核心题必须保留标签，不得在课堂或文档中被包装成全量核心满分闭环。")
    lines.append("- GPTPro、Claude Opus 4.7 Cowork、本地学生 agent 的 V5.9 攻击审查已经合并为 `07_cross_validation/v5_9_attack_review_synthesis_20260521.md`。")
    lines.append("- V5.9 带标签盲测作废；V6 后续必须做裸题盲测。")
    lines.append("- 待回源/待修 canonical：`CC0045`、`CC0223`、`CC0244`、`CC0119`、`CC0289` 等。")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    core = read_csv(CORE_CSV)
    noncore = read_csv(NONCORE_CSV)
    handbook = build_handbook(core, noncore)
    OUT.write_text(handbook, encoding="utf-8")
    FUSION_OUT.write_text(handbook, encoding="utf-8")
    PLAN_OUT.write_text(build_plan(core, noncore), encoding="utf-8")
    print(OUT)
    print(FUSION_OUT)
    print(PLAN_OUT)


if __name__ == "__main__":
    main()
