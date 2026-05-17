from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path.cwd()
FINAL_DIR = next(ROOT.rglob("06_final_handbook"))
STUDENT = FINAL_DIR / "选必一_当代国际政治与经济_主观题术语宝典_学生版.md"
NAV = FINAL_DIR / "选必一_当代国际政治与经济_主观题术语宝典_考前导航版.md"
AUDIT = FINAL_DIR / "选必一_宝典终稿_GOVERNOR_FINAL_AUDIT.md"
BUILD_AUDIT = FINAL_DIR / "选必一_主观题术语宝典_学生版_构建审计.md"


BUCKETS = [
    "时代背景",
    "理论",
    "经济全球化",
    "政治多极化",
    "中国",
    "联合国",
    "附：总说句 / 兜底加分表达",
    "附：模块边界 / 跨书提示",
]


@dataclass
class CoreBlock:
    title: str
    text: str


@dataclass
class Bucket:
    name: str
    prefix: str
    blocks: list[CoreBlock]
    suffix: str = ""


def normalize_newlines(s: str) -> str:
    return s.replace("\r\n", "\n").replace("\r", "\n")


def parse_student(text: str) -> tuple[str, dict[str, Bucket]]:
    marker = re.compile(r"(?m)^# (" + "|".join(re.escape(x) for x in BUCKETS) + r")\s*$")
    matches = list(marker.finditer(text))
    if not matches:
        raise RuntimeError("No bucket headings found")
    preface = text[: matches[0].start()]
    buckets: dict[str, Bucket] = {}
    for idx, match in enumerate(matches):
        name = match.group(1)
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end]
        blocks, prefix, suffix = parse_blocks(body)
        buckets[name] = Bucket(name=name, prefix=prefix, blocks=blocks, suffix=suffix)
    return preface, buckets


def parse_blocks(body: str) -> tuple[list[CoreBlock], str, str]:
    pat = re.compile(r"(?m)^## 核心答题点：(.+?)（出现\d+次）\s*$")
    matches = list(pat.finditer(body))
    if not matches:
        return [], body.strip("\n"), ""
    prefix = body[: matches[0].start()].strip("\n")
    blocks: list[CoreBlock] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        blocks.append(CoreBlock(match.group(1), body[start:end].strip("\n")))
    return blocks, prefix, ""


def render_student(preface: str, buckets: dict[str, Bucket]) -> str:
    parts = [preface.rstrip()]
    for name in BUCKETS:
        if name not in buckets:
            continue
        bucket = buckets[name]
        body_parts = [f"# {name}"]
        if bucket.prefix.strip():
            body_parts.append(bucket.prefix.strip())
        body_parts.extend(block.text.strip() for block in bucket.blocks)
        if bucket.suffix.strip():
            body_parts.append(bucket.suffix.strip())
        parts.append("\n\n".join(x for x in body_parts if x.strip()))
    return "\n\n".join(parts).rstrip() + "\n"


def find_block(bucket: Bucket, title: str) -> int:
    for idx, block in enumerate(bucket.blocks):
        if block.title == title:
            return idx
    raise KeyError(f"Core block not found: {bucket.name} / {title}")


def pop_block(bucket: Bucket, title: str) -> CoreBlock:
    return bucket.blocks.pop(find_block(bucket, title))


def insert_after(bucket: Bucket, after_title: str, block: CoreBlock) -> None:
    idx = find_block(bucket, after_title)
    bucket.blocks.insert(idx + 1, block)


def insert_before(bucket: Bucket, before_title: str, block: CoreBlock) -> None:
    idx = find_block(bucket, before_title)
    bucket.blocks.insert(idx, block)


def split_examples(block_text: str) -> tuple[str, list[str]]:
    pat = re.compile(r"(?m)^### \d+\. .*$")
    matches = list(pat.finditer(block_text))
    if not matches:
        return block_text.strip(), []
    prefix = block_text[: matches[0].start()].strip("\n")
    examples = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(block_text)
        examples.append(block_text[start:end].strip("\n"))
    return prefix, examples


def set_title_count(text: str, title: str, count: int) -> str:
    text = re.sub(r"^## 核心答题点：.+?（出现\d+次）", f"## 核心答题点：{title}（出现{count}次）", text, count=1, flags=re.M)
    text = re.sub(r"【本节点真题】共 \d+ 条。", f"【本节点真题】共 {count} 条。", text, count=1)
    return text


