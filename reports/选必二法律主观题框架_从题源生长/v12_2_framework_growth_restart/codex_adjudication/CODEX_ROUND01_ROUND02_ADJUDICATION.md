# Codex adjudication after real Round 01 + Round 02

Status: `candidate_pending_source_check`

This is not a final framework, not a baodian, not DOCX/PDF, and not TASK_COMPLETE.

## 1. Gate Record

Round 01 evidence pack:

- 42 core source-locked / recovered-locked subjective question chains.
- 5 `OPEN_OR_REFERENCE` records as boundary/reference only.
- 6 `FOUND_FOR_NEXT_BACKFILL` records as next-version candidates only.

Real model records now exist:

- GPT Round 01: `model_outputs/gpt_round01_independent_framework.md`
- Claude Round 01: `model_outputs/claude_round01_independent_framework.md`
- GPT critiques Claude: `cross_critiques/gpt_critiques_claude_round01.md`
- Claude critiques GPT: `cross_critiques/claude_critiques_gpt_round01.md`

Gate caution:

- Claude model label was visible as `Opus 4.7 Adaptive`.
- ChatGPT output was captured from the real ChatGPT web project, but the visible composer label captured by Codex was `专业`, not an independently visible exact `GPT-5.5 Pro` label. Treat the content as real ChatGPT web advice, but do not use it as a strict final-model PASS.

## 2. Core Adjudication

Local evidence wins over model agreement.

Both GPT and Claude converged on the same non-final verdict:

- `candidate_pending_real_call` / `candidate_pending_source_check`
- no final PASS
- no baodian
- no DOCX/PDF
- no TASK_COMPLETE

Codex verdict:

```text
Round 01 + Round 02 succeeded as a framework-growth council.
It produced a promoted candidate direction, not a final accepted framework.
```

## 3. Accepted Architecture

Accept the three-layer architecture below.

### Layer A. Method Spine

These are required thinking moves, not separate mother-question types:

1. 设问交付物识别  
   Evidence: most core cards are keyed by prompt action, such as 理由、意义、评析、完成表格、诉求能否支持、维权路径.

2. 事实转法词  
   Evidence: CC0025 maps 派单/签到/奖惩/结算 to 三从属性; CC0143 maps 隐蔽搭售 to 消费欺诈; CC0206 maps 唤醒词抢注/宣传 to 不正当竞争; CC0305 maps 监控公开 to 隐私权 and 虚假宣传 to 消费者欺诈.

3. 规则-事实-结论链  
   Evidence: nearly all 42 core chains reward element matching, responsibility/effect/procedure landing, or rule-to-value explanation.

4. 分链写作  
   Evidence: CC0077, CC0084, CC0137, CC0157, CC0180, CC0189, CC0213, CC0214, CC0325 require one table row, one case, one subject, or one claim per legal chain.

5. 规则生价值 / 手段-对象-效果  
   Evidence: CC0011, CC0019, CC0025, CC0045, CC0103, CC0131, CC0229, CC0283, CC0340 all require value meaning to be derived from concrete legal rules or judicial measures.

6. 反向筛查  
   Evidence: the `禁止命中` field repeatedly blocks wrong module jumps such as seeing 法院 and writing 必修三, seeing AI and only writing innovation slogans, or seeing consumer words and mechanically writing 退一赔三.

### Layer B. Student-Facing Prompt Entrances

Codex does not accept Claude's 8/9 entrances as-is, and does not accept GPT's 5 entrances if it merges 诉求支持 with ordinary 判决理由. The evidence supports 6 student entrances:

1. 表格 / 裁判要点 / 补链题：一格一链、一案一链  
   Strong cards: CC0077, CC0084, CC0137, CC0157, CC0180, CC0189, CC0213, CC0214, CC0289, CC0325.

2. 判决 / 裁判 / 责任分担理由题  
   Strong cards: CC0002, CC0025, CC0054, CC0119, CC0200, CC0364.  
   Rule: do not force `程序合法` as a fixed first step; use it only when the card evidence actually contains a procedure issue.

3. 诉求 / 请求能否支持题  
   Strong cards: CC0063, CC0143, CC0305, CC0373.  
   Rule: first make the support/not-support judgment, then split claims; do not merge this with ordinary 理由题.

4. 评析 / 认识 / 谈看法题  
   Strong cards: CC0051, CC0061, CC0238, CC0244, CC0254, CC0332.  
   Rule: one subject or one viewpoint per chain; do not write generic rule-of-law praise.

5. 意义 / 价值 / 作用 / 如何保护推动题  
   Strong cards: CC0011, CC0019, CC0025, CC0045, CC0103, CC0131, CC0150, CC0195, CC0229, CC0283, CC0340.  
   Rule: use `法律手段 -> 保护对象 -> 价值效果`, but every value statement must be tied to a card fact.

