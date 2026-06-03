# V29 学生正文回归与 Word 弹窗修补审计

时间：2026-05-26T14:18:00+08:00

verdict: `LOCAL_STUDENT_LANGUAGE_AND_WORD_PROMPT_PATCH_NOT_FINAL`

## 触发原因

V28 的内容修补方向成立，但新增/改写条目把少量教师编辑腔带回了学生正文，例如 `这题`、`这道题`、`单独挂题`、`必须在`、`第一段/第二段`、`第一层/第二层`、`第一步/第二步`。

用户同时反馈 Word 打开时反复询问：“该文档包含的域可能引用了其他文件。是否更新该文档中的这些域?”。仅移除 `w:updateFields` 不够稳，因为目录页码中的 `PAGEREF` 域仍可能触发 Word 安全提示。

## 已修补

- 思维册、推理册学生正文中的编辑腔扫描词清零：`这题`、`这道题`、`单独挂题`、`必须在`、`第一段`、`第二段`、`第一层`、`第二层`、`第一步`、`第二步` 均为 0。
- 两本 Markdown 结构未被破坏：
  - 思维册：H3=65，四标签各 65。
  - 推理册：H3=83，四标签各 83。
- `tools/build_handbook_docs.py` 已将目录页码从 `PAGEREF` 动态域改为静态页码文本，目录标题仍保留内部链接。
- 两个 DOCX 的 `word/document.xml` 已无 `fldChar`、`instrText`、`PAGEREF`；`word/settings.xml` 中 `updateFields` 为 0。
- 目录样式重建后保持哲学宝典式 `toc 1 / toc 2`：`TOC1/TOC2` 存在，`TOC11/TOC21` 为 0。
- 已用 Microsoft Word 正常打开思维 DOCX，未再出现更新域弹窗。

## 边界

- 本修补是本地格式与学生语言补丁，不等于 GPT Pro / Claude 真实 PASS。
- Claude 对 V27 的真实 verdict 仍为 `P2_POLISH`。
- GPT Pro 真实审核仍为 pending。
