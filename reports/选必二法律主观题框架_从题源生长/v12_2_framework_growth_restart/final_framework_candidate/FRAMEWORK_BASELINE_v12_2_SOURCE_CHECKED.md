# 选必二《法律与生活》主观题框架 v12.2 Source-Checked Baseline

Status: `complete_candidate_pending_gpt_round03_and_governance`

This is the complete source-checked candidate framework after Codex source review and Claude Opus 4.7 Round 03. It is not final PASS, not a baodian, not DOCX/PDF delivery, and not TASK_COMPLETE.

## 0. 先走命题人路径

Every question must be placed by the proposition path before it enters an answer template:

1. The prompt wants which deliverable: completion, reason, support/reject, evaluation, meaning/value, or path/advice?
2. The material uses which carrier: case, legal rule, legal phenomenon, or governance scene?
3. The answer rewards which action: identify a legal relationship, match elements, judge liability/effect, choose a dispute path, or explain rule-of-law value?
4. The case reinforces a high-frequency trunk or only opens a low-frequency container?
5. If the source or prompt is unclear, mark uncertainty instead of forcing placement.

Student first sentence:

> 先看题目让我交什么，再决定走哪条法律链。

## 1. Six Entrances

### E1. 表格 / 补链 / 裁判要点题

Use when the prompt gives a table, examples, blanks, multiple mini-cases, or a visible "one row, one answer" structure.

Student action:

1. Split the material into cells or mini-cases.
2. For each cell, write one legal chain: fact, rule, conclusion.
3. Do not merge two cells into one slogan.

Student phrase:

> 一个格子一条法律链，格子不同，法律关系不能混。

Core evidence includes CC0077, CC0084, CC0137, CC0157, CC0289 and other E1 rows.

Source-checked patches:

- CC0137: AI facts only support the copyright grid; credit-card facts only support the contract/default grid. Do not write a broad AI innovation answer.
- CC0289: the first part is E1 because it asks students to complete three Q&A answers with precise legal terms.

False transfer to block:

- seeing AI and writing technology innovation;
- seeing several legal issues and mixing them into one paragraph;
- using personal-information or 必修三 slogans when the rubric does not score them.

### E2. 判决 / 裁判 / 责任理由题

Use when the prompt asks why a court, arbitrator, or legal body judged this way, or asks for responsibility/liability reasoning.

Student action:

1. Identify the legal relationship.
2. Match the decisive facts to the legal elements.
3. State responsibility, effect, or legitimacy.
4. If the prompt asks meaning, add a value sentence after the legal reason.

Student phrase:

> 先定关系，再抓构成要件，最后落责任或裁判理由。

Core evidence includes CC0002, CC0025, CC0054, CC0119, CC0181, CC0200, CC0364 and other E2 rows.

Source-checked patches:

- CC0364 stays E2, but the formal source row is `CC0364_2026_通州_期末_19_1`; the v12.1/v12.2 alias uses `期中`.
- `程序合法` is rewarded in CC0364 because this case specifically involves proportion consent, legal procedure, reduced impact, and fact finding. It is not a universal E2 first sentence.
- The separate logic-and-thinking atoms attached to CC0364 must not enter the law framework.

False transfer to block:

- writing "程序合法" for every judgment question;
- seeing a court and writing generic 公正司法;
- importing non-law module atoms into the law answer.

### E3. 诉求 / 请求能否支持题

Use when the prompt asks whether a claim, request, rescission, compensation, or support position should be accepted.

Student action:

1. Name the request.
2. Identify the legal basis and decisive fact.
3. Judge support or non-support.
4. Explain the legal consequence.

Student phrase:

> 诉求能不能支持，关键看事实能不能落进法律要件。

Core evidence count is low: E3 currently has 3 locked rows.

Teaching warning:

- E3 must be taught as a low-frequency but clear entrance.
- Do not overuse E3 for every "can/cannot" expression unless the scoring task is truly claim support.

False transfer to block:

- replacing element matching with emotional fairness;
- writing only conclusion without the legal basis and decisive fact.

### E4. 评析 / 认识 / 谈看法题

Use when the prompt asks students to evaluate a view, comment on a statement, or discuss understanding.

Student action:

1. State the attitude: right, wrong, partial, or needs distinction.
2. Put the view back into the legal relationship and material context.
3. Explain with law and facts.
4. Land the boundary: what can be affirmed, what must be corrected.

Student phrase:

> 评析题先表态，再把话放回具体法律情境里。

