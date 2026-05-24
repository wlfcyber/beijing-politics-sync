# -*- coding: utf-8 -*-
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = next((ROOT / "reports").glob("*2026-05-16/06_final_handbook"))
STUDENT = BASE / "选必一_当代国际政治与经济_主观题术语宝典_学生版.md"
NAV = BASE / "选必一_当代国际政治与经济_主观题术语宝典_考前导航版.md"


CORE_RE = re.compile(r"^## 核心答题点：(.+?)（出现(\d+)次）\s*$", re.M)
H2_RE = re.compile(r"^## .*$", re.M)
H1_RE = re.compile(r"^# (.+?)\s*$", re.M)


def backup(path: Path) -> None:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = path.with_name(f"{path.stem}_backup_before_coverage_patch_{stamp}{path.suffix}")
    shutil.copy2(path, dst)


def section_bounds(text: str, heading_start: int, level: str = "## ") -> tuple[int, int]:
    line_end = text.find("\n", heading_start)
    if line_end == -1:
        return len(text), len(text)
    body_start = line_end + 1
    next_match = re.search(rf"^{re.escape(level)}|^# ", text[body_start:], re.M)
    body_end = len(text) if not next_match else body_start + next_match.start()
    return body_start, body_end


def find_core(text: str, core: str) -> re.Match[str]:
    for match in CORE_RE.finditer(text):
        if match.group(1) == core:
            return match
    raise ValueError(f"core not found: {core}")


def add_entry_to_core(text: str, core: str, marker: str, entry: str) -> str:
    match = find_core(text, core)
    body_start, body_end = section_bounds(text, match.start())
    body = text[body_start:body_end]
    if marker in body:
        return text
    insertion = "\n\n" + entry.strip() + "\n"
    return text[:body_end].rstrip() + insertion + text[body_end:]


def renumber_core(text: str, core: str) -> str:
    match = find_core(text, core)
    heading_start = match.start()
    heading_end = text.find("\n", heading_start)
    body_start, body_end = section_bounds(text, heading_start)
    body = text[body_start:body_end]
    index = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal index
        index += 1
        return f"### {index}. {m.group(1)}"

    body = re.sub(r"^###\s+\d+\.\s+(.+?)\s*$", repl, body, flags=re.M)
    heading = f"## 核心答题点：{core}（出现{index}次）"
    return text[:heading_start] + heading + text[heading_end:body_start] + body + text[body_end:]


def update_all_core_counts(text: str) -> str:
    matches = list(CORE_RE.finditer(text))
    pieces: list[str] = []
    cursor = 0
    for match in matches:
        heading_start = match.start()
        heading_end = text.find("\n", heading_start)
        body_start, body_end = section_bounds(text, heading_start)
        body = text[body_start:body_end]
        count = len(re.findall(r"^###\s+", body, flags=re.M))
        pieces.append(text[cursor:heading_start])
        pieces.append(f"## 核心答题点：{match.group(1)}（出现{count}次）")
        cursor = heading_end
    pieces.append(text[cursor:])
    return "".join(pieces)


def main_entry(source: str, when: str, prompt: str, signal: str, intent: str, action: str, sentence: str, group: str) -> str:
    return f"""
### 0. {source}

【什么时候写】{when}

【设问】{prompt}

【为什么能想到】
- 材料信号：{signal}
- 设问意图：{intent}
- 答题动作：{action}

【卷面句】{sentence}

【同题组】{group}
"""


AI_SOURCE = "2026石景山期末 第19题第(2)问（人工智能全球治理）"
AI_PROMPT = "第19题第(2)问：中国关于人工智能全球治理的主张。"
AI_SIGNAL = "评分文本直接给出“和平、发展、合作、共赢的时代潮流”“共同利益”“人类命运共同体理念”“坚持多边主义”“共商共建共享的全球治理观”“更加公正、合理的国际人工智能治理新秩序”“中国方案”等完整术语链。"
AI_INTENT = "这不是一般科技题，而是人工智能全球治理题，要求把中国主张放到全球治理、国际秩序和中国方案中解释。"
AI_GROUP = "和平与发展仍是时代主题（时代背景桶）；国家间共同利益是国家合作的基础（理论桶）；共商共建共享的全球治理观（政治多极化与国际秩序桶）；推动国际秩序和全球治理体系更加公正合理（政治多极化与国际秩序桶）；积极践行真正的多边主义〔可持续发展大国担当角度〕（政治多极化与国际秩序桶）；贡献中国智慧、中国方案、中国力量（中国桶）；中国推动构建人类命运共同体（中国桶）。"


