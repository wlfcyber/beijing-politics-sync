# DECISION_LOG — ClaudeCode B 线（选必三双宝典）

run: `选必三双宝典_哲学宝典完全对齐返工_2026-05-25`
lane: `claudecode_lane/`
说明：本 log 只记录 B 线本轮做出的真实裁决，不复制 Codex 旧裁决。每条裁决都有 `decision`、`evidence` 和 `consequence`。

## D01 — 身份与边界

- 2026-05-26T20:05:00+08:00
- decision: 本线为 ClaudeCode B 线厚内容矿，不是 reviewer，不裁决 Codex 现有 Word/PDF 是否能进入最终交付。
- evidence: 11 号包 `CLAUDECODE_THICK_CONTENT_PROMPT_20260526.md` 与 `CLAUDECODE_THICK_CONTENT_TASK_BRIEF_20260526.md`。
- consequence: 本 lane 所有输出都标记 `B_LANE_THICK_MINING_FIRST_ROUND_READY_FOR_FUSION_NOT_END`；不写 `PASS`、`final`、`最终版`、`候选稿门禁通过`。

## D02 — 不继承旧正文结论

- 2026-05-26T20:08:00+08:00
- decision: Codex 现有 `05_candidate_md/` 两本候选稿与 `06_candidate_audit/` 的所有 `body` 结论一律不继承到 B 线 entries。
- evidence: 11 号包 `MASTER_REQUIREMENTS` B 节 `不得把 Codex 当前候选稿直接改写成 ClaudeCode 输出`。
- consequence: B 线 entries 的 `material_trigger`、`why_this_method`、`answer_landing`、`correct_reason`、`tempting_wrong_options` 必须重新撰写，不能复制 Codex 句式或顺序；如果发现 B 线写法与 Codex 写法实质相同，必须改写到差异化角度。

## D03 — Coverage 范围基线

- 2026-05-26T20:10:00+08:00
- decision: B 线 `COVERAGE_MATRIX.csv` 以本 run `00_control/QUESTION_COVERAGE_MATRIX.csv` 的 143 条 question 为基线，每条独立给出 `body / index / blocked / excluded` 一种结论，不留 `待定 / needs review / not represented`。
- evidence: 11 号包 `ACCEPTANCE_GATE` 2.2 节 `不得有 not represented、needs review、待定 无裁决残留`。
- consequence: 任何 B 线没把握的条目都必须落入 `blocked` 并写 `blocked_reason`；任何被 Codex 排除的 thinking choice 也必须显式出现在 B 线 COVERAGE 中，决策为 `excluded` 并写 `book/部分边界` 原因。

## D04 — 思维选择题边界

- 2026-05-26T20:12:00+08:00
- decision: 凡 `book_part=thinking` 且 `question_type=choice_question` 一律不进入 B 线 `thinking_main.jsonl`，也不进入 `reasoning_choice.jsonl` 正文；只在 COVERAGE 中标 `excluded`，理由 `out_of_thinking_handbook_scope_user_confirmed`。如该题同时具备稳定推理形式，则改挂为 `reasoning_choice` body；否则留为 boundary 索引。
- evidence: 选必三 hard-rule notebook 第十五条与 11 号包 `MASTER_REQUIREMENTS` `思维选择题默认不能进入思维宝典正文`。
- consequence: Codex 现稿若把思维选择题混进思维正文，B 线 `fusion_candidates.md` 必须列 `reject_or_block`。

## D05 — `2024海淀二模 Q17(1)` 三节点复挂

- 2026-05-26T20:15:00+08:00
- decision: `2024海淀二模 Q17(1)` 在 B 线 `thinking_main.jsonl` 中按 `客观性`、`探索性与方法更新`、`整体安排` 三个科学思维子节点复挂，每节点独立写四要件；不复刻 Codex 老稿出现的 `科学/创新/辩证三模块并列设问` 风险表达。
- evidence: 选必三 hard-rule notebook 第十六条与第十八条 `2024 海淀二模第17题第(1)问` 锁定为 `SCIENCE_ONLY_SOURCE_SUPPORTED`。
- consequence: 任何 B 线产出若把该题挂到创新思维或辩证思维节点，将被 `governor` 拒绝。

## D06 — `2025顺义一模 Q7` 谬误名称定向

- 2026-05-26T20:18:00+08:00
- decision: `2025顺义一模 Q7` 在 B 线 `reasoning_choice.jsonl` 中正向锁为 `大项不当扩大谬误名称纠错`；选项 A 的诱因解释只能写为 `把大项不当扩大误称为小项不当扩大`；同类题挂载只允许 `三段论周延规则 / 大项不当扩大 / 谬误名称纠错`。
- evidence: 选必三 hard-rule notebook 第十九条。
- consequence: B 线 `framework_node_matrix.csv` 的 `三段论结构题与谬误题` 节点把本题作为 representative entry；`fusion_candidates.md` 列 `replace_codex_thin_entry` 若 Codex 现稿出现误正向描述。

## D07 — 推理硬样本节点最小覆盖

- 2026-05-26T20:21:00+08:00
- decision: 推理 7 类必须覆盖：充分条件假言、必要条件假言、三段论（含谬误题）、类比、归纳、概念外延/定义、逻辑规律。每个节点至少 1 条 body 主观题或 body 选择题。
- evidence: 11 号包 `TASK_BRIEF` Hard Samples 与 `MASTER_REQUIREMENTS` D 节 Required Framework Nodes。
- consequence: 节点缺则在 `framework_node_matrix.csv` 标 `blocked_no_question` 并在 `blocked_or_boundary.md` 写出缺哪类证据；不许伪造题源。

