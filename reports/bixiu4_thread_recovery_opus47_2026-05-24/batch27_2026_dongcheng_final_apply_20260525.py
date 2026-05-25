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

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH27_2026_DONGCHENG_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH27_2026_DONGCHENG_FINAL_CODEX_20260525.md"

PREPROCESSED = ROOT / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2026各区模拟题__2026各区期末和期中__2026东城期末.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "e4d67789c91d1b92_2026东城期末细则.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "15664381470d8300_2026北京东城高三_上_期末政治_教师版.md"

SUITE = "2026东城期末"
YEAR = "2026"
STAGE = "期末"
BATCH_ID = "batch27_2026_dongcheng_final"
MATRIX_SOURCE = "codex_batch27_2026_dongcheng_final"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; "
    "current DOCX verified: 7 existing unregistered 2026东城期末 headings were present before Batch27"
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "矛盾就是对立统一",
        "question_no": "Q3",
        "question_label": "第3题（选择题）",
        "material_trigger": "教师版第3题写“落叶缓扫”，正确项B为“保障城市安全卫生与尊重人文需求之间的矛盾推动城市精细化治理”；细则详解第269-274行确认B正确。",
        "question_prompt": "从城市落叶“片叶不留”到整体化“落叶缓扫”，设问要求判断这一治理变化说明了什么。",
        "why_trigger": "题干把城市安全卫生与市民审美、人文需求放在同一治理情境中，两方面既有张力又统一于城市精细化治理目标，因此对应矛盾双方的对立统一。",
        "answer_landing": "本题正确项B只作为客观选择题挂点。城市治理既要保障安全卫生，又要尊重市民对自然之美、季节之韵的需要；这两种要求在治理实践中形成矛盾关系，推动治理方式从简单清扫转向更精细、更有人文温度的安排。",
    },
    {
        "canonical_node": "联系的客观性",
        "question_no": "Q4",
        "question_label": "第4题（选择题）",
        "material_trigger": "教师版第4题正确答案D；正确项②为“核糖核酸与氨基酸的自在联系可能是生命起源的关键”，细则第340-344行确认②正确。",
        "question_prompt": "研究团队模拟早期地球环境，让核糖核酸与氨基酸通过自发化学反应结合，形成通向蛋白质合成的关键中间体。",
        "why_trigger": "材料强调的是早期地球条件下核糖核酸与氨基酸发生自发化学反应，这种自在联系不以人的意志为转移，研究只是发现和揭示这种联系。",
        "answer_landing": "本题正确项②只作为客观选择题挂点。生命起源研究发现核糖核酸与氨基酸之间可能存在客观的自在联系，人们不能随意创造这种联系，只能在尊重客观联系的基础上认识、把握并利用它。",
    },
    {
        "canonical_node": "认识对实践的反作用",
        "question_no": "Q4",
        "question_label": "第4题（选择题）",
        "material_trigger": "教师版第4题正确答案D；正确项④为“基础科学的突破能够推动生物工程与生物技术的应用”，细则第343-344行确认④正确。",
        "question_prompt": "该基础科学成果为解答生命起源关键问题提供全新思路，并有望应用于人工生命系统构建、原位蛋白质合成技术以及新型药物精准递送。",
        "why_trigger": "基础科学认识形成后，会反过来指导人工生命系统构建、蛋白质合成技术和药物递送等实践活动。",
        "answer_landing": "本题正确项④只作为客观选择题挂点。科学认识不是停留在解释层面，正确认识能够指导实践发展；生命起源研究的新突破能为生物工程、生物技术和医药应用提供新的实践路径。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "细则第156行将“意识能动作用（社会意识）”列为哲学知识角度；第159-161行提示可按“表象→深意”推进，可用“意识能动反映→文化作用→价值观”。",
        "question_prompt": "第16题围绕“白”的表象、留白、清白等意象，要求从哲学与文化角度说明“白，不止于白”。",
        "why_trigger": "材料不是单纯描述颜色，而是要求把“白”的可感表象上升为艺术手法、道德准则和文化符号，这需要说明意识对客观对象的能动反映和创造性表达。",
        "answer_landing": "“白，不止于白”说明意识具有能动作用。人能够在社会实践和文化传承中把客观色彩转化为审美意境、思维方法和价值表达；对“留白”“清白”的理解，体现了意识对现实的能动反映，也能反过来影响人的精神追求和行为选择。",
    },
    {
        "canonical_node": "价值判断与价值选择",
        "question_no": "Q16",
        "question_label": "第16题（主观题）",
        "material_trigger": "细则第156行明列“价值观（价值判断和价值选择）”；第174行示例把“清白”说明为清正廉洁、刚正不阿的道德准则和责任担当。",
        "question_prompt": "第16题要求围绕“白，不止于白”表达见解，材料包含“清白”所承载的清正廉洁、刚正不阿等价值意蕴。",
        "why_trigger": "“清白”已经不是颜色判断，而是对做人做事标准的价值判断，并指向清正廉洁、责任担当等价值选择。",
        "answer_landing": "分析“清白”时要落到正确价值判断与价值选择。清正廉洁、刚正不阿体现了符合社会发展要求和人民根本利益的价值取向；把“白”理解为人格操守和家国责任，能引导人们在实际生活中作出正确价值选择。",
    },
    {
        "canonical_node": "规律的客观性",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "细则第551行列明“运用系统观念/科学思维/辩证思维/矛盾观/尊重客观规律等”，材料第539-541行强调不同区域自然禀赋与发展基础存在差异。",
        "question_prompt": "第21题要求综合运用所学，说明我国如何在推进中国式现代化进程中把区域发展落差的势能转化为动能。",
        "why_trigger": "区域差异不是可以主观抹平的对象。材料要求立足各区域自然禀赋、发展基础和比较优势，把差异转化为协同发展的动能，这需要尊重区域发展规律。",
        "answer_landing": "推进区域协调发展要尊重规律的客观性。我国没有无视区域自然禀赋和发展基础差异，而是引导京津冀、长三角、粤港澳以及东北、中部、西部等区域立足比较优势，按区域分工和协同规律推动优势互补，把落差中的势能转化为现代化建设动能。",
    },
]


