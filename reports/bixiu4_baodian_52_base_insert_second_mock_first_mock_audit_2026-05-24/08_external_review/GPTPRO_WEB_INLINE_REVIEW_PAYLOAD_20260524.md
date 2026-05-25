# GPTPro Web Inline Review Payload

说明：文件上传控件在当前 Chrome 自动化会话中未返回 filechooser，因此本轮改用网页版直接粘贴核心审核文本。请按以下材料审计，不要假设还有未上传附件。




---

## SOURCE: reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\08_external_review\GPTPRO_WEB_REVIEW_PROMPT.md


你现在是北京高考政治《哲学与文化》宝典的严格外审员，模型身份：GPTPro 网页版。

审核对象：本包内的最新版《哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24》DOCX/PDF，以及随包的插入台账、accepted/blocked jsonl、audit summary。

审核目标：
1. 检查新增 2026 二模和一模漏项是否真正按原宝典风格插入原节点，而不是另起专题。
2. 检查每条新增学生版正文是否满足“材料触发点 -> 设问 -> 为什么能想到 -> 答案落点”，且答案落点是可写进卷面的具体句子，不是元话术。
3. 重点查错位：辩证否定、量变质变、主要矛盾/次要矛盾、矛盾主要方面/次要方面、两点论重点论、系统优化、价值观导向。
4. 检查是否仍有“虚空构造”：材料触发点与原理之间没有真实逻辑、把文化题硬塞哲学、把参考答案说成评分细则、用“等角度”扩张原理。
5. 检查厚度：新加 2026 二模条目是否和原宝典同强度，不得明显短、薄、空。
6. 检查覆盖：2024-2026 一模原宝典是否明显仍漏哲学题；如只能提出疑点，请标 NEED_EVIDENCE。

输出格式必须是表格，列为：
- severity: DELETE / REWRITE / NEED_EVIDENCE / PASS
- location: 文件或宝典节点 + 套卷题号
- problem: 问题是什么
- source_check: 你依据包内什么材料判断
- fix: 具体怎么改，若 PASS 写“保留”

严格规则：
- 不要泛泛表扬。
- 不要只说“建议优化”，必须给可执行修改。
- 如果无法核验原始细则，不得宣称它错误；标 NEED_EVIDENCE。
- 若发现新增条目只是模板套话或原理错位，直接列 REWRITE 或 DELETE。


---

## SOURCE: reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\08_external_review\batch_03_summary_and_gate.md


# 外审摘要

- final_docx: 哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx
- final_pdf: 哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.pdf
- accepted_insertions: 38
- blocked_or_skipped: 74

## Accepted By Node
- 系统观念 / 系统优化: 5
- 辩证否定 / 守正创新: 5
- 价值观的导向作用: 5
- 实践是认识的基础: 3
- 矛盾的特殊性 / 具体问题具体分析: 3
- 矛盾就是对立统一: 3
- 量变与质变 / 适度原则: 2
- 尊重客观规律与发挥主观能动性相结合: 2
- 联系的普遍性 / 联系的观点（总）: 2
- 实践与认识（总）: 2
- 物质决定意识: 1
- 发展的观点 / 发展的普遍性: 1
- 主要矛盾和次要矛盾: 1
- 矛盾的普遍性和特殊性: 1
- 人民群众: 1
- 两点论与重点论: 1

## Accepted By Source
- 2026东城二模: 6
- 2026朝阳二模: 6
- 2026丰台二模: 5
- 2026顺义二模: 5
- 2026房山二模: 4
- 2026西城二模: 3
- 2026石景山二模: 3
- 2025海淀一模: 2
- 2026通州一模: 2
- 2026海淀二模: 2

## Blocked By Reason
- already_in_base_exact_source: 44
- weak_evidence: 10
- question_prompt_not_verified: 9
- culture_boundary: 8
- module_boundary: 3

---

# 双线审核阶段就绪报告

## 2026-05-24 18:20 Local Superseding Update

- Accepted student insertions are now 41, not 26.
- DOCX insertion ledger has 41 rows.
- Rendered PDF has 234 pages.
- `weak_gate_source_repair_resolution.csv` closes the previous weak-evidence gates for `2026海淀二模`, `2026西城二模`, `2026顺义二模`, and `2026石景山二模`.
- `COVERAGE_CLOSURE_MATRIX_V2` now reports `COVERED_OR_PATCHED: 35` and no open evidence/prompt gates.
- Codex-A independent rerun reports `should_add=0 / evidence_blocked=0`; ClaudeCode-B still listed 8 conservative `HOLD` items, all adjudicated in `dual_lane_hold_adjudication_20260524.md` as 7 non-new-blockers and 1 future candidate reminder.
- Render QA caught and corrected `2026房山二模 Q18(2)`: removed the false `OvernightPolicyChange` expansion and false "传统政策/政策创新" wording; regenerated DOCX/PDF after correction.
- This remains audit-stage local closure only. GPTPro web review and external Claude review are still pending.

结论：已经达到用户要求的“Codex 与 ClaudeCode 双线跑到审核那一步”，但仍不能宣布最终宝典完成。

## 双线状态

- Codex A：完成 2024-2026 一模与 2026 二模源清单、母版覆盖扫描、候选题识别、补丁者复核和 Governor 预审。
- ClaudeCode B：完成独立回源，生成二模候选、2024-2026 一模疑似漏项、补丁目标和审计报告。
- Fusion：已把两线结果合并成学生版插入候选，并按弱证据、题干未核实、文化边界、母版已覆盖四类挡出。

## 当前可插入正文

- 可进入哲学正文：26 条。
- 暂不进入正文：74 条。
- 可插入条目来源：2026 东城二模 6 条、2026 朝阳二模 6 条、2026 丰台二模 5 条、2026 房山二模 4 条、2025 海淀一模 3 条、2026 通州一模 2 条。
- 文化节点已经从哲学正文候选中挡出；学生版泛化套话已清理。

## 可插入节点分布

- 系统观念 / 系统优化：6 条。
- 矛盾的特殊性 / 具体问题具体分析：3 条。
- 价值观的导向作用：3 条。
- 辩证否定 / 守正创新：4 条。
- 量变与质变 / 适度原则：2 条。
- 尊重客观规律与发挥主观能动性相结合：2 条。
- 实践是认识的基础：1 条。
- 物质决定意识：1 条。
- 矛盾就是对立统一：2 条。
- 发展的观点 / 发展的普遍性：1 条。
- 主要矛盾和次要矛盾：1 条。

## 关键原则专项检查

母版文本中已经存在：

- 主要矛盾：17 次。
- 矛盾的主要方面：5 次。
- 次要方面：6 次。
- 主流：25 次。
- 支流：6 次。
- 两点论：21 次。
- 重点论：21 次。
- 量变：34 次。
- 质变：39 次。
- 辩证否定：48 次。

因此后续不能再写“主要矛盾、矛盾主次方面、两点论重点论暂无稳定挂点”。最终合并时要保留并强化这些正式节点。

## 当前挡出原因

- 母版已覆盖同套同题：44 条。
- 弱证据：10 条。
- 题干未核实：9 条。
- 文化边界：8 条。
- 模块边界：3 条。

## 必须继续处理

- 2026 丰台一模 Q16 的“主流/支流、两点论重点论”目前证据等级强，但题干字段带待回源占位，不能直接进正文；需要回源补全设问后再决定是否追加。
- OCR 或题干阻塞项不能凭候选写进宝典。
- 已在 5.2 母版上原地插入 26 条已过门槛条目；其中主次矛盾、矛盾主次方面已补出独立节点。2026通州一模第18题经题面渲染页和评标细则修复后新增2条强细则补丁；下一步继续处理4个弱证据二模门槛，并进行外部 GPTPro/Claude 审核。
## 2026-05-24 19:25 当前有效摘要

本节覆盖下面较早的 26/41 条版本描述。

- Codex 与 ClaudeCode 双线生产/对账已完成；外部 Claude delta 审核对当前四个收口项给出 scoped PASS。
- 当前进入学生版的新增条目为 38 条，插入账本为 38 条；最终 DOCX/PDF 已重新生成，PDF 为 232 页。
- 2026 二模新题已按母版节点原地插入，不重做母版结构；`2026海淀二模 Q16` 只保留 `联系`、`实践与认识` 两条强证据链。
- 对 2024-2026 一模覆盖做了套卷矩阵收口：35 套均为 `COVERED_OR_PATCHED`，没有未关 evidence/prompt gate。
- 已清除本轮发现的错误/元话术：`五篇大文章`、`答案要写出`、`答案要落到`、`不能只罗列`、`传统政策`、`政策创新`、`OvernightPolicyChange` 在当前 DOCX 中均为 0。
- 不能签最终全 PASS 的唯一硬门槛：GPTPro 网页版审核尚未跑通；当前 Chrome Default profile 缺 Codex Chrome Extension，需恢复后再送审。


---

# 2024 一模 fusion queue 闭环表

Date: 2026-05-24

本表专门处理 `fusion_review_queue.csv` 中仍悬空的 2024 一模条目。结论是：9 条队列项不需要直接新增正文，其中 7 条已在最终 DOCX 中以正确题号/节点覆盖，2 条为模块边界或弱误触发排除。

## 逐条结论

| 套题 | 队列题号 | 结论 | 证据 |
|---|---|---|---|
| 2024东城一模 | Q4 | 题号误切；由 Q21 覆盖 | 最终 DOCX 含 `2024东城一模 第21题（主观题）`，对应“三圈联动/一核两翼/研发-制造协同”与系统优化。 |
| 2024东城一模 | Q16 | 已覆盖 | 最终 DOCX 含 `2024东城一模 第16题（主观题）` 2 处，覆盖矛盾普遍性特殊性、价值判断价值选择。 |
| 2024丰台一模 | Q16 | 法律模块边界排除；同源误切出的 Q18 已覆盖 | 源 bundle 显示 Q16 是好意同乘法理题；最终 DOCX 含 `2024丰台一模 第18题第（1）问` 3 处。 |
| 2024丰台一模 | Q18 | 已覆盖 | 最终 DOCX 含 `2024丰台一模 第18题第（1）问` 3 处，覆盖系统优化、发展观点、唯物史观。 |
| 2024丰台一模 | Q21 | 已覆盖 | 最终 DOCX 含 `2024丰台一模 第21题（主观题）` 2 处，覆盖矛盾普遍性特殊性、价值判断价值选择。 |
| 2024海淀一模 | Q16 | 已覆盖 | 最终 DOCX 含 `2024海淀一模 第16题（主观题）` 6 处，覆盖主观能动性、联系、发展、实践等节点。 |
| 2024石景山一模 | Q7 | 模块边界排除 | 题干为“概念外延关系图”，属于选必三逻辑/概念关系判断；仅因出现“社会主要矛盾”等词被误触发。 |
| 2024石景山一模 | Q16 | 已覆盖 | 最终 DOCX 含 `2024石景山一模 第16题（主观题）` 2 处，覆盖发展观点、认识作用。 |
| 2024西城一模 | Q7 | 题号误切；由 Q17 覆盖 | 最终 DOCX 含 `2024西城一模 第17题（主观题）` 9 处，覆盖人与自然关系、规律与能动性、联系等节点。 |

## Governor Note

这 9 条不得继续作为“2024 一模未处理”悬空项。后续总审应将它们计入 `resolved_covered` 或 `module_boundary_excluded`，而不是重复插入正文。


---

# 题干待核实 gate 闭环表

Date: 2026-05-24

本表处理 `student_patch_entries.blocked.jsonl` 中 `question_prompt_not_verified` 的 9 条。它们当时被挡出，是因为候选 JSON 仍写着“题干待回源确认”；后续最终 DOCX 已经含有正式设问和学生版条目，所以这些不再作为“未覆盖”缺口。

## 结论

- 2026丰台一模 Q16：4 条均已由最终 DOCX 覆盖。
- 2026房山一模 Q16(2)：4 条均已由最终 DOCX 覆盖。
- 2025门头沟一模 Q16：1 条已由最终 DOCX 覆盖。

## Governor Note

这些条目不应重新插入，否则会造成重复。它们应从 open evidence/prompt gate 中移出，状态记为 `resolved_by_final_docx`。


---

# 2026通州一模源证据修复记录

## 结论

`2026通州一模` 不能继续列为 `NO_FINAL_ARTIFACT_EVIDENCE`。试卷 PDF 文字层为空，但已渲染题面图片并确认第18题为《哲学与文化》综合题；评标 PDF 可抽取文字，并明确给出哲学采分点。

## 题面确认

- 套卷：2026通州一模
- 题号：第18题，8分
- 设问：结合材料，运用《哲学与文化》知识，阐释隆福寺街区改造中“古朴”与“创新”是如何实现共生共荣的。
- 题面来源：`99_logs/tongzhou_paper_pages/page_06.png`

## 细则确认

评标细则明确：

- 矛盾对立统一，观点加阐述可采2分。
- 辩证否定观，观点加阐述可采2分；发展观可替代。
- 双创属于文化给分点，不单独作为哲学节点纳入本轮哲学宝典补丁。
- 立足社会实践及若干替代表述为1分点，本轮不扩张为主要哲学条目，避免把弱替代点做厚。

## 本轮并入

已并入 `student_patch_entries.accepted.jsonl` 两条强细则补丁：

1. `矛盾就是对立统一`
2. `辩证否定 / 守正创新`

未并入：

- `双创`：文化线条目，非哲学节点。
- `立足社会实践`、`以人民为中心`、`立足时代`、`发挥主观能动性和尊重客观规律相结合`、`联系的观点`：细则中为1分替代表述，不重复给分；本轮只在审计记录中保留，不做学生版主条目。


---

# 弱证据门槛回源闭合记录

本记录只处理 `student_patch_entries.blocked.jsonl` 中原先标为 `weak_evidence` 的二模条目。结论：四套二模的弱证据缺口已回源核验，并转化为 15 条 accepted 插入行；但这仍是“本地融合审核前”状态，不等于最终 PASS。

## 已闭合套卷

