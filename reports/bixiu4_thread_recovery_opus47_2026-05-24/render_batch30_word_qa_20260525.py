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
OUTDIR = RECOVERY / "word_render_qa_20260525_batch30_word"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH30_2026_CHAOYANG_FINAL_CODEX_20260525.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
GLOBAL_AUDIT_CSV = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"

SUITE = "2026朝阳期末"
EXPECTED_HEADINGS = 10


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
        backup = pdf.with_name(f"{pdf.stem}_backup_before_batch30_render_20260525.pdf")
        counter = 1
        while backup.exists():
            backup = pdf.with_name(f"{pdf.stem}_backup_before_batch30_render_20260525_{counter}.pdf")
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
    hits = []
    try:
        doc = word.Documents.Open(str(docx), ReadOnly=True)
        for para in doc.Paragraphs:
            text = para.Range.Text.replace("\r", "").replace("\x07", "").strip()
            if SUITE in text and "第" in text and "题" in text:
                hits.append({"heading": text, "page": int(para.Range.Information(3))})
    finally:
        if doc is not None:
            doc.Close(False)
        word.Quit()
    return hits


def reset_outdir() -> None:
    if OUTDIR.exists():
        if OUTDIR.name != "word_render_qa_20260525_batch30_word" or OUTDIR.parent != RECOVERY:
            raise RuntimeError(f"Refusing to clear unexpected output directory: {OUTDIR}")
        shutil.rmtree(OUTDIR)
    OUTDIR.mkdir(parents=True)


