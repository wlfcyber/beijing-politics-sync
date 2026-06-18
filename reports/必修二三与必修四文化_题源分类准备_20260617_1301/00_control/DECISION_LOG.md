# DECISION_LOG

## D001 - 新建混合分类准备 run

- time: 2026-06-17 13:01 +08:00
- decision: 新建 `reports/必修二三与必修四文化_题源分类准备_20260617_1301`，用于三条未来宝典线的题源分类准备。
- reason: 当前目标横跨必修二、必修三、必修四文化，项目中没有现成的独立 lane。按三层 SOP，先补 run 控制文件再处理资料。
- validation: 控制文件齐备后才进入题源扫描。

## D002 - 分类粒度采用题/小问而非整卷

- time: 2026-06-17 13:01 +08:00
- decision: 试卷可做 suite 级索引，但真正分类必须落到题号/小问。
- reason: 北京区卷常在一套卷中混合必修、选必与哲学文化模块；整卷分类会污染后续宝典。
- validation: `COVERAGE_MATRIX.csv` 与 `module_classification_matrix.csv` 必须出现 question 字段。

## D003 - v1 覆盖失败写入本 run 硬规则

- time: 2026-06-17 13:01 +08:00
- decision: 本 run 禁止用条目数、页数、文档厚度、模型自述替代覆盖证明。
- reason: v1 哲学宝典曾出现大量重复头部题掩盖缺失套卷/选择题的失败。
- validation: 后续报告必须从源文件清单和唯一题矩阵出发统计。

## D004 - 2026 石景山期末默认排除

- time: 2026-06-17 13:01 +08:00
- decision: 除非用户以后提供新的可用评分细则来源，2026 石景山期末不进入三条主链。
- reason: 必修四分支规则明确用户已逐题复核该套没有可用评分细则，所有书/模块均排除。
- validation: 题源清单若发现该套，状态标为 `module-boundary-excluded` 或 `blocked` 并注明原因。

## D005 - 采用缓存优先抽取

- time: 2026-06-17 13:07 +08:00
- decision: 抽题前先按 sha256 命中 `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus`，只对未命中或缓存不足的 canonical 源回源抽取。
- reason: 必修四技能与项目规则都要求 cache-first，避免重复转换同一批原始 PDF/Word/PPT。
- validation: `02_text_cache/cache_manifest.csv` 记录 cache hit、raw extracted、failed/skipped 状态。

## D006 - 细则和讲评不参与题号切分

- time: 2026-06-17 13:08 +08:00
- decision: `COVERAGE_MATRIX.csv` 的题号来源只使用 `paper` 和 `reference-answer`；`rubric`、`marking-report`、`lecture` 先不参与题号切分。
- reason: 初版发现细则 PPT 页码/小节号会被误当成试卷第 1、2、3 题，存在污染覆盖矩阵的风险。
- validation: 脚本限定 `COVERAGE_SOURCE_TYPES = {"paper", "reference-answer"}`。

## D007 - 无题号 suite 必须显性阻塞

- time: 2026-06-17 13:09 +08:00
- decision: 对有源文件但未能形成题号级分类的 suite 写入 `SUITE_BLOCKER` 行。
- reason: v1 的失败之一是缺失题源被厚文档掩盖；本 run 不允许缺题号 suite 从覆盖矩阵里消失。
- validation: `module_classification_matrix.csv` 与 `COVERAGE_MATRIX.csv` 均包含 `SUITE_BLOCKER` 行，状态为 `ocr-needed`、`reference-only` 或硬规则排除。

## D008 - 吸收并补跑 Apple Vision OCR

- time: 2026-06-17 13:18 +08:00
- decision: 对缓存只有短摘要或空文本的套卷，使用本机 Apple Vision OCR 生成 run-local `02_text_cache/ocr_cache/<suite_id>/*.ocr.txt`，再由脚本吸收进入题号矩阵。
- reason: 多套扫描 PDF 在预处理缓存中只有 GPT 摘要，不能形成可靠题号级分类；通州一模纸面完全未抽出文字。
- validation: 2024 东城一模、2024 东城二模、2024 丰台二模、2025 海淀二模、2026 丰台一模、2026 丰台期末、2026 房山一模、2026 海淀一模、2026 通州一模、2026 西城期末均生成 OCR 文本并参与重跑。

