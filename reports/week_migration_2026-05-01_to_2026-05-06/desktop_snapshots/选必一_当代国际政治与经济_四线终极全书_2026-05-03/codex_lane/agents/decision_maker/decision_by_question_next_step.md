# Decision: By-Question View Next Step

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Role: Codex production lane A / 决策者

Scope: 只裁决下一步，不改 `07_student_doc/`、coverage、GPT/Claude 文件，不宣布最终成品。

## 已读依据

- `07_student_doc/by_question_view_draft_20260503.md`
- `08_review/gpt_content_review/section_batch_review_digest_20260503.md`
- `08_review/claude_advice.md`
- `COVERAGE_MATRIX.csv`
- `05_coverage/unresolved_blockers.md`
- `05_coverage/missing_questions.md`
- `05_coverage/coverage_by_evidence_level.csv`

## 当前判断

当前最优下一步：`先打通六桶索引与按题视图，同时做按题视图的高风险修补`。

不建议立刻进入最终成品，也不建议单纯继续扩展后续题源。理由：

1. GPT digest 明确判定当前 section batch 是 `NEEDS_FIX`，且下一版学生稿应优先变成 `按题视图 + 六桶索引`。
2. Claude advice 也要求“按题视图为正文，六桶视图作为索引”，两套目录共用同一组核心点，不重复正文。
3. 当前按题视图已经覆盖 11 个优先题的训练稿形态，适合先建立“题号 -> 六桶核心点 -> 分题卷面句”的桥。
4. coverage 当前 11 行仍是 `not_promoted/candidate_with_fixes`，`missing_questions.md` 也写明 full-suite exhaustion 尚未完成，所以不能宣布最终学生版。
5. 若现在继续扩源而不先打通索引，后续新增题会继续堆成孤立按题段落，六桶合并和频次口径会更难收束。

## 下一步分工裁决

### 1. 先叫醒融合线 / 文档结构劳动者

任务：生成桥接草案，不改最终文档。

输出建议：

- `07_student_doc/six_bucket_to_question_crosswalk_draft.md`
- 或同等文件名，由执行者自定，但必须在 `07_student_doc/` 下并标 `draft_not_final`。

内容要求：

- 六桶：时代背景、理论、经济全球化、政治多极化、中国、联合国。
- 每桶列核心点、命中题号、按题视图锚点、是否 P0/P1/P2/图片评分材料、是否有 boundary。
- 每个核心点只出现一次；同义变式进表述积累，不另起核心。
- 对每道题保留“审题结论 / 材料抓手 / 命中核心点 / 答题卡版答案 / 慎用提醒”的按题路径。

### 2. 再叫醒 Patcher

任务：对按题视图做高风险迁移修补，不重做源条目。

必须先判以下点：

- 2025海淀期中 Q16(2)：IP/合规风险与贸易摩擦、国际组织机制必须分层，不能一见知识产权就写贸易摩擦。
- 2025海淀期中 Q21(2)：`和平与发展仍是时代主题` 与 `维护世界和平、促进共同发展` 必须分开，图片备注未分类的内容不得刷成独立核心。
- 2025海淀二模 Q21：联合国三大支柱、联合国地位、中国地位、维护宪章必须对应到六桶索引，且保留“联合国”桶。
- 2026西城期末 Q20：`4选3` 和同槽变体不得拆频；绿色发展/新发展理念/有为政府+有效市场只作实践支撑或边界提示。
- 2026朝阳一模 Q20 与 2026顺义一模 Q20：`推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展` 必须保留完整高信息量核心名。

### 3. Governor 随后门禁

Governor 只判能否进入 `student_preview_candidate`，不得放行 final。

门禁条件：

- 按题视图与六桶索引已有同一核心点 crosswalk。
- 所有 11 个 coverage 题仍保留候选/证据层级，不把 P2 或图片材料混成 P0。
- 学生稿显式标注 `教学预览版 / 非终稿`。
- 学生正文不出现路径、页码、模型名、batch、phase、audit、debug 等后台语。
- 不出现终稿、闭环、coverage closed、FINAL_ACCEPTANCE 等表述。

## 关于继续扩展后续题源

不停止扩源，但本轮不把它作为第一优先级。

裁决：

- 自动化检测者/源扫描线可以并行维护“后续题源待扩展队列”。
- 但劳动主线先完成当前 11 题的 `按题视图 <-> 六桶索引` 桥接。
- `missing_questions.md` 中的 full-suite exhaustion 是下一阶段硬任务，不是当前学生预览稿放行条件。
- 等 bridge + patcher + governor 至少 `PASS_WITH_FIXES` 后，再扩展 2024-2026 全套源。

## 如果执行中出现分歧

- 如果按题视图修补发现核心点与六桶索引冲突：先修 crosswalk，不先扩题源。
- 如果 coverage 发现某题证据降级：该题在按题视图保留为 `preview/recheck_needed`，不删除整题。
- 如果新增源扫描发现高价值 P0 题：先加入待扩展队列，不打断当前 11 题桥接闭环，除非它能修复当前六桶核心空洞。
- 如果 Governor BLOCK：按 blocker 修桥接和高风险题，不推翻已有源证据，不停工。

## 明确禁止

- 不宣布最终成品。
- 不生成或放行 Word/PDF。
- 不写 `coverage closed` 或 `FINAL_ACCEPTANCE PASS`。
- 不删除、覆盖、回退现有 by-question draft、coverage、GPT digest、Claude advice。
- 不把扩源尚未完成的状态包装成“已穷尽”。
