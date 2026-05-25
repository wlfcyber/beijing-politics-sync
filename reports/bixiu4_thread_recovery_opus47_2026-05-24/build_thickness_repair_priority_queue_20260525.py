from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
IN_CSV = ROOT / "THICKNESS_DENSITY_AUDIT_20260525.csv"
OUT_CSV = ROOT / "THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.csv"
OUT_MD = ROOT / "THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.md"
OUT_JSON = ROOT / "THICKNESS_REPAIR_PRIORITY_QUEUE_20260525.json"


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M +08")


def as_int(value: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def classify_question_kind(heading: str) -> str:
    if "选择题" in heading:
        return "choice"
    if "主观题" in heading:
        return "subjective"
    return "unknown"


def priority_for(row: dict[str, str]) -> tuple[str, str]:
    flags = set(filter(None, row["thin_flags"].split("|")))
    group = row["group"]
    kind = classify_question_kind(row["heading"])
    triple = {"ANSWER_LT_120_CHARS", "WHY_LT_90_CHARS", "SHORT_WITHOUT_POINT_MARKERS"}.issubset(flags)
    if kind == "subjective" and triple:
        return "P0", "subjective triple-thin: answer<120, why<90, no point markers"
    if group == "inserted" and flags:
        return "P1", "inserted entry needs parity with legacy thickness"
    if kind == "subjective" and flags:
        return "P2", "subjective entry has density flags"
    if kind == "choice" and flags:
        return "P3", "choice-chain entry needs concise key/option/boundary clarity"
    return "P4", "lower-priority density review"


def recommended_action(row: dict[str, str], priority: str) -> str:
    flags = set(filter(None, row["thin_flags"].split("|")))
    actions = []
    if "WHY_LT_90_CHARS" in flags:
        actions.append("expand material-to-principle recognition path")
    if "ANSWER_LT_120_CHARS" in flags:
        actions.append("expand answer landing into concrete exam sentence")
    if "SHORT_WITHOUT_POINT_MARKERS" in flags:
        actions.append("add point structure only where the question is subjective")
    if priority == "P1":
        actions.append("match inserted-entry detail level to surrounding legacy entries")
    if priority == "P3":
        actions.append("keep as choice-chain; do not inflate into subjective rubric")
    return "; ".join(actions) if actions else "semantic review"


def main() -> None:
    with IN_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    candidates = [row for row in rows if row.get("thin_flags")]
    out_rows: list[dict[str, str]] = []
    for idx, row in enumerate(candidates, start=1):
        priority, reason = priority_for(row)
        out_rows.append(
            {
                "queue_id": f"T{idx:04d}",
                "priority": priority,
                "priority_reason": reason,
                "heading": row["heading"],
                "entry_group": row["group"],
                "question_kind": classify_question_kind(row["heading"]),
                "thin_flags": row["thin_flags"],
                "material_chars": row["material_chars"],
                "question_chars": row["question_chars"],
                "why_chars": row["why_chars"],
                "answer_chars": row["answer_chars"],
                "answer_point_markers": row["answer_point_markers"],
                "recommended_action": recommended_action(row, priority),
                "answer_excerpt": row["answer_excerpt"],
            }
        )
    priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3, "P4": 4}
    out_rows.sort(key=lambda r: (priority_order.get(r["priority"], 9), r["entry_group"] != "inserted", r["heading"]))

    fields = [
        "queue_id",
        "priority",
        "priority_reason",
        "heading",
        "entry_group",
        "question_kind",
        "thin_flags",
        "material_chars",
        "question_chars",
        "why_chars",
        "answer_chars",
        "answer_point_markers",
        "recommended_action",
        "answer_excerpt",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_rows)

    priority_counts = Counter(row["priority"] for row in out_rows)
    group_counts = Counter(row["entry_group"] for row in out_rows)
    kind_counts = Counter(row["question_kind"] for row in out_rows)
    flag_counts = Counter()
    for row in out_rows:
        flag_counts.update(filter(None, row["thin_flags"].split("|")))
    summary = {
        "updated": now(),
        "source": IN_CSV.name,
        "total_entries_in_density_audit": len(rows),
        "thin_candidates": len(candidates),
        "queue_rows": len(out_rows),
        "priority_counts": dict(priority_counts),
        "group_counts": dict(group_counts),
        "question_kind_counts": dict(kind_counts),
        "flag_counts": dict(flag_counts),
        "output_csv": OUT_CSV.name,
        "boundary": [
            "This prioritizes semantic repair work; it does not rewrite the handbook.",
            "P0/P1 should be repaired before any final external acceptance retry.",
            "Choice-chain entries must stay objective-answer-key chains, not subjective scoring rubrics.",
        ],
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Thickness Repair Priority Queue 20260525",
        "",
        f"Updated: {summary['updated']}",
        "",
        "Status: `THICKNESS_REPAIR_PRIORITY_QUEUE_CREATED_REPAIR_NOT_DONE`",
        "",
        f"- Source audit: `{IN_CSV.name}`.",
        f"- Total density-audit entries: `{len(rows)}`.",
        f"- Thin candidates queued: `{len(candidates)}`.",
        f"- Queue CSV: `{OUT_CSV.name}`.",
        f"- JSON summary: `{OUT_JSON.name}`.",
        "",
        "## Priority Counts",
        "",
    ]
    for key in sorted(priority_counts, key=lambda k: priority_order.get(k, 9)):
        lines.append(f"- `{key}`: `{priority_counts[key]}`")
    lines.extend(["", "## Group Counts", ""])
    for key, count in group_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Question Kind Counts", ""])
    for key, count in kind_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Flag Counts", ""])
    for key, count in flag_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(
        [
            "",
            "## Repair Rule",
            "",
            "- P0: subjective triple-thin rows: short answer, short reasoning, and no point markers.",
            "- P1: inserted rows with any density flag, because new additions must match legacy thickness.",
            "- P2: remaining subjective rows with density flags.",
            "- P3: choice-chain rows with density flags; keep them as objective-key chains.",
            "",
            "## Boundary",
            "",
            "- This queue is a worklist, not a completed thickness repair.",
            "- It does not close the GPTPro/Claude thickness gate.",
            "- It should be used to drive the next semantic rewrite pass before any external acceptance retry.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
