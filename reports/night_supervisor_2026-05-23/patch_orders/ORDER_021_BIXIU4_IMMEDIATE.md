# ORDER 021: 必修四即时补丁令

## 当前状态

状态词：`DELIVERED_WITH_GOVERNANCE_GAPS`

依据：

- `bixiu4_philosophy_strict_v8_2026-05-23/STRICT_GATE_REPORT.md` 明确写：v7 判定 FAIL，不能作为学生版终稿。
- 当前严格题源基数从旧 56 套改为 65 套。
- `remaining_old_subjective_presence_gaps_after_v7.csv` 只有 `empty`，说明旧主观题“同套同题出现”层面暂时无剩余缺口。
- `old_subjective_rows_present_but_quality_failed_v8.csv` 有 69 行，约 68 条旧主观题已出现但质量失败。
- `remaining_old_choice_presence_gaps_after_v7.csv` 有 175 行，约 174 条旧选择题仍未以同套同题来源行闭合。
- `04_review_packages/REVIEW_PACKAGE_MANIFEST.md` 显示 GPT Pro 网页审核包已生成，但不是已审结果：主观质量失败 68、选择题未闭环 174、高风险原理 38、新增 9 套。
- `00_control/GPTPRO_WEB_ONLY_BOUNDARY.md` 明确 GPT Pro 必须是网页版，不能用 Codex 子 agent 冒充。

## 禁止声称

不得称“必修四补题已完成”。v7/v8 文件存在不等于严格终版。当前必须称“已形成严格返工门与审查包，仍需补选择题链和主观质量失败项”。

## 下一步硬任务

1. 先不要重写已认可母版主体；所有修订先做候选补丁。
2. 处理 68 条旧主观题质量失败：
   - 补完整设问；
   - 把“先点原理、再扣材料、最后回设问”这类模板话改成可直接写的答案句；
   - 移除学生正文里的“评分细则/评标/补漏/审计/CSV”等污染词；
   - 保持原哲学原则/方法论框架，不按试卷流水账重排。
3. 处理 174 条旧选择题缺口：
   - 每题必须有完整题干、选项、正确项链、错项类型；
   - 不得只写“触发某原理”。
4. 新增 9 套必须进入 65 套总口径：
   - 不能只做附录；
   - 通州一模要先完成缓存/OCR/题目/答案/细则边界；
   - 2026 二模 A/B/C 分级要并入总清单。
5. GPT Pro 审核包 A-F 只能算“待网页端审查包”；拿到网页版真实结果前，不得写 GPT Pro PASS。
6. 重新生成候选后，再跑 Governor、Confucius、Word/PDF QA。

## 下一次汇报必须给出

- 68 条主观质量失败已修复多少。
- 174 条选择题缺口已闭合多少。
- 65 套中新增 9 套的处理状态。
- GPT Pro 网页真实回传是否已保存；若没有，状态写 `BLOCKED_ADVISOR` 或 `real_call_pending`。

