from __future__ import annotations

import csv
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent

THREAD_STATUS = ROOT / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = ROOT / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = ROOT / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
MODEL_LEDGER = ROOT / "MODEL_EVIDENCE_LEDGER.md"
REMAINING_MD = ROOT / "REMAINING_IN_BODY_NON_RUBRIC_EVIDENCE_BOUNDARIES_20260525.md"
REMAINING_CSV = ROOT / "REMAINING_IN_BODY_NON_RUBRIC_EVIDENCE_BOUNDARIES_20260525.csv"


def replace_section(path: Path, marker: str, section: str) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else f"# {path.stem}\n"
    needle = "\n## " + marker
    if needle in text:
        text = text[: text.index(needle)]
    path.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8", newline="\n")


def write_remaining_boundaries() -> None:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for path in [REMAINING_MD, REMAINING_CSV]:
        if path.exists():
            shutil.copy2(path, path.with_name(f"{path.stem}_backup_before_post_repair_zero_in_body_{stamp}{path.suffix}"))

    rows = [
        {
            "row_id": "M0144",
            "suite": "2024石景山一模",
            "question": "Q16/Q哲学",
            "previous_issue": "teacher-version broad answer only; no formal scoring source found",
            "final_disposition": "removed from current DOCX/PDF body and marked non-body boundary",
            "current_in_body_risk": "no",
            "evidence_file": "SHIJINGSHAN_2024_YIMO_Q16_SOURCE_EXHAUSTION_AND_DOCX_REMOVAL_20260525.md",
        },
        {
            "row_id": "M0195",
            "suite": "2024石景山一模",
            "question": "Q16/Q哲学",
            "previous_issue": "teacher-version broad answer only; duplicate/source-lane body risk",
            "final_disposition": "removed from current DOCX/PDF body and marked non-body boundary",
            "current_in_body_risk": "no",
            "evidence_file": "SHIJINGSHAN_2024_YIMO_Q16_SOURCE_EXHAUSTION_AND_DOCX_REMOVAL_20260525.md",
        },
        {
            "row_id": "M0201",
            "suite": "2024石景山一模",
            "question": "Q16/Q哲学",
            "previous_issue": "teacher-version broad answer only; duplicate/source-lane body risk",
            "final_disposition": "removed from current DOCX/PDF body and marked non-body boundary",
            "current_in_body_risk": "no",
            "evidence_file": "SHIJINGSHAN_2024_YIMO_Q16_SOURCE_EXHAUSTION_AND_DOCX_REMOVAL_20260525.md",
        },
        {
            "row_id": "M0315",
            "suite": "2024石景山一模",
            "question": "Q16/Q哲学",
            "previous_issue": "teacher-version broad answer only; duplicate/source-lane body risk",
            "final_disposition": "removed from current DOCX/PDF body and marked non-body boundary",
            "current_in_body_risk": "no",
            "evidence_file": "SHIJINGSHAN_2024_YIMO_Q16_SOURCE_EXHAUSTION_AND_DOCX_REMOVAL_20260525.md",
        },
        {
            "row_id": "M0771",
            "suite": "2026西城二模",
            "question": "Q20",
            "previous_issue": "teacher/reference broad-angle support only",
            "final_disposition": "repaired with rendered formal pingbiao PDF evidence; broad-angle scoring support, not point-by-point unique scoring",
            "current_in_body_risk": "no",
            "evidence_file": "XICHENG_2026_ERMO_Q20_FORMAL_PINGBIAO_REPAIR_20260525.md",
        },
    ]
    with REMAINING_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    REMAINING_MD.write_text("""# Remaining In-Body Non-Rubric Evidence Boundaries

status: `NO_REMAINING_IN_BODY_NON_RUBRIC_BOUNDARIES_AFTER_REPAIR`

Updated: 2026-05-25 13:58 +08

This file supersedes the earlier five-row open-boundary snapshot. The earlier snapshot correctly identified the remaining body risks at that time; later repairs removed or reclassified all five from the current in-body risk queue.

## Current Verified State

- Matrix rows audited: `1471`.
- Rows marked in-book/body in the latest risk audit: `424`.
- Total risk rows still queued for non-body/candidate disposition: `329`.
- In-book/body risk rows: `0`.
- Current risk audit: `MATRIX_EVIDENCE_RISK_AUDIT_20260525.md` and `MATRIX_EVIDENCE_RISK_AUDIT_20260525.csv`.

## Superseded Five-Row Disposition

- `M0144`, `M0195`, `M0201`, `M0315`: `2024石景山一模 Q16/Q哲学` had no formal scoring/rubric source in the local raw suite or preprocessed manifest. The two current DOCX body headings were removed, remaining heading hits are `0`, and the rows are now non-body evidence boundaries.
- `M0771`: `2026西城二模 Q20` was repaired with rendered formal `西城二模评标.pdf` evidence at `xicheng_rubric/page_014.png`. The support is broad-angle scoring support, not point-by-point unique scoring.

## Boundary

- This closes the current in-body non-rubric boundary queue only.
- It does not close GPTPro web review, Claude web/app Opus 4.7 review, ClaudeCode model confirmation, full manual every-page typography review, or the non-body/candidate risk queue.
""", encoding="utf-8", newline="\n")


