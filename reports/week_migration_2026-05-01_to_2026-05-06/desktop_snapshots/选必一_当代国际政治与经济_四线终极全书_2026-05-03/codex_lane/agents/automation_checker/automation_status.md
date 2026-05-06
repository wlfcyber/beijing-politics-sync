# Codex Lane A 自动化检测台账

检测时间：2026-05-03 18:38 CST

运行目录：`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

角色：Codex production lane A 内部智能体【自动化检测者】

本轮检测原则：只检测控制文件、目录、角色文件、source ledger、coverage、screen/ClaudeCode 可读状态；不改动其他文件，不回滚任何已有内容。

## 1. 当前总判定

状态：BOOTSTRAP_SHELL_PRESENT_BUT_NOT_RUN

含义：本轮目录骨架、控制文件、coverage 文件、delivery/review 占位文件和 Codex A 内部角色目录已建立，但核心证据台账和覆盖台账基本只有表头或标题，尚不能证明已经开始真实源扫描、条目提取、覆盖闭环、Governor 或 Confucius 验收。

## 2. 每轮必须核对的文件

### 2.1 控制与总规则

- `TASK_BRIEF.md`
- `MASTER_REQUIREMENTS.md`
- `RUN_MANIFEST.json`
- `00_control/RUN_MANIFEST.yaml`
- `00_control/START_CARD.md`
- `00_control/EVIDENCE_PRIORITY_RULES.md`
- `00_control/GOVERNOR_GATES.md`
- `00_control/NOTEBOOK_DIGEST.md`
- `00_control/DECISION_LOG.md`
- `00_control/MODEL_ADVICE_LOG.md`
- `00_control/PROGRESS_LEDGER.jsonl`
- `00_control/ZERO_START_DECLARATION.md`
- `USER_FRAMEWORK.md`
- `USER_QUESTIONS.md`

### 2.2 源扫描与证据

- `01_source_inventory/SOURCE_INVENTORY.csv`
- `01_source_inventory/FILE_TYPE_ROUTING.csv`
- `SOURCE_LEDGER.csv`
- `02_extraction/failed_extractions.md`
- `03_entries/evidence_level_index.csv`

每轮检查点：是否只有表头；是否有真实 source_id；是否记录 P0/P1/P2/P3/P4 证据层级；是否把参考答案冒充评分细则；是否登记不可读文件、图片表格、PPT、OCR 风险。

### 2.3 覆盖与套卷闭环

- `COVERAGE_MATRIX.csv`
- `04_suite_reports/suite_completion_matrix.csv`
- `05_coverage/coverage_by_book_unit.csv`
- `05_coverage/coverage_by_evidence_level.csv`
- `05_coverage/coverage_by_question_type.csv`
- `05_coverage/coverage_by_year_district_exam.csv`
- `05_coverage/missing_questions.md`
- `05_coverage/unresolved_blockers.md`

每轮检查点：是否有真实题目覆盖；是否标明已排除、blocked、reference-only、P0 已闭环；是否把 2026 石景山期末全模块排除；是否列出 2024-2026 北京区级源的缺口。

### 2.4 冲突、复核与外部审稿

- `06_conflicts/conflict_register.md`
- `06_conflicts/resolved_conflicts.md`
- `06_conflicts/unresolved_conflicts.md`
- `08_review/claude_context_pack.md`
- `08_review/claude_advice.md`
- `08_review/codex_response_to_advice.md`
- `08_review/gpt_context_pack.md`
- `08_review/gpt_advice.md`
- `08_review/gpt_phase_fallback_log.md`
- `08_review/gpt_content_review/gpt_content_review_index.md`
- `08_review/gpt_content_review/content_correction_log.md`
- `08_review/confucius_report.md`
- `08_review/confucius_fix_log.md`

每轮检查点：外部建议是否落盘；Codex 是否逐条响应；must_fix 是否闭环；被拒绝建议是否有本地证据理由；Confucius 是否从学生迁移性角度验收。

### 2.5 学生文档与交付

- `07_student_doc/student_doc_outline.md`
- `07_student_doc/student_doc_draft.md`
- `07_student_doc/student_doc_final.md`
- `07_student_doc/glossary.md`
- `09_delivery/delivery_manifest.md`
- `09_delivery/acceptance_report.md`
- `09_delivery/word_visual_check.md`
- `09_delivery/pdf_visual_check.md`
- `FINAL_ACCEPTANCE_REPORT.md`

每轮检查点：学生版是否仍按六桶组织；每条是否有“术语、完整设问、细则位置、来源、材料触发、答案句、表述积累”；是否出现后台词、本地路径、debug、模型聊天；Word/PDF 是否完成渲染验收。

### 2.6 Codex A 内部角色文件

- `codex_lane/agents/ROLE_LEDGER.md`
- `codex_lane/agents/decision_maker/`
- `codex_lane/agents/worker/`
- `codex_lane/agents/patcher/`
- `codex_lane/agents/governor/`
- `codex_lane/agents/automation_checker/automation_status.md`

每轮检查点：五角色是否各有任务产物；决策者是否给出下一瓶颈；劳动者是否有源处理日志；补丁者是否查误拆/误合并/框架错位；Governor 是否有否决记录；自动化检测者是否更新本台账。

### 2.7 ClaudeCode / screen 状态

- `screen -ls`
- `ps aux | rg -i "claude|claudecode|codex|screen"`
- `claudecode_lane/logs/`

每轮检查点：是否有可 attach 的 screen 会话；ClaudeCode 是否真实运行；是否有日志落盘；如果只看到 Claude 桌面进程而没有 ClaudeCode/screen 日志，不能判定 ClaudeCode lane 已启动。

## 3. 当前已确认存在

- 主控制文件存在：`TASK_BRIEF.md`、`MASTER_REQUIREMENTS.md`、`RUN_MANIFEST.json`、`00_control/RUN_MANIFEST.yaml`、`00_control/START_CARD.md`、`00_control/EVIDENCE_PRIORITY_RULES.md`、`00_control/GOVERNOR_GATES.md`。
- 源扫描与覆盖文件存在：`SOURCE_LEDGER.csv`、`COVERAGE_MATRIX.csv`、`01_source_inventory/SOURCE_INVENTORY.csv`、`04_suite_reports/suite_completion_matrix.csv`、`05_coverage/*.csv`、`missing_questions.md`、`unresolved_blockers.md`。
- Codex A 内部角色目录存在：`automation_checker`、`decision_maker`、`governor`、`patcher`、`worker`。
- `codex_lane/agents/ROLE_LEDGER.md` 存在。
- 学生文档、review、delivery 文件壳存在。

## 4. 当前缺口

1. `SOURCE_LEDGER.csv` 只有 1 行表头，没有真实源记录。
2. `COVERAGE_MATRIX.csv` 只有 1 行表头，没有真实题目覆盖记录。
3. `01_source_inventory/SOURCE_INVENTORY.csv` 只有 1 行表头，尚未形成源文件库存。
4. `04_suite_reports/suite_completion_matrix.csv` 只有 1 行表头，没有套卷完成状态。
5. `05_coverage/coverage_by_book_unit.csv`、`coverage_by_evidence_level.csv`、`coverage_by_question_type.csv`、`coverage_by_year_district_exam.csv` 均只有表头。
6. `05_coverage/missing_questions.md` 和 `05_coverage/unresolved_blockers.md` 只有标题，没有真实缺口/阻塞登记。
7. `00_control/PROGRESS_LEDGER.jsonl` 为 0 行。
8. `00_control/NOTEBOOK_DIGEST.md`、`00_control/DECISION_LOG.md`、`00_control/MODEL_ADVICE_LOG.md` 当前为空壳。
9. `USER_FRAMEWORK.md` 仍是占位说明，没有吸收用户六桶、硬样本和边界规则的可执行版本。
10. `RUN_MANIFEST.json` 标记 `status: not_started`，但 `00_control/RUN_MANIFEST.yaml` 标记 `codex_line_status: running`，状态不一致。
11. `00_control/RUN_MANIFEST.yaml` 存在重复 `mode:` 字段，其中一个为空，需后续由决策者修正。
12. `codex_lane/agents/decision_maker/`、`worker/`、`patcher/`、`governor/` 当前无角色产物文件。
13. `claudecode_lane/logs/` 未发现日志文件；`screen -ls` 返回无可用 socket。
14. 进程层面可见 Claude 桌面应用进程，但未见可读 ClaudeCode/screen 会话，不能证明 ClaudeCode lane 已经开始生产。
15. `07_student_doc/student_doc_draft.md`、`student_doc_final.md`、`glossary.md`、`09_delivery/*`、`08_review/confucius_report.md`、`confucius_fix_log.md` 当前均为标题壳，不能作为完成证据。
16. `FINAL_ACCEPTANCE_REPORT.md` 仅有标题，尚不能宣称最终验收。

## 5. 下一轮自动检测最低通过线

下一轮至少应看到：

1. `SOURCE_LEDGER.csv` 有真实源记录，且包含 evidence_type/status/notes。
2. `01_source_inventory/SOURCE_INVENTORY.csv` 有真实文件库存，且标明 has_answer/has_rubric/has_lecture。
3. `COVERAGE_MATRIX.csv` 至少有首批题目记录，能区分 codex_entry、claudecode_entry、fusion_status、evidence_status。
4. `00_control/PROGRESS_LEDGER.jsonl` 至少有本轮启动、源扫描、覆盖状态三类事件。
5. `05_coverage/unresolved_blockers.md` 明确写出未闭环源、不可读源、reference-only 源，而不是空白。
6. Codex A 五角色至少各有一个可读产物或明确的待启动状态说明。
7. 若 ClaudeCode 仍不可读，必须在 `claudecode_lane/logs/` 或控制文件中写明 fallback/blocked 状态。

## 6. 下一步叫醒指令模板

```text
你是 Codex production lane A 决策者。运行目录：
/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03

先读取：
1. MASTER_REQUIREMENTS.md
2. 00_control/RUN_MANIFEST.yaml
3. 00_control/EVIDENCE_PRIORITY_RULES.md
4. codex_lane/agents/automation_checker/automation_status.md
5. SOURCE_LEDGER.csv
6. COVERAGE_MATRIX.csv
7. 01_source_inventory/SOURCE_INVENTORY.csv
8. 05_coverage/unresolved_blockers.md

任务：
不要从学生文档开始写。先修正运行状态不一致，补真实源库存和 source ledger 的首批记录，建立 progress jsonl 事件，并给 worker 分配第一批可回源的 P0/P1 题目。禁止覆盖旧成果，禁止把参考答案冒充评分细则。完成后只写本轮新增/更新文件清单。
```

## 7. 自动化检测者给下一角色的简令

下一角色优先级：决策者 -> 劳动者 -> 补丁者 -> Governor -> 自动化检测者复检。

立即动作：不要宣称已跑完整本；先把空 ledger 变成可审计 ledger，再让学生文档生产线启动。
