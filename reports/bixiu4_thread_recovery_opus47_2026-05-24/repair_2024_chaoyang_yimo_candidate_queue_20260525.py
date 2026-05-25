from __future__ import annotations

import csv
import json
import shutil
import tempfile
import zipfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
W = f"{{{W_NS}}}"
XML = f"{{{XML_NS}}}"
NS = {"w": W_NS}

RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
LEDGER = DELIVERY / "docx_insert_ledger.csv"
REPORT_MD = RECOVERY / "CHAOYANG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "CHAOYANG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"

SUITE = "2024朝阳一模"
YEAR = "2024"
STAGE = "一模"
ROW_SOURCE = "codex_recovery_20260525_chaoyang_2024_yimo_repair"
BUNDLE = "data\\preprocessed_corpus\\gpt_suite_bundles\\2024各区模拟题__2024各区一模__2024朝阳一模.md"

LABELS = [
    ("【材料触发点】", "material_trigger"),
    ("【设问】", "question_prompt"),
    ("【为什么能想到】", "why_trigger"),
    ("【答案落点】", "answer_landing"),
]

ENTRIES = [
    {
        "canonical_node": "人民群众",
        "question_no": "Q5",
        "heading_suffix": "2024朝阳一模 第5题（选择题）",
        "material_trigger": "北京艺术中心、北京城市图书馆、北京大运河博物馆三大文化建筑向公众开放；参考答案键为A，正确项①指向传承北京历史文脉、落实首都战略定位，正确项③指向让文化发展成果更好惠及人民、满足大众精神文化需求。",
        "question_prompt": "京津冀协同发展十周年背景下，三大文化建筑对公众开放；参考答案键为A（①③）。",
        "why_trigger": "看到“向公众开放”“文化发展成果惠及人民”“满足大众精神文化需求”，应从人民群众与文化发展的关系切入：文化建设不能只停留在建筑景观本身，而要落到人民共享文化成果、满足人民精神文化生活需要。",
        "answer_landing": "本题应选A。本节点只处理③：三大文化建筑开放，把首都文化资源转化为人民可进入、可体验、可共享的公共文化服务，体现文化发展必须坚持以人民为中心，让文化发展成果惠及人民、满足人民精神文化需求；①的历史文脉传承作为文化线索保留，不扩展为主观题评分链。",
        "evidence_level": "答案键+题干正确项链（选择题，非主观题评分细则）",
    },
    {
        "canonical_node": "系统观念 / 系统优化",
        "question_no": "Q9",
        "heading_suffix": "2024朝阳一模 第9题（选择题）",
        "material_trigger": "几名中学生从模拟提案到政协委员正式提案，经历务实调查、充实内容、完善提案等环节；参考答案键为D，正确项③写明需要坚持系统观念，有序完成调查研究和思考任务。",
        "question_prompt": "从“模拟提案”到“正式提案”的探索；参考答案键为D（③④）。",
        "why_trigger": "模拟提案不是单点表达意见，而是围绕小区车位问题开展调查、论证、完善、提交的连续过程。看到“务实调查、充实内容、完善提案”，应想到系统观念：把问题、主体、材料、程序和制度理解为一个有序联动的整体。",
        "answer_landing": "本题应选D。本节点只处理③：从模拟提案到正式提案，需要坚持系统观念，有序完成调查研究和思考任务，把问题发现、利益关系、调查材料、提案完善和制度渠道衔接起来；④的制度认同作为政治线索保留，不扩展为主观题评分链。",
        "evidence_level": "答案键+题干正确项链（选择题，非主观题评分细则）",
    },
]


def source(lines: str) -> str:
    return f"{BUNDLE}:{lines}"


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def p_style(p) -> str:
    node = p.find("./w:pPr/w:pStyle", namespaces=NS)
    return node.get(W + "val") if node is not None else ""


def is_section(p) -> bool:
    return p_style(p) in {"Heading2", "2", "4"}


def is_entry(p) -> bool:
    return p_style(p) in {"Heading3", "3", "5"}


