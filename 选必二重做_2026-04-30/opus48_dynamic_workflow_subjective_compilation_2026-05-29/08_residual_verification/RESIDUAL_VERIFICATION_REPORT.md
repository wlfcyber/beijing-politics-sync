# RESIDUAL_VERIFICATION_REPORT — 选必二法律主观题汇编残项复核

- date: 2026-05-29
- scope: 复核 `07_acceptance/FINAL_ACCEPTANCE_REPORT.md` 第4节列出的 5 个诚实遗留点
- result: 5 项中 4 项已关闭，1 项保留为真实分值冲突

## 1. 复核结论

| question_id | 原遗留 | 复核结论 | 处理 |
|---|---|---|---|
| S33_Q20 | 案件三结果④被 PDF 翻拍底边裁切 | 已关闭 | 同套 `其他材料/朝阳高三期末2025.pptx` 第30-31张幻灯片补全案件二、案件三完整评分点；第④格为"乙公司赔偿甲经济损失"，并列出甲承担次要责任表述 |
| S42_Q18 | 材料一图表数值 OCR_gap | 已关闭/降级 | 原卷第6页图表未印逐年精确数值标签，细则第(1)问只要求总体趋势；且选必二落点在第(3)问，不受影响 |
| S16_Q19 | 细则6分 vs 题面8分 | 保留 | 原题页未印分值；试卷自带参考答案页标 8 分；正式阅卷细则标 6 分。冲突真实存在，仍按正式细则逐字保留 6 分并挂 `needs_review` |
| S18_Q19 | 细则8分 vs 题面5分 | 已关闭 | 原题页未印分值，未发现"5分"来源；此前为源包误记。以正式细则 8 分为准 |
| S62_Q17 | 原卷缺失、据细则重建 | 已关闭 | 同步镜像源找到教师版原卷 PDF，第6页含第17题完整题面与设问；已替换重建材料，保留"设问未标书名"的 `needs_review` 边界 |

## 2. 关键证据

- S33 补充来源：`/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025朝阳期末/其他材料/朝阳高三期末2025.pptx`；抽取文本见 `08_residual_verification/text_extracts/S33_other_pptx_text.txt` 第268-303行。
- S42 图表复核图：`08_residual_verification/rendered_pages/S42_paper_p6_full.png`；细则第(1)问为"总体上升/占比不断提高/结构优化"。
- S16 复核图：`08_residual_verification/rendered_pages/S16_paper_p7_full.png` 与 `S16_paper_ans_p9_full.png`；正式细则来自 `/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025丰台一模/细则/细则.docx`。
- S18 复核图：`08_residual_verification/rendered_pages/S18_paper_p6_full.png` 与 `S18_rubric_p19_full.png`；正式细则标 8 分。
- S62 原卷镜像：`/Users/wanglifei/GaokaoPolitics/2026各区模拟题/2026各区期末和期中/2026西城期末/2026北京西城高三（上）期末政治（教师版）.pdf`；第6页渲染图为 `08_residual_verification/rendered_pages/S62_found_teacher_pdf_p6.png`。

## 3. 已同步更新的文件

- `03_source_packets/S33_Q20.md`
- `03_source_packets/S42_Q18.md`
- `03_source_packets/S16_Q19.md`
- `03_source_packets/S18_Q19.md`
- `03_source_packets/S62_Q17.md`
- `00_control/SOURCE_LEDGER.csv`
- `00_control/QUESTION_COVERAGE_MATRIX.csv`
- `00_control/RUBRIC_SEARCH_LEDGER.csv`
- `04_outputs/build_compilation.py`
- `04_outputs/选必二法律主观题_习题与细则汇编_20260529.md`
- `04_outputs/选必二法律主观题_习题与细则汇编_20260529.csv`
- `05_framework_candidate/选必二考题规律与候选框架_20260529.md`

## 4. 当前剩余边界

- 内容层面仅剩 S16_Q19 的真实分值冲突：试卷参考答案页 8 分 vs 正式细则 6 分。
- 框架仍为 `candidate_framework`，外部网页可见审议门未闭合；本复核不把候选框架升级为定稿。
