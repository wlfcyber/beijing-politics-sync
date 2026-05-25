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
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH23_2025_CHAOYANG_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH23_2025_CHAOYANG_FINAL_CODEX_20260525.md"

PREPROCESSED = Path.home() / "Desktop" / "beijing_politics_research" / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2025各区模拟题__2025各区期末__2025朝阳期末.md"
PPT_SCORING_SOURCE = PREPROCESSED / "gpt_sources" / "195324f05d7e2fea_朝阳高三期末2025.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "ec82917288aa8774_2025北京朝阳高三_上_期末政治_教师版.md"
PDF_RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "953eaee3f98d8598_2025朝阳期末细则.md"
PDF_RUBRIC_RENDER_DIR = PREPROCESSED / "renders" / "953eaee3f98d8598"

SUITE = "2025朝阳期末"
YEAR = "2025"
STAGE = "期末"
BATCH_ID = "batch23_2025_chaoyang_final"
MATRIX_SOURCE = "codex_batch23_2025_chaoyang_final"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {PPT_SCORING_SOURCE}; {TEACHER_SOURCE}; {PDF_RUBRIC_SOURCE}; "
    "current DOCX text verified before Batch23 insertion"
)

Q2_PROMPT = (
    "回荡在四合院上空清脆的鸽子哨声，作为北京城的“空中交响乐”，成为很多北京人记忆中地道的“北京声音”。"
    "但是，很多杂乱无章的鸽子笼严重影响城市环境。某区与专业设计机构合作，“一户一策”设计新的鸽子笼，"
    "顶部做成老房顶样式，整体涂成深灰色，与周边风貌融为一体，做到了“让城市留住记忆，让人们记住乡愁”。"
    "该区的做法说明什么？教师版答案D：要从整体上把握事物的联系才能达到城市管理的良好效果。"
)
Q9_PROMPT = (
    "《北京韧性城市空间规划》提出以圈层协同为载体，整体提高城市抵御风险挑战的稳健性和可持续性。"
    "打造韧性城市需要什么？教师版答案A，正确项①为坚持问题导向、系统观念，统筹高质量发展和高水平安全。"
)
Q16_PROMPT = (
    "共建美美与共的文明百花园，要强化用文化同世界对话的理念。材料涉及《论语》《习近平谈治国理政》海外发行、"
    "中国汉代文物出境展出、春节成为联合国假日并列入人类非遗。结合材料，运用《哲学与文化》知识，谈谈应如何用文化同世界对话。"
)
Q22_PROMPT = (
    "推进马克思主义中国化时代化是一个追求真理、揭示真理、笃行真理的过程。十八大以来，国内外形势新变化和实践新要求，"
    "迫切需要从理论和实践的结合上回答重大时代课题。结合材料，综合运用所学，说明如何不断谱写马克思主义中国化时代化新篇章。"
)

