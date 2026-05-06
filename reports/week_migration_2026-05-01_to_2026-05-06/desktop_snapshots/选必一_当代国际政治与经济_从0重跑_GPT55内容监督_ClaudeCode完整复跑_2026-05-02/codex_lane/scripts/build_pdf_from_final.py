#!/usr/bin/env python3
"""Create a readable PDF directly from the final student Markdown."""

from __future__ import annotations

from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak


RUN = Path(__file__).resolve().parents[2]
MD = RUN / "09_delivery" / "飞哥政治庄园_选必一_当代国际政治与经济_细则术语成品版_2026-05-03.md"
OUT = RUN / "09_delivery" / "飞哥政治庄园_选必一_当代国际政治与经济_细则术语成品版_2026-05-03.pdf"


pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))


def safe(text: str) -> str:
    return escape(text).replace("《", "《").replace("》", "》")


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("STSong-Light", 8.5)
    canvas.setFillColor(colors.HexColor("#6B7280"))
    canvas.drawCentredString(A4[0] / 2, A4[1] - 1.05 * cm, "飞哥政治庄园 · 选必一《当代国际政治与经济》")
    canvas.setStrokeColor(colors.HexColor("#D1D5DB"))
    canvas.line(1.6 * cm, A4[1] - 1.22 * cm, A4[0] - 1.6 * cm, A4[1] - 1.22 * cm)
    canvas.drawCentredString(A4[0] / 2, 0.9 * cm, f"第 {doc.page} 页")
    canvas.restoreState()


def build() -> None:
    styles = getSampleStyleSheet()
    base = dict(fontName="STSong-Light", wordWrap="CJK")

    def style(name: str, **kwargs) -> ParagraphStyle:
        opts = {**base, **kwargs}
        return ParagraphStyle(name, **opts)

    styles.add(style("TitleCN", fontSize=18, leading=24, alignment=TA_CENTER, textColor=colors.HexColor("#111827"), spaceAfter=16))
    styles.add(style("H1CN", fontSize=14, leading=19, textColor=colors.HexColor("#0F766E"), spaceBefore=10, spaceAfter=8))
    styles.add(style("H2CN", fontSize=11.5, leading=16, textColor=colors.HexColor("#111827"), spaceBefore=8, spaceAfter=5))
    styles.add(style("H3CN", fontSize=10.5, leading=15, textColor=colors.HexColor("#374151"), spaceBefore=5, spaceAfter=4))
    styles.add(style("BodyCN", fontSize=9.5, leading=14.5, alignment=TA_LEFT, textColor=colors.HexColor("#1F2937"), spaceAfter=4))
    styles.add(style("NoteCN", fontSize=9, leading=13, textColor=colors.HexColor("#4B5563"), spaceAfter=8))

    story = []
    for raw in MD.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            story.append(Paragraph(safe(line[2:]), styles["TitleCN"]))
            story.append(Spacer(1, 0.2 * cm))
        elif line.startswith("## "):
            if story:
                story.append(Spacer(1, 0.1 * cm))
            story.append(Paragraph(safe(line[3:]), styles["H1CN"]))
        elif line.startswith("### 术语："):
            story.append(Paragraph(safe(line[4:]), styles["H2CN"]))
        elif line.startswith("#### "):
            story.append(Paragraph(safe(line[5:]), styles["H3CN"]))
        else:
            m = re.match(r"^(框架位置|完整设问|细则位置|来源|材料触发|答案句)：(.+)$", line)
            if m:
                story.append(Paragraph(f"<b>{safe(m.group(1))}：</b>{safe(m.group(2))}", styles["BodyCN"]))
            else:
                story.append(Paragraph(safe(line), styles["NoteCN"]))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=1.6 * cm,
        rightMargin=1.6 * cm,
        topMargin=1.55 * cm,
        bottomMargin=1.35 * cm,
        title="飞哥政治庄园 选必一细则术语成品版",
        author="Codex",
    )
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(OUT)


if __name__ == "__main__":
    build()
