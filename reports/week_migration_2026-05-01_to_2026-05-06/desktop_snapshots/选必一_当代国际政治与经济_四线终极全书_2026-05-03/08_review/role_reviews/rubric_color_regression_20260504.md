# Rubric Color Regression - 2026-05-04

## Trigger

用户抽查 `2026海淀一模 Q20`，提供细则截图。截图显示该题真实黄标/红字踩分层级为：

1. 角度1 对我国：制度型开放、国内国际两个市场两种资源、畅通双循环、新发展格局、走出国门、竞争力。
2. 角度2 对世界经济：开放、包容、普惠、平衡、共赢，国际合作/互利共赢，全球资源优化配置，以及低碳能源、人工智能等领域的国际标准、标准共通、技术共享、全球技术创新与绿色转型。
3. 角度3 对全球治理：参与全球经济治理和规则制定，全球治理体制更加公正合理，话语权、国际影响力、国际经济新秩序。

## Failure

此前 `red_scoring_words_patch_20260504.md` 的红色踩分词抽取，把框架积累词和同核心可迁移词混入了 `踩分词`，例如把 `参与国际分工`、`国际交流合作`、`对标国际规则、规制、管理和标准`、`依法运用国际规则和争端解决机制` 放进本题，导致与截图中的真实颜色细则不一致。

根因：`scoring_terms_for_group()` 从 `display_core / accumulation / expression` 自动抽词，而不是逐题绑定原始细则颜色标记。

## Immediate Fix Applied

- `tools/build_final_student_handout.py` 增加 `QUESTION_EXACT_SCORING_GROUPS["2026海淀一模 Q20"]`。
- 第一题按用户截图改为三角度：
  - 对我国（3分；替代2分）
  - 对世界经济（2分；结合材料1分）
  - 对全球治理（2分）
- 第一题的 `本题踩分点汇总`、`本题命中框架`、`整题汇总卷面答案`、`条目拆解` 均使用截图细则词，不再使用自动泛化词。
- Markdown/DOCX/PDF 已重生。

## Current QA After Immediate Fix

- Main training questions: 47.
- `本题踩分点汇总`: 47.
- Item chains: 177.
- Answer variants: 178.
- Mainline `踩分词`: 354.
- Mainline red marks: 4299.
- DOCX red runs: 4727.
- PDF pages: 135.
- Forbidden-term scan: PASS.

## Status

First sampled question fixed.

Global `red scoring words` certification is **not** considered fully reliable until all 47 main questions are rechecked against original colored rubrics / marking-rule visual sources. The previous PASS for red scoring-word presentation should be treated as a presentation-layer pass only, not a full color-rubric accuracy pass.
