from __future__ import annotations

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

IN_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第25轮材料污染与细则层纠错_带水印_20260603.docx")
OUT_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第26轮石景山同题组细则层同步_带水印_20260603.docx")
REPORT = Path(__file__).with_name("round26_shijingshan_tongtizu_report.json")

OLD = "推动国际秩序和全球治理体系更加公正合理"
NEW = "践行真正的多边主义，坚定维护以联合国为核心的国际体系、以国际法为基础的国际秩序"


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def replace_in_paragraph(paragraph: etree._Element, old: str, new: str) -> int:
    count = 0
    for node in paragraph.xpath(".//w:t", namespaces=NS):
        if node.text and old in node.text:
            node.text = node.text.replace(old, new)
            count += 1
    return count


def main() -> None:
    with ZipFile(IN_DOCX) as zin:
        root = etree.fromstring(zin.read("word/document.xml"))
        body = root.find(f".//{{{NS['w']}}}body")
        if body is None:
            raise RuntimeError("document body not found")
        paras = body.xpath("./w:p", namespaces=NS)
        touched: list[dict[str, str | int]] = []
        replacements = 0

        for i, paragraph in enumerate(paras):
            title = paragraph_text(paragraph)
            if "2025石景山一模Q17(2)" not in title:
                continue
            j = i + 1
            while j < len(paras):
                text = paragraph_text(paras[j])
                # Stop at the next example title or heading-like core/title paragraph.
                if j > i and (
                    text.startswith("核心答题点：")
                    or text.startswith("第")
                    or (text[:2].strip(".").isdigit() and "Q" in text)
                    or (text and text[0].isdigit() and ". " in text and "Q" in text)
                ):
                    break
                before = paragraph_text(paras[j])
                if before.startswith("· 政治多极化：") and OLD in before:
                    hit = replace_in_paragraph(paras[j], OLD, NEW)
                    if hit:
                        replacements += hit
                        touched.append({"paragraph_index": j, "before": before, "after": paragraph_text(paras[j])})
                j += 1

        updated_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
        with ZipFile(OUT_DOCX, "w", ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = updated_xml if info.filename == "word/document.xml" else zin.read(info.filename)
                zout.writestr(info, data)

    report = {"input": str(IN_DOCX), "output": str(OUT_DOCX), "replacements": replacements, "touched": touched}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
