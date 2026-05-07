你是本机真实 ClaudeCode 厚内容矿工。任务是为飞哥政治庄园选必三《逻辑与思维》做二线闭合中的 B 线厚内容，不是审美排版，不是终稿生成。

## 最高规则

1. 读取并遵守：
   - `C:\Users\Administrator\.codex\skills\feige-politics-garden\SKILL.md`
   - `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\SKILL.md`
   - `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbisan\references\xuanbisan-hard-rules-notebook.md`
2. 用户最新纠偏优先：当前返修稿没有穷尽题源，不能继续写“终稿/宝典成品/PASS/最终版/已穷尽”。
3. 本轮只做二线：ClaudeCode 厚内容矿 + Codex 验真融合。不要启动四线终极，不假装 GPT-5.5 Pro 或网页 Claude Opus 已参与。
4. 严格按用户给定的选必三框架组织厚内容：思维类型 -> 小方法/特点 -> 对应模拟题。不要把纯推理题型树当思维部分主体。
5. 学生正文或可融合正文中不要出现“固定分析流程”这个栏目或措辞。可以实质写清“材料怎么看、该用哪个方法、为什么触发、答案句怎么写、易错项怎么避”，但不要用这个被用户要求删除的标签。

## 本轮运行目录

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07`

你的输出写到：

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane`

## 必用源和索引

先读以下 GitHub 最新同步控制文件，不要从 33/29 旧稿开始自我确认：

- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\phase03_question_coverage_matrix.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\phase03_thinking_signal_chain_matrix.csv`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\missing_questions.md`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\week_migration_2026-05-01_to_2026-05-06\desktop_snapshots\选必三逻辑与思维_四线从0重跑_2026-05-04\05_coverage\blocked_questions.csv`

再读本机源：

- `C:\Users\Administrator\Desktop\2024各区模拟题`
- `C:\Users\Administrator\Desktop\2025各区模拟题`
- `C:\Users\Administrator\Desktop\2026各区模拟题`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`
- `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\artifacts`

## 必须完成的文件

在 `claudecode_lane` 下写：

1. `PROGRESS.md`：按套卷推进，不要泛泛写“完成”。
2. `SOURCE_LEDGER.csv`：源文件、套卷、题号、题面、答案、细则、讲评、缓存/原文状态。
3. `QUESTION_COVERAGE_MATRIX.csv`：从 528-row control base 出发，每行必须有 `入正文 / 同类索引 / blocked / excluded` 的当前结论或明确待补原因。
4. `MAIN_THINKING_LEDGER.csv`：主观题/子问的思维方法链，字段至少包含来源、设问、材料动作、总帽子、小方法、触发逻辑、答案句、证据等级、框架落点。
5. `CHOICE_TRAP_LEDGER.csv`：选择题题干、四个选项或四个选项单位、答案源、正确项理由、诱人错项、陷阱类型、是否可入学生稿。
6. `FRAMEWORK_NODE_MATRIX.csv`：按用户框架节点统计哪些题已挂载、哪些只有索引、哪些 blocked。
7. `BLOCKED_OR_BOUNDARY.md`：所有 blocked/excluded 行必须可追踪，尤其是 2026 二模、2026 石景山期末、纯形式逻辑、其他模块题。
8. `EXHAUSTIVENESS_AUDIT.md`：说明本轮能否穷尽、不能穷尽的具体原因、剩余缺口。
9. `suite_reports\<套卷名>.md`：每套卷必须写题源定位、题号筛选、证据判断、可入/不可入结论。
10. `entries\*.jsonl`：每条可融合厚内容一行 JSON，便于 Codex 后续融合。

## 分类规则

- 主观题：只有正式评分细则、评标、阅卷细则、阅卷总结、用户确认可用评分材料可作 `A-formal`。
- 讲评 PPT 有明确给分口径只能作 `A-support`。
- 普通参考答案不能冒充细则。
- 选择题必须有题面、选项、可靠客观答案源，才可写入 `B-choice-signal`。
- 纯形式逻辑、推理规则识别、小项/大项/中项谬误等，不能混入思维方法主链；但可进入推理/边界索引。
- 2026 石景山期末继续排除，除非发现用户提供的新评分细则。
- 2026 二模必须重新扫描本机源；若未发现，写明本轮扫描边界，不写成“尚未开考”。

## 输出风格

厚内容要像可融合进哲学宝典那样：每个条目都讲清材料怎么触发方法，答案句怎么落到卷面。不要写后台话术、不要写模型自夸、不要写终稿验收。

现在开始。先写 `PROGRESS.md` 的启动记录，再逐套卷推进。

