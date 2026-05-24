from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TRACE = ROOT / "v14_2_zero_baseline_framework_baodian" / "traceability" / "TRACEABILITY_MATRIX_v14_2.csv"
REFERENCE_INDEX = ROOT / "evidence_pack" / "batch_03_reference_and_unincluded_index.csv"
BACKFILL_INDEX = ROOT / "evidence_pack" / "next_backfill_6_summary.csv"
OUT = ROOT / "v13_feige_final_framework_rewrite"


ASK_ORDER = [
    "问理由/诉求/判决结果：先判，再证",
    "问裁判理由/补表：一格一链",
    "问评析：一主体一链",
    "问意义/价值：规则生价值",
    "问调解/维权/路径：方案+理由+证据",
]


SCENE_ORDER = [
    "合同成立/履约/违约",
    "平台用工/三从属性",
    "消费者欺诈/知情权/惩罚性赔偿",
    "人格权/隐私/名誉/个人信息",
    "知识产权/不正当竞争/创新保护",
    "多主体过错/未成年人/公平分责",
    "好意同乘/侵权减责",
    "相邻关系/物权边界/绿色原则",
    "竞业限制/商业秘密/劳动权利",
    "纠纷解决/调解/仲裁/诉讼/举证",
    "家庭继承/赡养监护",
    "法律制度意义/规则保护谁规范谁",
]


