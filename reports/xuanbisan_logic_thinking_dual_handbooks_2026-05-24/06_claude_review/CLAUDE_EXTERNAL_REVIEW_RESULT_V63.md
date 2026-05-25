# Claude External Review Result V63

Status: `EXTERNAL_REVIEW_DONE_NOT_PASS`

Reviewer lane: independent Claude external review V63, distinct from ClaudeCode B 线生产、Claude V0/V1/V2/V3 外审、Governor、Confucius、Word/PDF QA。本文件是本审唯一权威产物。

Scope: 仅复审 Claude V3 NOT_PASS 之后到 V65 包之间落地的：(a) 2026 二模 B 线 suite-slice 复跑 (Q0113-Q0140)；(b) V63 学生送审稿生成 + V64 框架重排稿 + V65 推理题型重排稿；(c) V87 新增 Q0141-Q0143 source-lock 与 V88 推理正文加入；(d) 真实 GPT Pro V65 结果 (`05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`) 及其本地 source-routed 处置 (V90/V91/V92)。读入 packet `10_packets/GPTPRO_REVIEW_PACKET_V65.md`、`05_gptpro_review/EXTERNAL_REVIEW_STATUS.md`、`05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md`、`06_claude_review/CLAUDE_EXTERNAL_REVIEW_RESULT_V3.md`、`06_claude_review/EXTERNAL_REVIEW_STATUS.md`、`01_source_inventory/2026_ERMO_SUITE_CLOSURE_REPORT.md`、`01_source_inventory/SUITE_COVERAGE_AUDIT_V87.md`、`03_claudecode_lane/suite_reports/2026二模_B线复跑.md`、`03_claudecode_lane/2026_ERMO_B_LINE_RERUN_RESULT.md`、`03_claudecode_lane/blockers_2026_ermo.csv`、`03_claudecode_lane/fusion_candidates_2026_ermo.csv`、四份 `08_delivery/选必三*.md` 学生稿、`08_delivery/STUDENT_REVIEW_DRAFT_CLEANUP_NOTE.md`、`08_delivery/STUDENT_SAFE_CLEANUP_SCAN_V91.md`、`02_codex_lane/MAIN_THINKING_LEDGER.csv`、`02_codex_lane/REASONING_FORM_LEDGER.csv`、`02_codex_lane/CHOICE_TRAP_LEDGER.csv`、`04_fusion/PROMOTION_QUALITY_CHECK.md`、`04_fusion/PROMOTION_LOG.md`、`04_fusion/PROMOTION_HOLD.md`、`04_fusion/GPTPRO_V65_SOURCE_PATCH_AUDIT_V90.md`、`04_fusion/GPTPRO_V65_SOURCE_PATCH_AUDIT_V91.md`、`04_fusion/GPTPRO_V65_SOURCE_PATCH_AUDIT_V92.md`、`04_fusion/Q0141_SOURCE_IDENTITY_RESOLUTION_V92.md`、`07_governor_confucius/STUDENT_REVIEW_DRAFT_GOVERNOR_PRE_GPT_V65.md`、`07_governor_confucius/STUDENT_REVIEW_DRAFT_CONFUCIUS_PRE_GPT_V65.md`、`07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md`。

## Verdict

**NOT_READY_FOR_FINAL — GPTPRO_V65_CAPTURED_AND_SOURCE_ROUTED_BUT_Q0141_IDENTITY_IS_ONLY_LOCAL_BOUNDARY_AUXILIARY_DIRECTORY_NOT_CLEANED_AND_PROMOTION_GATE_FILES_STALE_BEFORE_V64.**

GPT Pro V65 真实结果已经捕获并给出 `not_final`，本地 V90/V91/V92 已对 GPT Pro 五个 P0 做出 source-routed 处置：

1. Q0143（2025西城期末 Q17(2)）大前提已从“所有资源都可以通过适当方式被重新利用”收窄为“放错了地方的资源可以通过适当方式被重新利用”，并在 `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md:682-692` 与 `08_delivery/选必三_逻辑与思维_推理宝典_学生送审版.md:614-624` 两处同步落地，旁证 `04_fusion/GPTPRO_V65_SOURCE_PATCH_AUDIT_V90.md` GPTV65-003。GPT Pro V65 P0-03 的本审 verdict：**已修复**。
2. Q0141（2024东城二模 Q17(2)）双挂位置在 `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md:995-1017`（科学归纳/求异法）与 `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md:1107-1129`（类比推理）；正文已收窄为“因果探求主写求异法，只有材料比较关系能对应时才补写求同法或共变法”。这一收窄方向正确，对应 GPT Pro V65 P1-02 / GPTV65-007，本审接受。但 source-path/internal-header 冲突在 V92 走的是 Codex 本地 boundary 接受（`04_fusion/Q0141_SOURCE_IDENTITY_RESOLUTION_V92.md`：source path 与旧 ledger 把 `17-2.docx` 放在 `2024东城二模`，DOCX 内部 `高三政治一模阅卷总结 2024.4.10` 被判为“stale copied header or document-title typo”），不是外部源核对结论。这条 boundary 把 GPT Pro 原始 P0 从“无法判断身份”降级为“路径+ledger 优先于内部标题”，但 Claude 不能把它当作“GPT Pro 验证通过”。GPT Pro V65 P0-01 的本审 verdict：**仅本地 boundary 释放，未真正闭合**。
3. Q0136-Q0140 B 线证据在 V90 GPTV65-002 表里已被逐题点名（Q0136 A-support / Q0137-Q0138 B-choice-signal / Q0139 A-formal dual / Q0140 A-formal comprehensive-boundary），且 `03_claudecode_lane/2026_ERMO_B_LINE_RERUN_RESULT.md` 与 `03_claudecode_lane/blockers_2026_ermo.csv` 均把 B 线复跑列为 `patched_pending_external_review`。GPT Pro V65 P0-02 的本审 verdict：**本地可见性已闭合，作为外部审核证据仍待 Claude 本审与 Codex 进一步外审**。
4. 学生稿内部痕迹：`08_delivery/STUDENT_SAFE_CLEANUP_SCAN_V91.md` 报 4 份学生送审稿 (`选必三_逻辑与思维_思维宝典_学生送审版.md`、`选必三_逻辑与思维_推理宝典_学生送审版.md`、`选必三_逻辑与思维_思维宝典_框架重排送审版.md`、`选必三_逻辑与思维_推理宝典_题型重排送审版.md`) 对 16 个 pattern 全部 `0` hit；本审独立抽查这四份文件确认这 16 个 pattern 未命中。GPT Pro V65 P0-04 / P0-05 的本审 verdict：**4 份主学生稿已修复**。但 V91 扫描没有覆盖到 `08_delivery/选必三_逻辑与思维_思维宝典_框架检索目录_送审辅助.md`，该文件仍是 student-facing 形式（位于 `08_delivery/` 而非 `09_logs/`、文件名含“送审”），且对 16 个 pattern 命中“送审”等关键字（独立 grep 验证）；它出现在 V65 packet read 第 18 条 (`08_delivery/选必三_逻辑与思维_思维宝典_框架检索目录_送审辅助.md` 等同位置)，所以 GPT Pro 是把它当作待审件而不是 audit annex。该文件没有被 V91 student-safe scope 覆盖，本审视为 P0 残口。
5. Q0142（2025东城二模 Q18(2)）正文措辞“必要条件而非充分条件”在 `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md:124-146` 与 `08_delivery/选必三_逻辑与思维_推理宝典_学生送审版.md` 对应段落保留，符合 V87 source-lock 与 GPT Pro V65 P1-01 / GPTV65-006 的 `source_verified_no_patch_now` verdict。本审接受。

