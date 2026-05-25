# 2026 二模 B 线复跑报告

Status: `B_line_real_slice_rerun_captured_findings_open`

本报告记录 ClaudeCode B 线对 2026 二模 Q0113-Q0140 的真实分段复跑结果。它只说明 B 线证据已经捕获，不等于终稿、发布、通过或外审闭合。

## Run Method

整套一次性复跑曾出现 CLI 中断和挂起：

- `claudecode_2026_ermo_rerun_return_code.txt`: `-1`
- `claudecode_2026_ermo_rerun_return_code_v2.txt`: `-1`
- v3 调试日志显示 ClaudeCode 已进入读取和工具调用，但外层运行窗口中断，未生成必需产物。
- v4 脚本曾因中文路径字面量解析失败，修正为 `$PSScriptRoot` 推导路径后又出现长时间无产物挂起，已终止并改用套卷分段。

最终采用 suite-slice 真实复跑：每套二模独立调用 ClaudeCode，原始 stdout/stderr 与返回码分别留档。

## Return-Code Ledger

| Slice | Question rows | Return code | Raw output |
|---|---:|---:|---|
| 2026丰台二模 | Q0113-Q0115 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_fengtai_stdout.log` |
| 2026东城二模 | Q0116-Q0117 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_dongcheng_stdout.log` |
| 2026朝阳二模 | Q0118-Q0121 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_chaoyang_stdout.log` |
| 2026海淀二模 | Q0122-Q0128 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_haidian_stdout.log` |
| 2026房山二模 | Q0129 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_fangshan_stdout.log` |
| 2026西城二模 | Q0130-Q0132 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_xicheng_stdout.log` |
| 2026石景山二模 | Q0133-Q0135 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_shijingshan_stdout.log` |
| 2026顺义二模 | Q0136-Q0140 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_shunyi_stdout.log` |
| 2026顺义正文补充复核 | Q0136-Q0140 | 0 | `03_claudecode_lane/logs/claudecode_2026_ermo_shunyi_body_supplement_stdout.log` |

## High-Signal Findings

1. 证据等级总体被 B 线确认：A-support 选择题不得因已有答案表就升成 A-formal；B-choice-signal 行不得升入主链正例；A-formal 主观题可以保留正文位置但仍等真实外审。
2. 推理册最大的结构问题是同一推理形式聚合不足，尤其是必要条件、定义方法、类比推理、三段论、不完全归纳、同一律/矛盾律互引。
3. 思维册主要问题不是触发链缺失，而是个别 A-support 选择题正文层级过高。最明显的是 Q0136，B 线要求降为拓展/提示条，或显式标注 A-support 与“不作主链样本”。
4. Q0122、Q0123、Q0135、Q0139、Q0140 产生具体修补项：CT0054 D 项证据、Q0123 必修四边界、Q0135 替代角度备注、Q0139 一致性/确定性 CT 行、Q0140 综合题 boundary flag。
5. 顺义初跑误以为 `BODY_思维宝典.md` / `BODY_推理宝典.md` 不存在；补充复核已纠正，实际正文文件在 `04_fusion/THINKING_BAODIAN_V2_BODY_DRAFT.md` 与 `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`。

## Gate Verdict

`2026_ermo_B_line_real_slice_rerun_captured_but_patch_and_external_review_open`

## Local Patch Follow-Up

已处理一批不依赖外审的本地修补项：

- Q0136 正文 §71 已加 `A-support` 与“不作主链 A-formal 样本”提示。
- Q0123 推理正文 §56 已加必修四正确项边界提示。
- Q0134 推理正文 §62 已加同一律/矛盾律同形索引提示。
- Q0122 source-lock 已补 D 项陷阱证据说明。
- Q0125 source-lock 已补 DOCX 表格回源证据提示。
- MT0062 已补质量互变、辩证否定观替代角度说明。
- MT0065 与思维正文 §73 已补综合题边界标签。
- CT0066 已补入 Q0139 一致性要求 vs 确定性要求误挂。
- 硬性要求记事本已补 `B-choice-signal` 的 `book_part` 解释规则，以及综合题入库阈值规则。
- 推理正文已增加“同形聚合索引”，覆盖必要条件、定义方法、类比推理、不完全归纳、三段论、同一律/矛盾律等分散样本；Q0113 与 Q0115 也补了回链提示。

仍不得据此宣布终稿、通过、发布或 Word/PDF 成品。当前本地 B 线发现项已修到 `patched_pending_external_review` 或相应 patched 状态；GPT Pro V61、Claude V59 和最终交付门控仍未闭合。
