#!/usr/bin/env python3
"""OCR the two scanned PDFs: 西城二模评标 and 26顺义二模(1).
"""
import sys
from pathlib import Path

sys.path.insert(0, r"C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\scripts")
from cc_independent_extract import extract_pdf_ocr, OUT_ROOT

targets = [
    (
        Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区二模\2026西城二模\细则\西城二模评标.pdf"),
        OUT_ROOT / "2026西城二模" / "细则" / "西城二模评标_pdf.txt",
    ),
    (
        Path(r"C:\Users\Administrator\Desktop\2026各区模拟题\2026各区二模\2026顺义二模\26顺义二模(1).pdf"),
        OUT_ROOT / "2026顺义二模" / "26顺义二模(1)_pdf.txt",
    ),
]

for src, out in targets:
    out.parent.mkdir(parents=True, exist_ok=True)
    print(f"OCR start: {src.name}")
    text = extract_pdf_ocr(src)
    out.write_text(text, encoding="utf-8")
    print(f"OCR done : {src.name} -> {out} ({len(text)} chars)")
