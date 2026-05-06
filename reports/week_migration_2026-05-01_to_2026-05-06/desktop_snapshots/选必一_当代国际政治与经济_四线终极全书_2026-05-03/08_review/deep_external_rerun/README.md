# 选必一深度外部审稿补跑说明

time: 2026-05-04 09:57 CST
status: prepared_for_real_external_review

## 为什么补跑

用户指出上一轮最终阶段 GPT-5.5 Pro 和 Claude Opus 4.7 Adaptive 的参与过于验收化，外部模型没有充分承担深度压力测试和教学成品化职责。本目录用于补跑这一环。

本轮补跑不重跑源提取，不覆盖旧终稿，不把刚才误投/误点语音的网页尝试计入有效证据。

## 文件说明

- `artifact_for_external_review_选必一学生讲义_20260504.md`：从正式交付 Markdown 复制出的外审附件，供 GPT/Claude 审读。
- `gpt55_deep_external_review_prompt_20260504.md`：投给 GPT-5.5 Pro 的深度内容压力测试提示词。
- `claude_opus_deep_teaching_prompt_20260504.md`：投给 Claude Opus 4.7 Adaptive 的教学成品化审稿提示词。
- `external_submission_manifest_20260504.md`：真实外部提交时逐项勾选，防止再次串线程。
- `external_response_capture_template_20260504.md`：GPT/Claude 回复粘回本地后的保存模板。
- `local_decision_and_patch_log_20260504.md`：Codex 本地裁决、返修、Governor/Confucius 回归记录。

## 操作硬规则

1. 只在用户确认的正确 GPT/Claude 对话窗口投喂。
2. 投喂前确认输入框内没有残留文字，且没有打开语音/麦克风模式。
3. 如果网页焦点不确定，停止，让用户手动粘贴 prompt 和附件。
4. 外部模型只提供审稿建议，不能替代本地证据裁判。
5. 任何 substantive 修改都必须由 Codex 回到本地终稿、核查索引或既有证据台账裁决后再进入学生稿。
6. 如果补跑发现必须修改正文，修改后重新跑 Governor、Confucius、Markdown 清洁检查、DOCX/PDF 生成或可用 fallback QA。
