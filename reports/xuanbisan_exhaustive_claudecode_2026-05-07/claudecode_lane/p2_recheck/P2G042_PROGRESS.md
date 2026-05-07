# P2G042_PROGRESS

> Source_id: `042_Desktop_2026模拟题_2026各区一模_2026丰台一模_试卷_试卷.pdf`
> Status: COMPLETED（NOT_FINAL；小规模 source_id 级 P2 复核子产物）

## 1. 输入

- `fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv`（筛选 priority=P2 + source_id=042 → 4 行：Q4/Q7/Q8/Q9，manifest 第 60-63 行）
- `fusion/p2_recheck_sources/P2_SOURCE_TEXT_INDEX.csv`（042 源条目 2 项：1 paper + 1 support）
- `fusion/p2_recheck_sources/042_*paper.txt`（241 字节，仅 10 条 ===== PAGE n ===== 占位符；OCR 失败）
- `fusion/p2_recheck_sources/042_*support__2026丰台一模细则.pptx.txt`（68 张幻灯片，仅 Q17/Q18/Q19/Q20 主观题阅卷细则与复练试题，无 Q1-Q15 客观题答案）
- `fusion/framework_first_fusion/FRAMEWORK_FIRST_FUSION_P1_PATCHED.md`（已含 Q4/Q7/Q8/Q9 完整识别但带'需 Codex 回源复核'前置标签）

## 2. 步骤

1. ✅ 读取 manifest，确认 source_id=042 下 P2 行恰为 4 行：Q4（选必三导论-综合思维）/Q7（充分条件假言推理）/Q8（充分条件假言推理-否定后件式）/Q9（联言判断）。
2. ✅ 读取 source_index，确认 042 源仅 paper + 1 份 support pptx，无其他 support 文件。
3. ✅ 读取 042_*paper.txt 全文，确认仅 10 条 `===== PAGE n =====` 占位符（OCR 失败，扫描件 PDF 未提取出字符）。
4. ✅ 读取 042_*support__2026丰台一模细则.pptx.txt 全部 68 张幻灯片，确认通篇仅覆盖 Q17（生态环境法典）/Q18（加减乘除经济+逻辑推理）/Q19（哲学+文化 AI 与当代国际政治）/Q20（民法典安全保障+综合）四道**主观题**的阅卷细则与复练试题；不出现 Q4 题干"凹曲屋面/最速降线"、Q7 题干"四诊法"、Q8 题干"北京志愿者标识"、Q9 题干"元宵节猜灯谜"；不出现 Q1-Q15 客观题答案表。
5. ✅ 读取 fusion P1 第479-483/487-491/856-860/972-976 行，确认四行已含完整识别正文但带'需 Codex 回源复核'前置标签——本轮源级复核**无法**去除四标签（042 号源不含 stem/options/answer key）。
6. ✅ 应用 P2 复核硬规则——'Verify stem/options and answer key before confirming choice-trap rows' + 'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no'——四行全部判 source_insufficient。
7. ✅ 写 P2G042_RECHECK_DECISIONS.csv（1 表头 + 4 数据行 source_insufficient，evidence_level=B-choice-signal × 4，全部 patch_needed=yes / can_enter_fusion=no）。
8. ✅ 写 P2G042_RECHECK_PATCHES.jsonl（4 行 JSON，每行含 patched_material_signal/patched_trigger_logic/patched_answer_sentence/source_evidence/notes；patched_material_signal 与 patched_trigger_logic 仅留卷面识别要素与触发框架性留底，patched_answer_sentence 全部明文标注'源不足'未输出确定性答案）。
9. ✅ 写 P2G042_SOURCE_EVIDENCE.md（含 042 paper.txt 逐字摘录 + support pptx 68 张幻灯片内容覆盖矩阵 + 四行 stem/options/answer 可验证性矩阵）。
10. ✅ 写 P2G042_RECHECK_ACCEPTANCE.md（NOT_FINAL，行数/表头/允许集/硬规则全部校验通过；CSV header/decision rows count/evidence_level/source_id 范围/文件位置/允许集/不捏造各项均通过）。
11. ✅ 写 本文件 P2G042_PROGRESS.md。

## 3. 决策摘要

| 行 | framework_node | manifest evidence_level | decision | patch_needed | can_enter_fusion |
|----|---------------|------------------------|----------|--------------|-----------------|
| Q-2026丰台一模-4 | 选必三导论-综合思维（②正解） | B-choice-signal | source_insufficient | yes | no |
| Q-2026丰台一模-7 | 推理-充分条件假言推理（B正解） | B-choice-signal | source_insufficient | yes | no |
| Q-2026丰台一模-8 | 推理-充分条件假言推理-否定后件式有效（②正解） | B-choice-signal | source_insufficient | yes | no |
| Q-2026丰台一模-9 | 判断-联言判断（D正解） | B-choice-signal | source_insufficient | yes | no |

manifest phase12 状态对比：
- 四行均标 phase12_action=covered_by_74_review_body / phase12_category=already_in_74。
- 本轮源级复核**未维持**该判断——答案表证据缺失，按 P2 复核硬规则四行不应继续保留在 74-row review-only expanded body 中。
- 建议后续 supervisor 综合裁定时把四行从 covered_by_74_review_body 修正为 blocked_keep_out / answer_missing，与本 source_insufficient 决策对齐。

## 4. 边界

- 不写 Word/PDF/delivery 任何文件；
- 不写 fusion/ 子目录任何文件；
- 不修改 fusion P1 PATCHED.md（仅在 patch jsonl 与 acceptance 中说明后续 fusion patch 应保留四处'需 Codex 回源复核'前置标签或降级为 source_insufficient）；
- evidence_level 维持 manifest 标定（B-choice-signal × 4），未捏造任何上调下调；
- patched_answer_sentence 全部明文标注'源不足'，未输出确定性答案；
- patched_material_signal 与 patched_trigger_logic 明确标注'基于 fusion P1 已落体识别正文，本轮源级未能在 042 号源内逐字核验'，未捏造任何题干、选项、答案、细则或源文件；
- 未引用本 source_id 之外的任何 P2 源文件。

## 5. 终态

P2G042 四行（Q4/Q7/Q8/Q9）全部 source_insufficient，全部 can_enter_fusion=no（不进入 fusion 学生体）。
fusion P1 第479-483/487-491/856-860/972-976 行四节的'需 Codex 回源复核'前置标签**未去除**——042 号源不含 stem/options/answer key，本轮源级复核无源端依据去除标签。
本 P2 source 级复核子产物 NOT_FINAL，需上层 supervisor 综合多 source 子产物后裁定终稿，并补充丰台教研中心 2026 一模官方答案后再行回填确定性答案。
