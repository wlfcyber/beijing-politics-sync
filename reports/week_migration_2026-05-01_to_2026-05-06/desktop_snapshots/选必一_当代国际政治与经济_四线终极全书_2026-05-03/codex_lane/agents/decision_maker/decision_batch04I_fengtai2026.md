# Decision: Batch04I 2026丰台一模 Next Step

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex A / Decision Maker

Scope: 只裁决 Batch04I 下一步；不改总表、不改学生稿、不宣布最终成品。

## Status

Codex A 已处理 `2026丰台一模 Q19` 为 `guarded candidate expression accumulation`。核心原因是 `细则.pptx` slide 41-42 提供试题分析和参考答案段落，但不是可审计的逐点赋分细则。Q18、Q20 保持模块边界排除。当前 `screen -ls` 仍显示 `xuanbiyi_claudecode_batch04I_20260503` detached，Cross-thread guard 继续生效。

## Decision

Batch04I 不能立刻最终闭合。必须等待 ClaudeCode B 明确退出，或由总控保存 B 线当前快照后，再由 Patcher/Governor 做 A/B 差异合闸。

即使 A/B 合闸通过，Batch04I 的最高状态也应是 `candidate_with_guard / expression_accumulation`，不得升级为稳定 P0 逐点频次样本，除非后续发现真正逐点赋分细则。

允许现在做的事：
- Patcher 预读 Codex A 的 `fusion/scoring_atom_table_batch04I_fengtai2026_prelim.csv` 与 `fusion/merge_register_batch04I_fengtai2026_updates.md`。
- 对照 ClaudeCode B 已写出的 `claudecode_lane/progress_batch04I.md`、`batch04I_fengtai2026_entries.md`、`batch04I_fengtai2026_matrix.csv`、`batch04I_conflicts_for_codex.md`。
- 预设冲突清单：B 线 10 个术语原子是否被吸收为表达变体；Codex A 4 个合并原子是否过度压缩；是否有人虚构每短语分值；Q18/Q20 是否保持 excluded。

必须等待的事：
- ClaudeCode B screen 退出或快照确认。
- A/B 差异文件被读取并裁定。
- Patcher 给出 `PASS_AFTER_AB_REVIEW` 或 `FIX_REQUIRED`。
- Governor 给出 `PASS_AFTER_AB_REVIEW`、`PASS_WITH_GUARD` 或 `BLOCK`。

## Student Docs

学生稿、六桶索引、按题视图、Word/PDF、FINAL_ACCEPTANCE、coverage close 全部继续阻断。Batch04I 当前不能进入学生正文，也不能作为“满分四点模板”呈现。

## Next Batch After Closure

Batch04I 闭合后，下一批建议进入 `Batch04J 2026延庆一模 Q19(2) source-reverify`。

理由：
- 2026一模仍是高权重补遗源。
- 本地源清单已有 `2026延庆一模` P0 细则 `SRC_5bf6b7387198` 与 P3 试卷 `SRC_944b03f9c3be`。
- 旧线索中存在 `2026延庆一模_Q19_2` 相关记录，但只能后置比对，必须回原始细则/试卷重核。

后备顺序：`2026房山一模` -> `2026石景山一模` -> `2026丰台期末`。`2026石景山期末` 仍全模块排除，不得误回补。