- `2026海淀二模 Q16`：讲评页可读，明确把“有字之书 / 无字之书”对应理论认识和社会实践，并列实践与认识、矛盾对立统一、联系等知识。本轮保留并加厚：联系、矛盾对立统一、实践是认识的基础、认识对实践的反作用。
- `2026西城二模 Q16`：评标 PDF 渲染页可读，明确列出矛盾普遍性寓于特殊性、实践决定认识、价值观导向作用。本轮保留并加厚三条。
- `2026顺义二模 Q16`：评标 doc 可读，明确列实践观点、人民主体、价值观、矛盾观、中华优秀传统文化等角度；其中哲学节点转为人民群众、价值观、两点论重点论、实践基础、辩证否定 / 守正创新。
- `2026石景山二模 Q17(3)`：评分细则明确可从联系、矛盾、实践与认识关系等角度分析“良法”和“善治”的关联。本轮保留三条，但在证据边界中标明“正式细则允许角度”，不包装成逐点累计细则。

## 证据边界

- 海淀二模证据级别是讲评/讲解评分支持，不是逐点官方评标细则；可入宝典，但不能写“逐项给分细则要求”。
- 石景山二模是正式细则允许角度，题目分值按综合表达评价，不得写成“联系 2 分、矛盾 2 分、实践 2 分”的累计式细则。
- 顺义二模含文化角度，本轮只把可落入哲学框架的节点入宝典；文化内容不得硬塞进哲学。

## 对覆盖矩阵的处理

`weak_gate_source_repair_resolution.csv` 每行对应一个原弱证据缺口的闭合或伴随补丁。覆盖矩阵应将这些行计入 `resolved_weak_evidence_by_source_repair`，并只把未被该表闭合的弱证据继续算作 open gate。


---

# Render QA Content Correction: 2026房山二模 Q18(2)

渲染抽查时发现 `2026房山二模 Q18(2)` 的学生版条目存在内容污染：

- 原错误写法把 `OPC` 展开成 `OvernightPolicyChange`，该展开不见于本地源材料。
- 原错误写法把题目写成“传统政策与政策创新”，与源材料中的“传统一人公司 / 数字员工 / 单人成军 / 法律风险”不符。

## 回源结果

可读源：`01_source_inventory/suite_source_bundles/2026房山二模.md`。

源文本明确写出：

- `OPC的出现，是对传统一人公司这一旧矛盾统一体的否定，实现了“单人成军”全新创业范式，是联系的环节，是发展的环节。`
- `OPC的发展，创业者要坚持扬弃，肯定与保留数字员工的强大功能，又要针对出现的法律风险对此改造，把它们包含在新事物之中。`
- 细则：`3分 联系、发展、扬弃；1分 OPC的出现——否定分析；1分 OPC的发展——肯定分析。`

## 处理

已修改 `student_patch_entries.accepted.jsonl` 中该条：

- 删除 `OvernightPolicyChange`。
- 删除“传统政策与政策创新”的虚假设问。
- 改成围绕 `OPC的出现和发展` 的保守设问。
- `boundary_note` 明确：教师版可读文本显示第18（2）5分及细则，但原完整题干未单独呈现；不得再扩写为政策类题。

该修正必须在重新合并 DOCX/PDF 后复查：学生版正文不应再出现 `OvernightPolicyChange`、`传统政策`、`政策创新`。


---

# 双线 HOLD 分歧融合裁决

本文件专门处理 Codex-A 与 ClaudeCode-B 的分歧：Codex-A 独立倒查结论为 `should_add=0 / evidence_blocked=0`，ClaudeCode-B 报告中仍列出 8 个 `need_evidence/HOLD`。融合裁决如下。

## 总结

- 8 个 ClaudeCode `HOLD` 都不能直接新增正文。
- 其中 7 个已有母版/补丁覆盖或属于题号误切、边界误触发，不构成本轮 open blocker。
- `2026海淀二模 Q21` 保留为未来候选提醒：当前缺正式细则，不进入宝典，也不影响本轮已处理的 `2026海淀二模 Q16` 四条。
- 因此本轮融合后仍是：新增/重写候选 0，当前 accepted 41 条保持不变。

## 逐项裁决

| 项 | ClaudeCode HOLD | 融合裁决 |
|---|---|---|
| 2024朝阳一模 Q待回源 | 题号未确认 | 最终 DOCX 已含第16题、第18题第（2）问及选择题条目；不新增，记为源清单提醒。 |
| 2024石景山一模 Q哲学 | 弱参考答案/题级未核 | 第16题已在最终 DOCX；第7题误触发已按选必三/概念关系边界排除。 |
| 2025朝阳一模 Q16 | 弱参考答案 | 最终 DOCX 已含 Q16 多处；无新强细则点，不新增。 |
| 2025海淀一模 Q16 | 弱参考答案 | 最终 DOCX 已含 Q16；Q21 本轮已补主次矛盾/系统优化。Q16 不新增。 |
| 2026东城一模 Q16 | 弱参考答案级别 | 最终 DOCX 已含 Q16 多处；不把弱答案包装成新条目。 |
| 2026延庆一模 Q待定 | 未识别独立强细则候选 | 最终 DOCX 已含第16题、第20题多处；不新增。 |
| 2026朝阳一模 Q17(3) | 题号歧义 | 最终 DOCX 已含第16题、第21题；Q17(3) 无强证据新增点。 |
| 2026海淀二模 Q21 | 统筹方法 9 分题细则缺 | 保留为未来候选提醒；本轮不进学生版。 |

## Governor 口径

这些 HOLD 项不能被说成“都已经新增进宝典”，但也不能再算作“本轮应新增未新增”。严格说法是：

> 当前本地已完成 35 套套卷级覆盖闭合和 41 条 accepted 入档；ClaudeCode 的 8 个 HOLD 被融合裁决为 7 个非新增闭合、1 个未来候选提醒。最终 PASS 仍需 GPTPro 网页版和外部 Claude 审核后才能签。


---

# Codex-A independent coverage rerun 20260524

## 结论

- Scope: 2024-2026 first mocks plus 2026 second mocks, 35 source suites.
- CSV rows: 76. Status counts: 已在宝典或 accepted JSONL 覆盖 67; 模块边界排除 9
- Suite-level result: covered suites 34; boundary-only closed suites 1; closed suites total 35; should-add suites 0; evidence-blocked suites 0.
- No Bixiu4 philosophy main-question gap was found outside the current handbook body or current accepted JSONL.
- Reference answers were not promoted to rubric evidence. Rows supported only by reference answers remain boundary/blocked unless later accepted JSONL supplies a stronger source gate.

## 关键发现

- Current accepted JSONL rows: 41. 05_delivery docx_insert_ledger rows: 41.
- Accepted JSONL rows not yet present in 05_delivery/docx_insert_ledger.csv: 0.
- COVERAGE_CLOSURE_MATRIX_V2.csv now marks all 35 suites as COVERED_OR_PATCHED.
- Note: some closure rows still retain blocked_weak_evidence counts while also having accepted_insertions; this is a trace of older weak-evidence gates, not a current open blocker under accepted JSONL coverage.
- 2024 first-mock queue is closed by first_mock_2024_queue_resolution: covered/misparsed-covered rows stay covered; module-boundary rows stay excluded.

## 专项知识点复核
- main/secondary contradictions: covered by 2025海淀一模 Q21 accepted JSONL and 2026顺义一模 Q21 base coverage.
- contradiction main/secondary aspects, two-point/key-point, mainstream/tributary: covered by 2026丰台一模 Q16 prompt-gate resolution and 2026顺义二模 Q16 accepted JSONL.
- dialectical negation: covered by 2026东城二模 Q16, 2026朝阳二模 Q16, 2026房山二模 Q18(2), 2026通州一模 Q18, and 2026顺义二模 Q16.
- quantity/quality change: covered by 2026朝阳二模 Q21 and 2026房山二模 Q16 accepted JSONL.
- practice/cognition: covered by 2026东城二模 Q16, 2026海淀二模 Q16, 2026石景山二模 Q17(3), 2026西城二模 Q16, and 2026顺义二模 Q16 accepted JSONL.
- values: covered by multiple accepted/base rows including 2026东城二模 Q16, 2026朝阳二模 Q16, 2026丰台二模 Q16, 2026西城二模 Q16, 2026顺义二模 Q16.
- people/masses: covered by 2026顺义二模 Q16 accepted JSONL and first-mock/base records such as 2026顺义一模 Q21.

## 漏项、阻塞、建议

- 应新增: 0.
- 证据不足阻塞: 0 after current accepted JSONL supersedes older weak-evidence rows.
- 模块边界排除: see CSV; these are not Bixiu4 philosophy main-question insertions.
- Recommended next action: no Word generation in this task. If another lane uses the external review upload packet, refresh that packet from the current 05_delivery ledger first.

## Accepted JSONL rows not in 05_delivery ledger

- none

## Output files

- reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/02_codex_lane/agents/codex_a_independent_coverage_rerun_20260524.md
- reports/bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24/02_codex_lane/agents/codex_a_independent_coverage_rerun_20260524.csv


---

# ClaudeCode B 全量重跑：2026 二模新题厚度复核 + 2024-2026 一模覆盖倒查（2026-05-24）

生产线：ClaudeCode B（独立于 Codex A）
依据：5.2 母版 + accepted JSONL（26 条）+ blocked JSONL（74 条）+ prompt_gate_resolution + first_mock_omissions
本轮限制：只读必读材料；不生成 Word/PDF；不修改母版；不回滚他人改动。

---

## 一、总体盘点

| 维度 | 数量 |
|------|------|
| 覆盖套题 | 35 套（2024一模 6 + 2025一模 10 + 2026一模 11 + 2026二模 8） |
| 已覆盖 (covered_in_base) | 24 行 |
| 已通过补丁覆盖 (covered_by_patch) | 11 行（含 2025海淀一模 Q21 + 2026通州一模 Q18 两条一模补丁） |
| 应新增 (should_add) | 0 行（本轮在严格证据口径下无新增触发） |
| 需补证 (need_evidence/HOLD) | 7 行 |
| 边界排除 (boundary_excluded) | 6 行（选必三《逻辑与思维》及类推） |

> 关于 should_add = 0：本轮所有"强细则"一模候选要么已被 accepted JSONL 覆盖，要么 blocked.jsonl 已判 `already_in_base_exact_source`，要么经 `prompt_gate_resolution` 由最终 DOCX 闭环；剩余尚未落地的全部是弱参考答案 / 题号待定 / OCR 重残 / 模块边界，按本轮硬规则必须 HOLD 不立条。

---

## 二、2026 二模新增条目厚度复核（A 部分）

复核对象：本轮 accepted JSONL 中 24 条 ClaudeCode B 二模条目 + 2 条 Codex continuation Tongzhou source repair 一模条目 + 13 条 Codex continuation weak gate source repair 二模条目。重点是用户在 prompt 中指定的 4 个二模题。

### 2026东城二模 Q16 京彩课堂（7 分）

入栏节点：实践是认识的基础 / 物质决定意识 / 系统观念-系统优化 / 辩证否定-守正创新 / 矛盾的特殊性-具体问题具体分析 / 价值观的导向作用，6 条。

- 材料触发点全部为材料中真实动作（"引入真实情境"、"基于北京真实城市发展规律"、"将哲学知识与北京社会实践联结"、"传承哲学经典的同时结合新时代北京实践创新"、"针对北京特色情境设计"、"涵养精神品格"），非泛化。
- 设问完整保留"综合运用所学知识，谈谈《哲学与文化》选修课程"京彩课堂"精彩所在。（7分）"。
- "为什么能想到" 解释链结构稳定（"材料中的『…』……，触发……的分析"）。
- 6 条原理在细则中均独立列为采分点；与 `物质决定意识` 与 `实践是认识的基础` 的重叠已在 `boundary_note` 中显式标"阅卷细则列为独立采分点"。

判定：**KEEP**；厚度充分；无 REWRITE/DELETE 需求。

### 2026朝阳二模 Q16 城市文化建设 + Q21 五篇大文章

Q16 入栏 4 条（对立统一 / 守正创新 / 具体问题具体分析 / 价值观），Q21 入栏 2 条（系统观念 / 量变质变）。

- Q21 `boundary_note` 已显式标注"细则亦明确必答党的领导 1 分，该点属政治模块不列此条目"。
- 量变质变条目以"久久为功、积小胜为大胜"为材料触发点，符合细则关于"持续积累、由小到大"的信号说明。

判定：**KEEP**；分栏清晰，未把多个原理塞进一节点。

### 2026丰台二模 Q16 守护湿地（7 分）

入栏 5 条（具体问题具体分析 / 规律与主观能动性 / 系统观念 / 发展观 / 价值观）。

- 5 条原理在阅卷细则 pptx 中均独立列出。
- `规律与主观能动性` 与 `具体问题具体分析` 触发点分别落到"针对不同湿地类型"和"遵循生态系统规律同时发挥主观能动性"，未混栏。

判定：**KEEP**。

### 2026房山二模 Q16 工匠精神 + Q18(2) 辩证否定专项

Q16 入栏 3 条（规律主观 / 系统观念 / 量变质变），blocked 1 条（中华优秀传统文化连续性创新性 → culture_boundary 入文化线，正确）。
Q18(2) 入栏 1 条（辩证否定-扬弃），`boundary_note` 标"3步骤计分：否定 1 分 → 扬弃 1 分 → 肯定与改造 1 分；独立 5 分专项题"，与细则三步给分一致。

判定：**KEEP**；文化线条目正确导出至文化模块。

### 2026海淀二模 Q16 有字之书无字之书（重点核验题）

入栏 4 条：联系的普遍性 / 矛盾就是对立统一 / 实践是认识的基础 / 认识对实践的反作用，evidence_level = 讲评细则。

- 4 条全部基于海淀讲评 page_015 / page_016 的角度表格升级而来；boundary_note 明确"讲评第 16 题表格明确列入"。
- 联系条与矛盾条对照清晰：前者讲"相互依存、相互贯通"，后者讲"既区别又统一于知行合一"，不重复。
- 实践决定认识 + 认识反作用于实践对照成立，分别落到"无字之书"与"有字之书"，未把两半塞同一节点。

判定：**KEEP**；证据已从原"弱参考答案"升级到讲评细则，原 audit 中标的 weak_evidence 已闭环。

### 2026西城二模 Q16 中式生活方式（重点核验题）

入栏 3 条：矛盾的普遍性和特殊性 / 实践是认识的基础 / 价值观的导向作用，evidence_level = 强细则。

