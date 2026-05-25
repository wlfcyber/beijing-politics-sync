from __future__ import annotations

import json
import re
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET


RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
REPORT_MD = RECOVERY / "HEADING_STYLE_CONSISTENCY_FIX_20260525.md"
REPORT_JSON = RECOVERY / "HEADING_STYLE_CONSISTENCY_FIX_20260525.json"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"
QUESTION_HEADING_RE = re.compile(r"^\s*\d+\.\s*20(?:24|25|26).+第.+题")


ET.register_namespace("w", W_NS)
ET.register_namespace("w14", "http://schemas.microsoft.com/office/word/2010/wordml")
ET.register_namespace("w15", "http://schemas.microsoft.com/office/word/2012/wordml")
ET.register_namespace("w16cid", "http://schemas.microsoft.com/office/word/2016/wordml/cid")


def current_docx() -> Path:
    files = [
        p
        for p in DELIVERY.glob("*.docx")
        if not p.name.startswith("~$") and "_backup_" not in p.stem
    ]
    if len(files) != 1:
        raise RuntimeError(f"Expected one current docx, got {files}")
    return files[0]


def paragraph_text(p: ET.Element) -> str:
    return "".join((t.text or "") for t in p.iter(f"{W}t")).strip()


def make_heading_rpr() -> ET.Element:
    rpr = ET.Element(f"{W}rPr")
    lang = ET.SubElement(rpr, f"{W}lang")
    lang.set(f"{W}eastAsia", "zh-CN")
    return rpr


def normalize_document_xml(xml: bytes) -> tuple[bytes, list[str], int]:
    root = ET.fromstring(xml)
    changed_headings: list[str] = []
    changed_runs = 0
    for p in root.iter(f"{W}p"):
        text = paragraph_text(p)
        if not QUESTION_HEADING_RE.match(text):
            continue
        changed_this_heading = False
        for run in p.findall(f"{W}r"):
            current = run.find(f"{W}rPr")
            new_rpr = make_heading_rpr()
            if current is None:
                run.insert(0, new_rpr)
                changed_runs += 1
                changed_this_heading = True
            else:
                current_xml = ET.tostring(current, encoding="utf-8")
                target_xml = ET.tostring(new_rpr, encoding="utf-8")
                if current_xml != target_xml:
                    run.remove(current)
                    run.insert(0, new_rpr)
                    changed_runs += 1
                    changed_this_heading = True
        if changed_this_heading:
            changed_headings.append(text)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True), changed_headings, changed_runs


def rewrite_docx(docx: Path, new_document_xml: bytes) -> None:
    temp = docx.with_suffix(".tmp.docx")
    with zipfile.ZipFile(docx, "r") as zin, zipfile.ZipFile(temp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = new_document_xml
            zout.writestr(item, data)
    temp.replace(docx)


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_heading_rpr_normalization_{timestamp}.docx")
    shutil.copy2(docx, backup)
    with zipfile.ZipFile(docx, "r") as z:
        original_xml = z.read("word/document.xml")
    new_xml, changed_headings, changed_runs = normalize_document_xml(original_xml)
    rewrite_docx(docx, new_xml)

    summary = {
        "status": "HEADING_RPR_NORMALIZED",
        "timestamp": timestamp,
        "docx": str(docx),
        "backup": str(backup),
        "changed_heading_count": len(changed_headings),
        "changed_run_count": changed_runs,
        "changed_heading_sample": changed_headings[:40],
    }
    REPORT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    REPORT_MD.write_text(
        "\n".join(
            [
                "# HEADING_STYLE_CONSISTENCY_FIX_20260525",
                "",
                "Status: `HEADING_RPR_NORMALIZED`",
                f"Timestamp: `{timestamp}`",
                "",
                f"- DOCX: `{docx}`.",
                f"- Backup: `{backup}`.",
                f"- Question headings changed: `{len(changed_headings)}`.",
                f"- Heading runs changed: `{changed_runs}`.",
                "- Change scope: question-heading run properties only; no text, matrix row, source judgment, or placement content was changed.",
                "",
                "## Boundary",
                "",
                "- This fixes structural heading style consistency before re-render QA.",
                "- External GPTPro/Claude Opus review gates remain open.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
