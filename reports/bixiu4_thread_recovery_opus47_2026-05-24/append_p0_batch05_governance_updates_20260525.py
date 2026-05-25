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
## P0 Thickness Batch05 Recovery Update 20260525

- Updated: {updated}
- Status: `RECOVERED_EXECUTION_IN_PROGRESS_P0_BATCH05_APPLIED_GATES_OPEN`.
- Created repair script: `apply_p0_thickness_batch05_20260525.py`.
- Created draft/apply artifacts:
  - `P0_THICKNESS_REPAIR_BATCH05_DRAFT_20260525.md`
  - `P0_THICKNESS_REPAIR_BATCH05_DRAFT_20260525.csv`
  - `P0_THICKNESS_REPAIR_BATCH05_DRAFT_20260525.json`
  - `P0_THICKNESS_REPAIR_BATCH05_APPLY_20260525.md`
  - `P0_THICKNESS_REPAIR_BATCH05_APPLY_20260525.csv`
  - `P0_THICKNESS_REPAIR_BATCH05_APPLY_20260525.json`
- DOCX backup before repair: `05_delivery/*_backup_before_p0_thickness_batch05_20260525_213948.docx`.
- Local repair scope: 8 additional P0 subjective triple-thin rows, matched by exact heading plus old answer excerpt.
- Applied rows: T0248, T0163, T0133, T0234, T0330, T0025, T0250, T0083.
- Refreshed thickness result after Batch05: thin candidates `603` out of `721`; priority counts P0 `112`, P1 `259`, P2 `207`, P3 `25`.
- Cumulative local P0 repairs in this thread: `40`; P0 reduced from `152` to `112`.
- Re-export/render result after DOCX edit: PDF pages/rendered PNGs `294/294`; DOCX/PDF label counts `2891/2891`; blank-like body pages `0`.
- Every-page visual QA refreshed: `294` rows, metric review-required rows `0`, regenerated contact sheets pages `001-294` opened and reviewed at thumbnail level.
- Current blockers:
  - thickness queue remains open: 603 candidates remain, including P0 `112`;
  - post-Batch05 GPTPro/Claude external review is `real_call_pending`;
  - ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`;
  - ORDER_063 upload remains deferred; no GitHub push attempted.
"""

    model_section = f"""
## MODEL_GATE_P0_THICKNESS_BATCH05_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_P0_BATCH05_APPLIED`

- Updated: {updated}
- Local repair artifacts:
  - `apply_p0_thickness_batch05_20260525.py`
  - `P0_THICKNESS_REPAIR_BATCH05_DRAFT_20260525.md/.csv/.json`
  - `P0_THICKNESS_REPAIR_BATCH05_APPLY_20260525.md/.csv/.json`
- Local validation after repair:
  - DOCX zip structural check: `true`;
  - DOCX style consistency audit: `PASS`;
  - refreshed thickness queue: total candidates `603`, P0 `112`;
  - Word/PDF render: `294/294` pages, label counts `2891/2891`, blank-like body pages `0`;
  - every-page metric QA: `294` rows, review-required rows `0`.
- Model-evidence boundary:
  - this is local Codex production repair and QA, not new GPTPro, Claude web/app, or ClaudeCode evidence;
  - the current DOCX/PDF changed after previous external web reviews, so current-version external review remains pending after the remaining thickness queue is handled or explicitly bounded;
  - if a Claude web/app retry is attempted, use direct `https://claude.ai` auto-login instead of Google login.
