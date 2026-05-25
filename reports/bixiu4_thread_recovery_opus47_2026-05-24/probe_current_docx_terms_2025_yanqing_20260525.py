from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent
DELIVERY = ROOT.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24" / "05_delivery"
DOCX = next(p for p in DELIVERY.iterdir() if p.suffix.lower() == ".docx" and "backup" not in p.name)
OUT = ROOT / "CURRENT_DOCX_2025_YANQING_PROBE_20260525.md"

TERMS = [
    "2025延庆一模",
    "延庆一模",
    "中老年题材微短剧",
    "网络文艺作品的创作",
    "银发力量",
    "一切从实际出发",
    "中老年人",
    "低空经济",
    "产业链供应链",
    "人民群众",
    "社会主义核心价值观",
    "文化自信",
]


def paragraphs() -> list[str]:
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with ZipFile(DOCX) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    items: list[str] = []
    for p in root.findall(".//w:p", ns):
        text = "".join(t.text or "" for t in p.findall(".//w:t", ns))
        if text.strip():
            items.append(text.strip())
    return items


def main() -> None:
    paras = paragraphs()
    lines = [
        "# Current DOCX Probe - 2025 Yanqing Yimo",
        "",
        f"- DOCX: `{DOCX}`",
        f"- Paragraphs scanned: `{len(paras)}`",
        "",
        "## Term Hits",
        "",
    ]
    for term in TERMS:
        hits = [(i, text) for i, text in enumerate(paras) if term in text]
        lines.append(f"### {term}")
        lines.append(f"- hits: `{len(hits)}`")
        for idx, text in hits[:12]:
            safe = text.replace("|", "｜")
            lines.append(f"- `{idx}`: {safe[:500]}")
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