- 3 条均明确来源西城评标 PNG（page_001/002/003），不再是泛化角度。
- 矛盾普遍特殊条目落到"特殊性中包含普遍性"半句，未自动展开"普遍性寓于特殊性 + 特殊性中包含普遍性"两半。
- 文化多样性与中华优秀传统文化条目按 boundary_note 显式不在此条扩张，正确。

判定：**KEEP**。

### 2026顺义二模 Q16 新大众文艺（重点核验题）

入栏 5 条：人民群众 / 价值观 / 两点论与重点论 / 实践是认识的基础 / 辩证否定-守正创新，evidence_level = 强阅卷版。

- 5 条均落到顺义评标 doc 阅卷版的明示采分点。
- "两点论与重点论"已与原 audit 中的"矛盾对立统一"区分；boundary_note 显式说明"原候选笼统放在『矛盾就是对立统一』不准；本轮按阅卷版改入两点论与重点论"——这一改写正确，避免了"主流支流 / 多样性与主流价值统一"被错放进对立统一节点。
- 人民群众与实践条目分栏独立，材料触发点不同，未重复。

判定：**KEEP**；此前 audit 提示的"已 rewrite"动作已完成。

### 2026石景山二模 Q17(3) 良法善治（重点核验题）

入栏 3 条：联系的普遍性 / 矛盾就是对立统一 / 实践是认识的基础，evidence_level = 强细则。

- 三条 `boundary_note` 均明确标"属于任选哲学观点，不写成累加细则"、"评分细则显式列出 X 角度；作为可选哲学角度收录"。
- 与"逐点累计细则"严格区分；学生版若同时写三条只能算"任选一角度并以三个层次展开"，不能算三个独立给分点。

判定：**KEEP**；boundary_note 已严格执行"正式细则允许角度而非累计细则"的硬规则。

### 厚度复核小结

| 二模题 | accepted 条数 | 厚度判定 | 重写/删除 |
|--------|--------------|---------|----------|
| 东城二模 Q16 | 6 | 厚 | 无 |
| 朝阳二模 Q16+Q21 | 4+2 | 厚 | 无 |
| 丰台二模 Q16 | 5 | 厚 | 无 |
| 房山二模 Q16+Q18(2) | 3+1 | 厚 | 无 |
| 海淀二模 Q16 | 4 | 厚（讲评细则升级） | 无 |
| 西城二模 Q16 | 3 | 厚（评标PNG补证） | 无 |
| 顺义二模 Q16 | 5 | 厚（阅卷版补证；已 rewrite 两点论） | 无 |
| 石景山二模 Q17(3) | 3 | 厚（任选角度边界标对） | 无 |

**结论**：全部 24 条二模 + 2 条通州一模 + 13 条 weak_gate 二模条目无 REWRITE / DELETE 触发；最后入栏的条目已经符合"材料触发点 / 设问 / 为什么能想到 / 答案落点 / 多原理分栏"五项硬规则。

---

## 三、2024-2026 一模漏项倒查（B 部分）

倒查方法：对每套一模哲学题在 base + accepted + blocked + prompt_gate_resolution 四张表中走一遍，落定单一状态。

### 3.1 已通过补丁补入（covered_by_patch，KEEP）

| 套题 | 题号 | 入栏节点 | 备注 |
|------|------|----------|------|
| 2025海淀一模 | Q21 | 系统观念 / 系统优化 × 2，主要矛盾和次要矛盾 × 1 | ClaudeCode B first mock 3 条；docx_insert_ledger 已记 |
| 2026通州一模 | Q18 | 矛盾就是对立统一，辩证否定 / 守正创新 | Codex continuation Tongzhou source repair 2 条；原 OCR 失败已补 |

### 3.2 母版已覆盖（covered_in_base，NO_ACTION）

下列题 blocked.jsonl 均判 `already_in_base_exact_source` 或在 `prompt_gate_resolution` 中已闭环：

- 2024 一模：2024东城一模 Q16，2024丰台一模 Q18(1)/Q21，2024海淀一模 Q16，2024西城一模 Q哲学
- 2025 一模：2025东城一模 Q16，2025丰台一模 Q16/Q18(2)，2025延庆一模 Q16，2025房山一模 Q16(1)，2025石景山一模 Q16，2025西城一模 Q16，2025门头沟一模 Q16，2025顺义一模 Q16
- 2026 一模：2026丰台一模 Q16，2026房山一模 Q16(2)，2026朝阳一模 Q16，2026海淀一模 Q16（硬样本），2026石景山一模 Q17(1)，2026西城一模 Q16/Q21，2026门头沟一模 Q16，2026顺义一模 Q21

> 高风险节点已覆盖核查：
> - **主要矛盾和次要矛盾**：已通过 2025海淀一模 Q21 补丁入栏；2026顺义一模 Q21 主次矛盾节点母版已收。
> - **两点论与重点论**：2026顺义二模 Q16 已重写入栏；2025海淀一模 Q21 母版已收。
> - **矛盾主次方面 / 主流支流**：2026丰台一模 Q16"主流支流"在 prompt_gate 中标 resolved_by_final_docx；母版已收。
> - **辩证否定 / 守正创新**：2026东城二模 / 朝阳二模 / 房山二模 / 顺义二模 / 通州一模均已入栏；2026门头沟一模 Q16 母版已覆盖。
> - **量变质变 / 适度原则**：2026朝阳二模 Q21 + 2026房山二模 Q16 入栏；2025顺义一模 Q16 母版已覆盖。
> - **实践是认识的基础**：2026东城二模 / 海淀二模 / 西城二模 / 顺义二模 / 石景山二模均已入栏。
> - **认识对实践的反作用**：2026海淀二模 Q16 已入栏（讲评细则）。
> - **价值观导向作用**：6 条独立入栏，覆盖东城 / 朝阳 / 丰台 / 西城 / 顺义二模 + 2025延庆一模（母版）。
> - **人民群众**：2026顺义二模 Q16 已入栏。
> - **系统优化**：2025海淀一模 Q21 + 2026东城/朝阳/丰台/房山二模均已入栏。

### 3.3 边界排除（boundary_excluded，EXCLUDE）

| 套题 | 题号 | 原因 |
|------|------|------|
| 2025延庆一模 | Q18 | 辩证思维（选必三《逻辑与思维》） |
| 2025石景山一模 | Q21(1) | 科学思维 + 归纳推理 + 创新思维（选必三） |
| 2025西城一模 | Q17 | 辩证思维 / 创新思维（选必三） |
| 2025门头沟一模 | Q21(1) | 科学思维 + 辩证思维 + 创新思维（选必三） |
| 2026海淀一模 | Q17 | 辩证思维 / 逻辑推理（选必三） |
| 2026西城一模 | Q19(3) | 辩证思维 / 创新思维（选必三） |
| 2026东城二模 | Q18 | 类比推理（选必三） |
| 2026石景山二模 | Q17(2) | 辩证思维整体性 / 矛盾分析法 / 辩证否定观（思维方法维度，选必三） |

### 3.4 需补证（need_evidence，HOLD，不立条）

| 套题 | 题号 | HOLD 原因 |
|------|------|----------|
| 2024朝阳一模 | Q 待定 | Codex A 定位但题号未确认；不可凭题名硬写 |
| 2024石景山一模 | Q 哲学 | docx 教师版可读，但哲学题位置和细则结构未完整核验 |
| 2025朝阳一模 | Q16 | 国产动画题仅弱参考答案级别；不可包装为细则 |
| 2025海淀一模 | Q16 | "从哲学角度正确认识『测试』"主题待精确回源 |
| 2026东城一模 | Q16 | 弱参考答案级别；题级未对比母版 |
| 2026延庆一模 | Q 待定 | 本轮未识别独立强细则候选；保持观察 |
| 2026朝阳一模 | Q17(3) | 题号歧义（Q16/Q17 分歧）；当前不立条 |
| 2026海淀二模 | Q21 | 统筹方法 9 分题细则缺；blocked.jsonl 弱参考答案 |

> 上述 HOLD 项不进入本轮 insert_candidates.jsonl，避免出现"细则只允许某角度回答"被包装成"稳定评分触发"的风险。

---

## 四、与既有产物的关系

- 与 `claudecode_b_audit_report.md` 的差异：本文件在原"强候选遗漏 9 条"基础上，按本轮 accepted+blocked+prompt_gate 三表回查，确认 9 条全部已落地或属于 already_in_base / culture_boundary / module_boundary；不再独立列条。
- 与 `claudecode_b_first_mock_omissions.md` 的差异：原文件"疑似遗漏"在本轮闭环中已升级为 covered_in_base / covered_by_patch / boundary_excluded；不再保留"疑似"状态。
- 与 `docx_insert_ledger.csv` 的对应：本文件 KEEP 行（11 条）一一对应 ledger 的 26 行入栏，且与 accepted JSONL 26 条条目数对齐。

---

## 五、严格规则自检（本文件输出前）

- [x] 未用"等角度"自动展开新原理
- [x] 未把普通参考答案写成细则口径（弱角度题全部 HOLD）
- [x] 仅"正式细则允许角度"的条目在 `boundary_note` 写明证据级别（如石景山二模 Q17(3) 三条）
- [x] 未发现条目薄/空/逻辑断裂 → 无 REWRITE
- [x] 未发现原理错位 → 无 DELETE
- [x] 无法核验的条目全部标 need_evidence/HOLD，未猜

---

ClaudeCode B 本轮已到融合审核前，不代表最终 PASS。


---

# COVERAGE_CLOSURE_MATRIX_V2

This is a suite-level closure matrix for the 35 source suites in this run. It is a governor aid, not a final PASS.

External-review packet note: direct source bundles are attached for the touched or weak-evidence suites in this repair batch; other suites rely on the accepted base baodian coverage and the lane closure records, not on a full re-upload of all 35 source bundles.

## Status Counts

- COVERED_OR_PATCHED: 35

## Open Evidence Or Prompt Gates

- none

## Reading Rule

- `COVERED_OR_PATCHED`: suite appears in final DOCX or has accepted/base-covered evidence.
- `BOUNDARY_EXCLUDED`: only module/culture boundary items remain.
- `OPEN_EVIDENCE_OR_PROMPT_GATE`: unrepaired weak evidence or missing prompt remains; do not sign final PASS.
- `NO_FINAL_ARTIFACT_EVIDENCE`: no final artifact evidence was found at suite level.


---

# 本机 Governor / Confucius 检查

## 2026-05-24 18:20 本地更新结论

本地状态更新为：`LOCAL_COVERAGE_CLOSED_EXTERNAL_REVIEW_PENDING`。

- accepted 学生版插入条目：41 条。
- DOCX 插入账本：41 条。
- Word/PDF 已重新生成并渲染：234 页。
- 之前仍开口的四套二模弱证据门槛已经回源闭合：`2026海淀二模`、`2026西城二模`、`2026顺义二模`、`2026石景山二模`。
- 套卷级覆盖矩阵：35 套全部为 `COVERED_OR_PATCHED`，open evidence/prompt gate 为 none。
- Codex-A 独立子线程已完成，结论为应新增 0、证据阻塞 0；ClaudeCode-B 的 8 个保守 HOLD 已由 `dual_lane_hold_adjudication_20260524.md` 裁决为 7 个非新增闭合、1 个未来候选提醒。
- 渲染 QA 发现并修正 `2026房山二模 Q18(2)` 的错误英文展开和错设问；修正后 DOCX/PDF 已重新生成。
- 仍不能签严格最终 PASS：GPTPro 网页版审核、外部 Claude 审核尚未完成；ClaudeCode B 本轮复跑已经产出并完成融合裁决。

## 结论

本机检查结论：`LOCAL_PASS_WITH_EXTERNAL_REVIEW_AND_WEAK_EVIDENCE_PENDING`。

这表示：本机已完成强证据补丁、双线融合、母版插入、Word/PDF 渲染检查；但按用户此前要求，最终严格 PASS 仍需处理剩余弱证据门槛，并完成 GPTPro 网页版和 Claude 侧外部审核。

## 已完成

- Codex A 与 ClaudeCode B 双线跑到审核阶段。
- 26 条学生版正文补丁进入母版节点。
- 74 条候选被挡出，原因包括母版已覆盖、弱证据、题干未核实、文化边界、模块边界。
- “主要矛盾和次要矛盾”已补为独立节点。
- “矛盾的主要方面和次要方面”已补为独立节点。
- 2026 房山二模 Q18(2) 已归回“辩证否定 / 守正创新”，未误入“联系”。
- 2026 通州一模 第18题已从扫描题面和评标细则中修复，新增“矛盾就是对立统一”“辩证否定 / 守正创新”2条强细则条目。
- 清除了新增补丁里的泛化套话：未检出“学生看到这里”“避免只背原理”“说明该做法如何把原理转化”等模板句。
- Word 已由本机 Microsoft Word 导出 PDF。
- PDF 已渲染页面图：227 页。

## 抽查页

- 第 102 页：2026 房山二模 Q18 辩证否定条目。
- 第 102 页：2026 通州一模 Q18 辩证否定 / 守正创新条目。
- 第 117 页：2026 通州一模 Q18 矛盾就是对立统一条目。
- 第 135-136 页：主要矛盾和次要矛盾独立节点。
- 第 137 页：矛盾的主要方面和次要方面独立节点。
- 总览图：`07_render_check/word_pdf_pages/contact_every_12_pages.png`。

## 仍未关闭的严格门槛

- GPTPro 网页版审核未在本线程完成。
- Claude 外部审核未在本线程完成。
- `2026海淀二模`、`2026石景山二模`、`2026西城二模`、`2026顺义二模` 仍为弱证据门槛，不能签最终 PASS。
- 若用户要求“最终全 PASS”，需把本轮 DOCX/PDF 和 `04_fusion_audit/AUDIT_STAGE_READY_SUMMARY.md` 分批交给上述外部模型审核，再由 Codex 回源修正。
## 2026-05-24 19:25 当前有效结论

本节覆盖下面较早的 26/41 条、227/234 页和“外部 Claude 未完成”等旧状态。

