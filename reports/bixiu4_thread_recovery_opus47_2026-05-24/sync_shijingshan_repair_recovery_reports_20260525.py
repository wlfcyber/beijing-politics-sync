from pathlib import Path

ROOT = Path(__file__).resolve().parent

NEW_STATUS = "RECOVERED_EXECUTION_IN_PROGRESS_LOCAL_BODY_EVIDENCE_CLEARED_AFTER_SHIJINGSHAN_REPAIR_MODEL_GATES_OPEN"


def update_status_file() -> None:
    path = ROOT / "THREAD_RECOVERY_STATUS_20260524.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("Status: `"):
            lines[i] = f"Status: `{NEW_STATUS}`"
            break
    for i, line in enumerate(lines):
        if line.startswith("Timestamp: "):
            lines[i] = "Timestamp: 2026-05-25 14:25 +08"
            break
    marker = "## Shijingshan 2025 Yimo Candidate Queue Repair"
    section = f"""

{marker}
Updated: 2026-05-25 14:25 +08

- Status: `SHIJINGSHAN_2025_YIMO_MATRIX_REPAIRED_NO_DOCX_CHANGE_MODEL_GATES_OPEN`.
- Matrix repair: `28` 2025石景山一模 rows updated; matrix backup created before rewrite.
- Current DOCX finding: `7` 2025石景山一模 suite heading blocks remain valid current-body coverage: Q16 x3, Q21 x2, choice Q3 x1, choice Q4 x1.
- Current DOCX exclusion check: low-altitude-economy Q18 hits `0`; scientific-thinking Q19 hits `0`; legal Q20 hits `0`.
- Source adjudication: Q16 kept only under formal scoring support for 联系观/发展观/矛盾观 and Chinese excellent traditional culture value; the unsupported standalone objective-law/subjective-initiative placement was corrected.
- Boundary adjudication: Q17 politics/IR, Q18 economics, Q19 logic/scientific thinking, and Q20 law are excluded from Bixiu4 body; Q21 keeps only Bixiu4-relevant reform/social-development-law points.
- Choice-question boundary: Q3/Q4 remain current-DOCX choice chains with official answer-key support; they are not counted as main-question scoring-rubric evidence.
- Refreshed risk audit: matrix rows `1471`, in-book/body rows `442`, total risk rows `288`, in-book/body risk rows `0`, 2025石景山一模 risk rows `0`.
- DOCX/PDF unchanged in this repair; no re-render required beyond the current Yanqing/global-style render snapshot.
- External gates remain open: GPTPro web review `real_call_pending`; Claude Opus web/app review `real_call_pending`; ClaudeCode model confirmation remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- ORDER_063 remains binding: no GitHub push now; final upload waits for all active Beijing politics lines and future upload scope plus secret scan.
"""
    text2 = "\n".join(lines) + "\n"
    if marker not in text2:
        text2 += section
    path.write_text(text2, encoding="utf-8")


def append_once(filename: str, marker: str, section: str) -> None:
    path = ROOT / filename
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8")


def main() -> None:
    update_status_file()

    append_once(
        "GOVERNOR_RECOVERY_REPORT_20260524.md",
        "## Governor Finding: Shijingshan 2025 Yimo Candidate Queue Repair",
        """
## Governor Finding: Shijingshan 2025 Yimo Candidate Queue Repair
Updated: 2026-05-25 14:25 +08

- Governor decision: `LOCAL_MATRIX_BOUNDARY_REPAIRED_NO_DOCX_CHANGE_MODEL_GATES_OPEN`.
- Finding: 2025石景山一模 had candidate/pending matrix wording that blurred current-DOCX coverage, choice-question chains, and non-Bixiu4 module boundaries.
- Corrective action: `28` rows were rewritten against the cached source bundle and current DOCX context.
- Q16 is retained as formal-rubric coverage for 联系观/发展观/矛盾观 and Chinese excellent traditional culture value; the old independent objective-law/subjective-initiative node is no longer treated as supported by this suite.
- Q3/Q4 are retained only as choice-question chains supported by the official answer key; they are not main-question scoring evidence.
- Q17/Q18/Q19/Q20 are excluded by module boundary. Q21 keeps only Bixiu4-relevant reform/social-development-law points already present in current DOCX.
- Refreshed audit result: total risk rows `288`, in-book/body risk rows `0`, and 2025石景山一模 risk rows `0`.
- No DOCX/PDF text was changed in this repair, so the latest valid render snapshot remains the Yanqing/global-style snapshot: `278/278` pages, label counts `2771/2771`, blank-like body pages `0`.
- Boundary: this is local source/matrix/DOCX-context governance only. GPTPro web and Claude Opus web/app reviews remain `real_call_pending`; no final acceptance claim or early GitHub push is authorized.
""",
    )

    append_once(
        "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md",
        "## Artifact Check: Shijingshan 2025 Yimo Candidate Queue Repair",
        """
## Artifact Check: Shijingshan 2025 Yimo Candidate Queue Repair
Updated: 2026-05-25 14:25 +08

- `repair_2025_shijingshan_yimo_candidate_queue_20260525.py`: present.
- `SHIJINGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.md`: present and status `SHIJINGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIRED`.
- `SHIJINGSHAN_2025_YIMO_CANDIDATE_QUEUE_REPAIR_20260525.json`: present.
- Matrix backup before rewrite: present.
- `CURRENT_DOCX_2025_SHIJINGSHAN_YIMO_CONTEXT_20260525.md`: present; current DOCX has Q16/Q21/Q3/Q4 blocks only for this suite.
- Refreshed audit: matrix rows `1471`, in-book/body rows `442`, total risk rows `288`, in-book/body risk rows `0`, 2025石景山一模 risk rows `0`.
- DOCX/PDF unchanged in this repair; no new render artifact was required.
- Remaining open gates: GPTPro web review, Claude web/app Opus 4.7 review through direct `https://claude.ai`, ClaudeCode model confirmation, full manual typography pass, and deferred ORDER_063 final GitHub upload.
""",
    )

    append_once(
        "MODEL_EVIDENCE_LEDGER.md",
        "## MODEL_GATE_SUMMARY_AFTER_SHIJINGSHAN_LOCAL_REPAIR_20260525",
        """
