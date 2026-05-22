#!/usr/bin/env python3
"""Apply GPTPro guarded-v2 evidence cleanup before regenerating outputs."""

from __future__ import annotations

import csv
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
MERGED_RUBRIC = ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv"
CODEBOOK_IN = ROOT / "08_codebook" / "provisional_codebook_v1_2_after_fail4_cowork_20260519.csv"
CODEBOOK_OUT = ROOT / "08_codebook" / "provisional_codebook_v1_3_after_gptpro_guarded_review_20260519.csv"
PATCH_DIR = ROOT / "10_framework_validation" / "gptpro_guarded_v2_cleanup_20260519"
PATCH_REPORT = PATCH_DIR / "gptpro_guarded_v2_cleanup_report.md"


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


def backup(path: Path) -> None:
    if path.exists():
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        shutil.copy2(path, path.with_name(f"{path.stem}.pre_gptpro_cleanup_{stamp}{path.suffix}"))


def pipe_values(value: str) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for part in (value or "").split("|"):
        item = part.strip()
        if item and item not in seen:
            out.append(item)
            seen.add(item)
    return out


def replace_pipe(value: str, *, remove: set[str] = frozenset(), add: list[str] | None = None) -> str:
    values = [item for item in pipe_values(value) if item not in remove]
    for item in add or []:
        if item and item not in values:
            values.append(item)
    return "|".join(values)


def base_for(rows: list[dict[str, str]], atom_id: str) -> dict[str, str]:
    for row in rows:
        if row["rubric_atom_id"] == atom_id:
            return dict(row)
    raise KeyError(atom_id)


def patch_atom(base: dict[str, str], atom_id: str, phrase: str, desc: str) -> dict[str, str]:
    row = dict(base)
    row["rubric_atom_id"] = atom_id
    row["rubric_or_answer_phrase"] = phrase
    row["plain_reward_description"] = desc
    row["what_expression_is_rewarded"] = desc
    row["uncertainty"] = "gptpro_guarded_v2_patch_atom_from_formal_source_20260519"
    return row


