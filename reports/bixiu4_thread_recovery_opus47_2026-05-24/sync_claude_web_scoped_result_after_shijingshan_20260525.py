from pathlib import Path

ROOT = Path(__file__).resolve().parent

NEW_STATUS = "RECOVERED_EXECUTION_IN_PROGRESS_LOCAL_BODY_EVIDENCE_CLEARED_CLAUDE_SCOPED_REVIEW_CAPTURED_FULL_GATES_OPEN"


def append_once(filename: str, marker: str, section: str) -> None:
    path = ROOT / filename
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        path.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8")


def update_status() -> None:
    path = ROOT / "THREAD_RECOVERY_STATUS_20260524.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("Status: `"):
            lines[i] = f"Status: `{NEW_STATUS}`"
            break
    for i, line in enumerate(lines):
        if line.startswith("Timestamp: "):
            lines[i] = "Timestamp: 2026-05-25 14:36 +08"
            break
    marker = "## Claude Web Opus 4.7 Direct Scoped Review After Shijingshan"
    section = """

## Claude Web Opus 4.7 Direct Scoped Review After Shijingshan
Updated: 2026-05-25 14:36 +08

- Status: `SCOPED_CLAUDE_WEB_OPUS47_ADAPTIVE_REVIEW_CAPTURED_FULL_GATES_OPEN`.
- Route used: direct `https://claude.ai` auto-login.
- Google login path used: `no`.
- Chat URL: `https://claude.ai/chat/689edf8d-5b3f-4b27-9fb6-c733876734e9`.
- Observed model UI at submission: `Opus 4.7 Adaptive`; observed account plan UI: `Max plan`.
- Captured result: `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_RESULT_AFTER_SHIJINGSHAN_20260525.md`.
- Screenshot evidence: `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_RESULT_AFTER_SHIJINGSHAN_20260525.png`.
- Claude scoped verdict: keep recovered execution in progress/open gate; Sonnet 22:01 and 22:09 stay invalidated; ordinary reference answers cannot substitute formal rubric/marking evidence; current body row-level risk `0` does not close broader non-body candidate queue or external gates.
- Clean single-packet retry note: a later attempt to open/claim a fresh new Claude page through the same direct route timed out in browser automation and is not counted as a result.
- Still open: GPTPro web review `real_call_pending`; full Claude Opus web/app DOCX/PDF artifact review `real_call_pending`; ClaudeCode model confirmation `BLOCKED_MODEL_CONFIRMATION_REQUIRED`; full manual typography pass; ORDER_063 deferred upload gate.
"""
    text2 = "\n".join(lines) + "\n"
    if marker not in text2:
        text2 += section
    path.write_text(text2, encoding="utf-8")


def main() -> None:
    update_status()
    append_once(
        "MODEL_EVIDENCE_LEDGER.md",
        "## CLAUDE_WEB_OPUS47_DIRECT_SCOPED_REVIEW_AFTER_SHIJINGSHAN_20260525",
        """
## CLAUDE_WEB_OPUS47_DIRECT_SCOPED_REVIEW_AFTER_SHIJINGSHAN_20260525

status: `SCOPED_REVIEW_CAPTURED_FULL_ARTIFACT_REVIEW_PENDING`

