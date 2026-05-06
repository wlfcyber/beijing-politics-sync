#!/usr/bin/env python3
import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "05_coverage" / "phase04_control_base_status_after_batch02.csv"
OUT_ALL = ROOT / "05_coverage" / "phase04_batch03_Aonly_queue.csv"
OUT_SUBJECTIVE = ROOT / "05_coverage" / "phase04_batch03_A_subjective_queue.csv"
OUT_CHOICE = ROOT / "05_coverage" / "phase04_batch03_B_choice_queue.csv"
OUT_PLAN = ROOT / "05_coverage" / "phase04_batch03_Aonly_queue_plan.md"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def batch_id(row: dict[str, str]) -> str:
    if row["question_type"] == "主观题":
        return "B03A_subjective_first"
    return "B03B_choice_second"


def priority_tuple(row: dict[str, str]) -> tuple[int, int, str, str]:
    priority_rank = {"P0": 0, "P1": 1, "P2": 2, "P3": 3, "": 9}
    scope_rank = {"交叉": 0, "推理": 1, "思维": 2, "边界": 3, "": 9}
    return (
        priority_rank.get(row.get("gap_priority", ""), 8),
        scope_rank.get(row.get("section_scope", ""), 8),
        row.get("suite_id", ""),
        row.get("canonical_question_id", ""),
    )


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def main() -> None:
    rows = read_rows(CONTROL)
    l1 = [r for r in rows if r.get("phase04_level") == "L1_A_ONLY_PENDING_B_TARGET"]
    for row in l1:
        row["batch03_id"] = batch_id(row)
        row["batch03_student_permission"] = "NO_STUDENT_DRAFT"
        row["batch03_required_action"] = (
            "Return to original paper/answer/rubric or rendered visual source; verify module boundary, "
            "answer/rubric pairing, full stem/options or full subjective prompt, and exact reasoning/thinking node."
        )
    l1.sort(key=priority_tuple)
    subjective = [r for r in l1 if r["question_type"] == "主观题"]
    choice = [r for r in l1 if r["question_type"] == "选择题"]

    fields = [
        "batch03_id",
        "canonical_question_id",
        "suite_id",
        "source_id",
        "stable_locator",
        "original_qno",
        "question_type",
        "scope_status",
        "section_scope",
        "knowledge_node",
        "reasoning_node",
        "phase04_level",
        "verification_level",
        "answer_pairing_status",
        "rubric_pairing_status",
        "visual_status",
        "gap_priority",
        "gap_action",
        "blocker_reason",
        "batch03_required_action",
        "batch03_student_permission",
        "excerpt",
    ]
    write_csv(OUT_ALL, l1, fields)
    write_csv(OUT_SUBJECTIVE, subjective, fields)
    write_csv(OUT_CHOICE, choice, fields)

    by_batch = Counter(r["batch03_id"] for r in l1)
    by_type = Counter(r["question_type"] for r in l1)
    by_scope = Counter(r["section_scope"] for r in l1)
    by_priority = Counter(r["gap_priority"] for r in l1)
    top_suites = Counter(r["suite_id"] for r in l1).most_common(20)
    subjective_suites = Counter(r["suite_id"] for r in subjective).most_common(20)
    choice_suites = Counter(r["suite_id"] for r in choice).most_common(20)

    lines = [
        "# Phase04 Batch03 A-only Queue Plan",
        "",
        "- source_control_base: `05_coverage/phase04_control_base_status_after_batch02.csv`",
        "- all_queue: `05_coverage/phase04_batch03_Aonly_queue.csv`",
        "- first_queue_for_claudecode: `05_coverage/phase04_batch03_A_subjective_queue.csv`",
        "- second_queue: `05_coverage/phase04_batch03_B_choice_queue.csv`",
        "- student_doc_status: blocked for all rows",
        "",
        "## Counts",
        "",
        f"- total L1 rows: {len(l1)}",
        f"- by batch: {dict(by_batch)}",
        f"- by question_type: {dict(by_type)}",
        f"- by section_scope: {dict(by_scope)}",
        f"- by gap_priority: {dict(by_priority)}",
        "",
        "## Top Suites In Full Queue",
        "",
    ]
    lines.extend(f"- {suite}: {count}" for suite, count in top_suites)
    lines.extend([
        "",
        "## First Batch: B03A Subjective First",
        "",
        "Rationale: subjective rows carry the highest risk of missing formal rubric boundaries, incomplete prompts, and source-level answer logic. They are also the rows most likely to damage the final book if promoted too early.",
        "",
    ])
    lines.extend(f"- {suite}: {count}" for suite, count in subjective_suites)
    lines.extend([
        "",
        "## Second Batch: B03B Choice Second",
        "",
        "Rationale: choice rows require full stem/options plus reliable answer pairing and trap logic. They remain blocked until independent verification.",
        "",
    ])
    lines.extend(f"- {suite}: {count}" for suite, count in choice_suites)
    lines.extend([
        "",
        "## Hard Gates",
        "",
        "- No row can enter student稿 in Batch03.",
        "- `2024西城一模 Q11` correction remains binding: correct answer pairing is `B=①③`.",
        "- `2025海淀二模 Q12/Q13` must keep answer-source locators.",
        "- Archive skeletons are internal checking tools only.",
    ])
    OUT_PLAN.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
