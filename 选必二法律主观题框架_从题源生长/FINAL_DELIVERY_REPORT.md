# FINAL DELIVERY REPORT

生成时间：2026-05-19T13:58:00+08:00

## 交付状态

> 2026-05-19T14:45:00+08:00 边界恢复修正：本报告中“最终宝典完成”的状态降级为 `provisional_boundary_patch_required`。GPT-5.5 Pro 边界恢复复核确认 `CC0094`、`CC0229`、`CC0250`、`CC0373` 等条目需要拆分/删除/atom 修复；其中 `CC0229` rubric atoms 已用 F0153/F0146 修复，但最终宝典相关段落尚未重生成。当前控制口径见 `10_framework_validation/framework_v2_boundary_recovery_delta_after_gpt.csv` 和 `12_final_baodian/选必二法律主观题满分宝典_BOUNDARY_CORRECTION_ADDENDUM.md`。

- Source manifest：完成，403 个源文件，51 个失败/OCR-gap 记录。
- Codex A 抽取：完成。
- ClaudeCode B 独立抽取与审计：完成，CONDITIONAL_PASS。
- 合并审计与 missing17 修正：完成，最终 merged candidates 70，formal 65，reference_only 5，missing 0。
- GPT-5.5 Pro 开放观察：完成并捕获。
- Claude Opus 4.7 Adaptive 开放观察：完成并捕获。
- 双模型交叉验证：完成，51 条 comparison，17 条 strong shared。
- 临时代码本：完成，10 个 provisional code。
- 双模型候选框架：完成并捕获。
- framework_v1：完成。
- v1 全题压测：完成，PASS 37，PARTIAL 13，FAIL 20。
- framework_v2：provisional，已追加边界恢复校正。
- 最终宝典：provisional draft，Markdown + DOCX + CSV 附件存在，但课堂发放前必须完成边界补丁队列。

## 关键产物

- `11_final_framework/framework_v2.md`
- `11_final_framework/framework_v2_student_one_page.md`
- `11_final_framework/framework_v2_teacher_guide.md`
- `12_final_baodian/选必二法律主观题满分宝典.md`
- `12_final_baodian/选必二法律主观题满分宝典.docx`
- `12_final_baodian/选必二法律主观题满分宝典_BOUNDARY_PATCHED.docx`
- `12_final_baodian/DOCX_QA_BOUNDARY_PATCHED.md`
- `12_final_baodian/question_by_question_framework_runs.csv`
- `12_final_baodian/full_score_sentence_bank.csv`
- `12_final_baodian/common_failure_paths.md`
- `12_final_baodian/material_trigger_bank.csv`

## 审慎结论

最终框架不把 70 道合并候选全部强行认定为法律主观题正文样本。v1 压测后原采用：

- 37 道 PASS：主干正文示范。
- 13 道 PARTIAL：开放容器/弱证据示范。
- 20 道 FAIL：边界复核，不进入法律正文。

边界恢复后改用分层口径：

- 当前严格闭合核心：48 道。
- 当前核心 + 开放/弱示范容器：53 道。
- `CC0229_2026_东城_一模_18` rubric atoms 已修复，最终宝典对应段落已重生成。
- 待拆分/重抽/补证题不计入闭合题量。

## DOCX QA

DOCX 已通过结构校验：可由 python-docx 打开，压缩包完整无损。由于本机没有 `soffice`，无法完成 LibreOffice PNG 渲染视觉 QA；建议在 Word/WPS 中打开抽查页面后再课堂发放。

边界补丁版 DOCX 已生成：`12_final_baodian/选必二法律主观题满分宝典_BOUNDARY_PATCHED.docx`。它包含本轮 CC0094/CC0229/CC0250/CC0305/CC0373/CC0380 的 Markdown 修正，但仍需 Word/WPS 视觉抽查和 canonical CSV sidecar 再生。

Sidecar 补丁已同步到 `question_by_question_framework_runs.csv`、`material_trigger_bank.csv`、`common_failure_paths.md`。`full_score_sentence_bank.csv` 本轮未发现这些边界题的旧满分句命中，但最终 release 前仍建议统一重导。

## 2026-05-19T14:05:00+08:00 Canonical Patch Update

已生成边界修复后的 canonical corpus：

