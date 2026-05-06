#!/usr/bin/env python3
import csv
import re
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from pypdf import PdfReader

RUN_DIR = Path(__file__).resolve().parents[2]
LEDGER = RUN_DIR / "SOURCE_LEDGER.csv"
EXTRACT_DIR = RUN_DIR / "codex_lane" / "extracted_text"
MEDIA_DIR = RUN_DIR / "codex_lane" / "extracted_media"
REPORT = RUN_DIR / "codex_lane" / "priority_source_extract_report.md"

PRIORITY_SOURCE_IDS = [
    "SRC_1f17f2c91d92",  # 2024东城一模 细则.pptx
    "SRC_fa4ea186dba9",  # 2024东城一模 答案 PDF
    "SRC_35ef9424281a",  # 2026通州期末 细则.pptx
    "SRC_763b7470b96b",  # 2026朝阳期中 细则.docx
    "SRC_1babd6c525fe",  # 2026朝阳期中 补充细则.docx
    "SRC_cda046c2d36d",  # 2025海淀期中 细则.docx
    "SRC_61b68f14212d",  # 2025海淀期末 细则.pptx
    "SRC_93d2077755f7",  # 2026海淀期末 细则.pdf
    "SRC_7324e07095f8",  # 2026石景山期末 答案及评分参考.pdf
]

KEYWORDS = [
    "当代国际政治与经济",
    "国际政治与经济",
    "经济全球化",
    "世界多极化",
    "政治多极化",
    "和平与发展",
    "共同利益",
    "国家利益",
    "全球治理",
    "联合国",
    "中国智慧",
    "中国方案",
    "中国担当",
    "人类命运共同体",
    "多边主义",
    "国际关系民主化",
    "新型国际关系",
    "贸易",
    "投资",
    "制度型开放",
    "两个市场",
    "两种资源",
]


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def xml_text(blob: bytes) -> str:
    try:
        root = ET.fromstring(blob)
    except ET.ParseError:
        return ""
    chunks = []
    for elem in root.iter():
        if elem.text and elem.tag.endswith("}t"):
            chunks.append(elem.text)
    return clean_text(" ".join(chunks))


def extract_docx(path: Path, source_id: str) -> tuple[str, list[str]]:
    texts = []
    media_notes = []
    media_out = MEDIA_DIR / source_id
    with zipfile.ZipFile(path) as z:
        xml_names = [
            n
            for n in z.namelist()
            if n.startswith("word/")
            and n.endswith(".xml")
            and (
                n == "word/document.xml"
                or n.startswith("word/header")
                or n.startswith("word/footer")
                or n.startswith("word/footnotes")
                or n.startswith("word/endnotes")
            )
        ]
        for name in sorted(xml_names):
            text = xml_text(z.read(name))
            if text:
                texts.append(f"\n## {name}\n{text}")
        media_names = [n for n in z.namelist() if n.startswith("word/media/")]
        if media_names:
            media_out.mkdir(parents=True, exist_ok=True)
            for name in media_names:
                target = media_out / Path(name).name
                with z.open(name) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)
            media_notes.append(f"embedded_media={len(media_names)} saved_to={media_out}")
    return "\n".join(texts).strip(), media_notes


def extract_pptx(path: Path) -> tuple[str, list[str]]:
    texts = []
    with zipfile.ZipFile(path) as z:
        slide_names = sorted(
            [n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")],
            key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)),
        )
        for name in slide_names:
            slide_no = re.search(r"slide(\d+)\.xml", name).group(1)
            text = xml_text(z.read(name))
            if text:
                texts.append(f"\n## slide {slide_no}\n{text}")
        note_names = sorted(
            [n for n in z.namelist() if n.startswith("ppt/notesSlides/notesSlide") and n.endswith(".xml")]
        )
        for name in note_names:
            note_no = re.search(r"notesSlide(\d+)\.xml", name).group(1)
            text = xml_text(z.read(name))
            if text:
                texts.append(f"\n## notes {note_no}\n{text}")
    return "\n".join(texts).strip(), []


