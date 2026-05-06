# Decision Maker Next Step - after Batch04L toward Batch04M and final gates

裁决时间：2026-05-04
角色边界：Codex A 决策者；只写下一步瓶颈、分批、启动顺序和放行条件；不改 fusion / student / delivery / coverage / progress 文件；不宣布最终完成。

## 1. 当前瓶颈裁定

当前第一瓶颈不是立刻进最终六桶，而是先把 Batch04L 的闭合状态同步清楚。

本地文件系统中已经出现 Batch04L ClaudeCode B 输出与 `06_conflicts/batch04L_claudecode_conflict_resolution.md`，且冲突裁决允许 L 进入 guarded 候选层；但当前 `task_plan.md`、`progress.md`、`COVERAGE_MATRIX.csv` 仍显示 Batch04L 为 `claudecode_pending / patcher pending / governor pending / prelim_guarded_candidate`。因此：

- 先由负责状态同步的生产/自动化线程把 Batch04L 记录更新为 A/B closure 后的 guarded closure 状态。
- Batch04L 只能是 `candidate_with_guard`，不得升级为逐点评分细则。
- 在 L 的 coverage/progress 状态未同步前，不进入六桶总融合、外部 final review、DOCX/PDF。

## 2. Batch04M 的最短补齐路径

Batch04M 定义为“剩余套卷最短路径补齐批”，不是新一轮无限扩源。

输入池以 `05_coverage/batch04M_remaining_deep_scan_sources.csv` 和 `05_coverage/batch04M_remaining_suite_term_hits.csv` 为准。处理原则：

- 只处理本地已有原始试卷/细则/评分参考。
- 只提升“明确选必一主观设问 + 评分细则/评标/阅卷总结/明确给分口径”的题。
- 等级题、答案及评分参考、PPTX讲评角度只能 guarded。
- 没有明确选必一设问或没有可审计评分位置的，立即写 boundary/reference-only/no_xuanbiyi，不做长线挖掘。
- `2026石景山期末`继续排除；`2026海淀期末`按用户既有复核倾向优先做 no_xuanbiyi/boundary 复核，不作为 M 的重点抽取对象。

## 3. Batch04M 分批顺序

M0：状态同步与启动清场

- 先同步 Batch04L A/B closure 结果。
- 确认当前没有 `xuanbiyi` ClaudeCode screen 正在写本 run；当前可见活跃 screen 是 `xuanbier`，不得混用为选必一证据。
- 冻结 M 的源清单，不再边跑边扩新目录。

M1：最短高收益必查组

1. `2026丰台期末`
   - P0 PDF 细则命中当代国际政治与经济、全球治理、联合国、多边主义、人类命运共同体等；试卷文本抽取弱，需优先视觉/渲染核题面。
2. `2025丰台期末`
   - P0 PPTX/评分材料命中和平与发展、共同利益、全球治理、共商共建共享、人类命运共同体、中国方案等；优先找主观题逐点口径。
3. `2025顺义一模`
   - P0 docx 片段已显出 Q20 的 8 分细则结构，含正确义利观、共商共建共享、构建人类命运共同体、国际关系民主化等；应优先抽。
4. `2025石景山一模`
   - P0 doc 命中全球治理、国际关系民主化、联合国、多边主义等；优先判 Q17(2) 一类明确细则题是否可入选必一。

M2：次高收益补齐组

5. `2024丰台二模`
   - P0 docx 中 Q19 明确为当代国际政治与经济，6 分、三个角度各 2 分；但试卷 PDF 抽取弱，需视觉确认题面。
6. `2024丰台一模`
   - P0 docx 中 Q20 供应链共赢链，含贸易投资自由化便利化、生产要素流动、经济全球化活力；评分更像等级/任选结构，默认 guarded。
7. `2025房山一模`
   - P0 PDF 命中和平与发展、经济全球化、全球治理、联合国、义利观、开放型世界经济；优先判是否有逐点细则。
8. `2025延庆一模`
   - P0 docx 命中时代主题、共同利益、国家利益、经济全球化、人类命运共同体、多边主义；快速筛是否存在明确选必一主观题。

M3：快速边界/guard 扫尾组

9. `2025丰台一模`
   - 命中丰富，但需区分是否已由 2026丰台一模/2025丰台二模覆盖同核心；只收新增 P0，不重复堆频。
10. `2024石景山一模`
    - PPTX 与试卷均命中较多，但先判是否为可审计评分位置；没有逐点口径则 guarded 或 boundary。
11. `2024顺义二模`
    - 命中较少，优先判是否只是选择题/材料词；无明确主观细则即 boundary。
12. `2025昌平二模`
    - 命中集中在国际竞争、两个市场两种资源；只做快速复核，避免把必修二开放表述硬塞选必一。
13. `2026海淀期末`
    - 当前扫描无有效选必一命中，且用户已复核倾向为没考选必一；只做关闭性边界记录，不投入深抽。

## 4. 何时启动 ClaudeCode B Batch04M

ClaudeCode B Batch04M 可以尽早启动，但必须满足三个条件：