BOUNDARY_ROWS = [
    ("Q1", "文化/政治选择题", "典礼制度、政治品格、民族复兴力量", "教师版答案D；题干考查典礼制度的政治文化功能，不作为当前哲学正文条目。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q2", "文化与公共服务选择题", "城市书房、公共文化服务、书香社会", "教师版答案C；核心是公共文化服务适应人民文化需求，不强行转为哲学主观题落点。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q5", "经济/消费/文化选择题", "可爱经济、消费需求、企业经营", "教师版答案A；细则提示“可爱产品并不属于新事物”，不进入发展观正文。", "教师版客观题答案+细则边界", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q6", "逻辑与思维选择题", "三段论推理/前提补充", "教师版答案B；属选必三逻辑推理，不进入必修四哲学正文。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q7", "逻辑与思维选择题", "矛盾关系判断/预测推理", "教师版答案A；题目考查逻辑关系和推理，不等同哲学“矛盾就是对立统一”正文依据。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q8", "政治与法治选择题", "党的思想工作/意识形态工作", "教师版答案B；核心是党的思想政治工作，且错误项提示不要把实践误作社会意识。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q9", "政治与法治选择题", "人大常委会/法律监督/代表履职", "教师版答案A；属政治与法治模块，不进入哲学正文。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q10", "法律与生活选择题", "法律案例/责任承担", "教师版答案D；属法律与生活模块，不进入哲学正文。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q11", "法律与生活选择题", "劳动合同/劳动争议", "教师版答案C；属劳动法律规则，不进入哲学正文。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q12", "经济选择题", "农村集体经济/经营管理", "教师版答案B；属经济制度和乡村经营，不进入哲学正文。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q13", "经济选择题", "投资于人/宏观政策/扩大内需", "教师版答案C；属经济政策，不进入哲学正文。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q14", "当代国际政治与经济选择题", "具身智能/全球治理", "教师版答案D；属国际治理与经济科技议题，不进入哲学正文。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q15", "经济/国际经济选择题", "投资中国/开放发展", "教师版答案C；属经济与开放发展判断，不进入哲学正文。", "教师版客观题答案+模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q16-culture", "文化主观题点", "中华优秀传统文化、民族精神、文化作用", "细则第157行列文化角度；本交付为哲学宝典，文化点登记边界，不塞入哲学节点。", "正式细则边界", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q17(1)", "经济主观题", "新质生产力/经济高质量发展/产业政策", "细则第214-250行按经济知识组织答案，不进入必修四哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q17(2)", "逻辑与思维主观题", "三段论规则/有效推理", "细则第279-304行按三段论规则给分，属选必三逻辑，不进入哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q18", "法律与生活主观题", "合同、侵权、权利保护", "细则第324-414行按法律规则作答，不进入哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q19", "政治与法治主观题", "改革与法治互动、法治国家/政府/社会", "设问明确要求《政治与法治》知识，细则第437-482行按法治国家、法治政府、法治社会给分；不把普通改革表述冒充哲学改革细则。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q20", "当代国际政治与经济主观题", "国际合作/开放发展/全球治理", "细则第483-494行及对应材料属国际政治经济模块，不进入哲学正文。", "正式细则模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH27_DONGCHENG_FINAL"),
    ("Q21-nonphilosophy", "综合主观题中非哲学点", "党的领导、新发展理念、经济高质量发展、高水平开放", "细则第548-550、571-581行包含党的领导、人民立场、新发展理念等综合点；仅登记明确哲学/思维方法角度，其余非哲学点作边界。", "正式细则边界", "NONPHILOSOPHY_COMPREHENSIVE_POINT_BOUNDARY_EXCLUDED"),
]


