# Phase12 Teaching Patched Recheck · Digest (Claude Opus 4.7 Adaptive)

Status: `TEACHING_PATCHED_RECHECK_DIGEST_REVIEW_ONLY_NO_WORD_NO_PDF_NO_FINAL`

## verdict
**TEACHING_PATCH_NEEDS_SMALL_PATCH_NO_FINAL**

8 项强制 gate 全部 PASS，但 Codex 用同一组样板句批量填充 12+ 条主观题的"最小三件套"，引入"机械化模板感"这一新教学体感问题。建议在 Governor 之前收一次小补丁。

不授权 Word / PDF / final / 终稿 / 最终稿 / 宝典成品。

## 8 项 Gate 复核结果

| Gate | 结果 |
|---|---|
| 50/50 选择题 `【完整选项】` | PASS |
| 27/27 主观题最小三件套 | PASS（含模板化告警） |
| 双索引 `NEEDS_*` 清零并改名 | PASS |
| `Q-2025海淀二模-20` 答案/动作分句 | PASS |
| `Q-2024朝阳一模-20-1` 弱学生否定后件式口诀 | PASS |
| `Q-2025顺义一模-7` 四步口令 + 大项不当扩大锁定 | PASS |
| `Q-2026丰台一模-18-2` 【】框 + 甲乙锁定链 | PASS |
| 全包 review-only 边界 | PASS |

## 7 条 small_patch（不阻 gate，但 Governor 前应收）

1. **SP1 反模板**：12+ 条主观题 `易错陷阱 / 考场动作 / 同类题索引` 是统一样板句，应改写为题面级具体内容（永动机、图书馆、朝阳一模20(1)/(2)、海淀二模17(2)、西城二模16(2)/(3)、西城一模19(2)/(3)/(5)、东城一模19(4)、朝阳期中20/21(2)、朝阳二模19(1)/(2)、顺义一模19(1)/(2)、通州期末19(2)、顺义一模17(1) 等）。`【同类题索引】` 能列具体题号的优先列出，少用"见索引"meta 指针。
2. **SP2 `Q-2025顺义一模-7` 设问段去重**：`【完整选项】` 已给出 ABCD，`【设问】` 段不必再重写一遍 ABCD，仅留题干一行。
3. **SP3 `Q-2024朝阳一模-20-1` 字段合并**：`【考场口令】`（具体）与模板化的 `【考场动作】` 重复，应把口令并入考场动作，删模板；同时把 `【易错陷阱】` 改写为题面相关的"否后必否前 / 不能写成肯定后件式"。
4. **SP4 体例非强制项**：海淀二模20 仍 bullet 行格式；丰台期末18(1) 用旧字段名 `【可写规则】`；丰台一模18(2) 单行块体无空行；顺义一模7 选择题用主观题式扩展。final clean 时统一。
5. **SP5 双索引英文审计字符串**：`manual_lock:`、`phase06_logical_form_locked:`、`external_forced_check`、`SCIENCE_ONLY_SOURCE_SUPPORTED`、`no_phase06_locked_reasoning_row` 等仍在 review-only 文件中；final student clean 必须剥离。
6. **SP6 边界陷阱与混类醒目提示**：丰台期末7、通州期末9、海淀二模13、海淀期末8、朝阳期中12 顶端尚未加可视化提醒。
7. **SP7 上一轮 SF6/SF7/SF8/SF9/SF10 未关闭**：西城二模6 D 项、通州期末10 ④项、朝阳二模7 A 项、海淀期末8 D 项、海淀二模13 C 项均待加学生层硬判 / 口诀 / 周延快查。

## 没有引入的新风险

事实锁定全保留（顺义一模7 大项不当扩大、朝阳二模7 小项扩大、海淀二模17(1) 科学思维专项、朝阳一模20(1) 否定后件式、丰台一模18(2) 甲乙链）；双索引未新增"边界陷阱当正例"挂载；海淀二模20 答案/动作分段无内容增删错误。

## 闸口建议

- 教学补丁层：`TEACHING_PATCH_NEEDS_SMALL_PATCH_NO_FINAL`。
- 下一步：Governor 之前收一遍 SP1+SP2+SP3；SP4–SP7 可并入 final student clean 剥离动作执行。
- 不授权 Word / PDF / final / 终稿 / 最终稿 / 宝典成品；后续仍需外审回看、Governor、Confucius、final clean 剥离。
