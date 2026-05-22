#!/usr/bin/env python3
"""Build cross-validation artifacts for the post-Cowork codebook expansion round."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
OUT_DIR = ROOT / "07_cross_validation" / "codebook_expansion_after_cowork_sourcecheck_20260519"
OBS_DIR = ROOT / "06_open_observations" / "codebook_expansion_after_cowork_sourcecheck_20260519"

GPT_MD = OBS_DIR / "gpt55pro_codebook_expansion_after_cowork_sourcecheck_20260519.md"
GPT_CSV = OBS_DIR / "gpt55pro_codebook_expansion_after_cowork_sourcecheck_20260519.csv"
CLAUDE_CSV = OBS_DIR / "claude_opus_codebook_expansion_after_cowork_sourcecheck_20260519.csv"


def split_ids(value: str) -> set[str]:
    if not value:
        return set()
    parts = re.split(r"[|、,，\s]+", value)
    return {p.strip("` ") for p in parts if p.strip("` ")}


def read_gpt_tsv() -> list[dict[str, str]]:
    text = GPT_MD.read_text(encoding="utf-8")
    match = re.search(r"```tsv\n(.*?)\n```", text, flags=re.S)
    if not match:
        raise SystemExit(f"No TSV fenced block found in {GPT_MD}")
    rows = list(csv.DictReader(match.group(1).splitlines(), delimiter="\t"))
    GPT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with GPT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return rows


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def index(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    return {r[key]: r for r in rows}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    gpt_rows = read_gpt_tsv()
    claude_rows = read_csv(CLAUDE_CSV)
    gpt = index(gpt_rows, "expansion_decision_id")
    claude = index(claude_rows, "expansion_decision_id")

    comparisons = [
        {
            "comparison_id": "EXP_CMP_001",
            "gpt_observation_id": "DEC_001",
            "claude_observation_id": "EXP_DEC_001",
            "match_type": "similar",
            "difference_description": "Both accept CODE_COWORK_008, but GPT trims CC0143 and RECOVER_2026_西城_二模_18_2 from core support while Claude includes them.",
            "better_supported_side": "GPT+local_source_check",
            "needs_source_check": "no",
            "decision": "merge_keep_trimmed",
            "reason": "Use the stricter support set: CC0131, CC0206, CC0229, CC0283, CC0319, CC0103. CC0143 is a consumer-fraud counterexample; RECOVER_2026_西城_二模_18_2 stays AI open-container.",
        },
        {
            "comparison_id": "EXP_CMP_002",
            "gpt_observation_id": "DEC_002",
            "claude_observation_id": "EXP_DEC_002",
            "match_type": "same",
            "difference_description": "Both revise CODE_COWORK_001 with a table/completion sub-type, keeping the original independent-cell rule.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "keep",
            "reason": "Dual-model agreement and formal multi-question support.",
        },
        {
            "comparison_id": "EXP_CMP_003",
            "gpt_observation_id": "DEC_003|DEC_012",
            "claude_observation_id": "EXP_DEC_003|EXP_DEC_007",
            "match_type": "similar",
            "difference_description": "Both revise CODE_COWORK_002 for principle/institution/case significance. GPT is stricter about excluding RECOVER_2026_西城_二模_18_3 from core support.",
            "better_supported_side": "GPT+local_source_check",
            "needs_source_check": "no",
            "decision": "merge_keep_with_boundary_trim",
            "reason": "Use patched CC0019 atoms and keep governance-heavy RECOVER_2026_西城_二模_18_3 as open-container only.",
        },
        {
            "comparison_id": "EXP_CMP_004",
            "gpt_observation_id": "DEC_004",
            "claude_observation_id": "EXP_DEC_004",
            "match_type": "similar",
            "difference_description": "Both revise CODE_COWORK_007; GPT requires two sub-patterns instead of one broad code.",
            "better_supported_side": "GPT",
            "needs_source_check": "no",
            "decision": "split_then_keep",
            "reason": "Two sub-patterns prevent over-broad remedies/procedure wording and reduce 必修三化 or民诉格式化 risk.",
        },
        {
            "comparison_id": "EXP_CMP_005",
            "gpt_observation_id": "DEC_005",
            "claude_observation_id": "EXP_DEC_005",
            "match_type": "same",
            "difference_description": "Both revise CODE_COWORK_004/006 for multi-actor or multi-request independent chains, with CC0364 needing atom split.",
            "better_supported_side": "shared",
            "needs_source_check": "yes",
            "decision": "keep_pending_cc0364_split",
            "reason": "CC0238 and RECOVER_2026_西城_二模_18_1 can support limited revision; CC0364 must be split before stronger support is counted.",
        },
        {
            "comparison_id": "EXP_CMP_006",
            "gpt_observation_id": "DEC_011",
            "claude_observation_id": "EXP_DEC_006",
            "match_type": "same",
            "difference_description": "Both require CC0011 atom replacement with PATCH_CC0011_R01-R04.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "patch_before_use",
            "reason": "Current single atom is too collapsed; patch atoms are source-checked formal evidence.",
        },
        {
            "comparison_id": "EXP_CMP_007",
            "gpt_observation_id": "DEC_012",
            "claude_observation_id": "EXP_DEC_007",
            "match_type": "same",
            "difference_description": "Both require CC0019 atom replacement with PATCH_CC0019_R01-R06.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "patch_before_use",
            "reason": "Current single atom is too collapsed; patch atoms separate market-economy, contract, judiciary, operator, consumer rewards.",
        },
        {
            "comparison_id": "EXP_CMP_008",
            "gpt_observation_id": "DEC_013",
            "claude_observation_id": "EXP_DEC_008",
            "match_type": "same",
            "difference_description": "Both require CC0061 split/trim by 18(1), 18(2), 18(3).",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "split_before_use",
            "reason": "18(1)(2) are procedure micro-items; only 18(3) can support family-duty/value observations.",
        },
        {
            "comparison_id": "EXP_CMP_009",
            "gpt_observation_id": "DEC_014",
            "claude_observation_id": "EXP_DEC_009|EXP_DEC_012",
            "match_type": "same",
            "difference_description": "Both reject CC0254's current canonical R01-R08 as scoring atoms and require PATCH_CC0254_R01-R08.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "replace_wrong_atoms",
            "reason": "Current atoms came from student-problem/teaching-suggestion slides, not scoring atoms.",
        },
        {
            "comparison_id": "EXP_CMP_010",
            "gpt_observation_id": "DEC_015",
            "claude_observation_id": "EXP_DEC_010|EXP_DEC_012",
            "match_type": "same",
            "difference_description": "Both keep RECOVER_2026_房山_一模_17_1 formal but require 1+2 alternative logic.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "rewrite_alternative_atoms",
            "reason": "Subject/content/object dimensions are alternative explanations, not cumulative scoring atoms.",
        },
        {
            "comparison_id": "EXP_CMP_011",
            "gpt_observation_id": "DEC_008",
            "claude_observation_id": "EXP_DEC_011",
            "match_type": "same",
            "difference_description": "Both reject CC0276涉外法治公共政策论证 as core code.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "discard_core_open_container",
            "reason": "High module-boundary risk and single public-policy sample.",
        },
        {
            "comparison_id": "EXP_CMP_012",
            "gpt_observation_id": "DEC_010",
            "claude_observation_id": "EXP_DEC_013",
            "match_type": "same",
            "difference_description": "Both reject the four reference_only rows as core support.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "discard_core_reference_only",
            "reason": "reference_only cannot independently support core codebook nodes.",
        },
        {
            "comparison_id": "EXP_CMP_013",
            "gpt_observation_id": "DEC_006",
            "claude_observation_id": "EXP_DEC_014",
            "match_type": "same",
            "difference_description": "Both keep CC0025 platform labor subordination only as open container.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "open_container_only",
            "reason": "Single formal sample without repeated pattern.",
        },
        {
            "comparison_id": "EXP_CMP_014",
            "gpt_observation_id": "DEC_007",
            "claude_observation_id": "EXP_DEC_015",
            "match_type": "same",
            "difference_description": "Both keep CC0200 minor transaction/fault allocation only as open container.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "open_container_only",
            "reason": "Single formal sample without repeated pattern.",
        },
        {
            "comparison_id": "EXP_CMP_015",
            "gpt_observation_id": "DEC_016",
            "claude_observation_id": "EXP_DEC_016",
            "match_type": "same",
            "difference_description": "Both keep scattered singletons or wide-mouth transfer rows outside the core codebook.",
            "better_supported_side": "shared",
            "needs_source_check": "no",
            "decision": "open_container_only",
            "reason": "No stable common minimal judgment or repeated rubric reward pattern.",
        },
        {
            "comparison_id": "EXP_CMP_016",
            "gpt_observation_id": "DEC_005",
            "claude_observation_id": "EXP_DEC_017",
            "match_type": "similar",
            "difference_description": "Claude adds a CC0364 source-check-needed split; GPT already names CC0364 as partial support for CODE_COWORK_004/006.",
            "better_supported_side": "Claude",
            "needs_source_check": "yes",
            "decision": "source_check_pending",
            "reason": "CC0364 is currently one giant atom and must be split before being counted as strong support.",
        },
    ]

    for row in comparisons:
        g_ids = set()
        c_ids = set()
        for key in row["gpt_observation_id"].split("|"):
            if key in gpt:
                g_ids |= split_ids(gpt[key].get("supporting_question_ids", ""))
        for key in row["claude_observation_id"].split("|"):
            if key in claude:
                c_ids |= split_ids(claude[key].get("supporting_question_ids", ""))
        row["shared_question_ids"] = "|".join(sorted(g_ids & c_ids))
        row["shared_rubric_atom_ids"] = ""
        row["shared_material_atom_ids"] = ""

    fields = [
        "comparison_id",
        "gpt_observation_id",
        "claude_observation_id",
        "match_type",
        "shared_question_ids",
        "shared_rubric_atom_ids",
        "shared_material_atom_ids",
        "difference_description",
        "better_supported_side",
        "needs_source_check",
        "decision",
        "reason",
    ]
    comparison_csv = OUT_DIR / "codebook_expansion_after_cowork_sourcecheck_comparison.csv"
    with comparison_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(comparisons)

    accepted = [r for r in comparisons if r["decision"] in {"merge_keep_trimmed", "keep", "merge_keep_with_boundary_trim", "split_then_keep", "keep_pending_cc0364_split"}]
    rejected = [r for r in comparisons if r["decision"].startswith("discard") or r["decision"] == "open_container_only"]
    source_check = [r for r in comparisons if r["needs_source_check"] == "yes" or r["decision"] in {"patch_before_use", "split_before_use", "replace_wrong_atoms", "rewrite_alternative_atoms", "source_check_pending"}]

    for name, rows in [
        ("accepted_codebook_expansion_decisions.csv", accepted),
        ("rejected_or_open_container_expansion_decisions.csv", rejected),
        ("source_check_needed_after_expansion.csv", source_check),
    ]:
        with (OUT_DIR / name).open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    md = [
        "# Codebook Expansion Cross-Validation",
        "",
        "输入：GPT-5.5 Pro 扩码审议、Claude Opus 4.7 Cowork 扩码审议、Codex 五题回源核查。",
        "",
        "## 结论",
        "",
        "- 双模型共同允许新增 1 个核心 code：`CODE_COWORK_008`，但采用 GPT+Codex 更保守的裁剪支撑集，删除 `CC0143` 与 `RECOVER_2026_西城_二模_18_2` 的核心支撑。",
        "- 双模型共同允许修订 4 类 existing code：`CODE_COWORK_001`、`CODE_COWORK_002`、`CODE_COWORK_007`、`CODE_COWORK_004/006`。",
        "- 五题 P0 atom patch 必须先落 canonical atom 层：`CC0011`、`CC0019`、`CC0061`、`CC0254`、`RECOVER_2026_房山_一模_17_1`。",
        "- `CC0276`、4 道 reference_only、`CC0025`、`CC0200` 和其余单题/宽口径 transfer 行不进入核心 codebook，只保留开放容器或备忘。",
        "- `CC0364` 仍需切分巨型 rubric atom，切分前只能算 source_check_needed。",
        "",
        "## 比较表",
        "",
        "| comparison_id | GPT | Claude | decision | needs_source_check | reason |",
        "|---|---|---|---|---|---|",
    ]
    for r in comparisons:
        md.append(
            f"| {r['comparison_id']} | {r['gpt_observation_id']} | {r['claude_observation_id']} | {r['decision']} | {r['needs_source_check']} | {r['reason']} |"
        )
    md.extend([
        "",
        "## 下一步门槛",
        "",
        "1. 先按 `source_check_needed_after_expansion.csv` 完成 P0 atom patch。",
        "2. 再生成扩码后的 codebook v1-expansion-draft 与 evidence map。",
        "3. 再重跑全 65 题压测；压测前仍不得写 framework_v2 或最终宝典。",
        "",
    ])
    (OUT_DIR / "codebook_expansion_after_cowork_sourcecheck_comparison.md").write_text("\n".join(md), encoding="utf-8")

    print(f"Wrote {comparison_csv}")
    print(f"GPT TSV rows: {len(gpt_rows)}")
    print(f"Claude decision rows: {len(claude_rows)}")
    print(f"Comparison rows: {len(comparisons)}")
    print(f"Accepted/revise rows: {len(accepted)}")
    print(f"Rejected/open rows: {len(rejected)}")
    print(f"Source-check rows: {len(source_check)}")


if __name__ == "__main__":
    main()