PATCHES = [
    (
        "国家间共同利益是国家合作的基础",
        "2025东城二模 第20题（同球共济精神）",
        main_entry(
            "2025东城二模 第20题（同球共济精神）",
            "设问要求论证“同球共济”精神为何能成立、为何能丰富人类命运共同体内涵，当材料呈现国际局势变乱交织、局部动荡不断时，要先回答各国在和平、安全、发展上存在共同利益。",
            "结合材料，运用《当代国际政治与经济》知识，写一篇关于“同球共济”精神和中国行动的小论文。要求：自拟题目、观点明确、逻辑清晰，200字左右。",
            "当今国际局势变乱交织、局部动荡不断，单靠精神口号不足以解释“同球共济”的国际接受度。",
            "小论文要说明“同球共济”精神和中国行动的关系，必须先解释这一精神为什么有共同基础。",
            "先写各国在发展、安全、文明等问题上存在共同利益，再说明这使“同球共济”精神能够丰富人类命运共同体内涵并被国际社会接受。",
            "当今国际局势变乱交织，各国在发展、安全、文明等问题上存在共同利益，这是“同球共济”精神能够丰富人类命运共同体内涵、被各国接受的客观基础。",
            "推动国际关系民主化（政治多极化与国际秩序桶）；贡献中国智慧、中国方案、中国力量（中国桶）；中国推动构建人类命运共同体（中国桶）。",
        ),
    ),
    (
        "国家间共同利益是国家合作的基础",
        "2025朝阳二模 第21题（周边工作新局面）",
        main_entry(
            "2025朝阳二模 第21题（周边工作新局面）",
            "设问要求说明我国为什么要努力开创周边工作新局面，材料呈现中国与周边国家在发展、安全、互联互通等方面互相需要，必须先点明共同利益是合作基础。",
            "结合材料，运用《当代国际政治与经济》知识，说明我国为什么要努力开创周边工作新局面。",
            "材料写周边国家合作、互联互通、安全发展和区域联动，不是单边施惠，而是共同利益驱动的区域合作。",
            "题目问“为什么要努力开创”，需要解释中国开展周边工作的现实依据，而不是只写中国外交口号。",
            "先写中国与周边国家存在广泛共同利益，再接到和平发展、经济融合、国际关系民主化和人类命运共同体。",
            "共同的国家利益是国际合作的基础，中国与周边国家在发展、安全、互联互通等领域有广泛共同利益，这是我国努力开创周边工作新局面的客观依据。",
            "和平与发展仍是时代主题（时代背景桶）；推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展（经济全球化桶）；推动国际关系民主化（政治多极化与国际秩序桶）；中国推动构建人类命运共同体（中国桶）。",
        ),
    ),
    (
        "国家间共同利益是国家合作的基础",
        "2026西城一模 第20题第(2)问（中国—东盟自贸区3.0版）",
        main_entry(
            "2026西城一模 第20题第(2)问（中国—东盟自贸区3.0版）",
            "设问要求分析中国—东盟自贸区3.0版如何为区域发展和世界经济注入动力，材料中制度型开放、贸易投资便利化和区域规则升级都指向成员共同利益的扩大。",
            "结合材料，运用所学，分析中国—东盟自贸区3.0版是如何为区域发展和世界经济注入强劲动力的。",
            "自贸区3.0版不是单项贸易政策，而是通过制度型开放、规则对接和便利化安排扩大区域共同收益。",
            "题目要把区域合作如何转化为世界经济动力讲清楚，需要先说明共同利益如何把区域成员连接起来。",
            "先写自贸区升级扩大成员共同利益，再写贸易投资便利化、多边贸易体制和全球经济治理改革的外溢作用。",
            "中国—东盟自贸区3.0版通过制度型开放与贸易投资便利化，扩大成员共同利益，把区域合作转化为推动多边贸易体系完善与全球经济治理体系改革的世界动力。",
            "推进贸易和投资自由化便利化（经济全球化桶）；维护以世界贸易组织为核心的多边贸易体制（经济全球化桶）；推动国际关系民主化（政治多极化与国际秩序桶）。",
        ),
    ),
    (
        "和平与发展仍是时代主题",
        AI_SOURCE,
        main_entry(
            AI_SOURCE,
            "题目要求说明中国关于人工智能全球治理的主张，评分文本开头即写“顺应了和平、发展、合作、共赢的时代潮流”，应先把人工智能治理放入时代潮流与共同挑战背景中。",
            AI_PROMPT,
            AI_SIGNAL,
            AI_INTENT,
            "先写人工智能全球治理回应共同挑战、顺应和平发展合作共赢时代潮流，再转入具体治理主张。",
            "中国关于人工智能全球治理的主张顺应和平、发展、合作、共赢的时代潮流，回应人工智能全球治理中的风险和秩序问题，为各国以合作方式应对共同挑战提供方向。",
            AI_GROUP,
        ),
    ),
    (
        "国家间共同利益是国家合作的基础",
        AI_SOURCE,
        main_entry(
            AI_SOURCE,
            "题目要求说明人工智能全球治理主张，评分文本明确写“符合世界各国人民的共同利益”，因此要用共同利益解释为什么各国需要在人工智能治理上合作。",
            AI_PROMPT,
            AI_SIGNAL,
            AI_INTENT,
            "把人工智能风险、安全、发展和公平普惠归结为世界各国人民共同利益，再推出国际合作的必要性。",
            "人工智能全球治理关系各国发展、安全和公平普惠，中国主张符合世界各国人民的共同利益，说明国家间共同利益是开展人工智能治理合作的基础。",
            AI_GROUP,
        ),
    ),
    (
        "共商共建共享的全球治理观",
        AI_SOURCE,
        main_entry(
            AI_SOURCE,
            "题目要求说明中国人工智能全球治理主张，评分文本直接出现“倡导共商共建共享的全球治理观”，说明答案主干应写中国对全球治理方式的主张。",
            AI_PROMPT,
            AI_SIGNAL,
            AI_INTENT,
            "先写人工智能治理不能由少数国家垄断，再落到共商共建共享的全球治理观。",
            "中国倡导共商共建共享的全球治理观，主张各国共同参与人工智能规则制定和风险治理，推动全球人工智能治理更具代表性、包容性和有效性。",
            AI_GROUP,
        ),
    ),
    (
        "推动国际秩序和全球治理体系更加公正合理",
        AI_SOURCE,
        main_entry(
            AI_SOURCE,
            "题目要求说明人工智能全球治理主张，评分文本写“推动构建更加公正、合理的国际人工智能治理新秩序”，应归入国际秩序和全球治理体系公正合理节点。",
            AI_PROMPT,
            AI_SIGNAL,
            AI_INTENT,
            "把人工智能治理中的规则、秩序和公平问题提炼出来，写中国推动治理体系朝公正合理方向调整。",
            "中国主张推动构建更加公正、合理的国际人工智能治理新秩序，使人工智能全球治理摆脱少数国家规则垄断，服务各国共同安全与共同发展。",
            AI_GROUP,
        ),
    ),
    (
        "积极践行真正的多边主义〔可持续发展大国担当角度〕",
        AI_SOURCE,
        main_entry(
            AI_SOURCE,
            "题目要求说明人工智能全球治理主张，评分文本明确写“坚持多边主义”，说明中国不是搞排他小圈子，而是推动各国在多边框架下协商治理。",
            AI_PROMPT,
            AI_SIGNAL,
            AI_INTENT,
            "从“坚持多边主义”切入，说明人工智能治理需要各国平等参与、协商一致，而不是单边规则输出。",
            "中国坚持多边主义，主张各国在平等参与和协商合作中推进人工智能全球治理，反对少数国家垄断规则和技术霸权。",
            AI_GROUP,
        ),
    ),
    (
        "贡献中国智慧、中国方案、中国力量",
        AI_SOURCE,
        main_entry(
            AI_SOURCE,
            "题目要求说明中国关于人工智能全球治理的主张，评分文本结尾写“为全球人工智能治理提供了中国方案”，应落到中国智慧、中国方案、中国力量。",
            AI_PROMPT,
            AI_SIGNAL,
            AI_INTENT,
            "把“向善为民、尊重主权、发展导向、安全可控、公平普惠、开放合作”等目标原则归结为中国方案的具体内容。",
            "中国围绕人工智能治理提出向善为民、尊重主权、发展导向、安全可控、公平普惠、开放合作等目标原则，为全球人工智能治理提供中国方案。",
            AI_GROUP,
        ),
    ),
    (
        "中国推动构建人类命运共同体",
        AI_SOURCE,
        main_entry(
            AI_SOURCE,
            "题目要求说明中国人工智能全球治理主张，评分文本直接写“秉持人类命运共同体理念”，说明人工智能治理要从全人类共同安全、共同发展角度组织答案。",
            AI_PROMPT,
            AI_SIGNAL,
            AI_INTENT,
            "先写人工智能风险和机遇具有全球性，再写中国以人类命运共同体理念推动各国共治共享。",
            "中国秉持人类命运共同体理念，推动人工智能治理兼顾发展、安全、公平和开放合作，使人工智能更好服务全人类共同利益。",
            AI_GROUP,
        ),
    ),
]


