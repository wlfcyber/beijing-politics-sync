# ClaudeCode B 独立审计报告 — 选必二《法律与生活》主观题

_本报告全部基于 ClaudeCode 在 00_manifest/extracted_text/ 文本层语料上独立再抽取的结果，与 Codex A 的 01_subjective_candidates/all_candidate_subjective_law_questions_codex.csv 做对照。_

**审计裁定 (Verdict): `CONDITIONAL_PASS`**

## 1. 总体指标

- Codex 候选题数: **103**（formal=66）
- ClaudeCode 候选题数: **74**（formal=54, reference_only=3, missing=17）
- Codex 有但 ClaudeCode 拒收: **34**
- ClaudeCode 有但 Codex 漏收: **5**
- 证据等级分歧（含 Codex 升级/降级）: **12**（codex 升级为 formal 共 2 条；codex 偏低 7 条）
- 模块边界分歧: **35**
- 题面回源风险（仅在证据文件中重建出 16-22 槽位、未在 role=paper 命中）: **22**
- 2026 石景山 期末 按硬规则 12 暂挂题数: **1**
- 经模块边界判定剔除的 16-22 主观槽位段落: **307**

## 2. Codex 是否漏题？

独立抽取发现 **5** 处 Codex 未收的 16-22 主观槽段。请见 `claudecode_missing_from_codex.csv`。
主要漏题原因猜想（基于 Codex 脚本逻辑 `extract_codex_candidates_and_atoms.py` 的阈值）：
- 在多模块合编 docx 中段落跨模块且 strong_legal_hits<2，Codex 未保留；
- 部分题面没有“运用《法律与生活》”等显式短语，Codex 凭关键词数量阈值收紧后丢弃。

## 3. Codex 是否误收？

ClaudeCode 对 Codex 候选中 **34** 条做出拒收判定，其中模块边界类拒收 **27** 条。
代表性误收风险：
- 多模块合编 docx（如必修1/必修2/必修3/选必二混排）中，靠近“运用《法律与生活》”字样的题段被错误吸附；
- ask_text 实质属于经济与社会/政治与法治/哲学与文化，但因为材料附近散落 “权利/责任/义务/法治” 而被 Codex 误收；
- 例：`Q0001_2024_东城_一模_16` ask 实为“资源优化配置/区域协调”——属经济与社会题，Codex 仍标 evaluation_standard formal。

## 4. Codex 是否把 reference_only 升级为 formal？

评级冲突共 **12** 条，其中 codex 把 reference 升为 formal 的有 **2** 条，codex 把本应是 formal 的判低有 **7** 条。
Codex 评级风险来自其规则：
- 把 role=evaluation_standard / marking_report 一律视为 formal，未要求文本本身含等级量表/分点扣分；
- 把 role=subjective_rubric 文件名含 “细则/评分/评标/阅卷” 即一律 formal，未要求级别赋分模板；
- 这会把 “参考答案+评分要点提示” 性质的文件升格为 formal。
ClaudeCode 改为：必须文本中含等级量表(水平1-4)或显式 X 分扣分点或文件名带“评分细则/评标/阅卷”才标 formal。

## 5. 必须降级的题

按 ClaudeCode 评级规则，下列 **2** 条 Codex 标为 formal 的应降级为 reference_only —— 详见 `claudecode_evidence_level_disagreements.csv` 中 direction=codex_upgraded 行。
在这些题获得真正的官方评分细则/阅卷报告/等级量表之前，不得作为框架核心节点支撑证据。

## 6. 不能进入第一轮归纳的题

- 所有 evidence_level=missing 的题（共 30 条 Codex；17 条 ClaudeCode）。
- 所有被 ClaudeCode 模块边界判定剔除的 Codex 候选（见 `claudecode_module_boundary_disagreements.csv`）。
- 2026 石景山 期末 全部题目，直至用户给出可用 formal 评分细则（硬规则 12，本批次共 1 题暂挂）。
- 题面回源风险题（见 `claudecode_locator_or_ocr_risks.csv`），需先回试卷原 PDF 校核 page/题号后再纳入。

## 7. 可以进入第一轮开放归纳的题

在 ClaudeCode 候选 74 题中，evidence_level=formal 且 paper-role 文本同时定位到题面者为 **35** 题，建议作为第一轮 GPT/Claude 开放归纳的最小可信集。其余 formal 但题面来自证据文件重建的题，需先解决 `claudecode_locator_or_ocr_risks.csv` 列出的回源缺口。

## 8. 主要数据完整性 / OCR / 题号风险

- 题面未在 role=paper 文本层命中、仅靠证据文件重建定位：22 条。
- 当前批次未对 image_pdf / corrupted / no_text_layer 的原始 PDF 进行重新 OCR；这部分材料对应的题面与细则可能整体缺席于本审计。
- 所有 source_locator 字段以 `Fxxxx:page/slide N` 形式记录，可回查 00_manifest/source_manifest.csv 与 extracted_text/Fxxxx.txt 的页/幻灯片标记。

## 9. 旧选必二成果

本次审计未引用任何旧选必二框架/题库/错肢库结论；ClaudeCode 候选完全由本批 extracted_text 现场抽取生成，符合 D003 与硬规则 11。

## 10. 建议下一步

1. 优先补齐 ClaudeCode 候选中 `evidence_level∈{reference_only, missing}` 的题对应的 *官方* 评分细则或阅卷报告；
2. 对 `claudecode_locator_or_ocr_risks.csv` 列出的题回原始 PDF 校页/校题号；
3. 对 `claudecode_false_positive_candidates.csv` 中“模块边界拒收”的 Codex 候选，由用户/人工最终裁定是否确属其他模块；
4. 在硬规则 12 解除前，2026 石景山 期末 整套不进入归纳。
