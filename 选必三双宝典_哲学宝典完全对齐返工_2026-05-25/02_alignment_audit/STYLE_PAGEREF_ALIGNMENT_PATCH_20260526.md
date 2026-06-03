# STYLE_PAGEREF_ALIGNMENT_PATCH_20260526

verdict: `STYLE_ALIGNMENT_ADVANCED_NOT_FINAL`

## Why This Patch Exists

用户指出两本选必三宝典仍不像哲学宝典。本轮重新以哲学宝典 Word 本体为基准检查，发现当前双宝典仍有两个硬格式差距：

- 哲学宝典目录含真实 `PAGEREF` 页码字段；当前两本上一版只有可见页码与内部链接，`PAGEREF=0`。
- 哲学宝典封面与前置页使用中文黑体、楷体、宋体体系；当前两本上一版统一使用 Arial，Word 气质不一致。
- 哲学宝典开头段落顺序为 `标题/副题 -> 飞哥正志讲堂 -> 前言 -> 目录 -> 正文`，且前言不塞说明性段落；当前两本上一版在前言中加入了判题地图说明，形态更像使用说明。

## Applied Changes

修改文件：

- `tools/build_handbook_docs.py`
- `05_candidate_md/选必三_逻辑与思维_思维宝典_哲学完全对齐候选稿.md`
- `05_candidate_md/选必三_逻辑与思维_推理宝典_哲学完全对齐候选稿.md`

修改内容：

- 封面标题改为同段换行：`标题 -> 副题`，对应哲学宝典首段形态。
- 字体体系改为：标题/目录/一级标题用黑体，讲堂署名用楷体，正文用宋体，西文使用 Times New Roman。
- 页边距改为哲学宝典实测值：上 `1191`、右 `1219`、下 `1134`、左 `1219` dxa。
- 手工目录改为 `toc 1 / toc 2` 段落风格，并为每个目录项加入内部链接和 `PAGEREF` 字段。
- 前言页删除三段说明性“判题地图”，改回哲学宝典式空前言页；判题地图功能保留在各节点五步导引中，不占前置页。

## Current Structural QA

| 项目 | 哲学宝典 | 思维宝典当前 | 推理宝典当前 |
| --- | ---: | ---: | ---: |
| 开头顺序 | 标题/副题 -> 署名 -> 前言 -> 目录 | 已对齐 | 已对齐 |
| 页边距 dxa | 1191/1219/1134/1219 | 1191/1219/1134/1219 | 1191/1219/1134/1219 |
| `PAGEREF` 字段 | 38 | 19 | 8 |
| 内部链接 | 38 | 19 | 8 |
| 书签 | 38 | 19 | 8 |
| TOC 风格 | `toc 1/toc 2` | `toc 1/toc 2` | `toc 1` |
| PDF 页数 | 222+ | 27 | 41 |
| PDF/MD 禁词扫描 | 不适用 | 0 | 0 |

## Visual QA

新增抽样图：

- `08_visual_qa/双宝典_style_pageref_patch_v2_contact_sheet_20260526.png`
- `08_visual_qa/思维宝典_style_pageref_patch_v2_p001.png`
- `08_visual_qa/思维宝典_style_pageref_patch_v2_p002.png`
- `08_visual_qa/思维宝典_style_pageref_patch_v2_p003.png`
- `08_visual_qa/思维宝典_style_pageref_patch_v2_p013.png`
- `08_visual_qa/思维宝典_style_pageref_patch_v2_p027.png`
- `08_visual_qa/推理宝典_style_pageref_patch_v2_p001.png`
- `08_visual_qa/推理宝典_style_pageref_patch_v2_p002.png`
- `08_visual_qa/推理宝典_style_pageref_patch_v2_p003.png`
- `08_visual_qa/推理宝典_style_pageref_patch_v2_p020.png`
- `08_visual_qa/推理宝典_style_pageref_patch_v2_p041.png`

抽样结果：

- 封面页、目录页、正文页、末页均可读；
- 未见黑页、重叠、明显截断、页脚丢失；
- 目录页码已由 Word 更新字段后进入 PDF；
- PDF 文本层未命中后台词、禁词或 B 线污染词。

## Remaining Non-final Gates

- GPT Pro 真实外审仍为 `real_call_pending`。
- Claude 真实外审仍为 `real_call_pending`。
- 本补丁只是继续推进哲学宝典格式对齐，不能写 `PASS` 或 `最终版`。
