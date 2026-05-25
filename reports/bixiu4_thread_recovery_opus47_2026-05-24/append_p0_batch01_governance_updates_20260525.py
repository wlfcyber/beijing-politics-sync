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
## P0 Thickness Batch01 Recovery Update 20260525

- Updated: {updated}
- Status: `RECOVERED_EXECUTION_IN_PROGRESS_P0_BATCH01_APPLIED_GATES_OPEN`.
- Created repair script: `apply_p0_thickness_batch01_20260525.py`.
- Created draft/apply artifacts:
  - `P0_THICKNESS_REPAIR_BATCH01_DRAFT_20260525.md`
  - `P0_THICKNESS_REPAIR_BATCH01_DRAFT_20260525.csv`
  - `P0_THICKNESS_REPAIR_BATCH01_DRAFT_20260525.json`
  - `P0_THICKNESS_REPAIR_BATCH01_APPLY_20260525.md`
  - `P0_THICKNESS_REPAIR_BATCH01_APPLY_20260525.csv`
  - `P0_THICKNESS_REPAIR_BATCH01_APPLY_20260525.json`
- DOCX backup before repair: `05_delivery/*_backup_before_p0_thickness_batch01_20260525_205445.docx`.
- Local repair scope: 8 P0 subjective triple-thin rows, matched by exact heading plus old answer excerpt.
- Applied rows: T0159, T0267, T0515, T0348, T0095, T0476, T0643, T0276.
- Refreshed thickness result: thin candidates `635` out of `721`; priority counts P0 `144`, P1 `259`, P2 `207`, P3 `25`.
- Old thin-answer excerpts for all 8 repaired rows now have `0` remaining hits in the refreshed queue.
- Re-export/render result after DOCX edit: PDF pages/rendered PNGs `292/292`; DOCX/PDF label counts `2891/2891`; blank-like body pages `0`.
- Every-page visual QA refreshed: `292` rows, metric review-required rows `0`, contact sheets pages `001-292` opened and reviewed at thumbnail level.
- Current blockers:
  - thickness queue remains open: 635 candidates remain, including P0 `144`;
  - post-Batch01 GPTPro/Claude external review is `real_call_pending`;
  - ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`;
  - ORDER_063 upload remains deferred; no GitHub push attempted.
"""

    model_section = f"""
## MODEL_GATE_P0_THICKNESS_BATCH01_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_P0_BATCH01_APPLIED`

- Updated: {updated}
- Local repair artifacts:
  - `apply_p0_thickness_batch01_20260525.py`
  - `P0_THICKNESS_REPAIR_BATCH01_DRAFT_20260525.md/.csv/.json`
  - `P0_THICKNESS_REPAIR_BATCH01_APPLY_20260525.md/.csv/.json`
- Local validation after repair:
  - DOCX zip structural check: `true`;
  - DOCX style consistency audit: `PASS`;
  - refreshed thickness queue: total candidates `635`, P0 `144`;
  - Word/PDF render: `292/292` pages, label counts `2891/2891`, blank-like body pages `0`;
  - every-page metric QA: `292` rows, review-required rows `0`.
- Model-evidence boundary:
  - this is not new GPTPro evidence;
  - this is not new Claude web/app evidence;
  - this is not new ClaudeCode evidence;
  - prior Claude/GPT web reviews remain historical evidence for the pre-Batch01 artifact, but the changed DOCX/PDF require post-repair re-review after the remaining thickness queue is handled or explicitly bounded.
