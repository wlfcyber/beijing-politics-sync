# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07")
CODEX = RUN_DIR / "codex_lane"
CLAUDE = RUN_DIR / "claudecode_lane"
AUDIT = RUN_DIR / "codex_audit"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    codex = read_csv(CODEX / "QUESTION_COVERAGE_MATRIX.csv")
    claude = read_csv(CLAUDE / "QUESTION_COVERAGE_MATRIX.csv")
    codex_qids = {r.get("question_id", "") for r in codex if r.get("question_id", "")}
    claude_qids = {r.get("question_id", "") for r in claude if r.get("question_id", "")}

    conclusion_counts = Counter(r.get("本轮结论", "") for r in claude)
    invalid_conclusion_pending = [r for r in claude if "pending" in r.get("本轮结论", "").lower()]
    evidence_pending = [r for r in claude if "pending" in r.get("evidence_level", "").lower()]
    missing_qids = sorted(codex_qids - claude_qids)
    extra_qids = sorted(claude_qids - codex_qids)

    report_files = sorted((CLAUDE / "suite_reports").glob("*.md")) if (CLAUDE / "suite_reports").exists() else []
    expected_suites = sorted({r.get("suite_id", "") for r in codex if r.get("suite_id", "")})
    report_stems = {p.stem for p in report_files}
    missing_suite_reports = []
    for suite in expected_suites:
        visible = suite.replace("S-", "")
        if visible not in report_stems and suite not in report_stems:
            missing_suite_reports.append(suite)

    entry_counts = {}
    if (CLAUDE / "entries").exists():
        for p in sorted((CLAUDE / "entries").glob("*.jsonl")):
            entry_counts[p.name] = sum(1 for _ in p.open("r", encoding="utf-8", errors="ignore"))

    terminal_labels = {"入正文", "同类索引", "blocked", "excluded"}
    terminal_ok = all((r.get("本轮结论", "") in terminal_labels) for r in claude) and not missing_qids
    verdict = "CONTROL_BASE_TERMINAL_CLOSED_BUT_EVIDENCE_BLOCKED" if terminal_ok else "HARD_FAIL_NOT_CLOSED_YET"

    summary = {
        "verdict": verdict,
        "codex_union_rows": len(codex),
        "claudecode_coverage_rows": len(claude),
        "claudecode_conclusion_counts": dict(conclusion_counts),
        "claudecode_pending_conclusion_rows": len(invalid_conclusion_pending),
        "claudecode_evidence_pending_rows": len(evidence_pending),
        "missing_qids_from_codex_union": missing_qids,
        "extra_qids_not_in_codex_union": extra_qids,
        "suite_report_files": len(report_files),
        "missing_suite_reports": missing_suite_reports,
        "entry_jsonl_counts": entry_counts,
    }
    (AUDIT / "claudecode_output_qa_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# ClaudeCode 输出 QA",
        "",
        f"Verdict: `{verdict}`",
        "",
        "## 关键问题",
        "",
        f"- Codex union coverage rows: {len(codex)}",
        f"- ClaudeCode coverage rows: {len(claude)}",
        f"- ClaudeCode pending conclusion rows: {len(invalid_conclusion_pending)}",
        f"- ClaudeCode evidence pending rows: {len(evidence_pending)}",
        f"- Missing qids from Codex union: {len(missing_qids)}",
        f"- Suite reports: {len(report_files)} / expected {len(expected_suites)}",
        "",
        "## ClaudeCode 本轮结论分布",
        "",
    ]
    for k, v in conclusion_counts.most_common():
        lines.append(f"- `{k}`: {v}")
    lines.extend(["", "## 缺失 qids", ""])
    if missing_qids:
        for qid in missing_qids:
            lines.append(f"- `{qid}`")
    else:
        lines.append("- none")
    lines.extend(["", "## 缺失 suite_reports", ""])
    if missing_suite_reports:
        for suite in missing_suite_reports:
            lines.append(f"- `{suite}`")
    else:
        lines.append("- none")
    lines.extend([
        "",
        "## 处理意见",
        "",
        "- 若 verdict 仍为 HARD_FAIL，不允许 ClaudeCode 根任务宣称穷尽完成。",
        "- 若 verdict 为 CONTROL_BASE_TERMINAL_CLOSED_BUT_EVIDENCE_BLOCKED，只表示 coverage 四类终态闭合；仍不授权终稿或 Word/PDF。",
        "- evidence_level=pending 的 blocked 行必须保留 blocker，表示缺题面/选项/答案/细则/视觉核读；不得误写为入正文。",
        "- Batch01 还必须补齐厚内容 ledgers、entries、blocked/boundary 文档，不能只交 QUESTION_DECISIONS。",
    ])
    (AUDIT / "claudecode_output_qa.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
