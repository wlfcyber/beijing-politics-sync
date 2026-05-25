from __future__ import annotations

import csv
import json
import shutil
import tempfile
import zipfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from lxml import etree

import repair_2026_fangshan_ermo_candidate_queue_20260525 as base


ENTRY = dict(base.INSERT_ENTRIES[2])
ENTRY["heading_suffix"] = "2026房山二模 第21题（主观题·矛盾普遍性角度）"


def insert_entry(ts: str) -> str | None:
    docx = base.current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_2026_fangshan_q21_contradiction_{ts}.docx")
    shutil.copy2(docx, backup)
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        with zipfile.ZipFile(docx) as zin:
            zin.extractall(temp)
        xml_path = temp / "word" / "document.xml"
        tree = etree.parse(str(xml_path))
        body = tree.getroot().find("w:body", namespaces=base.NS)
        if body is None:
            raise RuntimeError("missing body")
        heading = base.add_entry(body, ENTRY)
        tree.write(str(xml_path), encoding="utf-8", xml_declaration=True, standalone=True)
        with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as zout:
            for path in temp.rglob("*"):
                if path.is_file():
                    zout.write(path, path.relative_to(temp).as_posix())
    return heading


def update_ledger(ts: str, heading: str | None) -> dict[str, object]:
    backup = base.LEDGER.with_name(f"{base.LEDGER.stem}_backup_before_2026_fangshan_q21_contradiction_{ts}{base.LEDGER.suffix}")
    shutil.copy2(base.LEDGER, backup)
    if heading is None:
        return {"ledger": str(base.LEDGER), "ledger_backup": str(backup), "added_rows": []}
    with base.LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or ["canonical_node", "source_suite", "question_no", "inserted_heading"]
        rows = list(reader)
    clean = heading.split(". ", 1)[1]
    existing = {(r.get("source_suite"), r.get("question_no"), r.get("inserted_heading")) for r in rows}
    added = []
    key = (base.SUITE, ENTRY["question_no"], clean)
    if key not in existing:
        row = {field: "" for field in fieldnames}
        row.update(
            {
                "canonical_node": ENTRY["canonical_node"],
                "source_suite": base.SUITE,
                "question_no": ENTRY["question_no"],
                "inserted_heading": clean,
            }
        )
        rows.append(row)
        added.append(row)
    with base.LEDGER.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return {"ledger": str(base.LEDGER), "ledger_backup": str(backup), "added_rows": added}


def update_report(heading: str | None, ledger_result: dict[str, object]) -> None:
    data = json.loads(base.REPORT_JSON.read_text(encoding="utf-8"))
    data.setdefault("docx", {}).setdefault("inserted_headings", [])
    if heading and heading not in data["docx"]["inserted_headings"]:
        data["docx"]["inserted_headings"].append(heading)
    data["ledger_q21_contradiction"] = ledger_result
    base.REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    text = base.REPORT_MD.read_text(encoding="utf-8")
    if heading and f"`{heading}`" not in text:
        marker = "## Matrix Closure"
        text = text.replace(marker, f"- `{heading}`\n\n{marker}")
    text = text.replace(
        "- Q21 inserted under `人民群众` and `矛盾的普遍性` using formal comprehensive-question angle evidence and level descriptors.",
        "- Q21 inserted under `人民群众` and `矛盾的普遍性` using formal comprehensive-question angle evidence and level descriptors.",
    )
    base.REPORT_MD.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    heading = insert_entry(ts)
    ledger_result = update_ledger(ts, heading)
    update_report(heading, ledger_result)
    print(json.dumps({"inserted_heading": heading, "ledger": ledger_result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