1. Batch04L A/B closure 已被本地接收，并同步到 coverage/progress 或有明确交接文件说明“L 已闭合但待同步”。
2. Batch04M 的 M1/M2/M3 源清单已冻结，不再让 B 自行扩大源目录。
3. 当前没有正在写本 run 的 `xuanbiyi` ClaudeCode screen；若只有其他模块如 `xuanbier` screen 活跃，必须在 prompt 中写明 cross-thread guard，不得采信或覆盖其他模块输出。

启动方式：

- B 线与 Codex A Worker 可并行跑同一个 Batch04M 冻结清单，以缩短时间。
- B 线只写 `claudecode_lane/`、`04_suite_reports/claudecode_suite_reports/`、`06_conflicts/`。
- B 线任务重点不是产出漂亮正文，而是独立判定每套：`promote / guarded / boundary / no_xuanbiyi / reference-only / ocr-needed`。
- B 输出后再做 A/B difference table；没有 A/B 差异闭合，不得启动总融合。

## 5. 何时进入六桶总融合

六桶总融合的启动条件是：

- Batch04L 已同步为 guarded A/B closure。
- Batch04M 至少 M1+M2 完成，M3 全部有 boundary/guard/no_xuanbiyi 状态，不留“未判定强命中源”。
- `COVERAGE_MATRIX.csv` 中所有 Batch04M 源都有可审计状态，不让剩余套卷消失。
- Patcher/Governor/Automation 对 Batch04M 给出 `PASS_AFTER_AB_REVIEW` 或明确的 guarded pass。

总融合动作应先做：

1. 冻结候选池：区分 P0逐点、P1/P2支撑、guarded等级题、boundary表达。
2. 同类项合并：同一采分核心只保留一个核心点，表述差异进“表述积累 / 答案句变体”。
3. 生成六桶总表：时代背景、理论、经济全球化、政治多极化、中国、联合国。
4. 生成按题视图：每题必须按 `完整设问 -> 设问触发 -> 材料触发 -> 框架落点 -> 答题点自身积累 -> 答案句变体`，不能呈现后台 atom 表。
5. 跑学生可见污染扫描：不得出现 path、source id、P0、candidate、guard、评分参考、评标、细则等后台词。

## 6. 何时进入外部 GPT/Claude final review

外部 final review 只能在“总融合 Markdown + 按题视图 + 六桶 crosswalk”形成完整内部稿后启动。

启动条件：

- Batch04M closure 完成。
- 总融合稿本地 Patcher/Governor 初审通过。
- 学生可见污染扫描通过。
- 所有 guarded 条目在正文中已明示为“可选/等级题训练/表述积累”，没有冒充逐点细则。

外部 review 顺序：

1. 先发 GPT-5.5 Pro：做内容、迁移、遗漏、错归桶、答案句可写性压力测试。
2. 再发 Claude Opus：只看教学表达、结构清晰度、学生能不能学会；不能让 Claude 新增评分事实。
3. 保存 raw review 与 digest。
4. 本地逐条核验并 patch。
5. Patcher/Governor/Confucius 复验；若仍有 `must_fix_content` 或 `should_fix_transfer`，继续补丁，不进 DOCX/PDF。

## 7. 何时进入 DOCX/PDF

DOCX/PDF 是最后阶段，不能早于外部 final review 和本地复验。

启动条件：

- final Markdown 已经通过 GPT/Claude review digest 的本地修复。
- Governor 放行 Markdown PASS。
- Confucius/学习性检查确认不是只好看、而是能按题迁移。
- coverage close 已准备好，但 FINAL_ACCEPTANCE 尚不提前写 PASS。

DOCX/PDF 流程：

- 先用最终 Markdown 生成 DOCX。
- 按文档技能要求渲染 DOCX 页面或截图做视觉 QA。
- 若用户要求或 Word 可用，必须真实 Word open-save 验证。
- PDF 只能在 DOCX 视觉与内容门禁通过后导出；若 PDF/Word 自动化失败，记录真实 blocker，不假称完成。
- 最后才更新 final delivery、FINAL_ACCEPTANCE、coverage close。

## 8. 不应阻塞事项

- Batch04M source locator 与 Batch04L 状态同步可以并行。
- Batch04M ClaudeCode prompt 可以现在准备，但启动要等 L 状态同步和 M 清单冻结。
- M1 高收益组可以先跑，不必等 M3 边界组全部完成。
- 低证据、跨模块、等级题来源不应拖慢主线：给 guarded/boundary/reference-only 后继续。
- 外部 GPT/Claude 不应阻塞本地 Batch04M 源补齐；但 final Markdown/DOCX/PDF 必须等外部 review 或明确 waiver。

## 9. 总裁决

下一步优先级：

1. 同步 Batch04L A/B guarded closure。
2. 冻结并启动 Batch04M M1 高收益组，同时准备 ClaudeCode B Batch04M。
3. M1+M2 完成后，让 B 输出与 Codex A 做 A/B closure；M3 快速边界扫尾。
4. Batch04M 全部有状态后，进入六桶总融合。
5. 六桶总融合通过本地门禁后，再进入 GPT/Claude final review。
6. 外审修复与 Governor/Confucius 通过后，才进入 DOCX/PDF。

当前不得宣布最终成品，不得写 FINAL_ACCEPTANCE PASS，不得进入 DOCX/PDF。