Core evidence includes CC0051, CC0061, CC0150, CC0238, CC0254, CC0332, CC0340 and other E4 rows.

Source-checked patch:

- CC0051 is a PASS_RECOVERED low-frequency evaluation case. It supports E4 because it asks students to evaluate a view through marriage-family law and good-law standards.
- CC0051 must not create a broad legal-change trunk and must not become 必修三 scientific-legislation slogans.

False transfer to block:

- writing "法律不断完善" as a universal answer;
- evaluating without returning to the case facts;
- importing broad rule-of-law progress language when the rubric needs legal comparison.

### E5. 意义 / 价值 / 作用 / 如何保护推动题

Use when the prompt asks the value, meaning, role, contribution, or how legal rules protect or promote a subject.

Student action:

First decide which internal sentence pattern applies.

Meaning/value pattern:

1. The rule protects a specific party or right.
2. It regulates similar behavior or cases.
3. It maintains legal order, social order, or public interest.

How-to-protect/promote pattern:

1. Name the legal means.
2. Name the protected object or subject.
3. Explain the practical effect.

Student phrase:

> 意义题不是空喊价值，要从法律手段长出保护对象和实际效果。

Core evidence count is high: E5 currently has 11 locked rows.

Source-checked patch:

- CC0195 stays E5. Its scoring anchor is labor law: union platform, collective contract, worker-rights protection, lawful employment, labor relationship, fairness, and production efficiency.
- CC0195 must not be thrown out as pure economics.

False transfer to block:

- writing economic fairness/efficiency without labor-law mechanism;
- treating every meaning question as a generic rule-of-law value paragraph;
- ignoring whether the prompt wants "meaning" or "how to protect".

### E6. 调解 / 维权 / 纠纷解决 / 证据路径题

Use when the prompt asks how to solve a dispute, protect rights, give advice, choose a path, preserve evidence, or pursue remedies.

Student action:

1. Identify the dispute or violated right.
2. Choose the lawful path.
3. Give basis, action, evidence, and remedy.
4. If there are multiple cases, keep one path per case.

Student phrase:

> 维权题先选路，再写依据、行动、证据和救济。

Core evidence includes CC0125, CC0223, CC0244, CC0245, plus CC0289 as secondary support.

Source-checked patches:

- CC0223 stays E6 primary. It rewards two dispute-resolution paths: litigation mediation and neighboring/common-area use in case 1; market-regulator adjudication, administrative lawsuit, and unfair competition in case 2.
- CC0289 supports E6 secondarily. `任选其一` means choose one problem and write a complete rights-protection chain.

False transfer to block:

- writing free-standing value language before naming the dispute path;
- answering all `任选其一` options incompletely;
- mixing two cases into one generic paragraph.

## 2. Open Container Layer

These items are useful but not core support:

- CC0162: reference-only format-contract/service-contract direction.
- CC0040: reference-only digital-person copyright direction.
- CC0353: reference-only with `期中/期末` alias risk.
- CC0380: formal boundary split, useful for future new-technology/data-risk work but not promoted to current core.
- Six next-backfill candidates: remain outside core until a new source pass promotes them.

Container rule:

> 开放容器只保留未来可能性，不为当前框架凑证据。

## 3. Cross-Entrance Red Lines

- Do not cite teacher reference answers as formal rubric evidence.
- Do not promote reference-only rows into core coverage.
- Do not turn one recovered low-frequency case into a new trunk.
- Do not collapse E1 and E6 just because a case has several subparts.
- Do not split E5 without new locked evidence showing coverage failure.
- Do not use 必修三 slogans to replace legal relationship, legal element, liability, procedure, or remedy.

## 4. Current Coverage

Core coverage remains 42/42 after source check.

| entrance | count |
|---|---:|
| E1 表格/补链/裁判要点 | 9 |
| E2 判决/裁判/责任理由 | 8 |
| E3 诉求/请求能否支持 | 3 |
| E4 评析/认识/谈看法 | 7 |
| E5 意义/价值/作用/如何保护推动 | 11 |
| E6 调解/维权/纠纷解决/证据路径 | 4 |

## 5. Promotion State

This baseline is complete enough to serve as the current source-checked candidate framework.

It is not final because:

- GPT Round 03 source-check review has not been captured;
- governance and traceability gates are not fully closed;
- next-backfill candidates remain outside the locked core;
- E3 low-sample and E5 high-variance teaching risks must remain visible.

