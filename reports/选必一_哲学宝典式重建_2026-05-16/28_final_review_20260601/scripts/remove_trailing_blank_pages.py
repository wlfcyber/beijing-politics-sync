from pathlib import Path

from docx import Document


DOCX = Path("/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终审修订版_20260601.docx")


def paragraph_is_empty(element) -> bool:
    if element.tag.rsplit("}", 1)[-1] != "p":
        return False
    text = "".join(element.xpath(".//w:t/text()")).strip()
    has_break = bool(element.xpath(".//w:br"))
    has_drawing = bool(element.xpath(".//w:drawing|.//w:pict|.//w:object"))
    has_sect = bool(element.xpath(".//w:sectPr"))
    return not text and not has_break and not has_drawing and not has_sect


def main() -> None:
    doc = Document(DOCX)
    body = doc._element.body
    removed = 0

    while len(body) >= 2:
        candidate = body[-2] if body[-1].tag.rsplit("}", 1)[-1] == "sectPr" else body[-1]
        if not paragraph_is_empty(candidate):
            break
        body.remove(candidate)
        removed += 1

    doc.save(DOCX)

    report = Path(__file__).resolve().parents[1] / "03_outputs" / "REMOVE_TRAILING_BLANK_PAGES_REPORT.md"
    report.write_text(
        "\n".join([
            "# REMOVE_TRAILING_BLANK_PAGES_REPORT",
            "",
            f"- DOCX: `{DOCX}`",
            f"- Removed trailing empty paragraphs: {removed}",
        ]) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