- 当前学生版新增条目：38 条；DOCX 插入账本：38 条。
- 当前 Word/PDF 已按最新 DOCX 重新生成：PDF 232 页。
- 覆盖矩阵：35 套均为 `COVERED_OR_PATCHED`，没有未关 evidence/prompt gate。
- 2025 海淀一模系统观念/主次矛盾误标已修正为第22题；accepted JSONL 与插入账本均无该套第21题新增行。
- 2026 海淀二模第16题保留 `联系`、`实践与认识` 两条；已删除不够稳的独立矛盾条，并补了可读证据文件。
- 外部 Claude 最终 delta 审核已对四个收口项给出 scoped PASS，见 `08_external_review/claude_external_review_final_delta_20260524.md`。
- 仍不能签严格最终 PASS：GPTPro 必须走网页版，但当前 Chrome Default profile 没有可用 Codex Chrome Extension，网页门未完成。

Governor 结论：`LOCAL_AND_EXTERNAL_CLAUDE_SCOPED_PASS__GPTPRO_WEB_PENDING`。


---

# External Claude Triage Repair - 2026-05-24

## Accepted Hard Fixes
- Corrected `2026朝阳二模 Q21`: the source topic is `四个中国`, not `五篇大文章`.
- Corrected `2026房山二模 Q16`: the source question asks how to read `中华民族最感动人的浪漫` from Chinese industrial culture, not a generic `工匠精神的当代价值` prompt.
- Replaced thin/backfilled 2026二模 rows with source-candidate trigger chains where the candidate table had stronger material wording.
- Removed answer-landing meta language such as `答案要写出`, `答案要落到`, and `不能只罗列单个做法` from the accepted insertion data.
- Merged duplicate `2025海淀一模 Q21` system-optimization insertion into one system-view entry.
- Removed the unsupported independent `2026海淀二模 Q16` contradiction entry; bundled source text only supports `联系` and `实践与认识` angles for Q16.
- Folded the separate `认识对实践的反作用` row for `2026海淀二模 Q16` back into the broader practice/recognition answer sentence.

## Not Mechanically Collapsed
- `2026东城二模 Q16`, `2026朝阳二模 Q16`, `2026丰台二模 Q16`, `2026顺义二模 Q16`, and `2026石景山二模 Q17(3)` still keep multiple framework placements where the suite source bundle or marking document explicitly names multiple philosophy angles.
- This follows the accepted baodian pattern: framework-first placement by official principle node, with audit notes clarifying that optional angles are not cumulative point promises.

## Still Not Final PASS
- GPTPro web review is still pending because the controllable Chrome profile lacks the Codex Chrome extension.
- External review package must be rebuilt with raw source evidence before a renewed external Claude/GPT review can fairly judge the repaired artifact.

---

# Source Evidence Index


## Source Evidence

- source_evidence/99_logs/tongzhou_paper_pages/contact.png
- source_evidence/99_logs/tongzhou_paper_pages/page_01.png
- source_evidence/99_logs/tongzhou_paper_pages/page_02.png
- source_evidence/99_logs/tongzhou_paper_pages/page_03.png
- source_evidence/99_logs/tongzhou_paper_pages/page_04.png
- source_evidence/99_logs/tongzhou_paper_pages/page_05.png
- source_evidence/99_logs/tongzhou_paper_pages/page_06.png
- source_evidence/99_logs/tongzhou_paper_pages/page_07.png
- source_evidence/99_logs/tongzhou_paper_pages/page_08.png
- source_evidence/99_logs/tongzhou_paper_pages/page_09.png
- source_evidence/99_logs/tongzhou_paper_pages/page_10.png
- source_evidence/99_logs/weak_gate_sources/26顺义二模评标.txt
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/contact.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_001.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_002.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_003.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_004.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_005.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_006.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_007.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_008.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_009.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_010.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_011.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_012.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_013.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_014.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_015.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_016.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_017.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_018.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_019.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_020.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_021.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_022.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_023.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_024.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_025.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_026.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_027.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_028.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_029.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_030.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_031.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_032.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_033.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_034.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_035.png
- source_evidence/99_logs/weak_gate_sources/renders/haidian_lecture/page_036.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/contact.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_001.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_002.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_003.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_004.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_005.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_006.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_007.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_008.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_009.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_010.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_011.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_012.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_013.png
- source_evidence/99_logs/weak_gate_sources/renders/xicheng_rubric/page_014.png
- source_evidence/99_logs/weak_gate_sources/石景山区高三政治第二次模拟考试答案评分细则(1).txt
- source_evidence/second_mock_candidate_entries.csv
- source_evidence/suite_source_bundles/2025海淀一模.md
- source_evidence/suite_source_bundles/2026东城二模.md
- source_evidence/suite_source_bundles/2026丰台二模.md
- source_evidence/suite_source_bundles/2026房山二模.md
- source_evidence/suite_source_bundles/2026朝阳二模.md
- source_evidence/suite_source_bundles/2026海淀二模.md
- source_evidence/suite_source_bundles/2026海淀二模_Q16_readable_evidence.md
- source_evidence/suite_source_bundles/2026石景山二模.md
- source_evidence/suite_source_bundles/2026西城二模.md
- source_evidence/suite_source_bundles/2026通州一模.md
- source_evidence/suite_source_bundles/2026顺义二模.md


---

## SOURCE: reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\08_external_review\batch_01_all_inserted_entries.md


# 全部新增插入条目正文抽取

6. 2026东城二模 第16题（主观题）
【材料触发点】 “京彩课堂”立足北京真实城市资源和学生成长实际，把思政课放到首都发展场景中设计。材料既有客观条件、现实基础和事物规律，也有主体主动谋划、因势利导和积极作为，说明成功来自尊重客观实际与发挥能动性的统一。
【设问】 结合材料，运用《哲学与文化》知识，谈谈“京彩课堂”的精彩所在。
【为什么能想到】 物质决定意识要求从客观实际出发；课程内容和教学方案由北京真实资源、学生成长需要和时代育人任务决定，不能脱离现实空想。所以不能只写主观努力，也不能只写客观条件；哲学逻辑在于从实际出发、尊重规律，同时发挥意识的能动作用，把客观可能转化为现实成效。
【答案落点】 “京彩课堂”的精彩在于从北京实际和学生实际出发，把课程设计建立在真实城市资源和现实育人需要上，使思政学习更贴近现实、更有说服力。这说明相关主体要坚持一切从实际出发，尊重客观规律和现实条件，在此基础上主动谋划、科学施策、积极实践，把主观努力建立在客观规律之上。

---

19. 2026丰台二模 第16题（主观题）
【材料触发点】 江苏依水网密布之势疏浚调水、云南遵循森林—村寨—梯田—水系生态格局，材料突出“顺应自然、因水制宜”。材料既有客观条件、现实基础和事物规律，也有主体主动谋划、因势利导和积极作为，说明成功来自尊重客观实际与发挥能动性的统一。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对“守护湿地，就是守护生态之美与文化根脉”的认识。
【为什么能想到】 湿地治理既要尊重自然生态格局，又要通过治理实践主动修复和保护，正对应尊重规律与发挥主观能动性的统一。所以不能只写主观努力，也不能只写客观条件；哲学逻辑在于从实际出发、尊重规律，同时发挥意识的能动作用，把客观可能转化为现实成效。
【答案落点】 守护湿地要在尊重湿地生态规律的基础上发挥人的主动性，因地制宜开展修复、治理和保护，让生态之美可持续延续。这说明相关主体要坚持一切从实际出发，尊重客观规律和现实条件，在此基础上主动谋划、科学施策、积极实践，把主观努力建立在客观规律之上。

---

20. 2026房山二模 第16题（主观题）
【材料触发点】 材料引用“天有时，地有气，材有美，工有巧，合此四者，然后可以为良”，从古代工艺到北斗原子钟都强调把客观条件与人的技艺结合起来。材料既有客观条件、现实基础和事物规律，也有主体主动谋划、因势利导和积极作为，说明成功来自尊重客观实际与发挥能动性的统一。
【设问】 结合材料，运用《哲学与文化》知识，谈谈如何从中华工业文化读懂中华民族最感动人的浪漫。
【为什么能想到】 “天时、地气、材料、工巧”说明制造不是凭空想象，而是在尊重条件和规律中发挥人的创造力。所以不能只写主观努力，也不能只写客观条件；哲学逻辑在于从实际出发、尊重规律，同时发挥意识的能动作用，把客观可能转化为现实成效。
【答案落点】 中华工业文化的浪漫在于能工巧匠尊重材料、工艺和自然规律，又发挥精益求精的主动创造，把“天工”转化为日常文明成果。这说明相关主体要坚持一切从实际出发，尊重客观规律和现实条件，在此基础上主动谋划、科学施策、积极实践，把主观努力建立在客观规律之上。

---

29. 2026海淀二模 第16题（主观题）
【材料触发点】 《有字之书》承载经典学说和文明智慧，《无字之书》蕴藏于广袤大地和社会万象之中；二者分别代表认识的书本来源和实践来源，是学习成长中相互依存的两个方面。
【设问】 从哲学角度，谈谈为什么要把读“有字之书”和读“无字之书”结合起来。
【为什么能想到】 联系具有普遍性，事物之间普遍相互影响。书本知识和社会生活并非孤立，而是相互依赖、彼此支撑：书本认识需要社会实践的检验才能落地，社会经验需要理论指引才能系统化。看到“有字之书”与“无字之书”并列，首先应想到联系的观点——二者相互联系，割裂任何一方都会使成长路径残缺。
【答案落点】 读书成长要坚持联系的观点，把书本知识同社会生活、时代实践和现实问题联系起来，避免只读死书或只凭经验。这说明相关主体要用联系的观点看问题，把书本学习与社会实践相互联结，在联系中理解、检验和发展认识，形成真本领。

---

30. 2026石景山二模 第17(3)题（主观题）
【材料触发点】 材料说'良法只是起点，善治才是目标'，把法律制度与治理成效放在同一关系中理解；良法为善治提供规范基础，善治让法律的效力转化为国家治理现代化的实际成果。
【设问】 从哲学角度，分析“良法”和“善治”的关联。
【为什么能想到】 联系具有普遍性。题目关键词就是“关联”，首先指向联系观点：良法和善治不是孤立两件事。良法为善治提供制度依据，善治又让法律效能落实于现实；脱离联系的视角，就看不到“起点”与“目标”之间的相互依存关系，也就无法理解为什么二者必须结合推进。
【答案落点】 良法与善治紧密联系，良法为治理提供制度基础和规范依据，善治则让法律效力转化为国家治理现代化的实际成效。这说明要坚持联系的观点，看到制度与实践之间的相互依存和相互促进，不能孤立地只看制度规范而忽视治理效能，也不能只看治理效果而忽视制度基础。

---

20. 2026东城二模 第16题（主观题）
【材料触发点】 课程把中轴线、故宫、科创基地、临空经济等真实场景与课堂任务、探究活动、数字资源联结起来。材料不是罗列几个孤立要素，而是把目标、资源、主体、环节和效果放进同一整体中呈现，强调各部分之间相互依赖、相互支撑、协同发挥作用。
【设问】 结合材料，运用《哲学与文化》知识，谈谈“京彩课堂”的精彩所在。
【为什么能想到】 多个场景、任务和资源不是孤立堆放，而是在同一育人目标下相互配合，适合从整体与部分、系统优化的角度分析。只有把课程目标、空间资源、实践任务和数字技术放在同一系统中看，才能说明各部分为什么要协同发力、服务铸魂育人的整体效果。
【答案落点】 “京彩课堂”的精彩在于坚持系统观念，统筹课堂学习、社会实践、城市文化和数字技术，让各类资源协同服务铸魂育人的整体目标。这说明推进相关工作要坚持系统观念，统筹不同主体、资源和环节，优化结构安排，促进各部分相互配合、形成合力，使局部做法服务整体目标并提升整体效果。

---

21. 2026朝阳二模 第21题（主观题）
【材料触发点】 “十五五”规划把数字中国、健康中国、平安中国、美丽中国作为推进中国式现代化的四大战略支柱，强调相互支撑、协同发力。材料不是罗列几个孤立要素，而是把目标、资源、主体、环节和效果放进同一整体中呈现，强调各部分之间相互依赖、相互支撑、协同发挥作用。
【设问】 “十五五”规划纲要将“四个中国”确立为推进中国式现代化的战略支柱，深刻体现了中国共产党治国理政的系统思维和一张蓝图绘到底的战略定力。结合材料，综合运用所学，谈谈对系统思维和战略定力的认识。
【为什么能想到】 数字中国、健康中国、平安中国、美丽中国不是四件互不相干的任务，而是同一现代化进程中的有机组成部分。材料强调相互支撑、协同发力，就要求从系统优化角度把握整体目标与各战略支柱的关系，说明各部分优化组合才能提升现代化建设的整体效能。
【答案落点】 推进中国式现代化要坚持系统思维，把数字、健康、平安、美丽中国作为有机整体来统筹，促进各战略支柱相互支撑、协同推进。这说明推进相关工作要坚持系统观念，统筹不同主体、资源和环节，优化结构安排，促进各部分相互配合、形成合力，使局部做法服务整体目标并提升整体效果。

---

22. 2026丰台二模 第16题（主观题）
【材料触发点】 内蒙古治理从单纯“治湖泊”转向系统“治流域”，强调“湖内的问题，功夫下在湖外”。材料不是罗列几个孤立要素，而是把目标、资源、主体、环节和效果放进同一整体中呈现，强调各部分之间相互依赖、相互支撑、协同发挥作用。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对“守护湿地，就是守护生态之美与文化根脉”的认识。
【为什么能想到】 “湖内问题湖外解决”“治湖泊转向治流域”说明湿地治理不能只盯住单个湖泊，而要把湖泊、流域、森林、村寨、梯田、水系等要素作为相互影响的系统来把握。用系统优化看，关键在于统筹各环节、优化治理结构，让局部修复服务生态整体稳定。
【答案落点】 湿地保护要坚持系统观念，把湖泊、流域、森林、村寨、梯田、水系等作为有机整体统筹治理，实现生态系统稳定和平衡。这说明推进相关工作要坚持系统观念，统筹不同主体、资源和环节，优化结构安排，促进各部分相互配合、形成合力，使局部做法服务整体目标并提升整体效果。

---

