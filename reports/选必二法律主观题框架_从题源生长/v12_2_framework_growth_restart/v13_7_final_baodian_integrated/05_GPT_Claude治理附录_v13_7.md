# 05 GPT/Claude 治理附录 v13.7

Status: `real_model_governance_captured_for_v13_7`

## 真实模型链

| 阶段 | 模型/角色 | 真实输出 | 结论 |
|---|---|---|---|
| Round03 | GPT source-check review | `model_outputs/gpt_round03_source_check_review.md` | source-check 后 v12.2 baseline 可作为框架底座 |
| Round03 | Claude source-check key capture | `model_outputs/claude_round03_source_check_review_key_capture.md` | 赞成保留 source-checked baseline，并强调学生迁移语言 |
| Round05 | GPT Pro final review | `round05_v13_final_advisor_review/model_outputs/gpt_round05_v13_final_review_pro_web_raw.md` | `ACCEPT_AFTER_MINOR_PATCHES` |
| Round05 | Claude Opus 4.7 Adaptive final review | `round05_v13_final_advisor_review/model_outputs/claude_round05_v13_final_review_opus47_web_raw.md` | `ACCEPT_AFTER_MINOR_PATCHES` |
| Round06 | GPT Pro with prior framework | `round06_gpt_v13_1_final_eval_with_prior_framework/model_outputs/gpt_round06_v13_1_final_eval_with_prior_framework_raw.md` | `ACCEPT_WITH_MINOR_PATCHES`；确认 A/B 双轴为最终主框架 |
| Round07 | Claude zero-baseline student retest | `claude_zero_baseline_iterative_test_20260523_round07/model_outputs/claude_zero_baseline_iterative_test_round07_opus47_raw.md` | 可以进入最终宝典写作 |

## Codex 证据裁决

- Round03 负责 source-check baseline，不能替代最终学生可迁移性测试。
- Round05/Round06 负责判断 v13.1 双轴主框架是否成立。
- Round07 不是让 Claude 评审答案，而是让 Claude 扮演“聪明但零基础高三学生”，只看框架和压缩题面现场作答；本地答案键、评分锚点、材料触发链、答案骨架和学生预警均未发送。
- v13.2-v13.7 的每一轮修改都来自 Claude 真实盲测暴露的问题，再由 Codex 本地按题源和框架目标裁决。

## 保留边界

- 本版可以宣称 v13.7 框架已完成零基础迁移闭环。
- 本版只有在 DOCX/HTML/PDF、42题题卡、开放容器附录、追溯矩阵、Governor、Confucius 和 PDF渲染 QA 都存在后，才可宣称 v13.7 宝典交付闭环。
- DOCX direct render QA 仍受本机 LibreOffice/soffice 缺失限制；可声明 Word COM 打开检查，不可声明 DOCX 直渲染通过。
