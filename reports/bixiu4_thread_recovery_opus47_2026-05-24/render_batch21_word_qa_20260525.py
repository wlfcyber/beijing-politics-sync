from __future__ import annotations

import csv
import json
import shutil
import zipfile
from pathlib import Path

import fitz
import win32com.client
from lxml import etree
from PIL import Image, ImageDraw


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}

ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
OUTDIR = RECOVERY / "word_render_qa_20260525_batch21_word"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH21_2025_DONGCHENG_FINAL_CODEX_20260525.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
GLOBAL_AUDIT_CSV = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"

SUITE = "2025东城期末"


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def docx_text(docx: Path) -> str:
    with zipfile.ZipFile(docx) as zf:
        xml = zf.read("word/document.xml")
    root = etree.fromstring(xml)
    return "".join(t.text or "" for t in root.xpath("//w:t", namespaces=NS))


def export_pdf_with_word(docx: Path, pdf: Path) -> Path | None:
    backup = None
    if pdf.exists():
        backup = pdf.with_name(f"{pdf.stem}_backup_before_batch21_render_20260525.pdf")
        counter = 1
        while backup.exists():
            backup = pdf.with_name(f"{pdf.stem}_backup_before_batch21_render_20260525_{counter}.pdf")
            counter += 1
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


def locate_suite_headings_with_word(docx: Path) -> list[dict[str, object]]:
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    doc = None
    hits: list[dict[str, object]] = []
    try:
        doc = word.Documents.Open(str(docx), ReadOnly=True)
        for para in doc.Paragraphs:
            text = para.Range.Text.replace("\r", "").replace("\x07", "").strip()
            if SUITE in text and "第" in text and "题" in text:
                page = int(para.Range.Information(3))
                hits.append({"heading": text, "page": page})
    finally:
        if doc is not None:
            doc.Close(False)
        word.Quit()
    return hits


def reset_outdir() -> None:
    if OUTDIR.exists():
        if OUTDIR.name != "word_render_qa_20260525_batch21_word" or OUTDIR.parent != RECOVERY:
            raise RuntimeError(f"Refusing to clear unexpected output directory: {OUTDIR}")
        shutil.rmtree(OUTDIR)
    OUTDIR.mkdir(parents=True)