## D009 - 修复 OCR suite 身份推断

- time: 2026-06-17 13:20 +08:00
- decision: OCR suite 推断使用明确 suite 父目录和最先出现的区县/阶段线索，不再按固定区县列表顺序命中。
- reason: 2024 东城一模 OCR 文本后段出现“海淀”时，旧规则会把东城误判成海淀；这会直接污染覆盖矩阵。
- validation: `infer_suite_id_from_text()` 对 `02_text_cache/ocr_cache/2024_东城_一模/试卷.ocr.txt` 返回 `2024_东城_一模`。

## D010 - 无稳定区县阶段身份的汇编降为 helper-only

- time: 2026-06-17 13:21 +08:00
- decision: `2024_unknown_district_unknown_stage` 与 `2024_unknown_district_一模` 这类无稳定区县/阶段身份的汇编文件标为 `REFERENCE_HELPER_ONLY` / `reference-only`。
- reason: 它们可帮助定位模块材料，但不能作为标准套卷覆盖证据；把它们列为 `ocr-needed` 会混淆真实套卷 blocker。
- validation: 最终矩阵仅保留 2026 石景山期末硬规则排除与两个 helper-only `SUITE_BLOCKER`，套卷级 `ocr-needed` 清零。

## D011 - 题号 gap 单独警示

- time: 2026-06-17 13:21 +08:00
- decision: 生成 `05_reports/question_gap_review.csv` 与 `.md`，把检测题号少于 1-21 的套卷列为复核项。
- reason: 一些卷可能实际只有 20 题，也可能是 OCR 漏切；在确认前不能把“有矩阵行”误读为“全题覆盖”。
- validation: gap 表当前 21 行；后续宝典闭环必须逐套处理或确认这些 gap。

## D012 - 禁止文件名模块加分

- time: 2026-06-17 13:29 +08:00
- decision: 删除 `filename_module_hint` 和 `filename_bixiu4_hint` 参与分类得分。
- reason: “必修2分类汇编”等路径名会把法律、逻辑、国政经题错误推入 B2/B4，属于 v1 式假覆盖风险。
- validation: 高风险扫描显示显式《法律与生活》《逻辑与思维》《当代国际政治与经济》题不再因路径名进入三条主链。

## D013 - 分类题面优先

- time: 2026-06-17 13:30 +08:00
- decision: 有 `paper` 题面时，用题面文本分类；只在没有题面时才使用 `reference-answer`。
- reason: 参考答案和解析常混入其他小问、其他模块术语，合并后会污染选择题/主观题模块判断。
- validation: `extract_and_classify.py` 中 grouped rows 先选 `paper_rows` 作为 classification_rows。

## D014 - 显式边界词优先

- time: 2026-06-17 13:31 +08:00
- decision: 题面出现《法律与生活》《逻辑与思维》《当代国际政治与经济》或强边界词时，先排除；若同题还出现目标书名，则标记 `manual_subquestion_split_needed`。
- reason: 多模块主观题不能整题收进必修二/三/文化；应按小问或得分点拆分。
- validation: 生成 `manual_subquestion_split_queue.csv` 45 行；显式边界词在 `included` 行中的命中数降为 0。

## D015 - 恢复线程后只做控制闭环同步

- time: 2026-06-17 13:41 +08:00
- decision: 继续本目标时先复核三层 SOP、矩阵一致性和总管状态，不新增正文型宝典内容。
- reason: 当前 run 的合理状态是准备包可交接、最终覆盖不能关闭；继续写正文会绕过 190 行人工复核、45 行小问拆分和 21 套题号 gap。
- validation: 机器复核显示 1203 行矩阵与 coverage 一致、无重复题号键、`ocr-needed` 为 0、高风险边界词未进入 `included`；master governor 已刷新到 2026-06-17T13:47:08+08:00。

## D016 - 小问拆分采用设问句优先草案

- time: 2026-06-17 13:42 +08:00
- decision: 对 45 行 `manual_subquestion_split_needed` 先生成 `subquestion_split_matrix.csv` 草案，不直接覆盖父矩阵。
- reason: 直接用整段材料分类会把下一问材料串入当前小问；OCR 还可能把下一道大题接到当前题后，必须先生成可审计草案。
- validation: 草案共 58 条小问，27 条目标小问、24 条边界排除小问、7 条仍需人工复核；重复小问键为 0。

