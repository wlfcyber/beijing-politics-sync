# Batch 013 Tail Reopen After Claude Opus

Claude Opus 对“无 Batch013”的审核没有直接放行，而是要求补查 OCR/图片源。Codex 按要求补查后发现 `2026朝阳期末Q20` 是正式可入链候选。

## 关键发现

- `2026朝阳期末` 的试卷与细则均在 manifest 中，但状态为 `rendered-ocr-needed`，没有文本缓存，因此此前 `rg` 关键词筛查漏掉。
- 试卷渲染图 `e1a49527cb4c175f\page_007.png` 显示 Q20 题面，明确要求运用《当代国际政治与经济》知识分析中国特色大国外交为什么要更有作为。
- 细则渲染图 `487b2d15b3a3ac2b\page_003.png` 显示 Q20 的 `【阅卷细则】`，并按和平发展、政治、经济、我国国家利益四个角度逐项赋分。

## 裁决

原先的 `Batch013 无题闭批` 不成立。现改为：

1. 开启 `BATCH_013_TAIL`。
2. 正式候选：`2026朝阳期末Q20`。
3. 继续阻断：`2026丰台期末Q20`。
4. 因当前只发现 1 道新增可入链题，本批按尾批处理：Codex + ClaudeCode 出稿，GPT Pro 与 Claude Opus 审核，Governor 后再进入累计合并/学生交付。

