# PROGRESS

## P0 门禁与控制文件

- status: completed
- evidence:
  - 2026-06-17 刷新并读取 master governor report 与 worker daily orders。
  - 读取 `feige-politics-garden` 路由规则。
  - 读取 `feige-politics-garden-bixiu4` 必修四规则、cache-first directive、artifact contracts、必修四硬规则记事本。
  - 建立本 run 目录与控制文件。
- next_action: 扫描题源根目录，生成 `source_inventory.csv`。
- completed_output: `00_control/*`

## P1 题源清单

- status: completed
- evidence:
  - 扫描 6 个源根目录。
  - `01_source_inventory/source_inventory.csv` 共 370 个源文件行。
  - 识别 194 个唯一 sha256，63 个 suite_id。
  - `00_control/SOURCE_LEDGER.csv` 已同步。

## P2 缓存优先与文本候选

- status: completed
- evidence:
  - 检查并使用 `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus`。
  - `02_text_cache/cache_manifest.csv` 共 195 个 canonical 源检查行。
  - cache hit 167 行，raw extracted 23 行，skipped excluded 2 行。
  - 补跑并吸收 Apple Vision OCR：2024 东城一模、2024 东城二模、2024 丰台二模、2025 海淀二模、2026 丰台一模、2026 丰台期末、2026 房山一模、2026 海淀一模、2026 通州一模、2026 西城期末。
  - `03_question_index/question_candidates.csv` 生成 3186 条题源候选。

## P3 三模块初分

- status: completed_with_blockers
- evidence:
  - `04_module_classification/module_classification_matrix.csv` 生成 1203 行。
  - 已纳入目标三类：B2 162 行、B3 141 行、B4_CULTURE 106 行。
  - 边界排除 598 行，reference-only 6 行，ocr-needed 0 行，blocked 190 行。
  - 细则/讲评不再参与题号切分，避免把 PPT 页码当作试卷题号。
  - 全角题号与私有字体题号点已归一，修复顺义一模等 OCR 文本无法切题的问题。
  - OCR suite 身份推断已改为优先使用明确 suite 父目录和最先出现的区县线索，修复东城一模被误判成海淀的问题。
  - 取消文件名模块加分，避免“必修2分类汇编”等路径把法律/逻辑题误收进 B2。
  - 分类依据改为题面优先；有 paper 题面时不再把参考答案解析合并进分类文本。
  - 显式边界词优先：题面出现《法律与生活》《逻辑与思维》《当代国际政治与经济》或强边界词时，默认排除或标记小问拆分，不进入三条主链。

## P4 交叉核验

