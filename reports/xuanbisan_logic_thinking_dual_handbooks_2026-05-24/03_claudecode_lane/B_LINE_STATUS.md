# B Line Status

- run_dir: `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24`
- lane: `03_claudecode_lane`
- owner: ClaudeCode (B line, 厚内容矿工)
- model: opus 4.7, effort max (per `claudecode_command.txt`)
- start_date: 2026-05-24
- scope: 2024-2026 北京各区考题中所有涉及选必三《逻辑与思维》的题目，双宝典（思维+推理）分册
- not_inherited: `选必三_逻辑与思维_二线闭合_从0开始_2026-05-06` 仅作旧索引，不作证据/结论
- closure_words_forbidden: `final / PASS / 终稿 / 完成 / 宝典成品 / Word/PDF 成品`

## Phase

- phase: PROD_THICK_MINE
- gate: not closed, not delivered, not reviewed

## Open Queue (must process or honestly mark blocked)

### Hard samples (前置必处理)

1. 2026顺义一模 Q19(2) — 科学思维三性
2. 2025海淀二模 Q20 — 辩证思维复合（分析与综合/整体性/动态性/质量互变/辩证否定）
3. 2026朝阳期中 Q21(2) — 创新思维复合（超前/联想/逆向/发散聚合）
4. 2026通州期末 Q11 — 思维抽象与思维具体 选择题陷阱
5. 2026东城期末 Q17(2) — 形式逻辑/推理 边界（推理册而非思维主链）

### Suite candidates (按 keyword hit ledger 优先级)

- 2024.11朝阳期中评标
- 2024朝阳一模、2024朝阳二模、2024海淀一模、2024海淀二模、2024丰台一模、2024丰台二模、2024西城一模、2024西城二模、2024东城一模、2024顺义二模
- 2025朝阳期中、2025朝阳一模、2025朝阳二模、2025朝阳期末、2025海淀期末、2025海淀一模、2025海淀二模、2025丰台一模、2025丰台二模、2025丰台期末、2025西城一模、2025西城二模、2025西城期末、2025东城一模、2025东城二模、2025东城期末、2025石景山一模、2025昌平二模、2025顺义一模、2025顺义二模、2025延庆一模、2025门头沟一模、2025房山一模
- 2026朝阳期中、2026朝阳一模、2026朝阳期末、2026海淀期中、2026海淀期末、2026海淀一模、2026丰台期末、2026丰台一模、2026西城期末、2026西城一模、2026东城期末、2026东城一模、2026通州期末、2026通州一模、2026顺义一模、2026石景山一模、2026延庆一模、2026门头沟一模、2026房山一模

### Exclusions

- 2026石景山期末：user 已确认无可用细则；除非新源出现，本轮排除。
- 必修四哲学题、选必一、选必二、政治与法治、经济与社会题：作为边界记录，不入思维主链。

## Output contract

- `entries/main_thinking_entries.jsonl`
- `entries/reasoning_entries.jsonl`
- `entries/choice_trap_entries.jsonl`
- `suite_reports/<suite>.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `framework_node_matrix.csv`
- `reasoning_form_matrix.csv`
- `blockers.csv`
- `blocked_or_boundary.md`
- `fusion_candidates.csv`
- `thick_body_REVIEW_ONLY.md`
- `claudecode_self_check.md`
- `PROGRESS.md`
- `DECISION_LOG.md`

## Hand-off rule

- 任一 entry 须可被 Codex A 线回源核验；若无法回源，必须落入 blockers。
- 不允许把代表例集合冒充全量穷尽。
- 不允许把普通参考答案包装成 `A-formal`。
- 不允许把状态字段、路径、OCR、模型话术写入 thick body。
