# ORDER 031: 选必二即时补丁令

## 当前状态

状态词：`CANDIDATE_DELIVERY_NEEDS_AUDIT`

依据：

- v13_10 目录已生成 Markdown、HTML、DOCX、PDF。
- `07_RENDER_QA_REPORT_v13_10.md` 显示 traceability 42 行、42 张题卡、PDF 29 页渲染、无空白页、DOCX 结构可读、Word COM 可打开。
- 同报告也明确：DOCX direct render via `render_docx.py` 未通过/不声称通过，原因是本机无 LibreOffice/soffice。
- `05_GPT_Claude_Confucius治理附录_v13_10.md` 记录 Round03、Round05、Round06、Round07 真实 GPT/Claude 链，以及本地 Confucius 试读 agent。
- v13.10 交付边界写的是 `v13_10_final_baodian_integrated_pdf_rendered_docx_generated_with_docx_render_caveat`。

## 禁止声称

不得直接称 `STRICT_FINAL_ACCEPTED`，除非下一轮确认：

- 所有真实 GPT/Claude 原始文件确实存在且内容支持当前 v13.10；
- 42 题 traceability 与正文一一匹配；
- Confucius 是 artifact-only 检查；
- DOCX/PDF 交付边界被清楚说明，DOCX direct render caveat 未被掩盖。

## 下一步硬任务

1. 核验真实外部模型文件：
   - `model_outputs/gpt_round03_source_check_review.md`
   - `model_outputs/claude_round03_source_check_review_key_capture.md`
   - `round05_v13_final_advisor_review/model_outputs/gpt_round05_v13_final_review_pro_web_raw.md`
   - `round05_v13_final_advisor_review/model_outputs/claude_round05_v13_final_review_opus47_web_raw.md`
   - `round06_gpt_v13_1_final_eval_with_prior_framework/model_outputs/gpt_round06_v13_1_final_eval_with_prior_framework_raw.md`
   - `claude_zero_baseline_iterative_test_20260523_round07/model_outputs/claude_zero_baseline_iterative_test_round07_opus47_raw.md`
2. 抽查 42 题中至少 6 个硬样本：
   - A/B 双轴入口是否真的能让学生定位；
   - 答案骨架是否能直接写；
   - 开放容器题是否没有被误晋升正文。
3. 复核 `TRACEABILITY_MATRIX_v13_10_final.csv`：
   - 42 行必须全部能对应正文题卡；
   - 不得有正文题卡缺 traceability 或 traceability 题缺正文。
4. 对 DOCX caveat 做清晰交付边界：
   - Word COM open check 已通过可写；
   - direct render 未通过不可写成通过；
   - PDF 渲染版作为视觉检查主交付。
5. 若以上都通过，再把状态提升为“可交付候选已强验收”，但若按总控硬规则仍缺 DOCX direct visual QA，则保持 caveat，不写无条件终版。

## 下一次汇报必须给出

- 六个外部模型原始文件是否全部存在。
- 42 行 traceability 与 42 张题卡是否完全一致。
- 抽查硬样本列表与结果。
- 最终允许给用户的准确状态语。

