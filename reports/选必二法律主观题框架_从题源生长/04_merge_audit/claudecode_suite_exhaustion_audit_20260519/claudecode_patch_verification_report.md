# Claude Code B Patch Verification Report — 2026-05-19

`PATCH_VERIFICATION: PASS`

本轮只复核 Codex 在上一轮 `FINAL_JUDGMENT: FAIL` 之后生成的修正包是否把 hard-fix list 全部落实。
未做全量重抽，只对 9 项 hard fix、atom/suite/计数自洽性、链路完整性、OCR/source 风险做补丁层校验。

修正后语料包：`04_merge_audit/suite_exhaustive_claudecode_corrected_20260519/`
修正后 reasoner packet：`05_reasoner_packets/suite_exhaustive_claudecode_corrected_20260519/`

---

## 一句话结论

- core_count: **65**（formal 61, reference_only 4）
- formal_count: **61**
- reference_only_count: **4**
- still_missing_core_candidates: **0**
- still_false_positive_core_ids: **0**
- still_stage_mismatch_ids: **0**
- remaining_blockers_before_reasoner: **0**（剩余 OCR/source 项已降级为可见风险，不阻断 reasoner 包交付）
- 修正包可否交给 GPT-5.5 Pro / Claude Opus 做开放观察：**可以**

---

## 1. 9 项 hard fix 落实情况

| # | hard fix | 期望 | 实际 | 结果 |
|---|---|---|---|---|
| 1 | 漏题 2026 朝阳期末 Q18(1) 补回核心 | 新增 `RECOVER_2026_朝阳_期末_18_1` formal, 期末 | jsonl/csv 均含该 row：evidence_level=formal, evidence_type=marking_rubric, ask_text="结合上述案例，运用《法律与生活》知识，说明法院判决的依据。（7分）", source_locator=F0213/F0392 page_005 + F0212/F0393 page_002 | PASS |
| 2 | `CC0051_2024_海淀_期中_21_1` 从核心移出并转 boundary | 不在核心 jsonl，进入 boundary 表 | 65 行 core 不含该 id；`boundary_mixed_or_blocked_cases_claudecode_corrected.csv` 有 `CC0051_2024_海淀_期中_21_1_DOWNGRADED_TO_BOUNDARY`；`removed_from_core_after_claudecode_audit.csv` 记录 `downgraded_to_boundary_by_claudecode_audit_same_as_2025_haidian_midterm` | PASS |
| 3 | `RECOVER_2024_顺义_二模_17` 从核心移出并转 boundary | 同上 | core 不含该 id；boundary 表有 `RECOVER_2024_顺义_二模_17_DOWNGRADED_TO_BOUNDARY`；removed 表 reason=`downgraded_to_boundary_by_claudecode_audit_economy_society_main_axis` | PASS |
| 4 | `CC0311_2026_海淀_二模_18` 拆分，仅 18_2 入核心 | core 仅含 `CC0311_2026_海淀_二模_18_2`，逻辑小问不在核心 | core 不含 `CC0311_2026_海淀_二模_18`，含 `CC0311_2026_海淀_二模_18_2`（sub=2, ask 明示《法律与生活》）；boundary 表有 `UNCERTAIN_2026_朝阳_期末_18_2_LOGIC`，并在 reasoner packet 同步；suite matrix 该套 core_count=1 | PASS |
| 5 | 7 个错误标为期中的 2026 期末 row 改为期末 | exam_stage 改 `期末`，question_id 与 suite 同步 | 7 个 id 全部由 `_期中_` 改为 `_期末_`：CC0244/CC0245 东城；CC0317/CC0318/CC0319 海淀；CC0353 西城；CC0364 通州；exam_stage 字段全为 `期末`；旧 _期中_ id 在 core/atom 三表均已消失 | PASS |
| 6 | suite 矩阵拆出 2026 朝阳期末、2026 海淀期末，且真期中不再被期末题污染 | 朝阳期末/海淀期末为独立行；朝阳期中/海淀期中为 no_law_subjective_confirmed | matrix 65 行齐：`2026 朝阳 期末`=has_suite_exhaustive_core_rows_after_claudecode_recovery，core=RECOVER_2026_朝阳_期末_18_1；`2026 海淀 期末`=has_suite_exhaustive_core_rows_after_stage_correction，core=CC0317/CC0318/CC0319；`2026 朝阳 期中`、`2026 海淀 期中` 均 no_law_subjective_confirmed，core_count=0 | PASS |
| 7 | 修正后核心题数 / evidence_level 统计自洽 | 65 = formal 61 + reference_only 4 | jsonl 计数：65; formal 61, reference_only 4（CC0040 / CC0162 / CC0311_18_2 / CC0353_17）；和 counts.json 与 suite matrix 65 套合计 core_question_count=65 一致 | PASS |
| 8 | material/ask/rubric atom 不再指向被删除核心题 question_id | 三表的 question_id 必须是 65 核心 id 集合的子集 | 65 核心 id 集合下：ask atoms 65 行 / 65 唯一 qid / 0 broken；material atoms 541 行 / 65 唯一 qid / 0 broken；rubric atoms 362 行 / 65 唯一 qid / 0 broken；旧 `_期中_` / `CC0051` / `RECOVER_2024_顺义_二模_17` / `CC0311_..._18`(无 sub) 全部不再出现 | PASS |
| 9 | rubric atoms 的 `related_material_atom_ids` 无明显断链 | 反向引用的 material_atom_id 全部存在 | 用 `|;,` 分隔解析；867 条 rubric→material 引用，broken=0；material atom id 池 541 全可被引用到（保留 `[空]` 行不计） | PASS |

