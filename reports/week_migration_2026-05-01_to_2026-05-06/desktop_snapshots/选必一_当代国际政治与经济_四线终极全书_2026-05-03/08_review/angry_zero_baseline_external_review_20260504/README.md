# Angry Zero-Baseline External Review

目的：回应用户关于 Confucius 是否真实闭环的追问，在既有 Confucius artifact-only gate 之外，再让真实 GPT-5.5 Pro 与 Claude Opus 4.7 Adaptive 模拟“聪明但零基础且满腔怒火的高三生”复读最终 Word/讲义，提出修改意见，并由 Codex 本地裁决后返修。

外审对象：

- `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.docx`
- 同源 Markdown：`09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md`

闸门：

- GPT 必须进入正确 ChatGPT Pro 选必一/Opus4.6 vs 4.7 对话后再发送。
- Claude 必须进入 Claude 桌面端 `学生文档审稿意见` 选必一专用对话后再发送。
- 若 UI 漂移到选必二或其他线程，停止发送并记录 blocker。
