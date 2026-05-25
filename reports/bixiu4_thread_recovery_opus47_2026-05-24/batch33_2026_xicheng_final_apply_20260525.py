from __future__ import annotations

import csv
import importlib.util
import json
import re
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree


BASE_PATH = Path(__file__).with_name("batch29_2026_chaoyang_midterm_apply_20260525.py")
spec = importlib.util.spec_from_file_location("batch29_core", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

W = base.W
NS = base.NS

ROOT = base.ROOT
RECOVERY = base.RECOVERY
RUN = base.RUN
DELIVERY = base.DELIVERY
MATRIX = base.MATRIX
LEDGER = base.LEDGER
ACCEPTED = base.ACCEPTED
GLOBAL_AUDIT_CSV = base.GLOBAL_AUDIT_CSV
GLOBAL_AUDIT_MD = base.GLOBAL_AUDIT_MD
FORMAT_QA = base.FORMAT_QA
THREAD_STATUS = base.THREAD_STATUS
GOVERNOR = base.GOVERNOR
CONFUCIUS = base.CONFUCIUS
MODEL_LEDGER = base.MODEL_LEDGER

PREPROCESSED = ROOT / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2026各区模拟题__2026各区期末和期中__2026西城期末.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "54715a1e650d940e_2026西城期末细则.md"
RAW_RUBRIC_PDF = Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区期末和期中\2026西城期末\细则\2026西城期末细则.pdf")
RAW_TEACHER_PDF = Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区期末和期中\2026西城期末\试卷\2026北京西城高三（上）期末政治（教师版）.pdf")
RAW_PINGBIAO_PPTX = Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区期末和期中\2026西城期末\西城高三期末评标.pptx")
RUBRIC_OCR_TEXT = RECOVERY / "BATCH33_2026_XICHENG_FINAL_RUBRIC_OCR_TRANSCRIPTION_20260525.md"
RUBRIC_OCR_LINES = RECOVERY / "BATCH33_2026_XICHENG_FINAL_RUBRIC_OCR_LINES_20260525.md"
TEACHER_OCR_TEXT = RECOVERY / "BATCH33_2026_XICHENG_FINAL_TEACHER_OCR_TRANSCRIPTION_20260525.md"
TEACHER_OCR_LINES = RECOVERY / "BATCH33_2026_XICHENG_FINAL_TEACHER_OCR_LINES_20260525.md"
PINGBIAO_TRANSCRIPTION = RECOVERY / "BATCH33_2026_XICHENG_FINAL_PINGBIAO_PPTX_TRANSCRIPTION_20260525.md"
SOURCE_RENDER_MANIFEST = RECOVERY / "BATCH33_2026_XICHENG_FINAL_SOURCE_RENDER_MANIFEST.json"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH33_2026_XICHENG_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH33_2026_XICHENG_FINAL_CODEX_20260525.md"

SUITE = "2026西城期末"
YEAR = "2026"
STAGE = "期末"
BATCH_ID = "batch33_2026_xicheng_final"
MATRIX_SOURCE = "codex_batch33_2026_xicheng_final"
EXPECTED_ENTRIES = 20
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; raw rubric PDF: {RAW_RUBRIC_PDF}; "
    f"raw teacher PDF: {RAW_TEACHER_PDF}; marking PPTX: {RAW_PINGBIAO_PPTX}; "
    f"rubric OCR: {RUBRIC_OCR_TEXT}; rubric lines: {RUBRIC_OCR_LINES}; "
    f"teacher OCR: {TEACHER_OCR_TEXT}; teacher lines: {TEACHER_OCR_LINES}; "
    f"marking PPT extract: {PINGBIAO_TRANSCRIPTION}; source render manifest: {SOURCE_RENDER_MANIFEST}; "
    "formal answer key: 1C,2B,3A,4D,5C,6C,7D,8B,9D,10B,11A,12C,13D,14C,15A."
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "认识发展原理",
        "question_no": "Q3",
        "question_label": "第3题（选择题）",
        "material_trigger": "试卷第3题以虚拟人模拟糖尿病新药疗效为材料，正式答案键为3A；正确项①为“促进人们认识能力的提高”。",
        "question_prompt": "判断通过虚拟人模拟进行新药研发为什么能节省研发时间。",
        "why_trigger": "正确项把新技术模拟与认识能力提升直接连接起来，属于选择题客观答案链；它只能作为客观挂点，不替代主观题评分细则。",
        "answer_landing": "虚拟模拟作为新的研究工具扩展了人们处理复杂医学对象的能力，能够促进认识能力提高，推动认识在技术条件中发展。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q3",
        "question_label": "第3题（选择题）",
        "material_trigger": "试卷第3题正式答案键为3A；正确项②为“加快实践与认识的循环过程”，错误项排除了省去感性阶段、避免一切错误偏差。",
        "question_prompt": "判断虚拟人模拟与实践、认识循环之间的关系。",
        "why_trigger": "题肢直接出现“实践与认识的循环过程”，可以进入实践认识总节点；但它是选择题答案键证据，不能写成主观评分稳定触发。",
        "answer_landing": "虚拟人模拟不能取消认识阶段，也不能保证没有偏差，但能让实践检验和认识调整更快循环，提高新药研发效率。",
    },
    {
        "canonical_node": "矛盾的普遍性和特殊性",
        "question_no": "Q4",
        "question_label": "第4题（选择题）",
        "material_trigger": "试卷第4题以古诗词中长江江豚踪迹为材料，正式答案键为4D；正确项说不同古诗词对江豚的个性化描写蕴含着江豚生存的一般规律。",
        "question_prompt": "判断从不同古诗词中遴选江豚诗句以重建历史分布的合理性。",
        "why_trigger": "正确项把个性化描写和一般规律联系起来，正是从特殊性中把握普遍性；这是选择题客观挂点。",
        "answer_landing": "不同诗词的具体描写是特殊表现，其中可能蕴含江豚生存与分布的一般规律，要在普遍性与特殊性的统一中提取线索。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q5",
        "question_label": "第5题（选择题）",
        "material_trigger": "试卷第5题以G20南非峰会“团结、平等、可持续”主题为材料，正式答案键为5C；正确项说关注国家间联系的普遍性和客观性，共同应对全球挑战。",
        "question_prompt": "判断G20峰会主题反映的哲学道理。",
        "why_trigger": "正确选项直接出现“联系的普遍性和客观性”，可作为联系观选择题客观挂点；不扩写成主观评分链。",
        "answer_landing": "全球挑战把各国客观联系在一起，应坚持联系观点，在普遍、客观的国家间联系中共同应对问题。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q16(1)",
        "question_label": "第16题第（1）问（主观题）",
        "material_trigger": "正式评分细则page_001 Q16(1)角度1写明“人民”，并给出变通表述“人民群众是精神财富的创造者，要坚持人民主体”。",
        "question_prompt": "结合材料，说明当代中国纪录片创作对增强文化自信的启示。",
        "why_trigger": "评分细则不是普通参考答案，而是明确把纪录片创作的文化自信落点与人民主体、人民群众创造精神财富相连。",
        "answer_landing": "纪录片创作要坚持人民主体，贴近人民精神生活，展现人民奋发有为的精神风貌，因为人民群众是社会精神财富的创造者。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q16(2)",
        "question_label": "第16题第（2）问（主观题）",
        "material_trigger": "正式评分细则page_002 Q16(2)唯物论角度写明“只有符合客观的正确意识才能有效发挥能动作用，正确指导实践”。",
        "question_prompt": "从哲学角度，谈谈为什么“真实”往往具有直抵人心的力量。",
        "why_trigger": "细则把“真实”定义为主观与客观事实相符合，并说明正确意识能指导实践、认识世界改造世界。",
        "answer_landing": "符合客观真实的正确意识能够有效发挥能动作用，正确指导实践、打破偏见、凝聚共识，所以真实具有直抵人心的力量。",
    },
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q16(2)",
        "question_label": "第16题第（2）问（主观题）",
        "material_trigger": "正式评分细则page_002写明“真实是指客观事物及其规律的本来面目，追求真实就是实现主观与客观事实相符合”。",
        "question_prompt": "从哲学角度，谈谈为什么“真实”往往具有直抵人心的力量。",
        "why_trigger": "“主观与客观事实相符合”是实事求是、一切从实际出发的核心表述，且出自正式细则。",
        "answer_landing": "追求真实就是坚持从客观事实出发，使主观认识符合客观实际，反对主观臆造和偏见，因此能形成说服力和共鸣。",
    },
    {
        "canonical_node": "真理观",
        "question_no": "Q16(2)",
        "question_label": "第16题第（2）问（主观题）",
        "material_trigger": "正式评分细则page_002认识论角度写明“追求真理是人类认识活动的根本任务”，酌情原则还列出“真理最基本属性”。",
        "question_prompt": "从哲学角度，谈谈为什么“真实”往往具有直抵人心的力量。",
        "why_trigger": "细则把追求真实与追求真理、真理属性直接对应，是正式评分支持的真理观落点。",
        "answer_landing": "真实认识经实践检验后才能获得真理，真理具有客观性，因而能够跨越偏见和隔阂，产生直抵人心的力量。",
    },
    {
        "canonical_node": "认识对实践的反作用",
        "question_no": "Q16(2)",
        "question_label": "第16题第（2）问（主观题）",
        "material_trigger": "正式评分细则page_002认识论角度写明“真实认识才能获得真理，对实践具有促进作用”。",
        "question_prompt": "从哲学角度，谈谈为什么“真实”往往具有直抵人心的力量。",
        "why_trigger": "细则明确要求把真实认识的实践促进作用讲出来，属于认识对实践反作用的正式细则支持。",
        "answer_landing": "真实认识能够正确指导实践、促进实践发展，使新闻、历史、司法、科学和纪录片等领域的活动形成可信力量。",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q16(2)",
        "question_label": "第16题第（2）问（主观题）",
        "material_trigger": "正式评分细则page_002价值观角度写明，对“真实”的追求能引导人们作出正确的价值判断与选择。",
        "question_prompt": "从哲学角度，谈谈为什么“真实”往往具有直抵人心的力量。",
        "why_trigger": "评分细则直接点名“价值判断与选择”，不是从普通参考答案外推。",
        "answer_landing": "追求真实体现正确价值判断与价值选择，引导人们尊重事实、规律和人民利益，因而能够跨领域达成价值共识。",
    },
    {
        "canonical_node": "社会存在与社会意识",
        "question_no": "Q16(2)",
        "question_label": "第16题第（2）问（主观题）",
        "material_trigger": "正式评分细则page_002酌情原则列明“社会存在社会意识”；唯物史观角度还要求如实反映社会矛盾和人民需求。",
        "question_prompt": "从哲学角度，谈谈为什么“真实”往往具有直抵人心的力量。",
        "why_trigger": "细则明确把社会存在与社会意识列入可酌情得分角度，并要求从真实反映社会矛盾和人民需求展开。",
        "answer_landing": "真实内容之所以能打动人，是因为它如实反映社会存在、社会矛盾和人民需求，形成能够回应现实生活的社会意识。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式评分细则page_005 Q21角度3写明“实事求是、实践与认识、发展观、科学思维（辩证思维动态性等）”。",
        "question_prompt": "结合材料，综合运用所学，谈谈对科学制定和接续实施五年规划这一政治优势的理解。",
        "why_trigger": "材料写规划在实施中根据新问题、新趋势、新机遇不断优化，细则又直接列出“实践与认识”，可进入实践认识总节点。",
        "answer_landing": "五年规划在实践中形成、实施并根据新情况优化，体现了实践与认识的互动统一，使规划不断贴合国家发展实际。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式评分细则page_005 Q21角度2为“全过程人民民主”，变通写明“人民至上/人民群众观点等”。",
        "question_prompt": "结合材料，综合运用所学，谈谈对科学制定和接续实施五年规划这一政治优势的理解。",
        "why_trigger": "细则把五年规划编制中的开门问策、集思广益和全过程人民民主与人民群众观点相连。",
        "answer_landing": "科学制定五年规划要坚持人民群众观点，广泛听取人民意见、凝聚共识，使规划反映人民需要并服务人民利益。",
    },
]