每项 hard fix 在核心 jsonl/csv、atom 三表、boundary 表、suite matrix、reasoner packet 五个表面全部一致落地。

---

## 2. 自洽性与链路

- core jsonl 行数 65，counts.json 一致，suite matrix `core_question_count` 求和=65。
- atom 三表的 question_id 集合 = 核心 id 集合（双向 0 漏 0 多）。
- rubric→material 反向引用 867 条全部可解析，0 断链。
- 9 个被重命名/新增/拆分/补回的 id 在 ask（1 行/题）、material（3–16 原子/题）、rubric（1–8 原子/题）三表均有完整原子记录，未见空挂。
- reasoner packet 与 04_merge_audit 修正包内容一致：core 65, RECOVER_2026_朝阳_期末_18_1 / CC0311_..._18_2 / 7 个 _期末_ 重命名均已镜像。
- suite matrix 状态计数：has_core(原口径) 51 + has_core_after_stage_correction 4 + has_core_after_claudecode_recovery 1 + no_law_subjective_confirmed 3 + midterm_boundary_no_core 1 + boundary_not_core 1 + midterm_mixed_law_reference 1 + mixed_boundary_only_after_stage_correction 1 + not_independent_stage_mapping_conflict 1 + special_user_excluded 1 = 65。

---

## 3. 剩余 OCR / source 风险（保留为风险，不阻断 reasoner 提交）

下列项在 `claudecode_source_or_ocr_blockers.csv` 已登记，全部在修正包的 notes / boundary 表保留可见，且**不阻断**把修正包交给 GPT-5.5 Pro / Claude Opus 做"开放观察"，因为核心题面/细则证据已通过 rendered_pages 或 docx 替代源恢复：

| 风险项 | 当前状态 | 风险性质 |
|---|---|---|
| 2026 朝阳期末 F0212/F0213/F0392/F0393 paper/rubric OCR 失败 | RECOVER_2026_朝阳_期末_18_1 已基于 rendered page_002（细则）+ page_005-006（题面）入核心，标 formal | 仅 paper_text 字段尚未机读全文，建议日后补 Vision OCR；不影响核心入库 |
| 2026 丰台期末 F0208/F0387 paper OCR 失败 | Q18 仍为 mixed boundary（含必修3 政治与法治+法律与生活），未入核心 | 后续若 OCR 出题面可决定是否拆出仅法律与生活子问；当前不影响 65 核心 |
| 2026 西城期末 F0219/F0400 细则 OCR 失败 | CC0353_2026_西城_期末_17 当前 evidence_level=reference_only | 若 OCR 出正式 marking_rubric 可升 formal；当前 reference_only 入库合规 |
| 2026 海淀期中 F0214/F0395 讲评 OCR 失败 | 已确认期中无法律与生活主观题；matrix=no_law_subjective_confirmed | 优先级低，不阻断 |
| 2026 石景山期末 F0225/F0226/F0398 | 用户 hard-rule 暂不入；matrix=special_user_excluded_or_source_blocked | 等待用户显式提供新试卷+评标；与本批补丁无关 |
| 多个 2024/2025 OCR_blocked PDF（东城/丰台/海淀/朝阳等） | 全部已通过 docx/ppt/同卷副本恢复入核心 | 仅 metadata 完整性问题，不阻断 |

无 hard blocker。所有 OCR/source 风险均保留为下游审计可见项。

---

## 4. 是否可把修正包交给 GPT-5.5 Pro / Claude Opus 做开放观察

**可以。**

- 9 项 hard fix 全部落实；
- 核心 65 题 + 541 material atoms + 65 ask atoms + 362 rubric atoms 完全自洽；
- 0 atom 断链、0 stage 错挂、0 false positive、0 已知漏题；
- reasoner packet 已镜像至 `05_reasoner_packets/suite_exhaustive_claudecode_corrected_20260519/`；
- 剩余 OCR 项均为质量提升项，不影响 65 核心证据等级与归纳，应在下游 GPT-5.5 Pro / Claude Opus 输出中以"风险注脚"形式保留，不需要在送入观察前再做修复。

下一步：以本修正包为唯一输入，重做 GPT-5.5 Pro 与 Claude Opus 的开放观察；旧 53/56/66 行包的开放观察输出全部作废。

---

## 5. 与上一轮 FINAL_JUDGMENT: FAIL 的关闭项对照

| 上一轮列出的 hard fix | 关闭凭证 |
|---|---|
| 补回 2026 朝阳期末 Q18(1) | core jsonl 新增 RECOVER_2026_朝阳_期末_18_1 (formal/期末) |
| 降级 CC0051 2024 海淀期中 Q21(1) | core 移除 + boundary 表登记 + suite matrix `midterm_boundary_no_core_after_claudecode_audit` |
| 降级 RECOVER_2024_顺义_二模_17 | core 移除 + boundary 表登记 + suite matrix `boundary_not_core_after_claudecode_audit` |
| 拆分 CC0311 2026 海淀二模 Q18 | core 仅 18_2；18_1 逻辑小问移到 boundary；material/rubric 限定 18_2 |
| 修正 7 处 stage_mismatch | 7 id 全部由 _期中_ → _期末_，exam_stage 字段、原子表、suite matrix 同步 |
| 拆出 2026 朝阳期末、2026 海淀期末独立 suite | matrix 已拆，并把 2026 朝阳期中 / 海淀期中标 no_law_subjective_confirmed |
| 保留并降级 OCR/source blockers 可见 | `claudecode_source_or_ocr_blockers.csv` + 修正包 notes / boundary 表全部保留 |

所有上一轮 FAIL 项已关闭。
