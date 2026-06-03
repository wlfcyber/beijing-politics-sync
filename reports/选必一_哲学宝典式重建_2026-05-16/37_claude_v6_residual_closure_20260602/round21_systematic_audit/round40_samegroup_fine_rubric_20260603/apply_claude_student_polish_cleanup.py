from __future__ import annotations

import json
import re
import shutil
import tempfile
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

from lxml import etree


INPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细颗粒全量修正_核心答题点红色强化_学生版_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_同题组细颗粒全量修正_核心答题点红色强化_标点话术清理版_学生版_带水印_20260603.docx")
REPORT = Path(__file__).with_name("claude_student_polish_cleanup_report.json")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def paragraph_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def replace_in_paragraph(p: etree._Element, replacements: list[tuple[str, str]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for t in p.xpath(".//w:t", namespaces=NS):
        if not t.text:
            continue
        text = t.text
        for old, new in replacements:
            if old in text:
                counts[old] = counts.get(old, 0) + text.count(old)
                text = text.replace(old, new)
        t.text = text
    return counts


def fix_document_xml(xml_bytes: bytes) -> tuple[bytes, dict[str, int]]:
    root = etree.fromstring(xml_bytes)
    stats = {
        "answer_halfwidth_commas_replaced": 0,
        "ke_xie_wei_replaced": 0,
        "defen_point_replaced": 0,
        "awkward_china_version_phrase_replaced": 0,
        "mixed_full_open_half_close_replaced": 0,
    }

    for p in root.xpath(".//w:body/w:p", namespaces=NS):
        text = paragraph_text(p)

        if text.startswith("【答案落点】") and "," in text:
            for t in p.xpath(".//w:t", namespaces=NS):
                if t.text and "," in t.text:
                    stats["answer_halfwidth_commas_replaced"] += t.text.count(",")
                    t.text = t.text.replace(",", "，")

        counts = replace_in_paragraph(
            p,
            [
                ("可写为：", "可写："),
                ("可写为", "可写："),
                ("不作为本题选必一得分点", "不作为本题选必一有效答案方向"),
                (
                    "先把低碳能源、人工智能等领域中国贡献国际标准作为“通用语言”的中国版本点出",
                    "先说明低碳能源、人工智能等领域的中国标准正在成为国际社会可共享的“通用语言”",
                ),
            ],
        )
        stats["ke_xie_wei_replaced"] += counts.get("可写为：", 0) + counts.get("可写为", 0)
        stats["defen_point_replaced"] += counts.get("不作为本题选必一得分点", 0)
        stats["awkward_china_version_phrase_replaced"] += counts.get(
            "先把低碳能源、人工智能等领域中国贡献国际标准作为“通用语言”的中国版本点出", 0
        )

        # Only normalize the specific mixed Chinese punctuation pattern `（... )`.
        # This intentionally does not touch question markers such as Q20(2).
        for t in p.xpath(".//w:t", namespaces=NS):
            if not t.text:
                continue
            new_text, count = re.subn(r"（([^）\r\n()]*)\)", r"（\1）", t.text)
            if count:
                stats["mixed_full_open_half_close_replaced"] += count
                t.text = new_text

    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes"), stats


def audit_docx(path: Path) -> dict[str, int]:
    with ZipFile(path) as z:
        root = etree.fromstring(z.read("word/document.xml"))
    texts = [paragraph_text(p) for p in root.xpath(".//w:body/w:p", namespaces=NS)]
    full = "\n".join(texts)
    return {
        "answer_halfwidth_commas_remaining": sum(t.count(",") for t in texts if t.startswith("【答案落点】")),
        "ke_xie_wei_remaining": full.count("可写为"),
        "defen_point_remaining": full.count("得分点"),
        "awkward_china_version_phrase_remaining": full.count("中国版本点出"),
        "mixed_full_open_half_close_remaining": sum(
            len(re.findall(r"（[^）\r\n()]*\)", t)) for t in texts
        ),
        "core_heading_count": sum(t.startswith("核心答题点：") for t in texts),
        "samegroup_count": full.count("【同题组】"),
    }


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(INPUT)

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        shutil.copy2(INPUT, tmp / "input.docx")

        with ZipFile(INPUT, "r") as zin, ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "word/document.xml":
                    data, stats = fix_document_xml(data)
                zout.writestr(item, data)

    before = audit_docx(INPUT)
    after = audit_docx(OUTPUT)
    report = {"input": str(INPUT), "output": str(OUTPUT), "changes": stats, "before": before, "after": after}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
