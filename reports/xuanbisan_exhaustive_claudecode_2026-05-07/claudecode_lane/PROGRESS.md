# PROGRESS — ClaudeCode 厚内容矿（B 线）

本文件按套卷推进，不写"整本完成"。任何时候 PROGRESS 与 entries/suite_reports/coverage 不一致都按硬失败处理。

## 2026-05-07 启动

- 已读 SKILL：`feige-politics-garden`、`feige-politics-garden-xuanbisan`、`xuanbisan-hard-rules-notebook.md`。
- 已读上层 `TASK_BRIEF.md`、`PROGRESS.md`、`codex_audit/穷尽性审计.md`，全部确认 NOT_EXHAUSTIVE。
- 已读 GitHub 同步控制文件：`phase03_question_coverage_matrix.csv`（528 行 control base）、`phase03_thinking_signal_chain_matrix.csv`（73 行）、`missing_questions.md`、`blocked_questions.csv`。
- 已扫本机题源根目录，并核对 `preprocessed_corpus`（153 个 cached texts）。

### 关键事实

- 528 行 control base 来自 17 套卷：2024 朝阳一模/二模/期中、2024 海淀二模、2024 西城一模、2025 东城期末、2025 丰台期末、2025 海淀二模/期末、2025 西城二模、2025 顺义一模、2026 东城一模/期末、2026 丰台一模、2026 朝阳期中、2026 通州期末、2026 顺义一模。
- 本机另有 30+ 套卷可走（2026 海淀期末/期中/一模、2026 西城期末/一模、2026 朝阳期末/一模、2026 丰台期末、2026 延庆/房山/石景山/门头沟一模、2025 海淀一模/西城一模/东城一模/丰台一模/朝阳一模、2025 朝阳期末/西城期末/海淀期中、2024 海淀一模/朝阳一模/东城一模/丰台一模/石景山一模/海淀期中、2024 朝阳二模/东城二模/西城二模/顺义思政二模、2025 东城二模/朝阳二模/丰台二模/昌平二模 等）。本轮先按 17 套卷出结论，再按时间允许扩展。
- `2026 二模`：本机 `2026各区模拟题` 目录下没有任何 `*二模*` 文件；写入 BLOCKED_OR_BOUNDARY.md。
- `2026 石景山期末`：用户已确认无可用评分细则，模块整体排除（试卷有 cached text，但不进入主链）。

### 口径

- A-formal：正式细则 / 评标 / 阅卷总结。
- A-support：讲评 PPT 有明确给分口径。
- B-choice-signal：试卷 + 客观答案表 (教师版) 同时具备。
- C-boundary：纯形式逻辑 / 推理规则 / 必修四哲学 / 选必一二法律国政经题。
- missing：题面/答案/细则任一缺失或 OCR 不可靠。
- 学生稿不写"固定分析流程"这个栏目；条目仍要写清材料怎么看、用哪个方法、为什么触发、答案句怎么写、易错项怎么避，但不用此标签。

### 推进顺序（按套卷闭环）

1. ✅ 17 套 control-base 套卷逐套关闭（每套 suite_report 已写入 `suite_reports/<套卷>.md`）。
2. ⏳ 73 行 thinking_signal_chain matrix 状态改写（合并到 528-row coverage matrix 的本轮结论中）。
3. ⏳ 处理本机额外 30+ 套卷（all `not_in_control_base`，本轮以 SOURCE_LEDGER 列出题源；待 fusion 阶段决定是否扩展）。
4. ⏳ 2026 二模：本轮 source roots 未发现，写入 BLOCKED_OR_BOUNDARY.md。

## 套卷推进日志

### 关闭（17 套 control-base）

