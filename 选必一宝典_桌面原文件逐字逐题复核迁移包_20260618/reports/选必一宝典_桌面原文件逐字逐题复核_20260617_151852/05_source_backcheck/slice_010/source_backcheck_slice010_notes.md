# Slice 010 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 46-50 only
- backcheck_time: 2026-06-17T17:53:47+0800

## Overall Finding

Slice 010 has real local source evidence for all five entries. The source evidence does not make the current desktop entry fully acceptable. The repeated defect remains: the desktop file uses bucket/core headings and same-question-group paragraphs, but does not provide independent hard-rule fields for exact `术语/核心采分点` and `细则位置`.

The five rows also differ in source role:

- Q0046: `共同利益` appears only as part of the `对世界` comprehensive-significance layer, not as the whole 8-point answer or as a direct `合作的基础` fixed point.
- Q0047: `当前国际竞争实质` is accepted only as a variation inside the 2-point challenge layer.
- Q0048: `当前国际竞争的实质` appears in the reference answer, but the source is a mixed `政治与法治` + `当代国际政治与经济` answer without independent subscore split.
- Q0049: `当前国际竞争实质` is one available angle in a 9-point level-scored comprehensive question, not an independent fixed scoring item.
- Q0050: `当前国际竞争的实质` is the strongest item in this slice: official rubric marks it as part of a 2-point required point.

## Q0046 doc_order=46

- desktop blocks: 566-576
- question: 2026西城一模Q20(2)（中国—东盟自贸区3.0版）
- source evidence:
  - `SRC_EXAM_2026_XICHENG_YIMO_Q20_2.txt:155-157` confirms the material and prompt.
  - `SRC_RUBRIC_2026_XICHENG_YIMO_Q20_2.txt:68-80` confirms the 8-point structure: standard rules 2, industry/supply chain 3, comprehensive significance 2, material 1.
  - `SRC_RUBRIC_2026_XICHENG_YIMO_Q20_2.txt:79` contains `合作共赢/开放包容/共同利益` in the `对世界` 1-point layer.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The current core `共同利益是合作的基础` over-promotes a phrase that appears only in the comprehensive-significance layer.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. The desktop entry gives the broad layer split but not an independent exact source position for the core term.
- `来源`: NEEDS_FIX. Local source is found, but the desktop file itself still lacks source identity and exact line/position.
- `材料触发`: NEEDS_FIX. Blocks 567 and 569 make common interests the cooperation root; the formal source mainly asks trade rules, supply chain, regional/world significance.
- `答案句`: NEEDS_FIX. Block 570 should not turn the answer into `共同利益` as the main causal chain.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. The same-question group includes industry, supply chain, employment, income and tax effects; these need boundary labeling rather than being flattened into a pure 选必一 cooperation point.

## Q0047 doc_order=47

- desktop blocks: 581-591
- question: 2024西城一模Q19(6)
- source evidence:
  - `SRC_EXAM_2024_XICHENG_YIMO_Q19.txt:203-204` confirms the prompt.
  - `SRC_RUBRIC_2024_XICHENG_YIMO_Q19.txt:86-88` gives opportunity 2, challenge 2, and bottleneck/opening support 6.
  - `SRC_RUBRIC_2024_XICHENG_YIMO_Q19.txt:92-101` confirms `当代国际竞争实质` only as a variation under the challenge point.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The term is source-backed, but only as a variation inside the challenge layer, not the whole 10-point row.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs an independent position such as challenge layer 2分, variation wording.
- `来源`: NEEDS_FIX. Local source is found, but the desktop entry still lacks formal source identity and position.
- `材料触发`: PASS. The challenge trigger from future-industry technology/talent/resource competition is legitimate.
- `答案句`: PASS. Block 585 is usable as a challenge-layer answer if marked as that layer.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. Block 590 already warns that `新质生产力` and industrial-system expressions are boundary expressions and should not become the 选必一 main item.

## Q0048 doc_order=48

- desktop blocks: 592-601
- question: 2024顺义思政二模Q19(2)
- source evidence:
  - `SRC_EXAM_2024_SHUNYI_ERMO_Q19_2.txt:170-171` confirms the prompt and mixed-module scope.
  - `SRC_RUBRIC_2024_SHUNYI_ERMO_Q19_2.txt:32-34` confirms the reference-answer language containing `当前国际竞争的实质`.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The term is present in the source answer, but the source is not split into an independent scoring point in the extracted text.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact note that this appears in the mixed-module reason paragraph, not as a separately numbered point.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and exact position.
- `材料触发`: PASS. The world new technological revolution and industrial transformation trigger is valid.
- `答案句`: PASS. Block 596 matches the source answer's international-competition reason.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. The entry mixes social-development law, government duties, people-centered stance, and 选必一 international competition; the current desktop row does not clearly separate non-选必一 layers.

## Q0049 doc_order=49

- desktop blocks: 602-615
- question: 2024西城二模Q17
- source evidence:
  - `SRC_EXAM_2024_XICHENG_ERMO_Q17.txt:134-137` confirms the prompt.
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:21-25` lists available answer angles including `当前国际竞争实质`.
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:75-85` confirms the 9-point level scoring table.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The term is a valid available angle, not a fixed independent score.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs level-scored wording and available-angle caveat.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The global technology-revolution framing justifies the international-competition angle.
- `答案句`: PASS. Block 606 can be a usable angle inside a broader level answer.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. The desktop same-question group separates development role, international role, security/talent support, and theory support rather than silently merging them into one 选必一 core.

## Q0050 doc_order=50

- desktop blocks: 616-625
- question: 2026朝阳一模Q20
- source evidence:
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:318-330` confirms material and prompt.
  - `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:96-112` confirms the official scoring structure.
  - `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:98` marks `当前国际竞争的实质...` plus innovation-driven strategy/technology strength as a 2-point required point.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The term is strongly source-backed as a required point, but the desktop row still lacks independent `术语` and exact `细则位置` hard-rule fields.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact line/position: required point, 2分（1+1）.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. Innovation examples directly trigger the technology-strength side of international competition.
- `答案句`: PASS. Block 620 aligns with the required point.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. The same-question group includes high-level opening, two markets/two resources, trade/investment liberalization, and factor flows; these are source-backed directions but need boundary labels so they do not obscure the `国际竞争实质` required point.