6. 调解 / 维权 / 纠纷解决 / 证据路径题  
   Strong cards: CC0125, CC0223, CC0245, CC0289, CC0092.  
   Rule: write path, evidence, claim, and boundary; do not answer with only "协商、调解、诉讼" as a slogan.

### Layer C. Open Containers

Keep the open-container layer. It prevents old v10-style false closure.

Current containers:

1. 6 next-backfill candidates: CC0251, CC0276, CC0277, CC0317, CC0318, CC0319.  
   Decision: cannot support core nodes until locked as PASS.

2. `OPEN_OR_REFERENCE` records from Batch 03.  
   Decision: may guide risk and boundary language, not core coverage.

3. New-technology / data / information-risk edge cases.  
   Decision: core cards like CC0137, CC0157, CC0206, CC0305 can support existing entrances; new cases such as CC0277 must stay pending until backfilled.

4. Format-clause / service-contract edge cases.  
   Decision: CC0084 can support current table/case-chain patterns; CC0317/CC0318 cannot enter the core until backfilled.

5. Mixed economy-law or module-boundary cases.  
   Decision: keep boundary warnings active; if a card is genuinely legal subjective content and already PASS, it can support a prompt entrance, but it must not inflate legal coverage with non-legal economics material.

## 4. Accepted From GPT

Accept:

- Stage 0: identify the prompt deliverable before choosing a legal rule.
- Fact-to-law translation as a teachable skill.
- Question-maker path analysis as a teacher-facing appendix.
- Red lines against final PASS, 65/70 style false closure, and using pending cards as core.
- The warning that Claude's "规则解释 / 识别法律问题 / 调解理由 / 减责理由" should not remain one independent trunk entrance.

Modify:

- GPT's 6 high-frequency actions are accepted as a method spine, not as the whole student-facing framework.
- GPT's 5 prompt entrances must split `诉求/请求能否支持` out from ordinary 判决/理由题.
- GPT's containerization of CC0195 and CC0051 is rejected: both are recovered/locked core evidence and should support main entrances with caution, not be thrown into containers.

Reject:

- Any framework that makes 6 actions alone the complete student framework.
- Any fixed "程序合法 first" recipe for all judgement-reason questions.

## 5. Accepted From Claude

Accept:

- Student-first entrance language.
- Table/case/subject/claim splitting.
- Evidence gaps and revision rules.
- Keeping next-backfill and reference records out of core.

Modify:

- Claude's 8 entrances are too many as a top-level student menu; compress into the 6 prompt entrances above.
- Claude's entrance ⑧ must be dissolved: 调解理由 goes to entrance 6, 减责理由 goes to entrance 2, 识别法律问题 goes to method spine + entrance 6, rule explanation goes to the relevant prompt entrance.
- Claude's ⑦A/⑦B split is useful internally, but should be presented as subtypes under entrance 5 rather than expanding the top-level menu.

Reject:

- Expanding from 8 to 9 top-level entrances after Round 02.
- Treating every rule-explanation phrasing as a standalone question type.

## 6. Pending Source Checks

Codex will not promote these until original text/rubric is checked again:

- CC0137: exact rubric boundary for AI copyright grid and credit-card contract grid.
- CC0289: whether "任选其一" belongs primarily to rights-protection path, table completion, or mixed entrance.
- CC0223: whether the main rewarded action is dispute-resolution path, legal-issue recognition, or two-case meaning extraction.
- CC0364: keep as judgement-reason evidence, but verify whether procedure legality is rewarded or only factual/no-impact reasoning is rewarded.
- CC0051: keep as recovered evidence for 评析/认识, but do not overgeneralize it into a large "legal change" trunk.
- CC0195: keep as core evidence for fairness/efficiency through collective consultation, but check whether it should sit under entrance 5 or a labor-rights subtype.
- CC0162 / CC0040 / CC0353 / CC0380 if used later: remain boundary candidates unless source-locked.
- All 6 next-backfill candidates remain outside the core until promoted by evidence.

## 7. Coverage Delta

Compared with v12.1 source cleanup, this v12.2 council adds:

- a real two-model growth loop, not a local Codex-only framework;
- a clean separation of method spine, student entrances, and open containers;
- explicit rejection of v10-style false exhaustive closure;
- a smaller student-facing top-level menu than Claude's 8/9, but broader coverage than GPT's 5 if 诉求题 is merged away;
- a direct path for the next local task: source-check the pending cards and then build a candidate framework sheet.

Remaining gaps:

- exact model label caution for ChatGPT web output;
- no final PASS until source checks and coverage matrix delta are completed;
- no final classroom document until Codex adjudication is converted into a checked framework version.

## 8. Next Required Action

Create `candidate_framework_v12_2_council.md` from this adjudication only after:

1. marking every accepted node with support cards;
2. marking every modified node with the reason for modification;
3. marking every rejected model suggestion in the advice log;
4. running a coverage check against the 42 core rows, 5 reference rows, and 6 next-backfill rows.

