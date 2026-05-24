# GPT Pro 网页端状态

## 2026-05-24 文件上传尝试

- Chrome 扩展通信：成功，已接管 ChatGPT 网页端标签页。
- ChatGPT 账号状态：页面显示用户为 Pro，并处于“进阶专业”模式。
- 文件上传：失败，错误为 `Not allowed / fileChooser.setFiles failed`。
- 处理：已按 Chrome 插件要求提示用户启用 Codex Chrome Extension 的 file URL access。

## 备用路径

- 不将文件上传失败计入 GPT Pro 审核完成。
- 改用真实 ChatGPT 网页端分批粘贴材料：
  1. 先发任务说明、哲学标杆标准摘要、本地预检。
  2. 再分批发送选必一候选稿目录和高风险桶内容。
  3. 如网页稳定，再继续发送全稿分段或要求 GPT Pro 对已发全量结构做终审。
- 只有收到 GPT Pro 明确 PASS 或 FAIL + 修改意见全文，才可计入模型证据。
