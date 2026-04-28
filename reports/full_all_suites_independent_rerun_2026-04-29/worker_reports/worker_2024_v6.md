# 劳动者-2024 v6 全量重跑报告

运行目录：`C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29`

处理范围：`SUITE_ROSTER.csv` 中 `year=2024` 的 15 套。执行方式为 cache-first，先读 roster 中的 `bundle_path`；仅在 cache 标记不清楚、题干/答案缺失或 S007 门头沟补源要求下回到补充源并记录边界。旧 `worker_2024` 草稿只用于覆盖自查，没有作为本轮证据。

## 输出文件

- `worker_outputs/2024_v6_audit_entries.csv`
- `worker_outputs/2024_v6_student_entries.md`
- `worker_outputs/2024_v6_choice_review.md`
- `worker_reports/worker_2024_v6.md`

## 覆盖汇总

| 项目 | 数量 | 说明 |
|---|---:|---|
| 处理套数 | 15 | S001-S015 全部完成本轮判定 |
| 学生版条目数 | 22 | 主观题 10、选择题正确项 6、选择题错肢 6 |
| 审计 CSV 数据行 | 38 | 不含表头；含学生条目证据、客观题全处理证据、阻塞/边界行 |
| 客观题全处理套数 | 10 | S001、S002、S004、S005、S006、S008、S009、S011、S013、S015 |
| 客观题未全处理套数 | 5 | S003、S007、S010、S012、S014 |

## 逐套状态

| suite_id | 套卷 | cache 状态 | 主观题状态 | 客观题状态 | 边界 |
|---|---|---|---|---|---|
| S001 | 2024海淀一模 | suite-bundle | PASS | 全 15 题 key 可读并处理 | 17(2) 有正式细则；高风险“主次矛盾”只保留源中有据表述，不扩写 |
| S002 | 2024西城一模 | suite-bundle | PASS | 全 15 题 key 可读并处理 | 17 题“生态价值观”等只按细则支撑保守表达 |
| S003 | 2024东城一模 | suite-bundle | PARTIAL | NEED_EVIDENCE | 试卷 PDF、答案 PDF 均为 rendered-ocr-needed；只用可读细则，不补造客观题 |
| S004 | 2024朝阳一模 | suite-bundle | PASS | 全 15 题 key 可读并处理 | 18 题“两点论和重点论”有讲评/细则原文支撑 |
| S005 | 2024丰台一模 | suite-bundle | PASS | 全 15 题 key 可读并处理 | 18(1) 只按“联系、发展、矛盾、唯物史观等角度”保守入 |
| S006 | 2024石景山一模 | suite-bundle | reference-only | 全 15 题 key 可读并处理 | 教师版/讲评不是正式评标，主观题不升级为正式细则链 |
| S007 | 2024门头沟一模 | classification-bundle-supplement | reference-only | NEED_EVIDENCE | 必须单列：分类汇编不是完整套卷；补源 PDF 存在但为扫描型，主观题保持 reference-only |
| S008 | 2024海淀二模 | suite-bundle | PASS | 全 15 题 key 可读并处理 | 16 题含联系、矛盾、价值观等，按答案/细则证据保守表达 |
| S009 | 2024西城二模 | suite-bundle | PASS | 全 15 题 key 可读并处理 | 17 题人与自然关系有评分参考支撑 |
| S010 | 2024东城二模 | suite-bundle | PARTIAL | NEED_EVIDENCE | 试卷/答案 PDF rendered-ocr-needed；主观题可用逐题细则，客观题不算全处理 |
| S011 | 2024朝阳二模 | suite-bundle | PASS | 全 15 题 key 可读并处理 | 16(2) 高风险哲学词只按“可从……角度阐释”记录，不扩写为唯一触发 |
| S012 | 2024丰台二模 | suite-bundle | PASS | NEED_EVIDENCE | 试卷 PDF rendered-ocr-needed；细则可读但客观题 paper/key 不足 |
| S013 | 2024顺义思政二模 | suite-bundle | reference-only | 全 15 题 key 可读并处理 | “细则”正文主要是参考答案，主观题不升级为正式评分链 |
| S014 | 2024海淀期中 | suite-bundle | PARTIAL | NEED_EVIDENCE | 试卷文本仅约 470 字，题干主要来自细则；客观题 key 不足 |
| S015 | 2024朝阳期中 | suite-bundle | PASS | 全 15 题 key 可读并处理 | 评标 docx 与细则 rtf 均可读，16/17 题可入学生版 |

## S007 门头沟一模专项边界

S007 的 `cache_status=classification-bundle-supplement`。本轮先读 roster 的分类汇编 bundle，可定位若干门头沟题目和参考答案方向；随后按 roster 记录检查补源 `C:\bp_sync_visible\reports\overnight_2026-04-25\downloaded_evidence\2024_mentougou_yimo_with_answers.pdf`。该 PDF 文件存在，但文本提取为 0 字，不能直接提供可核验的正式评分细则。

因此：S007 可作为题目索引与 reference-only 方向记录；不能把分类汇编或扫描补源当作完整套卷、答案 key 或主观题评分细则。学生版不写 S007 主观条目，审计 CSV 记录边界与 fallback。

## 高风险词处理

- `辩证否定`：只在 S003/S010/S015 等源文出现时记录为 source-supported 或 reference-only；未进学生版稳定触发链。
- `量变质变`、`主次矛盾`、`矛盾主次方面`、`主流支流`：未作为学生版触发链写入；仅在源文或边界中保留 NEED_EVIDENCE。
- `两点论重点论`：只在 S004 朝阳一模 18 题中写入，因为讲评/细则原文明确写“坚持‘两点论’和‘重点论’的统一”。
- `价值观导向`：未作为独立触发链写入；普通“价值观/核心价值观”只在有题源支撑时按材料语境保守使用。

## 阻塞项

- S003、S010：东城一模/二模的试卷或答案 PDF 在 cache 中为 `rendered-ocr-needed`，客观题不能算全处理。
- S007：门头沟一模是分类汇编 + 扫描补源，缺可读完整套卷答案 key 和正式评分细则；主观题保持 reference-only。
- S012：丰台二模试卷 PDF 为 `rendered-ocr-needed`，客观题缺完整可读 paper/key。
- S014：海淀期中试卷文本不足，客观题 key 不足；主观题只对细则可读部分保守处理。