但本审仍判 NOT_PASS，原因有四类未释放硬伤：

1. **Q0141 source identity 仍只是 Codex 本地 boundary，不是外部核对结论。** `04_fusion/Q0141_SOURCE_IDENTITY_RESOLUTION_V92.md:9-26` 自述：source path 与旧 ledger 把 17-2.docx 放在 `2024东城二模`，DOCX 内部 `高三政治一模阅卷总结 2024.4.10` 被判为 stale header；旁证只是“真 2024东城一模 Q17(2) 是北极熊毛衣题，不同条目”。这是 Codex 自审采纳了“路径优于标题”，没有引入外部审核或 GPT Pro 的二次确认。GPT Pro V65 原文 P0-01 要求“PDF 原题、答案表、评分细则、source-lock、ledger、internal-header、suite report”七项对账后再决定双挂安全；本仓证据只完成 source-lock、ledger、internal-header 三项的对照式判定。**这是本审 P0 V63-F1**。
2. **`08_delivery/选必三_逻辑与思维_思维宝典_框架检索目录_送审辅助.md` 未做 student-safe 清理。** V63 packet read 第 18 条已经把它列为 student-facing 读件；V91 scan 故意只覆盖四份学生稿，跳过本文件。该文件仍含 `送审` 字样（题名 + 正文），且按当前结构是学生在“框架重排稿/学生送审稿”之外查询节点时的辅助入口，不应该是只有 Codex 看的 audit annex。要么把它从 `08_delivery/` 移到 `09_logs/` 或 `07_governor_confucius/`，要么把它也纳入 V91 scope 重新清理。**这是本审 P0 V63-F2**。
3. **门控自身状态滞后于 V90/V91/V92。** `04_fusion/PROMOTION_LOG.md` 全表 check7 列仍写 `fail: Claude V3 NOT_PASS, GPT Pro pending`；`04_fusion/PROMOTION_QUALITY_CHECK.md` Current Ratings 表 external review 列同样全写 `fail: Claude V3 NOT_PASS, GPT Pro pending`；`04_fusion/PROMOTION_HOLD.md` 状态字段仍写 `ACTIVE` 且没有 V90/V91/V92 段更新；`07_governor_confucius/STUDENT_REVIEW_DRAFT_GOVERNOR_PRE_GPT_V65.md` verdict 仍是 `NOT_FINAL_READY_FOR_GPTPRO_V65_AFTER_BROWSER_FIX`（pre-GPT 写法，GPT Pro V65 已经被捕获后未生成 post-GPT Governor 段）；`07_governor_confucius/STUDENT_REVIEW_DRAFT_CONFUCIUS_PRE_GPT_V65.md` 同样保持 pre-GPT 维度（"GPT Pro V65 has not been submitted or captured" 该句已与事实矛盾）。这五个门控文件之间的描述都和 `05_gptpro_review/EXTERNAL_REVIEW_STATUS.md` line 4-15 的 `real_gptpro_v65_captured_not_final_p0_source_patches_pending` 不一致。门控合规度从 V3 的“口径自洽但 Check 7 长期 fail”跌回“口径不再自洽：实际已捕获 GPT Pro 结果但门控仍写 GPT Pro pending；实际 V92 已为 Claude gate 开门但 PROMOTION 系列没有同步状态”。**这是本审 P0 V63-F3**。
4. **GPT Pro 原文档为受损/部分乱码格式。** `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md` 中的表格大量使用 `?` 占位（含 P0/P1 表头和大量 cell），明文段落（verdict、思维宝典结构判断、推理宝典结构判断、必须修补清单、禁止声明、Codex 回源验证要求）可读，但 P0-01..P0-05 与 P1-01..P1-08 表格的“位置/问题/为什么影响学生/需要回源的证据/必须动作”各列是否完全保真，需要重新核对 — `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md` 已经把表格内容重新展开到可读 markdown，但本审无法独立确认 TRIAGE_FILLED 的表格条目与 GPT Pro 原始网页/PDF 100% 一致。如果 GPT Pro 原始结果在表格里写过 TRIAGE_FILLED 未抓到的 P0 子项，会被本流程吞掉。**这是本审 P1 V63-F4**。

未达可发布门槛。下一步只能进入 V64：先按 V63-F1/V63-F2/V63-F3/V63-F4 修，然后才有资格谈 Governor / Confucius / Word / PDF 终审。

## Delta Since V3 → Post-V3 / V65 / V90-V92（Claude V63 抽样）

| V3 P0/P1 编号 | 修复路径 | 现状 |
|---|---|---|
| V3-F1 Q0026 “材料分析”第三条理由出处 | V3 之后 RF0022 / V2 body 仍未对账，本审 V63 也没复核（不在 V63 scope，留给 Codex 后续） | not addressed in V65 scope |
| V3-F2 ledger 缺 `rubric_source` 列 | `02_codex_lane/MAIN_THINKING_LEDGER.csv` line 1 表头已存在 `rubric_source` 列且全部 137 行填值（line 2-137 行均有 `gpt_sources/...` 或 `09_logs/...` 路径），`02_codex_lane/REASONING_FORM_LEDGER.csv`、`02_codex_lane/CHOICE_TRAP_LEDGER.csv` 需要进一步逐文件抽查后才能定 fully fixed/partially fixed（本审 sample 只抽到 MAIN_THINKING_LEDGER） | substantially fixed in MAIN_THINKING_LEDGER；REASONING_FORM_LEDGER 与 CHOICE_TRAP_LEDGER 待外审 V64 sample 抽查 |
| V3-F3 GPT Pro 真实提交 | `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md` 已捕获，verdict `not_final` | fully fixed for the submission gate；但 PROMOTION_LOG / QUALITY_CHECK / HOLD 未同步（V63-F3） |
| V3-F4 PROMOTION_LOG/QUALITY_CHECK notes 不点名 V3 P1 | 部分新增段（如 Post-Q0140 Promotion Log Addendum）有按行说明，但 V3-F1/F2 仍未直接进入 notes 列；并新增 stale 字段 V63-F3 | partial |
| V3-F5 GAP008 规范选言推理代表题 | `04_fusion/PROMOTION_QUALITY_CHECK.md` Immediate Quality Gaps 段写 `Q0027/Q0028` 已 source-locked，但本审未独立核对其 evidence；GAP008 在 `01_source_inventory/COVERAGE_GAP.csv` 仍需被 V64 抽查 | partial (claimed fixed locally, not externally verified) |

