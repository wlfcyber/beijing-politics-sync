# Claude V17 Real Review Adjudication -> V18 Patch

time: 2026-05-26T11:45:00+08:00

review_raw: `09_external_review/CLAUDE_REAL_REVIEW_RAW_FORMAT_V17_20260526.md`

Claude verdict: `P1_REVISE`

Codex adjudication verdict: `ACCEPT_P1_STYLE_REPAIR_NOT_FINAL`

## Accepted Into V18 Student Body

1. 推理选择题 `【正确理由】` 以 `XX模 第N题 选 X。` 批量开头，确实不像哲学宝典学生正文。
   - action: 已移除 36 道选择题的答案册式来源前缀。
   - V18 body rule: 选择题只保留 `答案选X。` + 规则理由 + `错项分析：...`。

2. 推理选择题 7 标签过重，尤其 `【完整题干】/【完整选项】/【答案】/【正确理由】/【诱人错项和错因】` 是 QA 拆分痕迹。
   - benchmark check: 哲学宝典本体选择题使用 `【材料触发点】/【设问】/【为什么能想到】/【答案落点】` 四段式，并把选项放在 `【设问】` 下。
   - action: 已把推理册 36 道选择题全部改回四段式：题干和选项并入 `【设问】`，答案、正确理由和错项陷阱并入 `【答案落点】`。

3. `【为什么能想到】+【正确理由】+【诱人错项和错因】` 三段复述过重。
   - action: 已合并后两段，选择题正文从七段压回四段；保留完整题干、完整选项、答案和错项分析，但取消重复标签。

4. 推理册 TOC 过像元数据标签树。
   - action: 已把充分条件、必要条件、三段论等密集 H2 改成教学路径名，如 `有效式：前件成立，结论跟着走`、`四概念：同一个词前后换了对象`、`有效形式与真实前提要分开`。
   - builder action: 推理册目录改为从当前 Markdown 标题自动收集，避免旧手工 TOC 保留 V17 标签树。

5. `题目同时把...放进选项` 这类出题人视角口吻。
   - action: 已全册清零该类表达，改为学生视角的 `选项还会混入...` 或同类句式。

## Rejected Or Boundary

1. “材料触发点”本身应删除。
   - adjudication: reject for this run.
   - reason: 用户明确要求思维宝典讲“触发”，哲学宝典本体也使用 `【材料触发点】`；该标签不是本 run 后台泄漏。

2. 前言必须补正文。
   - adjudication: reject.
   - benchmark check: `/Users/wanglifei/Desktop/哲学宝典最终版 5.2双终极融合版_目录页码美化版_副本.docx` 中 `前言` 后直接进入 `目录`，当前空前言与 benchmark 一致。

3. 末页必须补 `全书完/结语/祝考场顺利`。
   - adjudication: reject as hard requirement.
   - benchmark check: 哲学宝典本体末尾也是最后一题 `【答案落点】` 收束，没有独立结语页。
   - note: 若后续用户要求可另做“考前方法卡”，但不能以此作为哲学对齐硬门槛。

## Source And Answer Recheck

- `00_control/QUESTION_COVERAGE_MATRIX.csv` 中推理选择题 body rows = 36；当前 MD choice headings = 36。
- 其中 29 道在 coverage decision text 中显式出现官方/正式答案字母，当前 MD 答案字母逐项匹配，mismatch = 0。
- 其余 7 道 coverage 标为 A-formal/B-choice-signal source_locked；当前未发现 coverage 与 MD 的字母冲突。
- `claudecode_lane/entries/reasoning_choice.jsonl` 有两处与 control ledger 冲突：
  - `2026石景山一模 第6题`: jsonl 为 B，但 `00_control/QUESTION_COVERAGE_MATRIX.csv` 明确 `官方答案锁定 Q6=D`，MD 采用 D。
  - `2026海淀二模 第7题`: jsonl 为 C，但 `00_control/QUESTION_COVERAGE_MATRIX.csv` 明确 `教师版原题和答案表锁定 Q7=A`，MD 采用 A。
  - adjudication: 以本 run control ledger/source-lock 为准，jsonl 记为 stale assistant-lane residue，不回改学生正文。

## V18 Boundary

V18 是 Codex 根据 Claude V17 `P1_REVISE` 做的本地返修，不是 Claude/GPT Pro PASS。GPT Pro 仍为 `blocked_advisor_not_completed`；Claude V17 真实结论仍记录为 `P1_REVISE`。
