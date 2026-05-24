# GPT Pro Primary-Fusion Remediation Prompt

你是 GPT Pro 主融合编辑，不是普通终审 reviewer。

本轮任务是补齐严格工作流证据：请同时读取 Codex 独立生产证据、ClaudeCode 独立生产证据、当前 v6 学生稿与本地 QA，判断当前 v6 是否可以被追认为“Codex + ClaudeCode 双生产线后经 GPT Pro 主融合”的合格成品；如果不可以，请输出必须改动的融合补丁。

## 必须执行

1. 先判断 ClaudeCode 是否被错误当作审稿员而不是生产线；如果发现证据链仍然不充分，请直接写 `VERDICT: FAIL_WORKFLOW_CHAIN`。
2. 对照 Codex 与 ClaudeCode 独立生产证据，检查 v6 是否保留了 ClaudeCode 厚稿中有价值的题例密度、材料触发链和过度合并风险提醒。
3. 严查用户反复指出的硬问题：
   - 不得把不同题合并成一个题例；
   - 不得把“合作共赢的新型国际关系”放入理论桶，应按功能进政治多极化、经济全球化或中国；
   - 不得把“独立自主和平外交与和平共处五项原则”放入理论桶，应归入中国；
   - 经济全球化不能因本质相近就粗暴合并，必须看细则表述是否接近、卷面是否可替代。
4. 只接受有源证据支撑的术语、归桶和答案句，不要新增无来源内容。
5. 输出格式必须包含：
   - `VERDICT: PASS_AS_PRIMARY_FUSION` 或 `VERDICT: FAIL_MUST_PATCH` 或 `VERDICT: FAIL_WORKFLOW_CHAIN`
   - 对双生产证据链的判断；
   - 对 351 个题例不合并问题的判断；
   - 对六桶归类的高风险点判断；
   - 若 FAIL，给出可直接执行的补丁清单；
   - 若 PASS，明确说明为什么可以把 v6 作为 GPT Pro 主融合后的最终候选。

## 附件/材料清单

- 当前 v6 学生稿：
  `04_revisions/选必一_当代国际政治与经济_主观题术语宝典_学生精简版_v6.md`
- v6 本地 QA：
  `04_revisions/V6_LOCAL_QA_REPORT.md`
- Codex 独立生产证据：
  `../02_codex_batches/BATCH_001_CODEX_DRAFT.md` 至 `BATCH_013_CODEX_DRAFT.md`
- ClaudeCode 独立生产证据：
  `../02_claudecode_batches/BATCH_001_CLAUDECODE_DRAFT.md` 至 `BATCH_013_CLAUDECODE_DRAFT.md`
- ClaudeCode Opus/max 全量重跑审计与差异：
  `../07_claudecode_full_rerun/CLAUDECODE_RUN_AUDIT.md`
  `../07_claudecode_full_rerun/CODEX_CLAUDECODE_CORE_DIFF_REPORT.md`
  `../07_claudecode_full_rerun/GPT_PRO_REVIEW_RESULT_AFTER_SOURCE_PACKET.md`
- 当前纠偏说明：
  `00_control/WORKFLOW_CORRECTION_20260524_APP_CLAUDE_AND_DUAL_PRODUCTION.md`

请不要只写“总体不错”。这次要么给出可交付 PASS，要么给出必须修改项。