- status: completed_with_blockers
- evidence:
  - `05_reports/suite_readiness_overview.csv` 覆盖 63 个 suite_id。
  - `05_reports/classification_readiness_report.md` 已生成。
  - `05_reports/question_gap_review.csv` 与 `.md` 已生成，列出 21 套需要确认题号完整性的试卷。
  - `05_reports/blocked_manual_review_queue.csv` 生成 190 行复核队列。
  - `05_reports/manual_subquestion_split_queue.csv` 生成 45 行小问拆分队列。
  - `05_reports/blocked_review_summary.md` 已生成。
  - 2026-06-17 13:41-13:42 生成 `04_module_classification/subquestion_split_matrix.csv` 小问拆分草案：45 个父题输入，58 条小问草案，27 条目标小问、24 条边界排除小问、7 条拆分后仍需人工复核；无重复小问键。
  - 小问拆分父题层面：20 个父题完整拆分为草案，4 个父题部分拆分为草案，21 个父题仍需回源或人工裁决。
  - 2026-06-17 继续生成 `04_module_classification/subquestion_integrated_classification_matrix.csv` 与 `00_control/SUBQUESTION_INTEGRATED_COVERAGE_MATRIX.csv`：保留原父矩阵，另建子题级整合视图；替换 25 个已拆 blocked 父题，整合 58 条小问，输出 1236 行。
  - 子题级整合矩阵当前统计：included 436、module-boundary-excluded 622、blocked 172、reference-only 6；目标 included 为 B2 184、B3 145、B4_CULTURE 107；无重复题/小问题键。
  - 2026-06-17 继续生成 `04_module_classification/prompt_resolved_classification_matrix.csv` 与 `00_control/PROMPT_RESOLVED_COVERAGE_MATRIX.csv`：只用强题面信号复核剩余 blocker，解决 53 行，剩余 blocked 119 行。
  - 强题面复核后当前最佳接手统计：included 453、module-boundary-excluded 658、blocked 119、reference-only 6；目标 included 为 B2 192、B3 152、B4_CULTURE 109；无重复题/小问题键。
  - 2026-06-17 生成 `05_reports/question_gap_triage.csv` 与 `.md`：21 套 gap 中，11 套疑似原卷实际 20 题，6 套题面/OCR 漏切但辅助材料有题号线索，4 套题面与辅助候选均未抓到缺号。
  - 2026-06-17 生成 `05_reports/question_gap_repair_candidates.csv` 与 `.md`：45 个缺号项分解为 2 个高置信切题漏切、8 个 raw marker 需视觉复核、6 个辅助材料线索、18 个原始源检查项、11 个 20 题结构待验收项。
  - 缺号修补脚本已收紧防伪命中：选择题选项序号、表格编号、材料序号不得直接升格为顶层题号。
  - 2026-06-17 生成 `04_module_classification/gap_high_confidence_repaired_classification_matrix.csv` 与 `00_control/GAP_HIGH_CONFIDENCE_REPAIRED_COVERAGE_MATRIX.csv`：只追加 2 个高置信缺号题，输出 1238 行；included 454、module-boundary-excluded 659、blocked 119、reference-only 6。
  - 高置信缺号修补新增：2024 东城一模第 4 题纳入 B3，2026 丰台期末第 10 题排除为 XB2；原 45 个缺号项剩余 43 个仍需处理或验收。
  - 2026-06-17 复核 8 个 `raw_marker_candidate_visual_check`：5 个确认为顶层题号，3 个确认为伪命中；生成 `05_reports/raw_marker_visual_review.csv` 与 `05_reports/raw_marker_review_repair_audit.csv`。
  - 2026-06-17 生成 `04_module_classification/raw_marker_review_repaired_classification_matrix.csv` 与 `00_control/RAW_MARKER_REVIEW_REPAIRED_COVERAGE_MATRIX.csv`：输出 1243 行；included 456、module-boundary-excluded 662、blocked 119、reference-only 6；目标 included 为 B2 193、B3 153、B4_CULTURE 110。
  - raw marker 复核新增：2024 西城二模第 1 题排除为 B4_PHILOSOPHY，2024 西城二模第 4 题纳入 B2，2026 丰台一模第 14 题排除为 XB1，2026 房山一模第 1 题纳入 B4_CULTURE，2026 西城期末第 15 题排除为 XB1。2026 丰台一模第 5 题、2026 丰台二模第 15 标记、2026 丰台期末第 2 标记均为伪命中，不写入矩阵。
  - 2026-06-17 复核 6 个 `raw_paper_repair_with_auxiliary_clue`：5 个父题号由原卷 DOCX/OCR 页上下文坐实，1 个丰台期末 Q6 只有细则线索、未找到可靠原卷位置，继续保留 gap。
  - 2026-06-17 生成 `04_module_classification/auxiliary_clue_repaired_classification_matrix.csv` 与 `00_control/AUXILIARY_CLUE_REPAIRED_COVERAGE_MATRIX.csv`：输出 1249 行；included 458、module-boundary-excluded 666、blocked 119、reference-only 6；目标 included 为 B2 193、B3 155、B4_CULTURE 110。
  - auxiliary clue 复核新增：2024 顺义二模 Q6 排除为 XB3，Q20 排除为 B1；2026 丰台一模 Q7 排除为 XB3；2026 丰台期末 Q9 纳入 B3；2026 房山一模 Q17 拆分为 Q17(1) XB2 排除与 Q17(2) B3 纳入。累计缺号项剩余 33。
  - 2026-06-17 复核 11 个 `accept_20_question_structure_after_source_spotcheck`：均由原卷/OCR Q20 题面、无顶层 Q21 候选、无行首顶层 Q21 文本命中证明为实际 20 题结构；生成 `05_reports/twenty_question_structure_review.csv` 与 `05_reports/twenty_question_structure_acceptance_audit.csv`。
  - 2026-06-17 生成 `04_module_classification/twenty_question_structure_accepted_classification_matrix.csv` 与 `00_control/TWENTY_QUESTION_STRUCTURE_ACCEPTED_COVERAGE_MATRIX.csv`：矩阵行数不变为 1249 行；included 458、module-boundary-excluded 666、blocked 119、reference-only 6；目标 included 为 B2 193、B3 155、B4_CULTURE 110。
  - twenty-question structure 复核不新增题目，只关闭 11 个被证明不存在的 Q21 缺口；累计缺号项从 33 降至 22。
  - 2026-06-17 复核 22 个剩余题号缺口：16 个确认是真实顶层题并写入矩阵，6 个确认为原卷实际 19/20 题结构而关闭缺口；生成 `05_reports/raw_source_inspection_review.csv` 与 `05_reports/raw_source_inspection_repair_audit.csv`。
  - 2026-06-17 生成 `04_module_classification/raw_source_inspection_repaired_classification_matrix.csv` 与 `00_control/RAW_SOURCE_INSPECTION_REPAIRED_COVERAGE_MATRIX.csv`：输出 1265 行；included 464、module-boundary-excluded 674、blocked 121、reference-only 6；目标 included 为 B2 195、B3 159、B4_CULTURE 110；无重复题/小问题键。
  - raw source inspection 复核新增 16 行，其中丰台期末 Q2/Q6 因 B3/B4_CULTURE 或 B4_CULTURE/XB3 混合被保留为 `UNKNOWN_OR_MIXED` blocked；该阶段题号 gap 剩余 0，但最终闭环仍受 121 行 blocked 队列限制，后续已进入 strong blocker 复核。
  - 2026-06-17 14:44 生成 `05_reports/strong_blocker_resolution_review.csv`、`05_reports/strong_blocker_resolution_audit.csv`、`04_module_classification/strong_blocker_resolved_classification_matrix.csv` 与 `00_control/STRONG_BLOCKER_RESOLVED_COVERAGE_MATRIX.csv`：只消解原卷/OCR 强证据可判定的 blocked 行，解决 64 行，blocked 从 121 降至 57。
  - strong blocker 复核后的最新接手统计：included 486、module-boundary-excluded 716、blocked 57、reference-only 6；目标 included 为 B2 206、B3 167、B4_CULTURE 113；无重复题/小问题键，题号 gap 仍为 0。
  - 本轮明确拒绝弱关键词规则：`继承发展` 不等于法律继承，`内涵` 不单独判逻辑，`出口/企业` 在全球贸易语境下不直接判 B2，客观题不使用细则/答案污染题面；小问拆分和答案键依赖行继续 blocked。
  - 2026-06-17 按用户提示补入“哲学文化混合题抽离文化采分点”规则，明确 `民族精神` 属于文化；生成 `05_reports/culture_component_extraction_audit.csv`、`05_reports/culture_component_row_resolution_audit.csv`、`04_module_classification/culture_component_extracted_classification_matrix.csv` 与 `00_control/CULTURE_COMPONENT_EXTRACTED_COVERAGE_MATRIX.csv`。
  - culture component 复核新增 20 行 `culture_component`，并对 5 个原父题做整题文化判定或非文化余项关闭；最新接手统计：1285 行，included 508、module-boundary-excluded 718、blocked 53、reference-only 6；目标 included 为 B2 206、B3 167、B4_CULTURE 135；无重复题/组件键，题号 gap 仍为 0。
  - 本轮只抽离题面、答案或细则中明确的文化判断点；未把所有材料背景中的文化词自动判入文化，跨选必法律/逻辑/国政经内容仍按边界排除或继续 blocked。
  - 2026-06-17 继续生成 `05_reports/remaining_strong_cleanup_audit.csv`、`05_reports/remaining_target_component_audit.csv`、`04_module_classification/remaining_strong_cleanup_classification_matrix.csv` 与 `00_control/REMAINING_STRONG_CLEANUP_COVERAGE_MATRIX.csv`：只处理源材料、选项、设问或答案上下文明示的剩余强证据行。
  - remaining strong cleanup 复核解决/排除 13 个原 blocked 行，新增 9 行 `target_component`，将 live blocked 从 53 降至 40。
  - 最新接手统计：1294 行，included 522、module-boundary-excluded 726、blocked 40、reference-only 6；目标 included 为 B2 213、B3 171、B4_CULTURE 138；行粒度为 suite 3、question 1202、subquestion 60、culture_component 20、target_component 9；无重复题/组件键，题号 gap 仍为 0。
  - 本轮修补审计证据回填逻辑：小问行没有直接候选文本时，回退到 `subquestion_split_matrix.csv` 或父题证据；`remaining_strong_cleanup_audit.csv` 与 `remaining_target_component_audit.csv` 已无空证据行。
  - 2026-06-17 继续生成 `05_reports/source_explicit_cleanup_audit.csv`、`05_reports/source_explicit_target_component_audit.csv`、`04_module_classification/source_explicit_cleanup_classification_matrix.csv` 与 `00_control/SOURCE_EXPLICIT_CLEANUP_COVERAGE_MATRIX.csv`：只处理设问/答案/细则明确限定目标或边界模块的整题，以及可抽出的目标组件。
  - source explicit cleanup 复核解决/排除 17 个原 blocked 行，新增 6 行 `target_component`，将 live blocked 从 40 降至 23。
  - 最新接手统计：1300 行，included 536、module-boundary-excluded 735、blocked 23、reference-only 6；目标 included 为 B2 217、B3 181、B4_CULTURE 138；行粒度为 suite 3、question 1202、subquestion 60、culture_component 20、target_component 15；无重复题/组件键，题号 gap 仍为 0。
  - 本轮明确保留 suite 身份混叠、答案键依赖客观题、以及题源/小问错位风险行，不为追求闭环强判。
  - 2026-06-17 16:01 继续生成 `05_reports/suite_identity_culture_repair_audit.csv`、`04_module_classification/suite_identity_culture_repaired_classification_matrix.csv` 与 `00_control/SUITE_IDENTITY_CULTURE_REPAIRED_COVERAGE_MATRIX.csv`：专门修复 `2025_海淀_期末` suite_id 同时混入海淀期中与海淀期末的问题，并按用户提示补抽期末第 22 题文化成分。
  - suite identity + culture repair 移除旧混叠行 22 行，重建 `2025_海淀_期中` 24 行、`2025_海淀_期末` 28 行，新增/保留显式目标组件 6 行；live blocked 从 23 降至 20。
  - 最新接手统计：1330 行，included 554、module-boundary-excluded 750、blocked 20、reference-only 6；目标 included 为 B2 223、B3 190、B4_CULTURE 141；行粒度为 suite 3、question 1222、subquestion 64、culture_component 20、target_component 21；无重复题/组件键，题号 gap 仍为 0。
  - 本轮明确执行用户提示：综合/哲学文化混合题中，`中华优秀传统文化`、`中华民族精神`、`愚公精神` 等文化点独立进入 B4_CULTURE；`民族精神` 按文化处理。2025 海淀期末第 22 题新增 `22#B4_CULTURE_COMPONENT`，并按细则另抽 `22#B3_COMPONENT`。
  - 2026-06-17 16:30 继续按用户现场提示“题目和细则中的文化部分都要抽离，民族精神属于文化”生成 `05_reports/culture_hint_final_cleanup_audit.csv`、`05_reports/culture_hint_final_component_audit.csv`、`04_module_classification/culture_hint_final_cleanup_classification_matrix.csv` 与 `00_control/CULTURE_HINT_FINAL_CLEANUP_COVERAGE_MATRIX.csv`。
  - culture-hint-final-cleanup 复核解决/关闭 17 个原 blocked 行，删除 1 个已被整小问吸收的冗余 B2 组件，新增 7 行组件；live blocked 从 20 降至 3。
  - 最新接手统计：1336 行，included 562、module-boundary-excluded 765、blocked 3、reference-only 6；目标 included 为 B2 225、B3 193、B4_CULTURE 144；行粒度为 suite 3、question 1222、subquestion 64、culture_component 23、target_component 24；无重复题/组件键，题号 gap 仍为 0。
  - 本轮新增文化组件包括：2025 海淀二模 Q16 `文化的功能/创造性转化创新性发展`、2026 丰台一模 Q21 `中华优秀传统文化的哲学智慧`、2026 丰台期末 Q16 `留白` 的中华优秀传统文化美学智慧；父题余项按哲学/选必/必修一边界关闭。
  - 当前仅剩 3 条 blocked：2026 丰台一模 Q1 缺可靠答案键；2026 丰台期末 Q2/Q6 选择题跨文化、B3/哲学或 XB3，缺可靠答案键或人工选项拆分。已将 `00_control/COVERAGE_MATRIX.csv` 与 `04_module_classification/module_classification_matrix.csv` 同步为本轮最新矩阵。
  - `00_control/COVERAGE_MATRIX.csv` 状态词检查通过，无非法 status。
  - 无题号 suite 已显式写入 `SUITE_BLOCKER` 行，不再从矩阵里消失。
  - 2024 两个无稳定区县/阶段身份的汇编文件降为 `REFERENCE_HELPER_ONLY`，可参考但不能作为套卷覆盖证据。

