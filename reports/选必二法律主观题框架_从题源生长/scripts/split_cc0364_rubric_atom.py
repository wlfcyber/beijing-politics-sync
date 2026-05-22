#!/usr/bin/env python3
"""Split the collapsed CC0364 rubric atom into source-checked scoring atoms."""

from __future__ import annotations

import csv
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
TARGET = ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv"
OUT_DIR = ROOT / "04_merge_audit" / "cc0364_split_patch_20260519"
QID = "CC0364_2026_通州_期末_19_1"


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def make_row(fields: list[str], **values: str) -> dict[str, str]:
    row = {field: "" for field in fields}
    row.update(
        {
            "question_id": QID,
            "evidence_type": "marking_rubric",
            "evidence_level": "formal",
            "source_locator": "F0223:slide 11 | F0403:slide 11",
            "can_be_written_without_material": "no",
        }
    )
    row.update(values)
    return row


def patch_rows(fields: list[str]) -> list[dict[str, str]]:
    mats_all = "|".join(f"M_CC0364_2026_通州_期末_19_1_{i:02d}" for i in range(1, 7))
    mats_fact = "|".join(
        [
            "M_CC0364_2026_通州_期末_19_1_01",
            "M_CC0364_2026_通州_期末_19_1_02",
            "M_CC0364_2026_通州_期末_19_1_03",
            "M_CC0364_2026_通州_期末_19_1_04",
            "M_CC0364_2026_通州_期末_19_1_05",
        ]
    )
    return [
        make_row(
            fields,
            rubric_atom_id="PATCH_CC0364_R01",
            rubric_or_answer_phrase="法理依据：依据《中华人民共和国民法典》规定。（1分；仅写“按照法律”不给分；若未写相邻关系法理但写出“法院判决以事实为根据，以法律为准绳”，可给1分，且不与本项重复给分）",
            plain_reward_description="奖励学生明确写出具体法律依据是《中华人民共和国民法典》，而不是空泛写依法。",
            related_material_atom_ids=mats_all,
            what_expression_is_rewarded="《中华人民共和国民法典》；法院以事实为根据、以法律为准绳只作本格替代1分，不重复。",
            what_judgment_student_must_make_before_writing="先判断本案属于民法典调整的不动产相邻关系纠纷，而不是泛泛法治题。",
            legal_knowledge_or_rule_if_explicit="民法典；相邻关系",
            value_expression_if_explicit="",
            knowledge_material_value_type="knowledge+material",
            uncertainty="cc0364_split_patch_20260519; alternative_anchor_not_cumulative_with_R02",
        ),
        make_row(
            fields,
            rubric_atom_id="PATCH_CC0364_R02",
            rubric_or_answer_phrase="法理依据：不动产的相邻权利人应当按照有利生产、方便生活、团结互助、公平合理的原则，正确处理相邻关系。（2分；写应当为相邻方提供便利或不侵害相邻方合法权益给1分）",
            plain_reward_description="奖励学生完整写出相邻关系处理原则，并能落到相邻权利人之间的权利义务边界。",
            related_material_atom_ids=mats_all,
            what_expression_is_rewarded="不动产相邻权利人；有利生产；方便生活；团结互助；公平合理；正确处理相邻关系。",
            what_judgment_student_must_make_before_writing="判断双方是相邻不动产权利人，争议焦点是加装电梯便利与采光通风等相邻利益的平衡。",
            legal_knowledge_or_rule_if_explicit="民法典相邻关系规则",
            value_expression_if_explicit="公平合理；团结互助",
            knowledge_material_value_type="knowledge+value",
            uncertainty="cc0364_split_patch_20260519",
        ),
        make_row(
            fields,
            rubric_atom_id="PATCH_CC0364_R03",
            rubric_or_answer_phrase="事实分析：从2单元业主角度说明，加装电梯已获业主同意、公示无异议并取得审批，电梯采用全玻璃设计且现场勘查未影响相邻楼采光，范某阻碍施工妨害业主合法权益，故判令停止阻挠。（2分）",
            plain_reward_description="奖励学生把材料事实转化为“程序合法、影响未成立、阻挠构成妨害”的判决理由。",
            related_material_atom_ids=mats_fact,
            what_expression_is_rewarded="业主同意；公示无异议；审批手续；全玻璃设计；未影响采光；停止阻挠/排除妨害。",
            what_judgment_student_must_make_before_writing="判断判决支持业主，是因为加装工程程序和事实基础成立，而范某阻碍施工缺乏事实依据。",
            legal_knowledge_or_rule_if_explicit="相邻关系；排除妨害；合法权益保护",
            value_expression_if_explicit="",
            knowledge_material_value_type="knowledge+material",
            uncertainty="cc0364_split_patch_20260519; fact_analysis_owner_angle_full_2_points",
        ),
        make_row(
            fields,
            rubric_atom_id="PATCH_CC0364_R04",
            rubric_or_answer_phrase="事实分析：从范某角度说明，其主张采光受影响，但法院现场勘查认定未造成影响；若投入使用后确有较大影响，相关权利人可另行协商或通过法律途径解决。（1分；不与业主角度2分重复给分）",
            plain_reward_description="奖励学生回应范某的权利主张，但该角度是事实分析的低分/替代口径，不得与业主角度累计成3分。",
            related_material_atom_ids="M_CC0364_2026_通州_期末_19_1_03|M_CC0364_2026_通州_期末_19_1_05|M_CC0364_2026_通州_期末_19_1_06",
            what_expression_is_rewarded="范某采光主张；现场勘查未造成影响；确有影响可协商或依法解决。",
            what_judgment_student_must_make_before_writing="判断相邻方权利并非不存在，而是本案当前事实不足以支持其阻工；未来实际损害可另行救济。",
            legal_knowledge_or_rule_if_explicit="相邻关系；民事纠纷解决",
            value_expression_if_explicit="",
            knowledge_material_value_type="knowledge+material",
            uncertainty="cc0364_split_patch_20260519; alternative_fact_angle_not_cumulative_with_PATCH_CC0364_R03",
        ),
        make_row(
            fields,
            rubric_atom_id="PATCH_CC0364_R05",
            rubric_or_answer_phrase="判决意义：维护相关业主合法权益。（1分）",
            plain_reward_description="奖励学生把判决意义落回具体权利保护，而不是只写宏观法治意义。",
            related_material_atom_ids=mats_fact,
            what_expression_is_rewarded="维护业主合法权益。",
            what_judgment_student_must_make_before_writing="先判断被保护的具体权益是加装电梯业主的合法权益和相邻权益平衡。",
            legal_knowledge_or_rule_if_explicit="民事权利保护；相邻关系",
            value_expression_if_explicit="维护合法权益",
            knowledge_material_value_type="knowledge+material+value",
            uncertainty="cc0364_split_patch_20260519",
        ),
        make_row(
            fields,
            rubric_atom_id="PATCH_CC0364_R06",
            rubric_or_answer_phrase="判决意义：有助于促进邻里和谐。（1分）",
            plain_reward_description="奖励学生从相邻关系规则推出邻里关系价值收束。",
            related_material_atom_ids=mats_all,
            what_expression_is_rewarded="促进邻里和谐。",
            what_judgment_student_must_make_before_writing="判断价值收束必须从相邻关系规则和具体争议解决推出。",
            legal_knowledge_or_rule_if_explicit="相邻关系",
            value_expression_if_explicit="邻里和谐",
            knowledge_material_value_type="knowledge+material+value",
            uncertainty="cc0364_split_patch_20260519",
        ),
        make_row(
            fields,
            rubric_atom_id="PATCH_CC0364_R07",
            rubric_or_answer_phrase="判决意义：践行友善等社会主义核心价值观。（1分）",
            plain_reward_description="奖励学生作价值收束，但必须附着在相邻关系和判决事实上，不能写成空泛必修三。",
            related_material_atom_ids=mats_all,
            what_expression_is_rewarded="践行友善的社会主义核心价值观。",
            what_judgment_student_must_make_before_writing="判断价值表达是法律规则和纠纷解决后的收束，不是答案主体。",
            legal_knowledge_or_rule_if_explicit="相邻关系",
            value_expression_if_explicit="友善；社会主义核心价值观",
            knowledge_material_value_type="knowledge+material+value",
            uncertainty="cc0364_split_patch_20260519; value_tail_not_independent_framework_core",
        ),
    ]