def main() -> int:
    write_remaining_boundaries()

    status_section = """
## Post-Repair Local Evidence Status
Updated: 2026-05-25 13:58 +08

- Current status: `RECOVERED_EXECUTION_IN_PROGRESS_LOCAL_BODY_EVIDENCE_CLEARED_MODEL_GATES_OPEN`.
- Latest matrix evidence audit: `1471` rows audited, `424` in-book/body rows, `329` total risk rows, `0` in-book/body risk rows.
- `2024石景山一模 Q16/Q哲学`: no formal scoring source found; `2` current DOCX headings removed; remaining heading hits `0`; affected rows `M0144`, `M0195`, `M0201`, `M0315` are non-body boundaries.
- `2026西城二模 Q20`: repaired with rendered formal `西城二模评标.pdf` evidence; row `M0771` now has formal broad-angle pingbiao support.
- DOCX/PDF after removal and re-export: `279/279` rendered pages, `2779/2779` DOCX/PDF label counts, `0` blank-like body pages.
- Post-repair ClaudeCode command-line recheck: `content_result=pass_with_notes`, `local_policy_result=pass_with_model_gate_blocked`; runtime evidence includes `claude-haiku-4-5-20251001` and `claude-opus-4-7`, so it is not promoted to fully qualified model evidence.
- Claude web/app external review remains `real_call_pending`; corrected retry route is direct `https://claude.ai` auto-login, never the Google-login loop.
- GPTPro web review remains `real_call_pending`.
- ORDER_063 GitHub upload remains deferred; no push is allowed until all active Beijing politics lines reach terminal status and the future upload scope plus secret scan is complete.
"""
    replace_section(THREAD_STATUS, "Post-Repair Local Evidence Status", status_section)

    governor_section = """
## Governor Finding: Post-Repair Local Evidence Status
Updated: 2026-05-25 13:58 +08

- Governor decision: `LOCAL_IN_BODY_EVIDENCE_PASS_EXTERNAL_MODEL_GATES_OPEN`.
- The earlier five in-body non-rubric evidence boundaries have been superseded by later repair:
  - `2024石景山一模 Q16/Q哲学` was removed from current DOCX/PDF body placement after source exhaustion found no formal scoring file.
  - `2026西城二模 Q20` was repaired with formal rendered pingbiao evidence and retained only as broad-angle scoring support.
- Refreshed audit result: `1471` matrix rows, `424` in-book/body rows, `329` total risk rows, `0` in-book/body risk rows.
- Render QA after the removal/export passes automated checks: `279/279` pages rendered, label counts `2779/2779`, blank-like body pages `0`.
- ClaudeCode post-repair recheck content result is `pass_with_notes`, but model evidence remains blocked because runtime evidence includes auxiliary Haiku plus Opus traces.
- External review gates remain open: GPTPro web review `real_call_pending`; Claude web/app Opus 4.7 adaptive review `real_call_pending` despite direct `https://claude.ai` login path being verified earlier.
- No final acceptance claim is authorized; the project remains recovered execution with open model/external-review gates.
- ORDER_063 remains binding: no GitHub push now; future upload requires selective scope, secret scan, `NO_SECRET_PATTERN_MATCHES`, then commit/push only after all active lines end.
"""
    replace_section(GOVERNOR, "Governor Finding: Post-Repair Local Evidence Status", governor_section)

    confucius_section = """
## Artifact Check: Post-Repair Local Evidence Status
Updated: 2026-05-25 13:58 +08

- `SHIJINGSHAN_2024_YIMO_Q16_SOURCE_EXHAUSTION_AND_DOCX_REMOVAL_20260525.md`: present; records source exhaustion, removal of `2` DOCX headings, and `0` remaining heading hits.
- `XICHENG_2026_ERMO_Q20_FORMAL_PINGBIAO_REPAIR_20260525.md`: present; records rendered formal pingbiao PDF evidence for Q20.
- `REMAINING_IN_BODY_NON_RUBRIC_EVIDENCE_BOUNDARIES_20260525.md`: updated to `NO_REMAINING_IN_BODY_NON_RUBRIC_BOUNDARIES_AFTER_REPAIR`.
- `OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RECHECK_RESULT.md`: present; content result `pass_with_notes`, local policy result `pass_with_model_gate_blocked`.
- `OPUS47_CLAUDECODE_POST_REPAIR_IN_BODY_EVIDENCE_RUNTIME_EVIDENCE.json`: present; observed models include `claude-haiku-4-5-20251001` and `claude-opus-4-7`, with thinking/signature evidence seen.
- `STYLE_NORMALIZATION_AUDIT_20260525.md` and `FORMAT_RENDER_QA_20260524.md`: current render snapshot shows `279/279` pages, label counts `2779/2779`, blank-like body pages `0`.
- Remaining open gates: GPTPro web review, Claude web/app Opus 4.7 review through direct `https://claude.ai`, ClaudeCode model confirmation, full manual typography pass, and deferred ORDER_063 final GitHub upload.
"""
    replace_section(CONFUCIUS, "Artifact Check: Post-Repair Local Evidence Status", confucius_section)

    model_section = """
## MODEL_GATE_SUMMARY_AFTER_POST_REPAIR_RECHECK_20260525

status: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`

- New post-repair ClaudeCode command-line call completed at `2026-05-25T13:56:12`.
- Content result: `pass_with_notes`.
- Local policy result: `pass_with_model_gate_blocked`.
- Observed models: `claude-haiku-4-5-20251001, claude-opus-4-7`.
- Thinking block/signature seen: `true`.
- Qualified model-evidence decision: not fully qualified because auxiliary Haiku appears in runtime/debug evidence.
- Claude web/app path correction remains active: retry must use direct `https://claude.ai` auto-login, not a Google-login loop.
- Claude web/app external review and GPTPro web review remain `real_call_pending` until real captured responses exist.
"""
    replace_section(MODEL_LEDGER, "MODEL_GATE_SUMMARY_AFTER_POST_REPAIR_RECHECK_20260525", model_section)
    print("post_repair_reports_synced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
