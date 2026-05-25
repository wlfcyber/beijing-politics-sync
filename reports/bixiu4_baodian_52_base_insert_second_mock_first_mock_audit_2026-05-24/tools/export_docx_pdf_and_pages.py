# -*- coding: utf-8 -*-
from __future__ import annotations

from pathlib import Path

import fitz  # PyMuPDF
import win32com.client
from PIL import Image, ImageDraw


RUN = Path(__file__).resolve().parents[1]
DELIVERY = RUN / "05_delivery"
RENDER = RUN / "07_render_check" / "word_pdf_pages"
RENDER.mkdir(parents=True, exist_ok=True)


def export_pdf(docx_path: Path, pdf_path: Path) -> None:
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = None
    try:
        doc = word.Documents.Open(str(docx_path.resolve()))
        try:
            doc.Fields.Update()
            doc.TablesOfContents(1).Update()
        except Exception:
            pass
        doc.ExportAsFixedFormat(str(pdf_path.resolve()), 17)
    finally:
        if doc is not None:
            doc.Close(False)
        word.Quit()


def render_pdf_pages(pdf_path: Path) -> int:
    for old_png in RENDER.glob("*.png"):
        old_png.unlink()
    pdf = fitz.open(pdf_path)
    zoom = 120 / 72
    matrix = fitz.Matrix(zoom, zoom)
    for i, page in enumerate(pdf):
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        pix.save(RENDER / f"page_{i + 1:03d}.png")
    count = len(pdf)
    pdf.close()
    return count


def make_contact_sheet(page_count: int, every: int = 12) -> None:
    thumbs = []
    for i in range(1, page_count + 1, every):
        path = RENDER / f"page_{i:03d}.png"
        if not path.exists():
            continue
        img = Image.open(path).convert("RGB")
        img.thumbnail((260, 340))
        canvas = Image.new("RGB", (280, 380), "white")
        x = (280 - img.width) // 2
        canvas.paste(img, (x, 20))
        draw = ImageDraw.Draw(canvas)
        draw.text((12, 350), f"page {i}", fill=(0, 0, 0))
        thumbs.append(canvas)
    if not thumbs:
        return
    cols = 4
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 280, rows * 380), "white")
    for idx, img in enumerate(thumbs):
        sheet.paste(img, ((idx % cols) * 280, (idx // cols) * 380))
    sheet.save(RENDER / "contact_every_12_pages.png")


def main() -> int:
    candidates = [
        p
        for p in DELIVERY.glob("*.docx")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
    if len(candidates) != 1:
        raise RuntimeError(f"Expected exactly one current DOCX, found {len(candidates)}: {candidates}")
    docx = candidates[0]
    pdf = DELIVERY / (docx.stem + ".pdf")
    export_pdf(docx, pdf)
    page_count = render_pdf_pages(pdf)
    make_contact_sheet(page_count)
    print(docx)
    print(pdf)
    print(RENDER)
    print(page_count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