V3 之后另有大量 V37-V60+ 区段新增 source-lock，本审在 V65 scope 内未逐条核对；只对 V65 packet 强调的 Q0113-Q0143、Q0136-Q0140 这条主线做了真复核。

## GPT Pro V65 Reconciliation

GPT Pro V65 的五个 P0、八个 P1 与“禁止声明”十二条的处置如下：

| GPT Pro V65 finding | Codex source-routed verdict (V90/V91/V92 / TRIAGE_FILLED) | Claude V63 verdict | 必须动作 |
|---|---|---|---|
| P0-01 Q0141 source-path/internal-header suite identity conflict | V92 `source_verified_header_typo_boundary_accepted` | 仅本地 boundary 接受，未做外部核对；释放 Claude gate 但不能写“身份已确认” | V63-F1：在 V64 前请独立外部来源（如教育部门官网、教师版纸质卷、第三方教辅）补一份外部凭证；若外部确实只能查到 17-2.docx 一份，则把 V92 boundary 升级为“外部不可校的本地优先 boundary”，并在学生稿 §3/§4 处加“题源以本地档为准，仍待外部核对”一句脚注 |
| P0-02 Q0136-Q0140 B 线证据 | V90 GPTV65-002 `source_verified_summary_closed_for_claude_packet` | 本地可见性已闭合（B 线 entries.jsonl、blockers、fusion candidates、suite report 与 V90 表对齐）；但 Claude 本审只能对 V90 摘要做对账，不能替代独立外审 | 接受为 Claude 本审通过；GPT Pro / 后续外审仍需逐题复核 |
| P0-03 Q0143 大前提过宽 | V90 GPTV65-003 `source_verified_patched` | 两份推理稿已收窄为“放错了地方的资源”；句式与 V87 source-lock 一致；卷面答案句、同类题对比、章节归类均自洽 | 接受为已修复 |
| P0-04 学生稿内部痕迹 | V91 `student_safe_cleanup_patched_scan_clean` (4 份学生稿) | 4 份主学生稿干净；本审独立抽 16 个 pattern grep 复核通过；但框架检索目录_送审辅助 未被覆盖 | V63-F2：把框架检索目录_送审辅助纳入 student-safe scope 或迁出 `08_delivery/` |
| P0-05 思维宝典“待外审裁定”章节 | V91 `student_safe_cleanup_patched_scan_clean` | 框架重排稿目录头 `框架速查` 段保留为“边界与选择题陷阱 / 综合辨析与边界判断”这样的稳定学生标签，不再有 `待外审裁定`；本审独立 grep 验证 | 接受为已修复 |
| P1-01 Q0142 “必要条件”措辞 | TRIAGE_FILLED GPTV65-006 `source_verified_no_patch_now` | V87 source-lock line 32 + GAP019/GAP020 source-lock 均支持“必要条件”表述；推理稿 §1 (line 124-146) 保留“良好的创新生态只是必要条件而非充分条件”，卷面答案句和易错比较段都对齐 | 接受为可保留 |
| P1-02 Q0141 因果方法范围 | V90 GPTV65-007 `source_verified_patched` | 推理稿 §3 line 999-1001 已写“因果探求主写求异法，只有材料比较关系能对应时才补写求同法或共变法”；高粱 AT1 求异比较关系明确 | 接受为已修复 |
| P1-03 2026顺义一模 Q19(2) 目录归类 | TRIAGE_FILLED GPTV65-008 `pending` | 本审在 `08_delivery/选必三_逻辑与思维_思维宝典_框架重排送审版.md` `框架速查` 段未独立 grep 复核归类位置；属于 V64 待办 | V63-F5（P1）：在 V64 前修复 |
| P1-04 多方法题主采角度 vs 可补角度 | TRIAGE_FILLED GPTV65-009 `pending` | 同上 | V63-F6（P1）：在 V64 前修复 |
| P1-05 2025海淀二模 Q20 共同富裕节点重复 | TRIAGE_FILLED GPTV65-011 `pending` (GPT Pro 原文为 P1-04，本地 triage 编号为 P2-011) | 同上 | V63-F7（P2）：可放 V64 之后处理 |
| P1-06 推理章二级标签 | TRIAGE_FILLED GPTV65-010 `pending` | 推理稿 §同形聚合索引段（推理宝典学生稿 line 16-26）已经有八类索引，本审接受这相当于二级标签；GPT Pro 关注的“选项设计类、规范选言推理类、联言真值类、复合链类”可作为后续细化 | V63-F8（P2）：在 V64-V65 之间细化 |
| P1-07 选择题陷阱库与主观题模板分层 | TRIAGE_FILLED GPTV65-012 `pending` | 框架重排稿头部 `框架速查` 已把“边界与选择题陷阱 / 选择题误挂和模块边界：19 节”单列为一类，本审视为已分层；GPT Pro 要求“单列陷阱库”可作为最终排版细化 | V63-F9（P2）：在 V64-V65 之间细化 |
| P1-08 三段论构造题前提真实性检查（Q0143、2026海淀二模 Q20(1)、2025丰台二模 Q16(2)） | partially `source_verified_patched` for Q0143；其他两题未独立加“前提真实性检查”一句 | Q0143 已经隐含在收窄后的大前提；2026海淀二模 Q20(1) 与 2025丰台二模 Q16(2) 在三段论章 (`08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md:651-696`) 未加“前提真实性检查”脚注 | V63-F10（P1）：在 V64 前为这两题各补一句“前提真实性检查”脚注 |

GPT Pro V65 的“禁止声明十二条”与“Codex 回源验证八条”被本审完整继承到本文件“Forbidden Claims”段，不另增减。

## Student Draft Cleanliness Audit

学生送审层一共有五份 markdown：

