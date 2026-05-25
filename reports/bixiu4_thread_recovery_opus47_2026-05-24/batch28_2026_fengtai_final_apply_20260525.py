from __future__ import annotations

import csv
import json
import re
import shutil
import tempfile
import zipfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"
NS = {"w": W_NS}

ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"
GLOBAL_AUDIT_CSV = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"
GLOBAL_AUDIT_MD = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH28_2026_FENGTAI_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH28_2026_FENGTAI_FINAL_CODEX_20260525.md"

PREPROCESSED = ROOT / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2026各区模拟题__2026各区期末和期中__2026丰台期末.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "dbc93cbfd3a93eff_2026丰台期末细则.md"
PAPER_SOURCE = PREPROCESSED / "gpt_sources" / "6553ff85e09d299a_2026北京丰台高三_上_期末政治.md"
PAPER_RENDERS = Path(r"C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\6553ff85e09d299a")
CURRENT_ARTIFACT = ROOT / "skills" / "beijing-gaokao-politics-rubric" / "assets" / "current-artifacts" / "必修四哲学材料-知识触发总框架_持续更新版_v2.md"
CURRENT_STATE = ROOT / "skills" / "feige-politics-garden-bixiu4" / "references" / "current-state.md"

SUITE = "2026丰台期末"
YEAR = "2026"
STAGE = "期末"
BATCH_ID = "batch28_2026_fengtai_final"
MATRIX_SOURCE = "codex_batch28_2026_fengtai_final"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {PAPER_SOURCE}; rendered paper pages: {PAPER_RENDERS}; "
    f"choice-answer closure evidence: {CURRENT_ARTIFACT} lines 1813-1836 and {CURRENT_STATE} lines 218-222; "
    "current DOCX verified: 4 existing unregistered 2026丰台期末 headings were present before Batch28"
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "社会存在与社会意识",
        "question_no": "Q1",
        "question_label": "第1题（选择题）",
        "material_trigger": "答案闭环文件记录第1题答案为B；当前框架第1827行确认正确项落在社会意识反作用、文化载体、精神力量。",
        "question_prompt": "经典歌曲记录人民历史选择、改革开放和强国复兴进程，激励人们勇毅前行。",
        "why_trigger": "经典歌曲作为社会意识和文化载体，来源于时代实践，又以精神力量反作用于社会实践。",
        "answer_landing": "本题只作客观选择题挂点。经典歌曲不是决定社会发展，而是承载时代精神、凝聚奋进力量，体现社会意识对社会存在具有反作用。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q2",
        "question_label": "第2题（选择题）",
        "material_trigger": "答案闭环文件记录第2题答案为C；当前框架第1828行确认正确项落在群众观点、人民立场。",
        "question_prompt": "智能呼叫、扫码支付培训、养老驿站、助餐就医等服务回应高龄独居老人照料难题。",
        "why_trigger": "材料从老年群体的具体困难出发，强调公共治理要听民声、回应人民群众真实需求。",
        "answer_landing": "本题只作客观选择题挂点。基层治理和公共服务要坚持群众观点，站稳人民立场，解决群众身边事，增强获得感、幸福感和安全感。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q4",
        "question_label": "第4题（选择题）",
        "material_trigger": "答案闭环文件记录第4题答案为B；当前框架第1829行确认正确项强调实践工具革新是人发挥主观能动性的结果。",
        "question_prompt": "水务机器人可读取仪表、检测异常气体、识别烟雾、清捞垃圾、感知避障和完成水下测绘，重塑水务治理模式。",
        "why_trigger": "水务机器人的设计、部署和改进体现人主动改造实践工具、提升治理能力的能动活动。",
        "answer_landing": "本题只作客观选择题挂点。机器人不会自行生成治理模式，其作为实践工具的革新，是人在认识水务治理问题基础上发挥主观能动性的结果。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q4",
        "question_label": "第4题（选择题）",
        "material_trigger": "答案闭环文件记录第4题答案为B；当前框架第1829行确认机器人延伸人的认识器官、提高水务治理实践水平。",
        "question_prompt": "水务机器人通过多种传感、识别、测绘能力获取水务治理信息并服务治理实践。",
        "why_trigger": "机器人扩展的是实践和认识手段，不是新增认识来源；认识来源仍是实践。",
        "answer_landing": "本题只作客观选择题挂点。水务机器人延伸人的认识器官和实践工具，使人能够更有效获取治理信息并改进水务治理实践。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "细则第51-53行明确“留白与周围事物相互联系、相互影响”，并写“联系具有普遍性、客观性，要坚持联系的观点”。",
        "question_prompt": "第16题要求结合材料，运用《哲学与文化》知识，谈谈对“留白”的理解。",
        "why_trigger": "留白不是孤立空白，它只有在山林、溪谷、高楼、绿地、喧嚣和沉静等关系中才形成整体意境。",
        "answer_landing": "分析留白要坚持联系的观点。留白与周围景物、空间节奏和生活情境相互作用，共同构成有张弛、有层次的审美整体，不能把留白孤立理解为空缺。",
    },
    {
        "canonical_node": "联系的客观性",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "细则第52-53行在联系角度中直接写“联系具有普遍性、客观性”。",
        "question_prompt": "第16题材料把留白放在山林、溪谷、高楼旁绿地、旷野沉思等实际场景中理解。",
        "why_trigger": "留白的审美效果受到空间结构、生态环境和周围事物固有联系制约，不是主观任意安排。",
        "answer_landing": "留白要尊重联系的客观性。只有把留白放回具体空间和周围事物的真实联系中，才能营造和谐有序的整体意境；随意空置或过度留白反而会破坏效果。",
    },
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "细则第444行把“与中国具体实际相结合”列为“是什么”维度可用知识。",
        "question_prompt": "第22题围绕五年规划，要求综合运用所学，谈谈对“科学制定和接续实施五年规划是我们党治国理政一条重要经验，也是中国特色社会主义一个重要政治优势”的理解。",
        "why_trigger": "五年规划不是抽象照搬，而是把现代化目标、发展阶段、群众意见和国家治理实际统一起来制定。",
        "answer_landing": "科学制定五年规划要坚持从中国具体实际出发。我国根据不同历史阶段的发展任务和现实条件接续编制规划，把顶层设计与实际国情结合起来，使战略安排符合现代化建设需要。",
    },
    {
        "canonical_node": "规律的客观性",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "细则第444、452行两次列出“遵循规律”；当前框架第1441行也把该题落到规律客观性。",
        "question_prompt": "材料强调从1953年至今，我国接续实施五年规划，科学制定和有效实施国家发展规划。",
        "why_trigger": "规划要服务经济社会发展，必须建立在对发展阶段、发展规律和现代化进程的客观把握之上。",
        "answer_landing": "五年规划体现尊重规律。党和国家在认识经济社会发展规律、现代化建设规律的基础上作出接续谋划，使长期战略和阶段任务相衔接，推动现代化建设有序推进。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "细则第448行列“群众观点、群众路线”；材料写编制过程中党广泛征求社会各界意见、问计于民。",
        "question_prompt": "第22题材料说明五年规划编制广泛征求社会各界意见，把顶层设计和问计于民统一起来。",
        "why_trigger": "规划来自人民实践、回应人民需要，人民群众的意见和实践经验是科学决策的重要基础。",
        "answer_landing": "科学制定五年规划要坚持群众观点和群众路线。党广泛听取社会各界意见，把人民意愿、实践经验和发展需求吸收到规划中，使规划凝聚共识、服务人民。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "细则第452行列“联系的观点”；材料强调长期战略性与中期灵活性结合、中央统筹、地方分解、部门协同。",
        "question_prompt": "第22题材料要求理解五年规划如何把长期战略、中期目标、中央地方部门协同统一起来。",
        "why_trigger": "五年规划涉及时间上的接续、主体上的协同和任务上的衔接，不能孤立看某一个阶段或部门。",
        "answer_landing": "理解五年规划要坚持联系观点。它把长期目标与阶段任务、中央统筹与地方落实、部门协同与社会参与联系起来，形成持续推进现代化建设的治理链条。",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "细则第452行明确列“系统优化”；材料写中央统筹、地方分解、部门协同，下好“全国一盘棋”。",
        "question_prompt": "第22题材料强调规划实施中中央统筹、地方分解、部门协同，处理长期战略和中期灵活性的关系。",
        "why_trigger": "五年规划是跨区域、跨部门、跨阶段的系统治理安排，需要统筹要素、优化结构、形成合力。",
        "answer_landing": "五年规划体现系统优化方法。通过中央统筹、地方分解、部门协同，把目标、任务、资源和政策组织为统一系统，推动国家治理形成“一盘棋”效能。",
    },
    {
        "canonical_node": "社会存在与社会意识",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "细则第444行列“社会意识”；当前框架第1443行说明发展规划属于社会意识形态的重要内容并反作用于实践。",
        "question_prompt": "第22题要求说明五年规划作为治国理政经验和政治优势的意义。",
        "why_trigger": "五年规划是对经济社会发展实际的认识和战略表达，属于社会意识层面的规划安排。",
        "answer_landing": "五年规划体现社会存在与社会意识的关系。它来源于我国经济社会发展的现实需要和实践经验，又通过战略目标、指标体系和政策安排反作用于经济社会发展实践。",
    },
    {
        "canonical_node": "社会发展的两大基本规律和基本矛盾",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "细则第444行列“上层建筑”；材料写《国家发展规划法》为规划提供法律支撑。",
        "question_prompt": "第22题材料说明《国家发展规划法》为科学编制和有效实施国家发展规划、发挥战略导向作用提供法律支撑。",
        "why_trigger": "发展规划法律化、制度化属于上层建筑调整，用制度和法律保障经济社会发展战略实施。",
        "answer_landing": "从社会基本矛盾看，国家发展规划法和规划制度属于上层建筑的重要内容。通过完善制度和法律支撑，使上层建筑更好服务经济社会发展和现代化建设需要。",
    },
    {
        "canonical_node": "认识对实践的反作用",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "细则第444行列“正确认识”；当前框架第1443行将该题表述为“正确认识指导实践”。",
        "question_prompt": "第22题材料说明科学制定和接续实施五年规划，保障“一张蓝图绘到底”，发挥战略导向作用。",
        "why_trigger": "科学规划是正确认识和战略判断的成果，会反过来指导经济社会发展实践。",
        "answer_landing": "正确认识对实践具有指导作用。五年规划把对发展阶段、任务和趋势的科学认识转化为战略安排和行动方案，指导各方面接续推进现代化建设。",
    },
]


