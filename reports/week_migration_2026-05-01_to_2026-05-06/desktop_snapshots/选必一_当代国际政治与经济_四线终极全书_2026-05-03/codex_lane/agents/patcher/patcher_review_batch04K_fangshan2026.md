# Batch04K 2026房山一模 Patcher Review

time: 2026-05-04 CST
role: Codex A Patcher
cross_thread_guard: active
external_lane_outputs_used: no
student_doc_touched: no
fusion_files_touched: no
verdict: PASS_WITH_GUARD

## 读取范围

- `05_coverage/batch04K_fangshan2026_candidate_questions.csv`
- `codex_lane/agents/worker/worker_batch04K_fangshan2026_triage.md`
- `02_extraction/codex_extraction_logs/batch04K_fangshan2026_manual_evidence_notes.md`
- `fusion/scoring_atom_table_batch04K_fangshan2026_prelim.csv`
- `fusion/merge_register_batch04K_fangshan2026_updates.md`
- `SOURCE_LEDGER.csv` 中 2026房山一模行
- `COVERAGE_MATRIX.csv` 中 2026房山一模行
- 选必一 skill 与术语协议

## 总结论

Batch04K 2026房山一模 Q19 预融合可以带 guard 进入下一门槛。证据为 P0 `细则.docx`，试卷第10页题面已视觉核读；Q19 设问为“海南自贸港封关是如何助力国际循环”，不能机械并入 2026门头沟一模 Q20 的“为什么注入新动能/新活力”结构。当前 FS26-01 至 FS26-04 覆盖市场/消费侧、生产侧、投资侧、制度型开放中国方案侧四组机制，没有漏收一材料多答题点。

需要保留的 guard：manual evidence notes 记录细则有“1-5每个2分，总分不超过6”的计分备注。当前四组 fusion atom 作为预融合机制组可接受，但后续 A/B 或 Governor 闭合前，不得把四个 atom 解释成四个完全独立必答满分频次；必须继续保留“前三类机制有封顶、制度型开放/中国方案侧补足2分”的审计提示，直到确认细则原貌。

## 必须修的点

无正式文件必须返修项。保留上述计分 guard 即可。

## 逐项复查

### 1. 一材料多答题点

PASS。Q19 材料的“一线放开、二线管住、岛内自由”没有被压成单点，当前拆分与 worker/细则 notes 对齐：

- FS26-01：市场/消费侧，超大规模市场优势、降低成本提高效率、货物服务贸易升级、要素自由流动、资源优化配置、贸易投资自由化便利化。
- FS26-02：生产侧，技术研发、企业竞争力、产业升级、优化产业结构、融入全球产业分工和合作。
- FS26-03：投资侧，优化营商环境、吸引外商投资、引进来。
- FS26-04：制度型开放中国方案侧，制度型开放、以国内大循环吸引全球资源要素、国内国际两个市场两种资源联动效应、中国方案。

### 2. 市场 / 生产 / 投资 / 制度型开放中国方案

PASS。四组没有过度合并，也没有把同一评分块拆得过碎：

- 市场侧与贸易投资自由化便利化合并合理，保留 `货物、服务贸易升级`、`要素自由流动`、`优化资源配置`。
- 生产侧落到 `融入全球产业分工和合作`，没有把 `产业升级` 误当作必修二独立主链。
- 投资侧只有在 `吸引外商投资 / 引进来 / 助力国际循环` 语境中进入经济全球化机制，没有裸收 `营商环境`。
- 制度型开放和中国方案侧单列合理，因为它回答的是“封关制度安排如何助力国际循环”，不是一般开放口号。

### 3. 开放 / 引进来 / 营商环境边界

PASS_WITH_GUARD。`优化营商环境`、`引进来`、`产业升级` 等表达有必修二交叉风险，但当前 fusion 与 merge register 均把它们绑定到选必一语境：国际循环、外商投资、全球产业分工合作、贸易投资自由化便利化。未发现裸塞必修二主链的问题。

下游学生稿若继承，必须保留“营商环境 -> 吸引外资 -> 引进来 -> 助力国际循环”的链条；不能把 `优化营商环境` 单独列为选必一术语。

### 4. 两个市场两种资源方向

PASS。FS26-04 明确把 `两个市场两种资源联动效应` 限定在海南封关、开放/循环语境中正面赋分；merge register 也写明不得泛化到无关世界意义题。方向处理正确。

建议后续与 Batch04H/04G 统一方向标签：

- 中国侧开放/循环/开放型经济新优势：可正面使用。
- 世界意义题裸写“中国自身利用两个市场两种资源”：不得替代世界侧效果。

### 5. 答案句与设问触发

PASS。四个答案句都能回到设问“如何助力国际循环”：

- FS26-01 回到降低跨境贸易成本、提高通关效率、促进贸易投资自由化便利化。
- FS26-02 回到技术攻坚、竞争力、产业升级、融入全球产业分工合作。
- FS26-03 回到极简审批、一网通办、吸引外资、引进来。
- FS26-04 回到制度型开放、国内大循环吸引全球资源要素、两个市场两种资源联动、中国方案。

未发现答案句只有口号或脱离材料的情况。

### 6. Q16(1) / Q20 边界

PASS。Q16(1) 虽含高水平对外开放、一带一路、贸易自由化便利化等词，但设问属于《经济与社会》因地制宜服务大局题，只作边界记录。Q20 是综合等级题，世界意义中可出现中国智慧、中国方案，但没有独立选必一逐点细则，保持 boundary-only 正确。

### 7. SOURCE / COVERAGE 状态

PASS_WITH_PROCESS_NOTE。

- `SOURCE_LEDGER.csv` 对 Q19 标为 `P0_formal_scoring_rule_docx`，对试卷标为 `P3_visual_prompt_support`，证据分级合适。
- `COVERAGE_MATRIX.csv` 当前显示 Batch04K 仍为 `candidate_pre_ab_review`、Patcher/Governor pending，这是本报告写入前的流程状态，不是内容缺陷。
- Q16(1)、Q20 在 SOURCE/COVERAGE 中均为边界记录，没有混入主频次。

## 后台字段 / 学生稿污染

PASS_WITH_STRONG_GUARD。fusion CSV 中自然存在 `evidence_level`、`source_boundary`、`promotion_status`、`source_ledger_refs`、`candidate_pre_ab_review` 等审计字段；这些只应留在审查文件中。当前答案句本身没有路径、模型名、candidate、evidence、source refs 等后台话。

下游学生稿只能继承术语、设问触发、材料触发和答案句，不得复制 CSV 列名、证据层级、source id、candidate 状态或 Patcher/Governor 过程语。

## 可放行点

- 四个机制组完整保留，未漏一材料多答题点。
- `贸易投资自由化便利化`、`融入全球产业分工和合作`、`制度型开放`、`两个市场两种资源联动效应` 均保留高信息表达。
- `市场/生产/投资/中国方案` 没有被粗暴合并成一个“开放”标签。
- `营商环境` 与 `引进来` 已绑定国际循环和外商投资语境，边界可控。

## 后续继承提醒

- A/B closure 前优先复核细则中“1-5每个2分，总分不超过6”的原貌，避免误建频次。
- 学生版若使用本题，建议呈现为“市场循环、生产循环、投资循环、制度型开放方案”四类抓手，并标明前三类可组合、制度型开放方案另成高阶收束。
- `中国方案` 是本题制度型开放助力国际循环的结果表达，不应扩写成万能帽。