BOUNDARY_ROWS = [
    ("Q1", "文化/精神动力选择题", "必胜信念/民族复兴精神动力", "正式答案键1C；正确项②④强调民族复兴追求和精神动力，但未形成稳定哲学节点证据，不把精神动力偷换为意识能动正文。", "正式答案键+试卷原题", "CULTURE_SPIRITUAL_POWER_BOUNDARY_NO_PHILOSOPHY_BODY"),
    ("Q2", "经济与开放选择题", "企业出海/开放格局", "正式答案键2B；题面为中国企业出海、开放格局和国际市场，属于经济与开放模块。", "正式答案键+试卷原题", "MODULE_BOUNDARY_EXCLUDED_BATCH33_XICHENG_FINAL"),
    ("Q6", "法律选择题", "无障碍视听作品/著作权/公共利益", "正式答案键6C；法律与生活中的著作权、许可使用和公共利益问题，不进入必修四哲学正文。", "正式答案键+试卷原题", "MODULE_BOUNDARY_EXCLUDED_BATCH33_XICHENG_FINAL"),
    ("Q7", "法律选择题", "民事诉讼/证据责任", "正式答案键7D；考查民事诉讼和证据责任，边界排除。", "正式答案键+试卷原题", "MODULE_BOUNDARY_EXCLUDED_BATCH33_XICHENG_FINAL"),
    ("Q8", "逻辑与思维选择题", "判断/推理/联言判断", "正式答案键8B；园林城市题考查选必三逻辑判断，不进入必修四哲学正文。", "正式答案键+试卷原题", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q9", "逻辑与思维选择题", "三段论结构", "正式答案键9D；考查三段论大小前提和结论，边界排除。", "正式答案键+试卷原题", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q10", "政治选择题", "调查研究/党的作风/执政基础", "正式答案键10B；正确项①④为作风建设和服务群众，未选第一手材料项③，不能作为实践认识客观挂点。", "正式答案键+试卷原题", "POLITICAL_PARTY_BUILDING_BOUNDARY_EXCLUDED"),
    ("Q11", "政治与法治选择题", "柔性执法/协同治理", "正式答案键11A；规范柔性执法和社会治理语境，不转写为哲学价值观节点。", "正式答案键+试卷原题", "POLITICAL_LAW_BOUNDARY_EXCLUDED"),
    ("Q12", "经济选择题", "火车票价/差别定价", "正式答案键12C；考查价格、资源配置和公共服务，属于经济模块。", "正式答案键+试卷原题", "ECONOMICS_BOUNDARY_EXCLUDED"),
    ("Q13", "经济选择题", "专利产业化/生产力", "正式答案键13D；专利产业化、资金市场法律约束等经济创新问题，不进入哲学正文。", "正式答案键+试卷原题", "ECONOMICS_BOUNDARY_EXCLUDED"),
    ("Q14", "经济选择题", "中国制造/国际标准/产业链", "正式答案键14C；制造业标准、国际产业链和政策支持，属于经济与开放模块。", "正式答案键+试卷原题", "ECONOMICS_BOUNDARY_EXCLUDED"),
    ("Q15", "国际政治选择题", "国际调解院/全球治理", "正式答案键15A；国际组织、国际法与全球治理语境，不进入必修四哲学正文。", "正式答案键+试卷原题", "INTERNATIONAL_POLITICS_BOUNDARY_EXCLUDED"),
    ("Q16(1)-culture", "文化主观题非哲学点", "中华优秀传统文化/文化自信/国际传播", "正式评分细则page_001 Q16(1)除人民群众外，其余角度为时代主题、优秀传统文化、国际传播影响力，作为文化模块边界登记。", "正式评分细则", "CULTURE_POINTS_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q17", "法律与生活主观题", "反不正当竞争/未成年人保护/诚信原则", "正式评分细则page_002-page_003限定反不正当竞争法、未成年人保护法、法律事实和价值分析；道德/价值观表述处在法律评价维度中，不转写为哲学正文。", "正式评分细则", "MODULE_BOUNDARY_EXCLUDED_BATCH33_XICHENG_FINAL"),
    ("Q18", "政治与法治主观题", "检察机关/人大监督/全过程人民民主/协同共治", "正式评分细则page_003限定政治与法治主体作用；人民群众相关语汇服务政治制度分析，不进入哲学正文。", "正式评分细则", "POLITICAL_LAW_BOUNDARY_EXCLUDED"),
    ("Q19(1)", "经济主观题", "投资于物/投资于人/新质生产力/内需", "正式评分细则page_004为经济模块供给、分配、消费和高质量发展，不进入必修四哲学正文。", "正式评分细则", "ECONOMICS_BOUNDARY_EXCLUDED"),
    ("Q19(2)", "逻辑与思维主观题", "不完全归纳推理", "正式评分细则page_004限定不完全归纳推理及提高可靠性措施，属于选必三逻辑边界。", "正式评分细则", "XUANBISAN_LOGIC_BOUNDARY_EXCLUDED"),
    ("Q20", "当代国际政治与经济主观题", "全球气候治理/中国方案", "正式评分细则page_004-page_005为全球气候治理、中国角色、国际责任和治理效果，不进入必修四哲学正文。", "正式评分细则", "XUANBIYI_BOUNDARY_EXCLUDED"),
    ("Q21-nonphilosophy", "综合主观题非哲学点", "党的领导/全过程人民民主/制度优势/科学思维", "正式评分细则page_005 Q21还支持党的领导、全过程人民民主、科学思维等角度；本批只把人民群众、实事求是、实践认识和发展观登记为哲学节点。", "正式评分细则+评标PPT slide 12", "NON_PHILOSOPHY_POINTS_BOUNDARY_EXCLUDED_BATCH33_XICHENG_FINAL"),
]


