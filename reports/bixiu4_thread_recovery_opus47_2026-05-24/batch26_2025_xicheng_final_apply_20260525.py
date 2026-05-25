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

SOURCE_TRANSCRIPTION = RECOVERY / "BATCH26_2025_XICHENG_FINAL_SOURCE_TRANSCRIPTION_20260525.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH26_2025_XICHENG_FINAL_CODEX_20260525.md"

PREPROCESSED = ROOT / "data" / "preprocessed_corpus"
GPT_BUNDLE = PREPROCESSED / "gpt_suite_bundles" / "2025各区模拟题__2025各区期末__2025西城期末.md"
RUBRIC_SOURCE = PREPROCESSED / "gpt_sources" / "89d264a31e348be6_2025西城期末细则.md"
TEACHER_SOURCE = PREPROCESSED / "gpt_sources" / "6662da1c2772cc38_2025北京西城高三_上_期末政治_教师版.md"

SUITE = "2025西城期末"
YEAR = "2025"
STAGE = "期末"
BATCH_ID = "batch26_2025_xicheng_final"
MATRIX_SOURCE = "codex_batch26_2025_xicheng_final"
SOURCE_PACKET = (
    f"{GPT_BUNDLE}; {RUBRIC_SOURCE}; {TEACHER_SOURCE}; "
    "current DOCX verified: 10 existing unregistered 2025西城期末 headings were present before Batch26"
)


NEW_ENTRY_SPECS = [
    {
        "canonical_node": "社会存在与社会意识",
        "question_no": "Q1",
        "question_label": "第1题（选择题）",
        "material_trigger": "教师版答案第1题为D，正确项④写“人民广场承载着人们的共同记忆，折射着社会发展和时代变迁”。",
        "question_prompt": "人民广场从上世纪90年代城市中心空间，到脱贫攻坚地区建设热潮，再到当下人民多彩生活舞台和智慧城市实践场，见证城市历史与活力。",
        "why_trigger": "“共同记忆”属于社会意识层面的历史文化记忆，“社会发展和时代变迁”是社会存在的变化。人民广场这一公共空间的变迁折射社会生活的发展。",
        "answer_landing": "本题正确项包含④。人民广场作为公共生活空间，承载不同时期人们的共同记忆，也反映脱贫攻坚、智慧城市和人民生活方式的变化。社会存在的变化会在社会意识、公共记忆和城市文化表达中反映出来。此条只作为客观选择题正确项挂点。",
    },
    {
        "canonical_node": "矛盾的普遍性",
        "question_no": "Q18",
        "question_label": "第18题（主观题）",
        "material_trigger": "细则第114-115行明确写“矛盾具有普遍性，面对新技术带来的问题，应坚持问题导向，敢于直面矛盾，积极寻找正确方法解决矛盾”。",
        "question_prompt": "技术恐惧伴随印刷机、机器生产、核技术、计算机和生成式人工智能等重大技术发展而反复出现，人们担心失业、隐私泄露和安全风险。",
        "why_trigger": "新技术发展不是没有矛盾的直线过程。技术进步会带来效率、创新和便利，也会带来风险、担忧和社会适应问题。题目要求学生承认这些矛盾的普遍存在并寻找解决方法。",
        "answer_landing": "看待技术恐惧，要承认矛盾具有普遍性。面对人工智能等新技术带来的就业、隐私、安全等问题，不能回避矛盾，也不能因为有问题就否定新技术，而要坚持问题导向，直面矛盾、分析矛盾、解决矛盾，在治理完善中促进新技术健康成长。",
    },
    {
        "canonical_node": "价值观的导向作用",
        "question_no": "Q18",
        "question_label": "第18题（主观题）",
        "material_trigger": "细则第116-118行明确写“价值观具有导向作用/正确价值判断和价值选择要符合客观规律，符合人民的根本利益，科技要以人为本”。",
        "question_prompt": "面对生成式人工智能迅速迭代，人们担心失去工作、担心隐私泄露、担心安全，备感恐慌和不安。",
        "why_trigger": "题目要求判断技术发展服务谁、保护谁、如何照顾被技术变革冲击的人群。这不是单纯效率问题，而是科技治理的价值方向问题。",
        "answer_landing": "价值观对人们认识世界和改造世界具有导向作用。看待技术恐惧，既要尊重技术发展规律，也要坚持科技以人为本，把人民利益作为技术治理的重要尺度，关注受技术变革冲击的人群，让人工智能发展服务人的全面发展和社会公共利益。",
    },
    {
        "canonical_node": "改革 / 改革的实质",
        "question_no": "Q21",
        "question_label": "第21题（主观题）",
        "material_trigger": "细则第190-193行要求说明改革与法治的区别，并明确“改革是社会主义制度的自我完善和自我发展/改革是解决社会基本矛盾/社会主义社会发展的直接动力”。",
        "question_prompt": "党的十八大以来，通过改革和法治的相互促动，不断完善各方面制度法规，推动中国特色社会主义制度更加成熟更加定型。",
        "why_trigger": "材料把改革放在制度完善和国家治理现代化进程中理解，细则直接给出改革的必修四历史观表述。",
        "answer_landing": "改革是社会主义制度的自我完善和自我发展，是解决社会主义社会基本矛盾、推动社会主义社会前进的直接动力。坚持改革和法治相统一，就是在法治轨道上推进改革、以改革完善法治，使制度建设更成熟定型、国家治理更有效。",
    },
]


