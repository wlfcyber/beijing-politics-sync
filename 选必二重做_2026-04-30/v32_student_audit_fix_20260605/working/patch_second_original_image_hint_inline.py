from __future__ import annotations

import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


DOCX = Path("/Users/wanglifei/Desktop/选必二法律与生活_试题细则汇编_学生可发版_v32.docx")
BACKUP = DOCX.with_suffix(DOCX.suffix + ".before_second_image_hint_inline_20260605.bak")
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

HINT = "【提示】 设问、细则与答案落点见下方原题图续块。"
INLINE_HINT = "（设问、细则与答案落点见下方原题图续块。）"


def p_text(p: etree._Element) -> str:
    return "".join(p.xpath(".//w:t/text()", namespaces=NS)).strip()


def append_to_last_text_run(p: etree._Element, extra: str) -> None:
    texts = p.xpath(".//w:t", namespaces=NS)
    if texts:
        texts[-1].text = (texts[-1].text or "") + extra


def remove_paragraph(p: etree._Element) -> None:
    parent = p.getparent()
    parent.remove(p)


def main() -> None:
    shutil.copy2(DOCX, BACKUP)
    with ZipFile(DOCX) as zin:
        root = etree.fromstring(zin.read("word/document.xml"))
        paras = list(root.xpath(".//w:p", namespaces=NS))
        orig_indexes = [i for i, p in enumerate(paras) if p_text(p) == "原题图"]
        if len(orig_indexes) < 2:
            raise RuntimeError("second 原题图 not found")

        second_orig = paras[orig_indexes[1]]
        second_hint = paras[orig_indexes[1] - 1]
        if p_text(second_hint) != HINT:
            raise RuntimeError("second hint paragraph not found before second 原题图")

        prev = second_hint.getprevious()
        while prev is not None and not p_text(prev):
            prev = prev.getprevious()
        if prev is None:
            raise RuntimeError("previous material paragraph not found")
        if INLINE_HINT not in p_text(prev):
            append_to_last_text_run(prev, INLINE_HINT)

        remove_paragraph(second_orig)
        remove_paragraph(second_hint)

        xml = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone="yes")
        with NamedTemporaryFile(delete=False) as tmp:
            tmp_path = Path(tmp.name)
        with ZipFile(tmp_path, "w", ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = xml if item.filename == "word/document.xml" else zin.read(item.filename)
                zout.writestr(item, data)
    shutil.move(tmp_path, DOCX)
    print("second_original_image_hint_inlined=1")
    print(f"backup={BACKUP}")


if __name__ == "__main__":
    main()
