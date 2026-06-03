# Coverage Repair Overlay

time: `2026-05-26T05:31:30+08:00`

verdict: `TWO_COVERAGE_RESIDUES_REPAIRED_BY_CODEX_OVERLAY_NOT_YET_APPLIED_TO_STUDENT_BODY`

本 overlay 只修正 ClaudeCode B 线 `COVERAGE_MATRIX.csv` 中两处 `待Codex回源细化` 残留的融合口径。它不直接改写 B 线原始文件，保留 B 线原件作为外部 lane 输出；后续 Codex 融合以本 overlay + 原 source lock + 候选正文为准。

## Repair 1 — BCV0083 / Q0083

source row:

`BCV0083,2024海淀一模,Q0083,main_question,thinking,thinking_main,body,A-formal,思维(待Codex回源细化),...`

Codex repair:

- decision: `body`
- handbook_target: `thinking_main`
- repaired_node: `辩证思维 / 分析与综合`
- source basis:
  - `00_control/QUESTION_COVERAGE_MATRIX.csv` 第 Q0083 行：正式细则锁定“分别分析三地特色、综合优势互补、二者对立统一服务协同发展”
  - `06_candidate_audit/THINKING_GATE_CLEAR_BATCH6_20260526.md`：Q0083 已按 A-formal 清理京津冀分析与综合条目门禁
  - `05_candidate_md/选必三_逻辑与思维_思维宝典_哲学完全对齐候选稿.md`：正文已写入 `2024海淀一模 Q17(2)` 的分析与综合四字段
- fusion instruction:
  - 以候选 MD 的“分析与综合”写法为主；
  - B 线 `T-2024-HAIDIAN-1MO-Q17-2` 中“整体性 + 动态性”只可作为审计参考，不能替代正式细则中的“分析与综合”主节点；
  - 学生正文保留 `材料触发点 / 设问 / 为什么能想到 / 答案落点` 四字段，不写 source lock。

## Repair 2 — BCV0084 / Q0084

source row:

`BCV0084,2024朝阳二模,Q0084,main_question,thinking+reasoning,reasoning_main,body,A-formal,推理+思维交叉(待Codex回源细化),...`

Codex repair:

- decision: `body`
- handbook_target: `reasoning_main`
- repaired_reasoning_node: `类比推理 / 填空式主观题`
- repaired_thinking_cross_mount: `辩证思维 / 动态性`
- source basis:
  - `00_control/QUESTION_COVERAGE_MATRIX.csv` 第 Q0084 行：原卷和 2024 朝阳二模主观题阅卷总结锁定 `①动态性 ②类比`
  - `06_candidate_audit/REASONING_MAIN_PROMPT_LOCK_BATCH1_20260526.md`：题面设问锁定为“生生之宇宙观体现了辩证思维的①特征。人效法天地之德体现的推理类型是②推理。”
  - `06_candidate_audit/CANDIDATE_GATE_CLEAR_BATCH3_20260526.md`：推理侧“效法天地之德”触发类比推理
  - `06_candidate_audit/THINKING_GATE_CLEAR_BATCH5_20260526.md`：思维侧“生生不息、日新、变易、革新、成长、展开 -> 动态性”
  - 候选 MD 已分别写入思维册动态性条目和推理册类比推理条目
- fusion instruction:
  - 推理册保留 `2024朝阳二模 Q19(1)` 于 `类比推理` 节点；
  - 思维册保留同题于 `辩证思维 / 动态性` 节点；
  - 不再使用“推理+思维交叉(待Codex回源细化)”作为正文或审计节点名；
  - 两册同题复挂时必须分清题目功能：第一空服务思维动态性，第二空服务推理类比。

## Repair 3 — BCV0084T / Q0084(thinking-mount)

source row:

`BCV0084T,2024朝阳二模,Q0084(thinking-mount),...,thinking_main,body,A-formal,思维(交叉挂载),...`

Codex repair:

- decision: `body`
- handbook_target: `thinking_main`
- repaired_node: `辩证思维 / 动态性`
- fusion instruction: 与 Repair 2 的 thinking_cross_mount 合并，不另建模糊“交叉挂载”节点。

## Gate Effect

After applying this overlay in Codex fusion:

- ClaudeCode B 线 coverage 的两处 `待Codex` 不再作为融合阻断；
- 原始 B 线文件仍保留，供外审查看它曾有残留；
- 学生正文必须以 repaired node 为准；
- 下一步可以进入 `CODEx_BLINE_FUSION_DIFF`，但仍需处理 B-choice-signal / 占位 choice body。
