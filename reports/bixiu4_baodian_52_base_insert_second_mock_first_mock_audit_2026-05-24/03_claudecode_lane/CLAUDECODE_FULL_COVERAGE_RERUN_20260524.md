# ClaudeCode B 独立生产线：2026 二模新题 + 2024-2026 一模覆盖倒查

你是飞哥政治庄园本轮必修四哲学宝典生产线 B。你不是 Codex 的审核员，也不是只做评论的 reviewer；你要独立从源材料和 5.2 母版出发，跑到“融合审核前”的可验收产物。

## 工作边界

- 仓库：`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`
- 本轮目录：`reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24`
- 只写入：`reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\03_claudecode_lane\`
- 不生成最终 Word/PDF。
- 不修改用户原始宝典。
- 不回滚别人正在做的改动。

## 必读材料

1. `skills\feige-politics-garden-bixiu4\references\baodian-hard-rules-notebook.md`
2. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\00_control\MASTER_REQUIREMENTS.md`
3. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\source_suite_inventory.csv`
4. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\base_coverage_by_suite.csv`
5. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\01_source_inventory\suite_source_bundles\*.md`
6. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\student_patch_entries.accepted.jsonl`
7. `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\docx_insert_ledger.csv`
8. 已知二模回源证据：
   - `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\99_logs\weak_gate_sources\26顺义二模评标.txt`
   - `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\99_logs\weak_gate_sources\石景山区高三政治第二次模拟考试答案评分细则(1).txt`
   - `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\99_logs\weak_gate_sources\renders\xicheng_rubric\page_001.png`
   - `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\99_logs\weak_gate_sources\renders\xicheng_rubric\page_002.png`
   - `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\99_logs\weak_gate_sources\renders\xicheng_rubric\page_003.png`
   - `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\99_logs\weak_gate_sources\renders\haidian_lecture\page_015.png`
   - `reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\99_logs\weak_gate_sources\renders\haidian_lecture\page_016.png`

## 你要同时完成两件事

### A. 2026 二模新题补强复跑

检查二模新增条目是否“像原宝典一样厚”：

- 材料触发点必须是材料中的真实动作、关系、矛盾、过程或主体。
- 设问必须保留真实任务句。
- “为什么能想到”必须解释学生如何从材料想到该原理，不能只说“细则提到”。
- 答案落点必须是学生可写入卷面的自然句子。
- 一题多原理必须拆成多行，不得把多个答题点塞进一个框架节点。

重点核验：

- 2026海淀二模 Q16：联系、矛盾对立统一、实践认识、认识反作用等是否证据足、表述厚。
- 2026西城二模 Q16：矛盾普遍性与特殊性、实践、价值观是否来自评标 PDF，而不是泛化。
- 2026顺义二模 Q16：人民群众、价值观、两点论重点论、实践、辩证否定/守正创新是否分别落到材料。
- 2026石景山二模 Q17(3)：联系、矛盾、实践认识只能标“正式细则允许角度”，不要写成逐点累计细则。

### B. 2024-2026 一模覆盖倒查

逐套检查一模哲学主观题是否在母版或本轮 accepted JSONL 中有去向。每套必须落入以下一种状态：

- `covered_in_base`：原宝典已经覆盖，题号和原理能精确对应。
- `covered_by_patch`：本轮 accepted JSONL 已补入。
- `should_add`：有正式评分/评标/讲评证据，应该新增。
- `boundary_excluded`：不是必修四哲学，或属于文化/选必/非本模块。
- `need_evidence`：题干、答案或评分来源不足，不能编。

特别查这些高风险节点是否漏收或放错：

- 主要矛盾和次要矛盾
- 矛盾主次方面 / 主流支流
- 两点论与重点论
- 辩证否定 / 守正创新
- 量变质变 / 适度原则
- 实践是认识的基础
- 认识对实践的反作用
- 价值观导向作用
- 人民群众
- 系统优化

## 输出文件

只写入下面三个文件：

1. `claudecode_b_full_coverage_rerun_20260524.csv`
   - columns: `suite,year,phase,question_no,status,existing_coverage,proposed_framework_node,evidence_level,action,reason`
2. `claudecode_b_full_coverage_rerun_20260524.md`
   - 总结总套数、已覆盖、应新增、阻塞、排除。
   - 分“2026二模新增条目厚度复核”和“2024-2026一模漏项倒查”两部分。
3. `claudecode_b_full_coverage_insert_candidates_20260524.jsonl`
   - 只写你认为应新增或应重写的条目。
   - 每行字段：`source_suite, question_no, framework_node, material_trigger, question_prompt, why_trigger, answer_landing, evidence_level, boundary_note`

## 严格规则

- 不要用“等角度”兜底新增原理。
- 普通参考答案不能写成评分细则。
- 若源材料只能支持“可以从某角度回答”，必须在 `boundary_note` 中写明证据级别，不能包装成稳定评分触发。
- 发现条目薄、空、逻辑断裂，标 `REWRITE`；发现原理错位，标 `DELETE`。
- 如果你无法核验原文，标 `need_evidence`，不要猜。
- 结尾必须明确一句：`ClaudeCode B 本轮已到融合审核前，不代表最终 PASS。`
