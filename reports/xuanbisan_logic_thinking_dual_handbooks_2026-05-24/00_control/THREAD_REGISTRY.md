# Thread Registry

| lane | owner | role | output root | status |
|---|---|---|---|---|
| A | Codex | 总控、证据裁决、独立制作、融合、清洗、交付 | `02_codex_lane/` | active |
| B | ClaudeCode | 厚内容挖矿、套卷闭环、遗漏捕捉、候选题源入账 | `03_claudecode_lane/` | pending_launch |
| Review-GPT | GPT Pro | 真实外审，主查触发链、推理形式聚类、错挂和漏题 | `05_gptpro_review/` | real_call_pending |
| Review-Claude | Claude | 真实外审，主查教学可读性、概念误分、迁移风险 | `06_claude_review/` | real_call_pending |
| Governor | Codex role | 否决假完成、弱证据、错误边界、学生版污染 | `07_governor_confucius/` | pending |
| Confucius | Codex role | 零基础学生能否只看产物完成迁移 | `07_governor_confucius/` | pending |

## 本线程硬边界

- 不把普通参考答案冒充评分细则。
- 不把思维部分写成概念表。
- 不把推理题混进思维宝典主链；推理题进入单独推理宝典。
- 不把“GPT/Claude 待审”说成“GPT/Claude 已审”。
- 不把旧 2026-05-06 二线版当作全量穷尽终版。
