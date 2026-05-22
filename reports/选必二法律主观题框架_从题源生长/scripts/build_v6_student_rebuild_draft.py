from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
CORE_CSV = ROOT / "12_final_baodian" / "question_by_question_framework_runs_v5_9_27core65guard_20260521.csv"
NONCORE_CSV = ROOT / "12_final_baodian" / "non_core_guardrails_v5_9_20260521.csv"
OUT = ROOT / "12_final_baodian" / "选必二法律主观题满分训练宝典_v6_学生启动重构草案_20260521.md"
PLAN_OUT = ROOT / "09_candidate_frameworks" / "framework_v6_rebuild_plan_preliminary_20260521.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def one_line(text: str, limit: int = 260) -> str:
    t = " ".join((text or "").replace("\r", "\n").split())
    if len(t) <= limit:
        return t
    return t[:limit].rstrip() + "..."


def main_card(row: dict[str, str]) -> str:
    entry = row.get("framework_entry_nodes", "")
    first = entry.split("；")[0].strip()
    return first.replace("主卡=", "") or "未定"


CARD_ORDER = [
    "一格一答",
    "分关系·定责任",
    "认产权·抓侵权",
    "排维权步骤",
    "划风险边界",
    "推价值",
]

CARD_TITLES = {
    "一格一答": "表格/笔记补全题：一格只完成一个任务",
    "分关系·定责任": "裁判评析与实体责任题：先判谁赢，再写依据",
    "认产权·抓侵权": "知识产权与不正当竞争题：保护对象、侵害行为、竞争秩序",
    "排维权步骤": "程序救济题：路径、证据、请求、效力",
    "划风险边界": "风险合规题：一项风险、一条边界、一项措施",
    "推价值": "意义价值题：本案处理推出保护、规范、价值",
}

CARD_STARTERS = {
    "一格一答": [
        "先看示例行，判断这个空是要机制、理由、结果、证据还是意义。",
        "每个空只回答一个功能，不把整段案例答案塞进同一个格。",
        "如果格子问意义，必须从该格对应的处理结果推出价值。",
    ],
    "分关系·定责任": [
        "第一句必须判：请求支持不支持、合同成立不成立、行为构成不构成。",
        "第二步把材料事实翻译成规则条件，不能只讲故事。",
        "混合题分段写，合同责任和侵权责任不能糊成一段。",
    ],
    "认产权·抓侵权": [
        "先认保护对象：作品、商标、商业秘密、数据权益、植物新品种等。",
        "再抓侵害行为：未经许可、混淆、虚假宣传、商业诋毁、恶意诉讼等。",
        "最后落到权利人权益、竞争秩序和创新活力。",
    ],
    "排维权步骤": [
        "先判程序阶段：调解、仲裁、诉讼、起诉状、举证、公益诉讼。",
        "普通维权写证据、请求、路径；调解题写理由和效力；公益题写主体和公共利益。",
        "不要用程序救济替代实体责任。",
    ],
    "划风险边界": [
        "先判这是具体民事风险，还是宏观治理/其他模块题。",
        "具体风险按一项风险、一条法律边界、一项措施写。",
        "AI 题不能一概套侵权，也不能一概写数字中国。",
    ],
    "推价值": [
        "先写本案法律处理是什么，再写保护谁。",
        "第二层写规范什么行业、司法、交易或劳动秩序。",
        "最后才写公平、诚信、友善、创新、公共利益等价值。",
    ],
}

NONCORE_KIND_GUIDE = {
    "source_check_pending": "先按设问分叉保分，正式上课前必须回源核题干和细则；不能背成闭合满分答案。",
    "low_frequency_container": "可训练低频保分句，但不升高频母题；按规则、材料、功能三句写。",
    "reference_only_locked": "只借表达，不借结论；不能支撑核心节点，不能当正式细则满分题。",
    "boundary_open_container": "先停核心私法模板，只写《法律与生活》能覆盖的权利、义务、责任和程序，其他模块另开段。",
    "excluded_logic_boundary": "主任务转出本书，法律只保留边界说明。",
}


