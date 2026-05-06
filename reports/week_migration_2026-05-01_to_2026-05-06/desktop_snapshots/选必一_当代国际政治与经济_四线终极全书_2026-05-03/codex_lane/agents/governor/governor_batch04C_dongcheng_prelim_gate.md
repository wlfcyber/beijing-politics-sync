# Governor Batch04C Dongcheng Prelim Gate

verdict: PASS_WITH_GUARD

scope: Batch04C 东城预融合证据与假完成门禁。只裁定是否允许进入 candidate_with_fixes / boundary_only 下一步；不放行学生稿、Word、PDF、final、FINAL_ACCEPTANCE、coverage close。

read_files:
- `codex_lane/agents/worker/worker_batch04C_dongcheng_triage.md`
- `02_extraction/codex_extraction_logs/batch04C_dongcheng_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04C_dongcheng_prelim.csv`
- `fusion/merge_register_batch04C_dongcheng_updates.md`
- `COVERAGE_MATRIX.csv`
- `SOURCE_LEDGER.csv`

## Gate Decision

允许进入下一步的范围：
- Batch04C 东城主候选可进入 `candidate_with_fixes`，用于后续 fusion 主表/合并表补丁，但仍需保留 evidence level、source refs、boundary note。
- `2026东城一模 Q19(3)` 只能保持 `boundary_only`，不得入选必一主链频次。
- 如后续更新 coverage，只能把 Batch04C 主候选行从 `pending/prelim_candidate` 推到 `pass_with_guard/candidate_with_fixes`；`2026东城一模 Q19(3)` 仍为 `boundary_only`。不得写成 coverage closed。

继续禁止：
- 不得生成或放行学生稿、学生预览终稿、Word、PDF。
- 不得写 `FINAL_ACCEPTANCE`。
- 不得做 coverage close / source exhaustion close。
- 不得把 `PASS_WITH_GUARD` 解读为 Patcher 已完成或终稿已可发。

## Evidence Boundary Check

P0 / P3 边界成立：
- `2026东城期末 Q20`：P0 为正式细则 PPTX，P3 试卷只支持题面；四大全球倡议 4+2+1 结构可入候选。
- `2025东城二模 Q20`：P0 为正式细则 PDF，P3 试卷只支持小论文题面；背景、精神、行动三层可入候选。
- `2025东城一模 Q20`：P0 为正式细则 PDF，P3 试卷只支持元首外交题面；共同利益、经济全球化完整方向、全球治理/国际关系民主化、人类命运共同体实践可入候选。
- `2024东城二模 Q20`：P0 为 `20小题二模阅卷总结.docx`，试卷 PDF 已渲染并视觉核读第10页；视觉源足够作为完整题面支持，但不能作为评分细则来源。
- `2025东城期末 Q20`：P0 为正式细则 PDF，P3 试卷含普通解析/参考答案；解析不得作为细则，当前表内已注明不使用后附解析冒充细则。
- `2026东城一模 Q19(3)`：有 P0 评标细则，但题目主轴混合未来产业、高水平对外开放、产业链韧性和安全，只能边界观察。

普通答案/解析冒充细则检查：
- 未发现 `scoring_atom_table_batch04C_dongcheng_prelim.csv` 将普通试卷解析、参考答案或 P3 题面升格为 P0 采分细则。
- `2025东城期末 Q20` 的 P3 source 明确标注 `paper_text_with_reference_answer` 且 notes 写明后附解析不作为细则，符合边界。

## Atom Disposition

可进 `candidate_with_fixes` 的 atoms：
- `ATOM-DC01` - `ATOM-DC06`：2026东城期末 Q20，四大全球倡议系统推动构建人类命运共同体。
- `ATOM-DC07` - `ATOM-DC08`：2024东城二模 Q20，三大倡议路径+效果+总论；题面由视觉核读支撑，评分来自 P0 阅卷总结。
- `ATOM-DC09` - `ATOM-DC11`：2025东城二模 Q20，同球共济小论文三层。
- `ATOM-DC12` - `ATOM-DC15`：2025东城一模 Q20，中拉元首外交中的共同利益、经济全球化完整方向、全球治理/国际关系民主化、大国外交实践。
- `ATOM-DC16` - `ATOM-DC18`：2025东城期末 Q20，新能源汽车、贸易保护主义/逆全球化、维护本国利益与互利共赢/贸易自由便利。

只做边界记录、不得计入主链频次：
- `ATOM-DC-B01`：2026东城一模 Q19(3)。可记录制度型开放、国际高标准经贸规则、国际科创合作、开放与安全协同等边界表述；不得把未来产业、高水平对外开放、产业链韧性、高质量发展写成选必一核心术语。

不得计频或不得升主链的内容：
- 2024东城二模 Q20 的视觉题面源，只能支持设问和材料触发，不计为评分证据。
- 2025东城期末 Q20 的试卷后附解析/普通参考答案，不得作为细则或频次来源。
- 2025东城期末 Q20 的绿色、能源产业贡献可作材料支撑，不单独升为选必一核心。
- 2026东城一模 Q19(3) 的未来产业、新质生产力、产业链韧性、高质量发展不得计入选必一主链。

## Merge Register Check

合并登记口径可接受：
- `全球倡议系统推动构建人类命运共同体` 合并三大倡议与四大全球倡议，且保留三大题的路径+效果、四大题的 4+2+1 差异，没有拆成虚假独立频次。
- `同球共济` 被保留为材料表述，核心仍落在人类命运共同体和共同利益，没有泛化为万能合作模板。
- 经济全球化方向保留“开放、包容、普惠、平衡、共赢”完整五词。
- 贸易保护主义/逆全球化并入贸易摩擦类，未把试卷普通解析作为依据。
- `2026东城一模 Q19(3)` 明确为边界观察。

## False Completion Check

未发现硬性假完成：
- `COVERAGE_MATRIX.csv` 中 Batch04C 行仍为 `pending/prelim_candidate/boundary_only`，未显示 coverage closed。
- 主候选 notes 均写明“暂未入学生稿”；本门禁不放行学生稿，也不检查/编辑学生正文。
- Patcher 仍为 pending，本报告只允许进入带防护的候选/边界下一步，不替代后续 Patcher/Governor/Confucius 检查。

## Required Guards

后续推进必须满足：
- 保留每条 atom 的 P0/P3 evidence label 和 `source_ledger_refs`，不得在主表中抹平为统一 P0。
- 任何引用 2024东城二模 Q20 的地方必须写清：评分来自 P0 阅卷总结，视觉源只作题面支持。
- 任何引用 2025东城期末 Q20 的地方必须写清：普通解析不作为细则。
- `ATOM-DC-B01` 必须持续 `boundary_only`，不得计频、不得入学生主链。
- 进入学生预览前，仍需重新跑清洁扫描、桥接一致性、coverage 复核、Governor/Confucius 学会性检查。
