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
## P0 Thickness Batch11 Recovery Update 20260525

- Updated: {updated}
- Status: `RECOVERED_EXECUTION_IN_PROGRESS_P0_BATCH11_APPLIED_GATES_OPEN`.
- Created repair script: `apply_p0_thickness_batch11_20260525.py`.
- Created draft/apply artifacts:
  - `P0_THICKNESS_REPAIR_BATCH11_DRAFT_20260525.md`
  - `P0_THICKNESS_REPAIR_BATCH11_DRAFT_20260525.csv`
  - `P0_THICKNESS_REPAIR_BATCH11_DRAFT_20260525.json`
  - `P0_THICKNESS_REPAIR_BATCH11_APPLY_20260525.md`
  - `P0_THICKNESS_REPAIR_BATCH11_APPLY_20260525.csv`
  - `P0_THICKNESS_REPAIR_BATCH11_APPLY_20260525.json`
- DOCX backup before repair: `05_delivery/*_backup_before_p0_thickness_batch11_20260525_230154.docx`.
- Local repair scope: 8 additional P0 subjective triple-thin rows, matched by exact heading plus old answer excerpt.
- Applied rows: T0048, T0519, T0106, T0204, T0377, T0486, T0049, T0107.
- Refreshed thickness result after Batch11: thin candidates `555` out of `721`; priority counts P0 `64`, P1 `259`, P2 `207`, P3 `25`.
- Refreshed grouping after Batch11: inserted `301`, legacy `254`; subjective `427`, choice `128`.
- Refreshed flag counts after Batch11: `ANSWER_LT_120_CHARS` 362, `WHY_LT_90_CHARS` 140, `SHORT_WITHOUT_POINT_MARKERS` 486.
- Cumulative local P0 repairs in this thread: `88`; P0 reduced from `152` to `64`.
- Re-export/render result after DOCX edit: PDF pages/rendered PNGs `299/299`; DOCX/PDF label counts `2891/2891`; blank-like body pages `0`.
- Every-page visual QA refreshed: `299` rows, metric review-required rows `0`, regenerated contact sheets pages `001-299` opened and reviewed at thumbnail level.
- Current blockers:
  - thickness queue remains open: 555 candidates remain, including P0 `64`;
  - post-Batch11 GPTPro/Claude external review is `real_call_pending`;
  - ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`;
  - ORDER_063 upload remains deferred; no GitHub push attempted.
"""

    model_section = f"""
## MODEL_GATE_P0_THICKNESS_BATCH11_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_P0_BATCH11_APPLIED`

- Updated: {updated}
- Local repair artifacts:
  - `apply_p0_thickness_batch11_20260525.py`
  - `P0_THICKNESS_REPAIR_BATCH11_DRAFT_20260525.md/.csv/.json`
  - `P0_THICKNESS_REPAIR_BATCH11_APPLY_20260525.md/.csv/.json`
- Local validation after repair:
  - DOCX zip structural check: `true`;
  - DOCX style consistency audit: `PASS`;
  - refreshed thickness queue: total candidates `555`, P0 `64`;
  - Word/PDF render: `299/299` pages, label counts `2891/2891`, blank-like body pages `0`;
  - every-page metric QA: `299` rows, review-required rows `0`;
  - contact-sheet visual review: pages `001-299` reviewed, page `299` confirmed short but not blank.
- Model-evidence boundary:
  - this is local Codex production repair and QA, not new GPTPro, Claude web/app, or ClaudeCode evidence;
  - the current DOCX/PDF changed after previous external web reviews, so current-version external review remains pending after the remaining thickness queue is handled or explicitly bounded;
  - if a Claude web/app retry is attempted, use direct `https://claude.ai` auto-login instead of Google login.
