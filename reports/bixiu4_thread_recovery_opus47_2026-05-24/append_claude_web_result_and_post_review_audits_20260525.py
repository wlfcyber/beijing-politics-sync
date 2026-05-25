from __future__ import annotations

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
NOW = datetime.now().strftime("%Y-%m-%d %H:%M +08")
MARKER = "CLAUDE_WEB_OPUS47_STYLE_FIX_REVIEW_AND_POST_AUDITS_20260525"


def append_once(name: str, marker: str, block: str) -> None:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    if text and not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n" + block.strip() + "\n", encoding="utf-8", newline="\n")


common = f"""
- Updated: {NOW}
- Claude web/app route: direct `https://claude.ai`; Google login path used: `no`.
- Real web/app evidence captured: `CLAUDE_WEB_OPUS47_FULL_ARTIFACT_REVIEW_RESULT_AFTER_STYLE_FIX_20260525.md`.
- Chat URL: `https://claude.ai/chat/36005659-2dac-47c5-9ece-037fb0fcc908`.
- Visible model/session evidence: signed-in `Max plan`, composer model `Opus 4.7 Adaptive`.
- Attached review set included latest matrix, risk audit, style audit, render manifest, model ledger, sonnet invalidation ledger, Governor report, DOCX, and PDF.
- Claude web external result: `pass_with_open_gates`; this is not final acceptance.
- Claude-identified open gates: full 721-entry thickness review, row-level reverse sampling beyond triage, weak/status-tag machine checks, ClaudeCode replacement evidence, GPTPro web capture, every-page visual review, and extra label breakdown.
- Post-Claude local audits generated:
  - `CLAUDE_RECOMMENDED_ROW_LEVEL_REVERSE_SAMPLE_AUDIT_20260525.md/.csv`: 80 deterministic body-row reverse samples; status `PASS_SAMPLE_NO_WEAK_ONLY_BODY_ROWS`.
  - `CLAUDE_RECOMMENDED_SPECIAL_TAG_AUDIT_20260525.md/.csv`: 106 matched special/status rows; status `SPECIAL_TAGS_CLASSIFIED_NO_UNRESOLVED_BODY_STATUS_TAGS`.
  - `BODY_WEAK_EVIDENCE_REVERSE_CHECK_20260525.md/.csv`: 558 body rows checked; 275 weak-signal body rows all have formal or objective-choice boundary support; status `PASS_NO_WEAK_ONLY_BODY_EVIDENCE`.
  - `FORMAT_EXTRA_LABEL_BREAKDOWN_20260525.md/.json`: explains the 2891 vs 4*721 tail difference as 7 extra bracketed source-subhead markers inside required label paragraphs; status `EXTRA_LABEL_BREAKDOWN_CLOSED`.
  - `THICKNESS_DENSITY_AUDIT_20260525.md/.csv`: 721 entries audited; 643 density candidates; status `THICKNESS_QUEUE_CREATED_REQUIRES_REVIEW`.
- Remaining blockers: GPTPro web full-artifact review `real_call_pending`; ClaudeCode replacement/model-confirmed lane still not closed; thickness queue remains open; full every-page manual visual log remains open; final GitHub upload remains deferred by ORDER_063.
- Sonnet/Haiku/model-unknown outputs remain excluded from qualified evidence.
- No GitHub push has been attempted.
""".strip()


append_once(
    "THREAD_RECOVERY_STATUS_20260524.md",
    MARKER,
    f"""
## {MARKER}

{common}
""",
)

append_once(
    "MODEL_EVIDENCE_LEDGER.md",
    MARKER,
    f"""
## CLAUDE_WEB_OPUS47_STYLE_FIX_REVIEW_CAPTURE_20260525

status: `REAL_CLAUDE_WEB_OPUS47_REVIEW_CAPTURED_PASS_WITH_OPEN_GATES`

{common}

Evidence boundary:

- This counts only as a real Claude web/app Opus 4.7 Adaptive external review capture.
- It does not count as ClaudeCode production-lane model proof.
- It does not close GPTPro review.
- It does not close final acceptance because the captured answer itself requires corrections before acceptance.
""",
)

