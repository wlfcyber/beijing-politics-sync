# 必修四文化 56 套重跑审计报告

生成时间：2026-04-29 02:08:09

- 合并条目：303
- 覆盖矩阵：56 套
- 覆盖状态：{'processed': 43, 'source-boundary-reference-only': 1, 'processed_with_choice_boundary': 10, 'module-boundary': 2}

## Worker Reports

### feynman_2025_late_culture.md

# Feynman 2025 Late Culture Worker Report

## Scope

- Run directory: `C:\bp_sync_visible\reports\culture_all_suites_rerun_2026-04-29`
- Assigned suites: S026-S037, covering 2025 二模与期中期末。
- Write scope used: `worker_outputs\feynman_2025_late_culture_entries.csv` and this report only.
- Final Word was not modified.

## Evidence Rules Applied

- Main questions enter the culture table only when the bundle contains a scoring rubric, marking rule, review/lecture rubric, or scan-rubric OCR that explicitly supports culture points.
- Reference answers were not treated as scoring rubrics unless the same bundle section exposed scoring/marking language.
- Choice questions enter only when both stem and reliable answer key or answer explanation are present in the bundle.
- Philosophy chains were kept separate. If a question used 《哲学与文化》 but the scoring point was philosophy-only, it was marked `MODULE_BOUNDARY`.

## Framework 0-7 Coverage

| Slot | Framework Node | Newly Used In This Batch |
|---:|---|---|
| 0 | 载体 | S027 Q9, S030 Q5/Q6, S031 Q16, S034 Q16(1), S035 Q16 |
| 1 | 特点 | S033 Q1, S035 Q4, S037 Q1 |
| 2 | 作用 | S026 Q17, S027 Q20, S029 Q16, S030 Q6, S034 Q1, S035 Q3, S036 Q4 |
| 3 | 横向 | S030 Q16(1), S034 Q3, S036 Q16 |
| 4 | 纵向 | S026 Q17, S029 Q16, S030 Q16(1), S031 Q3/Q16, S033 Q3/Q16, S034 Q16(1), S035 Q16, S036 Q4/Q16 |
| 5 | 文化强国/文化自信 | S027 Q20, S030 Q16(1), S031 Q16, S033 Q3, S034 Q16(1), S035 Q16, S036 Q16, S037 Q1 |
| 6 | 民族精神 | S027 Q1, S034 Q2, S031 Q16 |
| 7 | 习近平文化思想 | S033 Q16 |

## Suite Coverage

| Suite | Status | Main Culture Questions | Culture Choice Questions | Notes |
|---|---|---|---|---|
| S026 2025海淀二模 | PASS | Q17 | none confirmed | Q17 only has 1 分文化补点；choice coverage not forced because bundle did not expose full cultural objective stem+key set. |
| S027 2025西城二模 | PASS | Q20 | Q1, Q9 | Q20 has clear scoring split: cultural rights/supply/needs and talent/innovation. |
| S028 2025东城二模 | PASS | none | Q3, Q4 | Q16 is philosophy-only scoring; culture choice rows entered from reliable key. |
| S029 2025朝阳二模 | PASS | Q16 | Q3, Q4 | Q16 has culture传承、文化濡染、文化功能、文化创新 wording in scoring rules. |
| S030 2025丰台二模 | PASS | Q16(1) | Q5, Q6 | Q16(1) is mixed philosophy+culture; report keeps culture chain separate. |
| S031 2025昌平二模 | PASS | Q16 | Q3 | Main row uses PPT scoring support; choice Q3 is robot秧歌科技赋能文化创新. |
| S032 2025海淀期中 | MODULE_BOUNDARY | none | none | No confirmed culture module question found; objective candidates are economics/politics/legal. |
| S033 2025海淀期末 | PASS | Q16 | Q1, Q3 | Q16 excludes generic文化功能/中华文化特点 because local细则 lists them as typical non-scoring answers. |
| S034 2025西城期末 | PASS | Q16(1) | Q1, Q2, Q3 | Main row covers中轴线文物建筑活化利用. |
| S035 2025东城期末 | PASS | Q16 | Q3, Q4 | Q16 requires saying what the器物承载; only writing文化载体 is explicitly insufficient. |
| S036 2025朝阳期末 | PASS | Q16 | Q4 | Scan-rubric OCR gives culture 6 分 structure: 自信、弘扬、发展、传播. |
| S037 2025丰台期末 | PASS | none | Q1 | Main Q16 is philosophy-only; culture coverage comes from objective Q1 answer explanation. |