1. `08_delivery/选必三_逻辑与思维_思维宝典_学生送审版.md`
2. `08_delivery/选必三_逻辑与思维_推理宝典_学生送审版.md`
3. `08_delivery/选必三_逻辑与思维_思维宝典_框架重排送审版.md`
4. `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md`
5. `08_delivery/选必三_逻辑与思维_思维宝典_框架检索目录_送审辅助.md`

V91 `08_delivery/STUDENT_SAFE_CLEANUP_SCAN_V91.md` 只覆盖前四份。本审 grep 复核：

- 前四份对 16 个 pattern (`原§`、`送审`、`待外审`、`外审裁定`、`source-lock`、`ledger`、`Codex`、`Claude`、`teacher-key`、`old-index`、`wrong-option`、`证据等级`、`不是终稿`、`本稿`、`V[0-9]{2}`、`review`、`draft`) 全部 `0` hit，与 V91 一致。
- 第五份 `选必三_逻辑与思维_思维宝典_框架检索目录_送审辅助.md` 命中（文件名含“送审”；正文亦含 student-facing 索引词）。
- 抽查正文质量：思维宝典学生送审版头部 (line 1-15) 已经把“使用顺序”写成了零基础学生能直接读的入口；推理宝典学生送审版头部 (line 1-26) 提供同形聚合索引并把 §1-§63 按推理形式聚合；框架重排稿头部 (line 1-22) 把 73 节按 14 个思维节点归类；推理题型重排稿头部 (line 1-22) 把 64 节按 8 个推理形式章归类。文中“最终” (示例 line 42/59 思维宝典框架重排稿) 都指题目材料本身的“最终完成提案 / 最终确认”，没有任何“宝典已最终发布”的用法。

verdict: **主四份达 student-safe 标准（pass-equivalent under V91 scope）；第五份未达 student-safe 标准**。第五份不能继续以 `08_delivery/选必三_逻辑与思维_…_送审辅助.md` 的形态进入下一轮 packet。

## Framework-First Thinking Structure Audit

`08_delivery/选必三_逻辑与思维_思维宝典_框架重排送审版.md`：

- 章节归类按思维方法链：科学思维 / 客观性、预见性、可检验性（8 节）、科学思维 / 科学总帽下的复合触发（3 节）、超前思维（10 节）、辩证思维（分析与综合/动态性/辩证否定/矛盾分析等共 14 节）、创新思维（思路新、联想思维、发散与聚合共 11 节）、思维抽象与思维具体（5 节）、边界与选择题陷阱（19 节）、综合辨析与边界判断（3 节）。共 73 节，与 V63 学生送审版的 73 节对齐。
- 题节体例统一：每节给“对应题”→“材料动作”→“为什么能想到这些方法”→“卷面答案句”→“易错边界”。材料动作—方法触发链没有被打散为概念词典。本审抽查 `题组65 (Q0127 2026海淀二模 Q18(1))` 与 `题组35 (Q0069 2024门头沟一模 Q20)` 与 `题组72 (Q0139 2026顺义二模 Q18(1))` 三节，均完整保持 V63 触发链；卷面答案句忠实于评分细则。
- 框架速查段 (line 9-22) 没有把“待外审裁定”作为一个章节标题；该段已与 GPT Pro V65 P0-05 兼容。
- GPT Pro V65 P1-03 关注的“2026顺义一模 Q19(2) 在超前思维章但正文提醒不要这样写”，本审在 `框架重排送审版.md` `超前思维` 段未独立 grep 复核归类位置（V63 scope 内无足够时间），列入 V63-F5。

verdict: **框架优先 (framework-first) 结构条件已满足；触发链条未被概念词典化；个别归类目录冲突需要在 V64 前修复**。

## Reasoning-Form Chapter Audit

`08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md`：

- 题型速查段 (line 8-16) 列出 8 大推理形式章；八章内部共 64 个内容块，与 V65 packet 自述完全一致。
- 同形聚合体现为：章内每节都给出“推理形式 / 可检查式子 / 卷面答案句 / 同类题对比”四块；同形不同情境分小节但都回到同一形式树。例如类比推理章把晏子、海草迁移、长白山、月球毛、Q0141 高粱基因→水稻基因迁移聚合在同一章。
- Q0142 进入“充分条件假言推理与充分条件判断”章的“补充§1” (line 124-146)，与“题组1 充分条件肯定后件错误”并列，对比角度清晰。
- Q0143 进入“三段论、性质判断周延与换质位”章的“补充§2” (line 672-696)，与“题组33 性质判断周延” / “题组28 三段论形式有效不等于结论真实”形成同章对比。大前提收窄后样本可教。
- Q0141 双挂确实落地：在“归纳推理与探求因果联系”章作为“补充§3” (line 995-1017) 主写求异法；同一题号在“类比推理”章作为“补充§4” (line 1107-1129) 写从高粱 AT1 到水稻 GS3 的相似属性迁移。两节都把题号、对应题、推理形式、可检查式子、卷面答案句、同类题对比完整列出，互不冲突；但都没有显式声明“本题在另一章亦有侧面登记，请按答题要求选用单一角度”的脚注，导致学生若顺读容易在两个章节背两套答句。
- “真假关系、逻辑规律与关系判断”章包含 13 节，覆盖矛盾律、同一律、排中律、反对/下反对关系、关系判断等。

verdict: **同形聚合 (reasoning-form-first) 结构已满足；Q0141 双挂虽然两章各自正确，但缺少跨章互引脚注；Q0143 已修复**。

## Remaining P0 / P1 Findings