BOUNDARY_ROWS = [
    ("Q3", "逻辑与思维选择题", "概念外延关系、划分标准", "答案闭环表第3题答案A；题目考查逻辑概念外延和划分错误，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q5", "逻辑与思维选择题", "定义、三段论、换质位推理", "答案闭环表第5题答案C；题目考查逻辑规则，不进入必修四哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q6", "文化/逻辑选择题", "中国结、中华优秀传统文化、形象思维", "答案闭环表第6题答案A；当前框架第1830行将其列为文化载体和形象思维，当前哲学正文不设置文化节点。", "答案闭环表+当前框架", "CULTURE_LOGIC_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q7", "政治与法治选择题", "地方立法、法规清理、生态文明", "答案闭环表第7题答案B；属政治与法治地方立法，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q8", "政治与法治选择题", "宪法宣传周、法治思想、普法", "答案闭环表第8题答案D；属法治宣传和依法治国，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q9", "政治与法治选择题", "人民政协、科学讲堂、文化职能", "答案闭环表第9题答案C；属政协履职与科学传播，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q10", "法律与生活选择题", "诉讼调解、欠条、执行力", "答案闭环表第10题答案D；属法律与生活诉讼调解，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q11", "法律与生活选择题", "权利义务、司法保护、法治德治", "答案闭环表第11题答案D；属法律案例综合，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q12", "经济选择题", "京津冀产业链、集链成群、协同发展", "答案闭环表第12题答案A；虽有系统优化表述，但题目主旨为区域产业链和经济协同，不作为哲学正文挂点。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q13", "经济选择题", "促消费、扩大内需、供需适配", "答案闭环表第13题答案C；属经济政策，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q14", "经济/开放选择题", "海南自贸港、制度型开放、封关", "答案闭环表第14题答案B；属开放型经济制度安排，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q15", "当代国际政治与经济选择题", "亚投行、多边合作、区域合作", "答案闭环表第15题答案D；属国际政治经济，不进入哲学正文。", "试卷渲染页+答案闭环表", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q16-culture", "文化主观题点", "中华优秀传统文化、美学智慧、文化功能", "细则第55-57行列文化角度；当前交付为哲学正文，文化点登记边界。", "正式细则边界", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q17", "政治与法治主观题", "基层治理、党的领导、全过程人民民主、政府履职", "细则第107-170行按政治与法治基层治理评分，不进入哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q18", "法律与生活主观题", "未成年人保护、公益诉讼、市场监管", "细则第172-234行按法律与生活/法治规则评分，不进入哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q19", "经济主观题", "人工智能、有利条件、市场和政府、高质量发展", "细则第251-309行按经济与社会评分，不进入哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q20", "逻辑与思维主观题", "科学思维、辩证思维、创新思维、超前思维", "细则第314-363行明确知识板块为逻辑与思维；不把逻辑思维题中的辩证思维偷换为必修四哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q21", "当代国际政治与经济主观题", "全球倡议、人类命运共同体、新型国际关系", "细则第365-417行及试卷第21题均属当代国际政治与经济，不进入哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH28_FENGTAI_FINAL"),
    ("Q22-nonphilosophy", "综合主观题中非哲学点", "党的领导、人民当家作主、依法治国、超前思维", "细则第447-453行还列政治与法治、逻辑与思维等综合点；仅将明确哲学节点入正文，其余作边界。", "正式细则边界", "NONPHILOSOPHY_COMPREHENSIVE_POINT_BOUNDARY_EXCLUDED"),
]


