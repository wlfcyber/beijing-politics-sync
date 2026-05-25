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
## P0 Thickness Batch17 Recovery Update 20260526

- Updated: {updated}
- Status: `RECOVERED_EXECUTION_IN_PROGRESS_P0_BATCH17_APPLIED_GATES_OPEN`.
- Created repair script: `apply_p0_thickness_batch17_20260526.py`.
- Created draft/apply artifacts:
  - `P0_THICKNESS_REPAIR_BATCH17_DRAFT_20260526.md`
  - `P0_THICKNESS_REPAIR_BATCH17_DRAFT_20260526.csv`
  - `P0_THICKNESS_REPAIR_BATCH17_DRAFT_20260526.json`
  - `P0_THICKNESS_REPAIR_BATCH17_APPLY_20260526.md`
  - `P0_THICKNESS_REPAIR_BATCH17_APPLY_20260526.csv`
  - `P0_THICKNESS_REPAIR_BATCH17_APPLY_20260526.json`
- DOCX backup before repair: `05_delivery/*_backup_before_p0_thickness_batch17_20260526_003837.docx`.
- Local repair scope: 8 additional P0 subjective triple-thin rows with row-level matrix support from formal scoring/rubric sources.
- Applied rows: T0207, T0418, T0166, T0399, T0452, T0193, T0142, T0282.
- Deferred rows: P0 rows with only suite-level summary support were intentionally not repaired in this batch; they require later source recheck before any evidence claim.
- Refreshed thickness result after Batch17: thin candidates `507` out of `721`; priority counts P0 `16`, P1 `259`, P2 `207`, P3 `25`.
- Refreshed grouping after Batch17: legacy `248`, inserted `259`; subjective `379`, choice `128`.
- Refreshed flag counts after Batch17: `ANSWER_LT_120_CHARS` 314, `WHY_LT_90_CHARS` 92, `SHORT_WITHOUT_POINT_MARKERS` 438.
- Cumulative local P0 repairs in this recovery thread: `136`; P0 reduced from initial `152` to `16`.
- Re-export/render result after DOCX edit: render timestamp `20260526_003948`; DOCX bytes `465393`; PDF bytes `4666245`; PDF pages/rendered PNGs `304/304`; DOCX/PDF label counts `2891/2891`; blank-like body pages `0`.
- Every-page visual QA refreshed: `304` rows, metric review-required rows `0`, regenerated contact sheets pages `001-304` opened and reviewed at thumbnail level.
- Tail-page check: pages `301-304` contain visible content and footers; no tail blanking detected.
- Current blockers:
  - thickness queue remains open: 507 candidates remain, including P0 `16`;
  - current-version GPTPro/Claude external review is `real_call_pending`;
  - ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`;
  - ORDER_063 upload remains deferred; no GitHub push attempted.
"""

    model_section = f"""
## MODEL_GATE_P0_THICKNESS_BATCH17_20260526

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_P0_BATCH17_APPLIED`

- Updated: {updated}
- Local repair artifacts:
  - `apply_p0_thickness_batch17_20260526.py`
  - `P0_THICKNESS_REPAIR_BATCH17_DRAFT_20260526.md/.csv/.json`
  - `P0_THICKNESS_REPAIR_BATCH17_APPLY_20260526.md/.csv/.json`
- Local validation after repair:
  - DOCX zip structural check: `true`;
  - DOCX style consistency audit: `PASS`;
  - refreshed thickness queue: total candidates `507`, P0 `16`;
  - Word/PDF render: timestamp `20260526_003948`, `304/304` pages, label counts `2891/2891`, blank-like body pages `0`;
  - every-page metric QA: `304` rows, review-required rows `0`;
  - contact-sheet visual review: pages `001-304` reviewed, pages `301-304` confirmed visible content/footer.
- Model-evidence boundary:
  - this is local Codex production repair and QA, not new GPTPro, Claude web/app, or ClaudeCode evidence;
  - the current DOCX/PDF changed after previous external web reviews, so current-version external review remains pending after the remaining thickness queue is handled or explicitly bounded;
  - if a Claude web/app retry is attempted, use direct `https://claude.ai` auto-login instead of Google login.
