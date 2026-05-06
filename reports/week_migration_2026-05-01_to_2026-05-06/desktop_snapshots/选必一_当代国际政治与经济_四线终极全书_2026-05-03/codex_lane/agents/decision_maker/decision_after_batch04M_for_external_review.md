# Decision Maker - after Batch04M A/B fixes toward external review

裁决时间：2026-05-04
角色边界：Codex A 决策者；只裁定下一步，不改学生稿、coverage、fusion、delivery 或 review 文件；不宣布最终完成。

## 1. 当前总裁决

Batch04M A/B 修正后，可以进入真实外部评审阶段，但不能进入最终交付阶段。

允许启动：

- Claude Opus teaching-text review：允许。
- GPT-5.5 Pro `final_markdown` content review：允许。
- 交付管线预检：允许做污染扫描、分块、review prompt 准备、DOCX/PDF 前置清单。

继续禁止：

- 直接生成或发布最终 DOCX/PDF。
- 写 `FINAL_ACCEPTANCE PASS`。
- 宣布 coverage close。
- 把当前 `07_student_doc/选必一_完整学生讲义_融合稿_20260504.md` 当最终学生成品交付。

## 2. 是否还要 source hunt

不再做宽泛 source hunt。

Batch04M 已完成剩余套卷的 A/B 修正分层，当前应冻结源状态：

- `2026丰台期末 Q20`：保持 `BLOCKED_PROMPT_ONLY`。题面存在，但当前正式评分细则缺失；除非后续有人提供或定位到本题当前细则，否则不再拖全局。
- `2024石景山一模 Q19(2)` 与 `2024顺义二模 Q19(2)`：降为 `REFERENCE_ONLY_NOT_PROMOTED`，不进主频。
- `2025丰台一模 Q20`：降为 `GUARDED_FALLBACK_ONLY`，只保留“双循环 / 两个市场两种资源”兜底表达；主实践措施不得冒充选必一主码。
- `2025昌平二模 Q21`：`GUARDED_ADMIT`，只收选必一 exclusive 的经济全球化/全球经济治理表达。
- `2026石景山期末`：继续用户确认排除。
- `2024模块分类汇编`：继续 source-bundle boundary，不作新题源 promotion。

因此，下一步不再以“补源”为主线。只允许一个窄例外：若有人在本地原始目录中新找到 `2026丰台期末 Q20` 当前正式评分细则，可单独开补丁；没有新细则时不阻塞外审。

## 3. 外部评审启动条件

外审可以启动，但必须带着以下本地上下文一起送审：

- `06_conflicts/batch04M_claudecode_conflict_resolution.md`
- `07_student_doc/选必一_完整学生讲义_融合稿_20260504.md`
- Batch04M 的 blocked / guarded / reference-only / excluded 结论摘要
- 明确说明：外部模型不能新增评分事实，不能恢复 blocked source，只能做内容、教学、迁移、错归桶、污染词和可学性审查。

当前 ClaudeCode screen 已无活跃 socket；这一项不再阻塞。若另有其他模块线程并行写文件，外审材料必须只取本 run 目录内、文件名明确属于选必一 Batch04M/学生融合稿的内容。

## 4. Claude Opus teaching-text review 裁决

允许真实启动 Claude Opus teaching-text review。

Claude Opus 的任务边界：

- 看讲义是否像学生能学会的课稿，而不是后台融合表。
- 检查六桶速览是否有助于迁移。
- 检查每题是否符合 `完整设问 -> 设问触发 -> 材料触发 -> 框架落点 -> 答题点自身积累 -> 答案句变体`。
- 检查“慎用提醒”和 guarded 表达是否学生能看懂。
- 不得补充新题、新细则、新术语事实。
- 不得把 `2026丰台期末 Q20`、`2024石景山一模 Q19(2)`、`2024顺义二模 Q19(2)`恢复进主表。

Claude 返回后只作为 teaching-text advice，需要 Codex 本地核验后才可 patch。

## 5. GPT-5.5 Pro final_markdown review 裁决

允许真实启动 GPT-5.5 Pro `final_markdown` review。

GPT-5.5 Pro 的任务边界：

