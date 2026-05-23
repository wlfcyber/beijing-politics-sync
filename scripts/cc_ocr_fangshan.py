#!/usr/bin/env python3
"""OCR 房山二模 试卷 PDF (pages 1-8 image-based)."""
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\scripts")
from cc_independent_extract import extract_pdf_ocr, OUT_ROOT

src = Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区二模\2026房山二模\试卷\2026北京房山高三二模政治（教师版）.pdf")
out = OUT_ROOT / "2026房山二模" / "试卷" / "2026北京房山高三二模政治（教师版）_pdf_OCR.txt"
out.parent.mkdir(parents=True, exist_ok=True)
print(f"OCR start: {src.name}")
text = extract_pdf_ocr(src)
out.write_text(text, encoding="utf-8")
print(f"OCR done : {src.name} -> {out} ({len(text)} chars)")
