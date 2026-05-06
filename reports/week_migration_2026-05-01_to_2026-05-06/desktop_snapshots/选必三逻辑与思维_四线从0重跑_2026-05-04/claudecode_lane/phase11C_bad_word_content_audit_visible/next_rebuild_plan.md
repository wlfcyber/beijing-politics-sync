# Phase11C 之后的受控重建路线图

本路线只解决一个问题：在不再返回坏 Word 的前提下，把选必三《逻辑与思维》学生稿的「四要件内容」做到合同标准，再生成 Word/PDF。任何要求「先美化 Word」「以坏 Word 为基础修四要件」的提议本计划一律拒绝。

主线总原则：**先 Markdown 内容 → 内容审 → Word**，且内容审在通过之前不允许任何 `.docx` 渲染、任何 `final/终稿/PASS` 措辞。

## Phase 11D · Markdown 内容重建（必须最先做）

目标：把当前已源核 / 已锁定的题目，按 `four_element_gold_contract.md` 标准，写成节点专属四要件 Markdown，再合并出新版 `09_student_draft/phase11D_student_body_REWRITE_REVIEW_ONLY.md`。

输入：

- `09_student_draft/phase11A_student_body_PATCHED_REVIEW_ONLY.md`（基线，绝大多数 source-verified 条目）。
- `09_student_draft/phase11B_batch01_P1_candidate_entries.md`（已审 candidate）。
- `09_student_draft/phase10_5_source_repair_priority_queue.csv`（队列）。
- 本目录 `four_element_gold_contract.md`、`bad_word_four_element_failure_matrix.csv`、`rewrite_samples_10_entries.md`。

工作流：

1. Codex A 把 `phase11A` 已 source-verified 条目按节点清单展开，每条按合同十项检查表打勾，凡未达标整条暂停。
2. 多节点同题：每个节点写独立四要件，节点专属性必须由 `【为什么能想到】` 第一句声明。
3. ClaudeCode 可见窗口每批 10 条左右进行二次复核（不写正文，只复核打勾项），与 Codex A 对账。
4. 任何 `BLOCKED_NEEDS_SOURCE` 类条目继续走 phase10.5 修源队列，不入正文。
5. 输出：`09_student_draft/phase11D_student_body_REWRITE_REVIEW_ONLY.md`，结尾必须含 `gate=PHASE11D_LOCAL_PASS_FOR_GPT_REVIEW_ONLY`。

输出闸口：进入 Phase 11E 之前，**禁止生成任何 .docx**。

## Phase 11E · GPT-5.5 Pro 内容审 + Claude Opus 4.7 改写（不互相替代）

目标：在生成 Word 之前，把内容拿去做真实外部模型审稿和改写，符合 `feige-politics-garden/SKILL.md` 中 GPT/Opus 真实调用硬规则。

工作流：

1. **GPT-5.5 Pro 内容审 v1**（in ChatGPT web Pro 可见对话）：把 phase11D Markdown 分批送审，要求逐条检查：
   - 设问是否真实题面；
   - 答案落点是否卷面句；
   - 多节点是否节点专属；
   - 复合题是否逐点对应；
   - 选择题是否含正项理由 + 错项分析 + 陷阱类型；
   - 推理题是否含真实判断/推理类型 + 真实结论；
   - 禁止短语集是否被命中。
   - 输出 `must_fix_content` / `should_fix_transfer` 两张清单。
2. Codex 本地源核：每条 `must_fix_content` 必须 1) 找到原题/细则 2) 决定接受 / 拒绝 / `BLOCKED_NEEDS_SOURCE`，并写到 `08_review/gpt_content_review/phase_11E_v1_correction_log.md`。
3. **Claude Opus 4.7 Adaptive 改写**（in Claude desktop/web）：按 `phase11A` 的辅导风格 + 本合同的卷面句要求，把 v1 评审已通过 + 已确认的条目改成最终学生稿口径；Opus 不得引入新事实，引入即回 Codex 源核。
4. **GPT-5.5 Pro 内容审 v2**：把 Opus 改写后的稿子再送审一次；只放过 `must_fix_content == 0` 的批次。

