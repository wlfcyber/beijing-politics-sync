# PHILOSOPHY ALIGNMENT V30 STATIC TOC PAGE FIX

time: 2026-05-26T14:33:00+08:00
verdict: `LOCAL_DOCX_PDF_PATCH_NOT_FINAL`

## Trigger

用户要求 Word 不再反复询问：

> 该文档包含的域可能引用了其他文件。是否更新该文档中的这些域?

V29 为压掉该提示，把目录页码静态化，但复核发现推理宝典目录页码被固化为 `0`。这属于格式功能硬错误：不能用“不弹窗”换取“目录页码失真”。

## Fix

- 生成链恢复先写入 `PAGEREF`，让 Word 真实计算目录页码。
- 在 Word 中对推理宝典执行全选并更新域，推理目录页码从 `0` 更新为真实页码 `5-49`。
- 保存后再移除 `PAGEREF` 域外壳，只保留 Word 已算出的普通页码文本。
- 扩展 `tools/build_handbook_docs.py` 的 `freeze_pageref_fields()`，兼容 Word 保存后带 `w:rPr`、`w:noProof` 的复杂字段结构。
- `w:updateFields` 继续保持为 0，避免再次触发用户反馈的 Word 更新域弹窗。

## Verification

DOCX XML 检查：

- 思维 DOCX：`fldChar=0`，`instrText=0`，`PAGEREF=0`，`updateFields=0`。
- 推理 DOCX：`fldChar=0`，`instrText=0`，`PAGEREF=0`，`updateFields=0`。
- 两本 DOCX：正文目录样式为 `TOC1/TOC2`，无 `TOC11/TOC21`。

Word 实测：

- 思维 DOCX 用 Microsoft Word 真实打开并关闭，无更新域弹窗。
- 推理 DOCX 用 Microsoft Word 真实打开并关闭，无更新域弹窗。

PDF 文本检查：

- 思维 PDF：29 页，`材料触发点/为什么能想到/答案落点` 各 65。
- 推理 PDF：49 页，`材料触发点/为什么能想到/答案落点` 各 83。
- 推理 PDF 目录页无以 `0` 结尾的目录页码行，目录页码为真实页码。

## Status

V30 只修复 Word 文件体验和目录页码一致性。不得据此写 `PASS`、`TASK_COMPLETE` 或 `最终版`。

仍需否决最终声明：

- GPT Pro 真实审核仍未完成。
- Claude verdict 仍为 `P2_POLISH`，不是 PASS。
