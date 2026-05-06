# Codex A Governor - Batch04B Xicheng Fix Closure Gate

运行目录：`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

本轮性质：Batch04B 西城预融合返修后窄门禁。只读取指定四个文件，只判断 Patcher 四项修正是否闭合，以及是否允许 coverage 将 Batch04B 主候选从 `pending / prelim_candidate` 推进到 `pass_with_fixes / pass_with_guard / candidate_with_fixes`。本报告不改总表、不改学生稿、不放行 final。

## 读取文件

- `fusion/scoring_atom_table_batch04B_xicheng_prelim.csv`
- `fusion/merge_register_batch04B_xicheng_updates.md`
- `COVERAGE_MATRIX.csv`
- `SOURCE_LEDGER.csv`

## verdict

`PASS_WITH_GUARD`

允许：
- Batch04B 主候选在 coverage 中从 `pending / prelim_candidate` 更新为：
  - `patcher_status: pass_with_fixes`
  - `governor_status: pass_with_guard`
  - `fusion_status: candidate_with_fixes`
- 允许范围仅限 Batch04B 主候选，不包括边界题 `2025西城一模 Q18`。

继续阻断：
- 学生稿。
- Word/PDF/DOCX。
- final / FINAL_ACCEPTANCE。
- coverage close。

## Patcher 四项修正闭合判定

### 1. XC02 高信息量核心保留

闭合。

`ATOM-XC02` 已从宽泛经济安全表述修正为：

`维护产业链供应链安全稳定，形成多元稳定的经贸关系，发挥比较优势并深度加入国际分工`

`merge_register` 也单列该核心，说明不能只抽象成“经济安全”。该修正保留了西城一模 Q20(2) 细则里的高信息量表达。

### 2. XC04 共同利益不反向吞并理论桶

闭合。

`ATOM-XC04` 的 boundary note 已写明：

`共同利益只作本题世界意义同槽替代表述，不反向并入理论桶“共同利益是国家合作的基础”；多边主义和全球经济治理体系改革保留完整表述`

该修正防止把同槽表述误计为独立理论必答频次。

### 3. 2024西城二模 Q19 原 XC13 过宽问题拆分

闭合。

返修后已拆为：

- `ATOM-XC13A`：`推动构建人类命运共同体，超越集团政治、实力至上和西方普世价值逻辑`
- `ATOM-XC13B`：`推动国际秩序朝着更加公正合理的方向发展，倡导国际关系民主化和真正的多边主义`

`merge_register` 同步拆分为两个核心，且继续标明第二句是 `多选二`，不等于全部必答。该修正解决了原来一个大帽子吞并人类命运共同体、国际秩序、国际关系民主化、多边主义等不同功能的问题。

### 4. XC16 多选三与结果表述边界

闭合。

`ATOM-XC16` boundary note 已写明：

`助推作用6分为多选三，技术标准和贸易规则话语权、制度型开放、产品服务国际竞争力不得全计为同一必答频次；产品服务国际竞争力优先作结果表述`

该修正防止把 2024西城一模 Q19(6) 的多选三结构和结果性表述误作单一必答频次。

## Coverage 更新授权范围

可以更新为 `pass_with_fixes / pass_with_guard / candidate_with_fixes` 的 Batch04B 主候选：

- `2026西城一模 Q20(2)`
- `2025西城一模 Q21`
- `2025西城二模 Q19(2)`
- `2025西城期末 Q20(2)`
- `2024西城二模 Q19`
- `2024西城一模 Q19(6)`

必须继续保持边界状态：

- `2025西城一模 Q18`
  - 当前 coverage 为 `boundary_only`
  - evidence 为 `P0_formal_scoring_rule_text_but_wrong_book_prompt`
  - 题干为《经济与社会》
  - 不得进入选必一主链频次

## 证据与假完成边界

- `SOURCE_LEDGER.csv` 中 Batch04B 主候选仍区分 P0 细则源与 P3 题面支持源，未见 P3 冒充 P0。
- `COVERAGE_MATRIX.csv` 当前仍未实际改为 closed；本报告只授权候选状态更新，不授权 closure。
- `ATOM-XC-B01` 仍为 `boundary_only`，不属于主候选放行范围。
- `candidate_with_fixes` 不是稳定主表、不是学生终稿、不是频次终版。

## 禁止动作

- 禁止编辑学生稿。
- 禁止生成 Word/PDF/DOCX。
- 禁止写 final 或 FINAL_ACCEPTANCE。
- 禁止 coverage close。
- 禁止把 `2025西城一模 Q18`、P3 题面、跨模块表述、多选同槽变体计作 P0 必答频次。

## Governor 最终判定

`BATCH04B_FIX_CLOSURE: PASS_WITH_GUARD`

`PATCHER_FOUR_FIXES: CLOSED`

`BATCH04B_MAIN_CANDIDATES_COVERAGE_UPDATE: ALLOW_TO_PASS_WITH_FIXES_PASS_WITH_GUARD_CANDIDATE_WITH_FIXES`

`2025_XICHENG_YIMO_Q18: KEEP_BOUNDARY_ONLY`

`STUDENT_DRAFT: BLOCK`

`WORD_PDF_DELIVERY: BLOCK`

`FINAL_ACCEPTANCE: BLOCK`

`COVERAGE_CLOSE: BLOCK`
