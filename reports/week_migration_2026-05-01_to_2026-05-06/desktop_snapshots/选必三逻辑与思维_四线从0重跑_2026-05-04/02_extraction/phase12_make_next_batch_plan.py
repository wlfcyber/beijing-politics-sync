#!/usr/bin/env python3
"""Create the next concrete Phase12 repair batch.

Batch01 is intentionally small enough to review: it prioritizes GPT's
highest-value repair clusters before broad choice-question form work.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "05_coverage/phase12_45_nonbody_repair_queue.csv"
MATRIX = ROOT / "05_coverage/phase12_74row_expansion_decision_matrix.csv"

PRIORITY_ORDER = [
    "P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER",
    "P4_RECHECK_SUBJECTIVE_REASONING_FORM",
    "P3_REPAIR_THINKING_OR_CROSS_SOURCE",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], headers: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def action_for(row: dict[str, str]) -> str:
    perm = row.get("phase07_input_permission", "")
    if "hold_reasoning_form_risk" in perm:
        return "补 logical_form、题型归属、有效式/错误式、规则口令、易错陷阱；通过后转正文"
    if "hold_answer_locator_risk" in perm:
        return "回源确认题干/选项/答案来源；不得猜答案；通过后转正文或保留 blocked"
    return "逐条回源裁决"


def body_target(row: dict[str, str]) -> str:
    if row.get("question_type") == "主观题":
        return "主观题正文条目：材料触发点/设问/为什么能想到/答案落点"
    if row.get("module") == "推理":
        return "推理题型正文条目：题型归属/逻辑形式/规则口令/解题动作/错项陷阱"
    return "选择题正文条目：题干信号/正确项理由/错项陷阱/同类题"


def main() -> None:
    queue = read_csv(QUEUE)
    matrix = {r["question_id"]: r for r in read_csv(MATRIX)}
    selected = [r for r in queue if r.get("priority") in PRIORITY_ORDER]
    selected.sort(key=lambda r: (PRIORITY_ORDER.index(r["priority"]), r["question_id"]))

    rows: list[dict[str, str]] = []
    for idx, r in enumerate(selected, 1):
        m = matrix.get(r["question_id"], {})
        rows.append(
            {
                "batch_order": str(idx),
                "priority": r.get("priority", ""),
                "question_id": r.get("question_id", ""),
                "visible_title": r.get("visible_title", ""),
                "module": r.get("module", ""),
                "question_type": r.get("question_type", ""),
                "phase10_body_status": r.get("phase10_body_status", ""),
                "permission": r.get("phase07_input_permission", ""),
                "phase12_decision": m.get("decision", ""),
                "source_locator": r.get("source_locator", ""),
                "answer_locator": r.get("answer_locator", ""),
                "risk_note": r.get("risk_note", ""),
                "required_action": action_for(r),
                "body_target": body_target(r),
                "current_status": "queued_not_repaired",
            }
        )

    headers = [
        "batch_order",
        "priority",
        "question_id",
        "visible_title",
        "module",
        "question_type",
        "phase10_body_status",
        "permission",
        "phase12_decision",
        "source_locator",
        "answer_locator",
        "risk_note",
        "required_action",
        "body_target",
        "current_status",
    ]
    write_csv(ROOT / "05_coverage/phase12_next_repair_batch01.csv", rows, headers)

    c_priority = Counter(r["priority"] for r in rows)
    c_type = Counter(r["question_type"] for r in rows)
    lines = [
        "# Phase12 Next Repair Batch01",
        "",
        "Status: `QUEUED_REVIEW_ONLY_NO_WORD_NO_FINAL`",
        "",
        "Batch purpose: process the highest-value non-body rows before broad 362-row rescan.",
        "",
        f"- rows: {len(rows)}",
        f"- priority counts: {dict(c_priority)}",
        f"- question type counts: {dict(c_type)}",
        "",
        "## Rows",
        "",
    ]
    for r in rows:
        lines.extend(
            [
                f"### {r['batch_order']}. {r['visible_title']} `{r['question_id']}`",
                "",
                f"- priority: `{r['priority']}`",
                f"- module/type: {r['module']} / {r['question_type']}",
                f"- required action: {r['required_action']}",
                f"- body target: {r['body_target']}",
                f"- source: {r['source_locator']}",
                f"- answer: {r['answer_locator']}",
                f"- risk note: {r['risk_note']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Gate",
            "",
            "No row in this batch is promoted by being queued. Promotion requires source repair/reasoning-form repair and a row-level review note.",
        ]
    )
    (ROOT / "05_coverage/phase12_next_repair_batch01.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    prompt = [
        "# ClaudeCode Visible Review Prompt: Phase12 Batch01",
        "",
        "Use a real visible ClaudeCode/Claude window only if available; otherwise keep this as pending.",
        "",
        "Task: audit Phase12 Batch01 repair readiness. Do not generate Word/PDF/final.",
        "",
        "Read:",
        "- `05_coverage/phase12_next_repair_batch01.csv`",
        "- `05_coverage/phase12_74row_expansion_decision_matrix.csv`",
        "- `00_飞哥选必三逻辑与思维硬性要求记事本.md`",
        "",
        "For each row, verify whether the source locator and answer locator are enough for正文 expansion. For reasoning rows, identify logical form, valid/invalid rule, student rule口诀, and wrong-option trap. Output a CSV and MD report under `claudecode_lane/phase12_batch01_visible_review/`.",
        "",
        "Hard rule: no guessing answers, no Word/PDF/final, no calling the 29-row packet final.",
    ]
    (ROOT / "08_review/claudecode_phase12_batch01_visible_review_prompt_PENDING.md").write_text("\n".join(prompt) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
