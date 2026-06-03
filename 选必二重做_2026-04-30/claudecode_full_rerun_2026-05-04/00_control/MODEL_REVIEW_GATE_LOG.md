# 模型审稿 Gate 日志（MODEL_REVIEW_GATE_LOG）

| Gate | 模型 | 模式 | 当前状态 | 证据文件 | 备注 |
| --- | --- | --- | --- | --- | --- |
| Strategic Pressure Test | GPT-5.5 Pro | 网页端 | `real_call_pending` | `gpt55_review/GPT55_PRO_REVIEW_PROMPT.md` | 本生产线 B 不能完成真实外部调用；prompt 已生成，待用户人工驱动。 |
| Teaching-Text & Learnability | Claude Opus 4.7 Adaptive Thinking | 网页端 | `real_call_pending` | `opus47_review/CLAUDE_OPUS_47_ADAPTIVE_REVIEW_PROMPT.md` | 同上。 |
| Cross-Critique GPT ↔ Claude | 双向交叉 | 网页端 | `real_call_pending` | （依赖前两个 gate 完成后产出） | 把 GPT 原始建议交给 Claude 反驳、Claude 建议交给 GPT 反驳。 |
| 本地证据裁决 | Codex / ClaudeCode lane B | 本地 | `pending_after_external` | `fusion/` | 仅对照外部建议是否能回到本地细则；不能则不入正稿。 |

## 不闭环规则（强制执行）
- 任何 `real_call_pending` 未升为 `passed_with_evidence` 之前，最终 Word/PDF 状态必须显式写"外部模型审稿待补"，绝不写"已审"或"PASS"。
- 用户硬规则：除非用户明确豁免该 gate，否则即便 Word 已生成，也不得对外宣称已闭合。
