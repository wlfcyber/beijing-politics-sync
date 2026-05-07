# -*- coding: utf-8 -*-
"""Builder for batch03a (S-2025东城期末) outputs.

Writes:
- QUESTION_DECISIONS.csv
- MAIN_THINKING_LEDGER.csv
- CHOICE_TRAP_LEDGER.csv
- FRAMEWORK_NODE_MATRIX.csv
- FRAMEWORK_NODE_MATRIX_SUMMARY.csv
- BLOCKED_OR_BOUNDARY.md
- suite_reports/S-2025东城期末.md
- entries/batch03a_entries.jsonl

Note: PROGRESS.md and BATCH03A_ACCEPTANCE.md are written separately as static
markdown so the run-time evidence stays human-authored.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

BATCH_DIR = Path(__file__).resolve().parent
SUITE_ID = "S-2025东城期末"
SOURCE_BATCH = "batch03a_dongcheng_qimo_2025"


# ---------- raw decisions for all 24 unique question_ids ----------

decisions = [
    # 1-15 are choice questions; 16-21 are subjective (with sub-parts).
    {
        "question_id": "Q-2025东城期末-1",
        "original_qno": "1",
        "question_type": "选择题",
        "answer_letter": "D",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案D；十一届/十四届/二十届三中全会与改革开放这一主轴，"
            "考核改革开放是坚持发展中国特色社会主义的必由之路；属必修一中国特色社会主义模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-2",
        "original_qno": "2",
        "question_type": "选择题",
        "answer_letter": "D",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案D；邓小平理论是中国特色社会主义理论体系的奠基之作并明确提出走自己的路；属必修一中特理论体系考点，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-3",
        "original_qno": "3",
        "question_type": "选择题",
        "answer_letter": "B",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案B；优秀人物事迹生发报效祖国斗志、转化为推动社会发展的物质力量；属必修四文化的功能模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-4",
        "original_qno": "4",
        "question_type": "选择题",
        "answer_letter": "A",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案A；汉字笔画对立统一、笔画蕴含精神向往；属必修四矛盾观+中华优秀传统文化模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-5",
        "original_qno": "5",
        "question_type": "选择题",
        "answer_letter": "C",
        "claudecode_decision": "入正文",
        "decision_reason": (
            "答案C(②④)；社区公园直角改圆角、入口拓宽提升体验。"
            "②命中辩证思维整体性+动态性，④命中矛盾分析法；①把'人为事物联系'误说成'自在联系'(必修四联系观陷阱)，"
            "③把'否定不合理保留合理'误说成'否定过去肯定现在'(辩证否定观陷阱)。可入选必三辩证思维 choice trap。"
        ),
        "needs_codex_recheck": "yes",
    },
    {
        "question_id": "Q-2025东城期末-6",
        "original_qno": "6",
        "question_type": "选择题",
        "answer_letter": "C",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案C；全国人大常委会立法权+草案公开征求意见常态化推进科学民主立法；属必修三政治与法治模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-7",
        "original_qno": "7",
        "question_type": "选择题",
        "answer_letter": "B",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案B(①④)；宏观调控+优化营商环境+鼓励芯片技术研发推动产业转型升级；属必修二经济与社会传导路径题，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-8",
        "original_qno": "8",
        "question_type": "选择题",
        "answer_letter": "B",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案B；外资战略投资管理办法降低投资门槛、拓宽外资投资渠道营造公平投资环境；属必修二经济与社会更高层次开放型经济，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-9",
        "original_qno": "9",
        "question_type": "选择题",
        "answer_letter": "A",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案A；金砖国家会晤反映发展中国家谋和平发展、促合作共赢的强烈愿望；属选必一国际政治与经济模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-10",
        "original_qno": "10",
        "question_type": "选择题",
        "answer_letter": "C",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案C；全球发展倡议之友小组+中国方案中国行动凝聚国际共识；属选必一国际政治与经济模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-11",
        "original_qno": "11",
        "question_type": "选择题",
        "answer_letter": "C",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案C(②④)；数据知识产权登记证书降低举证难度+完善行政与司法协同保护机制；属选必二法律与生活+必修三政治与法治模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-12",
        "original_qno": "12",
        "question_type": "选择题",
        "answer_letter": "A",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "答案A；民法典合同/遗赠扶养/股票质押/作品转载付酬规则；属选必二法律与生活模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-13",
        "original_qno": "13",
        "question_type": "选择题",
        "answer_letter": "B",
        "claudecode_decision": "入正文",
        "decision_reason": (
            "答案B(①③)；①'大国重器'作中项不周延，③'适合山地骑行'作中项不周延，二者违反相同规则即'中项至少周延一次'。"
            "②'三盘六针'前提中不周延、结论中周延犯大项不当扩大；④'智能温控系统'前后含义错位犯四概念错误。可入选必三推理-三段论选择题陷阱。"
        ),
        "needs_codex_recheck": "yes",
    },
    {
        "question_id": "Q-2025东城期末-14",
        "original_qno": "14",
        "question_type": "选择题",
        "answer_letter": "D",
        "claudecode_decision": "入正文",
        "decision_reason": (
            "答案D；性质判断与关系判断综合题。A把整体与部分关系误标为属种关系；B'位于北京老城中心'是反对称关系不是传递关系；"
            "C两个'中'外延不一致；D'统领整个老城规划格局的建筑与遗址的组合体'是简单肯定判断的谓项，因联项肯定故谓项不周延，正解。"
            "可入选必三-判断章选择题陷阱。"
        ),
        "needs_codex_recheck": "yes",
    },
    {
        "question_id": "Q-2025东城期末-15",
        "original_qno": "15",
        "question_type": "选择题",
        "answer_letter": "B",
        "claudecode_decision": "入正文",
        "decision_reason": (
            "答案B；前提'如果赵→李陈/李大钊'是充分条件假言判断，规则'肯前必肯后、否后必否前'。"
            "B肯定前件赵且否定后件不去陈/不去大钊，违反'肯前必肯后'，必假；A为'只有…才'式必要条件不矛盾；"
            "C否前不能否后；D肯后不能肯前(逆否换位失败)。可入选必三推理-假言推理选择题陷阱。"
        ),
        "needs_codex_recheck": "yes",
    },
    {
        "question_id": "Q-2025东城期末-16",
        "original_qno": "16",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "8分；'器以述史，物以载道'+《哲学与文化》知识；细则三层为中华文化源远流长博大精深+文化载体+意识能动作用；属必修四哲学与文化模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-17",
        "original_qno": "17",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "9分；北京法院如何提升'生态颜值'+法治知识；细则三层为审判权惩处+劳务代偿创新司法+宣传教育公开道歉；属必修三政治与法治+选必二法律与生活模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-18-1",
        "original_qno": "18(1)",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "5分；'嫦娥揽月回'+《经济与社会》知识；细则三层为政府履行经济职能+社会主义基本经济制度新型举国体制+两个毫不动摇深化体制机制改革；"
            "属必修二经济与社会模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-18-2",
        "original_qno": "18(2)",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "入正文",
        "decision_reason": (
            "4分；登月服设计如何体现创新思维+《逻辑与思维》知识。"
            "东城期末细则PPTX明确两层：第一层创新思维表现/特点(思路新方法新结果新或多向性跨越性独特性)1分；"
            "第二层具体方法(聚焦核心问题综合考虑不同需要→聚合+发散；服装造型与火箭形象传统文化联系→联想；"
            "提前预判月面环境与航天员需求→超前)，写对一点2分、二点3分。可入选必三创新思维主链(联想/聚合+发散/超前)。"
        ),
        "needs_codex_recheck": "yes",
    },
    {
        "question_id": "Q-2025东城期末-19-1",
        "original_qno": "19(1)",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "短答；电动自行车充电柜涉及的法律问题；细则两思路：是否符合/违反消防与共有部分用途规定；涉及哪些权利(侵权、相邻权、人身安全、财产权)。属选必二法律与生活模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-19-2",
        "original_qno": "19(2)",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "短答；解决电动自行车安家难的利益相关方；细则得分主体为街道办事处/消防部门/居委会/党/基层党组织等。属必修三政治与法治+基层群众自治模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-19-3",
        "original_qno": "19(3)",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "短答；如何更好解决居民分歧达成共识；细则两层：相邻关系原则+权利有界限(选必二法律与生活)；民主协商+民主决策(必修三政治与法治)。不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-20",
        "original_qno": "20",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "excluded",
        "decision_reason": (
            "8分短文；新能源汽车反补贴税+《当代国际政治与经济》知识；细则三层为中国贡献+欧盟逆全球化贸易保护+国家利益与共同利益和平谈判。属选必一国际政治与经济模块，不进入选必三思维主链。"
        ),
        "needs_codex_recheck": "no",
    },
    {
        "question_id": "Q-2025东城期末-21",
        "original_qno": "21",
        "question_type": "主观题",
        "answer_letter": "",
        "claudecode_decision": "同类索引",
        "decision_reason": (
            "10分综合短文；'中国式现代化民生为大'+综合运用所学；细则按知识运用方面数给等级分(党的领导/以人民为中心/法治/公共服务/中华优秀传统文化等)。"
            "本题不限定选必三知识范围，不入选必三思维主链正文；可作为综合短文同类索引保留，提醒学生'综合运用所学'类设问可视答题角度涉及辩证思维等思维方法但本题细则未独立给分。"
        ),
        "needs_codex_recheck": "no",
    },
]


def write_question_decisions() -> Path:
    out = BATCH_DIR / "QUESTION_DECISIONS.csv"
    fieldnames = [
        "question_id",
        "suite_id",
        "original_qno",
        "question_type",
        "answer_letter",
        "claudecode_decision",
        "decision_reason",
        "needs_codex_recheck",
    ]
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for d in decisions:
            w.writerow({
                "question_id": d["question_id"],
                "suite_id": SUITE_ID,
                "original_qno": d["original_qno"],
                "question_type": d["question_type"],
                "answer_letter": d["answer_letter"],
                "claudecode_decision": d["claudecode_decision"],
                "decision_reason": d["decision_reason"],
                "needs_codex_recheck": d["needs_codex_recheck"],
            })
    return out


# ---------- subjective body entries ----------

main_thinking_rows = [
    {
        "question_id": "Q-2025东城期末-18-2",
        "suite_id": SUITE_ID,
        "original_qno": "18(2)",
        "score": "4",
        "rubric_phrase": "登月服的设计体现了思路新、方法新、结果新（创新思维表现/特点）",
        "full_question": (
            "结合材料，运用《逻辑与思维》知识，说明登月服设计是如何体现创新思维的。"
        ),
        "rubric_position": (
            "套卷S-2025东城期末第18(2)题；"
            "评分来源为《2025东城期末细则.pptx》Slide3-Slide4 阅卷细则；"
            "第一层次1分(创新思维表现/特点)；第二层次具体方法满分3分(写对1点2分、2点3分)。"
        ),
        "source": "2025-东城-期末-Q18(2)",
        "material_signal": (
            "登月服外观把'飞天'飘带造型、火箭升空尾焰造型与中华民族开拓进取精神相联系；"
            "聚焦完成登月任务核心问题，综合考虑月面环境、航天员行走攀爬驾车科考等不同需要；"
            "综合防护面料、全景式防眩光面窗等细节预先考虑月面热环境、月尘以及航天员视觉工效需求。"
        ),
        "total_hat": "创新思维",
        "small_method": "联想思维 + 聚合思维与发散思维 + 超前思维",
        "trigger_logic": (
            "把服装造型设计同火箭形象、传统文化这种本来不相关的对象在头脑中建立可比较、可借用的联系，是创新思维的联想小方法；"
            "围绕登月任务这一核心问题先在头脑中铺开月面环境、出舱动作、视觉工效等多方向需要再收束到一套统一的设计方案，"
            "这种方案铺开再收束的过程就是发散思维与聚合思维的配套使用；"
            "把月面热环境、月尘干扰、航天员登陆后的需求提前预判并据此设计细节，"
            "是把握事物变化趋势、未雨绸缪的超前思维。三个小方法共同支撑登月服设计在思路、方法、结果上都呈现出新的样态。"
        ),
        "answer_sentence": (
            "登月服把飞天飘带和火箭尾焰造型与中华传统文化形象联系起来，运用联想思维实现思路新；"
            "聚焦登月任务核心问题，把月面环境、航天员行走攀爬等不同需要先发散再聚合到一套设计方案中，"
            "运用发散思维与聚合思维实现方法新；提前预判月面热环境、月尘和航天员登陆后的需求，"
            "据此设计综合防护面料和全景式防眩光面窗等细节，运用超前思维实现结果新；"
            "整套设计因而体现了创新思维在思路、方法、结果三个维度的创新。"
        ),
        "framework_node": "创新思维 / 联想思维; 创新思维 / 发散思维与聚合思维; 创新思维 / 超前思维",
        "question_family": "创新思维体现类(产品设计/方案设计 → 思路新方法新结果新 + 联想/发散聚合/超前)",
        "evidence_level": "A-formal",
    },
]


def write_main_thinking_ledger() -> Path:
    out = BATCH_DIR / "MAIN_THINKING_LEDGER.csv"
    fieldnames = [
        "question_id",
        "suite_id",
        "original_qno",
        "score",
        "rubric_phrase",
        "full_question",
        "rubric_position",
        "source",
        "material_signal",
        "total_hat",
        "small_method",
        "trigger_logic",
        "answer_sentence",
        "framework_node",
        "question_family",
        "evidence_level",
    ]
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in main_thinking_rows:
            w.writerow(r)
    return out


# ---------- choice trap entries ----------

choice_trap_rows = [
    {
        "question_id": "Q-2025东城期末-5",
        "suite_id": SUITE_ID,
        "original_qno": "5",
        "answer_letter": "C",
        "answer_options": "②④",
        "framework_node": "辩证思维 / 整体性 + 动态性 + 矛盾分析法",
        "question_stem": (
            "社区公园原入口仅两块砖宽且呈直角转弯，道路狭窄、容易踩踏绿地。"
            "改造后把直角变圆角，入口变宽，居民结伴散步更安全便利、休闲体验提升。下列评论恰当的是。"
        ),
        "material_signal": (
            "原入口窄+直角+踩踏绿地→把入口拓宽+把直角变圆角→居民通行更顺、休闲体验提升；"
            "这是把入口、绿地、通行、居民体验等要素放在一起考量，并随着使用情况推动空间形态由直角向圆角的过程发展。"
        ),
        "correct_reasoning": (
            "②命中辩证思维的整体性与动态性：改造把入口宽度、转弯角度、绿地保护、居民通行多种要素放进同一个社区环境的有机整体里再调整，"
            "并以动态变化的视角看到原状态向更优状态的发展过程。"
            "④命中矛盾分析法：原入口的'窄'与居民'要走得开'的需要构成矛盾，改造正是通过抓住主要矛盾、化解对立来为居民解忧。"
        ),
        "wrong_options": (
            "①把'人为事物的联系'(改造形成的新空间联系)误说成'自在联系'，犯必修四联系观陷阱；"
            "③把辩证否定观'否定不合理因素、肯定合理因素'误说成'否定过去、肯定现在'，犯辩证否定观陷阱。"
        ),
        "trap_type": "辩证思维内部小方法张冠李戴 + 必修四联系观/辩证否定观跨模块陷阱",
        "trigger_logic": (
            "学生看到'改造、整体、协调多方'就要回到辩证思维的整体性+动态性，看到'抓住主要冲突来解决'就要回到矛盾分析法；"
            "看到'联系'两个字不能直接套联系观，要分清是人为事物的联系还是自在事物的联系；"
            "看到'否定'两个字不能直接套辩证否定，要看是否同时'否定不合理、保留合理'。"
        ),
        "answer_sentence": (
            "选C；②是辩证思维的整体性与动态性，因为改造把入口、绿地、居民通行多个要素整体考虑并在变化中优化；"
            "④是矛盾分析法，因为改造抓住了通行难这一主要矛盾。①把人为事物联系错说成自在联系，③把辩证否定错说成简单的否定过去肯定现在，均是混淆陷阱。"
        ),
        "evidence_level": "B-choice-signal",
    },
    {
        "question_id": "Q-2025东城期末-13",
        "suite_id": SUITE_ID,
        "original_qno": "13",
        "answer_letter": "B",
        "answer_options": "①③",
        "framework_node": "推理 / 三段论 / 中项不周延",
        "question_stem": (
            "下列三段论推理违反相同逻辑规则的是："
            "①祥云AS700是大国重器，有的大国重器是载人飞艇，有的载人飞艇是祥云AS700；"
            "②歼-20飞行员手表有三盘六针，这款手表不是歼-20飞行员手表，这款手表没有三盘六针；"
            "③碳纤维自行车适合山地骑行，山地车适合山地骑行，碳纤维自行车是山地车；"
            "④石墨烯围巾有智能温控系统，智能温控系统能自动调节温度，石墨烯围巾能自动调节温度。"
        ),
        "material_signal": (
            "四条推理形式上都是三段论，但分别藏着三类规则错误：①与③在中项处栽跟头；②在大项前后周延性变化处栽跟头；④在'同一名称、不同含义'处栽跟头。"
        ),
        "correct_reasoning": (
            "①把'大国重器'当中项，前提中两个'有的'都没有让中项至少周延一次，犯中项不周延错误；"
            "③把'适合山地骑行'当中项，两次出现都不周延，同样犯中项不周延错误。①③共同违反'中项在前提中至少周延一次'这条规则，故选B。"
        ),
        "wrong_options": (
            "②大前提中'三盘六针'作为肯定判断的谓项不周延，但结论否定判断中'三盘六针'被周延使用，犯大项不当扩大错误；"
            "④两次提到的'智能温控系统'分别指个体型号与抽象类别，前后含义不同，使三段论实质上出现了四个项，犯四概念错误。"
            "②④虽然都不合理，但与①③不是同一规则错误。"
        ),
        "trap_type": "三段论规则错误名称错配(中项不周延 vs 大项不当扩大 vs 四概念)",
        "trigger_logic": (
            "看到三段论选择题，固定先做四步：先找中项、看中项是否至少周延一次；再核对大项小项在前提与结论的周延性是否扩大；"
            "再核对全推理只能出现三个项；最后再看肯定否定数量是否合规。本题考的是中项规则，干扰项分别引诱学生把'大项不当扩大'和'四概念'混为'中项不周延'。"
        ),
        "answer_sentence": (
            "选B；①与③的中项'大国重器''适合山地骑行'在前提中都没有周延一次，违反'中项至少周延一次'，"
            "属同一规则错误即中项不周延；②是大项不当扩大、④是四概念错误，与①③不同名。"
        ),
        "evidence_level": "B-choice-signal",
    },
    {
        "question_id": "Q-2025东城期末-14",
        "suite_id": SUITE_ID,
        "original_qno": "14",
        "answer_letter": "D",
        "answer_options": "D",
        "framework_node": "判断 / 性质判断 + 关系判断 / 谓项周延性",
        "question_stem": (
            "北京中轴线由古代皇家宫苑建筑、皇家祭祀建筑等遗址组成，是中华文明'中''和'文化传统的特殊见证。下列选项正确的是："
            "A 北京中轴线和古代皇家宫苑建筑是属种关系；"
            "B 北京中轴线位于北京老城中心，'位于'是传递关系；"
            "C 北京中轴线与中华文明中和文化传统特殊见证在外延上一致；"
            "D 统领整个老城规划格局的建筑与遗址的组合体是不周延的。"
        ),
        "material_signal": (
            "题干同时给出两个不同分类轴：性质判断(主项+联项+谓项+量项)和关系判断(对称性、传递性)。"
            "学生需要先判断每个选项考的是哪一种判断，再用对应规则核对。"
        ),
        "correct_reasoning": (
            "D是简单肯定性质判断的例子。命题'北京中轴线是统领整个老城规划格局的建筑与遗址的组合体'里，"
            "'北京中轴线'是主项，'统领整个老城规划格局的建筑与遗址的组合体'是谓项，联项是肯定的。"
            "按性质判断周延规则——肯定判断的谓项不周延——所以D正确。"
        ),
        "wrong_options": (
            "A把整体与部分关系误标为属种关系：北京中轴线是这些建筑的整体而不是它们的种概念，属种关系考的是共性与个性而非整体与部分；"
            "B'位于北京老城中心'是反对称关系而不是传递关系：A位于B不能推出B位于A，更不能像传递关系那样从'A位于B、B位于C'推出'A位于C'；"
            "C忽略一词多义：'北京中轴线'里的'中'是空间方位，'中华文明'里的'中'是民族指代，二者在外延上并不一致。"
        ),
        "trap_type": "性质判断/关系判断/概念外延 多类规则混淆 + 谓项周延性盲区",
        "trigger_logic": (
            "做这种综合判断题，要求学生先把每个选项归类：'是…'走性质判断、'位于…/属于…'走关系判断、'外延一致'走概念外延关系。"
            "性质判断只要看主项+联项+谓项+量项以及对应的周延规则；关系判断要看对称性和传递性；外延关系要逐字核对所指对象是否真正同义。"
            "本题正解出在性质判断的'肯定判断谓项不周延'这条硬规则，不能因为其他三项似是而非就放弃这条核心规则。"
        ),
        "answer_sentence": (
            "选D；'北京中轴线是统领整个老城规划格局的建筑与遗址的组合体'是简单肯定性质判断，按肯定判断谓项不周延的规则，谓项不周延。"
            "A混淆整体部分与属种关系；B把反对称关系错当传递关系；C忽略两个'中'在外延上的差异。"
        ),
        "evidence_level": "B-choice-signal",
    },
    {
        "question_id": "Q-2025东城期末-15",
        "suite_id": SUITE_ID,
        "original_qno": "15",
        "answer_letter": "B",
        "answer_options": "B",
        "framework_node": "推理 / 假言推理 / 充分条件假言推理",
        "question_stem": (
            "前提：如果赵同学参观北大红楼，那么李同学参观陈独秀旧居或者参观李大钊故居。若约定为真，必假的判断是："
            "A 只有赵同学去北大红楼，李同学才去陈独秀旧居或者去李大钊故居；"
            "B 虽然赵同学去北大红楼，但李同学既不去陈独秀旧居也不去李大钊故居；"
            "C 即使赵同学不去北大红楼，李同学也会去陈独秀旧居；"
            "D 如果李同学去李大钊故居，那么赵同学去北大红楼。"
        ),
        "material_signal": (
            "前提是'如果P那么Q'结构(P=赵去北大红楼，Q=李去陈或李大钊)，属充分条件假言判断。"
            "充分条件假言推理规则只有四条：肯前必肯后、否前不能否后、否后必否前、肯后不能肯前。"
        ),
        "correct_reasoning": (
            "B把P当真(赵去北大红楼)、把Q当假(李既不去陈也不去大钊)，相当于'肯前但否后'，"
            "直接违反'肯前必肯后'这条充分条件假言推理硬规则，所以B在前提为真时必假，故选B。"
        ),
        "wrong_options": (
            "A是必要条件假言判断'只有P才Q'，与原前提'如果P那么Q'方向不同但并不必然为假，可与原前提同时成立；"
            "C是'否前不能否后'：赵不去北大红楼时，李同学是否去陈独秀旧居原前提没有约束，所以C不必假；"
            "D是'肯后不能肯前'(李去大钊→赵去红楼)，原前提没有给这个推理保障，但不一定必假，可由其他条件成立。"
        ),
        "trap_type": "充分条件假言推理'肯前否后'否定后件型陷阱 + 必要条件假言判断'只有…才'方向干扰",
        "trigger_logic": (
            "见到'如果…那么…'要立刻识别为充分条件，背口诀：肯前肯后、否后否前；剩下两步动作(肯后、否前)都不能做。"
            "B的结构是肯前+否后，是充分条件假言推理里唯一能直接判'必假'的形式；"
            "A换成'只有…才…'容易让学生误以为反过来等价；C/D是禁推动作但'禁推'不等于必假。"
            "学生需要严格区分'必假'与'不必真'两种结论强度。"
        ),
        "answer_sentence": (
            "选B；前提是充分条件假言判断'如果P那么Q'，B出现P真而Q假，违反'肯前必肯后'，必为假；"
            "A方向变为必要条件，C是否前不能否后，D是肯后不能肯前，三者只是不能由前提推出，不能直接判为必假。"
        ),
        "evidence_level": "B-choice-signal",
    },
]


def write_choice_trap_ledger() -> Path:
    out = BATCH_DIR / "CHOICE_TRAP_LEDGER.csv"
    fieldnames = [
        "question_id",
        "suite_id",
        "original_qno",
        "answer_letter",
        "answer_options",
        "framework_node",
        "question_stem",
        "material_signal",
        "correct_reasoning",
        "wrong_options",
        "trap_type",
        "trigger_logic",
        "answer_sentence",
        "evidence_level",
    ]
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in choice_trap_rows:
            w.writerow(r)
    return out


# ---------- framework node matrix ----------

framework_rows = [
    {
        "framework_node": "创新思维 / 联想思维",
        "question_id": "Q-2025东城期末-18-2",
        "mount_role": "正例(主观题)",
        "evidence_level": "A-formal",
        "rubric_position": "S-2025东城期末第18(2)题第二层次具体方法第一点",
        "note": "登月服飞天飘带+火箭尾焰+中华传统文化的造型联系是联想思维的标志性材料动作。",
    },
    {
        "framework_node": "创新思维 / 发散思维与聚合思维",
        "question_id": "Q-2025东城期末-18-2",
        "mount_role": "正例(主观题)",
        "evidence_level": "A-formal",
        "rubric_position": "S-2025东城期末第18(2)题第二层次具体方法第二点",
        "note": "围绕登月任务核心问题先发散到月面环境/航天员行走/科考再聚合为一套设计方案。",
    },
    {
        "framework_node": "创新思维 / 超前思维",
        "question_id": "Q-2025东城期末-18-2",
        "mount_role": "正例(主观题)",
        "evidence_level": "A-formal",
        "rubric_position": "S-2025东城期末第18(2)题第二层次具体方法第三点",
        "note": "提前预判月面热环境、月尘和航天员登陆后需求，据此设计细节，是超前思维。",
    },
    {
        "framework_node": "创新思维 / 创新思维表现(思路新方法新结果新)",
        "question_id": "Q-2025东城期末-18-2",
        "mount_role": "正例(主观题)",
        "evidence_level": "A-formal",
        "rubric_position": "S-2025东城期末第18(2)题第一层次表现/特点",
        "note": "细则明示思路新方法新结果新或多向性跨越性独特性，写一个词得1分。",
    },
    {
        "framework_node": "辩证思维 / 整体性",
        "question_id": "Q-2025东城期末-5",
        "mount_role": "正例(选择题)",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第5题正确项②前半",
        "note": "社区公园改造把入口、绿地、通行、休闲体验作为一个有机整体一起考量。",
    },
    {
        "framework_node": "辩证思维 / 动态性",
        "question_id": "Q-2025东城期末-5",
        "mount_role": "正例(选择题)",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第5题正确项②后半",
        "note": "改造体现以变化和发展的视角认识并优化社区环境。",
    },
    {
        "framework_node": "辩证思维 / 矛盾分析法",
        "question_id": "Q-2025东城期末-5",
        "mount_role": "正例(选择题)",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第5题正确项④",
        "note": "原入口窄与通行需要的对立通过把直角变圆角化解，是矛盾分析法。",
    },
    {
        "framework_node": "辩证思维 / 边界陷阱-必修四联系观",
        "question_id": "Q-2025东城期末-5",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第5题干扰项①",
        "note": "把'人为事物联系'误说成'自在联系'，必修四联系观跨模块陷阱。",
    },
    {
        "framework_node": "辩证思维 / 边界陷阱-必修四辩证否定观",
        "question_id": "Q-2025东城期末-5",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第5题干扰项③",
        "note": "把辩证否定误说成简单的'否定过去肯定现在'，必修四辩证否定观跨模块陷阱。",
    },
    {
        "framework_node": "推理 / 三段论 / 中项不周延",
        "question_id": "Q-2025东城期末-13",
        "mount_role": "正例(选择题)",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第13题正确项①③",
        "note": "①'大国重器'与③'适合山地骑行'两次出现都不周延，违反'中项至少周延一次'。",
    },
    {
        "framework_node": "推理 / 三段论 / 大项不当扩大",
        "question_id": "Q-2025东城期末-13",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第13题干扰项②",
        "note": "②'三盘六针'作肯定判断谓项不周延，结论否定判断里被周延使用，犯大项不当扩大。",
    },
    {
        "framework_node": "推理 / 三段论 / 四概念",
        "question_id": "Q-2025东城期末-13",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第13题干扰项④",
        "note": "④'智能温控系统'前后所指不同，实际出现四个项，犯四概念错误。",
    },
    {
        "framework_node": "判断 / 性质判断 / 谓项周延性",
        "question_id": "Q-2025东城期末-14",
        "mount_role": "正例(选择题)",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第14题正确项D",
        "note": "简单肯定性质判断的谓项不周延这条硬规则的直接考点。",
    },
    {
        "framework_node": "判断 / 关系判断 / 反对称关系",
        "question_id": "Q-2025东城期末-14",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第14题干扰项B",
        "note": "把'位于'反对称关系误标为传递关系。",
    },
    {
        "framework_node": "判断 / 概念 / 属种关系 vs 整体部分关系",
        "question_id": "Q-2025东城期末-14",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第14题干扰项A",
        "note": "把整体与部分关系误标为属种关系。",
    },
    {
        "framework_node": "判断 / 概念 / 外延一致性",
        "question_id": "Q-2025东城期末-14",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第14题干扰项C",
        "note": "两个'中'语义不同，外延并不一致。",
    },
    {
        "framework_node": "推理 / 假言推理 / 充分条件假言推理",
        "question_id": "Q-2025东城期末-15",
        "mount_role": "正例(选择题)",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第15题正确项B",
        "note": "肯前+否后必为假，是充分条件假言推理'肯前必肯后'规则的直接反例。",
    },
    {
        "framework_node": "推理 / 假言推理 / 必要条件假言判断方向干扰",
        "question_id": "Q-2025东城期末-15",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第15题干扰项A",
        "note": "'只有…才…'是必要条件假言判断，与原前提充分条件不矛盾，不必假。",
    },
    {
        "framework_node": "推理 / 假言推理 / 否前禁推 vs 肯后禁推",
        "question_id": "Q-2025东城期末-15",
        "mount_role": "选择题陷阱",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第15题干扰项C/D",
        "note": "C是'否前不能否后'、D是'肯后不能肯前'；禁推动作不必导致必假。",
    },
    {
        "framework_node": "综合短文 / 中国式现代化民生为大",
        "question_id": "Q-2025东城期末-21",
        "mount_role": "同类索引(综合短文)",
        "evidence_level": "B-choice-signal",
        "rubric_position": "S-2025东城期末第21题综合运用所学",
        "note": "细则按知识运用方面数等级给分，不限选必三；可作为综合短文的同类索引提示，不入选必三主链正文。",
    },
]


def write_framework_node_matrix() -> Path:
    out = BATCH_DIR / "FRAMEWORK_NODE_MATRIX.csv"
    fieldnames = [
        "framework_node",
        "question_id",
        "suite_id",
        "mount_role",
        "evidence_level",
        "rubric_position",
        "note",
    ]
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in framework_rows:
            w.writerow({
                "framework_node": r["framework_node"],
                "question_id": r["question_id"],
                "suite_id": SUITE_ID,
                "mount_role": r["mount_role"],
                "evidence_level": r["evidence_level"],
                "rubric_position": r["rubric_position"],
                "note": r["note"],
            })
    return out


def write_framework_node_summary() -> Path:
    out = BATCH_DIR / "FRAMEWORK_NODE_MATRIX_SUMMARY.csv"
    fieldnames = [
        "framework_node",
        "total_mounts",
        "primary_examples",
        "trap_examples",
        "auxiliary_examples",
    ]
    bucket: dict[str, dict[str, list[str]]] = {}
    for r in framework_rows:
        node = r["framework_node"]
        slot = bucket.setdefault(node, {"primary": [], "trap": [], "auxiliary": []})
        if "正例" in r["mount_role"]:
            slot["primary"].append(r["question_id"])
        elif "陷阱" in r["mount_role"]:
            slot["trap"].append(r["question_id"])
        else:
            slot["auxiliary"].append(r["question_id"])
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for node, slot in bucket.items():
            w.writerow({
                "framework_node": node,
                "total_mounts": len(slot["primary"]) + len(slot["trap"]) + len(slot["auxiliary"]),
                "primary_examples": "; ".join(slot["primary"]),
                "trap_examples": "; ".join(slot["trap"]),
                "auxiliary_examples": "; ".join(slot["auxiliary"]),
            })
    return out


# ---------- entries.jsonl ----------

def write_entries_jsonl() -> Path:
    out = BATCH_DIR / "entries" / "batch03a_entries.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []
    # subjective body entries
    for r in main_thinking_rows:
        rows.append({
            "question_id": r["question_id"],
            "type": "main",
            "framework_node": r["framework_node"],
            "material_signal": r["material_signal"],
            "trigger_logic": r["trigger_logic"],
            "answer_sentence": r["answer_sentence"],
            "evidence_level": r["evidence_level"],
            "needs_codex_recheck": "yes",
            "source_batch": SOURCE_BATCH,
        })
    # choice trap entries
    for r in choice_trap_rows:
        rows.append({
            "question_id": r["question_id"],
            "type": "choice",
            "framework_node": r["framework_node"],
            "material_signal": r["material_signal"],
            "trigger_logic": r["trigger_logic"],
            "answer_sentence": r["answer_sentence"],
            "evidence_level": r["evidence_level"],
            "needs_codex_recheck": "yes",
            "source_batch": SOURCE_BATCH,
        })
    with out.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return out


# ---------- BLOCKED_OR_BOUNDARY.md ----------

def write_blocked_or_boundary() -> Path:
    out = BATCH_DIR / "BLOCKED_OR_BOUNDARY.md"
    excluded = [d for d in decisions if d["claudecode_decision"] == "excluded"]
    same_index = [d for d in decisions if d["claudecode_decision"] == "同类索引"]
    blocked = [d for d in decisions if d["claudecode_decision"] == "blocked"]
    text_lines: list[str] = []
    text_lines.append("# Batch03a S-2025东城期末 边界与不入正文记录")
    text_lines.append("")
    text_lines.append("本文件记录所有未进入选必三思维主链正文的题目原因。共 24 个 unique question_id，")
    text_lines.append("入正文 5（Q5/Q13/Q14/Q15/Q18-2），同类索引 1（Q21），blocked 0，excluded 18。")
    text_lines.append("")
    text_lines.append("## blocked（无）")
    text_lines.append("")
    if blocked:
        for d in blocked:
            text_lines.append(f"- `{d['question_id']}` — {d['decision_reason']}")
    else:
        text_lines.append("无 blocker：试卷PDF（教师版）、参考答案、东城期末细则PPTX三套源齐全；")
        text_lines.append("选择题选项完整、客观答案与教师版解析一致；主观题细则与参考答案一致；")
        text_lines.append("无 OCR/视觉信息缺失。")
    text_lines.append("")
    text_lines.append("## 同类索引（保留作综合短文同类索引提示，不入选必三主链正文）")
    text_lines.append("")
    for d in same_index:
        text_lines.append(f"- `{d['question_id']}`（{d['original_qno']}） — {d['decision_reason']}")
    text_lines.append("")
    text_lines.append("## excluded（按模块边界划归其他模块，不入选必三思维主链）")
    text_lines.append("")
    for d in excluded:
        text_lines.append(f"- `{d['question_id']}`（{d['original_qno']}） — {d['decision_reason']}")
    text_lines.append("")
    text_lines.append("## 边界说明")
    text_lines.append("")
    text_lines.append("- Q1/Q2 属必修一中国特色社会主义中特理论体系。")
    text_lines.append("- Q3/Q4/Q16 属必修四文化与哲学（含矛盾观、文化的功能、中华文化源远流长博大精深、意识能动作用）。")
    text_lines.append("- Q6 属必修三政治与法治（推进科学民主立法）。")
    text_lines.append("- Q7/Q8/Q18(1) 属必修二经济与社会（宏观调控、对外开放、新型举国体制等）。")
    text_lines.append("- Q9/Q10/Q20 属选必一国际政治与经济（金砖、联合国、反补贴税）。")
    text_lines.append("- Q11/Q12/Q19(1)/Q19(3) 属选必二法律与生活（数据知识产权、民法典、相邻关系）。")
    text_lines.append("- Q17/Q19(2)/Q19(3) 含必修三政治与法治、基层群众自治、民主协商。")
    text_lines.append("- Q21 是综合运用所学的开放性短文，不限定选必三知识范围。")
    out.write_text("\n".join(text_lines), encoding="utf-8")
    return out


# ---------- suite_reports/S-2025东城期末.md ----------

def write_suite_report() -> Path:
    out = BATCH_DIR / "suite_reports" / f"{SUITE_ID}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter(d["claudecode_decision"] for d in decisions)
    lines: list[str] = []
    lines.append(f"# Suite Report — {SUITE_ID}")
    lines.append("")
    lines.append("## 套卷源")
    lines.append("")
    lines.append("- 试卷：`C:/Users/Administrator/Desktop/2025各区模拟题/2025各区期末/2025东城期末/试卷/2025北京东城高三（上）期末政治（教师版）.pdf`（20 页，含试卷+参考答案+点评）。")
    lines.append("- 评分细则：`C:/Users/Administrator/Desktop/2025各区模拟题/2025各区期末/2025东城期末/细则/2025东城期末细则.pptx`（34 张 slide，含 Q17/Q18(2)/Q19(1-3)/Q20/Q21 阅卷细则）。")
    lines.append("- 其他材料：`C:/Users/Administrator/Desktop/2025各区模拟题/2025各区期末/2025东城期末/其他材料/2025。1东城讲评 修改.pdf`（讲评 PDF，备查）。")
    lines.append("")
    lines.append("## 候选闭合统计")
    lines.append("")
    lines.append(f"- unique question_id 数：{len(decisions)}")
    lines.append(f"- 入正文：{counts.get('入正文', 0)}")
    lines.append(f"- 同类索引：{counts.get('同类索引', 0)}")
    lines.append(f"- blocked：{counts.get('blocked', 0)}")
    lines.append(f"- excluded：{counts.get('excluded', 0)}")
    lines.append("")
    lines.append("## 入正文条目")
    lines.append("")
    for d in decisions:
        if d["claudecode_decision"] != "入正文":
            continue
        lines.append(f"### {d['question_id']}（{d['question_type']}/第{d['original_qno']}题）")
        lines.append("")
        if d["question_type"] == "主观题":
            mt = next(r for r in main_thinking_rows if r["question_id"] == d["question_id"])
            lines.append(f"- 完整设问：{mt['full_question']}")
            lines.append(f"- 细则位置：{mt['rubric_position']}")
            lines.append(f"- 总帽子：{mt['total_hat']}")
            lines.append(f"- 小方法：{mt['small_method']}")
            lines.append(f"- 材料动作：{mt['material_signal']}")
            lines.append(f"- 触发逻辑：{mt['trigger_logic']}")
            lines.append(f"- 答案句：{mt['answer_sentence']}")
            lines.append(f"- 框架落点：{mt['framework_node']}")
            lines.append(f"- 题型标签：{mt['question_family']}")
            lines.append(f"- 证据等级：{mt['evidence_level']}")
        else:
            ct = next(r for r in choice_trap_rows if r["question_id"] == d["question_id"])
            lines.append(f"- 客观答案：{ct['answer_letter']}（{ct['answer_options']}）")
            lines.append(f"- 题干：{ct['question_stem']}")
            lines.append(f"- 材料/题干信号：{ct['material_signal']}")
            lines.append(f"- 正确项理由：{ct['correct_reasoning']}")
            lines.append(f"- 错项陷阱：{ct['wrong_options']}")
            lines.append(f"- 陷阱类型：{ct['trap_type']}")
            lines.append(f"- 触发逻辑：{ct['trigger_logic']}")
            lines.append(f"- 答案句：{ct['answer_sentence']}")
            lines.append(f"- 框架落点：{ct['framework_node']}")
            lines.append(f"- 证据等级：{ct['evidence_level']}")
        lines.append("")
    lines.append("## 同类索引条目")
    lines.append("")
    for d in decisions:
        if d["claudecode_decision"] != "同类索引":
            continue
        lines.append(f"- `{d['question_id']}`（第{d['original_qno']}题）— {d['decision_reason']}")
    lines.append("")
    lines.append("## 外推与硬样本结论")
    lines.append("")
    lines.append("- 创新思维硬样本配对：Q-2025东城期末-18-2 与 SKILL Trial Before Full Run 中的 `2026朝阳期中 Q21(2)`、`2026东城一模 Q19(4)` 形成创新思维三新+具体方法（联想/发散+聚合/超前）配对。")
    lines.append("- 辩证思维硬样本配对：Q-2025东城期末-5 在选择题口径上与 `2025海淀二模 Q20`（辩证思维复合主观题）形成同一类型互补；本套是选择题型，主观题需保留主观题口径。")
    lines.append("- 推理硬样本配对：Q-2025东城期末-13 与 `2024朝阳二模7`（小项不当扩大硬样本）、`2025顺义一模7`（大项不当扩大硬样本）形成三段论规则错误三人组（中项不周延 / 大项不当扩大 / 小项不当扩大）。")
    lines.append("- 推理硬样本配对：Q-2025东城期末-14 与必要条件 vs 充分条件假言判断、关系判断对称性硬样本群形成判断章覆盖。")
    lines.append("- 推理硬样本配对：Q-2025东城期末-15 与 `2024朝阳一模20(1)`、`2025西城二模16(2)`、`2026通州期末19(2)` 共同构成充分条件假言推理 vs 必要条件假言推理选择题陷阱集合。")
    lines.append("")
    lines.append("## 残余边界")
    lines.append("")
    lines.append("- Q21 综合短文按 BLOCKED_OR_BOUNDARY.md 同类索引保留，不强行下挂选必三主链。")
    lines.append("- 18 道 excluded 题已按模块边界归类，未来若 Codex 重新核源发现新角度，再按 needs_codex_recheck=no 转 yes 处理。")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> None:
    paths = [
        write_question_decisions(),
        write_main_thinking_ledger(),
        write_choice_trap_ledger(),
        write_framework_node_matrix(),
        write_framework_node_summary(),
        write_blocked_or_boundary(),
        write_suite_report(),
        write_entries_jsonl(),
    ]
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
