#!/usr/bin/env python3
"""Run the full gate matrix for an automated Chinese research-paper workflow."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
RUN_AUDIT = SCRIPT_DIR / "run_audit.py"
WORKFLOW_REPORT = SCRIPT_DIR / "workflow_report.py"
QUALITY_GATE_AUDIT = SCRIPT_DIR / "quality_gate_audit.py"
TOPIC_ENGINE_AUDIT = SCRIPT_DIR / "topic_engine_audit.py"
SOURCE_FILE_AUDIT = SCRIPT_DIR / "source_file_audit.py"


@dataclass
class Gate:
    key: str
    label: str
    command: list[str]
    required_for: str


def run_command(command: list[str], cwd: Path) -> tuple[int, str]:
    completed = subprocess.run(
        command,
        cwd=str(cwd),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return completed.returncode, completed.stdout.strip()


def parse_status_line(output: str) -> str:
    for line in output.splitlines():
        if line.startswith("status="):
            return line.removeprefix("status=").strip()
    for line in output.splitlines():
        if line.startswith("formal_ready="):
            return "PASS" if line.endswith("yes") else "INCOMPLETE"
    return "UNKNOWN"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir")
    parser.add_argument("--min-fulltext", type=int, default=8)
    parser.add_argument(
        "--source-search-root",
        action="append",
        default=[],
        help="Extra directory to search for migrated source PDFs/text files. Can be repeated.",
    )
    parser.add_argument("--out", help="Markdown output path. Defaults to <run_dir>/16_总闸口矩阵.md")
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    out = Path(args.out).expanduser().resolve() if args.out else run_dir / "16_总闸口矩阵.md"
    py = sys.executable
    inferred_source_roots = [run_dir.parent]
    if run_dir.parent.name == "runs":
        inferred_source_roots.append(run_dir.parent.parent)
    source_search_args: list[str] = []
    for root in [*inferred_source_roots, *(Path(root).expanduser().resolve() for root in args.source_search_root)]:
        source_search_args.extend(["--search-root", str(root)])

    gates = [
        Gate(
            "topic_engine",
            "选题层：20-30 个候选、评分维度齐全、1 个主选和 3 个备选",
            [py, str(TOPIC_ENGINE_AUDIT), str(run_dir)],
            "topic_selection_ready",
        ),
        Gate(
            "material",
            "材料层：8 篇可读全文/证据、引用映射、页码候选",
            [py, str(RUN_AUDIT), str(run_dir), "--min-fulltext", str(args.min_fulltext)],
            "paper_material_ready",
        ),
        Gate(
            "source_files",
            "当前设备材料文件层：正式全文源文件与提取文本在本机可复验",
            [py, str(SOURCE_FILE_AUDIT), str(run_dir), "--min-current-fulltext", str(args.min_fulltext), *source_search_args],
            "paper_material_ready",
        ),
        Gate(
            "text_quality",
            "文本质量层：研究对象、方法-数据匹配、比较诚实、段落推进与结论边界",
            [
                py,
                str(QUALITY_GATE_AUDIT),
                str(run_dir),
                "--require-quality-plan",
                "--require-method-data-fit",
                "--require-comparison-table",
            ],
            "paper_text_quality",
        ),
        Gate(
            "source_provenance",
            "来源溯源层：正式全文来源有检索/获取/本地文件/hash台账",
            [py, str(RUN_AUDIT), str(run_dir), "--min-fulltext", str(args.min_fulltext), "--require-source-provenance"],
            "paper_material_ready",
        ),
        Gate(
            "policy",
            "政策来源：官方政策已进入正式稿",
            [py, str(RUN_AUDIT), str(run_dir), "--min-fulltext", str(args.min_fulltext), "--require-policy-citation-merged"],
            "formal_submission",
        ),
        Gate(
            "page_numbers",
            "页码层：参考文献页码/正文脚注页码无占位",
            [py, str(RUN_AUDIT), str(run_dir), "--min-fulltext", str(args.min_fulltext), "--require-page-numbers"],
            "formal_submission",
        ),
        Gate(
            "primary_fulltext",
            "原刊层：正式来源均为 PDF/数据库/用户导出全文",
            [py, str(RUN_AUDIT), str(run_dir), "--min-fulltext", str(args.min_fulltext), "--require-primary-fulltext"],
            "formal_submission",
        ),
        Gate(
            "source_id_freeze",
            "Source ID freeze: S/C source numbers have no silent reuse",
            [py, str(RUN_AUDIT), str(run_dir), "--min-fulltext", str(args.min_fulltext), "--require-source-id-freeze"],
            "workflow_integrity",
        ),
        Gate(
            "browser_hands_free",
            "浏览器层：人大代理/CNKI 检索下载 hands-free 可控",
            [py, str(RUN_AUDIT), str(run_dir), "--min-fulltext", str(args.min_fulltext), "--require-browser-gate"],
            "hands_free_workflow",
        ),
        Gate(
            "external_review",
            "外部评审层：Claude Opus 与 GPT Pro/GPT-5.5 Pro 均真实通过",
            [py, str(RUN_AUDIT), str(run_dir), "--min-fulltext", str(args.min_fulltext), "--require-external-review"],
            "final_user_goal",
        ),
    ]

    report_code, report_output = run_command([py, str(WORKFLOW_REPORT), str(run_dir), "--target-fulltext", str(args.min_fulltext)], run_dir)

    rows: list[tuple[Gate, int, str, str]] = []
    for gate in gates:
        code, output = run_command(gate.command, run_dir)
        rows.append((gate, code, parse_status_line(output), output))

    all_passed = all(code == 0 for _, code, _, _ in rows)
    topic_passed = next((code == 0 for gate, code, _, _ in rows if gate.key == "topic_engine"), False)
    material_passed = next((code == 0 for gate, code, _, _ in rows if gate.key == "material"), False)

    lines = [
        "# 自动科研流总闸口矩阵",
        "",
        "## 总结",
        "",
        f"- topic_selection_ready: {'yes' if topic_passed else 'no'}",
        f"- paper_material_ready: {'yes' if material_passed else 'no'}",
        f"- final_user_goal_ready: {'yes' if all_passed else 'no'}",
        f"- workflow_report_exit_code: {report_code}",
        "",
        "## Gate Matrix",
        "",
        "| Gate | 适用层级 | 状态 | 关键输出 |",
        "| --- | --- | --- | --- |",
    ]

    for gate, code, status, output in rows:
        issues = [line.removeprefix("- ").strip() for line in output.splitlines() if line.startswith("- ")]
        key_output = "<br>".join(issues) if issues else status
        lines.append(f"| {gate.label} | {gate.required_for} | {'PASS' if code == 0 else 'INCOMPLETE'} | {key_output} |")

    lines.extend(["", "## Raw Gate Outputs", ""])
    for gate, code, status, output in rows:
        lines.extend(
            [
                f"### {gate.key}",
                "",
                f"- exit_code: {code}",
                f"- parsed_status: {status}",
                "",
                "```text",
                output,
                "```",
                "",
            ]
        )

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"paper_material_ready={'yes' if material_passed else 'no'}")
    print(f"final_user_goal_ready={'yes' if all_passed else 'no'}")
    print(f"out={out}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