NEW_ENTRIES = [
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q2",
        "heading_suffix": "2025朝阳期末 第2题（选择题）",
        "material_trigger": "教师版客观题答案为D，正确项直接表述“要从整体上把握事物的联系才能达到城市管理的良好效果”。题干中“一户一策”新鸽子笼与老房顶样式、深灰色外观、周边风貌相融，构成城市治理中的多要素联系。",
        "question_prompt": Q2_PROMPT,
        "why_trigger": "题目不是孤立评价鸽子笼外观，而是要求把居民记忆、传统风貌、城市环境治理和具体设计方案放在同一关系网络中考察。看到“与周边风貌融为一体”“让城市留住记忆”，应落到用联系的观点看问题。",
        "answer_landing": "本题应选D。城市治理要坚持联系的观点，从整体上把握传统文化记忆、居民生活需求、城市环境秩序和空间设计之间的联系，才能在整治杂乱鸽子笼的同时保留北京声音和乡愁记忆。本条只作为客观选择题正确项挂点，不升级为主观评分细则。",
        "evidence_level": "教师版客观题答案+正确项解析；非主观评分细则",
        "boundary_note": "Objective-choice evidence only; do not treat as subjective scoring-rule evidence.",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q9",
        "heading_suffix": "2025朝阳期末 第9题（选择题）",
        "material_trigger": "教师版客观题答案为A，正确项①明列“坚持问题导向、系统观念，统筹高质量发展和高水平安全”；题干列出功能核区、中心城区、副中心、两轴、多点、生态涵养区等圈层协同。",
        "question_prompt": Q9_PROMPT,
        "why_trigger": "韧性城市建设不是只抓单一设施，而是把空间治理、生命线系统、副中心、两轴、多点地区和生态涵养区作为系统来统筹。看到“圈层协同”“整体提高”“系统观念”，应定位到系统观念/系统优化。",
        "answer_landing": "本题应选A。打造韧性城市要坚持系统观念，把不同空间圈层、治理主体和安全发展目标作为相互联系的系统进行统筹，优化城市抵御风险和恢复运行的整体能力。本条只证明客观题正确项可以作为系统观念挂点，不冒充主观题细则。",
        "evidence_level": "教师版客观题答案+正确项解析；非主观评分细则",
        "boundary_note": "Objective-choice evidence only; Q9 does not justify importing all urban-governance policy points into philosophy nodes.",
    },
    {
        "canonical_node": "规律的客观性",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳期末 第16题（主观题）",
        "material_trigger": "PPT评分细则第129-138行哲学部分列“规律（2分）：文化发展有其自身规律，要尊重客观规律，正确发挥主观能动性，尊重文化传承、文化交流、文化交流的一般规律”。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "用文化同世界对话不能只凭主观热情硬推文化符号，而要遵循文化传承、交流、传播的一般规律。材料中文物出境展览要与当地策展人沟通，春节进入联合国假日和非遗名录也要遵循国际组织程序，说明文化交流有客观规律。",
        "answer_landing": "用文化同世界对话，要承认文化传承、文化交流和文化传播具有客观规律。尊重这些规律，才能让《论语》、文物展览、春节等中华文化载体在不同文化语境中被理解、接受和共享；脱离交流对象和传播规律的主观推介，难以形成真正对话。",
        "evidence_level": "PPT评分细则明列“规律”；PDF细则为渲染待OCR，不单独作文本证据",
        "boundary_note": "Q16 rubric supports law/objective-law landing; this row is not inferred from ordinary answer text alone.",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q16",
        "heading_suffix": "2025朝阳期末 第16题（主观题）",
        "material_trigger": "PPT评分细则第134行明列“发展（2分）：要坚持用发展的观点看问题/坚持辩证的否定观，把握中国文化和域外文化的过去、现在、未来，推动不同文化共同发展”。",
        "question_prompt": Q16_PROMPT,
        "why_trigger": "材料二要求挖掘文物的当代价值、寻找其与现代生活的契合点；材料三春节由传统节日走向联合国假日和非遗名录，都体现文化不是停留在过去，而是在传承中发展、在交流中发展。",
        "answer_landing": "用文化同世界对话，要坚持发展的观点，把中华优秀传统文化放在过去、现在、未来的连续发展中理解。既要看到《论语》、汉代文物、春节等传统文化资源的历史根脉，也要通过当代阐释、互动展览和国际传播使其获得新的生命力，推动不同文化共同发展。",
        "evidence_level": "PPT评分细则明列“发展”；PDF细则为渲染待OCR，不单独作文本证据",
        "boundary_note": "Existing Q16 row under辩证否定 is valid; this row补足 rubric-explicit development node.",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q22",
        "heading_suffix": "2025朝阳期末 第22题（主观题）",
        "material_trigger": "PPT评分细则第332-336行在辩证法部分明列“坚持系统观念，为整体性推进党和国家各项事业提供科学思想方法”。",
        "question_prompt": Q22_PROMPT,
        "why_trigger": "马克思主义中国化时代化不是局部观点更新，而是要围绕党和国家事业发展、党治国理政一系列重大时代课题，整体把握共产党执政规律、社会主义建设规律和人类社会发展规律。",
        "answer_landing": "不断谱写马克思主义中国化时代化新篇章，要坚持系统观念，把理论创新放在党和国家事业整体推进中谋划，统筹执政规律、社会主义建设规律、人类社会发展规律以及不同领域重大时代课题，使新的理论成果成为整体性推进事业发展的科学思想方法。",
        "evidence_level": "PPT评分细则明列“系统观念”；教师版参考答案仅作题面/背景辅助",
        "boundary_note": "Q22 is综合题；only rubric-listed philosophy nodes are imported.",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q22",
        "heading_suffix": "2025朝阳期末 第22题（主观题）",
        "material_trigger": "PPT评分细则第332-336行在辩证法部分列“坚持守正创新，坚持用发展的观点看待理论创新”。",
        "question_prompt": Q22_PROMPT,
        "why_trigger": "题干写“实践没有止境，理论创新也没有止境”“必须长期坚持并不断丰富发展”，说明马克思主义中国化时代化是随实践发展不断推进的过程。",
        "answer_landing": "谱写马克思主义中国化时代化新篇章，要坚持发展的观点看待理论创新。随着国内外形势新变化和实践新要求不断出现，马克思主义中国化时代化也要在长期坚持中不断丰富发展，用发展着的理论回答发展着的时代课题。",
        "evidence_level": "PPT评分细则明列“发展的观点”；教师版题面辅助",
        "boundary_note": "This row is tied to Q22 rubric's development wording, not a loose expansion.",
    },
    {
        "canonical_node": "辩证否定 / 守正创新",
        "question_no": "Q22",
        "heading_suffix": "2025朝阳期末 第22题（主观题）",
        "material_trigger": "PPT评分细则第332-336行在辩证法部分列“坚持守正创新，坚持用发展的观点看待理论创新”。",
        "question_prompt": Q22_PROMPT,
        "why_trigger": "“长期坚持并不断丰富发展”要求既守住马克思主义基本原理和习近平新时代中国特色社会主义思想的世界观方法论，又在新的实践中推进理论探索和创新。",
        "answer_landing": "谱写马克思主义中国化时代化新篇章，要坚持守正创新。守正，就是坚持马克思主义基本原理和贯穿党的创新理论的立场观点方法；创新，就是立足新的实践要求和重大时代课题，不断提出新理念新思路新办法，使马克思主义在中国实践中持续焕发生命力。",
        "evidence_level": "PPT评分细则明列“守正创新”；教师版题面辅助",
        "boundary_note": "Q22 rubric supports this node directly; no use of ordinary reference answer as rubric.",
    },
    {
        "canonical_node": "实践是认识的基础",
        "question_no": "Q22",
        "heading_suffix": "2025朝阳期末 第22题（主观题）",
        "material_trigger": "PPT评分细则第337-340行认识论部分列“坚持实践观点，坚持理论与实践相结合、相统一，推进实践基础上的理论创新”。",
        "question_prompt": Q22_PROMPT,
        "why_trigger": "题干直接写“实践没有止境，理论创新也没有止境”“继续推进实践基础上的理论创新”，说明理论创新的来源、动力和检验都离不开实践。",
        "answer_landing": "不断谱写马克思主义中国化时代化新篇章，要坚持实践是认识的基础。要从国内外形势新变化和中国具体实践新要求出发，总结实践经验、回答实践课题，在实践基础上形成新的理论认识。",
        "evidence_level": "PPT评分细则明列“实践观点/实践基础上的理论创新”；教师版题面辅助",
        "boundary_note": "Existing general实践与认识 row remains valid; this row补足 precise实践基础 node.",
    },
    {
        "canonical_node": "认识对实践的反作用",
        "question_no": "Q22",
        "heading_suffix": "2025朝阳期末 第22题（主观题）",
        "material_trigger": "PPT评分细则第337-340行认识论部分列“推进实践基础上的理论创新，以新的理论指导新的实践”。",
        "question_prompt": Q22_PROMPT,
        "why_trigger": "理论创新不是停留在文本中，而是要以新的理论指导新的实践。材料要求把握好习近平新时代中国特色社会主义思想的世界观和方法论，坚持好运用好贯穿其中的立场观点方法。",
        "answer_landing": "新的理论认识形成后，要反作用于实践、指导新的实践。谱写马克思主义中国化时代化新篇章，要用党的创新理论指导党治国理政和推进中国式现代化的实践，把理论优势转化为认识世界、改造世界的实践力量。",
        "evidence_level": "PPT评分细则明列“以新的理论指导新的实践”；教师版题面辅助",
        "boundary_note": "This row records认识反作用 only where the rubric explicitly says new theory guides new practice.",
    },
]

