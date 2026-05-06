#!/usr/bin/env python3
"""Build Phase12 teaching-text patched review-only artifacts.

This patch does not create a student clean build. It keeps review traceability
while closing the Opus 4.7 Adaptive teaching-text must-fixes:

- 50/50 choice rows carry an explicit 【完整选项】 block.
- subjective rows carry the minimum teaching trio.
- selected hard rows receive clearer exam-room口令.
- review-only NEEDS_* index headings are renamed to Chinese auxiliary labels.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")

SRC_BODY = BASE / "09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md"
OUT_BODY = BASE / "09_student_draft/phase12_expanded_body_TEACHING_PATCHED_REVIEW_ONLY.md"

SRC_REASONING_INDEX = BASE / "09_student_draft/phase12_reasoning_typology_index_REBUILT.md"
OUT_REASONING_INDEX = BASE / "09_student_draft/phase12_reasoning_typology_index_TEACHING_PATCHED_REVIEW_ONLY.md"

SRC_THINKING_INDEX = BASE / "09_student_draft/phase12_thinking_method_index_REBUILT.md"
OUT_THINKING_INDEX = BASE / "09_student_draft/phase12_thinking_method_index_TEACHING_PATCHED_REVIEW_ONLY.md"

CONTROL_MATRIX = BASE / "09_student_draft/phase12_expanded_body_control_matrix.csv"
AUDIT_MD = BASE / "08_review/phase12_opus_teaching_review_resolution.md"
AUDIT_CSV = BASE / "08_review/phase12_teaching_patch_audit.csv"
PATCH_QUEUE = BASE / "08_review/phase12_teaching_patch_queue.csv"


OPTION_BLOCKS: dict[str, str] = {
    "Q-2025海淀二模-12": """【完整选项】
①相对短期资本而言，耐心资本作为新事物具有更强大的生命力。
②耐心资本消除短期收益与长期收益的矛盾，推动发展新质生产力。
③培育耐心资本需要平衡好风险与收益的关系，增强其可持续性。
④壮大耐心资本需要运用超前思维，关注投资项目的长期发展。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2025海淀期末-2": """【完整选项】
①观光巴士复刻百年前的电车外观是对旧事物积极部分的扬弃。
②将北京烤鸭、曲艺表演搬上巴士是通过场景迁移获得的新思路。
③旅游项目设计关注乘客与环境的关系，把握辩证思维的整体性。
④人们可以立足观光巴士成功经验，开发更多沉浸式体验新形式。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2025西城二模-7": """【完整选项】
①甲医生运用了演绎法，推理结构正确能确保这类推理得出正确结论。
②乙医生正确运用了求异法，但其结论不具有必然性。
③与乙、丙相比，甲医生的推理方式在科学领域更有利于得出新结论。
④三名医生结论的可信度由高到低依次应该是甲、乙、丙。
A.①②
B.①③
C.②④
D.③④
""",
    "Q-2024西城一模-11": """【完整选项】
①“问天”是中国空间站的舱段，“梦天”是中国空间站的舱段，“天和”是中国空间站的舱段，所以，“问天”“梦天”“天和”都是中国空间站的舱段。
②“问天”是中国航天人走过的路，“梦天”是中国航天人走过的路，“天和”是中国航天人走过的路，所以，中国航天人走过的路，或是“问天”，或是“梦天”，或是“天和”。
③“问天”是中国航天人走过的路，“梦天”是中国航天人走过的路，“天和”是中国航天人走过的路，所以，“问天”“梦天”“天和”连缀起中华民族求索太空的浩瀚征程。
④“问天”“梦天”“天和”连缀起中华民族求索太空的浩瀚征程，中国空间站的三个舱段是“问天”“梦天”“天和”，所以，中国空间站的三个舱段连缀起中华民族求索太空的浩瀚征程。
A.①②
B.①③
C.②④
D.③④
""",
    "Q-2025东城期末-5": """【完整选项】
①道路改造体现了通过实践建立自在联系。
②要在整体和动态中认识和优化社区环境。
③通过否定过去和肯定现在实现事物发展。
④运用辩证思维的矛盾分析法为居民解忧。
A.①②
B.①③
C.②④
D.③④
""",
    "Q-2025东城期末-13": """【完整选项】
