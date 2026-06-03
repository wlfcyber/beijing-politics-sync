from __future__ import annotations

import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


FONT_PATH = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_NAME = "STHeitiLight"


def clean_inline(text: str) -> str:
    text = escape(text)
    text = text.replace("**", "")
    text = text.replace("`", "")
    return text


def build_pdf(md_path: Path, pdf_path: Path) -> None:
    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

    base = ParagraphStyle(
        "base",
        fontName=FONT_NAME,
        fontSize=8.8,
        leading=13,
        alignment=TA_LEFT,
        wordWrap="CJK",
        spaceAfter=2.2,
    )
    title = ParagraphStyle(
        "title",
        parent=base,
        fontSize=18,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#111111"),
        spaceAfter=8,
    )
    h1 = ParagraphStyle(
        "h1",
        parent=base,
        fontSize=15,
        leading=20,
        textColor=colors.HexColor("#111111"),
        spaceBefore=8,
        spaceAfter=6,
    )
    h2 = ParagraphStyle(
        "h2",
        parent=base,
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#222222"),
        spaceBefore=6,
        spaceAfter=4,
    )
    h3 = ParagraphStyle(
        "h3",
        parent=base,
        fontSize=10.2,
        leading=14,
        textColor=colors.HexColor("#333333"),
        spaceBefore=5,
        spaceAfter=3,
    )
    bullet = ParagraphStyle(
        "bullet",
        parent=base,
        leftIndent=10,
        firstLineIndent=-7,
    )

    story = []
    first_h1 = True
    for raw in md_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            story.append(Spacer(1, 2.5))
            continue
        if line.startswith("# "):
            if not first_h1:
                story.append(PageBreak())
            first_h1 = False
            story.append(Paragraph(clean_inline(line[2:]), title if not story else h1))
        elif line.startswith("## "):
            story.append(Paragraph(clean_inline(line[3:]), h2))
        elif line.startswith("### "):
            story.append(Paragraph(clean_inline(line[4:]), h3))
        elif line.startswith("- "):
            story.append(Paragraph("• " + clean_inline(line[2:]), bullet))
        else:
            story.append(Paragraph(clean_inline(line), base))

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
    )
    doc.build(story)


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: md_to_pdf_xuanbiyi_clean_20260526.py input.md output.pdf")
    build_pdf(Path(sys.argv[1]), Path(sys.argv[2]))


if __name__ == "__main__":
    main()
