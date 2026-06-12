# GitHub 同步说明 2026-06-12

本目录用于把“选必三思维宝典”迁移到 GitHub，方便另一台机器直接 `git pull` 后接手。

## 最终身份

用户此前明确指出的最终版 PDF 已放在：

- `成品/用户指定最终PDF/选必三思维宝典-飞哥正志讲堂.pdf`

原始来源路径：

- `/Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/2c0a1a14-78ce-4ddc-8f72-9d4f74dbff6e/703c2d6a-ade6-4ee8-94a4-92b2abb47bf1/local_f5632364-0fab-4ac5-8862-2f6834daf6a2/outputs/选必三思维宝典-飞哥正志讲堂.pdf`

该 PDF 的 SHA256：

- `ba830703c41a587675b525cdbbe0d082a5c91d59beee46fa1f3e8f70c31935fb`

## 可编辑对照

可编辑 Word 和旧同步 PDF 放在：

- `成品/可编辑Word与旧同步对照/选必三思维宝典-飞哥正志讲堂.docx`
- `成品/可编辑Word与旧同步对照/选必三思维宝典-飞哥正志讲堂_旧同步PDF_20260605.pdf`

注意：旧同步 PDF 与“用户指定最终 PDF”的哈希不同。接手时若只需要最终展示版，以 `成品/用户指定最终PDF/` 为准；若需要继续改 Word，则从可编辑 Word 对照入手，并重新导出新 PDF。

## 控制文件

本包保留两轮关键控制记录：

- `00_control/source_control/25_watermark_final_pair_20260605/`：水印版最终对照，记录 81 页、无空白页、目录链接核验等。
- `00_control/source_control/27_formal_rubric_reaudit_after_haidian_20260605/`：来源边界回查与收口，记录后续删除未锁定青海组、修正题源和学生版风险词清零等。

## 未同步内容

未同步 Claude 输出目录里的大量 `preview/` 截图、探针图片和页面缓存。它们是本地排版缓存，不是跨机接手必需文件。

## 接手顺序

1. 先打开 `成品/用户指定最终PDF/选必三思维宝典-飞哥正志讲堂.pdf` 确认最终展示版。
2. 若要继续改稿，再打开 `成品/可编辑Word与旧同步对照/选必三思维宝典-飞哥正志讲堂.docx`。
3. 改稿前先读 `00_control/source_control/27_formal_rubric_reaudit_after_haidian_20260605/reports/SOURCE_BOUNDARY_REAUDIT_20260605.md`。
