#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

import fitz


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
PDF_DIR = ROOT / "00_source_pdfs"
OUT_DIR = ROOT / "02_extraction" / "framework_pdfs"
TEXT_DIR = OUT_DIR / "text"
RENDER_DIR = OUT_DIR / "renders"


def safe_stem(path: Path) -> str:
    return path.stem.replace(" ", "_")


def extract_one(pdf_path: Path) -> dict:
    doc = fitz.open(pdf_path)
    stem = safe_stem(pdf_path)
    text_path = TEXT_DIR / f"{stem}.txt"
    pages_jsonl = TEXT_DIR / f"{stem}.pages.jsonl"
    render_subdir = RENDER_DIR / stem
    render_subdir.mkdir(parents=True, exist_ok=True)

    full_chunks: list[str] = []
    page_rows: list[dict] = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text("text") or ""
        full_chunks.append(f"===== PAGE {i} =====\n{text.rstrip()}\n")
        page_rows.append(
            {
                "page": i,
                "char_count": len(text),
                "text_preview": text.replace("\n", " ")[:160],
            }
        )
        # Render every page at moderate resolution so visual/diagram/table pages can be checked.
        pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
        pix.save(render_subdir / f"page_{i:02d}.png")

    text_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.write_text("\n".join(full_chunks), encoding="utf-8")
    with pages_jsonl.open("w", encoding="utf-8") as f:
        for row in page_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    return {
        "source_pdf": str(pdf_path),
        "pages": len(doc),
        "total_chars": sum(row["char_count"] for row in page_rows),
        "text_path": str(text_path),
        "pages_jsonl": str(pages_jsonl),
        "render_dir": str(render_subdir),
    }


def main() -> None:
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    rows = [extract_one(path) for path in sorted(PDF_DIR.glob("*.pdf"))]
    manifest = OUT_DIR / "framework_pdf_manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "source_pdf",
                "pages",
                "total_chars",
                "text_path",
                "pages_jsonl",
                "render_dir",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {manifest}")
    for row in rows:
        print(f"{Path(row['source_pdf']).name}: pages={row['pages']} chars={row['total_chars']}")


if __name__ == "__main__":
    main()
