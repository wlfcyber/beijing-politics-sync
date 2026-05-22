# Codebook Expansion Cross-Validation

输入：GPT-5.5 Pro 扩码审议、Claude Opus 4.7 Cowork 扩码审议、Codex 五题回源核查。

## 结论

- 双模型共同允许新增 1 个核心 code：`CODE_COWORK_008`，但采用 GPT+Codex 更保守的裁剪支撑集，删除 `CC0143` 与 `RECOVER_2026_西城_二模_18_2` 的核心支撑。
- 双模型共同允许修订 4 类 existing code：`CODE_COWORK_001`、`CODE_COWORK_002`、`CODE_COWORK_007`、`CODE_COWORK_004/006`。
- 五题 P0 atom patch 必须先落 canonical atom 层：`CC0011`、`CC0019`、`CC0061`、`CC0254`、`RECOVER_2026_房山_一模_17_1`。
- `CC0276`、4 道 reference_only、`CC0025`、`CC0200` 和其余单题/宽口径 transfer 行不进入核心 codebook，只保留开放容器或备忘。
- `CC0364` 仍需切分巨型 rubric atom，切分前只能算 source_check_needed。

## 比较表

| comparison_id | GPT | Claude | decision | needs_source_check | reason |
|---|---|---|---|---|---|
| EXP_CMP_001 | DEC_001 | EXP_DEC_001 | merge_keep_trimmed | no | Use the stricter support set: CC0131, CC0206, CC0229, CC0283, CC0319, CC0103. CC0143 is a consumer-fraud counterexample; RECOVER_2026_西城_二模_18_2 stays AI open-container. |
| EXP_CMP_002 | DEC_002 | EXP_DEC_002 | keep | no | Dual-model agreement and formal multi-question support. |
| EXP_CMP_003 | DEC_003|DEC_012 | EXP_DEC_003|EXP_DEC_007 | merge_keep_with_boundary_trim | no | Use patched CC0019 atoms and keep governance-heavy RECOVER_2026_西城_二模_18_3 as open-container only. |
| EXP_CMP_004 | DEC_004 | EXP_DEC_004 | split_then_keep | no | Two sub-patterns prevent over-broad remedies/procedure wording and reduce 必修三化 or民诉格式化 risk. |
| EXP_CMP_005 | DEC_005 | EXP_DEC_005 | keep_pending_cc0364_split | yes | CC0238 and RECOVER_2026_西城_二模_18_1 can support limited revision; CC0364 must be split before stronger support is counted. |
| EXP_CMP_006 | DEC_011 | EXP_DEC_006 | patch_before_use | no | Current single atom is too collapsed; patch atoms are source-checked formal evidence. |
| EXP_CMP_007 | DEC_012 | EXP_DEC_007 | patch_before_use | no | Current single atom is too collapsed; patch atoms separate market-economy, contract, judiciary, operator, consumer rewards. |
| EXP_CMP_008 | DEC_013 | EXP_DEC_008 | split_before_use | no | 18(1)(2) are procedure micro-items; only 18(3) can support family-duty/value observations. |
| EXP_CMP_009 | DEC_014 | EXP_DEC_009|EXP_DEC_012 | replace_wrong_atoms | no | Current atoms came from student-problem/teaching-suggestion slides, not scoring atoms. |
| EXP_CMP_010 | DEC_015 | EXP_DEC_010|EXP_DEC_012 | rewrite_alternative_atoms | no | Subject/content/object dimensions are alternative explanations, not cumulative scoring atoms. |
| EXP_CMP_011 | DEC_008 | EXP_DEC_011 | discard_core_open_container | no | High module-boundary risk and single public-policy sample. |
| EXP_CMP_012 | DEC_010 | EXP_DEC_013 | discard_core_reference_only | no | reference_only cannot independently support core codebook nodes. |
| EXP_CMP_013 | DEC_006 | EXP_DEC_014 | open_container_only | no | Single formal sample without repeated pattern. |
| EXP_CMP_014 | DEC_007 | EXP_DEC_015 | open_container_only | no | Single formal sample without repeated pattern. |
| EXP_CMP_015 | DEC_016 | EXP_DEC_016 | open_container_only | no | No stable common minimal judgment or repeated rubric reward pattern. |
| EXP_CMP_016 | DEC_005 | EXP_DEC_017 | source_check_pending | yes | CC0364 is currently one giant atom and must be split before being counted as strong support. |

## 下一步门槛

1. 先按 `source_check_needed_after_expansion.csv` 完成 P0 atom patch。
2. 再生成扩码后的 codebook v1-expansion-draft 与 evidence map。
3. 再重跑全 65 题压测；压测前仍不得写 framework_v2 或最终宝典。
