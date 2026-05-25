# ClaudeCode B 生产线任务：5.2 母版原地补题 + 2024-2026 一模穷尽审计

你是飞哥政治庄园本轮必修四哲学宝典生产线 B，不是 reviewer。Codex 会并行跑 A 线；你必须独立从源材料和母版出发，产出可融合的厚内容候选和覆盖审计。

## 最高要求

- 用户认可的是 5.2 哲学宝典母版。你不能重做结构，不能另起“2026二模专题”。新增题必须按原宝典哲学原理/方法论节点原地插入。
- 本轮只做到审核/融合前，不生成最终 Word/PDF。
- 同时完成两件事：
  1. 2026 二模新增哲学题的节点插入候选。
  2. 2024-2026 一模哲学题是否已被母版穷尽覆盖的清单审计。
- Codex 和 ClaudeCode 是双生产线。你要自己跑源材料，不要只评价 Codex。

## 必读文件

- `skills/feige-politics-garden-bixiu4/references/baodian-hard-rules-notebook.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/00_control/MASTER_REQUIREMENTS.md`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/source_suite_inventory.csv`
- `reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/base_coverage_by_suite.csv`
- 本轮专用源文本包：`reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/01_source_inventory/suite_source_bundles/`
- Codex A 初审只能作为对照，不能替代你的生产线：`reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/02_codex_lane/`
- 母版：`reports/bixiu4_philosophy_accepted_base_second_mock_patch_2026-05-23/accepted_base/accepted_base_哲学宝典最终版-飞哥正志讲堂.docx`
- 可定位但不可直接当证据的旧二模候选：`reports/bixiu4_philosophy_accepted_base_second_mock_patch_2026-05-23/04_fusion/fused_entries_2026_second_mock.json`

## 源材料范围

- `C:\Users\Administrator\Desktop\2024各区模拟题`
- `C:\Users\Administrator\Desktop\2025各区模拟题`
- `C:\Users\Administrator\Desktop\2026各区模拟题`
- 先用缓存：`C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`
- 缓存不够时必须回原 Word/PDF/PPT/图片，不得因为格式麻烦而跳过。

## 输出到固定目录

请只写入：

`reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/03_claudecode_lane/`

必须产出：

1. `claudecode_b_coverage_matrix.csv`
   - columns: suite,year,phase,question_no,module_judgment,evidence_level,base_status,proposed_framework_node,decision,note
2. `claudecode_b_second_mock_insert_candidates.jsonl`
   - 每行一题一节点。字段至少包括 source_suite, question_no, framework_node, material_trigger, question_prompt, why_trigger, answer_landing, evidence_level, boundary_note。
3. `claudecode_b_first_mock_omissions.md`
   - 按套卷列出：母版已覆盖、疑似遗漏、非哲学/边界排除、缺证据。
4. `claudecode_b_patch_targets.md`
   - 特别检查：主要矛盾和次要矛盾、矛盾的主要方面和次要方面、两点论与重点论/主流支流是否漏收或放错。
5. `claudecode_b_audit_report.md`
   - 简短说明总数、已确认候选、需回源核验、与母版冲突、不能进入融合的项。

## 质量线

- 每条主观题候选必须有：材料触发点、完整设问、为什么能想到、答案落点。
- 一题多原理必须拆多行进入不同节点。
- 不能用“等角度”兜底新增原理。
- 不能把普通参考答案写成评分细则。
- 如果发现旧二模候选薄、短、像模板，要重写成与原宝典同强度的厚内容候选。
- 如果源文件缺题干/选项/答案/细则，明确 blocked，不要猜。

## 当前已知风险，必须主动处理

- 2026 二模没有历史缓存套卷包，本轮已经抽取到专用文本包；不能只沿用旧 52 条候选。
- 2026 西城二模评标 PDF 文本抽取为 0，2026 顺义二模试卷 PDF 文本抽取为 0。你若无法 OCR/视觉读取，必须在 blocker 中写明边界，并优先利用同套题教师版/评标 doc 的可读内容。
- 母版覆盖判断必须用“年份+区+一模/二模+题号”精确匹配，禁止用“丰台二模”误命中“2025丰台二模”来冒充“2026丰台二模已覆盖”。
