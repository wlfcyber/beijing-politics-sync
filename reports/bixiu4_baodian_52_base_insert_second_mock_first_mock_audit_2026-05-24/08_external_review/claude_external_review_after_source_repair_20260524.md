I've read the prompt, triage doc, accepted JSONL, ledger, matrix, and the朝阳/房山/海淀一模/海淀二模 source bundles. Below is the external review based on what the upload packet actually contains.

## External Claude Review — 2026-05-24

| severity | location | finding | evidence_checked | required_fix |
|---|---|---|---|---|
| **PASS** | 2026朝阳二模 Q21 (JSONL lines 11–12) | Topic corrected to "四个中国"; question_prompt verbatim matches source paper line 299–300 ("将'四个中国'确立为推进中国式现代化的战略支柱"). Prior "五篇大文章" error is closed. | `suite_source_bundles/2026朝阳二模.md` lines 107, 299–300; 阅卷细则 line 116 ("四个中国") | 保留 |
| **PASS** | 2026房山二模 Q16 (JSONL lines 18–20) | question_prompt now "如何从中华工业文化读懂中华民族最感动人的浪漫"; source rubric explicitly names "中华工业文化…—— 中华民族最感动人的浪漫". Prior generic "工匠精神的当代价值" framing is closed. | `suite_source_bundles/2026房山二模.md` lines 27, 151, 321 | 保留 |
| **PASS** | answer_landing wording across all 38 accepted entries | No occurrences of "答案要写出", "答案要落到", or "不能只罗列单个做法" remain. Landings read as student-writeable卷面 sentences. | Full scan of `student_patch_entries.accepted.jsonl` | 保留 |
| **PASS** | Duplicate/overextended rows | 2025海淀一模 Q21 system-optimization merged; 2026海淀二模 Q16 contradiction entry dropped; 海淀二模 Q16 only keeps 联系/实践两角度. 38 rows total, matches `docx_insert_ledger.csv`. | `claude_external_review_triage_20260524.md`; ledger row count vs jsonl | 保留 |
| **PASS** | Q21 朝阳 boundary_note | Correctly carves out 党的领导1分 as politics-module-only and does not double-claim it as a 哲学 point. | JSONL line 11 boundary_note vs source line 120–122 | 保留 |
| **SHOULD_FIX** | 2025海淀一模 Q21 (JSONL lines 22–23, ledger rows 14 & 24 & 34) | Labeled "Q21", but source bundle shows Q21=演绎推理/国际贸易, Q22=系统观念 (材料"必须坚持系统观念…全面深化改革是一项复杂的系统工程…主要矛盾和次要矛盾"). The 系统观念/主次矛盾 content matches Q22, not Q21. | `suite_source_bundles/2025海淀一模.md` lines 84–99 (Q21=演绎推理) vs 101–162 (Q22=系统观念) | 把两条 question_no 由 `Q21` 改为 `Q22`，并同步 `docx_insert_ledger.csv` 与 `COVERAGE_CLOSURE_MATRIX_V2.csv` 中"2025海淀一模 第21题"标题为"第22题"。 |
| **NEED_EVIDENCE** | 2026海淀二模 Q16 (JSONL lines 26–27) | `source_evidence/suite_source_bundles/2026海淀二模.md` contains **only** "内部资料，严禁外传" watermark across ~32 pages — no readable rubric or question text. The triage claim "教师版参考答案：第16题可从'联系、实践与认识'等角度作答" cannot be verified from the packet. | `suite_source_bundles/2026海淀二模.md` lines 14–299 (全部为水印重复) | 补一份可读的海淀二模 Q16 题面+参考答案/讲评截图或重新抽取的 docx-text 到 bundle 中；在补全之前，海淀二模 Q16 两条不应宣称已 PASS。 |
| **SHOULD_FIX** | 2026东城二模 Q16 "辩证否定/守正创新" (JSONL line 4) | source_repair_basis 引用 "材料表列'发展（辩否）'" — 朝阳 Q16 细则确有"辩证否定/发展的观点"明列，但东城 Q16 我未在本包内见到独立细则文档；only 东城 suite bundle 同名引用所列，但本批阅其内容偏 朝阳模板。如东城确无"辩证否定"独立采分项，应归并入"发展的观点"角度避免重复采分宣称。 | `student_patch_entries.accepted.jsonl` line 4 source_repair_basis；东城 bundle 内未在本次摘录中独立验证 | 在 boundary_note 中明确"辩证否定与发展观可替代采分，不作累加"，或在 source_evidence 中补一份东城 Q16 评标细则截图佐证"发展（辩否）"独立列项。 |
| **SHOULD_FIX** | `COVERAGE_CLOSURE_MATRIX_V2.md` | 标头声称"35 source suites…COVERED_OR_PATCHED: 35"，但 `suite_source_bundles/` 实际只放了 10 份 bundle（2025海淀一模 + 9 份 2026 二模/一模），其余 25 个套卷在本上传包内无源材料。对外审而言这是空头声明。 | `COVERAGE_CLOSURE_MATRIX_V2.md` lines 5–11 vs 实际 bundle 目录 | 要么补齐其余 25 套源 bundle，要么把声明改为"本批 accepted 涉及的 10 个套卷已附源证据，其余 25 套依赖基线宝典覆盖"。 |
| **PASS** | 2026朝阳二模 Q16 (JSONL lines 7–10) | 5 角度（对立统一/辩否守正/具体问题/价值观+联系/系统观）与源细则表格 (suite bundle lines 123–148) 完全对应；boundary_note 注明不累加。 | `suite_source_bundles/2026朝阳二模.md` lines 123–157, 502–536 | 保留 |
| **PASS** | 2026丰台二模 / 2026顺义二模 / 2026石景山二模 / 2026西城二模 Q16 multi-angle | 多角度保留符合三角度阅卷版要求，且每条 boundary_note 都注明"任选/不累加"，未把可选角度宣称为累加采分。 | JSONL lines 13–17, 28–35, 36–38 boundary_note | 保留 |
| **PASS** | 2026房山二模 Q18(2) (JSONL line 21) | "联系-发展-扬弃-否定-肯定"对应房山评标 OPC 的 5 个采分点；boundary_note 主动声明"题面未单独呈现，按细则保守表述"，处理审慎。 | `suite_source_bundles/2026房山二模.md` lines 53–56, 176–179 | 保留 |
| **PASS** | 2026通州一模 Q18 (JSONL lines 24–25) | "对立统一+辩证否定/守正创新"两条均限定为 2 分采分点，并明确"双创属文化表述、不并入哲学" — 边界处理干净。 | JSONL line 24–25 boundary_note + source_repair_basis | 保留 |

---

### Overall verdict

**Conditional PASS.**

- 上一轮硬伤（朝阳 Q21 主题、房山 Q16 题面、答案落点元话术、海淀二模 Q16 矛盾扩张、海淀一模 Q21 系统观念重复行）**绝大多数已闭环**；学生条目读起来确实可以写到卷面，不再是模板套话或评分细则口吻。
- 但仍有 2 个必修项卡住"无条件 PASS"：
  1. **2025海淀一模 Q21 → Q22 题号错位**（必须改号，否则学生按 Q21 找不到该题）。
  2. **2026海淀二模 source bundle 全是水印**，外审无法独立核验海淀二模 Q16 的角度授权（必须补可读源证据，或在 triage 中显式标 NEED_EVIDENCE 不再宣称已 PASS）。
- 另需收口 `COVERAGE_CLOSURE_MATRIX_V2.md` 的"35/35 COVERED" 措辞——目前 bundle 只放了 10 份，对外审是夸大声明，需要按 accepted 实际涉及套卷重新口径化。

修完上述两条硬项 + 一条措辞收口，方可签发 external PASS。