BOUNDARIES = [
    (
        "丰台一模Q21 中国式现代化综合小论文中选必一术语细则明确不给分",
        "2025丰台一模Q21",
        "题目是“中国以确定的应对不确定的世界”类综合小论文，细则明确《当代国际政治与经济》中新型国际关系、构建人类命运共同体、推动经济全球化发展等不给分。",
        "2025丰台一模第21题：中国以确定的应对不确定的世界。",
        "评分细则直接列出若干选必一术语“不给分”，这是红线信号。",
        "本题考查中国式现代化等综合论证，不是国际关系或经济全球化主线题。",
        "回到题目要求的主线组织答案，选必一术语只作为排除提醒，不进入主链频次。",
        "本题主线应回到中国式现代化等设问要求，选必一术语如新型国际关系、人类命运共同体、经济全球化发展细则明确不给分，不能用来充主干。",
        "本条为边界提示，不对应主链核心答题点。",
        "新型国际关系、构建人类命运共同体、推动经济全球化发展等在本题细则中明确不给分。",
    ),
    (
        "门头沟一模Q20 劳动合同诚信题中国家关系民主化等术语不给分",
        "2025门头沟一模Q20",
        "题目主线是劳动合同诚信原则，细则明确国家关系民主化、世界多极化、多边主义不给分。",
        "2025门头沟一模第20题：劳动合同诚信原则相关设问。",
        "评分细则把国家关系民主化、世界多极化、多边主义列为不给分项，说明关键词相似不能替代法律主线。",
        "设问落在法律与生活的合同诚信，不要求解释国际关系结构。",
        "先按法律关系、合同履行和诚信原则答题，遇到选必一术语只作排除。",
        "劳动合同诚信题应围绕合同履行、诚信原则和法律责任展开，国家关系民主化、世界多极化、多边主义细则明确不给分。",
        "本条为边界提示，不对应主链核心答题点。",
        "法治诚信题不要硬塞政治多极化和多边主义术语。",
    ),
    (
        "海淀期末Q16 咖啡企业出海中的经济全球化术语只作跨书辅证",
        "2025海淀期末Q16",
        "题目主线是经济与社会中的企业出海和政策支持，细则借用经济全球化、国际国内两种资源两个市场、稳定供应链等术语作辅证。",
        "2025海淀期末第16题：咖啡企业出海相关设问。",
        "细则写政府可通过税收优惠等政策鼓励企业参与经济全球化、利用国际国内两种资源两个市场、打造稳定供应链。",
        "题目主线不是选必一专门题，而是企业经营、政策支持和经济发展机制。",
        "把选必一术语作为跨书支撑，不能反向把整题归入选必一主链。",
        "咖啡企业出海题可用经济全球化、两个市场两种资源和稳定供应链作辅证，但主答案仍应服务企业经营与政策支持机制。",
        "利用两个市场两种资源优化全球资源配置（经济全球化桶）；维护全球产业链供应链稳定畅通（经济全球化桶）。",
        "经济与社会主线借用选必一术语，不能作为选必一主链频次统计。",
    ),
    (
        "房山一模Q20 党与法治综合题中两市两源联动效应只作辅证",
        "2026房山一模Q20",
        "题目主线是党与法治在中国式现代化中的关系，细则出现两个市场两种资源联动效应，只能作为开放发展辅证。",
        "2026房山一模第20题：党与法治在中国式现代化中的关系。",
        "细则主干是中国特色社会主义法治体系、中国共产党地位、矛盾分析等，选必一只出现“两市两源联动效应”这类支撑语。",
        "设问要求综合论证党与法治，不能把经济全球化术语抬成主答案。",
        "主答案按党、法治和中国式现代化展开；若材料需要开放维度，再补两个市场两种资源联动效应。",
        "党与法治综合题中可以少量写两个市场两种资源联动效应作为开放发展辅证，但不能替代《政治与法治》和综合论证主线。",
        "利用两个市场两种资源优化全球资源配置（经济全球化桶）。",
        "本题不进入选必一主链频次；只保留为综合题选必一迁移边界。",
    ),
]


