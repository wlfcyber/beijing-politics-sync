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
## Fengtai 2026 Ermo Post-Render Status
Updated: 2026-05-25 17:42 +08

- Status: `RECOVERED_EXECUTION_IN_PROGRESS_FENGTAI_2026_ERMO_LOCAL_QA_PASS_MODEL_GATES_OPEN`.
- 2026 Fengtai Ermo Q4/Q5/Q6/Q7 choice-question chains and Q22 formal-PPT philosophy angle were inserted into the current DOCX and registered in `docx_insert_ledger.csv`.
- Q16 duplicate production-line candidates were closed against the existing five current-DOCX body entries and the formal marking PPT.
- Q1-Q3, Q8-Q15, and Q17-Q21 were explicitly closed as module-boundary exclusions where applicable.
- DOCX/PDF after repair were re-exported and rendered.
- Render QA: `285/285` pages, label counts `2859/2859`, blank-like body pages `0`.
- Target pages inspected: Q5/Q6 page `33`, Q4 page `81`, Q22 page `173`, Q7 page `209`.
- Matrix audit after repair: `1537` rows, `516` in-book/body rows, total risk rows `113`, in-book/body risk rows `0`; exact 2026 Fengtai Ermo risk-audit rows `0`.
- Choice rows are recorded as correct-option chains only, not main-question scoring-rubric evidence; Q22 is marked as formal marking-PPT angle/level evidence, not point-by-point scoring rules.
- GPTPro web review remains `real_call_pending`; full Claude Opus 4.7 web/app DOCX/PDF artifact review through direct `https://claude.ai` remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No GitHub push has been attempted; ORDER_063 upload remains deferred.
""",
    "governor": """
## Governor Finding: Fengtai 2026 Ermo Post-Render Verification
Updated: 2026-05-25 17:42 +08

- Governor decision: `LOCAL_DOCX_Q4_Q5_Q6_Q7_Q22_INSERT_RENDER_PASS_MODEL_GATES_OPEN`.
- Corrective action: inserted Q4 under `整体与部分`, Q5/Q6 under `主观能动性 / 意识的能动作用`, Q7 under `实践是认识的基础`, and Q22 under `主要矛盾和次要矛盾`.
- Evidence boundary: Q4-Q7 are answer-key plus stem/correct-option choice chains, not main-question scoring-rubric evidence.
- Q22 uses formal marking PPT philosophy-angle and level-description evidence; it is not treated as point-by-point scoring rules.
- Q16 duplicate rows were closed as existing current-DOCX coverage supported by the formal Fengtai Ermo marking PPT.
- Boundary exclusions: Q1-Q3, Q8-Q15, and Q17-Q21 do not enter the current philosophy body except where separately listed above.
- Render result after repair: `285/285` pages, DOCX/PDF label counts `2859/2859`, blank-like body pages `0`.
- Target rendered pages inspected: Q5/Q6 page `33`, Q4 page `81`, Q22 page `173`, Q7 page `209`.
- Matrix audit after repair: `1537` rows, `516` in-book/body rows, `113` total risk rows, `0` in-book/body risk rows; exact 2026 Fengtai Ermo risk rows `0`.
- Local integrity checks: current DOCX zip test passed, no Word temp lock was found, no WINWORD process remained, and touched files did not contain the prohibited final-acceptance label.
- External gates remain open: GPTPro web review `real_call_pending`; full Claude Opus web/app DOCX/PDF artifact review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
""",
    "confucius": """
## Artifact Check: Fengtai 2026 Ermo Post-Render Verification
Updated: 2026-05-25 17:42 +08

