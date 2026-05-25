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
## Fangshan 2026 Ermo Post-Render Status
Updated: 2026-05-25 17:56 +08

- Status: `RECOVERED_EXECUTION_IN_PROGRESS_FANGSHAN_2026_ERMO_LOCAL_QA_PASS_MODEL_GATES_OPEN`.
- 2026 Fangshan Ermo Q18(2) was inserted under `辩证否定 / 守正创新` from the formal marking document's OPC-negation/sublation scoring chain.
- 2026 Fangshan Ermo Q21 was inserted under `人民群众` and `矛盾的普遍性` from the formal comprehensive-question angle list and level descriptors.
- Existing Q16 current-DOCX coverage was closed against the formal marking document: `尊重客观规律与发挥主观能动性`, `系统观念 / 系统优化`, and `量变与质变 / 适度原则`.
- Q17, Q18(1), Q19, and Q20 were closed as legal/economy/international module-boundary rows and were not inserted into the philosophy body.
- DOCX/PDF after repair were re-exported and rendered.
- Render QA: `287/287` pages, label counts `2871/2871`, blank-like body pages `0`.
- Target pages inspected: Q18(2) page `133`, Q21 contradiction pages `153-154`, Q21 people pages `251-252`.
- Matrix audit after repair: `1537` rows, `525` in-book/body rows, total risk rows `102`, in-book/body risk rows `0`; exact 2026 Fangshan Ermo risk-audit rows `0`.
- Q21 evidence is recorded as formal comprehensive-question angle plus level evidence, not point-by-point scoring rules.
- GPTPro web review remains `real_call_pending`; full Claude Opus 4.7 web/app DOCX/PDF artifact review through direct `https://claude.ai` remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- No GitHub push has been attempted; ORDER_063 upload remains deferred.
""",
    "governor": """
## Governor Finding: Fangshan 2026 Ermo Post-Render Verification
Updated: 2026-05-25 17:56 +08

- Governor decision: `LOCAL_DOCX_Q18_Q21_INSERT_RENDER_PASS_MODEL_GATES_OPEN`.
- Corrective action: inserted Q18(2) under `辩证否定 / 守正创新`, Q21 under `人民群众`, and Q21 under `矛盾的普遍性`.
- Evidence boundary: Q18(2) uses formal point-by-point scoring from `26房山评标(2).docx`; Q21 uses formal comprehensive-question angle and level evidence, not point-by-point scoring rules.
- Existing Q16 rows remain accepted as current-DOCX coverage with formal marking-document support.
- Boundary exclusions: Q17, Q18(1), Q19, and Q20 do not enter the current philosophy body.
- Render result after repair: `287/287` pages, DOCX/PDF label counts `2871/2871`, blank-like body pages `0`.
- Target rendered pages inspected: Q18(2) page `133`, Q21 contradiction pages `153-154`, and Q21 people pages `251-252`.
- Matrix audit after repair: `1537` rows, `525` in-book/body rows, `102` total risk rows, `0` in-book/body risk rows; exact 2026 Fangshan Ermo risk rows `0`.
- Local integrity checks: current DOCX zip test passed, no Word temp lock was found, no WINWORD process remained, and touched files did not contain the prohibited final-acceptance label.
- External gates remain open: GPTPro web review `real_call_pending`; full Claude Opus web/app DOCX/PDF artifact review through direct `https://claude.ai` `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
""",
    "confucius": """
## Artifact Check: Fangshan 2026 Ermo Post-Render Verification
Updated: 2026-05-25 17:56 +08

- `repair_2026_fangshan_ermo_candidate_queue_20260525.py`: present.
- `insert_2026_fangshan_ermo_q21_contradiction_20260525.py`: present.
- `mark_2026_fangshan_ermo_render_pass_20260525.py`: present.
- `FANGSHAN_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md`: present and updated with post-render verification.
- `FANGSHAN_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.json`: present and updated with render manifest/page QA.
- DOCX backups before insertion: present for Q18/Q21 and Q21 contradiction insert.
- Matrix backup before rewrite: present.
- Ledger backups before insert registration: present.
- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`: updated to `1537` rows.
- `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`: refreshed after repair; total risk rows `102`, in-book/body risk rows `0`, exact 2026 Fangshan Ermo risk rows `0`.
- `FORMAT_RENDER_QA_20260524.md`: updated with `2026房山二模 Recovery Render QA 20260525`.
- Rendered target pages checked: `page_133.png`, `page_153.png`, `page_154.png`, `page_251.png`, `page_252.png`.
- Current DOCX/PDF render status: `287/287` pages, labels `2871/2871`, blank-like body pages `0`.
- Remaining open gates: GPTPro web review, full Claude Opus web/app DOCX/PDF review through direct `https://claude.ai`, ClaudeCode model confirmation, full manual typography pass, and deferred ORDER_063 final GitHub upload.
""",
    "model": """
## MODEL_GATE_RENDER_QA_AFTER_FANGSHAN_2026_ERMO_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- Fangshan 2026 Ermo repair was performed by local paper/formal-marking-document review, current DOCX insertion, matrix rewrite, PDF export, and rendered-page QA.
- Local repair inserted Q18(2) as formal point-by-point scoring evidence and Q21 as formal comprehensive-question angle/level evidence.
- Local render QA after repair: `287/287` pages, DOCX/PDF labels `2871/2871`, blank-like body pages `0`; target pages checked were Q18(2) page `133`, Q21 contradiction pages `153-154`, and Q21 people pages `251-252`.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local render QA.
- Correct future Claude web/app route remains direct `https://claude.ai` auto-login; do not use the Google-login loop.
- Claude web/app full artifact review remains `real_call_pending`; GPTPro web full artifact review remains `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
""",
    "upload": """
## ORDER_063 Binding Refresh After Fangshan 2026 Ermo Render QA
Updated: 2026-05-25 17:56 +08

- Include `FANGSHAN_2026_ERMO_CANDIDATE_QUEUE_REPAIR_20260525.md/.json`, `repair_2026_fangshan_ermo_candidate_queue_20260525.py`, `insert_2026_fangshan_ermo_q21_contradiction_20260525.py`, `mark_2026_fangshan_ermo_render_pass_20260525.py`, updated `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`, updated `docx_insert_ledger.csv`, refreshed `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md/.csv`, and refreshed Governor/Confucius/status/render QA/model-ledger files in the future upload scope.
- Add post-Fangshan-Ermo render QA evidence, including `word_render_qa_20260525_global_style_norm`, contact sheet, and inspected target pages `page_133.png`, `page_153.png`, `page_154.png`, `page_251.png`, `page_252.png`, to future upload-scope candidates where appropriate.
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
    upsert_section(FILES["status"], "Fangshan 2026 Ermo Post-Render Status", SECTIONS["status"])
    upsert_section(FILES["governor"], "Governor Finding: Fangshan 2026 Ermo Post-Render Verification", SECTIONS["governor"])
    upsert_section(FILES["confucius"], "Artifact Check: Fangshan 2026 Ermo Post-Render Verification", SECTIONS["confucius"])
    upsert_section(FILES["model"], "MODEL_GATE_RENDER_QA_AFTER_FANGSHAN_2026_ERMO_LOCAL_REPAIR_20260525", SECTIONS["model"])
    upsert_section(FILES["upload"], "ORDER_063 Binding Refresh After Fangshan 2026 Ermo Render QA", SECTIONS["upload"])
    print("FANGSHAN_2026_ERMO_GOVERNANCE_UPDATES_WRITTEN")


if __name__ == "__main__":
    main()
