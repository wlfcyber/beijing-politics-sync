# DECISION_LOG

| time | decision | reason |
|---|---|---|
| 2026-05-24 | 以 5.2 已认可母版为唯一底稿 | 用户明确不接受脱离母版的新结构，只允许把新题插回原宝典节点。 |
| 2026-05-24 | 本轮先到双线审计，不做 Word 成品 | 用户要求“先让 codex 和 claudecode 双线跑，到审核那一步”。 |
| 2026-05-24 | 2024-2026 一模与 2026 二模同时纳入覆盖核查 | 用户担心原宝典只覆盖少数反复出现题，必须查明遗漏。 |
| 2026-05-24 | ClaudeCode `--model opus` 被 403 拒绝后降级尝试默认/sonnet | B 线必须真实运行，但当前账号不允许 opus 请求；先保留失败日志并继续尝试可用 ClaudeCode 模型。 |
| 2026-05-24 | ClaudeCode 403 定位为 CLI 未继承本机代理环境 | 设置 `HTTP_PROXY/HTTPS_PROXY/ALL_PROXY=http://127.0.0.1:18001` 后，ClaudeCode 小请求返回 OK，可继续真实 B 线。 |
