# 劳动者-2024 独立重跑报告

运行目录：`C:\bp_sync_visible\reports\full_all_suites_independent_rerun_2026-04-29`

范围：新版 `SUITE_ROSTER.csv` 中 `year=2024` 的全部 15 套。执行规则为 cache-first，先读 roster `bundle_path`；S007 的 roster 当前已修复为分类汇编 bundle，并另有 supplemental_source 外部答案 PDF。旧 artifacts/reports 未作为历史结论来源；S007 的 supplemental PDF 是用户指定补源，仅按外部答案源记录。

## 逐套状态

| suite_id | suite_name | paper_status | answer_key_status | rubric_status | choice_status | subjective_status | blocker | 证据来源 |
|---|---|---|---|---|---|---|---|---|
| S001 | 2024海淀一模 | PASS：bundle 含试卷 PDF 文本 | PASS：答案 docx 含选择题与主观题答案 | PASS：细则 docx 含分点细则 | PASS | PASS：主观题可按细则映射材料与得分点 | 无 | bundle `2024各区模拟题__2024各区一模__2024海淀一模.md`；源：答案 docx、细则 docx、试卷 PDF |
| S002 | 2024西城一模 | PASS：bundle 含试卷 docx 文本 | PASS：答案及评分参考 docx | PASS：细则 docx 含变通与分点说明 | PASS | PASS：主观题可按评分参考/细则映射 | 无 | bundle `2024各区模拟题__2024各区一模__2024西城一模.md`；源：试卷 docx、答案 docx、细则 docx |
| S003 | 2024东城一模 | NEED_EVIDENCE：试卷 PDF 在 cache 中为 rendered-ocr-needed，bundle 主要可读内容来自细则 PPT | NEED_EVIDENCE：答案 PDF 为 rendered-ocr-needed | PASS：细则 PPT 可读，含阅卷细则与答案示例 | NEED_EVIDENCE：选择题缺可读答案 key | PASS/PARTIAL：有细则 PPT 的主观题可入，缺完整试卷 OCR 的题只保守入 | 原试卷/答案 PDF 仍需 OCR 校验 | bundle `2024各区模拟题__2024各区一模__2024东城一模.md`；源：细则 PPT；PDF 标记 rendered-ocr-needed |
| S004 | 2024朝阳一模 | PASS：bundle 含试卷 PDF 文本 | PASS：参考答案 docx | PASS：细则/讲评 PPT 含细则、答案逻辑 | PASS | PASS：主观题可按细则/讲评映射 | 无 | bundle `2024各区模拟题__2024各区一模__2024朝阳一模.md`；源：试卷 PDF、参考答案 docx、细则 PPT、讲评 PPT |
| S005 | 2024丰台一模 | PASS：bundle 含试卷 PDF 文本 | PASS：试题及答案 PDF | PASS：评分细则 docx 含“评分标准说明” | PASS | PASS：主观题可按评分标准说明映射 | 无 | bundle `2024各区模拟题__2024各区一模__2024丰台一模.md`；源：细则 docx、试题及答案 PDF、试卷 PDF |
| S006 | 2024石景山一模 | PASS：教师版带答案 docx 可读 | PASS：教师版答案可读 | REJECT：未见正式评分细则/阅卷/评标来源；PPT/教师版只能 reference-only | PASS：只可用于答案 key/选择题判断 | REJECT：主观题不能升级为细则链 | 缺正式评分来源 | bundle `2024各区模拟题__2024各区一模__2024石景山一模.md`；源：教师版带答案 docx、讲评 PPT |
| S007 | 2024门头沟一模 | NEED_EVIDENCE：roster bundle_path 已修复并可读，但 cache_status 为 classification-bundle-supplement，非完整套卷 bundle | NEED_EVIDENCE：supplemental_source PDF 存在但 pypdf 提取 0 字，为扫描型；分类汇编含部分答案摘录 | REJECT：未找到正式评标/阅卷/评分来源 | NEED_EVIDENCE：分类汇编可做题目索引，答案 key 需 OCR 校验 | REJECT：主观题只能 reference-only，不能升级细则 | 补源 PDF 需 OCR 或人工校验；无正式细则 | roster bundle `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_suite_bundles\2024各区模拟题__其他材料__202404各区一模试题分类_按模块.md`；补源 `C:\bp_sync_visible\reports\overnight_2026-04-25\downloaded_evidence\2024_mentougou_yimo_with_answers.pdf` |
| S008 | 2024海淀二模 | PASS：bundle 含 docx 与 PDF 试卷文本 | PASS：答案 docx | PASS：细则 docx | PASS | PASS：主观题可按细则映射 | 无 | bundle `2024各区模拟题__2024各区二模__2024海淀二模.md`；源：答案 docx、细则 docx、试卷 docx/PDF |
| S009 | 2024西城二模 | PASS：bundle 含试卷 docx 文本 | PASS：答案及评分参考 docx | PASS：细则 docx | PASS | PASS：主观题可按细则映射 | 无 | bundle `2024各区模拟题__2024各区二模__2024西城二模.md`；源：试卷 docx、答案 docx、细则 docx、选择题讲评 |
| S010 | 2024东城二模 | NEED_EVIDENCE：试卷 PDF 在 cache 中为 rendered-ocr-needed | NEED_EVIDENCE：答案 PDF 为 rendered-ocr-needed | PASS：逐题阅卷总结/评分细则 docx、PPT 可读 | NEED_EVIDENCE：选择题缺可读 answer key | PASS/PARTIAL：主观题可从逐题细则入，但题干仍需 OCR 对照 | 原试卷/答案 PDF 需 OCR 校验 | bundle `2024各区模拟题__2024各区二模__2024东城二模.md`；源：16-21题阅卷总结/评分细则文件 |
| S011 | 2024朝阳二模 | PASS：bundle 含试卷 PDF 文本 | PASS：参考答案 docx | PASS：主观题阅卷总结 PDF 含评分细则 | PASS | PASS：主观题可按阅卷总结映射 | 无 | bundle `2024各区模拟题__2024各区二模__2024朝阳二模.md`；源：试卷 PDF、参考答案 docx、细则 PDF |
| S012 | 2024丰台二模 | NEED_EVIDENCE：试卷 PDF 在 cache 中为 rendered-ocr-needed，但细则含主观题题干 | PASS：细则 docx 含参考答案 | PASS：评标/评分标准说明 docx | NEED_EVIDENCE：选择题缺可读 paper/key | PASS：主观题可按评标细则映射 | 完整试卷 OCR 仍需补 | bundle `2024各区模拟题__2024各区二模__2024丰台二模.md`；源：细则 docx；试卷 PDF 标记 rendered-ocr-needed |
| S013 | 2024顺义思政二模 | PASS：bundle 含试卷 docx 文本 | PASS：参考答案可读 | NEED_EVIDENCE：文件名为细则，但正文主要为参考答案/答案示例，未见稳定分点评分细则 | PASS：可按题目与答案 key 做基础判断 | NEED_EVIDENCE：主观题不能按正式细则升级，只可 reference-only 或待评分来源 | 缺正式评分细则 | bundle `2024各区模拟题__2024各区二模__2024顺义思政二模.md`；源：试卷 docx、参考答案/细则 docx |
| S014 | 2024海淀期中 | NEED_EVIDENCE：试卷 PDF cache 文本仅 470 字，题干主要来自细则 PDF | NEED_EVIDENCE：未见独立完整答案 key | PASS：细则 PDF 含评分细则、评阅说明 | NEED_EVIDENCE：选择题缺完整 key | PASS/PARTIAL：有细则的主观题可入，需补完整试卷对照 | 完整试卷文本不足 | bundle `2024各区模拟题__2024各区期中__2024海淀期中.md`；源：细则 PDF、试卷 PDF |
| S015 | 2024朝阳期中 | PASS：bundle 含试卷 PDF 文本 | PASS：评标/细则文件含阅卷前参考答案 | PASS：评标 docx 与细则 rtf 含评分细则、答案变通说明 | PASS | PASS：主观题可按评标/细则映射 | 无 | bundle `2024各区模拟题__2024各区期中__2024朝阳期中.md`；源：评标 docx、细则 rtf、试卷 PDF |