EVIDENCE_BY_KEY = {
    ("Q3", "矛盾就是对立统一"): ("教师版第3题答案B；细则第269-274行确认“保障安全卫生与尊重人文需求的矛盾”推动治理", "objective-choice-only"),
    ("Q4", "联系的客观性"): ("教师版第4题答案D；正确项②及细则第340-344行确认核糖核酸与氨基酸的自在联系", "objective-choice-only"),
    ("Q4", "认识对实践的反作用"): ("教师版第4题答案D；正确项④及细则第343-344行确认基础科学突破推动生物工程与生物技术应用", "objective-choice-only"),
    ("Q16", "整体与部分"): ("细则第156行列“整体部分等”为哲学知识角度；用于说明“白”意象由局部表象联结整体文化深意", "formal-rubric"),
    ("Q16", "矛盾就是对立统一"): ("细则第156行列“矛盾对立统一”；第173行示例说明“留白”以无衬有、以虚映实", "formal-rubric"),
    ("Q16", "价值观的导向作用"): ("细则第156行列“价值观”；第174行示例明确“价值观具有导向作用”", "formal-rubric"),
    ("Q16", "主观能动性 / 意识的能动作用"): ("细则第156行列“意识能动作用（社会意识）”；第159-161行提示“表象→深意”和意识能动反映", "formal-rubric"),
    ("Q16", "价值判断与价值选择"): ("细则第156行列“价值判断和价值选择”；第174行以“清白”道德准则和责任担当作示例", "formal-rubric"),
    ("Q21", "整体与部分"): ("细则第551行要求立足整体、统筹全局，以优势地区带动其他地区发展", "formal-rubric"),
    ("Q21", "系统观念 / 系统优化"): ("细则第551行明列“系统观念”，并要求统筹东中西部、南北方协调发展、国内协同与内外联动", "formal-rubric"),
    ("Q21", "矛盾就是对立统一"): ("细则第551行列“辩证思维/矛盾观”；按综合题宽角度说明区域落差可转化为发展动能", "formal-rubric-broad-angle"),
    ("Q21", "价值判断与价值选择"): ("细则第550行列人民价值导向，第573、581行确认人民立场为核心知识点", "formal-rubric-broad-angle"),
    ("Q21", "规律的客观性"): ("细则第551行明列“尊重客观规律等”；材料第539-541行强调区域自然禀赋和发展基础差异", "formal-rubric-broad-angle"),
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
    backup = docx.with_name(f"{docx.stem}_backup_before_batch27_2026_dongcheng_final_{timestamp}{docx.suffix}")
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
        n = next_heading_number(paras, node)
        heading = f"{n}. {SUITE} {spec['question_label']}"
        heading_template, body_template = template_paragraphs(paras, node)
        _start, end = find_node_bounds(paras, node)
        insert_at = end
        new_paras = [
            clone_with_text(heading_template, heading),
            clone_with_text(body_template, f"【材料触发点】{spec['material_trigger']}"),
            clone_with_text(body_template, f"【设问】{spec['question_prompt']}"),
            clone_with_text(body_template, f"【为什么能想到】{spec['why_trigger']}"),
            clone_with_text(body_template, f"【答案落点】{spec['answer_landing']}"),
        ]
        for offset, p in enumerate(new_paras):
            body.insert(insert_at + offset, p)
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch27_2026_dongcheng_final_{timestamp}{LEDGER.suffix}")
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
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch27_2026_dongcheng_final_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup_accepted)
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
                "source_lane": "Codex Batch27 Dongcheng final registration and insertion",
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
    is_objective = boundary == "objective-choice-only"
    is_broad = boundary == "formal-rubric-broad-angle"
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
        "证据等级": "教师版客观题答案+细则详解" if is_objective else ("正式细则宽角度支持" if is_broad else "正式细则"),
        "是否误放": "否：保留但标注综合题宽角度支持" if is_broad else "否",
        "是否需补厚": "否",
        "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else ("KEEP_IN_BODY_WITH_BROAD_FORMAL_SUPPORT" if is_broad else "KEEP_IN_BODY"),
        "备注": "Batch27登记既有正文并补入缺漏；客观题仅按正确项挂点，普通参考答案未冒充主观评分细则。",
        "source_artifact": SOURCE_PACKET,
    }


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch27_2026_dongcheng_final_{timestamp}{MATRIX.suffix}")
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
                "备注": "本题或本点不作为当前哲学宝典正文；不把法律、逻辑、经济、文化或综合非哲学点偷换为哲学原理。",
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
            row["current_status"] = "covered_by_batch27_recovery_matrix"
            row["blocker_or_next_action"] = "Batch27 registered existing DOCX entries, inserted formal-rubric/objective-choice points, and added boundary rows; render/model gates pending."
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

