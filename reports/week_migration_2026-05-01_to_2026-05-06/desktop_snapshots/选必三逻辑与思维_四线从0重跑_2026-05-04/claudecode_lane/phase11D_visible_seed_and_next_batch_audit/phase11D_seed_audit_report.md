# Phase11D 种子稿审稿（T1 Terminal ClaudeCode 可见窗口）

## 范围

- 输入：`09_student_draft/phase11D_seed_source_verified_04_REVIEW_ONLY.md`，共 8 条。
- 标准：`claudecode_lane/phase11C_bad_word_content_audit_visible/four_element_gold_contract.md`。
- 配套：`08_review/phase11D_seed_source_ledger.csv`、`08_review/phase11D_four_element_gate/phase11D_seed_source_verified_04_REVIEW_ONLY_four_element_gate.md`（机械闸口已 PASS，但不授权 Word/PDF/final）。
- 我作为 T1 Terminal 工人，只输出审稿反馈，不并入正文，不签发 Word/PDF/final，不替代 Codex 源核与 GPT-5.5 Pro 内容审。

## 总裁定

`PASS_SEED_FOR_GPT_REVIEW_ONLY`

8/8 条满足以下硬规则：

- `【材料触发点】` 含具体材料信号或原文引文（基本都用 `“”` 摘录）；不是话题标签。
- `【设问】` 看起来是真实题面，没有 Phase11C 失败样本里的三类模板假设问（已 grep 验证「本题要求结合材料说明其体现的思维方法 / 本题要求依据材料判断正确选项 / 本题要求识别或运用」均为 0）。
- `【为什么能想到】` 第一句基本以「本节点关注…」开头，节点专属，并解释为什么是这个小方法而不是相邻方法。
- `【答案落点】` 是「思维方法 / 术语 + 本题材料事实 + 因果 / 作用 / 结论」结构，不是「卷面要把…」式制作说明。
- 选择题（4 条中含选择性质：1, 5, 7, 8 行）均给出正项理由 + 诱人错项理由 + 陷阱类型。
- 全文 grep 未发现 Gold Contract 第五·禁止短语集中任何一项，未发现学生稿审计字段（`pass`、`yes`、`A-formal` 等）。
- 模块边界稳定：8 条均在选必三《逻辑与思维》思维主链/认识发展链/创新思维子方法/科学思维三特征/感性—抽象—具体链；没有把哲学题或纯形式逻辑题混进来。

## 解读：为什么是 `PASS_SEED_FOR_GPT_REVIEW_ONLY` 而不是 `PASS_FOR_MERGE`

- 本审稿为机械 + 启发式审稿，仅对照 Gold Contract 与禁止短语集；没有打开原 PDF 校对每一条材料引文是否 verbatim、设问是否逐字、答案是否与正式细则评分点对齐。
- `phase11D_seed_source_ledger.csv` 给出了源定位（如 012试卷 lines 199-203 + 012试卷 inline answer lines 681-698），但需要 Codex A 在源核环节逐条对齐，T1 不替代 Codex 源核。
- 真正进入 `09_student_draft/` 正文之前，必须再过 GPT-5.5 Pro 内容审、Claude Opus 4.7 Adaptive 改写、Governor / Confucius 闸口（见 `four_element_gold_contract.md` 第十条与 `next_rebuild_plan.md` Phase 11E）。

## 逐条 should_fix 提示（不是 must_fix）

以下提示只对 GPT 审稿与 Codex 源核有用；不属于 Gold Contract 必改项。

1. **2025 东城期末第18题第(2)问**
   - 答案落点末句「体现创新思维的思路新、方法新、结果新」需 GPT/Codex 核对：是细则原词还是脚本归纳。如果细则原词只列「思路新、方法新、结果新」其中之一，可调整。
   - 同节点同题在 `phase11B_batch01_student_body_30_REVIEW_ONLY.md` 已经存在审计版条目；正文化时建议合并 phase11D 卷面句 + phase11B 同类题索引，由 Codex 整合。
2. **2024 海淀二模第17题第(1)问**
   - 设问偏短：`结合材料，说明此次时间利用调查是如何体现科学思维的。`。请 Codex 用 027试卷 lines 202-224 复核原题是否还有「运用《逻辑与思维》知识」「分别从客观性、预见性等角度」之类限定语；如果有，应补回。
   - phase11A 把本题列为「科学思维 + 辩证思维 + 创新思维 三角度并列」复合题；本种子条目只取了科学思维一支。GPT 内容审需要明确：是按多节点拆 3 条，还是把题目限定在科学思维节点写一条 + 其余节点走索引。
