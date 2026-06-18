# Slice 014 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 66-70 only
- backcheck_time: 2026-06-17T18:29:24+0800

## Overall Finding

Slice 014 has local source evidence for all five entries. The common pattern is that the desktop document often contains useful same-question-group scaffolding, but the headline `core_point` is still a partial layer rather than the whole official rubric.

Key distinctions:

- Q0066: 通州一模 Q19 source uses a 4+4 structure and lists `共同利益`, `兼顾他国合理关切`, global governance, economic globalization direction, correct义利观 and other可采知识. The desktop national-interest formula is not an independent source label.
- Q0067: 朝阳二模 Q21 source is organized by `中国的发展需要`, `区域的发展需要`, `世界的发展需要`; national security and common interests are subpoints, not the whole organizing core.
- Q0068: 朝阳期末 Q20 source confirms the economic angle `开放型世界经济/世界经济共同繁荣/互利共赢/开放合作/共享成果`, but only as angle 3 of a four-angle 8-point rubric.
- Q0069: 朝阳期中 Q20(3) source confirms the digital-trade/global-commerce short-review structure. `共享中国发展新机遇` and economic-globalization direction are valid, but the short review also requires title, three material comments, summary, language logic and explicit prompt requirements.
- Q0070: 门头沟一模 Q20 source confirms a 7-point `原因2分 + 中国意义2分 + 世界意义2分 + 逻辑1分` rubric. The world-open-development point is source-backed, but cannot replace the China-side and reason layers.

## Q0066 doc_order=66

- desktop blocks: 796-804
- question: 2026通州一模Q19中国元首外交为世界注入稳定性与正能量
- source evidence:
  - `SRC_EXAM_2026_TONGZHOU_YIMO_Q19_VISUAL.txt:3-10` confirms Q19 prompt and four 元首外交镜头.
  - `SRC_RUBRIC_2026_TONGZHOU_YIMO_Q19.txt:160-192` confirms the 4+4 answer structure and可采知识 list.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The source supports `共同利益` and `兼顾他国合理关切`, not the fixed headline formula `维护国家利益是主权国家对外活动的出发点和落脚点`.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: knowledge/measures 4 points plus material-function 4 points; this point belongs to the可采知识 layer, not a standalone full-question core.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The entry correctly notices `兼顾他国合理关切` and the prompt's world-stability/effect target.
- `答案句`: NEEDS_FIX. The sentence over-adds the national-interest formula; the repair should center `共同利益` and `兼顾他国合理关切` while retaining the world-stability effect.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. The entry remains within 选择性必修一 international politics/economy.

## Q0067 doc_order=67

- desktop blocks: 807-817
- question: 2025朝阳二模Q21周边工作服务中国特色大国外交
- source evidence:
  - `SRC_EXAM_2025_CHAOYANG_ERMO_Q21.txt:215-228` confirms the prompt and 周边工作 material.
  - `SRC_RUBRIC_2025_CHAOYANG_ERMO_Q21.txt:283-314` confirms the three-subject scoring structure.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The source places national security inside the China-development layer and common interests inside the regional-development layer; the fixed national-interest formula is over-promoted.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: 中国3分, 区域3分, 世界2分, plus language/logic note; national-interest language cannot stand for all three layers.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The 周边国家、国家安全、共同利益 and regional-stability material supports this 选必一 angle.
- `答案句`: NEEDS_FIX. The sentence captures China security and regional stability, but still starts from the unsupported fixed formula and omits the world-development layer.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. The entry remains within 选择性必修一 international politics/economy.

## Q0068 doc_order=68

- desktop blocks: 822-833
- question: 2026朝阳期末Q20
- source evidence:
  - `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_VISUAL.txt:4-16` confirms the four-angle 8-point rubric.
  - `SRC_RUBRIC_2026_CHAOYANG_QIMO_Q20_CACHE_FROM_SAME_SOURCE.txt:119-134` confirms the same structure in OCR text, with line 130 as the economic angle and lines 132-134 as the national-interest angle.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. `共享成果/世界经济共同繁荣` is source-backed only as the target part of angle 3, not the whole 8-point question.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: economic angle, background 1 point plus target 1 point, inside a four-angle structure.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The entry correctly ties opening cooperation and multilateral trade to shared results and common prosperity.
- `答案句`: PASS. The answer sentence is usable for the economic angle if explicitly labelled partial.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. The entry remains within 选择性必修一 international economy.

## Q0069 doc_order=69

- desktop blocks: 834-845
- question: 2024朝阳期中Q20(3) `数字驱动 商通全球` short review
- source evidence:
  - `SRC_EXAM_2024_CHAOYANG_QIZHONG_Q20_3.txt:414-447` confirms the digital-trade material, prompt and four writing requirements.
  - `SRC_RUBRIC_2024_CHAOYANG_QIZHONG_Q20_3.txt:218-254` confirms the example answer and scoring notes.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. `共享中国发展新机遇` and economic-globalization direction are source-backed, but only as part of the third material comment and/or summary, not the entire short-review structure.
- `完整设问`: NEEDS_FIX. The desktop `设问` line omits the source's explicit requirements: theme focus, clear view, sufficient argument, logical clarity, standard terms and about 200 characters.
- `细则位置`: NEEDS_FIX. Needs exact position: title 1 point; three material comments 6 points; summary 2 points; language 1 point.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The trigger correctly identifies new products, new platform and new opportunities, and it keeps the world-angle warning visible.
- `答案句`: PASS. The sentence mirrors source-backed language about global trade bridge, shared China-development opportunity and inclusive/balanced/win-win globalization.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. The entry remains within 选择性必修一 international economy/global governance.

## Q0070 doc_order=70

- desktop blocks: 846-856
- question: 2026门头沟一模Q20 海南自贸港全岛封关
- source evidence:
  - `SRC_EXAM_2026_MENTOUGOU_YIMO_Q20.txt:341-356` confirms the prompt and specific material mechanisms.
  - `SRC_RUBRIC_2026_MENTOUGOU_YIMO_Q20.txt:120-131` confirms the 7-point reason/China/world/logic rubric.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The source-backed target is closer to `为世界经济开放发展注入新活力` and `推动建设开放型世界经济`; the desktop core should not replace the domestic and reason layers.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: reason 2 points, China significance 2 points, world significance 2 points, logic 1 point.
- `来源`: NEEDS_FIX. Local source is found and registered, but the desktop entry lacks formal source identity and position.
- `材料触发`: NEEDS_FIX. The visible trigger over-emphasizes domestic cost-reduction while the chosen core is a world-open-development point; it should explicitly connect market access,制度型开放, supply-chain stability and international division of labor to the world layer.
- `答案句`: PASS. The answer sentence is usable for the world-significance layer if explicitly labelled partial.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: PASS. The entry remains within 选择性必修一 international economy/opening-up.
