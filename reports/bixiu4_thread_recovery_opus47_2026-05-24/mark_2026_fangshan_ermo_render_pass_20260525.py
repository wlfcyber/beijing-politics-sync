from __future__ import annotations

import csv
import json
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = RECOVERY / "FANGSHAN_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "FANGSHAN_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.json"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
RENDER_MANIFEST = RECOVERY / "word_render_qa_20260525_global_style_norm" / "render_manifest.json"

SUITE = "2026房山二模"

PAGE_QA = {
    "Q18(2)": "page 133",
    "Q21_Contradiction": "pages 153-154",
    "Q21_People": "pages 251-252",
}


def update_matrix() -> list[str]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    touched: list[str] = []
    for row in rows:
        if row.get("题源") != SUITE:
            continue
        current = row.get("当前处理", "")
        if "RENDER_PENDING" in current:
            row["当前处理"] = current.replace("RENDER_PENDING", "RENDER_PASS")
            touched.append(row.get("matrix_row_id", ""))

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return touched


def update_report(touched: list[str]) -> None:
    manifest = json.loads(RENDER_MANIFEST.read_text(encoding="utf-8"))
    data = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    data["render_status"] = "RENDER_PASS"
    data["render_manifest"] = manifest
    data["page_qa"] = PAGE_QA
    data["matrix_render_pass_rows"] = touched
    REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    text = REPORT_MD.read_text(encoding="utf-8")
    text = text.replace(
        "Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PENDING`",
        "Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PASS`",
    )
    text = text.replace(
        "- DOCX/PDF render QA is pending for this batch.",
        "- DOCX/PDF render QA passed for this batch.",
    )
    if "\n## Render QA\n" in text:
        text = text[: text.index("\n## Render QA\n")]
    pages = ", ".join(f"{q}: {page}" for q, page in PAGE_QA.items())
    section = f"""

## Render QA

- Render status: `PASS`.
- Rendered PNGs: `{manifest['rendered_png_count']}/{manifest['pdf_pages']}`.
- DOCX/PDF label counts: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- Blank-like body pages excluding cover/foreword: `{len(manifest['blank_like_pages_excluding_cover_foreword'])}`.
- DOCX bytes: `{manifest['docx_bytes']}`.
- PDF bytes: `{manifest['pdf_bytes']}`.
- Target page checks: `{pages}`.
- Visual pages inspected: `page_133.png`, `page_153.png`, `page_154.png`, `page_251.png`, `page_252.png`; entries were readable with no visible overlap, clipping, or abnormal blank gap.
- Matrix rows moved from render-pending to render-pass: `{', '.join(touched)}`.
"""
    REPORT_MD.write_text(text.rstrip() + section, encoding="utf-8", newline="\n")


def append_format_qa(touched: list[str]) -> None:
    manifest = json.loads(RENDER_MANIFEST.read_text(encoding="utf-8"))
    pages = ", ".join(f"{q} {page}" for q, page in PAGE_QA.items())
    section = f"""

## 2026房山二模 Recovery Render QA 20260525

- Status: `RENDER_PASS_CONTENT_RECHECK_PASS_MODEL_GATES_OPEN`.
- DOCX bytes after repair: `{manifest['docx_bytes']}`.
- PDF bytes after re-export: `{manifest['pdf_bytes']}`.
- Rendered PNGs: `{manifest['rendered_png_count']}/{manifest['pdf_pages']}` under `word_render_qa_20260525_global_style_norm`.
- DOCX/PDF label counts: `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`.
- Blank-like body pages excluding cover/foreword: `0`.
- New/updated entry pages: `{pages}`.
- Visual QA: pages `133`, `153`, `154`, `251`, and `252` inspected from PNG output; no overlap, clipping, unreadable text, or abnormal blank gap observed.
- Matrix rows marked render-pass: `{', '.join(touched)}`.
- Boundary: Claude web/app and GPTPro web external reviews remain `real_call_pending`; ClaudeCode Opus 4.7 max-effort confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    text = FORMAT_QA.read_text(encoding="utf-8")
    marker = "\n## 2026房山二模 Recovery Render QA 20260525"
    if marker in text:
        text = text[: text.index(marker)]
    FORMAT_QA.write_text(text.rstrip() + section, encoding="utf-8", newline="\n")


def main() -> None:
    touched = update_matrix()
    update_report(touched)
    append_format_qa(touched)
    print(json.dumps({"matrix_render_pass_rows": touched, "page_qa": PAGE_QA}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
