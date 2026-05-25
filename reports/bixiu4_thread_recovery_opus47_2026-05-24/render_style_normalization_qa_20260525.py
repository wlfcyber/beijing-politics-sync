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
OUTDIR = RECOVERY / "word_render_qa_20260525_global_style_norm"
STYLE_JSON = RECOVERY / "STYLE_NORMALIZATION_AUDIT_20260525.json"
STYLE_MD = RECOVERY / "STYLE_NORMALIZATION_AUDIT_20260525.md"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"


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
        if OUTDIR.name != "word_render_qa_20260525_global_style_norm" or OUTDIR.parent != RECOVERY:
            raise RuntimeError(f"Refusing to clear unexpected output directory: {OUTDIR}")
        shutil.rmtree(OUTDIR)
    OUTDIR.mkdir(parents=True)


def export_pdf_with_word(docx: Path, pdf: Path, timestamp: str) -> Path | None:
    backup = None
    if pdf.exists():
        backup = pdf.with_name(f"{pdf.stem}_backup_before_style_normalization_render_{timestamp}.pdf")
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


def docx_label_count(docx: Path) -> int:
    label_left = chr(0x3010)
    texts: list[str] = []
    with zipfile.ZipFile(docx) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
    marker = "<w:t"
    pos = 0
    while True:
        start = xml.find(marker, pos)
        if start == -1:
            break
        gt = xml.find(">", start)
        end = xml.find("</w:t>", gt)
        if gt == -1 or end == -1:
            break
        texts.append(xml[gt + 1 : end])
        pos = end + 6
    return "".join(texts).count(label_left)


def render_pdf(pdf: Path) -> dict[str, object]:
    doc = fitz.open(pdf)
    pdf_text = []
    blank_like: list[int] = []
    for page_index, page in enumerate(doc):
        page_no = page_index + 1
        text = page.get_text("text") or ""
        pdf_text.append(text)
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
    label_left = chr(0x3010)
    return {
        "pdf_pages": doc.page_count,
        "rendered_png_count": len(list(OUTDIR.glob("page_*.png"))),
        "pdf_label_count": "".join(pdf_text).count(label_left),
        "blank_like_pages_excluding_cover_foreword": blank_like,
    }


def make_contact_sheet(pages: list[int]) -> str | None:
    existing_pages = []
    for page_no in pages:
        path = OUTDIR / f"page_{page_no:03d}.png"
        if path.exists():
            existing_pages.append(page_no)
    if not existing_pages:
        return None
    thumbs = []
    for page_no in existing_pages:
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
    out = OUTDIR / "global_style_norm_contact_sheet.png"
    sheet.save(out)
    for thumb in thumbs:
        thumb.close()
    return str(out)


def append_qa(manifest: dict[str, object]) -> None:
    style = json.loads(STYLE_JSON.read_text(encoding="utf-8"))
    blank = manifest["blank_like_pages_excluding_cover_foreword"]
    blank_note = "`0`" if not blank else "`" + ", ".join(str(p) for p in blank) + "`"
    section = f"""

## Global Style Normalization Render QA 20260525

- Status: `STYLE_NORMALIZATION_RENDER_PASS_WITH_MODEL_GATES_OPEN`.
- DOCX bytes after normalization: `{manifest['docx_bytes']}`.
- PDF bytes after re-export: `{manifest['pdf_bytes']}`.
- Word COM PDF export backup: `{manifest['pdf_backup']}`.
- Rendered PNGs: `{manifest['rendered_png_count']}/{manifest['pdf_pages']}` under `word_render_qa_20260525_global_style_norm`.
- DOCX/PDF label counts: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- Label-style failures before/after DOCX normalization: `{style['before_label_failures']}/{style['after_label_failures']}`.
- Heading pPr variants before/after: `{style['before_heading_stats']['ppr_variant_count']}/{style['after_heading_stats']['ppr_variant_count']}`.
- Heading rPr variants before/after: `{style['before_heading_stats']['rpr_variant_count']}/{style['after_heading_stats']['rpr_variant_count']}`.
- Blank-like body pages excluding cover/foreword: {blank_note}.
- Contact sheet: `{manifest['contact_sheet']}`.
- Boundary: this closes the structural new/old style mismatch found in the DOCX. Full manual every-page visual review and external model review remain open.
"""
    text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Global Style Normalization Render QA 20260525"
    if marker in text:
        text = text[: text.index(marker)]
    FORMAT_QA.write_text(text + section, encoding="utf-8", newline="\n")

    md = STYLE_MD.read_text(encoding="utf-8")
    md = md.replace(
        "Status: `DOCX_STYLE_NORMALIZED_RENDER_PENDING`",
        "Status: `DOCX_STYLE_NORMALIZED_AND_RENDERED`",
    )
    if "\n## Render QA\n" in md:
        md = md[: md.index("\n## Render QA\n")]
    md += f"""

## Render QA

- PDF export regenerated after DOCX style normalization.
- Rendered PNG pages: `{manifest['rendered_png_count']}/{manifest['pdf_pages']}`.
- DOCX/PDF label counts: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- Blank-like body pages excluding cover/foreword: {blank_note}.
- Contact sheet: `{manifest['contact_sheet']}`.
- Remaining boundary: GPTPro web and Claude Opus web/app external reviews are still `real_call_pending`; ClaudeCode model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    STYLE_MD.write_text(md, encoding="utf-8", newline="\n")


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    docx, pdf = current_pair()
    reset_outdir()
    pdf_backup = export_pdf_with_word(docx, pdf, timestamp)
    render_stats = render_pdf(pdf)
    sample_pages = [8, 12, 32, 39, 47, 55, 64, 80, 103, 148, 238, 280]
    contact_sheet = make_contact_sheet(sample_pages)
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
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    append_qa(manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
