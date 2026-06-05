from __future__ import annotations

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


DOCX = Path("/Users/wanglifei/Desktop/选必二法律与生活_试题细则汇编_学生可发版_v32.docx")
BACKUP = DOCX.with_suffix(DOCX.suffix + ".before_keep_original_image_heading_20260605.bak")
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def p_text(p: etree._Element) -> str:
    return "".join(p.xpath(".//w:t/text()", namespaces=NS)).strip()


def ensure_keep_next(p: etree._Element) -> None:
    p_pr = p.find(W + "pPr")
    if p_pr is None:
        p_pr = etree.Element(W + "pPr")
        p.insert(0, p_pr)
    if p_pr.find(W + "keepNext") is None:
        p_pr.insert(0, etree.Element(W + "keepNext"))


def main() -> None:
    shutil.copy2(DOCX, BACKUP)
    with ZipFile(DOCX) as zin:
        root = etree.fromstring(zin.read("word/document.xml"))
        changed = 0
        for p in root.xpath(".//w:p", namespaces=NS):
            if p_text(p) in {"【提示】 设问、细则与答案落点见下方原题图续块。", "原题图"}:
                ensure_keep_next(p)
                changed += 1
        xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
        with NamedTemporaryFile(delete=False) as tmp:
            tmp_path = Path(tmp.name)
        with ZipFile(tmp_path, "w", ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = xml if item.filename == "word/document.xml" else zin.read(item.filename)
                zout.writestr(item, data)
    shutil.move(tmp_path, DOCX)
    print(f"keep_next_paragraphs={changed}")
    print(f"backup={BACKUP}")


if __name__ == "__main__":
    main()