## D017 - 建立子题级整合覆盖矩阵

- time: 2026-06-17
- decision: 生成 `SUBQUESTION_INTEGRATED_COVERAGE_MATRIX.csv` 作为后续三条宝典线优先接手账本，原始父矩阵保留不覆盖。
- reason: 多模块父题不能长期以整题 `UNKNOWN_OR_MIXED` 卡住；已能按小问证明的部分应进入子题级账本，同时未证明部分继续 blocked。
- validation: 整合矩阵 1236 行，替换 25 个 blocked 父题，整合 58 条小问；blocked 从 190 降至 172；目标 included 从 409 增至 436；重复题/小问题键为 0，高风险边界词在 included 行中命中 0。

## D018 - 强题面规则只解决高置信 blocker

- time: 2026-06-17
- decision: 生成 `PROMPT_RESOLVED_COVERAGE_MATRIX.csv` 作为当前最佳接手账本；仅使用明确书名、明确题型或高辨识模块信号解决剩余 blocker。
- reason: 弱词会污染分类，例如“政府”“实践”“矛盾”“高质量发展”都不能单独决定归类；被标为 `manual_subquestion_split_needed` 的父题不得整题解决。
- validation: 强题面规则解决 53 行，blocked 从 172 降至 119；目标 included 为 B2 192、B3 152、B4_CULTURE 109；重复题/小问题键为 0；目标 prompt-resolved 行中高风险边界词命中 0。

## D019 - 题号 gap 分诊

- time: 2026-06-17
- decision: 生成 `question_gap_triage.csv`，把 21 套题号 gap 分为原卷可能实际 20 题、题面/OCR 漏切但辅助材料有线索、以及无候选缺号三类。
- reason: 不同 gap 的处理成本不同，不能把 20 题结构、OCR 漏切、真实缺源混成同一个 blocker。
- validation: 21 行 gap 中，11 行 `likely_actual_20_question_paper`，6 行 `paper_or_ocr_missing_but_auxiliary_present`，4 行 `source_or_ocr_missing_no_candidate`。

## D020 - 题号 gap 修补候选包与伪命中过滤

- time: 2026-06-17
- decision: 生成 `question_gap_repair_candidates.csv`，把缺号项拆成高置信切题漏切、raw marker 视觉复核、辅助材料线索、原始源检查和 20 题结构验收五类。
- reason: 初步 raw marker 搜索会把选择题选项序号误当作顶层题号；缺号修补必须先做置信分层，不能把孤立数字直接写回覆盖矩阵。
- validation: 45 个缺号项中，2 个 `repair_primary_question_split_high_confidence`、8 个 `raw_marker_candidate_visual_check`、6 个 `raw_paper_repair_with_auxiliary_clue`、18 个 `raw_source_manual_inspection_needed`、11 个 `accept_20_question_structure_after_source_spotcheck`。

## D021 - 高置信缺号修补矩阵

- time: 2026-06-17
- decision: 生成 `GAP_HIGH_CONFIDENCE_REPAIRED_COVERAGE_MATRIX.csv` 作为最新接手矩阵，只整合 2 个高置信缺号题，其余低置信或缺源项继续 blocked/gap。
- reason: 2024 东城一模第 4 题与 2026 丰台期末第 10 题在原 OCR 中有完整题干和设问框架，且模块去向明确；低置信 raw marker 仍可能是选项序号，不能写入矩阵。
- validation: 新矩阵 1238 行，新增 2 行；2024 东城一模第 4 题纳入 B3，2026 丰台期末第 10 题排除为 XB2；无重复题号键，blocked 仍为 119，原缺号项剩余 43。

## D022 - raw marker 版面/原卷复核矩阵