- Sonnet, Haiku, and model-unknown outputs remain excluded from qualified evidence.
- ClaudeCode production-lane replacement evidence remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""

    governor_section = f"""
## Governor P0 Thickness Batch17 Update 20260526

Updated: {updated}

Status: `PASS_LOCAL_BATCH17_WITH_OPEN_GATES`

- What changed: 8 additional P0 subjective triple-thin rows were locally thickened in the DOCX under their existing evidence-supported framework nodes.
- Precision guard: every edited row was matched by exact heading plus current queue old-answer excerpt; duplicate same-question rows were not overwritten.
- Local evidence guard: Batch17 deliberately used rows with row-level current-matrix support from formal scoring/rubric sources. P0 rows with only suite-level summary support remain deferred for later source recheck.
- Verification:
  - DOCX backup exists before edit;
  - DOCX structural zip check passed;
  - style consistency audit passed;
  - refreshed thickness queue dropped from 515 to 507 candidates and P0 from 24 to 16;
  - PDF re-export/render passed at `304/304` pages with no blank-like body pages;
  - regenerated contact sheets for pages `001-304` were opened and thumbnail-reviewed, including new tail pages `301-304`.
- Governor verdict: local Batch17 is accepted as an incremental repair, but the line remains non-terminal because 507 thickness candidates remain and current-version external review is pending.
- Claude web/app blocker wording: do not record this as Google-login failure; if retried, direct `https://claude.ai` auto-login is the required path.
- Upload rule: ORDER_063 remains deferred; Batch17 artifacts must be included in the eventual upload scope, but no push is allowed while gates remain open.
"""

    confucius_section = f"""
## Confucius P0 Thickness Batch17 Artifact Check 20260526

Updated: {updated}

Status: `ARTIFACTS_PRESENT_BATCH17_REVIEWED_GATES_OPEN`

- Draft artifacts present: `P0_THICKNESS_REPAIR_BATCH17_DRAFT_20260526.md/.csv/.json`.
- Apply artifacts present: `P0_THICKNESS_REPAIR_BATCH17_APPLY_20260526.md/.csv/.json`.
- Repair script present: `apply_p0_thickness_batch17_20260526.py`.
- Backup present: current DOCX has a `backup_before_p0_thickness_batch17` copy in `05_delivery`.
- Refreshed QA artifacts present:
  - `THICKNESS_DENSITY_AUDIT_20260525.md/.csv`;
  - `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.md/.csv/.json`;
  - `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md/.json`;
  - `word_render_qa_20260525_heading_style_fix/render_manifest.json`;
  - `EVERY_PAGE_VISUAL_QA_LOG_20260525.md/.csv/.json`;
  - `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`.
- Student-learning boundary: 136 rows are now thicker across Batch01-Batch17, but 507 queue rows remain; the whole handbook is not yet uniformly thick for zero-baseline learners.
- External boundary: current-version GPTPro/Claude review remains pending, and ClaudeCode model confirmation remains blocked.
"""

    format_section = f"""
## P0 Batch17 Render/Format Delta 20260526

Updated: {updated}

- Status: `RENDER_PASS_AFTER_P0_BATCH17_GATES_OPEN`.
- Render timestamp: `20260526_003948`.
- DOCX bytes: `465393`.
- PDF bytes: `4666245`.
- PDF pages/rendered PNGs: `304/304`.
- DOCX/PDF label counts: `2891/2891`.
- Blank-like body pages: `0`.
- Every-page visual metric rows: `304`; review-required rows `0`.
- Contact-sheet review: pages `001-304` opened at thumbnail level; no obvious full-page blank, missing page, severe clipping, page-order break, or page-scale layout drift. Pages `301-304` are visible tail pages with content/footer.
- Boundary: this is render/format QA after local Batch17 only; it does not close remaining thickness or model gates.
"""

    contact_section = f"""
# Every Page Visual QA Contact Sheet Review 20260525

Updated: {updated}

Status: `CONTACT_SHEETS_REVIEWED_AFTER_P0_BATCH17`

- Render basis: `word_render_qa_20260525_heading_style_fix/render_manifest.json`.
- Render timestamp: `20260526_003948`.
- PDF pages / rendered PNGs: `304/304`.
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
  - `301-304`
- Metric review-required rows: `0`.
- Blank-like body pages: `0`.
- Visual thumbnail finding: no obvious full-page blank, missing page, severe clipping, page-order break, or page-scale layout drift was visible in the 11 regenerated contact sheets.
- Note: pages `301-304` are visible tail pages with content and footers, not blank pages.

## Boundary

- This is a thumbnail-level visual review plus metric screen, not 100 percent zoom proofreading of every character.
- It verifies rendering stability after P0 thickness Batch17.
- It does not close the remaining thickness queue, ClaudeCode model-confirmation gate, or later GPTPro/Claude external-review gates.
"""

    upload_section = f"""
## Deferred Upload Scope Addition: P0 Batch17 20260526

Updated: {updated}

When ORDER_063 eventually permits the final GitHub upload, include these additional recovery-line artifacts in the upload scope:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/apply_p0_thickness_batch17_20260526.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/append_p0_batch17_governance_updates_20260526.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH17_DRAFT_20260526.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH17_DRAFT_20260526.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH17_DRAFT_20260526.json`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH17_APPLY_20260526.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH17_APPLY_20260526.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH17_APPLY_20260526.json`
- refreshed `THICKNESS_DENSITY_AUDIT_20260525.*` and `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.*`
- refreshed `FORMAT_RENDER_QA_20260524.md`
- refreshed `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.*`
- refreshed `word_render_qa_20260525_heading_style_fix/`
- refreshed `EVERY_PAGE_VISUAL_QA_LOG_20260525.*`, `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`, and `every_page_visual_qa_20260525/`
- current DOCX/PDF after Batch17 and the `backup_before_p0_thickness_batch17` DOCX backup.

Upload remains deferred. Before any final push, generate a concrete upload-scope file, scan the selected scope for secret patterns, require `NO_SECRET_PATTERN_MATCHES`, then commit and push only selected project artifacts to `origin https://github.com/wlfcyber/beijing-politics-sync.git`.
"""

    upload_binding_section = f"""
## Final Upload Binding Refresh After P0 Batch17 20260526

Updated: {updated}

- User hard instruction is active: do not push now.
- Final GitHub upload is allowed only after all active Beijing politics lines enter a clear terminal state or a user-approved blocker state.
- At that later point, this Bixiu4 recovery line must contribute the final deliverables, coverage matrix, Claude/GPT records, Governor/Confucius reports, Word/PDF QA, render artifacts, and process logs to the upload scope.
- Required future pre-push gate remains: exact upload scope first, sensitive-information scan second, upload report recording `NO_SECRET_PATTERN_MATCHES` third, then selective commit/push.
- Current line state remains open-gate: P0 thickness `16`, total thickness queue `507`, GPTPro/Claude current-version external review `real_call_pending`, ClaudeCode model confirmation `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- The prohibited terminal acceptance label must not be used for this line while these gates remain open.
"""

    claude_boundary = f"""
## Current Boundary After P0 Batch17
Updated: {updated}

- Direct `https://claude.ai` remains the required retry path for any further Claude web/app review.
- No new Claude web/app external review has been completed after P0 Batch17 changed the DOCX/PDF.
- Current-version Claude Opus 4.7 adaptive-thinking full-artifact review remains `real_call_pending`.
- The next retry must use the already signed-in direct Claude session and must not use the Google login button.
"""

    upsert_section(ROOT / "THREAD_RECOVERY_STATUS_20260524.md", "## P0 Thickness Batch17 Recovery Update 20260526", status_section)
    upsert_section(ROOT / "MODEL_EVIDENCE_LEDGER.md", "## MODEL_GATE_P0_THICKNESS_BATCH17_20260526", model_section)
    upsert_section(ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md", "## Governor P0 Thickness Batch17 Update 20260526", governor_section)
    upsert_section(ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md", "## Confucius P0 Thickness Batch17 Artifact Check 20260526", confucius_section)
    upsert_section(ROOT / "FORMAT_RENDER_QA_20260524.md", "## P0 Batch17 Render/Format Delta 20260526", format_section)
    upsert_section(
        ROOT / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
        "## Deferred Upload Scope Addition: P0 Batch17 20260526",
        upload_section,
    )
    upsert_section(
        ROOT / "ORDER_063_BIXIU4_UPLOAD_DEFERRED_ACK_20260525.md",
        "## Final Upload Binding Refresh After P0 Batch17 20260526",
        upload_binding_section,
    )
    upsert_section(ROOT / "CLAUDE_WEB_LOGIN_CORRECTION_20260525.md", "## Current Boundary After P0 Batch17", claude_boundary)
    (ROOT / "EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md").write_text(
        contact_section.strip() + "\n", encoding="utf-8", newline="\n"
    )
    print("updated governance files for P0 Batch17")


if __name__ == "__main__":
    main()
