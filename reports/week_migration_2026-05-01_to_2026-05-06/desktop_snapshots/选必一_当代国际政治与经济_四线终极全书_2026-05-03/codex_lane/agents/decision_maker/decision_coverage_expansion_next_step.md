# Decision: Coverage Expansion Next Step

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex A / Decision Maker

Scope: 只裁决 coverage 扩展下一步；不改学生稿、不宣布最终完成。

## 当前边界

Optional-label corrected narrow gate 已通过，但 Governor 只放行内部预览和 coverage expansion。当前不得发布最终 Markdown、Word/PDF、FINAL_ACCEPTANCE，也不得写 coverage closed。

`COVERAGE_MATRIX.csv` 当前覆盖 11 个优先题，均为 candidate / not-final 状态。`05_coverage/missing_questions.md` 明确写明 full-suite exhaustion 尚未完成，下一步必须从 priority rows 扩到 2024-2026 本地全套源。

## 扩展原则

1. 顺序：海淀 -> 西城 -> 东城 -> 朝阳；之后再进入丰台、顺义、昌平、通州、门头沟等其他区。
2. 来源：优先 `2024模拟题`、`2025模拟题`、`2026模拟题` 本地原始目录。旧 rerun 的 entries、suite reports、截图和 md 只可做后置比对，不能替代原始评分材料。
3. 证据：评分细则、评标、阅卷细则、阅卷总结、明确讲分/给分口径优先；普通参考答案只可 `reference-only`，不能提升成主链细则。
4. 2026石景山期末全模块排除。SOURCE_INVENTORY 中只有 `已放弃/2026石景山期末/其他材料/答案及评分参考.pdf`，不得重新打开补入。
5. 2026海淀期末此前已确认没考选必一，保持排除记录；除非发现新的评分细则明确含选必一，不进入下一批。

## 最小可执行分批

### Batch04A：海淀原始源定位优先批

劳动者下一批先处理 Batch04A。目标不是写正式条目，而是做套卷级 source triage：找出每套是否存在选必一主观题、题号、可用评分源、是否进入 Batch04 worker extraction。

先处理这些海淀套卷：

1. `2026海淀一模`
   - 细则：`SRC_14176e949dd0`，`2026各区一模/2026海淀一模/细则/细则.pdf`
   - 试卷：`SRC_184e191a3ddd`，`2026各区一模/2026海淀一模/试卷/试卷.pdf`
2. `2025海淀一模`
   - 细则：`SRC_a043a3fcb259`，`2025各区一模/2025海淀一模/细则/细则.docx`
   - 试卷：`SRC_20820628be28`，`2025各区一模/2025海淀一模/试卷/试卷.pdf`
   - 补充试卷：`SRC_8cf8c31e07b0`
3. `2024海淀一模`
   - 细则：`SRC_24a14c0c2355`，`2024海淀一模/细则/细则.docx`
   - 补充答案/细则候选：`SRC_5f85521d3602`
   - 试卷：`SRC_22a9fc350542`
4. `2024海淀二模`
   - 细则：`SRC_e6f22d1048fc`
   - 补充答案/细则候选：`SRC_da60e3ae2561`
   - 试卷：`SRC_a83c70cbad37`，必要时对照 `SRC_1c0a8eb1f6cd`
5. `2024海淀期中`
   - 细则：`SRC_e3f88f68dd56`
   - 试卷：`SRC_132d9a876bce`

暂不重跑这些已入 coverage 的海淀题：`2025海淀期中 Q16/Q21`、`2025海淀二模 Q21`、`2025海淀期末 Q22`。若 Batch04A 发现同套卷内还有未覆盖选必一主观题，只记录为 delta candidate。

### Batch04B：西城原始源定位批

Batch04A 写出 source triage 后，立即进入西城，不等待学生稿修完。

优先处理：

1. `2026西城一模`
   - 细则：`SRC_e28c940953ba`
   - 试卷：`SRC_5447227f6175`，必要时对照 `SRC_4ff3bc2e680a`
2. `2025西城一模`
   - 细则：`SRC_6ea5462e02af`
   - 试卷：`SRC_062e7a5c776b`
3. `2025西城二模`
   - 细则：`SRC_7e4a722d6d9e`
   - 试卷：`SRC_62207119d52d`
4. `2024西城一模`
   - 细则：`SRC_461b3fdcd830`
   - 补充材料：`SRC_ae7373932e0b`
   - 临时文件 `SRC_7591c6b9885f` 只作疑似残留，正常不优先读。
   - 试卷：`SRC_359083f91cd3`
5. `2024西城二模`
   - 细则：`SRC_ecba6fd5969d`
   - 补充材料：`SRC_3cb2df235603`
   - 试卷：`SRC_f9754eb81c9b`