## Blockers And Boundaries

- No `BLOCKED` suite in S026-S037.
- S032 is `MODULE_BOUNDARY`, not blocked: local bundle has answer key and stems, but no question was judged to be a culture-module entry under the template.
- S026 choice questions were not expanded because the local bundle evidence used for this run did not expose a reliable full cultural objective stem+answer-key pair. The suite still passes through Q17 culture scoring support.

## Output Counts

- CSV data rows: 41
- Coverage rows: 12
- Subjective rows: 11
- Choice rows: 18
- PASS coverage suites: 11
- MODULE_BOUNDARY coverage suites: 1
- BLOCKED coverage suites: 0


### franklin_2026_yimo_culture.md

# franklin 2026 一模文化线处理报告

## 范围与边界

- 范围：S038-S047，2026 各区一模。
- 输出：`worker_outputs/franklin_2026_yimo_culture_entries.csv` 与本报告。
- 边界：未修改最终 Word，未修改其他 worker 文件；选择题严格按“题干+可靠答案键”处理，主观题只采细则/评标/阅卷/讲评给分口径。

## 覆盖结论

| 套卷 | 覆盖状态 | 文化主观题 | 文化选择题/错肢 | 说明 |
|---|---|---|---|---|
| S038 2026海淀一模 | PASS | 第16题 | MODULE_BOUNDARY | 第16题按 B 类等级细则支持写入“文化功能”；当前缓存未见文化选择题题干。 |
| S039 2026西城一模 | PASS + BLOCKED | 第16题 | 第2题 BLOCKED | 第16题全民阅读入法有正式细则；第2题有题干但缺可靠答案键。 |
| S040 2026东城一模 | PASS | 第16题、第20题 | 第2题 PASS | 第16题优秀文艺、第20题生态文明传统智慧均有分题细则；第2题有题干与答案表。 |
| S041 2026朝阳一模 | PASS | 第16题 | 第3、4题 PASS | 农历智慧有阅卷细则；春节科普+非遗、中非人文交流均有题干与答案表。 |
| S042 2026丰台一模 | PASS + BLOCKED | 第16题 | 第4、6题 BLOCKED | 第16题 AI 与人文精神有等级细则；第4、6题答案键可补源，但当前文化线文本缓存缺完整题干。 |
| S043 2026延庆一模 | PASS | 第16题 | 第4题 PASS | 第16题赓续城市文脉有评分细则；第4题登记文化错肢“创新是文化发展根本动力”。 |
| S044 2026房山一模 | PASS + BLOCKED | 第16（1）题 | 第3题 BLOCKED | 第16（1）题为跨模块消费角度中的文化新业态；第3题答案键可补源但缺当前文化线题干文本。 |
| S045 2026石景山一模 | PASS + BLOCKED | 第17（1）题 | 第4题 PASS；第5题 BLOCKED | 中医药文化主观题入 B 类；第5题非遗题题干可见但同 bundle 答案键冲突。 |
| S046 2026门头沟一模 | PASS | 第16题 | 第4、12题 PASS | 永定河古渠文化角度有明确“1分、最多3分、结合材料1分”；选择题有题干与答案表。 |
| S047 2026顺义一模 | PASS + BLOCKED | 第16题、第21题 | choice_screen BLOCKED | 第16题文化功能为 B 类，第21题传统智慧双创为 2 分文化角度；选择题缺可靠答案键。 |

## 关键阻塞

- S039 西城一模第2题：题干可见，但 bundle 未提供可靠选择题答案键。
- S042 丰台一模第4、6题：overnight 可补答案键，但本轮文化线 bundle 未提供完整机器可读题干，需读 cached rendered page images 后才能转 PASS。
- S044 房山一模第3题：答案键可由 overnight 补源确认，但当前文化线 bundle 没有完整题干文本。
- S045 石景山一模第5题：非遗题题干可见，但同一 bundle 内第5题答案键出现 D/B 冲突，暂不写正确项链。
- S047 顺义一模文化选择题信号可见，但当前 bundle 缺可靠选择题答案表。

## 处理原则落实

- 没有把参考答案冒充细则：S044 房山第16（1）题标为 A-跨模块；S045 石景山第17（1）题标为评分参考/等级细则支持；S045 第17（2）题因知识限定为创新思维，列 MODULE_BOUNDARY。
- 没有把哲学链当文化链：S043 延庆第4题只登记文化错肢，不把正确项中的哲学链改写为文化正确项。
- 选择题未满足“题干+可靠答案键”的均写 BLOCKED，不硬凑 PASS。


