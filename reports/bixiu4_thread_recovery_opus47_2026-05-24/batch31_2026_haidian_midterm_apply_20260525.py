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
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2026各区模拟题__2026各区期末和期中__2026海淀期中.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "e65381bd22912637_2026海淀期中细则.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "11cac42f979196cd_2025北京海淀高三_上_期中政治_教师版.md"
OCR_TEXT = RECOVERY / "BATCH31_2026_HAIDIAN_MIDTERM_RUBRIC_OCR_TRANSCRIPTION_20260525.md"
OCR_LINES = RECOVERY / "BATCH31_2026_HAIDIAN_MIDTERM_RUBRIC_OCR_LINES_20260525.md"

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH31_2026_HAIDIAN_MIDTERM_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH31_2026_HAIDIAN_MIDTERM_CODEX_20260525.md"

SUITE = "2026海淀期中"
YEAR = "2026"
STAGE = "期中"
BATCH_ID = "batch31_2026_haidian_midterm"
MATRIX_SOURCE = "codex_batch31_2026_haidian_midterm"
EXPECTED_ENTRIES = 5
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; OCR text: {OCR_TEXT}; OCR line index: {OCR_LINES}; "
    "teacher source lines 92-97 for Q9 stem/options and lines 226-231 for answer key; "
    "teacher source lines 208-223 for Q22 prompt and lines 256-258 ordinary reference answer only; "
    "rubric OCR page_094 lines 013-029 formal Q22(2) scoring/common-knowledge list and lines 030-043 examples."
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "人民群众",
        "question_no": "Q9",
        "question_label": "第9题（选择题）",
        "material_trigger": "教师版第9题围绕北京市“十五五”规划建言征集，正确答案A对应①“坚持问计于民，激发人民群众的智慧和力量”和③“以人民为中心的价值取向”。",
        "question_prompt": "规划建言征集为什么能够体现人民群众在城市治理和发展规划中的作用。",
        "why_trigger": "题肢直接把“问计于民”和“人民群众的智慧和力量”作为正确选项，能客观挂到历史唯物主义的人民群众节点；但它只是选择题答案键，不扩展为主观评分细则。",
        "answer_landing": "答案选A。问计于民说明人民群众是社会历史的主体，规划形成要尊重人民主体地位，汇聚人民群众智慧和力量。",
    },
    {
        "canonical_node": "主观能动性 / 意识的能动作用",
        "question_no": "Q22(2)",
        "question_label": "第22题第（2）问（主观题）",
        "material_trigger": "正式阅卷细则page_094在Q22(2)“常见知识”中列明“发挥主观能动性”，并要求分析扣在“势”上，说明其在中华民族伟大复兴中的作用。",
        "question_prompt": "综合运用所学，谈谈你对“中华民族伟大复兴势不可挡”的理解。",
        "why_trigger": "题干要求解释“势不可挡”不仅是客观趋势，也要求主体把握历史机遇、积极作为；细则明确给出发挥主观能动性这一必修四可用知识。",
        "answer_landing": "中华民族伟大复兴要在尊重历史大势和发展规律的基础上发挥主观能动性，把民族复兴的目标、信心和行动统一起来，通过主动奋斗把有利态势转化为现实成果。",
    },
    {
        "canonical_node": "事物发展是前进性与曲折性的统一",
        "question_no": "Q22(2)",
        "question_label": "第22题第（2）问（主观题）",
        "material_trigger": "正式阅卷细则page_094把“发展观（前途光明、道路曲折）”列入Q22(2)常见知识，直接对应发展前途与道路曲折的辩证统一。",
        "question_prompt": "综合运用所学，谈谈你对“中华民族伟大复兴势不可挡”的理解。",
        "why_trigger": "“势不可挡”强调前途光明，但材料又放在百年未有之大变局语境中，必须同时看到复兴道路并非一帆风顺。",
        "answer_landing": "中华民族伟大复兴的前途是光明的，这是历史大势；但实现过程会遇到风险挑战和曲折考验，要坚定信心、迎难而上，在曲折中不断推进复兴进程。",
    },
    {
        "canonical_node": "社会发展的两大基本规律和基本矛盾",
        "question_no": "Q22(2)",
        "question_label": "第22题第（2）问（主观题）",
        "material_trigger": "正式阅卷细则page_094在Q22(2)常见知识中列明“人类社会发展规律”，要求从复兴为什么不可挡、如何做到不可挡展开分析。",
        "question_prompt": "综合运用所学，谈谈你对“中华民族伟大复兴势不可挡”的理解。",
        "why_trigger": "复兴不可挡的深层理由不能只写信心口号，而要说明中国式现代化和民族复兴符合社会发展规律、顺应历史前进方向。",
        "answer_landing": "中华民族伟大复兴符合人类社会发展规律和中国社会发展方向。要把握生产力发展、制度完善和社会进步的规律性，在顺应历史规律中推进复兴。",
    },
    {
        "canonical_node": "人民群众",
        "question_no": "Q22(2)",
        "question_label": "第22题第（2）问（主观题）",
        "material_trigger": "正式阅卷细则page_094在Q22(2)常见知识中列明“人民群众主体地位”，示例还写明人民群众是推动中华民族伟大复兴的力量之源。",
        "question_prompt": "综合运用所学，谈谈你对“中华民族伟大复兴势不可挡”的理解。",
        "why_trigger": "民族复兴的主体力量来自人民群众；细则不仅列出人民群众主体地位，还要求说明动员人民群众投身社会主义现代化建设。",
        "answer_landing": "人民群众是历史的创造者，是推进中华民族伟大复兴的力量之源。坚持人民主体地位，汇聚全体人民智慧和力量，才能使复兴大势转化为现实力量。",
    },
]


