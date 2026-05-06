# Batch04G 2025门头沟一模 Patcher Review

time: 2026-05-03 CST
role: Codex A Patcher
scope: Codex A local prelim only; ClaudeCode B not reviewed
student_doc_touched: no
fusion_files_touched: no
verdict: PASS

## 读取范围

- `05_coverage/batch04G_mengtougou_candidate_questions.csv`
- `codex_lane/agents/worker/worker_batch04G_mengtougou_triage.md`
- `02_extraction/codex_extraction_logs/batch04G_mengtougou_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04G_mengtougou_prelim.csv`
- `fusion/merge_register_batch04G_mengtougou_updates.md`

## 总结论

2025门头沟一模 Q19 可以作为 Batch04G 本地 prelim 候选进入下一门槛。题面明确要求运用《当代国际政治与经济》，评分来源为 P0 `细则.doc`，P3 试卷只作题面/材料支持。MTG01-MTG04 与四个 2 分角度一一对应，均保留了 1+1 结构，没有把一题四角度压成关键词，也没有过度合并为模糊的 `中国方案` 或 `全球治理方向`。

## 必须修的点

无。

## 逐项复查

### 1. Q19 题面与证据等级

PASS。候选表、worker triage 与 evidence notes 一致确认：题面为 `结合材料，运用《当代国际政治与经济》的相关知识，分析中国做“赋能型大国”的世界意义？`，评分源为 `2025门头沟一模/细则/细则.doc`，属于 P0 formal scoring source。`试卷.pdf` 只作为 P3 paper text support，未冒充细则。

### 2. 四个 2 分角度与 1+1 结构

PASS。

- MTG01：市场红利 1分 + 共享发展机遇/经济全球化方向 1分，保留 `广大而充满创新活力的市场`、`共享发展机遇`、`贸易投资自由化便利化` 和完整五词方向。
- MTG02：科技助力发展中国家 1分 + 自主发展能力/民生改善/全球可持续发展 1分，未简化成“中国技术先进”。
- MTG03：国际公共产品/中国智慧中国方案 1分 + 维护和平、促进共同发展、推动构建人类命运共同体 1分，已标明同角度不拆频。
- MTG04：文明平等互鉴/全人类共同价值 1分 + 国际秩序或全球治理体系更加公正合理 1分，保留价值体系和秩序方向双层。

### 3. 同核心合并

PASS。

- MTG01 正确并入经济全球化完整方向核心，fusion 答案句保留 `推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展`，没有压成 `全球化互利共赢` 低信息标签。
- MTG03 正确并入国际公共产品 / 中国智慧中国方案 / 人类命运共同体相关核心，但仍保留 1+1 采分结构，不拆成多个频次。
- MTG04 正确并入政治多极化下的国际秩序和全球治理体系公正合理方向核心，并保留 `文明平等互鉴`、`全人类共同价值`，没有只留 `全球治理方向`。

### 4. 边界警告

PASS。

边界足够强：`充分利用两个市场两种资源` 在 candidate、worker、evidence notes、MTG01 boundary note、merge register 中均标明本题不给分；`国家关系民主化`、`世界多极化`、`多边主义` 在 evidence notes、worker、MTG04 boundary note、merge register 中均标明不能单独得分。下游学生稿应继续继承这些警告，避免把教材通用词当成本题得分点。

## 可放行点

- 一材料多答题点未漏收：Q19 四个角度均已入 MTG01-MTG04。
- 同类项未过合并：MTG01/03/04 均保留最高信息量表述和本题场景触发。
- 同类项未欠合并：MTG03 未拆成公共产品、中国方案、HMC 三个独立频次；MTG04 未把新型国际关系或公正合理秩序拆成额外必答频次。
- 答案句均为解释链，未仅列关键词。

## 后续继承提醒

- MTG01 后续正文优先继承完整表述：`推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展`。
- MTG03 作为一个 1+1 评分角度处理，不拆频。
- MTG04 中 `合作共赢的新型国际关系` 只能作为同角度可用表述，不得替代 `文明平等互鉴 + 全人类共同价值 + 公正合理国际秩序/全球治理体系` 主链。

## A/B 闭合复验

recheck_time: 2026-05-03 CST
recheck_verdict: PASS_AFTER_AB_CLOSURE

只复验指定 A/B 闭合文件。ClaudeCode B 的四个 merge flags 已在 `06_conflicts/batch04G_claudecode_conflict_resolution.md` 中逐项裁定：MTG01 并入经济全球化完整方向核心，MTG03 作为公共产品/中国智慧中国方案到 HMC 的 1+1 场景积累，MTG04 的公正合理国际秩序并入 Batch04F FT04 家族，同时保留文明平等互鉴/全人类共同价值子点。`fusion/scoring_atom_table_batch04G_mengtougou_prelim.csv` 中 MTG01-MTG04 均已设为 `candidate_with_fixes`，`merge_register` 和 `COVERAGE_MATRIX.csv` 已同步边界警告与候选状态。无新增必须返修项。