EVIDENCE_BY_KEY = {
    ("Q3", "认识发展原理"): ("正式答案键3A；正确项①“促进人们认识能力的提高”，仅作选择题客观挂点。", "objective-choice-only-teacher-answer-key"),
    ("Q3", "实践与认识（总）"): ("正式答案键3A；正确项②“加快实践与认识的循环过程”，仅作选择题客观挂点。", "objective-choice-only-teacher-answer-key"),
    ("Q4", "矛盾的普遍性和特殊性"): ("正式答案键4D；正确项把不同古诗词的个性化描写与江豚生存的一般规律相连，仅作选择题客观挂点。", "objective-choice-only-teacher-answer-key"),
    ("Q5", "联系的普遍性 / 联系的观点（总）"): ("正式答案键5C；正确项直接写国家间联系的普遍性和客观性，仅作选择题客观挂点。", "objective-choice-only-teacher-answer-key"),
    ("Q16(1)", "人民群众"): ("正式评分细则page_001 Q16(1)角度1变通写明“人民群众是精神财富的创造者，要坚持人民主体”。", "formal-rubric-term-support"),
    ("Q16(2)", "物质决定意识"): ("正式评分细则page_002 Q16(2)唯物论角度写明“世界统一于物质（物质决定意识）”。", "formal-rubric"),
    ("Q16(2)", "主观能动性 / 意识的能动作用"): ("正式评分细则page_002 Q16(2)唯物论角度写明正确意识有效发挥能动作用、正确指导实践。", "formal-rubric"),
    ("Q16(2)", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("正式评分细则page_002写明追求真实就是实现主观与客观事实相符合。", "formal-rubric"),
    ("Q16(2)", "真理观"): ("正式评分细则page_002认识论角度写明追求真理是人类认识活动根本任务，并在酌情原则列出真理最基本属性。", "formal-rubric"),
    ("Q16(2)", "实践是认识的基础"): ("正式评分细则page_002认识论角度写明扎根实践、经实践检验获得真实认识才能获得真理。", "formal-rubric"),
    ("Q16(2)", "认识对实践的反作用"): ("正式评分细则page_002认识论角度写明真实认识对实践具有促进作用。", "formal-rubric"),
    ("Q16(2)", "矛盾的普遍性和特殊性"): ("正式评分细则page_002辩证法角度写明矛盾普遍性和特殊性相互联结。", "formal-rubric"),
    ("Q16(2)", "人民群众"): ("正式评分细则page_002唯物史观角度写明人民群众是历史的主体、从群众中来到群众中去。", "formal-rubric"),
    ("Q16(2)", "价值观的导向作用"): ("正式评分细则page_002价值观角度写明价值观对认识世界改造世界有重要导向作用。", "formal-rubric"),
    ("Q16(2)", "价值判断与价值选择"): ("正式评分细则page_002价值观角度写明引导人们作出正确价值判断与选择。", "formal-rubric"),
    ("Q16(2)", "社会存在与社会意识"): ("正式评分细则page_002酌情原则列明“社会存在社会意识”。", "formal-rubric-term-support"),
    ("Q21", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("正式评分细则page_005 Q21角度3列出“实事求是”。", "formal-rubric"),
    ("Q21", "实践与认识（总）"): ("正式评分细则page_005 Q21角度3列出“实践与认识”。", "formal-rubric-term-support"),
    ("Q21", "发展的观点 / 发展的普遍性"): ("正式评分细则page_005 Q21角度3列出“发展观”。", "formal-rubric"),
    ("Q21", "人民群众"): ("正式评分细则page_005 Q21角度2变通写明“人民至上/人民群众观点等”。", "formal-rubric-term-support"),
}


def current_docx() -> Path:
    return base.current_docx()


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS)).strip()