- `04_merge_audit/boundary_patched_20260519/merged_subjective_law_questions_boundary_patched.csv`
- `04_merge_audit/boundary_patched_20260519/merged_material_atoms_subjective_boundary_patched.csv`
- `04_merge_audit/boundary_patched_20260519/merged_ask_atoms_subjective_boundary_patched.csv`
- `04_merge_audit/boundary_patched_20260519/merged_rubric_atoms_subjective_boundary_patched.csv`
- `04_merge_audit/boundary_patched_20260519/boundary_patch_status_ledger.csv`
- `04_merge_audit/boundary_patched_20260519/canonical_integration_report.md`
- `04_merge_audit/boundary_patched_canonical_corpus_20260519.zip`

patched corpus 当前为 53 道框架可用题，含 3 道拆分恢复题；20 个原始 ID 被剔除、父题不计或待核移出。`CC0229` 的 question-level `answer_text/rubric_text` 已同步清理为 F0153/F0146 的 8 条法律细则原子，patched corpus 中不再残留“逃逸粒子/创新资源集聚/空间布局精准/全链条产业生态”等串页文本。

仍未给出最终课堂 PASS：`full_score_sentence_bank.csv` 尚未按 patched corpus 全量重导，Word/WPS 视觉 QA 仍未完成。

## 2026-05-19T14:10:00+08:00 Sidecar Regeneration Update

已按 53 行 boundary-patched corpus 重导：

- `12_final_baodian/question_by_question_framework_runs_boundary_patched.csv`
- `12_final_baodian/material_trigger_bank_boundary_patched.csv`
- `12_final_baodian/full_score_sentence_bank.csv`
- `12_final_baodian/full_score_sentence_bank_boundary_patched.csv`
- `12_final_baodian/SIDECARE_REGENERATION_REPORT_BOUNDARY_PATCHED.md`

三张 53 行 sidecar 现在统一为：37 个 `PASS`，11 个 `PASS_RECOVERED`，5 个 `OPEN_OR_REFERENCE`。原 70 行追踪表仍保留，用于审计被剔除、父题不计和待核题。

当前剩余阻塞只剩文档视觉验收：本机缺少 `soffice`，还不能给出 Word/WPS 视觉 PASS。

## 2026-05-19T14:15:00+08:00 Word/PDF QA Update

已完成 Microsoft Word 实机打开、保存与 PDF 导出：

- Canonical DOCX 已替换为 Word 保存后的边界修复版：`12_final_baodian/选必二法律主观题满分宝典.docx`
- 旧 canonical DOCX 已备份：`12_final_baodian/选必二法律主观题满分宝典.pre_boundary_patch_20260519.docx`
- Word 导出 PDF：`12_final_baodian/选必二法律主观题满分宝典_BOUNDARY_PATCHED_WORDSAVED.pdf`
- QA 报告：`12_final_baodian/DOCX_QA_WORD_PDF_RENDER.md`

PDF 共 198 页，已全部渲染为 PNG；疑似空白页 0。抽查 page 1 contact sheet、page 100、page 198，未见明显重叠、裁切或空白异常。

当前可称为 `boundary_patched_release_candidate`：证据语料、sidecar、DOCX 已对齐到 53 行 patched corpus。仍需注意：`CC0094`、`CC0259`、`CC0118` 保持 pending/excluded ledger，不进入本版框架闭合数。

## 2026-05-19T14:20:00+08:00 Final Acceptance Update

最终接受报告已写入：`FINAL_ACCEPTANCE_REPORT_BOUNDARY_PATCHED.md`。

当前状态：`BOUNDARY_PATCHED_RELEASE_CANDIDATE`。

可接受范围：53 行 patched corpus；37 个 `PASS`，11 个 `PASS_RECOVERED`，5 个 `OPEN_OR_REFERENCE`。不得把原始 70 个 merged candidates 全部说成已闭合选必二法律正文样本。

## 2026-05-19T14:25:00+08:00 Coverage Matrix Update

已补覆盖矩阵：

- `QUESTION_COVERAGE_MATRIX.csv`
- `QUESTION_COVERAGE_MATRIX_SUMMARY.md`

该矩阵覆盖 53 行 boundary-patched framework-ready corpus，pending/excluded 题继续只在 `boundary_patched_excluded_pending_ledger.csv` 中追踪。
