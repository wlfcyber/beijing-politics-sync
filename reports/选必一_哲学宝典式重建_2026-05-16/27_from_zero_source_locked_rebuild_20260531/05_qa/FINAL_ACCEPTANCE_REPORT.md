# 选必一终极版核查报告

## Deliverables

- Word 终稿：`/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终极版_20260531.docx`
- Run 内备份：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531/04_student_draft/选必一_当代国际政治与经济_主观题术语宝典_终极版_20260531.docx`
- 验收矩阵：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531/05_qa/FINAL_ACCEPTANCE_MATRIX.csv`

## Acceptance Summary

- 入正文条目：461
- 唯一证据卡：55
- 证据状态：{'RAW_CARD_READY': 461}
- 条目验收状态：{'PASS': 461}
- 六要素分布：{'时代背景': 21, '理论': 34, '经济全球化': 144, '政治多极化': 120, '中国': 127, '联合国': 15}
- 设问回源：{'EXACT': 429, 'PARTIAL': 32}
- 答案落点支撑：{'PARTIAL': 457, 'EXACT': 4}
- 讲义容器标题备注：{'CONTAINER_HEADING_NOT_LITERAL': 155}

## Requirement Audit

| 要求 | 当前证据 | 结论 |
| --- | --- | --- |
| 从零重建 run 与控制文件 | `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531`；TASK_BRIEF/PROGRESS 已记录上一版作废、证据卡先行 | PASS |
| 每条先有原卷/细则证据卡 | 55 张唯一证据卡，{'RAW_CARD_READY': 461} | PASS |
| 逐条核准设问 | `prompt_check`: {'EXACT': 429, 'PARTIAL': 32}，无 `NO_MATCH` | PASS |
| 逐条核准答案落点 | `answer_check`: {'PARTIAL': 457, 'EXACT': 4}，验收矩阵红灯 0 | PASS |
| 学生版删除后台证据字段 | 禁止词非零项：无 | PASS |
| 按用户二级框架重组 | H1 缺失：无；H2 缺失：无；核心标题数 104 | PASS |
| Word 终稿结构 | DOCX 压缩包完整性：PASS；段落条目抽检计数 461 | PASS |
| Word 视觉核验 | Microsoft Word 指定终极版 DOCX 导出 PDF `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531/05_qa/refined_render_check/final_word_export.pdf`，243 页；已抽检第 1、121、243 页 | PASS |

## Source Boundary Notes

- `2026海淀期中Q22(1)`：因正式细则未闭合，已从正文删除，不进入终稿。
- `2026石景山期末`：按用户复核结论，全模块排除，除非以后提供新评分细则。
- `2026西城期末Q20`：桌面原先缺试卷 PDF，已补回桌面试卷目录，并用该题第 8 页视觉核验设问。
- `CONTAINER_HEADING_NOT_LITERAL`：表示核心标题是讲义容器，不把它当作逐字细则原词；真正可落笔的答案句已单独回源核验。

## File Integrity

- `unzip -t` final DOCX: PASS
- forbidden residue: none
