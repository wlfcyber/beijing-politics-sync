from __future__ import annotations

import csv
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
W = f"{{{W_NS}}}"
XML = f"{{{XML_NS}}}"
NS = {"w": W_NS}

RECOVERY = Path(__file__).resolve().parent
RUN_DIR = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN_DIR / "05_delivery"
LEDGER = DELIVERY / "docx_insert_ledger.csv"

LABELS = [
    "【材料触发点】",
    "【设问】",
    "【为什么能想到】",
    "【答案落点】",
]


def current_docx() -> Path:
    docs = [
        p
        for p in DELIVERY.glob("*.docx")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
    if len(docs) != 1:
        raise SystemExit(f"expected exactly one current DOCX, found {len(docs)}: {docs}")
    return docs[0]


def para_text(p: ET.Element) -> str:
    return "".join(t.text or "" for t in p.findall(".//w:t", NS))


def ensure_spacing_after_80(p: ET.Element) -> bool:
    ppr = p.find("./w:pPr", NS)
    if ppr is None:
        ppr = ET.Element(W + "pPr", nsmap=p.nsmap)
        p.insert(0, ppr)
    spacing = ppr.find("./w:spacing", NS)
    if spacing is None:
        spacing = ET.Element(W + "spacing")
        ppr.append(spacing)
    changed = spacing.get(W + "after") != "80"
    spacing.set(W + "after", "80")
    return changed


def make_run(text: str, *, label: bool) -> ET.Element:
    r = ET.Element(W + "r")
    if label:
        rpr = ET.SubElement(r, W + "rPr")
        ET.SubElement(rpr, W + "b")
        color = ET.SubElement(rpr, W + "color")
        color.set(W + "val", "21574C")
    t = ET.SubElement(r, W + "t")
    if text.startswith(" ") or text.endswith(" "):
        t.set(XML + "space", "preserve")
    t.text = text
    return r


def replace_runs_with_label_split(p: ET.Element, label: str, full_text: str) -> bool:
    expected_rest = full_text[len(label) :]
    current_runs = p.findall("./w:r", NS)
    if len(current_runs) >= 2:
        first_text = para_text(current_runs[0])
        if first_text == label:
            rpr = current_runs[0].find("./w:rPr", NS)
            color = rpr.find("./w:color", NS).get(W + "val") if rpr is not None and rpr.find("./w:color", NS) is not None else None
            bold = rpr is not None and rpr.find("./w:b", NS) is not None
            if bold and color == "21574C":
                return False

    for child in list(p):
        if child.tag == W + "r":
            p.remove(child)

    p.append(make_run(label, label=True))
    if expected_rest:
        p.append(make_run(expected_rest, label=False))
    return True


def main() -> None:
    docx = current_docx()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = docx.with_name(f"{docx.stem}_backup_before_inserted_label_style_fix_{timestamp}{docx.suffix}")
    shutil.copy2(docx, backup)

    with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        headings = {row["inserted_heading"] for row in csv.DictReader(f)}

    with zipfile.ZipFile(docx, "r") as zin:
        document_xml = zin.read("word/document.xml")
        all_items = [(item, zin.read(item.filename)) for item in zin.infolist()]

    parser = ET.XMLParser(remove_blank_text=False, resolve_entities=False)
    root = ET.fromstring(document_xml, parser=parser)
    body_paras = root.findall(".//w:body/w:p", NS)
    heading_indexes = [i for i, p in enumerate(body_paras) if para_text(p) in headings]

    label_paragraphs_seen = 0
    spacing_updates = 0
    run_splits = 0

    for idx in heading_indexes:
        for p in body_paras[idx + 1 : idx + 6]:
            text = para_text(p)
            label = next((candidate for candidate in LABELS if text.startswith(candidate)), None)
            if label is None:
                continue
            label_paragraphs_seen += 1
            if ensure_spacing_after_80(p):
                spacing_updates += 1
            if replace_runs_with_label_split(p, label, text):
                run_splits += 1

    if label_paragraphs_seen != len(heading_indexes) * 4:
        raise SystemExit(
            f"expected {len(heading_indexes) * 4} inserted label paragraphs, "
            f"found {label_paragraphs_seen}; backup preserved at {backup}"
        )

    new_document_xml = ET.tostring(
        root,
        encoding="UTF-8",
        xml_declaration=True,
        standalone=True,
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)

    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for item, data in all_items:
            if item.filename == "word/document.xml":
                zout.writestr(item, new_document_xml)
            else:
                zout.writestr(item, data)

    shutil.move(str(tmp_path), docx)
    print(f"docx={docx}")
    print(f"backup={backup}")
    print(f"inserted_headings={len(heading_indexes)}")
    print(f"label_paragraphs_seen={label_paragraphs_seen}")
    print(f"spacing_updates={spacing_updates}")
    print(f"run_splits={run_splits}")


if __name__ == "__main__":
    main()
