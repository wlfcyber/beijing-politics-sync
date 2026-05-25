from __future__ import annotations

import csv
import importlib.util
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw


BASE_PATH = Path(__file__).with_name("render_batch32_word_qa_20260525.py")
spec = importlib.util.spec_from_file_location("render_batch32", BASE_PATH)
r32 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(r32)

r32.SUITE = "2026西城期末"
r32.EXPECTED_HEADINGS = 20
r32.OUTDIR = r32.RECOVERY / "word_render_qa_20260525_batch33_word"
r32.BATCH_REPORT = r32.RECOVERY / "COVERAGE_FUSION_BATCH33_2026_XICHENG_FINAL_CODEX_20260525.md"


def reset_outdir() -> None:
    if r32.OUTDIR.exists():
        if r32.OUTDIR.name != "word_render_qa_20260525_batch33_word" or r32.OUTDIR.parent != r32.RECOVERY:
            raise RuntimeError(f"Refusing to clear unexpected output directory: {r32.OUTDIR}")
        shutil.rmtree(r32.OUTDIR)
    r32.OUTDIR.mkdir(parents=True)


def make_contact_sheet(hit_pages: list[int]) -> str | None:
    if not hit_pages:
        return None
    thumbs = []
    for page_no in hit_pages:
        path = r32.OUTDIR / f"page_{page_no:03d}.png"
        img = Image.open(path).convert("RGB")
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
    out = r32.OUTDIR / "batch33_hit_pages_contact_sheet.png"
    sheet.save(out)
    for thumb in thumbs:
        thumb.close()
    return str(out)


def update_global_audit() -> None:
    with r32.GLOBAL_AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        rows = list(reader)
    for row in rows:
        if row.get("normalized_suite") == r32.SUITE:
            row["blocker_or_next_action"] = "Batch33 matrix/DOCX/render pass; ClaudeCode Opus 4.7 model-lane recheck pending."
    with r32.GLOBAL_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def append_reports(manifest: dict[str, object]) -> None:
    hit_pages = ", ".join(str(p) for p in manifest["suite_hit_pages"])
    blank_note = "`0`" if not manifest["blank_like_pages_excluding_cover_foreword"] else "`" + ", ".join(str(p) for p in manifest["blank_like_pages_excluding_cover_foreword"]) + "`"
    qa_append = f"""

## Batch33 Render QA: 2026西城期末
Updated: 2026-05-25

- Current DOCX bytes: `{manifest['docx_bytes']}`.
- Current PDF bytes: `{manifest['pdf_bytes']}`.
- PDF export was regenerated through local Word COM after Batch33 insertion/registration.
- Rendered PNGs were generated from the regenerated PDF with PyMuPDF under `word_render_qa_20260525_batch33_word`.
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
    text = r32.FORMAT_QA.read_text(encoding="utf-8")
    for marker in ["\n## Batch33 Pending Render QA: 2026西城期末", "\n## Batch33 Render QA: 2026西城期末"]:
        if marker in text:
            text = text[: text.index(marker)]
    r32.FORMAT_QA.write_text(text + qa_append, encoding="utf-8", newline="\n")

    report_text = r32.BATCH_REPORT.read_text(encoding="utf-8")
    marker = "\n## Render QA Result"
    if marker in report_text:
        report_text = report_text[: report_text.index(marker)]
    r32.BATCH_REPORT.write_text(report_text + f"""

## Render QA Result

- Render status: `RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING`.
- PDF pages/rendered PNGs: `{manifest['pdf_pages']}/{manifest['rendered_png_count']}`.
- DOCX/PDF label count: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- DOCX/Word-layout visible suite mentions: `{manifest['docx_suite_heading_count']}/{manifest['word_visible_heading_count']}`.
- Raw PDF exact text-extraction suite mentions: `{manifest['pdf_suite_text_count']}`.
- Hit pages: `{hit_pages}`.
- Manifest: `word_render_qa_20260525_batch33_word/render_manifest.json`.
""", encoding="utf-8", newline="\n")

    append_block = f"""

## Batch33 Render QA: 2026西城期末
Updated: 2026-05-25

- Status: `RENDER_PASS_CONTENT_RECHECK_PENDING_MODEL_PENDING`.
- DOCX/PDF label counts match: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- Visible suite headings match expected count: `{manifest['word_visible_heading_count']}/{r32.EXPECTED_HEADINGS}`.
- Blank-like body pages excluding cover/foreword: {blank_note}.
- ClaudeCode Opus 4.7 recheck remains pending; model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    for path in [r32.THREAD_STATUS, r32.GOVERNOR, r32.CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Batch33 Render QA: 2026西城期末"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + append_block, encoding="utf-8", newline="\n")


r32.reset_outdir = reset_outdir
r32.make_contact_sheet = make_contact_sheet
r32.update_global_audit = update_global_audit
r32.append_reports = append_reports


if __name__ == "__main__":
    raise SystemExit(r32.main())