3. **2024 海淀二模第17题第(2)问**
   - 答案落点已经把感性具体 → 思维抽象 → 思维具体的方向写对，应坚持「不能颠倒」的硬规则。建议 GPT 审稿时确认细则评分点对此三阶段是否各占独立分位。
4. **2026 顺义一模第19题第(2)问**
   - 这是 `xuanbisan-hard-rules-notebook.md` 第十三硬样本之一；本条目把客观性/预见性/可检验性三个特征全部覆盖了，建议保留。
   - 答案落点中「具有广阔应用空间和持续增长的市场潜力」这种判断属于细则要求时是合规的；不是细则原词时建议改为更克制的表述。
5. **2024 朝阳一模第7题**
   - 设问最后一句句号 `下列说法正确的是。`。原题选择题 stem 多以问号或左括号收尾；建议核对 030试卷 lines 76-84 原文，必要时改回「下列说法正确的是（   ）」。
   - 学生稿建议把四个选项原文也写出来，便于学生在题型族群里看清错项①、错项④的原文，而不是只看老师转述。
6. **2025 海淀期末第18题**
   - 「打造富有文化韵味的城市地标」一句若不在 015试卷 answer lines 146-147 范围内，建议改为更克制的「服务新型公共文化空间建设」。
   - 同化性迁移 vs 顺应性迁移的区分写法是 phase11A 的硬规则；本条目坚持「同化性迁移」是对的。
7. **2025 丰台期末第8题**
   - 设问偏短，结尾为句号；建议核对 040试卷 lines 110-125 原文。
   - 错项分析处建议把①「想象作为思维基本单元」、③「抽象思维主导」的具体陷阱类型都写明（已写「思维形态错配」是合格的，但可再细化为「形象思维基本单元误判」「形象/抽象主导误判」二类）。
8. **2026 通州期末第11题**
   - 题干已较完整。`【答案落点】` 中错项 A、B、D 的判断都正确，但建议在 GPT 审稿后把四选项原文（A 迁移和飞跃……；B 普遍—特殊—普遍……；C 感性具体—思维抽象—思维具体；D 类比推理—系统整合……）写入条目，便于学生在选择题陷阱库中复习。

## 学生稿干净度

8 条全部通过：

- 没有路径、line id、file id、`/Users/...`、`C:\...`。
- 没有 `yes`、`pass`、`filled`、`correct_option_chain`、`A-formal`、`B-choice-signal` 等审计字段。
- 没有 `评标`、`参考答案`、`答案写`、`可从……角度作答` 等审计话术。

## 模块边界检查

- 全部 8 条都在选必三《逻辑与思维》思维主链或同书认识链 / 创新思维子方法范围。
- 没有把必修四哲学题、选必一国政经题、选必二法律题混入。
- 边界陷阱条目（如「漫画从实际出发」类）未出现在本批种子里，符合 phase11D 第一波只取 source-stable A-formal/A-support 的策略。

## 与 Phase11A / Phase11B 的关系

- 8 条全部能在 `phase11A_student_body_PATCHED_REVIEW_ONLY.md` 或 `phase11B_batch01_student_body_30_REVIEW_ONLY.md` 中找到对应的「审计版条目」（材料信号 / 答题动作 / 易错陷阱 / 同类题索引）。
- 种子条目把审计版换成了哲学宝典风格的四要件、节点专属答案落点；同类题索引 / 易错陷阱栏建议正文化时由 Codex 从 phase11B 30-条版本回填，避免再造索引。

## 下一步建议

1. 把 8 条种子稿打包送 GPT-5.5 Pro 内容审 v1（哲学宝典风格 + 卷面句 + 节点专属 + 错项分析）。
2. GPT 反馈中所有 `must_fix_content` 由 Codex 回 030 / 027 / 028 / 012 / 015 / 040 / 006 试卷与细则源核；本 T1 lane 不替代源核。
3. v1 通过后才能由 Claude Opus 4.7 Adaptive 改写学生口径；Opus 不引入新事实。
4. v1 + Opus + v2 GPT 审稿全员 PASS 后再考虑批次扩展（见 `phase11D_next_batch_candidate_queue.csv`）。
5. `next_rebuild_plan.md` 中 Phase 11G Word 化在 phase11F Markdown 全员 PASS 之前一律不启动。
