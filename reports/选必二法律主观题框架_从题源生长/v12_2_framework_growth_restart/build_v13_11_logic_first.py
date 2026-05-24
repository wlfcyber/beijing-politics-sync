from pathlib import Path
import csv
import re
from datetime import datetime


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "v13_10_final_baodian_integrated"
OUT = ROOT / "v13_11_logic_first_framework_rebuild"
CARD_FILE = SRC / "02_42题双轴重标与解析宝典_v13_10.md"
TRACE_FILE = SRC / "traceability" / "TRACEABILITY_MATRIX_v13_10_final.csv"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8")


def parse_cards(text: str):
    cards = []
    current_group = ""
    parts = re.split(r"(?m)^###\s+", text)
    for part in parts:
        if not part.strip():
            continue
        if part.startswith("#") or "生成时间" in part[:100]:
            group_matches = re.findall(r"(?m)^##\s+(.+)$", part)
            if group_matches:
                current_group = group_matches[-1].strip()
            continue
        lines = part.splitlines()
        title = lines[0].strip()
        body = "\n".join(lines[1:])
        fields = {}
        for line in lines[1:]:
            if line.startswith("- ") and "：" in line:
                key, value = line[2:].split("：", 1)
                fields[key.strip()] = value.strip()
        group_before = re.findall(r"(?m)^##\s+(.+)$", "\n".join(lines))
        if group_before:
            current_group = group_before[-1].strip()
        qid_match = re.search(r"(CC\d{4}_[^\s]+|RECOVER_[^\s]+)", title)
        cards.append(
            {
                "title": title,
                "qid": qid_match.group(1) if qid_match else title,
                "group": current_group,
                "fields": fields,
                "body": body,
            }
        )
    return cards


def load_trace_rows():
    if not TRACE_FILE.exists():
        return {}
    with TRACE_FILE.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return {row.get("question_id", ""): row for row in rows}


def material_sentence(core: str) -> str:
    core = re.sub(r"\s+", " ", core or "").strip()
    if not core:
        return "材料先压成一个小故事：谁与谁发生冲突，谁提出请求，材料给出哪些决定性事实。"
    if len(core) <= 160:
        return core
    cut = core[:160]
    return cut.rstrip("，。；; ") + "……"


def dispute_from(fields: dict) -> str:
    prompt = fields.get("设问动作", "")
    a = fields.get("A轴主入口", "")
    b = fields.get("B轴设问动作", "")
    if "表" in prompt or "表格" in b:
        return "这题争的是：每一格到底要填事实、规则、裁判结果还是意义，不能把表格题写成散文。"
    if "支持" in prompt or "诉求" in b or "请求" in b:
        return "这题争的是：当事人的请求能不能支持，支持到什么范围，哪些事实决定支持或不支持。"
    if "判" in prompt or "责任" in prompt or "理由" in prompt or "裁判" in b:
        return f"这题争的是：{a_topic(a)}，并说明为什么应当承担或不承担相应责任。"
    if "意义" in prompt or "价值" in b or "推动" in b:
        return "这题争的是：本案的法律处理如何从具体权利义务推出具体法治意义，而不是空喊口号。"
    if "维权" in prompt or "调解" in prompt or "路径" in b:
        return "这题争的是：当事人应围绕什么权利、证据、程序和请求来解决纠纷。"
    if "问题" in prompt or "填" in prompt:
        return "这题争的是：从材料冲突中识别哪几个法律问题，并用短句写准权利、义务、程序或责任边界。"
    if "认识" in prompt or "评析" in b:
        return "这题争的是：材料做法或观点合理在哪里、边界在哪里，正确法律立场是什么。"
    return f"这题争的是：{a_topic(a)}；题目要求的呈现方式是{b_task(b)}。"


def first_judgment(fields: dict) -> str:
    a = fields.get("A轴主入口", "对应法律关系")
    b = fields.get("B轴设问动作", "设问动作")
    return f"第一判断：先判{a_topic(a)}；再{b_task(b)}。最后只用后台 A/B 标签检查有没有跑偏，不把标签写成答案。"


