# 发给 GPT 网页「必修四喂细则」项目中选必二计划对话的进度同步稿

给你同步一下“选必二《法律与生活》主观题框架从题源生长工程”的最新进度，供你接着做规划/监督用：

1. 证据层已经过 Codex A + ClaudeCode B 双线抽取与合并审计，不是单线结果。`missing17` 已重查：原 `70` merged candidates 中，正式口径为 `65 formal`、`5 reference_only`、`0 missing`；后续边界恢复又把误收、父题、待核题剥离。

2. GPT-5.5 Pro 和 Claude Opus 4.7 Adaptive 的开放观察、交叉验证、代码本、候选框架都已经真实跑过并保存。GPT boundary recovery 也已捕获，修正了 `CC0094`、`CC0229`、`CC0250` 等边界问题。

3. 当前已形成 boundary-patched canonical corpus：
   - 路径：`/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/boundary_patched_20260519/`
   - `53` 道 framework-ready 主观题
   - `535` 个材料原子
   - `53` 个设问原子
   - `319` 个细则原子
   - 打包：`04_merge_audit/boundary_patched_canonical_corpus_20260519.zip`

4. 题量口径现在是：`37 PASS`，`11 PASS_RECOVERED`，`5 OPEN_OR_REFERENCE`。不能再说“只有35/37题”，但也不能把原始 `70` 个 merged candidates 全部说成闭合正文样本。

5. 关键边界修复：
   - `CC0229_2026_东城_一模_18`：已修正 rubric atoms，用 `F0153/F0146` 的知识产权、诉讼调解、惩罚性赔偿、恶意诉讼等 8 条法律细则替换掉旧的逻辑/经济串页；patched corpus 和 DOCX XML 中已清除“逃逸粒子/创新资源集聚/空间布局精准/全链条产业生态”等坏词。
   - `CC0305_2026_海淀_一模_18_3`、`CC0373_2026_顺义_一模_18`、`CC0380_2026_顺义_二模_18_2`：已拆分为法律小问入库。
   - `CC0250_2026_丰台_一模_19`：剔除，不是选必二法律主观题。
   - `CC0094_2025_东城_期末_19_3`：只可能保留相邻关系 2 分法律层，当前仍 `split pending`，不进入闭合。
   - `CC0259_2026_丰台_期中_19`：缺正式法律细则，`pending`。
   - `CC0118_2025_丰台_期末_18_2`：可能与 `CC0119` 重复或错配，`pending`。

6. 最终产物已更新：
   - 宝典 Markdown：`12_final_baodian/选必二法律主观题满分宝典.md`
   - Canonical Word：`12_final_baodian/选必二法律主观题满分宝典.docx`
   - 53 行运行表：`12_final_baodian/question_by_question_framework_runs_boundary_patched.csv`
   - 53 行材料触发表：`12_final_baodian/material_trigger_bank_boundary_patched.csv`
   - 满分句库：`12_final_baodian/full_score_sentence_bank.csv`
   - 覆盖矩阵：`QUESTION_COVERAGE_MATRIX.csv`
   - 接受报告：`FINAL_ACCEPTANCE_REPORT_BOUNDARY_PATCHED.md`

7. Word QA 已完成：Microsoft Word 打开/保存 DOCX，导出 PDF，PDF `198` 页全部渲染，无疑似空白页。QA 报告在 `12_final_baodian/DOCX_QA_WORD_PDF_RENDER.md`。

8. 当前状态：`BOUNDARY_PATCHED_RELEASE_CANDIDATE`。可以基于 `53` 行 patched corpus 做后续教学化压缩和计划；不可以把 pending 的 `CC0094/CC0259/CC0118` 硬塞进闭合数，也不可以把 open/reference 行当作核心证据单独支撑框架节点。

请你接下来如果参与规划，只围绕这个 `53` 行 patched corpus 做监督和计划；如果要扩展，先从三个 pending case 的回源补证开始。