def make_run(text: str, label: bool = False):
    r = etree.Element(W + "r")
    if label:
        rpr = etree.SubElement(r, W + "rPr")
        etree.SubElement(rpr, W + "b")
        color = etree.SubElement(rpr, W + "color")
        color.set(W + "val", "21574C")
    t = etree.SubElement(r, W + "t")
    if text.startswith(" ") or text.endswith(" "):
        t.set(XML + "space", "preserve")
    t.text = text
    return r


def set_plain(p, text: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(text))


def set_label(p, label: str, rest: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(label, True))
    p.append(make_run(" " + rest))
    ppr = p.find("./w:pPr", namespaces=NS)
    if ppr is None:
        ppr = etree.Element(W + "pPr")
        p.insert(0, ppr)
    spacing = ppr.find("./w:spacing", namespaces=NS)
    if spacing is None:
        spacing = etree.SubElement(ppr, W + "spacing")
    spacing.set(W + "after", "80")


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def find_section(paras, heading: str) -> tuple[int, int]:
    start = next((i for i, p in enumerate(paras) if is_section(p) and para_text(p).strip() == heading), None)
    if start is None:
        raise RuntimeError(f"section not found: {heading}")
    end = next((i for i in range(start + 1, len(paras)) if is_section(paras[i])), len(paras))
    return start, end


def add_entry(body, entry: dict[str, str]) -> str | None:
    if any(entry["heading_suffix"] in para_text(p) for p in body if p.tag == W + "p"):
        return None
    paras = [p for p in body if p.tag == W + "p"]
    start, end = find_section(paras, entry["canonical_node"])
    h_template = next(p for p in paras[start + 1 : end] if is_entry(p))
    l_template = next(p for p in paras[start + 1 : end] if para_text(p).strip().startswith("【"))
    blank = next((p for p in paras[start + 1 : end] if not para_text(p).strip()), None)
    nums = []
    for p in paras[start + 1 : end]:
        if is_entry(p):
            head = para_text(p).strip().split(".", 1)[0]
            if head.isdigit():
                nums.append(int(head))
    heading_text = f"{(max(nums) if nums else 0) + 1}. {entry['heading_suffix']}"
    insert_at = list(body).index(paras[end]) if end < len(paras) else len(body)
    h = deepcopy(h_template)
    set_plain(h, heading_text)
    body.insert(insert_at, h)
    insert_at += 1
    for label, key in LABELS:
        p = deepcopy(l_template)
        set_label(p, label, entry[key])
        body.insert(insert_at, p)
        insert_at += 1
    if blank is not None:
        body.insert(insert_at, deepcopy(blank))
    return heading_text


def edit_docx(ts: str) -> dict[str, object]:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2024_chaoyang_yimo_insert_{ts}.docx")
    shutil.copy2(docx, backup)
    inserted: list[str] = []
    skipped: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        with zipfile.ZipFile(docx) as zin:
            zin.extractall(temp)
        xml_path = temp / "word" / "document.xml"
        tree = etree.parse(str(xml_path))
        body = tree.getroot().find("w:body", namespaces=NS)
        if body is None:
            raise RuntimeError("missing body")
        for entry in ENTRIES:
            heading = add_entry(body, entry)
            if heading is None:
                skipped.append(entry["heading_suffix"])
            else:
                inserted.append(heading)
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return {"docx": str(docx), "docx_backup": str(backup), "inserted_headings": inserted, "skipped_existing": skipped}


def update_ledger(ts: str, headings: list[str]) -> dict[str, object]:
    backup = None
    rows = []
    fieldnames = ["canonical_node", "source_suite", "question_no", "inserted_heading"]
    if LEDGER.exists():
        backup = LEDGER.with_name(f"{LEDGER.stem}_backup_before_2024_chaoyang_yimo_insert_{ts}{LEDGER.suffix}")
        shutil.copy2(LEDGER, backup)
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or fieldnames
            rows = list(reader)
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    for entry, heading in zip(ENTRIES, headings, strict=False):
        clean = heading.split(". ", 1)[1]
        key = (SUITE, entry["question_no"], clean)
        if key in existing:
            continue
        rows.append({"canonical_node": entry["canonical_node"], "source_suite": SUITE, "question_no": entry["question_no"], "inserted_heading": clean})
        added.append(clean)
    with LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"ledger_backup": str(backup) if backup else None, "ledger_rows_added": added}