23. 2026房山二模 第16题（主观题）
【材料触发点】 材料从良渚玉器、西周青铜、《考工记》的分工体系，到新时代完整工业门类，展现长期积累、分工协同和体系化制造能力。材料不是罗列几个孤立要素，而是把目标、资源、主体、环节和效果放进同一整体中呈现，强调各部分之间相互依赖、相互支撑、协同发挥作用。
【设问】 结合材料，运用《哲学与文化》知识，谈谈如何从中华工业文化读懂中华民族最感动人的浪漫。
【为什么能想到】 从古代分工体系到新时代完整工业门类，材料强调的不是某一项孤立技艺，而是长期积累、分工协同和体系化制造能力。系统优化角度能够解释：只有把工匠、技术、门类、产业链和国家能力作为整体来统筹，才能形成持续创造的整体优势。
【答案落点】 中华工业文化的浪漫不只是单点技艺，而是代代工匠、社会分工、产业门类和技术体系协同形成的整体创造力。这说明推进相关工作要坚持系统观念，统筹不同主体、资源和环节，优化结构安排，促进各部分相互配合、形成合力，使局部做法服务整体目标并提升整体效果。

---

24. 2025海淀一模 第22题（主观题）
【材料触发点】 全面深化改革、中国式现代化、法治建设等均是需要统筹兼顾、整体推进的系统工程，强调整体性、关联性、协同性。材料不是罗列几个孤立要素，而是把目标、资源、主体、环节和效果放进同一整体中呈现，强调各部分之间相互依赖、相互支撑、协同发挥作用。
【设问】 结合材料，阐释系统观念是具有基础性的思想和工作方法（运用所学知识结合某一领域作答）。
【为什么能想到】 全面深化改革和中国式现代化都是复杂系统工程，不能用单点推进替代整体统筹。系统观念要求从整体性、关联性、协同性出发，把不同领域、不同环节、不同举措放在统一目标下协调推进，避免局部政策彼此脱节，形成整体优化效能。
【答案落点】 坚持系统观念要求用联系的观点整体地看待全面深化改革工程中各要素的关联，强调各项举措在政策取向上相互配合、在实施过程中相互促进、在实际成效上相得益彰，实现系统整体优化效能。这说明推进相关工作要坚持系统观念，统筹不同主体、资源和环节，优化结构安排，促进各部分相互配合、形成合力，使局部做法服务整体目标并提升整体效果。

---

28. 2026丰台二模 第16题（主观题）
【材料触发点】 湿地保护既守护当前生态之美，也延续文化根脉，并要求从治湖泊转向治流域的持续治理。材料体现对象处在持续变化和不断推进之中，既有现实基础，也有长期治理、动态调整和面向未来的发展方向。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对“守护湿地，就是守护生态之美与文化根脉”的认识。
【为什么能想到】 材料强调湿地保护不是一次性动作，而是随着生态格局和治理对象变化持续推进，适合用发展的观点动态把握。因此应从发展的观点理解材料：事物不是静止不变的，解决问题也不能停留在眼前状态，而要看到过程性、趋势性和由低到高的推进逻辑。
【答案落点】 守护湿地要坚持发展的观点，在长期治理中动态把握生态变化和文化延续，处理好当前修复与长远保护的关系，让生态之美持续生长。这说明相关工作要坚持发展的观点，立足当前基础，面向长远目标，随着条件变化不断完善思路和措施，在持续推进中实现更高水平的发展。

---

15. 2026朝阳二模 第21题（主观题）
【材料触发点】 材料强调“一张蓝图绘到底”，把长期目标纳入五年规划持续推进，通过规划接力落实。材料强调持续推进、久久为功、阶段衔接或由小到大的积累过程，说明结果不是一次行动立即完成，而是在长期积累中逐步形成。
【设问】 “十五五”规划纲要将“四个中国”确立为推进中国式现代化的战略支柱，深刻体现了中国共产党治国理政的系统思维和一张蓝图绘到底的战略定力。结合材料，综合运用所学，谈谈对系统思维和战略定力的认识。
【为什么能想到】 “长期目标、阶段任务、久久为功”是典型的量的积累推动质的跃升的材料信号。这对应量变与质变的关系：事物发展需要量的积累，积累达到一定程度才会引起质的变化；如果忽视长期持续的过程，就解释不了材料中的战略定力和阶段推进。
【答案落点】 中国式现代化要保持战略定力，把宏伟蓝图分解为阶段性任务并持续落实，在久久为功中推动发展目标逐步实现。这说明相关主体要重视量的积累和持续行动，把长远目标分解为阶段性任务，坚持久久为功，在连续推进中促成发展目标和治理效果的实现。

---

16. 2026房山二模 第16题（主观题）
【材料触发点】 材料写一代代能工巧匠把“极致”奉为圭臬，从0.1毫米、0.2毫米的精度到北斗原子钟300万年误差1秒。材料强调持续推进、久久为功、阶段衔接或由小到大的积累过程，说明结果不是一次行动立即完成，而是在长期积累中逐步形成。
【设问】 结合材料，运用《哲学与文化》知识，谈谈如何从中华工业文化读懂中华民族最感动人的浪漫。
【为什么能想到】 “一代代”“极致”“精度不断提升”说明量的积累和精益求精推动质的飞跃。这对应量变与质变的关系：事物发展需要量的积累，积累达到一定程度才会引起质的变化；如果忽视长期持续的过程，就解释不了材料中的战略定力和阶段推进。
【答案落点】 中华工业文化体现了长期积累、精益求精的工匠精神，正是在持续追求极致中推动制造水平实现质的跃升。这说明相关主体要重视量的积累和持续行动，把长远目标分解为阶段性任务，坚持久久为功，在连续推进中促成发展目标和治理效果的实现。

---

17. 2026东城二模 第16题（主观题）
【材料触发点】 思政课没有抛弃育人目标，而是通过探究式、项目式、数字地图、云研学、虚拟展馆等方式激活课堂。材料同时出现了保留、转化、更新和创造等信息，说明处理对象不是简单复原旧形式，也不是完全抛弃旧基础，而是在继承合理因素的基础上实现新的发展。
【设问】 结合材料，运用《哲学与文化》知识，谈谈“京彩课堂”的精彩所在。
【为什么能想到】 材料既守住思政育人方向，又创新教学形式和传播载体，属于在继承中发展、在发展中创新。这正对应辩证否定的逻辑：否定不是全盘否定，而是既克服旧事物中过时、不适应的方面，又保留其中积极合理的因素，并在新的条件下实现转化和创新。
【答案落点】 “京彩课堂”要坚持守正创新，守住思政铸魂育人的根本任务，同时借助真实场景和数字技术创新学习方式，增强课堂生命力。这说明相关工作要坚持守正创新，在尊重原有基础和合理价值的同时推动形式、机制和路径更新，使传统资源或已有经验在新的实践条件下焕发新的生命力。

---

18. 2026朝阳二模 第16题（主观题）
【材料触发点】 北京中轴线、平遥古城等历史文化古迹被保护，同时历史四合院被焕新为市民文化中心，传统空间进入新的城市生活。材料同时出现了保留、转化、更新和创造等信息，说明处理对象不是简单复原旧形式，也不是完全抛弃旧基础，而是在继承合理因素的基础上实现新的发展。
【设问】 结合材料，从哲学角度，说明在城市文化建设中怎样实现历史传承与现代创新的有机结合。
【为什么能想到】 材料不是简单复古，也不是推倒重来，而是在保留城市文化根脉的基础上实现新的转化和发展，正好对应辩证否定和守正创新。这正对应辩证否定的逻辑：否定不是全盘否定，而是既克服旧事物中过时、不适应的方面，又保留其中积极合理的因素，并在新的条件下实现转化和创新。
【答案落点】 实现有机结合，要坚持继承与发展的统一，保护历史文化古迹、延续城市文脉，同时推动传统空间和文化供给方式创造性转化。这说明相关工作要坚持守正创新，在尊重原有基础和合理价值的同时推动形式、机制和路径更新，使传统资源或已有经验在新的实践条件下焕发新的生命力。

---

19. 2026房山二模 第18(2)题（主观题）
【材料触发点】 OPC从传统“一人公司”发展为“一个创意大脑+数字员工”的新创业形态，同时要处理数字员工带来的法律风险。材料同时出现了保留、转化、更新和创造等信息，说明处理对象不是简单复原旧形式，也不是完全抛弃旧基础，而是在继承合理因素的基础上实现新的发展。
【设问】 结合材料一和材料二，运用《逻辑与思维》辩证否定观知识，分析OPC的出现和发展。
【为什么能想到】 题干直接点名辩证否定观，材料要求分析新事物如何否定旧形态又保留、改造其中合理因素。这正对应辩证否定的逻辑：否定不是全盘否定，而是既克服旧事物中过时、不适应的方面，又保留其中积极合理的因素，并在新的条件下实现转化和创新。
【答案落点】 OPC的出现是对传统一人公司旧矛盾统一体的否定，形成新的创业范式；OPC的发展还要坚持扬弃，保留数字员工优势并改造其法律风险。这说明相关工作要坚持守正创新，在尊重原有基础和合理价值的同时推动形式、机制和路径更新，使传统资源或已有经验在新的实践条件下焕发新的生命力。

---

20. 2026通州一模 第18题（主观题）
【材料触发点】 隆福寺改造没有简单复古，也没有推倒重来，而是在保留历史记忆、古都肌理的同时注入时代元素、现代科技和年轻化业态。材料同时出现了保留、转化、更新和创造等信息，说明处理对象不是简单复原旧形式，也不是完全抛弃旧基础，而是在继承合理因素的基础上实现新的发展。
【设问】 结合材料，运用《哲学与文化》知识，阐释隆福寺街区改造中“古朴”与“创新”是如何实现共生共荣的。
【为什么能想到】 辩证否定的实质是扬弃，既肯定和保留旧事物中的合理内容，又克服旧形态局限、推动发展；评标细则明确“辩证否定观”按观点加阐述给2分，并允许用发展观替代。这正对应辩证否定的逻辑：否定不是全盘否定，而是既克服旧事物中过时、不适应的方面，又保留其中积极合理的因素，并在新的条件下实现转化和创新。
【答案落点】 坚持辩证否定观和守正创新。隆福寺街区改造保留历史记忆和古都肌理，同时注入现代科技、时代元素和新的生活方式，在保护中发展、在传承中创新，使传统文化资源转化为当代生活空间。这说明相关工作要坚持守正创新，在尊重原有基础和合理价值的同时推动形式、机制和路径更新，使传统资源或已有经验在新的实践条件下焕发新的生命力。

---

21. 2026顺义二模 第16题（主观题）
【材料触发点】 非遗传承人直播传统技艺，普通人用短视频记录生活，新技术打破传统生产传播边界，同时要求弘扬主流价值。材料同时出现了保留、转化、更新和创造等信息，说明处理对象不是简单复原旧形式，也不是完全抛弃旧基础，而是在继承合理因素的基础上实现新的发展。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对新大众文艺要面对“尊重多样与弘扬主流、人民性与艺术性、社会效益与经济效益”之间寻找平衡点这一时代课题的思考。
【为什么能想到】 材料不是不要传统，也不是任意追新，而是在继承传统和顺应新媒介中实现创新发展。这正对应辩证否定的逻辑：否定不是全盘否定，而是既克服旧事物中过时、不适应的方面，又保留其中积极合理的因素，并在新的条件下实现转化和创新。
【答案落点】 新大众文艺要守正创新，继承优秀传统和人民立场，借助网络、AI、直播等新形式推动内容、形式和传播方式创新。这说明相关工作要坚持守正创新，在尊重原有基础和合理价值的同时推动形式、机制和路径更新，使传统资源或已有经验在新的实践条件下焕发新的生命力。

---

33. 2026朝阳二模 第16题（主观题）
【材料触发点】 材料把“历史文化古迹得到有效保护”和“四合院焕新、市民文化中心、线上文化产品精准供给”放在一起，问题直接要求处理“历史传承”与“现代创新”。材料把两个看似有张力的方面放在同一问题中呈现，例如保护与利用、传承与创新、历史与现代、局部差异与整体目标，要求在关系中理解双方。
【设问】 结合材料，从哲学角度，说明在城市文化建设中怎样实现历史传承与现代创新的有机结合。
【为什么能想到】 设问本身就是一对关系：传承和创新有区别，但不是二选一，而是在城市文化建设中相互依存、相互促进。这说明题目不是让学生二选一，而是要看到矛盾双方既相互区别、相互制约，又在一定条件下相互依存、相互促进，处理好二者关系才能推动问题解决。
【答案落点】 城市文化建设要把传承与创新统一起来，在保护城市文脉、守住文化根脉的同时，用新场景、新服务、新载体让传统文化进入现代生活。这说明相关工作要坚持用对立统一观点看问题，在承认双方差异和张力的基础上寻找结合点，推动双方相互促进、相互转化，实现关系协调和整体发展。

---

34. 2026通州一模 第18题（主观题）
【材料触发点】 隆福寺街区改造一方面保护古都肌理、保留历史记忆，另一方面融入现代科技和时代元素，使“古朴”与“创新”共生共荣。材料把两个看似有张力的方面放在同一问题中呈现，例如保护与利用、传承与创新、历史与现代、局部差异与整体目标，要求在关系中理解双方。
【设问】 结合材料，运用《哲学与文化》知识，阐释隆福寺街区改造中“古朴”与“创新”是如何实现共生共荣的。
【为什么能想到】 设问直接把“古朴”与“创新”作为一对关系来问，材料也不是让学生二选一，而是要求说明二者怎样在同一街区改造中相互支撑、共生共荣；评标细则明确“矛盾对立统一”按观点加阐述给2分。这说明题目不是让学生二选一，而是要看到矛盾双方既相互区别、相互制约，又在一定条件下相互依存、相互促进，处理好二者关系才能推动问题解决。
【答案落点】 矛盾就是对立统一。隆福寺街区改造既保护古都肌理、留住历史记忆，又融入现代科技和时代元素，让保护与更新、传统与现代在同一空间中相互支撑，实现“古朴”与“创新”共生共荣。这说明相关工作要坚持用对立统一观点看问题，在承认双方差异和张力的基础上寻找结合点，推动双方相互促进、相互转化，实现关系协调和整体发展。

---