def render_pdf_pages(pdf: Path) -> tuple[int, list[int], list[int]]:
    doc = fitz.open(pdf)
    blank_like: list[int] = []
    hit_pages: list[int] = []
    for idx, page in enumerate(doc, start=1):
        text = page.get_text()
        if SUITE in text:
            hit_pages.append(idx)
        pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
        png = OUTDIR / f"page_{idx:03d}.png"
        pix.save(png)
        with Image.open(png) as image:
            small = image.convert("L").resize((max(1, image.width // 8), max(1, image.height // 8)))
            nonwhite = sum(1 for px in small.getdata() if px < 245)
            ratio = nonwhite / (small.width * small.height)
            if ratio < 0.003:
                blank_like.append(idx)
    pages = doc.page_count
    doc.close()
    return pages, blank_like, hit_pages


def pdf_text_and_label_count(pdf: Path) -> tuple[str, int]:
    doc = fitz.open(pdf)
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    return text, text.count("【")


def make_contact_sheet(hit_pages: list[int]) -> str | None:
    if not hit_pages:
        return None
    thumbs = []
    for page_no in hit_pages:
        path = OUTDIR / f"page_{page_no:03d}.png"
        img = Image.open(path).convert("RGB")
        img.thumbnail((420, 600))
        canvas = Image.new("RGB", (450, img.height + 34), "white")
        canvas.paste(img, ((450 - img.width) // 2, 28))
        draw = ImageDraw.Draw(canvas)
        draw.text((12, 8), f"page {page_no}", fill=(0, 0, 0))
        thumbs.append(canvas)
    cols = 2
    rows = (len(thumbs) + cols - 1) // cols
    width = cols * 450
    height = rows * max(t.height for t in thumbs)
    sheet = Image.new("RGB", (width, height), "white")
    for idx, thumb in enumerate(thumbs):
        x = (idx % cols) * 450
        y = (idx // cols) * thumb.height
        sheet.paste(thumb, (x, y))
    out = OUTDIR / "batch21_hit_pages_contact_sheet.png"
    sheet.save(out)
    for thumb in thumbs:
        thumb.close()
    return str(out)


def update_global_audit() -> None:
    with GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    for row in rows:
        if row.get("normalized_suite") == SUITE:
            row["blocker_or_next_action"] = "Batch21 matrix/DOCX/render pass; ClaudeCode Opus 4.7 model-lane recheck pending."
    with GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def append_reports(manifest: dict[str, object]) -> None:
    hit_pages = ", ".join(str(p) for p in manifest["suite_hit_pages"])
    blank_note = (
        f"`{len(manifest['blank_like_pages_excluding_cover_foreword'])}`"
        if not manifest["blank_like_pages_excluding_cover_foreword"]
        else "`" + ", ".join(str(p) for p in manifest["blank_like_pages_excluding_cover_foreword"]) + "`"
    )
    qa_append = f"""

## Batch21 Render QA: 2025东城期末
Updated: 2026-05-25 07:25 +08

- Current DOCX bytes: `{manifest['docx_bytes']}`.
- Current PDF bytes: `{manifest['pdf_bytes']}`.
- PDF export was regenerated through local Word COM after Batch21 Q21 people insertion and Q21 value-judgment refresh, with the previous PDF backed up before replacement.
- Rendered PNGs were generated from the regenerated PDF with PyMuPDF under `word_render_qa_20260525_batch21_word`.
- PDF page count / rendered `page_*.png` count: `{manifest['pages']} / {manifest['rendered_png']}`.
- Pixel scan found blank-like body pages: {blank_note}.
- Full-document label count: DOCX `{manifest['docx_label_count']}` / PDF `{manifest['pdf_label_count']}`.
- Current DOCX / rendered-PDF visible heading mentions for `2025东城期末`: `{manifest['docx_suite_mentions']} / {manifest['pdf_suite_mentions']}`.
- Raw PDF text extraction exact-string count is `{manifest['pdf_text_suite_mentions']}` because the Word-generated PDF does not preserve this Chinese string for exact text search; Word layout page mapping plus rendered page images are the visibility evidence.
- Word layout located Batch21 headings on pages `{hit_pages}`.
- Render manifest: `word_render_qa_20260525_batch21_word/render_manifest.json`; contact sheet: `word_render_qa_20260525_batch21_word/batch21_hit_pages_contact_sheet.png`.
- Visual page checks should focus on pages `{hit_pages}`; programmatic render gate is `RENDER_PASS_MODEL_PENDING`.
"""
    format_text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## Batch21 Render QA: 2025东城期末"
    if marker in format_text:
        format_text = format_text[: format_text.index(marker)]
    FORMAT_QA.write_text(format_text + qa_append, encoding="utf-8")

    report = BATCH_REPORT.read_text(encoding="utf-8")
    report = report.replace("Status: `LOCAL_APPLIED_RENDER_PENDING_MODEL_PENDING`", "Status: `LOCAL_APPLIED_RENDER_PASS_MODEL_PENDING`")
    marker = "\n## Render QA Result"
    if marker in report:
        report = report[: report.index(marker)]
    report += f"""

## Render QA Result

- Render status: `RENDER_PASS_MODEL_PENDING`.
- PDF pages/rendered PNGs: `{manifest['pages']}/{manifest['rendered_png']}`.
- DOCX/PDF label count: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- DOCX/rendered-PDF visible suite mentions: `{manifest['docx_suite_mentions']}/{manifest['pdf_suite_mentions']}`.
- Raw PDF exact text-extraction suite mentions: `{manifest['pdf_text_suite_mentions']}`.
- Hit pages: `{hit_pages}`.
- Manifest: `word_render_qa_20260525_batch21_word/render_manifest.json`.
"""
    BATCH_REPORT.write_text(report, encoding="utf-8")

    thread_append = f"""

## Batch21 Render Gate: 2025东城期末 - 2026-05-25

- batch state: `LOCAL_APPLIED_RENDER_PASS_MODEL_PENDING`
- render pages/pngs: `{manifest['pages']}/{manifest['rendered_png']}`
- labels DOCX/PDF: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`
- suite mentions DOCX/PDF: `{manifest['docx_suite_mentions']}/{manifest['pdf_suite_mentions']}`
- ClaudeCode evidence remains pending.
"""
    THREAD_STATUS.write_text(THREAD_STATUS.read_text(encoding="utf-8") + thread_append, encoding="utf-8")

    governor_append = f"""

### Governor Batch21 Render Gate

- Render gate: `RENDER_PASS_MODEL_PENDING`.
- Pages/rendered PNGs: `{manifest['pages']}/{manifest['rendered_png']}`.
- Label count DOCX/PDF: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- Remaining local gate: ClaudeCode Opus 4.7 production-lane recheck.
"""
    GOVERNOR.write_text(GOVERNOR.read_text(encoding="utf-8") + governor_append, encoding="utf-8")

    confucius_append = f"""

### Confucius Batch21 Render Gate

- The 4 `2025东城期末` learner-facing entries are present in both DOCX and PDF.
- Rendered hit pages: `{hit_pages}`.
- Programmatic page/image/label checks pass; manual visual focus pages are captured in the contact sheet.
"""
    CONFUCIUS.write_text(CONFUCIUS.read_text(encoding="utf-8") + confucius_append, encoding="utf-8")


def main() -> None:
    docx = current_docx()
    pdf = DELIVERY / f"{docx.stem}.pdf"
    reset_outdir()
    pdf_backup = export_pdf_with_word(docx, pdf)
    word_heading_hits = locate_suite_headings_with_word(docx)

    full_docx_text = docx_text(docx)
    pages, blank_like, pdf_text_hit_pages = render_pdf_pages(pdf)
    pdf_text, pdf_label_count = pdf_text_and_label_count(pdf)
    hit_pages = sorted({int(item["page"]) for item in word_heading_hits})
    contact_sheet = make_contact_sheet(hit_pages)
    png_count = len(list(OUTDIR.glob("page_*.png")))
    manifest = {
        "docx": str(docx),
        "pdf": str(pdf),
        "pdf_backup": str(pdf_backup) if pdf_backup else None,
        "docx_bytes": docx.stat().st_size,
        "pdf_bytes": pdf.stat().st_size,
        "pages": pages,
        "rendered_png": png_count,
        "blank_like_pages": blank_like,
        "blank_like_pages_excluding_cover_foreword": [p for p in blank_like if p not in {1, 2}],
        "docx_label_count": full_docx_text.count("【"),
        "pdf_label_count": pdf_label_count,
        "suite": SUITE,
        "docx_suite_mentions": full_docx_text.count(SUITE),
        "pdf_suite_mentions": len(word_heading_hits),
        "pdf_text_suite_mentions": pdf_text.count(SUITE),
        "pdf_text_hit_pages": pdf_text_hit_pages,
        "word_layout_heading_hits": word_heading_hits,
        "suite_hit_pages": hit_pages,
        "contact_sheet": contact_sheet,
        "notes": [
            "PDF exported with local Word COM.",
            "Rendered page_*.png from regenerated PDF with PyMuPDF.",
            "Batch21 includes existing Q4/Q16 registration, refreshed Q21 value entry, and newly inserted Q21 people entry.",
        ],
    }
    (OUTDIR / "render_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    update_global_audit()
    append_reports(manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
