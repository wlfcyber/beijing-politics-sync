# PHILOSOPHY_FORMAT_V12_CHOICE_LABEL_AND_QTITLE_PATCH_20260526

patch_time: 2026-05-26T09:41:35+08:00

verdict: `LOCAL_V12_CHOICE_LABEL_AND_QTITLE_PATCH_APPLIED_NOT_FINAL`

## 触发问题

本轮继续按“完全对齐哲学宝典”自审，发现两个前台不够像哲学宝典的问题：

1. 学生正文标题和引用仍保留工作流式 `Q19(2)`、`Q20` 标签。哲学宝典正文更接近“第16题第（2）问”这种自然题号，而不是审计索引号。
2. 推理选择题虽已收录完整题干和选项，但标签写成 `【完整题干与选项】`，不符合用户原计划中“完整题干、完整选项、答案、正确理由、诱人错项和错因”分栏展示要求。

## 本轮修补

- 思维候选稿与推理候选稿正文中的 `Qn` / `Qn(m)` 工作标签统一改为 `第n题` / `第n题第（m）问`。
- 推理册 36 道选择题全部拆分为：
  - `【完整题干】`
  - `【完整选项】`
  - `【答案】`
  - `【材料触发点】`
  - `【为什么能想到】`
  - `【正确理由】`
  - `【诱人错项和错因】`
- 重建两本 DOCX，经 Microsoft Word 更新字段并重新导出 PDF。
- Word 保存后再次归一化 DOCX 目录样式，维持哲学宝典式 `TOC1/TOC2`，避免回退为 `TOC11/TOC21`。

## 校验结果

- 思维 Markdown：`Q` 工作标签 0；中文题号引用 59。
- 推理 Markdown：`Q` 工作标签 0；中文题号引用 119；`【完整题干】=36`，`【完整选项】=36`，`【完整题干与选项】=0`。
- 思维 DOCX：`Q` 工作标签 0；`TOC1=4 / TOC2=15 / TOC11=0 / TOC21=0`；`PAGEREF=19`。
- 推理 DOCX：`Q` 工作标签 0；`【完整题干】=36`，`【完整选项】=36`；`TOC1=8 / TOC2=61 / TOC11=0 / TOC21=0`；`PAGEREF=69`。
- PDF 页数：思维 35 页，推理 54 页。

## 视觉 QA 说明

初始 `sips` 渲染 PDF 时出现黑底，是 macOS 对透明 PDF 背景的缩略图渲染假象；同页用 Quick Look 渲染为白底，正文可读。因此本轮正式视觉 QA 采用 Quick Look 白底截图：

- `08_visual_qa/V12_CHOICE_LABEL_AND_QTITLE_QUICKLOOK_CONTACT_SHEET_20260526.png`
- `08_visual_qa/V12_CHOICE_LABEL_DETAIL_QUICKLOOK_20260526.png`

## 继续阻断

- GPT Pro 真实审查仍为 `real_call_pending / blocked_advisor`。
- Claude 最新真实 verdict 仍是 V9 `CONDITIONAL_PASS`，不是 `PASS`。
- V12 是本地前台格式与选择题展示修补，不等于最终外审通过。
