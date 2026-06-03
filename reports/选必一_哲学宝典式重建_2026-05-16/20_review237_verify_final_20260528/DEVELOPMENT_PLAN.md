# DEVELOPMENT_PLAN

1. STEP_01_GATE_CONTROL: 完成三层 SOP、读取 skill 规则、建立本轮 run 控制文件。
2. STEP_02_PARSE_REVIEW: 抽取 237 条审稿意见，形成结构化台账，并定位 32 条 `⚠/❌` 重点复核项。
3. STEP_03_SOURCE_VERIFY: 对 237 条逐条给出核实判定；对 32 条重点项回查原始试卷/细则或 OCR 证据，区分“审稿意见成立需改”“材料支持可保留”“证据不足暂不动”。
4. STEP_04_APPLY_VALID_PATCHES: 只改成立/合理项，生成 237 条最终 DOCX/MD/PDF 与修正台账。
5. STEP_05_QA_DELIVERY: 检查条目数量、污染词、关键改动、DOCX/PDF 可读性与交付包完整性。