- Sonnet, Haiku, and model-unknown outputs remain excluded from qualified evidence.
- ClaudeCode production-lane replacement evidence remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""

    governor_section = f"""
## Governor P0 Thickness Batch05 Update 20260525

Updated: {updated}

Status: `PASS_LOCAL_BATCH05_WITH_OPEN_GATES`

- What changed: 8 additional P0 subjective triple-thin rows were locally thickened in the DOCX under their existing evidence-supported framework nodes.
- Precision guard: every edited row was matched by exact heading plus old answer excerpt; duplicate same-question rows were not overwritten.
- Local evidence guard: rewrites stayed within existing nodes and did not introduce new unsupported principles.
- Verification:
  - DOCX backup exists before edit;
  - DOCX structural zip check passed;
  - style consistency audit passed;
  - refreshed thickness queue dropped from 611 to 603 candidates and P0 from 120 to 112;
  - PDF re-export/render passed at `294/294` pages with no blank-like body pages;
  - regenerated contact sheets for pages `001-294` were opened and thumbnail-reviewed.
- Governor verdict: local Batch05 is accepted as an incremental repair, but the line remains non-terminal because 603 thickness candidates remain and current-version external review is pending.
- Claude web/app blocker wording: do not record this as Google-login failure; if retried, direct `https://claude.ai` auto-login is the required path.
- Upload rule: ORDER_063 remains deferred; Batch05 artifacts must be included in the eventual upload scope, but no push is allowed while gates remain open.
"""

    confucius_section = f"""
## Confucius P0 Thickness Batch05 Artifact Check 20260525

Updated: {updated}

Status: `ARTIFACTS_PRESENT_BATCH05_REVIEWED_GATES_OPEN`

- Draft artifacts present: `P0_THICKNESS_REPAIR_BATCH05_DRAFT_20260525.md/.csv/.json`.
- Apply artifacts present: `P0_THICKNESS_REPAIR_BATCH05_APPLY_20260525.md/.csv/.json`.
- Repair script present: `apply_p0_thickness_batch05_20260525.py`.
- Backup present: current DOCX has a `backup_before_p0_thickness_batch05` copy in `05_delivery`.
- Refreshed QA artifacts present:
  - `THICKNESS_DENSITY_AUDIT_20260525.md/.csv`;
  - `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.md/.csv/.json`;
  - `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md/.json`;
  - `word_render_qa_20260525_heading_style_fix/render_manifest.json`;
  - `EVERY_PAGE_VISUAL_QA_LOG_20260525.md/.csv/.json`;
  - `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`.
- Student-learning boundary: 40 rows are now thicker across Batch01-Batch05, but 603 queue rows remain; the whole handbook is not yet uniformly thick for zero-baseline learners.
- External boundary: post-Batch05 GPTPro/Claude review remains pending, and ClaudeCode model confirmation remains blocked.
"""

    format_section = f"""
## P0 Batch05 Render/Format Delta 20260525

Updated: {updated}

- Status: `RENDER_PASS_AFTER_P0_BATCH05_GATES_OPEN`.
- DOCX bytes: `450516`.
- PDF bytes: `4552421`.
- PDF pages/rendered PNGs: `294/294`.
- DOCX/PDF label counts: `2891/2891`.
- Blank-like body pages: `0`.
- Every-page visual metric rows: `294`; review-required rows `0`.
- Contact-sheet review: pages `001-294` opened at thumbnail level; no obvious full-page blank, missing page, severe clipping, page-order break, or page-scale layout drift.
- Boundary: this is render/format QA after local Batch05 only; it does not close remaining thickness or model gates.
"""

    upload_section = f"""
## Deferred Upload Scope Addition: P0 Batch05 20260525

Updated: {updated}

When ORDER_063 eventually permits the final GitHub upload, include these additional recovery-line artifacts in the upload scope:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/apply_p0_thickness_batch05_20260525.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH05_DRAFT_20260525.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH05_DRAFT_20260525.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH05_DRAFT_20260525.json`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH05_APPLY_20260525.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH05_APPLY_20260525.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH05_APPLY_20260525.json`
- refreshed `THICKNESS_DENSITY_AUDIT_20260525.*` and `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.*`
- refreshed `FORMAT_RENDER_QA_20260524.md`
- refreshed `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.*`
- refreshed `word_render_qa_20260525_heading_style_fix/`
- refreshed `EVERY_PAGE_VISUAL_QA_LOG_20260525.*`, `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`, and `every_page_visual_qa_20260525/`
- current DOCX/PDF after Batch05 and the `backup_before_p0_thickness_batch05` DOCX backup.

Upload remains deferred. Before any final push, generate a concrete upload-scope file, scan the selected scope for secret patterns, require `NO_SECRET_PATTERN_MATCHES`, then commit and push only selected project artifacts.
"""

    upsert_section(ROOT / "THREAD_RECOVERY_STATUS_20260524.md", "## P0 Thickness Batch05 Recovery Update 20260525", status_section)
    upsert_section(ROOT / "MODEL_EVIDENCE_LEDGER.md", "## MODEL_GATE_P0_THICKNESS_BATCH05_20260525", model_section)
    upsert_section(ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md", "## Governor P0 Thickness Batch05 Update 20260525", governor_section)
    upsert_section(ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md", "## Confucius P0 Thickness Batch05 Artifact Check 20260525", confucius_section)
    upsert_section(ROOT / "FORMAT_RENDER_QA_20260524.md", "## P0 Batch05 Render/Format Delta 20260525", format_section)
    upsert_section(
        ROOT / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
        "## Deferred Upload Scope Addition: P0 Batch05 20260525",
        upload_section,
    )
    print("updated governance files for P0 Batch05")


if __name__ == "__main__":
    main()
