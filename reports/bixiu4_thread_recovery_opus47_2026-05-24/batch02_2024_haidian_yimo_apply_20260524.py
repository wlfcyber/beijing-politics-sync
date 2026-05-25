from __future__ import annotations

import csv
import re
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree


RUN_DIR = "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DOCX_BASENAME = "哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def paragraph_text(p: etree._Element, ns: dict[str, str]) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=ns))


def set_paragraph_text(p: etree._Element, text: str, ns: dict[str, str]) -> None:
    text_nodes = p.xpath(".//w:t", namespaces=ns)
    if not text_nodes:
        raise RuntimeError("paragraph has no text nodes")
    text_nodes[0].text = text
    for node in text_nodes[1:]:
        node.text = ""


def remove_misplaced_q17_2(docx_path: Path, timestamp: str) -> dict[str, object]:
    backup = docx_path.with_name(
        f"{docx_path.stem}_backup_before_2024_haidian_q17_2_removal_{timestamp}.docx"
    )
    shutil.copy2(docx_path, backup)

    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(docx_path, "r") as zin:
        document_xml = zin.read("word/document.xml")
        entries = {info.filename: zin.read(info.filename) for info in zin.infolist()}
        infos = zin.infolist()

    root = etree.fromstring(document_xml)
    body = root.find("w:body", namespaces=ns)
    if body is None:
        raise RuntimeError("word/document.xml has no w:body")

    children = list(body)
    paragraphs = [child for child in children if child.tag == f"{{{ns['w']}}}p"]
    start = None
    for idx, p in enumerate(paragraphs):
        if paragraph_text(p, ns).strip() == "1. 2024海淀一模 第17题第（2）问（主观题）":
            start = idx
            break
    if start is None:
        raise RuntimeError("target 2024海淀一模 第17题第（2）问 not found")

    next_item = None
    for idx in range(start + 1, len(paragraphs)):
        txt = paragraph_text(paragraphs[idx], ns).strip()
        if re.match(r"^\d+\.\s", txt):
            next_item = idx
            break
    if next_item is None:
        raise RuntimeError("could not locate next numbered item after target")

    removed_text = [paragraph_text(p, ns).strip() for p in paragraphs[start:next_item]]
    for p in paragraphs[start:next_item]:
        body.remove(p)

    children_after = list(body)
    paragraphs_after = [child for child in children_after if child.tag == f"{{{ns['w']}}}p"]

    section_start = None
    for idx, p in enumerate(paragraphs_after):
        if paragraph_text(p, ns).strip() == "系统观念 / 系统优化":
            section_start = idx
            break
    if section_start is None:
        raise RuntimeError("section heading 系统观念 / 系统优化 not found after removal")

    section_end = None
    for idx in range(section_start + 1, len(paragraphs_after)):
        if paragraph_text(paragraphs_after[idx], ns).strip() == "发展的观点 / 发展的普遍性":
            section_end = idx
            break
    if section_end is None:
        raise RuntimeError("next section heading 发展的观点 / 发展的普遍性 not found")

    renumbered: list[tuple[str, str]] = []
    new_number = 1
    for p in paragraphs_after[section_start + 1 : section_end]:
        old = paragraph_text(p, ns).strip()
        if not re.match(r"^\d+\.\s", old):
            continue
        new = re.sub(r"^\d+\.", f"{new_number}.", old, count=1)
        if old != new:
            set_paragraph_text(p, new, ns)
            renumbered.append((old, new))
        new_number += 1

    entries["word/document.xml"] = etree.tostring(
        root,
        xml_declaration=True,
        encoding="UTF-8",
        standalone="yes",
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)

    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for info in infos:
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.comment = info.comment
            zi.extra = info.extra
            zi.internal_attr = info.internal_attr
            zi.external_attr = info.external_attr
            zi.create_system = info.create_system
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, entries[info.filename])

    shutil.move(str(tmp_path), docx_path)
    return {
        "backup": str(backup),
        "removed_paragraphs": removed_text,
        "renumbered_count": len(renumbered),
        "renumbered_preview": renumbered[:5],
    }