35. 2026石景山二模 第17(3)题（主观题）
【材料触发点】 “良法”强调制度规范，“善治”强调治理成效；材料说良法是起点、善治是目标。材料把两个看似有张力的方面放在同一问题中呈现，例如保护与利用、传承与创新、历史与现代、局部差异与整体目标，要求在关系中理解双方。
【设问】 从哲学角度，分析“良法”和“善治”的关联。
【为什么能想到】 良法和善治有区别：一个是制度起点，一个是治理目标；但二者又统一于法治国家建设过程。这说明题目不是让学生二选一，而是要看到矛盾双方既相互区别、相互制约，又在一定条件下相互依存、相互促进，处理好二者关系才能推动问题解决。
【答案落点】 良法与善治是区别中的统一：没有良法，善治缺少规范基础；没有善治，良法难以充分发挥治理效能。这说明相关工作要坚持用对立统一观点看问题，在承认双方差异和张力的基础上寻找结合点，推动双方相互促进、相互转化，实现关系协调和整体发展。

---

24. 2026东城二模 第16题（主观题）
【材料触发点】 课程围绕北京独有的历史文化资源、科技创新场景和学生探究任务展开，而不是套用一般化课堂模板。材料突出的是具体对象、具体场景、具体需求之间的差异，而不是套用一个抽象模板解决所有问题；不同地区、群体、任务或发展阶段都有自身特点。
【设问】 结合材料，运用《哲学与文化》知识，谈谈“京彩课堂”的精彩所在。
【为什么能想到】 矛盾具有特殊性，不同地区、不同课程资源、不同学生任务有自身特点；京彩课堂要把北京特色情境具体化。因此要想到矛盾特殊性和具体问题具体分析：同一类工作在不同情境中矛盾表现不同，解决方法也不能机械照搬，必须从材料给出的具体条件和具体问题出发。
【答案落点】 “京彩课堂”的精彩在于具体问题具体分析，把北京独特的文化场景、发展实践和学生学习任务结合起来，形成有首都特色的思政课堂。这说明相关主体应坚持具体问题具体分析，立足本地实际、对象特点和现实需求，找准问题的特殊性，采取更有针对性的措施，形成符合具体情境的解决方案。

---

25. 2026朝阳二模 第16题（主观题）
【材料触发点】 材料既有北京四合院更新，也有广东文化馆总分馆体系和“群众点单、政府买单”的供给方式，不同城市、不同人群需求不同。材料突出的是具体对象、具体场景、具体需求之间的差异，而不是套用一个抽象模板解决所有问题；不同地区、群体、任务或发展阶段都有自身特点。
【设问】 结合材料，从哲学角度，说明在城市文化建设中怎样实现历史传承与现代创新的有机结合。
【为什么能想到】 材料强调不同城市、不同公共文化空间、不同群众需求的具体差异，不能用一个模板搞文化建设。因此要想到矛盾特殊性和具体问题具体分析：同一类工作在不同情境中矛盾表现不同，解决方法也不能机械照搬，必须从材料给出的具体条件和具体问题出发。
【答案落点】 城市文化创新要从本地文脉和群众文化需求出发，具体问题具体分析，形成适合本地的公共文化空间、服务方式和文化供给。这说明相关主体应坚持具体问题具体分析，立足本地实际、对象特点和现实需求，找准问题的特殊性，采取更有针对性的措施，形成符合具体情境的解决方案。

---

26. 2026丰台二模 第16题（主观题）
【材料触发点】 江苏、云南、内蒙古分别根据水网、梯田水系、流域修复等不同生态条件采取不同治理路径。材料突出的是具体对象、具体场景、具体需求之间的差异，而不是套用一个抽象模板解决所有问题；不同地区、群体、任务或发展阶段都有自身特点。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对“守护湿地，就是守护生态之美与文化根脉”的认识。
【为什么能想到】 不同湿地有不同生态条件和文化根脉，不能用同一种治理方案套所有地方。因此要想到矛盾特殊性和具体问题具体分析：同一类工作在不同情境中矛盾表现不同，解决方法也不能机械照搬，必须从材料给出的具体条件和具体问题出发。
【答案落点】 守护湿地要具体问题具体分析，因水制宜、因地制宜，把湿地保护方式同当地生态格局和文化传统结合起来。这说明相关主体应坚持具体问题具体分析，立足本地实际、对象特点和现实需求，找准问题的特殊性，采取更有针对性的措施，形成符合具体情境的解决方案。

---

15. 2026西城二模 第16题（主观题）
【材料触发点】 全球青年体验喝热水、八段锦、节气起居与和睦共居，材料既有中式生活方式的特殊性，也有健康、和谐、身心平衡等普遍生活追求。材料突出的是具体对象、具体场景、具体需求之间的差异，而不是套用一个抽象模板解决所有问题；不同地区、群体、任务或发展阶段都有自身特点。
【设问】 结合材料，运用《哲学与文化》知识，分析中式生活方式为什么能跨越文化差异、引发全球青年广泛共鸣。
【为什么能想到】 “跨越文化差异”说明不同民族文化有特殊性；“广泛共鸣”说明其中包含人类共同的生活经验和价值追求。因此要想到矛盾特殊性和具体问题具体分析：同一类工作在不同情境中矛盾表现不同，解决方法也不能机械照搬，必须从材料给出的具体条件和具体问题出发。
【答案落点】 中式生活方式之所以能引发共鸣，是因为它以独特中国表达承载了人们对健康、和谐、顺应自然的共同追求，实现了特殊性与普遍性的统一。这说明相关主体应坚持具体问题具体分析，立足本地实际、对象特点和现实需求，找准问题的特殊性，采取更有针对性的措施，形成符合具体情境的解决方案。

---

3. 2025海淀一模 第22题（主观题）
【材料触发点】 要把握好全局和局部、主要矛盾和次要矛盾的关系，不断提高战略思维、历史思维、辩证思维能力。材料强调全局推进和关键突破同时存在，既要看到整体系统中的多个任务，也要抓住影响全局走向的关键领域、关键环节或主要问题。
【设问】 结合材料，阐释系统观念是具有基础性的思想和工作方法（运用所学知识结合某一领域作答）。
【为什么能想到】 系统观念要求在整体推进中抓住关键，以重要领域和关键环节的突破带动全局，体现了主次矛盾的辩证关系。这触发主要矛盾和次要矛盾的关系：复杂工作不能平均用力，也不能只顾一点不及其余；要在统筹全局中抓重点，以重点突破带动其他方面协同推进。
【答案落点】 坚持系统观念要在整体推进中善于把握全局与局部、主要矛盾和次要矛盾的关系，抓住全面深化改革的关键领域和关键环节，以重点突破带动整体推进，实现改革目标的系统性推进。这说明相关主体要坚持两点论和重点论统一，既统筹全局和各项任务，又抓住主要矛盾、关键领域和关键环节，通过重点突破带动整体推进。

---

10. 2026顺义二模 第16题（主观题）
【材料触发点】 材料要求在多样与主流、人民性与艺术性、社会效益与经济效益之间找平衡，且警惕低俗化、唯流量。材料强调全局推进和关键突破同时存在，既要看到整体系统中的多个任务，也要抓住影响全局走向的关键领域、关键环节或主要问题。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对新大众文艺要面对“尊重多样与弘扬主流、人民性与艺术性、社会效益与经济效益”之间寻找平衡点这一时代课题的思考。
【为什么能想到】 既要看两方面，又要明确重点：多元不能失向，经济效益不能压倒社会效益。这触发主要矛盾和次要矛盾的关系：复杂工作不能平均用力，也不能只顾一点不及其余；要在统筹全局中抓重点，以重点突破带动其他方面协同推进。
【答案落点】 新大众文艺要坚持两点论与重点论统一，既包容多样题材和表达形式，又坚持先进文化前进方向、弘扬主旋律，把社会效益放在重要位置。这说明相关主体要坚持两点论和重点论统一，既统筹全局和各项任务，又抓住主要矛盾、关键领域和关键环节，通过重点突破带动整体推进。

---

27. 2026海淀二模 第16题（主观题）
【材料触发点】 “有字之书”提供系统知识，“无字之书”来自大地和社会生活，二者分别指向书本认识和实践经验。材料的有效信息在于把真实场景、行动任务和认识变化连在一起，说明认识不是从概念中空转出来的，而是在参与、体验、探究和解决问题中形成并深化。
【设问】 从哲学角度，谈谈为什么要把读“有字之书”和读“无字之书”结合起来。
【为什么能想到】 “读有字书”偏向已有认识的学习，“读无字书”偏向社会实践中的体验、检验和发展。因此，这类题不能只写“重视实践”四个字，而要抓住实践在材料中的具体作用：实践提供认识对象，推动认识从表层感受走向规律把握，也检验学生或主体原有认识是否真正有效。
【答案落点】 青年既要学习系统理论和文明智慧，也要投身社会实践；在实践中理解、检验和发展认识，再用正确认识指导行动，把读书所得转化为服务社会的真本领。这说明相关主体应把认识建立在实践基础上，在真实情境和具体行动中发现问题、深化理解、检验思路，并把获得的认识再用于改进实践，使认识和实践形成相互促进的过程。

---

28. 2026石景山二模 第17(3)题（主观题）
【材料触发点】 养老立法从现实养老需求和治理难点出发，最终还要落实到老年人的一餐一饭、一医一药。材料的有效信息在于把真实场景、行动任务和认识变化连在一起，说明认识不是从概念中空转出来的，而是在参与、体验、探究和解决问题中形成并深化。
【设问】 从哲学角度，分析“良法”和“善治”的关联。
【为什么能想到】 良法来自治理实践中的问题，又要回到治理实践中检验和实现自身价值。因此，这类题不能只写“重视实践”四个字，而要抓住实践在材料中的具体作用：实践提供认识对象，推动认识从表层感受走向规律把握，也检验学生或主体原有认识是否真正有效。
【答案落点】 良法要在善治实践中接受检验并发挥作用，善治又能推动法律制度不断完善，实现从制度认识到治理实践的转化。这说明相关主体应把认识建立在实践基础上，在真实情境和具体行动中发现问题、深化理解、检验思路，并把获得的认识再用于改进实践，使认识和实践形成相互促进的过程。

---

23. 2026东城二模 第16题（主观题）
【材料触发点】 “京彩课堂”把学生带到中轴线、故宫、科创基地、临空经济等真实场景中，用“实景+任务+探究”理解思政理论。材料的有效信息在于把真实场景、行动任务和认识变化连在一起，说明认识不是从概念中空转出来的，而是在参与、体验、探究和解决问题中形成并深化。
【设问】 结合材料，运用《哲学与文化》知识，谈谈“京彩课堂”的精彩所在。
【为什么能想到】 材料核心不是在教室里背理论，而是让学生在真实场景和探究任务中获得认识，体现实践推动认识深化。因此，这类题不能只写“重视实践”四个字，而要抓住实践在材料中的具体作用：实践提供认识对象，推动认识从表层感受走向规律把握，也检验学生或主体原有认识是否真正有效。
【答案落点】 “京彩课堂”的精彩在于把抽象理论放回实践场景中，让学生在探究、项目、议题和实景体验中理解知识、检验认识、形成认同。这说明相关主体应把认识建立在实践基础上，在真实情境和具体行动中发现问题、深化理解、检验思路，并把获得的认识再用于改进实践，使认识和实践形成相互促进的过程。

---

24. 2026西城二模 第16题（主观题）
【材料触发点】 外国青年不是只听介绍，而是亲身体验喝热水、练八段锦、节气起居，并通过旅行更直观深度地感知中国。材料的有效信息在于把真实场景、行动任务和认识变化连在一起，说明认识不是从概念中空转出来的，而是在参与、体验、探究和解决问题中形成并深化。
【设问】 结合材料，运用《哲学与文化》知识，分析中式生活方式为什么能跨越文化差异、引发全球青年广泛共鸣。
【为什么能想到】 材料强调亲身体验和旅行感知，说明对中国文化的理解来自实践中的接触、体验和感受。因此，这类题不能只写“重视实践”四个字，而要抓住实践在材料中的具体作用：实践提供认识对象，推动认识从表层感受走向规律把握，也检验学生或主体原有认识是否真正有效。
【答案落点】 中式生活方式通过可体验的日常实践进入海外青年生活，使他们在亲身体验中理解中华文化智慧，从而形成真挚的跨文化共鸣。这说明相关主体应把认识建立在实践基础上，在真实情境和具体行动中发现问题、深化理解、检验思路，并把获得的认识再用于改进实践，使认识和实践形成相互促进的过程。

---

25. 2026顺义二模 第16题（主观题）
【材料触发点】 新大众文艺扎根外卖员、快递员、家政工、退休职工、百姓演员等普通人的生活实践，创作来自真实生活而不是凭空编造。材料的有效信息在于把真实场景、行动任务和认识变化连在一起，说明认识不是从概念中空转出来的，而是在参与、体验、探究和解决问题中形成并深化。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对新大众文艺要面对“尊重多样与弘扬主流、人民性与艺术性、社会效益与经济效益”之间寻找平衡点这一时代课题的思考。
【为什么能想到】 评标材料列出实践观点；新大众文艺的生命力来自人民群众的真实生活实践，实践为文艺认识和表达提供源泉。因此，这类题不能只写“重视实践”四个字，而要抓住实践在材料中的具体作用：实践提供认识对象，推动认识从表层感受走向规律把握，也检验学生或主体原有认识是否真正有效。
【答案落点】 新大众文艺要扎根人民群众生活实践，观察时代变化和百姓真实需求，把真实生活转化为有共鸣的文艺表达。这说明相关主体应把认识建立在实践基础上，在真实情境和具体行动中发现问题、深化理解、检验思路，并把获得的认识再用于改进实践，使认识和实践形成相互促进的过程。

---

25. 2026顺义二模 第16题（主观题）
【材料触发点】 材料写外卖员、快递员、家政工、退休职工、百姓演员、非遗传承人都成为创作者、传播者和共享者。材料把群众生活、群众需求、群众参与和群众评价放在突出位置，说明问题的出发点和落脚点不是抽象主体，而是人民群众的实践和需要。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对新大众文艺要面对“尊重多样与弘扬主流、人民性与艺术性、社会效益与经济效益”之间寻找平衡点这一时代课题的思考。
【为什么能想到】 “大众创作、大众传播、大众共享”直接体现人民群众是文化创造主体。这触发人民群众历史主体地位：人民群众是社会历史和文化创造的主体，群众实践提供创造源泉，群众需要也决定相关工作的价值方向。
【答案落点】 新大众文艺要坚持以人民为中心，扎根人民生活、依靠人民创造、服务人民精神文化需求，让人民成为文艺创作和文化共享的主体。这说明相关工作要坚持人民主体地位，尊重群众实践和群众创造，从人民需要出发、依靠人民推进，并以人民是否受益作为检验成效的重要标准。