- time: 2026-06-17
- decision: 生成 `RAW_MARKER_REVIEW_REPAIRED_COVERAGE_MATRIX.csv` 作为最新接手矩阵；8 个 raw marker 候选中，5 个确认是真顶层题号并整合，3 个确认为伪命中并保留为 gap/open-source 检查项。
- reason: raw marker 低置信项不能靠孤立数字入矩阵；必须用原 DOCX 文本、OCR 页上下文或 PDF 文本确认它是顶层题号，而不是选项序号、图表编号或材料列表项。
- validation: 新矩阵 1243 行，新增 5 行；2024 西城二模 Q1 排除为 B4_PHILOSOPHY，Q4 纳入 B2；2026 丰台一模 Q14 排除为 XB1；2026 房山一模 Q1 纳入 B4_CULTURE；2026 西城期末 Q15 排除为 XB1。无重复题号键，blocked 仍为 119，原缺号项剩余 38。

## D023 - auxiliary clue 回源复核矩阵

- time: 2026-06-17
- decision: 生成 `AUXILIARY_CLUE_REPAIRED_COVERAGE_MATRIX.csv` 作为最新接手矩阵；6 个辅助材料线索中，5 个父题号由原卷 DOCX/OCR 页上下文确认并整合，1 个丰台期末 Q6 因只见细则线索、未定位可靠原卷题面而保留 gap。
- reason: 细则或讲评中的题号只能提示回源，不能单独证明原卷覆盖；房山一模 Q17 同时包含选必二法律小问和必修三法治小问，必须拆分为 17(1)/17(2)，避免整题误收。
- validation: 新矩阵 1249 行，新增 6 行；2024 顺义二模 Q6 排除为 XB3、Q20 排除为 B1；2026 丰台一模 Q7 排除为 XB3；2026 丰台期末 Q9 纳入 B3；2026 房山一模 Q17(1) 排除为 XB2、Q17(2) 纳入 B3。无重复题号键，blocked 仍为 119，原缺号项剩余 33。

## D024 - 实际 20 题结构验收

- time: 2026-06-17
- decision: 生成 `TWENTY_QUESTION_STRUCTURE_ACCEPTED_COVERAGE_MATRIX.csv` 作为最新接手矩阵；11 个缺 Q21 的候选套卷全部验收为实际 20 题结构，不新增题目行，只关闭对应 Q21 gap。
- reason: 缺号审计不能把所有缺 `21` 都当作 OCR 漏切；若原卷/OCR 能确认到 Q20，且题目候选与行首文本搜索均没有顶层 Q21，则该卷应按 20 题结构验收。
- validation: 新矩阵仍为 1249 行；2024 朝阳二模、2024 朝阳期中、2024 海淀一模、2024 海淀期中、2024 石景山一模、2025 房山一模、2025 西城二模、2026 东城一模、2026 延庆一模、2026 石景山二模、2026 西城二模共 11 个 Q21 gap 已关闭。无重复题号键，blocked 仍为 119，原缺号项剩余 22。

## D025 - 原始题源检查修复矩阵

- time: 2026-06-17 14:36 +08:00
- decision: 生成 `RAW_SOURCE_INSPECTION_REPAIRED_COVERAGE_MATRIX.csv` 作为当时接手矩阵；22 个剩余题号缺口全部完成逐题回源，16 个真实顶层题补入矩阵，6 个不存在的 Q20/Q21 缺口按原卷 19/20 题结构验收关闭。
- reason: 题号 gap 不能长期停留在“raw-source inspection needed”；后续三条宝典需要清楚知道缺的是题、OCR、实际短卷，还是已找到但模块混合。
- validation: 新矩阵 1265 行；included 464、module-boundary-excluded 674、blocked 121、reference-only 6；目标 included 为 B2 195、B3 159、B4_CULTURE 110；题号 gap 剩余 0，重复题号键 0。该阶段最终闭环仍被 121 行 blocked 队列阻止，后续已由 D026 接续处理。

## D026 - 强证据 blocker 消解矩阵

- time: 2026-06-17 14:52 +08:00
- decision: 生成 `STRONG_BLOCKER_RESOLVED_COVERAGE_MATRIX.csv` 作为最新接手矩阵；只用原卷题面、OCR 上下文或明确题源信号消解 64 行 blocked，保留 57 行继续人工复核。
- reason: 题号 gap 清零后，剩余 blocker 需要分层处理。强证据足够的行应先进入目标或边界账本，但弱关键词、小问拆分、答案键依赖的混合选择题不能被强行关闭。
- validation: 新矩阵 1265 行；included 486、module-boundary-excluded 716、blocked 57、reference-only 6；目标 included 为 B2 206、B3 167、B4_CULTURE 113；题号 gap 剩余 0，重复题号键 0，高风险边界词在 newly resolved target included 行中命中 0。该阶段闭环仍被 57 行 blocked 队列阻止，后续已由 D027 接续处理。

