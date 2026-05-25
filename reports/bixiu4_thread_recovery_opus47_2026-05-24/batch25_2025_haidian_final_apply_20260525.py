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

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH25_2025_HAIDIAN_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH25_2025_HAIDIAN_FINAL_CODEX_20260525.md"

PREPROCESSED = Path.home() / "Desktop" / "beijing_politics_research" / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2025各区模拟题__2025各区期末__2025海淀期末.md"
RUBRIC_SOURCE = next((PREPROCESSED / "gpt_sources").glob("4b22b6c78aaddb3e_*.md"))
TEACHER_SOURCE = next((PREPROCESSED / "gpt_sources").glob("b960993a71bd93ca_*.md"))

SUITE = "2025海淀期末"
YEAR = "2025"
STAGE = "期末"
BATCH_ID = "batch25_2025_haidian_final"
MATRIX_SOURCE = "codex_batch25_2025_haidian_final"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; "
    "current DOCX verified: existing unregistered 2025海淀期末 headings were present before Batch25"
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "尊重客观规律与发挥主观能动性相结合",
        "question_no": "Q5",
        "question_label": "第5题（选择题）",
        "material_trigger": "教师版答案第5题为D，正确项③写“因地制宜，把高度的革命热情与严谨的科学态度结合起来”。",
        "question_prompt": "塔克拉玛干沙漠边缘绿色阻沙防护带实现“锁边合龙”。40多年来，新疆各族人民一代接着一代干，采用工程治沙、光伏治沙、生态治沙三种模式，筑起生态屏障与精神丰碑。选项③强调因地制宜、革命热情与科学态度结合。",
        "why_trigger": "“因地制宜”要求尊重当地干旱缺水、风沙治理和生态保护的客观条件；“革命热情与严谨科学态度结合”直接指向发挥主观能动性必须以尊重客观规律为基础。",
        "answer_landing": "本题正确项包含③。治沙不能凭热情蛮干，而要在尊重沙漠生态治理规律、当地水土条件和技术条件的基础上，发挥治沙人的主观能动性，科学选择工程治沙、光伏治沙、生态治沙等模式，把科学态度与实践热情统一起来。此条只作为客观选择题正确项挂点。",
    },
    {
        "canonical_node": "量变与质变 / 适度原则",
        "question_no": "Q5",
        "question_label": "第5题（选择题）",
        "material_trigger": "教师版答案第5题为D，正确项④写“久久为功，正确地把握沙漠治理中渐进性与飞跃性的统一”。",
        "question_prompt": "塔克拉玛干沙漠边缘绿色阻沙防护带实现“锁边合龙”。40多年接续治沙，累计植树7000多万亩，最终形成3046公里绿色阻沙防护带。选项④强调久久为功和渐进性与飞跃性统一。",
        "why_trigger": "“40多年”“一代接着一代干”“累计植树7000多万亩”是量的积累；“锁边合龙”“筑起生态屏障”是治理效果的质变。正确项直接用“渐进性与飞跃性的统一”表达量变质变关系。",
        "answer_landing": "本题正确项包含④。治沙成效来自长期持续的量的积累，一代代治沙人久久为功，逐步积累植绿锁沙成果，最终实现防护带锁边合龙这一质的飞跃。此条只作为客观选择题正确项挂点。",
    },
    {
        "canonical_node": "实践与认识（总）",
        "question_no": "Q6",
        "question_label": "第6题（选择题）",
        "material_trigger": "教师版答案第6题为B，正确项④写“胡克定律的发现及其在生产中的应用，体现了实践与认识之间的相互作用”。",
        "question_prompt": "胡克定律只有在物体保持弹性的情况下才有效，当力过大时不再适用；这一定律常被运用到弹簧制造、工程设计、地质力学等领域。正确项④指出其发现和应用体现实践与认识之间的相互作用。",
        "why_trigger": "胡克定律从科学实验和工程实践中被发现，又反过来指导弹簧制造、工程设计、地质力学等实践，体现实践决定认识与认识反作用于实践的双向关系。",
        "answer_landing": "本题正确项包含④。实践推动人们发现胡克定律，形成关于弹性形变与外力关系的认识；该认识又被运用于弹簧制造、工程设计和地质力学实践，体现实践与认识的相互作用。此条只作为客观选择题正确项挂点。",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "PPT细则第37-44行哲学部分明列“坚持辩证否定，推动创新/坚持发展的观点”。",
        "question_prompt": "守正不守旧，尊古不复古。药食同源主张食物与药物之间并无绝对界限；近年来结合中药元素的曲奇、面包、吐司等烘焙产品兴起。设问要求运用《哲学与文化》知识谈如何打造中医药新时尚。",
        "why_trigger": "题目要求解释“守正不守旧，尊古不复古”，不是停留在传统药食同源理念本身，而是把中医药文化放到当代消费场景、食品工艺和健康需求中发展。",
        "answer_landing": "打造中医药新时尚，要坚持发展的观点，在传承药食同源等中医药文化根脉的基础上，根据当代生活方式和健康需求推动其发展，使中药元素进入曲奇、面包、吐司等现代食品形态，让传统中医药文化在创新发展中焕发新活力。",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "PPT细则第37-40行哲学部分明列“坚持对立统一的观点”。",
        "question_prompt": "药食同源理念主张食物与药物之间并无绝对界限，很多食材既可以入药也可以作为日常饮食的一部分；各地将中药元素与烘焙产品结合形成中医药新时尚。",
        "why_trigger": "材料中的“药”与“食”、“尊古”与“不复古”、“守正”与“不守旧”构成相互区别又相互联结的关系。打造新时尚要在这些对立统一关系中寻找结合点，而不是把传统与现代割裂。",
        "answer_landing": "打造中医药新时尚，要坚持对立统一的观点，看见药与食、传统与现代、守正与创新既有区别又能相互贯通。正因为食材与药材并非绝对割裂，传统药食同源理念才能与现代烘焙方式结合，形成既有中医药文化根脉又符合现代消费需求的新产品。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "PPT细则第520-521行将“人民主体地位”列为必修四可选知识；材料引用毛泽东“这个上帝不是别人，就是全中国的人民大众。全国人民大众一齐起来和我们一道挖这两座山”。",
        "question_prompt": "围绕“愚公移山”主题自拟题目撰写短文。材料包括毛泽东把“上帝”解释为全中国人民大众，以及各民族团结实现“移山壮举”。",
        "why_trigger": "题目把愚公移山从神话转化为人民大众共同奋斗的历史叙事，明确要求看到人民大众才是改造世界、推动历史前进的主体力量。",
        "answer_landing": "围绕愚公移山写作，可以落到人民群众是社会历史的主体。真正能搬走压在人民头上的“大山”的，不是神秘力量，而是全中国人民大众的团结奋斗。要依靠人民、团结人民，发挥人民群众的主体作用，才能汇聚推进民族复兴和现代化建设的磅礴力量。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "PPT细则第520-521行将“主观能动性”列为必修四可选知识；材料多次强调“下决心”“坚持下去”“不断地工作”“持之以恒”。",
        "question_prompt": "材料从古代愚公“下决心将挡在家门口的两座大山移开”，到毛泽东“一定要坚持下去”，再到习近平引用“只要持之以恒，总有一天会把大山搬走”。",
        "why_trigger": "材料的核心不是自然条件自动改变，而是人有目标、有决心、有坚持，能在尊重客观条件的基础上通过长期实践改变现实。",
        "answer_landing": "围绕愚公移山写作，可以落到发挥主观能动性。面对困难和“大山”，人不能消极等待，而要树立坚定目标，发挥意识的能动作用，持之以恒地实践和奋斗，把改造世界的愿望转化为持续行动。",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q22",
        "question_label": "第22题（主观题）",
        "material_trigger": "PPT细则第520-521行将“价值观”列为必修四可选知识；题干说愚公移山彰显中华民族的精神品格，材料强调“目的必定达到”。",
        "question_prompt": "国家博物馆浮雕《愚公移山》以古代移山神话和抗战期间各民族团结实现的移山壮举为主题，彰显中华民族的精神品格；短文要求围绕“愚公移山”展开。",
        "why_trigger": "愚公移山精神作为价值追求，会引导人们如何认识困难、如何选择行动、如何坚持奋斗，体现价值观对人的认识和实践活动具有导向作用。",
        "answer_landing": "围绕愚公移山写作，可以落到价值观的导向作用。愚公移山精神引导我们把国家发展、民族复兴和人民幸福作为奋斗目标，面对困难不退缩、面对任务不懈怠，以正确价值观凝聚坚持不懈、团结奋斗的行动力量。",
    },
]


