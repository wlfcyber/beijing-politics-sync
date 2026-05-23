from __future__ import annotations

import re
from pathlib import Path

import fitz


DESKTOP = Path.home() / "Desktop"
RUN = (
    DESKTOP
    / "02_代码项目与工具"
    / "mac-thread-restore"
    / "beijing-politics-sync-visible"
    / "reports"
    / "bixiu4_philosophy_full_coverage_double_lane_2026-05-23"
)
PDF = DESKTOP / "哲学宝典最终版-飞哥正志讲堂_主次矛盾全覆盖补丁v7_2026-05-23.pdf"
OUT_DIR = RUN / "06_render_check"
OUT_MD = OUT_DIR / "pdf_v7_render_check.md"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(PDF))
    terms = ["主要矛盾和次要矛盾", "矛盾的主要方面和次要方面", "主流和支流", "本次补入题目索引"]
    found: dict[str, int] = {}
    for i, page in enumerate(doc):
        compact = re.sub(r"\s+", "", page.get_text())
        for term in terms:
            if term in compact and term not in found:
                found[term] = i + 1

    rendered: list[str] = []
    for term, page_no in found.items():
        page = doc[page_no - 1]
        pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
        safe = "".join(c for c in term if c.isalnum())[:12]
        image_path = OUT_DIR / f"v7_page_{page_no}_{safe}.png"
        pix.save(str(image_path))
        rendered.append(str(image_path))

    lines = [
        "# PDF v7 render check",
        "",
        f"- PDF: {PDF}",
        f"- Page count: {doc.page_count}",
        "",
        "## Term page map",
    ]
    for term in terms:
        lines.append(f"- {term}: {found.get(term, 'NOT_FOUND')}")
    lines.extend(["", "## Rendered sample pages"])
    for path in rendered:
        lines.append(f"- {path}")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
