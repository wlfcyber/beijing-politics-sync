from __future__ import annotations

import json
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


BASE_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1终极版_回源漏项修正最终交付_带水印_20260603.docx")
ROUND34_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1终极版_第34轮核心答题点红色强调_带水印_20260603.docx")
FINAL_DOCX = Path("/Users/wanglifei/Desktop/选必一6.1终极版_回源漏项修正最终交付_核心答题点红色强调_带水印_20260603.docx")
REPORT = Path(__file__).with_name("round34_core_heading_red_report.json")

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}


def qn(tag: str) -> str:
    return f"{{{W_NS}}}{tag}"


def paragraph_text(p: ET.Element) -> str:
    return "".join((t.text or "") for t in p.findall(".//w:t", NS))


def ensure(parent: ET.Element, child_name: str, *, first: bool = False) -> ET.Element:
    existing = parent.find(f"w:{child_name}", NS)
    if existing is not None:
        return existing
    child = ET.Element(qn(child_name))
    if first:
        parent.insert(0, child)
    else:
        parent.append(child)
    return child


def set_run_emphasis(run: ET.Element) -> None:
    rpr = ensure(run, "rPr", first=True)
    bold = ensure(rpr, "b")
    bold.set(qn("val"), "1")
    color = ensure(rpr, "color")
    color.set(qn("val"), "C00000")


def set_paragraph_emphasis(p: ET.Element) -> None:
    ppr = ensure(p, "pPr", first=True)
    rpr = ensure(ppr, "rPr")
    bold = ensure(rpr, "b")
    bold.set(qn("val"), "1")
    color = ensure(rpr, "color")
    color.set(qn("val"), "C00000")
    for run in p.findall(".//w:r", NS):
        set_run_emphasis(run)


def patch_docx(src: Path, dst: Path) -> dict:
    if not src.exists():
        raise FileNotFoundError(src)

    shutil.copy2(src, dst)
    with zipfile.ZipFile(dst, "r") as zin:
        entries = {info.filename: zin.read(info.filename) for info in zin.infolist()}

    document_xml = entries["word/document.xml"]
    root = ET.fromstring(document_xml)
    changed = 0
    targets: list[str] = []

    for p in root.findall(".//w:p", NS):
        text = paragraph_text(p).strip()
        if text.startswith("核心答题点："):
            set_paragraph_emphasis(p)
            changed += 1
            targets.append(text)

    entries["word/document.xml"] = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    with zipfile.ZipFile(dst, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in entries.items():
            zout.writestr(name, data)

    return {
        "source": str(src),
        "output": str(dst),
        "changed_core_headings": changed,
        "first_targets": targets[:10],
        "last_targets": targets[-5:],
    }


def main() -> None:
    report = patch_docx(BASE_DOCX, ROUND34_DOCX)
    shutil.copy2(ROUND34_DOCX, FINAL_DOCX)
    report["final_copy"] = str(FINAL_DOCX)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
