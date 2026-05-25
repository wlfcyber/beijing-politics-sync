from __future__ import annotations

from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent


def append_once(path: Path, marker: str, text: str) -> None:
    current = path.read_text(encoding="utf-8")
    if marker in current:
        return
    path.write_text(current.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8")


def main() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M +08")

    status_section = f"""
## Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo Matrix Closure Status
Updated: {now}

- Status: `RECOVERED_EXECUTION_IN_PROGRESS_MATRIX_RISK_29_IN_BODY_RISK_0_MODEL_GATES_OPEN`.
- 2026 Haidian Yimo was closed by matrix-only source/body comparison: Q16 remains covered by six current DOCX body nodes with formal scoring support; Q15/Q17/Q18/Q19/Q20 were excluded as international, logic, economy/legal, law, or international module-boundary rows.
- 2026 Tongzhou Yimo was closed by matrix-only source/body comparison: Q18 remains covered by existing current DOCX entries under contradiction and dialectical-negation nodes with formal rubric support; Q17 remains an economy/logic boundary row.
- 2026 Tongzhou Yimo Q1-Q3 are recorded as a source boundary because source images show choice questions but the available scoring file does not contain the official first-part choice answer key. They were not inserted into the body.
- 2024 Dongcheng Yimo was closed by matrix-only source review: Q1/Q2/Q4 were objective choice-question answer-key boundaries; old Q4 candidate text was a row-slicing error pointing to Q21, already covered by the current DOCX system-optimization entry.
- Latest matrix audit after this closure: `1537` rows, `554` in-book/body rows, total risk rows `29`, in-book/body risk rows `0`.
- Latest retained DOCX/PDF render remains the Shunyi Ermo render: `290/290` pages, label counts `2891/2891`, blank-like body pages `0`; no new DOCX/PDF export was required for these matrix-only repairs.
- GPTPro web full artifact review remains `real_call_pending`; full Claude Opus 4.7 web/app DOCX/PDF artifact review through direct `https://claude.ai` remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No GitHub push has been attempted; ORDER_063 upload remains deferred until all active Beijing politics lines reach a terminal or user-approved blocker status and upload scope plus secret scan are complete.
"""

    governor_section = f"""
## Governor Finding: Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo Matrix Closure
Updated: {now}

- Governor decision: `LOCAL_MATRIX_ONLY_CLOSURE_PASS_MODEL_GATES_OPEN`.
- Haidian Yimo: no DOCX change was needed. Q16 current-body coverage was accepted against formal scoring support; non-philosophy rows were closed as module boundaries.
- Tongzhou Yimo: no DOCX change was needed. Q18 current-body coverage was accepted against formal rubric support; Q1-Q3 remain source-boundary rows because the official choice answer key for the first part was not found in the available scoring file.
- Dongcheng 2024 Yimo: no DOCX change was needed. Q1/Q2/Q4 were closed as choice-question answer-key boundaries, and the old Q4 candidate was corrected as a Q21 row-slicing error already represented in the current system-optimization body entry.
- Matrix audit after closure: `1537` rows, `554` in-book/body rows, `29` total risk rows, `0` in-book/body risk rows.
- Render boundary: latest retained render is still the Shunyi Ermo post-insert render, `290/290` pages with DOCX/PDF labels `2891/2891` and blank-like body pages `0`.
- External gates remain open: GPTPro web full artifact review `real_call_pending`; full Claude Opus web/app DOCX/PDF artifact review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
"""

    confucius_section = f"""
## Artifact Check: Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo Matrix Closure
Updated: {now}

- `repair_2026_haidian_yimo_candidate_queue_20260525.py`: present.
- `HAIDIAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`: present.
- `repair_2026_tongzhou_yimo_candidate_queue_20260525.py`: present.
- `TONGZHOU_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`: present.
- `repair_2024_dongcheng_yimo_candidate_queue_20260525.py`: present.
- `DONGCHENG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`: present.
- Source render evidence directories present: `haidian_yimo_source_pages_20260525`, `tongzhou_yimo_source_pages_20260525`, `tongzhou_yimo_rubric_pages_20260525`, `dongcheng_2024_yimo_source_pages_20260525`.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`: updated to `1537` rows.
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`: refreshed after matrix-only closures; total risk rows `29`, in-book/body risk rows `0`.
- `FORMAT_RENDER_QA_20260524.md`: updated to record matrix-only closures and retained Shunyi Ermo render status.
- Current retained DOCX/PDF render status: `290/290` pages, labels `2891/2891`, blank-like body pages `0`.
- Remaining open gates: GPTPro web full artifact review, full Claude Opus web/app DOCX/PDF review through direct `https://claude.ai`, ClaudeCode model confirmation, full manual typography pass, remaining matrix risk queue, and deferred ORDER_063 final GitHub upload.
"""

    model_section = f"""
## MODEL_GATE_MATRIX_ONLY_AFTER_HAIDIAN_YIMO_TONGZHOU_YIMO_DONGCHENG2024_REPAIRS_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo closures were performed by local source renders, current DOCX comparison, matrix rewrite, and risk-audit refresh.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for these matrix-only repairs.
- Correct future Claude web/app route remains direct `https://claude.ai` auto-login; do not use the Google-login loop.
- Claude web/app full artifact review remains `real_call_pending`; GPTPro web full artifact review remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
"""

    render_section = f"""
## Matrix-Only Closure QA After Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo
Updated: {now}

- Status: `NO_NEW_RENDER_REQUIRED_MATRIX_ONLY_REPAIR`.
- The current DOCX/PDF was not modified by these three closures.
- Latest retained render remains `Shunyi 2026 Ermo Recovery Render QA 20260525`: `290/290` pages, DOCX/PDF label counts `2891/2891`, blank-like body pages `0`.
- Matrix-only QA refreshed `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` and `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`; total risk rows now `29`, in-book/body risk rows `0`.
- External model gates remain open and are not replaced by this local render/matrix check.
"""

    upload_section = f"""
## ORDER_063 Binding Refresh After Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo Matrix Closures
Updated: {now}

- Include `HAIDIAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`, `repair_2026_haidian_yimo_candidate_queue_20260525.py`, `TONGZHOU_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`, `repair_2026_tongzhou_yimo_candidate_queue_20260525.py`, `DONGCHENG_2024_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`, `repair_2024_dongcheng_yimo_candidate_queue_20260525.py`, source render evidence directories, updated matrix, refreshed risk audit, and refreshed Governor/Confucius/status/render QA/model-ledger files in the future upload scope.
- No new DOCX/PDF output was created by these matrix-only repairs; future upload scope should still include the current DOCX/PDF and latest retained render QA evidence because the matrix now maps these suites more accurately.
- Upload remains deferred. Do not push now; final upload still requires all active Beijing politics lines to end first, then exact upload scope, secret-pattern scan, commit, push, upload report, and final heartbeat.
"""

    append_once(BASE / "THREAD_RECOVERY_STATUS_20260524.md", "RECOVERED_EXECUTION_IN_PROGRESS_MATRIX_RISK_29_IN_BODY_RISK_0_MODEL_GATES_OPEN", status_section)
    append_once(BASE / "GOVERNOR_RECOVERY_REPORT_20260524.md", "Governor Finding: Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo Matrix Closure", governor_section)
    append_once(BASE / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md", "Artifact Check: Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo Matrix Closure", confucius_section)
    append_once(BASE / "MODEL_EVIDENCE_LEDGER.md", "MODEL_GATE_MATRIX_ONLY_AFTER_HAIDIAN_YIMO_TONGZHOU_YIMO_DONGCHENG2024_REPAIRS_20260525", model_section)
    append_once(BASE / "FORMAT_RENDER_QA_20260524.md", "Matrix-Only Closure QA After Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo", render_section)
    append_once(BASE / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md", "ORDER_063 Binding Refresh After Haidian Yimo, Tongzhou Yimo, and Dongcheng 2024 Yimo Matrix Closures", upload_section)

    print("governance_updates_appended")


if __name__ == "__main__":
    main()
