from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACE = ROOT / "traceability" / "TRACEABILITY_MATRIX_v13_7_final.csv"
OUT = Path(__file__).resolve().parent / "trial_pack_20260523"

SAMPLE_IDS = [
    "CC0084_2025_东城_二模_19",
    "CC0305_2026_海淀_一模_18_3",
    "CC0364_2026_通州_期中_19_1",
    "CC0200_2025_西城_二模_18",
    "CC0131_2025_房山_一模_19",
    "CC0213_2025_门头沟_一模_20",
    "CC0244_2026_东城_期中_18",
    "CC0092_2025_东城_期末_19_1",
]

BLIND_FIELDS = [
    "question_id",
    "year",
    "district",
    "exam_stage",
    "question_no",
    "prompt_action",
    "material_core",
]

KEY_FIELDS = [
    "question_id",
    "a_axis_primary",
    "a_axis_secondary_status",
    "b_axis",
    "proposition_path",
    "rubric_scoring_anchor",
    "material_trigger",
    "answer_skeleton",
    "student_warning",
]


def read_rows() -> list[dict[str, str]]:
    with TRACE.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    by_id = {r["question_id"]: r for r in rows}
    missing = [qid for qid in SAMPLE_IDS if qid not in by_id]
    if missing:
        raise SystemExit(f"missing sample ids: {missing}")
    return [by_id[qid] for qid in SAMPLE_IDS]


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_md(path: Path, rows: list[dict[str, str]]) -> None:
    parts = [
        "# Blind Trial Pack 20260523",
        "",
        "Use this pack to test whether the v13.7 framework can be learned and applied quickly.",
        "",
        "Rules for the reader agent:",
        "",
        "- You may read the framework chapter once before answering.",
        "- You may not read the local answer key, traceability matrix, solved 42-question handbook, scoring anchors, material-trigger chains, answer skeletons, or student warnings.",
        "- For each question, infer A-axis, secondary entrance, B-axis, proposition path, and answer skeleton from the framework plus the compressed question material below.",
        "",
    ]
    for idx, row in enumerate(rows, start=1):
        parts.extend(
            [
                f"## {idx}. {row['question_id']}",
                "",
                f"- 区年卷题：{row['year']}年 {row['district']} {row['exam_stage']} 第{row['question_no']}题",
                f"- 设问动作：{row['prompt_action']}",
                f"- 压缩材料：{row['material_core']}",
                "",
                "Reader output required:",
                "",
                "- A轴主入口：",
                "- A轴副入口/边界：",
                "- B轴设问动作：",
                "- 命题路径：",
                "- 答案骨架：",
                "- 信心分：",
                "- 框架帮到我的地方：",
                "- 框架卡住我的地方：",
                "",
            ]
        )
    path.write_text("\n".join(parts).strip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = read_rows()
    write_md(OUT / "BLIND_TRIAL_PACK.md", rows)
    write_csv(OUT / "BLIND_TRIAL_PACK.csv", rows, BLIND_FIELDS)
    write_csv(OUT / "LOCAL_ANSWER_KEY_NOT_FOR_AGENT.csv", rows, KEY_FIELDS)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
