# DECISION_LOG

## 2026-05-31

- 本 run 只核查 Claude 修订稿是否被原卷/细则支持；不做风格美化。
- 自动文本匹配只能作为定位辅助；最终 `PASS` 需要题号、设问和细则核心词均可回源。
- 若原文件为扫描 PDF 或文件缺失，状态标为 `BLOCKED_OCR` 或 `BLOCKED_MISSING_SOURCE`，不得用旧稿或记忆替代。