BOUNDARY_ROWS = [
    ("Q1", "文化选择题", "北京中轴线声音/中华文明连续性", "教师版答案A；文化记忆和中华文明连续性，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q2", "逻辑与思维/文化选择题", "场景迁移/辩证思维整体性", "教师版答案C；正确项为选必三迁移、辩证思维整体性和文化旅游分析，不进入必修四哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q3", "文化选择题", "讲好中国故事/传统文化独特魅力", "教师版答案B；文化传承传播选择题，不纳入当前哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q8", "逻辑与思维选择题", "推理结构/概念关系/逻辑错误/选言判断", "教师版答案D；题干明确《逻辑与思维》，不转入必修四哲学。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q9", "法律与生活选择题", "天然孳息/用益物权", "教师版答案B；民法典天然孳息归属，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q10", "法律与生活选择题", "买卖合同/违约责任", "教师版答案C；合同履行法律问题，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q11", "法律与生活选择题", "客运合同/诉讼上诉/承运人责任", "教师版答案D；法律模块选择题，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q12", "法律与生活选择题", "继承/遗产/抚恤金", "教师版答案A；婚姻继承法律问题，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q13", "法律与生活选择题", "隐形加班/劳动权益/公正司法", "教师版答案B；劳动法与司法保护，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q14", "法律与生活选择题", "著作权/举证/调解", "教师版答案C；著作权法律问题，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q15", "法律与生活/社会治理选择题", "探店视频/消费者权益/平台公约", "教师版答案D；消费者权益和社会治理法治化，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q16-culture", "哲学与文化主观题中的文化评分点", "中华优秀传统文化创造性转化/综合创新/时代问题", "PPT细则列文化点；当前交付件为哲学宝典正文，文化点不强行塞入哲学节点。", "PPT细则+文档边界", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q17(1)", "逻辑与思维主观题", "科学思维客观性/能量守恒定律", "题干明确运用科学思维知识；PPT细则按科学思维客观性、规律和材料分析给分，不作为必修四哲学正文。", "PPT细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q18", "逻辑与思维主观题", "逆向思维/联想思维/发散聚合/超前思维", "题干要求创新思维；PPT细则按选必三创新思维给分，不进入必修四哲学正文。", "PPT细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q19", "法律与生活主观题", "农村土地确权登记/用益物权/定分止争", "题干限定法治知识，PPT细则按财产权、定分止争和土地经营流转意义给分。", "PPT细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q20", "法律与生活主观题", "产品责任/危险动物/无过错侵权", "PPT细则按无过错侵权责任和消费者、动物饲养管理秩序给分。", "PPT细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q21", "法律与生活主观题", "竞业限制/商业秘密/劳动者权益平衡", "题干限定《法律与生活》，PPT细则按竞业限制规范和限制的法律意义给分。", "PPT细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH25_HAIDIAN_FINAL"),
    ("Q22-nonphilosophy", "综合短文非哲学点", "党的领导/中国式现代化/中国梦/传统文化/民族精神/人类命运共同体", "PPT细则列综合可选知识；只登记可进哲学正文的必修四哲学点，其余作为模块边界。", "PPT细则+文档边界", "NONPHILOSOPHY_COMPREHENSIVE_POINT_BOUNDARY_EXCLUDED"),
]


OBJECTIVE_KEYS = {"Q4", "Q5", "Q6", "Q7"}

EVIDENCE_BY_KEY = {
    ("Q4", "主观能动性 / 意识的能动作用"): ("教师版答案第4题C；客观选择题正确项文本支持“主观能动性”", "objective-choice-only"),
    ("Q5", "尊重客观规律与发挥主观能动性相结合"): ("教师版答案第5题D；正确项③支持规律与能动性组合", "objective-choice-only"),
    ("Q5", "量变与质变 / 适度原则"): ("教师版答案第5题D；正确项④支持渐进性与飞跃性统一", "objective-choice-only"),
    ("Q6", "真理观"): ("教师版答案第6题B；正确项①支持真理具体性、条件性和真理谬误关系", "objective-choice-only"),
    ("Q6", "实践与认识（总）"): ("教师版答案第6题B；正确项④支持实践与认识相互作用", "objective-choice-only"),
    ("Q7", "实践与认识（总）"): ("教师版答案第7题A；正确项③支持从群众中来到群众中去工作方法", "objective-choice-only"),
    ("Q7", "价值判断与价值选择"): ("教师版答案第7题A；正确项①支持人民利益最高价值标准", "objective-choice-only"),
    ("Q16", "主观能动性 / 意识的能动作用"): ("PPT细则第37-44行列“坚持客观规律和发挥主观能动性相结合”；当前条目按组合原理理解", "body-with-node-caution"),
    ("Q16", "尊重客观规律与发挥主观能动性相结合"): ("PPT细则第37-44行明列“坚持客观规律和发挥主观能动性相结合”", "formal-rubric"),
    ("Q16", "联系的普遍性 / 联系的观点（总）"): ("PPT细则第37-44行明列“坚持联系观点/根据固有联系建立新的联系”", "formal-rubric"),
    ("Q16", "根据固有联系建立新的具体联系"): ("PPT细则第37-44行明列“根据固有联系建立新的联系”", "formal-rubric"),
    ("Q16", "发展的观点 / 发展的普遍性"): ("PPT细则第37-44行明列“坚持发展的观点”", "formal-rubric"),
    ("Q16", "辩证否定 / 守正创新"): ("PPT细则第37-44行明列“坚持辩证否定，推动创新”", "formal-rubric"),
    ("Q16", "矛盾就是对立统一"): ("PPT细则第37-40行明列“坚持对立统一的观点”", "formal-rubric"),
    ("Q16", "矛盾的普遍性和特殊性"): ("PPT细则第37-44行明列“具体问题具体分析/矛盾普遍性和特殊性辩证统一”", "formal-rubric"),
    ("Q16", "价值判断与价值选择"): ("PPT细则第28-44行列“人民立场”；当前条目以人民立场/正确价值选择处理", "formal-rubric"),
    ("Q17(2)", "量变与质变 / 适度原则"): ("PPT细则第69-130行明列“量变是质变的前提和必要准备”", "formal-rubric"),
    ("Q17(2)", "事物发展是前进性与曲折性的统一"): ("PPT细则第73-75、115-119行明列“事物发展是前进性和曲折性的统一”", "formal-rubric"),
    ("Q17(2)", "矛盾就是对立统一"): ("PPT细则第78-80、129-130行明列“矛盾双方在一定条件下相互转化/矛盾有同一性”", "formal-rubric"),
    ("Q17(2)", "实践与认识（总）"): ("PPT细则第69-95行明列“实践是检验认识真理性的唯一标准/实践是认识发展的动力”", "formal-rubric"),
    ("Q17(2)", "实践是认识的基础"): ("PPT细则第71、94行明列“实践是检验认识真理性的唯一标准/实践是认识发展的动力”", "formal-rubric"),
    ("Q17(2)", "认识发展原理"): ("PPT细则第69-70、91-94行明列“认识有反复性或无限性/追求真理是一个过程”", "formal-rubric"),
    ("Q17(2)", "真理观"): ("PPT细则第69-70、91-94行支持追求真理过程；教师版参考答案写“追求真理是一个过程”", "formal-rubric"),
    ("Q17(2)", "人民群众"): ("PPT细则第78、125-126行明列“人民群众是社会历史的主体/历史的创造者/精神财富的创造者”", "formal-rubric"),
    ("Q22", "量变与质变 / 适度原则"): ("PPT细则第520-521行将“质量互变规律”列为必修四可选知识", "formal-rubric-comprehensive"),
    ("Q22", "人民群众"): ("PPT细则第520-521行将“人民主体地位”列为必修四可选知识", "formal-rubric-comprehensive"),
    ("Q22", "主观能动性 / 意识的能动作用"): ("PPT细则第520-521行将“主观能动性”列为必修四可选知识", "formal-rubric-comprehensive"),
    ("Q22", "价值观的导向作用"): ("PPT细则第520-521行将“价值观”列为必修四可选知识", "formal-rubric-comprehensive"),
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
    backup = docx.with_name(f"{docx.stem}_backup_before_batch25_2025_haidian_final_{timestamp}{docx.suffix}")
    shutil.copy2(docx, backup)

    with zipfile.ZipFile(docx, "r") as zin:
        xml = zin.read("word/document.xml")
    root = etree.fromstring(xml)
    body = root.find(f"{W}body")
    paras = body.findall(f"{W}p")
    existing_headings = {para_text(p) for p in paras if style_val(p) == "5"}

    inserted = 0
    for spec in NEW_ENTRY_SPECS:
        node = spec["canonical_node"]
        n = next_heading_number(paras, node)
        heading = f"{n}. {SUITE} {spec['question_label']}"
        if heading in existing_headings:
            continue
        heading_template, body_template = template_paragraphs(paras, node)
        start, end = find_node_bounds(paras, node)
        insert_at = end
        new_paras = [
            clone_with_text(heading_template, heading),
            clone_with_text(body_template, f"【材料触发点】 {spec['material_trigger']}"),
            clone_with_text(body_template, f"【设问】 {spec['question_prompt']}"),
            clone_with_text(body_template, f"【为什么能想到】 {spec['why_trigger']}"),
            clone_with_text(body_template, f"【答案落点】 {spec['answer_landing']}"),
        ]
        for offset, p in enumerate(new_paras):
            body.insert(insert_at + offset, p)
        inserted += 1
        existing_headings.add(heading)
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch25_2025_haidian_final_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
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
            evidence, boundary = evidence_for(e)
            record = {
                "source_suite": SUITE,
                "question_no": e["question_no"],
                "framework_node": e["canonical_node"],
                "canonical_node": e["canonical_node"],
                "student_facing_text": e["student_facing_text"],
                "evidence_level": evidence,
                "boundary_note": boundary,
                "source_lane": "Codex Batch25 Haidian final registration and insertion",
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


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch25_2025_haidian_final_{timestamp}{MATRIX.suffix}")
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
        evidence, boundary = evidence_for(e)
        is_objective = boundary == "objective-choice-only"
        qtype = "必修四哲学选择题客观挂点" if is_objective else "必修四哲学正文条目"
        in_body = "是：客观选择题挂点，已在当前DOCX正文登记" if is_objective else "是：已进入当前DOCX/PDF正文"
        new_rows.append(
            {
                "matrix_row_id": f"M{next_id:04d}",
                "row_source": MATRIX_SOURCE,
                "题源": SUITE,
                "年份": YEAR,
                "阶段": STAGE,
                "题号": e["question_no"],
                "题型或模块判断": qtype,
                "是否进宝典": in_body,
                "宝典节点": e["canonical_node"],
                "细则支持原理": evidence,
                "证据等级": "教师版客观题答案" if is_objective else "强细则/PPT评标细则",
                "是否误放": "否" if boundary != "body-with-node-caution" else "否：保留但须按规律+能动性组合原理理解",
                "是否需补厚": "否",
                "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else "KEEP_IN_BODY",
                "备注": "Batch25登记既有正文并补入缺失挂点；普通参考答案未冒充主观评分细则。",
                "source_artifact": SOURCE_PACKET,
            }
        )
        next_id += 1

    for q, qtype, node, support, evidence, status in BOUNDARY_ROWS:
        new_rows.append(
            {
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
                "备注": "本题或本点不作为当前哲学宝典正文；不把法律、逻辑、文化或综合非哲学点偷换为哲学原理。",
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
            row["current_status"] = "covered_by_batch25_recovery_matrix"
            row["blocker_or_next_action"] = "Batch25 registered existing DOCX entries, inserted missing philosophy/objective-choice points, and added boundary rows; render/model gates pending."
    with GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    missing = [r for r in rows if r.get("current_status") == "missing_from_current_47_suite_audit_scope"]
    covered = [r for r in rows if r.get("current_status") != "missing_from_current_47_suite_audit_scope"]
    missing_table = "\n".join(f"| {r['normalized_suite']} | {r['stage_dir']} | {r['current_status']} | {r['blocker_or_next_action']} |" for r in missing)
    GLOBAL_AUDIT_MD.write_text(
        f"""# Global Raw Suite Exhaustion Audit 2026-05-25

status: `GLOBAL_SOURCE_SCOPE_GAP_FOUND`

## Summary

- raw suite directories discovered under Desktop 2024-2026 stage folders: `{len(rows)}`
- current covered by first/second mock audit or recovery matrix: `{len(covered)}`
- remaining midterm/final raw suites outside current coverage: `{len(missing)}`
- current recovery matrix rows for `{SUITE}`: `{matrix_rows_for_suite}`
- current DOCX governed headings for `{SUITE}`: `{docx_entries}`

## Batch25 Finding

`{SUITE}` is now covered by question-level recovery matrix rows. Existing DOCX headings were present but unregistered before Batch25. Batch25 registered those existing entries, inserted missing objective-choice and rubric-supported philosophy points, and boundary-excluded law, logic, culture-only, and non-philosophy comprehensive points.

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


def write_reports(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    body_lines = "\n".join(f"- {e['question_no']}: {e['canonical_node']} -> `{e['registered_heading']}`" for e in entries)
    boundary_lines = "\n".join(f"- {q}: {node} -> `{status}`" for q, _qtype, node, _support, _evidence, status in BOUNDARY_ROWS)
    SOURCE_TRANSCRIPTION.write_text(
        f"""# Batch25 Source Transcription - 2025海淀期末

Status: `SOURCE_REVIEWED_BATCH25`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- PPT scoring/rubric cache: `{RUBRIC_SOURCE}`
- teacher-version paper cache: `{TEACHER_SOURCE}`
- raw rubric: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025海淀期末\\细则\\2025海淀期末细则.pptx`
- raw teacher paper: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025海淀期末\\试卷\\2025北京海淀高三（上）期末政治（教师版）.docx`

## Source Facts

- Teacher answer key: `1A 2C 3B 4C 5D 6B 7A 8D 9B 10C 11D 12A 13B 14C 15D`.
- Q16 PPT scoring source supports philosophy points: 联系观点/根据固有联系建立新的联系、对立统一、具体问题具体分析/矛盾普遍性和特殊性、辩证否定/发展的观点、人民立场、客观规律与主观能动性结合. It also contains culture points, which are not forced into philosophy nodes.
- Q17(1) is 科学思维 and is boundary-excluded; Q17(2) has philosophy scoring points: 认识反复/无限、实践检验或动力、前进性与曲折性、量变质变、人民群众、矛盾转化.
- Q18 is 选择性必修三创新思维 and is boundary-excluded.
- Q19-Q21 are 法律与生活 and are boundary-excluded.
- Q22 is 综合短文. PPT细则 lists 必修四 optional points including 质量互变规律、人民主体地位、主观能动性、价值观; non-philosophy points remain boundary rows.

## Governed DOCX Entries After Batch25

{body_lines}

## Boundary Rows

{boundary_lines}

## Guardrail

- Objective-choice rows are labeled as objective-only.
- Ordinary reference answers are not used as subjective scoring rubrics.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
""",
        encoding="utf-8",
    )

    BATCH_REPORT.write_text(
        f"""# Coverage Fusion Batch25 - 2025海淀期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch25 edit: `{backup}`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `{SUITE}` after Batch25: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `{SUITE}`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch25: `{global_result['missing']}`.

## Placement Verdict

- `2025海淀期末` was wrongly absent from the recovery matrix even though DOCX headings already existed; Batch25 repaired that ledger/matrix gap.
- Q5 and Q6 objective-choice philosophy points were added as objective-only entries.
- Q16 and Q17(2) formal PPT scoring points are retained as body entries.
- Q22 additional rubric-listed philosophy points were added; culture and non-philosophy comprehensive points were not forced into philosophy nodes.

## Remaining Gates

- Render QA is pending because Batch25 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
""",
        encoding="utf-8",
    )

    format_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch25 Render/Format QA: 2025海淀期末"
    if marker in format_text:
        format_text = format_text[: format_text.index(marker)]
    FORMAT_QA.write_text(
        format_text
        + f"""

## Batch25 Render/Format QA: 2025海淀期末
Updated: 2026-05-25

- Render status: `render_pending`.
- Reason: Batch25 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required check: render current DOCX/PDF and verify fonts, heading styles, page count, labels, and new/old entry consistency.
""",
        encoding="utf-8",
    )

    append_block = f"""

## Batch25 Local Application: 2025海淀期末
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Existing DOCX entries registered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Current governed DOCX entries for `{SUITE}`: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` (`{matrix_result['body_rows']}` body / `{matrix_result['boundary_rows']}` boundary).
- Global remaining raw midterm/final gap: `{global_result['missing']}`.
- Model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`; GPTPro/Claude external full-artifact review remain `real_call_pending`.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch25 Local Application: 2025海淀期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + append_block, encoding="utf-8")

    model_text = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH25_HAIDIAN_FINAL_RECHECK"
    if marker in model_text:
        model_text = model_text[: model_text.index(marker)]
    MODEL_LEDGER.write_text(
        model_text
        + """

## CLAUDECODE_BATCH25_HAIDIAN_FINAL_RECHECK

status: `real_call_pending`

- No ClaudeCode Opus 4.7 max/adaptive recheck has been completed for Batch25 yet.
- No Sonnet/Haiku/model-unknown result is accepted as qualified evidence.
- Until runtime evidence proves the required lane, the model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
""",
        encoding="utf-8",
    )


def main() -> int:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    root = load_docx_xml(current_docx())
    entries = extract_entries_from_root(root)
    if len(entries) < 28:
        raise RuntimeError(f"Expected at least 28 {SUITE} governed entries after Batch25, found {len(entries)}")
    unmapped = [e for e in entries if evidence_for(e)[0] == "NEED_EVIDENCE_REVIEW"]
    if unmapped:
        raise RuntimeError(f"Unmapped evidence rows: {[(e['question_no'], e['canonical_node']) for e in unmapped]}")
    ledger_result = update_ledger_and_accepted(entries, timestamp)
    matrix_result = update_matrix(entries, timestamp)
    global_result = update_global_audit(len(entries), int(matrix_result["batch_rows"]))
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