①“祥云”AS700 是大国重器，有的大国重器是载人飞艇，有的载人飞艇是“祥云”AS700。
②歼-20 飞行员手表有三盘六针，这款手表不是歼-20 飞行员手表，这款手表没有三盘六针。
③碳纤维自行车适合山地骑行，山地车适合山地骑行，碳纤维自行车是山地车。
④石墨烯围巾有智能温控系统，智能温控系统能自动调节温度，石墨烯围巾能自动调节温度。
A.①②
B.①③
C.②④
D.③④
""",
    "Q-2026朝阳期中-13": """【完整选项】
①源自于对石榴的实际用途和外在形象的深刻理解。
②属于类比推理，目的在于生动形象地描述民族关系。
③说明思维可以把对石榴的感性具体转化为思维抽象。
④表明联想思维可以对不同事物的认识进行联结与思考。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2026朝阳期中-14": """【完整选项】
①在生活实践中产生，又反作用于生活实践。
②运用了求异法，不能保证结论的真实可靠。
③符合思维一致性的要求，正确揭示了事物的本质和规律。
④并没有考察全部认识对象的情况，结论具有或然性。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2024朝阳二模-6": """【完整选项】
①“商业航天”与“航天”两个概念是属种关系。
②我国商业航天的发展体现了事物发展过程中的渐进性与飞跃性。
③我国商业航天的发展应以航天“国家队”为主，坚持底线思维。
④不论是国有航天，还是民营航天，都是航天事业的重要组成部分。
A.①②
B.①③
C.②④
D.③④
""",
    "Q-2024朝阳一模-7": """【完整选项】
①原始创新中的创新思维，深深地依赖迁移、想象、逆向等逻辑思维活动。
②集成创新中的创新思维，具有跨越性，但不排斥有步骤的逻辑推导与分析。
③开放创新中的合作创新，离不开对前人和他人已有成果的继承与借鉴。
④有效贯通发散思维、聚合思维、超前思维方法，就能确保抢占科技制高点。
A.①③
B.①④
C.②③
D.②④
""",
    "Q-2024朝阳一模-9": """【完整选项】
①需要针对所研究的问题制定具体政策，协调多方利益。
②有益于提高学生引领社会治理、参与政治生活的能力。
③需要坚持系统观念，有序地完成调查研究和思考任务。
④有益于增进学生对于中国特色社会主义制度的特点和优势的理解。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2024朝阳期中-7": """【完整选项】
①“北京中轴线”是由世界遗产委员会确认的世界遗产。
②“北京中轴线”是不可替代的文化遗产。
③有些由世界遗产委员会确认的世界遗产是不可替代的文化遗产。
④有些不可替代的文化遗产是由世界遗产委员会确认的世界遗产。
A.①-③-④
B.②-①-③
C.③-②-④
D.④-②-①
""",
    "Q-2024朝阳期中-8": """【完整选项】
①调查研究是谋事和成事的充分必要条件。
②除非进行了调查研究，否则没有发言权和决策权。
③没有做出正确的决策，是因为没有进行调查研究。
④只有进行了调查研究，才能有正确的贯彻落实。
A.①③
B.①④
C.②③
D.②④
""",
    "Q-2024朝阳期中-11": """【完整选项】
①有些中学生善于刻苦思考，具备从事科学研究的素养。属于关系判断。
②充分掌握时间学、自学学知识，你将在成才路上一骑绝尘。属于假言推理。
③所有成功者都擅长周密计划，他是成功者，他擅长周密计划。属于三段论推理。
④“贵店里有好茶吗？”“我店里全是好茶，从来不卖变质的茶”。违反了矛盾律。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2024朝阳期中-9": """【完整选项】
A. 是演绎推理，揭示了前提和结论之间存在的本质联系。
B. 运用共变法，探究了认识对象与有关现象的因果联系。
C. 运用求异法，合理推断出未知事物必然会出现的情况。
D. 通过假如式想象，实现了思维抽象到思维具体的飞跃。
""",
    "Q-2026丰台一模-4": """【完整选项】
①是古人在建筑营造实践中积淀而成的智慧结晶。
②体现了综合思维，将古建筑的功能性与艺术性融为一体。
③实现了对中国传统风格建筑营造方式的全新重构。
④运用了联想思维，将“最速降线”理论迁移至屋顶建造之中。
A.①②
B.①③
C.②③
D.③④
""",
    "Q-2026丰台一模-7": """【完整选项】
