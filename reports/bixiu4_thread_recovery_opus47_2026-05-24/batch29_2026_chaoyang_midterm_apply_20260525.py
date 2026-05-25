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

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH29_2026_CHAOYANG_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH29_2026_CHAOYANG_MIDTERM_CODEX_20260525.md"

PREPROCESSED = ROOT / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2026各区模拟题__2026各区期末和期中__2026朝阳期中.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "885e694cf464c22b_2026朝阳期中细则.md"
RUBRIC_DUP = PREPROCESSED / "gpt_sources" / "885e694cf464c22b_2025.11朝阳期中政治评标.md"
PAPER_SOURCE = PREPROCESSED / "gpt_sources" / "5a53b5c6863d7f95_2025北京朝阳高三_上_期中政治_教师版.md"

SUITE = "2026朝阳期中"
YEAR = "2026"
STAGE = "期中"
BATCH_ID = "batch29_2026_chaoyang_midterm"
MATRIX_SOURCE = "codex_batch29_2026_chaoyang_midterm"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; duplicate rubric cache: {RUBRIC_DUP}; {PAPER_SOURCE}; "
    "teacher-version answer key lines 580-585; Q4 paper lines 373-380; Q7 paper lines 399-410; "
    "Q14 paper lines 455-461; Q18 prompt/rubric lines 52-85; Q19 prompt/rubric lines 87-104; "
    "current DOCX verified: 11 existing unregistered 2026朝阳期中 headings were present before Batch29"
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q7",
        "question_label": "第7题（选择题）",
        "material_trigger": "教师版答案键第7题为D；正确题肢③明确“从具体实际出发，深入挖掘城市内涵，推动城市创新发展”。",
        "question_prompt": "北京市前门商圈以“老字号+国潮”、国粹体验、茉莉花茶推广和科技赋能中轴线等方式推动城市内涵式发展。",
        "why_trigger": "前门商圈的更新不是抽象扩张，而是从中轴线、老字号、国粹体验和现实消费场景出发，挖掘本地文化资源。",
        "answer_landing": "本题只作客观选择题挂点。推动城市内涵式发展要从具体实际出发，立足前门商圈的历史文化资源和现实消费需求，通过文化挖掘与科技赋能推动创新发展。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q14",
        "question_label": "第14题（选择题）",
        "material_trigger": "教师版答案键第14题为B；正确题肢①说天气谚语“在生活实践中产生，又反作用于生活实践”。",
        "question_prompt": "天气谚语是劳动人民通过口述和笔记代代相传的经验总结，用来对天气情况进行预测。",
        "why_trigger": "天气谚语来自长期生活实践和经验归纳，又被用于指导人们预测天气、安排生活生产。",
        "answer_landing": "本题只作客观选择题挂点。天气谚语来源于生活实践，是劳动人民实践经验的概括；它又能反作用于生活实践，帮助人们预判天气、安排活动。",
    },
    {
        "canonical_node": "规律的客观性",
        "question_no": "Q18",
        "question_label": "第18题（主观题）",
        "material_trigger": "正式评分细则第57-59行在支持理由中列“按规律办事/从实际出发/矛盾特殊性或具体问题具体分析等”。",
        "question_prompt": "第18题要求从哲学角度思考是否应该使用AI提供情绪价值。",
        "why_trigger": "AI情绪陪伴能否发挥作用，要受到人的情绪调节规律、现实交往规律和技术工具局限的制约。",
        "answer_landing": "可以有条件使用AI提供情绪价值，但必须按客观规律办事。既要看到AI作为工具可辅助疏导情绪，也要尊重人类情感理解和真实交往的规律，不能把AI替代现实关系。",
    },
    {
        "canonical_node": "物质决定意识",
        "question_no": "Q18",
        "question_label": "第18题（主观题）",
        "material_trigger": "正式评分细则第60-62行在反对理由中列“意识依赖于物质”。",
        "question_prompt": "材料指出AI在情感共情和动机共情方面存在缺陷，无法真正理解或共鸣人类情感。",
        "why_trigger": "人的情感、意识和共情能力依赖现实的人脑、身体经验和社会交往实践，不能由算法模拟完全替代。",
        "answer_landing": "反对把AI情绪陪伴当作真实人际关系的替代品，因为意识依赖于物质。AI缺少人的生命体验、现实关系和共情基础，难以真正理解人类情感。",
    },
    {
        "canonical_node": "量变与质变 / 适度原则",
        "question_no": "Q18",
        "question_label": "第18题（主观题）",
        "material_trigger": "正式评分细则第60-62行在反对理由中列“适度原则”。",
        "question_prompt": "材料说AI短期内能抚慰情绪，但长期依赖会削弱真实互动能力、模糊现实与虚拟界限。",
        "why_trigger": "AI情绪陪伴从偶尔辅助到长期依赖会发生性质变化，关键是把握使用的度。",
        "answer_landing": "使用AI提供情绪价值要坚持适度原则。把AI作为短期辅助可以缓解压力，但过度依赖会削弱现实交往能力，因此要把握限度、防止辅助工具变成逃避现实的依赖。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q18",
        "question_label": "第18题（主观题）",
        "material_trigger": "正式评分细则第60-62行在反对理由中列“实践等”。",
        "question_prompt": "材料强调长期退回AI安全情绪泡泡会让人不愿面对复杂现实冲突，削弱与他人真实互动的能力。",
        "why_trigger": "情绪调适和关系修复最终要回到现实交往实践中完成，不能停留在虚拟互动和工具回应里。",
        "answer_landing": "AI可以提供辅助性情绪疏导，但认识和能力的形成要回到实践。人应在真实互动中理解他人、处理冲突、提升情绪调节能力，不能用虚拟回应替代现实实践。",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q18",
        "question_label": "第18题（主观题）",
        "material_trigger": "正式评分细则第63-66行在“如何做”中列“正确价值观的导向作用”。",
        "question_prompt": "第18题要求针对是否应该使用AI提供情绪价值提出哲学思考和做法。",
        "why_trigger": "AI情绪陪伴涉及科技向善、人的真实成长、现实交往能力等价值方向。",
        "answer_landing": "使用AI提供情绪价值要发挥正确价值观的导向作用，坚持科技服务人的健康成长，让AI成为辅助疏导工具，而不是引导人逃避现实关系、沉溺虚拟安慰。",
    },
    {
        "canonical_node": "认识对实践的反作用",
        "question_no": "Q19",
        "question_label": "第19题（主观题）",
        "material_trigger": "正式评分细则第98-99行把“正确认识对实践的反作用”列为弘扬抗战精神的哲学角度。",
        "question_prompt": "第19题要求运用《哲学与文化》知识，为“继承和弘扬伟大抗战精神”特刊写卷首语。",
        "why_trigger": "对抗战精神内涵的正确认识，会转化为新时代继承弘扬、强国复兴的行动方向。",
        "answer_landing": "要形成对抗战精神的正确认识，并用这种认识指导新时代实践。把爱国情怀、民族气节、英雄气概和必胜信念转化为强国建设、民族复兴的实际行动。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q19",
        "question_label": "第19题（主观题）",
        "material_trigger": "正式评分细则第98-99行把“正确意识的能动作用”列为弘扬抗战精神的哲学角度。",
        "question_prompt": "素材三引用习近平总书记对伟大抗战精神丰富内涵的阐释，并要求新时代继承和弘扬。",
        "why_trigger": "抗战精神作为正确意识和精神力量，能激励人们主动投身新时代奋斗。",
        "answer_landing": "弘扬抗战精神要发挥正确意识的能动作用。以爱国情怀、民族气节、英雄气概和必胜信念激励青年主动担当，把精神力量转化为砥砺前行的行动自觉。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q19",
        "question_label": "第19题（主观题）",
        "material_trigger": "正式评分细则第100-102行把“联系的观点”列为如何弘扬抗战精神的哲学角度。",
        "question_prompt": "材料把古代家国情怀、全民族抗战实践、习近平总书记对抗战精神的阐释和新时代弘扬要求联系起来。",
        "why_trigger": "抗战精神不是孤立口号，而是历史传统、抗战实践、民族精神和新时代使命之间的联系。",
        "answer_landing": "弘扬抗战精神要坚持联系观点，把中华民族家国传统、全民族抗战实践和新时代强国复兴使命联系起来理解，使伟大精神在现实奋斗中延续。",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q19",
        "question_label": "第19题（主观题）",
        "material_trigger": "正式评分细则第100-102行把“发展的观点”列为如何弘扬抗战精神的哲学角度。",
        "question_prompt": "素材三要求从中华民族精神的发展和全民族抗战实践方面深刻领会抗战精神内涵。",
        "why_trigger": "抗战精神是中华民族精神在特定历史条件下的发展形态，新时代继承弘扬也要随着实践发展不断展开。",
        "answer_landing": "弘扬抗战精神要坚持发展的观点。既看到它是中华民族精神在抗战实践中的发展升华，也要在新时代强国建设中不断继承、弘扬和发展其精神价值。",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q19",
        "question_label": "第19题（主观题）",
        "material_trigger": "正式评分细则第100-102行把“矛盾的观点”列为如何弘扬抗战精神的哲学角度。",
        "question_prompt": "第19题要求在继承和弘扬伟大抗战精神的卷首语中处理历史与现实、精神传承与实践奋斗的关系。",
        "why_trigger": "弘扬抗战精神需要把历史记忆与现实使命、精神传承与实践行动统一起来，而不是停留在单一纪念或抽象赞美。",
        "answer_landing": "从矛盾观点看，弘扬抗战精神要把历史传承和现实奋斗统一起来，既铭记抗战岁月形成的精神内核，又把这种精神转化为新时代解决现实问题、推进民族复兴的力量。",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q19",
        "question_label": "第19题（主观题）",
        "material_trigger": "正式评分细则第100-102行把“价值判断与价值选择的标准”列为如何弘扬抗战精神的哲学角度。",
        "question_prompt": "第19题围绕继承和弘扬伟大抗战精神，要求写出面向新时代的卷首语。",
        "why_trigger": "抗战精神中的爱国情怀、民族气节、英雄气概和必胜信念体现正确价值判断和价值选择标准。",
        "answer_landing": "弘扬抗战精神要作出正确价值判断和价值选择，坚持国家民族利益和人民立场，把个人理想融入强国建设和民族复兴，在新时代延续爱国奋斗。",
    },
]


