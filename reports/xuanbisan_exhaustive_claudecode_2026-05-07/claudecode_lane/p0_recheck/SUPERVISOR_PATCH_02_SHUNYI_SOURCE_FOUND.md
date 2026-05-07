# Supervisor Patch 02 - Shunyi Q19(1) source found

Issued by Codex supervisor at 2026-05-07 15:52 Asia/Shanghai.

## Correction

The row `Q-2026顺义一模-19-1` must not remain `source_insufficient`.

The source is available at:

`fusion/p0_recheck_sources/001_Desktop_2026模拟题_2026各区一模_2026顺义一模_试卷_试卷.pdf__support__2026顺义一模细则.pptx.txt`

Use `===== SLIDE 8 =====`.

## Evidence

Slide 8 contains:

- the full Q19(1) material;
- the three-line syllogism:
  - all industries driven by frontier technology with forward-looking, strategic, disruptive features are future industries;
  - quantum technology is an industry with those features;
  - quantum technology is a future industry;
- the question: judge whether the reasoning is correct and explain why;
- the scoring rule:
  - the reasoning is wrong;
  - deductive reasoning needs true premises;
  - the material statement cannot necessarily infer the universal major premise;
  - the syllogism structure itself is correct;
  - therefore the reasoning is wrong.

## Required Patch

For `Q-2026顺义一模-19-1`:

- `decision`: `confirmed_with_patch`
- `can_enter_fusion`: `yes`
- `source_evidence`: cite `2026顺义一模细则.pptx.txt::SLIDE 8`
- keep framework node:
  `推理边界>演绎推理>三段论保真两条件（前提真实+结构有效）`
- patch any locator saying Slide6 to Slide8.

## Other Required Fixes

- Repair `P0_RECHECK_DECISIONS.csv` bad-width row caused by unescaped punctuation.
- Finish `P0_SOURCE_EVIDENCE.md`.
- Finish `P0_RECHECK_ACCEPTANCE.md`.

## Boundary

- Do not generate Word/PDF.
- Do not authorize final.
