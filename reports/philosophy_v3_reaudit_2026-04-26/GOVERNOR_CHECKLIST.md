# GOVERNOR_CHECKLIST

日期：2026-04-26

## STEP_00 检查

- [x] v3 独立工作区已创建。
- [x] 旧核心产物已复制到 `freeze/`，未直接覆盖旧正本。
- [x] 已记录旧产物 SHA256。
- [x] 已创建 plan/progress/control 文件。
- [x] 已明确旧 `已闭环` 状态不自动有效。
- [x] 第一批抽查没有把普通参考答案升级成细则。
- [x] 第一批抽查已把 ClaudeCode v2 正文降级为控制层证据。
- [x] 第一批抽查已识别 B/C/D 证据边界风险。
- [x] 本轮未改正式总框架、错肢库、题源清单、ledger；总 governor 只追加来源复核状态记录。
- [x] STEP_00 阶段未提前勾选后续步骤。

## STEP_00 结论

STEP_00 通过。

## STEP_01-06 来源复核检查

- [x] 框架触发条目 496 行全部分类，无未分类行。
- [x] 框架不同来源键 310 个全部形成来源层结论。
- [x] 错肢库来源行 1583 行全部分类，无未分类行。
- [x] 旧题源清单 56 行全部形成 v3 口径结论。
- [x] E 行未被强行升级；已明确为缺 OCR、缺答案键、缺用户补充原件或未证实来源。
- [x] D 行未被强行升级；已限制为 reference-only/方向边界。
- [x] B 行未被写成逐点官方细则；已限制为评标角度清单或整理者材料链。
- [x] `all_source_reaudit_summary.md`、`全来源复核_边界与缺口清单.md`、3 个逐行 CSV 已生成。
- [x] 本轮未改正式总框架、错肢库、题源清单、ledger；总 governor 只追加来源复核状态记录。

## STEP_06A 内容回源复核检查

- [x] 496 条 V2 框架来源均已回到 bundle 中对应原题/细则片段。
- [x] 只把原题/细则直接出现或等价给分表述的条目标为 `SUPPORTED_DIRECT_*`。
- [x] 仅由 V2 材料链解释推出、原题/细则未直接支撑的条目标为 `WEAK_INFERRED_FROM_MATERIAL` 或 `NEEDS_HUMAN_CONTENT_CHECK`。
- [x] 来源缺口、答案键缺口、reference-only 条目继续阻断，不用旧逻辑链补洞。
- [x] `content_backtrace_review.csv`、`content_backtrace_summary.md`、`content_backtrace_non_direct_full.md` 已生成。

## 当前 governor 结论

来源层复核通过：旧框架、错肢库、题源清单的所有来源行都已被 v3 分类。

内容回源复核通过：V2 496 条框架来源已按“原题/细则是否真的支撑所挂原理”完成保守分类；277 条直接支撑，219 条不得自动进入正文。

v3 正文未完成。下一步只能进入 `STEP_07` 生成 diffable draft，不得写 `TASK_COMPLETE`，不得把 D/E 行放入正式正文。