| # | 严重度 | 文件 / 位置 | 问题 | 必须修正 |
|---|---|---|---|---|
| V63-F1 | **P0** | `04_fusion/Q0141_SOURCE_IDENTITY_RESOLUTION_V92.md`；`08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md:995-1017,1107-1129`；`08_delivery/选必三_逻辑与思维_推理宝典_学生送审版.md` 对应位置 | Q0141 source identity 仍只是 Codex 本地 boundary：path + 旧 ledger + DOCX 内部 `一模` header 三方互证后判 header 为 stale typo，并和真 2024东城一模 Q17(2)（北极熊毛衣）题面差异作旁证。这一判定 GPT Pro V65 P0-01 七项证据中只覆盖了 source path、ledger、internal-header 三项；PDF 原题、答案表、评分细则、suite report 四项没有以独立外部凭证形式入档。Claude 接受 V92 作为 release-blocker 释放（不再阻断 Claude 入审），但不能升格为“题源身份已确认”。 | (a) 在 V64 前请用户或 Codex 提供 2024东城二模 Q17(2) 原题 PDF / 教辅 / 答案表 / 评分细则 PPT 任一外部独立凭证存档；(b) 若搜遍仍无外部 PDF 或教辅可校，则把 V92 boundary 在两份推理稿 §3/§4 处加一句脚注：“题源以本地档为准，仍待外部核对，请教师在使用前对照纸质卷再确认”；(c) PROMOTION_HOLD 增 Q0141 行，hold reason 写 “source identity locally bounded, not externally verified”。 |
| V63-F2 | **P0** | `08_delivery/选必三_逻辑与思维_思维宝典_框架检索目录_送审辅助.md`；`08_delivery/STUDENT_SAFE_CLEANUP_SCAN_V91.md`；`10_packets/GPTPRO_REVIEW_PACKET_V65.md:32-37` | V63 packet read 第 18 条把“框架检索目录_送审辅助” 列为送审件（实质 student-facing），但 V91 student-safe scope 只覆盖四份学生稿，跳过本文件。文件名含“送审”、正文按现有结构是学生“按节点快速检索”的辅助入口，不应保留 student-facing 形式的工作流措辞。 | (a) 把本文件纳入 V91 scan scope 并按四份学生稿同步清理；或 (b) 将本文件从 `08_delivery/` 迁到 `09_logs/` 或 `07_governor_confucius/` 作为 audit-only annex，并在 V65/V64 packet 中把它从 student-facing 第 18 条改为 audit annex；(c) STUDENT_SAFE_CLEANUP_SCAN_V91 同步增加一行新报告。 |
| V63-F3 | **P0** | `04_fusion/PROMOTION_LOG.md` Current Status 字段与 check7 列；`04_fusion/PROMOTION_QUALITY_CHECK.md` Current Ratings 表 external review 列；`04_fusion/PROMOTION_HOLD.md` Current External-Review Hold V70 段；`07_governor_confucius/STUDENT_REVIEW_DRAFT_GOVERNOR_PRE_GPT_V65.md` Findings 表与 verdict；`07_governor_confucius/STUDENT_REVIEW_DRAFT_CONFUCIUS_PRE_GPT_V65.md` Verdict 段 | 这五个门控文件还停在 V3 NOT_PASS / GPT Pro pending 状态：(i) PROMOTION_LOG 全表 check7 列写 `fail: Claude V3 NOT_PASS, GPT Pro pending`，状态名 `CLAUDE_V3_NOT_PASS_GATE_HOLD` 没有反映 V65/V90/V91/V92；(ii) PROMOTION_QUALITY_CHECK Current Ratings 表 external review 列全行写 `fail: Claude V3 NOT_PASS, GPT Pro pending`；(iii) PROMOTION_HOLD 状态字段仍写 `ACTIVE` + V70 段，没有 V90-V92 同步；(iv) GOVERNOR_PRE_GPT_V65 verdict 仍 `NOT_FINAL_READY_FOR_GPTPRO_V65_AFTER_BROWSER_FIX`，与 GPT Pro V65 已捕获事实矛盾；(v) CONFUCIUS_PRE_GPT_V65 仍写“GPT Pro V65 has not been submitted or captured”，同样矛盾。门控合规度从 V3 的“口径自洽但 Check 7 长期 fail”跌回“口径与事实不一致”。 | (a) PROMOTION_LOG 增 `2026-05-25 GPT_PRO_V65_CAPTURED_NOT_FINAL_POST_PATCH_V90_V91_V92` 段，check7 列写 `not_final: GPT Pro V65 captured, Codex P0 patched V90/V91/V92, Claude V63 NOT_PASS pending V64`；(b) PROMOTION_QUALITY_CHECK 增 “2026-05-25 Post-GPT-V65 Ratings Addendum” 段，把 external review 列改为按行写明 `GPT Pro V65 not_final / Claude V63 NOT_PASS / Codex P0 patched V90/V91/V92`；(c) PROMOTION_HOLD 增 V92 段保留 V70 段；(d) Governor 与 Confucius 在 `07_governor_confucius/` 新增 `STUDENT_REVIEW_DRAFT_GOVERNOR_POST_GPTPRO_V65.md` 与 `STUDENT_REVIEW_DRAFT_CONFUCIUS_POST_GPTPRO_V65.md`，把 verdict 改为 post-GPT 维度。 |
| V63-F4 | **P1** | `05_gptpro_review/GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md`；`05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md` | GPT Pro 原结果文件中 P0/P1 表的大量 cell 显示为 `?`（OCR/编码受损或抓取丢字）。明文段落（verdict、思维宝典/推理宝典结构判断、必须修补清单、禁止声明、Codex 回源验证八条）可读，但表格列内容只能从 TRIAGE_FILLED 反推。如果 GPT Pro 在表格里写过 TRIAGE_FILLED 没抓到的子项（例如某 P1 在表里点名了具体题号或文件路径，明文段没复述），本流程会吞掉它。 | (a) 在 V64 前重新提交一次 GPT Pro V65 截图或 plaintext 重抓，确认表格列内容；(b) 若 GPT Pro 无法重抓，则在 GPTPRO_EXTERNAL_REVIEW_RESULT_V65.md 顶端加 ENCODING_DAMAGE 段，说明 P0/P1 表格列由 TRIAGE_FILLED 重建，TRIAGE_FILLED 的字段以本仓 source-routed verdict 为准；(c) 保留原始文件，不要覆盖。 |
| V63-F5 | **P1** | `08_delivery/选必三_逻辑与思维_思维宝典_框架重排送审版.md` 超前思维段；`02_codex_lane/MAIN_THINKING_LEDGER.csv` Q0019 / 2026顺义一模 Q19(2) 对应行 | GPT Pro V65 P1-03 / GPTV65-008 指出 2026顺义一模 Q19(2) 主线是科学思维三性，被放在超前思维章；正文又提醒不要写超前。目录与正文矛盾会在零基础学生层面造成迷路。本审 V63 scope 内未独立 grep 复核归类位置。 | (a) 在 V64 前回源 2026顺义一模 Q19(2) 评分细则确认主线；(b) 把节点从超前思维章移到科学思维三性章，超前章保留交叉索引；(c) 同步 MAIN_THINKING_LEDGER。 |
| V63-F6 | **P1** | `08_delivery/选必三_逻辑与思维_思维宝典_框架重排送审版.md` 多方法主观题段（共同富裕、京津冀、北京城市图书馆、低空经济、温榆生态心等节）；`02_codex_lane/MAIN_THINKING_LEDGER.csv` 对应行 | GPT Pro V65 P1-04 / GPTV65-009 指出多方法题需要“主采角度”vs“可补角度”标识，否则限时作答容易堆砌。本审 V63 抽查 Q0127、Q0050、Q0054、Q0046 等节，确认未加显式主采/可补标识。 | (a) 在 V64 前对每道多方法主观题增加“主采角度”与“可补角度”两行；(b) 评分细则只支持单一主线时，把“可替代”一律改为“分值不足时补写”或“题干允许时补写”；(c) MAIN_THINKING_LEDGER 增 `primary_angle` / `supplementary_angle` 两列。 |
| V63-F7 | **P1** | `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md:995-1017,1107-1129`；同号两节 | Q0141 在“归纳推理与探求因果联系”章与“类比推理”章各自独立成节，缺少“另见本册 类比章 补充§4 / 另见本册 归纳章 补充§3”的跨章脚注。学生若顺读两章会以为是两题，背两套答句，临考时混淆主线。 | (a) 在两节末各加一句 “另见本册 类比章/归纳章 补充§4/补充§3 同题号 Q0141 的另一侧面，答题时只按题干设问选其一作主线”；(b) 同步推理学生送审版同位置；(c) STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88 增 cross-link 段。 |
| V63-F8 | **P1** | `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md` 选言/联言/复合推理章、真假关系/逻辑规律/关系判断章；`08_delivery/选必三_逻辑与思维_推理宝典_学生送审版.md:16-26` | GPT Pro V65 P1-06 / GPTV65-010 指出复合推理章与真假关系章容量大，学生易把“选言判断完整性”和“规范选言推理有效式”混用，把“矛盾律 vs 同一律 vs 反对关系”混用。本审接受当前同形聚合索引段已经部分缓解，但章内仍可加二级标签。 | (a) 复合推理章首加二级标签：问卷选项 / 规范选言推理 / 联言真值 / 复合链；(b) 真假关系章首加“先判真假关系→再判逻辑规律→再判关系判断”顺序提示；(c) 同步推理学生送审版同位置。 |
| V63-F9 | **P1** | `08_delivery/选必三_逻辑与思维_思维宝典_框架重排送审版.md` 边界与选择题陷阱（19 节）；`08_delivery/选必三_逻辑与思维_思维宝典_学生送审版.md` 对应段 | GPT Pro V65 P1-07 / GPTV65-012 指出选择题陷阱与主观题模板混排会降低主观题模板稳定感。当前框架重排稿已经把“边界与选择题陷阱”单列章组，但学生送审版主体仍按 §1-§73 顺序混排。 | (a) 在最终排版（Word/PDF 前）单列“选择题陷阱库”作为附录；(b) 主体 §1-§73 仅保留主观题模板与触发链；(c) STUDENT_REVIEW_DRAFT_CLEANUP_NOTE 增分册段。 |
| V63-F10 | **P1** | `08_delivery/选必三_逻辑与思维_推理宝典_题型重排送审版.md` 三段论章（含 2026海淀二模 Q20(1) / 2025丰台二模 Q16(2)） | GPT Pro V65 P1-08 / Codex 回源验证第 8 条要求三段论构造题每题加“前提真实性检查”脚注。Q0143 已通过收窄大前提隐含修复；2026海淀二模 Q20(1) 与 2025丰台二模 Q16(2) 在三段论章尚未加显式脚注。 | (a) 在两题节末各加一句“前提真实性检查：大前提是否过宽？小前提与中项是否一致？”；(b) REASONING_FORM_LEDGER 对应行增 `premise_truth_check` 字段；(c) 抽查“题组24 / 题组60”等同类节是否也漏写。 |
| V63-F11 | **P2** | `04_fusion/PROMOTION_LOG.md`；`04_fusion/PROMOTION_QUALITY_CHECK.md` row 列 | V3-F2 / V3-F4 老问题：PROMOTION_LOG 和 PROMOTION_QUALITY_CHECK 的 row 列仍合并多题；Q0011 / Q0017 / Q0019 / Q0020 / Q0023 / Q0026 / Q0136-Q0140 / Q0141-Q0143 等焦点题仍未单行化。 | (a) 在 V64 PROMOTION_LOG / PROMOTION_QUALITY_CHECK 增量段把焦点题逐题展开；(b) notes 列按行点名 V63-F1..V63-F10。 |
| V63-F12 | **P2** | `02_codex_lane/REASONING_FORM_LEDGER.csv`、`02_codex_lane/CHOICE_TRAP_LEDGER.csv` | V3-F2 老问题：MAIN_THINKING_LEDGER 已经加了 rubric_source 列且完整填值（本审独立看到 MT0001-MT0065 行 137 行均有路径或行号）；但 REASONING_FORM_LEDGER、CHOICE_TRAP_LEDGER 是否同步、是否覆盖到 RF/CT 全表（含 V90 改写后的 Q0143 主前提收窄证据），本审 V63 scope 未独立抽查。 | (a) 在 V64 sample 抽 RF0001-RF0080 / CT0001-CT0066 各 5 行复核 rubric_source 列是否齐；(b) 至少 RF/CT 中与 V90/V91/V92 patch 直接相关行须填值。 |

