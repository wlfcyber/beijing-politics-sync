# CODEX A 线源索引进度

## 2026-05-07

- 已生成本机 2024-2026 文件级题源清单。
- 已生成套卷候选清单。
- 已扫描预处理缓存中的选必三相关术语命中。
- 已审计 528-row control base 和 73-row thinking signal matrix。

## 关键计数

- source_inventory_rows: 175
- suite_candidate_rows: 53
- corpus_manifest_rows: 173
- term_hit_rows: 733
- control_base_rows: 528
- signal_matrix_rows: 73
- source_root_2026_erm_files: 0

## control base 分布

```json
{
  "by_suite": {
    "S-2024朝阳一模": 23,
    "S-2024朝阳二模": 24,
    "S-2024朝阳期中": 22,
    "S-2024海淀二模": 24,
    "S-2024西城一模": 26,
    "S-2025东城期末": 54,
    "S-2025丰台期末": 46,
    "S-2025海淀二模": 2,
    "S-2025海淀期末": 34,
    "S-2025西城二模": 34,
    "S-2025顺义一模": 92,
    "S-2026东城一模": 31,
    "S-2026东城期末": 30,
    "S-2026丰台一模": 2,
    "S-2026朝阳期中": 31,
    "S-2026通州期末": 29,
    "S-2026顺义一模": 24
  },
  "by_part": {
    "待判": 281,
    "思维": 49,
    "边界": 72,
    "推理": 100,
    "交叉": 24,
    "missing": 2
  },
  "by_final": {
    "pending": 528
  },
  "by_block": {
    "pending_pairing": 486,
    "blocked_until_options_visual_check": 34,
    "locked_pending_laneB_visual_confirmation": 2,
    "blocked_until_full_paper_visual_or_ocr_question_inventory": 2,
    "blocked_until_answer_or_rubric_pairing": 4
  }
}
```

## 下一步

- 将 control base 的 528 行转为正式 `入正文 / 同类索引 / blocked / excluded` 裁决矩阵。
- 对 term hit index 中 2026 一模/期末/期中与 2024-2025 二模额外源进行回源抽样。
- 等 ClaudeCode B 线产出 suite_reports 和 entries 后做交叉验证。

## 2026-05-07 12:38 更新

- 已生成 `CODEX_EXHAUSTIVE_DECISION_MATRIX.csv`，union rows `534`。
- 当前 union 判定：`入正文 77`、`blocked 183`、`excluded 104`、`同类索引 170`。
- 已生成 `CODEX_EXHAUSTIVE_CANONICAL_DECISION_MATRIX.csv`，canonical 362 判定：`入正文 77`、`blocked 181`、`excluded 104`。
- 已生成 `CODEX_SIGNAL_CLOSURE_MATRIX.csv`，73-row signal 当前判定：`入正文 44`、`excluded 29`。
- 已生成 `CODEX_PHASE05_PHASE12_BASELINE.md`。该文件只授权底账监督，不授权终稿、Word 或 PDF。