- 按最终 Markdown 审查内容准确性、同类项合并、错归桶、术语保形和答案句可写性。
- 专查 Batch04M A/B 修正是否继承到学生稿：
  - `2026丰台期末 Q20`未进入主框架；
  - `2024石景山一模`、`2024顺义二模`仅边界；
  - `2025丰台一模 Q20`只作兜底表达；
  - `2025昌平二模 Q21`保持 no-explicit-book guard；
  - 共商共建共享统一为全球治理观；
  - 经济全球化完整五词不被短句替代。
- 专查学生稿是否仍有后台感过重的问题。
- 返回项必须分为 `must_fix_content`、`should_fix_transfer`、`style_or_layout`、`no_action`。

若 GPT verdict 为 `NEEDS_FIX`，不得进 DOCX/PDF；必须先本地修复并重跑 Patcher/Governor。

## 6. 当前学生融合稿的已知外审重点

`07_student_doc/选必一_完整学生讲义_融合稿_20260504.md` 已具备外审价值：

- 六桶结构已形成；
- 同类项合并和出现次数已初步呈现；
- 大多数条目已有完整设问、设问触发、材料触发、框架落点、答题点自身积累、答案句变体；
- 慎用与排除区已经纳入 Batch04M 关键边界。

但它还不是交付稿。外审和本地 Patcher 必须重点检查：

- 是否仍有“得分位置 / 评分 / 细则 / 等级题”等过强后台语言需要改成学生可读但可审计的表达；
- `含等级题或边界表达` 是否会让学生误以为都是同权主频；
- `慎用提醒` 是否足够清楚，能阻止学生把 guarded 表达当固定模板；
- 频次是否把 guarded / reference-only / boundary 表达混得过重；
- 是否存在同一核心被重复拆成多个近义条；
- 答案句是否都能直接写在卷面上，而不是制作说明。

## 7. 交付管线裁决

可以开始交付管线预检，不可以开始最终交付。

允许并行准备：

- final_markdown review prompt 分块；
- Claude teaching-text review prompt；
- 学生稿污染词扫描；
- guarded/source-boundary 扫描；
- DOCX/PDF 生成脚本或模板检查；
- delivery checklist。

禁止执行：

- 生成最终 DOCX 并标为定稿；
- 导出最终 PDF；
- Word open-save 最终验收；
- FINAL_ACCEPTANCE；
- coverage close。

进入 DOCX/PDF 的最小条件：

1. Claude Opus teaching-text review 已完成并 digest。
2. GPT-5.5 Pro final_markdown review 已完成并 digest。
3. 所有 `must_fix_content` 与阻断性 `should_fix_transfer` 已本地修复。
4. Patcher/Governor 复验给出 Markdown PASS 或 PASS_WITH_NONBLOCKING_NOTES。
5. 学生可见污染扫描通过。
6. Confucius/学习性检查确认讲义能支持迁移答题。

## 8. 角色分工

Codex 生产：

- 冻结当前源猎结论，准备外审投递包。
- 不再扩源；只保留 2026丰台期末 Q20 的窄补丁入口。
- 外审回来后逐条本地核验并 patch。

劳动者：

- 不再重翻全部套卷。
- 只在外审指出具体题目/术语疑点时，回对应本地证据核验。

Patcher：

- 外审前做一次快扫：确认 Batch04M 的 blocked/guarded/reference-only/excluded 结论在学生融合稿里没有被反向恢复。
- 外审后处理 `must_fix_content` 和 `should_fix_transfer`。

Governor：

- 当前只可放行外审，不可放行交付。
- 外审修复后再判定是否进入 DOCX/PDF。

Automation：

- 确认 ClaudeCode screen 已退出。
- 扫描学生稿中的后台词、guarded 标记、路径/source id/atom/candidate 等污染。
- 检查 coverage 中 Batch04M rows 是否仍有 `pending_ab_closure_review`；若有，外审可继续，但 DOCX/PDF 不可继续。

## 9. 最终裁决

下一步优先级：

1. 立即准备并启动真实 Claude Opus teaching-text review。
2. 立即准备并启动 GPT-5.5 Pro `final_markdown` review。
3. 同步做学生稿污染扫描和 Batch04M guard 继承快扫。
4. 暂停宽泛 source hunt；仅保留 2026丰台期末 Q20 正式细则的窄补丁入口。
5. 外审与本地修复完成前，不进入 DOCX/PDF、FINAL_ACCEPTANCE、coverage close。

本文件只给下一步裁决，不代表最终成品完成。
