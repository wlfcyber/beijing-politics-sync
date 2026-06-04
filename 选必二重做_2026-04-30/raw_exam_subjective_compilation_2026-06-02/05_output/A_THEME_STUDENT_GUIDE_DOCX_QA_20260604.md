# A类十主题学生宝典 DOCX QA

## 1. 文件

- DOCX: `05_output/选必二法律与生活_A类十主题学生宝典工作稿_20260604.docx`
- 桌面副本: `C:\Users\Administrator\Desktop\选必二法律与生活_A类十主题学生宝典工作稿_20260604.docx`
- 覆盖报告: `05_output/A_THEME_STUDENT_GUIDE_COVERAGE_REPORT_20260604.md`
- 回源审计: `05_output/A_THEME_SOURCE_REPAIR_AUDIT_20260604.md`
- 回源覆盖层: `05_output/A_THEME_SOURCE_REPAIR_OVERRIDES_20260604.json`
- 边界裁决覆盖层: `05_output/A_THEME_PENDING_BOUNDARY_RESOLUTIONS_20260604.json`
- 细则原文QA: `05_output/A_THEME_RUBRIC_SOURCE_INTEGRITY_QA_20260604.md`
- 剩余待核复查: `05_output/A_THEME_REMAINING_PENDING_RECHECK_20260604.md`
- Word COM视觉QA: `05_output/A_THEME_WORD_COM_VISUAL_QA_20260604.md`
- 视觉接触表复查: `05_output/A_THEME_VISUAL_CONTACT_SHEET_REVIEW_20260604.md`

## 2. 本阶段新增结构

- A类十主题速查页: 1
- 章首学习页: 10
- 每章新增学习卡片: 本章怎么学 / 题源画像 / 一眼判断 / 采分动作 / 考场句型 / 边界提醒
- 每章二轮加深卡片: 命题人路径 / 判题四步 / 高频给分件 / 易混边界
- 每章新增方法页组件: 本章先背 / 核心链条 / 常见设问翻译 / 采分模板 / 错答清单 / 真题分组导读
- 封面标题: `《法律与生活》A类十主题学生宝典工作稿`

## 3. 结构核验

| 项目 | 结果 |
| --- | ---: |
| DOCX 文件大小 | 160958 bytes |
| Word 段落数 | 999 |
| Word 表格数 | 0 |
| A类 Heading 2 | 38（含 A类十主题速查 + A1-A10） |
| Heading 3 真题条目 | 74 |
| 本章怎么学 | 10 |
| 题源画像 | 10 |
| 一眼判断 | 10 |
| 采分动作 | 10 |
| 考场句型 | 10 |
| 边界提醒 | 10 |
| 本章先背 | 10 |
| 核心链条 | 10 |
| 常见设问翻译 | 10 |
| 采分模板 | 10 |
| 错答清单 | 10 |
| 真题分组导读 | 10 |
| 命题人路径 | 10 |
| 判题四步 | 10 |
| 高频给分件 | 10 |
| 易混边界 | 10 |
| 回源修复 | 10 |
| 待回源重排 | 0 |
| 边界裁决 | 16 |
| 待核边界 | 2 |
| 末尾待核/待补清单 | 1 |
| 工程痕迹 `SRC_` / `source_id` / `entry_E` | 0 |

## 4. 五件套核验

| 标签 | 段落数 |
| --- | ---: |
| 【入口】 | 74 |
| 【判定依据】 | 74 |
| 【题目材料】 | 74 |
| 【设问】 | 74 |
| 【细则】 | 74 |
| 【答案落点】 | 74 |

## 5. 学生正文噪音扫描

| 词/模式 | 命中 |
| --- | ---: |
| `SRC_` | 0 |
| `source_id` | 0 |
| `entry_E` | 0 |
| `题眼` | 0 |
| `评分锚点` | 0 |
| `PAGEPAGE` | 0 |
| `阅卷总结` | 0 |
| `学生问题` | 0 |
| `学生表现` | 0 |
| `教师教学` | 0 |
| `改进措施` | 0 |
| `全球治理倡议` | 0 |
| `上合组织` | 0 |
| `全球南方` | 0 |

## 6. Word / 渲染

- Word COM smoke test: `WORD_OPEN_OK pages=99 paragraphs=999`
- `render_docx.py --emit_pdf`: WORD_COM_PDF_PNG_OK: rendered_pages=99 suspicious_blank=0 contact_sheets=5 manually_reviewed=yes; render_docx.py unavailable
- 若 render_status 记录 Word COM -> PDF -> PNG，则本阶段另以 `A_THEME_WORD_COM_VISUAL_QA_20260604.md` 和接触表复查作为视觉渲染证据。

## 7. 状态边界

- 本稿是 A类十主题学生化加工稿，不是最终闭合稿。
- 覆盖口径仍为 63 套 / 67 道大题 / 74 个分问。
- Word 末尾已单列待核/待补清单。
- 原始 18 个 pending_reason 中，本轮边界裁决清除 16 个，正文仍保留 2 个【待核边界】。
- 未闭合待回源重排/材料风险项为 0。