## D027 - 哲学文化混合题文化采分点抽离矩阵

- time: 2026-06-17 15:00 +08:00
- decision: 生成 `CULTURE_COMPONENT_EXTRACTED_COVERAGE_MATRIX.csv` 作为最新接手矩阵；根据用户提示，把哲学文化混合题中的文化采分点抽离为 `culture_component` 行，并明确 `民族精神` 属于 B4_CULTURE。
- reason: 文化宝典不能因为题中同时出现哲学方法论就丢掉民族精神、文化自信、中华优秀传统文化双创、非遗/文物/博物馆/文创等文化采分点；也不能整题混收哲学内容，所以采用组件行记录文化部分。
- validation: 新矩阵 1285 行；新增 20 行 `culture_component`，5 个原父题整题判定或余项关闭；included 508、module-boundary-excluded 718、blocked 53、reference-only 6；目标 included 为 B2 206、B3 167、B4_CULTURE 135；题号 gap 剩余 0，重复题号键 0，重复文化组件键 0。最终闭环仍被 53 行 blocked 队列阻止。

## D028 - 剩余强证据清理与目标组件矩阵

- time: 2026-06-17 15:29 +08:00
- decision: 生成 `REMAINING_STRONG_CLEANUP_COVERAGE_MATRIX.csv` 作为最新接手矩阵；在 53 行剩余 blocked 中，只消解源材料、设问、选项或答案上下文明确的行，并把可明确拆出的 B2/B3/B4_CULTURE 部分记为 `target_component`。
- reason: 后续必修二、必修三、必修四文化宝典需要尽量少的 live blocker，但不能把答案键依赖、小问权重不清或边界混合项强行关闭。组件行能接住明确目标内容，父题余项仍按边界排除或保留 blocked。
- validation: 新矩阵 1294 行；原 blocked 行解决/排除 13 行，新增 9 行 `target_component`；included 522、module-boundary-excluded 726、blocked 40、reference-only 6；目标 included 为 B2 213、B3 171、B4_CULTURE 138；题号 gap 剩余 0，重复题号键 0，重复组件键 0。审计证据回填已修补，小问行可回退到 `subquestion_split_matrix.csv` 取证，两张审计表空证据行为 0。最终闭环仍被 40 行 blocked 队列阻止。

## D029 - 源明示清理矩阵

- time: 2026-06-17 15:42 +08:00
- decision: 生成 `SOURCE_EXPLICIT_CLEANUP_COVERAGE_MATRIX.csv` 作为最新接手矩阵；只处理设问、答案或细则明确限定 B2/B3/边界模块的整题，或同一大题中可明确抽出的 B2/B3 目标组件。
- reason: `remaining_strong_cleanup_blocked_queue.csv` 中仍有一批主观题已经由设问或细则明确模块，可以安全入账；但同一 suite_id 下期中/期末混叠、客观题答案键依赖、以及小问切分错位风险不能用规则强关。
- validation: 新矩阵 1300 行；原 blocked 行解决/排除 17 行，新增 6 行 `target_component`；included 536、module-boundary-excluded 735、blocked 23、reference-only 6；目标 included 为 B2 217、B3 181、B4_CULTURE 138；题号 gap 剩余 0，重复题号键 0，重复组件键 0。两张 source-explicit 审计表空证据行为 0。最终闭环仍被 23 行 blocked 队列阻止。

## D030 - 2025 海淀期中/期末身份修复与 Q22 文化组件补抽