BOUNDARY_ROWS = [
    ("Q5", "逻辑与思维选择题", "充分必要条件/联言选言判断/换位推理", "教师版答案C；攀椰竞速题考查逻辑推理规则，不进入必修四哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q6", "逻辑与思维选择题", "归纳推理/类比推理", "教师版答案A；题目要求比较推理方式，属于选必三逻辑与思维，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q8", "经济与法治选择题", "用水权市场化交易/资源优化配置", "教师版答案C；题目核心是黄河保护法、市场机制和资源配置，不作为必修四哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q9", "经济制度选择题", "土地承包关系/农村基本经营制度", "教师版答案B；农村土地承包政策属于经济制度与改革政策选择题，不单独进入哲学宝典正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q10", "政治与法治选择题", "党的领导/政治局会议/党风廉政建设", "教师版答案A；题目为党的领导与党的建设，不进入当前哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q11", "政治与法治选择题", "政协委员提案/模拟政协", "教师版答案D；政协履职题，不进入必修四哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q12", "法律与生活选择题", "先用后付/合同/消费者权益", "教师版答案B；法律与生活合同和消费者权益题，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q13", "法律与生活选择题", "侵权责任/举证责任/高空抛物", "教师版答案A；侵权责任法律题，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q14", "经济选择题", "出口结构/价值链中高端", "教师版答案B；中国商品出口结构判断，属于经济模块，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q15", "国际政治与经济选择题", "全球减贫/G20/零关税待遇", "教师版答案B；国际合作与全球发展题，不进入哲学正文。", "教师版答案+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q16(1)", "文化主观题", "文物建筑活化利用/传统文化双创/文化产业", "正式细则第32-41行列文化传承、文化认同、双创、文化消费和文化产业点；当前交付件为哲学宝典正文，文化点不强行塞入哲学节点。", "强细则+文档边界", "CULTURE_POINT_BOUNDARY_EXCLUDED_FOR_PHILOSOPHY_BODY"),
    ("Q16(2)", "经济/政治与法治主观题", "市场竞争/政务公开/法治政府", "正式细则第43-49行按平等竞争、市场机制、政务公开和监督权给分，不进入必修四哲学正文。", "强细则+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q17(1)", "经济主观题", "国有经济/资源循环/绿色发展", "正式细则第55-68行按国有经济、所有制、资源环境角度给分，不进入哲学正文。", "强细则+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q17(2)", "逻辑与思维主观题", "三段论基本规则", "正式细则第70-77行明确按三段论基本规则给分，属于选必三逻辑与思维。", "强细则+题面模块限定", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q19", "法律与生活主观题", "反不正当竞争/混淆/虚假宣传", "正式细则第129-142行按反不正当竞争法、诚实信用、营商环境给分，不进入哲学正文。", "强细则+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q20", "国际政治与经济主观题", "全球汽车产业链/国际规则/出口市场多元化", "正式细则第143-166行按国际规则维权、竞争优势、市场多元化和走出去给分，不进入哲学正文。", "强细则+题面模块判断", "MODULE_BOUNDARY_EXCLUDED_BATCH26_XICHENG_FINAL"),
    ("Q21-nonphilosophy", "综合主观题中的法治/党领导点", "法治保障/党的领导/法定程序", "正式细则第168-205行包含法治和党领导维度；仅登记其中明确的改革历史观落点，其余法治政治点作为模块边界。", "强细则+文档边界", "NONPHILOSOPHY_COMPREHENSIVE_POINT_BOUNDARY_EXCLUDED"),
]


EVIDENCE_BY_KEY = {
    ("Q1", "社会存在与社会意识"): ("教师版答案第1题D；正确项④支持公共记忆折射社会发展和时代变迁", "objective-choice-only"),
    ("Q2", "实践是认识的基础"): ("教师版答案第2题B；正确项④支持亲身实践改造主观世界、弘扬伟大建党精神", "objective-choice-only"),
    ("Q3", "实践与认识（总）"): ("教师版答案第3题C；正确项③支持亲眼所见、亲身所历有利于了解真实中国", "objective-choice-only"),
    ("Q4", "发展的观点 / 发展的普遍性"): ("教师版答案第4题D；正确项③支持着眼长远、从更长时限思考问题", "objective-choice-only"),
    ("Q7", "矛盾就是对立统一"): ("教师版答案第7题B；正确项④支持处理快与慢、同与异的辩证关系", "objective-choice-only"),
    ("Q18", "发展的观点 / 发展的普遍性"): ("正式细则第80-118行明列“新事物的特点”：新事物从小到大、从不完善到完善", "formal-rubric"),
    ("Q18", "事物发展是前进性与曲折性的统一"): ("正式细则第106-108行支持新事物发展过程和技术恐惧的两面性；按新事物成长曲折性登记", "formal-rubric-with-node-caution"),
    ("Q18", "矛盾就是对立统一"): ("正式细则第111-113行明列“矛盾就是对立统一，要一分为二辩证看问题”", "formal-rubric"),
    ("Q18", "矛盾的普遍性"): ("正式细则第114-115行明列“矛盾具有普遍性”，要直面矛盾、解决矛盾", "formal-rubric"),
    ("Q18", "认识发展原理"): ("正式细则第109-110行明列认识受实践水平、立场观点方法、知识水平、思维能力等条件限制", "formal-rubric"),
    ("Q18", "价值观的导向作用"): ("正式细则第116-118行明列“价值观具有导向作用”，科技要以人为本", "formal-rubric"),
    ("Q18", "价值判断与价值选择"): ("正式细则第116-118行明列正确价值判断和价值选择要符合客观规律、符合人民根本利益", "formal-rubric"),
    ("Q21", "社会发展的两大基本规律和基本矛盾"): ("正式细则第190-193行明列改革是解决社会基本矛盾、社会主义社会发展的直接动力", "formal-rubric"),
    ("Q21", "改革 / 改革的实质"): ("正式细则第190-193行明列改革是社会主义制度的自我完善和自我发展", "formal-rubric"),
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
    backup = docx.with_name(f"{docx.stem}_backup_before_batch26_2025_xicheng_final_{timestamp}{docx.suffix}")
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
            clone_with_text(body_template, f"【材料触发点】 {spec['material_trigger']}"),
            clone_with_text(body_template, f"【设问】 {spec['question_prompt']}"),
            clone_with_text(body_template, f"【为什么能想到】 {spec['why_trigger']}"),
            clone_with_text(body_template, f"【答案落点】 {spec['answer_landing']}"),
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
    backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_batch26_2025_xicheng_final_{timestamp}{LEDGER.suffix}")
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
    backup_accepted = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_batch26_2025_xicheng_final_{timestamp}{ACCEPTED.suffix}")
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
                "source_lane": "Codex Batch26 Xicheng final registration and insertion",
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


def update_matrix(entries: list[dict[str, str]], timestamp: str) -> dict[str, int | str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_batch26_2025_xicheng_final_{timestamp}{MATRIX.suffix}")
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
        is_caution = boundary == "formal-rubric-with-node-caution"
        new_rows.append(
            {
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
                "证据等级": "教师版客观题答案" if is_objective else ("强细则/节点解释延展" if is_caution else "强细则"),
                "是否误放": "否：保留但按新事物成长曲折性理解" if is_caution else "否",
                "是否需补厚": "否",
                "当前处理": "KEEP_IN_BODY_OBJECTIVE_ONLY" if is_objective else "KEEP_IN_BODY",
                "备注": "Batch26登记既有正文并补入正式细则明确落点；客观题仅作客观答案挂点，普通参考答案未冒充主观评分细则。",
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
            row["current_status"] = "covered_by_batch26_recovery_matrix"
            row["blocker_or_next_action"] = "Batch26 registered existing DOCX entries, inserted formal-rubric/objective-choice points, and added boundary rows; render/model gates pending."
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

## Batch26 Finding

`{SUITE}` is now covered by question-level recovery matrix rows. Existing DOCX headings were present but unregistered before Batch26. Batch26 registered those existing entries, inserted four missing rubric/objective-supported philosophy points, and boundary-excluded law, logic, economy, culture-only, international-politics, and non-philosophy comprehensive points.

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
        f"""# Batch26 Source Transcription - 2025西城期末

Status: `SOURCE_REVIEWED_BATCH26`

## Source Files

- suite bundle: `{GPT_BUNDLE}`
- formal scoring/rubric cache: `{RUBRIC_SOURCE}`
- teacher-version paper cache: `{TEACHER_SOURCE}`
- raw rubric: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025西城期末\\细则\\2025西城期末细则.pdf`
- raw teacher paper: `C:\\Users\\Administrator\\Desktop\\2025各区模拟题\\2025各区期末\\2025西城期末\\试卷\\2025北京西城高三（上）期末政治（教师版）.pdf`

## Source Facts

- Teacher/formal answer key: `1D 2B 3C 4D 5C 6A 7B 8C 9B 10A 11D 12B 13A 14B 15B`.
- Q1 objective answer D supports a social-existence/social-consciousness objective-only row through correct item ④.
- Q2, Q3, Q4, and Q7 are objective-choice philosophy rows only; they are not treated as subjective scoring rubrics.
- Q16(1) is culture-only for current philosophy body; Q16(2), Q17(1), Q19, Q20, and part of Q21 are non-philosophy boundaries.
- Q17(2) is Logic and Thinking because the formal scoring source uses syllogism rules.
- Q18 formal scoring source supports new-things/development, cognition limitations, contradiction/opposition-unity, contradiction universality, value guidance, and value judgment/value choice.
- Q21 formal scoring source supports the reform/social-basic-contradiction history-view point;法治 and party-leadership dimensions remain boundary rows.

## Governed DOCX Entries After Batch26

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
        f"""# Coverage Fusion Batch26 - 2025西城期末

Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`

## Execution Summary

- DOCX backup before Batch26 edit: `{backup}`.
- Existing unregistered DOCX entries recovered: `{len(entries) - inserted}`.
- New DOCX entries inserted: `{inserted}`.
- Governed DOCX entries for `{SUITE}` after Batch26: `{len(entries)}`.
- Ledger rows added: `{ledger_result['ledger_added']}`.
- Accepted JSONL records added: `{ledger_result['accepted_added']}`.
- Matrix rows added for `{SUITE}`: `{matrix_result['batch_rows']}` total, `{matrix_result['body_rows']}` body rows, `{matrix_result['boundary_rows']}` boundary rows.
- Global raw-suite remaining gap after Batch26: `{global_result['missing']}`.

## Placement Verdict

- `2025西城期末` was absent from the recovery matrix while 10 DOCX headings already existed; Batch26 repaired that ledger/matrix gap.
- Four new DOCX entries were inserted: Q1 social-existence/social-consciousness objective row, Q18 contradiction universality, Q18 value-guidance, and Q21 reform essence.
- Q5/Q6/Q8-Q17/Q19/Q20 and the non-philosophy parts of Q21 are boundary-excluded by formal source or module judgment.

## Remaining Gates

- Render QA is pending because Batch26 modified the DOCX.
- ClaudeCode Opus 4.7 recheck is pending.
- Model-effort/adaptive proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.
""",
        encoding="utf-8",
    )

    format_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch26 Render/Format QA: 2025西城期末"
    if marker in format_text:
        format_text = format_text[: format_text.index(marker)]
    FORMAT_QA.write_text(
        format_text
        + f"""

## Batch26 Render/Format QA: 2025西城期末
Updated: 2026-05-25

- Render status: `render_pending`.
- Reason: Batch26 inserted `{inserted}` DOCX entries and registered `{len(entries)}` governed headings.
- Required check: render current DOCX/PDF and verify fonts, heading styles, page count, labels, and new/old entry consistency.
""",
        encoding="utf-8",
    )

    append_block = f"""

## Batch26 Local Application: 2025西城期末
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
        marker = "\n## Batch26 Local Application: 2025西城期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + append_block, encoding="utf-8")

    model_text = MODEL_LEDGER.read_text(encoding="utf-8")
    marker = "\n## CLAUDECODE_BATCH26_XICHENG_FINAL_RECHECK"
    if marker in model_text:
        model_text = model_text[: model_text.index(marker)]
    MODEL_LEDGER.write_text(
        model_text
        + """

## CLAUDECODE_BATCH26_XICHENG_FINAL_RECHECK

status: `real_call_pending`

- No ClaudeCode Opus 4.7 max/adaptive recheck has been completed for Batch26 yet.
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
    if len(entries) != 14:
        raise RuntimeError(f"Expected 14 {SUITE} governed entries after Batch26, found {len(entries)}")
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
