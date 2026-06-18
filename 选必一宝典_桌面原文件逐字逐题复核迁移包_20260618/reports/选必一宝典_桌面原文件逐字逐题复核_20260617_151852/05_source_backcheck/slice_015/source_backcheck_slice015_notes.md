# Slice 015 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 71-75 only
- backcheck_time: 2026-06-17T18:39:09+0800

## Overall Finding

Slice 015 has source evidence for all five entries. The slice is mixed:

- Q0071 is strongly source-aligned: `处理好自力更生和对外开放的关系` is the first 3-point layer of 朝阳期中 Q17.
- Q0072 is source-backed but the desktop core label is too generic. The official source is not a plain `自力更生/对外开放` template; it is `开放促进韧性4分 + 韧性支撑开放3分 + 开放与安全协同1分`.
- Q0073 is source-aligned as the China-contribution layer of 东城期末 Q20, but must remain inside a three-layer short essay.
- Q0074 is source-aligned as a material-comment point of the 朝阳期中 digital-trade short review; the same strict prompt-requirement issue from Q0069 remains.
- Q0075 is source-backed, but the official labels are `贸易投资便利化自由化`, `全球资源要素自由流动/两种资源两个市场`, and `高水平对外开放`; the desktop's `促进全球资源优化配置和国际贸易发展` should be labelled as a derived summary, not the exact rubric wording.

## Q0071 doc_order=71

- desktop blocks: 859-869
- question: 2026朝阳期中Q17
- source evidence:
  - `SRC_EXAM_2026_CHAOYANG_QIZHONG_Q17.txt:148-169` confirms the AI material and prompt.
  - `SRC_RUBRIC_2026_CHAOYANG_QIZHONG_Q17.txt:14-21` confirms the first layer: self-reliance/opening, core technology autonomy, and international cooperation/globalization/international division of labor.

Codex judgment:

- `术语/核心采分点`: PASS. The core point matches the first 3-point layer.
- `完整设问`: PASS.
- `细则位置`: PASS. The desktop same-group notes identify this as the first layer and preserve the full three-layer structure.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: PASS. The autonomous/not-closed-door material supports the self-reliance/opening relation.
- `答案句`: PASS. The answer sentence is directly usable for the first layer.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.

## Q0072 doc_order=72

- desktop blocks: 870-879
- question: 2026东城一模Q19(3)
- source evidence:
  - `SRC_EXAM_2026_DONGCHENG_YIMO_Q19_3.txt:218-227` confirms material two and the prompt.
  - `SRC_RUBRIC_2026_DONGCHENG_YIMO_Q19_3.txt:16-28` confirms the 4+3+1 scoring structure.
  - `SRC_EXAM_2026_DONGCHENG_YIMO_Q19_3.txt:305-308` confirms the teacher-answer summary.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The official frame is `高水平对外开放` and `产业链韧性` in a 4+3+1 relation; the desktop core `自力更生和对外开放` is a broad paraphrase.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact 4+3+1 position and relation wording.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: PASS. The trigger correctly notices open platforms/global resources and key-core-tech resilience.
- `答案句`: NEEDS_FIX. The answer should be rewritten around `开放促进韧性`, `韧性支撑开放`, and `开放与安全协同`, not a generic self-reliance/opening sentence.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.

## Q0073 doc_order=73

- desktop blocks: 882-892
- question: 2025东城期末Q20
- source evidence:
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:192-201` confirms the new-energy-vehicle material and short-essay prompt.
  - `SRC_RUBRIC_2025_DONGCHENG_QIMO_Q20_PDF.txt:127-142` confirms title/three-paragraph form, China contribution, EU criticism, and China attitude/doings layers.

Codex judgment:

- `术语/核心采分点`: PASS. `促进资源优化配置/促进国际贸易` is directly source-backed inside the China-contribution layer.
- `完整设问`: PASS.
- `细则位置`: PASS. The desktop same-group notes preserve title/paragraph form and three content layers.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: PASS. The trigger correctly says the answer cannot only criticize the EU and must first address China's industry contribution.
- `答案句`: PASS. The answer sentence is usable for the China-contribution layer if labelled as partial.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.

## Q0074 doc_order=74

- desktop blocks: 893-904
- question: 2024朝阳期中Q20(3) `数字驱动 商通全球` short review
- source evidence:
  - `SRC_EXAM_2024_CHAOYANG_QIZHONG_Q20_3.txt:414-447` confirms the digital-trade material, prompt and writing requirements.
  - `SRC_RUBRIC_2024_CHAOYANG_QIZHONG_Q20_3.txt:238-249` confirms the title, three comments, summary and key material-comment options.

Codex judgment:

- `术语/核心采分点`: PASS. Resource optimization and international trade are source-backed in the new-platform/new-product comment layer.
- `完整设问`: NEEDS_FIX. The desktop `设问` line omits the source's explicit writing requirements.
- `细则位置`: PASS. The same-group notes preserve title, three comments, summary, language and easy-error boundaries.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: PASS.
- `答案句`: PASS. The answer sentence is usable for the material-comment layer.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.

## Q0075 doc_order=75

- desktop blocks: 905-914
- question: 2024海淀一模Q18(1)
- source evidence:
  - `SRC_EXAM_2024_HAIDIAN_YIMO_Q18_1.txt:252-262` confirms the免签/口岸签证 material and prompt.
  - `SRC_RUBRIC_2024_HAIDIAN_YIMO_Q18_1.txt:55-66` confirms the three answer requirements and substitute terms.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The desktop core is a valid derived summary, but the exact scoring labels are trade/investment liberalization and facilitation, global factor flow/two markets and resources, and higher-level opening.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact three-requirement position and point values.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: PASS. The trigger correctly connects visa facilitation with people-factor movement and opening.
- `答案句`: PASS. The answer sentence is usable if relabelled to the three source requirements.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.
