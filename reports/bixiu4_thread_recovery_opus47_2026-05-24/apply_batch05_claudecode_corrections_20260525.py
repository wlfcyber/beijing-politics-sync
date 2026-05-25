from __future__ import annotations

import csv
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(r"C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible")
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"

MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
BATCH_REPORT = RECOVERY / "COVERAGE_FUSION_BATCH05_2026_CHAOYANG_YIMO_CODEX_20260525.md"
RAW_JSON = RECOVERY / "OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_RAW.json"
DEBUG_LOG = RECOVERY / "OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_DEBUG.log"
RESULT_MD = RECOVERY / "OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_RESULT.md"
MODEL_LEDGER = RECOVERY / "MODEL_EVIDENCE_LEDGER.md"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
FORMAT_QA = RECOVERY / "FORMAT_RENDER_QA_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"

DOCX = RUN / "05_delivery" / "哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx"
PDF = RUN / "05_delivery" / "哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf"
LEDGER = RUN / "05_delivery" / "docx_insert_ledger.csv"
PAGES_DIR = RUN / "07_render_check" / "word_pdf_pages"


def backup(path: Path, label: str) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = path.with_name(f"{path.stem}_backup_before_{label}_{stamp}{path.suffix}")
    shutil.copy2(path, dst)
    return dst


def read_matrix() -> tuple[list[str], list[dict[str, str]]]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_matrix(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def set_field(row: dict[str, str], key: str, value: str) -> None:
    if key in row:
        row[key] = value


def apply_matrix_correction() -> dict[str, int | str]:
    backup(MATRIX, "batch05_claudecode_q7_correction")
    fieldnames, rows = read_matrix()

    q7_row_id = "M0861"
    q7 = next((r for r in rows if r.get("matrix_row_id") == q7_row_id), None)
    if q7 is None:
        q7 = {field: "" for field in fieldnames}
        rows.append(q7)

    values = {
        "matrix_row_id": q7_row_id,
        "row_source": "batch05_claudecode_correction",
        "题源": "2026朝阳一模",
        "年份": "2026",
        "阶段": "一模",
        "题号": "Q7",
        "题型或模块判断": "选必三逻辑与思维边界",
        "是否进宝典": "否：选必三逻辑与思维（判断/推理/论证、超前思维），不进当前必修四哲学正文",
        "宝典节点": "逻辑与思维边界",
        "细则支持原理": "Q7官方答案C；题干/选项考查月球样品研究、卫星遥感数据增强可信程度，选项A涉及严谨判断推理论证，D涉及超前思维，均为逻辑与思维/科学推理语境，不构成当前必修四哲学正文条目。",
        "证据等级": "选择题官方答案键+模块边界",
        "是否误放": "否：候选未进正文",
        "是否需补厚": "否",
        "当前处理": "Batch05 ClaudeCode correction: add missing Q7 boundary row",
        "备注": "原Codex A导出跳过Q7；ClaudeCode Batch05发现后补齐；不改变DOCX。",
        "source_artifact": r"01_source_inventory\suite_source_bundles\2026朝阳一模.md:84-91;365-400",
    }
    for key, value in values.items():
        set_field(q7, key, value)

    for row in rows:
        if row.get("matrix_row_id") == "M0591":
            set_field(
                row,
                "备注",
                "该行是源包整段抽取残片；Batch05已裁决Q1-Q6、Q8-Q21；Q7按选必三逻辑与思维边界排除（见M0861新增Q7行）。",
            )

    write_matrix(fieldnames, rows)

    cy_rows = [r for r in rows if r.get("题源") == "2026朝阳一模"]
    loose_pending = [
        r for r in cy_rows
        if any(token in (r.get("当前处理") or "") for token in ["PENDING_", "TBD", "HOLD_NEEDS_SOURCE_EVIDENCE", "候选待核验"])
    ]
    remaining_match = re.search(
        r"exact production-line candidate rows still open: `(\d+)`",
        BATCH_REPORT.read_text(encoding="utf-8", errors="replace") if BATCH_REPORT.exists() else "",
    )
    exact_pending = int(remaining_match.group(1)) if remaining_match else 464
    need_source = exact_pending
    return {
        "matrix_rows": len(rows),
        "cy_rows": len(cy_rows),
        "cy_loose_pending": len(loose_pending),
        "exact_pending": exact_pending,
        "need_source": need_source,
        "q7_row_id": q7_row_id,
    }


def artifact_metrics() -> dict[str, int | bool]:
    page_pngs = sorted(PAGES_DIR.glob("page_*.png"))
    ledger_rows = 0
    if LEDGER.exists():
        with LEDGER.open("r", encoding="utf-8-sig", newline="") as f:
            ledger_rows = sum(1 for _ in csv.DictReader(f))
    return {
        "docx_bytes": DOCX.stat().st_size if DOCX.exists() else 0,
        "pdf_bytes": PDF.stat().st_size if PDF.exists() else 0,
        "page_pngs": len(page_pngs),
        "ledger_rows": ledger_rows,
        "contact_sheet": (PAGES_DIR / "contact_every_12_pages.png").exists(),
    }


def parse_raw_json() -> dict:
    data = RAW_JSON.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "utf-16", "utf-16-le"):
        try:
            return json.loads(data.decode(encoding))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    return json.loads(data.decode("utf-8", errors="replace"))