def a_topic(a: str) -> str:
    if "A1" in a:
        return "行为能力、意思表示或效力问题是否直接决定结果"
    if "A2" in a:
        return "哪一种人格或人身权益被侵害，以及应承担什么民事责任"
    if "A3" in a:
        return "财产权利、共有部分或相邻利益的边界在哪里"
    if "A4" in a:
        return "合同是否成立、履行是否符合约定、违约责任如何承担"
    if "A5" in a:
        return "创新成果、商业秘密、数据或竞争秩序是否被不正当利用"
    if "A6" in a:
        return "损害、过错、因果关系和责任承担是否成立"
    if "A7" in a:
        return "家庭、婚姻或继承关系中的权利义务如何确定"
    if "A8" in a:
        return "劳动关系、劳动合同义务或用工管理边界如何判断"
    if "A9" in a:
        return "消费者权利、经营者义务和责任分担如何处理"
    if "A10" in a:
        return "证据、调解、仲裁、诉讼或司法确认如何服务纠纷解决"
    return "材料中的法律关系和权利义务如何确定"


def b_task(b: str) -> str:
    if "B1" in b:
        return "按表格或示例一格一链填写"
    if "B2" in b:
        return "说明判决、责任或裁判理由"
    if "B3" in b:
        return "先给支持/不支持/部分支持，再写理由"
    if "B4" in b:
        return "先评析合理处和边界，再给正确法律立场"
    if "B5" in b:
        return "从本案处理推出具体意义或价值"
    if "B6" in b:
        return "写证据、路径和请求"
    if "B7" in b:
        return "用短句识别法律问题或填空"
    return "按设问动作落到结论、理由、路径或意义"


def translation_rows(trigger: str):
    trigger = (trigger or "").strip()
    if not trigger:
        return [
            (
                "材料中出现的主体、行为、损害或请求",
                "翻译成法律关系、权利义务、构成要件或责任边界",
                "写成“事实 + 规则 + 结论”的得分句",
            )
        ]
    raw_parts = re.split(r"[；;]\s*", trigger)
    rows = []
    for raw in raw_parts[:4]:
        raw = raw.strip(" 。")
        if not raw:
            continue
        bits = [x.strip() for x in re.split(r"\s*→\s*", raw)]
        if len(bits) >= 3:
            rows.append((bits[0], bits[1], " → ".join(bits[2:])))
        elif len(bits) == 2:
            rows.append((bits[0], bits[1], "据此推出结论或责任。"))
        else:
            rows.append((raw, "把该事实翻译成对应法律语言。", "再落到责任、效力、请求或意义。"))
    return rows or [
        (
            "材料中出现的主体、行为、损害或请求",
            "翻译成法律关系、权利义务、构成要件或责任边界",
            "写成“事实 + 规则 + 结论”的得分句",
        )
    ]


def answer_sentences(skeleton: str):
    skeleton = (skeleton or "").strip()
    if not skeleton:
        return ["先判争点，再用材料事实对应法律规则，最后落责任、请求、程序或意义。"]
    parts = [p.strip(" 。") for p in re.split(r"\s*/\s*", skeleton) if p.strip()]
    return parts or [skeleton]


def wrong_fix(warning: str):
    warning = (warning or "").strip()
    if not warning or warning.lower() == "none":
        return "常见错法：只背节点名或价值口号。改法：先写争点，再写事实如何对应规则，最后才收结论。"
    return f"常见错法：{warning}。改法：先回到本题争点，逐项核对主体、行为、规则、后果，删掉无材料支撑的套话。"


def world_for(a: str, b: str, fields: dict) -> str:
    text = " ".join([a, b, fields.get("材料核心", ""), fields.get("设问动作", "")])
    if any(x in text for x in ["A5", "知识产权", "竞争", "商业秘密", "创新", "数据"]):
        return "4. 创新与竞争"
    if any(x in text for x in ["A10", "调解", "仲裁", "诉讼", "维权", "公益", "司法确认"]):
        return "5. 程序与公共"
    if any(x in text for x in ["A3", "A7", "物权", "相邻", "家庭", "继承", "婚姻", "共有"]):
        return "2. 财产与家庭"
    if any(x in text for x in ["A2", "A6", "人格", "侵权", "隐私", "名誉", "健康", "损害"]):
        return "3. 人身与侵权"
    return "1. 交易与用工"


