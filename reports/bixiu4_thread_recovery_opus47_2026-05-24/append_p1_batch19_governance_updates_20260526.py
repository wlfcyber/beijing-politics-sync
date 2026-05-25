from __future__ import annotations

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M +08")


def upsert_section(path: Path, marker: str, section: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    start = text.find(marker)
    if start >= 0:
        text = text[:start].rstrip()
    path.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    updated = now()

    status_section = f"""
## P1 Thickness Batch19 Recovery Update 20260526

- Updated: {updated}
- Status: `RECOVERED_EXECUTION_IN_PROGRESS_P1_BATCH19_APPLIED_GATES_OPEN`.
- Created inspection artifact: `P1_SUBJECTIVE_CANDIDATE_INSPECTION_20260526.md`.
- Created repair script: `apply_p1_thickness_batch19_20260526.py`.
- Created draft/apply artifacts:
  - `P1_THICKNESS_REPAIR_BATCH19_DRAFT_20260526.md`
  - `P1_THICKNESS_REPAIR_BATCH19_DRAFT_20260526.csv`
  - `P1_THICKNESS_REPAIR_BATCH19_DRAFT_20260526.json`
  - `P1_THICKNESS_REPAIR_BATCH19_APPLY_20260526.md`
  - `P1_THICKNESS_REPAIR_BATCH19_APPLY_20260526.csv`
  - `P1_THICKNESS_REPAIR_BATCH19_APPLY_20260526.json`
- DOCX backup before repair: `05_delivery/*_backup_before_p1_thickness_batch19_20260526_011733.docx`.
- Local repair scope: first 16 P1 subjective thin rows that had row-level support from formal scoring/rubric or formal marking-rule matrix evidence.
- Applied rows: T0047, T0199, T0282, T0404, T0307, T0074, T0057, T0233, T0345, T0467, T0187, T0188, T0213, T0061, T0062, T0144.
- Matrix evidence cited in apply artifact: M1095, M1100, M1098, M1102, M0031, M1030-M1037, M1203, M1248, M0177/M0209/M0424, M1244, M0012/M0240, M0020, M0004, M1436, M0014, M0011/M0240.
- Evidence boundary:
  - Batch19 did not use ordinary reference answers as scoring rubrics;
  - all selected rows were accepted only because the current matrix contained formal scoring/rubric or formal marking-rule support;
  - Sonnet, Haiku, and model-unknown outputs remain excluded from qualified model evidence.
- Refreshed thickness result after Batch19: thin candidates `475` out of `721`; priority counts P0 `0`, P1 `243`, P2 `207`, P3 `25`.
- Refreshed grouping after Batch19: legacy `232`, inserted `243`; subjective `347`, choice `128`.
- Refreshed flag counts after Batch19: `ANSWER_LT_120_CHARS` 282, `WHY_LT_90_CHARS` 76, `SHORT_WITHOUT_POINT_MARKERS` 406.
- Cumulative local repairs in this recovery thread: at least `168` rows, including `152` P0 rows and `16` P1 rows.
- Re-export/render result after DOCX edit: render timestamp `20260526_011902`; DOCX bytes `472132`; PDF bytes `4704473`; PDF pages/rendered PNGs `308/308`; DOCX/PDF label counts `2891/2891`; blank-like body pages `0`.
- Every-page visual QA refreshed: `308` rows, metric review-required rows `0`, regenerated contact sheets pages `001-308` opened and reviewed at thumbnail level.
- Tail-page check: pages `301-308` contain visible content and footers; no tail blanking detected.
- Current blockers:
  - thickness queue remains open: P1 `243`, P2 `207`, P3 `25`;
  - current-version GPTPro/Claude external review is `real_call_pending`;
  - ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`;
  - ORDER_063 upload remains deferred; no GitHub push attempted.
"""

    model_section = f"""
## MODEL_GATE_P1_THICKNESS_BATCH19_20260526

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_P1_BATCH19_APPLIED`

- Updated: {updated}
- Local repair artifacts:
  - `inspect_p1_subjective_candidates_20260526.py`
  - `P1_SUBJECTIVE_CANDIDATE_INSPECTION_20260526.md`
  - `apply_p1_thickness_batch19_20260526.py`
  - `P1_THICKNESS_REPAIR_BATCH19_DRAFT_20260526.md/.csv/.json`
  - `P1_THICKNESS_REPAIR_BATCH19_APPLY_20260526.md/.csv/.json`
- Local validation after repair:
  - DOCX zip structural check: `true`;
  - DOCX style consistency audit: `PASS`;
  - refreshed thickness queue: total candidates `475`, P0 `0`, P1 `243`, P2 `207`, P3 `25`;
  - Word/PDF render: timestamp `20260526_011902`, `308/308` pages, label counts `2891/2891`, blank-like body pages `0`;
  - every-page metric QA: `308` rows, review-required rows `0`;
  - contact-sheet visual review: pages `001-308` reviewed, pages `301-308` confirmed visible content/footer.
- Model-evidence boundary:
  - this is local Codex production repair and QA, not new GPTPro, Claude web/app, or ClaudeCode evidence;
  - the current DOCX/PDF changed after previous external web reviews, so current-version GPTPro/Claude external review remains pending after remaining thickness gates are handled or explicitly bounded;
  - if a Claude web/app retry is attempted, use direct `https://claude.ai` auto-login instead of any Google-login path.
- Sonnet, Haiku, and model-unknown outputs remain excluded from qualified evidence.
- ClaudeCode production-lane replacement evidence remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""

    governor_section = f"""
## Governor P1 Thickness Batch19 Update 20260526

Updated: {updated}

Status: `PASS_LOCAL_BATCH19_P1_INCREMENT_WITH_OPEN_GATES`

- What changed: 16 P1 subjective thin rows were locally thickened in the DOCX under their existing framework nodes.
- Precision guard: every edited row was matched by exact heading plus current queue old-answer excerpt; duplicate same-question rows in other nodes were not overwritten.
- Evidence guard:
  - Batch19 used only rows with current row-level matrix support from formal scoring/rubric or formal marking-rule evidence;
  - ordinary reference answers were not upgraded into scoring rubrics;
  - Sonnet/Haiku/model-unknown material was not used as qualified model evidence.
- Verification:
  - DOCX backup exists before edit;
  - DOCX structural zip check passed;
  - style consistency audit passed;
  - refreshed thickness queue dropped from 491 to 475 candidates and P1 from 259 to 243;
  - PDF re-export/render passed at `308/308` pages with no blank-like body pages;
  - regenerated contact sheets for pages `001-308` were opened and thumbnail-reviewed, including tail pages `301-308`.
- Governor verdict: local Batch19 is accepted as an incremental P1 repair. The line remains non-terminal because P1/P2/P3 thickness candidates remain and current-version external review is pending.
- Claude web/app retry rule: direct `https://claude.ai` auto-login is the required path; do not record this as Google-login failure.
- Upload rule: ORDER_063 remains deferred; Batch19 artifacts must be included in the eventual upload scope, but no push is allowed while gates remain open.
"""

    confucius_section = f"""
## Confucius P1 Thickness Batch19 Artifact Check 20260526

Updated: {updated}

Status: `ARTIFACTS_PRESENT_BATCH19_P1_INCREMENT_GATES_OPEN`

- Inspection artifact present: `P1_SUBJECTIVE_CANDIDATE_INSPECTION_20260526.md`.
- Draft artifacts present: `P1_THICKNESS_REPAIR_BATCH19_DRAFT_20260526.md/.csv/.json`.
- Apply artifacts present: `P1_THICKNESS_REPAIR_BATCH19_APPLY_20260526.md/.csv/.json`.
- Repair script present: `apply_p1_thickness_batch19_20260526.py`.
- Backup present: current DOCX has a `backup_before_p1_thickness_batch19` copy in `05_delivery`.
- Refreshed QA artifacts present:
  - `THICKNESS_DENSITY_AUDIT_20260525.md/.csv`;
  - `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.md/.csv/.json`;
  - `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md/.json`;
  - `word_render_qa_20260525_heading_style_fix/render_manifest.json`;
  - `EVERY_PAGE_VISUAL_QA_LOG_20260525.md/.csv/.json`;
  - `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`.
- Student-learning boundary: P0 is still cleared, but 475 thinner rows remain across P1/P2/P3; the whole handbook is not yet uniformly thick for zero-baseline learners.
- External boundary: current-version GPTPro/Claude review remains pending, and ClaudeCode model confirmation remains blocked.
"""

    format_section = f"""
## P1 Batch19 Render/Format Delta 20260526

Updated: {updated}

- Status: `RENDER_PASS_AFTER_P1_BATCH19_GATES_OPEN`.
- Render timestamp: `20260526_011902`.
- DOCX bytes: `472132`.
- PDF bytes: `4704473`.
- PDF pages/rendered PNGs: `308/308`.
- DOCX/PDF label counts: `2891/2891`.
- Blank-like body pages: `0`.
- Every-page visual metric rows: `308`; review-required rows `0`.
- Contact-sheet review: pages `001-308` opened at thumbnail level; no obvious full-page blank, missing page, severe clipping, page-order break, or page-scale layout drift. Pages `301-308` are visible tail pages with content/footer.
- Boundary: this is render/format QA after local Batch19 only; it does not close remaining P1/P2/P3 thickness or model gates.
"""

    contact_section = f"""
# Every Page Visual QA Contact Sheet Review 20260525

Updated: {updated}

Status: `CONTACT_SHEETS_REVIEWED_AFTER_P1_BATCH19`

- Render basis: `word_render_qa_20260525_heading_style_fix/render_manifest.json`.
- Render timestamp: `20260526_011902`.
- PDF pages / rendered PNGs: `308/308`.
- Contact sheets opened: `11`.
- Page ranges reviewed:
  - `001-030`
  - `031-060`
  - `061-090`
  - `091-120`
  - `121-150`
  - `151-180`
  - `181-210`
  - `211-240`
  - `241-270`
  - `271-300`
  - `301-308`
- Metric review-required rows: `0`.
- Blank-like body pages: `0`.
- Visual thumbnail finding: no obvious full-page blank, missing page, severe clipping, page-order break, or page-scale layout drift was visible in the 11 regenerated contact sheets.
- Note: pages `301-308` are visible tail pages with content and footers, not blank pages.

## Boundary

- This is a thumbnail-level visual review plus metric screen, not 100 percent zoom proofreading of every character.
- It verifies rendering stability after P1 thickness Batch19.
- It does not close the remaining P1/P2/P3 thickness queue, ClaudeCode model-confirmation gate, or later GPTPro/Claude external-review gates.
"""

    upload_section = f"""
## Deferred Upload Scope Addition: P1 Batch19 20260526

Updated: {updated}

When ORDER_063 eventually permits the final GitHub upload, include these additional recovery-line artifacts in the upload scope:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/inspect_p1_subjective_candidates_20260526.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P1_SUBJECTIVE_CANDIDATE_INSPECTION_20260526.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/apply_p1_thickness_batch19_20260526.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/append_p1_batch19_governance_updates_20260526.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P1_THICKNESS_REPAIR_BATCH19_DRAFT_20260526.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P1_THICKNESS_REPAIR_BATCH19_DRAFT_20260526.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P1_THICKNESS_REPAIR_BATCH19_DRAFT_20260526.json`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P1_THICKNESS_REPAIR_BATCH19_APPLY_20260526.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P1_THICKNESS_REPAIR_BATCH19_APPLY_20260526.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P1_THICKNESS_REPAIR_BATCH19_APPLY_20260526.json`
- refreshed `THICKNESS_DENSITY_AUDIT_20260525.*` and `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.*`
- refreshed `FORMAT_RENDER_QA_20260524.md`
- refreshed `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.*`
- refreshed `word_render_qa_20260525_heading_style_fix/`
- refreshed `EVERY_PAGE_VISUAL_QA_LOG_20260525.*`, `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`, and `every_page_visual_qa_20260525/`
- current DOCX/PDF after Batch19 and the `backup_before_p1_thickness_batch19` DOCX backup.

Upload remains deferred. Before any final push, generate a concrete upload-scope file, scan the selected scope for secret patterns, require `NO_SECRET_PATTERN_MATCHES`, then commit and push only selected project artifacts to `origin https://github.com/wlfcyber/beijing-politics-sync.git`.
"""

    upload_binding_section = f"""
## Final Upload Binding Refresh After P1 Batch19 20260526

Updated: {updated}

- User hard instruction is active: do not push now.
- Final GitHub upload is allowed only after all active Beijing politics lines enter a clear terminal state or a user-approved blocker state.
- At that later point, this Bixiu4 recovery line must contribute the final deliverables, coverage matrix, Claude/GPT records, Governor/Confucius reports, Word/PDF QA, render artifacts, and process logs to the upload scope.
- Required future pre-push gate remains: exact upload scope first, sensitive-information scan second, upload report recording `NO_SECRET_PATTERN_MATCHES` third, then selective commit/push.
- Current line state remains open-gate: P0 `0`, P1 `243`, P2 `207`, P3 `25`, GPTPro/Claude current-version external review `real_call_pending`, ClaudeCode model confirmation `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- The prohibited terminal acceptance label must not be used for this line while these gates remain open.
"""

    claude_boundary = f"""
## Current Boundary After P1 Batch19
Updated: {updated}

- Direct `https://claude.ai` remains the required retry path for any further Claude web/app review.
- No new Claude web/app external review has been completed after P1 Batch19 changed the DOCX/PDF.
- Current-version Claude Opus 4.7 adaptive-thinking full-artifact review remains `real_call_pending`.
- The next retry must use the already signed-in direct Claude session and must not use the Google login button.
"""

    upsert_section(ROOT / "THREAD_RECOVERY_STATUS_20260524.md", "## P1 Thickness Batch19 Recovery Update 20260526", status_section)
    upsert_section(ROOT / "MODEL_EVIDENCE_LEDGER.md", "## MODEL_GATE_P1_THICKNESS_BATCH19_20260526", model_section)
    upsert_section(ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md", "## Governor P1 Thickness Batch19 Update 20260526", governor_section)
    upsert_section(ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md", "## Confucius P1 Thickness Batch19 Artifact Check 20260526", confucius_section)
    upsert_section(ROOT / "FORMAT_RENDER_QA_20260524.md", "## P1 Batch19 Render/Format Delta 20260526", format_section)
    upsert_section(
        ROOT / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
        "## Deferred Upload Scope Addition: P1 Batch19 20260526",
        upload_section,
    )
    upsert_section(
        ROOT / "ORDER_063_BIXIU4_UPLOAD_DEFERRED_ACK_20260525.md",
        "## Final Upload Binding Refresh After P1 Batch19 20260526",
        upload_binding_section,
    )
    upsert_section(ROOT / "CLAUDE_WEB_LOGIN_CORRECTION_20260525.md", "## Current Boundary After P1 Batch19", claude_boundary)
    (ROOT / "EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md").write_text(
        contact_section.strip() + "\n", encoding="utf-8", newline="\n"
    )
    print("updated governance files for P1 Batch19")


if __name__ == "__main__":
    main()
