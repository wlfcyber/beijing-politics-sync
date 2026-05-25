from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
NOW = datetime.now().strftime("%Y-%m-%d %H:%M +08")


def read_json(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def append_once(name: str, marker: str, block: str) -> None:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    if text and not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n" + block.strip() + "\n", encoding="utf-8")


audit = read_json("DOCX_STYLE_CONSISTENCY_AUDIT_20260525.json")
manifest = read_json("word_render_qa_20260525_heading_style_fix/render_manifest.json")

status = "RECOVERED_EXECUTION_IN_PROGRESS_HEADING_STYLE_QA_PASS_MODEL_GATES_OPEN"
marker = "HEADING_STYLE_CONSISTENCY_FIX_GOVERNANCE_20260525"
sample_pages = "019, 034, 044, 081, 112, 133, 153, 173, 209, 221, 251, 280"

common_lines = f"""
- Updated: {NOW}
- Status: `{status}`.
- Independent DOCX style audit: `{audit['status']}` with `{audit['question_entry_count']}` question entries, inserted/legacy `{audit['inserted_entry_count']}/{audit['legacy_entry_count']}`.
- Missing ledger headings in current DOCX: `{audit['missing_ledger_heading_count']}`; missing required label blocks: `{audit['missing_label_count']}`; duplicate required label blocks: `{audit['duplicate_label_count']}`.
- Heading paragraph/run-property variants after fix: `{audit['heading_ppr_variant_count']}/{audit['heading_rpr_variant_count']}`.
- Required label first-run style variants after fix: one variant each for material-trigger, question, reasoning, and answer-landing labels.
- Render QA after Word-compatible fix: `{manifest['rendered_png_count']}/{manifest['pdf_pages']}` pages rendered, DOCX/PDF label counts `{manifest['docx_label_count']}/{manifest['pdf_label_count']}`, blank-like body pages `{len(manifest['blank_like_pages_excluding_cover_foreword'])}`.
- Visual spot check: contact sheet `word_render_qa_20260525_heading_style_fix/heading_style_fix_contact_sheet.png` was opened and sampled pages `{sample_pages}` showed no obvious blank page, text overlap, or clipping.
- Integrity checks after fix: current DOCX zip test passed, no `~$*` Word temp lock was found, and no `WINWORD` process remained.
- Rollback note: the raw XML normalization attempt was rolled back after Word rejected the output; the retained fix is the python-docx API normalization plus successful Word COM PDF export.
- Boundary: this was a local formatting/style repair. Matrix content, row-level source evidence, and body placement decisions were not reinterpreted by this operation.
- External gates remain open: GPTPro web full artifact review `real_call_pending`; Claude Opus 4.7 web/app full DOCX/PDF review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No Sonnet, Haiku, or model-unknown output is counted as qualified evidence.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines plus upload scope and secret scan.
""".strip()

append_once(
    "THREAD_RECOVERY_STATUS_20260524.md",
    marker,
    f"""
## {marker}

{common_lines}
""",
)

append_once(
    "GOVERNOR_RECOVERY_REPORT_20260524.md",
    marker,
    f"""
## Governor Finding: Heading Style Consistency Fix

{common_lines}
- Governor decision: `LOCAL_HEADING_STYLE_CONSISTENCY_RENDER_PASS_MODEL_GATES_OPEN`.
- Acceptance boundary: local Word/PDF formatting evidence is stronger than before, but it does not close GPTPro, Claude Opus 4.7 web/app, or ClaudeCode model-confirmation gates.
""",
)

append_once(
    "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md",
    marker,
    f"""
## Artifact Check: Heading Style Consistency Fix

{common_lines}
- Present artifacts: `docx_style_consistency_audit_20260525.py`, `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md/.json`, `normalize_question_heading_rpr_docxapi_20260525.py`, `HEADING_STYLE_CONSISTENCY_FIX_DOCXAPI_20260525.md/.json`, `render_after_heading_style_fix_20260525.py`, `word_render_qa_20260525_heading_style_fix/render_manifest.json`, and the contact sheet.
- Process artifacts retained: the rolled-back raw XML attempt script/report remain process evidence and must not be treated as the retained DOCX patch.
- Zero-baseline learner boundary: old/new entry visual mismatch is closed structurally, but full external learner-model review remains pending.
""",
)

append_once(
    "MODEL_EVIDENCE_LEDGER.md",
    marker,
    f"""
## MODEL_GATE_AFTER_HEADING_STYLE_CONSISTENCY_FIX_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_FORMAT_REPAIR_ONLY`

{common_lines}
- This section records local DOCX/PDF style QA only and adds no qualifying ClaudeCode, Claude web/app, or GPTPro web evidence.
- Correct future Claude web/app route remains direct `https://claude.ai` using the already logged-in session; do not use the Google-login loop.
""",
)

append_once(
    "FORMAT_RENDER_QA_20260524.md",
    marker,
    f"""
## Heading Style Consistency Visual QA Clean Summary 20260525

{common_lines}
- Clean label summary: material-trigger, question, why-this-principle, and answer-landing labels each appear `{audit['question_entry_count']}` times in the DOCX audit.
- The current retained render evidence is `word_render_qa_20260525_heading_style_fix`.
""",
)

append_once(
    "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
    marker,
    f"""
## ORDER_063 Binding Refresh After Heading Style Consistency Fix

{common_lines}
- Add to future upload scope candidates: `docx_style_consistency_audit_20260525.py`, `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md/.json`, `normalize_question_heading_rpr_docxapi_20260525.py`, `HEADING_STYLE_CONSISTENCY_FIX_DOCXAPI_20260525.md/.json`, `render_after_heading_style_fix_20260525.py`, `word_render_qa_20260525_heading_style_fix/`, refreshed `FORMAT_RENDER_QA_20260524.md`, refreshed `GOVERNOR_RECOVERY_REPORT_20260524.md`, refreshed `CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md`, refreshed `THREAD_RECOVERY_STATUS_20260524.md`, refreshed `MODEL_EVIDENCE_LEDGER.md`, and the current DOCX/PDF in `05_delivery`.
- Include process logs/reports for the rolled-back raw XML attempt only as process history, not as the retained patch.
- Upload remains deferred. Do not push now; final upload still requires all active Beijing politics lines to reach terminal or user-approved blocker state, then exact upload scope, secret-pattern scan, `NO_SECRET_PATTERN_MATCHES`, commit, push, upload report, and final heartbeat.
""",
)

print(marker)