BOUNDARY_ROWS = [
    ("Q1", "经济与社会选择题", "国有企业、改革活力、资源配置效率", "教师版第342-350行及答案键第584-585行；属经济与社会，不进入哲学正文。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q2", "经济与社会选择题", "新型消费基础设施、消费场景、就业", "教师版第351-358行及答案键第584-585行；属经济与社会，不进入哲学正文。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q3", "当代国际政治与经济选择题", "全球治理倡议、国际公共产品、全球治理体系", "教师版第362-368行及答案键第584-585行；虽有“守正创新”表述，但主旨为全球治理倡议，不作为哲学正文挂点。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q5", "经济/社会治理选择题", "银发经济、养老保障、政府职责", "教师版第381-389行及答案键第584-585行；主旨为养老保障政策，不进入哲学正文。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q6", "当代国际政治与经济选择题", "巴黎协定、绿色发展、共同但有区别责任", "教师版第390-398行及答案键第584-585行；主旨为国际气候治理，不进入哲学正文。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q7-culture", "选择题中的文化/经济点", "文化价值与经济价值统一、城市商业文化", "第7题仅把正确题肢③登记为客观哲学挂点；题肢④等文化经济内容不进入哲学正文。", "教师版试卷+答案键", "CULTURE_ECONOMY_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q8", "文化选择题", "科学家精神、文化育人、理想信念", "教师版第411-417行及答案键第584-585行；属文化育人和科学家精神，不进入哲学正文。", "教师版试卷+答案键", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q9", "文化/民族共同体选择题", "物质力量、精神力量、中华民族共同体", "教师版第418-424行及答案键第584-585行；主旨为民族共同体文化认同，不进入哲学正文。", "教师版试卷+答案键", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q10", "文化选择题", "文物活化、数字化、文化发展", "教师版第425-429行及答案键第584-585行；属文化传承与创新，不进入哲学正文。", "教师版试卷+答案键", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q11", "逻辑与思维选择题", "三段论补大前提", "教师版第430-436行及答案键第584-585行；属逻辑与思维，不进入哲学正文。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q12", "逻辑与思维选择题", "逻辑规则、概念划分、矛盾律", "教师版第437-446行及答案键第584-585行；属逻辑与思维，不进入哲学正文。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q13", "逻辑与思维选择题", "类比推理、联想思维、感性具体与思维抽象", "教师版第447-454行及答案键第584-585行；属逻辑与思维，不进入哲学正文。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q14-logic", "选择题中的逻辑点", "不完全归纳、或然性", "第14题仅把正确题肢①登记为客观哲学挂点；题肢④的或然推理属于逻辑与思维边界。", "教师版试卷+答案键", "LOGIC_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q15", "逻辑与思维选择题", "联言判断否定、关系判断", "教师版第462-468行及答案键第584-585行；属逻辑与思维，不进入哲学正文。", "教师版试卷+答案键", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q16", "经济与社会主观题", "绿色金融、高质量发展、绿色转型", "教师版第471-485行及参考答案第588-590行；属经济与社会，不进入哲学正文。", "教师版试卷+参考答案", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q17", "当代国际政治与经济主观题", "人工智能+、自主开放、发展安全、中国世界", "教师版第486-516行及参考答案第591-593行；属当代国际政治与经济，不进入哲学正文。", "教师版试卷+参考答案", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q19-culture", "文化主观题点", "民族精神、爱国主义、革命文化、文化功能、双创", "正式细则第88-97、100-101行列文化角度；当前交付为哲学正文，文化点登记边界。", "正式细则边界", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q20", "逻辑与思维主观题", "辩证思维方法、分析综合、质量互变、动态性思维", "正式细则第108-124行明确知识板块为辩证思维方法；不把选必三逻辑思维题偷换为必修四哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
    ("Q21", "经济/文化/逻辑主观题", "人文经济学、文化传承与创新、创新思维", "正式细则第126-160行分别按经济与社会、文化传承与创新、逻辑与思维评分，不进入哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH29_CHAOYANG_MIDTERM"),
]


EVIDENCE_BY_KEY = {
    ("Q4", "联系的多样性"): ("教师版第373-380行+答案键第584-585行：第4题答案A，正确题肢①为把握联系的多样性", "objective-choice-only-teacher-answer-key"),
    ("Q7", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("教师版第399-410行+答案键第584-585行：第7题答案D，正确题肢③为从具体实际出发", "objective-choice-only-teacher-answer-key"),
    ("Q14", "实践与认识（总）"): ("教师版第455-461行+答案键第584-585行：第14题答案B，正确题肢①为生活实践中产生并反作用于生活实践", "objective-choice-only-teacher-answer-key"),
    ("Q18", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("正式评分细则第57-59、69-71行：支持理由列从实际出发，并要求结合用户需求调整对话模式", "formal-rubric"),
    ("Q18", "规律的客观性"): ("正式评分细则第57-59、69-71行：支持理由列按规律办事", "formal-rubric"),
    ("Q18", "矛盾的特殊性 / 具体问题具体分析"): ("正式评分细则第57-59、69-71行：支持理由列矛盾特殊性或具体问题具体分析", "formal-rubric"),
    ("Q18", "主观能动性 / 意识的能动作用"): ("正式评分细则第60-62、78-81行：反对理由列主观能动性，并指向过度依赖削弱现实交往能力", "formal-rubric"),
    ("Q18", "物质决定意识"): ("正式评分细则第60-62行：反对理由列意识依赖于物质", "formal-rubric"),
    ("Q18", "量变与质变 / 适度原则"): ("正式评分细则第60-62、78-81行：反对理由列适度原则", "formal-rubric"),
    ("Q18", "实践与认识（总）"): ("正式评分细则第60-62、78-81行：反对理由列实践等，并指向现实交往能力", "formal-rubric-broad-angle"),
    ("Q18", "辩证否定 / 守正创新"): ("正式评分细则第63-66、72-85行：如何做列辩证否定观", "formal-rubric"),
    ("Q18", "价值观的导向作用"): ("正式评分细则第63-66、72-85行：如何做列正确价值观的导向作用", "formal-rubric"),
    ("Q18", "价值判断与价值选择"): ("正式评分细则第63-66、72-85行：如何做列价值判断价值选择", "formal-rubric"),
    ("Q18", "矛盾的普遍性"): ("正式评分细则第54-56行：总说列矛盾的普遍性/一分为二/全面观点", "formal-rubric"),
    ("Q18", "矛盾就是对立统一"): ("正式评分细则第54-56行：总说列对立统一/一分为二/全面观点", "formal-rubric"),
    ("Q19", "社会存在与社会意识"): ("正式评分细则第98-99行：为什么弘扬列正确社会意识的推动作用", "formal-rubric"),
    ("Q19", "价值观的导向作用"): ("正式评分细则第98-99行：为什么弘扬列正确价值观的导向作用", "formal-rubric"),
    ("Q19", "认识对实践的反作用"): ("正式评分细则第98-99行：为什么弘扬列正确认识对实践的反作用", "formal-rubric"),
    ("Q19", "主观能动性 / 意识的能动作用"): ("正式评分细则第98-99行：为什么弘扬列正确意识的能动作用", "formal-rubric"),
    ("Q19", "实践与认识（总）"): ("正式评分细则第100-102行：如何弘扬列立足实践、知行合一", "formal-rubric"),
    ("Q19", "联系的普遍性 / 联系的观点（总）"): ("正式评分细则第100-102行：如何弘扬列联系的观点", "formal-rubric-broad-angle"),
    ("Q19", "发展的观点 / 发展的普遍性"): ("正式评分细则第100-102行：如何弘扬列发展的观点", "formal-rubric-broad-angle"),
    ("Q19", "矛盾就是对立统一"): ("正式评分细则第100-102行：如何弘扬列矛盾的观点", "formal-rubric-broad-angle"),
    ("Q19", "价值判断与价值选择"): ("正式评分细则第100-102行：如何弘扬列价值判断与价值选择的标准", "formal-rubric"),
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
    entries.sort(key=lambda e: (int(re.sub(r"\D", "", e["question_no"]) or "999"), e["canonical_node"], e["registered_heading"]))
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
    backup = docx.with_name(f"{docx.stem}_backup_before_batch29_2026_chaoyang_midterm_{timestamp}{docx.suffix}")
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch29_2026_chaoyang_midterm_{timestamp}{LEDGER.suffix}")
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
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch29_2026_chaoyang_midterm_{timestamp}{ACCEPTED.suffix}")
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
                "source_lane": "Codex Batch29 Chaoyang midterm registration and insertion",
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
        "证据等级": "教师版答案键+试卷原题" if is_objective else ("正式细则宽角度/术语支持" if is_broad else "正式细则"),
        "是否误放": "否：保留但标注宽角度或术语支持" if is_broad else "否",
        "是否需补厚": "否",
        "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else ("KEEP_IN_BODY_WITH_BROAD_FORMAL_SUPPORT" if is_broad else "KEEP_IN_BODY"),
        "备注": "Batch29登记既有正文并补入缺漏；选择题只按教师版答案键作客观挂点，普通参考答案未冒充主观评分细则。",
        "source_artifact": SOURCE_PACKET,
    }


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch29_2026_chaoyang_midterm_{timestamp}{MATRIX.suffix}")
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
            "备注": "本题或本点不作为当前哲学宝典正文；不把经济、法律、逻辑、国际政治、文化或综合非哲学点偷换为哲学原理。",
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
            row["current_status"] = "covered_by_batch29_recovery_matrix"
            row["blocker_or_next_action"] = "Batch29 registered existing DOCX entries, inserted rubric-supported/objective-choice points, and added boundary rows; render/model gates pending."
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

## Batch29 Update

- `2026朝阳期中` is now covered by `COVERAGE_FUSION_BATCH29_2026_CHAOYANG_MIDTERM_CODEX_20260525.md`.
- Matrix rows for the suite: `{matrix_rows_for_suite}`.
- Current DOCX mentions for the suite: `{docx_entries}`.
- Render QA and ClaudeCode Opus 4.7 recheck are still separate gates.
- `2026石景山期末` remains a special excluded source unless the user supplies a usable scoring rubric.
""", encoding="utf-8", newline="\n")
    return {"remaining_missing": len(missing), "covered": len(covered), "total": len(rows)}


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    body_list = "\n".join(f"- {e['question_no']} -> {e['canonical_node']} -> {e['registered_heading']}" for e in entries)
    SOURCE_TRANSCRIPTION.write_text(f"""# Batch29 Source Transcription - 2026朝阳期中

status: `SOURCE_PACKET_REGISTERED`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- scoring/rubric cache: `{RUBRIC_SOURCE}`
- duplicate same-hash rubric cache: `{RUBRIC_DUP}`
- teacher-version paper/answer cache: `{PAPER_SOURCE}`

## Key Evidence

- Q4 objective row uses teacher answer key `4A`: correct option ① is `把握联系的多样性`. It is objective-only and not treated as a subjective scoring rubric.
- Q7 objective row uses teacher answer key `7D`: correct option ③ is `从具体实际出发`. It is objective-only.
- Q14 objective row uses teacher answer key `14B`: correct option ① is `在生活实践中产生，又反作用于生活实践`. It is objective-only.
- Q18 is directly supported by formal scoring lines 54-85: 矛盾普遍性/对立统一/全面观点、按规律办事、从实际出发、矛盾特殊性、主观能动性、意识依赖于物质、适度原则、实践、辩证否定、正确价值观、价值判断价值选择.
- Q19 is supported by formal scoring lines 87-104: 正确价值观、正确认识对实践、正确意识、正确社会意识、联系观点、发展观点、矛盾观点、立足实践知行合一、价值判断与价值选择标准.
- Q20 is boundary-excluded even though it names矛盾分析、质量互变、动态性等术语 because the formal source explicitly limits it to辩证思维方法/逻辑与思维.

## Governed DOCX Body Entries

{body_list}

## Evidence Guardrail

- 普通参考答案只用于客观题答案键和题面核对；第18、19题正文落点使用正式评标/阅卷细则，不把普通参考答案冒充评分细则。
- Q19 的联系、发展、矛盾等泛称角度在矩阵中标为 `正式细则宽角度/术语支持`，不夸大为逐点详细评分细则。
""", encoding="utf-8", newline="\n")


def append_control_reports(inserted: int, entries: list[dict[str, str]], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    appendix = f"""

## Batch29 Local Application: 2026朝阳期中
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries after Batch29: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch29: `{global_result['remaining_missing']}`.
- Render QA is pending for this batch.
- ClaudeCode Opus 4.7 recheck is pending for this batch; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch29 Local Application: 2026朝阳期中"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")
    qa_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch29 Pending Render QA: 2026朝阳期中"
    if marker in qa_text:
        qa_text = qa_text[: qa_text.index(marker)]
    FORMAT_QA.write_text(qa_text + f"""

## Batch29 Pending Render QA: 2026朝阳期中
Updated: 2026-05-25

- Status: `RENDER_PENDING_AFTER_DOCX_MODIFICATION`.
- Batch29 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required next check: current DOCX/PDF render, heading styles, page count, labels, and new/old entry consistency.
""", encoding="utf-8", newline="\n")
    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH29_CHAOYANG_MIDTERM_RECHECK"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    MODEL_LEDGER.write_text(ledger + """

## CLAUDECODE_BATCH29_CHAOYANG_MIDTERM_RECHECK

status: `real_call_pending`

- Batch: `2026朝阳期中`.
- Prompt: `OPUS47_CLAUDECODE_BATCH29_2026_CHAOYANG_MIDTERM_RECHECK_PROMPT.md`.
- Required command shape: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Model gate before real evidence: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output is not qualified ClaudeCode evidence.
""", encoding="utf-8", newline="\n")


def write_batch_report(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    BATCH_REPORT.write_text(f"""# Coverage Fusion Batch29 - 2026朝阳期中

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch29 edit: `{backup}`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `2026朝阳期中` after Batch29: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `2026朝阳期中`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch29: `{global_result['remaining_missing']}`.

## Placement Verdict

- `2026朝阳期中` had 11 existing Q4/Q18/Q19 DOCX headings but no recovery-matrix rows; Batch29 repaired that ledger/matrix gap.
- Objective-choice body rows are limited to Q4, Q7, and Q14, where the teacher-version answer key fixes the correct option and the option directly contains a 必修四 philosophy trigger.
- Q18 was completed from formal rubric rows for AI emotional-value use: 矛盾、规律/实际/特殊性、主观能动性/物质决定意识/适度/实践、辩证否定/价值观/价值选择.
- Q19 was completed from formal rubric rows for弘扬抗战精神；culture-only points are boundary-excluded.
- Q20 remains excluded because its formal source is 选必三《逻辑与思维》辩证思维方法, not 必修四哲学正文.

## Remaining Gates

- Render QA is pending because Batch29 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
""", encoding="utf-8", newline="\n")


def main() -> None:
    for required in [GPT_BUNDLE, RUBRIC_SOURCE, PAPER_SOURCE, MATRIX, LEDGER, ACCEPTED]:
        if not required.exists():
            raise FileNotFoundError(required)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    root = load_docx_xml(current_docx())
    entries = extract_entries_from_root(root)
    if len(entries) != 24:
        raise RuntimeError(f"Expected 24 governed {SUITE} entries after Batch29, found {len(entries)}")
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
