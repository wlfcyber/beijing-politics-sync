#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from pathlib import Path


RUN = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531")
MANIFEST = RUN / "01_inputs" / "EXTRACTED_SOURCE_MANIFEST.csv"
OCR_ROOT = RUN / "01_inputs" / "ocr_vision"
FINAL_DIR = RUN / "01_inputs" / "source_texts_final"
FINAL_MANIFEST = RUN / "01_inputs" / "FINAL_SOURCE_TEXT_MANIFEST.csv"


def find_ocr(source_id):
    d = OCR_ROOT / source_id
    if not d.exists():
        return ""
    files = sorted(d.glob("*.ocr.txt"))
    return str(files[0]) if files else ""


def main():
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8-sig")))
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    out_rows = []
    for row in rows:
        original_text = Path(row["text_path"]).read_text(encoding="utf-8")
        ocr_path = find_ocr(row["source_id"])
        if ocr_path:
            ocr_text = Path(ocr_path).read_text(encoding="utf-8")
            final_text = f"{original_text}\n\n===== VISION OCR =====\n\n{ocr_text}"
            final_status = "TEXT_PLUS_OCR"
        else:
            final_text = original_text
            final_status = "TEXT_ONLY"
        final_path = FINAL_DIR / Path(row["text_path"]).name
        final_path.write_text(final_text, encoding="utf-8")
        out_rows.append({
            **row,
            "ocr_text_path": ocr_path,
            "final_status": final_status,
            "final_char_count": len(final_text.strip()),
            "final_text_path": str(final_path),
        })
    with FINAL_MANIFEST.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)
    print("final_sources", len(out_rows), "with_ocr", sum(1 for r in out_rows if r["ocr_text_path"]))


if __name__ == "__main__":
    main()
