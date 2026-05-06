你是 ClaudeCode lane B，正在参与“飞哥政治庄园”选必三《逻辑与思维》四线从0重跑。

工作目录：
/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04

最高规则：
1. 这是从0重跑，不继承旧选必三稿件、旧结论、旧表格、旧学生版正文。
2. 你可以读取 MASTER_REQUIREMENTS.md、00_control/NOTEBOOK_DIGEST.md、你的 Phase 01 输出、原始试卷/细则/讲评源文件、用户上传的框架 PDF。
3. 为保持独立复核，本阶段不要读取或依赖 Codex 已写的 `03_entries/phase02_hard_sample_entries_internal.md`、`05_coverage/reasoning_question_attachment_matrix.csv`、`04_suite_reports/codex_suite_reports/phase02_hard_samples_report.md`。
4. 本阶段只做证据复核和矩阵，不写学生正文，不做 Word/PDF，不宣布完成。
5. 所有 PDF、DOC/DOCX、PPT/PPTX、图片、扫描页、表格都要调动可用工具处理。缺 pdftotext、pdftoppm、soffice、OCR 时，改用 python-docx、python-pptx、PyMuPDF、页面渲染、截图/视觉阅读、textutil/qlmanage 等 fallback；不能直接放弃。

本阶段任务：独立复核五个硬样本，并输出 A/B 可融合的结果。

五个硬样本：

HS01 2026顺义一模 Q19(2)
- 原卷：/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/试卷/试卷.pdf
- 细则：/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/细则/细则.pptx
- 目标：思维部分 / 科学思维特征

HS02 2025海淀二模 Q20
- 原卷：/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/试卷/试卷.pdf
- 细则/评标：/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/细则/补充材料/2025年海淀二模评标实录.docx
- 目标：思维部分 / 辩证思维
- 注意：此原卷可能是扫描/弱文本层，必须视觉或渲染核对题面。

HS03 2026朝阳期中 Q21(2)
- 原卷：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf
- 细则：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/细则.docx
- 补充细则：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/补充材料/细则.docx
- 目标：思维部分 / 创新思维

HS04 2026通州期末 Q11
- 原卷：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf
- 细则：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/细则/细则.pptx
- 目标：思维选择题 / 感性具体、思维抽象、思维具体
- 必须摘全题干、四个选项、答案键。

HS05 2026东城期末 Q17(2)
- 原卷：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026东城期末/试卷/试卷.pdf
- 细则：/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026东城期末/细则/细则.pptx
- 目标：推理部分 / 形式逻辑综合主观题

每个样本必须输出：
- 题干/设问原文锚点，带源文件和页码/行号/幻灯片号/段落号。
- 细则/答案/讲评锚点，带源文件和页码/行号/幻灯片号/段落号。
- 属于思维部分还是推理部分，若是边界题要说明。
- 可锁定知识或规则。
- 材料信号 -> 知识/规则 -> 论证动作的链条。
- 选择题必须写全四个选项与答案。
- 状态：LOCKED / LOCKED_PENDING_VISUAL / BLOCKED / SUSPECT。
- 如果与 Codex 未来融合可能有争议，请先写入 disagreement candidate。

请写入这些文件：
- claudecode_lane/phase02_hard_sample_crosscheck.md
- claudecode_lane/phase02_hard_sample_matrix.csv
- claudecode_lane/phase02_disagreements_and_blockers.md
- 04_suite_reports/claudecode_suite_reports/phase02_hard_samples_report.md
- 更新 claudecode_lane/progress.md

最后在终端输出简短摘要：每个 HS 的状态、主要知识/规则、阻塞项。