MODULE_HINTS = {
    "时代背景": "先看是否背景支撑。",
    "理论": "先找解释性原理。",
    "经济全球化": "按具体卷面术语定位，不要粗暴合并。",
    "政治多极化与国际秩序": "先判断是否需要国际关系和秩序主答。",
    "中国": "先判断是否是中国行动、中国主张、中国方案。",
    "联合国": "只有材料出现联合国机构、原则或作用时再写。",
    "附：模块边界 / 跨书提示": "边界提醒，不进主链频次。",
}


def boundary_section(title: str, source: str, when: str, prompt: str, signal: str, intent: str, action: str, sentence: str, group: str, warning: str) -> str:
    return f"""
## 边界提示：{title}

### 1. {source}

【什么时候写】{when}

【设问】{prompt}

【为什么能想到】
- 材料信号：{signal}
- 设问意图：{intent}
- 答题动作：{action}

【卷面句】{sentence}

【同题组】{group}

【跨模块提醒】{warning}
"""


def add_boundaries(text: str) -> str:
    appendix = "# 附：模块边界 / 跨书提示"
    if appendix not in text:
        raise ValueError("boundary appendix not found")
    for title, source, when, prompt, signal, intent, action, sentence, group, warning in BOUNDARIES:
        if f"## 边界提示：{title}" in text:
            continue
        text = text.rstrip() + "\n\n" + boundary_section(title, source, when, prompt, signal, intent, action, sentence, group, warning).strip() + "\n"
    return text


