from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from lxml import etree


INPUT = Path("/Users/wanglifei/Desktop/选必一6.1最终版_第26轮石景山同题组细则层同步_带水印_20260603.docx")
OUTPUT = Path("/Users/wanglifei/Desktop/选必一6.1终极版_系统复审美化终稿_带水印_20260603.docx")

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "v": "urn:schemas-microsoft-com:vml",
}
W = NS["w"]


def qn(tag: str) -> str:
    prefix, name = tag.split(":")
    return f"{{{NS[prefix]}}}{name}"


def clear_children(el: etree._Element) -> None:
    for child in list(el):
        el.remove(child)


def ensure_ppr(p: etree._Element) -> etree._Element:
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        ppr = etree.Element(qn("w:pPr"))
        p.insert(0, ppr)
    return ppr


def remove_ppr_child(ppr: etree._Element, name: str) -> None:
    for child in list(ppr.findall(qn(name))):
        ppr.remove(child)


def set_spacing(ppr: etree._Element, before: int | None = None, after: int | None = None) -> None:
    spacing = ppr.find(qn("w:spacing"))
    if spacing is None:
        spacing = etree.SubElement(ppr, qn("w:spacing"))
    if before is not None:
        spacing.set(qn("w:before"), str(before))
    if after is not None:
        spacing.set(qn("w:after"), str(after))


def set_indent(ppr: etree._Element, left: int = 0, first_line: int = 0) -> None:
    ind = ppr.find(qn("w:ind"))
    if ind is None:
        ind = etree.SubElement(ppr, qn("w:ind"))
    ind.set(qn("w:left"), str(left))
    ind.set(qn("w:firstLine"), str(first_line))


def set_shading_and_border(ppr: etree._Element, fill: str | None, border: str | None) -> None:
    remove_ppr_child(ppr, "w:shd")
    remove_ppr_child(ppr, "w:pBdr")
    if fill:
        shd = etree.SubElement(ppr, qn("w:shd"))
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), fill)
    if border:
        pbdr = etree.SubElement(ppr, qn("w:pBdr"))
        left = etree.SubElement(pbdr, qn("w:left"))
        left.set(qn("w:val"), "single")
        left.set(qn("w:sz"), "10")
        left.set(qn("w:space"), "4")
        left.set(qn("w:color"), border)


def make_rpr(
    *,
    bold: bool = False,
    color: str = "202124",
    size: int = 21,
    font: str = "Hiragino Sans GB",
) -> etree._Element:
    rpr = etree.Element(qn("w:rPr"))
    fonts = etree.SubElement(rpr, qn("w:rFonts"))
    for attr in ["ascii", "hAnsi", "eastAsia", "cs"]:
        fonts.set(qn(f"w:{attr}"), font)
    if bold:
        etree.SubElement(rpr, qn("w:b"))
    else:
        b = etree.SubElement(rpr, qn("w:b"))
        b.set(qn("w:val"), "0")
    c = etree.SubElement(rpr, qn("w:color"))
    c.set(qn("w:val"), color)
    sz = etree.SubElement(rpr, qn("w:sz"))
    sz.set(qn("w:val"), str(size))
    return rpr


def add_run(
    p: etree._Element,
    text: str,
    *,
    bold: bool = False,
    color: str = "202124",
    size: int = 21,
    font: str = "Hiragino Sans GB",
) -> None:
    r = etree.SubElement(p, qn("w:r"))
    r.append(make_rpr(bold=bold, color=color, size=size, font=font))
    t = etree.SubElement(r, qn("w:t"))
    if text[:1].isspace() or text[-1:].isspace() or "  " in text:
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text


def paragraph_text(p: etree._Element) -> str:
    return "".join(p.xpath(".//w:t/text()", namespaces=NS))


def replace_runs(p: etree._Element, pieces: list[dict]) -> None:
    ppr = p.find(qn("w:pPr"))
    for child in list(p):
        if child is not ppr:
            p.remove(child)
    for piece in pieces:
        add_run(p, **piece)