def render_pdf_pages(pdf: Path) -> tuple[int, list[int], list[int]]:
    doc = fitz.open(pdf)
    blank_like = []
    hit_pages = []
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
        img.close()
    cols = 2
    row_height = max(t.height for t in thumbs)
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 450, rows * row_height), "white")
    for idx, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((idx % cols) * 450, (idx // cols) * row_height))
    out = OUTDIR / "batch30_hit_pages_contact_sheet.png"
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
            row["blocker_or_next_action"] = "Batch30 matrix/DOCX/render pass; ClaudeCode Opus 4.7 model-lane recheck pending."
    with GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def append_reports(manifest: dict[str, object]) -> None:
    hit_pages = ", ".join(str(p) for p in manifest["suite_hit_pages"])
    blank_note = "`0`" if not manifest["blank_like_pages_excluding_cover_foreword"] else "`" + ", ".join(str(p) for p in manifest["blank_like_pages_excluding_cover_foreword"]) + "`"
    qa_append = f"""

## Batch30 Render QA: 2026朝阳期末
Updated: 2026-05-25 09:58 +08

- Current DOCX bytes: `{manifest['docx_bytes']}`.
- Current PDF bytes: `{manifest['pdf_bytes']}`.
- PDF export was regenerated through local Word COM after Batch30 insertion/registration.
- Rendered PNGs were generated from the regenerated PDF with PyMuPDF under `word_render_qa_20260525_batch30_word`.
- PDF pages/rendered PNGs: `{manifest['pdf_pages']}/{manifest['rendered_png_count']}`.
- Blank-like body pages, excluding cover/foreword pages 1-2: {blank_note}.
- DOCX label count: `{manifest['docx_label_count']}`.
- PDF label count: `{manifest['pdf_label_count']}`.
- DOCX suite heading count: `{manifest['docx_suite_heading_count']}`.
- Word layout visible suite headings: `{manifest['word_visible_heading_count']}`.
- PDF text suite mention count: `{manifest['pdf_suite_text_count']}`.
- Suite hit pages in regenerated PDF: `{hit_pages}`.
- Contact sheet: `{manifest['contact_sheet']}`.
- Result: `RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING`.
"""
    text = FORMAT_QA.read_text(encoding="utf-8")
    for marker in ["\n## Batch30 Pending Render QA: 2026朝阳期末", "\n## Batch30 Render QA: 2026朝阳期末"]:
        if marker in text:
            text = text[: text.index(marker)]
    FORMAT_QA.write_text(text + qa_append, encoding="utf-8", newline="\n")

    report_text = BATCH_REPORT.read_text(encoding="utf-8")
    marker = "\n## Render QA Result"
    if marker in report_text:
        report_text = report_text[: report_text.index(marker)]
    BATCH_REPORT.write_text(report_text + f"""

## Render QA Result

- Render status: `RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING`.
- PDF pages/rendered PNGs: `{manifest['pdf_pages']}/{manifest['rendered_png_count']}`.
- DOCX/PDF label count: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- DOCX/Word-layout visible suite mentions: `{manifest['docx_suite_heading_count']}/{manifest['word_visible_heading_count']}`.
- Raw PDF exact text-extraction suite mentions: `{manifest['pdf_suite_text_count']}`.
- Hit pages: `{hit_pages}`.
- Manifest: `word_render_qa_20260525_batch30_word/render_manifest.json`.
""", encoding="utf-8", newline="\n")

    append_block = f"""

## Batch30 Render QA: 2026朝阳期末
Updated: 2026-05-25 09:58 +08

- Status: `RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING`.
- DOCX/PDF label counts match: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- Visible suite headings match expected count: `{manifest['word_visible_heading_count']}/{EXPECTED_HEADINGS}`.
- Blank-like body pages excluding cover/foreword: {blank_note}.
- ClaudeCode Opus 4.7 recheck remains pending; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch30 Render QA: 2026朝阳期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + append_block, encoding="utf-8", newline="\n")


def main() -> int:
    docx = current_docx()
    pdf = docx.with_suffix(".pdf")
    reset_outdir()
    pdf_backup = export_pdf_with_word(docx, pdf)
    dtext = docx_text(docx)
    word_hits = locate_suite_headings_with_word(docx)
    pages, blank_like, pdf_text_hit_pages = render_pdf_pages(pdf)
    ptext, pdf_label_count = pdf_text_and_label_count(pdf)
    docx_suite_count = dtext.count(SUITE)
    pdf_suite_count = ptext.count(SUITE)
    docx_label_count = dtext.count("【")
    word_hit_pages = sorted({int(hit["page"]) for hit in word_hits})
    hit_pages = sorted(set(pdf_text_hit_pages) | set(word_hit_pages))
    contact_sheet = make_contact_sheet(hit_pages)
    rendered_count = len(list(OUTDIR.glob("page_*.png")))
    body_blank = [p for p in blank_like if p not in {1, 2}]
    manifest = {
        "suite": SUITE,
        "docx": str(docx),
        "pdf": str(pdf),
        "pdf_backup": str(pdf_backup) if pdf_backup else None,
        "docx_bytes": docx.stat().st_size,
        "pdf_bytes": pdf.stat().st_size,
        "pdf_pages": pages,
        "rendered_png_count": rendered_count,
        "blank_like_pages_all": blank_like,
        "blank_like_pages_excluding_cover_foreword": body_blank,
        "docx_label_count": docx_label_count,
        "pdf_label_count": pdf_label_count,
        "docx_suite_heading_count": docx_suite_count,
        "word_visible_heading_count": len(word_hits),
        "word_visible_headings": word_hits,
        "pdf_suite_text_count": pdf_suite_count,
        "suite_hit_pages": hit_pages,
        "contact_sheet": contact_sheet,
    }
    (OUTDIR / "render_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    if rendered_count != pages:
        raise RuntimeError(f"Rendered page count mismatch: {rendered_count} vs {pages}")
    if body_blank:
        raise RuntimeError(f"Blank-like body pages detected: {body_blank}")
    if docx_label_count != pdf_label_count:
        raise RuntimeError(f"DOCX/PDF label mismatch: {docx_label_count} vs {pdf_label_count}")
    if len(word_hits) != EXPECTED_HEADINGS:
        raise RuntimeError(f"Expected {EXPECTED_HEADINGS} visible headings, found {len(word_hits)}")
    if docx_suite_count != EXPECTED_HEADINGS:
        raise RuntimeError(f"Expected {EXPECTED_HEADINGS} DOCX suite mentions, found {docx_suite_count}")
    update_global_audit()
    append_reports(manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