P0 = V64 启动前必须修；P1 = V64 前必须修，不修则学生 / 后续阶段会被误导；P2 = V64-V65 之间内可放。

## Gate Audit

| 文件 | 当前状态 | 是否自洽 | 处置 |
|---|---|---|---|
| `04_fusion/PROMOTION_LOG.md` | Current Status `CLAUDE_V3_NOT_PASS_GATE_HOLD`；check7 全行写 `fail: Claude V3 NOT_PASS, GPT Pro pending` | 与 `05_gptpro_review/EXTERNAL_REVIEW_STATUS.md` 中 `real_gptpro_v65_captured_not_final_p0_source_patches_pending` 不一致 | V63-F3 |
| `04_fusion/PROMOTION_QUALITY_CHECK.md` | external review 列全行 `fail: Claude V3 NOT_PASS, GPT Pro pending` | 同上 | V63-F3 |
| `04_fusion/PROMOTION_HOLD.md` | Status `ACTIVE`；V70 段为最近段 | 缺 V92 同步段 | V63-F3 |
| `05_gptpro_review/EXTERNAL_REVIEW_STATUS.md` | `real_gptpro_v65_captured_not_final_p0_source_patches_pending` | 与 V90/V91/V92 一致 ✓ | 本文件写盘后追加 Claude V63 段 |
| `06_claude_review/EXTERNAL_REVIEW_STATUS.md` | 未读全（文件过大）；本审仅依赖 packet 与 V3 段 | 不在本审深度审范围 | 本文件写盘后追加 Claude V63 段 |
| `01_source_inventory/2026_ERMO_SUITE_CLOSURE_REPORT.md` | A 线本地闭合 `A_line_local_suite_closed_pending_B_line_and_external_review`；与 V90 GPTV65-002 / B 线 result 一致 | 自洽 ✓ | 不动 |
| `01_source_inventory/SUITE_COVERAGE_AUDIT_V87.md` | `SUITE_COVERAGE_AUDIT_UPDATED_EXTERNAL_REVIEW_PENDING`；143 行；Q0141 source-identity flag 已与 V92 boundary 互补 | 自洽 ✓；建议追加 V92 段交叉引用 | V64 时增交叉引用 |
| `07_governor_confucius/STUDENT_ARTIFACT_TRACEABILITY_DELTA_V88.md` | 153 行；matched 153；Q0141 双挂；Q0141 source-identity flag 保留 | 自洽 ✓ | 不动 |
| `07_governor_confucius/STUDENT_REVIEW_DRAFT_GOVERNOR_PRE_GPT_V65.md` | verdict `NOT_FINAL_READY_FOR_GPTPRO_V65_AFTER_BROWSER_FIX`；Findings 表写 GPT Pro fail | 与事实不符 | V63-F3 |
| `07_governor_confucius/STUDENT_REVIEW_DRAFT_CONFUCIUS_PRE_GPT_V65.md` | 写 GPT Pro V65 未提交 | 与事实不符 | V63-F3 |
| `03_claudecode_lane/blockers_2026_ermo.csv` | B2026ERMO-016 仍 `open_external_review`；required_action 段已说明 V92 已闭合 source-identity gate | 自洽 ✓（已记录 V92） | 不动；本文件写盘后建议增一行 Claude V63 段 |
| `03_claudecode_lane/fusion_candidates_2026_ermo.csv` | F2026ERMO-001..012 均 `patched_*` | 自洽 ✓ | 不动 |
| `04_fusion/GPTPRO_V65_SOURCE_PATCH_AUDIT_V90/V91/V92.md` | V90 partial / V91 student-safe patched / V92 Q0141 boundary accepted | 自洽 ✓ | 不动 |
| `05_gptpro_review/GPTPRO_V65_TRIAGE_FILLED.md` | `READY_FOR_CLAUDE_V63_AFTER_GPTPRO_TRIAGE`；P0 全部 ready_for_claude；P1 大量 pending | 自洽 ✓；GPT Pro 原文档表格受损（V63-F4）需要并行处理 | 不动 |