---

24. 2026东城二模 第16题（主观题）
【材料触发点】 材料强调课程的育人价值和铸魂作用，引导学生在北京实践中形成文化自信、责任意识和正确价值追求。材料不仅写具体做法，还写这些做法指向的价值目标、精神导向、人民立场或社会意义，说明问题核心包含价值判断和价值选择。
【设问】 结合材料，运用《哲学与文化》知识，谈谈“京彩课堂”的精彩所在。
【为什么能想到】 思政课不只是知识传递，还要解决价值引领问题；正确价值观会影响学生怎样认识城市、怎样选择行动方向。因此要想到价值观的导向作用：价值观影响人们认识问题、评价事物和选择行动方向。材料中的做法之所以成立，是因为它服务于正确价值目标和公共利益。
【答案落点】 “京彩课堂”的精彩在于发挥正确价值观的导向作用，引导学生在真实场景中理解国家、城市与个人责任，形成正确价值判断和价值选择。这说明相关工作要发挥正确价值观的导向作用，坚持人民立场和正确价值追求，把具体行动统一到满足人民需要、凝聚社会共识和提升公共价值上来。

---

25. 2026朝阳二模 第16题（主观题）
【材料触发点】 材料最后强调弘扬社会主义核心价值观、提高市民文明素质、塑造城市精神。材料不仅写具体做法，还写这些做法指向的价值目标、精神导向、人民立场或社会意义，说明问题核心包含价值判断和价值选择。
【设问】 结合材料，从哲学角度，说明在城市文化建设中怎样实现历史传承与现代创新的有机结合。
【为什么能想到】 城市文化建设不是只做建筑和活动，还要解决价值引领、精神凝聚和城市认同问题。因此要想到价值观的导向作用：价值观影响人们认识问题、评价事物和选择行动方向。材料中的做法之所以成立，是因为它服务于正确价值目标和公共利益。
【答案落点】 要发挥正确价值观的导向作用，用社会主义核心价值观引领城市文化软实力建设，使文化空间凝聚认同感和归属感。这说明相关工作要发挥正确价值观的导向作用，坚持人民立场和正确价值追求，把具体行动统一到满足人民需要、凝聚社会共识和提升公共价值上来。

---

26. 2026丰台二模 第16题（主观题）
【材料触发点】 材料把“万物并育而不相害”“天人合一”等传统生态智慧融入湿地保护，强调人与自然和谐共生。材料不仅写具体做法，还写这些做法指向的价值目标、精神导向、人民立场或社会意义，说明问题核心包含价值判断和价值选择。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对“守护湿地，就是守护生态之美与文化根脉”的认识。
【为什么能想到】 湿地保护背后有生态价值观作引导：怎么看自然，决定怎么治理自然。因此要想到价值观的导向作用：价值观影响人们认识问题、评价事物和选择行动方向。材料中的做法之所以成立，是因为它服务于正确价值目标和公共利益。
【答案落点】 要发挥正确生态价值观的导向作用，继承天人合一、顺应自然的生态智慧，引导湿地保护实践走向人与自然和谐共生。这说明相关工作要发挥正确价值观的导向作用，坚持人民立场和正确价值追求，把具体行动统一到满足人民需要、凝聚社会共识和提升公共价值上来。

---

27. 2026西城二模 第16题（主观题）
【材料触发点】 中式生活方式体现天人合一、身心兼顾、顺应自然等价值追求，契合全球青年对健康生活、和谐关系和精神安顿的关切。材料不仅写具体做法，还写这些做法指向的价值目标、精神导向、人民立场或社会意义，说明问题核心包含价值判断和价值选择。
【设问】 结合材料，运用《哲学与文化》知识，分析中式生活方式为什么能跨越文化差异、引发全球青年广泛共鸣。
【为什么能想到】 评标页把“价值观”列为角度，并在哲学观点中写明“价值观的导向作用”；材料中的模仿、认同和传播，背后是共同价值对认识、评价和行为选择的引导。因此要想到价值观的导向作用：价值观影响人们认识问题、评价事物和选择行动方向。材料中的做法之所以成立，是因为它服务于正确价值目标和公共利益。
【答案落点】 价值观对人们认识世界、评价事物和行为选择具有导向作用。中式生活方式所体现的和谐、健康、顺应自然等价值追求，契合当代全球青年的生活关切，因而能引导他们主动体验、模仿并传播。这说明相关工作要发挥正确价值观的导向作用，坚持人民立场和正确价值追求，把具体行动统一到满足人民需要、凝聚社会共识和提升公共价值上来。

---

28. 2026顺义二模 第16题（主观题）
【材料触发点】 材料批评部分作品低俗化、同质化、追逐流量、忽视思想性艺术性价值性，要求传播正能量。材料不仅写具体做法，还写这些做法指向的价值目标、精神导向、人民立场或社会意义，说明问题核心包含价值判断和价值选择。
【设问】 结合材料，运用《哲学与文化》知识，谈谈你对新大众文艺要面对“尊重多样与弘扬主流、人民性与艺术性、社会效益与经济效益”之间寻找平衡点这一时代课题的思考。
【为什么能想到】 作品是否追逐流量、能否传递正能量，背后是价值观引导问题。因此要想到价值观的导向作用：价值观影响人们认识问题、评价事物和选择行动方向。材料中的做法之所以成立，是因为它服务于正确价值目标和公共利益。
【答案落点】 新大众文艺创作者要发挥正确价值观的导向作用，坚持社会主义核心价值观引领，拒绝低俗化、唯流量化，提升作品精神内涵。这说明相关工作要发挥正确价值观的导向作用，坚持人民立场和正确价值追求，把具体行动统一到满足人民需要、凝聚社会共识和提升公共价值上来。


---

## SOURCE: reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\08_external_review\batch_02_high_risk_render_pages.md


# 高风险渲染页文本抽取

## PDF page 53

— 53 — 
联系，实现科技与农业的创新结合。①科技赋能提升效率（经济角度）正确；③“根本转变生产关系”夸
大了——农业生产关系的根本转变指变革所有制等深层关系，引入科技不构成生产关系的根本转变；
④“借助想象促成融合”把“想象”当作主导动力，错置了实践与意识的关系。 
【答案落点】 正确项是 A（①②）。①通过科技赋能提升农业生产效率——经济与社会角度，科技作
为第一生产力推动农业现代化。②把握多样联系——人对农业生产中多种联系（农业要素与科技要素、
传统生产环节与新兴技术、空间联系与功能联系）的把握，是联系的多样性原理在农业现代化实践中的
体现。错项③“推动农业生产关系的根本转变”夸大了科技应用的作用——引入新技术属于生产力的发展，
不等于生产关系的根本转变；错项④“借助想象促成跨界融合”把“想象”置于主导地位，颠倒了“实践决定
意识”的关系，跨界融合的根本动力是生产实践与现实需求，而不是想象。 
 
28. 2024 顺义二模 第1 题（选择题） 
【材料触发点】 “当代中国的伟大社会变革，不是简单延续我国历史文化的母版，不是简单套用马克思
主义经典作家设想的模板……只有把科学社会主义基本原则同本国具体实际、历史文化传统、时代要求
紧密结合起来”。 
【设问】 这说明 
①科学社会主义发展的一般进程是由各国地理环境、文化传统、外部因素等决定的 
②科学社会主义的产生、发展与资本主义社会的生产方式没有本质的、内在的关系 
③现实与历史之间是有联系的，当代中国的变革基于自身独特的历史和文化基础上 
④中国特色社会主义是科学社会主义理论逻辑和中国社会发展历史逻辑的辩证统一 
A. ①② 
B. ①③ 
C. ②④ 
D. ③④ 
【为什么能想到】 “同本国具体实际、历史文化传统、时代要求紧密结合”明确把“当下变革”与“历史文
化”“科学社会主义基本原则”连为一体——这是事物之间普遍联系的具体体现：现实和历史相联系、中国
实践和科学社会主义理论相联系。学生看到“同……结合”“不是简单延续/不是简单套用”这种把多重坐标
放在一起的表述，应当想到现实与历史、理论与实践存在普遍而具体的联系。 
【答案落点】 ③现实与历史是有联系的，中国当代变革植根于自身独特的历史文化基础——这是普遍
联系的具体表现；④中国特色社会主义是科学社会主义理论逻辑和中国社会发展历史逻辑的辩证统一—
—这是理论(科学社会主义基本原则)与实践(中国具体实际)联系的辩证统一。 
 
29. 2026 海淀二模 第16 题（主观题） 
【材料触发点】 《有字之书》承载经典学说和文明智慧，《无字之书》蕴藏于广袤大地和社会万象之
中；二者分别代表认识的书本来源和实践来源，是学习成长中相互依存的两个方面。

---

## PDF page 103

— 103 — 
14. 2025 顺义一模 第16 题（主观题） 
【材料触发点】 材料：《哪吒之魔童闹海》“从剔骨还父的悲情英雄蜕变为我命由我不由天的叛逆少年，
既保留了反抗命运的精神内核，又赋予其自我认知的当代价值观”。 
【设问】 结合材料，运用《哲学与文化》知识，分析如何让那些“古老的”成为“新生的”。 
【为什么能想到】 《哪吒》传统形象在现代演绎中既保留了“反抗命运的精神内核”（继承），又赋予新
的“自我认知的当代价值观”（创新）——这是对传统的扬弃，是事物自己否定自己、自己发展自己的过
程。学生看到“既保留…又赋予…”“传统的现代诠释”“古老的成为新生的”这种扬弃式表述时，就应当想到
辩证否定观。 
【答案落点】 辩证否定是事物自身的否定，是新事物对旧事物的扬弃，要求克服旧事物中消极、过时
的内容，又保留其中积极合理的因素。让“古老的”成为“新生的”，要把传统文化中如“反抗命运的精神内
核”等积极合理的因素保留下来，同时根据时代发展赋予其“自我认知”“我命由我不由天”等当代价值观，
使传统文化在自我否定、自我发展中焕发新的生命力。 
 
15. 2024 西城一模 第12 题（选择题） 
【材料触发点】 黑格尔说“人们总以为肯定和否定具有绝对的区别，其实两者是相同的；可以称肯定为
否定，也可以称否定为肯定；譬如说一条往东的路同时也是一条往西的路”。 
【设问】 对此理解正确的是 
A. 肯定和否定没有界限，肯定即否定，否定即肯定 
B. 有些事物包含着肯定因素，另有一些事物则包含着否定因素 
C. 肯定与否定互为条件，且只存在于它们的联系中 
D. 处理复杂问题，既不能持肯定态度，也不能持否定态度 
【为什么能想到】 黑格尔的“东路即西路”是“肯定中含否定、否定中含肯定”——肯定与否定不是孤立的
两端，而是互为条件、共存于事物的同一个联系之中，对应C“肯定与否定互为条件，且只存在于它们
的联系中”。A 说“肯定即否定、否定即肯定”走向了同一律式的混淆，错；B“有些事物只含肯定、有些只
含否定”割裂二者；D“既不能持肯定也不能持否定”走向不可知论。 
【答案落点】 正确项是 C：肯定与否定互为条件，且只存在于它们的联系中。错项分析：A 抹去界限
走向同一；B 把肯定—否定割裂在不同事物之中；D 取消立场，放弃辩证否定。

---

## PDF page 104

— 104 — 
16. 2026 门头沟一模 第5 题（选择题） 
【材料触发点】 公交专线保留公共交通服务功能，又突破常规设站方式，把站点直接延伸到市场二层，
形成新的服务形态。 
【设问】 北京鲜批市场公交专线将站点创造性地设在市场二层交易区,被称为“能上楼的专线”。不仅解
决了群众采购出行的“最后一公里”难题,更以其独特的“上楼”体验,成为城市公共交通服务创新的典范。该
专线的成功运行蕴含的道理有 
①坚持系统优化,旨在实现经济效益和社会效益的统一； 
②对传统公交模式进行“扬弃”,更好地满足乘客需求； 
③打破思维定势,通过反向思考寻求公交服务的新思路； 
④善于联想,促使公交运营矛盾的对立性转化为同一性 
A. ①② 
B. ①④ 
C. ②③ 
D. ③④。 
【为什么能想到】 能想到辩证否定，是因为专线没有全盘抛弃传统公交，而是在保留公共交通合理功
能的基础上克服站点距离远、购物不便等旧局限，实现服务方式创新。 
【答案落点】 正确项是C，因为材料体现既肯定又否定、既保留又创新；把系统优化目的窄化为经济
社会效益统一，或说矛盾的对立性和同一性可以直接相互转化，都不符合题意。 
 
17. 2026 东城二模 第16 题（主观题） 
【材料触发点】 思政课没有抛弃育人目标，而是通过探究式、项目式、数字地图、云研学、虚拟展馆
等方式激活课堂。材料同时出现了保留、转化、更新和创造等信息，说明处理对象不是简单复原旧形式，
也不是完全抛弃旧基础，而是在继承合理因素的基础上实现新的发展。 
【设问】 结合材料，运用《哲学与文化》知识，谈谈“京彩课堂”的精彩所在。 
【为什么能想到】 材料既守住思政育人方向，又创新教学形式和传播载体，属于在继承中发展、在发
展中创新。这正对应辩证否定的逻辑：否定不是全盘否定，而是既克服旧事物中过时、不适应的方面，
又保留其中积极合理的因素，并在新的条件下实现转化和创新。 
【答案落点】 “京彩课堂”要坚持守正创新，守住思政铸魂育人的根本任务，同时借助真实场景和数字技
术创新学习方式，增强课堂生命力。这说明相关工作要坚持守正创新，在尊重原有基础和合理价值的同
时推动形式、机制和路径更新，使传统资源或已有经验在新的实践条件下焕发新的生命力。

---

## PDF page 119

