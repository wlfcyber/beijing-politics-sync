# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
FUSION = RUN / "fusion" / "framework_first_fusion"
FORBIDDEN = ["固定分析流程", "FINAL_PASS", "终稿已通过", "最终版"]


def input_output(priority: str) -> tuple[Path, Path, Path, Path, Path]:
    lane = RUN / "claudecode_lane" / f"{priority.lower()}_recheck"
    if priority == "P0":
        source = FUSION / "FRAMEWORK_FIRST_FUSION_DRAFT.md"
    elif priority == "P1":
        source = FUSION / "FRAMEWORK_FIRST_FUSION_P0_PATCHED.md"
    else:
        prev = f"P{int(priority[1:]) - 1}"
        source = FUSION / f"FRAMEWORK_FIRST_FUSION_{prev}_PATCHED.md"
    output = FUSION / f"FRAMEWORK_FIRST_FUSION_{priority}_PATCHED.md"
    report = FUSION / f"{priority}_FUSION_PATCH_REPORT.md"
    qa = FUSION / f"{priority}_FUSION_PATCH_QA.json"
    return lane, source, output, report, qa


def load_decisions(lane: Path, priority: str) -> dict[tuple[str, str], dict[str, str]]:
    with (lane / f"{priority}_RECHECK_DECISIONS.csv").open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return {(row["question_id"], row["framework_node"]): row for row in rows}


def source_label(decision: dict[str, str]) -> str:
    qid = decision["question_id"]
    parent_qid = decision["parent_question_id"]
    if qid.startswith("Q-2024朝阳期中-18-"):
        return qid
    raw = parent_qid.removeprefix("Q-")
    parts = raw.split("-")
    if len(parts) >= 3 and parts[-2].isdigit() and parts[-1].isdigit():
        suite = "-".join(parts[:-2])
        q = f"{parts[-2]}({parts[-1]})"
    else:
        suite = "-".join(parts[:-1])
        q = parts[-1]
    return f"S-{suite} Q{q}"


def load_patches(lane: Path, priority: str) -> list[dict[str, str]]:
    decisions = load_decisions(lane, priority)
    rows = [
        json.loads(line)
        for line in (lane / f"{priority}_RECHECK_PATCHES.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    for row in rows:
        decision = decisions[(row["question_id"], row["framework_node"])]
        row["_decision_row"] = decision
        row["_source_label"] = source_label(decision)
        row["_aliases"] = list(
            dict.fromkeys(
                [
                    row["_source_label"],
                    row["question_id"],
                    row["parent_question_id"],
                ]
            )
        )
        row["_patch_id"] = f"{row['question_id']}||{row['framework_node']}"
    return rows


def replacement_block(patch: dict[str, str], priority: str, label_override: str | None = None) -> list[str]:
    decision = patch["_decision_row"]
    label = label_override or patch["_source_label"]
    close_note = f"{priority}复核已闭合"
    if decision["decision"] == "downgrade_to_index":
        close_note = f"{priority}复核已闭合；同类索引"
    return [
        f"**{label}**（{decision['type']}；{decision['evidence_level']}；{close_note}）",
        "",
        f"- 材料怎么看：{patch['patched_material_signal']}",
        f"- 为什么想到：{patch['patched_trigger_logic']}",
        f"- 卷面句：{patch['patched_answer_sentence']}",
        f"- {priority}证据：{patch['source_evidence']}",
        "",
    ]


def apply(priority: str) -> dict[str, object]:
    lane, source, output, report_path, qa_path = input_output(priority)
    patches = load_patches(lane, priority)
    by_node_label = {}
    for patch in patches:
        for alias in patch["_aliases"]:
            by_node_label[(patch["framework_node"], alias)] = patch
    text_lines = source.read_text(encoding="utf-8", errors="replace").splitlines()

    out: list[str] = []
    current_node = ""
    applied: list[tuple[str, str, str]] = []
    i = 0
    while i < len(text_lines):
        line = text_lines[i]
        if line.startswith("### "):
            current_node = line[4:].strip()
            out.append(line)
            i += 1
            continue
        if line.startswith("**"):
            source_name = line.split("**", 2)[1]
            patch = by_node_label.get((current_node, source_name))
            if patch:
                out.extend(replacement_block(patch, priority, source_name))
                applied.append((patch["_patch_id"], current_node, source_name))
                i += 1
                while i < len(text_lines):
                    nxt = text_lines[i]
                    if nxt.startswith("**") or nxt.startswith("### ") or nxt.startswith("## "):
                        break
                    i += 1
                continue
        out.append(line)
        i += 1

    output.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    patched_text = output.read_text(encoding="utf-8", errors="replace")
    patched_lines = patched_text.splitlines()
    applied_ids = {patch_id for patch_id, _node, _source_name in applied}
    missing = [patch for patch in patches if patch["_patch_id"] not in applied_ids]
    recheck_left = []
    for _patch_id, node, source_name in applied:
        needle = f"**{source_name}**"
        matching = [line for line in patched_lines if line.startswith(needle)]
        if any("需 Codex 回源复核" in line for line in matching):
            recheck_left.append({"node": node, "source": source_name})
    forbidden_hits = {token: patched_text.count(token) for token in FORBIDDEN}
    qa = {
        "verdict": f"{priority}_FUSION_PATCH_OK_NOT_FINAL"
        if not missing and not recheck_left and not any(forbidden_hits.values())
        else f"{priority}_FUSION_PATCH_FAIL",
        "priority": priority,
        "patch_rows": len(patches),
        "applied_rows": len(applied),
        "missing_rows": len(missing),
        "missing": [{"framework_node": patch["framework_node"], "source": patch["_source_label"]} for patch in missing],
        "recheck_left": recheck_left,
        "forbidden_hits": forbidden_hits,
        "evidence_counts": dict(Counter(p["_decision_row"]["evidence_level"] for p in patches)),
        "decision_counts": dict(Counter(p["_decision_row"]["decision"] for p in patches)),
        "source": str(source),
        "output": str(output),
    }
    qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# {priority} Fusion Patch Report",
        "",
        f"Verdict: `{qa['verdict']}`",
        "",
        f"- patch rows: `{qa['patch_rows']}`",
        f"- applied rows: `{qa['applied_rows']}`",
        f"- missing rows: `{qa['missing_rows']}`",
        f"- decision counts: `{qa['decision_counts']}`",
        f"- evidence counts: `{qa['evidence_counts']}`",
        f"- source: `{source}`",
        f"- output: `{output}`",
        "",
        "## Boundary",
        "",
        "- This is a fusion draft patch only.",
        "- It does not authorize Word/PDF/delivery.",
    ]
    if missing:
        lines.extend(["", "## Missing", ""])
        for patch in missing:
            lines.append(f"- `{patch['_source_label']}` under `{patch['framework_node']}`")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(qa, ensure_ascii=False, indent=2))
    return qa


def main() -> int:
    priority = (sys.argv[1] if len(sys.argv) > 1 else "P1").upper()
    apply(priority)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