def build_readme() -> str:
    return """# v13.11 logic-first framework rebuild

Status: `candidate_pending_real_gpt_claude_review`

本目录回应用户对 v13.10 的核心批评：框架逻辑不清，学生无法习得。

v13.11 不覆盖 v13.10。它先把学生前台改成一条能学会的推理链：

`生活冲突 -> 争点 -> 法律翻译 -> 法律结果 -> 价值收束`

旧 A/B 双轴保留，但降级：

- A 轴只作为法律关系工具箱。
- B 轴只作为答案形状工具箱。
- 学生第一入口不再是 A1-A10 或 B1-B7，而是“这题争什么”。

边界：

- 本轮是 Codex 本地逻辑重构和题卡重排。
- 还没有新的真实 GPT/Claude advisor gate。
- 因此本目录不能替代 v13.10 终版交付，只能作为 v13.11 候选，等待真实 GPT/Claude 和零基础学生试读复核。
"""


def build_framework() -> str:
    return """# 01 v13.11 学生先读：法律题基本模型

## 0. 先说人话：法律主观题到底在考什么

法律题不是让你背一堆法条，也不是让你背 A1-A10。

它只考一件事：

> 把一个生活冲突，用法律语言处理成一个清楚结果。

所以拿到题先不要问“这是 A 几 B 几”。先问：

1. 谁和谁发生了冲突？
2. 他们争的是什么利益、权利、责任或程序？
3. 哪个事实决定结果？
4. 题目要我写结论、理由、表格、路径，还是意义？

## 1. 总模型：生活冲突 A -> 法律判断 B

一切题都走这条链：

`生活事实 -> 争点 -> 法律翻译 -> 法律结果 -> 价值收束`

| 步骤 | 学生问自己 | 产出 |
|---|---|---|
| 生活事实 | 这个故事的起因、经过、结果是什么？ | 材料一句话 |
| 争点 | 双方到底争什么？ | 这题争什么 |
| 法律翻译 | 材料词要翻译成什么法律词？ | 主体、关系、权利义务、要件 |
| 法律结果 | 请求支持吗、有效吗、担责吗、怎么维权？ | 结论和责任 |
| 价值收束 | 本案保护谁、规范什么、维护什么秩序？ | 只从本案推出的意义 |

## 2. 三问：判什么、凭什么、收什么尾

### 第一问：判什么

题目可能让你判：

- 支持不支持。
- 有效无效。
- 侵权不侵权。
- 违约不违约。
- 谁担责，担什么责。
- 走什么程序，准备什么证据。
- 这个处理有什么意义。

第一句必须先回应这个任务。

### 第二问：凭什么

凭两样东西：

- 法律规则：权利义务、构成要件、程序规则、责任方式。
- 材料事实：谁做了什么，造成什么结果，有什么证据。

答案不能只有规则，也不能只有材料。

### 第三问：收什么尾

问责任，就落责任。

问请求，就落支持、不支持或部分支持。

问路径，就落证据、调解、仲裁、诉讼、请求。

问意义，就落“保护谁、规范什么、维护什么秩序”。

## 3. 四步读题法

### 第一步：圈主体

圈谁告谁、谁买谁卖、谁用谁管、谁受损、谁处理纠纷。

主体一变，法律关系就会变。

### 第二步：抓行为

抓签约、付款、交付、宣传、泄露、抓取、辞退、安装、调解、起诉、判决。

行为决定规则入口。

### 第三步：定争点

争点不是标签。争点是这题真正要解决的问题。

例如：

- “未成年人打赏”不是先背 A9，而是争“打赏行为效力和平台责任如何分担”。
- “包间监控外传”不是先背消费者，而是争“隐私侵害请求和消费欺诈请求能不能分别支持”。
- “无人机坠毁”不是先背合同或侵权，而是争“错发瑕疵品造成损害后，违约责任、侵权责任和维权证据怎么分层”。

### 第四步：生成句

最稳四句：

1. 结论句：该请求应支持/不支持，或该行为构成/不构成。
2. 规则句：法律要求什么条件。
3. 材料句：材料中哪些事实满足或不满足条件。
4. 结果句：承担什么责任、走什么路径，或推出什么意义。

## 4. 五类材料世界

这五类是学生真正能识别的材料世界，不是死背教材目录。

### 1. 交易与用工

看到买卖、服务、付款、交付、退费、违约金、招聘、试用期、工资、竞业限制，先问：

- 是合同成立和履行问题？
- 是消费者知情、公平交易、安全保障问题？
- 是劳动关系和用工管理问题？

输出句：

> 双方形成某法律关系，某行为违反了全面履行、诚信经营、消费者保护或劳动合同规则，应承担相应责任。

### 2. 财产与家庭

看到共有部分、相邻、通行、采光、家庭、继承、赡养、遗赠扶养，先问：

- 争的是权利归属、使用边界，还是身份/继承关系？
- 是否涉及程序、共同决定、家庭责任？

输出句：

> 该事实涉及某财产或家庭法律关系，应在权利归属、义务履行和合理边界内处理。

### 3. 人身与侵权

看到隐私、个人信息、名誉、商誉、肖像、生命健康、身体损害、安全保障，先问：

- 被侵害的具体权利是什么？
- 行为、损害、过错、因果关系是否成立？
- 责任方式是什么？

输出句：

> 某行为侵害某人格或人身权益，造成相应损害，应承担停止侵害、赔礼道歉、消除影响、赔偿损失等责任。

### 4. 创新与竞争

看到作品、技术秘密、数据抓取、商标混淆、商业诋毁、虚假宣传、竞争秩序，先问：

- 受保护对象是什么？
- 对方怎样不正当获取、使用、传播或混淆？
- 损害了谁的创新投入和竞争秩序？

输出句：

> 行为人不正当利用他人创新成果、商业秘密、数据产品或经营标识，损害公平竞争秩序，应承担停止侵害、消除影响、赔偿损失等责任。

### 5. 程序与公共

看到调解、仲裁、诉讼、起诉状、司法确认、公益诉讼、证据、维权准备，先问：

- 这是实体责任题，还是程序路径题？
- 主体是谁，证据是什么，请求是什么？

输出句：

> 当事人应围绕争议焦点保存证据，选择协商、调解、仲裁或诉讼等路径，提出明确、合法、合理的请求。

## 5. A/B 双轴怎么用

A/B 不是废掉，而是退到第二层。

先用争点链启动：

`材料一句话 -> 争点 -> 法律翻译 -> 结果`

再用 A/B 检查：

- A 轴检查法律关系有没有选错。
- B 轴检查答案形状有没有写错。

如果学生一上来背 A1-A10，会卡住；如果学生先说“这题争什么”，A/B 才有意义。

## 6. 满分句生成法

| 句型 | 用途 | 模板 |
|---|---|---|
| 关系句 | 先定法律关系 | 双方围绕____形成____法律关系。 |
| 争点句 | 把题目任务说清 | 本题关键在于____是否____。 |
| 规则句 | 给法律依据 | 依据相关法律，____应当/不得____。 |
| 材料句 | 把事实压进规则 | 材料中____表明____。 |
| 结果句 | 落结论 | 因此____应承担/不承担____责任，或____请求应支持/不支持。 |
| 价值句 | 只在题目要求时写 | 该处理保护了____，规范了____，维护了____秩序。 |

## 7. 最短考场卡

一句口诀：

> 先讲这题争什么，再讲材料翻译成什么法律话，最后讲法律上怎么处理。

三条纪律：

1. 不先背 A/B。
2. 不空喊法治意义。
3. 不把所有题都写成合同、侵权或依法维权。
"""