## MODEL_GATE_SUMMARY_AFTER_SHIJINGSHAN_LOCAL_REPAIR_20260525

status: `NO_NEW_EXTERNAL_MODEL_EVIDENCE_LOCAL_REPAIR_ONLY`

- 2025石景山一模 repair was performed by local cached source bundle, current DOCX context, and matrix verification only.
- No new ClaudeCode, Claude web/app, or GPTPro web answer is counted for this local repair.
- Claude web/app route remains direct `https://claude.ai` auto-login; no Google-login loop is valid.
- Claude web/app external review remains `real_call_pending`.
- GPTPro web external review remains `real_call_pending`.
- ClaudeCode post-repair model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` because prior runtime/debug evidence includes auxiliary Haiku alongside Opus.
- Sonnet/Haiku/model-unknown output remains excluded from qualified evidence.
""",
    )

    append_once(
        "FORMAT_RENDER_QA_20260524.md",
        "## Shijingshan Matrix-Only Repair Render Note 20260525",
        """
## Shijingshan Matrix-Only Repair Render Note 20260525

- Status: `NO_DOCX_CHANGE_NO_RERENDER_REQUIRED_AFTER_SHIJINGSHAN_MATRIX_REPAIR`.
- 2025石景山一模 repair updated the coverage matrix and governance ledgers only.
- Current DOCX/PDF content was not modified; no new Word COM export or PDF render was required for this suite.
- Latest applicable render QA remains the Yanqing/global-style snapshot: `278/278` pages, DOCX/PDF label counts `2771/2771`, blank-like body pages `0`.
- Boundary: automated render QA remains pass for the current files, while GPTPro/Claude Opus web external reviews remain `real_call_pending`.
""",
    )

    append_once(
        "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
        "## Shijingshan Repair Artifacts To Consider",
        """
## Shijingshan Repair Artifacts To Consider

Updated: 2026-05-25 14:25 +08

- Include the Shijingshan repair script, repair report/JSON, matrix backup pointer, current DOCX context probe, refreshed matrix audit, and updated Governor/Confucius/status/model ledgers in the future upload scope.
- Do not upload now. ORDER_063 still requires all active Beijing politics lines to end first, then exact upload scope, secret-pattern scan, `NO_SECRET_PATTERN_MATCHES`, commit, push, upload report, and final heartbeat.
""",
    )


if __name__ == "__main__":
    main()
