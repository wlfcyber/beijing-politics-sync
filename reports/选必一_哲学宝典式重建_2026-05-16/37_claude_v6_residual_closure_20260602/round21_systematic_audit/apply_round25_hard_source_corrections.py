from __future__ import annotations

import copy
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

IN_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第24轮海淀期中设问标点回源_带水印_20260603.docx")
OUT_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第25轮材料污染与细则层纠错_带水印_20260603.docx")
REPORT = Path(__file__).with_name("round25_hard_source_corrections_report.json")

OLD_GENERIC_CORE = "推动国际秩序和全球治理体系更加公正合理"
NEW_SHIJINGSHAN_CORE = "践行真正的多边主义，坚定维护以联合国为核心的国际体系、以国际法为基础的国际秩序"
HEADING_OLD = f"核心答题点：{OLD_GENERIC_CORE}"
HEADING_NEW = f"核心答题点：{NEW_SHIJINGSHAN_CORE}"

REPLACEMENTS = [
    {
        "label": "fengtai_2026_er_mo_q20_remove_dongcheng_pollution",
        "old": "“投资中国”靠扩大服务业市场准入、对接国际标准、外资税收抵免压低进入门槛与成本，门槛降外资才进得便利，对应推进贸易和投资自由化便利化。",
        "new": "材料写自贸区、自贸港推动跨境金融、离岸贸易、高端制造等新业态发展，这些都在降低跨境流通和投资合作成本。设问问“为世界注入确定性”，应把这些平台功能上升为贸易投资自由化便利化和稳定制度预期。",
    },
    {
        "label": "shijingshan_2025_q17_answer_exact_rubric",
        "old": "中国主张践行真正的多边主义，坚定以平等协商推动全球治理完善。",
        "new": "中国主张践行真正的多边主义，坚定维护以联合国为核心的国际体系、以国际法为基础的国际秩序。",
    },
    {
        "label": "shijingshan_2025_q17_why_exact_rubric",
        "old": "北京宣言强调\"国际法平等统一适用\"\"开放包容\"，指向治理方式应回到以联合国和国际法为基础的国际体系，而不是少数国家自定的规则。问\"中国主张\"，主张指向治理体系与秩序基础的根本表态，而不是个别治理事项的处理意见。先把国际法平等统一适用和开放包容作为题面给出的治理方式特征摆出，再写中国主张践行真正的多边主义、进而接到以平等协商推动全球治理完善。",
        "new": "北京宣言强调“国际法平等统一适用”“开放包容”，指向治理方式应回到以联合国和国际法为基础的国际体系，而不是少数国家自定规则。问“中国主张”，应把这一路径落到细则第④层：践行真正的多边主义，坚定维护以联合国为核心的国际体系、以国际法为基础的国际秩序。",
    },
]


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def set_paragraph_text(paragraph: etree._Element, text: str) -> None:
    text_nodes = paragraph.xpath(".//w:t", namespaces=NS)
    if not text_nodes:
        run = etree.SubElement(paragraph, f"{{{NS['w']}}}r")
        node = etree.SubElement(run, f"{{{NS['w']}}}t")
        node.text = text
        return
    text_nodes[0].text = text
    for node in text_nodes[1:]:
        node.text = ""


def replace_text_nodes(root: etree._Element) -> dict[str, int]:
    counts = {item["label"]: 0 for item in REPLACEMENTS}
    for paragraph in root.xpath(".//w:body/w:p", namespaces=NS):
        before = paragraph_text(paragraph)
        if not before:
            continue
        for item in REPLACEMENTS:
            if item["old"] not in before:
                continue
            for node in paragraph.xpath(".//w:t", namespaces=NS):
                if node.text and item["old"] in node.text:
                    node.text = node.text.replace(item["old"], item["new"])
                    counts[item["label"]] += 1
    return counts


def insert_precision_heading(root: etree._Element) -> dict[str, int]:
    body = root.find(f".//{{{NS['w']}}}body")
    if body is None:
        raise RuntimeError("document body not found")
    paras = body.xpath("./w:p", namespaces=NS)
    heading_template = None
    q17_para = None
    q22_para = None
    existing_new = False

    for paragraph in paras:
        text = paragraph_text(paragraph)
        if text == HEADING_NEW:
            existing_new = True
        if text == HEADING_OLD and heading_template is None:
            heading_template = paragraph
        if text == "14. 2025石景山一模Q17(2)":
            q17_para = paragraph
        if text.startswith("15. 2026海淀期中Q22(1)全球治理倡议指引公正合理治理体系建设"):
            q22_para = paragraph

    if heading_template is None or q17_para is None or q22_para is None:
        raise RuntimeError("required heading or target paragraphs not found")

    inserted = 0
    if not existing_new:
        new_heading = copy.deepcopy(heading_template)
        set_paragraph_text(new_heading, HEADING_NEW)
        body.insert(body.index(q17_para), new_heading)
        inserted += 1

    # Restore the original generic heading before the following Q22 entry so only Q17(2) is under the precision core.
    prev = q22_para.getprevious()
    if prev is None or paragraph_text(prev) != HEADING_OLD:
        restore_heading = copy.deepcopy(heading_template)
        set_paragraph_text(restore_heading, HEADING_OLD)
        body.insert(body.index(q22_para), restore_heading)
        inserted += 1

    return {"inserted_headings": inserted}


def replace_shijingshan_tongtizu(root: etree._Element) -> int:
    count = 0
    for paragraph in root.xpath(".//w:body/w:p", namespaces=NS):
        text = paragraph_text(paragraph)
        if "2025石景山一模Q17(2)" in text:
            # Titles are handled separately; keep scanning nearby by direct text replacement in all paragraphs.
            pass
        if OLD_GENERIC_CORE in text and "【同题组】" in text:
            # Only replace in the Q17(2) same-group blocks. They have the unique economic-globalization peer.
            if "推进普惠包容的经济全球化，推动构建更加开放、包容的全球经济格局" in text:
                for node in paragraph.xpath(".//w:t", namespaces=NS):
                    if node.text and OLD_GENERIC_CORE in node.text:
                        node.text = node.text.replace(OLD_GENERIC_CORE, NEW_SHIJINGSHAN_CORE)
                        count += 1
    return count


def main() -> None:
    with ZipFile(IN_DOCX) as zin:
        root = etree.fromstring(zin.read("word/document.xml"))
        counts = replace_text_nodes(root)
        heading_counts = insert_precision_heading(root)
        tong_count = replace_shijingshan_tongtizu(root)

        updated_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
        with ZipFile(OUT_DOCX, "w", ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = updated_xml if info.filename == "word/document.xml" else zin.read(info.filename)
                zout.writestr(info, data)

    report = {
        "input": str(IN_DOCX),
        "output": str(OUT_DOCX),
        "text_replacements": counts,
        "heading_changes": heading_counts,
        "shijingshan_tongtizu_replacements": tong_count,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