def next_matrix_id(rows: list[dict[str, str]]) -> int:
    nums = []
    for row in rows:
        rid = row.get("matrix_row_id", "")
        if rid.startswith("M") and rid[1:].isdigit():
            nums.append(int(rid[1:]))
    return max(nums, default=0) + 1


def new_row(fieldnames: list[str], mid: int, question: str, qtype: str, in_book: str, node: str, support: str,
            evidence: str, current: str, artifact: str) -> dict[str, str]:
    row = {name: "" for name in fieldnames}
    row.update({
        "matrix_row_id": f"M{mid:04d}",
        "row_source": ROW_SOURCE,
        "题源": SUITE,
        "年份": YEAR,
        "阶段": STAGE,
        "题号": question,
        "题型或模块判断": qtype,
        "是否进宝典": in_book,
        "宝典节点": node,
        "细则支持原理": support,
        "证据等级": evidence,
        "是否误放": "否",
        "是否需补厚": "否",
        "当前处理": current,
        "备注": "逐题覆盖补齐。",
        "source_artifact": artifact,
    })
    return row


def update_matrix(ts: str) -> dict[str, object]:
    backup = MATRIX.with_name(f"{MATRIX.stem}_backup_before_2024_chaoyang_yimo_repair_{ts}{MATRIX.suffix}")
    shutil.copy2(MATRIX, backup)
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    by_id = {r.get("matrix_row_id", ""): r for r in rows}
    updated: list[str] = []
    yes_body = "是：已进入当前DOCX/PDF正文"
    no_body = "否：不进入当前哲学宝典正文"
    choice_evidence = "答案键+题干正确项链（选择题，非主观题评分细则）"

    updates = {
        "M0271": (no_body, "不进入当前哲学宝典正文", "模块边界/参考答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "Q1答案B，属于中国特色社会主义道路与文化根基的中特边界。", source("944-950;420-455")),
        "M0272": (no_body, "不进入当前哲学宝典正文", "模块边界/参考答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "Q2答案C，生成式人工智能和新质生产力，属于经济/科技发展边界。", source("951-959;420-455")),
        "M0273": (yes_body, "实现人生价值", choice_evidence, "KEEP_IN_BODY_VERIFIED", "Q3答案B，当前DOCX已保留人生价值选择题链。", source("28-34;420-455")),
        "M0274": (yes_body, "根据固有联系建立新的具体联系", choice_evidence, "KEEP_IN_BODY_VERIFIED", "Q4答案A，当前DOCX已保留根据固有联系建立新联系的选择题链。", source("35-40;553-560")),
        "M0275": (yes_body, "人民群众", choice_evidence, "KEEP_IN_BODY_INSERTED_20260525", "Q5答案A，本轮新增人民共享文化成果选择题链，只处理正确项③。", source("979-989;420-455")),
        "M0276": (no_body, "不进入当前哲学宝典正文", "模块边界/参考答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "Q6答案B，逻辑规则题，属于选必三逻辑与思维边界。", source("45-50;563-568")),
        "M0277": (no_body, "不进入当前哲学宝典正文", "模块边界/参考答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "Q8答案D，政府服务与人民中心思想，政治法治边界。", source("570-576")),
        "M0278": (yes_body, "系统观念 / 系统优化", choice_evidence, "KEEP_IN_BODY_INSERTED_20260525", "Q9答案D，本轮新增系统观念选择题链，只处理正确项③。", source("577-583")),
        "M0279": (no_body, "不进入当前哲学宝典正文", "模块边界/参考答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "Q14答案A，制度型开放属于当代国际政治经济/经济开放边界。", source("615-621")),
        "M0280": (no_body, "不进入当前哲学宝典正文", "模块边界/参考答案键", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "Q15答案C，新时代中国特色大国外交属于当代国际政治经济边界。", source("623-629")),
        "M0281": (yes_body, "内因与外因", "强细则", "KEEP_IN_BODY_VERIFIED", "Q16当前DOCX已保留内因外因/对立统一关系条目；讲评PPT有评分细则支持。", source("144-191;662-678")),
        "M0282": (yes_body, "系统观念 / 系统优化；矛盾就是对立统一", "强细则", "KEEP_IN_BODY_VERIFIED", "Q18(2)当前DOCX已保留系统优化和矛盾对立统一条目；参考答案和细则明确系统优化、两点论重点论等。", source("210-239;487-497")),
        "M0283": (no_body, "不进入当前哲学宝典正文", "模块边界/参考答案", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "Q19为法律与生活诚信原则题；不进入当前哲学宝典正文。", source("499-502;1128-1144")),
        "M0284": (no_body, "不进入当前哲学宝典正文", "模块边界/参考答案", "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", "Q21为经济形势和推动中国经济开新局，属于选必一/经济边界。", source("513-525;1159-1161")),
        "M0285": ("候选已核：逐题矩阵承接", "SUPERSEDED_BY_ROW_LEVEL_MATRIX", "套卷抽取残留", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", "抽取残留行，不是独立题号；逐题覆盖已承接。", source("944-1161")),
        "M0199": ("候选已核：逐题矩阵承接", "SUPERSEDED_BY_ROW_LEVEL_MATRIX", "套卷候选承接", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", "旧待回源占位已由2026-05-25逐题回源承接。", source("407-525")),
        "M0815": ("套卷级行已被逐题矩阵承接", "SUPERSEDED_BY_ROW_LEVEL_MATRIX", "套卷级承接", "SUPERSEDED_BY_ROW_LEVEL_REPAIR", "套卷级覆盖口径已由2026-05-25逐题矩阵修复承接。", source("1-1161")),
    }
    for rid, (in_book, node, evidence, current, support, artifact) in updates.items():
        row = by_id.get(rid)
        if not row:
            continue
        row["是否进宝典"] = in_book
        row["宝典节点"] = node
        row["证据等级"] = evidence
        row["当前处理"] = current
        row["细则支持原理"] = support
        row["是否误放"] = "否"
        row["是否需补厚"] = "否"
        row["备注"] = "2026-05-25回源闭合。"
        row["source_artifact"] = artifact
        if in_book.startswith("是"):
            row["题型或模块判断"] = "选择题正确项链" if "选择题" in evidence else "必修四哲学主观题正文条目"
        elif rid in {"M0285", "M0199", "M0815"}:
            row["题型或模块判断"] = "候选/套卷口径已由逐题矩阵承接"
        else:
            row["题型或模块判断"] = "模块边界排除"
        updated.append(rid)

    mid = next_matrix_id(rows)
    additions = [
        ("Q7", "选必三逻辑与思维选择题边界", no_body, "不进入当前哲学宝典正文", "Q7为创新思维、迁移/想象/逆向/发散聚合超前思维，属选必三边界。", "模块边界/题干边界", source("995-1001")),
        ("Q10", "法律与生活选择题边界", no_body, "不进入当前哲学宝典正文", "Q10为健康权、安全保障义务和侵权责任，属法律与生活边界。", "模块边界/题干边界", source("1021-1032")),
        ("Q11", "法律与生活选择题边界", no_body, "不进入当前哲学宝典正文", "Q11为所有权归属争议，属法律与生活边界。", "模块边界/题干边界", source("71-77;1033-1039")),
        ("Q12", "法律与生活选择题边界", no_body, "不进入当前哲学宝典正文", "Q12为专利保护期和授权使用，属法律与生活边界。", "模块边界/题干边界", source("90-95;1042-1047")),
        ("Q13", "经济与社会选择题边界", no_body, "不进入当前哲学宝典正文", "Q13为超长期特别国债和国民经济影响路径，属经济与社会边界。", "模块边界/题干边界", source("1048-1057")),
        ("Q17", "经济与社会主观题边界", no_body, "不进入当前哲学宝典正文", "Q17为银发经济、政府与企业主体、宏观调控和市场监管，属经济与社会边界。", "参考答案/模块边界", source("473-485;193-209")),
        ("Q20", "选必三逻辑与思维主观题边界", no_body, "不进入当前哲学宝典正文", "Q20为充分条件假言推理和必要条件推理补全，属选必三逻辑与思维边界。", "正式细则-模块边界", source("320-338;1145-1155")),
    ]
    existing = {(r.get("题源"), r.get("题号"), r.get("宝典节点"), r.get("当前处理")) for r in rows}
    added: list[str] = []
    for q, qtype, in_book, node, support, evidence, artifact in additions:
        key = (SUITE, q, node, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED")
        if key in existing:
            continue
        row = new_row(fieldnames, mid, q, qtype, in_book, node, support, evidence, "MODULE_BOUNDARY_EXCLUDED_SOURCE_REVIEWED", artifact)
        rows.append(row)
        added.append(row["matrix_row_id"])
        mid += 1

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return {"matrix_backup": str(backup), "updated_rows": updated, "added_rows": added}


def write_report(ts: str, docx_info: dict[str, object], ledger_info: dict[str, object], matrix_info: dict[str, object]) -> dict[str, object]:
    summary = {
        "status": "CHAOYANG_2024_YIMO_REPAIRED_DOCX_Q5_Q9_INSERTED_RENDER_PENDING",
        "timestamp": ts,
        **docx_info,
        **ledger_info,
        **matrix_info,
        "model_gates": {
            "gptpro_web": "real_call_pending",
            "claude_opus_web_app": "real_call_pending_direct_claude_ai",
            "claudecode_model_confirmation": "BLOCKED_MODEL_CONFIRMATION_REQUIRED",
        },
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# CHAOYANG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525",
        "",
        "Status: `CHAOYANG_2024_YIMO_REPAIRED_DOCX_Q5_Q9_INSERTED_RENDER_PENDING_MODEL_GATES_OPEN`",
        "",
        f"- Timestamp: `{ts}`.",
        "- Corrective action: inserted Q5 choice chain under `人民群众`.",
        "- Corrective action: inserted Q9 choice chain under `系统观念 / 系统优化`.",
        "- Existing current-DOCX coverage for Q3/Q4/Q16/Q18 was verified and reflected in the matrix.",
        "- Remaining non-book questions were closed as module-boundary rows or source-reviewed no-DOCX-action rows.",
        f"- DOCX backup: `{Path(str(docx_info['docx_backup'])).name}`.",
        f"- Matrix backup: `{Path(str(matrix_info['matrix_backup'])).name}`.",
        f"- Ledger backup: `{Path(str(ledger_info['ledger_backup'])).name if ledger_info.get('ledger_backup') else 'NONE'}`.",
        f"- Matrix rows updated: `{len(matrix_info['updated_rows'])}`.",
        f"- Matrix rows added: `{len(matrix_info['added_rows'])}`.",
        "",
        "## Inserted Headings",
        "",
    ]
    for heading in docx_info["inserted_headings"]:
        lines.append(f"- `{heading}`")
    lines.extend([
        "",
        "## Open Gates",
        "",
        "- Render QA is required because the DOCX changed.",
        "- GPTPro web full artifact review remains `real_call_pending`.",
        "- Claude Opus web/app full artifact review remains `real_call_pending`; corrected route is direct `https://claude.ai` auto-login.",
        "- ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.",
    ])
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx_info = edit_docx(ts)
    ledger_info = update_ledger(ts, docx_info["inserted_headings"])
    matrix_info = update_matrix(ts)
    summary = write_report(ts, docx_info, ledger_info, matrix_info)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