def style_val(p) -> str:
    vals = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return vals[0] if vals else ""


def parse_question_no(heading: str) -> str:
    m = re.search(r"第(\d+)题(?:第（(\d+)）问)?", heading)
    if not m:
        return "Q?"
    return f"Q{m.group(1)}" + (f"({m.group(2)})" if m.group(2) else "")


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
    p = etree.fromstring(etree.tostring(template))
    set_para_text(p, text)
    return p


def load_docx_xml(docx: Path):
    with zipfile.ZipFile(docx, "r") as zf:
        return etree.fromstring(zf.read("word/document.xml"))


def update_docx(timestamp: str) -> tuple[Path, int]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_batch33_2026_xicheng_final_{timestamp}{docx.suffix}")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as zin:
        xml = zin.read("word/document.xml")
    root = etree.fromstring(xml)
    body = root.find(f"{W}body")
    paras = body.findall(f"{W}p")
    existing_signature = {(e["canonical_node"], e["question_no"]) for e in extract_entries_from_root(root)}
    inserted = 0
    for spec_item in NEW_ENTRY_SPECS:
        signature = (spec_item["canonical_node"], spec_item["question_no"])
        if signature in existing_signature:
            continue
        node = spec_item["canonical_node"]
        heading = f"{base.next_heading_number(paras, node)}. {SUITE} {spec_item['question_label']}"
        heading_template, body_template = base.template_paragraphs(paras, node)
        _start, end = base.find_node_bounds(paras, node)
        insert_index = body.index(paras[end - 1]) + 1
        new_paras = [
            clone_with_text(heading_template, heading),
            clone_with_text(body_template, f"【材料触发点】{spec_item['material_trigger']}"),
            clone_with_text(body_template, f"【设问】{spec_item['question_prompt']}"),
            clone_with_text(body_template, f"【为什么能想到】{spec_item['why_trigger']}"),
            clone_with_text(body_template, f"【答案落点】{spec_item['answer_landing']}"),
        ]
        for offset, p in enumerate(new_paras):
            body.insert(insert_index + offset, p)
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch33_2026_xicheng_final_{timestamp}{LEDGER.suffix}")
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
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch33_2026_xicheng_final_{timestamp}{ACCEPTED.suffix}")
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
                "source_lane": "Codex Batch33 Xicheng final registration and insertion",
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
        "证据等级": "正式答案键+试卷原题（客观选择题）" if is_objective else ("正式评分标准宽角度/术语支持" if is_broad else "正式评分标准"),
        "是否误放": "否：保留但标注宽角度或客观挂点" if (is_objective or is_broad) else "否",
        "是否需补厚": "否",
        "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else ("KEEP_IN_BODY_WITH_BROAD_FORMAL_SUPPORT" if is_broad else "KEEP_IN_BODY"),
        "备注": "Batch33登记；普通参考答案只作题面/答案键核对，未冒充主观评分细则。",
        "source_artifact": SOURCE_PACKET,
    }


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch33_2026_xicheng_final_{timestamp}{MATRIX.suffix}")
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
            row["current_status"] = "covered_by_batch33_recovery_matrix"
            row["blocker_or_next_action"] = "Batch33 inserted/registered formal-rubric and objective-choice entries plus question-level boundary rows; render/model gates pending."
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