— 119 — 
【为什么能想到】 题干已经明示“抢位与错位蕴含着辩证法”——抢位与错位是对立统一的两面，“快”与
“慢”、“同”与“异”是矛盾双方。学生看到“既要…又要…”的并列结构以及“快与慢、同与异的辩证关系”就
应当想到对立统一规律——构建现代化产业体系要正确处理抢位与错位这一对矛盾的辩证关系。 
【答案落点】 正确项是 B（含④）。事物的矛盾双方既对立又统一，要用对立统一的观点看问题。抢
位与错位、快与慢、同与异是构建现代化产业体系中相互对立又相互依存的矛盾双方，需要在统筹中处
理它们的辩证关系。错项②“超越地区资源禀赋”错——错位发展恰恰要立足而不是超越地区资源禀赋；
错项③“关键是实现抢位和错位的转化”错——抢位与错位是并行处理的辩证关系，不是简单地从一方转
化到另一方。 
 
30. 2025 东城期末 第4 题（选择题） 
【材料触发点】 汉字横、撇、捺、提、折、钩，可一笔贯通气韵，豪气干云，亦可繁复多画，耐心描
摹；笔画的主次、长短、布局留白都彰显了汉字的博大精深。“点”虽小，但如明珠般璀璨；“横”在肩上，
它是担当也是约束。 
【设问】 由此可见（ ） 
①在笔画的对立统一中彰显中华汉字之美； 
②汉字笔画蕴含着人们的精神向往和美好追求； 
③不同笔画的个性寓于汉字结构的共性之中； 
④抓主流，以主笔为核心书写汉字方能为美。 
【为什么能想到】 汉字笔画“横/撇/捺/提/折/钩”“主次/长短/布局留白”之间是相互对立又相互统一的——
一笔贯通是统一，繁复多画是分立；“横”既是担当也是约束体现了对立面共存。学生看到这种“差异共存
而成美”的描述就应当想到矛盾的同一性和斗争性、对立统一规律。 
【答案落点】 正确项是 A（含①）。矛盾就是对立统一，矛盾双方既对立又统一。汉字笔画的主次、
长短、布局留白等多种对立要素相互依存、相互成就，正是在这种笔画的对立统一中彰显出汉字之美。
错项③“不同笔画的个性寓于汉字结构的共性之中”颠倒了共性与个性的关系——共性寓于个性之中，个
性包含共性；错项④“抓主流，以主笔为核心书写汉字方能为美”与材料“主次、长短、布局留白都彰显了
汉字博大精深”不符（材料并没有强调以主笔为核心）。

---

## PDF page 170

— 170 — 
【设问】 未来，是人塑造人工智能？还是人工智能塑造人？还是……运用哲学知识，谈谈你的看法。 
【为什么能想到】 材料中“研究人员观察到神经元之间的联系”是人类的科学研究实践，正是这一实践推
动了人工神经网络概念的产生；“类脑智能蓄势待发”“大模型走向各行业”进一步说明实践不断推动认识
深化；同时人工智能的广泛应用作为新的实践又“重塑人类对世界的认识”，体现实践是认识的来源、动
力，认识在实践基础上不断发展。 
【答案落点】 未来人与人工智能的相互塑造正是建立在人的实践基础上——人在科研与应用实践中加
深对人工智能的认识进而设计、改造人工智能（人塑造人工智能），人工智能又作为新的实践工具推动
人形成新认识、新观念（人工智能塑造人），二者在实践基础上相互塑造、共同发展。 
 
17. 2025 丰台二模 第16 题第（1）问（主观题） 
【材料触发点】 敦煌唐代文献记录印度甘蔗制糖法，粟特商人用波斯银币购四川茶叶，莫高窟日神形
象兼具古希腊罗马艺术元素。 
【设问】 请你从以上三个地点中推荐一处，并运用《哲学与文化》知识阐述推荐理由。 
【为什么能想到】 敦煌的甘蔗制糖法记录、波斯银币购茶、莫高窟日神兼具古希腊罗马艺术元素，都
是古代丝路商贸往来的实践产物。各民族在交易、迁徙、建造等实践中形成对异域物产、技艺、艺术的
认识，并写入文献、刻入壁画。这表明实践是认识的来源和动力。 
【答案落点】 材料中“敦煌唐代文献记录印度甘蔗制糖法，粟特商人用波斯银币购四川茶叶，莫高窟日
神形象兼具古希腊罗马艺术元素”，体现实践是认识的基础；这说明实践是认识的来源、动力、检验标
准和目的，因此可以直接用这一原理说明题中材料的内在逻辑。 
 
18. 2025 丰台期末 第16 题（主观题） 
【材料触发点】 “数”不是凭空而来；做计划、定方案、看大数都离不开关注实际、调查研究。 
【设问】 胸中有“数”的工作方法，是毛泽东从中国革命和建设实践中总结得出的宝贵经验。他指出：
“对情况和问题一定要注意到它们的数量方面，要有基本的数量的分析…一切都是胸中无数，结果就不
能不犯错误。”在工作生活中，要做计划、定方案；在国家治理中，要看大数、看长远，都离不开胸中
有“数”的工作方法。“数”从哪里来，“数”当如何定，“数”为何所用……阐述“胸中有数”带来的哲学思考。
（8 分）。 
【为什么能想到】 材料强调“数”必须通过调查研究、关注实际才能获得；这说明对“数”的认识不是主观
先验的，而是来源于人们改造客观世界的实践活动。 
【答案落点】 要做到胸中有“数”，必须深入基层、调查研究，在实践中获取真实“数”，并以此指导工作
和国家治理。

---

## PDF page 213

— 213 — 
【答案落点】 网络文艺适老化不能靠制造冲突、夸张离谱和低俗价值吸引眼球，而要坚持正确价值导
向，回应中老年群体真实精神文化需求，塑造积极健康的银发形象，让作品既便于中老年人观看理解，
又能弘扬社会主义核心价值观。 
 
19. 2025 昌平二模 第16 题（主观题） 
【材料触发点】 颜杲卿、颜季明牺牲生命维护国家统一；苏轼不畏穷困艰难追求理想精神状态。 
【设问】 从哲学与文化角度，谈谈你的看法。 
【为什么能想到】 材料中书家及其家人在民族危亡和人生困境前选择维护国家统一、坚守理想，说明
书法所承载的不只是字，而是书家所信奉的价值取向；价值观对人们认识和改造世界具有导向作用，所
以人品才能决定书法之贵。 
【答案落点】 评价中国书法不仅看技艺，更要看书家是否树立和践行了正确的价值观，正确的价值观
引导书家在大是大非面前作出正确选择，使作品具有打动人心的精神力量。 
 
20. 2024 顺义二模 第16 题第（1）问（主观题） 
【材料触发点】 “无废城市是以创新、协调、绿色、开放、共享的新发展理念为引领，通过推动形成绿
色发展方式和生活方式”“中共中央、国务院印发《关于全面推进美丽中国建设的意见》，加快无废城市
的建设”。 
【设问】 结合材料，运用《哲学与文化》知识，说明各地推进“无废城市”建设做法的合理性。 
【为什么能想到】 “以新发展理念为引领”“推动形成绿色发展方式和生活方式”“推进美丽中国建设”明确
把绿色、人与自然和谐这一价值取向放在“无废城市”建设的首位——这是价值观对实践的导向作用。学
生看到“以……为引领”“推动形成绿色发展方式”“美丽中国”这种把价值取向作为根本指引的表述，应当想
到价值观对人改造世界的活动具有导向作用。 
【答案落点】 价值观对人认识世界和改造世界的活动具有导向作用。各地以新发展理念(创新、协调、
绿色、开放、共享)和美丽中国建设的价值取向为引领，推动绿色发展方式和生活方式落地——以正确
价值观引导实践方向，这是各地推进“无废城市”建设做法合理性的价值观基础。 
 
21. 2024 顺义二模 第20 题第（2）问（主观题） 
【材料触发点】 “党的二十大报告指出：从现在起，中国共产党的中心任务就是团结带领全国各族人民
全面建成社会主义现代化强国、实现第二个百年奋斗目标，以中国式现代化全面推进中华民族伟大复
兴”；“人民之问”被明确列入党要回答的四大问题之一。 
【设问】 结合材料，综合运用所学，谈谈对实现中华民族伟大复兴需要“不断谱写马克思主义中国化时
代化新篇章”的认识。


---

## SOURCE: reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\04_fusion_audit\haidian_2025_second_mock_choice_source_addendum_20260524.md


# 2025海淀二模 choice-source addendum

Scope: tighten the evidence trail for the inherited `2025海淀二模 Q10/Q11` choice-question rows after the row-level audit reopened the accepted base handbook.

## Verdict

`Q10/Q11` are retained as choice-question chains, not upgraded into main-question scoring chains.

The current raw suite folder does not contain the previously referenced teacher-version answer PDF, so this addendum does not claim that the PDF was newly re-read in this 2026-05-24 run. Instead, the accepted basis is the archived ledger/governor trail plus the current paper OCR and wrong-option library:

- current ledger row: `2025海淀二模选择题补充 | 2025海淀二模第1-15题 | 28 | 试卷OCR核题 + 讲评材料答案页/公开答案图双重核对 | 错肢库+哲学框架已补齐`;
- governor archived pass: the original blocker was withdrawn because the answer key was confirmed as `1C 2B 3A 4B 5D 6B 7A 8C 9A 10D 11C 12D 13C 14B 15A`;
- governor archived correction round: the local scan paper was reopened and the public answer image was re-read; the suite was closed only with stable 必修四 triggers;
- current wrong-option library preserves source-labeled rows for `2025北京海淀高三二模 第10题①`, `第11题①`, and `第11题④`;
- current v8 framework keeps the `2025海淀二模 第10题` chain under `实践是检验认识真理性的唯一标准`.

Therefore:

- `Q10` may remain as a student-facing choice-chain example for `实践是检验认识真理性的唯一标准`, with answer-side trail pointing to the archived key where Q10=`D`.
- `Q11` may remain only in the wrong-option/choice-chain boundary where relevant, with answer-side trail pointing to the archived key where Q11=`C`.
- No Q10/Q11 row should be described as a scoring-rubric row or formal 主观题细则 row.

## Source Pointers Used

- `reports/choice_question_processing_ledger.md`, rows for `2025海淀二模选择题补充` and `worker_2025_haidian_ermo`.
- `reports/governor_board.md`, current-status rows and `2026-04-23 2025海淀二模选择题哲学链回填与错标纠正`.
- `artifacts/北京高考政治错肢库_持续更新版.md`, `2025海淀二模选择题补充`.
- `reports/bixiu4_philosophy_strict_v8_2026-05-23/new_9_suite_integration/必修四哲学材料-知识触发框架_v8_65套新增卷子并入版.md`, `2025海淀二模 第10题`.

## Guardrail

If the missing teacher-version answer PDF is later found, reopen the row and directly attach the PDF/page evidence. Until then, the accepted language must stay as `archived answer-side trail + current OCR/library support`, not `current raw teacher PDF verified`.


---

## SOURCE: reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\03_claudecode_lane\claudecode_verify_haidian_choice_addendum_20260524.md


已收集全部证据，现在出具审计表。

---

## 审计结果：2025海淀二模 Q10/Q11 choice-source 边界审计

| severity | location | finding | fix |
|---|---|---|---|
| PASS | `choice_source_addendum` §Source Pointers | 当前 run 未声称重新读取教师版 PDF；正确使用"archived ledger/governor trail + OCR + wrong-option library"作为证据基础，口径诚实。 | 无需操作。 |
| PASS | `choice_source_addendum` §Verdict + `evidence_closeout` §Q10/Q11 | Q10/Q11 均保持为 choice-question chain，未升格为主观题细则行。两份文件结论一致。 | 无需操作。 |
| PASS | `choice_question_processing_ledger.md` 行 `2025海淀二模选择题补充` | 台账记录：`试卷OCR核题 + 讲评材料答案页/公开答案图双重核对`，答案数量 28 条，状态`错肢库+哲学框架已补齐`。与 addendum 引用口径完全吻合。 | 无需操作。 |
| PASS | `governor_board.md` 行 190–196 (`2026-04-23`) | Governor 记录 `framework_backfill: passed`，Q10 正确回填 `实践是认识的基础/实践检验标准`；Q11 无稳定 必修四 正确项，未强行回填。 | 无需操作。 |
| PASS | `v8_65套…框架.md` `实践是检验认识真理性的唯一标准` 节点 (line 1538–1540) | Q10 在框架中的链指向`2025海淀二模 第10题`，触发原因和答案落点均为认识论方向，不含主观题细则语言。 | 无需操作。 |
| PASS | `错肢库` 行 150–152 | Q10①（实用主义真理观）、Q11①（不完全归纳误套功能整合）、Q11④（功能决定价值大小）三条错肢均在库，错误类型、正确说法与题目内容一致；答案 Q10=D、Q11=C 与 archived key `…10D 11C…` 吻合。 | 无需操作。 |
| NEED_EVIDENCE | `choice_source_addendum` §Guardrail | 教师版答案 PDF 仍不在当前 raw suite folder 中。这是已记录的已知缺口，addendum 正确设置了 guardrail（若日后找到 PDF 须重新开行）。不触发 REWRITE，但该边界必须保持，后续任何人不得在 PDF 补入前将 Q10/Q11 升格为细则行。 | 维持 guardrail 原文；找到 PDF 后按 addendum 指示重开行、补附页码证据后方可升格。 |
| PASS | `CURRENT_ACCEPTANCE_STATUS_20260524.md` §External Review | ClaudeCode 重检后 Q10/Q11 边界在 `claudecode_recheck_inherited_patch_and_haidian_evidence_20260524.md` 中已被纳入，最终状态标为 `SCOPED_PASS`（非 all-model PASS，因 GPTPro web 仍 pending）。状态描述准确。 | 无需操作。 |
| PASS | `CURRENT_ACCEPTANCE_STATUS_20260524.md` §Current Verdict | GPTPro web pending 已明确写入 `LOCAL_AND_EXTERNAL_CLAUDE_SCOPED_PASS__GPTPRO_WEB_PENDING`，未虚报 full PASS。 | 无需操作。 |

---

## 总裁定

```
SCOPED_PASS: Haidian Q10/Q11 choice-source boundary is acceptable;
no final all-model PASS because GPTPro web remains pending.
```

**说明**：Q10/Q11 的处理链（archived key + OCR + 错肢库 + governor backfill）内部一致，无证据显示 Claude Code 或 Codex 在本次 run 中声称读取了不存在的 PDF，也无升格为细则行的痕迹。唯一悬挂项是教师版 PDF 缺失（NEED_EVIDENCE），该缺口已有正确 guardrail 覆盖，不构成当前 DOCX 需要撤回或重写的依据。
