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
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2026各区模拟题__2026各区期末和期中__2026朝阳期末.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "487b2d15b3a3ac2b_2026朝阳期末细则.md"
PAPER_SOURCE = PREPROCESSED / "gpt_sources" / "e1a49527cb4c175f_2026北京朝阳高三_上_期末政治.md"
OCR_TEXT = RECOVERY / "BATCH30_2026_CHAOYANG_FINAL_OCR_TRANSCRIPTION_20260525.md"
OCR_LINES = RECOVERY / "BATCH30_2026_CHAOYANG_FINAL_OCR_LINES_20260525.md"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH30_2026_CHAOYANG_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH30_2026_CHAOYANG_FINAL_CODEX_20260525.md"

SUITE = "2026朝阳期末"
YEAR = "2026"
STAGE = "期末"
BATCH_ID = "batch30_2026_chaoyang_final"
MATRIX_SOURCE = "codex_batch30_2026_chaoyang_final"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {PAPER_SOURCE}; OCR text: {OCR_TEXT}; OCR line index: {OCR_LINES}; "
    "rubric lines 11-21 for Q16; rubric lines 144-158 for Q21; paper OCR lines 207-236, 332-361, 463-485; "
    "choice answer key not found, so Q1-Q15 are not inserted as objective body rows."
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式阅卷细则第21行补充列“从实际出发”；题面第359-360行强调以当代之思叩问传统、在保留戏曲精髓基础上赋予时代内涵。",
        "question_prompt": "结合材料，运用《哲学与文化》知识，谈谈你对“传统戏曲焕发新的生命力”的理解。",
        "why_trigger": "传统戏曲的当代化不是抽象复制，而是从当代审美、受众需求和传统戏曲自身条件出发，处理传统精髓与时代内涵的关系。",
        "answer_landing": "传统戏曲焕发新生命力要坚持一切从实际出发，立足当代文化生活和戏曲艺术特点，在保留传统精髓的基础上赋予新的时代内涵，而不是简单复制粘贴。",
    },
    {
        "canonical_node": "规律的客观性",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式阅卷细则第21行补充列“规律”；第15-18行要求遵循辩证否定观，剔除脱节部分、保留精髓并推动创造性转化和创新性发展。",
        "question_prompt": "材料要求说明传统戏曲如何在当代转化中焕发生命力。",
        "why_trigger": "传统艺术的传承创新受文化发展规律、艺术表达规律和当代接受规律制约，不能违背艺术自身和时代发展的客观要求。",
        "answer_landing": "推动传统戏曲创新发展要尊重文化传承和艺术发展的客观规律，既保留行当、唱腔、人物塑造等精髓，又按当代审美和时代要求转化表达方式。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式阅卷细则第19-21行把传统戏曲说成连接过去、现在与未来的文化纽带，并补充“联系”。",
        "question_prompt": "题面要求解释传统戏曲焕发新的生命力。",
        "why_trigger": "材料把传统戏曲精髓、当代表达、现代元素、观众需求和未来发展联系起来，说明生命力来自多方面关系的联结。",
        "answer_landing": "理解传统戏曲焕发生命力要坚持联系观点，把过去的戏曲传统、当代艺术表达和未来文化发展联系起来，在传统与现代元素融合中实现传承创新。",
    },
    {
        "canonical_node": "发展的观点 / 发展的普遍性",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式阅卷细则第18、21行分别写明创造性转化、创新性发展，并补充“发展”。",
        "question_prompt": "题面围绕传统戏曲在当代艺术创作中的转化和突破。",
        "why_trigger": "传统戏曲不是静止保存的符号，材料中的虞姬剑舞突破行当限制，体现传统艺术在时代变化中继续发展。",
        "answer_landing": "传统戏曲焕发生命力要用发展的观点看问题，在继承精髓的基础上创造性转化、创新性发展，使传统艺术随着时代和实践变化不断获得新的表达。",
    },
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "正式阅卷细则第21行补充“矛盾”；第15-18行围绕保留与剔除、传统与时代、精髓与新内涵展开。",
        "question_prompt": "题面要求理解传统戏曲焕发新的生命力。",
        "why_trigger": "传统戏曲创新要处理守根与求变、剔除与保留、传统程式与现代元素的对立统一关系。",
        "answer_landing": "传统戏曲焕发生命力要坚持矛盾观点，把守住文化之根和紧跟时代之变统一起来，在保留精髓与突破旧形式中实现新的发展。",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式阅卷细则第152-153行直接列“整体与部分的辩证统一 / 系统优化 / 联系的观点看问题”；题面第469-470行写“四大优势是相互依存、协同赋能的有机整体”。",
        "question_prompt": "结合材料，综合运用所学，谈谈对“四大优势是相互依存、协同赋能的有机整体，共同构成中国式现代化的独特禀赋”的认识。",
        "why_trigger": "四大优势不是并列堆放，而是制度、市场、产业、人才之间相互支撑、协同赋能，只有系统把握才能说明其整体支撑作用。",
        "answer_landing": "认识四大优势要坚持系统优化方法，把制度优势、超大规模市场优势、完整产业体系优势和人才优势作为相互依存的系统来统筹，推动各要素协同发力。",
    },
    {
        "canonical_node": "联系的普遍性 / 联系的观点（总）",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式阅卷细则第152-153行直接列“联系的观点看问题”；题面第469-470行写相互依存、协同赋能、有机整体。",
        "question_prompt": "第21题要求认识四大优势共同构成中国式现代化独特禀赋。",
        "why_trigger": "制度优势能够为市场、产业、人才优势释放提供条件，市场、产业和人才又反过来支撑制度优势转化为现代化建设效能。",
        "answer_landing": "认识四大优势要坚持联系观点，看到四种优势之间相互依存、相互作用、协同赋能，共同为全面建成社会主义现代化强国提供支撑。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "正式阅卷细则第157-158行直接列“坚持以人民为中心 / 群众观”，并要求激发人民群众投身现代化建设的积极性、主动性、创造性。",
        "question_prompt": "第21题在制度优势分析中要求说明人民至上与现代化建设的关系。",
        "why_trigger": "材料第471行把人民至上作为制度优势之一，细则明确要求从群众观说明人民群众在现代化建设中的主体作用。",
        "answer_landing": "发挥制度优势要坚持群众观点和群众路线，坚持以人民为中心，激发人民群众投身中国式现代化建设的积极性、主动性、创造性。",
    },
]