## P5 总管验收

- status: completed
- evidence:
  - Governor 不能通过最终覆盖闭环：仍有 190 行 `blocked` 需要人工模块复核，其中 45 行是显式多模块小问拆分；21 套列入题号 gap 复核。
  - 本 run 可作为后续宝典准备包接手，但不得宣称全覆盖完成。
  - 2026-06-17 13:41 复核矩阵与覆盖账本一致：1203 行矩阵、1203 行 coverage、无重复 `(suite_id, question)` 键、`ocr-needed` 为 0。
  - 2026-06-17 13:41 高风险边界词扫描通过：`法律与生活`、`当代国际政治与经济`、`逻辑与思维`、`民法典`、`合同`、`侵权`、`三段论`、`元首外交`、`经济全球化` 在 `included` 行中命中 0。
  - 2026-06-17 已刷新 master governor；最新时间以 `reports/master_governor/latest_master_governor_report.md` 为准。总管继续标记 `possible_false_closure`，原因与本 run 留下的真实 blocker 一致。
  - 2026-06-17 13:42 小问拆分草案已生成但未整合回父矩阵；下一步如要闭环，需处理 `blocked_manual_review_queue.csv`，整合/复核 `subquestion_split_matrix.csv`，并逐套确认 `question_gap_review` 中的题号缺口是真缺题、OCR 漏切，还是该卷实际题量小于 21。
  - 2026-06-17 子题级整合矩阵已完成，后续三条宝典线优先用 `SUBQUESTION_INTEGRATED_COVERAGE_MATRIX.csv` 接手；最终闭环仍需处理剩余 172 行 blocked 与 21 套题号 gap。
  - 2026-06-17 强题面复核矩阵已完成，后续三条宝典线优先用 `PROMPT_RESOLVED_COVERAGE_MATRIX.csv` 接手；最终闭环仍需处理剩余 119 行 blocked 与 21 套题号 gap。
  - 2026-06-17 题号 gap 已完成首轮分诊；最终闭环仍需回源修复 6 套辅助材料有线索的漏切项，人工检查 4 套无候选缺号项，并确认 11 套 20 题结构。
  - 2026-06-17 题号 gap 已生成修补候选包；下一步优先处理 2 个高置信切题漏切，并对 8 个 raw marker 进行版面/原卷视觉复核。
  - 2026-06-17 高置信切题漏切 2 行已整合成新矩阵；下一步从 8 个 raw marker 视觉复核、6 个辅助线索回源、18 个原始源检查项继续。
  - 2026-06-17 raw marker 复核已闭合；最新矩阵为 `RAW_MARKER_REVIEW_REPAIRED_COVERAGE_MATRIX.csv`。下一步从 6 个辅助材料线索、18 个原始源检查项、11 个 20 题结构验收项继续；累计缺号项剩余 38。
  - 2026-06-17 auxiliary clue 回源复核已闭合；最新矩阵为 `AUXILIARY_CLUE_REPAIRED_COVERAGE_MATRIX.csv`。下一步从 119 行 blocked、33 个题号缺口、18 个原始源检查项和 11 个 20 题结构验收项继续，不得宣称最终覆盖闭环。
  - 2026-06-17 实际 20 题结构验收已闭合；该阶段矩阵为 `TWENTY_QUESTION_STRUCTURE_ACCEPTED_COVERAGE_MATRIX.csv`。后续已由原始题源检查继续处理 22 个题号缺口。
  - 2026-06-17 原始题源检查已闭合；该阶段矩阵为 `RAW_SOURCE_INSPECTION_REPAIRED_COVERAGE_MATRIX.csv`。题号缺口已降为 0；随后由 strong blocker 复核继续处理当时剩余的 121 行 blocked。
  - 2026-06-17 强证据 blocker 复核已闭合；该阶段矩阵为 `STRONG_BLOCKER_RESOLVED_COVERAGE_MATRIX.csv`。题号缺口维持 0，后续已由 culture component 复核继续处理 57 行 blocked。
  - 2026-06-17 文化成分抽离复核已闭合；最新矩阵为 `CULTURE_COMPONENT_EXTRACTED_COVERAGE_MATRIX.csv`。B4_CULTURE 已从 113 增至 135，下一步从 53 行 blocked 继续，不能宣称最终覆盖闭环。
  - 2026-06-17 剩余强证据清理已闭合；最新矩阵为 `REMAINING_STRONG_CLEANUP_COVERAGE_MATRIX.csv`。B2/B3/B4_CULTURE 分别增至 213/171/138，live blocked 降至 40。最终闭环仍未通过，后续需继续处理 40 行 blocked。
  - 2026-06-17 源明示清理已闭合；最新矩阵为 `SOURCE_EXPLICIT_CLEANUP_COVERAGE_MATRIX.csv`。B2/B3/B4_CULTURE 分别增至 217/181/138，live blocked 降至 23。最终闭环仍未通过，后续需继续处理 23 行 blocked。
  - 2026-06-17 suite 身份与文化组件修复已闭合；最新矩阵为 `SUITE_IDENTITY_CULTURE_REPAIRED_COVERAGE_MATRIX.csv`。B2/B3/B4_CULTURE 分别增至 223/190/141，live blocked 降至 20。最终闭环仍未通过，后续需继续处理 20 行 blocked。
  - 2026-06-17 用户现场文化提示复核已闭合；最新矩阵为 `CULTURE_HINT_FINAL_CLEANUP_COVERAGE_MATRIX.csv`，并已同步为通用 `COVERAGE_MATRIX.csv`。B2/B3/B4_CULTURE 分别增至 225/193/144，live blocked 降至 3。最终闭环仍未通过，后续只剩 3 条答案键/选项拆分 blocker。
  - 2026-06-17 最终答案键闭合已完成：回源确认 2026 丰台一模 Q1 答案 B，2026 丰台期末 Q2 答案 C，2026 丰台期末 Q6 答案 A；新增 2026 丰台一模 Q1 的 B3 组件，保留 Q2/Q6 既有文化组件，并关闭三题父题余项。
  - 最新接手矩阵为 `FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv`，并已同步为通用 `COVERAGE_MATRIX.csv` 与 `module_classification_matrix.csv`。
  - 最终矩阵统计：1337 行，included 563、module-boundary-excluded 768、reference-only 6、blocked 0；B2/B3/B4_CULTURE 分别为 225/194/144；行粒度为 suite 3、question 1222、subquestion 64、culture_component 23、target_component 25。
  - 最终机器复核通过：题号 gap 0，重复题/小问/组件键 0，状态词合法，审计空证据行 0，canonical 矩阵与最终矩阵一致。

