# -*- coding: utf-8 -*-
"""Build all batch04a outputs for S-2025顺义一模 closure."""
from __future__ import annotations

import csv
import json
from pathlib import Path

BATCH_DIR = Path(__file__).resolve().parent
SUITE_ID = "S-2025顺义一模"
SOURCE_BATCH = "batch04a_shunyi_yimo_2025"

# ---------------------------------------------------------------------------
# Per-question decisions. All 23 unique question_ids must appear.
# decision in {入正文, 同类索引, blocked, excluded}
# needs_codex_recheck in {yes, no}
# ---------------------------------------------------------------------------

QUESTIONS = [
    # ---- 选择题 1-15 ----
    {
        "qid": "Q-2025顺义一模-1",
        "qno": "1",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为加强党的建设、健全全面从严治党体系，归属必修三政治与法治；选必三《逻辑与思维》无设问角度。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-2",
        "qno": "2",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为共建社区微花园治理理念，归属必修二经济与社会、必修三基层治理；与选必三思维方法及推理形式无对应。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-3",
        "qno": "3",
        "qtype": "选择题",
        "decision": "同类索引",
        "decision_reason": "题干主体为冰雪文化交流（必修四矛盾普遍性、共性与个性），但 D 选项把跨文化合作误读成逆向思维，可作为创新思维-逆向思维章节的边界陷阱索引。",
        "evidence_level": "B-choice-signal",
        "framework_node": "创新思维 / 逆向思维 / 边界陷阱",
        "needs_codex_recheck": "yes",
    },
    {
        "qid": "Q-2025顺义一模-4",
        "qno": "4",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为时间利用调查公报，考查必修四实践与认识、价值判断与价值选择；非选必三思维或推理。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-5",
        "qno": "5",
        "qtype": "选择题",
        "decision": "入正文",
        "decision_reason": "考查联言命题“A 且 B”的矛盾命题为“非 A 或非 B”，属选必三《逻辑与思维》推理部分形式逻辑章节，有可靠客观答案 B。",
        "evidence_level": "B-choice-signal",
        "framework_node": "推理部分 / 简单判断 / 联言判断与其矛盾命题",
        "needs_codex_recheck": "yes",
    },
    {
        "qid": "Q-2025顺义一模-6",
        "qno": "6",
        "qtype": "选择题",
        "decision": "入正文",
        "decision_reason": "四选项依次考查主项识别、联言判断、划分（越级划分错误）、关系判断（反对称关系），属选必三推理部分概念与判断章节，客观答案 A。",
        "evidence_level": "B-choice-signal",
        "framework_node": "推理部分 / 概念与判断 / 主项·联言·划分·关系判断",
        "needs_codex_recheck": "yes",
    },
    {
        "qid": "Q-2025顺义一模-7",
        "qno": "7",
        "qtype": "选择题",
        "decision": "入正文",
        "decision_reason": "三段论周延规则四选项辨析（大项不当扩大、两否定前提、四概念、中项不周延），A 项把大项不当扩大“误称”为小项不当扩大，是顺义一模 7 谬误名称纠错硬样本（小本本第十九节锁定）。",
        "evidence_level": "B-choice-signal",
        "framework_node": "推理部分 / 三段论 / 三段论周延规则·大项不当扩大",
        "needs_codex_recheck": "yes",
    },
    {
        "qid": "Q-2025顺义一模-8",
        "qno": "8",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为人大代表法修正草案、代表联络机制；归属必修三人民代表大会制度；与选必三思维或推理无设问角度。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-9",
        "qno": "9",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为 12356 心理援助热线、政府服务实效；归属必修三服务型政府；与选必三思维方法、推理无关。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-10",
        "qno": "10",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为劳动合同纠纷、女职工特殊保护、解约合法性；归属选必二《法律与生活》劳动法章节。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-11",
        "qno": "11",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为见义勇为补偿、民法典第 183 条受益人补偿；归属选必二《法律与生活》侵权与公平责任章节。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-12",
        "qno": "12",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为传感器数据指导农业、新质生产力；归属必修二经济与社会、创新驱动发展。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-13",
        "qno": "13",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为矿业权竞争性出让、市场配置资源；归属必修二经济与社会、市场体系。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-14",
        "qno": "14",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为国家安全宣传教育主题；归属必修三国家安全观；与选必三思维及推理无对应。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-15",
        "qno": "15",
        "qtype": "选择题",
        "decision": "excluded",
        "decision_reason": "题干为中国国际形象调查、负责任大国；归属选必一《当代国际政治与经济》。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    # ---- 主观题 16-21 ----
    {
        "qid": "Q-2025顺义一模-16",
        "qno": "16",
        "qtype": "主观题",
        "decision": "excluded",
        "decision_reason": "设问明确“运用《哲学与文化》知识”，归属必修四；细则覆盖联系/发展/矛盾/双创/文化功能，与选必三思维方法不重叠。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-17-1",
        "qno": "17(1)",
        "qtype": "主观题",
        "decision": "入正文",
        "decision_reason": "设问明确“运用《逻辑与思维》知识”，考查充分条件假言判断（甲）、必要条件假言判断（乙）、相容选言判断（丙）以及三者同真的条件；2025顺义一模细则给出三类判断对应得分点，证据级别 A-formal。",
        "evidence_level": "A-formal_or_phase12_source_confirmed",
        "framework_node": "推理部分 / 复合判断的演绎推理 / 充分条件假言·必要条件假言·相容选言",
        "needs_codex_recheck": "yes",
    },
    {
        "qid": "Q-2025顺义一模-17-2",
        "qno": "17(2)",
        "qtype": "主观题",
        "decision": "excluded",
        "decision_reason": "设问明确“运用《政治与法治》知识”，归属必修三政府职能与依法治国；非选必三。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-18",
        "qno": "18",
        "qtype": "主观题",
        "decision": "excluded",
        "decision_reason": "设问明确“运用《经济与社会》知识”，归属必修二新发展理念、现代化产业体系。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-19-1",
        "qno": "19(1)",
        "qtype": "主观题",
        "decision": "excluded",
        "decision_reason": "设问明确“运用《法律与生活》知识”分析两个案例如何解决纠纷，归属选必二相邻关系、不正当竞争、行政裁决与诉讼。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-19-2",
        "qno": "19(2)",
        "qtype": "主观题",
        "decision": "excluded",
        "decision_reason": "设问要求“运用法治知识阐释定分止争的价值”，对个人/企业/社会三层价值，归属选必二法治意义专题；非选必三思维或推理。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-20",
        "qno": "20",
        "qtype": "主观题",
        "decision": "excluded",
        "decision_reason": "设问明确“运用《当代国际政治与经济》知识”，归属选必一一带一路、经济全球化、人类命运共同体。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
    {
        "qid": "Q-2025顺义一模-21",
        "qno": "21",
        "qtype": "主观题",
        "decision": "excluded",
        "decision_reason": "设问“综合运用所学”，参考答案分文化角度、政治角度、哲学角度（整体与部分），均无选必三思维方法或推理形式给分点。",
        "evidence_level": "C-boundary_or_duplicate",
        "framework_node": "",
        "needs_codex_recheck": "no",
    },
]

assert len({q["qid"] for q in QUESTIONS}) == 23

# ---------------------------------------------------------------------------
# Detailed entries for 入正文 + 同类索引 questions.
# ---------------------------------------------------------------------------

ENTRIES = [
    # Q3 — 同类索引 (创新思维-逆向思维 边界陷阱)
    {
        "question_id": "Q-2025顺义一模-3",
        "type": "选择题-边界陷阱",
        "framework_node": "创新思维 / 逆向思维 / 边界陷阱",
        "framework_branch": "思维部分",
        "decision": "同类索引",
        "qno": "3",
        "stem_signal": "冰雪运动“通过赛事竞技和文化活动搭建跨文化交流的桥梁”，“通过冰雪文化的传播与共享深化不同国家和地区间的理解与合作”——主体之间是同向交流、共享互鉴，没有把方向、关系或状态反过来的动作。",
        "correct_option": "B",
        "correct_reason": "材料把多元冰雪文化放在交流与交融的语境里，强调文化在互动中赋能不同国家和地区发展，对应共性寓于个性、文化交流相互促进的判断；B 直接复现这层关系。",
        "wrong_option_traps": "A 把共性与个性的方向写反，材料是各国独具个性的文化寓于冰雪运动这一共性文化之中，A 把寓含关系倒置；C 把促进文化交流与经济合作的关键说成承认矛盾普遍性，实际上关键是具体问题具体分析；D 误把跨文化合作读成“运用逆向思维”，材料从头到尾是同向促进，没有把关系或方向反过来的操作。",
        "trap_type": "模块边界陷阱：跨文化合作误读为创新思维-逆向思维。",
        "material_signal": "材料是冰雪运动通过赛事竞技、文化活动搭建跨文化桥梁，是同向促进、共享互鉴，主体行为没有把因当果、把客体当主体或把过程倒过来。",
        "trigger_logic": "选必三逆向思维要求题面出现关系、方向或状态的反转动作；本题材料只有正向桥梁与共享，缺少反转线索，因此 D 选项的“运用逆向思维”属于模块边界误判，不能仅看到“跨界”“合作”就套到逆向思维上。",
        "answer_sentence": "D 错：材料是冰雪运动通过同向交流和共享传播促进各国合作，未出现把关系、方向或状态反过来的动作，不构成逆向思维；正确选项是 B，多元冰雪文化在交流交融中赋能不同国家和地区发展。",
        "evidence_level": "B-choice-signal",
        "needs_codex_recheck": "yes",
        "answer_key_source": "2025顺义一模教师版参考答案 B；细则未为此题设主观题给分项。",
    },
    # Q5 — 入正文 推理部分/形式逻辑/联言矛盾命题
    {
        "question_id": "Q-2025顺义一模-5",
        "type": "选择题-推理形式辨析",
        "framework_node": "推理部分 / 简单判断 / 联言判断与其矛盾命题",
        "framework_branch": "推理部分",
        "decision": "入正文",
        "qno": "5",
        "stem_signal": "原命题“这篇散文不但文笔生动，而且富有哲理”是联言判断 A∧B（A=文笔生动，B=富有哲理）。题目要求选出与之相矛盾的命题。",
        "correct_option": "B",
        "correct_reason": "联言判断 A∧B 的矛盾命题是 ¬A∨¬B，即“至少一个不成立”。B 项“或者文笔不生动，或者不富有哲理”正是 ¬A∨¬B，与原命题在所有可能取值上恰好相反，构成矛盾。",
        "wrong_option_traps": "A 是 ¬A∧¬B，比矛盾命题更强，与原命题是反对关系不是矛盾；C 是 ¬A→B，等价于 A∨B，与原命题可同真，不矛盾；D“只有富有哲理才文笔生动”表达 A→B，必要条件假言判断，与原命题在 A=真且 B=真时同真，不构成矛盾。",
        "trap_type": "把反对命题误当矛盾（A）；把蕴含或假言命题误当矛盾（C、D）。",
        "material_signal": "题干给出的是一个标准的联言判断，没有任何跨模块情境，纯粹考查 A∧B 的矛盾形式。",
        "trigger_logic": "矛盾命题要求两个命题的真值在每一种取值下都相反；联言判断 A∧B 在“仅一个为假”时已经为假，因此其矛盾必须能在 A、B 中至少一个为假时为真，唯有 ¬A∨¬B 满足，对应选言判断。",
        "answer_sentence": "选 B：联言判断 A∧B 的矛盾命题是 ¬A∨¬B，对应“或者文笔不生动，或者不富有哲理”；A 是反对而非矛盾，C、D 是蕴含或假言关系，与原命题可共存。",
        "evidence_level": "B-choice-signal",
        "needs_codex_recheck": "yes",
        "answer_key_source": "2025顺义一模教师版参考答案 B；细则第一部分客观题答案确认 5.B。",
    },
    # Q6 — 入正文 推理部分/概念与判断
    {
        "question_id": "Q-2025顺义一模-6",
        "type": "选择题-概念与判断综合",
        "framework_node": "推理部分 / 概念与判断 / 主项·联言·划分·关系判断",
        "framework_branch": "推理部分",
        "decision": "入正文",
        "qno": "6",
        "stem_signal": "材料是 SFISF 互换便利政策工具，四个选项分别考查“主项识别”“联言判断”“划分错误”“关系判断”四类概念与判断知识点。",
        "correct_option": "A",
        "correct_reason": "①“这个政策工具能够改善非银机构总体的流动性环境”是直言判断，被断定的对象（主项）就是“政策工具”，①正确；②“互换便利不是央行直接给钱，而是通过新工具盘活资产，统筹安排不同市场”是同时对多个特征作出断定的联言判断，能从多方面把握互换便利特点，②正确。",
        "wrong_option_traps": "③把财政政策、公开市场业务、存款准备金、央行贷款并列划分，错误根源是“把宏观调控政策大类与货币政策子类混为一级”，属于“越级划分”而不是“划分标准不一”，③错；④把“获得流动性支持”说成反对称关系不准确——反对称关系要求 A 对 B 有该关系则 B 对 A 一定无；本题情境里央行向证券公司提供流动性支持本身没有逻辑上必然的反向否定关系，④错。",
        "trap_type": "①主项误判（把谓项当主项）；②联言判断与选言判断混淆；③越级划分误称为划分标准不一；④对称/非对称/反对称关系定义混淆。",
        "material_signal": "题干给出 SFISF 政策工具的多种判断表述（功能、机制、政策工具分类、给予流动性支持），需要逐句辨析其逻辑结构。",
        "trigger_logic": "主项是被断定的对象；联言判断要求多个命题同时成立；划分要求标准统一且分项覆盖一级而非跨级；关系判断要根据“A 对 B 关系是否必然反否 B 对 A”来判定对称/反对称。本题逐项调用上述定义即可。",
        "answer_sentence": "选 A：①“政策工具”是该判断的主项；②对互换便利多侧面的同时断定属联言判断；③把财政政策与货币政策子工具并列是越级划分，不是划分标准不一；④央行向金融机构提供流动性支持不构成反对称关系，所以①②对、③④错。",
        "evidence_level": "B-choice-signal",
        "needs_codex_recheck": "yes",
        "answer_key_source": "2025顺义一模教师版参考答案 A；细则第一部分客观题答案确认 6.A。",
    },
    # Q7 — 入正文 推理部分/三段论硬样本
    {
        "question_id": "Q-2025顺义一模-7",
        "type": "选择题-三段论谬误辨析",
        "framework_node": "推理部分 / 三段论 / 三段论周延规则·大项不当扩大",
        "framework_branch": "推理部分",
        "decision": "入正文",
        "qno": "7",
        "stem_signal": "题干为逆向选择，要求选出三段论“逻辑分析错误”的一项。A 项三段论“凡共青团员都是青年；并非所有的青年工人都是共青团员；所以并非所有的青年工人都是青年”被作者标注为“小项不当扩大”。",
        "correct_option": "A",
        "correct_reason": "在 A 项三段论里，大项是“青年”：在大前提“凡共青团员都是青年”里作为肯定判断的谓项，不周延；在结论“并非所有的青年工人都是青年”里作为否定判断的谓项，周延。前提不周延而结论周延，所以犯的是“大项不当扩大”，作者却把它写成“小项不当扩大”，名称错配——即“分析错误”，正是题目要选的项。",
        "wrong_option_traps": "B“两个否定前提不能必然推出结论”——分析正确；C“四概念”错误，前后两个“物质”分别是哲学概念与具体形态，分析正确；D“中项不周延”，中项“农民”在两个特称前提中都不周延，分析正确。它们都是对原三段论错误类型的正确诊断，与题意（要选错误分析）不符。",
        "trap_type": "三段论谬误名称纠错：把“大项不当扩大”误称为“小项不当扩大”。这是顺义一模 7 永久硬样本（小本本第十九节）。",
        "material_signal": "选项中给出的是三段论原文 + 作者对错误类型的标签，要求识别标签是否与三段论真正违反的规则一致。",
        "trigger_logic": "三段论周延规则规定：前提中不周延的项在结论中不得周延。判断时要先定大项/小项/中项，再分别考察其在前提与结论中的周延情况；只有“在结论中周延而在前提中不周延”的项扩大才叫“大项不当扩大”或“小项不当扩大”，其判定取决于该项是大项还是小项，不能凭名字相似互换。",
        "answer_sentence": "选 A：该三段论中“青年”是大项，前提里不周延、结论里周延，犯的是“大项不当扩大”；作者把它写成“小项不当扩大”属于谬误名称错配，所以 A 的逻辑分析错误，符合逆向选择题题意。",
        "evidence_level": "B-choice-signal",
        "needs_codex_recheck": "yes",
        "answer_key_source": "2025顺义一模教师版参考答案 A；细则第一部分客观题答案确认 7.A；选必三硬规则记事本第十九节锁定为三段论谬误名称纠错硬样本。",
    },
    # Q17(1) — 入正文 推理部分/复合判断
    {
        "question_id": "Q-2025顺义一模-17-1",
        "type": "主观题-复合判断演绎推理",
        "framework_node": "推理部分 / 复合判断的演绎推理 / 充分条件假言·必要条件假言·相容选言",
        "framework_branch": "推理部分",
        "decision": "入正文",
        "qno": "17(1)",
        "full_question": "结合材料，运用《逻辑与思维》知识，写出上述同学判断同时为真的条件，并说明理由。",
        "rubric_position": "2025顺义一模细则 17（1）：1.条件 1 分（既┄┄又┄┄）；2.理由 3 分（1+2），具体采分点：（1）能够准确并全部写对三位同学判断类型，给 1 分（甲—充分条件假言判断、乙—必要条件假言判断、丙—相容选言判断）；（2）三个判断类型中，有一个具体分析准确，即可得 2 分。",
        "source": "2025年北京市顺义区高三一模 政治学科 第17题第（1）问",
        "material_action": "甲、乙、丙三位同学就“为什么是杭州”分别给出三种复合判断：甲是“如果……那么……”假言句、乙是“除非……否则不能……”句式、丙是“……或者……或者……”选言句，要求把三人同时为真的条件写出并解释。",
        "judgment_type_chain": "甲为充分条件假言判断（如 P 则 Q，肯前必肯后、否后必否前）；乙为必要条件假言判断（除非 P 否则不能 Q ⇔ 只有 P 才 Q，肯后必肯前、否前必否后）；丙为相容选言判断（P 或 Q，至少一支为真即整体为真，可全真）。",
        "trigger_logic": "三个判断都涉及“科创基金支持”（P）与“成为科创人才高地”（Q）。要让三句话同时为真：甲只要 P→Q 的真值表不出现“P 真 Q 假”即可；乙只要不出现“Q 真 P 假”即可；丙只要 P、Q 至少一个为真即可。三者同时为真的最稳条件是 P 与 Q 都真——即“杭州既获得科创基金支持，又成为科创人才高地”。",
        "answer_sentence": "条件：杭州既获得科创基金支持，又成为科创人才高地。理由：甲是充分条件假言判断，肯前必肯后，当“有科创基金支持”为真且“成为科创人才高地”为真时，甲的判断为真；乙是必要条件假言判断（“除非 P 否则不能 Q”等价于“只有 P 才 Q”），肯后必肯前，当“成为科创人才高地”为真且“有科创基金支持”为真时，乙的判断为真；丙是相容选言判断，只要其选言支至少一个为真即整体为真，当 P、Q 都为真时丙必然为真。所以三人判断同时为真的充要条件是“杭州既获得科创基金支持又成为科创人才高地”。",
        "framework_node_text": "推理部分 / 复合判断的演绎推理 / 充分条件假言·必要条件假言·相容选言（同真条件题）",
        "question_family_tag": "复合判断同真条件辨析；多个假言/选言并立时求三者同真的最稳取值组合。",
        "material_signal": "甲“如果……那么……”、乙“除非……否则不能……”、丙“或者……或者……”——三种典型复合判断同时出现，要求识别类型并求同真。",
        "evidence_level": "A-formal_or_phase12_source_confirmed",
        "needs_codex_recheck": "yes",
    },
]

# ---------------------------------------------------------------------------
# CSV writers
# ---------------------------------------------------------------------------

def write_question_decisions() -> None:
    path = BATCH_DIR / "QUESTION_DECISIONS.csv"
    fields = [
        "question_id",
        "suite_id",
        "original_qno",
        "question_type",
        "claudecode_decision",
        "decision_reason",
        "evidence_level",
        "framework_node",
        "needs_codex_recheck",
        "source_batch",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for q in QUESTIONS:
            w.writerow({
                "question_id": q["qid"],
                "suite_id": SUITE_ID,
                "original_qno": q["qno"],
                "question_type": q["qtype"],
                "claudecode_decision": q["decision"],
                "decision_reason": q["decision_reason"],
                "evidence_level": q["evidence_level"],
                "framework_node": q["framework_node"],
                "needs_codex_recheck": q["needs_codex_recheck"],
                "source_batch": SOURCE_BATCH,
            })


def write_main_thinking_ledger() -> None:
    path = BATCH_DIR / "MAIN_THINKING_LEDGER.csv"
    fields = [
        "question_id",
        "suite_id",
        "original_qno",
        "thinking_method_or_score_point",
        "full_question",
        "rubric_position",
        "source",
        "material_action",
        "main_hat",
        "small_method",
        "trigger_logic",
        "answer_sentence",
        "framework_node",
        "question_family_tag",
        "evidence_level",
        "claudecode_decision",
        "needs_codex_recheck",
        "source_batch",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        # Only main-question entries (主观题 with thinking/reasoning content).
        # 17(1) is the only 主观题 in this suite that maps to 选必三 (推理部分).
        e = next(x for x in ENTRIES if x["question_id"] == "Q-2025顺义一模-17-1")
        w.writerow({
            "question_id": e["question_id"],
            "suite_id": SUITE_ID,
            "original_qno": e["qno"],
            "thinking_method_or_score_point": "充分条件假言判断 / 必要条件假言判断 / 相容选言判断 三类同真条件",
            "full_question": e["full_question"],
            "rubric_position": e["rubric_position"],
            "source": e["source"],
            "material_action": e["material_action"],
            "main_hat": "推理部分（演绎推理 - 复合判断）",
            "small_method": e["judgment_type_chain"],
            "trigger_logic": e["trigger_logic"],
            "answer_sentence": e["answer_sentence"],
            "framework_node": e["framework_node_text"],
            "question_family_tag": e["question_family_tag"],
            "evidence_level": e["evidence_level"],
            "claudecode_decision": e["decision"],
            "needs_codex_recheck": e["needs_codex_recheck"],
            "source_batch": SOURCE_BATCH,
        })


def write_choice_trap_ledger() -> None:
    path = BATCH_DIR / "CHOICE_TRAP_LEDGER.csv"
    fields = [
        "question_id",
        "suite_id",
        "original_qno",
        "stem_signal",
        "correct_option",
        "correct_reason",
        "wrong_option_traps",
        "trap_type",
        "material_signal",
        "trigger_logic",
        "answer_sentence",
        "framework_node",
        "evidence_level",
        "answer_key_source",
        "claudecode_decision",
        "needs_codex_recheck",
        "source_batch",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for e in ENTRIES:
            if e["type"].startswith("选择题"):
                w.writerow({
                    "question_id": e["question_id"],
                    "suite_id": SUITE_ID,
                    "original_qno": e["qno"],
                    "stem_signal": e["stem_signal"],
                    "correct_option": e["correct_option"],
                    "correct_reason": e["correct_reason"],
                    "wrong_option_traps": e["wrong_option_traps"],
                    "trap_type": e["trap_type"],
                    "material_signal": e["material_signal"],
                    "trigger_logic": e["trigger_logic"],
                    "answer_sentence": e["answer_sentence"],
                    "framework_node": e["framework_node"],
                    "evidence_level": e["evidence_level"],
                    "answer_key_source": e["answer_key_source"],
                    "claudecode_decision": e["decision"],
                    "needs_codex_recheck": e["needs_codex_recheck"],
                    "source_batch": SOURCE_BATCH,
                })


def write_framework_node_matrix() -> None:
    path = BATCH_DIR / "FRAMEWORK_NODE_MATRIX.csv"
    fields = [
        "framework_branch",
        "framework_node",
        "subnode",
        "question_id",
        "original_qno",
        "type",
        "mount_role",
        "evidence_level",
        "claudecode_decision",
        "source_batch",
    ]
    rows = [
        # Q3 — 同类索引 to 创新思维-逆向思维 (boundary)
        {
            "framework_branch": "思维部分",
            "framework_node": "创新思维",
            "subnode": "逆向思维 / 边界陷阱",
            "question_id": "Q-2025顺义一模-3",
            "original_qno": "3",
            "type": "选择题",
            "mount_role": "边界陷阱（同类索引）",
            "evidence_level": "B-choice-signal",
            "claudecode_decision": "同类索引",
            "source_batch": SOURCE_BATCH,
        },
        # Q5 — 入正文 推理部分/简单判断
        {
            "framework_branch": "推理部分",
            "framework_node": "简单判断",
            "subnode": "联言判断与其矛盾命题（A∧B 的矛盾为 ¬A∨¬B）",
            "question_id": "Q-2025顺义一模-5",
            "original_qno": "5",
            "type": "选择题",
            "mount_role": "正文正例（选择题）",
            "evidence_level": "B-choice-signal",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q6 — 入正文 推理部分/概念与判断 (复合 4 选项)
        {
            "framework_branch": "推理部分",
            "framework_node": "概念与判断",
            "subnode": "主项·联言·划分·关系判断综合辨析",
            "question_id": "Q-2025顺义一模-6",
            "original_qno": "6",
            "type": "选择题",
            "mount_role": "正文正例（选择题）",
            "evidence_level": "B-choice-signal",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q6 重复挂载: ③ 越级划分（划分章节子点）
        {
            "framework_branch": "推理部分",
            "framework_node": "概念与判断",
            "subnode": "划分 / 越级划分误称划分标准不一",
            "question_id": "Q-2025顺义一模-6",
            "original_qno": "6",
            "type": "选择题",
            "mount_role": "选择题陷阱（辅助挂载）",
            "evidence_level": "B-choice-signal",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q6 重复挂载: ④ 反对称关系
        {
            "framework_branch": "推理部分",
            "framework_node": "概念与判断",
            "subnode": "关系判断 / 反对称关系定义",
            "question_id": "Q-2025顺义一模-6",
            "original_qno": "6",
            "type": "选择题",
            "mount_role": "选择题陷阱（辅助挂载）",
            "evidence_level": "B-choice-signal",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q7 — 入正文 推理部分/三段论 (硬样本)
        {
            "framework_branch": "推理部分",
            "framework_node": "三段论",
            "subnode": "三段论周延规则 / 大项不当扩大（小本本硬样本）",
            "question_id": "Q-2025顺义一模-7",
            "original_qno": "7",
            "type": "选择题",
            "mount_role": "正文正例（选择题硬样本：谬误名称纠错）",
            "evidence_level": "B-choice-signal",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q7 辅助挂载: 中项不周延 (D 项)
        {
            "framework_branch": "推理部分",
            "framework_node": "三段论",
            "subnode": "三段论周延规则 / 中项不周延（D 项辅助挂载）",
            "question_id": "Q-2025顺义一模-7",
            "original_qno": "7",
            "type": "选择题",
            "mount_role": "辅助挂载（中项不周延实例）",
            "evidence_level": "B-choice-signal",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q7 辅助挂载: 四概念
        {
            "framework_branch": "推理部分",
            "framework_node": "三段论",
            "subnode": "三段论 / 四概念错误（C 项辅助挂载）",
            "question_id": "Q-2025顺义一模-7",
            "original_qno": "7",
            "type": "选择题",
            "mount_role": "辅助挂载（四概念实例）",
            "evidence_level": "B-choice-signal",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q17(1) — 入正文 推理部分/复合判断
        {
            "framework_branch": "推理部分",
            "framework_node": "复合判断的演绎推理",
            "subnode": "充分条件假言判断 + 必要条件假言判断 + 相容选言判断 同真条件",
            "question_id": "Q-2025顺义一模-17-1",
            "original_qno": "17(1)",
            "type": "主观题",
            "mount_role": "正文正例（主观题，A-formal）",
            "evidence_level": "A-formal_or_phase12_source_confirmed",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q17(1) 辅助挂载: 必要条件假言判断
        {
            "framework_branch": "推理部分",
            "framework_node": "复合判断的演绎推理",
            "subnode": "必要条件假言判断 / 除非……否则不能……",
            "question_id": "Q-2025顺义一模-17-1",
            "original_qno": "17(1)",
            "type": "主观题",
            "mount_role": "辅助挂载（必要条件假言子点）",
            "evidence_level": "A-formal_or_phase12_source_confirmed",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
        # Q17(1) 辅助挂载: 相容选言
        {
            "framework_branch": "推理部分",
            "framework_node": "复合判断的演绎推理",
            "subnode": "相容选言判断 / 至少一支为真",
            "question_id": "Q-2025顺义一模-17-1",
            "original_qno": "17(1)",
            "type": "主观题",
            "mount_role": "辅助挂载（相容选言子点）",
            "evidence_level": "A-formal_or_phase12_source_confirmed",
            "claudecode_decision": "入正文",
            "source_batch": SOURCE_BATCH,
        },
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_framework_node_matrix_summary() -> None:
    path = BATCH_DIR / "FRAMEWORK_NODE_MATRIX_SUMMARY.csv"
    fields = [
        "framework_branch",
        "framework_node",
        "total_mounts",
        "ruzhengwen_count",
        "tonglei_index_count",
        "blocked_count",
        "excluded_count",
        "questions",
    ]
    summary = [
        {
            "framework_branch": "思维部分",
            "framework_node": "创新思维 / 逆向思维",
            "total_mounts": 1,
            "ruzhengwen_count": 0,
            "tonglei_index_count": 1,
            "blocked_count": 0,
            "excluded_count": 0,
            "questions": "Q-2025顺义一模-3 (边界陷阱，同类索引)",
        },
        {
            "framework_branch": "推理部分",
            "framework_node": "简单判断 / 联言判断与其矛盾命题",
            "total_mounts": 1,
            "ruzhengwen_count": 1,
            "tonglei_index_count": 0,
            "blocked_count": 0,
            "excluded_count": 0,
            "questions": "Q-2025顺义一模-5",
        },
        {
            "framework_branch": "推理部分",
            "framework_node": "概念与判断",
            "total_mounts": 3,
            "ruzhengwen_count": 3,
            "tonglei_index_count": 0,
            "blocked_count": 0,
            "excluded_count": 0,
            "questions": "Q-2025顺义一模-6 (主挂主项·联言；辅助挂载越级划分、反对称关系)",
        },
        {
            "framework_branch": "推理部分",
            "framework_node": "三段论",
            "total_mounts": 3,
            "ruzhengwen_count": 3,
            "tonglei_index_count": 0,
            "blocked_count": 0,
            "excluded_count": 0,
            "questions": "Q-2025顺义一模-7 (主挂大项不当扩大-硬样本；辅助挂载中项不周延、四概念)",
        },
        {
            "framework_branch": "推理部分",
            "framework_node": "复合判断的演绎推理",
            "total_mounts": 3,
            "ruzhengwen_count": 3,
            "tonglei_index_count": 0,
            "blocked_count": 0,
            "excluded_count": 0,
            "questions": "Q-2025顺义一模-17(1) (主挂三类同真；辅助挂载必要条件假言、相容选言)",
        },
        {
            "framework_branch": "（边界 - 不入选必三任何节点）",
            "framework_node": "其他模块（必修二/三/四 + 选必一/二）",
            "total_mounts": 18,
            "ruzhengwen_count": 0,
            "tonglei_index_count": 0,
            "blocked_count": 0,
            "excluded_count": 18,
            "questions": "Q1, Q2, Q4, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17(2), Q18, Q19(1), Q19(2), Q20, Q21",
        },
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in summary:
            w.writerow(r)


# ---------------------------------------------------------------------------
# JSONL writer
# ---------------------------------------------------------------------------

def write_entries_jsonl() -> None:
    path = BATCH_DIR / "entries" / "batch04a_entries.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for e in ENTRIES:
            obj = {
                "question_id": e["question_id"],
                "type": e["type"],
                "framework_node": e["framework_node"],
                "material_signal": e["material_signal"],
                "trigger_logic": e["trigger_logic"],
                "answer_sentence": e["answer_sentence"],
                "evidence_level": e["evidence_level"],
                "needs_codex_recheck": e["needs_codex_recheck"],
                "source_batch": SOURCE_BATCH,
                "suite_id": SUITE_ID,
                "original_qno": e["qno"],
                "claudecode_decision": e["decision"],
                "framework_branch": e["framework_branch"],
            }
            if e["type"].startswith("选择题"):
                obj["stem_signal"] = e["stem_signal"]
                obj["correct_option"] = e["correct_option"]
                obj["correct_reason"] = e["correct_reason"]
                obj["wrong_option_traps"] = e["wrong_option_traps"]
                obj["trap_type"] = e["trap_type"]
                obj["answer_key_source"] = e["answer_key_source"]
            else:
                obj["full_question"] = e["full_question"]
                obj["rubric_position"] = e["rubric_position"]
                obj["source"] = e["source"]
                obj["material_action"] = e["material_action"]
                obj["judgment_type_chain"] = e["judgment_type_chain"]
                obj["question_family_tag"] = e["question_family_tag"]
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def main() -> None:
    write_question_decisions()
    write_main_thinking_ledger()
    write_choice_trap_ledger()
    write_framework_node_matrix()
    write_framework_node_matrix_summary()
    write_entries_jsonl()
    print("CSV/JSONL outputs written.")


if __name__ == "__main__":
    main()
