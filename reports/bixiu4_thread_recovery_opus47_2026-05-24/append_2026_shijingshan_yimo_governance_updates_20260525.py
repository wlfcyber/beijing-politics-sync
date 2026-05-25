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
## Shijingshan 2026 Yimo Post-Render Status
Updated: 2026-05-25 18:07 +08

- Status: `RECOVERED_EXECUTION_IN_PROGRESS_SHIJINGSHAN_2026_YIMO_LOCAL_QA_PASS_MODEL_GATES_OPEN`.
- 2026 Shijingshan Yimo Q2 was inserted under `发展的观点 / 发展的普遍性` from the official answer-key correct-option chain.
- 2026 Shijingshan Yimo Q3 was inserted under `主观能动性 / 意识的能动作用` from the official answer-key correct-option chain.
- Existing Q17(1) and Q21 current-DOCX coverage was closed against the formal scoring document and recorded as comprehensive-angle/level evidence, not point-by-point scoring rules.
- Q1, Q4-Q5, Q7-Q11, Q14-Q16, and Q18-Q20 were closed as politics/culture/legal/economy/logic/international module-boundary rows where applicable.
- DOCX/PDF after repair were re-exported and rendered.
- Render QA: `288/288` pages, label counts `2879/2879`, blank-like body pages `0`.
- Target pages inspected: Q3 page `34`, Q2 page `112`.
- Matrix audit after repair: `1537` rows, `535` in-book/body rows, total risk rows `82`, in-book/body risk rows `0`; exact 2026 Shijingshan Yimo risk-audit rows `0`.
- Q2/Q3 are recorded as choice-question chains only, not main-question scoring-rubric evidence.
- GPTPro web review remains `real_call_pending`; full Claude Opus 4.7 web/app DOCX/PDF artifact review through direct `https://claude.ai` remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No GitHub push has been attempted; ORDER_063 upload remains deferred.
""",
    "governor": """
## Governor Finding: Shijingshan 2026 Yimo Post-Render Verification
Updated: 2026-05-25 18:07 +08

- Governor decision: `LOCAL_DOCX_Q2_Q3_INSERT_RENDER_PASS_MODEL_GATES_OPEN`.
- Corrective action: inserted Q2 under `发展的观点 / 发展的普遍性` and Q3 under `主观能动性 / 意识的能动作用`.
- Evidence boundary: Q2/Q3 use official answer-key plus stem/correct-option chains; they are not treated as main-question scoring-rubric evidence.
- Existing Q17(1) and Q21 rows were closed as current-DOCX coverage with formal scoring-document support.
- Boundary exclusions: Q1, Q4-Q5, Q7-Q11, Q14-Q16, and Q18-Q20 do not enter the current philosophy body.
- Render result after repair: `288/288` pages, DOCX/PDF label counts `2879/2879`, blank-like body pages `0`.
- Target rendered pages inspected: Q3 page `34`, Q2 page `112`.
- Matrix audit after repair: `1537` rows, `535` in-book/body rows, `82` total risk rows, `0` in-book/body risk rows; exact 2026 Shijingshan Yimo risk rows `0`.
- Local integrity checks remain required at final pass; this section records source/matrix/render closure only.
- External gates remain open: GPTPro web review `real_call_pending`; full Claude Opus web/app DOCX/PDF artifact review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
""",
    "confucius": """
## Artifact Check: Shijingshan 2026 Yimo Post-Render Verification
Updated: 2026-05-25 18:07 +08

- `repair_2026_shijingshan_yimo_candidate_queue_20260525.py`: present.
- `mark_2026_shijingshan_yimo_render_pass_20260525.py`: present.
- `SHIJINGSHAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md`: present and updated with post-render verification.
- `SHIJINGSHAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json`: present and updated with render manifest/page QA.
- DOCX backup before insertion: present.
- Matrix backup before rewrite: present.
- Ledger backup before insert registration: present.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`: updated to `1537` rows.
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`: refreshed after repair; total risk rows `82`, in-book/body risk rows `0`, exact 2026 Shijingshan Yimo risk rows `0`.
- `FORMAT_RENDER_QA_20260524.md`: updated with `2026石景山一模 Recovery Render QA 20260525`.
- Rendered target pages checked: `page_034.png`, `page_112.png`.
- Current DOCX/PDF render status: `288/288` pages, labels `2879/2879`, blank-like body pages `0`.
- Remaining open gates: GPTPro web review, full Claude Opus web/app DOCX/PDF review through direct `https://claude.ai`, ClaudeCode model confirmation, full manual typography pass, and deferred ORDER_063 final GitHub upload.
""",
    "model": """
## MODEL_GATE_RENDER_QA_AFTER_SHIJINGSHAN_2026_YIMO_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- Shijingshan 2026 Yimo repair was performed by local paper/formal-scoring-document review, current DOCX insertion, matrix rewrite, PDF export, and rendered-page QA.
- Local repair inserted Q2 and Q3 as official answer-key plus stem/correct-option chains; these are explicitly not main-question scoring-rubric evidence.
- Local render QA after repair: `288/288` pages, DOCX/PDF labels `2879/2879`, blank-like body pages `0`; target pages checked were Q3 page `34` and Q2 page `112`.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local render QA.
- Correct future Claude web/app route remains direct `https://claude.ai` auto-login; do not use the Google-login loop.
- Claude web/app full artifact review remains `real_call_pending`; GPTPro web full artifact review remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
""",
    "upload": """
## ORDER_063 Binding Refresh After Shijingshan 2026 Yimo Render QA
Updated: 2026-05-25 18:07 +08

- Include `SHIJINGSHAN_2026_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`, `repair_2026_shijingshan_yimo_candidate_queue_20260525.py`, `mark_2026_shijingshan_yimo_render_pass_20260525.py`, updated `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`, updated `docx_insert_ledger.csv`, refreshed `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`, and refreshed Governor/Confucius/status/render QA/model-ledger files in the future upload scope.
- Add post-Shijingshan-Yimo render QA evidence, including `word_render_qa_20260525_global_style_norm`, contact sheet, and inspected target pages `page_034.png`, `page_112.png`, to future upload-scope candidates where appropriate.
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
    upsert_section(FILES["status"], "Shijingshan 2026 Yimo Post-Render Status", SECTIONS["status"])
    upsert_section(FILES["governor"], "Governor Finding: Shijingshan 2026 Yimo Post-Render Verification", SECTIONS["governor"])
    upsert_section(FILES["confucius"], "Artifact Check: Shijingshan 2026 Yimo Post-Render Verification", SECTIONS["confucius"])
    upsert_section(FILES["model"], "MODEL_GATE_RENDER_QA_AFTER_SHIJINGSHAN_2026_YIMO_LOCAL_REPAIR_20260525", SECTIONS["model"])
    upsert_section(FILES["upload"], "ORDER_063 Binding Refresh After Shijingshan 2026 Yimo Render QA", SECTIONS["upload"])
    print("SHIJINGSHAN_2026_YIMO_GOVERNANCE_UPDATES_WRITTEN")


if __name__ == "__main__":
    main()