BODY_EVIDENCE_OVERRIDES = {
    ("Q2", "联系的普遍性 / 联系的观点（总）"): ("教师版客观题答案+正确项解析；非主观评分细则", "objective-choice-only"),
    ("Q9", "系统观念 / 系统优化"): ("教师版客观题答案+正确项解析；非主观评分细则", "objective-choice-only"),
    ("Q16", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("PPT评分细则第131行明列“实际/一切从实际出发”", "formal scoring rule"),
    ("Q16", "主观能动性 / 意识的能动作用"): ("PPT评分细则第132行明列“正确发挥主观能动性”", "formal scoring rule"),
    ("Q16", "尊重客观规律与发挥主观能动性相结合"): ("PPT评分细则第132行明列“尊重客观规律，正确发挥主观能动性”", "formal scoring rule"),
    ("Q16", "规律的客观性"): ("PPT评分细则第132行明列“文化发展有其自身规律，要尊重客观规律”", "formal scoring rule"),
    ("Q16", "联系的普遍性 / 联系的观点（总）"): ("PPT评分细则第133行明列“联系”", "formal scoring rule"),
    ("Q16", "发展的观点 / 发展的普遍性"): ("PPT评分细则第134行明列“发展”", "formal scoring rule"),
    ("Q16", "辩证否定 / 守正创新"): ("PPT评分细则第134行明列“辩证的否定观”", "formal scoring rule"),
    ("Q16", "矛盾的普遍性和特殊性"): ("PPT评分细则第135行明列“普遍性与特殊性的具体的历史的统一”", "formal scoring rule"),
    ("Q16", "人民群众"): ("PPT评分细则第137行明列“尊重人民群众主体地位/群众观点群众路线”", "formal scoring rule"),
    ("Q16", "价值判断与价值选择"): ("PPT评分细则第136行明列“正确的价值判断和价值选择/正确价值观”", "formal scoring rule"),
    ("Q22", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("PPT评分细则第329-330行明列“一切从实际出发，实事求是”", "formal scoring rule"),
    ("Q22", "系统观念 / 系统优化"): ("PPT评分细则第332-336行明列“系统观念”", "formal scoring rule"),
    ("Q22", "发展的观点 / 发展的普遍性"): ("PPT评分细则第332-336行明列“发展的观点”", "formal scoring rule"),
    ("Q22", "辩证否定 / 守正创新"): ("PPT评分细则第332-336行明列“守正创新”", "formal scoring rule"),
    ("Q22", "矛盾的特殊性 / 具体问题具体分析"): ("PPT评分细则第332-336行明列“问题导向/具体问题具体分析”", "formal scoring rule"),
    ("Q22", "实践与认识（总）"): ("PPT评分细则第337-340行明列“实践观点/理论与实践相结合”", "formal scoring rule"),
    ("Q22", "实践是认识的基础"): ("PPT评分细则第337-340行明列“实践基础上的理论创新”", "formal scoring rule"),
    ("Q22", "认识对实践的反作用"): ("PPT评分细则第337-340行明列“以新的理论指导新的实践”", "formal scoring rule"),
    ("Q22", "人民群众"): ("PPT评分细则第342-344行明列“人民至上，站稳人民立场、把握人民愿望、尊重人民创造、集中人民智慧”", "formal scoring rule"),
}

BOUNDARY_ROWS = [
    ("Q1", "中国特色社会主义选择题", "否：模块边界排除", "中国特色社会主义/改革开放历史", "教师版答案C；题干考查新中国75年与中国特色社会主义历史进程，不属于必修四哲学正文。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "中特模块边界。"),
    ("Q3", "经济/法治/网络治理选择题", "否：模块边界排除", "算法治理/反垄断/社会主义核心价值观", "教师版答案B；正确项含反垄断与算法设计符合社会主义核心价值观，主线为算法治理和公共价值规范，不把普通客观题扩展为哲学价值观方法论。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "社会主义核心价值观只作网络治理规范，不进入哲学正文。"),
    ("Q4", "文化/经济选择题", "否：哲学正文边界排除", "乡村特色文旅/文化资源转化", "教师版答案C；题干主线为乡村文化资源转化、文旅产业带动就业增收，属文化与经济结合，不形成哲学正文挂点。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "文化线不进入当前哲学宝典正文。"),
    ("Q5", "逻辑与思维选择题", "否：模块边界排除", "联言/选言/假言推理", "教师版答案D；题干明确考查逻辑推理真假关系。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必三逻辑边界。"),
    ("Q6", "逻辑与思维选择题", "否：模块边界排除", "类比推理", "教师版答案A；题干明确考查类比推理。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必三逻辑边界。"),
    ("Q7", "逻辑与思维/辩证思维选择题", "否：模块边界排除", "辩证思维/创新思维", "教师版答案A；虽有“既克服又保留”等表达，但题型处于逻辑与思维辩证思维语境，未作为必修四哲学正文新增。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必三边界，不偷换为必修四辩证否定。"),
    ("Q8", "政治与法治选择题", "否：模块边界排除", "人民代表大会制度", "教师版答案B；考查新时代坚持完善人民代表大会制度。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "政治与法治边界。"),
    ("Q10", "法律与生活选择题", "否：模块边界排除", "相邻关系/侵权责任", "教师版答案D；考查照明侵权纠纷和排除妨碍。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必二法律边界。"),
    ("Q11", "法律与生活选择题", "否：模块边界排除", "劳动者权益/劳动争议", "教师版答案A；考查加班、扣发工资和劳动者合法权益。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必二法律边界。"),
    ("Q12", "经济与社会选择题", "否：模块边界排除", "物流成本/产业链供应链", "教师版答案C；考查物流成本、供应链韧性和经济运行效率。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "经济与社会边界。"),
    ("Q13", "经济/公共服务选择题", "否：模块边界排除", "京津冀社保卡一卡通办", "教师版答案B；主线是公共服务资源整合和区域资源共享。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "公共服务/区域协同边界。"),
    ("Q14", "当代国际政治与经济选择题", "否：模块边界排除", "政体/代议制", "教师版答案D；考查国体政体和代议制。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必一边界。"),
    ("Q15", "当代国际政治与经济/经济开放选择题", "否：模块边界排除", "海南自由贸易港/高水平开放", "教师版答案A；考查自由贸易港政策制度和开放型经济。", "教师版客观题答案+模块边界", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必一/经济边界。"),
    ("Q16(文化部分)", "哲学与文化主观题文化评分点", "否：哲学正文边界排除", "文化自信/优秀传统文化/文化创新/文化传播", "PPT评分细则第79-84行文化部分列自信、弘扬、发展、传播等文化评分点；当前交付物为哲学宝典，文化点只登记边界，不进哲学正文。", "PPT评分细则+交付物边界", "PHILOSOPHY_BODY_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "Q16哲学评分点已逐节点登记，文化评分点不混入哲学框架。"),
    ("Q17", "政治与法治主观题", "否：模块边界排除", "全过程人民民主/人民代表大会制度/基层群众自治", "题干明确限定《政治与法治》；PPT评分细则第139-183行按全过程人民民主、制度安排、民主特点功能等给分。", "PPT评分细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "政治与法治边界。"),
    ("Q18", "经济与社会主观题", "否：模块边界排除", "消费能力/消费意愿/消费层级", "题干明确限定《经济与社会》；PPT评分细则第184-213行按生产、分配、交换、消费与社会保障等给分。", "PPT评分细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "经济与社会边界。"),
    ("Q19", "逻辑与思维主观题", "否：模块边界排除", "排中律/矛盾律/三段论", "题干明确限定《逻辑与思维》；教师版与PPT评分细则按两不可、自相矛盾、三段论规则给分。", "PPT评分细则+教师版答案", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必三逻辑边界。"),
    ("Q20", "法律与生活主观题", "否：模块边界排除", "反不正当竞争/侵权责任", "题干为人民法院审理案件裁判要点；PPT评分细则第273-302行按法律依据、法律事实、法律责任等给分。", "PPT评分细则+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必二法律边界。"),
    ("Q21", "当代国际政治与经济主观题", "否：模块边界排除", "中国特色大国外交/全球治理/经济全球化", "题干明确限定《当代国际政治与经济》；PPT评分细则第303-318行按外交、国际政治经济文化环境等给分。", "PPT评分细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "选必一边界。"),
    ("Q22(中特/综合部分)", "综合主观题非哲学评分点", "否：哲学正文边界排除", "党的领导/两个结合/习近平新时代中国特色社会主义思想", "PPT评分细则第324-328行总说部分列党的领导、世界观方法论、两个结合；本批只把其后明列的唯物论、辩证法、认识论、历史观价值观哲学节点进正文。", "PPT评分细则+交付物边界", "PHILOSOPHY_BODY_BOUNDARY_EXCLUDED_BATCH23_CHAOYANG_FINAL", "综合题非哲学评分点不混入哲学节点。"),
]


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS)).strip()


def style_val(p: etree._Element) -> str:
    vals = p.xpath("./w:pPr/w:pStyle/@w:val", namespaces=NS)
    return vals[0] if vals else ""


def clear_runs(p: etree._Element) -> None:
    for child in list(p):
        if child.tag in {W + "r", W + "hyperlink"}:
            p.remove(child)


def make_run(text: str, label: bool = False) -> etree._Element:
    r = etree.Element(W + "r")
    if label:
        rpr = etree.SubElement(r, W + "rPr")
        etree.SubElement(rpr, W + "b")
        color = etree.SubElement(rpr, W + "color")
        color.set(W + "val", "21574C")
    t = etree.SubElement(r, W + "t")
    if text.startswith(" ") or text.endswith(" "):
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return r


def new_heading_para(template: etree._Element, text: str) -> etree._Element:
    p = deepcopy(template)
    clear_runs(p)
    p.append(make_run(text))
    return p


def new_label_para(template: etree._Element, label: str, body_text: str) -> etree._Element:
    p = deepcopy(template)
    clear_runs(p)
    p.append(make_run(label, label=True))
    p.append(make_run(" " + body_text))
    return p


def next_entry_number(paras: list[etree._Element], section_idx: int, end_idx: int) -> int:
    count = 0
    for p in paras[section_idx + 1 : end_idx]:
        if style_val(p) == "5" and re.match(r"^\d+\.", para_text(p)):
            count += 1
    return count + 1


def update_docx(timestamp: str) -> tuple[Path, int]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_batch23_2025_chaoyang_final_{timestamp}.docx")
    shutil.copy2(docx, backup)

    with zipfile.ZipFile(docx, "r") as zin:
        xml = zin.read("word/document.xml")
        all_parts = {item.filename: zin.read(item.filename) for item in zin.infolist() if item.filename != "word/document.xml"}

    root = etree.fromstring(xml)
    body = root.xpath("//w:body", namespaces=NS)[0]
    inserted = 0
    for entry in NEW_ENTRIES:
        paras = body.xpath("./w:p", namespaces=NS)
        texts = [para_text(p) for p in paras]
        section_idx = next(
            (i for i, text in enumerate(texts) if style_val(paras[i]) == "4" and text == entry["canonical_node"]),
            None,
        )
        if section_idx is None:
            raise RuntimeError(f"Missing section: {entry['canonical_node']}")
        end_idx = len(paras)
        for i in range(section_idx + 1, len(paras)):
            if style_val(paras[i]) in {"3", "4"}:
                end_idx = i
                break
        if any(entry["heading_suffix"] in para_text(p) for p in paras[section_idx + 1 : end_idx]):
            continue
        heading_template = next((p for p in reversed(paras[section_idx + 1 : end_idx]) if style_val(p) == "5"), None)
        if heading_template is None:
            heading_template = next(p for p in paras if style_val(p) == "5")
        body_template = next((p for p in paras[section_idx + 1 : end_idx] if para_text(p).startswith("【材料触发点】")), None)
        if body_template is None:
            body_template = next(p for p in paras if para_text(p).startswith("【材料触发点】"))
        heading = f"{next_entry_number(paras, section_idx, end_idx)}. {entry['heading_suffix']}"
        new_paras = [
            new_heading_para(heading_template, heading),
            new_label_para(body_template, "【材料触发点】", entry["material_trigger"]),
            new_label_para(body_template, "【设问】", entry["question_prompt"]),
            new_label_para(body_template, "【为什么能想到】", entry["why_trigger"]),
            new_label_para(body_template, "【答案落点】", entry["answer_landing"]),
        ]
        for offset, new_p in enumerate(new_paras):
            body.insert(end_idx + offset, new_p)
        inserted += 1

    new_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
    with tempfile.TemporaryDirectory() as tmp:
        tmp_docx = Path(tmp) / docx.name
        with zipfile.ZipFile(tmp_docx, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for name, data in all_parts.items():
                zout.writestr(name, data)
            zout.writestr("word/document.xml", new_xml)
        shutil.copy2(tmp_docx, docx)
    return backup, inserted


def extract_docx_entries() -> list[dict[str, str]]:
    docx = current_docx()
    with zipfile.ZipFile(docx, "r") as zf:
        root = etree.fromstring(zf.read("word/document.xml"))
    entries: list[dict[str, str]] = []
    node = ""
    current: dict[str, str] | None = None
    parts: list[str] = []
    for p in root.xpath("//w:p", namespaces=NS):
        text = para_text(p)
        if not text:
            continue
        style = style_val(p)
        if style == "4":
            if current is not None:
                current["student_facing_text"] = "\n".join(parts)
                entries.append(current)
                current = None
                parts = []
            node = text
        if style == "5" and SUITE in text and "第" in text and "题" in text:
            if current is not None:
                current["student_facing_text"] = "\n".join(parts)
                entries.append(current)
                parts = []
            q_match = re.search(r"第(\d+)题", text)
            current = {
                "canonical_node": node,
                "question_no": f"Q{q_match.group(1)}" if q_match else "Q?",
                "registered_heading": text,
            }
            parts = [text]
        elif current is not None:
            if style in {"3", "4", "5"}:
                current["student_facing_text"] = "\n".join(parts)
                entries.append(current)
                current = None
                parts = []
                if style == "4":
                    node = text
            else:
                parts.append(text)
    if current is not None:
        current["student_facing_text"] = "\n".join(parts)
        entries.append(current)
    entries = [e for e in entries if e["canonical_node"]]
    entries.sort(key=lambda e: (int(e["question_no"][1:]) if e["question_no"][1:].isdigit() else 999, e["canonical_node"], e["registered_heading"]))
    return entries


def evidence_for(question_no: str, node: str) -> tuple[str, str]:
    if (question_no, node) in BODY_EVIDENCE_OVERRIDES:
        return BODY_EVIDENCE_OVERRIDES[(question_no, node)]
    return ("NEED_EVIDENCE_REVIEW", "unmapped current DOCX entry")


def update_ledger_and_accepted(entries: list[dict[str, str]], timestamp: str) -> dict[str, int]:
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        ledger_rows = list(reader)
    existing_keys = {(r.get("canonical_node"), r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in ledger_rows}
    added_ledger = 0
    for e in entries:
        row = {
            "canonical_node": e["canonical_node"],
            "source_suite": SUITE,
            "question_no": e["question_no"],
            "inserted_heading": e["registered_heading"],
        }
        key = (row["canonical_node"], row["source_suite"], row["question_no"], row["inserted_heading"])
        if key not in existing_keys:
            ledger_rows.append(row)
            existing_keys.add(key)
            added_ledger += 1
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch23_2025_chaoyang_final_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(ledger_rows)

    accepted_records = [json.loads(line) for line in ACCEPTED.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
    accepted_keys = {
        (r.get("source_suite"), r.get("question_no"), r.get("canonical_node"), r.get("registered_heading"))
        for r in accepted_records
    }
    added_accepted = 0
    with ACCEPTED.open("a", encoding="utf-8") as f:
        for e in entries:
            evidence, boundary = evidence_for(e["question_no"], e["canonical_node"])
            record = {
                "source_suite": SUITE,
                "question_no": e["question_no"],
                "framework_node": e["canonical_node"],
                "canonical_node": e["canonical_node"],
                "student_facing_text": e["student_facing_text"],
                "evidence_level": evidence,
                "boundary_note": boundary,
                "source_lane": "Codex Batch23 Chaoyang final registration and insertion",
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
    return {"ledger_added": added_ledger, "accepted_added": added_accepted, "ledger_backup": str(backup)}


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch23_2025_chaoyang_final_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    rows = [r for r in rows if not (r.get("题源") == SUITE and r.get("row_source") == MATRIX_SOURCE)]
    max_id = 0
    for r in rows:
        m = re.match(r"M(\d+)", r.get("matrix_row_id", ""))
        if m:
            max_id = max(max_id, int(m.group(1)))

    new_rows: list[dict[str, str]] = []
    next_id = max_id + 1
    for e in entries:
        evidence, boundary = evidence_for(e["question_no"], e["canonical_node"])
        qtype = "必修四哲学正文条目"
        if boundary == "objective-choice-only":
            qtype = "必修四哲学选择题客观挂点"
        new_rows.append(
            {
                "matrix_row_id": f"M{next_id:04d}",
                "row_source": MATRIX_SOURCE,
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": e["question_no"],
                "题型或模块判断": qtype,
                "是否进宝典": "是：已进入当前DOCX/PDF正文",
                "宝典节点": e["canonical_node"],
                "细则支持原理": evidence,
                "证据等级": "客观题答案" if boundary == "objective-choice-only" else "强细则",
                "是否误放": "否",
                "是否需补厚": "否",
                "当前处理": "KEEP_IN_BODY" if boundary != "objective-choice-only" else "KEEP_IN_BODY_OBJECTIVE_ONLY",
                "备注": "当前DOCX正文已存在或Batch23补入；普通参考答案未冒充主观评分细则。",
                "source_artifact": SOURCE_PACKET,
            }
        )
        next_id += 1

    for q, qtype, in_body, node, support, evidence, status, note in BOUNDARY_ROWS:
        new_rows.append(
            {
                "matrix_row_id": f"M{next_id:04d}",
                "row_source": MATRIX_SOURCE,
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": q,
                "题型或模块判断": qtype,
                "是否进宝典": in_body,
                "宝典节点": node,
                "细则支持原理": support,
                "证据等级": evidence,
                "是否误放": "否",
                "是否需补厚": "否",
                "当前处理": status,
                "备注": note,
                "source_artifact": SOURCE_PACKET,
            }
        )
        next_id += 1

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    return {
        "matrix_rows_total": len(rows) + len(new_rows),
        "batch_rows": len(new_rows),
        "body_rows": sum(1 for r in new_rows if r["是否进宝典"].startswith("是")),
        "boundary_rows": sum(1 for r in new_rows if not r["是否进宝典"].startswith("是")),
        "matrix_backup": str(backup),
    }


def update_global_audit(docx_mentions: int, matrix_rows_for_suite: int) -> dict[str, int]:
    with GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    updated = False
    for row in rows:
        if row.get("normalized_suite") == SUITE or row.get("raw_suite") == SUITE:
            row["in_full_source_vs_docx_audit"] = "True"
            row["matrix_rows"] = str(matrix_rows_for_suite)
            row["current_docx_mentions"] = str(docx_mentions)
            row["current_status"] = "covered_by_batch23_recovery_matrix"
            row["blocker_or_next_action"] = "Batch23 registered inherited DOCX entries, inserted missing philosophy nodes, and added question-level boundary rows; render/model gates pending."
            updated = True
    if not updated:
        raise RuntimeError(f"global audit row for {SUITE} not found")
    with GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    missing = [r for r in rows if r.get("current_status") == "missing_from_current_47_suite_audit_scope"]
    covered = [r for r in rows if r.get("current_status") != "missing_from_current_47_suite_audit_scope"]
    missing_table = "\n".join(
        f"| {r['normalized_suite']} | {r['stage_dir']} | {r['current_status']} | {r['blocker_or_next_action']} |"
        for r in missing
    )
    GLOBAL_AUDIT_MD.write_text(
        f"""# Global Raw Suite Exhaustion Audit 2026-05-25

status: `GLOBAL_SOURCE_SCOPE_GAP_FOUND`

## Summary

- raw suite directories discovered under Desktop 2024-2026 stage folders: `{len(rows)}`
- current covered by first/second mock audit or recovery matrix: `{len(covered)}`
- remaining midterm/final raw suites outside current coverage: `{len(missing)}`
- current recovery matrix rows for `{SUITE}`: `{matrix_rows_for_suite}`
- current DOCX mentions for `{SUITE}`: `{docx_mentions}`

## Batch23 Finding

`{SUITE}` is now covered by question-level recovery matrix rows. Q2 and Q9 have objective-choice philosophy placements; Q16 and Q22 have rubric-supported philosophy placements. Culture, politics, economics, law, logic, and international-politics parts are explicitly boundary-excluded.

## Remaining Gap Suites

| normalized_suite | stage_dir | status | next action |
|---|---|---|---|
{missing_table}

## Guardrail

- This audit does not establish whole-project final acceptance.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- The model-effort/adaptive proof gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
""",
        encoding="utf-8",
    )
    return {"covered": len(covered), "missing": len(missing)}


def write_reports(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int], matrix_result: dict[str, int], global_result: dict[str, int]) -> None:
    by_question: dict[str, list[str]] = {}
    for e in entries:
        by_question.setdefault(e["question_no"], []).append(e["canonical_node"])
    body_lines = "\n".join(
        f"- {q}: " + "; ".join(nodes)
        for q, nodes in sorted(by_question.items(), key=lambda item: int(re.sub(r'\D', '', item[0]) or 999))
    )
    boundary_lines = "\n".join(f"- {row[0]} -> {row[3]} -> `{row[6]}`" for row in BOUNDARY_ROWS)
    source_paths = "\n".join(
        [
            f"- suite bundle: `{GPT_BUNDLE}`",
            f"- PPT scoring/answer-detail cache: `{PPT_SCORING_SOURCE}`",
            f"- teacher-version paper cache: `{TEACHER_SOURCE}`",
            f"- formal rubric PDF cache record: `{PDF_RUBRIC_SOURCE}`",
            f"- formal rubric PDF rendered pages: `{PDF_RUBRIC_RENDER_DIR}`",
            "- raw formal rubric PDF: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025朝阳期末\\细则\\2025朝阳期末细则.pdf`",
            "- raw scoring PPT: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025朝阳期末\\其他材料\\朝阳高三期末2025.pptx`",
            "- raw teacher paper: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025朝阳期末\\试卷\\2025北京朝阳高三（上）期末政治（教师版）.pdf`",
        ]
    )
    SOURCE_TRANSCRIPTION.write_text(
        f"""# Batch23 Source Transcription - 2025朝阳期末

Status: `SOURCE_REVIEWED_BATCH23`

## Source Files

{source_paths}

## Source Facts

- Teacher-version answer key: `1C 2D 3B 4C 5D 6A 7A 8B 9A 10D 11A 12C 13B 14D 15A`.
- Formal rubric PDF cache has no reliable text layer and is recorded as `rendered-ocr-needed`; the cached rendered pages remain available for visual/OCR follow-up. It is not used as independent text evidence in this batch.
- The PPT scoring source contains detailed scoring rules and answer-variation notes. Batch23 treats it as the usable scoring source, not as an ordinary reference answer.
- Q2 answer D supports only an objective-choice `联系的观点` placement.
- Q9 answer A supports only an objective-choice `系统观念` placement.
- Q16 rubric supports: actual conditions/一切从实际出发, 规律/尊重客观规律/主观能动性, 联系, 发展/辩证否定, 矛盾普遍性与特殊性, 正确价值判断价值选择/正确价值观, 人民群众主体地位.
- Q22 rubric supports: 一切从实际出发, 系统观念, 守正创新, 发展的观点, 问题导向/具体问题具体分析, 实践观点/理论与实践相结合, 实践基础上的理论创新, 以新的理论指导新的实践, 人民至上/人民立场.

## Current DOCX Entries After Batch23

{body_lines}

## Boundary Rows

{boundary_lines}

## Guardrail

- Objective-choice evidence is not upgraded to subjective scoring-rule evidence.
- Culture, politics, economics, law, logic, and international-politics rows are explicitly boundary-excluded from the current philosophy body.
- No Sonnet/Haiku/model-unknown evidence is counted as qualified ClaudeCode evidence.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
""",
        encoding="utf-8",
    )

    BATCH_REPORT.write_text(
        f"""# Coverage Fusion Batch23 - 2025朝阳期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- Current thread remains the recovered execution owner; old failed thread context is not used as execution evidence.
- DOCX backup before edit: `{backup}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `{SUITE}` after Batch23: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `{SUITE}`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch23: `{global_result['missing']}`.

## Placement Verdict

- Existing Q16/Q22 DOCX entries were registered rather than duplicated where already present.
- Missing rubric-supported philosophy placements were inserted for Q2, Q9, Q16, and Q22.
- Q16 culture scoring points and Q22 non-philosophy comprehensive points were not merged into philosophy nodes.
- Q7's “辩证思维” choice item stays in the logic/thinking boundary and is not converted into 必修四辩证否定 evidence.

## Remaining Gates

- Render QA is pending for Batch23.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until independently confirmed.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final; no `STRICT_FINAL_ACCEPTED` claim is made.
""",
        encoding="utf-8",
    )

    append_block = f"""

## Batch23 Local Application: 2025朝阳期末
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Inserted missing DOCX entries: `{inserted}`.
- Current governed DOCX entries for `{SUITE}`: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` (`{matrix_result['body_rows']}` body / `{matrix_result['boundary_rows']}` boundary).
- Global remaining raw midterm/final gap: `{global_result['missing']}`.
- Model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`; GPTPro/Claude external full-artifact review remain `real_call_pending`.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch23 Local Application: 2025朝阳期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + append_block, encoding="utf-8")

    model_text = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH23_CHAOYANG_FINAL_RECHECK"
    if marker in model_text:
        model_text = model_text[: model_text.index(marker)]
    model_text += """

## CLAUDECODE_BATCH23_CHAOYANG_FINAL_RECHECK

status: `real_call_pending`

- No ClaudeCode Opus 4.7 max/adaptive recheck has been completed for Batch23 yet.
- No Sonnet/Haiku/model-unknown result is accepted as qualified evidence.
- Until runtime evidence proves the required lane, the model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    MODEL_LEDGER.write_text(model_text, encoding="utf-8")


def main() -> int:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    entries = extract_docx_entries()
    if len(entries) < 21:
        raise RuntimeError(f"Expected at least 21 {SUITE} entries after Batch23, found {len(entries)}")
    ledger_result = update_ledger_and_accepted(entries, timestamp)
    matrix_result = update_matrix(entries, timestamp)
    global_result = update_global_audit(len(entries), matrix_result["batch_rows"])
    write_reports(backup, inserted, entries, ledger_result, matrix_result, global_result)
    print(
        json.dumps(
            {
                "inserted": inserted,
                "docx_entries": len(entries),
                "ledger": ledger_result,
                "matrix": matrix_result,
                "global": global_result,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
