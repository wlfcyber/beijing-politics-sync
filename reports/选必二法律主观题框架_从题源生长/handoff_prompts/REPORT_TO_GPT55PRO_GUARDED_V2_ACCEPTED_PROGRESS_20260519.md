# 给 GPT-5.5 Pro 的进度同步：选必二法律主观题框架 guarded v2 已完成清洗与 QA

你之前对 guarded v2 的审查结论是 `YES_WITH_GUARDS`。Codex A 已按你的 P0 意见完成本地证据清洗和再生成，现在同步当前状态，请你继续作为 GPT-5.5 Pro 审查者，只做进度核验与下一步建议，不要重写总框架。

## 当前状态

- corpus: 65 道主观题
- questions evidence: 61 formal, 4 reference_only, 0 missing
- material atoms: 482
- ask atoms: 65
- rubric/answer atoms: 377（含 7 个 patch scoring atoms）
- pressure: PASS 45 = 43 core + 2 boundary-gate, PARTIAL 20, FAIL 0
- baodian labels: 43 core_full_score_supported, 14 formal_open_container_partial, 4 reference_only_demo, 2 boundary_non_core, 2 open_container_only

## 已按你意见修补

1. `CC0077`, `CC0084`：只保留 scoring atoms 进入满分句，学生问题/教学启示移出核心答案列。
2. `CC0150`：删除第21题《当代国际政治与经济》内容，只保留第20题法律与生活 scoring chain。
3. `CC0245`：拆成维权途径、证据准备、合理诉求三个 patch scoring atoms；R02-R04 只作风险/易错。
4. `CC0251`：拆成裁判锚句、公共场所规则、事实无过错、价值边界四个 patch scoring atoms；R02-R16 不进答案列。
5. `CC0143`：`expansion_status` 修成 `CORE_CODEBOOK_SUPPORT_AFTER_CC0143_PATCH`。
6. `CODE_COWORK_007`：framework 层拆成 007A 法律边界识别与合规措施、007B 维权准备与诉讼请求、007C 调解方案与合同诚信理由、007D 公益诉讼与司法确认。
7. `CC0380`：保持 `OPEN_CONTAINER_ONLY`，不支撑核心节点。
8. 非核心行在宝典中改为题内参考句 / reference_only 参考句 / 边界说明，不再混叫满分句。
9. 答案列污染词扫描：`当代国际政治`, `学生问题`, `建议`, `复练试题`, `反复训练`, `继续短周期`, `教学启示` 命中 0。
10. DOCX 经 Microsoft Word 导出 PDF；PyMuPDF 渲染 114 页，空白页检测 0。

## 关键产物

- `FINAL_ACCEPTANCE_REPORT_GUARDED_V2.md`
- `FINAL_DELIVERY_REPORT_GUARDED_V2.md`
- `12_final_baodian/DOCX_QA_GUARDED_V2.md`
- `10_framework_validation/gptpro_guarded_v2_cleanup_20260519/gptpro_guarded_v2_cleanup_report.md`
- `10_framework_validation/framework_v1_2_question_by_question_test_20260519.csv`
- `12_final_baodian/question_by_question_framework_runs.csv`
- `12_final_baodian/full_score_sentence_bank.csv`
- `09_candidate_frameworks/framework_v1_2_evidence_map.csv`

## 请你核验

请只回答以下问题：

1. 以上 guarded v2 是否可以被称为“当前可交付的 guarded core teaching version”？
2. 是否仍有必须在交付前修的 P0 证据污染或过度宣称问题？
3. 如果进入下一轮，不是重做框架，而是应该优先做哪三件增量工作？
4. 请不要输出新的总框架；若你提出修改，必须点名文件、question_id、rubric_atom_id 或明确标签。