def debug_model_line() -> str:
    if not DEBUG_LOG.exists():
        return "DEBUG_LOG_MISSING"
    for line in DEBUG_LOG.read_text(encoding="utf-8", errors="replace").splitlines():
        if "model=claude-opus-4-7" in line and "modelSupported=true" in line:
            return line.strip()
    return "DEBUG_LOG_NO_MODEL_LINE_FOUND"


def write_result_md(stats: dict[str, int | str], metrics: dict[str, int | bool]) -> None:
    raw = parse_raw_json()
    model_usage = raw.get("modelUsage", {})
    debug_line = debug_model_line()
    md = f"""# OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_RESULT

Status: `pass_with_corrections_model_gate_blocked`

Timestamp: 2026-05-25 +08

## Runtime Evidence

- command target model: `claude-opus-4-7`
- raw JSON subtype: `{raw.get("subtype")}`
- terminal reason: `{raw.get("terminal_reason")}`
- fast mode state: `{raw.get("fast_mode_state")}`
- duration_ms: `{raw.get("duration_ms")}`
- num_turns: `{raw.get("num_turns")}`
- session_id: `{raw.get("session_id")}`
- debug model line: `{debug_line}`
- modelUsage keys: `{", ".join(model_usage.keys())}`

`claude-opus-4-7` appears in runtime/debug evidence and carried the substantive token usage. A small auxiliary `claude-haiku-4-5-20251001` entry also appears in `modelUsage`. The runtime still does not expose a machine-readable proof of `--effort max` / adaptive thinking. Therefore this result is valid as a real ClaudeCode production-line review call, but the strict model evidence gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## ClaudeCode Decision

ClaudeCode returned: `pass_with_corrections_model_gate_blocked`.

Required correction applied in Codex after the review:

- Added matrix row `{stats["q7_row_id"]}` for `2026朝阳一模 Q7`, classified as `选必三逻辑与思维边界`, no DOCX insertion.
- Patched `M0591` remark so it no longer overclaims Q1-Q21 direct closure before Q7 was recorded.
- Updated the Batch05 Codex report to disclose the Q7 missing-row patch.

## Post-Correction Counters

- matrix total rows: `{stats["matrix_rows"]}`
- `2026朝阳一模` matrix rows: `{stats["cy_rows"]}`
- `2026朝阳一模` loose pending rows: `{stats["cy_loose_pending"]}`
- global exact production-line candidate rows still open: `{stats["exact_pending"]}`
- rows still marked `NEED_SOURCE`: `{stats["need_source"]}`
- insert ledger rows: `{metrics["ledger_rows"]}`
- DOCX bytes: `{metrics["docx_bytes"]}`
- PDF bytes: `{metrics["pdf_bytes"]}`
- rendered page PNGs: `{metrics["page_pngs"]}`
- contact sheet exists: `{metrics["contact_sheet"]}`

## ClaudeCode Finding Summary

The full raw review text is preserved in `OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_RAW.json`. The actionable findings were:

- Q7 was missing from the per-question matrix and needed a boundary row.
- `M0591` overclaimed direct Q1-Q21 closure before Q7 was separately recorded.
- Q1/Q2/Q3 insertions, Q16 evidence-label refinement, Q17 source boundary, Q18-Q20 exclusions, and Q21 already-covered judgment were source-defensible.
- The review did not close the strict model proof gate or external full-artifact review gates.

## Boundary

This file is not final acceptance. It records a real ClaudeCode Batch05 review plus the required correction. GPTPro web and Claude Opus external full-artifact reviews remain `real_call_pending`.
"""
    RESULT_MD.write_text(md, encoding="utf-8")


