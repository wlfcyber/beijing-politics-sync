# Codex A Governor - Batch04B Xicheng Prelim Gate

运行目录：`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

本轮性质：Batch04B 西城预融合证据与假完成门禁。只判断预融合是否可进入下一步 `candidate_with_fixes`；不改学生稿，不改总表，不放行 final / Word / PDF / FINAL_ACCEPTANCE / coverage close。

## 读取文件

- `02_extraction/codex_extraction_logs/batch04B_xicheng_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04B_xicheng_prelim.csv`
- `fusion/merge_register_batch04B_xicheng_updates.md`
- `COVERAGE_MATRIX.csv`
- `SOURCE_LEDGER.csv`

## verdict

`PASS_WITH_GUARD`

允许：
- `ATOM-XC01` 至 `ATOM-XC16` 进入下一步 `candidate_with_fixes`。
- `ATOM-XC-B01` 只能保持 `boundary_only`。
- Batch04B 只可继续融合候选、Patcher/Governor 复核、coverage 回填。

继续阻断：
- 学生稿改写或学生版发布。
- Word/PDF/DOCX 生成。
- final / FINAL_ACCEPTANCE。
- coverage close。
- 把 P3 题面、普通答案、跨书边界题或多选同槽变体当作 P0 必答频次。

## P0 / P3 证据边界

Batch04B 的 P0 与 P3 标注整体守边界：

- `2026西城一模 Q20(2)`：`SOURCE_LEDGER` 区分 `P0_formal_scoring_rule_text` 的细则源与 `P3_paper_text` 的题面源；`ATOM-XC01` 至 `ATOM-XC04` 可入候选。
- `2025西城一模 Q21`：细则源为 `P0_formal_scoring_rule_text`，题面源为 `P3_paper_text`；新发展理念本体已明确只作材料支撑，不升选必一主链。
- `2025西城二模 Q19(2)`：细则源为 `P0_formal_scoring_rule_text`，题面源为 `P3_paper_text`；零关税材料下的正确义利观、共享机遇和经济全球化方向可入候选。
- `2025西城期末 Q20(2)`：细则源为 `P0_formal_scoring_rule_pdf_text`，题面源为 `P3_paper_text`；国际规则维权与市场多元化可入候选。
- `2024西城二模 Q19`：细则源为 `P0_formal_scoring_rule_text`，题面源为 `P3_paper_text`；多选口径已写入 atom 与 coverage，不得全作必答频次。
- `2024西城一模 Q19(6)`：细则源为 `P0_formal_scoring_rule_text`，题面源为 `P3_paper_text`；可入候选但必须带混模块边界。
- `2025西城一模 Q18`：虽然有细则文本，但题干明确《经济与社会》，`ATOM-XC-B01` 和 coverage 均已标 `boundary_only`，不得进入选必一主链频次。

判定：**未发现 P3 题面或普通答案冒充细则。**

## 重点门禁项

### 1. 普通答案是否冒充细则

未发现。当前 Batch04B 主候选均回链到 `P0_formal_scoring_rule_text` 或 `P0_formal_scoring_rule_pdf_text`；题面/材料来源保持 `P3_paper_text` 支撑身份。`SOURCE_LEDGER` 中普通题面、纸面材料、旧运行定位均未被提升为正式细则。

### 2. Q18《经济与社会》边界

通过。`2025西城一模 Q18` 在 manual notes、atom 表、coverage、source ledger 中均被降为边界：

- atom：`ATOM-XC-B01`
- promotion status：`boundary_only`
- evidence：`P0_formal_scoring_rule_text_but_wrong_book_prompt`
- 裁决：两个市场两种资源联动、贸易便利化只作跨书迁移提示，不计选必一主链频次。

### 3. 2024西城二模 Q19 多选口径

通过但必须带 guard。

- `ATOM-XC12`：第一句 `1分多选一`，命运与共、利益交汇、和平与发展等只能并入同槽表述积累，不拆成多条必答频次。
- `ATOM-XC13`：第二句 `多选二，每点2分`，人类命运共同体、国际关系民主化、真正的多边主义、全球治理、发展中国家发言权等只能作为同槽变体进入表述积累，不得全部作必答频次。
- `merge_register` 已写明“第二句多选二不等于全部必答”。

### 4. 学生稿是否被误改

未发现 Batch04B 进入学生稿。

只读检索 `07_student_doc` 未发现 `2026西城一模`、`2025西城一模 Q21`、`2025西城二模`、`2025西城期末`、`2024西城二模`、`2024西城一模`、`零关税`、`欧盟反补贴`、`自贸区3.0` 等 Batch04B 新题内容进入学生预览稿。检索到的“国际公共产品”属于既有通州/中国方案表达，不构成本批误改。

### 5. 假完成风险

未发现假完成，但必须继续阻断。

`COVERAGE_MATRIX.csv` 中 Batch04B 行仍为：

- `governor_status: pending`
- `fusion_status: prelim_candidate / prelim_candidate_with_boundary / boundary_only`
- `notes: 暂未入学生稿` 或边界说明

因此本报告只能授权下一步进入 `candidate_with_fixes`，不得解释为 coverage closed、终稿完成或可交付。

## Atom 放行范围

可进入 `candidate_with_fixes`：

- `ATOM-XC01` 至 `ATOM-XC04`：2026西城一模 Q20(2)，自贸区3.0、贸易投资便利化、供应链安全、国际分工、发展中国家发言权、多边主义与全球经济治理。
- `ATOM-XC05` 至 `ATOM-XC07`：2025西城一模 Q21，国际公共产品、人类共同利益、中国智慧中国方案、经济全球化完整五词方向；新发展理念本体不升主链。
- `ATOM-XC08` 至 `ATOM-XC09`：2025西城二模 Q19(2)，正确义利观、中国市场、共享发展机遇、普惠包容经济全球化。
- `ATOM-XC10` 至 `ATOM-XC11`：2025西城期末 Q20(2)，国际规则维权、国际组织权利、市场多元化、走出去合作、贸易壁垒应对；不得擅自扩写政府职责。
- `ATOM-XC12` 至 `ATOM-XC13`：2024西城二模 Q19，但必须保留多选一/多选二口径，不得全作必答频次。
- `ATOM-XC14` 至 `ATOM-XC16`：2024西城一模 Q19(6)，可作为选必一相关候选，但未来产业、新质生产力、现代化产业体系不入选必一主链。

必须保持 `boundary_only`：

- `ATOM-XC-B01`：2025西城一模 Q18，《经济与社会》题，只作跨书迁移/触发提示。

## 必须保留的 guard

1. P0 scoring source 与 P3 paper support 必须继续分列，不得合并成同一证据等级。
2. `2024西城二模 Q19` 的多选同槽表述只能计作变体，不得拆成全部必答频次。
3. `2025西城一模 Q18` 不得进入选必一主链或频次。
4. 经济与社会、未来产业、新质生产力、现代化产业体系、企业技术创新等跨模块内容只能作材料支撑或边界记录。
5. 任何进入 `candidate_with_fixes` 的 atom 仍需后续 Patcher/Governor 与 coverage 回填，不得直接进入学生稿。

## 禁止动作

- 禁止编辑学生稿。
- 禁止生成 Word/PDF/DOCX。
- 禁止宣布 final 或 `FINAL_ACCEPTANCE`。
- 禁止关闭 coverage。
- 禁止把 `candidate_with_fixes` 当作稳定主表、终稿闭合或频次终版。

## Governor 最终判定

`BATCH04B_PRELIM_FUSION: PASS_WITH_GUARD`

`ATOM-XC01_TO_XC16: PASS_TO_CANDIDATE_WITH_FIXES`

`ATOM-XC-B01: BOUNDARY_ONLY`

`STUDENT_DRAFT: BLOCK`

`WORD_PDF_DELIVERY: BLOCK`

`FINAL_ACCEPTANCE: BLOCK`

`COVERAGE_CLOSE: BLOCK`
