# hume 2026 late culture worker report

## Scope

- Run: `C:\bp_sync_visible\reports\culture_all_suites_rerun_2026-04-29`
- Suites: S048-S056, 2026期中期末
- Output CSV: `worker_outputs\hume_2026_late_culture_entries.csv`
- Rule applied: 主观题只收细则、评标、阅卷、讲评给分口径；选择题只在同时具备题干和可靠答案键时写正确项链或错肢。

## Suite Coverage

| suite_id | suite_name | coverage_status | culture entries | blocker |
| --- | --- | --- | ---: | --- |
| S048 | 2026海淀期中 | PASS | 1 | 无主观文化细则；已处理文化选择题Q5。 |
| S049 | 2026海淀期末 | PASS | 1 | Q17为B类等级支持，不作逐点标分。 |
| S050 | 2026西城期末 | PASS | 1 | 当前bundle细则需读图，依据旧复核确认A类；不把参考答案冒充细则。 |
| S051 | 2026东城期末 | PASS | 3 | 无。 |
| S052 | 2026朝阳期中 | PASS | 6 | 无。 |
| S053 | 2026朝阳期末 | PASS_WITH_BLOCKED_OBJECTIVE | 2 | 主观Q16可由旧读图细则入链；客观题缺可靠答案键，BLOCKED。 |
| S054 | 2026丰台期末 | PASS_WITH_BLOCKED_OBJECTIVE | 2 | 主观Q16可由评标PDF入链；客观题缺可靠答案键，BLOCKED。 |
| S055 | 2026石景山期末 | PASS_WITH_BLOCKED_OBJECTIVE | 2 | Q18(1)仅按答案及评分参考登记B类；Q1-Q2缺完整题干，BLOCKED。 |
| S056 | 2026通州期末 | PASS | 2 | 无。 |

## Evidence Notes

- S053朝阳期末：当前suite bundle对试卷和细则均标为 `rendered-ocr-needed`，未见客观答案表；只采用旧复核表中已确认读图的Q16评分细则文化链，不新增扫描不清的高风险词。
- S054丰台期末：评标PDF文本可读，Q16文化角度为等级支持；试卷文本层缺失且未见客观答案键，选择题不补。
- S055石景山期末：本地bundle只有“答案及评分参考”，所以Q18(1)写为B类等级支持，不写成详细评标细则；文化选择题只有答案键/旧清单线索，缺完整题干，阻塞。

## Counts

- Processed suites: 9
- CSV rows including header: 21
- CSV data entries: 20
- PASS/MODULE rows: 17
- BLOCKED rows: 3
- Objective fully handled suites: 4 (S048, S051, S052, S056)
- Objective blocked suites: 3 (S053, S054, S055)
