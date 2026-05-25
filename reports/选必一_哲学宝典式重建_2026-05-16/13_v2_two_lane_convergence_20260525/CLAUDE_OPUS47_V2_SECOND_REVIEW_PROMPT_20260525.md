# Claude Opus 4.7 Adaptive V2 二审提示词（2026-05-25）

你现在担任选必一《当代国际政治与经济》主观题术语宝典的 Claude Opus 4.7 Adaptive 二审。

GPT Pro 已经以“V2 主融合编辑”身份读取当前终稿、Codex/ClaudeCode 差异材料、ClaudeCode Opus 融合建议和当前 SHA 覆盖审计，并返回 `V2_STRICT_ACCEPTED`。

你的任务不是重新泛泛审稿，而是二审 GPT Pro 主融合是否可以作为 V2 闭合证据。

请重点判断：

1. GPT Pro 是否真的按“主融合编辑”口径判断，而不是只做普通外审。
2. 当前终稿是否仍有必须落盘补丁。
3. Codex 线与 ClaudeCode Opus 线是否已经充分重合。
4. GPT Pro 对覆盖范围的限定是否合理：104 个 P0 候选/裁决宇宙闭合，但若要声明“桌面全部源文件重新扫描闭合版”，仍需另跑全源 recrawl。
5. 当前终稿是否可以登记为“Codex + ClaudeCode Opus 双线厚稿，经 GPT Pro 主融合、Claude Opus 4.7 Adaptive 二审、Codex 证据回查的选必一宝典最终候选版”。

请严格输出：

```markdown
# Claude Opus 4.7 Adaptive V2 二审结论

## VERDICT

STRICT_V2_ACCEPTED / ACCEPTED_WITH_LIMIT / NOT_ACCEPTED

## 对 GPT Pro 主融合的审查

## 对当前终稿的硬伤检查

## 对覆盖口径的裁定

## 必须落盘补丁

| 优先级 | 位置 | 问题 | 应如何改 |
|---|---|---|---|

如无 must-fix，请写“无”。

## 最终声明

能否登记为 V2 最终候选版：可以 / 不可以。
```

