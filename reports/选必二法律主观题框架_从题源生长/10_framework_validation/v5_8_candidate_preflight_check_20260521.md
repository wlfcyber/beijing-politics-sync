# V5.8 Candidate Preflight Check

时间：2026-05-21 04:08 CST

## 检查对象

- `12_final_baodian/选必二法律主观题满分训练宝典_v5_8_27核心38题保分索引_P1入口修补候选版_20260521.md`
- `12_final_baodian/question_by_question_framework_runs_v5_8_27core65guard_20260521.csv`
- `12_final_baodian/non_core_guardrails_v5_8_20260521.csv`
- `04_merge_audit/candidate70_to_current65_delta_ledger_20260521.csv`

## 机器检查结果

| 项目 | 结果 |
|---|---:|
| 核心题标题 | 27 |
| 核心题入口行 | 27 |
| 含 `+` 或多卡乱入口的入口行 | 0 |
| 非核心题标题 | 38 |
| 非核心标题带 question_id | 38 |
| 非核心 question_id 去重后 | 38 |
| `SOURCE-CHECK` 醒目红线 | 23 |
| `REFERENCE-ONLY` 醒目红线 | 4 |
| `BOUNDARY` 醒目红线 | 4 |
| `TRANSFER` 醒目红线 | 1 |
| `DUPLICATE-CROSSREF` 醒目红线 | 1 |
| 27 核心逐题运行 CSV 行数 | 27 |
| 38 非核心护栏 CSV 行数 | 38 |
| 70->65 去向台账 CSV 行数 | 53 |

## 裁定

V5.8 候选稿通过本地机械预检：没有把 38 道非核心题升为核心；27 道核心题入口已统一为 `主卡 + 最多 1 辅卡`；非核心题均带 question_id 和红线提示。

但 V5.8 仍是 `candidate_pending_gptpro_capture`，不得生成最终 Word/PDF，也不得在 GPTPro V5.7 捕获与交叉验证前称为最终版。