def extract_rows(student_text: str) -> list[tuple[str, str, int, str, str, str]]:
    rows: list[tuple[str, str, int, str, str, str]] = []
    current_module: str | None = None
    matches = list(re.finditer(r"^(#|##) (.+?)\s*$", student_text, flags=re.M))
    title_seen = False
    for idx, match in enumerate(matches):
        level, heading = match.group(1), match.group(2)
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(student_text)
        body = student_text[start:end]
        if level == "#":
            if not title_seen:
                title_seen = True
                current_module = None
            else:
                current_module = heading
            continue
        if current_module is None:
            continue
        core_match = re.match(r"核心答题点：(.+?)（出现(\d+)次）", heading)
        if core_match:
            core = core_match.group(1)
            count = int(core_match.group(2))
            first_sentence_match = re.search(r"^【卷面句】(.+?)\s*$", body, flags=re.M)
            first_sentence = first_sentence_match.group(1).strip() if first_sentence_match else ""
            rows.append((current_module, core, count, first_sentence, "同名二级标题", MODULE_HINTS.get(current_module, "按材料信号定位。")))
        elif heading.startswith("边界提示："):
            count = len(re.findall(r"^###\s+", body, flags=re.M))
            first_sentence_match = re.search(r"^【卷面句】(.+?)\s*$", body, flags=re.M)
            first_sentence = first_sentence_match.group(1).strip() if first_sentence_match else ""
            rows.append((current_module, heading, count, first_sentence, "同名二级标题", MODULE_HINTS.get(current_module, "边界提醒，不进主链频次。")))
    return rows


