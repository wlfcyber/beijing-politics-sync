# 选必一细则术语积累协议

Use this reference for 选择性必修一《当代国际政治与经济》主观题. The user wants a cumulative scoring-term document, not a normal answer explanation.

## 1. Source Hierarchy

Use sources in this order:

1. 正式评分细则、评标、阅卷细则、阅卷总结.
2. 明确讲分、标分、替换词、必答点的讲评材料.
3. User-confirmed scoring material.
4. Ordinary teacher reference answers only as support, never as `细则位置` unless confirmed.

If no scoring source is found, keep the question out of the main term table and record the blocker. Do not promote reference-answer wording into a scoring term.

## 2. Entry Format

Use this exact unit for every term:

```markdown
## <top-level bucket>
### <second-level heading, only if needed>
#### <third-level summary, only if needed>

**术语：<rubric original phrase(s)>**

- 完整设问：<copy the full question prompt>
- 细则位置：<year district exam + question + scoring section + exact point + score + required/optional status>
- 来源：<year district exam + question>
- 材料触发：<trigger logic>
- 答案句：<candidate answer-sheet sentence: scoring term + material fact + reasoning/result>
```

Required fields: `完整设问`, `细则位置`, `来源`, `材料触发`, `答案句`.

Forbidden field: `真题规律`.

`答案句` is not an explanation of how to answer. It is the sentence a candidate would write on the exam paper. It must include the scoring term, a concrete material fact from that question, and the causal/result link. Reject answers that only say a title "顺应时代潮流" or merely repeat the term.

## 3. What Counts As 术语

`术语：` records scoring-rule wording:

- Red/marked scoring terms.
- Rubric point terms.
- Explicit replacements or acceptable synonyms in the scoring source.
- Required theoretical statements in the marking rules.

`术语：` must not record:

- Your own summary.
- A material fact.
- A reference-answer landing if it is not the marked scoring term.
- A broad textbook phrase from another module.

Example:

- Correct: `术语：当前国际竞争的实质是以经济和科技实力为基础的综合国力较量；坚持创新驱动发展战略`
- Incorrect: `术语：全球产业链供应链稳定`

`全球产业链供应链稳定` can appear in `答案句` as the result, but it is not the accumulated term when the rubric marks `坚持创新驱动发展战略`.

## 4. Merge Rules

Merge entries when all are true:

- Same suite and question.
- Same scoring section or scoring point.
- Same score layer.
- Same answer function.
- Same framework placement.

For student-facing six-bucket indexes, merge more aggressively by scoring core:

- Same textbook core, same scoring function, or same answer role must appear as one core point.
- But the merge must still be student-facing: the wording must be close enough to substitute on the answer sheet, or the scoring source must explicitly list the phrases as alternatives in the same point. Do not merge merely because two terms are conceptually related.
- Different wording from different questions becomes `表述积累`, not separate rows.
- Keep source and trigger differences under the merged point.
- Do not let tiny wording differences create fake new terms.
- The merged `核心采分点` name must preserve the highest-information scoring wording. Do not collapse it into a vague container label. For example, use `推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展`, not merely `经济全球化正确方向`.

Examples:

- `时代主题`, `和平与发展`, `和平与发展仍是时代主题`, and `中国做法符合和平与发展时代主题` are one core point: `和平与发展仍是时代主题`. The other phrases are expression variants.
- `推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展` and `经济全球化方向：普惠、平衡、共赢` are one core point, and the core point name should preserve `开放、包容、普惠、平衡、共赢`.
- `合作共赢的新型国际关系`, `推动建设合作共赢的新型国际关系`, and `体现合作共赢、互利共赢、共享发展成果` should be归并 under the same `新型国际关系/合作共赢` core when their answer function is the same.

Negative economic-globalization example:

- Do not put `开放型世界经济`, `开放型经济`, `创新型、开放型世界经济`, `全球经济治理和规则制定`, `多边贸易体系`, `普惠包容的经济全球化`, and `贸易自由化` into one core just because they all support opening or globalization. Keep them as separate nodes unless the rubric itself lists them as alternatives in one scoring point; even then, preserve the exact grouped rubric phrase as its own node.

Preferred student-facing merged unit:

```markdown
| 核心采分点 | 来源题目 | 表述积累 | 迁移用法 |
|---|---|---|---|
| 和平与发展仍是时代主题 | 2026通州Q20；2026顺义Q20；2026朝阳一模Q20 | 和平与发展仍是时代主题；顺应和平与发展的世界大势；中国做法符合和平与发展时代主题 | 遇到倡议、合作、中国方案为什么正当或能成立，先判断是否需要写时代背景。 |
```

