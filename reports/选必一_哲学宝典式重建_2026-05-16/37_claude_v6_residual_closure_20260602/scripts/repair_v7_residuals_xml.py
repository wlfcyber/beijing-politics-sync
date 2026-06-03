from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
ET.register_namespace("w", NS["w"])


def load_helper(path: Path):
    spec = importlib.util.spec_from_file_location("repair_v7_residuals_helper", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load helper: {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def build_changes(entries: list[dict], helper) -> tuple[dict[int, str], list[dict]]:
    changes: dict[int, str] = {}
    log: list[dict] = []

    for rule in helper.DIRECT_RULES:
        hits = [entry for entry in entries if helper.matches(entry, rule)]
        if not hits:
            raise RuntimeError(f"MISS title={rule.get('title')} h3={rule.get('h3','')} field_contains={rule.get('field_contains',{})}")
        if len(hits) > 1 and not rule.get("field_contains") and rule.get("h3") not in {None, ""}:
            h1s = {hit["h1"] for hit in hits}
            if len(h1s) > 1:
                raise RuntimeError(f"AMBIG title={rule.get('title')} h3={rule.get('h3','')} hits={len(hits)} h1s={sorted(h1s)}")

        for entry in hits:
            changed = []
            for label, value in rule["fields"].items():
                if label not in entry["field_para_idx"]:
                    raise RuntimeError(f"NO_FIELD {label} title={entry['entry_title']} h3={entry['h3']}")
                para_idx = entry["field_para_idx"][label]
                text = f"【{label}】 {value}"
                entry["fields"][label] = value
                changes[para_idx] = text
                changed.append(label)
            log.append(
                {
                    "idx": entry.get("idx"),
                    "title": entry["entry_title"],
                    "h1": entry["h1"],
                    "h2": entry["h2"],
                    "h3": entry["h3"],
                    "fields": changed,
                    "kind": "direct",
                }
            )

    for idx, entry in enumerate(entries):
        why = entry["fields"].get("为什么能想到", "")
        if not helper.is_formula_why(why):
            continue
        if "为什么能想到" not in entry["field_para_idx"]:
            continue
        new_why = helper.rewrite_formula_why(entry, idx)
        entry["fields"]["为什么能想到"] = new_why
        para_idx = entry["field_para_idx"]["为什么能想到"]
        changes[para_idx] = f"【为什么能想到】 {new_why}"
        log.append(
            {
                "idx": idx,
                "title": entry["entry_title"],
                "h1": entry["h1"],
                "h2": entry["h2"],
                "h3": entry["h3"],
                "fields": ["为什么能想到"],
                "kind": "formula_rewrite",
            }
        )

    return changes, log


def set_paragraph_text(paragraph, text: str) -> None:
    text_nodes = paragraph.findall(".//w:t", NS)
    if text_nodes:
        text_nodes[0].text = text
        text_nodes[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        for node in text_nodes[1:]:
            node.text = ""
        return

    run = ET.SubElement(paragraph, f"{{{NS['w']}}}r")
    node = ET.SubElement(run, f"{{{NS['w']}}}t")
    node.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    node.text = text


def patch_docx_xml(input_docx: Path, output_docx: Path, changes: dict[int, str]) -> None:
    tmp_docx = output_docx.with_suffix(".tmp.docx")
    shutil.copy2(input_docx, tmp_docx)

    with ZipFile(tmp_docx, "r") as zin:
        document_xml = zin.read("word/document.xml")
        root = ET.fromstring(document_xml)
        body = root.find("w:body", NS)
        if body is None:
            raise RuntimeError("word/document.xml has no body")
        paragraphs = body.findall("w:p", NS)
        max_idx = max(changes) if changes else -1
        if max_idx >= len(paragraphs):
            raise RuntimeError(f"paragraph index {max_idx} >= paragraph count {len(paragraphs)}")

        for idx, text in changes.items():
            set_paragraph_text(paragraphs[idx], text)

        new_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        with ZipFile(output_docx, "w", compression=ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == "word/document.xml":
                    zout.writestr(item, new_xml)
                else:
                    zout.writestr(item, zin.read(item.filename))

    tmp_docx.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_docx", type=Path)
    parser.add_argument("input_entries_json", type=Path)
    parser.add_argument("output_docx", type=Path)
    parser.add_argument("--entries-json", type=Path, required=True)
    parser.add_argument("--log-json", type=Path, required=True)
    parser.add_argument("--helper", type=Path, required=True)
    args = parser.parse_args()

    helper = load_helper(args.helper)
    entries = json.loads(args.input_entries_json.read_text(encoding="utf-8"))
    changes, log = build_changes(entries, helper)
    patch_docx_xml(args.input_docx, args.output_docx, changes)
    args.entries_json.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    args.log_json.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"changes={len(changes)}")
    print(f"direct={sum(1 for x in log if x['kind']=='direct')}")
    print(f"formula_rewrite={sum(1 for x in log if x['kind']=='formula_rewrite')}")


if __name__ == "__main__":
    main()
