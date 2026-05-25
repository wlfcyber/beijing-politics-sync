from __future__ import annotations

import csv
import importlib.util
import json
import re
import shutil
import tempfile
import zipfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from lxml import etree


CORE_PATH = Path(__file__).with_name("batch29_2026_chaoyang_midterm_apply_20260525.py")
spec = importlib.util.spec_from_file_location("batch29_core", CORE_PATH)
core = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(core)

W = core.W
NS = core.NS

ROOT = core.ROOT
RECOVERY = core.RECOVERY
RUN = core.RUN
DELIVERY = core.DELIVERY
MATRIX = core.MATRIX
LEDGER = core.LEDGER
ACCEPTED = core.ACCEPTED
GLOBAL_AUDIT_CSV = core.GLOBAL_AUDIT_CSV
GLOBAL_AUDIT_MD = core.GLOBAL_AUDIT_MD
FORMAT_QA = core.FORMAT_QA
THREAD_STATUS = core.THREAD_STATUS
GOVERNOR = core.GOVERNOR
CONFUCIUS = core.CONFUCIUS
MODEL_LEDGER = core.MODEL_LEDGER

PREPROCESSED = ROOT / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2026各区模拟题__2026各区期末和期中__2026海淀期末.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "7832041a93d37e1f_2026海淀期末细则.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "ac3124113aec7062_2026北京海淀高三_上_期末政治_教师版.md"
RUBRIC_OCR_TEXT = RECOVERY / "BATCH32_2026_HAIDIAN_FINAL_RUBRIC_OCR_TRANSCRIPTION_20260525.md"
RUBRIC_OCR_LINES = RECOVERY / "BATCH32_2026_HAIDIAN_FINAL_RUBRIC_OCR_LINES_20260525.md"
TEACHER_OCR_TEXT = RECOVERY / "BATCH32_2026_HAIDIAN_FINAL_TEACHER_OCR_TRANSCRIPTION_20260525.md"
TEACHER_OCR_LINES = RECOVERY / "BATCH32_2026_HAIDIAN_FINAL_TEACHER_OCR_LINES_20260525.md"
SOURCE_RENDER_MANIFEST = RECOVERY / "BATCH32_2026_HAIDIAN_FINAL_SOURCE_RENDER_MANIFEST.json"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH32_2026_HAIDIAN_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH32_2026_HAIDIAN_FINAL_CODEX_20260525.md"