## D08 — 证据等级保留

- 2026-05-26T20:24:00+08:00
- decision: B 线 entries 与 COVERAGE 全部保留五级证据等级 `A-formal / A-support / B-choice-signal / C-boundary / missing`，禁止把普通参考答案标 `A-formal`。
- evidence: 11 号包 `MASTER_REQUIREMENTS` F 节。
- consequence: 学生字段不能出现 `A-formal / B-choice-signal` 等等级缩写；它们只能出现在审计字段 `evidence_level`。

## D09 — `2024北京高考 Q19(2)` 缺细则

- 2026-05-26T20:27:00+08:00
- decision: `2024北京高考 Q19(2)` 评分细则在本机 run 内不可用，B 线 COVERAGE 决策 `blocked`，`blocked_reason=missing_official_rubric_for_2024_beijing_gaokao_q192`，不进 body。
- evidence: 当前 run `QUESTION_COVERAGE_MATRIX.csv` 第 30 行 `evidence_level=missing`，加上 hard-rule notebook 第二条 `普通参考答案不能冒充正式细则`。
- consequence: `blocked_or_boundary.md` 写明：等待用户提供正式细则或评标后再开题。

## D10 — `2024房山一模 Q20(1)` 汇编降级

- 2026-05-26T20:30:00+08:00
- decision: `2024房山一模 Q20(1)` 在本 run 标为 `B-compilation`，B 线 COVERAGE 决策 `excluded`，`excluded_reason=compilation_only_no_official_district_source`，不进 body，与 Codex 现稿决策一致但 B 线独立复核。
- evidence: 本 run `QUESTION_COVERAGE_MATRIX.csv` 与 hard-rule notebook 第二条 `分类汇编不作独立套卷`。
- consequence: `blocked_or_boundary.md` 写清；`fusion_candidates.md` 列 `keep_as_index`。

## D11 — Q0123/Q0137/Q0138 B-choice-signal 边界

- 2026-05-26T20:33:00+08:00
- decision: `2026海淀二模 Q4`、`2026顺义二模 Q6`、`2026顺义二模 Q7` 三条 `B-choice-signal` 选择题，在 B 线判 `index`（不进 body），并把题面、四选项、官方答案、错项分析写到 `reasoning_choice.jsonl` 审计字段下，便于 Codex 外审通过后再决定升级。
- evidence: 本 run `02_alignment_audit/COVERAGE_RESOLUTION_PATCH_20260526.md` 与 hard-rule notebook 第八条 `B-choice-signal 选择题不冒充主观题评分链`。
- consequence: `fusion_candidates.md` 标 `keep_as_index`。

## D12 — 输出 schema 严格按 11 号包

- 2026-05-26T20:36:00+08:00
- decision: `entries/*.jsonl` 字段名严格按 11 号包 `OUTPUT_SCHEMA` 英文字段名 + 中文字段值，不擅自加 `book`、`page`、`order` 等字段。
- evidence: 11 号包 `OUTPUT_SCHEMA` Section 1。
- consequence: schema 不匹配的字段全部进入 `audit_note`。

## D13 — fusion_candidates 7 类硬分类

- 2026-05-26T20:39:00+08:00
- decision: `fusion_candidates.md` 一律分入 7 类：`replace_codex_thin_entry`、`append_missing_material_trigger`、`append_missing_answer_landing`、`append_choice_wrong_option_reason`、`add_framework_node_mount`、`keep_as_index`、`reject_or_block`；每条必须写 ClaudeCode entry id + Codex 对应条目或缺口 + 建议动作 + 证据理由 + 学生版清洗注意。
- evidence: 11 号包 `OUTPUT_SCHEMA` Section 5 与 `ACCEPTANCE_GATE` 6 节。
- consequence: Codex 融合时可直接按 7 类入口取用。

## D14 — B 线本轮自检与禁词扫描

- 2026-05-26T21:30:00+08:00
- decision: B 线本轮完工自检按以下 6 项硬指标执行，确认满足后才把状态从 `IN_PROGRESS` 写成 `B_LANE_THICK_MINING_FIRST_ROUND_READY_FOR_FUSION_NOT_END`。
- evidence: 11 号包 `ACCEPTANCE_GATE` 全部 6 节。
- 自检结果：
  - 必备文件齐全：11/11 项必需文件存在；`suite_reports/` 7 份(5 硬样本套卷 + 2 汇总)；
  - COVERAGE：147 行全部带合法 `decision`(body/index/blocked/excluded) 与合法 `handbook_target`；
  - entries：thinking_main 31 + reasoning_main 31 + reasoning_choice 23 = 85 条 JSON 全部 valid；
  - 学生字段禁词扫描：`/Users/、C:\、OCR、debug、line id、file id、question_id、A-formal、B-choice-signal、评标、参考答案、答案写、PASS、final、候选稿门禁` 共 15 个禁词在 student-facing 字段中 **0 命中**；
  - framework_node_matrix：思维 20 节点 + 推理 13 节点共 33 行；`covered=29 / covered_by_support=3 / blocked_no_question=1`；blocked 节点写明缺哪类证据；
  - 硬样本出现次数：2026顺义一模 6 / 2025海淀二模 5 / 2026朝阳期中 4 / 2024海淀二模 5 / 2025顺义一模 1，全部到位。
- consequence: B 线本包可移交 Codex 进入融合阶段；但仍不得写 `PASS` / `final` / `最终版` / `候选稿门禁通过`，不得跳过 Codex 回源核验、外审、Word/PDF 重建与最终 acceptance。
