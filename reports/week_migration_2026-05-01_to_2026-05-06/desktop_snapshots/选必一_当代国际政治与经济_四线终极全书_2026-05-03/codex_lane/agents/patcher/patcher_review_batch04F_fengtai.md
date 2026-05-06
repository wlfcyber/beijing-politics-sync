# Batch04F 2025丰台二模 Patcher Review

time: 2026-05-03 CST
role: Codex A Patcher
student_doc_touched: no
fusion_files_touched: no
verdict: PASS_WITH_FIXES

## 读取范围

- `05_coverage/batch04F_fengtai_candidate_questions.csv`
- `codex_lane/agents/worker/worker_batch04F_fengtai_triage.md`
- `02_extraction/codex_extraction_logs/batch04F_fengtai_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04F_fengtai_prelim.csv`
- `fusion/merge_register_batch04F_fengtai_updates.md`
- `06_conflicts/batch04F_claudecode_conflict_resolution.md`
- `claudecode_lane/batch04F_fengtai_entries.md`
- `claudecode_lane/batch04F_conflicts_for_codex.md`

## 总结论

Batch04F 融合主行可以进入下一门槛：只收 2025丰台二模 Q20，且 FT01-FT04 与 P0 `20题.docx` 四个角度一一对应，没有把四个 2 分角度压成关键词，也没有把 FT02/FT03 或 FT04 过度合并成空泛标签。

但下游继承前必须处理两个小风险：Q21 的边界标签要统一为 `boundary_only / exhaustion-only`，不能被 ClaudeCode 原始条目简化成纯 `no_xuanbiyi`；FT04 若继承 ClaudeCode 原始文本，必须改用 `共商共建共享`，不要继承 `共建共商共享` 的错序。

## 必须修的点

1. Q21 标签统一：`05_coverage`、worker 与本地 evidence notes 均把 Q21 判为 `checked_boundary_only / boundary_only`，理由是综合等级题、定档主轴为“势”的智慧和综合论证，不提升选必一频次。`claudecode_lane/batch04F_fengtai_entries.md` 将其写成 `no_xuanbiyi`，下游不得照搬。最小修法：后续交叉表或总控登记统一写作 `Q21 = boundary_only/exhaustion-only，不入选必一主链，不计频次`。

2. FT04 术语词序防污染：P0/本地证据与 fusion 行使用的是 `共商共建共享` 或保留 `平等、开放、合作、共享` 及 `更加公正合理方向`。`claudecode_lane/batch04F_fengtai_entries.md` 中 FT04 出现 `共建共商共享`，下游学生稿和总表不得继承。最小修法：如写全球治理观，统一为 `共商共建共享的全球治理观`；如沿用 fusion 句，则保留 `中国推动构建人类命运共同体，遵循平等、开放、合作、共享等原则，同世界各国一起推动全球治理体制向着更加公正合理的方向发展`。

## 逐项复查

### 1. Q18/Q19(2)/Q21 排除与边界

PASS_WITH_LABEL_FIX。

- Q18：设问限定《经济与社会》，内容为提振消费，命中 `普惠` 属串扰，不入选必一。
- Q19(2)：设问限定《法律与生活》，内容为司法建议和 AI 法律边界，命中 `平衡` 属串扰，不入选必一。
- Q21：应保留为 `boundary_only`，不是选必一候选。其样例中虽有“一带一路/全球治理”等表达，但评分主轴不是选必一术语采分点。

### 2. Q20 四角度与 P0 对应

PASS。

- FT01 对应角度一：`最大发展中国家身份 -> 国际政治经济格局重要力量 -> 参与全球治理 -> 推动全球南方现代化`，解释链完整，未只存 `全球南方`。
- FT02 对应角度二：`积极参与国际组织 -> 联合国/金砖/G20/博鳌等平台 -> 全球治理体系的重要参与者、贡献者和改革者`，bucket 改为 `中国` 是正确的。
- FT03 对应角度三：`联合国常任理事国 -> 联合国宪章宗旨原则 -> 践行多边主义 -> 维护多边体制权威性和有效性`，bucket 为 `联合国`，与 FT02 已分开。
- FT04 对应角度四：`推动构建人类命运共同体 -> 平等、开放、合作、共享 / 共商共建共享 -> 全球治理体制向更加公正合理方向发展`，bucket 改为 `政治多极化` 可接受，并以 HMC/中国作交叉引用。

### 3. FT02 / FT03 桶位风险

PASS。

FT02 是中国通过多个国际组织平台参与全球治理的角色点，核心是 `中国`；FT03 是联合国常任理事国身份、联合国宪章和多边体制权威有效性，核心是 `联合国`。当前 fusion 表和 merge register 已明确拆开，没有把 `国际组织` 泛化吞掉 `联合国常任理事国`。

### 4. FT04 过度合并风险

PASS_WITH_WORDING_GUARD。

当前 fusion 行没有压成 `中国方案` 或 `全球治理方向` 这类低信息标签，仍保留了 `推动构建人类命运共同体`、`平等、开放、合作、共享`、`全球治理体制向更加公正合理方向发展`。建议下游继续按一个评分槽处理，不拆成 HMC、原则、方向三个频次；同时避免继承 ClaudeCode 原始条目的错序词。

### 5. 一材料多答题点与同核心合并

PASS。

Q20 同一材料包下确有四个独立 2 分角度，当前 FT01-FT04 四行完整保留，未漏收。合并方向也正确：FT01 并入中国身份/全球治理角色场景变体；FT02 作为 `重要参与者、贡献者和改革者` 高信息新表述保留；FT03 作为联合国桶表述积累；FT04 作为 HMC/全球治理原则与方向的同一评分槽保留。没有发现过度合并或欠合并的实质 blocker。

## 可放行点

- Q20 的评分依据来自 P0 formal marking docx，P3 试卷只作题面支持，未把普通参考答案冒充评分细则。
- FT01-FT04 的 `answer_sentence_fusion` 均是可写入答卷的解释链，不是单独关键词。
- `经济全球化“开放、包容、普惠、平衡、共赢”` 不属于本题新增核心，未被错误拉入 Batch04F。

## 下一步补丁清单

- downstream/register: Q21 统一标为 `boundary_only/exhaustion-only`。
- downstream/student-or-total ingestion: FT04 统一使用 `共商共建共享`，不得继承 `共建共商共享`。

## 返修复验

recheck_time: 2026-05-03 CST
recheck_verdict: PASS_AFTER_FIXES

只复验指定 downstream 文件。Q21 已在 merge register、conflict resolution 与 `COVERAGE_MATRIX.csv` 中作为 `boundary_only/exhaustion-only` 继承，不再丢失为普通 `no_xuanbiyi`；FT04 已写明下游统一使用 `共商共建共享`，不得继承 ClaudeCode 原始 `共建共商共享` 错序；FT01-FT04 的 `promotion_status` 均已改为 `candidate_with_fixes`。无新增必须返修项。
