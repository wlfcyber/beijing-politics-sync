import csv
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from pypdf import PdfReader
from docx import Document


RUN = Path(__file__).resolve().parents[1]
PRIORITY = sys.argv[1].upper() if len(sys.argv) > 1 else "P0"
OUT = RUN / "fusion" / f"{PRIORITY.lower()}_recheck_sources"
MANIFEST = RUN / "fusion" / "framework_first_fusion" / "RECHECK_MANIFEST_ENRICHED.csv"
SOURCE_LEDGER = RUN / "codex_lane" / "SOURCE_LEDGER.csv"


def safe_name(text):
    return re.sub(r'[<>:"/\\\\|?*\s]+', "_", text).strip("_")[:160]


def source_id_suite_token(source_id):
    tokens = source_id.split("_")
    candidates = [t for t in tokens if re.match(r"20\d{2}.+", t) and "模拟题" not in t and "各区" not in t]
    return candidates[-1] if candidates else ""


def map_source_paths(source_ids):
    with SOURCE_LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
        ledger = list(csv.DictReader(f))
    out = {}
    for sid in source_ids:
        suite = source_id_suite_token(sid)
        candidates = []
        for row in ledger:
            path = row["source_path"]
            if suite and suite not in path:
                continue
            if row.get("suffix", "").lower() != ".pdf":
                continue
            score = 0
            if "试卷" in path:
                score += 5
            if suite and suite in path:
                score += 10
            if "教师版" in path:
                score += 1
            candidates.append((score, path))
        candidates.sort(reverse=True)
        out[sid] = Path(candidates[0][1]) if candidates else None
    return out


def suite_support_files(pdf_path):
    if not pdf_path:
        return []
    suite_dir = pdf_path.parents[1]
    files = []
    for child in suite_dir.rglob("*"):
        if not child.is_file():
            continue
        if child.suffix.lower() in {".pdf", ".pptx", ".docx"} and child != pdf_path:
            files.append(child)
    return sorted(files)


def extract_pdf(path):
    reader = PdfReader(str(path))
    parts = []
    for idx, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:
            text = f"[page extraction failed: {exc}]"
        parts.append(f"\\n\\n===== PAGE {idx} =====\\n{text}")
    return "".join(parts)


def extract_docx(path):
    doc = Document(str(path))
    return "\\n".join(p.text for p in doc.paragraphs if p.text.strip())


def extract_pptx(path):
    ns = {
        "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
        "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    }
    parts = []
    with zipfile.ZipFile(path) as z:
        slides = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)])
        for slide_no, name in enumerate(slides, start=1):
            root = ET.fromstring(z.read(name))
            texts = [node.text for node in root.findall(".//a:t", ns) if node.text]
            if texts:
                parts.append(f"\\n\\n===== SLIDE {slide_no} =====\\n" + "\\n".join(texts))
    return "".join(parts)


def extract_any(path):
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf(path)
    if suffix == ".pptx":
        return extract_pptx(path)
    if suffix == ".docx":
        return extract_docx(path)
    return ""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for stale in OUT.glob("*.txt"):
        stale.unlink()
    old_index = OUT / f"{PRIORITY}_SOURCE_TEXT_INDEX.csv"
    if old_index.exists():
        old_index.unlink()
    rows = [r for r in csv.DictReader(MANIFEST.open("r", encoding="utf-8-sig", newline="")) if r["priority"] == PRIORITY]
    source_ids = sorted({r["source_id"] for r in rows})
    source_map = map_source_paths(source_ids)

    index_rows = []
    for sid, pdf_path in source_map.items():
        if not pdf_path or not pdf_path.exists():
            index_rows.append({"source_id": sid, "kind": "paper", "path": "", "text_path": "", "status": "missing"})
            continue
        paper_text_path = OUT / (safe_name(sid) + "__paper.txt")
        paper_text_path.write_text(extract_any(pdf_path), encoding="utf-8")
        index_rows.append({"source_id": sid, "kind": "paper", "path": str(pdf_path), "text_path": str(paper_text_path), "status": "extracted"})
        for support in suite_support_files(pdf_path):
            text_path = OUT / (safe_name(sid) + "__support__" + safe_name(support.name) + ".txt")
            try:
                text = extract_any(support)
                text_path.write_text(text, encoding="utf-8")
                status = "extracted"
            except Exception as exc:
                text_path.write_text(str(exc), encoding="utf-8")
                status = "extract_failed"
            index_rows.append({"source_id": sid, "kind": "support", "path": str(support), "text_path": str(text_path), "status": status})

    with (OUT / f"{PRIORITY}_SOURCE_TEXT_INDEX.csv").open("w", encoding="utf-8-sig", newline="") as f:
        fields = ["source_id", "kind", "path", "text_path", "status"]
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(index_rows)

    print({"priority": PRIORITY, "source_ids": len(source_ids), "index_rows": len(index_rows), "out": str(OUT)})


if __name__ == "__main__":
    main()