def polish_document_xml(xml: bytes) -> bytes:
    root = etree.fromstring(xml)
    body = root.find(qn("w:body"))
    assert body is not None

    labels = {
        "【材料触发点】": ("2F6F9F", "EAF3F8", None),
        "【设问】": ("536471", None, None),
        "【为什么能想到】": ("1F5E8C", None, None),
    }

    for p in body.findall(qn("w:p")):
        text = paragraph_text(p).strip()
        if not text:
            continue
        ppr = ensure_ppr(p)

        if text.startswith("【答案落点】"):
            body_text = text[len("【答案落点】") :].strip()
            set_spacing(ppr, before=80, after=100)
            set_indent(ppr, left=0, first_line=0)
            set_shading_and_border(ppr, "FFF2CC", "D2691E")
            replace_runs(
                p,
                [
                    {"text": "【答案落点】  ", "bold": True, "color": "8A3B12", "size": 21},
                    {"text": body_text, "bold": True, "color": "111111", "size": 21},
                ],
            )
            continue

        if text.startswith("【同题组】"):
            rest = text[len("【同题组】") :].strip()
            set_spacing(ppr, before=80, after=35)
            set_indent(ppr, left=0, first_line=0)
            set_shading_and_border(ppr, None, None)
            pieces = [{"text": "【同题组】", "bold": True, "color": "697780", "size": 20}]
            if rest:
                pieces.append({"text": f"  {rest}", "bold": False, "color": "697780", "size": 19})
            replace_runs(p, pieces)
            continue

        matched = False
        for label, (label_color, fill, border) in labels.items():
            if text.startswith(label):
                body_text = text[len(label) :].strip()
                set_spacing(ppr, before=45, after=65)
                set_indent(ppr, left=0, first_line=0)
                set_shading_and_border(ppr, fill, border)
                replace_runs(
                    p,
                    [
                        {"text": f"{label}  ", "bold": True, "color": label_color, "size": 21},
                        {"text": body_text, "bold": False, "color": "202124", "size": 21},
                    ],
                )
                matched = True
                break
        if matched:
            continue

        if text.startswith("· "):
            set_spacing(ppr, before=0, after=45)
            set_indent(ppr, left=260, first_line=0)
            set_shading_and_border(ppr, None, None)
            if "：" in text:
                prefix, rest = text.split("：", 1)
                replace_runs(
                    p,
                    [
                        {"text": f"{prefix}：", "bold": True, "color": "1F5E8C", "size": 19},
                        {"text": rest, "bold": False, "color": "27323A", "size": 19},
                    ],
                )
            else:
                replace_runs(p, [{"text": text, "bold": False, "color": "27323A", "size": 19}])
            continue

        if text.startswith("核心答题点："):
            set_spacing(ppr, before=120, after=90)
            set_indent(ppr, left=0, first_line=0)
            set_shading_and_border(ppr, "EAF3F8", "2F6F9F")
            term = text[len("核心答题点：") :].strip()
            replace_runs(
                p,
                [
                    {"text": "核心答题点：", "bold": True, "color": "1F5E8C", "size": 23},
                    {"text": term, "bold": True, "color": "1F5E8C", "size": 23},
                ],
            )
            continue

        # Entry titles: make each source question easy to catch while scanning.
        if text[:2].strip().isdigit() and ". 20" in text[:12]:
            set_spacing(ppr, before=120, after=75)
            set_indent(ppr, left=0, first_line=0)
            replace_runs(p, [{"text": text, "bold": True, "color": "1F5E8C", "size": 24}])

    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def polish_header_xml(xml: bytes) -> bytes:
    root = etree.fromstring(xml)
    for shape in root.xpath(".//v:shape", namespaces=NS):
        if shape.get("id") == "PowerPlusWaterMarkObjectCodexFeige":
            shape.set("fillcolor", "#6F6F6F")
            fill = shape.find(".//v:fill", namespaces=NS)
            if fill is not None:
                fill.set("opacity", ".42")
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(INPUT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        with ZipFile(INPUT) as zin:
            zin.extractall(tmp_path)

        document_xml = tmp_path / "word" / "document.xml"
        document_xml.write_bytes(polish_document_xml(document_xml.read_bytes()))

        for header in (tmp_path / "word").glob("header*.xml"):
            header.write_bytes(polish_header_xml(header.read_bytes()))

        if OUTPUT.exists():
            OUTPUT.unlink()
        with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zout:
            for path in sorted(tmp_path.rglob("*")):
                if path.is_file():
                    zout.write(path, path.relative_to(tmp_path).as_posix())

    shutil.copystat(INPUT, OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