## Batch33 Update

- `2026西城期末` is now covered by `COVERAGE_FUSION_BATCH33_2026_XICHENG_FINAL_CODEX_20260525.md`.
- Matrix rows for the suite: `{matrix_rows_for_suite}`.
- Current DOCX governed entries for the suite: `{docx_entries}`.
- Render QA and ClaudeCode Opus 4.7 recheck are still separate gates.
- `2026石景山期末` remains a special excluded source unless the user supplies a usable scoring rubric.
""", encoding="utf-8", newline="\n")
    return {"remaining_missing": len(missing), "covered": len(covered), "total": len(rows)}


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    body_list = "\n".join(f"- {e['question_no']} -> {e['canonical_node']} -> {e['registered_heading']}" for e in entries)
    SOURCE_TRANSCRIPTION.write_text(f"""# Batch33 Source Transcription - 2026西城期末

status: `SOURCE_PACKET_REGISTERED`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- formal scoring/rubric cache: `{RUBRIC_SOURCE}`
- raw rubric PDF: `{RAW_RUBRIC_PDF}`
- raw teacher PDF: `{RAW_TEACHER_PDF}`
- marking PPTX: `{RAW_PINGBIAO_PPTX}`
- rubric OCR transcription: `{RUBRIC_OCR_TEXT}`
- rubric OCR line index: `{RUBRIC_OCR_LINES}`
- teacher OCR transcription: `{TEACHER_OCR_TEXT}`
- teacher OCR line index: `{TEACHER_OCR_LINES}`
- marking PPT transcription: `{PINGBIAO_TRANSCRIPTION}`
- raw source render manifest: `{SOURCE_RENDER_MANIFEST}`