### harvey_2024_culture.md

# harvey 2024 culture worker report

## Scope

- Run directory: `C:\bp_sync_visible\reports\culture_all_suites_rerun_2026-04-29`
- Assignment: S001-S015, all 2024 suites.
- Write scope honored: only `worker_outputs\harvey_2024_culture_entries.csv` and this report.
- Rule applied: cache-first. I used each roster `bundle_path` first; when bundle text was scan-only or incomplete, I recorded the rendered-image/supplement boundary instead of upgrading weak evidence.

## Framework

Entries use the user culture framework:

0. 载体
1. 特点
2. 作用
3. 横向
4. 纵向
5. 建设文化强国，树立文化自信
6. 民族精神
7. 坚持习近平文化思想

Subjective rows were admitted only when the evidence was a formal rubric, marking summary, evaluation PPT, lecture scoring source, or the provided prior复核 table classified the item as A/B. Reference-only material is marked as a boundary or blocker.

## Suite Coverage

| suite_id | suite_name | status | culture handling |
| --- | --- | --- | --- |
| S001 | 2024海淀一模 | PASS | Choice 1/4 and subjective 16 processed. Subjective 16 is B-level rubric support, not逐点标分. |
| S002 | 2024西城一模 | PASS | Choice 4/10 and cross-module subjective 18(3) processed. |
| S003 | 2024东城一模 | PASS | Choice 1/2/3 processed from rendered paper/key; subjective 16 formal rubric processed. |
| S004 | 2024朝阳一模 | PASS | Choice 1/2/5 and subjective 18(2) processed; 18(2) is B-level support. |
| S005 | 2024丰台一模 | PASS | Choice 1/2 and subjective 21 B-level support processed. |
| S006 | 2024石景山一模 | BLOCKED | Culture signal exists in teacher-version answer, but current evidence is reference/level only, not a formal scoring source. |
| S007 | 2024门头沟一模 | BLOCKED | Roster marks classification-bundle-supplement; objective supplement exists, but subjective culture remains reference-only boundary. |
| S008 | 2024海淀二模 | PASS | Choice 15 and subjective 21 B-level support processed. |
| S009 | 2024西城二模 | PASS | Subjective 18(4)乡村文化振兴 B-level support processed. |
| S010 | 2024东城二模 | PASS | Choice 1/2 processed from rendered paper/key; subjective 16 formal rubric and 21 B-level support processed. |
| S011 | 2024朝阳二模 | PASS | Choice 4 and subjective 19(3) formal rubric processed. |
| S012 | 2024丰台二模 | BLOCKED | Paper is rendered-ocr-needed in bundle and no culture subjective rubric was verified. |
| S013 | 2024顺义思政二模 | PASS | Choice 3/4 processed from text bundle and answer key. |
| S014 | 2024海淀期中 | MODULE_BOUNDARY | Prior复核 excludes 2024海淀期中 subjective questions from 必修四文化. |
| S015 | 2024朝阳期中 | PASS | Subjective 17 formal rubric processed. |

## Evidence Notes

- S003 and S010 objective choices used cached rendered page images because the suite bundle records the question PDFs and answer PDFs as `rendered-ocr-needed`. The CSV marks these as `objective_key_rendered`.
- S007 remains a hard boundary because the roster source is a classification bundle plus supplement; the prior文化复核 explicitly says only objective answer source was supplemented and subjective reference/level descriptions must not be promoted.
- S006 and S012 are blocked rather than forced: S006 lacks formal scoring evidence for the culture chain, and S012 does not provide enough readable objective evidence to safely certify culture choice coverage.
- S014 is a module boundary, not a failure: the prior复核 says the subjective modules are 必修2、必修3、选择性必修1, so no 必修四文化主观链 is created.

## Counts

- Suites processed: 15
- CSV rows including header: 34
- Data entries: 33
- PASS suites: 11
- MODULE_BOUNDARY suites: 1
- BLOCKED suites: 3


### hume_2026_late_culture.md

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


### linnaeus_2025_yimo_culture.md

# linnaeus_2025_yimo_culture

范围：S016-S025，2025 各区一模文化线。只处理文化主观题与文化选择题；不改最终 Word，不改其他 worker 文件。

证据边界：主观题只采用细则、评标、阅卷报告、讲评给分口径。选择题只在题干和答案键同时可靠时入表。参考答案只作答案键或题面辅助，不冒充主观题细则；哲学链不写成文化链。

## 0-7 框架覆盖