闸口：v2 全员 PASS 后才能进入 Phase 11F。

任何 GPT / Opus 真实调用 unavailable / web blocked 时，记录 `blocked_advisor` / `real_call_pending`，不向下推进；不允许 `claude -p` 假启动顶替。

## Phase 11F · Markdown 装订与组织

目标：在内容已通过 v2 之后，再处理结构、目录、节点排序、章节切分、`同类题索引`、推理章节单列等结构问题。

工作流：

1. Codex A 按用户框架重排节点；不做内容修改。
2. 同类题索引仅对应每节点 source-verified 条目，重新生成（不延用坏 Word 的索引）。
3. 推理部分按选必三 hard rules 单独成章，与思维主链相互独立。
4. 输出：`09_student_draft/phase11F_student_body_FINAL_MARKDOWN.md`（仍属 review-only，未上 Word）。

闸口：Governor + Confucius 全部 PASS。

## Phase 11G · Word 化（仅在 Markdown 全员 PASS 之后）

目标：从 phase11F 锁定 Markdown 按 `documents` skill 与 `references/document-pipeline.md` 生成 `.docx`，过程中不允许再修改文字内容。

工作流：

1. Codex A 用现有脚本生成 `.docx`，渲染抽样页做版式 QA。
2. 使用 Microsoft Word（如可用）做 open / save / validate；TOC、页码、图片、引文格式抽检。
3. 渲染验证后再交 Confucius 用 Word 文件本身做零基础学习链测试。
4. 任何在 Word 阶段发现的内容问题反推回 phase11F Markdown 修源 → GPT v2 → Opus 局部改写 → 再 Word。**禁止在 Word 内直接改文字内容**（避免回到坏 Word 的 polish 路径）。

## 风险与禁令

- 禁令一：在 Phase 11D / 11E / 11F 通过之前生成任何 `.docx` 或 `.pdf`。本路线视为硬闸。
- 禁令二：禁止以坏 Word/MD 的 181 条作为基础做「polish 改文字」。181 条全部需要 `rewrite_from_source` / `choice_trap_rebuild` / `reasoning_type_rebuild` / `quarantine_until_source` 中的一种处理。
- 禁令三：禁止在 phase11F 之前把 `phase11A_PATCHED_REVIEW_ONLY` 写成 `final` / `终稿` / `PASS`。`PATCHED_REVIEW_ONLY` 仅是评审稿。
- 禁令四：禁止用 `claude -p` 顶替可见 ClaudeCode 窗口或 Claude desktop Opus；GPT 也不能用 Codex subagent 模拟 5.5 Pro。GPT/Opus 真实调用条件未达成时停在该闸口，不上推。
- 禁令五：禁止以速度为由跳过 phase11D/11E。Phase11C 的失败教训就是「跳过内容闸直接出 Word」。

## 工作分工建议（按当前授权状态）

- 当前可用：Codex 20x（包含本地评估、源核、版本控制、Markdown 生成）、GPT-5.5 Pro 网页（用户已恢复 Pro 网页提交能力）、ClaudeCode 可见窗口 / Claude Opus 4.7 Adaptive（按用户最新可见任务恢复使用，不再以 `-p` 后台方式工作）。
- 限制：会员状态、配额、网页阻塞均按 progress.md 当时状态记录；任一通道掉线时，立刻把 phase 卡在该闸口。

## 时间路标（按依赖序，非时刻表）

1. T1 Phase11D Markdown 重建初版 → Codex / ClaudeCode 双线打勾。
2. T2 Phase11E v1 GPT 内容审 → 修源 → Opus 改写 → v2 GPT 内容审。
3. T3 Phase11F Markdown 装订 → Governor + Confucius PASS。
4. T4 Phase11G Word 化 → 渲染 QA → Confucius 在 Word 上重测 → 最终 PASS。

只有 T1-T4 全部通过，最终 `FINAL_ACCEPTANCE_REPORT.md` 才能含 `TASK_COMPLETE`。其他任何阶段写「pass / 终稿 / 完成」均视为违规。