- time: 2026-06-17 16:01 +08:00
- decision: 生成 `SUITE_IDENTITY_CULTURE_REPAIRED_COVERAGE_MATRIX.csv` 作为最新接手矩阵；移除旧 `2025_海淀_期末` 中 22 行混叠记录，按真实文件重建 `2025_海淀_期中` 与 `2025_海淀_期末`，并补入 2025 海淀期末第 22 题的文化与必修三组件。
- reason: `2025_海淀_期末` suite_id 同时承载海淀期中 paper/rubric 与海淀期末 paper/rubric，导致同题号题干、答案和细则混在一起；旧矩阵不能靠重命名修复，必须移除污染行后重建。用户进一步提示“民族精神属于文化”，所以第 22 题综合短文中的 `中华优秀传统文化`、`中华民族精神`、`愚公精神` 必须作为文化组件入账，不能被哲学/综合题余项吞掉。
- validation: 新矩阵 1330 行；removed contaminated rows 22；`2025_海淀_期中` 当前 24 行，`2025_海淀_期末` 当前 28 行；included 554、module-boundary-excluded 750、blocked 20、reference-only 6；目标 included 为 B2 223、B3 190、B4_CULTURE 141；题号 gap 剩余 0，重复题号/组件键 0，matrix 与 coverage 完全一致，审计空证据行为 0。最终闭环仍被 20 行 blocked 队列阻止。

## D031 - 用户现场文化提示最终清理矩阵

- time: 2026-06-17 16:30 +08:00
- decision: 生成 `CULTURE_HINT_FINAL_CLEANUP_COVERAGE_MATRIX.csv` 作为最新接手矩阵，并同步到通用 `COVERAGE_MATRIX.csv` 与 `module_classification_matrix.csv`；按用户提示从题目与细则双向抽文化部分，解决/关闭 17 个原 blocked 行，新增 7 个目标/文化组件，删除 1 个冗余 B2 组件。
- reason: 哲学文化混合题不能被“哲学”外壳吞掉文化采分点。2025 海淀二模 Q16、2026 丰台一模 Q21、2026 丰台期末 Q16 等题的细则或讲评明确出现文化功能、中华优秀传统文化、美学智慧等文化内容，必须作为 B4_CULTURE 组件入账。但丰台一模 Q1、丰台期末 Q2/Q6 仍缺可靠答案键或选项拆分，不能为清零强判。
- validation: 新矩阵 1336 行；included 562、module-boundary-excluded 765、blocked 3、reference-only 6；目标 included 为 B2 225、B3 193、B4_CULTURE 144；culture_component 23、target_component 24；题号 gap 剩余 0，重复题号/组件键 0，matrix 与 coverage 完全一致，审计空证据行为 0，整题 included 边界污染 0。最终闭环仍被 3 行答案键/选项拆分 blocker 阻止。

## D032 - 最终答案键闭合矩阵

- time: 2026-06-17 17:00 +08:00
- decision: 生成 `FINAL_ANSWER_KEY_CLOSURE_COVERAGE_MATRIX.csv` 作为最新接手矩阵，并同步到通用 `COVERAGE_MATRIX.csv` 与 `module_classification_matrix.csv`；用可靠答案键闭合最后 3 条混合选择题 blocker。
- reason: 最后三题均为选择题，模块去向取决于正确项。找到 2026 丰台一模答案文本与 2026 丰台期末答案页后，可以按正确项拆出目标组件并关闭父题余项，避免继续把文化/B3 正确项悬空，也避免把哲学、必修一、选必三余项混入目标三类。
- validation: 新矩阵 1337 行；included 563、module-boundary-excluded 768、blocked 0、reference-only 6；目标 included 为 B2 225、B3 194、B4_CULTURE 144；culture_component 23、target_component 25；题号 gap 剩余 0，重复题号/小问/组件键 0，matrix 与 coverage 完全一致，审计空证据行为 0。

## D033 - Fable5 源缓存交接包

- time: 2026-06-17 17:29 +08:00
- decision: 生成 `06_fable5_source_cache`，把源文件级 AI-readable 缓存集中成 `fable5_ai_readable_source_cache.jsonl`，并修复 3 条原 `empty-or-unsupported` 缓存行。
- reason: 用户要求 Fable5 制作宝典时能在电脑里直接找到可读缓存，不再逐个 OCR PDF/PPTX；同时必须保证参考答案不冒充细则。现有最终矩阵已闭合题目覆盖，但缺少单独的 Fable5 入口文件和缓存覆盖验收。
- validation: `cache_manifest.csv` 中 `empty-or-unsupported` 为 0；fable5 JSONL 195 行，193 行 `ai_readable_text_ready`、2 行 `excluded_by_hard_rule`；`needs_repair_after_handoff` 为 0；最终 included 主观题使用 reference-answer 的行数为 0；最终矩阵证据路径缺失为 0。

