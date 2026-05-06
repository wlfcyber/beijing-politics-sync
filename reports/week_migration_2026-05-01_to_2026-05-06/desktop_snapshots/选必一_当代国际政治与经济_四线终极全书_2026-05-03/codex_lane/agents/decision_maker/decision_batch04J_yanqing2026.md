# Decision: Batch04J 2026延庆一模 Next Step

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex A / Decision Maker

Scope: 只裁决 Batch04J 下一步；不改 fusion、student、delivery 文件；不宣布最终成品。

## Status

Batch04J `2026延庆一模 Q19(2)` 已进入 Codex A prelim candidate fusion。当前证据强度高于 Batch04I：`细则.docx` 是 P0 formal scoring，给出明确 8 分结构；原卷 PDF 已视觉核读 page 6-7，完整设问稳定。

当前仍未闭合：

- `COVERAGE_MATRIX.csv` 仍为 `batch04J_candidate_pre_ab_review / claudecode_batch04J_running / pending / pending`。
- `screen -ls` 仍显示 `xuanbiyi_claudecode_batch04J_20260503` detached。
- 尚未见 ClaudeCode B 的 Batch04J entries / matrix / conflicts 文件完成产出。

## 三选一裁决

下一步不是直接继续下一套，也不是空等 ClaudeCode B；裁决为：

**先做 Patcher 窄补丁返修清单，同时等待 ClaudeCode B 完成。Batch04J 最终闭合必须等 B 线退出或快照确认后再做 A/B closure。**

允许并行：

- Patcher 先审 `fusion/scoring_atom_table_batch04J_yanqing2026_prelim.csv`、`merge_register_batch04J_yanqing2026_updates.md`、manual evidence notes 的证据和输出形态。
- Codex生产可准备 Batch04K 的 source locator，但不得把 Batch04J 写成 closed，也不得改学生稿。

不得现在做：

- 不得直接进入学生正文。
- 不得 coverage close。
- 不得把 ClaudeCode B 未完成状态解释为已闭合。
- 不得因为 Batch04J 证据较强就跳过 Patcher/Governor。

## 输出形态检查

用户刚纠正的最终展示形态是：

`完整设问 -> 设问触发 -> 材料触发 -> 框架落点 -> 答题点自身积累 -> 答案句变体`

当前 Batch04J 状态检查：

1. `完整设问`
   - 已在 manual evidence notes 和 worker triage 中稳定存在。
   - 但 fusion atom CSV 没有单独字段承载完整设问；后续进入学生稿前必须从 evidence notes 拉入。

2. `设问触发`
   - worker triage 已写出：`理论逻辑` 问合作为什么成立，`价值意蕴` 问实践创造什么治理/秩序价值。
   - atom CSV 中尚未显式落列；Patcher 需要求后续 shape supplement 保留。

3. `材料触发`
   - atom CSV 有 `material_trigger_fusion`。
   - 但部分表述仍是后台口径，如 `材料中...`、`材料说...`；进入学生展示前必须改成自然卷面逻辑，避免后台制作语气。

4. `框架落点`
   - merge register 已有 Framework Landing 表。
   - 需要保留主桶与交叉引用关系：理论、时代背景/经济全球化、政治多极化、中国，不得把交叉引用误写成多重频次。

5. `答题点自身积累`
   - merge register 已有同核心合并方向。
   - 但还需要在补丁审查中明确每个点的“已有核心 + 本题新增表述”：例如共同利益与正确义利观分功能积累，HMC 是正式评分点，中国方案/公共产品属性只作表达积累。

6. `答案句变体`
   - atom CSV 目前每个 atom 只有一个 `answer_sentence_fusion`。
   - 后续若进入学生形态，需补为“可直接写的一条主句 + 可替换表达/变体”，不能只复制后台 atom 句。

结论：Batch04J 证据可以进入 A/B review，但输出形态未达到最终学生展示要求；必须先由 Patcher 形成 shape-fix 要求，不能直接放入学生稿。

## Patcher/Governor Gate

Patcher 必查：

- `YQ26-01` 中 `共同利益`、`维护国家利益`、`正确义利观` 是否分功能积累，而不是合成空泛合作逻辑。
- `YQ26-02` 中 `时代主题 / 经济全球化趋势` 是否作为同一历史潮流角度，不被拆成虚假两个必答频次。
- `YQ26-03` 必须保留完整 `共商共建共享的全球治理观`。
- `YQ26-04` 必须保留完整 `相互尊重、公平正义、合作共赢的新型国际关系`。
- `YQ26-05` 中 `人类命运共同体` 是正式评分点，`具有公共产品属性的中国方案` 只作答案表达积累。
- final/display shape 必须满足六段结构，且不得出现 backend labels、source paths、candidate、atom、guard、model names、audit vocabulary。

Governor 只可在 B 线完成后裁定：

- `PASS_AFTER_AB_REVIEW`
- `PASS_WITH_FIXES`
- `BLOCK`

不得裁定 final pass。

## Student Docs

学生稿、按题视图、六桶索引、Word/PDF、FINAL_ACCEPTANCE、coverage close 全部继续阻断。Batch04J 当前只能是 `prelim_candidate / shape_fix_pending / B_review_pending`。

## Next Batch After Closure

Batch04J 完成 B 线 A/B closure 与 Patcher/Governor 后，下一批建议进入：

`Batch04K 2026房山一模 source-reverify`

理由：

- 2026一模仍是高权重补遗源。
- 本地源清单已有 `2026房山一模` P0 细则 `SRC_7301f6d3c6e2` 与 P3 试卷 `SRC_0e98e571e5b0`。
- 旧视觉页或旧 rerun 只能后置比对，必须回原始细则/试卷重核。

后备顺序：`2026石景山一模` -> `2026丰台期末`。`2026石景山期末` 仍全模块排除，不得误回补。
