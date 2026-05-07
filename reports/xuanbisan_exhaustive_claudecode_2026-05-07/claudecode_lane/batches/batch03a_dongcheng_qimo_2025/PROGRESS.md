# Batch03a S-2025东城期末 单套闭合 PROGRESS

## 启动 — 2026-05-07

任务边界：本批仅修复 Batch03 东城整批 `自称完成但无正式输出` 的失败现场。
只处理 `S-2025东城期末` 一套，`_dongcheng_candidates.csv` 中该套共 54 行候选，
unique question_id 闭合到 24 个。每个候选必须落入 `入正文 / 同类索引 / blocked / excluded`。
不写终稿，不写 PASS，不生成 Word/PDF。

## 控制源已读

- `feige-politics-garden/SKILL.md`：四线分工与套卷闭环监督。
- `feige-politics-garden-xuanbisan/SKILL.md`：选必三流程、Trial Before Full Run 硬样本（含 `2026东城期末 Q17(2)` 形式逻辑边界硬样本，但本批是 2025 套卷不涉及）。
- `feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`：
  - 一、二、四：模块边界 / 学生版与审计版分离；
  - 八：选择题硬规则（题面+选项+可靠答案）；
  - 二十一：框架版结构硬规则（思维类型 → 三性/三新/小方法 → 配题）；
  - 二十二：ClaudeCode 厚内容优先；
  - 二十三：套卷闭环监督。
- 本 run 小本本 `00_飞哥选必三逻辑与思维硬性要求记事本.md`：穷尽口径、528 行控制基底、73 行思维信号矩阵、无 PASS。
- `batch03_dongcheng/PROGRESS.md`：东城整批进度，已确认 S-2025东城期末 候选 54 行 → 24 unique question_id；入正文 5（Q5/Q13/Q14/Q15/Q18-2）+ 同类索引 1（Q21）+ excluded 18，blocked 0。
- `batch03_dongcheng/QUESTION_DECISIONS.csv`：已含本套 24 行裁决，本批以同口径独立产出正式产物。

## 套卷源已读

| 文件 | 内容 | 状态 |
|---|---|---|
| `2025各区模拟题/2025各区期末/2025东城期末/试卷/2025北京东城高三（上）期末政治（教师版）.pdf`（20 页） | 试卷+参考答案+点评 | OK：选择题答案 1.D 2.D 3.B 4.A 5.C 6.C 7.B 8.B 9.A 10.C 11.C 12.A 13.B 14.D 15.B；主观题参考答案完整。 |
| `2025各区模拟题/2025各区期末/2025东城期末/细则/2025东城期末细则.pptx`（34 张 slide） | 阅卷细则 | OK：Slide3-Slide4 Q18(2) 创新思维两层细则；Slide8 Q17 法治三层；Slide11-15 Q19(1-3) 法律与生活/政治与法治；Slide16/21 Q16 哲学与文化三层；Slide23-26 Q20 国际政治与经济三层；Slide27-29 Q21 综合短文等级细则。 |
| `2025各区模拟题/2025各区期末/2025东城期末/其他材料/2025。1东城讲评 修改.pdf` | 讲评 PDF | 备查（本批未独立摘录）。 |

无 suite-level OCR blocker。无视觉缺失。无答案冲突。

## 套卷推进时序

1. ✓ 读 `_dongcheng_candidates.csv` 抽出本套 54 行候选 → unique question_id 24（Q1-Q15 选择题 + Q16/Q17/Q18(1)/Q18(2)/Q19(1)/Q19(2)/Q19(3)/Q20/Q21）。
2. ✓ 读教师版 PDF（pymupdf 提取 20 页全文）+ 细则 PPTX（zipfile + ElementTree 抽 34 张 slide 文本）。
3. ✓ 用 `csv.DictWriter` 结构化写入 `QUESTION_DECISIONS.csv`（24 行）+ `MAIN_THINKING_LEDGER.csv`（1 行 Q18(2) 创新思维主观题）+ `CHOICE_TRAP_LEDGER.csv`（4 行 Q5/Q13/Q14/Q15 选择题）+ `FRAMEWORK_NODE_MATRIX.csv`（20 节点挂载）+ `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`（按节点聚合）。
4. ✓ 写 `BLOCKED_OR_BOUNDARY.md`：blocker 0，同类索引 1（Q21），excluded 18 按模块边界归类。
5. ✓ 写 `suite_reports/S-2025东城期末.md`：套卷源 + 候选闭合统计 + 入正文条目（含完整设问/细则位置/材料动作/触发逻辑/答案句）+ 同类索引 + 外推与硬样本结论 + 残余边界。
6. ✓ 写 `entries/batch03a_entries.jsonl`：5 行（Q18-2 main + Q5/Q13/Q14/Q15 choice），每行含 question_id/type/framework_node/material_signal/trigger_logic/answer_sentence/evidence_level/needs_codex_recheck/source_batch 九字段。
7. ⧗ 跑 `codex_audit/audit_batch_dir.py` 自检（结构完整即 BATCH_QA_STRUCTURALLY_OK_NOT_FINAL，PASS 不归本批）。

## 入正文条目摘要

- `Q-2025东城期末-18-2`（创新思维·登月服设计·4分）：A-formal。
  - 第一层细则 1 分：思路新方法新结果新（多向性/跨越性/独特性）。
  - 第二层细则 3 分：聚合+发散（聚焦核心问题综合考虑不同需要）/ 联想（造型与火箭形象传统文化）/ 超前（提前预判月面环境与航天员需求），写对一点 2 分、二点 3 分。
- `Q-2025东城期末-5`（辩证思维·社区道路改造·选 C(②④)）：B-choice-signal。整体性+动态性 + 矛盾分析法；①必修四自在联系陷阱、③必修四辩证否定观陷阱。
- `Q-2025东城期末-13`（推理·三段论·选 B(①③)）：B-choice-signal。①③共同犯中项不周延；②大项不当扩大；④四概念错误。
- `Q-2025东城期末-14`（判断·性质判断/关系判断·选 D）：B-choice-signal。简单肯定性质判断谓项不周延；A整体部分vs属种、B反对称vs传递、C外延一致性。
- `Q-2025东城期末-15`（推理·充分条件假言推理·选 B）：B-choice-signal。肯前+否后必假；A必要条件方向、C否前禁推、D肯后禁推。

## 同类索引

- `Q-2025东城期末-21`（中国式现代化民生为大综合短文·10分）：综合运用所学，细则按知识运用方面数等级给分；不限选必三知识范围，作为综合短文同类索引保留。

## 监督备忘

- 学生候选条目（`MAIN_THINKING_LEDGER.csv` / `CHOICE_TRAP_LEDGER.csv` / `entries/*.jsonl` / `suite_reports/*.md`）正文不含
  `评标 / 参考答案 / 答案写 / 可从…角度作答 / yes / pass / filled / correct_option_chain / A-formal / B-choice-signal / phase / phase05 / source_pool / question_id / file id / line id / OCR / debug / /Users/... / C:\\...` 等审计或后台话术，且不含字串 `固定分析流程`。
- 审计字段（证据等级、套卷归属、是否 codex 复查）只出现在 csv/jsonl 元数据列。
- `needs_codex_recheck` 列只取 `yes / no` 二值。
- 本批不生成 Word/PDF，不写 PASS、final、终稿、宝典成品；仅作为可融合的 thick body + 闭环裁决。