## Key Evidence

- Formal answer key from rubric PDF: `1C, 2B, 3A, 4D, 5C, 6C, 7D, 8B, 9D, 10B, 11A, 12C, 13D, 14C, 15A`.
- Q3-Q5 enter only as objective-choice hooks where the correct option text explicitly carries a philosophy trigger.
- Q16(1) enters only on the formal rubric's people-subject variant; other culture-confidence points remain boundary rows.
- Q16(2) formal scoring page_002 supports materialism, truth, practice/knowledge, contradiction, people, value and social existence/social consciousness points.
- Q21 formal scoring page_005 supports实事求是、实践与认识、发展观 and人民群众观点; party leadership and political-system points remain boundary rows.
- Q17-Q20 and most choice questions are boundary-excluded as法律与生活、政治与法治、经济、国际政治 or逻辑与思维.

## Governed DOCX Body Entries

{body_list}

## Evidence Guardrail

- 普通参考答案没有冒充评分细则。
- 选择题只登记为客观答案键证据。
- 主观题正文条只使用正式评分标准/细则支持。
""", encoding="utf-8", newline="\n")


def append_control_reports(inserted: int, entries: list[dict[str, str]], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    appendix = f"""

## Batch33 Local Application: 2026西城期末
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries after Batch33: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch33: `{global_result['remaining_missing']}`.
- Render QA is pending for this batch.
- ClaudeCode Opus 4.7 recheck is pending for this batch; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final; `STRICT_FINAL_ACCEPTED` is not claimed.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch33 Local Application: 2026西城期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")
    qa_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch33 Pending Render QA: 2026西城期末"
    if marker in qa_text:
        qa_text = qa_text[: qa_text.index(marker)]
    FORMAT_QA.write_text(qa_text + f"""

## Batch33 Pending Render QA: 2026西城期末
Updated: 2026-05-25

- Status: `RENDER_PENDING_AFTER_DOCX_MODIFICATION`.
- Batch33 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required next check: current DOCX/PDF render, heading styles, page count, labels, and new/old entry consistency.
""", encoding="utf-8", newline="\n")
    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH33_XICHENG_FINAL_RECHECK"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    MODEL_LEDGER.write_text(ledger + """