## Remaining Missing Midterm/Final Suites

| suite | stage_dir | status | next action |
|---|---|---|---|
{missing_table}

## Batch27 Update

- `2026东城期末` is now covered by `COVERAGE_FUSION_BATCH27_2026_DONGCHENG_FINAL_CODEX_20260525.md`.
- Matrix rows for the suite: `{matrix_rows_for_suite}`.
- Current DOCX mentions for the suite: `{docx_entries}`.
- Render QA and ClaudeCode Opus 4.7 recheck are still separate gates.
- `2026石景山期末` remains a special excluded source unless the user supplies a usable scoring rubric.
""",
        encoding="utf-8",
        newline="\n",
    )
    return {"remaining_missing": len(missing), "covered": len(covered), "total": len(rows)}


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    body_list = "\n".join(f"- {e['question_no']} -> {e['canonical_node']} -> {e['registered_heading']}" for e in entries)
    SOURCE_TRANSCRIPTION.write_text(
        f"""# Batch27 Source Transcription - 2026东城期末

status: `SOURCE_PACKET_REGISTERED`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- scoring/rubric cache: `{RUBRIC_SOURCE}`
- teacher paper cache: `{TEACHER_SOURCE}`

## Key Evidence

- Q3: teacher paper lines 45-49 ask about “落叶缓扫”; correct option B says “保障城市安全卫生与尊重人文需求之间的矛盾推动城市精细化治理”. Rubric/source lines 269-274 confirm B correct and name that contradiction.
- Q4: teacher paper lines 55-63 and answer key give D. Rubric/source lines 340-344 confirm option ② “自在联系” and option ④ “基础科学突破能够推动生物工程与生物技术的应用”.
- Q16: rubric/source lines 154-176 list philosophy angles: 矛盾对立统一、价值观（价值判断和价值选择）、意识能动作用（社会意识）、整体部分等; example lines 173-174 support 留白/虚实 and 清白/价值观.
- Q19: rubric/source lines 437-482 are explicitly 政治与法治 scoring rules. This is boundary-excluded and not used as a philosophy “改革” scoring source.
- Q21: rubric/source lines 548-551 and 571-581 support 党的领导、人民立场、新发展理念、系统观念等; philosophy rows keep only system/overall/contradiction/value/rule angles with evidence labels.