def esc_cell(value: str) -> str:
    return value.replace("|", "／").replace("\n", " ").strip()


def rebuild_nav(student_text: str) -> str:
    rows = extract_rows(student_text)
    grouped: dict[str, list[tuple[str, int, str, str, str]]] = {}
    for module, core, count, sentence, loc, hint in rows:
        grouped.setdefault(module, []).append((core, count, sentence, loc, hint))

    lines = [
        "# 选必一《当代国际政治与经济》主观题术语宝典：考前导航版",
        "",
        "这份导航版只保留框架、核心答题点、出现次数、最常用表述和迁移提醒；完整题例见学生厚版。导航节点与厚版同名，复习时可直接搜索同名“核心答题点”。",
        "",
        "“出现N次”仅表示本宝典收录样本中的命中次数，用于判断复习优先级，不等同于考试预测，也不代表该点在所有设问中都可直接套用。高出现次数不代表优先于材料语义；材料不触发就不写。",
        "",
        "导航版只提示节点，不替代厚版中的来源等级判断；厚版标为参考答案术语、来源等级B/C的内容，只作迁移参考，不按稳定正式细则背诵。",
        "",
    ]

    for module, module_rows in grouped.items():
        lines.append(f"## {module}")
        lines.append("")
        if module in MODULE_HINTS:
            lines.append(f"- {MODULE_HINTS[module]}")
            lines.append("")
        lines.append("| 核心答题点 | 出现 | 表述积累首句 | 厚版定位 | 迁移提醒 |")
        lines.append("|---|---:|---|---|---|")
        for core, count, sentence, loc, hint in module_rows:
            lines.append(f"| {esc_cell(core)} | {count} | {esc_cell(sentence)} | {esc_cell(loc)} | {esc_cell(hint)} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def apply_patch() -> tuple[str, str]:
    text = STUDENT.read_text(encoding="utf-8")
    backup(STUDENT)
    backup(NAV)

    for core, marker, entry in PATCHES:
        text = add_entry_to_core(text, core, marker, entry)

    text = add_boundaries(text)

    target_cores = sorted({core for core, _, _ in PATCHES})
    for core in target_cores:
        text = renumber_core(text, core)
    text = update_all_core_counts(text)

    STUDENT.write_text(text, encoding="utf-8", newline="\n")
    nav_text = rebuild_nav(text)
    NAV.write_text(nav_text, encoding="utf-8", newline="\n")
    return text, nav_text


if __name__ == "__main__":
    student_text, nav_text = apply_patch()
    main_cases = 0
    boundary_cases = 0
    current_appendix = False
    for line in student_text.splitlines():
        if line == "# 附：模块边界 / 跨书提示":
            current_appendix = True
        elif line.startswith("# ") and line != "# 附：模块边界 / 跨书提示":
            current_appendix = False
        elif line.startswith("### "):
            if current_appendix:
                boundary_cases += 1
            else:
                main_cases += 1
    print(f"student_main_cases={main_cases}")
    print(f"student_boundary_cases={boundary_cases}")
    print(f"nav_rows={sum(1 for line in nav_text.splitlines() if line.startswith('| ') and not line.startswith('|---'))}")
