from __future__ import annotations

import json
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

from lxml import etree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{W_NS}}}"
NS = {"w": W_NS}

RECOVERY = Path(__file__).resolve().parent
RUN_DIR = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN_DIR / "05_delivery"
ACCEPTED = RUN_DIR / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"

OLD = "“良法”强调制度规范，“善治”强调治理成效；材料说良法是起点、善治是目标。材料把两个看似有张力的方面放在同一问题中呈现，例如保护与利用、传承与创新、历史与现代、局部差异与整体目标，要求在关系中理解双方。"
NEW = "“良法”强调制度规范和立法起点，“善治”强调治理成效和目标实现；材料说良法只是起点、善治才是目标，说明二者有区别又统一于同一法治建设过程。良法为善治提供规范基础，善治检验并实现良法价值，必须在二者关系中理解双方。"


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


def replace_text_in_para(p: ET.Element, old: str, new: str) -> bool:
    full = para_text(p)
    if old not in full:
        return False
    replaced = full.replace(old, new)
    runs = p.findall("./w:r", NS)
    if not runs:
        raise SystemExit("target paragraph has no runs")
    first_text = None
    for r in runs:
        t = r.find("./w:t", NS)
        if t is not None:
            first_text = t
            break
    if first_text is None:
        raise SystemExit("target paragraph has no text run")
    first_text.text = replaced
    seen_first = False
    for r in runs:
        for t in r.findall("./w:t", NS):
            if t is first_text and not seen_first:
                seen_first = True
                continue
            t.text = ""
    return True


def patch_jsonl(timestamp: str) -> int:
    backup = ACCEPTED.with_name(f"{ACCEPTED.stem}_backup_before_row35_material_fix_{timestamp}{ACCEPTED.suffix}")
    shutil.copy2(ACCEPTED, backup)
    rows = []
    count = 0
    for line in ACCEPTED.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if (
            row.get("source_suite") == "2026石景山二模"
            and row.get("question_no") == "Q17(3)"
            and row.get("framework_node") == "矛盾就是对立统一"
        ):
            if row.get("material_trigger") != OLD:
                raise SystemExit("row35 material_trigger did not match expected old text")
            row["material_trigger"] = NEW
            count += 1
        rows.append(row)
    ACCEPTED.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
    return count


def patch_docx(timestamp: str) -> int:
    docx = current_docx()
    backup = docx.with_name(f"{docx.stem}_backup_before_row35_material_fix_{timestamp}{docx.suffix}")
    shutil.copy2(docx, backup)

    with zipfile.ZipFile(docx, "r") as zin:
        document_xml = zin.read("word/document.xml")
        all_items = [(item, zin.read(item.filename)) for item in zin.infolist()]

    parser = ET.XMLParser(remove_blank_text=False, resolve_entities=False)
    root = ET.fromstring(document_xml, parser=parser)
    hits = 0
    for p in root.findall(".//w:body/w:p", NS):
        if replace_text_in_para(p, OLD, NEW):
            hits += 1

    if hits != 1:
        raise SystemExit(f"expected exactly 1 DOCX paragraph replacement, got {hits}")

    new_document_xml = ET.tostring(root, encoding="UTF-8", xml_declaration=True, standalone=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)

    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for item, data in all_items:
            zout.writestr(item, new_document_xml if item.filename == "word/document.xml" else data)
    shutil.move(str(tmp_path), docx)
    return hits


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    jsonl_count = patch_jsonl(timestamp)
    docx_count = patch_docx(timestamp)
    print(f"accepted_jsonl_replacements={jsonl_count}")
    print(f"docx_replacements={docx_count}")
    print(f"replacement={NEW}")


if __name__ == "__main__":
    main()
