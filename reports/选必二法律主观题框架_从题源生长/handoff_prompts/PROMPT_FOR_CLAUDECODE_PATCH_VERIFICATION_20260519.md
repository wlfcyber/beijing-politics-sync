# Claude Code B Patch Verification Prompt

你现在继续作为“选必二《法律与生活》主观题框架从题源生长工程”的 Claude Code B。

你上一轮对 66 题包的裁决是 `FINAL_JUDGMENT: FAIL`，并列出 hard-fix list。Codex 已按你的报告生成了一个修正后的 65 题包。你本轮不要重新全量扫源，只做补丁落实校验。

工程根目录：

`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长`

上一轮审计输出：

`04_merge_audit/claudecode_suite_exhaustion_audit_20260519/`

修正后语料包：

`04_merge_audit/suite_exhaustive_claudecode_corrected_20260519/`

修正后 reasoner packet：

`05_reasoner_packets/suite_exhaustive_claudecode_corrected_20260519/`

输出目录：

`04_merge_audit/claudecode_suite_exhaustion_audit_20260519/`

请核查：

1. 漏题 `2026 朝阳 期末 Q18(1)` 是否已补为核心题。
2. `CC0051_2024_海淀_期中_21_1` 是否已从核心移出并转 boundary。
3. `RECOVER_2024_顺义_二模_17` 是否已从核心移出并转 boundary。
4. `CC0311_2026_海淀_二模_18` 是否已拆成只保留法律小问 `18_2`，逻辑小问不再在核心中。
5. 7 个错误标为期中的 2026 期末题是否已改为期末：
   - CC0244 / CC0245 东城
   - CC0317 / CC0318 / CC0319 海淀
   - CC0353 西城
   - CC0364 通州
6. suite 矩阵是否拆出 2026 朝阳期末、2026 海淀期末，且真期中无法律题不再被期末题污染。
7. 修正后核心题数、evidence_level 统计是否自洽。
8. material/ask/rubric atoms 是否仍有指向被删除核心题的 question_id。
9. rubric atoms 的 related_material_atom_ids 是否存在明显断链。
10. 剩余 OCR/source blockers 是否仍然阻断把修正包交给 GPT-5.5 Pro / Claude Opus 做“开放观察”。如果只是保留为风险，请说明；如果仍阻断，请列 hard blocker。

请输出：

`claudecode_patch_verification_report.md`

报告开头必须是：

- `PATCH_VERIFICATION: PASS`
- 或 `PATCH_VERIFICATION: CONDITIONAL_PASS`
- 或 `PATCH_VERIFICATION: FAIL`

并简要列出：

- core_count
- formal_count
- reference_only_count
- still_missing_core_candidates
- still_false_positive_core_ids
- still_stage_mismatch_ids
- remaining_blockers_before_reasoner
- whether corrected packet may be sent to GPT-5.5 Pro / Claude Opus for open observation

终端最后只输出 verification 状态和报告路径。
