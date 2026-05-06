#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "05_coverage/phase04_control_base_status.csv"
OUT = ROOT / "05_coverage"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    rows = read_csv(CONTROL)

    reasoning_rows = []
    thinking_rows = []
    for r in rows:
        if r["section_scope"] in {"推理", "交叉"}:
            reasoning_rows.append({
                "question_id": r["canonical_question_id"],
                "suite_id": r["suite_id"],
                "stable_locator": r["stable_locator"],
                "qno": r["original_qno"],
                "question_type": r["question_type"],
                "primary_reasoning_type": r["reasoning_node"],
                "secondary_reasoning_type": "",
                "logical_form": "",
                "rule_slogan": "",
                "valid_or_invalid_pattern": "",
                "trap": "",
                "answer_action": "",
                "same_type_question_ids": "",
                "fusion_status": r["fusion_status"],
                "phase04_level": r["phase04_level"],
                "student稿_permission": r["student稿_permission"],
                "blocker_reason": r["blocker_reason"],
            })
        if r["section_scope"] in {"思维", "交叉"}:
            thinking_rows.append({
                "question_id": r["canonical_question_id"],
                "suite_id": r["suite_id"],
                "stable_locator": r["stable_locator"],
                "qno": r["original_qno"],
                "question_type": r["question_type"],
                "thinking_or_method": r["knowledge_node"],
                "material_signal": "",
                "answer_action": "",
                "answer_landing": "",
                "source_example": r["canonical_question_id"],
                "same_type_question_ids": "",
                "optional_angle_pool": "",
                "trap_or_boundary": "",
                "fusion_status": r["fusion_status"],
                "phase04_level": r["phase04_level"],
                "student稿_permission": r["student稿_permission"],
                "blocker_reason": r["blocker_reason"],
            })

    write_csv(
        OUT / "phase04_reasoning_attachment_matrix.csv",
        list(reasoning_rows[0]) if reasoning_rows else ["question_id"],
        reasoning_rows,
    )
    write_csv(
        OUT / "phase04_thinking_signal_chain_matrix.csv",
        list(thinking_rows[0]) if thinking_rows else ["question_id"],
        thinking_rows,
    )

    reasoning_groups: dict[str, list[str]] = defaultdict(list)
    for r in reasoning_rows:
        node = r["primary_reasoning_type"] or "PENDING_TYPE_EXTRACTION"
        reasoning_groups[node].append(r["question_id"])

    thinking_groups: dict[str, list[str]] = defaultdict(list)
    for r in thinking_rows:
        node = r["thinking_or_method"] or "PENDING_SIGNAL_EXTRACTION"
        thinking_groups[node].append(r["question_id"])

    with (OUT / "phase04_same_type_archive.md").open("w", encoding="utf-8") as f:
        f.write("# Phase04 Same-Type Archive Skeleton\n\n")
        f.write("This is an evidence-pool skeleton only. It does not authorize student稿.\n\n")
        f.write("## Reasoning\n\n")
        for node, ids in sorted(reasoning_groups.items()):
            f.write(f"### {node}\n\n")
            for qid in ids:
                f.write(f"- {qid}\n")
            f.write("\n")
        f.write("## Thinking\n\n")
        for node, ids in sorted(thinking_groups.items()):
            f.write(f"### {node}\n\n")
            for qid in ids:
                f.write(f"- {qid}\n")
            f.write("\n")

    (OUT / "phase04_reasoning_typology_tree_observed.md").write_text(
        "# Phase04 Observed Reasoning Typology Tree Skeleton\n\n"
        "Derived from Phase04 control rows. Empty or pending nodes must be resolved by targeted source verification before any student-facing prose.\n\n"
        + "\n".join(f"- {node}: {len(ids)} row(s)" for node, ids in sorted(reasoning_groups.items()))
        + "\n",
        encoding="utf-8",
    )

    (OUT / "phase04_thinking_method_archive.md").write_text(
        "# Phase04 Thinking Method Archive Skeleton\n\n"
        "Derived from Phase04 control rows. Each node still needs material signal, answer action, and source-example verification.\n\n"
        + "\n".join(f"- {node}: {len(ids)} row(s)" for node, ids in sorted(thinking_groups.items()))
        + "\n",
        encoding="utf-8",
    )

    print("reasoning rows", len(reasoning_rows))
    print("thinking rows", len(thinking_rows))


if __name__ == "__main__":
    main()