| slot | 框架 | 本批命中 |
|---|---|---|
| 0 | 载体：文化载体、文化符号、展示平台、精神标识 | S019-16 动画电影；S020-3 中国建筑；S023-16 中华版本；S025-16 哪吒/黑悟空/唐宫夜宴 |
| 1 | 特点：源远流长、博大精深 | S018-16 春节；S023-16 中华优秀传统文化特点 |
| 2 | 作用：引领风尚、教育人民、服务社会、推动发展 | S018-16 春节价值；S019-16 人民需求；S021-16 网络文艺适老化；S022-16 博物馆热；S024-5 灯会文化 |
| 3 | 横向：文化交流与传播 | S016-3 中国时节走向世界；S018-16 世界的中国年；S018-14 哪吒出海；S025-3 亚冬会冰雪文化；S025-20 小而美项目传播中华文化 |
| 4 | 纵向：继承发展、融通资源、立足时代、双创 | S017-16 诗经研学；S018-16 中国年创新；S019-16 动画电影；S021-16 网络文艺；S022-16 博物馆；S024-16 数字文旅；S025-16 哪吒等 |
| 5 | 建设文化强国，树立文化自信 | S017-16 文化认同；S018-16 春节影响力；S019-16 兜底文化强国/自信；S023-16 文化自信；S024-16 文化自信认同；S025-16 文化自信 |
| 6 | 民族精神 | S017-22 长期主义；S020-1 红色基因；S020-16 家风与民族精神；S022-20 奋斗精神 |
| 7 | 坚持习近平文化思想 | S020-16 家风建设可用角度 |

## 逐套状态

| suite_id | 套卷 | 文化主观题 | 文化选择题 | 覆盖状态 | 边界 |
|---|---|---|---|---|---|
| S016 | 2025海淀一模 | 主观题细则只列矛盾、实践认识、价值观等，未见文化主观给分口径 | Q2、Q3、Q7 有题干和答案键 | PASS | 主观题记 MODULE_BOUNDARY，选择题入文化/跨模块选择链 |
| S017 | 2025西城一模 | Q16、Q22 有细则 | 未纳入文化选择题；Q6 是逻辑题，题面虽有传统文化之美但不写文化链 | PASS | Q16 知情行；Q22 民族精神 |
| S018 | 2025东城一模 | Q16 阅卷报告逐点给分 | Q4、Q14 有题干和答案键 | PASS | Q16 中国年为本批最完整文化主观样本 |
| S019 | 2025朝阳一模 | Q16 讲评/扫描细则给分口径可用 | 未纳入文化选择题；Q4 正确项落哲学/逻辑，不写文化链 | PASS | 细则 PDF 在 bundle 为 rendered-ocr-needed，但讲评 PPT 文本给出分值口径 |
| S020 | 2025丰台一模 | Q16 阅卷细则可用 | Q1、Q3 有题干和答案键 | PASS | Q16 属等级细则，且要求核心价值观否则不能满分 |
| S021 | 2025延庆一模 | Q16 细则可用 | 未纳入文化选择题；Q6 是逻辑/创新思维题，不写文化链 | PASS | Q16 每个观点 2 分、材料 1 分 |
| S022 | 2025房山一模 | Q16(1)、Q20 跨模块文化点有细则 | Q5 有题干和答案键 | PASS | Q20 只取“中华民族精神-奋斗精神”文化给分点 |
| S023 | 2025石景山一模 | Q16 等级细则支持文化角度 | 未纳入文化选择题 | PASS | Q16 是 B 类等级细则支持，不称逐点标分 |
| S024 | 2025门头沟一模 | Q16 评分细则逐词列文化关键词 | Q5 有题干和答案键 | PASS | 文化关键词任一 1 分、文化角度最高 4 分 |
| S025 | 2025顺义一模 | Q16、Q20 跨模块文化点有细则 | Q3 有题干和答案键 | PASS | Q16 是等级细则支持；Q20 是国际合作题中的文化传播点 |

## 阻塞项

无整套 BLOCKED。局部边界如下：

- S016：没有文化主观题给分口径，主观题按 MODULE_BOUNDARY 处理；选择题可闭合。
- S019：正式细则 PDF 在 bundle 中为 rendered-ocr-needed，但同 bundle 的讲评材料已经给出 Q16 各文化点分值，可作为讲评给分口径。
- S025：教师版参考答案明示“无原始答案，此答案仅供参考”，因此 Q16 主观题不采该参考答案作细则；只采前置细则 docx 中“文化角度”给分口径。

CSV 输出：`worker_outputs\linnaeus_2025_yimo_culture_entries.csv`。