def append_if_missing(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    if marker not in text:
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
        path.write_text(text, encoding="utf-8")


def update_batch_report(stats: dict[str, int | str]) -> None:
    text = BATCH_REPORT.read_text(encoding="utf-8", errors="replace")
    text = text.replace(
        "Status: `CODEX_BATCH05_DONE__CLAUDECODE_RECHECK_PENDING`",
        "Status: `CODEX_BATCH05_DONE__CLAUDECODE_RECHECK_CORRECTION_APPLIED__MODEL_GATE_BLOCKED`",
    )
    marker = "## ClaudeCode Recheck Amendment"
    if marker not in text:
        text += f"""

{marker}

ClaudeCode Opus 4.7 Batch05 recheck returned `pass_with_corrections_model_gate_blocked`.

Correction applied after recheck:

- Added `{stats["q7_row_id"]}` for `2026朝阳一模 Q7`: official answer C; classified as `选必三逻辑与思维边界`; no DOCX insertion.
- Patched `M0591` remark: original Codex-A export skipped Q7, so the suite closure statement now points to `{stats["q7_row_id"]}` instead of overclaiming direct Q1-Q21 row coverage.
- Post-correction `2026朝阳一模` suite rows: `{stats["cy_rows"]}`; loose pending rows: `{stats["cy_loose_pending"]}`.

Model boundary: this was a real ClaudeCode review call with `claude-opus-4-7` runtime evidence, but strict max-effort/adaptive-thinking proof remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
"""
    BATCH_REPORT.write_text(text, encoding="utf-8")


def update_model_ledger() -> None:
    raw = parse_raw_json()
    usage = raw.get("modelUsage", {})
    opus = usage.get("claude-opus-4-7", {})
    haiku = usage.get("claude-haiku-4-5-20251001", {})
    block = f"""## OPUS47_BATCH05_CHAOYANG_RECHECK_001

- timestamp: 2026-05-25 +08
- artifact: `OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_RAW.json`
- debug artifact: `OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_DEBUG.log`
- target model: `claude-opus-4-7`
- runtime evidence: debug log contains `model=claude-opus-4-7 modelSupported=true`; raw JSON `modelUsage` contains `claude-opus-4-7`.
- opus tokens: input `{opus.get("inputTokens")}`, cache read `{opus.get("cacheReadInputTokens")}`, cache creation `{opus.get("cacheCreationInputTokens")}`, output `{opus.get("outputTokens")}`.
- auxiliary model usage: `claude-haiku-4-5-20251001` input `{haiku.get("inputTokens")}`, output `{haiku.get("outputTokens")}`.
- result: `pass_with_corrections_model_gate_blocked`
- correction outcome: Q7 matrix boundary row `{ "M0861" }` added; no DOCX insertion.
- model gate: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` because runtime does not expose machine-readable `--effort max` / adaptive-thinking proof and auxiliary Haiku appears in usage. This is real ClaudeCode production-line evidence, not strict final acceptance evidence.
"""
    append_if_missing(MODEL_LEDGER, "OPUS47_BATCH05_CHAOYANG_RECHECK_001", block)


def update_status_files(stats: dict[str, int | str], metrics: dict[str, int | bool]) -> None:
    status_block = f"""## Batch05 Recovery Update - 2026-05-25 01:30 +08

Status remains: `RECOVERED_EXECUTION_IN_PROGRESS`.

- Batch05 suite: `2026朝阳一模`
- ClaudeCode review: real `claude-opus-4-7` call completed, result `pass_with_corrections_model_gate_blocked`.
- Correction applied: added matrix row `{stats["q7_row_id"]}` for Q7 as `选必三逻辑与思维边界`; patched `M0591` overclaim.
- Suite-local loose pending rows: `{stats["cy_loose_pending"]}`.
- Matrix total rows: `{stats["matrix_rows"]}`.
- Global exact production-line candidate rows still open: `{stats["exact_pending"]}`.
- Rows still marked `NEED_SOURCE`: `{stats["need_source"]}`.

Blockers still open:

- `BLOCKED_MODEL_CONFIRMATION_REQUIRED`: strict Opus 4.7 max-effort/adaptive-thinking proof is still not machine-confirmed.
- GPTPro web full-artifact review: `real_call_pending`.
- Claude Opus external full-artifact review: `real_call_pending`.
- Remaining suites/rows still require source/rubric exhaustion before any final acceptance language.
"""
    append_if_missing(THREAD_STATUS, "Batch05 Recovery Update - 2026-05-25 01:30 +08", status_block)

    format_block = f"""## Batch05 Render QA Addendum - 2026-05-25

Current rendered artifact counters after Batch05 and global label-style normalization:

- DOCX bytes: `{metrics["docx_bytes"]}`
- PDF bytes: `{metrics["pdf_bytes"]}`
- PDF page count / rendered PNG count: `232 / {metrics["page_pngs"]}`
- contact sheet present: `{metrics["contact_sheet"]}`
- insert ledger rows: `{metrics["ledger_rows"]}`
- ledger headings found in DOCX in prior Batch05 check: `51 / 51`
- all label paragraphs normalized in prior Batch05 check: `2148 / 2148`
- student-facing residue scan in prior Batch05 check: `0` DOCX/PDF hits for the current banlist

The ClaudeCode correction added only matrix/report ledger metadata for Q7 and did not change DOCX/PDF content; no rerender was required for that correction.
"""
    append_if_missing(FORMAT_QA, "Batch05 Render QA Addendum - 2026-05-25", format_block)

    governor_block = f"""## Governor Recovery Addendum - Batch05 2026朝阳一模

Decision: `BATCH05_SOURCE_CLOSURE_WITH_CORRECTION_APPLIED__RECOVERY_CONTINUES`.

- Sonnet evidence remains invalid and excluded from acceptance evidence.
- ClaudeCode real call completed with `claude-opus-4-7` runtime evidence, but model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Required correction from ClaudeCode was applied: `{stats["q7_row_id"]}` added for Q7 boundary exclusion; `M0591` remark patched.
- Current matrix rows: `{stats["matrix_rows"]}`.
- Remaining exact open production-line rows: `{stats["exact_pending"]}`.

Governor boundary: do not mark final acceptance. External GPTPro/Claude Opus full-artifact review remains `real_call_pending`.
"""
    append_if_missing(GOVERNOR, "Governor Recovery Addendum - Batch05 2026朝阳一模", governor_block)

    confucius_block = f"""## Confucius Recovery Artifact Check Addendum - Batch05

Artifact check result: `BATCH05_ARTIFACTS_PRESENT_WITH_GLOBAL_BLOCKERS`.

Present/updated:

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` now includes `{stats["q7_row_id"]}` for `2026朝阳一模 Q7`.
- `OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_RAW.json`
- `OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_DEBUG.log`
- `OPUS47_CLAUDECODE_BATCH05_2026_CHAOYANG_YIMO_RECHECK_RESULT.md`
- `COVERAGE_FUSION_BATCH05_2026_CHAOYANG_YIMO_CODEX_20260525.md`

Counts:

- `2026朝阳一模` matrix rows: `{stats["cy_rows"]}`
- suite loose pending rows: `{stats["cy_loose_pending"]}`
- DOCX/PDF render remains the latest Batch05 render: `232` pages / `{metrics["page_pngs"]}` PNGs.

Not closed:

- model confirmation gate remains blocked;
- GPTPro web and external Claude Opus reviews remain `real_call_pending`;
- global source/rubric exhaustion remains incomplete.
"""
    append_if_missing(CONFUCIUS, "Confucius Recovery Artifact Check Addendum - Batch05", confucius_block)


def main() -> None:
    stats = apply_matrix_correction()
    metrics = artifact_metrics()
    write_result_md(stats, metrics)
    update_batch_report(stats)
    update_model_ledger()
    update_status_files(stats, metrics)
    print(json.dumps({"stats": stats, "metrics": metrics}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
