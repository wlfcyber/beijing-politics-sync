from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


RECOVERY = Path(__file__).resolve().parent
STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"
UPLOAD_SCOPE = RECOVERY / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md"
MANIFEST = RECOVERY / "YANQING_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json"
RENDER_MANIFEST = RECOVERY / "word_render_qa_20260525_global_style_norm" / "render_manifest.json"


def replace_last_status(text: str) -> str:
    old = "Status: `RECOVERED_EXECUTION_IN_PROGRESS`"
    new = "Status: `RECOVERED_EXECUTION_IN_PROGRESS_LOCAL_BODY_EVIDENCE_CLEARED_AFTER_YANQING_REPAIR_MODEL_GATES_OPEN`"
    if old in text:
        return text.replace(old, new, 1)
    return text


def append_once(path: Path, marker: str, section: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        text = text[: text.index(marker)].rstrip() + "\n"
    path.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M +08")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    render = json.loads(RENDER_MANIFEST.read_text(encoding="utf-8"))

    status_text = replace_last_status(STATUS.read_text(encoding="utf-8"))
    STATUS.write_text(status_text, encoding="utf-8", newline="\n")

    common = {
        "updated": now,
        "q18_before": manifest["q18_blocks_before"],
        "q18_after": manifest["q18_blocks_after"],
        "removed_paragraphs": manifest["q18_removed_paragraphs"],
        "rows_changed": manifest["rows_changed"],
        "risk_rows": 308,
        "in_body_rows": 433,
        "in_body_risk_rows": 0,
        "pages": render["pdf_pages"],
        "rendered": render["rendered_png_count"],
        "docx_labels": render["docx_label_count"],
        "pdf_labels": render["pdf_label_count"],
        "blank": len(render["blank_like_pages_excluding_cover_foreword"]),
        "docx_bytes": render["docx_bytes"],
        "pdf_bytes": render["pdf_bytes"],
    }

    append_once(
        STATUS,
        "## Yanqing 2025 Yimo Candidate Queue Repair",
        f"""
## Yanqing 2025 Yimo Candidate Queue Repair
Updated: {common['updated']}

- Status: `YANQING_2025_YIMO_REPAIRED_LOCAL_QA_PASS_MODEL_GATES_OPEN`.
- DOCX repair: Q18 headings `{common['q18_before']} -> {common['q18_after']}`; removed paragraphs `{common['removed_paragraphs']}` after backup.
- Matrix repair: `{common['rows_changed']}` 2025延庆一模 rows updated; refreshed audit now shows matrix rows `1471`, in-book/body rows `{common['in_body_rows']}`, total risk rows `{common['risk_rows']}`, in-book/body risk rows `{common['in_body_risk_rows']}`.
- DOCX/PDF after repair and re-export: rendered pages `{common['rendered']}/{common['pages']}`, label counts `{common['docx_labels']}/{common['pdf_labels']}`, blank-like body pages `{common['blank']}`.
- Evidence: `YANQING_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md`, `CURRENT_DOCX_2025_YANQING_Q18_CONTEXT_20260525.md`, `CURRENT_DOCX_2025_YANQING_Q21_CONTEXT_20260525.md`, refreshed `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md`, refreshed `FORMAT_RENDER_QA_20260524.md`.
- External gates remain open: GPTPro web review `real_call_pending`; Claude Opus web/app review `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
""",
    )

    append_once(
        GOVERNOR,
        "## Governor Finding: Yanqing 2025 Yimo Candidate Queue Repair",
        f"""
## Governor Finding: Yanqing 2025 Yimo Candidate Queue Repair
Updated: {common['updated']}

- Governor decision: `LOCAL_DOCX_MISPLACEMENT_REMOVED_AND_MATRIX_CLOSED_MODEL_GATES_OPEN`.
- Finding: 2025延庆一模Q18 was present twice in the current DOCX even though its source question belongs to 《逻辑与思维》/辩证思维. This was a real body-placement defect.
- Corrective action: backed up the current DOCX, removed both Q18 body blocks, regenerated the PDF, and refreshed render QA.
- Verification: Q18 headings `{common['q18_before']} -> {common['q18_after']}`; low-altitude-economy probe now has `0` current-DOCX hits; Q21 remains present as one Bixiu4-relevant current-DOCX block.
- Matrix result: `{common['rows_changed']}` Yanqing rows updated. Q1-Q15 are choice-key boundaries; Q16 is formal-rubric covered; Q17/Q19/Q20 are module-boundary exclusions; Q18 is removed/excluded; Q21 keeps only Bixiu4-relevant scoring points.
- Refreshed audit: total risk rows `{common['risk_rows']}`, in-book/body risk rows `{common['in_body_risk_rows']}`.
- Render result: `{common['rendered']}/{common['pages']}` pages, label counts `{common['docx_labels']}/{common['pdf_labels']}`, blank-like body pages `{common['blank']}`.
- Boundary: this is local source/DOCX/rubric repair only. GPTPro web and Claude Opus web/app reviews remain `real_call_pending`; no final acceptance claim or early GitHub push is authorized.
""",
    )

    append_once(
        CONFUCIUS,
        "## Artifact Check: Yanqing 2025 Yimo Candidate Queue Repair",
        f"""
## Artifact Check: Yanqing 2025 Yimo Candidate Queue Repair
Updated: {common['updated']}

- `repair_2025_yanqing_yimo_candidate_queue_20260525.py`: present.
- `clean_yanqing_q16_false_pending_wording_20260525.py`: present.
- `YANQING_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md`: present and status `YANQING_2025_YIMO_CANDIDATE_QUEUE_REPAIRED`.
- `YANQING_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json`: present.
- DOCX backup before Q18 removal: present at `{manifest['docx_backup']}`.
- Matrix backup before Yanqing rewrite: present at `{manifest['matrix_backup']}`.
- `CURRENT_DOCX_2025_YANQING_Q18_CONTEXT_20260525.md`: present; target headings `0` after repair.
- `CURRENT_DOCX_2025_YANQING_Q21_CONTEXT_20260525.md`: present; target headings `1`.
- `CURRENT_DOCX_2025_YANQING_PROBE_20260525.md`: refreshed; low-altitude-economy hits `0`.
- Refreshed audit: matrix rows `1471`, in-book/body rows `{common['in_body_rows']}`, total risk rows `{common['risk_rows']}`, in-book/body risk rows `{common['in_body_risk_rows']}`.
- Refreshed render QA: `{common['rendered']}/{common['pages']}` pages, label counts `{common['docx_labels']}/{common['pdf_labels']}`, blank-like body pages `{common['blank']}`.
- Remaining open gates: GPTPro web review, Claude web/app Opus 4.7 review through direct `https://claude.ai`, ClaudeCode model confirmation, full manual typography pass, and deferred ORDER_063 final GitHub upload.
""",
    )

    append_once(
        FORMAT_QA,
        "## Yanqing Q18 Removal Render QA 20260525",
        f"""
## Yanqing Q18 Removal Render QA 20260525

- Status: `RENDER_PASS_AFTER_YANQING_Q18_REMOVAL_MODEL_GATES_OPEN`.
- DOCX bytes: `{common['docx_bytes']}`.
- PDF bytes: `{common['pdf_bytes']}`.
- PDF pages/rendered PNGs: `{common['pages']}/{common['rendered']}`.
- DOCX/PDF label counts: `{common['docx_labels']}/{common['pdf_labels']}`.
- Blank-like body pages excluding cover/foreword: `{common['blank']}`.
- Yanqing Q18 target headings after repair: `0`.
- Yanqing low-altitude-economy current-DOCX hits after repair: `0`.
- Contact sheet: `{render['contact_sheet']}`.
- Boundary: render QA passes automated checks after the removal, but GPTPro/Claude Opus web external reviews remain `real_call_pending`.
""",
    )

    append_once(
        MODEL_LEDGER,
        "## MODEL_GATE_SUMMARY_AFTER_YANQING_LOCAL_REPAIR_20260525",
        f"""
## MODEL_GATE_SUMMARY_AFTER_YANQING_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- 2025延庆一模 Q18/Q21 repair was performed by local source/DOCX/matrix verification only.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local repair.
- Claude web/app route remains direct `https://claude.ai` auto-login; no Google-login loop is valid.
- Claude web/app external review remains `real_call_pending`.
- GPTPro web external review remains `real_call_pending`.
- ClaudeCode post-repair model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` because prior runtime/debug evidence includes auxiliary Haiku alongside Opus.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
""",
    )

    upload_text = UPLOAD_SCOPE.read_text(encoding="utf-8")
    upload_text = upload_text.replace(
        "Reason: 蹇呬慨鍥?recovery still has open gates, including row-level risk adjudication and external model-review gates.",
        "Reason: 蹇呬慨鍥?recovery still has open external model-review and final typography/upload gates; local in-body evidence audit is currently `0` in-book/body risk rows after Yanqing repair.",
    )
    UPLOAD_SCOPE.write_text(upload_text, encoding="utf-8", newline="\n")
    append_once(
        UPLOAD_SCOPE,
        "## Yanqing Repair Artifacts To Consider",
        f"""
## Yanqing Repair Artifacts To Consider

Updated: {common['updated']}

- Include the Yanqing repair report, manifest, DOCX backup pointer, matrix backup pointer, refreshed Q18/Q21/probe files, refreshed matrix audit, refreshed Word/PDF QA, and updated Governor/Confucius/status ledgers in the future upload scope.
- Do not upload now. ORDER_063 still requires all active Beijing politics lines to end first, then exact upload scope, secret-pattern scan, `NO_SECRET_PATTERN_MATCHES`, commit, push, upload report, and final heartbeat.
""",
    )

    print(json.dumps({"status": "synced", **common}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
