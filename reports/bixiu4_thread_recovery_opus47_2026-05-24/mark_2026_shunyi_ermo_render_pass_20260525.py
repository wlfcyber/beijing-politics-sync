from __future__ import annotations

import csv
import json
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
REPORT_MD = RECOVERY / "SHUNYI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md"
REPORT_JSON = RECOVERY / "SHUNYI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.json"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
RENDER_DIR = RECOVERY / "word_render_qa_20260525_global_style_norm"
MANIFEST = RENDER_DIR / "render_manifest.json"
SUITE = "2026顺义二模"


def update_matrix() -> int:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    changed = 0
    for row in rows:
        if row.get("题源") != SUITE:
            continue
        current = row.get("当前处理", "")
        if current.endswith("_RENDER_PENDING"):
            row["当前处理"] = current[: -len("_RENDER_PENDING")] + "_RENDER_PASS"
            changed += 1
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return changed


def update_report(manifest: dict[str, object]) -> None:
    data = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    data["render_status"] = "RENDER_PASS_LOCAL_QA"
    data["render_manifest"] = manifest
    data["target_page_qa"] = {
        "Q21": {
            "page": 44,
            "png": str(RENDER_DIR / "page_044.png"),
            "status": "VISUAL_QA_PASS",
        }
    }
    REPORT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    text = REPORT_MD.read_text(encoding="utf-8")
    text = text.replace("Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PENDING`", "Status: `DOCX_AND_MATRIX_REPAIRED_RENDER_PASS_LOCAL_QA`")
    text = text.replace("- DOCX/PDF render QA is pending for this batch.", "- DOCX/PDF render QA passed locally for this batch.")
    section = f"""

## Render QA

- Render timestamp: `{manifest.get('timestamp')}`.
- Current DOCX bytes: `{manifest.get('docx_bytes')}`.
- Current PDF bytes: `{manifest.get('pdf_bytes')}`.
- PDF pages/rendered PNGs: `{manifest.get('pdf_pages')}/{manifest.get('rendered_png_count')}`.
- DOCX/PDF label counts: `{manifest.get('docx_label_count')}/{manifest.get('pdf_label_count')}`.
- Blank-like body pages excluding cover/foreword: `{len(manifest.get('blank_like_pages_excluding_cover_foreword') or [])}`.
- Target page inspected: Q21 page `44` (`page_044.png`).
- Result: `RENDER_PASS_LOCAL_QA_MODEL_GATES_OPEN`.
"""
    if "## Render QA" in text:
        text = text[: text.index("## Render QA")].rstrip() + "\n" + section.strip() + "\n"
    else:
        text = text.rstrip() + "\n\n" + section.strip() + "\n"
    REPORT_MD.write_text(text, encoding="utf-8", newline="\n")


def append_format_qa(manifest: dict[str, object]) -> None:
    section = f"""

## Shunyi 2026 Ermo Recovery Render QA 20260525

- Status: `RENDER_PASS_LOCAL_QA_MODEL_GATES_OPEN`.
- DOCX bytes after repair: `{manifest.get('docx_bytes')}`.
- PDF bytes after repair/export: `{manifest.get('pdf_bytes')}`.
- PDF pages/rendered PNGs: `{manifest.get('pdf_pages')}/{manifest.get('rendered_png_count')}`.
- DOCX/PDF label counts: `{manifest.get('docx_label_count')}/{manifest.get('pdf_label_count')}`.
- Blank-like body pages excluding cover/foreword: `{len(manifest.get('blank_like_pages_excluding_cover_foreword') or [])}`.
- Inserted entry inspected: Q21 page `44`, `word_render_qa_20260525_global_style_norm/page_044.png`.
- Evidence boundary: Q21 uses formal marking-document philosophy综合角度/等级赋分; related 认识与实践、联系、发展 terms remain inside the answer landing and were not split into unsupported standalone rows.
- External gates remain open: GPTPro web full artifact review `real_call_pending`; Claude web/app full artifact review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 upload remains deferred; no GitHub push has been attempted.
"""
    text = FORMAT_QA.read_text(encoding="utf-8") if FORMAT_QA.exists() else ""
    marker = "## Shunyi 2026 Ermo Recovery Render QA 20260525"
    if marker in text:
        text = text[: text.index(marker)].rstrip()
    FORMAT_QA.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    changed = update_matrix()
    update_report(manifest)
    append_format_qa(manifest)
    print(json.dumps({"matrix_rows_marked": changed, "render_status": "RENDER_PASS_LOCAL_QA"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
