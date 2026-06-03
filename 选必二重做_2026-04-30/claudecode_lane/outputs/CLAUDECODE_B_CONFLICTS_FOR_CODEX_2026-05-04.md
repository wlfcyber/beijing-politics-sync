# Lane B 对 Codex A 的冲突清单（待 Codex 本地裁决）

不修改 Codex A 文件。以下是 Lane B 提交给 Codex 的本地证据冲突，请 Codex Leader 在 `06_conflicts/` 主裁决文件内引用本文件并给出本地证据裁决意见。

## C-001 evidence_type=`paper_source` / `unknown` 不应等同于 `rubric matched`

- 现状：`FRAMEWORK_PLACEMENT_MATRIX_2026-05-03.csv` 中 22 条 `paper_source` + 4 条 `unknown` 都计入 `included` 而 `rubric pending: 0`。
- Lane B 主张：这 26 条应改为 `rubric_match_pending`，并在 QUALITY_REPORT 与框架文档"待补正式细则清单"中显式列出。
- 影响：当前"匹配 78"是 113 题中 78/113，不是 113/113；如果延续现状，框架文档的"高频示范题"可能用了缺细则的题。
- 列表见 `CLAUDECODE_B_SOURCE_AUDIT_MATRIX_2026-05-04.csv`。

## C-002 2024 海淀一模 第13题排除待复核

- Codex A 状态：`excluded_by_curation`（私法/程序法锚点不足）。
- Lane B 异议：题面涉及职业资格/劳动者保护，可能仍属选必二《劳动就业与职业边界》。建议 Codex 二次扫描题面后裁决。
- 证据等级：弱；不强制翻案，仅请求复核。

## C-003 选择题候选答案标签不统一

- 现状：框架文档第 5 题示例已用"仅有本地候选答案"，但其他章节出现该 9 题时，标签格式不一致。
- Lane B 主张：在合集与框架文档里统一"候选答案 X｜未锁定（answer_pending_official）"格式，避免将来误读为官方答案。

## C-004 扫描件 OCR 缺口

- 2026 东城一模 第10、11题 evidence_type=unknown，原因是只有"原卷扫描版.pdf"，未做按题号 vision OCR 切块。
- Lane B 主张：先对该扫描件做按题号 OCR，再纳入 framework 高频示范，否则保持 `rubric_match_pending`。

## C-005 模块边界排除：建议保留可追溯证据

- 3 道模块边界排除（2025海淀二模 Q17、2025西城二模 Q19、2026东城期末 Q19）当前在矩阵里只剩 1 行，未在框架文档显式记录"为何不进入"。
- Lane B 建议：在框架文档附录"模块边界排除清单"列出，并用一句话解释非选必二的设问关键词，避免后续审稿误以为遗漏。

## C-006 14 道 `included_needs_review` 未拆分前不应计入域频次

- 现状：14 题已计入域频次（合同/纠纷程序/人格权/知产/劳动/婚姻），与未拆小问的策展规则有张力。
- Lane B 主张：在频次统计中保留两套口径——"已拆小问入框"与"含待拆混合题入框"——避免高频假象。

## 不冲突项

- 总框架（一核二线三问四步 + 8 域）：Lane B 同意 Codex A 当前结构，无需重构。
- 113 入框总数、78 formal 匹配、9 候选答案、3 边界排除、域分布（25/20/17/15/13/11/10/2）：Lane B 复算一致。
- 命题路径反推抽样：Lane B 在 8 域上抽样均能解释，无 `proposition_path_uncertain` 必须新增。