def renumber_examples(examples: list[str]) -> list[str]:
    out = []
    for idx, ex in enumerate(examples, 1):
        out.append(re.sub(r"^### \d+\.", f"### {idx}.", ex, count=1, flags=re.M))
    return out


def make_block(title: str, expressions: list[str], examples: list[str], boundary: str | None = None) -> CoreBlock:
    examples = renumber_examples(examples)
    lines = [
        f"## 核心答题点：{title}（出现{len(examples)}次）",
        "",
        "【表述积累】",
    ]
    lines.extend(f"- {x}" for x in expressions)
    lines.extend(["", f"【本节点真题】共 {len(examples)} 条。"])
    if boundary:
        lines.extend(["", f"【本节点边界】{boundary}"])
    lines.append("")
    lines.append("\n\n".join(examples))
    return CoreBlock(title, "\n".join(lines).strip())


def first_expression(block: CoreBlock) -> str:
    m = re.search(r"【表述积累】\n((?:- .+\n?)+)", block.text)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("- "):
            return line[2:]
    return ""


def example_count(block: CoreBlock) -> int:
    return len(re.findall(r"(?m)^### \d+\. ", block.text))


def block_count_from_title(block: CoreBlock) -> int:
    m = re.search(r"（出现(\d+)次）", block.text.splitlines()[0])
    return int(m.group(1)) if m else example_count(block)


def update_preface_counts(preface: str, buckets: dict[str, Bucket]) -> str:
    counts = {name: sum(block_count_from_title(b) for b in bucket.blocks) for name, bucket in buckets.items()}
    for name in ["时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国", "附：总说句 / 兜底加分表达"]:
        if name in counts:
            preface = re.sub(rf"- {re.escape(name)}（\d+条题例）", f"- {name}（{counts[name]}条题例）", preface)
    return preface