def main() -> None:
    fields, rows = read_csv(TARGET)
    original_counts = Counter(row["question_id"] for row in rows)
    original_cc0364 = [row for row in rows if row.get("question_id") == QID]

    backup_dir = ROOT / "tool_outputs" / f"pre_cc0364_split_patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TARGET, backup_dir / TARGET.name)

    patches = patch_rows(fields)
    output = []
    inserted = False
    removed = 0
    for row in rows:
        if row.get("question_id") == QID:
            removed += 1
            if not inserted:
                output.extend(patches)
                inserted = True
            continue
        output.append(row)
    if not inserted:
        output.extend(patches)

    write_csv(TARGET, fields, output)

    report_fields = [
        "question_id",
        "original_atoms_removed",
        "patch_atoms_added",
        "original_count_before_patch",
        "backup_file",
    ]
    write_csv(
        OUT_DIR / "cc0364_split_patch_report.csv",
        report_fields,
        [
            {
                "question_id": QID,
                "original_atoms_removed": str(removed),
                "patch_atoms_added": str(len(patches)),
                "original_count_before_patch": str(original_counts[QID]),
                "backup_file": str(backup_dir / TARGET.name),
            }
        ],
    )
    write_csv(OUT_DIR / "cc0364_original_collapsed_atom_backup.csv", fields, original_cc0364)
    write_csv(OUT_DIR / "cc0364_patch_atoms.csv", fields, patches)

    md = [
        "# CC0364 Rubric Atom Split Patch",
        "",
        f"- target: `{TARGET}`",
        f"- backup: `{backup_dir / TARGET.name}`",
        f"- question_id: `{QID}`",
        f"- removed collapsed atoms: {removed}",
        f"- added split atoms: {len(patches)}",
        "",
        "## Split Logic",
        "",
        "- `PATCH_CC0364_R01`: 民法典依据 1 分；“以事实为根据，以法律为准绳”只作不重复替代锚点。",
        "- `PATCH_CC0364_R02`: 相邻关系原则 2 分。",
        "- `PATCH_CC0364_R03`: 业主角度事实分析 2 分。",
        "- `PATCH_CC0364_R04`: 范某角度事实分析 1 分；不与 R03 累加。",
        "- `PATCH_CC0364_R05`: 维护业主合法权益 1 分。",
        "- `PATCH_CC0364_R06`: 促进邻里和谐 1 分。",
        "- `PATCH_CC0364_R07`: 践行友善等社会主义核心价值观 1 分。",
        "",
        "## Gate Impact",
        "",
        "`CC0364` is no longer source-check pending at atom level. It may now be counted as limited support for the expanded 004/006 code branch, while its value-tail atoms cannot independently support a core framework node.",
        "",
    ]
    (OUT_DIR / "cc0364_split_patch_report.md").write_text("\n".join(md), encoding="utf-8")

    print(f"Backed up target to {backup_dir / TARGET.name}")
    print(f"CC0364 split row count: {len(rows)} -> {len(output)}")
    print(f"Removed {removed}, added {len(patches)}")


if __name__ == "__main__":
    main()
