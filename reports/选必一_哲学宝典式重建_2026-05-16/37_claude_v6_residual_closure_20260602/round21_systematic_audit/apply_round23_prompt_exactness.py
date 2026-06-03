from __future__ import annotations

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

IN_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第22轮源卡补证与书名纠错_带水印_20260603.docx")
OUT_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第23轮设问逐字回源_带水印_20260603.docx")
REPORT = Path(__file__).with_name("round23_prompt_exactness_report.json")


REPLACEMENTS = [
    {
        "label": "haidian_2026_er_mo_q20_2_restore_theme_quotes_score",
        "old": " 结合材料，运用《当代国际政治与经济》知识，围绕全球发展倡议从合作理念到丰富实践这一主题，撰写一篇短评。",
        "new": " 结合材料，运用《当代国际政治与经济》知识，围绕“全球发展倡议从合作理念到丰富实践”这一主题，撰写一篇短评。（7分）",
    },
    {
        "label": "haidian_2026_midterm_q22_1_restore_original_comma_score",
        "old": " 运用《当代国际政治与经济》知识，说明全球治理倡议为什么能获得国际社会广泛认同。（6分）",
        "new": " 运用《当代国际政治与经济》知识，说明全球治理倡议为什么能获得国际社会广泛认同，（6分）",
    },
]


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def main() -> None:
    with ZipFile(IN_DOCX) as zin:
        root = etree.fromstring(zin.read("word/document.xml"))
        counts = {item["label"]: 0 for item in REPLACEMENTS}
        touched: list[dict[str, str | int]] = []

        for idx, paragraph in enumerate(root.xpath(".//w:p", namespaces=NS)):
            before = paragraph_text(paragraph)
            if not before:
                continue
            for item in REPLACEMENTS:
                for node in paragraph.xpath(".//w:t", namespaces=NS):
                    if node.text and item["old"] in node.text:
                        node.text = node.text.replace(item["old"], item["new"])
                        counts[item["label"]] += 1
                        touched.append(
                            {
                                "paragraph_index": idx,
                                "label": item["label"],
                                "before": before,
                                "after": paragraph_text(paragraph),
                            }
                        )

        updated_xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
        with ZipFile(OUT_DOCX, "w", ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = updated_xml if info.filename == "word/document.xml" else zin.read(info.filename)
                zout.writestr(info, data)

    report = {"input": str(IN_DOCX), "output": str(OUT_DOCX), "counts": counts, "touched_paragraphs": touched}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