EVIDENCE_BY_KEY = {
    ("Q1", "社会存在与社会意识"): ("当前框架第1827行+current-state第218-222行答案闭环：第1题答案B，正确项支持社会意识反作用/精神力量", "objective-choice-only-current-artifact"),
    ("Q2", "人民群众"): ("当前框架第1828行+current-state第218-222行答案闭环：第2题答案C，正确项支持群众观点/人民立场", "objective-choice-only-current-artifact"),
    ("Q4", "主观能动性 / 意识的能动作用"): ("当前框架第1829行+current-state第218-222行答案闭环：第4题答案B，正确项①支持实践工具革新是发挥主观能动性的结果", "objective-choice-only-current-artifact"),
    ("Q4", "实践与认识（总）"): ("当前框架第1829行+current-state第218-222行答案闭环：第4题答案B，正确项④支持机器人延伸认识器官、提高实践水平", "objective-choice-only-current-artifact"),
    ("Q16", "尊重客观规律与发挥主观能动性相结合"): ("正式细则第54行：留白需要在尊重客观规律的基础上充分发挥主观能动性", "formal-rubric"),
    ("Q16", "整体与部分"): ("正式细则第51-52行：立足整体、正确处理整体与部分关系", "formal-rubric"),
    ("Q16", "量变与质变 / 适度原则"): ("正式细则第49-50行：量变质变与把握适度原则", "formal-rubric"),
    ("Q16", "矛盾就是对立统一"): ("正式细则第46-48行：矛盾双方对立统一、相互对立相互依存", "formal-rubric"),
    ("Q16", "联系的普遍性 / 联系的观点（总）"): ("正式细则第51-53行：留白与周围事物相互联系、相互影响；坚持联系的观点", "formal-rubric"),
    ("Q16", "联系的客观性"): ("正式细则第52-53行：联系具有普遍性、客观性", "formal-rubric"),
    ("Q22", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("正式细则第444行：与中国具体实际相结合", "formal-rubric"),
    ("Q22", "规律的客观性"): ("正式细则第444、452行：遵循规律", "formal-rubric"),
    ("Q22", "人民群众"): ("正式细则第448行：群众观点、群众路线；试卷材料问计于民", "formal-rubric"),
    ("Q22", "联系的普遍性 / 联系的观点（总）"): ("正式细则第452行：联系的观点；材料长期战略、中期灵活、中央地方部门协同", "formal-rubric"),
    ("Q22", "系统观念 / 系统优化"): ("正式细则第452行：系统优化；材料中央统筹、地方分解、部门协同、全国一盘棋", "formal-rubric"),
    ("Q22", "社会存在与社会意识"): ("正式细则第444行：社会意识；当前框架第1443行说明规划属于社会意识并反作用于实践", "formal-rubric"),
    ("Q22", "社会发展的两大基本规律和基本矛盾"): ("正式细则第444行：上层建筑；试卷材料《国家发展规划法》提供法律支撑", "formal-rubric-term-support"),
    ("Q22", "认识对实践的反作用"): ("正式细则第444行：正确认识；当前框架第1443行：正确认识指导实践", "formal-rubric-broad-angle"),
}


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS)).strip()


