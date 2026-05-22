# v12.2 council candidate framework

Status: `candidate_source_checked_round01_not_final`

This file is a candidate grown from the evidence pack plus real GPT/Claude Round 01 and Round 02 council outputs. It is not final PASS, not a baodian, not DOCX/PDF, and not TASK_COMPLETE.

Source-check overlay: `codex_source_checks/pending_source_check_20260522.md` and `candidate_framework_v12_2_council_source_checked.md`.

## 0. Evidence Base

- Core rows checked: 42
- Coverage check file: `codex_adjudication/coverage_check_v12_2_council.csv`
- Coverage result: all 42 core rows mapped to a candidate entrance.
- Boundary/reference rows: 5, not core support.
- Next-backfill rows: 6, not core support.

Coverage distribution:

| entrance | count |
|---|---:|
| E1 表格 / 裁判要点 / 补链 | 9 |
| E2 判决 / 裁判 / 责任理由 | 8 |
| E3 诉求 / 请求能否支持 | 3 |
| E4 评析 / 认识 / 谈看法 | 7 |
| E5 意义 / 价值 / 作用 / 如何保护推动 | 11 |
| E6 调解 / 维权 / 纠纷解决 / 证据路径 | 4 |

## 1. Method Spine

Every subjective question first goes through these moves.

1. 识别设问交付物  
   Ask: this question wants 理由、意义、评析、表格、诉求判断, or path?

2. 事实转法词  
   Translate material facts into legal terms before writing doctrine.

3. 规则-事实-结论链  
   Each answer point must contain rule, fact match, and legal result/value.

4. 分链写作  
   One row, one case, one subject, or one claim gets its own chain.

5. 规则生价值  
   Value language must be derived from legal measures and concrete protected objects.

6. 反向筛查  
   Remove wrong-module and over-abstract answers before finalizing.

## 2. Six Student Entrances

### E1. 表格 / 裁判要点 / 补链题

Student move:

```text
先看每一格、每一案、每一行要补什么。
一格只写一条法律链：事实定性 + 法律规则 + 法律后果。
```

Support cards:

- CC0077
- CC0084
- CC0137
- CC0157
- CC0180
- CC0189
- CC0213
- CC0214
- CC0289
- CC0325

Do not:

- use one broad value slogan across multiple rows;
- merge different cases into one legal relationship;
- treat a table as an ordinary essay.

### E2. 判决 / 裁判 / 责任理由题

Student move:

```text
先判断法院/仲裁为什么这样处理。
再写事实触发了什么法律规则。
最后落到责任承担、责任减轻、合同成立、劳动关系认定或责任分担。
```

Support cards:

- CC0002
- CC0025
- CC0054
- CC0119
- CC0200
- CC0364

Do not:

- make `程序合法` the fixed first sentence for all such questions;
- skip the material facts and only write "于法有据";
- merge judgement-result questions with broad meaning questions.

### E3. 诉求 / 请求能否支持题

Student move:

```text
先表态：支持、部分支持、不支持。
再按诉求分链：权利依据 + 事实证明 + 法律后果。
```

Support cards:

- CC0143
- CC0305
- CC0373
- related boundary support: CC0063 for over-claim / limited support logic.

Do not:

- mechanically write 退一赔三 whenever consumers appear;
- put all claims into one chain;
- ignore evidence limits.

### E4. 评析 / 认识 / 谈看法题

Student move:

```text
先定被评对象。
再一主体一链或一观点一链。
最后回到法律边界和现实意义。
```

Support cards:

- CC0051
- CC0061
- CC0238
- CC0244
- CC0254
- CC0332

Do not:

- turn evaluation into empty rule-of-law praise;
- judge multiple subjects with one sentence;
- ignore historical or factual condition limits.

### E5. 意义 / 价值 / 作用 / 如何保护推动题

Student move:

```text
法律手段 -> 保护对象 -> 价值效果。
每一句意义都必须从材料中的规则或司法措施长出来。
```

Support cards:

- CC0011
- CC0019
- CC0025
- CC0045
- CC0103
- CC0131
- CC0150
- CC0195
- CC0229
- CC0283
- CC0340

Do not:

- write "维护公平正义" as a universal ending;
- treat CC0195 as non-legal economics by default;
- turn innovation, ecology, elderly care, or labor protection into generic policy slogans.

### E6. 调解 / 维权 / 纠纷解决 / 证据路径题

Student move:

```text
先选路径。
再列证据。
最后写请求、责任和边界。
```

Support cards:

- CC0125
- CC0223
- CC0245
- CC0289
- CC0092

Do not:

- only list 协商、调解、仲裁、诉讼;
- forget evidence and claim design;
- skip legal relationship recognition.

## 3. Open Containers

These are not deleted, but cannot inflate the core.

1. Six next-backfill candidates:
   - CC0251
   - CC0276
   - CC0277
   - CC0317
   - CC0318
   - CC0319

2. Five `OPEN_OR_REFERENCE` records:
   - reference only until locked.

3. New-technology and data-risk edge cases:
   - current locked cards can support existing entrances;
   - new cards remain pending until source-locked.

4. Format-clause and service-contract edge cases:
   - CC0084 supports current framework;
   - CC0317/CC0318 cannot enter core before backfill.

5. Module-boundary mixed cases:
   - do not count economics or governance material as legal coverage unless the legal prompt and scoring anchor are locked.

## 4. Pending Checks Before Promotion

- CC0137: exact rubric boundary for AI copyright grid and credit-card contract grid.
- CC0289: primary placement of "任选其一" and rights-protection path.
- CC0223: dispute-resolution path vs legal-issue recognition vs two-case meaning extraction.
- CC0364: whether procedure legality is actually rewarded.
- CC0051: use as recovered evaluation evidence, but prevent over-expansion into a legal-change trunk.
- CC0195: confirm placement under E5 rather than an economics boundary.
- Any later use of CC0162 / CC0040 / CC0353 / CC0380.
- All six next-backfill candidates.

## 4A. Source-Check Resolution

Resolved in `codex_source_checks/pending_source_check_20260522.md`:

- CC0137: keep E1; exact boundary is AI copyright grid plus credit-card contract/违约 grid, not a broad AI innovation trunk.
- CC0289: keep E1 primary and E6 secondary; completion task comes first, `任选其一` rights-protection path comes second.
- CC0223: keep E6 primary; rewarded action is dispute-resolution path across two cases, with value language derived from the cases.
- CC0364: keep E2 with alias warning; v12.1 uses `期中`, merged formal source is `期末`; procedure legality is rewarded only in this case, not as a universal starter.
- CC0051: keep E4 as PASS_RECOVERED low-frequency evaluation evidence; do not expand into a legal-change trunk.
- CC0195: keep E5; formal scoring anchors labor-rights fairness/efficiency, not non-legal economics alone.
- CC0162 / CC0040 / CC0353 / CC0380: not promoted to core in this pass.
- All six next-backfill candidates remain outside core until a new evidence pass promotes them.

## 5. Promotion Rule

This candidate can be promoted only after:

1. every support card in the 6 entrances is source-checked against the original question/rubric when marked pending above;
2. the 5 reference rows remain excluded from core coverage;
3. the 6 next-backfill rows either stay excluded or are promoted by a new evidence pass;
4. GPT/Claude advice log records rejected and modified suggestions;
5. a new coverage delta confirms no core row is unmapped.
