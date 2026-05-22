# Claude Cowork E — Ready for Reasoner Decision

生成时间: 2026-05-19
范围: 基于 `suite_exhaustive_claudecode_corrected_20260519` 包对 65 道选必二《法律与生活》核心主观题完成的全题完善审查。

---

## COWORK_VERDICT: CONDITIONAL_PASS

---

## 1. 总体裁定

当前 65 题作为**"全题完善后"的开放观察输入**: **可，但需先执行第 2 节列出的硬阻塞修订**。

- 题集**结构层**（题数、阶段、套卷矩阵、边界表、reference_only 名单、阶段修正、边界不混入）通过审查；
- 题集**文本层**（material/ask/rubric atoms 的内容质量、文本字段完整性）存在系统性问题，主要由 OCR/text 层提取失败传递而来；
- 因此**不允许直接送 GPT-5.5 Pro / Claude Opus 做框架级开放观察**，但可继续生成"双模型开放观察输入包"——前提是**先把第 2.1–2.4 节的硬阻塞修复并随包附带**或**在输入包内显式降级标注**。

## 2. 必须在送 GPT-5.5 Pro / Claude Opus 前修的 patch

### 2.1 ask_text 为空且 ask atom 为占位符（19 条 — 硬阻塞）

19 条记录的 ask_text 字段为空，ask atom 使用 `ask_function_plain="不确定" / student_task_plain="从材料与法律证据中判断作答任务"` 占位符。
必须从 `full_question_text` 解析出原始设问句，回写 ask_text；并重写 ask atom 的 ask_function_plain、student_task_plain、module_requirement、requires_* 五个字段。
受影响题目清单见 `claude_cowork_question_refinement_report.md` 第 3.1 节与 `claude_cowork_ask_atom_patch_suggestions.csv` 中 must_fix_before_reasoner=yes 的 20 行。

### 2.2 material_text == rubric_text 全文泄漏（8 条 — 硬阻塞）

`CC0019_2024_朝阳_一模_19, CC0092_2025_东城_期末_19_1, CC0214_2025_门头沟_一模_20_2, CC0245_2026_东城_期末_18_2, CC0317_2026_海淀_期末_18, CC0318_2026_海淀_期末_18_2, CC0319_2026_海淀_期末_19, CC0353_2026_西城_期末_17`。

必须从 paper 原 PDF/PPTX 回源 OCR 重抽 material_text，重新生成 material atoms，并重新对齐 `related_material_atom_ids`。
若 formal 题源回不来：临时降级为 `reference_only` 或剥离至 boundary；**绝不允许在 formal 框架内继续使用现有 material atoms（因为 atoms 实为细则/答案句）**。

### 2.3 material_text 实为答案分点（2 条 — 硬阻塞）

`CC0131_2025_房山_一模_19, CC0180_2025_海淀_期末_20`。
处置同 2.2。

### 2.4 CC0364_2026_通州_期末_19_1 ask_text 模块错挂（1 条 — 硬阻塞）

该记录的 ask_text 是 19(2) 的《逻辑与思维》设问，而 question_id 与细则 `R_..._01` 对应的是 19(1) 法律部分。
必须:
- 回源拿到 19(1) 真实法律设问填入 ask_text；
- 将 R_..._02 ~ _08 这 7 条逻辑评分 rubric atom 从核心法律 rubric 表移出（不属于 19_1）；
- 重新计算 ask atom 的 module_requirement 与 requires_* 字段。

### 2.5 pending_locator_check 状态 10 条 + 8 条阶段修正题（locator 复核 — 硬阻塞）

`merge_status='pending_locator_check'` 的 10 条加上 8 条 stage_corrected_locator 题，必须由 Codex/ClaudeCode 在 reasoner 阶段前过一次 locator 复核，确认 source_locator/paper_page/rubric_page 指向的 F-id 与文件夹一致。
完成后请生成一份 `cowork_patch_apply_audit.md` 附在双模型输入包内。

## 3. 可在送 reasoner 前清理但不强制阻塞的修订

- 17 题"单 rubric atom 但 phrase 过长且多句聚合" → split。
- 33 个 ">200 字" rubric atom（part of 上一项） → split。
- 27 个 material atom 仅含 `[page X]/[slide X]/第X页/共X页` → delete。
- 16 个 rubric atom `what_judgment_student_must_make_before_writing` 长度 <15 字 → 替换为题域具体判断。
- 3 个 ask atom `module_requirement=不确定` → 标定为"法律与生活"。
- kmv 与 can_be_written_without_material 不一致条目 → 按 kmv 包含 material 时 no_mat=no、kmv=knowledge 单一时 no_mat=yes/uncertain 修正。
- `related_material_atom_ids` 字段统一 `|` 分隔符 → 在 reasoner schema 文档中显式声明。
- 14 个 paper_file 字段空 → 显式补齐。
- 6 个 material_text 含细则关键词（评分/酌情/答出/参考答案）→ 检查是否为材料原文叙述并按需清洗。

