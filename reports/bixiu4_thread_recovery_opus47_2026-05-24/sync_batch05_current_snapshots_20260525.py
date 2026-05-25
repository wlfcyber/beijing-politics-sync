from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(r"C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible")
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
THREAD = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"


def sync_thread() -> None:
    text = THREAD.read_text(encoding="utf-8", errors="replace")
    text = text.replace(
        "3. Built `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` with 860 rows.",
        "3. Built `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv`; current post-Batch05 row count is 861.",
    )
    if "Completed Batch05 for `2026朝阳一模`" not in text:
        text = re.sub(
            r"(10\. Completed Batch04[^\n]*`M0034`, `M0035`, `M0036`\.)",
            r"\1\n11. Completed Batch05 for `2026朝阳一模`; inserted Q1/Q2/Q3 supported choice-key entries, retained supported Q16/Q21, excluded non-philosophy module rows, and applied ClaudeCode Q7 matrix-completeness correction `M0861`.",
            text,
        )

    artifact_section = """## Current Artifact Snapshot

- Current DOCX: `349,550` bytes.
- Current PDF: `3,856,219` bytes.
- PDF page count: `232`.
- Rendered page PNGs: `232` plus contact sheet.
- `docx_insert_ledger.csv`: `51` rows, `51 / 51` exact heading matches in DOCX.
- Full-document label style check: `2148 / 2148` label paragraphs pass.
- Automated DOCX/PDF scans: `0` hits for the current audit/source/reference/local-path residue banlist.

"""
    text = re.sub(r"## Current Artifact Snapshot\n\n.*?\n## Matrix Snapshot", artifact_section + "## Matrix Snapshot", text, flags=re.S)

    matrix_section = """## Matrix Snapshot

- Total rows: `861`.
- Batch02 `2024海淀一模` active pending rows: `0`.
- Batch03 `2026朝阳二模` active pending rows: `0`.
- Batch04 `2026石景山二模` active pending rows: `0`.
- Batch05 `2026朝阳一模` active pending rows: `0`.
- Exact rows still marked production-line candidate: `464`.
- Rows still marked as needing source/fusion adjudication: `464`.

"""
    text = re.sub(r"## Matrix Snapshot\n\n.*?\n## ClaudeCode / Model State", matrix_section + "## ClaudeCode / Model State", text, flags=re.S)

    if "`OPUS47_BATCH05_CHAOYANG_RECHECK_001`" not in text:
        text = text.replace(
            "- `OPUS47_BATCH04_SHIJINGSHAN_RECHECK_001`\n",
            "- `OPUS47_BATCH04_SHIJINGSHAN_RECHECK_001`\n- `OPUS47_BATCH05_CHAOYANG_RECHECK_001`\n",
        )
    text = text.replace("`485` production-line candidate rows", "`464` production-line candidate rows")
    THREAD.write_text(text, encoding="utf-8")


def sync_governor() -> None:
    text = GOVERNOR.read_text(encoding="utf-8", errors="replace")
    if "`OPUS47_BATCH05_CHAOYANG_RECHECK_001`" not in text:
        text = text.replace(
            "- `OPUS47_BATCH04_SHIJINGSHAN_RECHECK_001`\n",
            "- `OPUS47_BATCH04_SHIJINGSHAN_RECHECK_001`\n- `OPUS47_BATCH05_CHAOYANG_RECHECK_001`\n",
        )

    coverage_section = """## Coverage Matrix

`FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` contains `861` rows.

Current state after Batch05:

- Batch02 `2024海淀一模` active pending rows: `0`.
- Batch03 `2026朝阳二模` active pending rows: `0`.
- Batch04 `2026石景山二模` active pending rows: `0`.
- Batch05 `2026朝阳一模` active pending rows: `0`.
- Exact rows still marked production-line candidate: `464`.
- Rows still carrying need-source/fusion adjudication: `464`.

Boundary:

- This is a recovery control matrix, not final closure.
- Remaining candidate rows still require source/fusion disposition if the target is full-question exhaustion.

"""
    text = re.sub(r"## Coverage Matrix\n\n.*?\n## Batch01", coverage_section + "## Batch01", text, flags=re.S)

    if "## Batch05: 2026朝阳一模" not in text:
        text = text.replace(
            "This remains model-gate-blocked and is not final evidence.\n\n## Format / Render Gate",
            "This remains model-gate-blocked and is not final evidence.\n\n## Batch05: 2026朝阳一模\n\nGovernor decision: `BATCH05_SOURCE_CLOSURE_WITH_CORRECTION_APPLIED__RECOVERY_CONTINUES`\n\nCodex completed all suite rows, inserted Q1/Q2/Q3 final-body entries from official choice-key / correct-option chains, retained supported Q16/Q21 entries, excluded non-philosophy module rows, and applied the ClaudeCode correction by adding `M0861` for Q7 as a logic-and-thinking boundary row.\n\nThis remains model-gate-blocked and is not final evidence.\n\n## Format / Render Gate",
            1,
        )

    format_section = """## Format / Render Gate

Governor decision: `STYLE_AND_BATCH05_RENDER_CHECKED_STILL_SCOPE_BOUND`

Confirmed after latest rerender:

- DOCX exists: `349,550` bytes.
- PDF exists: `3,856,219` bytes.
- PDF page count: `232`.
- Rendered page PNGs: `232`, plus contact sheet.
- Insert ledger rows: `51`.
- Insert ledger exact heading matches: `51 / 51`.
- Full-document label style check: `2148 / 2148`.
- Automated DOCX/PDF scan: `0` hits for current residue banlist.
- Page-image scan: all `232` pages rendered at `993 x 1404 px`; only `page_002.png` is near-blank and was manually verified as the intended foreword page.

Boundary:

- Full every-page manual typography comparison is not claimed.

"""
    text = re.sub(r"## Format / Render Gate\n\n.*?\n## External Review Gates", format_section + "## External Review Gates", text, flags=re.S)
    text = text.replace("completed three suite batches", "completed four suite batches")
    text = text.replace("`485` production-line candidate rows", "`464` production-line candidate rows")
    GOVERNOR.write_text(text, encoding="utf-8")


def main() -> None:
    sync_thread()
    sync_governor()
    print("batch05 current snapshots synced")


if __name__ == "__main__":
    main()
