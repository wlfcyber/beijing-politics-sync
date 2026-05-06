# 外部模型状态记录：选必一教学返工版

## Claude Opus 4.7 Adaptive

- 状态：已使用真实 Claude 桌面端，同一 `学生文档审稿意见` 对话，模型显示 `Opus 4.7 Adaptive`。
- 本轮标记：`XBY1-TEACHING-REBUILD-REVIEW-20260504`。
- 原始回复：`10_teaching_rebuild_20260504/02_external/claude_opus_teaching_rebuild_response_20260504.md`。
- 核心裁定：Claude 认为旧版相对哲学/选必三标杆的最大差距是组织主轴仍偏题号驱动，应改为“知识点驱动 + 按题精练/速查”。

## GPT-5.5 Pro

- 状态：本轮教学返工没有再次安全提交新的 GPT 网页请求。
- 原因 1：Computer Use 无权操作 ChatGPT 桌面 App，返回 `Computer Use is not allowed to use the app 'com.openai.chat' for safety reasons.`。
- 原因 2：本运行目录的 `00_control/CROSS_THREAD_TOOL_GUARD.md` 明确要求 Safari/ChatGPT 只能在安全空窗使用；当前没有新的安全空窗确认，所以没有触碰 Safari，避免再次串入其他线程。
- 处理：不把本轮 GPT 记为 PASS；沿用此前已捕获的 GPT deep/final/strict-4 审稿作为历史参考，本轮新增结构返工由 Claude 教学意见 + Codex 本地证据/结构 QA/Governor/Confucius 补闭合。

## 边界

- Claude/GPT 均不是证据裁判。所有踩分词、框架归类、题目来源、排除项仍以本地源文件、融合表、教师索引和 Codex/Governor 裁决为准。
