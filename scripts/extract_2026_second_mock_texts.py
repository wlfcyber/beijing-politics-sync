from __future__ import annotations

import argparse
import csv
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from docx import Document
from pypdf import PdfReader


TEXT_EXTS = {".txt", ".md"}
SUPPORTED_EXTS = {".docx", ".pdf", ".pptx", ".txt", ".md"}


def safe_name(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    name = "__".join(rel.parts)
    name = re.sub(r'[<>:"/\\|?*\s]+', "_", name)
    return name


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + ("\n" if text.strip() else "")


def extract_docx(path: Path) -> str:
    doc = Document(str(path))
    parts: list[str] = []
    for p in doc.paragraphs:
        if p.text.strip():
            parts.append(p.text.strip())
    for table_idx, table in enumerate(doc.tables, 1):
        parts.append(f"\n[表格 {table_idx}]")
        for row in table.rows:
            cells = [cell.text.strip().replace("\n", " / ") for cell in row.cells]
            if any(cells):
                parts.append(" | ".join(cells))
    return clean_text("\n".join(parts))


def extract_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    parts: list[str] = []
    for idx, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:  # noqa: BLE001
            text = f"[PDF page extraction error: {exc}]"
        parts.append(f"\n--- PAGE {idx} ---\n{text}")
    return clean_text("\n".join(parts))


def extract_pptx(path: Path) -> str:
    # Avoid requiring python-pptx. Read slide XML text boxes directly.
    ns = {
        "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
        "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    }
    parts: list[str] = []
    with zipfile.ZipFile(path) as zf:
        slide_names = sorted(
            [n for n in zf.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)],
            key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)),  # type: ignore[union-attr]
        )
        for slide_name in slide_names:
            slide_no = int(re.search(r"slide(\d+)\.xml", slide_name).group(1))  # type: ignore[union-attr]
            root = ET.fromstring(zf.read(slide_name))
            texts = [node.text for node in root.findall(".//a:t", ns) if node.text]
            if texts:
                parts.append(f"\n--- SLIDE {slide_no} ---\n" + "\n".join(texts))
    return clean_text("\n".join(parts))


def extract_text(path: Path) -> tuple[str, str]:
    ext = path.suffix.lower()
    if ext == ".docx":
        return extract_docx(path), "docx"
    if ext == ".pdf":
        return extract_pdf(path), "pdf"
    if ext == ".pptx":
        return extract_pptx(path), "pptx"
    if ext in TEXT_EXTS:
        for enc in ("utf-8-sig", "utf-8", "gb18030"):
            try:
                return clean_text(path.read_text(encoding=enc)), f"text:{enc}"
            except UnicodeDecodeError:
                continue
        return clean_text(path.read_text(encoding="utf-8", errors="replace")), "text:replace"
    raise ValueError(f"unsupported extension: {path.suffix}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    out_dir = args.out_dir.resolve()
    text_dir = out_dir / "texts"
    text_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    for path in sorted(source_root.rglob("*")):
        if not path.is_file():
            continue
        ext = path.suffix.lower()
        if ext not in SUPPORTED_EXTS:
            rows.append(
                {
                    "status": "skipped",
                    "extractor": "",
                    "chars": "0",
                    "lines": "0",
                    "source": str(path),
                    "text_path": "",
                    "error": f"unsupported extension {path.suffix}",
                }
            )
            continue
        out_path = text_dir / f"{safe_name(path, source_root)}.txt"
        try:
            text, extractor = extract_text(path)
            out_path.write_text(text, encoding="utf-8")
            rows.append(
                {
                    "status": "ok",
                    "extractor": extractor,
                    "chars": str(len(text)),
                    "lines": str(text.count("\n") + (1 if text else 0)),
                    "source": str(path),
                    "text_path": str(out_path),
                    "error": "",
                }
            )
        except Exception as exc:  # noqa: BLE001
            rows.append(
                {
                    "status": "error",
                    "extractor": "",
                    "chars": "0",
                    "lines": "0",
                    "source": str(path),
                    "text_path": str(out_path),
                    "error": repr(exc),
                }
            )

    manifest = out_dir / "manifest.csv"
    with manifest.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["status", "extractor", "chars", "lines", "source", "text_path", "error"]
        )
        writer.writeheader()
        writer.writerows(rows)

    ok = sum(1 for r in rows if r["status"] == "ok")
    errors = sum(1 for r in rows if r["status"] == "error")
    skipped = sum(1 for r in rows if r["status"] == "skipped")
    print(f"manifest={manifest}")
    print(f"ok={ok} errors={errors} skipped={skipped}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
