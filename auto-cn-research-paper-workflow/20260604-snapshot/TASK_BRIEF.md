# TASK_BRIEF

- created_at: 2026-06-04T21:24:50+0800
- task: Mac 设备迁移后重新拉取、同步并验收 `auto-cn-research-paper` 工作流。
- scope: 仅限 `auto-cn-research-paper-workflow/20260604-snapshot` 和对应个人 skill 副本；不处理北京高考政治题库、评分细则或学生讲义正文。
- user_boundary: 用户已手动登录；Codex 可检查授权浏览器状态，但不得读取、保存或绕过任何密码、Cookie、验证码、SSO 或下载权限门槛。
- external_review_boundary: ChatGPT/GPT Pro 与 Claude 只在真实可见网页或 App 会话中满足最终审阅门；CLI/API 只可作为构建建议，不计入最终通过。

## Current Minimal Step

1. 确认 Chrome/RUC-CNKI 授权路径在 Mac 上可见。
2. 同步 skill 新增脚本、测试和模板到仓库/工作区副本。
3. 重新跑测试和总闸口矩阵。
4. 只报告真实通过项与阻塞项，不做最终完成声称。