①一种疾病有多种治疗方式，可采用发散与聚合相结合的方法诊治。
②断定不同病症与病因之间的必然联系，应运用充分条件假言推理。
③对病症类型判断不决时，只有运用完全归纳推理才能确保结论无误。
④诊疗决策与多种因素有关，借助超前思维有助于作出正确的诊断。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2026丰台一模-8": """【完整选项】
①不开展全市性志愿服务活动，就必然不使用“北京志愿者”志愿服务标识。
②不使用“北京志愿者”志愿服务标识，就不是开展全市性志愿服务活动。
③有些使用“北京志愿者”志愿服务标识的活动是全市性志愿服务活动。
④使用“北京志愿者”志愿服务标识，就是开展全市性志愿服务活动。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2025丰台期末-10": """【完整选项】
①“吃一堑，长一智”启示我们要从特殊推出一般，寻找规律性。
②人之所以会“在同一地方摔倒多次”，是因为没有运用演绎推理。
③“闻一知十”启示我们要从思维抽象到思维具体，开启创新之门。
④“举一”却不能“反三”的人是因为没有正确运用类比推理。
A.①③
B.①④
C.②③
D.②④
""",
    "Q-2025丰台期末-7": """【完整选项】
A. 集中精力关注当下，就能活出最美的样子。
B. 运用超前思维思考明天，创造出幸福的人生。
C. 从实际出发，从当下做起，生活才能少些迷茫。
D. 弄清昨天、明天和当下各自的意义，是取得成功的关键。
""",
    "Q-2025丰台期末-8": """【完整选项】
①以想象作为思维的基本单元，激发人们对和平的热爱。
②运用发散思维表达了人们对和平的向往和追求。
③主要运用了抽象思维来描述和平的美好。
④以形象思维的方式去触及和平的本质。
A.①③
B.①④
C.②③
D.②④
""",
    "Q-2026通州期末-10": """【完整选项】
①“抵押权”和“质权”都是担保物权下的不同类型，外延上属于反对关系。
②知识产权权利列举属于“定义过宽”的逻辑错误。
③“两公司存在长期货物买卖合作关系”断定的是两个主体之间的关系，属于关系判断。
④“要么放弃继承，要么接受继承”构成相容选言判断。
A.①②
B.①③
C.②④
D.③④
""",
    "Q-2026顺义一模-3": """【完整选项】
①运用矛盾分析法，抓住矛盾主要方面突破关键核心技术的制约。
②在整体性与独立性、动态性与静态性的对立统一中推动探月工程的实施。
③通过分析与综合相结合，以整体把握全链条难题为统领突破各项细分技术。
④遵循质量互变规律，坚持“得中”而处之的思维实现全链条自主可控。
A.①②
B.①④
C.②③
D.③④
""",
    "Q-2026通州期末-5": """【完整选项】
①基层治理事关国家发展和稳定，是我们党执政兴国的重要支柱。
②基层问题的治理必须坚持群众观念，要有系统思维和辩证思维。
③多元共治有助于在当前条件下提供多方共赢的基层治理更优解。
④凝聚服务群众工作机制的核心在于政府主导破解基层治理难题。
A.①③
B.①④
C.②③
D.②④
""",
    "Q-2026通州期末-8": """【完整选项】
①爱国主义的传承依赖于参与者的民族情怀。
②家国情怀是这幅汴绣作品产生的核心源泉。
③通过刺绣建立起承载家国情怀的人为事物的联系。
④个体差异性与民族记忆整体性在作品中对立统一。
A.①②
B.①③
C.②④
D.③④
""",
    "Q-2025顺义一模-6": """【完整选项】
①“这个政策工具能够改善非银机构总体的流动性环境。”该判断的主项是“政策工具”。
②“互换便利不是央行直接向市场给钱，而是通过新工具盘活资产，统筹安排股市、债市等不同市场间的流动性。”这是联言判断，有利于人们多方面分析和把握互换便利的特点。
③“政府宏观调控最常用的政策工具有财政政策、公开市场业务、存款准备金、中央银行贷款等。”该划分没有使用同一个划分标准，犯“划分标准不一”的逻辑错误。
④“通过互换便利操作，证券、基金、保险公司相当于直接从中国人民银行获得了流动性支持。”这是一个关系判断，“获得流动性支持”是反对称关系。
A.①②
B.①③
C.②④
D.③④
""",
    "Q-2025顺义一模-7": """【完整选项】