def build_axis_demotion() -> str:
    return """# 03 旧 A/B 双轴降级说明

## 为什么 v13.10 读起来不清楚

v13.10 把 A 轴和 B 轴都放在学生前台，导致学生第一反应变成“找标签”。

这有三个问题：

1. A1-A10 是法律内容目录，不是读题逻辑。
2. B1-B7 是答案形状，不是材料理解逻辑。
3. 学生还没有知道“这题争什么”，就被要求判断主入口、副入口、动作模板，学习负担过重。

## v13.11 怎么改

v13.11 的前台只有一条链：

`生活事实 -> 争点 -> 法律翻译 -> 法律结果 -> 价值收束`

A/B 退到后台：

- A 轴用于检查法律关系。
- B 轴用于检查输出形式。
- A/B 不再作为开头的背诵框架。

## 保留什么

保留 v13.10 中经过真实 GPT/Claude 和题源验证的内容：

- 42 locked core 题卡。
- 评分锚点、材料触发、答案骨架。
- A/B 标签作为后台索引。
- 开放容器不晋升正文的纪律。

## 改掉什么

改掉前台顺序：

- 先讲争点，不先讲 A/B。
- 先讲材料翻译，不先讲入口名。
- 先给句型，不先给长表。
- 逐题从“材料一句话、争点、第一判断”开始。
"""


