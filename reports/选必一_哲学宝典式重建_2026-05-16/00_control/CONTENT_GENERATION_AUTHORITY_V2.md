# 选必一宝典 V2 内容生成权威链

## 用户要求

用户要求主体内容不再采用“Codex 主融合、GPT Pro / Claude 外审”的模式，而改为：

1. Codex 独立生成厚稿。
2. ClaudeCode 独立生成厚稿。
3. GPT Pro 读取两份厚稿后做主融合。
4. Codex 只做证据回查、格式落盘、Governor 校验。
5. Claude Opus 4.7 Adaptive 可在 GPT Pro 融合后做教学化审阅和误用风险审查，但不替代 GPT Pro 主融合。

## 对当前终稿的定性

当前 `06_final_handbook` 终稿已经经过 ClaudeCode 厚稿审阅、GPT Pro 外审、Claude Opus 外审并回写补丁，但其主体生成链不是严格的 V2：

- 主体聚合与终稿生成由 Codex 执行。
- ClaudeCode 参与了批次生产与厚稿审阅，但不是所有最终学生内容都由 ClaudeCode 与 Codex 双线独立厚稿后交给 GPT Pro 主融合。
- GPT Pro 参与了批次和终稿审阅/修改建议，但终稿阶段不是 GPT Pro 主融合权威。

因此当前版只能称为：

> Codex 主体生成与融合，ClaudeCode 参与生产/诊断，GPT Pro 与 Claude Opus 外审补丁回写版。

不能称为：

> Codex + ClaudeCode 双独立厚稿，GPT Pro 主融合版。

## V2 每五题批次必需产物

每个五题批次必须至少留下以下文件，缺一不可：

- `source_packet/BATCH_xxx_SOURCE_PACKET.md`
- `codex_lane/BATCH_xxx_CODEX_INDEPENDENT_THICK_DRAFT.md`
- `claudecode_lane/BATCH_xxx_CLAUDECODE_INDEPENDENT_THICK_DRAFT.md`
- `comparison/BATCH_xxx_CODEX_VS_CLAUDECODE_DIFF.md`
- `gptpro_fusion/BATCH_xxx_GPT_PRO_PRIMARY_FUSION.md`
- `evidence_check/BATCH_xxx_CODEX_EVIDENCE_BACKCHECK.md`
- `governor/BATCH_xxx_GOVERNOR_AUDIT.md`

## GPT Pro 主融合提示词硬约束

提交给 GPT Pro 时，必须明确：

- 你不是审稿员，而是本批次主融合编辑。
- 你必须同时读取 Codex 厚稿与 ClaudeCode 厚稿。
- 你需要逐条决定：保留 Codex、保留 ClaudeCode、综合改写、拆分、合并、驳回。
- 不得新增没有源包支持的术语、细则或材料事实。
- 输出必须是可直接进入学生宝典的融合稿，不只是修改建议。
- 每条融合条目必须保留：术语、设问、细则位置、来源、材料触发、答案句。

## Codex 后处理边界

GPT Pro 融合后，Codex 只能执行：

- 回原始细则和材料核验 GPT Pro 融合稿是否有证据。
- 删除或标记无证据新增内容。
- 将融合稿格式化进六桶宝典。
- 生成 Word/DOCX 并渲染检查。
- 写 Governor 审计。

Codex 不得把 GPT Pro 融合稿重新改成自己的版本，除非有明确证据冲突；所有冲突必须写入裁决日志。