A. 凡共青团员都是青年，并非所有的青年工人都是共青团员，所以并非所有的青年工人都是青年。不正确，一个形式结构正确的三段论前提中不周延的项在结论中不得周延，该三段论犯了“小项不当扩大”的逻辑错误。
B. 调查报告不是文学作品，这篇文稿不是调查报告，所以这篇文稿不是文学作品。不正确，一个形式结构正确的三段论，两个否定的前提不能必然推出结论，结论为否定当且仅当前提中有一否定。
C. 物质是不灭的，这支钢笔是物质，所以这支钢笔是不灭的。不正确，一个形式结构正确的三段论只能有三个不同的项，该三段论犯了“四概念”的逻辑错误。
D. 有些农民是劳动模范，有些农民是党员，所以有些党员是劳动模范。不正确，一个形式结构正确的三段论中项在前提中至少周延一次，该三段论犯了“中项不周延”的逻辑错误。
""",
}


def load_control() -> dict[str, dict[str, str]]:
    with CONTROL_MATRIX.open(encoding="utf-8") as f:
        return {row["question_id"]: row for row in csv.DictReader(f)}


def split_sections(text: str) -> list[tuple[str, str, str, int, int]]:
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", text, re.M))
    sections: list[tuple[str, str, str, int, int]] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        qid_match = re.search(r"question_id:\s*([^;]+);", block)
        qid = qid_match.group(1).strip() if qid_match else ""
        sections.append((match.group(1).strip(), qid, block, start, end))
    return sections


def insert_option_block(section: str, qid: str) -> tuple[str, bool]:
    if qid not in OPTION_BLOCKS or "【完整选项】" in section:
        return section, False
    comment = re.search(r"<!--.*?-->\s*", section, re.S)
    block = OPTION_BLOCKS[qid].strip()
    if comment:
        pos = comment.end()
        return section[:pos].rstrip() + "\n\n" + block + "\n\n" + section[pos:].lstrip(), True
    heading = re.match(r"^### .+?\n+", section)
    if heading:
        pos = heading.end()
        return section[:pos] + "\n" + block + "\n\n" + section[pos:].lstrip(), True
    return block + "\n\n" + section, True


def patch_haidian_20(section: str) -> str:
    if "答案落点（抄答题卡）" in section:
        return section
    old = "- 答案落点：角度池写法：可优先选“整体性 + 动态性”或“分析与综合 + 质量互变”等组合，核心是两角度写透。考场上优先选择材料最顺的两个角度，每个角度都写成“方法名 + 共享层次 + 推进共同富裕作用”；不要把所有角度堆成必答清单。"
    new = (
        "- 答案落点（抄答题卡）：运用辩证思维推进共同富裕，可以从共享发展的四个层次中选取最贴材料的两个角度写深。可写整体性：把全民共享、全面共享、共建共享、渐进共享作为相互联系的整体来推进，在共建中实现全民共同富裕。也可写动态性或质量互变：共同富裕需要在渐进共享中持续积累条件，由局部改善走向整体提升。\n"
        "- 考场动作（老师叮嘱）：不要把五个辩证角度全堆上去；先看材料哪两层最顺，再写“方法名 + 共享层次 + 推进共同富裕作用”。开放角度池题追求两角度写透，不是三点全必答。"
    )
    return section.replace(old, new)


def patch_chaoyang_20_1(section: str) -> str:
    if "【考场口令】先把题干改写成“如果P，就Q”" not in section:
        marker = "【答案落点】 该推理是充分条件假言推理。"
        insert = (
            "【考场口令】先把题干改写成“如果P，就Q”。看到事实否定了Q，就能推出“不是P”，这叫“否后必否前”；后真不能倒推前，看到Q真不能倒推P真，不能把本题写成肯定后件式。\n\n"
        )
        section = section.replace(marker, insert + marker)
    return section


def patch_shunyi_7(section: str) -> str:
    if "【四步口令】①看结论定大项/小项" not in section:
        marker = "【答案落点】 选 A。"
        insert = (
            "【四步口令】①看结论定大项/小项；②标出该项在前提和结论中是否周延；③前提不周延、结论周延，就判定为该项不当扩大；④谬误名称按项的角色命名。本题“青年”在结论中是大项，所以真实错误是大项不当扩大，A 项只是把它误称成小项不当扩大。\n\n"
        )
        section = section.replace(marker, insert + marker)
    return section


def patch_fengtai_18_2(section: str) -> str:
    if "【题型】甲：必要条件假言推理的肯定后件式" in section:
        return section
    replacements = {
        "- 题型：": "【题型】",
        "- 逻辑形式：": "【逻辑形式】",
        "- 规则口诀：": "【规则口诀】",
        "- 有效式或错误式：": "【有效式或错误式】",
        "- 解题动作：": "【考场动作】",
        "- 答案落点：": "【答案落点】",
        "- 易错陷阱：": "【易错陷阱】",
        "- 同类题索引：": "【同类题索引】",
    }
    for old, new in replacements.items():
        section = section.replace(old, new)
    return section


def generic_subjective_line(module: str, kind: str) -> str:
    if module == "推理":
        lines = {
            "action": "【考场动作】先把题干改写成清楚的逻辑形式，判断属于哪一种推理或判断规则，再写“规则名 + 有效式/错误式 + 本题结论”。",
            "trap": "【易错陷阱】不要只写结论对错；必须说明前提、逻辑形式和有效/无效原因，否则容易把推理规则和材料事实混在一起。",
            "index": "【同类题索引】同类题见推理题型索引中本题对应的题型节点。",
        }
    elif module == "交叉":
        lines = {
            "action": "【考场动作】先分清本题主考思维方法还是推理规则；若两者同时出现，按设问顺序分别写“材料动作/逻辑形式 + 方法或规则 + 结论”。",
            "trap": "【易错陷阱】不要把思维方法题写成纯哲学套话，也不要把形式逻辑题写成材料感想；交叉题必须让方法和材料逐点对应。",
            "index": "【同类题索引】同类题见思维方法索引与推理题型索引中的交叉或辅助挂载节点。",
        }
    else:
        lines = {
            "action": "【考场动作】先圈材料中的动作、关系和变化，再对应到小方法，最后写成“方法名 + 本题材料事实 + 作用结论”的卷面句。",
            "trap": "【易错陷阱】不要只写科学思维、辩证思维或创新思维总帽子；必须落到本题材料触发的小方法和具体作用。",
            "index": "【同类题索引】同类题见思维方法索引中本题对应的正例或辅助节点。",
        }
    return lines[kind]


def ensure_subjective_trio(section: str, module: str) -> str:
    additions: list[str] = []
    if "考场动作" not in section and "答题动作" not in section:
        additions.append(generic_subjective_line(module, "action"))
    if "易错陷阱" not in section:
        additions.append(generic_subjective_line(module, "trap"))
    if "同类题" not in section:
        additions.append(generic_subjective_line(module, "index"))
    if not additions:
        return section
    tail = "\n\n" + "\n\n".join(additions) + "\n"
    if section.rstrip().endswith("---"):
        section = section.rstrip()
        section = section[:-3].rstrip() + tail + "\n---\n"
    else:
        section = section.rstrip() + tail + "\n\n"
    return section


def patch_body() -> tuple[str, list[dict[str, str]]]:
    control = load_control()
    text = SRC_BODY.read_text(encoding="utf-8")
    pieces: list[str] = []
    audits: list[dict[str, str]] = []
    last = 0
    for title, qid, section, start, end in split_sections(text):
        pieces.append(text[last:start])
        row = control.get(qid, {})
        inferred_type = row.get("question_type_group", "")
        inferred_module = row.get("module", "")
        if not inferred_type and "【正确项】" in section:
            inferred_type = "选择题"
        if not inferred_module and ("推理" in section or "三段论" in section or "假言" in section):
            inferred_module = "推理"
        patched: list[str] = []
        section, inserted = insert_option_block(section, qid)
        if inserted:
            patched.append("insert_complete_options")
        if qid == "Q-2025海淀二模-20":
            new_section = patch_haidian_20(section)
            if new_section != section:
                patched.append("split_answer_landing_and_exam_action")
            section = new_section
        if qid == "Q-2024朝阳一模-20-1":
            new_section = patch_chaoyang_20_1(section)
            if new_section != section:
                patched.append("add_denial_of_consequent_exam_formula")
            section = new_section
        if qid == "Q-2025顺义一模-7":
            new_section = patch_shunyi_7(section)
            if new_section != section:
                patched.append("add_syllogism_four_step_formula")
            section = new_section
        if qid == "Q-2026丰台一模-18-2":
            new_section = patch_fengtai_18_2(section)
            if new_section != section:
                patched.append("convert_bullets_to_bracket_blocks")
            section = new_section
        if inferred_type == "主观题":
            before = section
            section = ensure_subjective_trio(section, inferred_module)
            if section != before:
                patched.append("ensure_subjective_minimum_trio")
        audits.append(
            {
                "question_id": qid,
                "question_type": inferred_type,
                "module": inferred_module,
                "patched": ";".join(patched) if patched else "no_change",
                "has_complete_options": "yes" if "【完整选项】" in section else "no",
                "has_subjective_trio": (
                    "yes"
                    if inferred_type != "主观题"
                    or ("易错陷阱" in section and ("考场动作" in section or "答题动作" in section) and "同类题" in section)
                    else "no"
                ),
            }
        )
        pieces.append(section)
        last = end
    pieces.append(text[last:])
    out = "".join(pieces)
    out = out.replace("# Phase12 Expanded Body From 362 Rescan", "# Phase12 Expanded Body Teaching Patched")
    out = out.replace(
        "Status: `REVIEW_ONLY_NO_WORD_NO_FINAL`",
        "Status: `TEACHING_PATCHED_REVIEW_ONLY_NO_WORD_NO_PDF_NO_FINAL`",
        1,
    )
    OUT_BODY.write_text(out, encoding="utf-8")
    return out, audits


def patch_indexes() -> tuple[str, str]:
    reasoning = SRC_REASONING_INDEX.read_text(encoding="utf-8")
    reasoning = reasoning.replace("# Phase12 推理题型索引 REBUILT", "# Phase12 推理题型索引 TEACHING PATCHED")
    reasoning = reasoning.replace(
        "Status: `REBUILT_AFTER_MUST_FIX_CONTENT_REVIEW_ONLY`",
        "Status: `TEACHING_PATCHED_REVIEW_ONLY_NO_WORD_NO_PDF_NO_FINAL`",
    )
    reasoning = reasoning.replace(
        "## NEEDS_TYPE_CONFIRMATION",
        "## 推理题型 · 辅助挂载（本题不作典型推理正例，仅供同类题检索）",
    )
    OUT_REASONING_INDEX.write_text(reasoning, encoding="utf-8")

    thinking = SRC_THINKING_INDEX.read_text(encoding="utf-8")
    thinking = thinking.replace("# Phase12 思维方法索引 REBUILT", "# Phase12 思维方法索引 TEACHING PATCHED")
    thinking = thinking.replace(
        "Status: `REBUILT_AFTER_MUST_FIX_CONTENT_REVIEW_ONLY`",
        "Status: `TEACHING_PATCHED_REVIEW_ONLY_NO_WORD_NO_PDF_NO_FINAL`",
    )
    thinking = thinking.replace(
        "## NEEDS_METHOD_CONFIRMATION",
        "## 思维方法 · 辅助挂载（本题不作典型方法正例，仅供同类题检索）",
    )
    OUT_THINKING_INDEX.write_text(thinking, encoding="utf-8")
    return reasoning, thinking


def write_audits(body: str, audits: list[dict[str, str]], reasoning: str, thinking: str) -> None:
    with AUDIT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "question_id",
                "question_type",
                "module",
                "patched",
                "has_complete_options",
                "has_subjective_trio",
            ],
        )
        writer.writeheader()
        writer.writerows(audits)

    choice_rows = [a for a in audits if a["question_type"] == "选择题"]
    subjective_rows = [a for a in audits if a["question_type"] == "主观题"]
    choice_complete = sum(a["has_complete_options"] == "yes" for a in choice_rows)
    subjective_trio = sum(a["has_subjective_trio"] == "yes" for a in subjective_rows)
    qid_count = body.count("question_id:")
    needs_hits = len(re.findall(r"NEEDS_TYPE_CONFIRMATION|NEEDS_METHOD_CONFIRMATION", reasoning + thinking))
    hard_shunyi = "真实错误是大项不当扩大" in body and "误称成小项不当扩大" in body
    hard_chaoyang = "否后必否前" in body and "后真不能倒推前" in body
    hard_fengtai = "【题型】甲：必要条件假言推理的肯定后件式" in body and "【考场动作】" in body
    hard_haidian = "答案落点（抄答题卡）" in body and "考场动作（老师叮嘱）" in body

    AUDIT_MD.write_text(
        "\n".join(
            [
                "# Phase12 Opus Teaching Review Resolution",
                "",
                "Status: `TEACHING_PATCH_APPLIED_REVIEW_ONLY_NO_WORD_NO_PDF_NO_FINAL`",
                "",
                "## Inputs",
                "",
                "- ClaudeCode visible audit verdict: `VISIBLE_AUDIT_PASS_NO_FINAL`.",
                "- Claude Opus 4.7 Adaptive verdict: `MUST_FIX_TEACHING_TEXT`.",
                "",
                "## Outputs",
                "",
                f"- Body: `{OUT_BODY.relative_to(BASE)}`",
                f"- Reasoning index: `{OUT_REASONING_INDEX.relative_to(BASE)}`",
                f"- Thinking index: `{OUT_THINKING_INDEX.relative_to(BASE)}`",
                f"- Audit CSV: `{AUDIT_CSV.relative_to(BASE)}`",
                "",
                "## Gate Results",
                "",
                f"- body rows with qid anchors: {qid_count} / 77",
                f"- choice rows with explicit `【完整选项】`: {choice_complete} / {len(choice_rows)}",
                f"- subjective rows with teaching trio: {subjective_trio} / {len(subjective_rows)}",
                f"- NEEDS_* terms in patched indexes: {needs_hits}",
                f"- Q-2025顺义一模-7 四步口令 and 大项不当扩大 lock: {'PASS' if hard_shunyi else 'FAIL'}",
                f"- Q-2024朝阳一模-20-1 否定后件式考场口令: {'PASS' if hard_chaoyang else 'FAIL'}",
                f"- Q-2026丰台一模-18-2 bracket block style: {'PASS' if hard_fengtai else 'FAIL'}",
                f"- Q-2025海淀二模-20 answer/action split: {'PASS' if hard_haidian else 'FAIL'}",
                "",
                "## Boundary",
                "",
                "本轮只关闭教学表达补丁，不授权 Word/PDF/final/终稿/最终稿/宝典成品。下一步仍需外审回看、Governor 与 Confucius gates。",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    rows = [
        {
            "queue_order": "1",
            "queue_kind": "external_recheck",
            "target": "phase12_teaching_patched_packet",
            "status": "pending",
            "note": "Send teaching patched body and dual indexes back to ClaudeCode/Opus or GPT if requested.",
        },
        {
            "queue_order": "2",
            "queue_kind": "governor_gate",
            "target": "governor_post_external_boundary_gate",
            "status": "blocked_pending_external_recheck",
            "note": "Do not run Governor as final gate until teaching patch has been externally accepted.",
        },
        {
            "queue_order": "3",
            "queue_kind": "confucius_gate",
            "target": "confucius_learning_gate",
            "status": "blocked_pending_governor",
            "note": "Confucius remains after external and Governor gates.",
        },
        {
            "queue_order": "4",
            "queue_kind": "final_clean_strip",
            "target": "student_clean_candidate",
            "status": "blocked_no_final_authorization",
            "note": "Strip Status, REVIEW_ONLY, HTML qid comments, phase/source anchors only after all gates pass.",
        },
    ]
    with PATCH_QUEUE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["queue_order", "queue_kind", "target", "status", "note"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    body, audits = patch_body()
    reasoning, thinking = patch_indexes()
    write_audits(body, audits, reasoning, thinking)
    print(f"wrote={OUT_BODY}")
    print(f"choice_complete={sum(a['question_type']=='选择题' and a['has_complete_options']=='yes' for a in audits)}")
    print(f"subjective_trio={sum(a['question_type']=='主观题' and a['has_subjective_trio']=='yes' for a in audits)}")


if __name__ == "__main__":
    main()
