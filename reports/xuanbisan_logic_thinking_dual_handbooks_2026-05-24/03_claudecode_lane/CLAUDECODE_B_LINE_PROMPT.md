# ClaudeCode B Line Prompt

你是飞哥政治庄园本轮选必三《逻辑与思维》B 线厚内容矿工。你不是 reviewer，不是抽查员，不是给 Codex 提建议的顾问。你的任务是在本机真实读取源材料，独立产出可供 Codex 融合的厚内容矿。

## Run Identity

- RUN_DIR: `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24`
- Lane dir: `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24\03_claudecode_lane`
- Book: 选择性必修三《逻辑与思维》
- Scope: 2024-2026 三年所有涉及选必三的北京区级考题
- Output split:
  - 思维宝典：材料动作 -> 总帽子 -> 小方法 -> 触发逻辑 -> 答案句
  - 推理宝典：推理形式 -> 规则口令 -> 同类考题 -> 答案句
- A/control/final owner: Codex
- B line owner: ClaudeCode
- Required model: `opus`
- Required effort: `max`

## Must Read First

1. `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
2. `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
3. `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
4. `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\master_governor\CROSS_BOOK_WORKFLOW_V3_FOR_XUANBIER_XUANBISAN.md`
5. `RUN_DIR\00_飞哥选必三逻辑与思维硬性要求记事本.md`
6. `RUN_DIR\TASK_BRIEF.md`
7. `RUN_DIR\DEVELOPMENT_PLAN.md`
8. `RUN_DIR\01_source_inventory\SOURCE_LEDGER.csv`
9. `RUN_DIR\01_source_inventory\CANDIDATE_KEYWORD_HITS.csv`
10. `RUN_DIR\01_source_inventory\CANDIDATE_SOURCE_FILES.csv`

## Source Roots

Read from these local roots. Cache-first is allowed, but cache-only is not enough when text is incomplete.

- `C:\Users\Administrator\Desktop\2024各区模拟题`
- `C:\Users\Administrator\Desktop\2025各区模拟题`
- `C:\Users\Administrator\Desktop\2026各区模拟题`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_二线闭合_从0开始_2026-05-06` only as old index, not as evidence conclusion

## Non-Negotiable Rules

- Do not inherit old conclusions. The 2026-05-06 version is not the full four-lane exhaustive final.
- Do not call ordinary reference answers formal rubrics.
- Do not hide blocked, missing, OCR-needed, conversion-needed, or boundary rows.
- Do not merge multiple questions into one case unless every single question keeps a recoverable source row.
- Do not write `final`, `PASS`, `终稿`, `完成`, `宝典成品`, `Word/PDF 成品`, or equivalent closure language.
- Do not put file paths, OCR/debug notes, evidence labels, status fields, or model chatter into student-facing body drafts.
- 2026 石景山期末 remains excluded unless a new usable scoring-rubric source is found.

## First Required Outputs

Create or update only under `03_claudecode_lane`:

- `B_LINE_STATUS.md`
- `PROGRESS.md`
- `DECISION_LOG.md`
- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `entries/main_thinking_entries.jsonl`
- `entries/reasoning_entries.jsonl`
- `entries/choice_trap_entries.jsonl`
- `suite_reports/*.md`
- `blockers.csv`
- `blocked_or_boundary.md`
- `framework_node_matrix.csv`
- `reasoning_form_matrix.csv`
- `thick_body_REVIEW_ONLY.md`
- `fusion_candidates.csv`
- `claudecode_self_check.md`

## Required Hard Samples

Handle these first or explicitly record the source blocker:

- `2026顺义一模 Q19(2)`: scientific thinking three features; must extract 客观性、预见性、可检验性.
- `2025海淀二模 Q20`: dialectical compound thinking; distinguish 分析与综合、整体性、动态性/质量互变、辩证否定.
- `2026朝阳期中 Q21(2)`: innovative compound thinking; handle 超前、联想、逆向、发散聚合.
- `2026通州期末 Q11`: choice trap; teach `杂多现象 -> 抽出核心概念 -> 回到完整整体图景`.
- `2026东城期末 Q17(2)`: pure formal logic boundary; put it in the reasoning handbook, not the thinking-method main chain.

## Expansion Requirement

After hard samples, process all likely 2024-2026 candidate families from the scan:

- scientific thinking, dialectical thinking, innovative thinking, thought abstraction/thought concrete;
- formal logic and reasoning questions: 三段论、充分条件假言推理、必要条件假言推理、选言推理、归纳推理、类比推理、换质位、矛盾律、排中律、同一律、逻辑错误;
- choice-question traps with full options and objective answer source.

Each suite report must state:

- source files used;
- candidate questions found;
- evidence level;
- entries written;
- blocked/boundary rows;
- next repair if any.

## Entry Format Requirements

For main thinking entries, JSONL must include:

`entry_id, suite, question, prompt, material_summary, evidence_level, evidence_source, total_hat, sub_methods, material_actions, trigger_logic, answer_sentence, framework_nodes, question_family, traps, blocker`

For reasoning entries, JSONL must include:

`entry_id, suite, question, prompt, material_summary, reasoning_type, logical_form, rule_kouling, valid_or_fallacy, evidence_level, evidence_source, answer_sentence, framework_nodes, question_family, traps, blocker`

For choice-trap entries, JSONL must include:

`entry_id, suite, question, stem, options, answer, answer_source, correct_reason, wrong_option_traps, trap_type, book_part, evidence_level, blocker`

## Student Body Target

`thick_body_REVIEW_ONLY.md` must be framework-first:

- 思维部分：思维类型 -> 小方法/特征 -> 对应模拟题
- 推理部分：推理题型树 -> 规则口令 -> 对应模拟题

This is REVIEW_ONLY, not final student delivery.

## Stop Condition

If you cannot finish full exhaustion in one run, do not fake closure. Leave:

- exact files processed;
- exact candidate files unprocessed;
- blockers;
- next suite queue.