def style_val(p) -> str:
    style = p.find(f".//{W}pStyle")
    return style.get(f"{W}val") if style is not None else ""


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


def parse_question_no(heading: str) -> str:
    m = re.search(r"第(\d+)题(?:第（(\d+)）问)?", heading)
    if not m:
        return "Q?"
    if m.group(2):
        return f"Q{m.group(1)}({m.group(2)})"
    return f"Q{m.group(1)}"


def load_docx_xml(docx: Path):
    with zipfile.ZipFile(docx, "r") as zf:
        return etree.fromstring(zf.read("word/document.xml"))


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
                current = {"canonical_node": current_node, "registered_heading": text, "question_no": parse_question_no(text)}
                parts = [text]
        elif current is not None:
            parts.append(text)
    if current is not None:
        current["student_facing_text"] = "\n".join(parts)
        entries.append(current)
    entries.sort(key=lambda e: (e["question_no"], e["canonical_node"], e["registered_heading"]))
    return entries


def find_node_bounds(paras, node: str) -> tuple[int, int]:
    start = None
    for i, p in enumerate(paras):
        if style_val(p) == "4" and para_text(p) == node:
            start = i
            break
    if start is None:
        raise RuntimeError(f"Node not found in DOCX: {node}")
    end = len(paras)
    for j in range(start + 1, len(paras)):
        if style_val(paras[j]) in {"3", "4"}:
            end = j
            break
    return start, end