## CLAUDECODE_BATCH33_XICHENG_FINAL_RECHECK

status: `real_call_pending`

- Batch: `2026西城期末`.
- Prompt: `OPUS47_CLAUDECODE_BATCH33_2026_XICHENG_FINAL_RECHECK_PROMPT.md`.
- Required command shape: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Model gate before real evidence: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output is not qualified ClaudeCode evidence.
""", encoding="utf-8", newline="\n")


def write_batch_report(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    BATCH_REPORT.write_text(f"""# Coverage Fusion Batch33 - 2026西城期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch33 edit: `{backup}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `2026西城期末` after Batch33: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `2026西城期末`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch33: `{global_result['remaining_missing']}`.

## Placement Verdict

- Q3-Q5 enter only as objective-choice body hooks with evidence level `正式答案键+试卷原题（客观选择题）`.
- Q16(1) enters only for the formal people-subject/rich spiritual wealth variant.
- Q16(2) enters through formal scoring support for materialism, truth, practice/knowledge, contradiction, people, value and social existence/social consciousness.
- Q21 enters through formal scoring support for实事求是、实践与认识、发展观 and人民群众观点.
- Q1-Q2, Q6-Q15, Q17-Q20 and non-philosophy parts of Q16/Q21 are boundary-excluded.
- Ordinary teacher reference answers are kept as context only and do not substitute for formal scoring text.

## Remaining Gates

- Render QA is pending because Batch33 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final; `STRICT_FINAL_ACCEPTED` is not claimed.
""", encoding="utf-8", newline="\n")


def main() -> None:
    for required in [
        GPT_BUNDLE,
        RUBRIC_SOURCE,
        RAW_RUBRIC_PDF,
        RAW_TEACHER_PDF,
        RAW_PINGBIAO_PPTX,
        RUBRIC_OCR_TEXT,
        RUBRIC_OCR_LINES,
        TEACHER_OCR_TEXT,
        TEACHER_OCR_LINES,
        PINGBIAO_TRANSCRIPTION,
        SOURCE_RENDER_MANIFEST,
        MATRIX,
        LEDGER,
        ACCEPTED,
    ]:
        if not required.exists():
            raise FileNotFoundError(required)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    root = load_docx_xml(current_docx())
    entries = extract_entries_from_root(root)
    if len(entries) != EXPECTED_ENTRIES:
        raise RuntimeError(f"Expected {EXPECTED_ENTRIES} governed {SUITE} entries after Batch33, found {len(entries)}")
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