总结：捕获 GPT Pro V65 后，V92 已为 Claude gate 开门；但 PROMOTION / Governor / Confucius 三类门控未跟上现实状态，门控合规度本审降为“事实领先于门控自身字段”。Claude V63 必须在本文件中明示这条裂口，避免后续把“V92 开门”当作“门控全部对齐”。

## Required Next Patches（按学生使用风险倒序）

1. **`08_delivery/选必三_逻辑与思维_思维宝典_框架检索目录_送审辅助.md` student-safe 清理或迁出**（V63-F2）。把它纳入 V91 scan scope 并重命名为不含“送审”的学生检索目录；或迁出 `08_delivery/`。
2. **门控状态同步**（V63-F3）。PROMOTION_LOG / PROMOTION_QUALITY_CHECK / PROMOTION_HOLD / Governor / Confucius 五处同步 V90/V91/V92 + V63 状态。
3. **Q0141 source identity 外部凭证**（V63-F1）。提供 2024东城二模 Q17(2) 原题 PDF/教辅/答案表/评分细则 PPT 任一外部独立凭证存档；或在两份推理稿同节加“题源仍待外部核对”脚注。
4. **GPT Pro V65 原结果编码受损处理**（V63-F4）。重抓表格或在原文档顶端加 ENCODING_DAMAGE 段说明。
5. **Q0141 双挂跨章互引脚注**（V63-F7）。两节末加“另见本册 类比章/归纳章 补充§4/补充§3”。
6. **多方法题主采/可补角度标识**（V63-F6）。MAIN_THINKING_LEDGER 增字段；学生稿增标识。
7. **2026顺义一模 Q19(2) 目录归类回源**（V63-F5）。从超前思维章移到科学思维三性章，超前章保留交叉索引。
8. **三段论构造题前提真实性检查脚注**（V63-F10）。2026海淀二模 Q20(1) / 2025丰台二模 Q16(2) 各加一句。
9. **复合推理章 / 真假关系章二级标签**（V63-F8）。问卷选项 / 规范选言推理 / 联言真值 / 复合链；先判真假关系→再判逻辑规律→再判关系判断。
10. **选择题陷阱库与主观题模板分册**（V63-F9）。最终排版前单列陷阱库附录。
11. **PROMOTION_LOG / PROMOTION_QUALITY_CHECK row 列逐题展开**（V63-F11）。焦点题单行化；notes 列按行点名 V63-F1..V63-F10。
12. **REASONING_FORM_LEDGER / CHOICE_TRAP_LEDGER rubric_source 列抽查**（V63-F12）。各 5 行复核。
13. **PROGRESS.md 状态码追加 Claude V63**。建议：`CLAUDE_V63_NOTPASS_GPT_V65_CAPTURED_SOURCE_ROUTED_PATCHED_Q0141_LOCAL_BOUNDARY_AUX_DIR_PENDING_PROMOTION_GATES_STALE_BEFORE_V64`。
14. **EXTERNAL_REVIEW_STATUS 加 V63 段**（本文件写盘后调度方动作）。含 runner、result、return_code、verdict、summary，与 V0/V1/V2/V3 段格式对齐。
15. **真实启动 Claude V64 外审**（仅在 #1-#4 修完后才有资格）。本文件写盘前不要直接进入。

## Coverage Pressure（V63 视角）

- source-locked 行 V63 期已达 153 行（V88 traceability），其中 Q0141-Q0143 三行需 V64 复核身份与同形归类。
- 2026 二模 Q0113-Q0140 已经全部 source-locked + B 线复跑 + 本地 patched_pending_external_review；进入 V64 时按 V90 GPTV65-002 表逐题再核。
- 2024 / 2025 backlog (GAP005/GAP006) 在 V3 之后大量新增，本审 V63 scope 未独立逐行核对，列为 V64 抽查。
- GAP008 规范选言推理：V3-F5 残项，本地声明已通过 Q0027/Q0028 source-locked，未独立外部核对，V64 须复核。
- GAP010 GPT Pro 外审：V65 已捕获，但 V92 boundary 不等于 GPT Pro 对 Q0141 的二次确认，coverage 计数已减但未清零。
- 评标实录 / 讲评 PPT 三角证据：本审未独立扩查。

## Forbidden Final Claims