| 套卷 | 证据等级 | suite_report | entries | 备注 |
| --- | --- | --- | --- | --- |
| 2024朝阳一模 | A-formal | ✅ | E-2024朝阳一模-19-1, -19-2; C-2024朝阳一模-9 | Q19 4 子问；Q9 系统观念 |
| 2024朝阳二模 | A-formal partial | ✅ | C-2024朝阳二模-7 | Q7 三段论小项不当扩大；Q19 全部 C-boundary-other-module |
| 2024朝阳期中 | A-support | ✅ | E-2024朝阳期中-19（占位） | RTF 细则未拆题；fusion 前必须回源 |
| 2024海淀二模 | A-formal | ✅ | E-2024海淀二模-17-1, -17-2 | 硬样本：科学思维 SCIENCE_ONLY + 思维抽象与思维具体 |
| 2024西城一模 | A-formal not_in_control_base | ✅ | — | 不在控制矩阵；扩展候选 |
| 2025东城期末 | A-formal | ✅ | E-2025东城期末-16 | 登月服硬样本：创新思维多角度 |
| 2025丰台期末 | A-support | ✅ | E-2025丰台期末-16; C-2025丰台期末-7, -10 | 辩证思维多维'界'；Q7 唯物论伪装边界 |
| 2025海淀二模 | A-formal | ✅ | E-2025海淀二模-20 | 辩证思维多角度硬样本 |
| 2025海淀期末 | A-support | ✅ | E-2025海淀期末-17（占位） | PPTX 待按题号拆 |
| 2025西城二模 | A-support | ✅ | E-2025西城二模-16-2 | 充分条件假言推理 |
| 2025顺义一模 | A-support | ✅ | E-2025顺义一模-16 | 辩证否定；Q7 大项不当扩大警示 |
| 2026东城一模 | A-formal partial | ✅ | （Q19 4 子问占位） | 4 子问 PPTX 待汇总 |
| 2026东城期末 | A-formal | ✅ | E-2026东城期末-17-2, -21; C-2026东城期末-Q-逻辑思维 | 形式逻辑三主张诊断硬样本 + 综合题思维方法子角度 |
| 2026丰台一模 | A-support | ✅ | E-2026丰台一模-18-2 | 必要条件假言推理 + 三段论大项不当扩大 |
| 2026朝阳期中 | A-formal | ✅ | E-2026朝阳期中-20, -21-2; C-2026朝阳期中-13 | 辩证思维 + 创新思维双硬样本 |
| 2026通州期末 | A-formal | ✅ | C-2026通州期末-11, -9, -5, -8 | 思维抽象与思维具体永久硬样本 |
| 2026顺义一模 | A-formal | ✅ | E-2026顺义一模-19-2, -21 | 科学思维三性硬样本 + Q21'势'多角度 |

### 输出文件

- `PROGRESS.md`（本文件）
- `SOURCE_LEDGER.csv`：17 套 control-base + 30+ 扩展候选 + 2026 二模 blocked = 32 行
- `QUESTION_COVERAGE_MATRIX.csv`：528 行控制基本轮结论
- `MAIN_THINKING_LEDGER.csv`：18 条主观题厚内容
- `CHOICE_TRAP_LEDGER.csv`：13 条选择题陷阱
- `FRAMEWORK_NODE_MATRIX.csv`：按用户框架节点统计挂载
- `BLOCKED_OR_BOUNDARY.md`：2026 二模 + 2026 石景山期末 + 形式逻辑/其他模块边界
- `EXHAUSTIVENESS_AUDIT.md`：本轮能否穷尽 / 不能穷尽的具体原因 / 剩余缺口
- `entries/hard_samples.jsonl`：11 条硬样本
- `entries/additional_main.jsonl`：12 条增量主观题（含占位）
- `entries/additional_choice.jsonl`：9 条增量选择题（含待回源）
- `suite_reports/<套卷>.md`：17 份套卷报告

### 本轮分类分布（534 行 = 528 control base + 6 Phase12 canonical）

经 SUPERVISOR_PATCH_01 规整到 4 桶后：
- 入正文：80 行（A-formal/A-support/B-choice-signal）
- 同类索引：4 行（边界陷阱不进正文，进陷阱库）
- blocked：336 行（缺题面/选项/答案/细则/视觉核读；包括 6 行 Phase12 canonical 新增）
- excluded：114 行（纯形式逻辑 95 + 其他模块 19）

### 本轮**不能**穷尽的硬证据
- 2026 二模整批 blocked。
- 336 行 blocked 包括：约 117 行主观题（GitHub label 含思维方法术语但本轮未独立读完整子问细则）+ 约 213 行选择题（需回源补完整选项+正确项理由+错项陷阱，含6 行 Phase12 canonical）+ 部分题型未识别 blocked。
- 2025海淀期末 / 2024朝阳期中 / 2025西城二模 / 2025顺义一模 / 2026丰台一模 / 2026东城一模 等 PPTX/RTF 细则需 fusion 前按题号拆开。

不要把本轮交付当作终稿。下一轮进入 Codex 验真融合时，必须先解决 336 行 blocked 的回源缺口。

### SUPERVISOR_PATCH_01 状态
Codex 监管已发出 `SUPERVISOR_PATCH_01.md` (HARD_FAIL_NOT_CLOSED_YET)。本轮已：
- 补 6 行 Phase12 canonical 缺失 qids（全部 blocked）。
- `本轮结论` 字段规整到 4 桶。
- 行数从 528 升到 534，与 Codex union matrix 对齐。

监管的 PASS 条件仍未达：仍存在 336 行 blocked 需 fusion 前补完。