def build_plan(core: list[dict[str, str]], noncore: list[dict[str, str]]) -> str:
    by_card: dict[str, list[dict[str, str]]] = {}
    for row in core:
        by_card.setdefault(main_card(row), []).append(row)

    lines = []
    lines.append("# V6 重构方案草案：从证据安全稿转为学生启动稿")
    lines.append("")
    lines.append("状态：preliminary。等待 GPTPro、Claude Opus、本地 student-agent 三方攻击报告后再合并修订。")
    lines.append("")
    lines.append("## 不能变的底线")
    lines.append("")
    lines.append("- active corpus 仍为 65 题。")
    lines.append("- 27 道 strict core 作为满分训练主线。")
    lines.append("- 38 道非核心只作保分、边界、回源、参考、转出索引。")
    lines.append("- 4 道 reference_only 不得支撑核心节点。")
    lines.append("- V6 解决的是学生启动和满分句生成，不是扩核心。")
    lines.append("")
    lines.append("## 重构目录")
    lines.append("")
    lines.append("1. 法律主观题到底在考什么。")
    lines.append("2. 一张总模型：生活冲突 A -> 法律判断 B。")
    lines.append("3. 30 秒判题门：设问门、情境门、证据门。")
    lines.append("4. 主体法律动作积累页。")
    lines.append("5. 情境触发翻译词典。")
    lines.append("6. 满分句工厂。")
    lines.append("7. 六类考场产品。")
    lines.append("8. 27 核心逐题训练，按题型重排。")
    lines.append("9. 38 非核心保分索引，放在附录。")
    lines.append("10. 六大陷阱专项练。")
    lines.append("")
    lines.append("## 27 核心重排")
    lines.append("")
    for card in CARD_ORDER:
        rows = by_card.get(card, [])
        if not rows:
            continue
        lines.append(f"### {CARD_TITLES.get(card, card)}")
        lines.append("")
        for row in rows:
            lines.append(f"- {row['display_index']}. `{row['question_id']}`：{one_line(row.get('ask_text', ''), 90)}")
        lines.append("")
    lines.append("## 38 非核心分区")
    lines.append("")
    counts: dict[str, int] = {}
    for row in noncore:
        counts[row.get("audit_category", "")] = counts.get(row.get("audit_category", ""), 0) + 1
    for key, count in sorted(counts.items()):
        lines.append(f"- {key}: {count} 题。{NONCORE_KIND_GUIDE.get(key, '')}")
    lines.append("")
    return "\n".join(lines) + "\n"