## P6 最终答案键闭合

- status: completed
- evidence:
  - 输出 `04_module_classification/final_answer_key_closure_classification_matrix.csv` 与 `00_control/FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv`。
  - 输出 `05_reports/final_answer_key_closure_audit.csv`、`05_reports/final_answer_key_component_audit.csv`、`05_reports/final_answer_key_blocked_queue.csv` 与 `05_reports/final_answer_key_closure_report.md`。
  - `05_reports/final_answer_key_blocked_queue.csv` 只有表头，live blocker 为 0。

## P7 Fable5 源缓存交接

- status: superseded_by_p9_completion
- evidence:
  - 自查 `cache_manifest.csv` 发现 3 条 canonical 源仍为 `empty-or-unsupported`：2026 西城二模评标 PDF、2026 通州一模试卷 PDF、2026 顺义二模试卷 PDF。
  - 已用 Apple Vision OCR 或既有 OCR absorbed 文本修复 3 条缓存，写回 `02_text_cache/texts/`，并将 `cache_manifest.csv` 中 `empty-or-unsupported` 清零。
  - 输出 `06_fable5_source_cache/fable5_ai_readable_source_cache.jsonl`：195 行 source packet，其中 193 行 `ai_readable_text_ready`、2 行 `excluded_by_hard_rule`。
  - 输出 `06_fable5_source_cache/fable5_source_cache_manifest.csv`、`fable5_suite_source_index.csv`、`cache_repair_audit.csv`、`matrix_evidence_path_audit.csv` 与 `FABLE5_READ_ME_FIRST.md`。
  - 验证：JSONL 195 行均可解析，嵌入源文本约 1,060,103 字符；`needs_repair_after_handoff` 为 0；最终矩阵证据路径缺失为 0。
  - 验证：最终 included 主观题中使用 `reference-answer` 作来源的行数为 0；reference-answer 在 fable5 manifest 中带 `do_not_use_as_rubric`。
  - 边界：OCR 转写用于 AI 阅读与检索，不承诺人工逐字校勘；若后续宝典需要逐字引用，应回原 PDF/渲染页复核。
  - 后续 P8/P9 发现 P7 仍非全源闭合：source_inventory 唯一 sha 为 194，而当时 Fable5 缓存未覆盖全部唯一 sha；P7 保留为历史阶段，不作为最终交接结论。