def next_heading_number(paras, node: str) -> int:
    start, end = find_node_bounds(paras, node)
    max_num = 0
    for p in paras[start + 1 : end]:
        if style_val(p) == "5":
            m = re.match(r"(\d+)\.", para_text(p))
            if m:
                max_num = max(max_num, int(m.group(1)))
    return max_num + 1


def template_paragraphs(paras, node: str):
    start, end = find_node_bounds(paras, node)
    heading_template = None
    body_template = None
    after_heading = False
    for p in paras[start + 1 : end]:
        if style_val(p) == "5":
            heading_template = p
            after_heading = True
            continue
        if after_heading and style_val(p) not in {"3", "4", "5"} and para_text(p):
            body_template = p
            break
    if heading_template is None:
        heading_template = next(p for p in paras if style_val(p) == "5")
    if body_template is None:
        body_template = next(p for p in paras if style_val(p) not in {"3", "4", "5"} and para_text(p))
    return heading_template, body_template


def update_docx(timestamp: str) -> tuple[Path, int]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_batch28_2026_fengtai_final_{timestamp}{docx.suffix}")
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
        heading = f"{next_heading_number(paras, node)}. {SUITE} {spec['question_label']}"
        heading_template, body_template = template_paragraphs(paras, node)
        _start, end = find_node_bounds(paras, node)
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


def evidence_for(e: dict[str, str]) -> tuple[str, str]:
    return EVIDENCE_BY_KEY.get((e["question_no"], e["canonical_node"]), ("NEED_EVIDENCE_REVIEW", "unmapped-current-docx-entry"))


