# 外部模型证据台账

| 时间 | 模型/入口 | 材料 | 结果 | 保存位置 | 是否计入最终验收 |
|---|---|---|---|---|---|
| 2026-05-24 | GPT Pro 网页端 | 文件上传 | BLOCKED_FILE_UPLOAD_NOT_ALLOWED | `02_gptpro_web/GPTPRO_WEB_STATUS.md` | 否 |
| 2026-05-24 | GPT Pro 网页端 | 分批粘贴材料：哲学标杆 + 选必一清洁稿 + END_AND_REVIEW | FAIL_MUST_REVISE | `02_gptpro_web/GPTPRO_REVIEW_CAPTURE_20260524.md` | 是，作为未通过审稿意见 |
| 2026-05-24 | Claude Opus / Adaptive Thinking | 待提交 | PENDING | `03_claude_opus/` | 否 |
| 2026-05-24 | ClaudeCode `--model opus` | v5/v6 学生版分段清理 | FALLBACK_LOCAL_REWRITE_DONE | `03_claude_opus/V5_RESIDUAL_CLEANUP_*_STDOUT.md` | 否，作为 ClaudeCode 生产/修订证据，不替代 Claude 网页 Opus/Adaptive 最终验收 |
| 2026-05-24 | Codex 本地预检 | v6 学生版 | LOCAL_READY_FOR_EXTERNAL_REVIEW | `04_revisions/V6_LOCAL_QA_REPORT.md` | 否，作为提交外部复审前的本地门槛 |
| 2026-05-24 | ClaudeCode `--model opus` | v6 学生版全稿复审 | FAIL_P0_REMAINING | `03_claude_opus/CLAUDE_CODE_OPUS_V6_REVIEW_CAPTURE_20260524.md` | 否，作为本地修订依据 |
| 2026-05-24 | ClaudeCode `--model opus` | v6 P0 修订后复审 | PASS_READY_FOR_EXTERNAL_REVIEW | `03_claude_opus/CLAUDE_CODE_OPUS_V6_REVIEW2_CAPTURE_20260524.md` | 否，作为本地 ClaudeCode 通过证据，不替代 GPT Pro / Claude Opus 网页端最终验收 |
| 2026-05-24 | GPT Pro 网页端 | v6 学生版 + 哲学标杆 + QA 报告 + 终审提示 | PASS | `02_gptpro_web/GPTPRO_V6_REVIEW_CAPTURE_20260524.md` | 是，作为 GPT Pro 真实网页端最终复审通过证据 |
| 2026-05-24 | Claude 网页端 Opus/Adaptive | v6 待提交 | BLOCKED_LOGIN | `03_claude_opus/CLAUDE_WEB_BLOCKED_LOGIN_20260524.md` | 否，未进入可提交的 Claude 对话页 |
| 2026-05-24 | ClaudeCode `--model opus --effort max` | v6 学生版 + GPT Pro PASS + 哲学标杆 + QA 报告 | FALLBACK_PASS | `03_claude_opus/CLAUDE_CODE_OPUS_AFTER_GPT_PASS_FALLBACK_CAPTURE_20260524.md` | 否，作为备用 Opus 内容审查，不替代用户可见 Claude 网页 Opus/Adaptive 门槛 |

## 计入规则

- 只接受真实 GPT Pro 网页端输出或用户可确认的 GPT Pro 页面输出。
- 本轮用户指定的是 Claude Opus/Adaptive 网页端复审；ClaudeCode 锁定 Opus 的输出只能作为备用内容审查，除非用户明确放宽本轮网页端门槛，否则不计入最终闭环。
- 普通 API、子智能体、模拟评审、摘要转述不计入最终验收。
- 若模型输出不完整、只有短字、卡住、无法提交或无法保存，记录为 BLOCKED，不得写 PASS。
