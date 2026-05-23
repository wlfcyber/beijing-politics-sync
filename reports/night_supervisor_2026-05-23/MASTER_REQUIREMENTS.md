# 2026-05-23 夜间总管硬要求

## 总目标

用户已睡觉，Codex 本线程作为夜间总管和用户分身，负责监督三个正在进行的线程持续推进到可验收闭环。

三条线目标：

1. 选必一：《当代国际政治与经济》要做成和必修四哲学宝典同级的宝典，覆盖全部考题，不能只交一份可读稿。
2. 必修四：把先前没有补入的考题继续补进既有哲学宝典框架，不能破坏已认可版本和框架组织。
3. 选必二：《法律与生活》要持续与 GPT Pro、Claude 互动，继续完善框架，直到聪明高三学生能够直接上手并尽量全对。

## 夜间授权边界

允许在本地政治研究与同步仓库范围内执行非破坏性读取、写入控制文件、生成补丁指令、生成审查包、渲染 Word/PDF、读取已有截图和日志、检查 Git 状态、启动/监督子 agent、写入新的监督报告。

不允许删除源文件、覆盖已认可成品、用旧结论冒充证据、把普通参考答案冒充评分细则、把 Codex 本地模拟冒充真实 GPT Pro 或 Claude Opus 调用。

## 最高验收标准

任何线只有同时满足下列条件，才允许写“完成/终版/PASS”：

- 覆盖：逐题或逐套覆盖矩阵闭合，缺口有明确边界原因。
- 证据：题干、答案、评分细则、讲评或用户确认来源分级清楚；普通参考答案不得冒充评分细则。
- 框架：正文按用户框架组织，不按试卷流水账堆砌；同核合并但不抹平不同触发点。
- 学生可用：材料信号 -> 知识/法律关系/答题动作 -> 答案落点，聪明高三学生可直接迁移。
- 外部模型：GPT Pro 与 Claude 的真实调用记录、截图、原始回复或明确 pending/blocked 记录存在；Codex 自写“模拟意见”不计入。
- Governor：拒绝假闭环、缺证据、错挂框架、审计语污染学生正文。
- Confucius：只读学生成品，从零基础/高三学生角度验证能否学会。
- 交付：Markdown、Word、PDF 或渲染证据存在；Word/PDF 视觉 QA 不得由 Markdown PASS 代替。

## 三线状态判定

状态词只允许使用：

- `RUNNING`
- `CANDIDATE_DELIVERY_NEEDS_AUDIT`
- `BLOCKED_ADVISOR`
- `BLOCKED_SOURCE_BOUNDARY`
- `DELIVERED_WITH_GOVERNANCE_GAPS`
- `STRICT_FINAL_ACCEPTED`

默认不得把 `CANDIDATE_DELIVERY_NEEDS_AUDIT` 或 `DELIVERED_WITH_GOVERNANCE_GAPS` 说成完成。

## 当前定位到的工作目录

选必一：

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\11_strict_final_rebuild_2026-05-23`

必修四：

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23`

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_philosophy_strict_v8_2026-05-23`

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_philosophy_full_coverage_double_lane_2026-05-23`

选必二：

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必二法律主观题框架_从题源生长\v12_2_framework_growth_restart\v13_10_final_baodian_integrated`

## 总管工作节奏

1. 每次醒来先看三个目录最近写入时间、控制文件、覆盖矩阵、审查报告、最终交付物。
2. 先找阻塞和假闭环，再看正文润色。
3. 若线程卡住，写入 `patch_orders/` 下的具体补丁命令，不写泛泛建议。
4. 若发现“完成”但缺逐题覆盖、真实外部模型、Governor、Confucius、Word/PDF QA 任一项，立刻降级为 `DELIVERED_WITH_GOVERNANCE_GAPS` 或 `CANDIDATE_DELIVERY_NEEDS_AUDIT`。
5. 任何新增正文内容必须回到本地证据核验后才能进入学生文档。