def update_ledger_and_accepted(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        ledger_rows = list(reader)
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch28_2026_fengtai_final_{timestamp}{LEDGER.suffix}")
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
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch28_2026_fengtai_final_{timestamp}{ACCEPTED.suffix}")
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
                "source_lane": "Codex Batch28 Fengtai final registration and insertion",
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


def matrix_body_row(next_id: int, e: dict[str, str]) -> dict[str, str]:
    evidence, boundary = evidence_for(e)
    is_objective = boundary.startswith("objective-choice-only")
    is_broad = boundary in {"formal-rubric-broad-angle", "formal-rubric-term-support"}
    return {
        "matrix_row_id": f"M{next_id:04d}",
        "row_source": MATRIX_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": e["question_no"],
        "题型或模块判断": "必修四哲学选择题客观挂点" if is_objective else "必修四哲学正文条目",
        "是否进宝典": "是：客观选择题挂点，已在当前DOCX正文登记" if is_objective else "是：已进入当前DOCX/PDF正文",
        "宝典节点": e["canonical_node"],
        "细则支持原理": evidence,
        "证据等级": "答案闭环表+试卷渲染页+当前框架" if is_objective else ("正式细则宽角度/术语支持" if is_broad else "正式细则"),
        "是否误放": "否：保留但标注宽角度或术语支持" if is_broad else "否",
        "是否需补厚": "否",
        "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else ("KEEP_IN_BODY_WITH_BROAD_FORMAL_SUPPORT" if is_broad else "KEEP_IN_BODY"),
        "备注": "Batch28登记既有正文并补入缺漏；选择题只按已记录答案闭环作客观挂点，普通参考答案未冒充主观评分细则。",
        "source_artifact": SOURCE_PACKET,
    }


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch28_2026_fengtai_final_{timestamp}{MATRIX.suffix}")
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
            "备注": "本题或本点不作为当前哲学宝典正文；不把法律、逻辑、经济、文化或综合非哲学点偷换为哲学原理。",
            "source_artifact": SOURCE_PACKET,
        })
        next_id += 1
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    return {"matrix_rows_total": len(rows) + len(new_rows), "batch_rows": len(new_rows), "body_rows": sum(1 for r in new_rows if r["是否进宝典"].startswith("是")), "boundary_rows": sum(1 for r in new_rows if not r["是否进宝典"].startswith("是")), "matrix_backup": str(backup)}


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
            row["current_status"] = "covered_by_batch28_recovery_matrix"
            row["blocker_or_next_action"] = "Batch28 registered existing DOCX entries, inserted rubric-supported/objective-choice points, and added boundary rows; render/model gates pending."
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

## Batch28 Update

- `2026丰台期末` is now covered by `COVERAGE_FUSION_BATCH28_2026_FENGTAI_FINAL_CODEX_20260525.md`.
- Matrix rows for the suite: `{matrix_rows_for_suite}`.
- Current DOCX mentions for the suite: `{docx_entries}`.
- Render QA and ClaudeCode Opus 4.7 recheck are still separate gates.
- `2026石景山期末` remains a special excluded source unless the user supplies a usable scoring rubric.
""", encoding="utf-8", newline="\n")
    return {"remaining_missing": len(missing), "covered": len(covered), "total": len(rows)}


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    body_list = "\n".join(f"- {e['question_no']} -> {e['canonical_node']} -> {e['registered_heading']}" for e in entries)
    SOURCE_TRANSCRIPTION.write_text(f"""# Batch28 Source Transcription - 2026丰台期末

status: `SOURCE_PACKET_REGISTERED`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- scoring/rubric cache: `{RUBRIC_SOURCE}`
- scan-only paper cache: `{PAPER_SOURCE}`
- rendered paper pages: `{PAPER_RENDERS}`
- objective-answer closure: `{CURRENT_ARTIFACT}` lines 1813-1836; `{CURRENT_STATE}` lines 218-222

## Key Evidence

- Q1/Q2/Q4 objective rows use the recorded answer closure `1B 2C 3A 4B 5C 6A 7B 8D 9C 10D 11D 12A 13C 14B 15D`; they are labeled objective-only and not treated as subjective scoring rubrics.
- Q16 is directly supported by the formal rubric: lines 46-54 list 矛盾对立统一, 量变质变/适度原则, 整体与部分, 联系普遍性/客观性, and 尊重客观规律与发挥主观能动性.
- Q17-Q21 are boundary-excluded by formal scoring module labels: 政治与法治, 法律与生活, 经济与社会, 逻辑与思维, 当代国际政治与经济.
- Q22 is a综合运用题. Rubric lines 442-454 list 正确认识, 上层建筑, 社会意识, 遵循规律, 与中国具体实际相结合, 群众观点/群众路线, 联系观点, 系统优化等; only those explicit philosophy nodes were inserted.

