# GPT Pro 网页版状态

## 结论

GPT Pro 必须使用 ChatGPT 网页版，不能用 `multi_agent_v1` 或 API 子智能体替代。

## 当前状态

- 已生成网页版审核包：`04_review_packages/GPTPRO_WEB_BATCH_*.md`
- Chrome 扩展一开始能列出已有 ChatGPT 标签页，但新开 `chatgpt.com` 后扩展连接断开。
- 按 Chrome 技能规则重试连接一次，仍显示 `Browser is not available: extension`。
- 2026-05-23 本机复查：Chrome 正在运行，Codex Chrome Extension 在 `Profile 1` 已安装且启用，Native Messaging Host 配置正确。
- 但扩展通信仍不可用。按 Chrome 技能规则，下一步需要用户确认是否允许打开新的 Chrome 窗口后再重试；用户已准备睡觉，本轮不越权操作。
- 因此本轮不能把 GPT Pro 网页端审核写成已完成，只能记录为 `WAITING_FOR_WEB_GPTPRO_REVIEW`。

## 处理原则

- 不把非网页版 GPT 子智能体结果计入验收。
- 不用 API/子模型冒充网页版 GPT Pro。
- 后续只接受从 ChatGPT 网页端复制回来的审查意见，或在 Chrome 扩展恢复后由 Codex 操作网页端完成。
