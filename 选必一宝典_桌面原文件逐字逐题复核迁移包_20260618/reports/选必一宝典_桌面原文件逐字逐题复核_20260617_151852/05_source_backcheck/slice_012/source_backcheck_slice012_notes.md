# Slice 012 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 56-60 only
- backcheck_time: 2026-06-17T18:10:42+0800

## Overall Finding

Slice 012 has source evidence for all five entries. None should be treated as accepted-final at entry level because the desktop source still lacks independent hard-rule `术语/核心采分点` and `细则位置` fields, and several entries promote a source-backed sub-angle into a fixed whole-question core.

Key distinctions:

- Q0056: the source supports `维护我国的主权、安全和发展利益` as one `不变` aspect and basic foreign-policy goal, but not the exact fixed formula `出发点和落脚点` as an independent score point.
- Q0057: `坚定维护本国利益` is one optional item inside the `中国态度/怎么做` layer of a short essay, not the whole 8-point core.
- Q0058: the exact national-interest formula is source-backed, but only as angle 4 of a four-angle 8-point rubric.
- Q0059: `国家安全与核心利益` is one available angle in a 9-point level-scored comprehensive question, not a fixed point.
- Q0060: `维护我国主权、安全和发展利益` appears inside the 1-point `总体外部环境` bundle of a four-environment 8-point answer; it cannot replace the whole external-environment framework.

## Q0056 doc_order=56

- desktop blocks: 684-692
- question: 2025海淀期中Q21(2)
- source evidence:
  - `SRC_EXAM_2025_HAIDIAN_QIZHONG_Q21_2.txt:239-256` confirms the diplomatic-stage material and prompt.
  - `SRC_EXAM_2025_HAIDIAN_QIZHONG_Q21_2.txt:311-315` gives the reference answer's `不变` aspects.
  - `SRC_RUBRIC_2025_HAIDIAN_QIZHONG_Q21_2.txt:15-17` confirms the same answer chain.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. Source supports `维护我国的主权、安全和发展利益`, but the exact `出发点和落脚点` formula is not independently positioned.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact note: `不变` aspect / basic goal, no fixed score layer.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The three-stage diplomacy material supports the `变/不变` reasoning.
- `答案句`: PASS. The answer sentence is source-aligned for the `不变` aspect.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. The listed diplomatic principles are mainly within 选必一 foreign-policy content.

## Q0057 doc_order=57

- desktop blocks: 693-703
- question: 2025东城期末Q20
- source evidence:
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:192-201` confirms the NEV anti-subsidy-tax material and prompt.
  - `SRC_RUBRIC_2025_DONGCHENG_QIMO_Q20_PDF.txt:127-142` confirms title, paragraph format, contribution, EU critique, and China attitude/doings layers.
  - `SRC_EXAM_2025_DONGCHENG_QIMO_Q20.txt:645-655` confirms the teacher-answer angles including national interest and negotiation/common-interest logic.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. `维护本国利益` is source-backed, but only inside the China attitude/doings layer.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: third layer, one point 2分 / two points 3分, not whole-question core.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The business-ministry response and continued consultation support the national-interest/doings layer.
- `答案句`: PASS. The answer is a usable sentence for this local layer, if clearly marked as partial.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. The source question is mainly economic-globalization/trade-protection/market-order plus China attitude, not a pure `国家安全` item.

## Q0058 doc_order=58

- desktop blocks: 704-715
- question: 2026朝阳期末Q20
- source evidence:
  - `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_VISUAL.txt:4-16` confirms the rendered formal scoring page.
  - `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_CACHE_FROM_SAME_SOURCE.txt:119-134` mirrors the same four-angle structure.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The exact national-interest formula is source-backed, but the desktop still lacks independent hard-rule fields.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: angle 4 `我国国家利益`, background 1 + goal 1, not whole 8分.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The formal rubric itself ties the national-interest angle to主权、安全、发展利益 and中国式现代化.
- `答案句`: PASS. The answer is valid as the national-interest angle only.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. The four-angle rubric remains within 选必一 international-politics/economy content, provided each angle is kept distinct.

## Q0059 doc_order=59

- desktop blocks: 716-729
- question: 2024西城二模Q17
- source evidence:
  - `SRC_EXAM_2024_XICHENG_ERMO_Q17.txt:101-103` confirms the prompt and material.
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:19-23` lists available angles, including `国家安全与核心利益`.
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:66-76` confirms the 9-point level table.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The source has `国家安全与核心利益`, not the fixed `维护国家利益是...出发点和落脚点` formula.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs level-question available-angle wording, not a fixed score position.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. Global technology revolution and new quality productive forces can support a security/core-interest angle.
- `答案句`: NEEDS_FIX. The desktop answer overstates the exact theory formula and should be softened to an available angle.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. This is a cross-module comprehensive level question; security/core interest must remain one optional angle.

## Q0060 doc_order=60

- desktop blocks: 730-741
- question: 2025朝阳期末Q21
- source evidence:
  - `SRC_EXAM_2025_CHAOYANG_QIMO_Q21.txt:229-237` confirms the prompt and material frame.
  - `SRC_OTHER_2025_CHAOYANG_QIMO_PPTX.txt:1314-1324` confirms the question and structure requirement.
  - `SRC_OTHER_2025_CHAOYANG_QIMO_PPTX.txt:1326-1350` confirms `总体外部环境` and `维护我国的主权、安全和发展利益`.
  - `SRC_OTHER_2025_CHAOYANG_QIMO_PPTX.txt:1368-1489` confirms the political, economic, cultural/public-opinion environment layers and the max-score warning for mere textbook piling.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The term is source-backed only as one item inside the 1-point `总体外部环境` bundle.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: overall environment layer, not the whole 8-point framework.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. External risks and diplomatic environment directly support the need to维护主权、安全、发展利益.
- `答案句`: NEEDS_FIX. The current answer is too narrow and does not answer the four-environment external-environment frame.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. This large duplicate group must keep overall, political, economic, cultural/public-opinion environment layers separate.
