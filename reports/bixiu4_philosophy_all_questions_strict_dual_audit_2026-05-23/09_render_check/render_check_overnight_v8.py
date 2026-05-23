from __future__ import annotations

from pathlib import Path

import fitz


DESKTOP = Path.home() / "Desktop"
OUT_DIR = (
    DESKTOP
    / "02_代码项目与工具"
    / "mac-thread-restore"
    / "beijing-politics-sync-visible"
    / "reports"
    / "bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23"
    / "09_render_check"
)

PDFS = [
    DESKTOP / "5.24凌晨严审结果v8" / "01_学生版Word" / "必修四哲学宝典_v8_65套严审学生版.pdf",
    DESKTOP / "5.24凌晨严审结果v8" / "02_选择题专册" / "必修四哲学选择题触发与错肢专册_v8.pdf",
    DESKTOP / "5.24凌晨严审结果v8" / "03_严审报告" / "65套覆盖与模型审核状态.pdf",
]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines = ["# Overnight v8 PDF render check", ""]
    for pdf in PDFS:
        doc = fitz.open(str(pdf))
        lines.append(f"## {pdf.name}")
        lines.append(f"- pages: {doc.page_count}")
        for page_no in sorted({1, max(1, doc.page_count // 2), doc.page_count}):
            page = doc[page_no - 1]
            pix = page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False)
            out = OUT_DIR / f"{pdf.stem}_page_{page_no}.png"
            pix.save(str(out))
            lines.append(f"- rendered: {out}")
        lines.append("")
    report = OUT_DIR / "overnight_v8_render_check.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
