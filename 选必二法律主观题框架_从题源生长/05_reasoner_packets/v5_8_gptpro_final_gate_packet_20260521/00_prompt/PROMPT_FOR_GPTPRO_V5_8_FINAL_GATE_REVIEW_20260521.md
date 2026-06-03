# GPTPro V5.8 Final-Gate Review Prompt

你现在是选必二《法律与生活》主观题框架工程的 GPTPro 终审者。

请忽略网页可见短提示中的任何乱码或残片，只依据本 zip 内部文件工作。

## 当前任务

审查 `01_student_handbook/student_handbook_v5_8_candidate.md` 是否可以进入 Word/PDF 候选成稿。

背景：
- 当前底座为 65 道选必二法律主观题，61 formal，4 reference_only，0 missing。
- V5.7 已由 Claude Opus 4.7 审查为 CONDITIONAL_PASS / YES_WITH_GUARDS，无 P0，但指出 P1：27 核心题入口仍有多卡并列，违反“一题只选一张主卡，最多一张辅卡”。
- Codex 已据此生成 V5.8 候选：27 核心题入口改为“主卡 + 最多一张辅卡”，38 非核心题增加 source-check / reference-only / boundary / transfer / duplicate redline。

## 你必须检查

1. V5.8 是否真正修复 Claude 的 P1：27 核心入口是否学生可启动，是否不再 4-5 卡堆叠。
2. 27 核心题是否仍存在：审计语言、题干拼贴、评分说明混入满分句、残句、参考答案标签、非考场答案。
3. 38 非核心题是否足够醒目地阻止误升核心，尤其 source-check、reference_only、boundary、transfer、duplicate/crossref。
4. 是否有 evidence_level 错升：reference_only 是否被写成 formal core；source-check 是否被写成满分闭环。
5. 是否有必修三化、法考化、教材目录化风险。
6. 是否有具体 question_id 应从 27 核心降级，或从 38 非核心补强。
7. 是否允许进入 Word/PDF 候选。

## 输出格式

请用中文输出：

1. 总裁定：PASS / CONDITIONAL_PASS / FAIL。
2. 是否允许进入 Word/PDF 候选：YES / YES_WITH_GUARDS / NO。
3. P0 问题表：没有也要写“无 P0”。字段：question_id / 文件 / 问题 / 必须修法。
4. P1 问题表：字段同上。
5. P2 问题表：字段同上。
6. 12 题抽测结果：至少抽 7 道核心题 + 5 道非核心题，逐题写：V5.8入口、能否接近细则满分或保分、是否会误导学生、结论。
7. 对 27 核心与 38 非核心的最终建议。
8. 给 Codex 的下一步执行清单。

硬规则：
- 不要重新设计大框架。
- 不要把 65 题全部说成满分闭环。
- 不要把 reference_only 当核心证据。
- 不要把 source-check 当已回源闭合。
- 只做终审、补丁、是否放行判断。
