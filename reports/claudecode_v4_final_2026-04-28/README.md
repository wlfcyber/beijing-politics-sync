# ClaudeCode v4 最终成果与过程交接

本目录用于让另一台电脑完整理解 2026-04-27 至 2026-04-28 这轮 ClaudeCode 必修四哲学重跑的结果、过程和后续接管边界。

## 最终成果

`final_artifacts/` 包含本轮 ClaudeCode 生成的 v4 终极版：

- `必修四哲学材料-知识触发框架_原框架节点版_v4.docx`：学生可读 Word 版。
- `必修四哲学材料-知识触发框架_原框架节点版_v4.md`：学生可读 Markdown 版。
- `必修四哲学材料-知识触发框架_原框架节点版_v4_审计证据版.md`：审计证据版。
- `PHILOSOPHY_FRAMEWORK_ENTRIES_CANONICAL.csv`：结构化条目表。

## 过程与审计

- `process/`：ClaudeCode 运行配置、用户修正记录、最终 Word prompt、OCR rerun prompt、cache-assisted 修正说明、项目级 `CLAUDE.md`。
- `audit/`：55 套覆盖与边界文件，包括 `SUITE_REVIEW.csv`、`FOLLOWUP_OR_BLOCKED_ITEMS.csv`、`V4_COVERAGE_AUDIT.md`、客观题/源文件清单。
- `compare/`：Codex 与 ClaudeCode 两版比对，高置信共同项、分歧项、Claude 独有、Codex 独有、解释链审核、OCR-needed 控制清单。
- `render_samples/`：最终 Word 的首页/前言页等渲染抽样图，用于快速确认版式方向。

## 当前边界

本轮 v4 曾被认为覆盖 55 套并生成最终成果，但后续用户人工抽查发现仍有 OCR-needed 和框架归属风险，尤其包括：

- S001 `2024东城一模`：需按 cache-first 规则重跑，补全试卷正文、完整设问、材料触发和答案落点。
- S042 `2026海淀一模`：需纠偏“社会存在与社会意识/物质决定意识”相关处理，不能因细则没有字面“物质决定意识”就粗暴清出唯物史观点。
- 其它 OCR-needed / source 边界见 `compare/08_OCR-needed重跑控制清单.md`。

因此，本目录不是“绝对最终可交付锁死版”，而是“ClaudeCode v4 已完成轮次 + 后续复核入口”。另一台电脑接管时，必须从 handoff 文件和 S001 cache-first prompt 继续复核。

## 昨天训练出的写法原则

最重要的经验不是格式，而是写清楚“材料如何触发原理方法论，并如何回应设问”：

1. 触发逻辑不能写“因为细则写了，所以可以放在这里”。细则只放在准确性校验或审计证据里。
2. 触发逻辑要先抓材料里的信号词、动作、关系、矛盾、过程、条件或价值指向。
3. 再说明这些材料信号为什么在知识上对应某个原理方法论。
4. 最后必须写出“答案落点”：这个原理如何变成回答设问的具体答案句。
5. 如果设问问“为什么”，答案落点要写原因/必要性/价值如何被证明。
6. 如果设问问“如何”，答案落点要写主体应该怎样做。
7. 如果设问问“说明/体现/认识”，答案落点要把材料动作或关系映射到原理，并说明它证明了什么。
8. 学生最终版必须干净，不出现路径、F04、L24、slide、OCR log、debug 等工程信息。

这些规则已同步到：

- `skills/feige-politics-garden/references/philosophy-trigger-standards.md`
- `cloudcode/claudecode_philosophy_rerun_package/skill/feige-politics-garden/references/philosophy-trigger-standards.md`
- 本目录 `process/CLAUDE_project_cache_first.md`

## 给另一台电脑的使用方式

先读：

1. `reports/handoff_to_home_computer_2026-04-28.md`
2. `reports/claude_ocr_rerun_s001_cache_first_prompt_2026-04-28.md`
3. 本目录 `README.md`
4. 本目录 `compare/08_OCR-needed重跑控制清单.md`

然后让 ClaudeCode 从 S001 开始按 cache-first 重跑，不要跳卷，不要用旧结论冒充证据。