## Governed DOCX Entries

{body_list}

## Evidence Rule

- Objective-choice rows remain objective-only.
- Culture-only and non-philosophy points are boundary rows.
- Q22 broad terms are labeled as formal-rubric broad/term support where the rubric names a term but does not provide detailed point-by-point scoring.
""", encoding="utf-8", newline="\n")


def append_control_reports(inserted: int, entries: list[dict[str, str]], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    appendix = f"""

## Batch28 Local Application: 2026丰台期末
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries after Batch28: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch28: `{global_result['remaining_missing']}`.
- Render QA is pending for this batch.
- ClaudeCode Opus 4.7 recheck is pending for this batch; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch28 Local Application: 2026丰台期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")
    qa_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch28 Pending Render QA: 2026丰台期末"
    if marker in qa_text:
        qa_text = qa_text[: qa_text.index(marker)]
    FORMAT_QA.write_text(qa_text + f"""

## Batch28 Pending Render QA: 2026丰台期末
Updated: 2026-05-25

- Status: `RENDER_PENDING_AFTER_DOCX_MODIFICATION`.
- Batch28 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required next check: current DOCX/PDF render, heading styles, page count, labels, and new/old entry consistency.
""", encoding="utf-8", newline="\n")
    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH28_FENGTAI_FINAL_RECHECK"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    MODEL_LEDGER.write_text(ledger + """

## CLAUDECODE_BATCH28_FENGTAI_FINAL_RECHECK

status: `real_call_pending`

- Batch: `2026丰台期末`.
- Prompt: `OPUS47_CLAUDECODE_BATCH28_2026_FENGTAI_FINAL_RECHECK_PROMPT.md`.
- Required command shape: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Model gate before real evidence: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output is not qualified ClaudeCode evidence.
""", encoding="utf-8", newline="\n")


def write_batch_report(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    BATCH_REPORT.write_text(f"""# Coverage Fusion Batch28 - 2026丰台期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch28 edit: `{backup}`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `2026丰台期末` after Batch28: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `2026丰台期末`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch28: `{global_result['remaining_missing']}`.

## Placement Verdict

- `2026丰台期末` had 4 existing Q16 DOCX headings but no recovery-matrix rows; Batch28 repaired that ledger/matrix gap.
- Objective-choice body rows were added only where the current answer-closure artifact records a stable answer and a 必修四 philosophy trigger: Q1, Q2, Q4.
- Q16 was completed from the formal rubric, including联系普遍性/客观性补项.
- Q22 was inserted only for rubric-listed philosophy terms; politics, law, culture, logic, and international-economy points were boundary-excluded.

## Remaining Gates

- Render QA is pending because Batch28 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
""", encoding="utf-8", newline="\n")


def main() -> int:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    entries = extract_entries_from_root(load_docx_xml(current_docx()))
    if len(entries) != 18:
        raise RuntimeError(f"Expected 18 governed {SUITE} DOCX entries after Batch28, found {len(entries)}")
    unmapped = [e for e in entries if evidence_for(e)[0] == "NEED_EVIDENCE_REVIEW"]
    if unmapped:
        raise RuntimeError(f"Unmapped evidence entries: {unmapped}")
    ledger_result = update_ledger_and_accepted(entries, timestamp)
    matrix_result = update_matrix(entries, timestamp)
    global_result = update_global_audit(len(entries), int(matrix_result["batch_rows"]))
    write_source_transcription(entries)
    append_control_reports(inserted, entries, matrix_result, global_result)
    write_batch_report(backup, inserted, entries, ledger_result, matrix_result, global_result)
    print(json.dumps({"suite": SUITE, "inserted": inserted, "entries": len(entries), "matrix": matrix_result, "ledger": ledger_result, "global": global_result, "backup": str(backup)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