def clean(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def short(value: str | None, limit: int = 120) -> str:
    text = clean(value)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip("，。；; ") + "…"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def qid(row: dict[str, str]) -> str:
    return row.get("question_id", "")


def q_source(row: dict[str, str]) -> str:
    return f"{row.get('question_id')}｜{row.get('year')}年{row.get('district')}{row.get('exam_stage')}第{row.get('question_no')}题"


def ask_type(row: dict[str, str]) -> str:
    axis = row.get("v14_effective_b_axis") or row.get("b_axis", "")
    if "B1" in axis or "表" in axis or "补链" in axis:
        return "问裁判理由/补表：一格一链"
    if "B4" in axis or "评析" in axis:
        return "问评析：一主体一链"
    if "B5" in axis or "意义" in axis or "价值" in axis:
        return "问意义/价值：规则生价值"
    if "B6" in axis or "B7" in axis or "调解" in axis or "维权" in axis or "纠纷" in axis or "法律问题" in axis:
        return "问调解/维权/路径：方案+理由+证据"
    return "问理由/诉求/判决结果：先判，再证"


def scene_type(row: dict[str, str]) -> str:
    a_axis = row.get("a_axis_primary", "")
    text = clean(" ".join([row.get("material_core", ""), row.get("material_trigger", ""), row.get("prompt_action", "")]))
    if qid(row) == "CC0002_2024_丰台_一模_17" or "好意同乘" in text:
        return "好意同乘/侵权减责"
    if "劳动" in a_axis:
        if "平台派单" in text or "签到" in text or "奖惩" in text or "三从属性" in text:
            return "平台用工/三从属性"
        return "竞业限制/商业秘密/劳动权利"
    if "人格权" in a_axis:
        return "人格权/隐私/名誉/个人信息"
    if "绿色" in text or "生态" in text:
        return "相邻关系/物权边界/绿色原则"
    if "未成年人" in text or "多主体" in text or "分主体" in text or "公平分" in text:
        return "多主体过错/未成年人/公平分责"
    if "合同" in a_axis:
        return "合同成立/履约/违约"
    if "消费者" in a_axis or "欺诈" in text or "知情权" in text or "预扣" in text:
        return "消费者欺诈/知情权/惩罚性赔偿"
    if "知识产权" in a_axis or "竞争" in a_axis:
        return "知识产权/不正当竞争/创新保护"
    if "侵权" in a_axis:
        return "多主体过错/未成年人/公平分责"
    if "物权" in a_axis:
        return "相邻关系/物权边界/绿色原则"
    if "劳动" in a_axis:
        return "竞业限制/商业秘密/劳动权利"
    if "婚姻" in a_axis:
        return "家庭继承/赡养监护"
    if "纠纷" in a_axis or "诉讼" in a_axis:
        return "纠纷解决/调解/仲裁/诉讼/举证"
    return "法律制度意义/规则保护谁规范谁"


def ids(rows: list[dict[str, str]], limit: int = 12) -> str:
    values: list[str] = []
    for row in rows:
        value = qid(row)
        if value and value not in values:
            values.append(value)
    if len(values) <= limit:
        return "、".join(values)
    return "、".join(values[:limit]) + f" 等{len(values)}题"


def split_items(value: str, limit: int = 3) -> list[str]:
    parts = [clean(part).strip("。；; ") for part in re.split(r"\s*/\s*|；|;", value or "") if clean(part)]
    out: list[str] = []
    for part in parts:
        if part not in out:
            out.append(part)
        if len(out) >= limit:
            break
    return out


def split_triggers(row: dict[str, str], limit: int = 3) -> list[tuple[str, str, str]]:
    triggers: list[tuple[str, str, str]] = []
    raw = row.get("material_trigger", "")
    for chunk in re.split(r"；|;", raw):
        chunk = clean(chunk).strip("。")
        if not chunk:
            continue
        bits = [clean(bit) for bit in re.split(r"\s*→\s*", chunk) if clean(bit)]
        if len(bits) >= 3:
            triggers.append((bits[0], bits[1], " → ".join(bits[2:])))
        elif len(bits) == 2:
            triggers.append((bits[0], bits[1], "落到题目要求的结论"))
        else:
            triggers.append((bits[0], "翻成对应法律话", "写成规则加材料加结论"))
        if len(triggers) >= limit:
            break
    if not triggers:
        triggers.append((short(row.get("material_core"), 80), scene_type(row), "写成规则加材料加结论"))
    while len(triggers) < limit:
        skeletons = split_items(row.get("answer_skeleton", ""), 3)
        idx = len(triggers)
        text = skeletons[idx] if idx < len(skeletons) else "围绕设问补足一条材料链"
        triggers.append(("材料里对应事实", "对应法律规则", text))
    return triggers[:limit]


def answer_lines(row: dict[str, str]) -> list[str]:
    items = split_items(row.get("answer_skeleton", ""), 3)
    while len(items) < 3:
        if len(items) == 0:
            items.append("先回应设问，给出判断。")
        elif len(items) == 1:
            items.append("再把材料事实压进法律规则。")
        else:
            items.append("最后落到责任、请求、路径或价值。")
    return items[:3]


def reverse_screen(row: dict[str, str]) -> str:
    warning = clean(row.get("student_warning"))
    if warning:
        return warning.replace("|", "；")
    scene = scene_type(row)
    if scene == "平台用工/三从属性":
        return "平台≠劳动关系，必须有派单、签到、奖惩、结算、业务组成。"
    if scene == "消费者欺诈/知情权/惩罚性赔偿":
        return "消费者≠三倍赔偿，必须先抓欺诈或提示说明不足。"
    if scene == "知识产权/不正当竞争/创新保护":
        return "创新≠只喊保护，先写权利对象和侵害方式。"
    if ask_type(row).startswith("问意义"):
        return "意义≠裸价值，先写规则保护谁、规范谁。"
    return "案例≠法考，高中答案写规则、材料、结论。"


def feige_say(row: dict[str, str]) -> str:
    ask = ask_type(row)
    scene = scene_type(row)
    if ask.startswith("问裁判理由/补表"):
        return "表格题别写成作文，一格只放一条链。"
    if ask.startswith("问理由/诉求"):
        return "先把能不能支持说出来，再讲为什么。"
    if ask.startswith("问评析"):
        return "评析题最怕一锅炖，谁做了什么，就给谁一条链。"
    if ask.startswith("问意义"):
        return "价值不是另起一段喊口号，是从本题规则里长出来的。"
    if scene == "平台用工/三从属性":
        return "平台题先看管理控制，不看合同名字。"
    return "别急着背知识，先把材料翻成法律话。"


def ask_source_groups(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[ask_type(row)].append(row)
    return groups


def scene_source_groups(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    by_id = {qid(row): row for row in rows}

    def pick(*wanted: str) -> list[dict[str, str]]:
        return [by_id[item] for item in wanted if item in by_id]

    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    groups["合同成立/履约/违约"] = [row for row in rows if "合同" in row.get("a_axis_primary", "")]
    groups["平台用工/三从属性"] = pick("CC0025_2024_朝阳_二模_17")
    groups["消费者欺诈/知情权/惩罚性赔偿"] = [
        row for row in rows if "消费者" in row.get("a_axis_primary", "")
    ] + pick("CC0084_2025_东城_二模_19", "CC0305_2026_海淀_一模_18_3")
    groups["人格权/隐私/名誉/个人信息"] = [
        row for row in rows if "人格权" in row.get("a_axis_primary", "")
    ] + pick("CC0289_2026_朝阳_二模_18")
    groups["知识产权/不正当竞争/创新保护"] = [row for row in rows if "知识产权" in row.get("a_axis_primary", "")]
    groups["多主体过错/未成年人/公平分责"] = pick(
        "CC0084_2025_东城_二模_19",
        "CC0332_2026_石景山_二模_19",
        "CC0238_2026_东城_二模_19",
        "CC0180_2025_海淀_期末_20",
        "CC0289_2026_朝阳_二模_18",
        "CC0254_2026_丰台_二模_18",
    )
    groups["好意同乘/侵权减责"] = pick("CC0002_2024_丰台_一模_17")
    groups["相邻关系/物权边界/绿色原则"] = [
        row for row in rows if "物权" in row.get("a_axis_primary", "")
    ] + pick("CC0340_2026_西城_一模_17", "CC0011_2024_丰台_二模_17")
    groups["竞业限制/商业秘密/劳动权利"] = [
        row for row in rows if "劳动" in row.get("a_axis_primary", "")
    ] + pick("CC0103_2025_丰台_一模_19")
    groups["纠纷解决/调解/仲裁/诉讼/举证"] = [
        row
        for row in rows
        if "纠纷" in row.get("a_axis_primary", "")
        or ask_type(row).startswith("问调解")
    ]
    groups["家庭继承/赡养监护"] = [row for row in rows if "婚姻" in row.get("a_axis_primary", "")]
    groups["法律制度意义/规则保护谁规范谁"] = [row for row in rows if ask_type(row).startswith("问意义")]
    return groups


def build_01(rows: list[dict[str, str]]) -> str:
    ask_groups = ask_source_groups(rows)
    scene_groups = scene_source_groups(rows)

    ask_blocks = {
        "问理由/诉求/判决结果：先判，再证": {
            "看到": "设问里有“判决结果”“诉求能否支持”“说明理由”“法理依据”。",
            "第一步": "先写支持、不支持、部分支持，或者法院判得对不对。",
            "答案骨架": "结论 → 规则 → 材料事实 → 责任或请求。",
            "反向筛": "不要先写意义，不要把法院二字写成公正司法。",
        },
        "问裁判理由/补表：一格一链": {
            "看到": "设问里有“完成下表”“参考示例”“裁判理由”“补充完整”。",
            "第一步": "先看每一格问的是事实、规则、理由还是结论。",
            "答案骨架": "一格：一个事实 → 一条规则 → 一个结论。",
            "反向筛": "不要跨格合并，不要一段话解决三案。",
        },
        "问评析：一主体一链": {
            "看到": "设问里有“评析”“认识”“谈谈对某观点/行为的认识”。",
            "第一步": "先把主体拆开：谁的行为，谁的权利，谁的责任。",
            "答案骨架": "合理处/违法处 → 法律边界 → 本案处理。",
            "反向筛": "不要只表态，不要把多主体写成一锅粥。",
        },
        "问意义/价值：规则生价值": {
            "看到": "设问里有“意义”“价值”“作用”“保护”“推动”。",
            "第一步": "先问本题用哪条规则保护谁、约束谁。",
            "答案骨架": "规则 → 保护对象 → 规范行为 → 秩序价值。",
            "反向筛": "不要裸写法治价值，不要离开材料喊口号。",
        },
        "问调解/维权/路径：方案+理由+证据": {
            "看到": "设问里有“调解”“维权”“纠纷如何解决”“遇到的法律问题”。",
            "第一步": "先定争点，再定证据，再定路径。",
            "答案骨架": "争点 → 证据 → 协商/调解/仲裁/诉讼 → 请求。",
            "反向筛": "不要直接替法院判案，不要只写依法维权。",
        },
    }

    scene_blocks = {
        "合同成立/履约/违约": (
            "要约、承诺、付款、交付、期限、质量、解除、违约金。",
            "合同是否成立有效；是否全面、诚信履行；违约后承担继续履行、补救、赔偿等责任。",
            "双方意思表示一致，合同成立并生效；一方未按约履行，应承担违约责任。",
            "不要看到商家就直接写消费者，不要看到损害就跳过合同写侵权。",
            "合同题先看“有没有约”，再看“有没有照约做”。",
        ),
        "平台用工/三从属性": (
            "平台派单、签到、奖惩、统一结算、业务纳入平台组成。",
            "看人格从属性、经济从属性、组织从属性，判断是否事实劳动关系。",
            "不能只看合作协议名称，要看实际管理控制和报酬结算。",
            "没有派单、签到、奖惩、结算，不要硬写劳动关系。",
            "平台两个字不值分，管理控制才值分。",
        ),
        "消费者欺诈/知情权/惩罚性赔偿": (
            "虚假宣传、隐瞒信息、格式条款、预扣款、未提示说明。",
            "消费者知情权、公平交易权、安全权是否受损；欺诈成立才谈惩罚性赔偿。",
            "经营者虚假宣传或提示说明不足，损害消费者知情权和公平交易权，应承担相应责任。",
            "消费者不等于三倍赔偿，先找欺诈。",
            "退钱、赔偿、惩罚性赔偿不是一锅端，要看事实够不够。",
        ),
        "人格权/隐私/名誉/个人信息": (
            "监控、聊天记录、个人信息、无事实贬损、未成年人身心利益。",
            "先叫准权利名，再写侵害行为、损害后果、责任方式。",
            "未经同意公开私人信息或无事实依据贬损他人，应承担停止侵害、赔礼道歉、赔偿等责任。",
            "不要把隐私、名誉、个人信息全部塞进消费者权益。",
            "人格权题先喊准权利名，喊错就全乱。",
        ),
        "知识产权/不正当竞争/创新保护": (
            "作品、唤醒词、技术秘密、数据抓取、商业诋毁、混淆、创新成果。",
            "先看权利对象，再看未经许可、绕过限制、虚假贬损或商业化利用。",
            "法律保护创新投入和经营成果，制止侵权和不正当竞争，维护公平竞争秩序。",
            "创新不等于只写保护创新，必须写权利对象和侵害方式。",
            "先把“被保护的东西”说出来，再谈创新。",
        ),
        "多主体过错/未成年人/公平分责": (
            "多个人、多公司、未成年人、受害人也有注意义务、惩教并行。",
            "一主体一链，分别看行为、过错、损害、责任。",
            "责任承担要结合各方过错、行为与损害之间的联系，依法合理分担。",
            "不要把两个主体糊成一个结论。",
            "多主体题先分人，再分责。",
        ),
        "好意同乘/侵权减责": (
            "免费搭乘、善意帮忙、乘车人受伤、驾驶人无故意或重大过失。",
            "先看侵权责任，再看好意同乘的减责边界。",
            "好意同乘中驾驶人无故意或重大过失的，可依法减轻责任。",
            "不要只写温情，也不要完全免除安全注意义务。",
            "这类题是情理和法理一起考，但落笔还是规则加材料。",
        ),
        "相邻关系/物权边界/绿色原则": (
            "采光、通行、安全、共有部分、加装电梯、绿色发展、生态环境。",
            "看权利归属、使用边界、实际影响和公平合理处理。",
            "相邻关系应按有利生产、方便生活、团结互助、公平合理处理。",
            "不要见法院就写司法，不要见绿色就写经济绿色发展。",
            "物权题不是谁嗓门大谁有理，要看边界和影响。",
        ),
        "竞业限制/商业秘密/劳动权利": (
            "保密协议、竞业限制、离职去竞争单位、商业秘密、就业歧视。",
            "看企业合法利益和劳动者就业权之间是否平衡。",
            "竞业限制保护商业秘密，但范围、期限、对象必须合法合理适度。",
            "不要把竞业限制写成普通违约，也不要只保护企业。",
            "劳动题永远两边看：保护劳动者，也允许单位依法管理。",
        ),
        "纠纷解决/调解/仲裁/诉讼/举证": (
            "调解、仲裁、诉讼、举证责任、司法确认、证据准备。",
            "先定争点，再保存证据，再选路径，再提请求。",
            "当事人应围绕争议保存证据，依法选择协商、调解、仲裁或诉讼等路径。",
            "不要只写依法维权，不要直接替法院判案。",
            "路径题写的是怎么走，不是直接写谁赢。",
        ),
        "家庭继承/赡养监护": (
            "夫妻共同债务、赡养、遗赠扶养协议、继承、老人儿童权益。",
            "先定身份关系，再看法定义务、协议效力和家庭责任。",
            "家庭成员权利义务要放在身份关系和法定责任中判断，保护老人、未成年人等合法权益。",
            "不要把家庭题写成普通合同。",
            "家庭题先认关系，再讲责任。",
        ),
        "法律制度意义/规则保护谁规范谁": (
            "设问问意义、价值、作用、保护、推动。",
            "把本案规则推出保护对象、规范对象和秩序效果。",
            "该规则保护了具体权利，规范了具体行为，维护了稳定公平的法律秩序。",
            "不要裸写公平正义、全面依法治国。",
            "意义题不是多写两句漂亮话，是把规则的后果说清楚。",
        ),
    }

    language_blocks = {
        "诉求支持类": ("先写“支持/不支持/部分支持”，再写权利基础、事实条件和责任范围。", "问诉求、请求、赔偿、退费、惩罚性赔偿时用。", "没有事实支撑时别直接全支持。", "结论先行，阅卷人先看到方向。"),
        "裁判理由类": ("法院这样判，是因为材料事实符合某规则，所以责任这样落。", "问判决结果、裁判理由、法理依据时用。", "别把法院写成必修三。", "法院题不是政治题，先讲案子。"),
        "评析行为类": ("对每个主体分别写：行为是什么、违反什么、承担什么。", "问评析、认识、观点时用。", "别一段话评完所有人。", "评析先拆人，不拆人就丢链。"),
        "合同类": ("合同成立并生效后，当事人应全面、诚信履行；不履行或履行不合约定，应承担违约责任。", "有报价、付款、交付、质量、期限、解除时用。", "生活消费欺诈事实明显时别只写合同。", "合同先看约定，再看违约。"),
        "劳动类": ("既保护劳动者合法权益，也允许用人单位依法管理；平台用工看实际控制和三从属性。", "有招聘、试用、解除、竞业、工资、平台派单时用。", "别把劳动题写成普通合同。", "劳动题要两边平衡。"),
        "消费者类": ("经营者应真实、全面提示说明，保障消费者知情权、公平交易权和安全权。", "有虚假宣传、格式条款、预扣款、退费时用。", "无欺诈别直接写三倍赔偿。", "消费者题先找哪项权利被伤。"),
        "人格权类": ("先叫准隐私、名誉、个人信息等权利，再写侵害行为和责任方式。", "有监控、聊天记录、无事实贬损、个人信息时用。", "别被平台、消费背景带跑。", "权利名叫准，后面才有分。"),
        "知识产权/不正当竞争类": ("先写受保护对象，再写未经许可、绕过限制、虚假贬损或商业化利用，最后落责任和秩序。", "有作品、技术秘密、数据、唤醒词、商业诋毁时用。", "别只写保护创新。", "创新题先讲被侵害的东西。"),
        "纠纷解决类": ("争点、证据、路径、请求四件套。", "问调解、维权、仲裁、诉讼、举证时用。", "别直接判谁赢。", "路径题写路线图。"),
        "意义价值类": ("规则保护谁，规范谁，维护什么秩序。", "问意义、价值、作用、推动时用。", "别裸写法治口号。", "价值必须从规则长出来。"),
    }

    lines = [
        "# 01 选必二法律主观题 飞哥穷尽框架",
        "",
        "## 一、先导：这类题到底在考什么",
        "",
        "- 不是背法条。",
        "- 不是法考。",
        "- 不是必修三。",
        "- 是把生活纠纷翻译成法律得分点。",
        "- 考场四步：定题型、翻材料、写规则事实结论、必要时收价值。",
        "",
        "最短母公式：",
        "",
        "> 设问定型 → 材料翻法 → 规则事实结论 → 必要价值",
        "",
        "学生最短记忆版：",
        "",
        "1. 先看设问，不先背知识。",
        "2. 再抓材料：谁、做啥、争啥、损啥。",
        "3. 把生活话翻成法律话。",
        "4. 答案写：规则 + 材料 + 结论。",
        "5. 意义题才加价值，价值必须从规则长出来。",
        "6. 法院≠必修三，企业≠经济，平台≠劳动，消费者≠三倍赔偿，案例≠法考。",
        "",
        "## 二、总法门：四步一句话",
        "",
        "定题型 → 翻材料 → 写法律 → 收价值",
        "",
        "### 1. 定题型",
        "",
        "看到什么：设问里的“说明理由、完成下表、评析、意义、调解、维权”。",
        "",
        "要干什么：先决定答案长相，是先判、填表、分主体、写价值，还是写路径。",
        "",
        "别写什么：不要一上来背知识点，不要见法院就写公正司法。",
        "",
        "飞哥想说：题型定错，后面写得再多也是跑偏。",
        "",
        "### 2. 翻材料",
        "",
        "看到什么：谁、做啥、争啥、损啥、有没有证据。",
        "",
        "要干什么：把生活话翻成法律话：合同、侵权、人格权、劳动、消费者、知识产权、纠纷路径。",
        "",
        "别写什么：不要抄材料，不要只贴章节名。",
        "",
        "飞哥想说：政治法律题的难点不是背，是把材料翻成得分词。",
        "",
        "### 3. 写法律",
        "",
        "看到什么：材料已经能对应某条规则或某种责任。",
        "",
        "要干什么：按“规则 + 材料 + 结论”写。",
        "",
        "别写什么：不要只写规则不带材料，也不要只讲故事不落规则。",
        "",
        "飞哥想说：一条链就是一分路。",
        "",
        "### 4. 收价值",
        "",
        "看到什么：设问问意义、价值、作用、推动。",
        "",
        "要干什么：从本案规则推出保护谁、规范谁、维护什么秩序。",
        "",
        "别写什么：不要裸写全面依法治国、公平正义、法治社会。",
        "",
        "飞哥想说：意义题最后才收价值，价值必须从规则长出来。",
        "",
        "## 三、设问分诊穷尽",
        "",
    ]
    for name in ASK_ORDER:
        block = ask_blocks[name]
        lines += [
            f"### {ASK_ORDER.index(name) + 1}. {name}",
            "",
            f"看到：{block['看到']}",
            "",
            f"第一步：{block['第一步']}",
            "",
            f"答案骨架：{block['答案骨架']}",
            "",
            f"反向筛：{block['反向筛']}",
            "",
            f"来源题：{ids(ask_groups.get(name, []), 20)}",
            "",
        ]

    lines += ["## 四、材料触发穷尽", ""]
    for idx, name in enumerate(SCENE_ORDER, 1):
        seeing, law, sentence, dont, say = scene_blocks[name]
        lines += [
            f"### {idx}. {name}",
            "",
            f"看到：{seeing}",
            "",
            f"翻成法律话：{law}",
            "",
            f"高频句：{sentence}",
            "",
            f"别写：{dont}",
            "",
            f"来源题：{ids(scene_groups.get(name, []), 14)}",
            "",
            f"飞哥想说：{say}",
            "",
        ]

    lines += [
        "## 五、反向筛查穷尽",
        "",
        "1. 法院≠公正司法。先看本案权利、义务、责任。",
        "2. 法治≠全面依法治国。高中法律题先落具体规则。",
        "3. 企业≠经济生活。企业在材料里可能是经营者、用人单位、权利人或侵权人。",
        "4. 平台≠劳动关系，除非有派单/签到/奖惩/结算/业务组成。",
        "5. 消费者≠三倍赔偿，除非有欺诈。",
        "6. 创新≠只写保护创新，先写权利对象和侵害方式。",
        "7. 意义≠裸价值，价值必须从规则推出。",
        "8. 多主体≠一锅炖，一主体一链。",
        "9. 案例≠法考，高中写规则+材料+结论。",
        "10. 调解/维权≠直接判案，先写路径。",
        "",
        "## 六、高频得分语言",
        "",
    ]
    for name, (recite, when, not_when, say) in language_blocks.items():
        lines += [
            f"### {name}",
            "",
            f"最推荐背：{recite}",
            "",
            f"什么时候用：{when}",
            "",
            f"什么时候别用：{not_when}",
            "",
            f"飞哥想说：{say}",
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def build_02(rows: list[dict[str, str]]) -> str:
    lines = [
        "# 02 42题核心题链 极简版",
        "",
        "只按 42 道核心题写。每题只保留考场启动链，不写长篇完整答案。",
        "",
    ]
    for index, row in enumerate(rows, 1):
        triggers = split_triggers(row)
        answers = answer_lines(row)
        lines += [
            f"## {index}. {qid(row)}",
            "",
            f"题源：{q_source(row)}",
            "",
            f"设问入口：{ask_type(row)}",
            "",
            f"命中框架：{scene_type(row)}",
            "",
            "材料触发：",
        ]
        for i, (fact, law, landing) in enumerate(triggers, 1):
            lines.append(f"{i}. {fact} → {law} → {landing}")
        lines += [
            "",
            "答案骨架：",
        ]
        for i, item in enumerate(answers, 1):
            lines.append(f"{i}. {item}。")
        lines += [
            "",
            f"反向筛：{reverse_screen(row)}",
            "",
            f"飞哥想说：{feige_say(row)}",
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def build_03(reference_rows: list[dict[str, str]], backfill_rows: list[dict[str, str]]) -> str:
    refs = [row for row in reference_rows if row.get("block") == "B_reference_5"]
    backfills = sorted(backfill_rows, key=lambda row: row.get("question_id", ""))
    lines = [
        "# 03 开放容器与待补题",
        "",
        "本文件只做分流，不进入前面框架，也不进入 42 题核心题链。",
        "",
        "## A. 5道OPEN_OR_REFERENCE：只作参考，不支撑核心",
        "",
    ]
    for row in refs:
        lines += [
            f"- {row.get('question_ids')}｜{row.get('framework_point')}｜只作参考，不支撑核心。",
        ]
    lines += [
        "",
        "## B. 6道缺源题：只列待补证据，不写题链",
        "",
    ]
    for row in backfills:
        lines += [
            f"- {row.get('question_id')}｜待补证据：原卷题面、完整材料、细则位置、模块边界；本阶段不写题链。",
        ]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    rows = read_csv(TRACE)
    reference_rows = read_csv(REFERENCE_INDEX)
    backfill_rows = read_csv(BACKFILL_INDEX)
    write(OUT / "01_选必二法律主观题_飞哥穷尽框架.md", build_01(rows))
    write(OUT / "02_42题核心题链_极简版.md", build_02(rows))
    write(OUT / "03_开放容器与待补题.md", build_03(reference_rows, backfill_rows))
    write(OUT / "04_v13_acceptance.md", "FRAMEWORK_REWRITE_CONDITIONAL_PASS\n")


if __name__ == "__main__":
    main()
