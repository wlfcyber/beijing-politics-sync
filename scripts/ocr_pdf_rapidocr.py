from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

import fitz
from rapidocr_onnxruntime import RapidOCR


def page_lines(ocr_result):
    if not ocr_result:
        return []
    rows = []
    for item in ocr_result:
        box, text, score = item
        if not text:
            continue
        y = sum(point[1] for point in box) / 4
        x = sum(point[0] for point in box) / 4
        rows.append((y, x, text.strip(), float(score)))
    rows.sort(key=lambda r: (r[0], r[1]))
    return rows


def ocr_pdf(pdf_path: Path, out_txt: Path, dpi: int) -> dict:
    out_txt.parent.mkdir(parents=True, exist_ok=True)
    ocr = RapidOCR()
    doc = fitz.open(str(pdf_path))
    meta = {"source": str(pdf_path), "pages": doc.page_count, "dpi": dpi, "page_items": []}
    blocks = []
    for page_index, page in enumerate(doc, start=1):
        pix = page.get_pixmap(dpi=dpi, alpha=False)
        fd, tmp_name = tempfile.mkstemp(suffix=".png")
        os.close(fd)
        try:
            pix.save(tmp_name)
            result, elapsed = ocr(tmp_name)
            rows = page_lines(result)
            meta["page_items"].append(
                {"page": page_index, "items": len(rows), "elapsed": elapsed}
            )
            blocks.append(f"--- PAGE {page_index} OCR ---")
            blocks.extend(text for _, _, text, _ in rows)
        finally:
            try:
                os.remove(tmp_name)
            except OSError:
                pass
    doc.close()
    out_txt.write_text("\n".join(blocks), encoding="utf-8")
    return meta


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--dpi", type=int, default=220)
    args = parser.parse_args()
    meta = ocr_pdf(Path(args.pdf), Path(args.out), args.dpi)
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