## D034 - 2026 海淀期中/期末身份与 OCR 文化补丁

- time: 2026-06-17 17:52 +08:00
- decision: 生成 `HAIDIAN_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv`，把原 `2026_海淀_期末` 中混入的期中行拆回 `2026_海淀_期中`，并用 Apple Vision OCR 重建真实 `2026_海淀_期末` 题源行与文化组件。
- reason: 海淀期末试卷 PDF 无文本层，旧缓存只有短摘要/答案片段；继续沿用会让 Fable5 和矩阵把期中、期末证据混看。用户明确要求抽离题目与细则中的文化部分，民族精神属于文化，所以海淀期末第 17/18/19 等题的文化点必须组件化。
- validation: 新矩阵 1365 行，included 572、module-boundary-excluded 787、reference-only 6、blocked 0；B2/B3/B4_CULTURE 为 226/197/149；重复键 0；海淀期末 OCR 写入 `02_text_cache/ocr_cache/2026_海淀_期末_试卷/试卷.ocr.txt`。

## D035 - 2026 朝阳期中/期末身份与 OCR 文化补丁

- time: 2026-06-17 18:01 +08:00
- decision: 生成 `CHAOYANG_2026_IDENTITY_OCR_CULTURE_PATCHED_COVERAGE_MATRIX.csv`，把原 `2026_朝阳_期末` 中 22 行实际期中矩阵行拆回 `2026_朝阳_期中`，并用真实朝阳期末 OCR 重建 28 行。
- reason: source_inventory/cache/question_candidates 中 `2026_朝阳_期末` 同时含 `2026朝阳期中` 和 `2026朝阳期末` 源；若只看最终矩阵，会把真实朝阳期末整卷漏掉。朝阳期末试卷和细则都是扫描 PDF，必须回源 OCR 后才能抽离文化/B2/B3 组件。
- validation: 新矩阵 1393 行，included 586、module-boundary-excluded 801、reference-only 6、blocked 0；B2/B3/B4_CULTURE 为 231/202/153；重复键 0；朝阳期末 OCR 写入 `02_text_cache/ocr_cache/2026_朝阳_期末_试卷/试卷.ocr.txt` 与 `02_text_cache/ocr_cache/2026_朝阳_期末_细则/细则.ocr.txt`。

## D036 - 源层期中/期末身份必须同步修复

- time: 2026-06-17 18:02 +08:00
- decision: 对 `source_inventory.csv`、`SOURCE_LEDGER.csv`、`cache_manifest.csv`、`question_candidates.csv` 同步修复 2025 海淀、2026 海淀、2026 朝阳的期中/期末身份，不能只修覆盖矩阵。
- reason: Fable5 和未来宝典会优先读取源缓存和候选索引；如果源层仍混着期中/期末，矩阵层闭合也会在下游重新污染。
- validation: 身份交叉扫描通过：上述五个文件中，`2025_海淀_期末` 含 `2025海淀期中` 为 0，`2026_朝阳_期末` 含 `2026朝阳期中` 为 0，`2026_海淀_期末` 含 `2026海淀期中` 为 0。

## D037 - Fable5 全源 sha 对账闭合

- time: 2026-06-17 18:06 +08:00
- decision: 生成 `fable5_missing_source_cache_completion_report.md`，将 source_inventory 的 194 个唯一 sha 全部补齐进 `cache_manifest.csv` 和 Fable5 JSONL；P7 原结论降级为历史阶段，由 P9 替代。
- reason: 仅验证 JSONL 可解析和 `needs_repair=0` 不足以证明 Fable5 有完整源缓存；对账发现 source_inventory unique sha 194，而当时缓存只覆盖 171 个唯一 sha。缺的 23 个唯一源若不补齐，Fable5 仍可能回到逐个打开/OCR 原文件。
- validation: 最终 source_inventory unique sha 194、cache unique sha 194、Fable5 unique sha 194；Fable5 JSONL 194 行、0 个解析错误、1,091,691 个嵌入文本字符；handoff status 为 `ai_readable_text_ready` 193、`excluded_by_hard_rule` 1、`needs_repair` 0；`empty-or-unsupported` 0；included 主观题 reference-answer 来源 0。
