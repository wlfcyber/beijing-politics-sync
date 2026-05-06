import json
import re
from pathlib import Path

from docx import Document


DOCX = Path("/Users/wanglifei/Desktop/哲学宝典最终版 5.2凌晨.docx")
OUT_DIR = Path("/Users/wanglifei/Desktop/北京高考政治/哲学宝典5.2原地修订/audit")


FIELD_RE = re.compile(r"^【([^】]+)】\s*(.*)$")


def para_style_name(p):
    try:
        return p.style.name or ""
    except Exception:
        return ""


def is_heading(p):
    style = para_style_name(p)
    return style.startswith("Heading") or style in {"Title", "Subtitle"}


def heading_level(p):
    style = para_style_name(p)
    if style.startswith("Heading"):
        m = re.search(r"(\d+)", style)
        if m:
            return int(m.group(1))
    if style == "Title":
        return 0
    return None


def para_has_image(p):
    return bool(p._p.xpath(".//w:drawing"))


def extract():
    doc = Document(DOCX)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    paragraphs = []
    for idx, p in enumerate(doc.paragraphs):
        text = p.text.strip()
        paragraphs.append(
            {
                "idx": idx,
                "text": text,
                "style": para_style_name(p),
                "heading_level": heading_level(p),
                "has_image": para_has_image(p),
            }
        )

    entries = []
    current_module = ""
    current_node = ""
    current = None
    seen_first_entry = False
    for item in paragraphs:
        text = item["text"]
        if not text and not item["has_image"]:
            continue
        level = item["heading_level"]
        if level == 1:
            current_module = text
            current_node = ""
            current = None
            continue
        if level == 2:
            current_node = text
            current = None
            continue
        if level == 3:
            current = {
                "start_para": item["idx"],
                "heading": text,
                "module": current_module,
                "node": current_node,
                "fields": {},
                "images": [],
                "raw": [],
            }
            entries.append(current)
            seen_first_entry = True
            continue
        if current and seen_first_entry:
            if item["has_image"]:
                current["images"].append(item["idx"])
            if text:
                current["raw"].append({"idx": item["idx"], "text": text, "style": item["style"]})
                m = FIELD_RE.match(text)
                if m:
                    current["fields"][m.group(1)] = m.group(2).strip()

    # Include the paragraph index where the next entry starts for easier surgery.
    for i, entry in enumerate(entries):
        entry["end_para_exclusive"] = entries[i + 1]["start_para"] if i + 1 < len(entries) else len(paragraphs)

    summary = {
        "docx": str(DOCX),
        "paragraph_count": len(paragraphs),
        "entry_count": len(entries),
        "modules": {},
    }
    for e in entries:
        summary["modules"].setdefault(e["module"], {}).setdefault(e["node"], 0)
        summary["modules"][e["module"]][e["node"]] += 1

    (OUT_DIR / "docx_paragraphs.json").write_text(json.dumps(paragraphs, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "docx_entries.json").write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "docx_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = ["# 哲学宝典5.2当前 Word 抽取稿", ""]
    for module, nodes in summary["modules"].items():
        md.append(f"## {module}")
        for node, count in nodes.items():
            md.append(f"- {node}: {count}")
        md.append("")
    for e in entries:
        md.append(f"## {e['module']} / {e['node']}")
        md.append(f"### {e['heading']}")
        for k in ["材料触发点", "设问", "为什么能想到", "答案落点"]:
            md.append(f"【{k}】 {e['fields'].get(k, '')}")
        if e["images"]:
            md.append(f"【图片段落】 {e['images']}")
        md.append("")
    (OUT_DIR / "当前Word抽取稿.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    extract()
