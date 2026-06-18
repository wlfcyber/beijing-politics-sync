# Slice 016 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 76-80 only
- backcheck_time: 2026-06-17T19:37:00+0800

## Overall Finding

Slice 016 has source evidence for all five entries. The slice is mixed:

- Q0076 is source-backed only if relabelled to the exact source point `促进人才、商品、服务和生产要素在全球范围内流动` inside the 2026朝阳一模Q20 development-potential layer. The desktop's `资源优化配置/国际贸易发展` wording is too broad.
- Q0077 is repair-needed: the desktop entry promotes the 2-point world-significance layer into the whole core and misses the 3-point `中国担当` layer.
- Q0078 is source-aligned: `推动贸易投资自由化便利化` is an exact 1-point development-potential direction in 2026朝阳一模Q20, and the desktop preserves the layer cap.
- Q0079 is source-aligned in main structure, but the strict exclusion/boundary field is incomplete: it omits the source's `《经济与社会》政府与市场知识` no-credit warning.
- Q0080 is source-backed as one consumer/market-layer item, but the desktop answer's `国际循环消费端` wording is nonstandard and the `一线放开/二线管住` trigger needs correction. The paper prompt comes from an OCR auxiliary extract because direct PDF text extraction was blank.

## Q0076 doc_order=76

- desktop blocks: 915-924
- question: 2026朝阳一模Q20
- source evidence:
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:218-230` confirms the material and prompt.
  - `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:83-99` confirms the official 2 + 3 + development-potential structure.
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:390-393` confirms the teacher-answer explanation for factor flow and efficient global allocation.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The source point is a 1-point development-potential direction about global flow of talent, goods, services and production factors. `优化全球资源配置/国际贸易发展` is an effect or analytical wording, not the exact scoring label.
- `完整设问`: PASS.
- `细则位置`: PASS. The desktop same-group notes preserve the 2 + 3 + capped 5-point structure.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: PASS.
- `答案句`: NEEDS_FIX. The answer should foreground the exact factor-flow scoring phrase and treat resource optimization/trade development as effect language.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.

## Q0077 doc_order=77

- desktop blocks: 927-935
- question: 2025西城二模Q19(2)
- source evidence:
  - `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:221-225` confirms the zero-tariff material and prompt.
  - `SRC_RUBRIC_2025_XICHENG_ERMO_Q19_2.txt:61-70` confirms the 3-point China-responsibility layer and 2-point world-significance layer.
  - `SRC_EXAM_2025_XICHENG_ERMO_Q19_2.txt:303-306` confirms the teacher-answer summary.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The desktop core promotes `贸易自由化/普惠包容全球化`, which belongs to the 2-point world-significance layer, and underplays the 3-point `中国担当` layer.
- `完整设问`: PASS.
- `细则位置`: PASS. The desktop same-group notes preserve the 3 + 2 structure.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: NEEDS_FIX. The trigger should point first to open Chinese market/correct义利观 and shared development opportunities, not only lower trade cost.
- `答案句`: NEEDS_FIX. The answer sentence must add `开放广阔中国市场/正确义利观` and `与最不发达国家共享发展新机遇、惠民生增福祉、互利共赢`.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.

## Q0078 doc_order=78

- desktop blocks: 937-946
- question: 2026朝阳一模Q20
- source evidence:
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:218-230`
  - `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt:83-99`
  - `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt:390-393`

Codex judgment:

- `术语/核心采分点`: PASS. `推动贸易投资自由化便利化` is an exact source-backed 1-point direction inside the development-potential layer.
- `完整设问`: PASS.
- `细则位置`: PASS. The desktop labels it under the capped development-potential layer.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: PASS.
- `答案句`: PASS.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.

## Q0079 doc_order=79

- desktop blocks: 947-956
- question: 2025丰台一模Q20
- source evidence:
  - `SRC_EXAM_2025_FENGTAI_YIMO_Q20.txt:206-220` confirms the 北京“两区” material and prompt.
  - `SRC_RUBRIC_2025_FENGTAI_YIMO_Q20.txt:13-14` confirms the 4-point trade/investment and 4-point technology-innovation structure and no-credit exclusions.
  - `SRC_EXAM_2025_FENGTAI_YIMO_Q20.txt:287-289` confirms the teacher-answer summary.

Codex judgment:

- `术语/核心采分点`: PASS. The trade/investment facilitation point is source-backed as the 4-point first angle, with detailed trade and investment mechanisms.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. The desktop notes omit source warnings about `《经济与社会》政府与市场知识` no-credit and material-copying without logical chain.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity.
- `材料触发`: PASS.
- `答案句`: PASS.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. Add the omitted source boundary: piling up government/market knowledge is no-credit in this item.

## Q0080 doc_order=80

- desktop blocks: 957-967
- question: 2026房山一模Q19
- source evidence:
  - `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt:300-342` is an OCR auxiliary extract for the original exam PDF; direct PDF text extraction was blank.
  - `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt:59-64` confirms the four 2-point layers: consumer/market, production/industry, investment/business environment, and China-solution/institutional opening.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. `贸易投资自由化便利化` is source-backed only as one item inside the consumer/market 2-point layer, not the whole question's core.
- `完整设问`: PASS.
- `细则位置`: PASS. The desktop same-group notes preserve the four 2-point layers.
- `来源`: NEEDS_FIX. Add formal source identity and note the OCR auxiliary extraction level for the prompt.
- `材料触发`: NEEDS_FIX. `一线放开` should be described as international-facing cross-border opening; `进出岛` belongs more to the `二线管住` relation.
- `答案句`: NEEDS_FIX. Replace the nonstandard `国际循环消费端` with `助力/畅通国际循环`.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS.