- `repair_2026_fengtai_ermo_candidate_queue_20260525.py`: present.
- `mark_2026_fengtai_ermo_render_pass_20260525.py`: present.
- `FENGTAI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md`: present and updated with post-render verification.
- `FENGTAI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.json`: present and updated with render manifest/page QA.
- DOCX backup before insertion: present.
- Matrix backup before rewrite: present.
- Ledger backup before insert registration: present.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`: updated to `1537` rows.
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`: refreshed after repair; total risk rows `113`, in-book/body risk rows `0`, exact 2026 Fengtai Ermo risk rows `0`.
- `FORMAT_RENDER_QA_20260524.md`: updated with `2026丰台二模 Recovery Render QA 20260525`.
- Rendered target pages checked: `page_033.png`, `page_081.png`, `page_173.png`, `page_209.png`.
- Current DOCX/PDF render status: `285/285` pages, labels `2859/2859`, blank-like body pages `0`.
- Remaining open gates: GPTPro web review, full Claude Opus web/app DOCX/PDF review through direct `https://claude.ai`, ClaudeCode model confirmation, full manual typography pass, and deferred ORDER_063 final GitHub upload.
""",
    "model": """
## MODEL_GATE_RENDER_QA_AFTER_FENGTAI_2026_ERMO_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- Fengtai 2026 Ermo repair was performed by local paper/answer/PPT source review, current DOCX insertion, matrix rewrite, PDF export, and rendered-page QA.
- Local repair inserted Q4/Q5/Q6/Q7 as choice-question chains and Q22 as formal marking-PPT philosophy-angle evidence.
- Local render QA after repair: `285/285` pages, DOCX/PDF labels `2859/2859`, blank-like body pages `0`; target pages checked were Q5/Q6 page `33`, Q4 page `81`, Q22 page `173`, and Q7 page `209`.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local render QA.
- Correct future Claude web/app route remains direct `https://claude.ai` auto-login; do not use the Google-login loop.
- Claude web/app full artifact review remains `real_call_pending`; GPTPro web full artifact review remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
""",
    "upload": """
## ORDER_063 Binding Refresh After Fengtai 2026 Ermo Render QA
Updated: 2026-05-25 17:42 +08

- Include `FENGTAI_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`, `repair_2026_fengtai_ermo_candidate_queue_20260525.py`, `mark_2026_fengtai_ermo_render_pass_20260525.py`, updated `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`, updated `docx_insert_ledger.csv`, refreshed `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`, and refreshed Governor/Confucius/status/render QA/model-ledger files in the future upload scope.
- Add post-Fengtai-Ermo render QA evidence, including `word_render_qa_20260525_global_style_norm`, contact sheet, and inspected target pages `page_033.png`, `page_081.png`, `page_173.png`, `page_209.png`, to future upload-scope candidates where appropriate.
- Current DOCX/PDF after render QA should remain in future upload scope.
- Upload remains deferred. Do not push now; final upload still requires all active Beijing politics lines to end first, then exact upload scope, secret-pattern scan, `NO_SECRET_PATTERN_MATCHES`, commit, push, upload report, and final heartbeat.
""",
}


def upsert_section(path: Path, title: str, section: str) -> None:
    text = path.read_text(encoding="utf-8")
    marker = f"\n## {title}"
    if marker in text:
        text = text[: text.index(marker)]
    path.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    upsert_section(FILES["status"], "Fengtai 2026 Ermo Post-Render Status", SECTIONS["status"])
    upsert_section(FILES["governor"], "Governor Finding: Fengtai 2026 Ermo Post-Render Verification", SECTIONS["governor"])
    upsert_section(FILES["confucius"], "Artifact Check: Fengtai 2026 Ermo Post-Render Verification", SECTIONS["confucius"])
    upsert_section(FILES["model"], "MODEL_GATE_RENDER_QA_AFTER_FENGTAI_2026_ERMO_LOCAL_REPAIR_20260525", SECTIONS["model"])
    upsert_section(FILES["upload"], "ORDER_063 Binding Refresh After Fengtai 2026 Ermo Render QA", SECTIONS["upload"])
    print("FENGTAI_2026_ERMO_GOVERNANCE_UPDATES_WRITTEN")


if __name__ == "__main__":
    main()
