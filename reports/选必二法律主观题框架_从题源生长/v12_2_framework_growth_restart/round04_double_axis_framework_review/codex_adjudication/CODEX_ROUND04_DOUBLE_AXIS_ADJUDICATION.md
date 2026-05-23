# Codex Round04 Double-Axis Adjudication

Date: 2026-05-23

Status: `v12_2_frozen_v13_0_double_axis_required`

## Gate Record

Round04 was triggered by the user's objection that v12.2 looked useful as a question-action framework but might not be a truly good legal baodian framework when compared with the earlier user framework.

The first ChatGPT CDP-manager capture is explicitly not counted:

- `model_outputs/gpt_round04_double_axis_framework_review_web_cdp_raw.md`
- Status: `INVALID_FOR_GATE_WRONG_CHATGPT_ACCOUNT`
- Reason: the user identified that browser/profile as a non-Pro ChatGPT account.

The valid Round04 advisor captures are:

- GPT Pro web: `model_outputs/gpt_round04_double_axis_framework_review_pro_web_raw_fullpage_clipboard.md`
- GPT Pro visible screenshot: `model_outputs/gpt_round04_pro_web_visible_output_screenshot.png`
- Claude Opus 4.7 Adaptive web: `model_outputs/claude_round04_double_axis_framework_review_opus47_web_raw_fullpage_clipboard.md`
- Claude visible screenshot: `model_outputs/claude_round04_opus47_web_visible_output_screenshot.png`

Both valid model lanes were user-visible web/app lanes, not Codex simulation.

## Model Verdicts

GPT Pro verdict:

`UPGRADE_TO_DOUBLE_AXIS`

Key instruction: keep E1-E6 as the B axis, immediately add an A axis for legal relationship/content, and do not allow rows without double-axis labeling into v12.3/v13.0.

Claude Opus 4.7 Adaptive verdict:

`UPGRADE_TO_DOUBLE_AXIS`

Key instruction: freeze v12.2, build v13.0 with A axis as the main legal relationship/content axis and B axis as the renamed E1-E6 question-action axis. Re-label all 42 locked rows and require `secondary_entry_counts` none to become 0.

## Codex Evidence Adjudication

Codex accepts the shared GPT/Claude critique.

Reason:

1. The v12.2 traceability matrix has 42 locked rows, but each row is labeled only by the six question-action entrances. This proves coverage for answer-action routing, not a legal-knowledge baodian.
2. The earlier user framework and framework-architect findings already contained the missing legal relationship/content axis: civil legal relationship, personal/property rights, contracts, intellectual property, tort, marriage/family/inheritance, labor/consumer/market order, and dispute-resolution procedure.
3. E5 is too large as a primary node. Its 11 rows mix labor, governance, market, family, IP, and other legal objects under the shared output action of "meaning/value/protection".
4. E2 and E3 overlap as legal-claim/court-judgment actions and should share the same legal relationship/content substrate.
5. The source-checked Round03 boundary patches themselves used legal-relationship language. That means the content axis was already being smuggled in as a patch rather than made explicit.

## Accepted Structural Decision

v12.2 is frozen as a source-checked and rendered baodian candidate, but it is no longer accepted as the final high-quality framework for the legal baodian.

The next accepted framework target is:

`v13.0_double_axis_framework_candidate`

Top-level structure:

- A axis: legal relationship/content axis, primary baodian axis.
- B axis: question-action/proposition-path axis, preserving v12.2 E1-E6 as renamed B1-B6.
- Meaning/value output: not a standalone main trunk; it becomes a controlled output slot inside A x B cells and must be triggered by fact, rule, or governance target.

## Working A Axis

The initial A axis for re-labeling the 42 locked rows is:

- A1 民事法律关系总论: 主体、客体、内容、行为能力、权利义务。
- A2 人身权与人格权: 生命健康、姓名、肖像、名誉、隐私、个人信息等。
- A3 物权与相邻关系: 所有权、用益物权、担保物权、相邻关系。
- A4 合同: 成立、生效、履行、变更、违约责任、免责。
- A5 知识产权与市场竞争接口: 著作权、专利、商标、不正当竞争接口。
- A6 侵权责任: 要件、归责、举证、责任方式、边界。
- A7 婚姻家庭与继承: 夫妻、父母子女、财产、继承、遗产债务。
- A8 劳动关系: 劳动合同、劳动权益、劳动争议解决、公平与效率。
- A9 消费者权益与经营秩序: 消费者权利、食品安全、惩罚性赔偿、市场秩序。
- A10 多元纠纷解决与诉讼程序: 和解、调解、仲裁、诉讼、代理/辩护、上诉期限。

This is a starting adjudicated axis, not yet final. Nodes with insufficient row support must be merged or marked `待证据补充` during v13.0 re-labeling.

## Working B Axis

The v12.2 six entrances are preserved as B-axis answer actions:

- B1 = E1 表格/裁判要点/补链。
- B2 = E2 判决/裁判/责任理由。
- B3 = E3 诉求能否支持, low-frequency subpath.
- B4 = E4 评析/认识/观点。
- B5 = E5 意义/价值/保护/推动, no longer a large catch-all.
- B6 = E6 调解/维权/纠纷解决路径。

The Round03 boundary patches remain inherited. They may not be silently deleted.

## New Governance Gates

v13.0 must not be promoted unless:

1. Every locked core row has both an A-axis and B-axis label.
2. The new traceability matrix has no `secondary_entry` or content-axis equivalent set to `none`.
3. Every enabled A-axis node has enough row support or is explicitly marked as an open/pending node.
4. Every answer skeleton states: legal relationship/content, material trigger, rule/element, answer action, conclusion, and conditional value/meaning output.
5. Open-container/reference-only rows stay outside the locked core and are not promoted by double-axis enthusiasm.
6. v12.2 files remain preserved as the rollback baseline.

## Next Codex Action

Build v13.0 in a new output directory. Start by re-labeling the 42 locked rows into A x B, then rewrite the framework chapter and all-question analysis under the double-axis structure. Do not overwrite v12.2.