append_once(
    "GOVERNOR_RECOVERY_REPORT_20260524.md",
    MARKER,
    f"""
## Governor Finding: Claude Web Opus 4.7 Style-Fix Review And Post-Audits

{common}

Governor decision: `EXTERNAL_CLAUDE_WEB_REVIEW_CAPTURED_LOCAL_POST_AUDITS_PARTIAL_CLOSURE_GATES_OPEN`.

Governor boundary:

- Local coverage/placement evidence is stronger after the reverse sample, special-tag audit, weak-evidence reverse check, and extra-label breakdown.
- The thickness audit creates an explicit content-review queue and prevents any final acceptance claim.
""",
)

append_once(
    "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md",
    MARKER,
    f"""
## Artifact Check: Claude Web Opus 4.7 Result And Post-Audits

{common}

Artifact boundary:

- The captured Claude answer and screenshot are present.
- The post-Claude audit scripts and outputs are present.
- The zero-baseline learner thickness queue remains open because density triage produced 643 candidates.
""",
)

append_once(
    "FORMAT_RENDER_QA_20260524.md",
    MARKER,
    f"""
## Claude Web Opus 4.7 Format Findings And Extra Label Closure 20260525

{common}

Format-specific update:

- Structural style/render evidence remains local-pass: 721 entries, inserted/legacy 415/306, heading pPr/rPr 1/1, rendered pages 290/290, DOCX/PDF labels 2891/2891.
- Claude requested the 7-label tail difference be explained; `FORMAT_EXTRA_LABEL_BREAKDOWN_20260525.md/.json` closes that accounting issue.
- Every-page visual review is still open; contact-sheet inspection is not equivalent to 290-page manual review.
""",
)

append_once(
    "CLAUDE_WEB_LOGIN_CORRECTION_20260525.md",
    MARKER,
    f"""
## Direct Route Success After Heading Style Fix
Updated: {NOW}

- Direct `https://claude.ai` route succeeded.
- Google login path used: `no`.
- Signed-in session and `Opus 4.7 Adaptive` model button were visible.
- Full artifact review was submitted with attached latest DOCX/PDF and governance artifacts.
- Captured result: `CLAUDE_WEB_OPUS47_FULL_ARTIFACT_REVIEW_RESULT_AFTER_STYLE_FIX_20260525.md`.
- Result status: `pass_with_open_gates`; the review is real but does not authorize final acceptance.
""",
)

append_once(
    "BIXIU4_DEFERRED_FINAL_UPLOAD_SCOPE_REQUIREMENTS_20260525.md",
    MARKER,
    f"""
## ORDER_063 Binding Refresh After Claude Web Opus 4.7 Style-Fix Review

{common}

Future upload scope additions:

- `CLAUDE_WEB_OPUS47_FULL_ARTIFACT_REVIEW_PACKET_AFTER_STYLE_FIX_20260525.md`
- `CLAUDE_WEB_OPUS47_FULL_ARTIFACT_REVIEW_RESULT_AFTER_STYLE_FIX_20260525.md`
- `CLAUDE_WEB_OPUS47_FULL_ARTIFACT_REVIEW_RESULT_AFTER_STYLE_FIX_20260525.png`
- `post_claude_recommendation_audits_20260525.py`
- `CLAUDE_RECOMMENDED_ROW_LEVEL_REVERSE_SAMPLE_AUDIT_20260525.md/.csv`
- `CLAUDE_RECOMMENDED_SPECIAL_TAG_AUDIT_20260525.md/.csv`
- `BODY_WEAK_EVIDENCE_REVERSE_CHECK_20260525.md/.csv`
- `FORMAT_EXTRA_LABEL_BREAKDOWN_20260525.md/.json`
- `THICKNESS_DENSITY_AUDIT_20260525.md/.csv`
- refreshed status, model ledger, Governor, Confucius, and format QA files.

Upload remains deferred until all active Beijing politics lines reach terminal or user-approved blocker state, then exact upload scope, secret-pattern scan, `NO_SECRET_PATTERN_MATCHES`, commit, push, upload report, and final heartbeat.
""",
)

print(MARKER)