- Sonnet, Haiku, and model-unknown outputs remain excluded from qualified evidence.
- ClaudeCode production-lane replacement evidence remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""

    governor_section = f"""
## Governor P0 Thickness Batch01 Update 20260525

Updated: {updated}

Status: `PASS_LOCAL_BATCH01_WITH_OPEN_GATES`

- What changed: 8 P0 subjective triple-thin rows were locally thickened in the DOCX under their existing evidence-supported framework nodes.
- Precision guard: every edited row was matched by exact heading plus old answer excerpt; duplicate same-question rows in other nodes were not overwritten.
- Local evidence guard: each rewrite stayed within the existing node and cited the recorded formal scoring/marking support note in the apply artifact.
- Verification:
  - DOCX backup exists before edit;
  - DOCX structural zip check passed;
  - style consistency audit passed after edit;
  - refreshed thickness queue dropped from 643 to 635 candidates and P0 from 152 to 144;
  - PDF re-export/render passed at `292/292` pages with no blank-like body pages;
  - contact sheets for pages `001-292` were opened and thumbnail-reviewed.
- Governor verdict: local Batch01 is accepted as an incremental repair, but the line is not terminal because 635 thickness candidates remain and current-version external review is pending.
- Upload rule: ORDER_063 remains deferred; this recovery line must add Batch01 artifacts to the eventual upload scope, but no push is allowed while gates remain open.
"""

    confucius_section = f"""
## Confucius P0 Thickness Batch01 Artifact Check 20260525

Updated: {updated}

Status: `ARTIFACTS_PRESENT_BATCH01_REVIEWED_GATES_OPEN`

- Draft artifacts present: `P0_THICKNESS_REPAIR_BATCH01_DRAFT_20260525.md/.csv/.json`.
- Apply artifacts present: `P0_THICKNESS_REPAIR_BATCH01_APPLY_20260525.md/.csv/.json`.
- Repair script present: `apply_p0_thickness_batch01_20260525.py`.
- Backup present: current DOCX has a `backup_before_p0_thickness_batch01` copy in `05_delivery`.
- Refreshed QA artifacts present:
  - `THICKNESS_DENSITY_AUDIT_20260525.md/.csv`;
  - `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.md/.csv/.json`;
  - `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.md/.json`;
  - `word_render_qa_20260525_heading_style_fix/render_manifest.json`;
  - `EVERY_PAGE_VISUAL_QA_LOG_20260525.md/.csv/.json`;
  - `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`.
- Student-learning boundary: these 8 rows are thicker and more answer-ready, but the remaining queue means the whole handbook is not yet uniformly thick for zero-baseline learners.
- External boundary: post-repair GPTPro/Claude review remains pending, and ClaudeCode model confirmation remains blocked.
"""

    format_section = f"""
## P0 Batch01 Render/Format Delta 20260525

Updated: {updated}

- Status: `RENDER_PASS_AFTER_P0_BATCH01_GATES_OPEN`.
- DOCX bytes: `445701`.
- PDF bytes: `4520079`.
- PDF pages/rendered PNGs: `292/292`.
- DOCX/PDF label counts: `2891/2891`.
- Blank-like body pages: `0`.
- Every-page visual metric rows: `292`; review-required rows `0`.
- Contact-sheet review: pages `001-292` opened at thumbnail level; no obvious full-page blank, missing page, severe clipping, page-order break, or page-scale layout drift.
- Boundary: this is render/format QA after local Batch01 only; it does not close remaining thickness or model gates.
"""

    upload_section = f"""
## Deferred Upload Scope Addition: P0 Batch01 20260525

Updated: {updated}

When ORDER_063 eventually permits the final GitHub upload, include these additional recovery-line artifacts in the upload scope:

- `reports/bixiu4_thread_recovery_opus47_2026-05-24/apply_p0_thickness_batch01_20260525.py`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH01_DRAFT_20260525.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH01_DRAFT_20260525.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH01_DRAFT_20260525.json`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH01_APPLY_20260525.md`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH01_APPLY_20260525.csv`
- `reports/bixiu4_thread_recovery_opus47_2026-05-24/P0_THICKNESS_REPAIR_BATCH01_APPLY_20260525.json`
- refreshed `THICKNESS_DENSITY_AUDIT_20260525.*` and `THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.*`
- refreshed `FORMAT_RENDER_QA_20260524.md`
- refreshed `DOCX_STYLE_CONSISTENCY_AUDIT_20260525.*`
- refreshed `word_render_qa_20260525_heading_style_fix/`
- refreshed `EVERY_PAGE_VISUAL_QA_LOG_20260525.*`, `EVERY_PAGE_VISUAL_QA_CONTACT_SHEET_REVIEW_20260525.md`, and `every_page_visual_qa_20260525/`
- current DOCX/PDF after Batch01 and the `backup_before_p0_thickness_batch01` DOCX backup.

Upload remains deferred. Before any final push, generate a concrete upload-scope file, scan the selected scope for secret patterns, require `NO_SECRET_PATTERN_MATCHES`, then commit and push only selected project artifacts.
"""

    upsert_section(ROOT / "THREAD_RECOVERY_STATUS_20260524.md", "## P0 Thickness Batch01 Recovery Update 20260525", status_section)
    upsert_section(ROOT / "MODEL_EVIDENCE_LEDGER.md", "## MODEL_GATE_P0_THICKNESS_BATCH01_20260525", model_section)
    upsert_section(ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md", "## Governor P0 Thickness Batch01 Update 20260525", governor_section)
    upsert_section(ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md", "## Confucius P0 Thickness Batch01 Artifact Check 20260525", confucius_section)
    upsert_section(ROOT / "FORMAT_RENDER_QA_20260524.md", "## P0 Batch01 Render/Format Delta 20260525", format_section)
    upsert_section(
        ROOT / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
        "## Deferred Upload Scope Addition: P0 Batch01 20260525",
        upload_section,
    )

    print("updated governance files for P0 Batch01")


if __name__ == "__main__":
    main()