BOUNDARY_ROWS = [
    ("Q1", "中国特色社会主义选择题", "中国特色社会主义制度/历史主动", "教师版答案B；题面属于中国特色社会主义制度与历史方位判断，不含可进必修四哲学正文的细则支持原理。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q2", "经济与法治选择题", "民营经济/法治化营商环境", "教师版答案D；考查民营经济与法律政策环境，非必修四哲学落点。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q3", "经济与社会选择题", "市场竞争/产业发展", "教师版答案A；经济模块判断，不作为哲学原理登记。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q4", "经济与社会选择题", "就业/民生政策", "教师版答案B；就业与经济政策模块，不进入必修四哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q5", "文化/经济选择题", "文化产品出海/文化传播", "教师版答案C；文化传播和经济场景，可作文化边界材料，不作为本批哲学正文落点。", "教师版答案键+题面", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q6", "经济与社会选择题", "社会保障/投资于人", "教师版答案D；经济社会政策判断，不进入哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q7", "政治与法治选择题", "党的作风/自我革命", "教师版答案C；政治与法治模块，不作为哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q8", "政治与法治选择题", "人民代表大会/政协/制度运行", "教师版答案B；政治制度模块，不进入必修四哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q9-value", "政治与法治选择题价值表述", "以人民为中心的价值取向", "教师版答案A含③“以人民为中心的价值取向”，但该表述在规划建言政治治理语境中使用；本批只把①③合并为人民群众客观挂点，不另造价值观正文条。", "教师版答案键+题面", "VALUE_WORDING_BOUNDARY_NO_SEPARATE_BODY_ROW"),
    ("Q10", "政治与法治选择题", "民族区域自治/西藏发展", "教师版答案D；民族政策和政治制度模块，不进入哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q11", "政治与法治/法律选择题", "生态环境法典/法治建设", "教师版答案A；法治建设模块，不作为哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q12", "当代国际政治与经济选择题", "绿色丝绸之路/国际合作", "教师版答案B；国际政治经济和生态文明表达，不进哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q13", "当代国际政治与经济选择题", "中国-中亚精神/国际关系", "教师版答案D；国际政治经济模块，不进入哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q14", "当代国际政治与经济选择题", "海南自由贸易港/开放发展", "教师版答案C；开放经济与国际经济规则，不作为哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q15", "当代国际政治与经济选择题", "中国欧盟关系/国际合作", "教师版答案C；国际关系模块，不进入哲学正文。", "教师版答案键+题面", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q16", "经济与社会主观题", "绿色就业/产业转型/就业结构", "题干限定《经济与社会》；无必修四哲学评分细则落点。", "题面模块限定+教师版参考", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q17", "经济与社会主观题", "要素市场化配置改革", "题干限定经济与社会；评分方向为要素市场改革和经济体制，不进入哲学正文。", "题面模块限定+教师版参考", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q18", "政治与法治主观题", "人民城市/治理效能", "题干限定政治与法治；不把人民城市治理语言偷换为人民群众哲学正文。", "题面模块限定+教师版参考", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q19", "政治与法治主观题", "基层群众自治/法律修订", "题干限定政治与法治；基层治理与法律修订不作为必修四哲学正文。", "题面模块限定+教师版参考", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q20", "政治与法治/法律主观题", "检察机关/公益诉讼", "题干和参考方向为法治建设、检察履职和公益诉讼，不进入哲学正文。", "题面模块限定+教师版参考", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q21", "经济与社会主观题", "机器人应用标杆城市/产业政策", "题干限定经济与社会；材料虽有城市建设语境，但评分不支撑哲学正文。", "题面模块限定+教师版参考", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q22(1)", "当代国际政治与经济主观题", "全球治理/人类命运共同体/国际关系民主化", "正式阅卷细则page_083为Q22(1)全球治理评分，限定《当代国际政治与经济》，不进入必修四哲学正文。", "正式阅卷细则", "MODULE_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
    ("Q22(2)-nonphilosophy", "综合主观题非哲学点", "党的领导/制度优势/人民当家作主/人类命运共同体/民族精神", "正式阅卷细则page_094允许多模块作答；本批只登记其中有必修四哲学支撑的主观能动性、发展前途与曲折、人类社会发展规律、人民群众主体地位，其余模块点边界排除。", "正式阅卷细则模块边界", "NON_PHILOSOPHY_POINTS_BOUNDARY_EXCLUDED_BATCH31_HAIDIAN_MIDTERM"),
]


EVIDENCE_BY_KEY = {
    ("Q9", "人民群众"): (
        "教师版第9题题面与答案键A：正确项①“坚持问计于民，激发人民群众的智慧和力量”、③“以人民为中心的价值取向”；仅作客观选择题挂点。",
        "objective-choice-only-teacher-answer-key",
    ),
    ("Q22(2)", "主观能动性 / 意识的能动作用"): (
        "正式阅卷细则page_094 Q22(2)常见知识列明“发挥主观能动性”，并要求分析扣在“势”上、说明其在民族复兴中的作用。",
        "formal-rubric-term-support",
    ),
    ("Q22(2)", "事物发展是前进性与曲折性的统一"): (
        "正式阅卷细则page_094 Q22(2)常见知识列明“发展观（前途光明、道路曲折）”。",
        "formal-rubric",
    ),
    ("Q22(2)", "社会发展的两大基本规律和基本矛盾"): (
        "正式阅卷细则page_094 Q22(2)常见知识列明“人类社会发展规律”，属于社会历史发展规律的宽口径正式支持。",
        "formal-rubric-broad-angle",
    ),
    ("Q22(2)", "人民群众"): (
        "正式阅卷细则page_094 Q22(2)常见知识列明“人民群众主体地位”，示例写明人民群众是推动中华民族伟大复兴的力量之源。",
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
    backup = docx.with_name(f"{docx.stem}_backup_before_batch31_2026_haidian_midterm_{timestamp}{docx.suffix}")
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch31_2026_haidian_midterm_{timestamp}{LEDGER.suffix}")
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
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch31_2026_haidian_midterm_{timestamp}{ACCEPTED.suffix}")
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
                "source_lane": "Codex Batch31 Haidian midterm registration and insertion",
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
        "证据等级": "教师版答案键+试卷原题" if is_objective else ("正式阅卷细则宽角度/术语支持" if is_broad else "正式阅卷细则"),
        "是否误放": "否：保留但标注宽角度或客观挂点" if (is_objective or is_broad) else "否",
        "是否需补厚": "否",
        "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else ("KEEP_IN_BODY_WITH_BROAD_FORMAL_SUPPORT" if is_broad else "KEEP_IN_BODY"),
        "备注": "Batch31新增登记；普通参考答案只作题面/答案键核对，未冒充主观评分细则。",
        "source_artifact": SOURCE_PACKET,
    }


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch31_2026_haidian_midterm_{timestamp}{MATRIX.suffix}")
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
            "备注": "本题或本点不作为当前哲学宝典正文；不把经济、法律、国际政治、文化或普通参考答案偷换为哲学原理。",
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
            row["current_status"] = "covered_by_batch31_recovery_matrix"
            row["blocker_or_next_action"] = "Batch31 inserted rubric-supported/objective-choice entries and added question-level boundary rows; render/model gates pending."
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

## Batch31 Update

- `2026海淀期中` is now covered by `COVERAGE_FUSION_BATCH31_2026_HAIDIAN_MIDTERM_CODEX_20260525.md`.
- Matrix rows for the suite: `{matrix_rows_for_suite}`.
- Current DOCX mentions for the suite: `{docx_entries}`.
- Render QA and ClaudeCode Opus 4.7 recheck are still separate gates.
- `2026石景山期末` remains a special excluded source unless the user supplies a usable scoring rubric.
""", encoding="utf-8", newline="\n")
    return {"remaining_missing": len(missing), "covered": len(covered), "total": len(rows)}


def write_source_transcription(entries: list[dict[str, str]]) -> None:
    body_list = "\n".join(f"- {e['question_no']} -> {e['canonical_node']} -> {e['registered_heading']}" for e in entries)
    SOURCE_TRANSCRIPTION.write_text(f"""# Batch31 Source Transcription - 2026海淀期中

status: `SOURCE_PACKET_REGISTERED`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- scoring/rubric cache metadata: `{RUBRIC_SOURCE}`
- teacher-version paper/answer cache: `{TEACHER_SOURCE}`
- OCR transcription: `{OCR_TEXT}`
- OCR line index: `{OCR_LINES}`

## Key Evidence

- Q9 objective row uses the teacher-version answer key `9A`; correct option ① writes “坚持问计于民，激发人民群众的智慧和力量” and option ③ writes “以人民为中心的价值取向”. This is objective-choice-only evidence.
- Q22(2) formal scoring page_094 says knowledge can come from multiple modules and lists the 必修四 angles: “发挥主观能动性，发展观（前途光明、道路曲折），人类社会发展规律，人民群众主体地位，民族精神等”.
- Q22(2) formal scoring page_094 examples include “人民群众是推动中华民族伟大复兴的力量之源” and “动员人民群众积极投身社会主义现代化建设”.
- Teacher-version Q22(2) ordinary reference answer only says it can be answered from党的领导、人民力量、制度优势、人类命运共同体等 angles; it is not used as a formal scoring rubric.
- Q22(1) formal scoring page_083 is restricted to《当代国际政治与经济》global governance and is boundary-excluded from the 必修四哲学 body.

## Governed DOCX Body Entries

{body_list}

## Evidence Guardrail

- 普通参考答案没有冒充评分细则。
- Q9 only counts as an objective-choice body hook, not as a subjective rubric.
- Q22(2) only registers the philosophy angles directly supported by page_094 formal scoring text.
""", encoding="utf-8", newline="\n")


def append_control_reports(inserted: int, entries: list[dict[str, str]], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    appendix = f"""

## Batch31 Local Application: 2026海淀期中
Updated: 2026-05-25

- Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries after Batch31: `{len(entries)}`.
- Matrix rows added: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch31: `{global_result['remaining_missing']}`.
- Render QA is pending for this batch.
- ClaudeCode Opus 4.7 recheck is pending for this batch; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final; `STRICT_FINAL_ACCEPTED` is not claimed.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch31 Local Application: 2026海淀期中"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")
    qa_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch31 Pending Render QA: 2026海淀期中"
    if marker in qa_text:
        qa_text = qa_text[: qa_text.index(marker)]
    FORMAT_QA.write_text(qa_text + f"""

## Batch31 Pending Render QA: 2026海淀期中
Updated: 2026-05-25

- Status: `RENDER_PENDING_AFTER_DOCX_MODIFICATION`.
- Batch31 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required next check: current DOCX/PDF render, heading styles, page count, labels, and new/old entry consistency.
""", encoding="utf-8", newline="\n")
    ledger = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH31_HAIDIAN_MIDTERM_RECHECK"
    if marker in ledger:
        ledger = ledger[: ledger.index(marker)]
    MODEL_LEDGER.write_text(ledger + """

## CLAUDECODE_BATCH31_HAIDIAN_MIDTERM_RECHECK

status: `real_call_pending`

- Batch: `2026海淀期中`.
- Prompt: `OPUS47_CLAUDECODE_BATCH31_2026_HAIDIAN_MIDTERM_RECHECK_PROMPT.md`.
- Required command shape: `claude -p --model claude-opus-4-7 --effort max --tools Read,Grep --output-format json --verbose`.
- Model gate before real evidence: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output is not qualified ClaudeCode evidence.
""", encoding="utf-8", newline="\n")


def write_batch_report(backup: Path, inserted: int, entries: list[dict[str, str]], ledger_result: dict[str, int | str], matrix_result: dict[str, int | str], global_result: dict[str, int]) -> None:
    BATCH_REPORT.write_text(f"""# Coverage Fusion Batch31 - 2026海淀期中

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch31 edit: `{backup}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `2026海淀期中` after Batch31: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `2026海淀期中`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch31: `{global_result['remaining_missing']}`.

## Placement Verdict

- Q9 enters only as an objective-choice `人民群众` hook based on the teacher answer key `9A`; it is not treated as a subjective scoring rubric.
- Q22(2) enters through page_094 formal scoring support for `发挥主观能动性`, `发展观（前途光明、道路曲折）`, `人类社会发展规律`, and `人民群众主体地位`.
- Q22(1), Q16-Q21, and the non-philosophy Q22(2) module points are boundary-excluded.
- Ordinary teacher reference answer lines for Q22(2) are kept as context only and do not substitute for the formal scoring text.

## Remaining Gates

- Render QA is pending because Batch31 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final; `STRICT_FINAL_ACCEPTED` is not claimed.
""", encoding="utf-8", newline="\n")


def main() -> None:
    for required in [GPT_BUNDLE, RUBRIC_SOURCE, TEACHER_SOURCE, OCR_TEXT, OCR_LINES, MATRIX, LEDGER, ACCEPTED]:
        if not required.exists():
            raise FileNotFoundError(required)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup, inserted = update_docx(timestamp)
    root = load_docx_xml(current_docx())
    entries = extract_entries_from_root(root)
    if len(entries) != EXPECTED_ENTRIES:
        raise RuntimeError(f"Expected {EXPECTED_ENTRIES} governed {SUITE} entries after Batch31, found {len(entries)}")
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