def extract_pdf(path: Path) -> tuple[str, list[str]]:
    notes = []
    chunks = []
    try:
        reader = PdfReader(str(path))
        for idx, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ""
            text = clean_text(text)
            if text:
                chunks.append(f"\n## page {idx}\n{text}")
    except Exception as exc:
        notes.append(f"pdf_extract_error={type(exc).__name__}:{exc}")
    if not chunks:
        notes.append("needs_visual_read_or_ocr=true")
    return "\n".join(chunks).strip(), notes


def extract_any(row: dict) -> tuple[str, list[str]]:
    path = Path(row["path"])
    ext = path.suffix.lower()
    if ext == ".docx":
        return extract_docx(path, row["source_id"])
    if ext == ".pptx":
        return extract_pptx(path)
    if ext == ".pdf":
        return extract_pdf(path)
    return "", [f"unsupported_priority_ext={ext}"]


def keyword_hits(text: str) -> dict[str, int]:
    return {kw: text.count(kw) for kw in KEYWORDS if kw in text}


def excerpts(text: str) -> list[str]:
    hits = []
    compact = re.sub(r"\s+", " ", text)
    for kw in KEYWORDS:
        start = compact.find(kw)
        if start == -1:
            continue
        lo = max(0, start - 90)
        hi = min(len(compact), start + len(kw) + 120)
        hits.append(compact[lo:hi])
        if len(hits) >= 8:
            break
    return hits


def main() -> None:
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)

    with LEDGER.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    by_id = {row["source_id"]: row for row in rows}
    report_items = []

    for source_id in PRIORITY_SOURCE_IDS:
        row = by_id[source_id]
        text, notes = extract_any(row)
        out_name = f"{source_id}_{Path(row['path']).stem}.txt"
        out_path = EXTRACT_DIR / out_name
        out_path.write_text(text, encoding="utf-8")
        hits = keyword_hits(text)
        chars = len(text)

        if row["file_type"] == "pdf" and not text:
            row["status"] = "needs_visual_read"
        elif chars > 0:
            row["status"] = "source_checked"
        else:
            row["status"] = "blocked_source"

        row["extraction_method"] = {
            "docx": "zip_word_xml",
            "pptx": "zip_pptx_xml",
            "pdf": "pypdf_text_attempt",
        }.get(row["file_type"], row["extraction_method"])
        note_bits = [n for n in [row.get("notes", "")] if n]
        note_bits.extend(notes)
        if hits:
            note_bits.append("keyword_hits=" + ";".join(f"{k}:{v}" for k, v in hits.items()))
        row["notes"] = " | ".join(note_bits)

        report_items.append(
            {
                "row": row,
                "out_path": out_path,
                "chars": chars,
                "hits": hits,
                "notes": notes,
                "excerpts": excerpts(text),
            }
        )

    with LEDGER.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    with REPORT.open("w", encoding="utf-8") as f:
        f.write("# Priority Source Extract Report\n\n")
        f.write("| source_id | suite | file | status | chars | keyword hits | notes |\n")
        f.write("|---|---|---|---:|---:|---|---|\n")
        for item in report_items:
            row = item["row"]
            hits = "; ".join(f"{k}:{v}" for k, v in item["hits"].items()) or "-"
            notes = "; ".join(item["notes"]) or "-"
            f.write(
                f"| {row['source_id']} | {row['suite']} | {Path(row['path']).name} | "
                f"{row['status']} | {item['chars']} | {hits} | {notes} |\n"
            )
        for item in report_items:
            row = item["row"]
            f.write(f"\n## {row['suite']} - {Path(row['path']).name}\n\n")
            f.write(f"- source_id: `{row['source_id']}`\n")
            f.write(f"- extracted_text: `{item['out_path']}`\n")
            if item["excerpts"]:
                f.write("- excerpts:\n")
                for ex in item["excerpts"]:
                    f.write(f"  - {ex}\n")
            else:
                f.write("- excerpts: none; needs visual/OCR if source remains relevant.\n")

    print(f"wrote {REPORT}")
    print(f"processed {len(report_items)} priority sources")


if __name__ == "__main__":
    main()