## Governed DOCX Entries

{body_list}

## Evidence Rule

- Objective-choice rows are labeled objective-only.
- Ordinary teacher reference answers do not become subjective scoring rubrics.
- Broad comprehensive Q21 angles are not treated as detailed point-by-point scoring unless the scoring text directly names the principle.
""",
        encoding="utf-8",
        newline="\n",
    )


def append_control_reports(inserted: int, entries: list[dict[str, str]], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    appendix = f"""

## Batch27 Local Application: 2026东城期末
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries after Batch27: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch27: `{global_result['remaining_missing']}`.
- Render QA is pending for this batch.
- ClaudeCode Opus 4.7 recheck is pending for this batch; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch27 Local Application: 2026东城期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")

    qa_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch27 Pending Render QA: 2026东城期末"
    if marker in qa_text:
        qa_text = qa_text[: qa_text.index(marker)]
    FORMAT_QA.write_text(
        qa_text
        + f"""

## Batch27 Pending Render QA: 2026东城期末
Updated: 2026-05-25

- Status: `RENDER_PENDING_AFTER_DOCX_MODIFICATION`.
- Batch27 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required next check: current DOCX/PDF render, heading styles, page count, labels, and new/old entry consistency.
""",
        encoding="utf-8",
        newline="\n",
    )

    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH27_DONGCHENG_FINAL_RECHECK"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    MODEL_LEDGER.write_text(
        ledger
        + """

## CLAUDECODE_BATCH27_DONGCHENG_FINAL_RECHECK

status: `real_call_pending`

- Batch: `2026东城期末`.
- Prompt: `OPUS47_CLAUDECODE_BATCH27_2026_DONGCHENG_FINAL_RECHECK_PROMPT.md`.
- Required command shape: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Model gate before real evidence: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output is not qualified ClaudeCode evidence.
""",
        encoding="utf-8",
        newline="\n",
    )


def write_batch_report(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    BATCH_REPORT.write_text(
        f"""# Coverage Fusion Batch27 - 2026东城期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch27 edit: `{backup}`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `2026东城期末` after Batch27: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `2026东城期末`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch27: `{global_result['remaining_missing']}`.

## Placement Verdict

- `2026东城期末` had 7 existing DOCX headings but no recovery-matrix rows; Batch27 repaired that ledger/matrix gap.
- Six new DOCX entries were inserted: Q3 矛盾就是对立统一 objective row; Q4 联系的客观性 and 认识对实践的反作用 objective rows; Q16 意识能动作用 and 价值判断与价值选择; Q21 规律的客观性.
- Q1/Q2/Q5-Q15/Q17-Q20 and non-philosophy parts of Q16/Q21 were registered as boundary exclusions.
- Q19 was explicitly kept out of the philosophy “改革” node because its set question and scoring rules are 《政治与法治》.

## Remaining Gates

- Render QA is pending because Batch27 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` until real runtime evidence is recorded.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
""",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    entries = extract_entries_from_root(load_docx_xml(current_docx()))
    if len(entries) != 13:
        raise RuntimeError(f"Expected 13 governed {SUITE} DOCX entries after Batch27, found {len(entries)}")
    unmapped = [e for e in entries if evidence_for(e)[0] == "NEED_EVIDENCE_REVIEW"]
    if unmapped:
        raise RuntimeError(f"Unmapped evidence entries: {unmapped}")
    ledger_result = update_ledger_and_accepted(entries, timestamp)
    matrix_result = update_matrix(entries, timestamp)
    global_result = update_global_audit(len(entries), int(matrix_result["batch_rows"]))
    write_source_transcription(entries)
    append_control_reports(inserted, entries, matrix_result, global_result)
    write_batch_report(backup, inserted, entries, ledger_result, matrix_result, global_result)
    print(json.dumps({
        "suite": SUITE,
        "inserted": inserted,
        "entries": len(entries),
        "matrix": matrix_result,
        "ledger": ledger_result,
        "global": global_result,
        "backup": str(backup),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
