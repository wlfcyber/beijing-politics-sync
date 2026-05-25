from __future__ import annotations

import json
import re
import shutil
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
REPORT_MD = RECOVERY / "HEADING_STYLE_CONSISTENCY_FIX_DOCXAPI_20260525.md"
REPORT_JSON = RECOVERY / "HEADING_STYLE_CONSISTENCY_FIX_DOCXAPI_20260525.json"
QUESTION_HEADING_RE = re.compile(r"^\s*\d+\.\s*20(?:24|25|26).+第.+题")


def current_docx() -> Path:
    files = [
        p
        for p in DELIVERY.glob("*.docx")
        if not p.name.startswith("~$") and "_backup_" not in p.stem
    ]
    if len(files) != 1:
        raise RuntimeError(f"Expected one current docx, got {files}")
    return files[0]


def ensure_lang_only(run) -> bool:
    r = run._r
    existing = r.rPr
    if existing is not None:
        existing_xml = existing.xml
        lang = existing.find(qn("w:lang"))
        if (
            lang is not None
            and lang.get(qn("w:eastAsia")) == "zh-CN"
            and len(existing) == 1
        ):
            return False
        r.remove(existing)
    rpr = OxmlElement("w:rPr")
    lang = OxmlElement("w:lang")
    lang.set(qn("w:eastAsia"), "zh-CN")
    rpr.append(lang)
    r.insert(0, rpr)
    return True


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_heading_rpr_docxapi_{timestamp}.docx")
    shutil.copy2(docx, backup)

    document = Document(docx)
    changed_headings: list[str] = []
    changed_runs = 0
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        if not QUESTION_HEADING_RE.match(text):
            continue
        changed_this = False
        for run in paragraph.runs:
            if ensure_lang_only(run):
                changed_runs += 1
                changed_this = True
        if changed_this:
            changed_headings.append(text)
    document.save(docx)

    summary = {
        "status": "HEADING_RPR_NORMALIZED_DOCXAPI",
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
                "# HEADING_STYLE_CONSISTENCY_FIX_DOCXAPI_20260525",
                "",
                "Status: `HEADING_RPR_NORMALIZED_DOCXAPI`",
                f"Timestamp: `{timestamp}`",
                "",
                f"- DOCX: `{docx}`.",
                f"- Backup: `{backup}`.",
                f"- Question headings changed: `{len(changed_headings)}`.",
                f"- Heading runs changed: `{changed_runs}`.",
                "- Change scope: question-heading run properties only; no visible text, matrix row, source judgment, or placement content was changed.",
                "- Prior raw-XML attempt was rolled back to its automatic backup before this Word-compatible DOCX API patch.",
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