下列说法在任何 user-facing 产物（宝典 MD / DOCX / PDF / README / 进度小结 / 移交消息 / 用户对话）中**均不得书写、不得显示、不得暗示**：

- 不得写 “选必三《逻辑与思维》宝典 已完成 / 终稿 / 定稿 / 最终版 / V63 / V64 / V65 终稿”。
- 不得写 “已穷尽 2024-2026 三年北京选必三考题”、“全量覆盖”、“已覆盖所有选必三题”。
- 不得写 “已经过 Claude 外审 / 通过 Claude review / Claude PASS”。V0/V1/V2/V3 + 本审 V63 共五次 NOT_PASS。
- 不得写 “已经过 GPT Pro 外审 / GPT Pro 已通过 / GPT Pro 已认可”。GPT Pro V65 真实 verdict 为 `not_final`，不是 pass。
- 不得宣称 “GPT Pro V65 已同意发布”或类似口径。
- 不得宣称 “Q0141 source identity 已确认 / 已闭合 / 已解决”。V92 是 Codex 本地 boundary（path + ledger + internal-header 互证 + 与真 2024东城一模 Q17(2) 题面比对），未引入独立外部凭证。可写的最强表述是 “Q0141 题源已按本地档接受为 2024东城二模 Q17(2)，仍待外部核对”。
- 不得宣称 “Q0141-Q0143 已全部安全”。Q0142 / Q0143 可写为 “source-supported，待终审”；Q0141 必须保留 V63-F1 P0 后缀。
- 不得宣称 “2026 二模 B 线复跑已足以支撑 Q0136-Q0140 进入 Claude / 进入终稿”。本审仅接受 V90 GPTV65-002 为 “可见性闭合”，不是 “外审闭合”。
- 不得宣称 “学生可见稿已经完成内部痕迹清理”。4 份主学生稿干净；第 5 份 `08_delivery/选必三_逻辑与思维_思维宝典_框架检索目录_送审辅助.md` 仍 fail V63-F2。
- 不得宣称 “PROMOTION_LOG / PROMOTION_QUALITY_CHECK / PROMOTION_HOLD 已与现实状态一致”。V63-F3 P0 明示三处仍写 `Claude V3 NOT_PASS, GPT Pro pending`，与 GPT Pro V65 已捕获事实矛盾。
- 不得宣称 “Governor / Confucius 已对 V65 完成 post-GPT 审”。当前 `STUDENT_REVIEW_DRAFT_GOVERNOR_PRE_GPT_V65.md` 与 `STUDENT_REVIEW_DRAFT_CONFUCIUS_PRE_GPT_V65.md` 仍是 pre-GPT 维度。
- 不得宣称 “Word 成品已完成 / Word QA 已通过 / DOCX 可下发”。
- 不得宣称 “PDF 成品已完成 / PDF QA 已通过 / PDF 可下发”。
- 不得宣称 “可作为学生练习材料 / 可直接发学生 / 可印刷下发 / 可作期末复习底稿 / 可入终稿 / 可入印 / 入交付”。
- 不得宣称 “A/B 双线已对齐 / 双线闭合 / 双线一致” —— ledger 抽查未在 V63 scope 全覆盖（V63-F12）。
- 不得宣称 “BLK-013 / B2026ERMO-016 已闭合”。本审接受 V92 释放 Claude gate，但 blockers_2026_ermo.csv 仍 `open_external_review`。
- 不得宣称 “覆盖缺口已收口” / “缺口已收尾”。GAP008 残口、Q0141 外部凭证残口仍在。
- 不得宣称 “规范选言推理已覆盖”。GAP008 P0 在 V3-F5 之后只完成本地声明，未独立外部核对。
- 不得给区 / 年份 / 试卷-级完成率数字（仍 153 / 估计更高）。
- 不得引用本审结果反过来说 “Claude V63 已确认 Q0141-Q0143 教学语言无问题”。本审深度核了 Q0141 source identity boundary 与双挂跨章互引、Q0142 / Q0143 措辞与源支持、Q0136-Q0140 B 线可见性、4 份主学生稿 student-safe scan、框架重排 / 题型重排结构条件、门控自身状态裂口；未对每条逐字回源原始试题与细则。
- 不得把 `PROMOTION_LOG` 中含 `pending_next_external_review` / `v2_body_coverage_added_hold_external_review_and_gaps` / `f1_crossref_fixed_pending_body_rewrite_and_next_review` / `source_locked_hold_pending_next_external_review` / `choice_options_embedded_hold_other_gates` 字样的状态名解读为 “已通过 V63 门”。本审仍 NOT_PASS。
- 不得宣称 “V90 / V91 / V92 已闭合全部 GPT Pro V65 P0”。V90 / V91 / V92 闭合的是 GPTV65-002/003/004/005 与 GPTV65-001 的本地 boundary；GPT Pro 原始 P0-01 七项证据未全覆盖，GPT Pro V65 P1 仍多数 pending。
- 不得宣称 “Q0141 双挂已经过 Claude 外审确认”。本审接受双挂的两节内容各自正确，但同时点名 V63-F1（外部凭证）与 V63-F7（跨章互引脚注）两项必须修补。
- 不得宣称 “框架重排 / 题型重排稿等于宝典正文”。它们仍是 review draft；选择题陷阱库未分册（V63-F9）、多方法主采/可补未标识（V63-F6）、目录归类冲突未消除（V63-F5）。
- 不得在 PROGRESS.md 状态码中把 `CLAUDE_V63_DONE_NOT_PASS` 简写为 “Claude V63 done” —— 必须保留 NOT_PASS 后缀。
- 不得宣称 “post-GPTPro 补丁已闭环 / 已收口”。本审 V63 仍 NOT_PASS；V63-F1 / V63-F2 / V63-F3 / V63-F4 至少四项 P0/P1 仍 open。
- 不得宣称 “Q0143 已与 2025西城期末 Q17(2) 评分细则原文 1:1 对齐”。本审仅接受 V90 source-routed 收窄后样本 self-consistent；未独立打开评分细则 PDF 行号。
- 不得用 “Claude 外审 V63 通过 / Claude V63 PASS / Claude V63 approved” 表述本文件。本文件结论是 `EXTERNAL_REVIEW_DONE_NOT_PASS`。

下一可达状态（建议命名）：`V63_EXTERNAL_REVIEWED_REQUIRES_AUX_DIR_CLEANUP_PROMOTION_GATE_SYNC_Q0141_EXTERNAL_EVIDENCE_AND_GPTPRO_ENCODING_FIX_BEFORE_V64`。

— Claude 外审 V63（独立 lane）· 完
