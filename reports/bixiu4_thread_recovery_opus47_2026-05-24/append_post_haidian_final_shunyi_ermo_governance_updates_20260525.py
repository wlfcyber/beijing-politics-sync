from __future__ import annotations

from pathlib import Path


RECOVERY = Path(__file__).resolve().parent

FILES = {
    "status": RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md",
    "governor": RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md",
    "confucius": RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md",
    "model": RECOVERY / "MODEL_EVIDENCE_LEDGER.md",
    "upload": RECOVERY / "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
}


SECTIONS = {
    "status": """
## Haidian Final And Shunyi Ermo Post-Render Status
Updated: 2026-05-25 18:36 +08

- Status: `RECOVERED_EXECUTION_IN_PROGRESS_HAIDIAN_FINAL_BOUNDARY_CLOSED_SHUNYI_ERMO_LOCAL_QA_PASS_MODEL_GATES_OPEN`.
- 2026 Haidian Final rows M1364-M1374 were matrix-only boundary repaired: they remain excluded module-boundary rows, with evidence normalized to `正式教师版答案键+题面-模块边界（非评分细则）`.
- 2026 Shunyi Ermo Q21 was inserted under `尊重客观规律与发挥主观能动性相结合` from the source-paper philosophy prompt and formal marking-document philosophy综合角度.
- 2026 Shunyi Ermo Q16 weak-reference duplicate rows were closed against existing current-DOCX coverage and the formal marking-document/阅卷版.
- 2026 Shunyi Ermo Q11, Q17, Q18, and Q20 were closed as legal, political, logic/legal, and international module-boundary rows.
- Render QA after Shunyi Ermo repair: `290/290` pages, label counts `2891/2891`, blank-like body pages `0`.
- Target page inspected: Q21 page `44`.
- Matrix audit after repairs: `1537` rows, `548` in-book/body rows, total risk rows `49`, in-book/body risk rows `0`; exact 2026 Shunyi Ermo risk-audit rows `0`.
- GPTPro web full artifact review remains `real_call_pending`; full Claude Opus 4.7 web/app DOCX/PDF artifact review through direct `https://claude.ai` remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No GitHub push has been attempted; ORDER_063 upload remains deferred.
""",
    "governor": """
## Governor Finding: Haidian Final Boundary Repair And Shunyi Ermo Render Verification
Updated: 2026-05-25 18:36 +08

- Governor decision: `LOCAL_MATRIX_BOUNDARY_AND_DOCX_INSERT_RENDER_PASS_MODEL_GATES_OPEN`.
- Haidian Final correction: M1364-M1374 were normalized as module-boundary exclusions using formal teacher-answer-key and stem evidence only; no DOCX change was needed.
- Shunyi Ermo correction: Q21 was added to `尊重客观规律与发挥主观能动性相结合`; Q16 weak rows were closed as duplicates of existing strong-evidence current-DOCX coverage.
- Shunyi Ermo boundary exclusions: Q11 legal, Q17 political/legal governance, Q18 logic/legal, Q20 international politics/economy.
- Render result after Shunyi Ermo repair: `290/290` pages, DOCX/PDF label counts `2891/2891`, blank-like body pages `0`.
- Target rendered page inspected: Q21 page `44`.
- Matrix audit after repairs: `1537` rows, `548` in-book/body rows, `49` total risk rows, `0` in-book/body risk rows.
- External gates remain open: GPTPro web full artifact review `real_call_pending`; full Claude Opus web/app DOCX/PDF artifact review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
""",
    "confucius": """
## Artifact Check: Haidian Final Boundary Repair And Shunyi Ermo Render Verification
Updated: 2026-05-25 18:36 +08

- `repair_2026_haidian_final_boundary_risk_20260525.py`: present.
- `HAIDIAN_2026_FINAL_BOUNDARY_RISK_REPAIR_20260525.md/.json`: present.
- `repair_2026_shunyi_ermo_candidate_queue_20260525.py`: present.
- `mark_2026_shunyi_ermo_render_pass_20260525.py`: present.
- `SHUNYI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`: present and updated with render QA.
- Shunyi source page renders: `shunyi_ermo_source_pages_20260525/page_05.png`, `page_12.png`.
- DOCX backup before Shunyi Ermo insertion: present.
- Matrix backups before Haidian Final and Shunyi Ermo rewrites: present.
- Ledger backup before Shunyi Ermo insert registration: present.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`: updated to `1537` rows.
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`: refreshed after repairs; total risk rows `49`, in-book/body risk rows `0`.
- `FORMAT_RENDER_QA_20260524.md`: updated with Shunyi Ermo render QA.
- Rendered target page checked: `page_044.png`.
- Current DOCX/PDF render status: `290/290` pages, labels `2891/2891`, blank-like body pages `0`.
- Remaining open gates: GPTPro web full artifact review, full Claude Opus web/app DOCX/PDF review through direct `https://claude.ai`, ClaudeCode model confirmation, full manual typography pass, and deferred ORDER_063 final GitHub upload.
""",
    "model": """
## MODEL_GATE_RENDER_QA_AFTER_HAIDIAN_FINAL_AND_SHUNYI_ERMO_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- Haidian Final boundary repair and Shunyi Ermo Q21 insertion were performed by local source-paper/marking-document review, matrix rewrite, DOCX insertion where needed, PDF export, and rendered-page QA.
- Shunyi Ermo local render QA after repair: `290/290` pages, DOCX/PDF labels `2891/2891`, blank-like body pages `0`; target page checked was Q21 page `44`.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local repair.
- Correct future Claude web/app route remains direct `https://claude.ai` auto-login; do not use the Google-login loop.
- Claude web/app full artifact review remains `real_call_pending`; GPTPro web full artifact review remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
""",
    "upload": """
## ORDER_063 Binding Refresh After Haidian Final And Shunyi Ermo Repairs
Updated: 2026-05-25 18:36 +08

- Include `HAIDIAN_2026_FINAL_BOUNDARY_RISK_REPAIR_20260525.md/.json`, `repair_2026_haidian_final_boundary_risk_20260525.py`, `SHUNYI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`, `repair_2026_shunyi_ermo_candidate_queue_20260525.py`, `mark_2026_shunyi_ermo_render_pass_20260525.py`, `append_post_haidian_final_shunyi_ermo_governance_updates_20260525.py`, updated `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`, updated `docx_insert_ledger.csv`, refreshed `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`, and refreshed Governor/Confucius/status/render QA/model-ledger files in the future upload scope.
- Add Shunyi Ermo source page renders and post-render QA evidence, including `word_render_qa_20260525_global_style_norm/page_044.png`, to future upload-scope candidates where appropriate.
- Current DOCX/PDF after render QA should remain in future upload scope.
- Upload remains deferred. Do not push now; final upload still requires all active Beijing politics lines to end first, then exact upload scope, secret-pattern scan, `NO_SECRET_PATTERN_MATCHES`, commit, push, upload report, and final heartbeat.
""",
}


def upsert_section(path: Path, title: str, section: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    marker = f"\n## {title}"
    if marker in text:
        text = text[: text.index(marker)]
    path.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    upsert_section(FILES["status"], "Haidian Final And Shunyi Ermo Post-Render Status", SECTIONS["status"])
    upsert_section(FILES["governor"], "Governor Finding: Haidian Final Boundary Repair And Shunyi Ermo Render Verification", SECTIONS["governor"])
    upsert_section(FILES["confucius"], "Artifact Check: Haidian Final Boundary Repair And Shunyi Ermo Render Verification", SECTIONS["confucius"])
    upsert_section(FILES["model"], "MODEL_GATE_RENDER_QA_AFTER_HAIDIAN_FINAL_AND_SHUNYI_ERMO_LOCAL_REPAIR_20260525", SECTIONS["model"])
    upsert_section(FILES["upload"], "ORDER_063 Binding Refresh After Haidian Final And Shunyi Ermo Repairs", SECTIONS["upload"])
    print("HAIDIAN_FINAL_AND_SHUNYI_ERMO_GOVERNANCE_UPDATES_WRITTEN")


if __name__ == "__main__":
    main()