def apply_rubric_cleanup() -> dict[str, int]:
    fields, rows = read_csv(MERGED_RUBRIC)
    backup(MERGED_RUBRIC)

    non_scoring_exact = {
        *{f"R_CC0077_2025_东城_一模_19_{i:02d}" for i in range(5, 13)},
        *{f"R_CC0084_2025_东城_二模_19_{i:02d}" for i in range(6, 12)},
        *{f"R_CC0150_2025_朝阳_二模_20_{i:02d}" for i in range(12, 25)},
        "R_CC0244_2026_东城_期末_18_08",
        *{f"R_CC0245_2026_东城_期末_18_2_{i:02d}" for i in range(2, 5)},
        *{f"R_CC0251_2026_丰台_一模_20_{i:02d}" for i in range(2, 17)},
    }
    marked = 0
    for row in rows:
        atom_id = row["rubric_atom_id"]
        if atom_id in non_scoring_exact:
            row["uncertainty"] = replace_pipe(
                row.get("uncertainty", ""),
                add=["gptpro_guarded_v2_non_scoring_risk_or_other_question_not_core_support"],
            )
            marked += 1

    existing = {row["rubric_atom_id"] for row in rows}
    new_atoms: list[dict[str, str]] = []

    cc0245_base = base_for(rows, "R_CC0245_2026_东城_期末_18_2_01")
    cc0245_atoms = [
        (
            "PATCH_CC0245_R01A_REMEDY_PATH",
            "维权途径：可选择调解、仲裁或诉讼；材料已经协商未果时，不再把协商作为主要维权路径。",
            "奖励学生根据材料程序状态选择合适维权途径，避免写错上诉、行政诉讼或继续协商。",
        ),
        (
            "PATCH_CC0245_R01B_EVIDENCE_PREP",
            "证据准备：依法收集并固定合同、订单、转账、邮件记录、无人机故障、受伤事实和经济损失等证据，形成证据链。",
            "奖励学生把材料事实转成证据类型，并说明依法收集、固定证据。",
        ),
        (
            "PATCH_CC0245_R01C_REASONABLE_REQUEST",
            "合理诉求：明确权利义务和法律依据，围绕违约责任或侵权责任提出退还购置费、赔偿医疗费、误工费、经济损失等请求。",
            "奖励学生把实体权利、责任类型和具体诉求写在同一答题层。",
        ),
    ]
    for atom_id, phrase, desc in cc0245_atoms:
        if atom_id not in existing:
            new_atoms.append(patch_atom(cc0245_base, atom_id, phrase, desc))

    cc0251_base = base_for(rows, "R_CC0251_2026_丰台_一模_20_01")
    cc0251_atoms = [
        (
            "PATCH_CC0251_R01A_COURT_ANCHOR",
            "人民法院以事实为根据、以法律为准绳作出判决。",
            "奖励学生使用裁判题的事实与法律锚句。",
        ),
        (
            "PATCH_CC0251_R01B_PUBLIC_PLACE_RULE",
            "根据民法典，经营场所、公共场所经营者、管理者因过错造成他人损害的，应承担侵权责任。",
            "奖励学生准确写出公共场所管理者过错责任规则。",
        ),
        (
            "PATCH_CC0251_R01C_FACT_NO_FAULT",
            "材料表明事发现场不存在影响通行的客观因素，原告系完全民事行为能力人且未尽安全注意义务，某餐饮公司和某商业管理公司无过错，不承担赔偿责任。",
            "奖励学生把材料事实嵌入责任归属判断。",
        ),
        (
            "PATCH_CC0251_R01D_VALUE_BOUNDARY",
            "该判决有利于平衡原被告权利义务，倡导安全文明出行和自我负责的安全责任意识，明确公共场所经营者、管理者安全保障义务边界，弘扬社会主义核心价值观。",
            "奖励学生从判决推出规范公共行为与安全保障义务边界的价值收束。",
        ),
    ]
    for atom_id, phrase, desc in cc0251_atoms:
        if atom_id not in existing:
            new_atoms.append(patch_atom(cc0251_base, atom_id, phrase, desc))

    rows.extend(new_atoms)
    patch_atoms_present = sum(1 for row in rows if row["rubric_atom_id"].startswith(("PATCH_CC0245_", "PATCH_CC0251_")))
    write_csv(MERGED_RUBRIC, fields, rows)
    return {
        "marked_non_scoring_atoms": marked,
        "added_patch_atoms_this_run": len(new_atoms),
        "patch_atoms_present": patch_atoms_present,
        "rubric_atom_total": len(rows),
    }


