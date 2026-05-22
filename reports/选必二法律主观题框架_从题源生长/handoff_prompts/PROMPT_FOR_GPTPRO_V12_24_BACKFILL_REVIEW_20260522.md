# 给 GPT Pro 的审核 prompt：v12_24_question_backfill

你现在是“选必二《法律与生活》主观题框架从题源生长工程”的外部总审稿人 GPT Pro。

请只审核我上传的 v12 包，不要重新发明框架，不要扩大语料，不要进入最终宝典写作。

## 当前事实基准

当前唯一语料仍然是 boundary_patched_20260519 的 53 道主观题：

- 37 道 PASS
- 11 道 PASS_RECOVERED
- 5 道 OPEN_OR_REFERENCE

v11.1 已经通过的是：

`V11_1_WRITTEN_CHAIN_PATCH_PASS`

但它不是最终宝典。当前阶段是：

`v12_24_question_backfill`

目标是处理 v11.1 中 24 道“待回源确认”题。

## 本轮 v12 的 Codex 产出

请重点审核这些文件：

1. `v12_24_question_backfill/01_24题待回源清单.md`
2. `v12_24_question_backfill/01_24题待回源清单.csv`
3. `v12_24_question_backfill/source_lock_cards_index.csv`
4. `v12_24_question_backfill/source_lock_cards/*.md`
5. `v12_24_question_backfill/02_24题回填题链.md`
6. `v12_24_question_backfill/02_24题回填题链.csv`
7. `v12_24_question_backfill/03_all_53_question_chains_v12.md`
8. `v12_24_question_backfill/03_all_53_question_chains_v12.csv`
9. `v12_24_question_backfill/04_无法回填或降级清单.md`
10. `v12_24_question_backfill/04_无法回填或降级清单.csv`
11. `v12_24_question_backfill/05_upper_strong_triage_framework_v12_patch.md`
12. `v12_24_question_backfill/06_true_coverage_matrix_v12.md`
13. `v12_24_question_backfill/06_true_coverage_matrix_v12.csv`
14. `v12_24_question_backfill/07_v12_acceptance.md`

包中也附有 v11.1 对照文件，供你比较 v12 是否真正修补了待回源题。

## Codex 自报状态

Codex 当前自报：

- 24 题待回源清单已生成。
- 24 张 source lock card 已生成。
- 18 题判定为可回填，并写入 v12 回填题链。
- 6 题判定为无法可靠回填/待用户确认，未放入学生正文伪装完成。
- v12 的 `03_all_53_question_chains_v12` 当前只有 47 道已锁源题。
- v12 验收结论写为 `CONDITIONAL_PASS`，不是最终 PASS。
- 未生成最终宝典，未生成 DOCX，未写 TASK_COMPLETE。

6 道未回填题：

1. `CC0251_2026_丰台_一模_20`
2. `CC0276_2026_房山_二模_17`
3. `CC0277_2026_房山_二模_18`
4. `CC0317_2026_海淀_期中_18`
5. `CC0318_2026_海淀_期中_18_2`
6. `CC0319_2026_海淀_期中_19`

## 禁止你做的事

1. 不得扩大到 65/70。
2. 不得纳入 pending 三题：
   - `CC0094_2025_东城_期末_19_3`
   - `CC0259_2026_丰台_期中_19`
   - `CC0118_2025_丰台_期末_18_2`
3. 不得让 OPEN_OR_REFERENCE 支撑核心框架。
4. 不得把当前 v12 直接说成最终宝典完成。
5. 不得用“应该可以”替代逐题核查。
6. 不得把参考答案、评分说明、设问要素、讲评分析当成学生正文材料。

## 你的审核任务

请你按 P0/P1/P2 审核。

### A. 总体判定

请只从下面三个结论中选一个：

- `V12_24_BACKFILL_PASS`
- `CONDITIONAL_PASS`
- `FAIL`

并说明是否允许进入下一步。

下一步只能是以下之一：

- 继续找 6 道缺源题
- 允许基于 47+6降级状态进入阶段性整合
- 不允许继续，必须返工 v12

### B. 审核 24 题清单

检查：

1. 24 题是否列全。
2. 分组 A/B/C 是否合理。
3. 6 道无法回填题是否确实应移出学生正文。
4. 有没有本应回填却被 Codex 过早放弃的题。

### C. 审核 source lock cards

逐题检查：

1. 是否真的有原设问。
2. 是否真的有原材料核心。
3. 是否有答案/细则/评标/明确给分口径。
4. 是否仍属于选必二法律主观题。
5. 是否存在必修三/经济/逻辑等模块边界风险。
6. 是否有参考答案或讲评分析混入材料。

### D. 审核 18 道回填题链

逐题检查：

1. 主入口是否只有 1 个。
2. 副入口是否最多 2 个。
3. 主材料触发是否最多 3 个。
4. 材料事实是否是真材料，不是答案/细则/分析说明。
5. “法律翻译”是否贴合选必二法律语言。
6. “细则喜欢的话”是否没有变成评分说明原文。
7. 答案骨架是否学生可写。
8. 飞哥想说是否抓住本题本质。

### E. 审核 v12 的 53 题全量题链

重点看：

1. 是否真的清除了所有“待回源确认”占位。
2. 47 题正文是否没有把 6 个未锁源题伪装完成。
3. 6 题移出正文后，是否可以暂时接受为阶段性 conditional。
4. 是否有材料错配、题源错配、触发错配。
5. 是否有 v10 那种万能合同、万能纠纷解决、万能意义价值回流。

### F. 审核覆盖矩阵

检查：

1. 是否再次虚高。
2. OPEN_OR_REFERENCE 是否没有单独支撑核心点。
3. 新增框架点是否有 formal 或 PASS_RECOVERED 支撑。
4. 题数统计是否和 47 已锁源正文、6 未锁源清单一致。

## 输出格式

请按以下格式输出：

1. 总判定：
2. 是否允许进入下一步：
3. P0 必修问题：
4. P1 重要问题：
5. P2 可后修问题：
6. 18 道回填题逐题审核表：
   - question_id
   - 是否通过
   - 问题
   - 修复建议
7. 6 道无法回填题逐题裁断：
   - question_id
   - 是否同意移出正文
   - 是否建议继续找源
   - 需要什么原始文件
8. 对 v12 验收报告的评价：
9. 给 Codex 的下一步指令：

请直说。不要客气。如果你发现 v12 仍然垃圾化、泛化、错配，请直接判 FAIL。
