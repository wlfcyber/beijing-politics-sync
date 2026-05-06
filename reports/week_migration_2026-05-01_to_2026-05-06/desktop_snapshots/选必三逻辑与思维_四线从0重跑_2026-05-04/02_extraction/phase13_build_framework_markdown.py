#!/usr/bin/env python3
"""Rebuild Phase12 content into a philosophy-baodian-style framework body.

The Phase12 final was source-order. The user corrected the required structure:
framework node first, then the mock questions under that node. This script
reuses the clean 77-entry body and the manually rebuilt clean indexes to mount
entries under thinking-method and reasoning-typology nodes.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BODY_MD = ROOT / "09_student_draft/phase12_student_clean_candidate.md"
THINKING_INDEX = ROOT / "09_student_draft/phase12_thinking_method_index_STUDENT_CLEAN_CANDIDATE.md"
REASONING_INDEX = ROOT / "09_student_draft/phase12_reasoning_typology_index_STUDENT_CLEAN_CANDIDATE.md"

OUT_MD = ROOT / "09_student_draft/phase13_framework_rebuild/phase13_framework_student_candidate.md"
OUT_MATRIX = ROOT / "08_review/phase13_framework_rebuild/phase13_framework_mount_matrix.csv"
OUT_AUDIT = ROOT / "08_review/phase13_framework_rebuild/phase13_framework_rebuild_audit.md"


@dataclass
class Entry:
    title: str
    source_section: str
    body: str


@dataclass
class Mount:
    title: str
    source_section: str
    framework_part: str
    framework_node: str
    sub_node: str
    tag: str
    included_as: str
    reason: str


def clean_title(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def parse_entries(path: Path) -> dict[str, Entry]:
    entries: dict[str, Entry] = {}
    current_section = ""
    current_title: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_title, current_lines, current_section
        if current_title:
            title = clean_title(current_title)
            entries[title] = Entry(title=title, source_section=current_section, body="\n".join(current_lines).strip())
        current_lines = []

    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("## "):
            if raw.startswith("## 主观题"):
                current_section = "主观题"
            elif raw.startswith("## 选择题"):
                current_section = "选择题"
        if raw.startswith("### "):
            flush()
            current_title = raw[4:].strip()
            current_lines = []
            continue
        if current_title is not None:
            current_lines.append(raw)
    flush()
    return entries


def parse_index(path: Path, part: str, entries: dict[str, Entry]) -> list[Mount]:
    mounts: list[Mount] = []
    current_node = ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            current_node = line[3:].strip()
            continue
        if not line.startswith("- ["):
            continue
        match = re.match(r"^- \[([^\]]+)\]\s+(.+?)(?:：归类提示：(.+))?$", line)
        if not match:
            continue
        tag, title, reason = match.groups()
        title = clean_title(title)
        if title not in entries:
            continue
        source_section = entries[title].source_section
        framework_node, sub_node = split_node(current_node, part)
        mounts.append(
            Mount(
                title=title,
                source_section=source_section,
                framework_part=part,
                framework_node=framework_node,
                sub_node=sub_node,
                tag=tag,
                included_as=include_role(tag),
                reason=reason or "",
            )
        )
    return mounts


def split_node(node: str, part: str) -> tuple[str, str]:
    node = node.strip()
    if "· 相关检索" in node:
        return ("相关检索与边界辅助", "暂不作为正例")
    if part == "思维方法框架":
        if " / " in node and node.startswith(("边界", "易混")):
            return ("边界陷阱与易混选择题", node)
        if "：" in node:
            major, sub = node.split("：", 1)
            return (major.strip(), sub.strip())
        return (node, "总口令与综合题")
    return ("推理题型框架", node)


def include_role(tag: str) -> str:
    if "可正用例" in tag:
        return "模拟题正例"
    if "易混" in tag:
        return "易混选择题"
    if "边界" in tag:
        return "边界提醒"
    return "相关检索"


def normalize_quotes(text: str) -> str:
    text = re.sub(r"(?<![A-Za-z0-9])'([^'\n]{1,80})'(?![A-Za-z0-9])", r"“\1”", text)
    return text


THINKING_ORDER: list[tuple[str, list[str]]] = [
    ("科学思维", ["总口令与综合题", "客观性", "预见性", "可检验性", "探索性与方法更新", "整体安排"]),
    ("辩证思维", ["总口令与综合题", "整体性", "动态性", "分析与综合", "质量互变", "辩证否定"]),
    ("创新思维", ["总口令与综合题", "思路新方法新结果新", "联想思维", "发散思维与聚合思维", "逆向思维", "超前思维", "改变条件/建立新联系"]),
    ("认识发展历程", ["总口令与综合题", "感性具体", "思维抽象", "思维具体"]),
    ("系统观念", ["总口令与综合题"]),
    ("类比推理", ["总口令与综合题"]),
    ("边界陷阱与易混选择题", ["边界提醒 / 选必三干扰项 / 哲学唯物论伪装", "易混选择题 / 数字化治理材料事实与选必三方法区分"]),
    ("相关检索与边界辅助", ["暂不作为正例"]),
]

REASONING_ORDER = [
    "概念外延关系",
    "联言判断与联言推理",
    "相容选言推理",
    "不相容选言推理",
    "充分条件假言推理",
    "必要条件假言推理",
    "三段论结构题",
    "三段论周延规则 / 大项不当扩大 / 谬误名称纠错",
    "归纳推理",
    "类比推理",
    "逻辑三律",
    "演绎推理与前提真实性",
    "推理题型 · 相关检索（本题不作典型推理正例，仅供同类题检索）",
    "暂不作为正例",
]


def flow_lines(node: str, sub: str, part: str) -> list[str]:
    key = f"{node}：{sub}"
    if part == "推理题型框架":
        return reasoning_flow(sub)
    if node == "科学思维":
        if sub == "客观性":
            return [
                "材料怎么看：圈“调查、真实、准确、事实、规律、客观限制、从实际出发”等信号。",
                "该写哪个方法：科学思维的客观性。",
                "为什么触发：材料要求认识如实反映对象，不能凭想象或主观方案替代客观事实。",
                "答案句怎么落：客观性 + 本题事实/规律 + 因而方案或认识才科学。",
                "易错项怎么避：不要写成泛泛创新，也不要把物理规律、生活事实遗漏掉。",
            ]
        if sub == "预见性":
            return [
                "材料怎么看：圈“趋势、未来、潜力、提前布局、市场空间、发展方向”。",
                "该写哪个方法：科学思维的预见性，必要时和超前思维区分。",
                "为什么触发：材料不是空想未来，而是根据现实条件和趋势作合理判断。",
                "答案句怎么落：依据现实情况研判趋势，预见未来可能发展，为行动提供方向。",
                "易错项怎么避：只写“有远见”不够，必须写清预见所依据的现实材料。",
            ]
        if sub == "可检验性":
            return [
                "材料怎么看：圈“测试、验证、试点、迭代、打磨、实践效果”。",
                "该写哪个方法：科学思维的可检验性。",
                "为什么触发：材料把认识放回实践中检验和修正，而不是停留在设想。",
                "答案句怎么落：通过测试/实践检验方案效果，并在反馈中优化认识。",
                "易错项怎么避：不要把“验证”写成简单证明，要写出实践检验和迭代。",
            ]
        if sub == "探索性与方法更新":
            return [
                "材料怎么看：圈“范围拓宽、对象扩展、方式更新、分类细化、方法新变化”。",
                "该写哪个方法：本题来源支持的科学调查探索性与方法更新。",
                "为什么触发：材料在科学调查主线下更新思路和方法，服务更准确的认识。",
                "答案句怎么落：通过调查思路和方法更新，提高对对象的科学把握。",
                "易错项怎么避：这是特定题源支持点，不要泛化成所有科学思维题必写。",
            ]
        if sub == "整体安排":
            return [
                "材料怎么看：圈“准备、实施、开发应用、分阶段、任务明确、整体推进”。",
                "该写哪个方法：本题来源支持的科学调查整体安排。",
                "为什么触发：复杂调查任务需要把阶段、对象和结果应用作为整体统筹。",
                "答案句怎么落：分阶段组织调查并整体安排任务，为科学决策提供支撑。",
                "易错项怎么避：不要脱离科学调查主线空写辩证思维整体性。",
            ]
        return [
            "材料怎么看：先看材料是否在处理事实、规律、趋势、验证和科学调查。",
            "该写哪个方法：先判科学思维总帽子，再下沉到客观性、预见性、可检验性等小方法。",
            "为什么触发：科学思维强调真实反映对象、合理预见和实践检验。",
            "答案句怎么落：方法名 + 材料事实 + 对形成科学认识或解决问题的作用。",
            "易错项怎么避：不要只写“体现科学思维”，必须把三性或来源支持点落细。",
        ]
    if node == "辩证思维":
        if sub == "整体性":
            return [
                "材料怎么看：圈“多主体、多层次、多环节、系统、一盘棋、整体推进”。",
                "该写哪个方法：辩证思维的整体性。",
                "为什么触发：材料要求把各部分放进整体关系中看，不能只抓单点。",
                "答案句怎么落：把若干要素作为相互联系的整体统筹，推动整体功能优化。",
                "易错项怎么避：只写“整体”两个字不够，要写出部分之间的联系和整体作用。",
            ]
        if sub == "动态性":
            return [
                "材料怎么看：圈“阶段、过程、变化、当前与长远、逐步推进、发展趋势”。",
                "该写哪个方法：辩证思维的动态性。",
                "为什么触发：材料要求在变化过程和发展阶段中把握对象。",
                "答案句怎么落：在发展变化中把握条件和任务，随阶段推进调整行动。",
                "易错项怎么避：不要把动态性写成单纯时间顺序，要写“变化中的关系”。",
            ]
        if sub == "分析与综合":
            return [
                "材料怎么看：圈“拆成几个层次/方面/条件，再合起来推进”。",
                "该写哪个方法：分析与综合。",
                "为什么触发：材料既要分解要素，又要把要素综合成解决方案。",
                "答案句怎么落：先分析各层次/条件，再综合统筹，形成整体推进路径。",
                "易错项怎么避：不要只拆不合，也不要把所有分点堆成清单。",
            ]
        if sub == "质量互变":
            return [
                "材料怎么看：圈“渐进、积累、由量变到提升、从局部到整体”。",
                "该写哪个方法：质量互变。",
                "为什么触发：材料强调条件持续积累，推动事物状态跃升。",
                "答案句怎么落：通过渐进积累条件，推动发展由局部改善走向整体提升。",
                "易错项怎么避：不要把任何“变化”都写成质量互变，必须有积累和转化。",
            ]
        if sub == "辩证否定":
            return [
                "材料怎么看：圈“继承、改造、扬弃、升级、不是全盘否定”。",
                "该写哪个方法：辩证否定。",
                "为什么触发：材料对旧事物既保留合理因素，又改造其旧形式。",
                "答案句怎么落：在继承中改造、在保留中创新，推动事物发展。",
                "易错项怎么避：不要写成否定一切，也不要把普通更新硬套成辩证否定。",
            ]
        return [
            "材料怎么看：先看有没有整体关系、动态过程、矛盾条件、层次拆合。",
            "该写哪个方法：辩证思维总帽子下，精确落到整体性、动态性、分析综合等。",
            "为什么触发：辩证思维要求在联系、发展和矛盾中把握对象。",
            "答案句怎么落：小方法 + 材料关系/过程 + 对解决问题或推进发展的作用。",
            "易错项怎么避：不要把辩证法大词搬上去，必须下沉到小方法。",
        ]
    if node == "创新思维":
        if sub == "思路新方法新结果新":
            return [
                "材料怎么看：圈“新思路、新方法、新方案、新结果、设计创新、技术适配”。",
                "该写哪个方法：创新思维的三新。",
                "为什么触发：材料不是普通改变，而是在思路、方法或成果上形成新方案。",
                "答案句怎么落：从思路新/方法新/结果新中选材料最顺的点，写出创新作用。",
                "易错项怎么避：不要只喊“有创新”，要拆清楚新在哪里。",
            ]
        if sub == "联想思维":
            return [
                "材料怎么看：圈“把A意象/经验/形象迁移到B对象，跨域联结”。",
                "该写哪个方法：联想思维，常见为迁移和想象。",
                "为什么触发：材料把已有经验迁移到新对象，形成新的理解或设计。",
                "答案句怎么落：把某一文化/经验/形象迁移到新场景，形成新方案。",
                "易错项怎么避：不要把所有比喻都写成类比推理；要看是否服务创新设计。",
            ]
        if sub == "发散思维与聚合思维":
            return [
                "材料怎么看：圈“多方案、多需求、多场景展开，再围绕目标收束”。",
                "该写哪个方法：先发散后聚合。",
                "为什么触发：材料先打开多种可能，再集中到可实施方案。",
                "答案句怎么落：围绕任务多角度发散设想，再聚焦资源形成方案。",
                "易错项怎么避：只写发散会散，只写聚合会窄；二者要配材料动作。",
            ]
        if sub == "逆向思维":
            return [
                "材料怎么看：圈“反过来、由人找书到书找人、冷资源变热经济”等方向反转。",
                "该写哪个方法：逆向思维。",
                "为什么触发：材料把原有顺序、关系或价值方向倒过来重新思考。",
                "答案句怎么落：对既有顺序/关系作反向思考，形成新的服务或发展路径。",
                "易错项怎么避：不要把普通改进写成逆向，必须有方向或关系的反转。",
            ]
        if sub == "超前思维":
            return [
                "材料怎么看：圈“预测趋势、提前布局、面向未来需求、制度预置”。",
                "该写哪个方法：超前思维。",
                "为什么触发：材料根据现有条件预判未来，并提前谋划行动。",
                "答案句怎么落：立足现实趋势作前瞻判断，提前布局条件和方案。",
                "易错项怎么避：不要看到“明天/未来”就选超前，要有现实依据和预判链。",
            ]
        if sub == "改变条件/建立新联系":
            return [
                "材料怎么看：圈“创造条件、调整结构、建立新联系、化解二选一矛盾”。",
                "该写哪个方法：创新思维中改变条件、建立新的具体联系。",
                "为什么触发：材料不是在原条件里硬选，而是改造条件让问题有新解。",
                "答案句怎么落：通过改变条件/建立新联系，使冲突双方获得新的解决路径。",
                "易错项怎么避：不要只劝说或表态，要写出被创造出来的新条件。",
            ]
        return [
            "材料怎么看：先看材料是否出现跨界联结、反向思考、方案展开收束、未来预判。",
            "该写哪个方法：创新思维必须下沉到三新、联想、发散聚合、逆向、超前等。",
            "为什么触发：创新思维要突破常规，形成新思路、新方法或新结果。",
            "答案句怎么落：具体方法 + 材料中的创新动作 + 新方案的作用。",
            "易错项怎么避：不要泛写“创新”，必须说清楚创新动作。",
        ]
    if node == "认识发展历程":
        return [
            "材料怎么看：圈“先接触杂多现象，再抽出本质，再回到完整图景”。",
            "该写哪个方法：感性具体 -> 思维抽象 -> 思维具体。",
            "为什么触发：材料呈现的是认识深化过程，不是简单拆分或系统整合。",
            "答案句怎么落：从感性材料出发，经抽象把握本质，再形成具体完整认识。",
            "易错项怎么避：不要误写成分析与综合、系统整合或联想类比。",
        ]
    if node == "系统观念":
        return [
            "材料怎么看：圈“整体布局、要素协同、机制联动、系统集成”。",
            "该写哪个方法：系统观念。",
            "为什么触发：材料要求把多环节和多主体放在系统中协同推进。",
            "答案句怎么落：统筹各环节和主体，推动系统功能优化。",
            "易错项怎么避：不要把任何“多个要素”都写成系统观念，必须有协同机制。",
        ]
    return [
        "材料怎么看：先判断这是正例、易混选择题还是边界提醒。",
        "该写哪个方法：只把正例迁移到主观题；边界题只用于避坑。",
        "为什么触发：看题干、选项和设问是否真的要求该方法。",
        "答案句怎么落：正例写方法与材料对应；陷阱题写清为什么不能这样套。",
        "易错项怎么避：不要把相关检索和边界提醒当成万能模板。",
    ]


def reasoning_flow(sub: str) -> list[str]:
    if "充分条件" in sub:
        return [
            "题型怎么看：把句子写成“如果P，那么Q”。",
            "规则口令：肯前肯后、否后否前有效；肯后肯前、否前否后无效。",
            "解题动作：先标P和Q，再看题目给的是前件、后件、肯定还是否定。",
            "答案句怎么落：说明用了哪一个有效式，或指出错在肯后/否前。",
            "易错项怎么避：看到后件为真不能倒推前件为真。",
        ]
    if "必要条件" in sub:
        return [
            "题型怎么看：把句子写成“只有P，才Q”，即没有P就没有Q。",
            "规则口令：否前否后、肯后肯前有效；肯前肯后、否后否前无效。",
            "解题动作：先找必要条件P和结果Q，再判断题目用的是哪个式子。",
            "答案句怎么落：说明必要条件是否被满足，能否推出结论。",
            "易错项怎么避：肯定必要条件不等于结果一定发生。",
        ]
    if "三段论" in sub:
        return [
            "题型怎么看：找大项、小项、中项，看中项是否搭桥成功。",
            "规则口令：中项至少周延一次；前提不周延的项结论中不得周延。",
            "解题动作：标出结论主谓项，再回看前提里这些项是否被扩大。",
            "答案句怎么落：指出结构是否有效，错在中项不周延/大项扩大/小项扩大/四概念。",
            "易错项怎么避：不要只看结论像不像真，三段论先看结构。",
        ]
    if "联言" in sub:
        return [
            "题型怎么看：看到“并且、同时、兼具、既……又……”先判联言。",
            "规则口令：联言支全真才真，一假即假；真联言可拆出各支真。",
            "解题动作：逐一检查每个联言支的真假。",
            "答案句怎么落：说明某一支假导致整体假，或由整体真推出支判断真。",
            "易错项怎么避：不能只抓其中一支就判断整个联言为真。",
        ]
    if "选言" in sub:
        return [
            "题型怎么看：看到“或者/要么”先判相容还是不相容。",
            "规则口令：相容选言否定一支可肯定另一支，肯定一支不能否定另一支；不相容选言肯定一支可否定另一支。",
            "解题动作：先判是否可以同真，再决定能否排除另一支。",
            "答案句怎么落：说明选言支之间是否互斥，推出哪一支成立或不成立。",
            "易错项怎么避：不要把所有“或者”都当成不相容。",
        ]
    if "归纳" in sub:
        return [
            "题型怎么看：从个别事实推出一般结论，先判完全归纳还是不完全归纳。",
            "规则口令：完全归纳较稳；不完全归纳具有或然性。",
            "解题动作：看样本是否覆盖全部对象，是否存在代表性问题。",
            "答案句怎么落：说明结论的可靠程度及样本依据。",
            "易错项怎么避：不要把不完全归纳说成必然正确。",
        ]
    if "类比" in sub:
        return [
            "题型怎么看：由一个对象的相似属性迁移到另一个对象。",
            "规则口令：相似点越本质、越多，类比越可靠；差异越关键，类比越弱。",
            "解题动作：找相似属性和迁移边界。",
            "答案句怎么落：说明类比根据及其可靠程度。",
            "易错项怎么避：不要把形象联想、比喻表达都当成严格类比推理。",
        ]
    if "概念" in sub:
        return [
            "题型怎么看：看概念范围、定义结构、属种/交叉/全同/不相容关系。",
            "规则口令：定义=被定义项+联结词+种差+邻近属；外延关系看范围。",
            "解题动作：先画范围，再判断是否越级、倒置或混同。",
            "答案句怎么落：写清两个概念的外延关系或定义构成。",
            "易错项怎么避：不要把整体部分、个体集合误判成属种。",
        ]
    if "逻辑三律" in sub:
        return [
            "题型怎么看：看是否同一话题被偷换、两个判断互相矛盾、二者不能同假。",
            "规则口令：同一律不偷换，矛盾律不同时真，排中律不同时假。",
            "解题动作：固定讨论对象和判断范围，再看真假关系。",
            "答案句怎么落：指出违反哪一律以及错在哪里。",
            "易错项怎么避：不要把所有冲突都叫矛盾律，先看真假关系。",
        ]
    return [
        "题型怎么看：先把材料语言翻译成逻辑形式或规则类型。",
        "规则口令：写出该题型的有效式、错误式或保真条件。",
        "解题动作：标概念、前件后件、选言支、联言支或三段论三项。",
        "答案句怎么落：规则名 + 本题结构 + 有效/无效结论。",
        "易错项怎么避：不要凭语感选答案，先形式化。",
    ]


def entry_block(entry: Entry, mount: Mount) -> str:
    heading = f"##### {entry.title}（{entry.source_section}｜{mount.included_as}）"
    note = f"【本节点归类】{mount.reason}" if mount.reason else ""
    body = entry.body.strip()
    if note:
        body = f"{note}\n\n{body}"
    return f"{heading}\n\n{body}".rstrip()


def main() -> None:
    entries = parse_entries(BODY_MD)
    thinking_mounts = parse_index(THINKING_INDEX, "思维方法框架", entries)
    reasoning_mounts = parse_index(REASONING_INDEX, "推理题型框架", entries)
    all_mounts = thinking_mounts + reasoning_mounts

    seen = set()
    deduped: list[Mount] = []
    for m in all_mounts:
        key = (m.title, m.framework_part, m.framework_node, m.sub_node, m.tag)
        if key not in seen:
            seen.add(key)
            deduped.append(m)
    all_mounts = deduped

    mounted_titles = {m.title for m in all_mounts}
    unmounted = [t for t in entries if t not in mounted_titles]
    for title in unmounted:
        e = entries[title]
        all_mounts.append(
            Mount(
                title=title,
                source_section=e.source_section,
                framework_part="兜底补挂",
                framework_node="暂未稳定归入框架的题",
                sub_node="只供复查",
                tag="相关检索",
                included_as="相关检索",
                reason="原 clean body 有条目，但双索引未挂载；保留供 Codex 复查。",
            )
        )

    by_thinking: dict[tuple[str, str], list[Mount]] = {}
    by_reasoning: dict[str, list[Mount]] = {}
    fallback: list[Mount] = []
    for m in all_mounts:
        if m.framework_part == "思维方法框架":
            by_thinking.setdefault((m.framework_node, m.sub_node), []).append(m)
        elif m.framework_part == "推理题型框架":
            by_reasoning.setdefault(m.sub_node, []).append(m)
        else:
            fallback.append(m)

    lines: list[str] = [
        "# 2026北京高考政治选必三《逻辑与思维》宝典：框架触发版",
        "",
        "**飞哥正志讲堂**",
        "",
        "## 使用方法",
        "",
        "这版按哲学宝典的方式使用：先找框架节点，再看该节点下面的模拟题。不要先按区、年份、题号背题；要训练自己看到材料动作后，能把它挂到“思维类型—思维特点/方法—卷面句”的链条上。",
        "",
        "每个节点都按同一个动作走：材料怎么看、该写哪个方法或规则、为什么触发、答案句怎么落、易错项怎么避。节点下面的题就是这个框架的模拟题库。",
        "",
        "## 第一部分：思维方法框架",
        "",
    ]

    for node, subnodes in THINKING_ORDER:
        present = [(node, sub) for sub in subnodes if by_thinking.get((node, sub))]
        if not present:
            continue
        lines.append(f"### {node}")
        lines.append("")
        for _, sub in present:
            mounts = by_thinking[(node, sub)]
            lines.append(f"#### {sub}")
            lines.append("")
            lines.append("【固定分析流程】")
            lines.extend([f"- {x}" for x in flow_lines(node, sub, "思维方法框架")])
            lines.append("")
            lines.append(f"【本节点模拟题】共 {len(mounts)} 条。")
            lines.append("")
            for m in mounts:
                lines.append(entry_block(entries[m.title], m))
                lines.append("")
                lines.append("---")
                lines.append("")

    lines.append("## 第二部分：推理题型框架")
    lines.append("")
    for sub in REASONING_ORDER:
        mounts = by_reasoning.get(sub, [])
        if not mounts:
            continue
        lines.append(f"### {sub}")
        lines.append("")
        lines.append("【固定分析流程】")
        lines.extend([f"- {x}" for x in flow_lines("推理题型框架", sub, "推理题型框架")])
        lines.append("")
        lines.append(f"【本题型模拟题】共 {len(mounts)} 条。")
        lines.append("")
        for m in mounts:
            lines.append(entry_block(entries[m.title], m))
            lines.append("")
            lines.append("---")
            lines.append("")

    if fallback:
        lines.append("## 第三部分：待复查补挂题")
        lines.append("")
        lines.append("这些题来自 77 条 clean body，但没有稳定进入双索引。保留在这里供下一轮人工归类，不当作正向模板。")
        lines.append("")
        for m in fallback:
            lines.append(entry_block(entries[m.title], m))
            lines.append("")
            lines.append("---")
            lines.append("")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MATRIX.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(normalize_quotes("\n".join(lines).rstrip() + "\n"), encoding="utf-8")

    with OUT_MATRIX.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "title",
                "source_section",
                "framework_part",
                "framework_node",
                "sub_node",
                "tag",
                "included_as",
                "reason",
            ],
        )
        writer.writeheader()
        for m in all_mounts:
            writer.writerow(m.__dict__)

    unique_mounted = {m.title for m in all_mounts}
    core_checks = {
        "科学思维：客观性": len(by_thinking.get(("科学思维", "客观性"), [])),
        "科学思维：预见性": len(by_thinking.get(("科学思维", "预见性"), [])),
        "科学思维：可检验性": len(by_thinking.get(("科学思维", "可检验性"), [])),
        "创新思维：思路新方法新结果新": len(by_thinking.get(("创新思维", "思路新方法新结果新"), [])),
        "创新思维：联想思维": len(by_thinking.get(("创新思维", "联想思维"), [])),
        "创新思维：发散思维与聚合思维": len(by_thinking.get(("创新思维", "发散思维与聚合思维"), [])),
        "创新思维：逆向思维": len(by_thinking.get(("创新思维", "逆向思维"), [])),
        "创新思维：超前思维": len(by_thinking.get(("创新思维", "超前思维"), [])),
        "辩证思维：整体性": len(by_thinking.get(("辩证思维", "整体性"), [])),
        "辩证思维：动态性": len(by_thinking.get(("辩证思维", "动态性"), [])),
        "辩证思维：分析与综合": len(by_thinking.get(("辩证思维", "分析与综合"), [])),
        "认识发展历程：感性具体": len(by_thinking.get(("认识发展历程", "感性具体"), [])),
        "认识发展历程：思维抽象": len(by_thinking.get(("认识发展历程", "思维抽象"), [])),
        "认识发展历程：思维具体": len(by_thinking.get(("认识发展历程", "思维具体"), [])),
        "充分条件假言推理": len(by_reasoning.get("充分条件假言推理", [])),
        "必要条件假言推理": len(by_reasoning.get("必要条件假言推理", [])),
        "三段论结构题": len(by_reasoning.get("三段论结构题", [])),
    }
    audit_lines = [
        "# Phase13 Framework Rebuild Audit",
        "",
        "- status: `FRAMEWORK_REBUILD_CANDIDATE_BUILT_REVIEW_REQUIRED`",
        f"- clean_body_entries: `{len(entries)}`",
        f"- unique_mounted_titles: `{len(unique_mounted)}`",
        f"- mount_rows: `{len(all_mounts)}`",
        f"- unmounted_from_indexes_then_fallback: `{len(unmounted)}`",
        f"- output_markdown: `{OUT_MD}`",
        f"- mount_matrix: `{OUT_MATRIX}`",
        "",
        "## Core Node Counts",
        "",
    ]
    for k, v in core_checks.items():
        audit_lines.append(f"- {k}: `{v}`")
    audit_lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a framework-structured candidate. It fixes the user's structural objection but still requires ClaudeCode comparison, Codex review, GPT/Claude review if requested, and Word/PDF rebuild before replacing final outputs.",
        ]
    )
    OUT_AUDIT.write_text("\n".join(audit_lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