- Route used: direct `https://claude.ai` auto-login.
- Google login path used: `no`.
- Chat URL: `https://claude.ai/chat/689edf8d-5b3f-4b27-9fb6-c733876734e9`.
- Observed model UI at submission: `Opus 4.7 Adaptive`.
- Captured result file: `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_RESULT_AFTER_SHIJINGSHAN_20260525.md`.
- Screenshot evidence: `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_RESULT_AFTER_SHIJINGSHAN_20260525.png`.
- Evidence decision: counts only as a real scoped Claude web/app Opus 4.7 Adaptive review of governance/evidence boundaries after Shijingshan local repair.
- It does not close the full DOCX/PDF Claude artifact review; that remains `real_call_pending`.
- GPTPro web external review remains `real_call_pending`.
- ClaudeCode model evidence remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` when runtime/debug artifacts include auxiliary Haiku alongside Opus.
- Sonnet/Haiku/model-unknown output remains excluded from qualified ClaudeCode evidence.
- Clean single-packet retry attempt after this result timed out in browser automation; it is not counted as model evidence or as a failure of direct login.
""",
    )
    append_once(
        "GOVERNOR_RECOVERY_REPORT_20260524.md",
        "## Governor Finding: Claude Web Opus 4.7 Direct Scoped Review After Shijingshan",
        """
## Governor Finding: Claude Web Opus 4.7 Direct Scoped Review After Shijingshan
Updated: 2026-05-25 14:36 +08

- Governor decision: `SCOPED_EXTERNAL_REVIEW_CAPTURED_BUT_FULL_GATES_REMAIN_OPEN`.
- The corrected direct Claude path was used: `https://claude.ai` auto-login, with no Google login loop.
- UI evidence at submission showed `Opus 4.7 Adaptive`; account/plan UI showed `Max plan`.
- Captured Claude scoped verdict agrees with local governance: keep the thread in recovered execution/open-gate status; do not count Sonnet/Haiku/model-unknown output; do not treat ordinary references as formal rubric evidence; do not convert body-risk `0` into full final acceptance.
- The scoped review also flagged that stale and latest risk counts can coexist in packets; latest local audit must be the single facts source for current status.
- Boundary: this scoped review does not equal a full DOCX/PDF Claude artifact review and does not close GPTPro review, ClaudeCode model confirmation, typography review, or ORDER_063 upload.
""",
    )
    append_once(
        "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md",
        "## Artifact Check: Claude Web Opus 4.7 Direct Scoped Review After Shijingshan",
        """
## Artifact Check: Claude Web Opus 4.7 Direct Scoped Review After Shijingshan
Updated: 2026-05-25 14:36 +08

- `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_PACKET_AFTER_SHIJINGSHAN_20260525.md`: present.
- `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_RESULT_AFTER_SHIJINGSHAN_20260525.md`: present and status `SCOPED_CLAUDE_WEB_OPUS47_ADAPTIVE_REVIEW_CAPTURED_OPEN_GATES_REMAIN`.
- `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_RESULT_AFTER_SHIJINGSHAN_20260525.png`: present.
- Direct route verified: `https://claude.ai` auto-login; Google login path not used.
- Captured chat URL: `https://claude.ai/chat/689edf8d-5b3f-4b27-9fb6-c733876734e9`.
- Result boundary: scoped governance/evidence-boundary review captured; full DOCX/PDF artifact review remains `real_call_pending`.
""",
    )
    append_once(
        "CLAUDE_WEB_LOGIN_CORRECTION_20260525.md",
        "## Direct Route Outcome After Shijingshan Repair",
        """
## Direct Route Outcome After Shijingshan Repair
Updated: 2026-05-25 14:36 +08

- Corrected route was used successfully: direct `https://claude.ai` auto-login.
- Google login path used: `no`.
- Captured scoped review result: `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_RESULT_AFTER_SHIJINGSHAN_20260525.md`.
- Chat URL: `https://claude.ai/chat/689edf8d-5b3f-4b27-9fb6-c733876734e9`.
- Remaining blocker wording must distinguish the completed scoped review from the still pending full DOCX/PDF Claude Opus artifact review.
""",
    )
    append_once(
        "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
        "## Claude Web Scoped Review Artifacts To Consider",
        """
## Claude Web Scoped Review Artifacts To Consider

Updated: 2026-05-25 14:36 +08

- Include `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_PACKET_AFTER_SHIJINGSHAN_20260525.md`, `CLAUDE_WEB_OPUS47_DIRECT_REVIEW_RESULT_AFTER_SHIJINGSHAN_20260525.md`, screenshot evidence, and the updated model/governor/confucius/status ledgers in the future upload scope.
- Do not upload now. ORDER_063 still requires all active Beijing politics lines to end first, then exact upload scope, secret-pattern scan, `NO_SECRET_PATTERN_MATCHES`, commit, push, upload report, and final heartbeat.
""",
    )


if __name__ == "__main__":
    main()