## P8 期中/期末身份与 OCR 文化补丁

- status: completed
- evidence:
  - 2026-06-17 发现 `2026_海淀_期末` 与 `2026_朝阳_期末` 都存在真实期中/期末源身份混叠风险；按真实源文件夹和 OCR 内容拆分。
  - 2026 海淀期末试卷 PDF 无系统文本层，已用 Apple Vision OCR 写入 `02_text_cache/ocr_cache/2026_海淀_期末_试卷/试卷.ocr.txt`，并覆盖原 1790 字符级摘要缓存。
  - 2026 朝阳期末试卷与细则 PDF 均无系统文本层，已用 Apple Vision OCR 写入 `02_text_cache/ocr_cache/2026_朝阳_期末_试卷/试卷.ocr.txt` 与 `02_text_cache/ocr_cache/2026_朝阳_期末_细则/细则.ocr.txt`。
  - 生成 `00_control/HAIDIAN_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv`：矩阵 1365 行，included 572、module-boundary-excluded 787、reference-only 6、blocked 0；B2/B3/B4_CULTURE 为 226/197/149。
  - 生成 `00_control/CHAOYANG_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv` 并同步 canonical：矩阵 1393 行，included 586、module-boundary-excluded 801、reference-only 6、blocked 0；B2/B3/B4_CULTURE 为 231/202/153。
  - 朝阳补丁将原 `2026_朝阳_期末` 中 22 行实际期中矩阵行拆回 `2026_朝阳_期中`，并为真实 `2026_朝阳_期末` 新增 22 行父题/小问和 6 行目标/文化组件。
  - 按用户规则，朝阳期末题目中的中华优秀传统文化滋养、中华法律文化精华/文化根基，以及第 16 题细则中的中华优秀传统文化、文化自信、民族文化认同、创造性转化和创新性发展均抽为 B4_CULTURE 组件。
  - 源身份复核通过：`source_inventory.csv`、`SOURCE_LEDGER.csv`、`cache_manifest.csv`、`question_candidates.csv`、`COVERAGE_MATRIX.csv` 中，2025 海淀期末不再含 2025 海淀期中路径，2026 朝阳期末不再含 2026 朝阳期中路径，2026 海淀期末不再含 2026 海淀期中路径。