SUITE = "2026海淀期末"
YEAR = "2026"
STAGE = "期末"
BATCH_ID = "batch32_2026_haidian_final"
MATRIX_SOURCE = "codex_batch32_2026_haidian_final"
EXPECTED_ENTRIES = 22
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; "
    f"rubric OCR: {RUBRIC_OCR_TEXT}; rubric lines: {RUBRIC_OCR_LINES}; "
    f"teacher OCR: {TEACHER_OCR_TEXT}; teacher lines: {TEACHER_OCR_LINES}; "
    f"source render manifest: {SOURCE_RENDER_MANIFEST}; "
    "teacher PDF text page 9 answer key: 1B,2A,3A,4C,5D,6C,7D,8A,9D,10B,11B,12C,13C,14B,15D; "
    "rubric OCR pages 1-2 formal Q16-Q17 scoring; rubric OCR page 6 formal Q21 scoring."
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q1",
        "question_label": "第1题（选择题）",
        "material_trigger": "教师版第1题以圭表测日影、定节气、规划疆域为材料，答案键为1B；正确项包含圭表的应用服务于社会实践并受历史条件制约。",
        "question_prompt": "由圭表从计时工具到规划疆域工具的发展，判断技术工具与社会实践、历史条件的关系。",
        "why_trigger": "题肢把工具应用、社会实践和历史条件放在同一条判断链中，能客观挂到实践与认识关系；但它只是选择题答案键证据，不扩展为主观评分细则。",
        "answer_landing": "计时和测量工具在社会实践需要中被使用、发展和赋义，认识工具及其应用要服务实践，也受特定历史条件制约。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q2",
        "question_label": "第2题（选择题）",
        "material_trigger": "教师版第2题以“邹忌照镜”为材料，答案键为2A；正确项强调坚持全面的观点，既重视他人评价又不盲从。",
        "question_prompt": "从他人评价、自我认识和不同动机之间的关系中得到党员干部自我审视的启示。",
        "why_trigger": "正确项的“全面的观点”属于辩证看问题的客观选择题挂点；不把政治本色等非哲学项另造为哲学正文。",
        "answer_landing": "看待评价和自我认识要坚持全面观点，既看到他人评价的参考意义，也看到评价背后的动机和条件，避免片面盲从。",
    },
    {
        "canonical_node": "认识发展原理",
        "question_no": "Q3",
        "question_label": "第3题（选择题）",
        "material_trigger": "教师版第3题以具身智能机器人分析京剧经典为材料，答案键为3A；正确项说其作为新型研究工具，能深化人们对表演规律的认识。",
        "question_prompt": "判断人工智能研究工具在戏剧研究中对认识深化的作用。",
        "why_trigger": "正确项把新型工具和认识深化连接起来，同时排除了“成为创作主体”“根本动力”等错误表述，适合作为认识发展节点的客观选择题挂点。",
        "answer_landing": "新工具可以扩展材料处理和分析能力，帮助人们发现新的艺术特征、深化对规律的认识，但认识主体仍然是人。",
    },
    {
        "canonical_node": "实践是认识的基础",
        "question_no": "Q4",
        "question_label": "第4题（选择题）",
        "material_trigger": "教师版第4题说新时代人文经济学以我国人文经济实践为现实基础，答案键为4C；正确项包含文化繁荣与经济发展统一于中国式现代化实践。",
        "question_prompt": "判断新时代人文经济学与中国式现代化实践、人民福祉之间的关系。",
        "why_trigger": "题干和正确项都把理论研究放回现实实践和中国式现代化实践中理解，能客观挂到实践是认识的基础；人民福祉等政治经济表述不另造哲学条。",
        "answer_landing": "理论创新来自实践、服务实践。新时代人文经济学要在中国式现代化实践中把文化繁荣和经济发展统一起来。",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式评分标准page_001写明Q16“可从矛盾的观点、意识的能动作用、实践的观点等角度作答”，细则中矛盾观为“一分为二、两重统一”。",
        "question_prompt": "结合材料或个人体验，从哲学角度谈谈“数字原住民”应如何与技术进步相伴成长。",
        "why_trigger": "材料同时呈现网络技术红利和负面影响，要求学生把技术进步的积极作用与依赖、惰化、表达弱化等风险统一起来分析。",
        "answer_landing": "看待技术进步要坚持一分为二，既看到网络与智能工具提供资源和便利，也看到沉溺、依赖、思维惰化等风险，在对立统一中作出合理使用。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式评分标准page_001将“意识的能动作用”列为Q16可用角度，并在细则中把“主观能动性”放入行动角度。",
        "question_prompt": "结合材料或个人体验，从哲学角度谈谈“数字原住民”应如何与技术进步相伴成长。",
        "why_trigger": "材料不是让学生被动接受技术，而是要求提高警惕、主动选择、培养独立思考和深度表达能力。",
        "answer_landing": "数字原住民要发挥意识的能动作用，主动识别算法诱导和信息工具局限，把技术作为辅助工具，而不是让工具替代判断和思考。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式评分标准page_001把“实践的观点”列入Q16可用角度，并要求结合材料或个人体验作答。",
        "question_prompt": "结合材料或个人体验，从哲学角度谈谈“数字原住民”应如何与技术进步相伴成长。",
        "why_trigger": "设问要求从个人体验出发，说明在真实学习、表达、探索和使用技术的实践中形成合理认识和行动方式。",
        "answer_landing": "对技术的认识和使用能力要在实践中形成并检验，学生应在学习、表达和问题解决实践中训练独立探索，而不是停留在复制粘贴和即时答案上。",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式评分标准page_001写明“价值观具有导向作用，正确价值观具有促进作用，应树立正确价值观”。",
        "question_prompt": "结合材料或个人体验，从哲学角度谈谈“数字原住民”应如何与技术进步相伴成长。",
        "why_trigger": "如何使用技术本质上包含价值取向问题：是把技术作为服务成长的工具，还是让技术支配注意力、表达和判断。",
        "answer_landing": "正确价值观能够引导技术使用方向。面对数字化世界，要坚持以人的成长和真实能力提升为导向，让技术服务于人的全面发展。",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式评分标准page_001在“知”的角度列出“价值观、价值判断价值选择等”。",
        "question_prompt": "结合材料或个人体验，从哲学角度谈谈“数字原住民”应如何与技术进步相伴成长。",
        "why_trigger": "数字原住民要在海量信息、算法刺激、便捷工具和真实成长之间作出选择，题目要求把选择标准说清楚。",
        "answer_landing": "面对技术诱惑和便利，要作出正确价值判断和价值选择，把独立思考、真实表达和能力成长置于短时刺激与机械依赖之上。",
    },
    {
        "canonical_node": "实现人生价值",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式评分标准page_001在行动角度列出“实践、主观能动性、实现人生价值”。",
        "question_prompt": "结合材料或个人体验，从哲学角度谈谈“数字原住民”应如何与技术进步相伴成长。",
        "why_trigger": "题目问“相伴成长”，不是单纯评价技术利弊，而是要求把技术使用落到人的能力发展和成长路径上。",
        "answer_landing": "数字原住民应在正确使用技术、发展思考能力和参与真实实践中促进自身成长，把技术红利转化为实现人生价值的条件。",
    },
    {
        "canonical_node": "矛盾的普遍性和特殊性",
        "question_no": "Q17",
        "question_label": "第17题（主观题）",
        "material_trigger": "正式评分标准page_002在Q17“红色文化的内涵”维度列出“矛盾的普遍性和特殊性的辩证关系”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，说明红色文化为何能“圈粉”年轻人。",
        "why_trigger": "红色文化既承载中华民族精神、革命文化的一般价值，又在井冈山、遵义、延安等具体场景中呈现特殊表达。",
        "answer_landing": "红色文化把共同精神价值与具体历史场景、时代传播方式结合起来，在普遍性与特殊性的统一中增强年轻人的认同。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q17",
        "question_label": "第17题（主观题）",
        "material_trigger": "正式评分标准page_002在Q17“红色文化的内涵”维度列出“意识的能动作用/认识的作用/价值观的导向作用”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，说明红色文化为何能“圈粉”年轻人。",
        "why_trigger": "红色文化不是静态陈列，而是通过体验、数字艺术、青年讲解等方式影响认识、激发精神力量。",
        "answer_landing": "红色文化能够通过精神感召和意义阐释发挥意识的能动作用，激励青年理解历史、坚定理想并主动参与实践。",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q17",
        "question_label": "第17题（主观题）",
        "material_trigger": "正式评分标准page_002在Q17哲学知识栏列出“价值观的导向作用”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，说明红色文化为何能“圈粉”年轻人。",
        "why_trigger": "材料中的红军生活体验、长征数字呈现、延安精神讲解都在引导青年理解奋斗、信仰和责任。",
        "answer_landing": "红色文化承载正确价值导向，能够引导年轻人形成理想信念、责任意识和奋斗方向。",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q17",
        "question_label": "第17题（主观题）",
        "material_trigger": "正式评分标准page_002在Q17“红色文化的发展”维度列出“发展的观点/联系的观点”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，说明红色文化为何能“圈粉”年轻人。",
        "why_trigger": "红色文化通过数字艺术馆、青年讲解视频等新形式不断发展，不是停留在旧有展示方式。",
        "answer_landing": "红色文化要在时代发展中创新表达，通过数字技术、沉浸体验和青年化叙事焕发生机。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q17",
        "question_label": "第17题（主观题）",
        "material_trigger": "正式评分标准page_002在Q17“红色文化的发展”维度列出“发展的观点/联系的观点”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，说明红色文化为何能“圈粉”年轻人。",
        "why_trigger": "材料把历史遗址、数字技术、青年实践、讲解传播和现实成长联系起来，说明红色文化吸引力来自多要素联动。",
        "answer_landing": "推动红色文化传播要坚持联系观点，联通历史资源、技术媒介、青年生活和时代需求，让红色文化进入真实生活。",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q17",
        "question_label": "第17题（主观题）",
        "material_trigger": "正式评分标准page_002在“红色文化滋养年轻人”维度写明，有助于年轻人形成正确价值观、明确价值选择和价值判断的标准。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，说明红色文化为何能“圈粉”年轻人。",
        "why_trigger": "红色文化能帮助青年在历史记忆和时代生活之间建立判断标准，明确什么值得追求、应如何行动。",
        "answer_landing": "红色文化能够为青年提供正确的价值判断和价值选择标准，使青年在理解历史和现实责任中选择奋斗方向。",
    },
    {
        "canonical_node": "认识对实践的反作用",
        "question_no": "Q17",
        "question_label": "第17题（主观题）",
        "material_trigger": "正式评分标准page_002写明“正确的认识有助于推动年轻人积极投身于实践”。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，说明红色文化为何能“圈粉”年轻人。",
        "why_trigger": "材料中的体验活动、实践小组和讲解视频表明，青年对红色文化的理解会进一步转化为实践参与。",
        "answer_landing": "正确认识对实践具有反作用。青年理解红色文化的精神内涵和时代价值后，更能主动参与传承、传播和社会实践。",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式评分标准page_006写明Q21可从“矛盾的观点”作答，并要求运用对立统一观点分析“活力与秩序”的关系。",
        "question_prompt": "综合运用所学，谈谈对“中国式现代化应当而且能够实现活而不乱、活跃有序的动态平衡”的理解。",
        "why_trigger": "设问核心就是活力与秩序的关系，要求说明二者既对立又统一，不能只强调活力或只强调秩序。",
        "answer_landing": "活力与秩序是对立统一的关系。中国式现代化既要释放发展活力，也要维护社会秩序，在动态平衡中推进现代化。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式评分标准page_006在“以人民为中心”角度写明人民群众是历史的主体，坚持群众观点、群众路线，把人民利益作为最高出发点和落脚点。",
        "question_prompt": "综合运用所学，谈谈对“中国式现代化应当而且能够实现活而不乱、活跃有序的动态平衡”的理解。",
        "why_trigger": "材料强调中国共产党领导人民创造经济快速发展和社会长期稳定两大奇迹，评分细则把以人民为中心和人民群众主体地位列为可用知识。",
        "answer_landing": "人民群众是历史的主体。中国式现代化要为了人民、依靠人民、成果由人民共享，在群众观点和群众路线中实现活力有序释放。",
    },
]


