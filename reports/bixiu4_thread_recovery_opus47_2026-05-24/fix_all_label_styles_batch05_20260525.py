from __future__ import annotations

import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
W = f"{{{W_NS}}}"
XML = f"{{{XML_NS}}}"
NS = {"w": W_NS}

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"

LABELS = [
    "【材料触发点】",
    "【设问】",
    "【为什么能想到】",
    "【答案落点】",
]


def current_docx() -> Path:
    docs = [
        p for p in DELIVERY.glob("*.docx")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def para_text(p: etree._Element) -> str:
    return "".join(t.text or "" for t in p.xpath(".//w:t", namespaces=NS))


def make_run(text: str, *, label: bool) -> etree._Element:
    r = etree.Element(W + "r")
    if label:
        rpr = etree.SubElement(r, W + "rPr")
        etree.SubElement(rpr, W + "b")
        color = etree.SubElement(rpr, W + "color")
        color.set(W + "val", "21574C")
    t = etree.SubElement(r, W + "t")
    if text.startswith(" ") or text.endswith(" "):
        t.set(XML + "space", "preserve")
    t.text = text
    return r


def normalize_label_para(p: etree._Element, label: str, rest: str) -> None:
    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)
    p.append(make_run(label, label=True))
    p.append(make_run(" " + rest.strip(), label=False))
    ppr = p.find("./w:pPr", namespaces=NS)
    if ppr is None:
        ppr = etree.Element(W + "pPr", nsmap=p.nsmap)
        p.insert(0, ppr)
    spacing = ppr.find("./w:spacing", namespaces=NS)
    if spacing is None:
        spacing = etree.SubElement(ppr, W + "spacing")
    spacing.set(W + "after", "80")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_all_label_style_fix_batch05_{timestamp}.docx")
    shutil.copy2(docx, backup)

    with zipfile.ZipFile(docx, "r") as zin:
        infos = zin.infolist()
        data = {info.filename: zin.read(info.filename) for info in infos}
    root = etree.fromstring(data["word/document.xml"])

    changed = 0
    for p in root.xpath(".//w:p", namespaces=NS):
        text = para_text(p)
        for label in LABELS:
            if text.startswith(label):
                normalize_label_para(p, label, text[len(label):])
                changed += 1
                break

    data["word/document.xml"] = etree.tostring(root, encoding="UTF-8", xml_declaration=True, standalone=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)
    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
        for info in infos:
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.comment = info.comment
            zi.extra = info.extra
            zi.internal_attr = info.internal_attr
            zi.external_attr = info.external_attr
            zi.create_system = info.create_system
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, data[info.filename])
    shutil.move(str(tmp_path), docx)
    print(f"DOCX_BACKUP={backup}")
    print(f"LABEL_PARAGRAPHS_NORMALIZED={changed}")


if __name__ == "__main__":
    main()
