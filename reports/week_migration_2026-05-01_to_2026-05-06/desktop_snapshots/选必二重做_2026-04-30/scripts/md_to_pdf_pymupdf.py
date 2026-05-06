#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz


FONT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
PAGE_W, PAGE_H = 595, 842
MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM = 48, 48, 48


def wrap_text(font: fitz.Font, text: str, fontsize: float, max_width: float) -> list[str]:
    text = text.strip()
    if not text:
        return []
    lines: list[str] = []
    current = ""
    for ch in text:
        trial = current + ch
        if current and font.text_length(trial, fontsize=fontsize) > max_width:
            lines.append(current.rstrip())
            current = ch.lstrip()
        else:
            current = trial
    if current.strip():
        lines.append(current.rstrip())
    return lines


def style_for(line: str) -> tuple[str, float, float, float]:
    if line.startswith("# "):
        return line[2:].strip(), 22, 28, 10
    if line.startswith("## "):
        return line[3:].strip(), 16, 22, 8
    if line.startswith("### "):
        return line[4:].strip(), 13, 18, 5
    if line.startswith("#### "):
        return line[5:].strip(), 11.5, 16, 4
    if line.startswith("- "):
        return "• " + line[2:].strip(), 10.5, 15, 2
    if re.match(r"^\d+\. ", line):
        return line.strip(), 10.5, 15, 2
    return line.strip(), 10.5, 15, 3


def convert(md_path: Path, pdf_path: Path) -> None:
    font = fitz.Font(fontfile=FONT)
    doc = fitz.open()
    page = doc.new_page(width=PAGE_W, height=PAGE_H)
    page.insert_font(fontname="cjk", fontfile=FONT)
    y = MARGIN_TOP
    max_width = PAGE_W - MARGIN_X * 2

    for raw in md_path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line:
            y += 3
            continue
        text, fontsize, line_height, after = style_for(line)
        indent = 14 if line.startswith("- ") else 0
        width = max_width - indent
        wrapped = wrap_text(font, text, fontsize, width)
        block_height = line_height * max(1, len(wrapped)) + after
        if y + block_height > PAGE_H - MARGIN_BOTTOM:
            page = doc.new_page(width=PAGE_W, height=PAGE_H)
            page.insert_font(fontname="cjk", fontfile=FONT)
            y = MARGIN_TOP
        for wrapped_line in wrapped:
            page.insert_text((MARGIN_X + indent, y), wrapped_line, fontname="cjk", fontsize=fontsize, color=(0, 0, 0))
            y += line_height
        y += after

    for idx, page in enumerate(doc, start=1):
        footer = f"{idx}"
        page.insert_text((PAGE_W - MARGIN_X, PAGE_H - 24), footer, fontname="cjk", fontsize=9)
    doc.subset_fonts()
    doc.save(pdf_path, garbage=4, deflate=True)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: md_to_pdf_pymupdf.py input.md output.pdf", file=sys.stderr)
        return 2
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
    print(sys.argv[2])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