BOUNDARY_ROWS = [
    ("Q5", "文化选择题", "文化传承/文化自信", "教师版答案键5D；题面为文博会、数字技术与文化传播，属于文化模块，不进入当前哲学正文节点。", "教师版答案键+题面", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q6", "法律选择题", "商业秘密/侵权责任", "教师版答案键6C；考查法律与生活中的商业秘密保护和侵权责任，不进入必修四哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH32_HAIDIAN_FINAL"),
    ("Q7", "法律选择题", "侵权责任/诉讼", "教师版答案键7D；交通事故责任与民事侵权问题，非必修四哲学落点。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH32_HAIDIAN_FINAL"),
    ("Q8", "法律选择题", "婚姻登记/行政服务/个人信息", "教师版答案键8A；婚姻登记条例与法律程序问题，边界排除。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH32_HAIDIAN_FINAL"),
    ("Q9", "法律选择题", "劳动合同/劳动争议", "教师版答案键9D；企业用工、劳动合同和劳动争议，边界排除。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH32_HAIDIAN_FINAL"),
    ("Q10", "法律选择题", "诚信原则/市场规则", "教师版答案键10B；诚信表述处在消费者权益和市场规则法治语境中，不转写为价值观正文条。", "教师版答案键+题面", "LEGAL_VALUE_WORDING_BOUNDARY_NO_PHILOSOPHY_BODY"),
    ("Q11", "逻辑与思维选择题", "判断谓项周延", "教师版答案键11B；考查形式逻辑判断，不进入必修四哲学正文。", "教师版答案键+题面", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q12", "逻辑与思维选择题", "三段论推理", "教师版答案键12C；三段论推理规则属于逻辑与思维边界，排除。", "教师版答案键+题面", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q13", "逻辑与思维选择题", "研究方法/归纳推理", "教师版答案键13C；考查探究方案与推理方法，排除。", "教师版答案键+题面", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q14", "逻辑与思维选择题", "归纳结论/具体条件", "教师版答案键14B；研究结论不具备必然性属于逻辑思维与科学思维判断，不进入哲学正文。", "教师版答案键+题面", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q15", "逻辑与思维/公共服务选择题", "综合思维/问题导向", "教师版答案键15D；正确项含公共服务精准对接和综合思维方法，归入选必三逻辑与思维边界，不进必修四哲学正文。", "教师版答案键+题面", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q16-substitute-only", "主观题替代性哲学点", "联系观/发展观/适度原则", "正式评分标准page_001说明如果用联系观、发展观、适度原则等其他知识点，仅替代1分；本批不把替代1分项扩写为独立正文条。", "正式评分标准", "SUBSTITUTE_ONLY_NO_BODY_ROW"),
    ("Q17-culture", "主观题文化点", "民族精神/革命文化/中国特色社会主义文化/文化自信", "正式评分标准page_002列出大量文化知识；本批仅登记哲学节点，文化知识留在模块边界，不冒充哲学原理。", "正式评分标准", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q18(1)", "法律与生活主观题", "格式条款/公平原则", "正式评分标准page_002限定格式条款、合同效力和公平原则，属于法律与生活，不进入必修四哲学正文。", "正式评分标准", "MODULE_BOUNDARY_EXCLUDED_BATCH32_HAIDIAN_FINAL"),
    ("Q18(2)", "法治主观题", "合同示范文本/诚信价值观/法治政府", "正式评分标准page_002-page_003为住房租赁条例现实意义，诚信和价值观表述处在法治与市场秩序语境中，不转写为哲学正文。", "正式评分标准", "LEGAL_VALUE_WORDING_BOUNDARY_NO_PHILOSOPHY_BODY"),
    ("Q19", "法律与生活主观题", "反不正当竞争/商业道德/社会主义核心价值观", "正式评分标准page_003-page_004限定反不正当竞争法、客观行为和后果；价值维度是法律评价维度，不转写为必修四价值观节点。", "正式评分标准", "MODULE_BOUNDARY_EXCLUDED_BATCH32_HAIDIAN_FINAL"),
    ("Q20(1)", "逻辑与思维主观题", "充分条件假言推理", "正式评分标准page_004为充分条件假言推理类型和有效/无效式判断，属于选必三逻辑边界。", "正式评分标准", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q20(2)", "逻辑与思维主观题", "超前思维/调查研究/矛盾分析方法/推理和想象", "正式评分标准page_005限定超前思维方法；其中矛盾分析方法作为选必三方法项出现，不作为必修四正文条。", "正式评分标准", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q21-nonphilosophy", "综合主观题非哲学点", "党的领导/制度优势/人民当家作主/法治/统筹发展与安全", "正式评分标准page_006允许党的领导、制度优势等多模块作答；本批只登记对立统一和人民群众两项必修四支持点。", "正式评分标准", "NON_PHILOSOPHY_POINTS_BOUNDARY_EXCLUDED_BATCH32_HAIDIAN_FINAL"),
    ("Q21-substitute-only", "主观题替代性哲学点", "联系观/辩证思维", "正式评分标准page_006说明联系观、辩证思维可替代分析活力与秩序关系1分；本批保留为替代项边界，不扩写为正文条。", "正式评分标准", "SUBSTITUTE_ONLY_NO_BODY_ROW"),
]


EVIDENCE_BY_KEY = {
    ("Q1", "实践与认识（总）"): (
        "教师版第1题答案键1B；题面和正确项包含圭表应用服务于社会实践并受历史条件制约，仅作客观选择题挂点。",
        "objective-choice-only-teacher-answer-key",
    ),
    ("Q2", "联系的普遍性 / 联系的观点（总）"): (
        "教师版第2题答案键2A；正确项含“坚持全面的观点，既重视他人评价又不盲从”，仅作客观选择题挂点。",
        "objective-choice-only-teacher-answer-key",
    ),
    ("Q3", "认识发展原理"): (
        "教师版第3题答案键3A；正确项说明具身智能机器人作为新型研究工具能深化人们对表演规律的认识，仅作客观选择题挂点。",
        "objective-choice-only-teacher-answer-key",
    ),
    ("Q4", "实践是认识的基础"): (
        "教师版第4题答案键4C；题干与正确项把新时代人文经济学置于我国人文经济实践和中国式现代化实践中理解，仅作客观选择题挂点。",
        "objective-choice-only-teacher-answer-key",
    ),
    ("Q16", "矛盾就是对立统一"): (
        "正式评分标准page_001 Q16列明“矛盾的观点”，细则写“一分为二、两重统一”。",
        "formal-rubric",
    ),
    ("Q16", "两点论与重点论"): (
        "正式评分标准page_001 Q16矛盾观细则写“一分为二、两重统一”，并提示“重点论”出不来只能1分，支持两点论与重点论的宽口径登记。",
        "formal-rubric-broad-angle",
    ),
    ("Q16", "主观能动性 / 意识的能动作用"): (
        "正式评分标准page_001 Q16列明“意识的能动作用”，并在行动角度列出主观能动性。",
        "formal-rubric",
    ),
    ("Q16", "实践与认识（总）"): (
        "正式评分标准page_001 Q16列明“实践的观点”，且设问要求结合材料或个人体验作答。",
        "formal-rubric-term-support",
    ),
    ("Q16", "实践是认识的基础"): (
        "正式评分标准page_001 Q16列明“实践的观点”，题干要求结合材料或个人体验说明数字原住民如何在技术使用实践中成长。",
        "formal-rubric-broad-angle",
    ),
    ("Q16", "价值观的导向作用"): (
        "正式评分标准page_001 Q16写明“价值观具有导向作用，正确价值观具有促进作用，应树立正确价值观”。",
        "formal-rubric",
    ),
    ("Q16", "价值判断与价值选择"): (
        "正式评分标准page_001 Q16在“知”的角度列出“价值观、价值判断价值选择等”。",
        "formal-rubric-term-support",
    ),
    ("Q16", "实现人生价值"): (
        "正式评分标准page_001 Q16在行动角度列出“实践、主观能动性、实现人生价值”。",
        "formal-rubric-term-support",
    ),
    ("Q17", "矛盾的普遍性和特殊性"): (
        "正式评分标准page_002 Q17哲学知识栏列出“矛盾的普遍性和特殊性的辩证关系”。",
        "formal-rubric",
    ),
    ("Q17", "主观能动性 / 意识的能动作用"): (
        "正式评分标准page_002 Q17哲学知识栏列出“意识的能动作用/认识的作用/价值观的导向作用”。",
        "formal-rubric",
    ),
    ("Q17", "价值观的导向作用"): (
        "正式评分标准page_002 Q17哲学知识栏列出“价值观的导向作用”。",
        "formal-rubric",
    ),
    ("Q17", "发展的观点 / 发展的普遍性"): (
        "正式评分标准page_002 Q17“红色文化的发展”维度列出“发展的观点/联系的观点”。",
        "formal-rubric",
    ),
    ("Q17", "联系的普遍性 / 联系的观点（总）"): (
        "正式评分标准page_002 Q17“红色文化的发展”维度列出“发展的观点/联系的观点”。",
        "formal-rubric",
    ),
    ("Q17", "根据固有联系建立新的具体联系"): (
        "正式评分标准page_002 Q17“红色文化的发展”维度列出“联系的观点”，材料通过体验、数字技术和青年讲述建立红色文化与青年生活的新具体联系。",
        "formal-rubric-broad-angle",
    ),
    ("Q17", "价值判断与价值选择"): (
        "正式评分标准page_002 Q17“红色文化滋养年轻人”维度写明形成正确价值观、明确价值选择和价值判断的标准。",
        "formal-rubric",
    ),
    ("Q17", "认识对实践的反作用"): (
        "正式评分标准page_002 Q17写明“正确的认识有助于推动年轻人积极投身于实践”。",
        "formal-rubric",
    ),
    ("Q21", "矛盾就是对立统一"): (
        "正式评分标准page_006 Q21要求运用对立统一观点分析“活力与秩序”的关系，原理1分+分析1分。",
        "formal-rubric",
    ),
    ("Q21", "人民群众"): (
        "正式评分标准page_006 Q21“以人民为中心”角度写明人民群众是历史的主体，坚持群众观点、群众路线。",
        "formal-rubric",
    ),
}


def current_docx() -> Path:
    return core.current_docx()


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS)).strip()


def style_val(p) -> str:
    vals = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return vals[0] if vals else ""


def parse_question_no(heading: str) -> str:
    m = re.search(r"第(\d+)题(?:第（(\d+)）问)?", heading)
    if not m:
        return "Q?"
    if m.group(2):
        return f"Q{m.group(1)}({m.group(2)})"
    return f"Q{m.group(1)}"


def extract_entries_from_root(root) -> list[dict[str, str]]:
    entries = []
    current_node = ""
    current = None
    parts = []
    for p in root.xpath("//w:p", namespaces=NS):
        text = para_text(p)
        if not text:
            continue
        style = style_val(p)
        if style in {"3", "4", "5"}:
            if current is not None:
                current["student_facing_text"] = "\n".join(parts)
                entries.append(current)
                current = None
                parts = []
            if style == "4":
                current_node = text
            if style == "5" and SUITE in text:
                current = {
                    "canonical_node": current_node,
                    "registered_heading": text,
                    "question_no": parse_question_no(text),
                }
                parts = [text]
        elif current is not None:
            parts.append(text)
    if current is not None:
        current["student_facing_text"] = "\n".join(parts)
        entries.append(current)
    entries.sort(key=lambda e: (int(re.sub(r"\D", "", e["question_no"]) or "999"), e["canonical_node"], e["registered_heading"]))
    return entries


def set_para_text(p, text: str) -> None:
    texts = p.xpath(".//w:t", namespaces=NS)
    if not texts:
        r = etree.SubElement(p, f"{W}r")
        t = etree.SubElement(r, f"{W}t")
        t.text = text
        return
    texts[0].text = text
    for t in texts[1:]:
        t.text = ""


def clone_with_text(template, text: str):
    p = deepcopy(template)
    set_para_text(p, text)
    return p


def load_docx_xml(docx: Path):
    with zipfile.ZipFile(docx, "r") as zf:
        return etree.fromstring(zf.read("word/document.xml"))


def update_docx(timestamp: str) -> tuple[Path, int]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_batch32_2026_haidian_final_{timestamp}{docx.suffix}")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as zin:
        xml = zin.read("word/document.xml")
    root = etree.fromstring(xml)
    body = root.find(f"{W}body")
    paras = body.findall(f"{W}p")
    existing_signature = {(e["canonical_node"], e["question_no"]) for e in extract_entries_from_root(root)}
    inserted = 0
    for spec in NEW_ENTRY_SPECS:
        signature = (spec["canonical_node"], spec["question_no"])
        if signature in existing_signature:
            continue
        node = spec["canonical_node"]
        heading = f"{core.next_heading_number(paras, node)}. {SUITE} {spec['question_label']}"
        heading_template, body_template = core.template_paragraphs(paras, node)
        _start, end = core.find_node_bounds(paras, node)
        new_paras = [
            clone_with_text(heading_template, heading),
            clone_with_text(body_template, f"【材料触发点】{spec['material_trigger']}"),
            clone_with_text(body_template, f"【设问】{spec['question_prompt']}"),
            clone_with_text(body_template, f"【为什么能想到】{spec['why_trigger']}"),
            clone_with_text(body_template, f"【答案落点】{spec['answer_landing']}"),
        ]
        for offset, p in enumerate(new_paras):
            body.insert(end + offset, p)
        inserted += 1
        existing_signature.add(signature)
        paras = body.findall(f"{W}p")
    with tempfile.TemporaryDirectory() as td:
        tmp_docx = Path(td) / docx.name
        with zipfile.ZipFile(docx, "r") as zin, zipfile.ZipFile(tmp_docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "word/document.xml":
                    data = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
                zout.writestr(item, data)
        shutil.copy2(tmp_docx, docx)
    return backup, inserted


def evidence_for(entry: dict[str, str]) -> tuple[str, str]:
    return EVIDENCE_BY_KEY.get((entry["question_no"], entry["canonical_node"]), ("NEED_EVIDENCE_REVIEW", "unmapped-current-docx-entry"))


def update_ledger_and_accepted(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        ledger_rows = list(reader)
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch32_2026_haidian_final_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    existing_keys = {(r.get("canonical_node"), r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in ledger_rows}
    added_ledger = 0
    for e in entries:
        row = {"canonical_node": e["canonical_node"], "source_suite": SUITE, "question_no": e["question_no"], "inserted_heading": e["registered_heading"]}
        key = (row["canonical_node"], row["source_suite"], row["question_no"], row["inserted_heading"])
        if key not in existing_keys:
            ledger_rows.append(row)
            existing_keys.add(key)
            added_ledger += 1
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(ledger_rows)

    accepted_records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch32_2026_haidian_final_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup_accepted)
    accepted_keys = {(r.get("source_suite"), r.get("question_no"), r.get("canonical_node"), r.get("registered_heading")) for r in accepted_records}
    added_accepted = 0
    with ACCEPTED.open("a", encoding="utf-8") as f:
        for e in entries:
            evidence, boundary = evidence_for(e)
            record = {
                "source_suite": SUITE,
                "question_no": e["question_no"],
                "framework_node": e["canonical_node"],
                "canonical_node": e["canonical_node"],
                "student_facing_text": e["student_facing_text"],
                "evidence_level": evidence,
                "boundary_note": boundary,
                "source_lane": "Codex Batch32 Haidian final registration and insertion",
                "source_repair_basis": SOURCE_PACKET,
                "source_lines": SOURCE_PACKET,
                "batch": BATCH_ID,
                "registered_heading": e["registered_heading"],
            }
            key = (record["source_suite"], record["question_no"], record["canonical_node"], record["registered_heading"])
            if key in accepted_keys:
                continue
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            accepted_keys.add(key)
            added_accepted += 1
    return {"ledger_added": added_ledger, "accepted_added": added_accepted, "ledger_backup": str(backup), "accepted_backup": str(backup_accepted)}


def matrix_body_row(next_id: int, entry: dict[str, str]) -> dict[str, str]:
    evidence, boundary = evidence_for(entry)
    is_objective = boundary.startswith("objective-choice-only")
    is_broad = boundary in {"formal-rubric-broad-angle", "formal-rubric-term-support"}
    return {
        "matrix_row_id": f"M{next_id:04d}",
        "row_source": MATRIX_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": entry["question_no"],
        "题型或模块判断": "必修四哲学选择题客观挂点" if is_objective else "必修四哲学正文条目",
        "是否进宝典": "是：客观选择题挂点，已在当前DOCX正文登记" if is_objective else "是：已进入当前DOCX/PDF正文",
        "宝典节点": entry["canonical_node"],
        "细则支持原理": evidence,
        "证据等级": "教师版答案键+试卷原题（客观选择题）" if is_objective else ("正式评分标准宽角度/术语支持" if is_broad else "正式评分标准"),
        "是否误放": "否：保留但标注宽角度或客观挂点" if (is_objective or is_broad) else "否",
        "是否需补厚": "否",
        "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else ("KEEP_IN_BODY_WITH_BROAD_FORMAL_SUPPORT" if is_broad else "KEEP_IN_BODY"),
        "备注": "Batch32新增登记；普通参考答案只作题面/答案键核对，未冒充主观评分细则。",
        "source_artifact": SOURCE_PACKET,
    }


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch32_2026_haidian_final_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    rows = [r for r in rows if not (r.get("题源") == SUITE and r.get("row_source") == MATRIX_SOURCE)]
    max_id = 0
    for r in rows:
        m = re.match(r"M(\d+)", r.get("matrix_row_id", ""))
        if m:
            max_id = max(max_id, int(m.group(1)))
    new_rows = []
    next_id = max_id + 1
    for e in entries:
        new_rows.append(matrix_body_row(next_id, e))
        next_id += 1
    for q, qtype, node, support, evidence, status in BOUNDARY_ROWS:
        new_rows.append({
            "matrix_row_id": f"M{next_id:04d}",
            "row_source": MATRIX_SOURCE,
            "题源": SUITE,
            "年份": YEAR,
            "阶段": STAGE,
            "题号": q,
            "题型或模块判断": qtype,
            "是否进宝典": "否：模块边界排除",
            "宝典节点": node,
            "细则支持原理": support,
            "证据等级": evidence,
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": status,
            "备注": "本题或本点不作为当前哲学宝典正文；不把法律、文化、逻辑与思维、政治经济或普通参考答案偷换为哲学原理。",
            "source_artifact": SOURCE_PACKET,
        })
        next_id += 1
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    body_rows = sum(1 for r in new_rows if r["是否进宝典"].startswith("是"))
    return {
        "matrix_rows_total": len(rows) + len(new_rows),
        "batch_rows": len(new_rows),
        "body_rows": body_rows,
        "boundary_rows": len(new_rows) - body_rows,
        "matrix_backup": str(backup),
    }


def update_global_audit(docx_entries: int, matrix_rows_for_suite: int) -> dict[str, int]:
    with GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    for row in rows:
        if row.get("normalized_suite") == SUITE or row.get("raw_suite") == SUITE:
            row["in_full_source_vs_docx_audit"] = "True"
            row["matrix_rows"] = str(matrix_rows_for_suite)
            row["current_docx_mentions"] = str(docx_entries)
            row["current_status"] = "covered_by_batch32_recovery_matrix"
            row["blocker_or_next_action"] = "Batch32 inserted rubric-supported/objective-choice entries and added question-level boundary rows; render/model gates pending."
    with GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    missing = [r for r in rows if r.get("current_status") == "missing_from_current_47_suite_audit_scope"]
    covered = [r for r in rows if r.get("current_status") != "missing_from_current_47_suite_audit_scope"]
    missing_table = "\n".join(f"| {r['normalized_suite']} | {r['stage_dir']} | {r['current_status']} | {r['blocker_or_next_action']} |" for r in missing)
    GLOBAL_AUDIT_MD.write_text(f"""# Global Raw Suite Exhaustion Audit 2026-05-25

status: `GLOBAL_SOURCE_SCOPE_GAP_FOUND`

## Summary

- raw suite directories discovered under Desktop 2024-2026 stage folders: `{len(rows)}`
- current covered by first/second mock audit or recovery matrix: `{len(covered)}`
- remaining midterm/final raw suites outside current coverage: `{len(missing)}`

## Remaining Missing Midterm/Final Suites

| suite | stage_dir | status | next action |
|---|---|---|---|
{missing_table}

## Batch32 Update

- `2026海淀期末` is now covered by `COVERAGE_FUSION_BATCH32_2026_HAIDIAN_FINAL_CODEX_20260525.md`.
- Matrix rows for the suite: `{matrix_rows_for_suite}`.
- Current DOCX mentions for the suite: `{docx_entries}`.
- Render QA and ClaudeCode Opus 4.7 recheck are still separate gates.
- `2026石景山期末` remains a special excluded source unless the user supplies a usable scoring rubric.
""", encoding="utf-8", newline="\n")
    return {"remaining_missing": len(missing), "covered": len(covered), "total": len(rows)}


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    body_list = "\n".join(f"- {e['question_no']} -> {e['canonical_node']} -> {e['registered_heading']}" for e in entries)
    SOURCE_TRANSCRIPTION.write_text(f"""# Batch32 Source Transcription - 2026海淀期末

status: `SOURCE_PACKET_REGISTERED`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- formal scoring/rubric cache: `{RUBRIC_SOURCE}`
- teacher-version paper/answer cache: `{TEACHER_SOURCE}`
- rubric OCR transcription: `{RUBRIC_OCR_TEXT}`
- rubric OCR line index: `{RUBRIC_OCR_LINES}`
- teacher OCR transcription: `{TEACHER_OCR_TEXT}`
- teacher OCR line index: `{TEACHER_OCR_LINES}`
- raw source render manifest: `{SOURCE_RENDER_MANIFEST}`

## Key Evidence

- Choice-question answer key is from the teacher PDF answer page: `1B, 2A, 3A, 4C, 5D, 6C, 7D, 8A, 9D, 10B, 11B, 12C, 13C, 14B, 15D`.
- Q1-Q4 enter only as objective-choice hooks where the correct option text clearly carries a philosophy trigger; they are not treated as subjective scoring rubrics.
- Q16 formal scoring page_001 supports `矛盾就是对立统一`, `主观能动性 / 意识的能动作用`, `实践与认识（总）`, `价值观的导向作用`, `价值判断与价值选择`, and `实现人生价值`.
- Q17 formal scoring page_002 supports `矛盾的普遍性和特殊性`, `主观能动性 / 意识的能动作用`, `价值观的导向作用`, `发展的观点 / 发展的普遍性`, `联系的普遍性 / 联系的观点（总）`, `价值判断与价值选择`, and `认识对实践的反作用`.
- Q21 formal scoring page_006 supports `矛盾就是对立统一` and `人民群众`.
- Q18-Q20 and non-philosophy portions of Q21 are boundary-excluded; Q20(2) mentions “矛盾分析方法” only inside 选必三超前思维方法 scoring, not as a 必修四正文条.

## Governed DOCX Body Entries

{body_list}

## Evidence Guardrail

- 普通参考答案没有冒充评分细则。
- 选择题只登记为客观答案键证据。
- 主观题正文条只使用正式评分标准/细则支持。
""", encoding="utf-8", newline="\n")


def append_control_reports(inserted: int, entries: list[dict[str, str]], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    appendix = f"""

## Batch32 Local Application: 2026海淀期末
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries after Batch32: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch32: `{global_result['remaining_missing']}`.
- Render QA is pending for this batch.
- ClaudeCode Opus 4.7 recheck is pending for this batch; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final; `STRICT_FINAL_ACCEPTED` is not claimed.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch32 Local Application: 2026海淀期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")
    qa_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch32 Pending Render QA: 2026海淀期末"
    if marker in qa_text:
        qa_text = qa_text[: qa_text.index(marker)]
    FORMAT_QA.write_text(qa_text + f"""

## Batch32 Pending Render QA: 2026海淀期末
Updated: 2026-05-25

- Status: `RENDER_PENDING_AFTER_DOCX_MODIFICATION`.
- Batch32 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required next check: current DOCX/PDF render, heading styles, page count, labels, and new/old entry consistency.
""", encoding="utf-8", newline="\n")
    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH32_HAIDIAN_FINAL_RECHECK"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    MODEL_LEDGER.write_text(ledger + """

## CLAUDECODE_BATCH32_HAIDIAN_FINAL_RECHECK

status: `real_call_pending`

- Batch: `2026海淀期末`.
- Prompt: `OPUS47_CLAUDECODE_BATCH32_2026_HAIDIAN_FINAL_RECHECK_PROMPT.md`.
- Required command shape: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Model gate before real evidence: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output is not qualified ClaudeCode evidence.
""", encoding="utf-8", newline="\n")


def write_batch_report(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    BATCH_REPORT.write_text(f"""# Coverage Fusion Batch32 - 2026海淀期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch32 edit: `{backup}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `2026海淀期末` after Batch32: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `2026海淀期末`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch32: `{global_result['remaining_missing']}`.

## Placement Verdict

- Q1-Q4 enter only as objective-choice body hooks with evidence level `教师版答案键+试卷原题（客观选择题）`.
- Q16 enters through formal scoring support for矛盾观点、意识能动作用、实践观点、价值观/价值判断价值选择 and实现人生价值.
- Q17 enters through the formal scoring table for哲学知识 and excludes pure culture points from the philosophy body.
- Q21 enters through formal scoring support for对立统一 and人民群众;党的领导、制度优势等非哲学点 are boundary-excluded.
- Q18-Q20 are boundary-excluded as法律与生活 or逻辑与思维.
- Ordinary teacher reference answers are kept as context only and do not substitute for formal scoring text.

## Remaining Gates

- Render QA is pending because Batch32 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final; `STRICT_FINAL_ACCEPTED` is not claimed.
""", encoding="utf-8", newline="\n")


def main() -> None:
    for required in [GPT_BUNDLE, RUBRIC_SOURCE, TEACHER_SOURCE, RUBRIC_OCR_TEXT, RUBRIC_OCR_LINES, TEACHER_OCR_TEXT, TEACHER_OCR_LINES, SOURCE_RENDER_MANIFEST, MATRIX, LEDGER, ACCEPTED]:
        if not required.exists():
            raise FileNotFoundError(required)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    root = load_docx_xml(current_docx())
    entries = extract_entries_from_root(root)
    if len(entries) != EXPECTED_ENTRIES:
        raise RuntimeError(f"Expected {EXPECTED_ENTRIES} governed {SUITE} entries after Batch32, found {len(entries)}")
    unmapped = [e for e in entries if evidence_for(e)[0] == "NEED_EVIDENCE_REVIEW"]
    if unmapped:
        raise RuntimeError(f"Unmapped evidence rows: {unmapped}")
    ledger_result = update_ledger_and_accepted(entries, timestamp)
    matrix_result = update_matrix(entries, timestamp)
    global_result = update_global_audit(len(entries), matrix_result["batch_rows"])
    write_source_transcription(entries)
    append_control_reports(inserted, entries, matrix_result, global_result)
    write_batch_report(backup, inserted, entries, ledger_result, matrix_result, global_result)
    print(json.dumps({
        "suite": SUITE,
        "inserted": inserted,
        "entries": len(entries),
        "ledger_added": ledger_result["ledger_added"],
        "accepted_added": ledger_result["accepted_added"],
        "matrix_batch_rows": matrix_result["batch_rows"],
        "matrix_body_rows": matrix_result["body_rows"],
        "matrix_boundary_rows": matrix_result["boundary_rows"],
        "remaining_missing": global_result["remaining_missing"],
        "backup": str(backup),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