## Fallback 记录

- S007：新版 roster `bundle_path` 已修复为 `2024各区模拟题__其他材料__202404各区一模试题分类_按模块.md`，该 bundle 可读，但 `cache_status=classification-bundle-supplement`，按合同单独说明证据边界，不能当完整套卷细则。
- S007：检查 supplemental_source `2024_mentougou_yimo_with_answers.pdf`，文件存在，但 `pypdf` 对前 6 页提取文本均为 0 字，判定为扫描型答案 PDF。因未找到正式评标/阅卷/评分来源，相关主观题保持 `REJECT` 或 `NEED_EVIDENCE`，不升级为评分细则。
- S003/S010/S012/S014：cache 已显示试卷或答案 PDF 为 `rendered-ocr-needed` 或文本不足；只对细则/评标来源中已可读、可映射的主观题做 PASS，选择题或缺题干处标 `NEED_EVIDENCE`。

## 审核边界

- 普通参考答案、教师版答案、分类汇编答案只标 reference-only，不作为正式 rubric。
- S006、S007、S013 的主观题没有正式评分/阅卷/评标证据支撑，不进入正式细则链。
- 高风险词已按源文约束处理；未见明确细则支撑时不写入 `knowledge_point`，只在 `risk_note` 中提示。

## 汇总

- 处理套数：15
- entries 输出：`worker_outputs\2024_entries.csv`
- entry status 计数：PASS 30；NEED_EVIDENCE 3；REJECT 2
- 主要阻塞：S007 补源 PDF 扫描型且无正式评分来源；S003/S010 原试卷/答案 PDF OCR 未完成；S012/S014 完整试卷或选择题 key 不足；S006/S013 缺正式评分细则。
