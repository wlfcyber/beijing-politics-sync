from __future__ import annotations

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

IN_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第21轮系统同题组与设问校正_带水印_20260603.docx")
OUT_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第22轮源卡补证与书名纠错_带水印_20260603.docx")
REPORT = Path(__file__).with_name("round22_source_fix_report.json")


REPLACEMENTS = [
    {
        "label": "remove_backend_phrase_yaoluodao",
        "old": " 甲同学反复强调芯片、算法、大模型等核心环节要自主可控、把握创新主动权；这层技术自立要落到能力上，便是加强技术创新、提高质量以增强核心竞争力。",
        "new": " 甲同学反复强调芯片、算法、大模型等核心环节要自主可控、把握创新主动权；这些信息说明人工智能发展不能只依赖外部技术输入，而要通过技术创新和质量提升形成核心竞争力。",
    },
    {
        "label": "xicheng_qimo_q20_book_title_exact_source",
        "old": " 结合材料，运用《当代国际政治与经济》知识，阐释参与全球气候治理的中国实践。",
        "new": " 结合材料，运用《国际政治与经济》知识，阐释参与全球气候治理的中国实践。",
    },
]


def paragraph_text(paragraph: etree._Element) -> str:
    return "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))


def replace_in_text_nodes(paragraph: etree._Element, old: str, new: str) -> int:
    changed = 0
    for node in paragraph.xpath(".//w:t", namespaces=NS):
        if node.text and old in node.text:
            node.text = node.text.replace(old, new)
            changed += 1
    return changed


def main() -> None:
    with ZipFile(IN_DOCX) as zin:
        document_xml = zin.read("word/document.xml")
        root = etree.fromstring(document_xml)

        counts = {item["label"]: 0 for item in REPLACEMENTS}
        touched_paragraphs: list[dict[str, str | int]] = []

        for idx, paragraph in enumerate(root.xpath(".//w:p", namespaces=NS)):
            before = paragraph_text(paragraph)
            if not before:
                continue
            for item in REPLACEMENTS:
                if item["old"] in before:
                    node_hits = replace_in_text_nodes(paragraph, item["old"], item["new"])
                    if node_hits:
                        counts[item["label"]] += node_hits
                        touched_paragraphs.append(
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

    report = {
        "input": str(IN_DOCX),
        "output": str(OUT_DOCX),
        "counts": counts,
        "touched_paragraphs": touched_paragraphs,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
