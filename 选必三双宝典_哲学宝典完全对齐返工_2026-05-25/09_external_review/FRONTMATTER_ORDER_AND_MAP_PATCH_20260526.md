# FRONTMATTER_ORDER_AND_MAP_PATCH_20260526

patch_time: 2026-05-26T04:21:06+08:00

verdict: `FRONTMATTER_STRUCTURE_IMPROVED_STILL_NOT_FINAL`

## 本次发现的硬差距

复核哲学宝典本体后确认，哲学宝典的开头顺序是：

1. 封面标题
2. 飞哥正志讲堂
3. 前言
4. 目录
5. 正文一级模块

本 run 生成脚本在上一版中实际输出为：

1. 封面标题
2. 目录
3. 前言
4. 正文一级模块

这属于格式骨架差距，不是普通润色问题。即使正文四标题和五步导引存在，也不能说完全对齐哲学宝典。

## 已做处理

- 修改 `tools/build_handbook_docs.py`：生成顺序改为封面、前言、目录、正文。
- `emit_content` 现在跳过 Markdown 前言和手工目录，只从正文一级模块开始输出。
- 新增 `emit_front_matter`，把 Markdown 中 `## 前言` 与其正文放在目录之前。
- 思维册目录移除 `前言` 条目，更接近哲学宝典目录从一级模块开始的阅读秩序。
- 思维册目录页码按新 PDF 分页重新校正：
  - `科学思维统领下的复合方法`：第 5 页
  - `四、创新思维`：第 17 页
  - `思路新、方法新、结果新`：第 17 页
- 两本前言各补入一段学生判题地图，作为从材料/题干进入框架的整本入口。

## QA 结果

- 思维 PDF：26 页。
- 推理 PDF：后续经 `CLICKABLE_TOC_BOOKMARK_PATCH_20260526` 重排并校正为 40 页。
- 两本 PDF 文本层均确认 `前言` 出现在 `目录` 之前。
- 两本 PDF 与 DOCX 均各有 1 处 `判题地图`。
- 思维正文 `【材料触发点】`：52 条。
- 推理正文 `【材料触发点】`：80 条。
- 扩展学生语言与后台污染门禁命中：0。

新增视觉抽样图：

- `08_visual_qa/思维宝典_抽样视觉QA_contact_sheet_20260526_frontmatter.png`
- `08_visual_qa/推理宝典_抽样视觉QA_contact_sheet_20260526_frontmatter.png`

视觉抽样确认：

- 第 1 页为标题、讲堂、前言和判题地图；
- 第 2 页为带页码目录；
- 第 3 页进入正文一级模块；
- 抽样页未见文字重叠、黑底、截断、页脚丢失或标题明显断裂。

## 仍不得称最终版

本补丁只解决前言/目录顺序与整本入口缺口，不等于最终验收通过。仍未完成：

- 真实 GPT Pro 审查：`real_call_pending`
- 真实 Claude 审查：`real_call_pending`
- ClaudeCode 厚内容生产 lane 与融合记录：未完成
- 本 run 逐题重新回源：未完全闭环
- Governor / Confucius artifact-only 最终验收：未完成
