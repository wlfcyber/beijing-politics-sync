from pathlib import Path

from docx import Document
from docx.oxml.ns import qn


DOCX = Path("/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终审修订版_20260601.docx")


def main() -> None:
    doc = Document(DOCX)
    removed = 0
    touched_paragraphs = 0

    for paragraph in doc.paragraphs:
        if paragraph.style is None or paragraph.style.name != "Normal":
            continue
        if not paragraph.text.strip():
            continue
        touched = False
        for run in paragraph.runs:
            rpr = run._element.rPr
            if rpr is None:
                continue
            rfonts = rpr.find(qn("w:rFonts"))
            if rfonts is not None:
                rpr.remove(rfonts)
                removed += 1
                touched = True
        if touched:
            touched_paragraphs += 1

    doc.save(DOCX)

    report = Path(__file__).resolve().parents[1] / "03_outputs" / "ALIGN_BODY_FONTS_REPORT.md"
    report.write_text(
        "\n".join([
            "# ALIGN_BODY_FONTS_REPORT",
            "",
            f"- DOCX: `{DOCX}`",
            f"- Normal paragraphs touched: {touched_paragraphs}",
            f"- Direct run font overrides removed: {removed}",
            "",
            "Scope: text, bold/italic/color, headings, page setup, and paragraph spacing were not rewritten. The change only removes direct run font overrides in Normal paragraphs so the body inherits the same Normal style as the philosophy reference document.",
        ]) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