def update_matrix(matrix_path: Path, timestamp: str) -> dict[str, object]:
    backup = matrix_path.with_name(
        f"FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_batch02_2024_haidian_{timestamp}.csv"
    )
    shutil.copy2(matrix_path, backup)

    col_in_book = "\u662f\u5426\u8fdb\u5b9d\u5178"
    col_node = "\u5b9d\u5178\u8282\u70b9"
    col_principle = "\u7ec6\u5219\u652f\u6301\u539f\u7406"
    col_evidence = "\u8bc1\u636e\u7b49\u7ea7"
    col_misplaced = "\u662f\u5426\u8bef\u653e"
    col_need = "\u662f\u5426\u9700\u8865\u539a"
    col_current = "\u5f53\u524d\u5904\u7406"
    col_note = "\u5907\u6ce8"

    q16_principle = (
        "2024海淀一模 source bundle lines 23-24 / 63: "
        "Q16可从发挥主观能动性、联系的观点、发展的观点、实践的观点、民族精神等角度作答。"
    )

    decisions: dict[str, dict[str, str]] = {
        "M0142": {
            col_in_book: "是：已在最终DOCX覆盖（无需新增）",
            col_node: "主观能动性/联系/发展/实践",
            col_principle: q16_principle,
            col_evidence: "强细则",
            col_misplaced: "否",
            col_need: "否",
            col_current: "Batch02回源闭合：保留现有Q16多节点条目。",
            col_note: "final DOCX已有Q16多处；民族精神角度不作为当前哲学节点新增。",
        },
        "M0194": {
            col_in_book: "是：已在最终DOCX覆盖（无需新增）",
            col_node: "主观能动性/联系/发展/实践",
            col_principle: q16_principle,
            col_evidence: "强细则",
            col_misplaced: "否",
            col_need: "否",
            col_current: "Batch02回源闭合：将原参考答案等级提升为细则支持的已覆盖。",
            col_note: "ClaudeCode B旧行只作候选；本次以source bundle细则行闭合。",
        },
        "M0286": {
            col_in_book: "否：不入当前哲学宝典（文化/民族精神另线候选）",
            col_node: "文化线：长征精神/民族精神（非本哲学节点）",
            col_principle: "source bundle lines 159-169为Q1选择题；Codex A此行的主要矛盾等命中来自错切片段，不能作为Q1哲学证据。",
            col_evidence: "题号误切/需文化线另审",
            col_misplaced: "否：候选误触发，正文未新增",
            col_need: "否：当前哲学宝典不补；若扩展文化宝典需另审",
            col_current: "Batch02排除当前哲学宝典；保留文化线提示。",
            col_note: "不得用Q17(2)分析综合细则倒贴到Q1。",
        },
        "M0287": {
            col_in_book: "是：已在最终DOCX覆盖（无需新增）",
            col_node: "主观能动性/固有联系",
            col_principle: "source bundle lines 170-177为Q2题干与选项，answer key line 18给出Q2=A。",
            col_evidence: "选择题官方答案键+题干",
            col_misplaced: "否",
            col_need: "否",
            col_current: "Batch02回源闭合：Q2已在最终DOCX覆盖。",
            col_note: "原行混入Q17(3)等片段的风险已剔除，只按Q2原题裁决。",
        },
        "M0288": {
            col_in_book: "是：已在最终DOCX覆盖（无需新增）",
            col_node: "实践检验真理/认识过程",
            col_principle: "source bundle lines 178-185为Q3题干与选项，answer key line 18给出Q3=C。",
            col_evidence: "选择题官方答案键+题干",
            col_misplaced: "否",
            col_need: "否",
            col_current: "Batch02回源闭合：Q3已在最终DOCX覆盖。",
            col_note: "原rubric_term_hit混入Q20活动题词，不能作为Q3依据。",
        },
        "M0289": {
            col_in_book: "否：不入当前哲学宝典（文化审美线另列）",
            col_node: "文化线：中华优秀传统文化/审美意识",
            col_principle: "source bundle lines 196-229为服饰纹样文化选择题，answer key line 18给出Q4=D；不是当前哲学原理节点。",
            col_evidence: "选择题官方答案键+模块边界",
            col_misplaced: "否：候选未入正文",
            col_need: "否：当前哲学宝典不补；若扩展文化宝典需另审",
            col_current: "Batch02模块边界排除当前哲学宝典。",
            col_note: "可作为文化专题候选，不用意识一词误放到哲学节点。",
        },
        "M0290": {
            col_in_book: "是：已在最终DOCX覆盖（无需新增）",
            col_node: "矛盾双方对立统一/矛盾普遍性与特殊性",
            col_principle: "source bundle lines 230-240为Q5围棋选择题，answer key line 18给出Q5=C。",
            col_evidence: "选择题官方答案键+题干",
            col_misplaced: "否",
            col_need: "否",
            col_current: "Batch02回源闭合：Q5已在最终DOCX覆盖。",
            col_note: "只保留②④对应的矛盾落点，不扩展到发展等误触发。",
        },
        "M0291": {
            col_in_book: "否：选必三逻辑，不入必修四哲学宝典",
            col_node: "-",
            col_principle: "source bundle lines 242-252为Q6推理方法选择题，answer key line 19给出Q6=B。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除：选必三逻辑。",
            col_note: "不能因出现联系一词进入必修四。",
        },
        "M0292": {
            col_in_book: "否：政治与法治/法律情境，不入当前哲学宝典",
            col_node: "-",
            col_principle: "source bundle Q8为司法建议相关选择题，answer key line 19给出Q8=D。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除。",
            col_note: "矛盾词命中不是必修四哲学原理落点。",
        },
        "M0293": {
            col_in_book: "否：政治与法治/政协情境，不入当前哲学宝典",
            col_node: "-",
            col_principle: "source bundle Q9为政协相关选择题，answer key line 19给出Q9=B。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除。",
            col_note: "人民群众词命中不能替代题目模块判断。",
        },
        "M0294": {
            col_in_book: "否：法律与生活，不入当前哲学宝典",
            col_node: "-",
            col_principle: "source bundle Q11为法律选择题，answer key line 20给出Q11=C。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除。",
            col_note: "旧answer_support_only不能作哲学细则。",
        },
        "M0295": {
            col_in_book: "否：社会/经济情境，不入当前哲学宝典",
            col_node: "-",
            col_principle: "source bundle Q12为轨道服务等社会经济选择题，answer key line 20给出Q12=B。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除。",
            col_note: "矛盾词命中不足以入哲学宝典。",
        },
        "M0296": {
            col_in_book: "否：经济与社会，不入当前哲学宝典",
            col_node: "-",
            col_principle: "source bundle Q13为经济选择题，answer key line 20给出Q13=A。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除。",
            col_note: "发展词命中不足以入哲学宝典。",
        },
        "M0297": {
            col_in_book: "否：当代国际政治与经济，不入当前哲学宝典",
            col_node: "-",
            col_principle: "source bundle Q15为国际政治选择题，answer key line 20给出Q15=A。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除。",
            col_note: "发展/部分词命中不足以入哲学宝典。",
        },
        "M0298": {
            col_in_book: "是：已在最终DOCX覆盖（无需新增）",
            col_node: "主观能动性/联系/发展/实践",
            col_principle: q16_principle,
            col_evidence: "强细则",
            col_misplaced: "否",
            col_need: "否",
            col_current: "Batch02回源闭合：Q16已覆盖。",
            col_note: "剔除主要矛盾等非Q16正式角度。",
        },
        "M0299": {
            col_in_book: "否：题组不新增；Q17(2)误放已从DOCX移除",
            col_node: "Q17(2)应路由选必三分析与综合；Q17(1)经济；Q17(3)政治与法治",
            col_principle: "source bundle lines 67-82及432显示Q17(2)设问为分析与综合的思维方法；非必修四哲学原理节点。",
            col_evidence: "强细则+模块边界",
            col_misplaced: "是：旧DOCX含Q17(2)系统观念条目，Batch02已移除",
            col_need: "否：当前哲学宝典不补",
            col_current: "Batch02纠偏：删除旧误放条目并重编号系统观念节点。",
            col_note: "不得用分析综合题伪装系统优化题。",
        },
        "M0300": {
            col_in_book: "否：当代国际政治与经济/选必三逻辑，不入当前哲学宝典",
            col_node: "-",
            col_principle: "source bundle lines 29-32显示Q18含开放便利与不完全归纳推理，非当前哲学节点。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除。",
            col_note: "发展/认识词命中不足以入哲学宝典。",
        },
        "M0301": {
            col_in_book: "否：法律与生活，不入当前哲学宝典",
            col_node: "-",
            col_principle: "source bundle Q19为法律题，非必修四哲学原理节点。",
            col_evidence: "模块边界明确",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02边界排除。",
            col_note: "发展/整体/认识/部分词命中不足以入哲学宝典。",
        },
        "M0302": {
            col_in_book: "否：活动方案题，不作为当前哲学原理节点新增",
            col_node: "党史学习教育活动设计（文化/活动题另线）",
            col_principle: "source bundle lines 496-523为党史学习教育活动方案设计；评分看主题、内容、依据，不给具体哲学原理细则。",
            col_evidence: "活动题边界/无具体哲学细则",
            col_misplaced: "否：候选未入正文",
            col_need: "否：当前哲学宝典不补；若文化活动题专题化需另审",
            col_current: "Batch02边界排除当前哲学宝典。",
            col_note: "价值观/发展等词命中不能冒充评分细则。",
        },
        "M0303": {
            col_in_book: "否：抽取残片/题号未知，不入当前哲学宝典",
            col_node: "-",
            col_principle: "该行是source extraction残片，无法对应独立题号；不得入正文。",
            col_evidence: "抽取错误",
            col_misplaced: "否：候选未入正文",
            col_need: "否",
            col_current: "Batch02排除：题号未知残片。",
            col_note: "由逐题Q1-Q20裁决覆盖，不单列。",
        },
    }

    with matrix_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames
    if fieldnames is None:
        raise RuntimeError("matrix has no header")

    touched = []
    for row in rows:
        mid = row.get("matrix_row_id")
        if mid in decisions:
            row.update(decisions[mid])
            touched.append(mid)

    missing = sorted(set(decisions) - set(touched))
    if missing:
        raise RuntimeError(f"matrix ids not found: {missing}")

    with matrix_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return {"backup": str(backup), "touched": touched}


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    root = repo_root()
    delivery = root / "reports" / RUN_DIR / "05_delivery"
    docx_path = delivery / DOCX_BASENAME
    matrix_path = (
        root
        / "reports"
        / "bixiu4_thread_recovery_opus47_2026-05-24"
        / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
    )
    if not docx_path.exists():
        raise FileNotFoundError(docx_path)
    if not matrix_path.exists():
        raise FileNotFoundError(matrix_path)

    docx_result = remove_misplaced_q17_2(docx_path, ts)
    matrix_result = update_matrix(matrix_path, ts)
    print("DOCX_BACKUP", docx_result["backup"])
    print("REMOVED_PARAGRAPHS", len(docx_result["removed_paragraphs"]))
    for line in docx_result["removed_paragraphs"]:
        print("REMOVED", line)
    print("RENUMBERED_COUNT", docx_result["renumbered_count"])
    print("MATRIX_BACKUP", matrix_result["backup"])
    print("MATRIX_TOUCHED", ",".join(matrix_result["touched"]))


if __name__ == "__main__":
    main()
