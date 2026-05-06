你是 ClaudeCode 生产线 B，不是审稿人。你不是独自一个人在代码库里，Codex A 线正在并行处理本轮任务；不要回滚、覆盖或重写别人正在维护的文件。你的写入范围只限于：

- `claudecode_lane/`
- 必要时可在 `claudecode_lane/tmp/` 下生成临时抽取文件

本轮工作目录：

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维双线四线终极跑_2026-05-04`

最高优先级规则：

1. 读取并服从 `MASTER_REQUIREMENTS.md`、`USER_FRAMEWORK.md`、`/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`。
2. 选必三《逻辑与思维》拆成两线：
   - 思维部分：完全按必修四哲学最终工作流同构处理，把每个思维/方法当作“原理+方法论”，做材料触发链。
   - 推理部分：按题型族群总结，三段论、假言推理、选言推理、归纳推理、类比推理、逻辑三律、换质换位等同类放一起。
3. 旧选必三稿只可当定位索引，不可当证据或结论。每个候选必须回到本地试卷、答案、细则、评标、讲评或可靠客观答案源核验。
4. PDF、Word、PPT、图片、扫描件、表格等都要调动可用工具处理；某个工具缺失不能成为直接放弃理由。
5. 学生版最终不得有路径、line id、OCR/debug、A-formal、评标、参考答案、可从……角度作答等审计话术。
6. 不处理 `2026石景山期末`，除非用户提供新的评分细则来源。

你现在的生产任务：

一、框架确认

- 读取用户上传的两份 PDF 源及 Codex 已抽取文本：
  - `00_source_pdfs/逻辑与思维_思维部分_原文件.pdf`
  - `00_source_pdfs/逻辑与思维_推理部分_原文件.pdf`
  - `02_extraction/pdf_text/`
- 写 `claudecode_lane/framework_reading_report.md`，确认你吸收的思维框架与推理框架。不要只是复述目录，要说明“思维部分如何按哲学触发链处理、推理部分如何按题型族群处理”。

二、独立候选扫描

- 先读 Codex A 已生成的候选账作为索引，但不要照抄结论：
  - `01_source_inventory/logic_candidate_hits_enriched.csv`
  - `01_source_inventory/thinking_candidate_hits.md`
  - `01_source_inventory/reasoning_candidate_hits.md`
- 再独立扫描本机 2024-2026 北京区卷/cache。优先使用已有文本缓存，必要时回原始文件。
- 输出：
  - `claudecode_lane/thinking_candidate_matrix.csv`
  - `claudecode_lane/reasoning_type_matrix.csv`
  - `claudecode_lane/source_gap_and_blockers.md`
  - `claudecode_lane/conflict_candidates.md`
  - `claudecode_lane/progress.md`

三、矩阵字段要求

`thinking_candidate_matrix.csv` 字段：

`suite,question,source_kind,evidence_level_candidate,framework_node,material_action,trigger_logic_short,student_answer_direction_short,original_source_path_or_cache,needs_original_recheck,notes`

`reasoning_type_matrix.csv` 字段：

`suite,question,reasoning_family,rule_or_error,tested_move,common_trap,solution_protocol,original_source_path_or_cache,needs_original_recheck,notes`

四、阶段结论要求

- 最后在 `claudecode_lane/progress.md` 写清：
  - 你确认的高优先思维题有哪些；
  - 你确认的高优先推理题型族群有哪些；
  - 哪些必须回源核验；
  - 哪些看起来是跨模块/边界，不能进思维主链；
  - 你改动/创建了哪些文件。
- 不要生成最终学生稿，不要写 TASK_COMPLETE。当前只做 B 线生产候选与闭环准备。
