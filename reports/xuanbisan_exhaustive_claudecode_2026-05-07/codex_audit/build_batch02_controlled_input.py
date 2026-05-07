# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import shutil
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
SRC_BATCH = RUN_DIR / "claudecode_lane" / "batches" / "batch02_chaoyang"
REPAIRED_QD = RUN_DIR / "codex_audit" / "repaired_csv" / "batch02_chaoyang_QUESTION_DECISIONS.csv"
OUT = RUN_DIR / "fusion" / "batch02_chaoyang_controlled_input"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def copy_file(name: str) -> None:
    shutil.copy2(SRC_BATCH / name, OUT / name)


def build_entries(main_rows: list[dict[str, str]], choice_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for row in main_rows:
        entries.append(
            {
                "question_id": row.get("question_id", ""),
                "type": "subjective",
                "framework_node": row.get("框架落点", ""),
                "material_signal": row.get("材料动作", ""),
                "trigger_logic": row.get("触发逻辑", ""),
                "answer_sentence": row.get("答案句", ""),
                "evidence_level": row.get("证据等级", ""),
                "needs_codex_recheck": "no",
                "source_batch": "batch02_chaoyang_controlled_input",
            }
        )
    for row in choice_rows:
        needs = row.get("needs_codex_recheck", "").strip() or "no"
        if needs not in {"yes", "no"}:
            needs = "yes"
        entries.append(
            {
                "question_id": row.get("question_id", ""),
                "type": "choice",
                "framework_node": row.get("陷阱类型", ""),
                "material_signal": row.get("题干信号", ""),
                "trigger_logic": row.get("正确项理由", ""),
                "answer_sentence": f"正确项理由：{row.get('正确项理由', '')}；排错要点：{row.get('诱人错项', '')}",
                "evidence_level": "B-choice-signal" if row.get("是否可入学生稿", "") == "可" else "blocked",
                "needs_codex_recheck": needs,
                "source_batch": "batch02_chaoyang_controlled_input",
            }
        )
    return entries


def write_jsonl(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_boundary(qd_rows: list[dict[str, str]]) -> None:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in qd_rows:
        if row["claudecode_decision"] != "入正文":
            grouped[row["claudecode_decision"]].append(row)
    lines = [
        "# Batch02 朝阳受控输入 - 边界与阻断",
        "",
        "本文件由 Codex 从 ClaudeCode Batch02 的修复后判定表机械生成，用于融合输入控制；不作为学生正文。",
        "",
    ]
    for label in ["同类索引", "blocked", "excluded"]:
        rows = grouped.get(label, [])
        lines.extend([f"## {label}", ""])
        if not rows:
            lines.append("- none")
        else:
            for row in rows:
                lines.append(f"- `{row['question_id']}` ({row['suite_id']} {row['original_qno']}): {row['decision_reason']}")
        lines.append("")
    (OUT / "BLOCKED_OR_BOUNDARY.md").write_text("\n".join(lines), encoding="utf-8")


def write_suite_reports(qd_rows: list[dict[str, str]]) -> None:
    suite_dir = OUT / "suite_reports"
    suite_dir.mkdir(parents=True, exist_ok=True)
    suites: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in qd_rows:
        suites[row["suite_id"]].append(row)
    for suite, rows in sorted(suites.items()):
        counts = Counter(row["claudecode_decision"] for row in rows)
        lines = [
            f"# {suite} 受控闭合报告",
            "",
            "本报告由 Codex 从 ClaudeCode Batch02 输出与修复后判定表生成，用于融合前控制审计；不授权终稿。",
            "",
            "## 统计",
            "",
        ]
        for label in ["入正文", "同类索引", "blocked", "excluded"]:
            lines.append(f"- {label}: {counts.get(label, 0)}")
        lines.extend(["", "## 入正文/同类索引/blocked 题", ""])
        for row in rows:
            if row["claudecode_decision"] in {"入正文", "同类索引", "blocked"}:
                lines.append(f"- `{row['question_id']}`: `{row['claudecode_decision']}` - {row['decision_reason']}")
        lines.extend(["", "## 说明", "", "- 选择题、主观题厚内容仍以本目录 ledgers 与 entries 为准；所有内容进入学生稿前需 Codex 再做框架归位和禁用话术过滤。"])
        (suite_dir / f"{suite}.md").write_text("\n".join(lines), encoding="utf-8")


def write_acceptance(qd_rows: list[dict[str, str]], entries: list[dict[str, str]]) -> None:
    counts = Counter(row["claudecode_decision"] for row in qd_rows)
    type_counts = Counter(row["type"] for row in entries)
    lines = [
        "# Batch02 朝阳受控融合输入验收说明",
        "",
        "结论：本目录是 Codex 受控融合输入，不是终稿，不授权 Word/PDF。",
        "",
        "## 来源",
        "",
        "- `QUESTION_DECISIONS.csv`: 来自 Codex 对 ClaudeCode Batch02 破损 CSV 的机械转义修复。",
        "- 厚内容 ledgers: 来自 ClaudeCode Batch02 原始厚内容输出。",
        "- `entries/batch02_entries.jsonl`: 由 Codex 从厚内容 ledgers 机械打包。",
        "",
        "## 统计",
        "",
        f"- 判定表数据行：{len(qd_rows)}",
        f"- 入正文：{counts.get('入正文', 0)}",
        f"- 同类索引：{counts.get('同类索引', 0)}",
        f"- blocked：{counts.get('blocked', 0)}",
        f"- excluded：{counts.get('excluded', 0)}",
        f"- entries：{len(entries)}（{dict(type_counts)}）",
        "",
        "## 限制",
        "",
        "- 原 ClaudeCode Batch02 的 `QUESTION_DECISIONS.csv` 仍保留为破损原件，本目录只作为融合可读版本。",
        "- 因 Batch02 原件仍缺正式 entries 和 suite reports，后续融合必须引用本目录并保留来源说明。",
        "- 学生正文必须从 ledgers/entries 再做框架化改写，不能直接复制审计文档。",
    ]
    (OUT / "BATCH02_CONTROLLED_INPUT_ACCEPTANCE.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    qd_rows = read_csv(REPAIRED_QD)
    write_csv(OUT / "QUESTION_DECISIONS.csv", qd_rows, list(qd_rows[0].keys()))
    for name in [
        "MAIN_THINKING_LEDGER.csv",
        "CHOICE_TRAP_LEDGER.csv",
        "FRAMEWORK_NODE_MATRIX.csv",
        "FRAMEWORK_NODE_MATRIX_SUMMARY.csv",
    ]:
        copy_file(name)
    main_rows = read_csv(OUT / "MAIN_THINKING_LEDGER.csv")
    choice_rows = read_csv(OUT / "CHOICE_TRAP_LEDGER.csv")
    entries = build_entries(main_rows, choice_rows)
    write_jsonl(OUT / "entries" / "batch02_entries.jsonl", entries)
    write_boundary(qd_rows)
    write_suite_reports(qd_rows)
    write_acceptance(qd_rows, entries)
    print(json.dumps({"out": str(OUT), "decision_rows": len(qd_rows), "entries": len(entries)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