BOUNDARY_ROWS = [
    {"题号": "Q1", "题型或模块判断": "选择题答案键缺失/制度创新综合题", "宝典节点": "中国特色社会主义制度、制度创新、历史连续性与现实针对性", "细则支持原理": "试卷OCR第207-215行；未发现可核验答案键，且主旨跨中特/制度与文化滋养，不能作为客观哲学正文挂点。", "证据等级": "试卷原题OCR；答案键缺失", "当前处理": "CHOICE_ANSWER_KEY_MISSING_NO_BODY_ENTRY", "是否进宝典": "否：选择题无可靠答案键"},
    {"题号": "Q2", "题型或模块判断": "选择题答案键缺失/城市更新哲学表述", "宝典节点": "人民群众、系统观念、规律、联系等候选题肢", "细则支持原理": "试卷OCR第216-226行；题肢含人民需求、系统观念、规律等，但无答案键，不能确认正确选项。", "证据等级": "试卷原题OCR；答案键缺失", "当前处理": "CHOICE_ANSWER_KEY_MISSING_NO_BODY_ENTRY", "是否进宝典": "否：选择题无可靠答案键"},
    {"题号": "Q3", "题型或模块判断": "选择题答案键缺失/认识工具题", "宝典节点": "认识器官延伸、认识和改造客观世界能力", "细则支持原理": "试卷OCR第228-236行；未发现答案键，不能把某一题肢登记为客观挂点。", "证据等级": "试卷原题OCR；答案键缺失", "当前处理": "CHOICE_ANSWER_KEY_MISSING_NO_BODY_ENTRY", "是否进宝典": "否：选择题无可靠答案键"},
    {"题号": "Q4", "题型或模块判断": "选择题答案键缺失/文化审美题", "宝典节点": "文化审美、艺术价值", "细则支持原理": "试卷OCR第241-249行；文化/审美主旨且无答案键。", "证据等级": "试卷原题OCR；答案键缺失", "当前处理": "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q5", "题型或模块判断": "选择题答案键缺失/AI幻觉题", "宝典节点": "逻辑与认识边界", "细则支持原理": "试卷OCR第250-257行；未发现答案键，且主要用于AI信息识别/逻辑判断。", "证据等级": "试卷原题OCR；答案键缺失", "当前处理": "CHOICE_ANSWER_KEY_MISSING_NO_BODY_ENTRY", "是否进宝典": "否：选择题无可靠答案键"},
    {"题号": "Q6", "题型或模块判断": "逻辑与思维选择题", "宝典节点": "三段论、逻辑推理", "细则支持原理": "试卷OCR第258-268行；属选必三逻辑与思维。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q7", "题型或模块判断": "政治与法治选择题", "宝典节点": "全面从严治党、党内法规", "细则支持原理": "试卷OCR第269-276行；政治与法治主旨。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q8", "题型或模块判断": "政治与法治选择题", "宝典节点": "全过程人民民主、规划编制", "细则支持原理": "试卷OCR第277-287行；政治与法治主旨。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q9", "题型或模块判断": "政治/法治选择题", "宝典节点": "普法、法治德治", "细则支持原理": "试卷OCR第291-298行；法治建设主旨。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q10", "题型或模块判断": "法律与生活选择题", "宝典节点": "物权/财产权", "细则支持原理": "试卷OCR第299-306行；法律与生活。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q11", "题型或模块判断": "法律与生活选择题", "宝典节点": "数字人著作权/人格权", "细则支持原理": "试卷OCR第307-314行；法律与生活。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q12", "题型或模块判断": "经济与社会选择题", "宝典节点": "民间投资、民营经济", "细则支持原理": "试卷OCR第315-321行；经济与社会。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q13", "题型或模块判断": "经济与社会选择题", "宝典节点": "新质生产力、高质量发展", "细则支持原理": "试卷OCR第322-328行；经济与社会。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q14", "题型或模块判断": "当代国际政治与经济选择题", "宝典节点": "金砖国家新开发银行、国际金融治理", "细则支持原理": "试卷OCR第332-339行；当代国际政治与经济。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q15", "题型或模块判断": "当代国际政治与经济选择题", "宝典节点": "亚太经合组织、经济全球化", "细则支持原理": "试卷OCR第340-347行；当代国际政治与经济。", "证据等级": "试卷原题OCR", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q16-culture", "题型或模块判断": "文化主观题点", "宝典节点": "中华优秀传统文化、文化自信、创造性转化创新性发展", "细则支持原理": "正式阅卷细则第12-20行列文化传承创新、文化价值与文化自信；哲学正文只登记有哲学术语支撑的落点。", "证据等级": "正式阅卷细则边界", "当前处理": "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q17", "题型或模块判断": "政治与法治主观题", "宝典节点": "网络生态治理、党的领导、科学立法、严格执法、全民守法", "细则支持原理": "正式阅卷细则第22-46行明确运用《政治与法治》知识。", "证据等级": "正式阅卷细则", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q18(1)", "题型或模块判断": "法律与生活主观题", "宝典节点": "合同成立、合同效力、违约责任", "细则支持原理": "正式阅卷细则第50-70行明确运用《法律与生活》知识。", "证据等级": "正式阅卷细则", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q18(2)", "题型或模块判断": "逻辑与思维主观题", "宝典节点": "充分条件、必要条件、假言推理", "细则支持原理": "正式阅卷细则第71-93行明确运用《逻辑与思维》知识。", "证据等级": "正式阅卷细则", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q19", "题型或模块判断": "经济与社会主观题", "宝典节点": "海南自贸港、新发展格局、高水平开放", "细则支持原理": "正式阅卷细则第98-121行围绕经济与社会/自贸港政策。", "证据等级": "正式阅卷细则", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q20", "题型或模块判断": "当代国际政治与经济主观题", "宝典节点": "国际关系、国家利益、全球治理", "细则支持原理": "正式阅卷细则第122-140行属当代国际政治与经济。", "证据等级": "正式阅卷细则", "当前处理": "MODULE_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
    {"题号": "Q21-nonphilosophy", "题型或模块判断": "第21题非哲学政策点", "宝典节点": "党的领导、市场经济、举国体制、产业体系、人才优势", "细则支持原理": "正式阅卷细则第155-188行中除整体部分/系统优化/联系/群众观点外，主要为政治经济政策分析。", "证据等级": "正式阅卷细则边界", "当前处理": "NON_PHILOSOPHY_POINTS_BOUNDARY_EXCLUDED_BATCH30_CHAOYANG_FINAL", "是否进宝典": "否：模块边界排除"},
]


EVIDENCE_BY_KEY = {
    ("Q16", "辩证否定 / 守正创新"): ("正式阅卷细则第15-18行：遵循辩证否定观，剔除脱节部分、保留精髓、赋予时代内涵并推动双创", "formal-rubric"),
    ("Q16", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"): ("正式阅卷细则第21行补充“从实际出发”；题面第359-360行要求以当代之思叩问传统", "formal-rubric-broad-angle"),
    ("Q16", "规律的客观性"): ("正式阅卷细则第21行补充“规律”；第15-18行要求在传承创新中遵循辩证否定和文化发展逻辑", "formal-rubric-broad-angle"),
    ("Q16", "联系的普遍性 / 联系的观点（总）"): ("正式阅卷细则第19-21行：连接过去、现在与未来，并补充“联系”", "formal-rubric-broad-angle"),
    ("Q16", "发展的观点 / 发展的普遍性"): ("正式阅卷细则第18、21行：创造性转化、创新性发展，并补充“发展”", "formal-rubric-broad-angle"),
    ("Q16", "矛盾就是对立统一"): ("正式阅卷细则第21行补充“矛盾”；第15-18行材料逻辑围绕剔除与保留、传统与时代统一", "formal-rubric-broad-angle"),
    ("Q21", "整体与部分"): ("正式阅卷细则第152-153行：整体与部分的辩证统一；题面第469-470行：四大优势是相互依存、协同赋能的有机整体", "formal-rubric"),
    ("Q21", "系统观念 / 系统优化"): ("正式阅卷细则第152-153行：系统优化；题面第469-470行：四大优势相互依存、协同赋能", "formal-rubric"),
    ("Q21", "联系的普遍性 / 联系的观点（总）"): ("正式阅卷细则第152-153行：联系的观点看问题；题面第469-470行：相互依存、协同赋能、有机整体", "formal-rubric"),
    ("Q21", "人民群众"): ("正式阅卷细则第157-158行：坚持以人民为中心/群众观，激发人民群众投身现代化建设的积极性、主动性、创造性", "formal-rubric"),
}


def evidence_for(entry: dict[str, str]) -> tuple[str, str]:
    return EVIDENCE_BY_KEY.get((entry["question_no"], entry["canonical_node"]), ("NEED_EVIDENCE_REVIEW", "unmapped-current-docx-entry"))


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


def update_docx(timestamp: str) -> tuple[Path, int]:
    docx = core.current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_batch30_2026_chaoyang_final_{timestamp}{docx.suffix}")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as zin:
        xml = zin.read("word/document.xml")
    root = etree.fromstring(xml)
    body = root.find(f"{W}body")
    paras = body.findall(f"{W}p")
    existing_signature = {(e["canonical_node"], e["question_no"]) for e in core.extract_entries_from_root(root)}
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


def extract_entries() -> list[dict[str, str]]:
    old_suite = core.SUITE
    core.SUITE = SUITE
    try:
        root = core.load_docx_xml(core.current_docx())
        return core.extract_entries_from_root(root)
    finally:
        core.SUITE = old_suite


def update_ledger_and_accepted(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        ledger_rows = list(reader)
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch30_2026_chaoyang_final_{timestamp}{LEDGER.suffix}")
    shutil.copy2(LEDGER, backup)
    existing_keys = {(r.get("canonical_node"), r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in ledger_rows}
    added_ledger = 0
    for entry in entries:
        row = {"canonical_node": entry["canonical_node"], "source_suite": SUITE, "question_no": entry["question_no"], "inserted_heading": entry["registered_heading"]}
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
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch30_2026_chaoyang_final_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup_accepted)
    accepted_keys = {(r.get("source_suite"), r.get("question_no"), r.get("canonical_node"), r.get("registered_heading")) for r in accepted_records}
    added_accepted = 0
    with ACCEPTED.open("a", encoding="utf-8") as f:
        for entry in entries:
            evidence, boundary = evidence_for(entry)
            record = {
                "source_suite": SUITE,
                "question_no": entry["question_no"],
                "framework_node": entry["canonical_node"],
                "canonical_node": entry["canonical_node"],
                "student_facing_text": entry["student_facing_text"],
                "evidence_level": evidence,
                "boundary_note": boundary,
                "source_lane": "Codex Batch30 Chaoyang final registration and insertion",
                "source_repair_basis": SOURCE_PACKET,
                "source_lines": SOURCE_PACKET,
                "batch": BATCH_ID,
                "registered_heading": entry["registered_heading"],
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
    is_broad = boundary in {"formal-rubric-broad-angle", "formal-rubric-term-support"}
    return {
        "matrix_row_id": f"M{next_id:04d}",
        "row_source": MATRIX_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": entry["question_no"],
        "题型或模块判断": "必修四哲学正文条目",
        "是否进宝典": "是：已进入当前DOCX/PDF正文",
        "宝典节点": entry["canonical_node"],
        "细则支持原理": evidence,
        "证据等级": "正式细则宽角度/术语支持" if is_broad else "正式细则",
        "是否误放": "否：保留但标注宽角度或术语支持" if is_broad else "否",
        "是否需补厚": "否",
        "当前处理": "KEEP_IN_BODY_WITH_BROAD_FORMAL_SUPPORT" if is_broad else "KEEP_IN_BODY",
        "备注": "Batch30登记既有正文并补入缺漏；选择题因未见可靠答案键不进入正文，普通参考答案未冒充评分细则。",
        "source_artifact": SOURCE_PACKET,
    }


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch30_2026_chaoyang_final_{timestamp}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    rows = [r for r in rows if not (r.get("题源") == SUITE and r.get("row_source") == MATRIX_SOURCE)]
    max_id = 0
    for row in rows:
        match = re.match(r"M(\d+)", row.get("matrix_row_id", ""))
        if match:
            max_id = max(max_id, int(match.group(1)))
    new_rows = []
    next_id = max_id + 1
    for entry in entries:
        new_rows.append(matrix_body_row(next_id, entry))
        next_id += 1
    for boundary in BOUNDARY_ROWS:
        new_rows.append({
            "matrix_row_id": f"M{next_id:04d}",
            "row_source": MATRIX_SOURCE,
            "题源": SUITE,
            "年份": YEAR,
            "阶段": STAGE,
            "题号": boundary["题号"],
            "题型或模块判断": boundary["题型或模块判断"],
            "是否进宝典": boundary["是否进宝典"],
            "宝典节点": boundary["宝典节点"],
            "细则支持原理": boundary["细则支持原理"],
            "证据等级": boundary["证据等级"],
            "是否误放": "否",
            "是否需补厚": "否",
            "当前处理": boundary["当前处理"],
            "备注": "本题或本点不作为当前哲学宝典正文；选择题无答案键时不登记客观挂点，跨模块内容不偷换为必修四哲学原理。",
            "source_artifact": SOURCE_PACKET,
        })
        next_id += 1
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    return {
        "matrix_rows_total": len(rows) + len(new_rows),
        "batch_rows": len(new_rows),
        "body_rows": sum(1 for row in new_rows if row["是否进宝典"].startswith("是")),
        "boundary_rows": sum(1 for row in new_rows if not row["是否进宝典"].startswith("是")),
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
            row["current_status"] = "covered_by_batch30_recovery_matrix"
            row["blocker_or_next_action"] = "Batch30 registered existing DOCX entries, inserted rubric-supported Q16/Q21 points, and added boundary rows; render/model gates pending."
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

## Batch30 Update

- `2026朝阳期末` is now covered by `COVERAGE_FUSION_BATCH30_2026_CHAOYANG_FINAL_CODEX_20260525.md`.
- Matrix rows for the suite: `{matrix_rows_for_suite}`.
- Current DOCX mentions for the suite: `{docx_entries}`.
- Render QA and ClaudeCode Opus 4.7 recheck are still separate gates.
- `2026石景山期末` remains a special excluded source unless the user supplies a usable scoring rubric.
""", encoding="utf-8", newline="\n")
    return {"remaining_missing": len(missing), "covered": len(covered), "total": len(rows)}


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    body_list = "\n".join(f"- {entry['question_no']} -> {entry['canonical_node']} -> {entry['registered_heading']}" for entry in entries)
    SOURCE_TRANSCRIPTION.write_text(f"""# Batch30 Source Transcription - 2026朝阳期末

status: `SOURCE_PACKET_REGISTERED`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- scoring/rubric cache: `{RUBRIC_SOURCE}`
- paper cache: `{PAPER_SOURCE}`
- OCR full transcription: `{OCR_TEXT}`
- OCR line index: `{OCR_LINES}`

## Key Evidence

- Q16 rubric lines 11-18 require `辩证否定观`, 保留精髓、赋予时代内涵、立足时代之基、推动传统文化与现代元素融合、实现创造性转化和创新性发展.
- Q16 rubric lines 19-21 add the overall logic of connecting past, present, and future and explicitly list `从实际出发、规律、联系、发展、矛盾等`; these are retained as broad formal support, not inflated into detailed per-point rubric.
- Q21 rubric lines 152-153 directly list `整体与部分的辩证统一 / 系统优化 / 联系的观点看问题`.
- Q21 rubric lines 157-158 directly list `坚持以人民为中心 / 群众观` and require激发人民群众投身现代化建设的积极性、主动性、创造性.
- Q1-Q15 have paper OCR evidence, but no reliable answer key was found; therefore no objective-choice body rows were inserted.
- Q17, Q18(1), Q18(2), Q19, Q20 are excluded by formal rubric module boundaries.

## Governed DOCX Body Entries

{body_list}

## Evidence Guardrail

- 普通参考答案未被当作评分细则；正文落点使用正式阅卷细则/OCR行证据。
- Q16 的从实际出发、规律、联系、发展、矛盾等作为细则补充术语，矩阵标为 `正式细则宽角度/术语支持`。
- 选择题没有可核验答案键时，不登记客观选择题挂点。
""", encoding="utf-8", newline="\n")


def append_control_reports(inserted: int, entries: list[dict[str, str]], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    appendix = f"""

## Batch30 Local Application: 2026朝阳期末
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries after Batch30: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch30: `{global_result['remaining_missing']}`.
- Render QA is pending for this batch.
- ClaudeCode Opus 4.7 recheck is pending for this batch; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch30 Local Application: 2026朝阳期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")
    qa_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch30 Pending Render QA: 2026朝阳期末"
    if marker in qa_text:
        qa_text = qa_text[: qa_text.index(marker)]
    FORMAT_QA.write_text(qa_text + f"""

## Batch30 Pending Render QA: 2026朝阳期末
Updated: 2026-05-25

- Status: `RENDER_PENDING_AFTER_DOCX_MODIFICATION`.
- Batch30 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required next check: current DOCX/PDF render, heading styles, page count, labels, and new/old entry consistency.
""", encoding="utf-8", newline="\n")
    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH30_CHAOYANG_FINAL_RECHECK"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    MODEL_LEDGER.write_text(ledger + """

## CLAUDECODE_BATCH30_CHAOYANG_FINAL_RECHECK

status: `real_call_pending`

- Batch: `2026朝阳期末`.
- Prompt: `OPUS47_CLAUDECODE_BATCH30_2026_CHAOYANG_FINAL_RECHECK_PROMPT.md`.
- Required command shape: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Model gate before real evidence: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output is not qualified ClaudeCode evidence.
""", encoding="utf-8", newline="\n")


def write_batch_report(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    BATCH_REPORT.write_text(f"""# Coverage Fusion Batch30 - 2026朝阳期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch30 edit: `{backup}`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `2026朝阳期末` after Batch30: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `2026朝阳期末`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch30: `{global_result['remaining_missing']}`.

## Placement Verdict

- `2026朝阳期末` had 2 existing Q16/Q21 DOCX headings but no recovery-matrix rows; Batch30 repaired that ledger/matrix gap.
- Q16 keeps the existing辩证否定/守正创新 entry and adds the formal broad terms from the Q16 supplement: 从实际出发、规律、联系、发展、矛盾.
- Q21 keeps the existing整体与部分 entry and adds系统优化、联系观点、群众观, all directly supported by the Q21 marking rules.
- Q1-Q15 are not inserted as objective-choice body rows because no reliable answer key was found.
- Q17, Q18, Q19, Q20 and Q21 non-philosophy policy points are boundary-excluded by module or point scope.

## Remaining Gates

- Render QA is pending because Batch30 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
""", encoding="utf-8", newline="\n")


def main() -> None:
    for required in [GPT_BUNDLE, RUBRIC_SOURCE, PAPER_SOURCE, OCR_TEXT, OCR_LINES, MATRIX, LEDGER, ACCEPTED]:
        if not required.exists():
            raise FileNotFoundError(required)
    core.SUITE = SUITE
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    entries = extract_entries()
    if len(entries) != 10:
        raise RuntimeError(f"Expected 10 governed {SUITE} entries after Batch30, found {len(entries)}")
    unmapped = [entry for entry in entries if evidence_for(entry)[0] == "NEED_EVIDENCE_REVIEW"]
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
