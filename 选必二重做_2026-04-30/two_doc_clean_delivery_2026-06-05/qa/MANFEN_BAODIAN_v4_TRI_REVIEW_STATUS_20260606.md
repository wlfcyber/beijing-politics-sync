# 满分宝典 v4 三路审核状态

- candidate: `选必二法律与生活_满分宝典_v4_0606_精简截图校准版`
- created_at: 2026-06-06 03:55 CST
- local_status: LOCAL_STRUCTURAL_PASS
- final_status: NOT_FINAL

## 本地校验摘要

| 项目 | 结果 |
| --- | --- |
| 题源覆盖 | 74/74 |
| 细则答题点 | 1035 |
| 材料段落 | 210 |
| 原题图 | 23 |
| DOCX 表格 | 1 |
| DOCX 色块 | 0 |
| 禁用包装词 | 0 |
| PDF 页数 | 93 |
| PDF 首页文字抽取 | PASS |

## 外部审核门

| 审核 | 目标 | 状态 | 结论 |
| --- | --- | --- | --- |
| Claude cowork 应用端 | 依托原卷与细则逐题核准准确性、完整性、图文对应和满分答题点 | PENDING | 未完成 |
| Claude Opus 4.8 Max 网页/应用 | 审整体结构、语言、学生可用性和冗余表达 | PENDING | 未完成 |
| GPT-5.5 Pro 网页/应用 | 终审是否简单、全面、高效，列出最终阻断项 | PENDING | 未完成 |

## 边界

- 本地结构校验通过不等于最终通过。
- 三路审核均无阻断项后，才允许进入最终闭合。
- `render_docx.py` 因缺少 LibreOffice/`soffice` 未完成 PNG 视觉渲染；当前以 Word 导出的 PDF 可读性校验作为临时替代。
