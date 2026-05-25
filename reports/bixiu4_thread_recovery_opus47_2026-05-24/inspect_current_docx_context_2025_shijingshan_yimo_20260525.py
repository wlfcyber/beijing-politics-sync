from __future__ import annotations

from pathlib import Path

from docx import Document


RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
OUT = RECOVERY / "CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md"


def current_docx() -> Path:
    files = [
        p
        for p in DELIVERY.glob("*.docx")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
    if len(files) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {files}")
    return files[0]


def text(paragraph) -> str:
    return "".join(run.text for run in paragraph.runs).strip()


def is_heading(paragraph) -> bool:
    name = getattr(paragraph.style, "name", "") or ""
    return name.startswith("Heading")


def main() -> None:
    docx = current_docx()
    doc = Document(str(docx))
    paragraphs = list(doc.paragraphs)
    blocks = []
    for idx, paragraph in enumerate(paragraphs):
        ptext = text(paragraph)
        if not is_heading(paragraph) or "2025石景山一模" not in ptext:
            continue
        end = len(paragraphs)
        for j in range(idx + 1, len(paragraphs)):
            if is_heading(paragraphs[j]):
                end = j
                break
        blocks.append((idx, end, ptext))

    term_hits = {}
    for term in [
        "2025石景山一模",
        "不数既往",
        "不能知将来",
        "中华版本",
        "低空经济",
        "科学建议奖",
        "破与立",
    ]:
        hits = []
        for idx, paragraph in enumerate(paragraphs):
            ptext = text(paragraph)
            if term in ptext:
                hits.append((idx, ptext[:300]))
        term_hits[term] = hits

    lines = [
        "# Current DOCX Context - 2025 Shijingshan Yimo",
        "",
        f"- DOCX: `{docx}`",
        f"- Paragraphs scanned: `{len(paragraphs)}`",
        f"- Suite heading blocks: `{len(blocks)}`",
        "",
        "## Suite Heading Blocks",
        "",
    ]
    for start, end, heading in blocks:
        lines.append(f"### Paragraph {start}: {heading}")
        for i in range(start, min(end, start + 8)):
            lines.append(f"- `{i}` style=`{paragraphs[i].style.name}` text={text(paragraphs[i])}")
        lines.append("")
    lines.append("## Term Hits")
    lines.append("")
    for term, hits in term_hits.items():
        lines.append(f"### {term}")
        lines.append(f"- hits: `{len(hits)}`")
        for idx, ptext in hits[:20]:
            lines.append(f"- `{idx}`: {ptext}")
        lines.append("")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