Do not split parallel rubric phrases that form one scoring point. For example:

```markdown
**术语：中国作为联合国创始会员国 / 安理会常任理事国；世界上最大的发展中国家 / 国际政治经济格局中的重要力量**
```

This is one term entry if the rubric places all phrases under the same `中国的地位` point.

Second-level and third-level headings are only containers. Create them only when they prevent confusion. If a phrase such as `中国的联合国身份与国际格局地位` is useful, put it as a third-level heading, not after `术语：`.

## 5. 材料触发 Rules

`材料触发` must answer: why does this question require this scoring term?

Write the logic in this order:

1. What the prompt asks: reason, deep logic, measure, meaning, role, relation, or evaluation.
2. What relation the material sets up: cooperation, competition, opening, governance, UN-China relation, development, security, etc.
3. Why that relation triggers the term.

Do not merely rewrite the material and append "therefore use this term."

Example for `共同利益`:

- Good: `设问问“南南合作典范的深层逻辑”，实质是在问合作为什么能够成立、为什么能够持续。回答合作成立的原因时，必须先写国家间共同利益是合作的基础，再把科技小院满足全球南方农业发展需求接上。`
- Bad: `材料写科技小院走向多个全球南方国家，帮助当地农业治理、绿色发展和人才培养，所以体现共同利益。`

## 6. Framework Placement

### 时代背景

Put broad world conditions here:

- 和平与发展仍是时代主题.
- 经济全球化、世界多极化深入发展 as background.
- 霸权主义、强权政治、单边主义、贸易保护主义、逆全球化.
- Global governance challenges when the rubric uses them as the situation.

### 理论

Put explanatory principles about international relations here:

- 国家利益、国家安全.
- 共同利益是国家合作的基础.
- 国际竞争的实质是以经济和科技实力为基础的综合国力较量.
- 综合国力、科技实力、经济实力.
- `共同利益是合作的基础` when used as why cooperation works. Do not use bare `合作共赢` as a theory-bucket default.

If the phrase answers "why competition/cooperation happens", place it in `理论`.
If the phrase is `新型国际关系` or `合作共赢的新型国际关系`, it is not a theory bucket item. Place it in `政治多极化` because it answers the direction of international relations and international order. If the cooperation-win phrase is about trade, markets, supply chains, resources, rules, or open platforms, place it in `经济全球化`; if it is about China's responsibility, shared opportunities, developing-country livelihood, or development cooperation, place it in `中国`.
If the phrase is `独立自主和平外交政策`, `独立自主的基本立场`, `和平共处五项原则`, or `对外关系基本准则`, place it in `中国`, because it answers China's foreign-policy stance and action. If `独立自主 / 自力更生 / 自主可控 / 发展主动权` appears in technology, industry-chain, security, or development-capacity contexts, also place it in `中国`; do not keep it in the theory bucket.

### 经济全球化

Put mechanisms of global economic operation here:

- 贸易和投资自由化便利化.
- 商品、服务、资本、技术、人员等生产要素跨国流动.
- 两个市场两种资源.
- 国际分工与协作.
- 推动经济全球化朝着开放、包容、普惠、平衡、共赢方向发展.

If the phrase answers "how international economic circulation, opening, or resource allocation works", place it here.

Within this bucket, classification is expression-sensitive. `推动建设开放型世界经济` is not the same student-facing node as `提高开放型经济水平`, `创新型、开放型世界经济`, `积极参与全球经济治理和规则制定`, or `促进贸易自由化便利化` unless the scoring source explicitly makes them same-point alternatives.

Split `积极参与全球经济治理和规则制定` by answer function: enterprise outbound-rule environment, high-standard economic/trade rules and international-standard voice, developing-country representation and voice, and multilateral trade system are not one broad node. Keep `推动普惠包容的经济全球化 / 建设开放型世界经济 / 促进贸易自由化` together only when the rubric explicitly says they are same-point alternatives such as "任意1点1分".

### 政治多极化

Put international order and governance-orientation terms here:

- 构建新型国际关系.
- 合作共赢的新型国际关系 / 相互尊重、公平正义、合作共赢的新型国际关系.
- 共商共建共享的全球治理观.
- 国际关系民主化.
- 反对单边主义、霸权主义、强权政治.
- 推动构建人类命运共同体 when the emphasis is global political order.

### 中国

Use existing second-level headings:

- 政策
- 智慧
- 责任
- 外交政策：独立自主和平外交政策、独立自主的基本立场、和平共处五项原则、对外关系基本准则、维护世界和平促进共同发展的宗旨和目标.
- 发展主动权：独立自主、自力更生、自主可控、发展主动权、核心技术攻关 when the question asks how China acts under external pressure or industrial-chain risk.

Add reluctant second-level headings only when needed:

- 地位: China identity, status, and weight in the international system.

### 联合国

Use for:

- 联合国地位和作用.
- 《联合国宪章》宗旨和原则.
- 实践多边主义的最佳场所.
- 以联合国为核心的国际体系.
- 联合国成为中国开展多边合作的主要舞台.
- 中国与联合国相互需要的 relation terms.

## 7. Module Boundary

Do not put these 必修二 terms in the 选必一 main table:

- 扩大国际市场.
- 推进高水平对外开放.
- 落实开放发展理念.
- 新发展理念、高质量发展、现代化产业体系 when the scoring source is clearly 必修二.

If a mixed question contains them, record them outside the 选必一 main table as `模块边界：必修二`.

## 8. Sample Entries

### A. 2025海淀二模第21题

## 中国
### 地位
#### 中国的联合国身份与国际格局地位

**术语：中国作为联合国创始会员国 / 安理会常任理事国；世界上最大的发展中国家 / 国际政治经济格局中的重要力量**

- 完整设问：结合材料，运用《当代国际政治与经济》知识，阐释“中国需要联合国，联合国也需要中国”。
- 细则位置：2025海淀二模第21题，“联合国需要中国”部分，第1点“中国的地位”，1分。
- 来源：2025海淀二模 第21题
- 材料触发：设问要求论证“联合国也需要中国”，不是只说明中国参与了联合国事务，而是要先说明中国为什么有资格、有分量成为联合国事业的重要力量；所以同一采分点要合并写中国在联合国中的身份和国际格局中的地位。
- 答案句：中国作为联合国创始会员国和安理会常任理事国，同时是世界上最大的发展中国家、国际政治经济格局中的重要力量，能够为联合国事业和全球治理提供重要支持。

### B. 2026朝阳一模第20题

## 理论

**术语：当前国际竞争的实质是以经济和科技实力为基础的综合国力较量；坚持创新驱动战略**

- 完整设问：结合材料，运用《当代国际政治与经济》知识，阐述中国为什么能为全球发展注入稳定性和正能量。
- 细则位置：2026朝阳一模第20题阅卷细则，第①点，2分（1+1），标注为必答点。
- 来源：2026朝阳一模 第20题
- 材料触发：设问问“中国为什么能”提供稳定性和正能量，需要回答能力来源；材料呈现中国科技创新和产业能力时，触发的是国际竞争实质与中国创新驱动带来的综合国力支撑，而不是把“全球产业链供应链稳定”当作要积累的细则术语。
- 答案句：当前国际竞争的实质是以经济和科技实力为基础的综合国力较量，中国坚持创新驱动战略，科技实力日益增强，因而能够为全球产业链供应链稳定和全球发展提供支撑。

### C. 2026顺义一模第20题

## 理论

**术语：共同利益**

- 完整设问：结合材料，运用《当代国际政治与经济》知识，阐述科技小院成为南南合作典范的深层逻辑。
- 细则位置：2026顺义一模第20题评标，“共同利益”，1分，标注为必答。
- 来源：2026顺义一模 第20题
- 材料触发：设问问“南南合作典范的深层逻辑”，实质是在问合作为什么能够成立、为什么能够持续；回答合作成立原因时，必须写共同利益这一理论基础，再结合科技小院回应全球南方国家农业发展和可持续发展需求。
- 答案句：国家间共同利益是国家合作的基础，科技小院契合全球南方国家提升农业生产、培养人才和实现可持续发展的共同需求，因此能够成为南南合作典范。

## 9. Batch Acceptance Checklist

Before a batch is accepted:

- No entry lacks `细则位置`.
- No `术语：` phrase is invented.
- Same scoring point has not been split into multiple entries.
- Same scoring core across questions has been merged, with wording variants kept as expression accumulation.
- No 必修二 term has entered the 选必一 main table.
- `材料触发` is question-driven, not material-summary-driven.
- `答案句` is answer-sheet prose, not backstage prose. It must not contain `设问`, `细则`, `证据层级`, `v7`, `本题需要`, `采分点`, or similar production/audit wording.
- Every repeated term accumulates multiple source-trigger cases under one term when the scoring function is genuinely the same.