## P9 Fable5 全源缓存闭合

- status: completed_with_ocr_exactness_boundary
- evidence:
  - 2026-06-17 对账发现 source_inventory 唯一 sha 194，而当时 Fable5 缓存只覆盖 171 个唯一 sha；不能继续称为全源闭合。
  - 生成 `05_reports/fable5_missing_source_cache_completion_report.md` 与 `05_reports/fable5_missing_source_cache_completion_audit.csv`，补入 23 个缺登记唯一 sha，覆盖 39 个 source_inventory 行。
  - 对 2026 西城一模 PDF paper 与 2026 西城期末细则 PDF 补跑 Apple Vision OCR，避免把 `rendered-ocr-needed` 或“无可靠文本层”占位文本交给 Fable5。
  - 2026 石景山期末继续按硬规则登记为 `skipped-excluded` / `excluded_by_hard_rule`，不把答案及评分参考升级为细则。
  - 重新生成 `06_fable5_source_cache/fable5_ai_readable_source_cache.jsonl`、`fable5_source_cache_manifest.csv`、`fable5_suite_source_index.csv`、`cache_repair_audit.csv`、`matrix_evidence_path_audit.csv` 与 `FABLE5_READ_ME_FIRST.md`。
  - 最终验证：source_inventory unique sha 194、cache unique sha 194、Fable5 unique sha 194；`cache_manifest.csv` 状态为 raw-extracted 44、cache-hit 149、skipped-excluded 1、empty-or-unsupported 0。
  - 最终验证：Fable5 JSONL 194 行，0 个 JSON parse error，嵌入源文本 1,091,691 字符；handoff status 为 `ai_readable_text_ready` 193、`excluded_by_hard_rule` 1、`needs_repair` 0。
  - 最终验证：矩阵 1393 行，blocked 0、ocr-needed 0、重复题/小问/组件键 0、证据路径缺失 0；included 主观题使用 reference-answer 作来源为 0；reference-answer packet 标记 `do_not_use_as_rubric`。
