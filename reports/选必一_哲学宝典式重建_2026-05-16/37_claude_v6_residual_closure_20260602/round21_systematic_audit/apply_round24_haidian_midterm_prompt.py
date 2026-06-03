from __future__ import annotations

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

IN_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第23轮设问逐字回源_带水印_20260603.docx")
OUT_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第24轮海淀期中设问标点回源_带水印_20260603.docx")
REPORT = Path(__file__).with_name("round24_haidian_midterm_prompt_report.json")

OLD = "运用《当代国际政治与经济》知识，说明全球治理倡议为什么能获得国际社会广泛认同。（6分）"
NEW = "运用《当代国际政治与经济》知识，说明全球治理倡议为什么能获得国际社会广泛认同，（6分）"


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def main() -> None:
    with ZipFile(IN_DOCX) as zin:
        root = etree.fromstring(zin.read("word/document.xml"))
        touched: list[dict[str, str | int]] = []
        count = 0

        for idx, paragraph in enumerate(root.xpath(".//w:p", namespaces=NS)):
            before = paragraph_text(paragraph)
            if OLD not in before:
                continue
            for node in paragraph.xpath(".//w:t", namespaces=NS):
                if node.text and OLD in node.text:
                    node.text = node.text.replace(OLD, NEW)
                    count += 1
            touched.append({"paragraph_index": idx, "before": before, "after": paragraph_text(paragraph)})

        updated_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
        with ZipFile(OUT_DOCX, "w", ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = updated_xml if info.filename == "word/document.xml" else zin.read(info.filename)
                zout.writestr(info, data)

    report = {"input": str(IN_DOCX), "output": str(OUT_DOCX), "count": count, "touched_paragraphs": touched}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
