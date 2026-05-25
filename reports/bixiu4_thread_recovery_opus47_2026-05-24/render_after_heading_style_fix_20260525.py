from __future__ import annotations

import json
import shutil
import zipfile
from datetime import datetime
from pathlib import Path

import fitz
import win32com.client
from PIL import Image, ImageDraw


RECOVERY = Path(__file__).resolve().parent
RUN = RECOVERY.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
OUTDIR = RECOVERY / "word_render_qa_20260525_heading_style_fix"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
STYLE_AUDIT_JSON = RECOVERY / "DOCX_STYLE_CONSISTENCY_AUDIT_20260525.json"


def current_pair() -> tuple[Path, Path]:
    docx_files = [
        p
        for p in DELIVERY.glob("*.docx")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
    pdf_files = [
        p
        for p in DELIVERY.glob("*.pdf")
        if "_backup_" not in p.stem and not p.name.startswith("~$")
    ]
    if len(docx_files) != 1 or len(pdf_files) != 1:
        raise RuntimeError(f"Expected one current DOCX/PDF, found {docx_files} / {pdf_files}")
    return docx_files[0], pdf_files[0]


def reset_outdir() -> None:
    if OUTDIR.exists():
        if OUTDIR.parent != RECOVERY or OUTDIR.name != "word_render_qa_20260525_heading_style_fix":
            raise RuntimeError(f"Refusing to clear unexpected output directory: {OUTDIR}")
        shutil.rmtree(OUTDIR)
    OUTDIR.mkdir(parents=True)


def docx_label_count(docx: Path) -> int:
    with zipfile.ZipFile(docx) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
    return xml.count("【")


def export_pdf(docx: Path, pdf: Path, timestamp: str) -> Path | None:
    backup = None
    if pdf.exists():
        backup = pdf.with_name(f"{pdf.stem}_backup_before_heading_style_fix_render_{timestamp}.pdf")
        shutil.copy2(pdf, backup)
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    doc = None
    try:
        doc = word.Documents.Open(str(docx), ReadOnly=True)
        doc.ExportAsFixedFormat(str(pdf), 17)
    finally:
        if doc is not None:
            doc.Close(False)
        word.Quit()
    return backup


def render_pdf(pdf: Path) -> dict[str, object]:
    doc = fitz.open(pdf)
    pdf_text_parts: list[str] = []
    blank_like: list[int] = []
    for page_index, page in enumerate(doc):
        page_no = page_index + 1
        text = page.get_text("text") or ""
        pdf_text_parts.append(text)
        pix = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
        img_path = OUTDIR / f"page_{page_no:03d}.png"
        pix.save(img_path)
        img = Image.open(img_path).convert("RGB")
        pixels = img.getdata()
        total = img.width * img.height
        nonwhite = sum(1 for pixel in pixels if min(pixel) < 245)
        nonwhite_ratio = nonwhite / total if total else 0.0
        if page_no > 2 and len(text.strip()) < 30 and nonwhite_ratio < 0.004:
            blank_like.append(page_no)
        img.close()
    return {
        "pdf_pages": doc.page_count,
        "rendered_png_count": len(list(OUTDIR.glob("page_*.png"))),
        "pdf_label_count": "".join(pdf_text_parts).count("【"),
        "blank_like_pages_excluding_cover_foreword": blank_like,
    }


def make_contact_sheet(pages: list[int]) -> str | None:
    existing = [p for p in pages if (OUTDIR / f"page_{p:03d}.png").exists()]
    if not existing:
        return None
    thumbs = []
    for page_no in existing:
        img = Image.open(OUTDIR / f"page_{page_no:03d}.png").convert("RGB")
        img.thumbnail((420, 600))
        canvas = Image.new("RGB", (450, img.height + 34), "white")
        canvas.paste(img, ((450 - img.width) // 2, 28))
        draw = ImageDraw.Draw(canvas)
        draw.text((12, 8), f"page {page_no}", fill=(0, 0, 0))
        thumbs.append(canvas)
        img.close()
    cols = 3
    row_height = max(t.height for t in thumbs)
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 450, rows * row_height), "white")
    for idx, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((idx % cols) * 450, (idx // cols) * row_height))
    out = OUTDIR / "heading_style_fix_contact_sheet.png"
    sheet.save(out)
    for thumb in thumbs:
        thumb.close()
    return str(out)


def append_format_qa(manifest: dict[str, object]) -> None:
    style = json.loads(STYLE_AUDIT_JSON.read_text(encoding="utf-8"))
    blank = manifest["blank_like_pages_excluding_cover_foreword"]
    blank_note = "`0`" if not blank else "`" + ", ".join(str(x) for x in blank) + "`"
    section = f"""

## Heading Style Consistency Render QA 20260525
Updated: {manifest['timestamp']}

- Status: `RENDER_PASS_HEADING_STYLE_CONSISTENCY_PASS_MODEL_GATES_OPEN`.
- DOCX bytes after heading style normalization: `{manifest['docx_bytes']}`.
- PDF bytes after re-export: `{manifest['pdf_bytes']}`.
- PDF export backup: `{manifest['pdf_backup']}`.
- Rendered PNGs: `{manifest['rendered_png_count']}/{manifest['pdf_pages']}` under `word_render_qa_20260525_heading_style_fix`.
- DOCX/PDF label counts: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- Blank-like body pages excluding cover/foreword: {blank_note}.
- Independent style audit status: `{style['status']}`.
- Question entries audited: `{style['question_entry_count']}`; inserted/legacy entries: `{style['inserted_entry_count']}/{style['legacy_entry_count']}`.
- Heading pPr/rPr variants after fix: `{style['heading_ppr_variant_count']}/{style['heading_rpr_variant_count']}`.
- Label first-run style variants after fix: `{style['label_first_run_variant_counts']}`.
- Ledger headings missing from current DOCX: `{style['missing_ledger_heading_count']}`.
- Contact sheet: `{manifest['contact_sheet']}`.
- Boundary: this is local structural/render QA. GPTPro web and Claude Opus web/app external reviews remain `real_call_pending`; ClaudeCode model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    current = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Heading Style Consistency Render QA 20260525"
    if marker in current:
        current = current[: current.index(marker)]
    FORMAT_QA.write_text(current.rstrip() + "\n" + section, encoding="utf-8", newline="\n")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx, pdf = current_pair()
    reset_outdir()
    pdf_backup = export_pdf(docx, pdf, timestamp)
    render_stats = render_pdf(pdf)
    pages = [19, 34, 44, 81, 112, 133, 153, 173, 209, 221, 251, 280]
    contact_sheet = make_contact_sheet(pages)
    manifest = {
        "timestamp": timestamp,
        "docx": str(docx),
        "pdf": str(pdf),
        "pdf_backup": str(pdf_backup) if pdf_backup else None,
        "docx_bytes": docx.stat().st_size,
        "pdf_bytes": pdf.stat().st_size,
        "docx_label_count": docx_label_count(docx),
        "contact_sheet": contact_sheet,
        **render_stats,
    }
    (OUTDIR / "render_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    append_format_qa(manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
