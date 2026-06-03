#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt


DOCX = Path("/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终审修订版_20260601.docx")
REPORT = Path(
    "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/"
    "选必一_哲学宝典式重建_2026-05-16/28_final_review_20260601/03_outputs/"
    "RENUMBER_REVISED_DOCX_REPORT.md"
)
ENTRY_RE = re.compile(r"^(\d+)\.\s*(.+)$")


def set_font(run) -> None:
    run.font.name = "宋体"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")
    run.font.size = Pt(10.5)


def main() -> None:
    doc = Document(DOCX)
    expected = None
    changed = []
    for p in doc.paragraphs:
        text = p.text.strip()
        if text.startswith("核心答题点："):
            expected = 1
            continue
        if p.style.name.startswith("Heading") and p.style.name != "Heading 3":
            expected = None
            continue
        if expected is None:
            continue
        m = ENTRY_RE.match(text)
        if not m:
            continue
        old = int(m.group(1))
        suffix = m.group(2)
        if old != expected:
            changed.append(f"{old} -> {expected}: {suffix}")
            p.text = f"{expected}. {suffix}"
            for run in p.runs:
                set_font(run)
        expected += 1
    doc.save(DOCX)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        "\n".join(
            [
                "# RENUMBER_REVISED_DOCX_REPORT",
                "",
                f"- DOCX: `{DOCX}`",
                f"- Renumbered headings: {len(changed)}",
                "",
                *[f"- {x}" for x in changed],
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(REPORT)


if __name__ == "__main__":
    main()