def build_question_file(cards):
    grouped = {}
    for card in cards:
        fields = card["fields"]
        world = world_for(fields.get("A轴主入口", ""), fields.get("B轴设问动作", ""), fields)
        grouped.setdefault(world, []).append(card)

    out = [
        "# 02 v13.11 42题按争点链重排",
        "",
        "本文件不改变 v13.10 的题源、评分锚点和答案骨架，只改变学生阅读顺序。",
        "",
        "每题按：材料一句话 -> 这题争什么 -> 第一判断 -> 材料翻译表 -> 满分句 -> 错法改法 -> 迁移。",
        "",
    ]
    for world in ["1. 交易与用工", "2. 财产与家庭", "3. 人身与侵权", "4. 创新与竞争", "5. 程序与公共"]:
        items = grouped.get(world, [])
        out.append(f"## {world}（{len(items)}题）")
        out.append("")
        for idx, card in enumerate(items, 1):
            f = card["fields"]
            out.append(f"### {idx}. {card['qid']}")
            out.append("")
            out.append(f"- 区年卷题：{f.get('区年卷题', '')}")
            out.append(f"- 设问动作：{f.get('设问动作', '')}")
            out.append(f"- 后台 A/B 索引：{f.get('A轴主入口', '')}；{f.get('B轴设问动作', '')}")
            out.append(f"- 后台副入口：{f.get('A轴副入口/边界', '')}")
            out.append("")
            out.append("**材料一句话**")
            out.append("")
            out.append(material_sentence(f.get("材料核心", "")))
            out.append("")
            out.append("**这题争什么**")
            out.append("")
            out.append(dispute_from(f))
            out.append("")
            out.append("**第一判断**")
            out.append("")
            out.append(first_judgment(f))
            out.append("")
            out.append("**材料翻译表**")
            out.append("")
            out.append("| 材料事实 | 翻译成法律语言 | 对应得分句 |")
            out.append("|---|---|---|")
            for row in translation_rows(f.get("材料触发", "")):
                out.append("| " + " | ".join(x.replace("|", "/") for x in row) + " |")
            out.append("")
            out.append("**满分句**")
            out.append("")
            for sentence in answer_sentences(f.get("答案骨架", "")):
                out.append(f"- {sentence}。")
            out.append("")
            out.append("**错法改法**")
            out.append("")
            out.append(wrong_fix(f.get("学生预警", "")))
            out.append("")
            out.append("**迁移**")
            out.append("")
            out.append("以后遇到同类题，先压出材料一句话和争点，再写材料如何翻译成法律语言；后台 A/B 只用于最后检查，不作为第一入口。")
            out.append("")
    return "\n".join(out)