详见 6 个 patch / risk CSV。

## 4. 是否还可能漏题

- 经矩阵 + 边界表 + missed-core 文件 + 65 题字段比对，**未发现新的实质性漏题候选**；
- BLOCKED_2026_石景山_期末_17 是源阻塞，不构成漏题；
- 上述 8+2 条 OCR/源问题若回源成功，会增加 material atom 数量，但不会增加题数。

## 5. 是否有 reference_only 被误升 formal

- **否**。4 条 reference_only(CC0040, CC0162, CC0311, CC0353) 全部保持 `teacher_reference_answer + reference_only`，与其 rubric atoms 类型与等级一致。

## 6. 是否有 formal 需要降级

- **现状不主动降级**。但如下 7 条 formal 在 OCR 回源失败时**必须降级**：
  `CC0019_2024_朝阳_一模_19; CC0092_2025_东城_期末_19_1; CC0214_2025_门头沟_一模_20_2; CC0245_2026_东城_期末_18_2; CC0317_2026_海淀_期末_18; CC0318_2026_海淀_期末_18_2; CC0319_2026_海淀_期末_19`
- 此外 `CC0131_2025_房山_一模_19, CC0180_2025_海淀_期末_20`(material=答案分点) 同样存在降级风险。
- 即合计 **最多 9 条 formal 在最坏情况下会被临时降级到 reference_only/boundary**。

## 7. 是否有阶段/区县/题号/小问错挂

- 阶段错挂: **无残留**(7+1 条修正全部到位)。
- 区县错挂: **无**。
- 题号错挂: **无**。
- 小问错挂: **1 条**——CC0364_2026_通州_期末_19_1 的 ask_text 指向 19(2) 逻辑模块，对应 question_id _19_1 法律的实际设问需回源补齐。

## 8. 是否允许 Codex 继续生成双模型开放观察输入包

**允许，但有 4 个前置条件：**

1. **先应用 §2.1–§2.4 的硬阻塞 patch**：补齐 19 条空 ask_text、修复 8+2 条 material 文本泄漏与 CC0364 模块错挂、过完 18 条 locator 复核；
2. 对暂时无法回源的 formal 条目，在 reasoner 输入包内显式标注 `temporary_evidence_level=reference_only`（与 `evidence_level` 字段并列），并在 reasoner 提示词内禁止其单独支撑核心框架；
3. 在输入包附 `cowork_patch_apply_audit.md`，逐条对应本 cowork 报告的 patch_id；
4. **不得在输入包中包含本 cowork 报告中的任何"框架/口诀/总图"暗示**——本轮 cowork 输出全部仅为完善审查清单与 patch 建议，不含框架建议。

## 9. cowork E 自检

- 报告与 6 个 patch/risk CSV、1 个 reference_only review CSV、1 个 decision.md 之间口径一致（同一 question_id 在多文件中描述相互不矛盾）；
- patch_type 只使用规定枚举：`keep / add / delete / update / split / merge / downgrade / promote_if_source_verified / source_check_needed / no_action`；
- must_fix_before_reasoner 只使用 `yes / no / uncertain`；
- blocks_reasoner 只使用 `yes / no / uncertain`；
- 本轮 cowork 未生成任何框架文本、代码本、候选框架、口诀、总图——遵守用户指令。

---

最终结论行（供下游脚本抓取）：

```
COWORK_VERDICT: CONDITIONAL_PASS
HARD_BLOCKERS: 19_empty_ask_text + 8_material_full_leak + 2_material_as_answer + 1_module_miscoupling_CC0364 + 10_pending_locator_check + 8_stage_corrected_locator_audit
ALLOWS_DOUBLE_MODEL_INPUT_PACKET_BUILD: yes_if_patches_applied_and_temporary_downgrade_labels_added
NEW_MISSING_QUESTIONS_DISCOVERED: 0
REFERENCE_ONLY_INCORRECTLY_PROMOTED: 0
FORMAL_REQUIRING_DOWNGRADE_IF_SOURCE_NOT_RECOVERED: up_to_9
STAGE_DISTRICT_QNO_SUBQ_MISCLASSIFICATION: 1 (CC0364_2026_通州_期末_19_1 sub-module mismatch)
```