- Sonnet, Haiku, and model-unknown outputs remain excluded from qualified evidence.
- ClaudeCode production-lane replacement evidence remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""

    governor_section = f"""
## Governor P0 Thickness Batch11 Update 20260525

Updated: {updated}

Status: `PASS_LOCAL_BATCH11_WITH_OPEN_GATES`

- What changed: 8 additional P0 subjective triple-thin rows were locally thickened in the DOCX under their existing evidence-supported framework nodes.
- Precision guard: every edited row was matched by exact heading plus old answer excerpt; duplicate same-question rows were not overwritten.
- Local evidence guard: each evidence note cites a current matrix row with formal scoring/rubric or formal broad-angle support; no ordinary reference answer was upgraded into a scoring rubric.
- Verification:
  - DOCX backup exists before edit;
  - DOCX structural zip check passed;
  - style consistency audit passed;
  - refreshed thickness queue dropped from 563 to 555 candidates and P0 from 72 to 64;
  - PDF re-export/render passed at `299/299` pages with no blank-like body pages;
  - regenerated contact sheets for pages `001-299` were opened and thumbnail-reviewed, including short final page `299`.
- Governor verdict: local Batch11 is accepted as an incremental repair, but the line remains non-terminal because 555 thickness candidates remain and current-version external review is pending.
- Claude web/app blocker wording: do not record this as Google-login failure; if retried, direct `https://claude.ai` auto-login is the required path.
- Upload rule: ORDER_063 remains deferred; Batch11 artifacts must be included in the eventual upload scope, but no push is allowed while gates remain open.
"""

    confucius_section = f"""
## Confucius P0 Thickness Batch11 Artifact Check 20260525

Updated: {updated}

Status: `ARTIFACTS_PRESENT_BATCH11_REVIEWED_GATES_OPEN`

- Draft artifacts present: `P0_THICKNESS_REPAIR_BATCH11_DRAFT_20260525.md/.csv/.json`.
- Apply artifacts present: `P0_THICKNESS_REPAIR_BATCH11_APPLY_20260525.md/.csv/.json`.
- Repair script present: `apply_p0_thickness_batch11_20260525.py`.
- Backup present: current DOCX has a `backup_before_p0_thickness_batch11` copy in `05_delivery`.
- Refreshed QA artifacts present:
  - `THICKNESS_DENSITY_AUDIT_20260525.md/.csv`;
  - `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.md/.csv/.json`;
  - `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md/.json`;
  - `word_render_qa_20260525_heading_style_fix/render_manifest.json`;
  - `EVERY_PAGE_VISUAL_QA_LOG_20260525.md/.csv/.json`;
  - `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`.
- Student-learning boundary: 88 rows are now thicker across Batch01-Batch11, but 555 queue rows remain; the whole handbook is not yet uniformly thick for zero-baseline learners.
- External boundary: post-Batch11 GPTPro/Claude review remains pending, and ClaudeCode model confirmation remains blocked.
"""

    format_section = f"""
## P0 Batch11 Render/Format Delta 20260525

Updated: {updated}

- Status: `RENDER_PASS_AFTER_P0_BATCH11_GATES_OPEN`.
- DOCX bytes: `457344`.
- PDF bytes: `4609383`.
- PDF pages/rendered PNGs: `299/299`.
- DOCX/PDF label counts: `2891/2891`.
- Blank-like body pages: `0`.
- Every-page visual metric rows: `299`; review-required rows `0`.
- Contact-sheet review: pages `001-299` opened at thumbnail level; no obvious full-page blank, missing page, severe clipping, page-order break, or page-scale layout drift. Page `299` is a short final page with visible content/footer.
- Boundary: this is render/format QA after local Batch11 only; it does not close remaining thickness or model gates.
"""

    contact_section = f"""
# Every Page Visual QA Contact Sheet Review 20260525

Updated: {updated}

Status: `CONTACT_SHEETS_REVIEWED_AFTER_P0_BATCH11`

- Render basis: `word_render_qa_20260525_heading_style_fix/render_manifest.json`.
- Render timestamp: `20260525_230244`.
- PDF pages / rendered PNGs: `299/299`.
- Contact sheets opened: `10`.
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
  - `271-299`
- Metric review-required rows: `0`.
- Blank-like body pages: `0`.
- Visual thumbnail finding: no obvious full-page blank, missing page, severe clipping, page-order break, or page-scale layout drift was visible in the 10 regenerated contact sheets.
- Note: page `299` is a short final page with visible content and footer, not a blank page.

## Boundary

- This is a thumbnail-level visual review plus metric screen, not 100 percent zoom proofreading of every character.
- It verifies rendering stability after P0 thickness Batch11.
- It does not close the remaining thickness queue, ClaudeCode model-confirmation gate, or later GPTPro/Claude external-review gates.
"""

    upload_section = f"""
## Deferred Upload Scope Addition: P0 Batch11 20260525

Updated: {updated}

When ORDER_063 eventually permits the final GitHub upload, include these additional recovery-line artifacts in the upload scope:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/apply_p0_thickness_batch11_20260525.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/append_p0_batch11_governance_updates_20260525.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH11_DRAFT_20260525.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH11_DRAFT_20260525.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH11_DRAFT_20260525.json`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH11_APPLY_20260525.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH11_APPLY_20260525.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH11_APPLY_20260525.json`
- refreshed `THICKNESS_DENSITY_AUDIT_20260525.*` and `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.*`
- refreshed `FORMAT_RENDER_QA_20260524.md`
- refreshed `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.*`
- refreshed `word_render_qa_20260525_heading_style_fix/`
- refreshed `EVERY_PAGE_VISUAL_QA_LOG_20260525.*`, `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`, and `every_page_visual_qa_20260525/`
- current DOCX/PDF after Batch11 and the `backup_before_p0_thickness_batch11` DOCX backup.

Upload remains deferred. Before any final push, generate a concrete upload-scope file, scan the selected scope for secret patterns, require `NO_SECRET_PATTERN_MATCHES`, then commit and push only selected project artifacts.
"""

    claude_boundary = f"""
## Current Boundary After P0 Batch11
Updated: {updated}

- Direct `https://claude.ai` remains the required retry path for any further Claude web/app review.
- No new Claude web/app external review has been completed after P0 Batch11 changed the DOCX/PDF.
- Current-version Claude Opus 4.7 adaptive-thinking full-artifact review remains `real_call_pending`.
- The next retry must use the already signed-in direct Claude session and must not use the Google login button.
"""

    upsert_section(ROOT / "THREAD_RECOVERY_STATUS_20260524.md", "## P0 Thickness Batch11 Recovery Update 20260525", status_section)
    upsert_section(ROOT / "MODEL_EVIDENCE_LEDGER.md", "## MODEL_GATE_P0_THICKNESS_BATCH11_20260525", model_section)
    upsert_section(ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md", "## Governor P0 Thickness Batch11 Update 20260525", governor_section)
    upsert_section(ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md", "## Confucius P0 Thickness Batch11 Artifact Check 20260525", confucius_section)
    upsert_section(ROOT / "FORMAT_RENDER_QA_20260524.md", "## P0 Batch11 Render/Format Delta 20260525", format_section)
    upsert_section(
        ROOT / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
        "## Deferred Upload Scope Addition: P0 Batch11 20260525",
        upload_section,
    )
    upsert_section(ROOT / "CLAUDE_WEB_LOGIN_CORRECTION_20260525.md", "## Current Boundary After P0 Batch11", claude_boundary)
    (ROOT / "EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md").write_text(
        contact_section.strip() + "\n", encoding="utf-8", newline="\n"
    )
    print("updated governance files for P0 Batch11")


if __name__ == "__main__":
    main()
