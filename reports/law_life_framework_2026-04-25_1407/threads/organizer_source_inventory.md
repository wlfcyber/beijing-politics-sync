# Organizer Source Inventory

## Scope read

角色：资料组织者 / Organizer。

本轮只盘点当前运行目录与用户给定 PDF 的源材料状态，读取并核对：

- `SOURCE_LEDGER.csv`
- `COVERAGE_MATRIX.csv`
- `sources\pdf_text_by_page.md`
- `sources\page_images`
- `sources\contact_sheets`

写入范围严格限定为本文件：

- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\threads\organizer_source_inventory.md`

证据边界：

- 不引入、不发明外部来源。
- 只把当前 PDF 识别为“用户给定旧课件/学生版拷贝 PDF”及其渲染、抽取文本。
- PDF 中出现的题目截图、答案样式、细则字样、教师批注，只能作为课件内部材料状态记录；未获得官方答案、官方评分细则、阅卷报告或用户确认前，不可登记为官方评分细则。

## Files inspected

| 文件或目录 | 当前状态 |
| --- | --- |
| `SOURCE_LEDGER.csv` | 仅有表头：`suite_id,year,district,stage,file_path,file_type,source_type,question_range,status,notes`；无已登记来源。 |
| `COVERAGE_MATRIX.csv` | 仅有表头：`suite_id,question,book_module,question_type,evidence_source,status,artifact_location,decision_reason,next_action`；无已登记覆盖项。 |
| `sources\pdf_text_by_page.md` | 35 页 PyMuPDF 文本抽取；多页 OCR/编码质量差，p4、p16、p22 无可抽取文本，需以页面图像为主证据。 |
| `sources\pdf_text_by_page.json` | 存在，作为逐页文本结构化副本；本轮主要读取 markdown 版本。 |
| `sources\page_images` | 存在 `page_01.png` 至 `page_35.png`，共 35 张页面渲染图。 |
| `sources\contact_sheets` | 存在 `contact_sheet_1.png`、`contact_sheet_2.png`，用于总览页面结构和手写批注。 |
| `threads\framework_architect_findings.md` | 已存在的框架架构师报告，作为同一 PDF 的结构交叉参考；本轮不修改。 |

## Findings

### 1. 总体来源状态

当前运行目录中的核心源材料只有一份用户给定 PDF 及其派生件：

- 原 PDF：路径在 `pdf_text_by_page.md` 中记录为 `C:\Users\Administrator\Desktop\班课进度选必二法律与生活 原文件学生版 拷贝.pdf`，当前文本层显示为乱码路径但可对应同一用户给定 PDF。
- 派生文本：`sources\pdf_text_by_page.md` / `.json`。
- 派生图像：`sources\page_images\page_01.png` 至 `page_35.png`。
- 总览图：`sources\contact_sheets\contact_sheet_1.png`、`contact_sheet_2.png`。

该 PDF 是混合型旧课件材料，不是单一类型的试卷包。内部包含：

- 考情分析和备考建议；
- 《选必二 法律与生活》知识框架和课堂板书；
- 北京高考、海淀、西城、东城等题目截图或题目材料；
- 部分答案示范或“细则样式”页面；
- 大量红蓝手写课堂批注、圈画和学生作答/教师批改痕迹。

### 2. 页面类型判定

| 页码 | 主要类型 | 可登记性质 | 备注 |
| --- | --- | --- | --- |
| p1 | 考情 | 课件-考情分析 | 以 2024 北京高考相关案例引入《法律与生活》考查方式；不是完整真题来源。 |
| p2 | 考情 / 题例 | 课件-考情分析 / 题例截图 | 出现 2025 海淀期末、2024 海淀期末等题例信息；不是完整套卷。 |
| p3 | 考情 / 题例 / 课堂批注 | 课件-题例截图 | 东城期末等材料，带蓝色批注；可作为题型观察，不可当官方答案。 |
| p4 | 题例 / 答案样式 | 课件-题例截图 | 文本层无字；图像显示西城一模等材料和答案区。需人工/OCR复核。 |
| p5 | 考情 / 框架总论 | 课件-框架 | 明确“法条基础 + 法治意义”的考查总入口。 |
| p6 | 备考建议 | 课件-备考建议 | 包括阅读教材、掌握法律语言、积累疑难杂症、刷选择、总结意义模板等。 |
| p7-p8 | 知识框架 / 法治意义 | 课件-知识框架 | 经济、社会、权利、秩序、平衡、法治、公平正义、德治法治等意义维度。 |
| p9-p13 | 知识框架 | 课件-知识框架 | 民事法律关系、民事权利体系、合同、知识产权、违约责任等。 |
| p14-p16 | 主观题示范 / 答案样式 / 课堂批注 | 课件-主观题训练 | 东城一模合同诉状训练、学生作答或批改、答案/细则样式；不得登记为官方评分细则。 |
| p17-p21 | 知识框架 / 课堂批注 | 课件-知识框架 | 侵权、归责、举证责任、责任承担、侵权边界、相邻关系等；部分页有批注和例题截图。 |
| p22-p23 | 主观题示范 / 答案样式 / 课堂批注 | 课件-主观题训练 | p22 文本层无字；图像显示西城期末污染侵权题及答案样式。p23 为东城期末滑梯案，圈画和批注明显。 |
| p24-p27 | 知识框架 / 主观题示范 | 课件-知识框架 / 题例截图 | 家庭、继承、赡养、夫妻财产；p25-p26 有东城/西城题例与答案方向。 |
| p28-p29 | 知识框架 | 课件-知识框架 | 企业与劳动者、消费者、企业之间，不正当竞争等。 |
| p30-p31 | 主观题示范 / 答案样式 / 课堂批注 | 课件-主观题训练 | 海淀一模虚拟数字人案、西城二模食品安全/消费者权益案；大量圈画批注。 |
| p32-p34 | 知识框架 / 课堂批注 | 课件-知识框架 | 多元纠纷解决、调解、仲裁、诉讼角色、两审终审、上诉期限等。 |
| p35 | 主观题示范 / 答案样式 / 课堂批注 | 课件-主观题训练 | 社区纠纷“三聚焦”材料及知识角度表格，含批注；不可登记为官方评分细则。 |

### 3. 分类汇总

考情：

- p1-p5 为核心考情区。
- 可登记为“课件-考情分析/题例观察”，状态建议为 `reference-only`。
- 不可登记为“真题套卷覆盖完成”，因为 PDF 只截取或引用题例，不是完整试卷包。

备考建议：

- p6 为明确备考建议页。
- 可登记为“课件-备考建议”，状态建议为 `reference-only`。

知识框架：

- p5、p7-p13、p17-p21、p24、p27-p29、p32-p34 是主要知识框架页。
- 可登记为“课件-知识框架”，用于迁移框架结构和触发链候选。
- 其中 p17-p21 侵权部分结构较完整，可作为后续 mapper 的高优先级框架骨架。

主观题示范：

- p14-p16、p22-p23、p25-p26、p30-p31、p35 属于主观题训练、题例截图、答案方向或学生作答/教师批改材料。
- 可登记为“课件-主观题训练/题例截图”，状态建议为 `reference-only` 或 `needs-verification`。
- 若后续需要纳入 coverage matrix，应以“题例观察”登记，不应直接登记为已验证真题题号或评分规则。

评分细则：

- 当前未发现可独立确认的官方评分细则。
- p16、p22、p30-p31 等页面存在答案/细则样式、采分点圈画或表格，但来源身份未独立验证。
- 建议登记为“answer-like / rubric-like in courseware, not official rubric”，状态为 `needs-verification` 或 `source-missing`，下一步需寻找原套卷官方答案、评分细则、阅卷报告或由用户确认其权威性。

课堂批注：

- p3、p5-p13、p14-p17、p19-p21、p23-p24、p26-p35 均可见红蓝手写批注或圈画。
- 这些批注可用于识别教师强调的材料触发点、易错点和框架迁移方向。
- 批注不能替代官方评分细则，也不能作为“标准答案唯一依据”。

### 4. 台账登记建议

`SOURCE_LEDGER.csv` 当前为空。建议主线程新增以下候选行，具体 CSV 写入由主线程完成：

```csv
suite_id,year,district,stage,file_path,file_type,source_type,question_range,status,notes
law_life_old_courseware_2026-04-25,unknown,mixed,courseware,"C:\Users\Administrator\Desktop\班课进度选必二法律与生活 原文件学生版 拷贝.pdf",pdf,courseware_framework,p1-p35,reference-only,"用户给定旧课件/学生版拷贝；含考情、备考建议、知识框架、题例截图、答案样式和课堂批注；不是官方套卷或评分细则。"
law_life_old_courseware_text_2026-04-25,unknown,mixed,derived,"sources\pdf_text_by_page.md",markdown,extracted_text,p1-p35,ocr-needed,"PyMuPDF文本抽取；多页乱码/低文本，p4/p16/p22无可抽取文本；需结合页面图像。"
law_life_old_courseware_images_2026-04-25,unknown,mixed,derived,"sources\page_images",png_rendered_pages,pdf_page_images,p1-p35,included,"35张页面渲染图，是低文本页和手写批注核对的主证据。"
law_life_old_courseware_contact_sheets_2026-04-25,unknown,mixed,derived,"sources\contact_sheets",png_contact_sheets,page_overview,p1-p35,included,"2张contact sheet，用于页面类型总览和批注密度核对。"
```

建议不要为 PDF 内部提到的“北京高考、海淀期末、西城一模、东城期末”等分别建立正式 district suite，除非后续找到对应完整原卷、官方答案或评分材料。当前最多可在 notes 中记录“PDF 内引用题例来源名称”。

### 5. 覆盖矩阵登记建议

`COVERAGE_MATRIX.csv` 当前为空。建议先登记模块级覆盖，不登记具体真题题号，避免把题例截图误当成完整题源：

```csv
suite_id,question,book_module,question_type,evidence_source,status,artifact_location,decision_reason,next_action
law_life_old_courseware_2026-04-25,p1-p5,考情分析,courseware_reference,courseware_pdf_pages,reference-only,sources/page_images/page_01.png; sources/page_images/page_05.png,"考情和题例观察来自旧课件，不是完整官方题源。","主线程可合并为考情背景；后续用正式题库验证。"
law_life_old_courseware_2026-04-25,p6,备考建议,courseware_reference,courseware_pdf_page,reference-only,sources/page_images/page_06.png,"备考建议来自教师课件，可作为迁移说明，不作为题目证据。","可合并进框架使用说明。"
law_life_old_courseware_2026-04-25,p7-p13,民事法律关系/合同/知识产权,framework_reference,courseware_pdf_pages,reference-only,sources/page_images/page_07.png,"知识框架较完整，但未由真题评分细则验证。","交给框架/mapper线程转为候选触发链。"
law_life_old_courseware_2026-04-25,p14-p16,合同主观题训练,main-question-example,courseware_pdf_pages,needs-verification,sources/page_images/page_14.png,"含题例、学生作答/批改、答案或细则样式；不能认定为官方评分细则。","查找对应东城一模原卷及官方答案/评分细则。"
law_life_old_courseware_2026-04-25,p17-p23,侵权责任,framework_and_example,courseware_pdf_pages,needs-verification,sources/page_images/page_17.png,"侵权知识框架完整，p22-p23含题例与答案样式；官方性未确认。","框架可先合并；题例和采分点需官方材料确认。"
law_life_old_courseware_2026-04-25,p24-p27,家庭/继承/赡养/夫妻财产,framework_and_example,courseware_pdf_pages,needs-verification,sources/page_images/page_24.png,"含知识框架和东城/西城题例方向；不是完整套卷。","后续查找对应原题和权威答案。"
law_life_old_courseware_2026-04-25,p28-p31,劳动/消费者/不正当竞争/知识产权,framework_and_example,courseware_pdf_pages,needs-verification,sources/page_images/page_28.png,"含框架、海淀一模和西城二模题例批注；不能当官方评分细则。","框架可作候选；题例需补源。"
law_life_old_courseware_2026-04-25,p32-p35,多元纠纷解决/仲裁/诉讼/基层治理,framework_and_example,courseware_pdf_pages,needs-verification,sources/page_images/page_32.png,"知识框架加社区纠纷题例和答案样式；来源权威性未确认。","合并为框架候选，另查正式题源。"
```

### 6. 证据使用建议

可直接用于迁移的内容：

- 旧课件的框架结构：法条基础 + 法治意义。
- 模块目录和课堂板书：民事法律关系、权利体系、合同、知识产权、侵权、家庭继承、劳动消费者市场经营、多元纠纷解决。
- 教师批注中的材料识别习惯：圈主体、行为、损害、因果关系、权利、程序角色、意义词。

需要降级使用的内容：

- PDF 内的题例截图：只作为题例线索，不作为完整试卷覆盖。
- PDF 内答案样式和“细则”样式：只作为课堂答案示范或疑似采分结构，不作为官方评分细则。
- 手写批注：只作为教师强调点或课堂方法线索，不作为权威答案来源。

需要补源后才能正式入库的内容：

- 北京高考、海淀、西城、东城等具体题目的完整题干、题号、答案、评分细则或阅卷报告。
- 当前 PDF 中疑似官方答案/细则页面的出处证明。

## Merge candidates

建议主线程合并以下组织结论：

1. 将当前 PDF 作为一个总来源登记：`law_life_old_courseware_2026-04-25`，来源类型为 `courseware_framework`，状态为 `reference-only`。
2. 将页面图像和 contact sheets 作为该 PDF 的派生证据登记，状态可为 `included`；文本抽取登记为 `ocr-needed`，因为文本层乱码和无文本页较多。
3. 在 coverage matrix 中先按模块级页面范围登记，不按具体 district/question 登记，避免制造虚假题源覆盖。
4. 对 p14-p16、p22-p23、p25-p26、p30-p31、p35 标注 `needs-verification`：这些页面可为主观题示范和材料触发链提供线索，但不得直接当作官方评分细则。
5. 将 p7-p13、p17-p21、p24、p27-p29、p32-p34 交给框架/mapper 线程作为“候选知识框架”处理，后续必须用正式题源和评分依据验证。
6. 将 p6 备考建议合并为迁移说明，不进入题目覆盖统计。

## Blockers

1. `SOURCE_LEDGER.csv` 和 `COVERAGE_MATRIX.csv` 当前均为空，主线程尚未登记任何来源或覆盖项。
2. 当前只见用户给定 PDF 及其派生文本/图像，未见完整 district 原卷、官方答案、评分细则、阅卷报告或用户确认的权威评分材料。
3. `pdf_text_by_page.md` 文本质量较差，多处乱码；p4、p16、p22 无可抽取文本。页面图像能支撑分类，但若要抽取具体题干/答案，需要进一步 OCR 或人工复核。
4. PDF 内有“答案/细则样式”材料，但官方性无法确认。证据边界要求不得将其登记为官方评分细则。
5. PDF 内引用多个年份、区县和考试阶段，但多为题例截图或课堂材料混排；当前无法拆分为可靠的独立套卷来源。

## Decision: needs-merge

理由：

当前源材料状态已经盘点清楚，页面类型可支持主线程登记 source ledger 和 coverage matrix 的初始候选；但台账和覆盖矩阵尚未实际合并，且关键题例/答案/细则仍缺少官方来源验证。因此本轮资料组织结论为 `needs-merge`，不是最终通过。

建议主线程下一步：

1. 按本报告“台账登记建议”新增 courseware 和 derived sources。
2. 按本报告“覆盖矩阵登记建议”新增模块级 coverage rows。
3. 明确标注所有答案/细则样式页为 `needs-verification`，不要登记为 official rubric。
4. 另行寻找或等待用户提供对应区县原卷、官方答案、评分细则或阅卷报告后，再提升题例和主观题采分点的证据等级。