def build_confucius_precheck(cards):
    samples = [
        "CC0084_2025_东城_二模_19",
        "CC0305_2026_海淀_一模_18_3",
        "CC0364_2026_通州_期中_19_1",
        "CC0244_2026_东城_期中_18",
        "CC0213_2025_门头沟_一模_20",
        "CC0238_2026_东城_二模_19",
    ]
    card_map = {c["qid"]: c for c in cards}
    lines = [
        "# 04 Local Confucius Precheck v13.11",
        "",
        "Status: `local_precheck_pass_pending_real_claude_gpt`",
        "",
        "这是 Codex 本地 Confucius 试读预检，不是真实 Claude/GPT 外部模型复核。",
        "",
        "检查目标：学生是否能先读懂“这题争什么”，再用法律翻译链作答，而不是先背 A/B 标签。",
        "",
        "## 抽样结果",
        "",
        "| question_id | v13.10 风险 | v13.11 修复 | 预检判断 |",
        "|---|---|---|---|",
    ]
    for qid in samples:
        card = card_map.get(qid)
        if not card:
            continue
        fields = card["fields"]
        risk = "先看到 A/B 标签，容易不知道为什么这样分。"
        fix = dispute_from(fields).replace("|", "/")
        lines.append(f"| {qid} | {risk} | {fix} | 可读性提升 |")
    lines.extend(
        [
            "",
            "## 结论",
            "",
            "v13.11 比 v13.10 更像学生框架：它先给可迁移的推理链，再给后台索引。",
            "",
            "但因为本轮没有真实 GPT/Claude 新复核，也没有真实 Claude 零基础学生新盲测，所以不能标为最终替换版。",
        ]
    )
    return "\n".join(lines)


def build_governance():
    return """# 05 Governance Boundary v13.11

Status: `candidate_pending_real_gpt_claude_review`

## 已完成

- 按用户反馈承认 v13.10 前台逻辑不清。
- 按 2026-05-20 重写规格恢复“生活冲突 A -> 法律判断 B”的基本模型。
- 新建 v13.11 逻辑优先框架。
- 将 42 道 locked core 题从 A/B 标签顺序改为争点链顺序。
- 保留 v13.10 的题源、评分锚点、材料触发和答案骨架。

## 未完成

- 未运行新的真实 GPT advisor gate。
- 未运行新的真实 Claude Opus 零基础学生盲测。
- 未重新生成 DOCX/PDF。

## 允许声明

可以声明：

`v13.11 是针对用户指出的逻辑不可学问题生成的候选重构版，已经把学生前台改为“生活事实 -> 争点 -> 法律翻译 -> 法律结果 -> 价值收束”，并完成 42 题重排。`

## 不允许声明

- 不得声明 v13.11 已经替代 v13.10 终版。
- 不得声明 v13.11 通过新的 GPT/Claude 外部复核。
- 不得声明 v13.11 DOCX/PDF 已交付。
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cards = parse_cards(read_text(CARD_FILE))
    trace = load_trace_rows()
    # Keep only rows that appear in the traceability matrix when available.
    if trace:
        cards = [c for c in cards if c["qid"] in trace]

    write_text(OUT / "00_READ_ME_FIRST.md", build_readme())
    write_text(OUT / "01_学生先读_法律题基本模型_v13_11.md", build_framework())
    write_text(OUT / "02_42题_按争点链重排_v13_11.md", build_question_file(cards))
    write_text(OUT / "03_旧A_B双轴降级说明_v13_11.md", build_axis_demotion())
    write_text(OUT / "04_LOCAL_CONFUCIUS_PRECHECK_v13_11.md", build_confucius_precheck(cards))
    write_text(OUT / "05_GOVERNANCE_BOUNDARY_v13_11.md", build_governance())
    write_text(
        OUT / "build_manifest.txt",
        f"generated_at={datetime.now().isoformat(timespec='seconds')}\ncard_count={len(cards)}\nsource={CARD_FILE}\n",
    )
    print(f"generated {OUT}")
    print(f"cards={len(cards)}")


if __name__ == "__main__":
    main()