def apply_codebook_cleanup() -> dict[str, int]:
    fields, rows = read_csv(CODEBOOK_IN)
    exact_remove = {
        "CODE_COWORK_001": {
            "R_CC0077_2025_东城_一模_19_07",
            "R_CC0084_2025_东城_二模_19_07",
        },
        "CODE_COWORK_006": {"R_CC0244_2026_东城_期末_18_08"},
        "CODE_COWORK_007": {
            "R_CC0245_2026_东城_期末_18_2_01",
            "R_CC0245_2026_东城_期末_18_2_02",
            "R_CC0245_2026_东城_期末_18_2_03",
            "R_CC0245_2026_东城_期末_18_2_04",
            "R_CC0380_2026_顺义_二模_18_2_P01",
            "R_CC0380_2026_顺义_二模_18_2_P03",
            "R_CC0380_2026_顺义_二模_18_2_P04",
        },
    }
    exact_add = {
        "CODE_COWORK_001": [
            "R_CC0077_2025_东城_一模_19_03",
            "R_CC0077_2025_东城_一模_19_04",
            "R_CC0084_2025_东城_二模_19_02",
            "R_CC0084_2025_东城_二模_19_03",
            "R_CC0084_2025_东城_二模_19_04",
            "R_CC0084_2025_东城_二模_19_05",
        ],
        "CODE_COWORK_006": [
            "R_CC0244_2026_东城_期末_18_03",
            "R_CC0244_2026_东城_期末_18_05",
        ],
        "CODE_COWORK_007": [
            "PATCH_CC0245_R01A_REMEDY_PATH",
            "PATCH_CC0245_R01B_EVIDENCE_PREP",
            "PATCH_CC0245_R01C_REASONABLE_REQUEST",
        ],
        "CODE_COWORK_002": ["PATCH_CC0251_R01D_VALUE_BOUNDARY"],
        "CODE_COWORK_003": ["PATCH_CC0251_R01A_COURT_ANCHOR"],
        "CODE_COWORK_004": [
            "R_CC0150_2025_朝阳_二模_20_09",
            "R_CC0150_2025_朝阳_二模_20_10",
            "R_CC0150_2025_朝阳_二模_20_11",
            "PATCH_CC0251_R01B_PUBLIC_PLACE_RULE",
            "PATCH_CC0251_R01C_FACT_NO_FAULT",
        ],
    }
    q_remove = {"CODE_COWORK_007": {"CC0380_2026_顺义_二模_18_2"}}
    material_remove_prefix = {"CODE_COWORK_007": ("M_CC0380_2026_顺义_二模_18_2_",)}

    changed = 0
    for row in rows:
        code_id = row["code_id"]
        before = dict(row)
        row["supporting_rubric_atom_ids"] = replace_pipe(
            row.get("supporting_rubric_atom_ids", ""),
            remove=exact_remove.get(code_id, set()),
            add=exact_add.get(code_id, []),
        )
        if code_id in q_remove:
            row["supporting_question_ids"] = replace_pipe(
                row.get("supporting_question_ids", ""),
                remove=q_remove[code_id],
            )
        if code_id in material_remove_prefix:
            values = [
                item for item in pipe_values(row.get("supporting_material_atom_ids", ""))
                if not any(item.startswith(prefix) for prefix in material_remove_prefix[code_id])
            ]
            row["supporting_material_atom_ids"] = "|".join(values)
        if code_id == "CODE_COWORK_007":
            row["reason"] = row.get("reason", "") + "|gptpro_guarded_v2: framework layer must split 007A/007B/007C/007D; CC0380 moved to open container; CC0245 support uses patch scoring atoms."
        if code_id == "CODE_COWORK_001":
            row["reason"] = row.get("reason", "") + "|gptpro_guarded_v2: student-problem atoms moved out of core support."
        if row != before:
            changed += 1

    write_csv(CODEBOOK_OUT, fields, rows)
    return {"codebook_rows_changed": changed, "codebook_rows_total": len(rows)}


def main() -> None:
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    rubric_stats = apply_rubric_cleanup()
    codebook_stats = apply_codebook_cleanup()
    report = [
        "# GPTPro Guarded v2 Evidence Cleanup Report",
        "",
        "- Source: real GPT-5.5 Pro guarded-v2 review captured at `tool_outputs/gpt55pro_guarded_v2_review_response_20260519.md`.",
        "- Purpose: remove student-problem, teaching-suggestion, other-question, and non-core open-container material from scoring support before regeneration.",
        "",
        "## Results",
        "",
        f"- marked_non_scoring_atoms: {rubric_stats['marked_non_scoring_atoms']}",
        f"- added_patch_atoms_this_run: {rubric_stats['added_patch_atoms_this_run']}",
        f"- patch_atoms_present: {rubric_stats['patch_atoms_present']}",
        f"- rubric_atom_total_after_patch: {rubric_stats['rubric_atom_total']}",
        f"- codebook_rows_changed: {codebook_stats['codebook_rows_changed']}",
        f"- codebook_rows_total: {codebook_stats['codebook_rows_total']}",
        "",
        "## Hard Rules Applied",
        "",
        "- CC0077 support trimmed to scoring atoms R02-R04; later student-problem atoms are risk evidence only.",
        "- CC0084 support trimmed to scoring atoms R02-R05; later student-problem atoms are risk evidence only.",
        "- CC0150 answer/pressure support is limited to the Q20 legal scoring chain R05-R11; Q21 国际政治经济 atoms are archived as non-project material.",
        "- CC0245 uses three patch scoring atoms for path, evidence, and reasonable request; R02-R04 are risk/teaching notes.",
        "- CC0251 uses four patch scoring atoms; R02-R16 are risk/teaching/other-question material.",
        "- CODE_COWORK_007 is no longer treated as a single framework node; framework generation must split it into subtypes.",
        "",
    ]
    PATCH_REPORT.write_text("\n".join(report), encoding="utf-8")
    print(PATCH_REPORT)


if __name__ == "__main__":
    main()
