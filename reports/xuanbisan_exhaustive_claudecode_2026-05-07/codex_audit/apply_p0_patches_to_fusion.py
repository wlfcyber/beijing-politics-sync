# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
FUSION = RUN / "fusion" / "framework_first_fusion"
P0 = RUN / "claudecode_lane" / "p0_recheck"

SOURCE_DRAFT = FUSION / "FRAMEWORK_FIRST_FUSION_DRAFT.md"
PATCHED_DRAFT = FUSION / "FRAMEWORK_FIRST_FUSION_P0_PATCHED.md"
PATCH_REPORT = FUSION / "P0_FUSION_PATCH_REPORT.md"
PATCH_QA = FUSION / "P0_FUSION_PATCH_QA.json"


def load_decisions() -> dict[tuple[str, str], dict[str, str]]:
    with (P0 / "P0_RECHECK_DECISIONS.csv").open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return {(row["question_id"], row["framework_node"]): row for row in rows}


def load_patches() -> list[dict[str, str]]:
    rows = [json.loads(line) for line in (P0 / "P0_RECHECK_PATCHES.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    decisions = load_decisions()
    for row in rows:
        row["_decision_row"] = decisions[(row["question_id"], row["framework_node"])]
        row["_source_label"] = source_label(row["_decision_row"])
    return rows


def source_label(decision: dict[str, str]) -> str:
    qid = decision["question_id"]
    parent_qid = decision["parent_question_id"]
    if qid.startswith("Q-2024朝阳二模"):
        return qid
    raw = parent_qid.removeprefix("Q-")
    parts = raw.split("-")
    suite = "-".join(parts[:-1])
    q = parts[-1]
    if len(parts) >= 3 and parts[-2].isdigit() and parts[-1].isdigit():
        suite = "-".join(parts[:-2])
        q = f"{parts[-2]}({parts[-1]})"
    return f"S-{suite} Q{q}"


def replacement_block(patch: dict[str, str]) -> list[str]:
    decision = patch["_decision_row"]
    label = patch["_source_label"]
    return [
        f"**{label}**（{decision['type']}；{decision['evidence_level']}；P0复核已闭合）",
        "",
        f"- 材料怎么看：{patch['patched_material_signal']}",
        f"- 为什么想到：{patch['patched_trigger_logic']}",
        f"- 卷面句：{patch['patched_answer_sentence']}",
        f"- P0证据：{patch['source_evidence']}",
        "",
    ]


def apply_patches() -> dict:
    patches = load_patches()
    by_node_label = {(p["framework_node"], p["_source_label"]): p for p in patches}
    text_lines = SOURCE_DRAFT.read_text(encoding="utf-8", errors="replace").splitlines()

    out: list[str] = []
    current_node = ""
    applied: list[tuple[str, str]] = []
    skipped_source_blocks = 0
    i = 0
    while i < len(text_lines):
        line = text_lines[i]
        if line.startswith("### "):
            current_node = line[4:].strip()
            out.append(line)
            i += 1
            continue
        if line.startswith("**"):
            source = line.split("**", 2)[1]
            key = (current_node, source)
            patch = by_node_label.get(key)
            if patch:
                out.extend(replacement_block(patch))
                applied.append(key)
                i += 1
                # Skip the existing source block until next source or heading.
                while i < len(text_lines):
                    nxt = text_lines[i]
                    if nxt.startswith("**") or nxt.startswith("### ") or nxt.startswith("## "):
                        break
                    i += 1
                continue
            skipped_source_blocks += 1
        out.append(line)
        i += 1

    PATCHED_DRAFT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    applied_set = set(applied)
    missing = [key for key in by_node_label if key not in applied_set]
    p0_recheck_left = []
    patched_text = PATCHED_DRAFT.read_text(encoding="utf-8", errors="replace")
    patched_lines = patched_text.splitlines()
    for node, source in applied:
        needle = f"**{source}**"
        matching_lines = [line for line in patched_lines if line.startswith(needle)]
        if any("需 Codex 回源复核" in line for line in matching_lines):
            p0_recheck_left.append({"node": node, "source": source})

    qa = {
        "verdict": "P0_FUSION_PATCH_OK_NOT_FINAL" if not missing and not p0_recheck_left and "固定分析流程" not in patched_text else "P0_FUSION_PATCH_FAIL",
        "p0_patch_rows": len(patches),
        "applied_rows": len(applied),
        "missing_rows": len(missing),
        "missing": [{"framework_node": k[0], "source": k[1]} for k in missing],
        "p0_recheck_left": p0_recheck_left,
        "forbidden_fixed_flow_hits": patched_text.count("固定分析流程"),
        "evidence_counts": dict(Counter(p["_decision_row"]["evidence_level"] for p in patches)),
        "decision_counts": dict(Counter(p["_decision_row"]["decision"] for p in patches)),
        "output": str(PATCHED_DRAFT),
    }
    PATCH_QA.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    report = [
        "# P0 Fusion Patch Report",
        "",
        f"Verdict: `{qa['verdict']}`",
        "",
        f"- P0 patch rows: `{qa['p0_patch_rows']}`",
        f"- applied rows: `{qa['applied_rows']}`",
        f"- missing rows: `{qa['missing_rows']}`",
        f"- decision counts: `{qa['decision_counts']}`",
        f"- evidence counts: `{qa['evidence_counts']}`",
        f"- output: `{PATCHED_DRAFT}`",
        "",
        "## Boundary",
        "",
        "- This is a fusion draft patch only.",
        "- It does not authorize Word/PDF/final delivery.",
    ]
    if missing:
        report.extend(["", "## Missing", ""])
        for node, source in missing:
            report.append(f"- `{source}` under `{node}`")
    PATCH_REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps(qa, ensure_ascii=False, indent=2))
    return qa


if __name__ == "__main__":
    apply_patches()