def make_navigation(buckets: dict[str, Bucket]) -> str:
    bucket_notes = {
        "时代背景": [
            "本桶只负责解释中国主张、倡议或外交行动为什么有正当性和必要性。",
            "如果材料重点落在开放、市场、贸易、产业链、共享发展成果或全球经济治理，应转入“经济全球化”桶。",
            "如果题目已经要求分析国际关系结构本身，时代背景里的多极化表述只能作前提铺垫，主体落点应转入“政治多极化”桶。",
        ],
        "理论": [
            "本桶只负责解释合作、竞争、国家行动和外交立场背后的原理。",
            "“合作共赢的新型国际关系”归政治多极化；贸易、市场、产业链中的合作共赢归经济全球化；中国担当、共享机遇和发展中国家民生归中国。",
            "“正确义利观”只有在细则明确列入国家利益角度、理论逻辑或合作基础可选表达时才放在本桶。",
        ],
        "经济全球化": [
            "本桶负责开放、市场、贸易、投资、产业链供应链、经济规则和开放合作平台。",
            "同类项合并必须看细则表述是否接近、卷面是否可替代；不能把“开放型世界经济”“开放型经济”“全球经济治理和规则制定”“贸易自由化”仅因本质相关就压成一类。",
            "对发展中国家技术赋能、民生改善和自主发展能力提升，归中国责任担当和发展合作链条。",
        ],
        "政治多极化": [
            "看到国际关系、国际秩序、全球治理方向、多边主义、新型国际关系，优先从本桶组织答案。",
            "“合作共赢的新型国际关系”不放理论桶；裸“合作共赢”必须按语境分流。",
            "全球治理原则、国际秩序公正合理、国际关系民主化和真正多边主义在本桶展开。",
        ],
        "中国": [
            "本桶侧重中国主张、中国方案、中国行动、中国外交和中国贡献。",
            "中国外交政策链包括独立自主和平外交政策、独立自主的基本立场、和平共处五项原则、维护世界和平促进共同发展的宗旨和目标。",
            "技术、产业链、安全发展语境中的独立自主、自力更生、自主可控、发展主动权，属于中国如何行动和提升能力。",
        ],
        "联合国": [
            "本桶只负责联合国地位作用、宪章宗旨原则、以联合国为核心的国际体系、共同议程以及联合国与中国关系。",
            "如果材料重点落在国际秩序改革、国际关系民主化或全球治理方向，应转入“政治多极化”桶。",
        ],
        "附：总说句 / 兜底加分表达": [
            "本附录只用于答案收束、过渡或最后补充，不能替代核心答题点。",
        ],
        "附：模块边界 / 跨书提示": [
            "本附录记录混合设问中的跨书机制，不进入选必一主链背诵优先级。",
        ],
    }
    reminders = {
        "时代背景": "遇到原因、前提、正当性和时代依据，先判断它是不是背景支撑。",
        "理论": "遇到合作为什么成立、竞争为什么激烈、国家为什么这样行动，先找解释性原理。",
        "经济全球化": "遇到贸易、投资、市场、供应链、规则和开放合作，优先从全球化机制写。",
        "政治多极化": "遇到秩序、治理、话语权、多边主义和新型国际关系，优先从政治多极化写。",
        "中国": "遇到中国行动、中国方案、中国责任，先写中国定位、政策和贡献。",
        "联合国": "遇到联合国、宪章、2030议程和多边场域，先写联合国框架。",
        "附：总说句 / 兜底加分表达": "只能作收束或补充，不能代替具体节点。",
    }
    lines = [
        "# 选必一《当代国际政治与经济》主观题术语宝典：考前导航版",
        "",
        "这份导航版只保留框架、核心答题点、出现次数、最常用表述和迁移提醒；完整题例见学生厚版。导航节点与厚版同名，复习时可直接搜索同名“核心答题点”。",
        "",
        "“出现N次”仅表示本宝典收录样本中的命中次数，用于判断复习优先级，不等同于考试预测，也不代表该点在所有设问中都可直接套用。高出现次数不代表优先于材料语义；材料不触发就不写。",
        "",
        "导航版只提示节点，不替代厚版中的来源等级判断；厚版标为参考答案术语、来源等级B/C的内容，只作迁移参考，不按稳定正式细则背诵。",
    ]
    for name in BUCKETS:
        if name not in buckets or name == "附：模块边界 / 跨书提示":
            continue
        lines.extend(["", f"## {name}", ""])
        for note in bucket_notes.get(name, []):
            lines.append(f"- {note}")
        lines.extend(["", "| 核心答题点 | 出现 | 表述积累首句 | 厚版定位 | 迁移提醒 |", "|---|---:|---|---|---|"])
        for block in buckets[name].blocks:
            title = block.title.replace("|", "/")
            count = block_count_from_title(block)
            expr = first_expression(block).replace("|", "/")
            reminder = reminders.get(name, "").replace("|", "/")
            lines.append(f"| {title} | {count} | {expr} | 同名二级标题 | {reminder} |")
    if "附：模块边界 / 跨书提示" in buckets:
        lines.extend(["", "## 附：模块边界 / 跨书提示", ""])
        lines.extend(f"- {note}" for note in bucket_notes["附：模块边界 / 跨书提示"])
        lines.extend(["", "具体边界条目见学生厚版末尾附录。"])
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    text = normalize_newlines(STUDENT.read_text(encoding="utf-8"))
    preface, buckets = parse_student(text)

    econ = buckets["经济全球化"]
    politics = buckets["政治多极化"]
    china = buckets["中国"]
    un = buckets["联合国"]

    # 1. 共同发展、持久和平、共同推进现代化：经济全球化 -> 政治多极化。
    common = pop_block(econ, "促进共同发展、维护持久和平 / 共同推进现代化")
    common.text = common.text.replace("【本节点归类】经济全球化方向", "【本节点归类】共同发展、共同推进现代化与持久和平")
    common.text = common.text.replace(
        "且题目追问贸易、投资、市场、产业链、规则或开放合作的作用，就把材料事实接到“促进共同发展、维护持久和平 / 共同推进现代化”。",
        "且题目追问国际秩序、共同发展、共同推进现代化或持久和平的方向，就把材料事实接到“促进共同发展、维护持久和平 / 共同推进现代化”。",
    )
    insert_after(politics, "推动国际秩序和全球治理体系更加公正合理", common)

    # 2. 必修二边界：移出选必一主链，放附录。
    boundary = pop_block(econ, "优惠政策吸引高新技术企业入驻；降低企业税费成本；助力企业科技创新")
    boundary_text = boundary.text
    boundary_text = re.sub(
        r"^## 核心答题点：.+?（出现1次）",
        "## 边界提示：模块边界（必修二）优惠政策吸引高新技术企业入驻；降低企业税费成本；助力企业科技创新",
        boundary_text,
        count=1,
        flags=re.M,
    )
    boundary_text = boundary_text.replace("【细则术语】", "【模块边界术语】")
    boundary_text = boundary_text.replace(
        "【本节点真题】共 1 条。",
        "【边界说明】本条来自《经济与社会》与选必一混合设问中的必修二机制，只作跨书提示，不计入选必一主链核心答题点。",
    )
    buckets["附：模块边界 / 跨书提示"] = Bucket(
        name="附：模块边界 / 跨书提示",
        prefix="【使用边界】本附录只记录混合设问中的跨书机制。学生答选必一主链时，不把这里的条目当作《当代国际政治与经济》的稳定术语背诵。",
        blocks=[],
        suffix=boundary_text,
    )

    # 3. 裸合作共赢拆掉：供应链产业链语境留经济全球化，发展中国家民生语境转中国。
    pop_block(econ, "合作共赢；实现合作共赢；推动各国合作共赢")
    supply_block = make_block(
        "畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢",
        ["畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢"],
        [
            """### 1. 2024丰台一模Q20，参考答案，未定位正式评分细则

【本节点归类】供应链产业链开放合作

【参考答案术语】畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢

【材料触发点】丰台一模问供应链如何成为国际合作“共赢链”，基础设施联通、供应链金融创新、链博会平台和数字绿色技术都指向全球供应链产业链的开放合作机制。

【设问】结合材料，运用《当代国际政治与经济》知识，说明我国的实践是如何推动供应链成为国际合作“共赢链”的。

【为什么能想到】看到材料围绕供应链产业链、平台联通、金融创新和数字绿色技术展开，且设问追问国际合作如何形成“共赢链”，就把材料事实接到“畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢”。

【答案落点】中国通过基础设施联通、供应链金融创新、链博会平台和数字绿色技术畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢。

【细则位置】2024丰台一模Q20，参考答案“畅通全球供应链产业链，增强经济全球化活力，推动各国合作共赢”，等级化细则，答案提示角度，非固定逐点赋分。

【来源】教师版参考答案来源：2024丰台一模Q20；来源等级C：未定位正式细则，只作迁移参考，不作为稳定采分点"""
        ],
    )
    insert_after(econ, "维护全球产业链供应链稳定畅通", supply_block)

    tech = pop_block(econ, "通过技术交流与资源共享，带动当地经济、社会发展")
    _, tech_examples = split_examples(tech.text)
    tech_ex = tech_examples[0]
    tech_ex = tech_ex.replace("【本节点归类】经济全球化趋势与国际产业分工", "【本节点归类】发展合作与技术赋能")
    tech_ex = tech_ex.replace(
        "且题目追问贸易、投资、市场、产业链、规则或开放合作的作用，就把材料事实接到“通过技术交流与资源共享，带动当地经济、社会发展”。",
        "且题目追问中国企业如何在发展合作中带动当地民生、技术交流和可持续发展，就把材料事实接到“促进技术共享和民生改善；为全球可持续发展贡献力量”。",
    )
    target_idx = find_block(china, "促进技术共享和民生改善；为全球可持续发展贡献力量")
    target = china.blocks[target_idx]
    prefix, examples = split_examples(target.text)
    if "通过技术交流与资源共享，带动当地经济、社会发展" not in prefix:
        prefix = prefix.replace("【表述积累】\n", "【表述积累】\n- 通过技术交流与资源共享，带动当地经济、社会发展\n")
    examples.append(tech_ex)
    new_text = set_title_count(prefix + "\n\n" + "\n\n".join(renumber_examples(examples)), target.title, len(examples))
    china.blocks[target_idx] = CoreBlock(target.title, new_text)

    # 4. 联合国两条从宽节点拆为独立节点。
    un_core = pop_block(un, "维护以联合国为核心的国际体系")
    _, un_examples = split_examples(un_core.text)
    un_status_title = "联合国是当今世界最具普遍性、代表性和权威性的政府间国际组织，并在维护和平、推动发展、促进人类文明进步中发挥重要作用"
    un_china_title = "联合国对中国对外开放和现代化事业作出独特贡献，成为中国开展多边合作的主要舞台"
    un_examples[0] = un_examples[0].replace("就把材料事实接到“维护以联合国为核心的国际体系”。", f"就把材料事实接到“{un_status_title}”。")
    un_examples[1] = un_examples[1].replace("就把材料事实接到“维护以联合国为核心的国际体系”。", f"就把材料事实接到“{un_china_title}”。")
    un_status = make_block(
        un_status_title,
        ["联合国是当今世界最具普遍性、代表性和权威性的政府间国际组织；集体安全机制的核心；实践多边主义的最佳场所；在维护世界和平、推动共同发展、促进人类文明进步中发挥重要作用"],
        [un_examples[0]],
    )
    un_china = make_block(
        un_china_title,
        ["联合国对中国的对外开放和现代化事业作出了独特贡献，成为中国开展多边合作的主要舞台"],
        [un_examples[1]],
    )
    insert_after(un, "维护《联合国宪章》宗旨和原则", un_china)
    insert_after(un, "维护《联合国宪章》宗旨和原则", un_status)

    # 5. 中国桶：周边四定位、四大全球倡议总纲从“人类命运共同体”宽节点拆出。
    hmc_idx = find_block(china, "中国推动构建人类命运共同体")
    hmc = china.blocks[hmc_idx]
    hmc_prefix, hmc_examples = split_examples(hmc.text)
    zhoubian: list[str] = []
    initiatives: list[str] = []
    remain: list[str] = []
    for ex in hmc_examples:
        if "实现发展繁荣的重要基础；维护国家安全的重点；运筹外交全局的首要；推动构建人类命运共同体的关键" in ex:
            zhoubian.append(ex)
        elif "四大全球倡议相互促进、有机统一" in ex or "携手构建人类命运共同体，就是要建设持久和平、普遍安全、共同繁荣、开放包容、清洁美丽的世界" in ex:
            initiatives.append(ex)
        else:
            remain.append(ex)
    hmc_prefix = re.sub(r"- 实现发展繁荣的重要基础；维护国家安全的重点；运筹外交全局的首要；推动构建人类命运共同体的关键\n", "", hmc_prefix)
    hmc_prefix = re.sub(r"- 携手构建人类命运共同体，就是要建设持久和平、普遍安全、共同繁荣、开放包容、清洁美丽的世界\n", "", hmc_prefix)
    hmc_prefix = re.sub(r"- 四大全球倡议相互促进、有机统一，系统推动构建人类命运共同体\n", "", hmc_prefix)
    hmc_text = set_title_count(hmc_prefix + "\n\n" + "\n\n".join(renumber_examples(remain)), hmc.title, len(remain))
    china.blocks[hmc_idx] = CoreBlock(hmc.title, hmc_text)
    if zhoubian:
        ztitle = "周边工作新局面四定位：发展繁荣的重要基础、维护国家安全的重点、运筹外交全局的首要、推动构建人类命运共同体的关键"
        zblock = make_block(
            ztitle,
            ["实现发展繁荣的重要基础；维护国家安全的重点；运筹外交全局的首要；推动构建人类命运共同体的关键"],
            zhoubian,
            "本节点只处理中国周边工作在国家发展、安全和外交全局中的定位；周边经贸合作本身另入经济全球化。",
        )
        insert_before(china, "中国推动构建人类命运共同体", zblock)
    if initiatives:
        ititle = "四大全球倡议相互促进、有机统一，系统推动构建人类命运共同体"
        iblock = make_block(
            ititle,
            [
                "携手构建人类命运共同体，就是要建设持久和平、普遍安全、共同繁荣、开放包容、清洁美丽的世界",
                "四大全球倡议相互促进、有机统一，系统推动构建人类命运共同体",
            ],
            initiatives,
            "本节点是四大全球倡议的总纲，不替代后面发展、安全、文明、治理四个倡议的分点。",
        )
        insert_before(china, "全球发展倡议：以发展促繁荣", iblock)

    # 6. 巴黎协定/NDC 从气候治理宽节点拆出。
    climate_idx = find_block(china, "中国推进绿色低碳转型并参与全球气候治理")
    climate = china.blocks[climate_idx]
    climate_prefix, climate_examples = split_examples(climate.text)
    ndc_examples: list[str] = []
    climate_remain: list[str] = []
    for ex in climate_examples:
        if "严格落实《巴黎协定》要求；每五年提交国家自主贡献目标；维护全球气候治理多边进程" in ex:
            ndc_examples.append(ex)
        else:
            climate_remain.append(ex)
    if ndc_examples:
        climate_prefix = re.sub(r"- 严格落实《巴黎协定》要求；每五年提交国家自主贡献目标；维护全球气候治理多边进程\n", "", climate_prefix)
        climate_text = set_title_count(climate_prefix + "\n\n" + "\n\n".join(renumber_examples(climate_remain)), climate.title, len(climate_remain))
        china.blocks[climate_idx] = CoreBlock(climate.title, climate_text)
        ntitle = "严格落实《巴黎协定》要求，每五年向联合国提交国家自主贡献目标，维护全球气候治理多边进程"
        nblock = make_block(
            ntitle,
            ["严格落实《巴黎协定》要求；每五年提交国家自主贡献目标；维护全球气候治理多边进程"],
            ndc_examples,
            "当设问问中国实践、中国贡献或中国参与全球气候治理时，本节点归中国；不因出现联合国提交机制而归入联合国桶。《巴黎协定》本身长期有效，不存在“到期”问题；2025年节点是新一轮国家自主贡献目标（NDC）更新节点。",
        )
        nblock.text = nblock.text.replace(
            "就把材料事实接到“中国推进绿色低碳转型并参与全球气候治理”。",
            f"就把材料事实接到“{ntitle}”。",
        )
        insert_after(china, "中国推进绿色低碳转型并参与全球气候治理", nblock)

    preface = update_preface_counts(preface, buckets)
    STUDENT.write_text(render_student(preface, buckets), encoding="utf-8", newline="\n")
    NAV.write_text(make_navigation(buckets), encoding="utf-8", newline="\n")

    # Update lightweight audits.
    counts = {name: sum(block_count_from_title(b) for b in bucket.blocks) for name, bucket in buckets.items()}
    core_counts = {name: len(bucket.blocks) for name, bucket in buckets.items()}
    BUILD_AUDIT.write_text(
        "\n".join(
            [
                "# 选必一主观题术语宝典学生版构建审计",
                "",
                "- 输入批次终稿：13",
                "- 输出题例：245（选必一主链244条，附录模块边界1条不计入背诵优先级）",
                f"- 输出核心节点：{sum(core_counts.get(x, 0) for x in BUCKETS if x != '附：模块边界 / 跨书提示')}",
                "- 七字段数量：术语（细则术语/参考答案术语）、材料触发点、设问、为什么能想到、答案落点、细则位置、来源均随每条题例输出",
                f"- 时代背景：{core_counts['时代背景']}个核心节点，{counts['时代背景']}条题例",
                f"- 理论：{core_counts['理论']}个核心节点，{counts['理论']}条题例",
                f"- 经济全球化：{core_counts['经济全球化']}个核心节点，{counts['经济全球化']}条题例",
                f"- 政治多极化：{core_counts['政治多极化']}个核心节点，{counts['政治多极化']}条题例",
                f"- 中国：{core_counts['中国']}个核心节点，{counts['中国']}条题例",
                f"- 联合国：{core_counts['联合国']}个核心节点，{counts['联合国']}条题例",
                f"- 附：总说句 / 兜底加分表达：{core_counts['附：总说句 / 兜底加分表达']}个核心节点，{counts['附：总说句 / 兜底加分表达']}条题例",
                "- 附：模块边界 / 跨书提示：1条边界提示，已从经济全球化主链移出",
                "- 2026-05-17 Opus 4.7 融合补丁：已拆出联合国地位作用、联合国对中国贡献、周边工作四定位、四大全球倡议总纲、巴黎协定/NDC；已迁移共同发展/持久和平、技术赋能民生；已删除裸合作共赢主节点。",
                "",
            ]
        ),
        encoding="utf-8",
        newline="\n",
    )

    audit_append = """

## 2026-05-17 Opus 4.7 全量重跑后的最终融合

- 采用新 Opus 4.7 重跑索引建议，未把 ClaudeCode 厚稿整体覆盖终稿，而是按细则功能择优融合。
- 已补成独立节点：联合国地位和作用、联合国对中国对外开放和现代化事业的独特贡献、周边工作新局面四定位、四大全球倡议相互促进有机统一总纲、巴黎协定/NDC 中国实践节点。
- 已迁移归桶：`促进共同发展、维护持久和平 / 共同推进现代化` 由经济全球化转入政治多极化；`通过技术交流与资源共享，带动当地经济、社会发展` 转入中国发展合作链条。
- 已移出主链：`优惠政策吸引高新技术企业入驻；降低企业税费成本；助力企业科技创新` 改为“模块边界：必修二”附录提示。
- 已删除裸节点：`合作共赢；实现合作共赢；推动各国合作共赢` 不再作为经济全球化默认核心；供应链产业链合作保留在经济全球化，发展中国家民生和技术赋能转入中国。
""".strip()
    audit_text = normalize_newlines(AUDIT.read_text(encoding="utf-8"))
    if "2026-05-17 Opus 4.7 全量重跑后的最终融合" not in audit_text:
        AUDIT.write_text(audit_text.rstrip() + "\n\n" + audit_append + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