def build_handbook(core: list[dict[str, str]], noncore: list[dict[str, str]]) -> str:
    by_card: dict[str, list[dict[str, str]]] = {}
    for row in core:
        by_card.setdefault(main_card(row), []).append(row)

    lines: list[str] = []
    lines.append("# 选必二《法律与生活》主观题满分训练宝典 V6")
    lines.append("")
    lines.append("副标题：学生启动重构草案")
    lines.append("")
    lines.append("生成时间：2026-05-21")
    lines.append("")
    lines.append("## 先说清楚")
    lines.append("")
    lines.append("这不是把 V5.9 换个标题。V6 的任务是把证据安全稿改成学生能启动的训练稿。")
    lines.append("")
    lines.append("- 底座仍是 65 道选必二法律主观题。")
    lines.append("- 核心训练只承认 27 道已清洗核心题。")
    lines.append("- 其余 38 题只能作为保分、边界、回源、参考或转出索引。")
    lines.append("- 参考答案题不能支撑核心框架。")
    lines.append("- 学生正面先学启动动作，证据编号放到教师后台。")
    lines.append("")
    lines.append("## 第一部分：法律主观题到底在考什么")
    lines.append("")
    lines.append("法律主观题不是让你背一堆法条，也不是让你写全面依法治国大作文。它考的是：把材料里的生活冲突，压成一个明确的法律判断。")
    lines.append("")
    lines.append("你要完成的变化是：")
    lines.append("")
    lines.append("```text")
    lines.append("生活事实 A -> 法律判断 B")
    lines.append("主体 -> 行为 -> 争点 -> 规则 -> 材料事实 -> 责任/程序/价值")
    lines.append("```")
    lines.append("")
    lines.append("所以每一道题先问三句话：")
    lines.append("")
    lines.append("1. 这件事争什么。")
    lines.append("2. 哪个材料事实决定法律结果。")
    lines.append("3. 阅卷人奖励的是责任、程序、权利边界，还是价值收束。")
    lines.append("")
    lines.append("## 第二部分：30 秒判题门")
    lines.append("")
    lines.append("拿到陌生题，不先背知识。先过三道门。")
    lines.append("")
    lines.append("### 1. 设问门")
    lines.append("")
    lines.append("| 设问问法 | 先做什么 | 第一笔答案 |")
    lines.append("| --- | --- | --- |")
    lines.append("| 是否支持、是否有效、是否构成 | 先表态 | 某请求应/不应支持，某行为构成/不构成…… |")
    lines.append("| 说明理由、判决依据 | 找规则条件和决定性事实 | 人民法院以事实为根据、以法律为准绳…… |")
    lines.append("| 分析法律责任 | 分合同、侵权、消费、劳动、相邻 | 甲乙之间形成某法律关系…… |")
    lines.append("| 如何维权、怎么准备、诉讼请求 | 写证据、请求、路径、效力 | 当事人应收集……证据，提出……请求，通过……路径维权。 |")
    lines.append("| 完成表格、补全笔记 | 看示例行和格子功能 | 本格问机制/理由/结果/意义，所以只写…… |")
    lines.append("| 意义、价值、作用 | 先写本案怎么处理 | 本案通过……保护了……，规范了……，弘扬了……。 |")
    lines.append("| AI、边界、治理、涉外、逻辑 | 先判是否本书核心 | 若不是纯法律核心题，只写法律层最低句，其他模块另开段。 |")
    lines.append("")
    lines.append("### 2. 情境门")
    lines.append("")
    lines.append("- 买卖、付款、交付、瑕疵：先想合同，必要时再想消费或侵权。")
    lines.append("- 受伤、隐私、名誉、相邻妨害：先想侵权或权利边界。")
    lines.append("- 派单、签到、奖惩、报酬、解除：先想劳动关系和从属性。")
    lines.append("- 作品、商标、数据、商业秘密、混淆宣传：先想知识产权和不正当竞争。")
    lines.append("- 起诉、调解、仲裁、证据、起诉状：先想程序救济。")
    lines.append("- AI、平台、算法、代码、自动回复：先分具体民事风险、综合治理、转出模块。")
    lines.append("")
    lines.append("### 3. 证据门")
    lines.append("")
    lines.append("- 27 核心：可按本稿训练到闭合答案。")
    lines.append("- low-frequency：可保分，不升母题。")
    lines.append("- source-check：按问法保分，正式使用前回源。")
    lines.append("- reference-only：只借表达，不借结论。")
    lines.append("- boundary / transfer：先停核心模板，必要时转其他模块。")
    lines.append("")
    lines.append("## 第三部分：一二三四五总图")
    lines.append("")
    lines.append("一件事：用法律把生活冲突处理成一个明确结果。")
    lines.append("")
    lines.append("两条线：事实规则线和价值收束线。")
    lines.append("")
    lines.append("三问：判什么，凭什么，怎么得分。")
    lines.append("")
    lines.append("四步：圈主体，抓行为，定争点，落结果。")
    lines.append("")
    lines.append("五类材料世界：交易与用工，财产与家庭，人身与侵权，创新与竞争，程序与公共/新技术。")
    lines.append("")
    lines.append("## 第四部分：主体法律动作积累页")
    lines.append("")
    lines.append("| 主体 | 一出现先想 | 可直接写的句子 |")
    lines.append("| --- | --- | --- |")
    lines.append("| 法院/仲裁委 | 支持或不支持请求，理由必须是事实 + 规则 | 人民法院/仲裁机构应以事实为根据、以法律为准绳，结合双方关系、行为性质和法律后果作出处理。 |")
    lines.append("| 经营者 | 真实、诚信、提示说明、不得欺诈 | 经营者应依法诚信经营，真实全面提供商品或服务信息，保障消费者知情权、自主选择权和公平交易权。 |")
    lines.append("| 消费者 | 依法、诚信、有证据地维权 | 消费者依法享有维权权利，但应遵循诚信原则，不得滥用权利损害经营者合法权益。 |")
    lines.append("| 用人单位/平台 | 是否管理、控制、支付报酬，是否依法解除 | 判断是否形成劳动关系，不能只看协议名称，应结合人格、经济和组织从属性。 |")
    lines.append("| 劳动者 | 如实说明、遵守纪律、商业秘密边界 | 劳动者应遵守劳动纪律和职业道德，履行与劳动合同直接相关的如实说明义务。 |")
    lines.append("| AI/平台企业 | 提示、审核、保密、权利边界 | 平台和企业应对算法、数据、作品和用户权益尽到必要提示、审核、保密和合规义务。 |")
    lines.append("| 当事人 | 程序、证据、请求 | 当事人维权应选择适当纠纷解决路径，围绕合同、付款、损害、因果关系和请求收集证据。 |")
    lines.append("")
    lines.append("## 第五部分：情境触发翻译词典")
    lines.append("")
    pairs = [
        ("付款、出票、中标通知", "要约、承诺、合同成立"),
        ("材质不符、虚假宣传、费用不清", "欺诈、知情权、自主选择权、惩罚性赔偿"),
        ("派单、签到、奖惩、结算、业务组成", "人格从属性、经济从属性、组织从属性"),
        ("包厢监控、聊天记录、公开发布", "隐私权、个人信息、停止侵害、赔礼道歉"),
        ("名称图标近似、引人误认", "混淆、不正当竞争、停止侵害、赔偿"),
        ("AI 承诺、AI 幻觉", "AI 不具备民事主体资格、提示义务、注意义务、损害和因果"),
        ("表格空格", "看示例、按格子填，不写散文"),
        ("起诉状", "诉讼请求、事实经过、法律理由"),
    ]
    for a, b in pairs:
        lines.append(f"- {a} -> {b}。")
    lines.append("")
    lines.append("## 第六部分：满分句工厂")
    lines.append("")
    lines.append("### 1. 表态句")
    lines.append("")
    lines.append("某请求应予支持/不予支持；某合同成立/不成立；某行为构成/不构成侵权、违约、欺诈或不正当竞争。")
    lines.append("")
    lines.append("### 2. 争点句")
    lines.append("")
    lines.append("本案争点在于材料中的某行为是否触发某法律规则，并导致某法律后果。")
    lines.append("")
    lines.append("### 3. 规则条件句")
    lines.append("")
    lines.append("依据相关法律，判断某责任是否成立，应看主体关系、行为性质、损害结果、过错或因果关系等条件。")
    lines.append("")
    lines.append("### 4. 材料嵌入句")
    lines.append("")
    lines.append("本案中，材料显示……，这些事实符合/不符合上述规则条件。")
    lines.append("")
    lines.append("### 5. 责任/程序落点句")
    lines.append("")
    lines.append("因此，某方应承担违约责任、侵权责任、停止侵害、赔偿损失、退款、赔礼道歉，或通过调解、仲裁、诉讼等路径维权。")
    lines.append("")
    lines.append("### 6. 价值收束句")
    lines.append("")
    lines.append("该处理有利于保护某主体合法权益，规范某类行为或行业秩序，引导社会成员依法行使权利、诚信履行义务。")
    lines.append("")
    lines.append("## 第七部分：六类考场产品")
    lines.append("")
    for card in CARD_ORDER:
        lines.append(f"### {CARD_TITLES.get(card, card)}")
        lines.append("")
        for item in CARD_STARTERS.get(card, []):
            lines.append(f"- {item}")
        lines.append("")
    lines.append("## 第八部分：27 核心逐题训练")
    lines.append("")
    lines.append("每题不再只给答案，而是按：材料一句话、争点一句话、第一判断、满分句零件、考场成稿、错法改法来训练。")
    lines.append("")
    for card in CARD_ORDER:
        rows = by_card.get(card, [])
        if not rows:
            continue
        lines.append(f"## {CARD_TITLES.get(card, card)}")
        lines.append("")
        for row in rows:
            lines.append(f"### 核心题 {row.get('display_index')}: {row.get('year')} {row.get('district')} {row.get('exam_stage')} 第{row.get('question_no')}题")
            lines.append("")
            lines.append(f"- question_id: `{row.get('question_id')}`")
            lines.append(f"- 设问：{one_line(row.get('ask_text', ''), 180)}")
            lines.append(f"- 材料一句话：{one_line(row.get('material_trigger', ''), 240)}")
            lines.append(f"- 这题争什么：{one_line(row.get('student_first_judgment_v5_5', row.get('minimum_judgment', '')), 180)}")
            lines.append("")
            lines.append("#### 满分前检查")
            for part in (row.get("student_score_checklist_v5_5") or "").split(" | "):
                if part.strip():
                    lines.append(f"- {part.strip()}")
            lines.append("")
            lines.append("#### 满分句零件")
            for part in (row.get("full_score_sentence_bank") or "").split(" | "):
                if part.strip():
                    lines.append(f"- {part.strip()}")
            lines.append("")
            lines.append("#### 考场成稿")
            lines.append("")
            lines.append((row.get("clean_exam_answer") or row.get("complete_answer_generated") or "").replace(" | ", "\n\n"))
            lines.append("")
            lines.append("#### 错法改法")
            lines.append("")
            lines.append(row.get("rewrite_cautions", "").strip() or "本题后续需补充真实错答改写。")
            lines.append("")
    lines.append("## 第九部分：38 非核心保分索引")
    lines.append("")
    lines.append("这部分不抢主线。它的用途是保分、守边界、提醒回源，不是扩核心。")
    lines.append("")
    for row in noncore:
        lines.append(f"### {row.get('title_with_id') or row.get('question_id')}")
        lines.append("")
        lines.append(f"- 标签：`{row.get('audit_category')}`")
        lines.append(f"- 证据等级：`{row.get('evidence_level')}`")
        lines.append(f"- 使用纪律：{NONCORE_KIND_GUIDE.get(row.get('audit_category', ''), row.get('student_category', ''))}")
        if row.get("duplicate_or_crossref"):
            lines.append(f"- 交叉引用：{row.get('duplicate_or_crossref')}")
        lines.append("")
        lines.append("最低可写三句：")
        for i in range(1, 4):
            val = row.get(f"minimum_sentence_{i}", "").strip()
            if val:
                lines.append(f"{i}. {val}")
        lines.append("")
        lines.append(f"别这样写：{row.get('do_not_write', '').strip()}")
        lines.append(f"能不能背：{row.get('memorization_status', '').strip()}")
        lines.append("")
    lines.append("## 第十部分：六大陷阱专项练")
    lines.append("")
    traps = [
        ("多小问漏问", "先拆问号，每个问号至少对应一段。"),
        ("表格格子错位", "先判格子功能，再写短答案。"),
        ("AI 宏观化", "先三分流：具体民事风险、综合治理、转出模块。"),
        ("价值空泛化", "本案处理、保护对象、规范对象、社会效果四步走。"),
        ("source-check 当满分", "按问法保分，不背成闭合答案。"),
        ("reference_only 误升核心", "只借表达，不借结论。"),
    ]
    for title, fix in traps:
        lines.append(f"- {title}：{fix}")
    lines.append("")
    lines.append("## 当前版本限制")
    lines.append("")
    lines.append("这是 V6 草案，不是最终发布稿。下一步必须吸收 GPTPro、Claude Opus、本地 student-agent 的攻击审查，并重新压测。")
    lines.append("")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    core_rows = read_csv(CORE_CSV)
    noncore_rows = read_csv(NONCORE_CSV)
    OUT.write_text(build_handbook(core_rows, noncore_rows), encoding="utf-8")
    PLAN_OUT.write_text(build_plan(core_rows, noncore_rows), encoding="utf-8")
    print(OUT)
    print(PLAN_OUT)