`2026西城期末 Q20` 已是 Batch03 candidate，只在 coverage 表中保留，不作为下一批重跑对象。

### Batch04C：东城原始源定位批

东城放在西城之后，原因是已覆盖 `2024东城一模 Q16/Q20`，但仍有大量 2024二模、2025、2026 原始 P0 评分材料未做选必一筛查。

优先处理：

1. `2026东城一模`
   - 先读总细则 `SRC_1475504e2bc4`、`SRC_db98c4fdd4da`
   - 再读分题评标：`SRC_69f4a5c96bf0`、`SRC_03696854d360`、`SRC_5d17aa87bc17`、`SRC_7e06d068910f`、`SRC_1ebc5ea95bc8`、`SRC_90391f5178e4`、`SRC_0eef31593a11`、`SRC_1b5cd611d75c`
   - 试卷：`SRC_0fca4fc46247`，必要时对照 `SRC_3177a54aaed5`
2. `2026东城期末`
   - 细则：`SRC_88c6e8f353db`
   - 试卷：`SRC_9aba5c7460e6`
3. `2025东城一模 / 二模 / 期末`
   - 一模：`SRC_d39f12bd12f3` + `SRC_da5883631078`
   - 二模：`SRC_bd8e9436f81d` + `SRC_e1c925184ab8`
   - 期末：`SRC_f5c5ada09871`、`SRC_7d84ce85cb4b` + `SRC_8ab211d978d9`
4. `2024东城二模`
   - 优先阅卷总结/分题细则目录：`SRC_9c72a99890c0`、`SRC_6f5e364530de`、`SRC_242c241d6288`、`SRC_76b0722d57f1`、`SRC_c94e22c92a69`、`SRC_f89c1a3533f5`、`SRC_9080f96f9701`、`SRC_c492176058fd`、`SRC_593d33b50bbf`、`SRC_82b0237dce42`、`SRC_322c2db4a7fe`、`SRC_144e07c6e537`
   - 试卷：`SRC_6a382f2c9e97`

### Batch04D：朝阳原始源定位批

朝阳在东城后处理；已覆盖 `2026朝阳期中 Q17`、`2026朝阳一模 Q20`，下一步查剩余朝阳原始套卷。

优先处理：

1. `2025朝阳一模`
   - 总细则：`SRC_c3d1aea637c9`
   - 阅卷总结/讲分口径：`SRC_341c036102eb`、`SRC_e70708293da1`、`SRC_07886c57967f`
   - 试卷：`SRC_832947a8c994`
2. `2025朝阳二模`
   - 细则：`SRC_436f84dc1edf`
   - 试卷：`SRC_d411e2158d47`，必要时对照 `SRC_87571762455e`
3. `2025朝阳期末`
   - 细则：`SRC_49b23fecab97`
   - 试卷：`SRC_131c6c890bd4`
4. `2024朝阳一模 / 二模 / 期中`
   - 一模：`SRC_4fc81e818683`、`SRC_8a924a245316` + `SRC_d3b447f0ea3a`
   - 二模：`SRC_df323259ba77`、`SRC_8802a640c1e2` + `SRC_4de874d0f669`
   - 期中：`SRC_3d4cd35f4494`、`SRC_486fe5ba720a`、`SRC_b706c444e16d` + `SRC_611ed7564625`

## 劳动者下一批实际动作

下一批先做 `Batch04A 海淀原始源定位优先批`。

每套卷只产出 source triage，不写学生正文：

- `suite`
- `raw_source_ids`
- `scoring_source_type`: 评分细则 / 评标 / 阅卷总结 / 讲评给分口径 / reference-only
- `candidate_subjective_questions`
- `xuanbiyi_signal`: 明确选必一 / 疑似混模块 / 无选必一
- `action`: promote_to_worker_extraction / boundary_note / blocked_no_scoring_source / excluded
- `notes`

题源类型读取顺序：

1. P0 scoring: `细则`、`评标`、`阅卷总结`、明确讲分给分口径。
2. Paper/source prompt: 试卷 PDF/DOCX，仅用于题面、材料、完整设问定位。
3. P1 reference answer: 只作参考或材料辅助，不能作为 `细则位置`。
4. Previous run artifacts: 仅在原始源定位后做漏项比对。

## 停工与门禁

- 不因某一套卷找不到选必一而停工；写 `无选必一 / blocked / reference-only` 后继续下一套。
- 不因 2026石景山期末存在答案及评分参考而重开；它是用户确认排除项。
- Batch04A 完成后叫醒 Patcher 做 coverage-source audit；Patcher 只查证据等级、是否误用参考答案、是否漏了主观题。
- Governor 只可放行 `coverage_expansion_candidate`，不得放行最终成品。
