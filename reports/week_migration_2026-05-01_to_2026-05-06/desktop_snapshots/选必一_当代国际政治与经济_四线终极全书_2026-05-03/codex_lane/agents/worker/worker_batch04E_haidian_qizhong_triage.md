# Worker Batch04E - 2024海淀期中补遗

generated: 2026-05-03
worker: Codex A local worker role
scope: 2024海淀期中 only
student_doc_touched: no

## Source Triage

### 2024海淀期中 Q16(2)

- Classification: `candidate_with_boundary_guard`
- Evidence:
  - `SRC_e3f88f68dd56` P0 scoring PDF text, pages 3 and 13-15.
  - `SRC_132d9a876bce` paper PDF text is unusable, but current-run visual render `02_extraction/screenshots/batch04E_2024海淀期中_paper/page_06.png` confirms the prompt.
- Prompt:
  - `结合材料三，从经济角度，为中国咖啡企业“出海”提出建议。（6分）`
- Boundary:
  - This is a mixed `经济角度` question. The scoring analysis explicitly says `必修二4分 + 选必一2分`.
  - Only the trade-friction/global-governance/rule-making line is promoted as Xuanbiyi; strategy, brand, market research, product innovation, cost reduction, enterprise management, and tax policy are boundary support.
- Usable Xuanbiyi point:
  - 企业和政府可利用国际组织赋予的权利，积极参与全球经济治理和规则制定，为企业出海营造良好国际环境。

### 2024海淀期中 Q21(2)

- Classification: `candidate`
- Evidence:
  - `SRC_e3f88f68dd56` P0 scoring PDF text, pages 61-66.
  - `SRC_132d9a876bce` paper PDF text is unusable, but current-run visual render `02_extraction/screenshots/batch04E_2024海淀期中_paper/page_08.png` confirms the prompt.
- Prompt:
  - `结合材料，运用《当代国际政治与经济》知识，分析新中国外交的“变”与“不变”。（9分）`
- Scoring structure:
  - `变` 4分:
    - 世界之变 2分：时代背景变化，政治多极化、经济全球化深入发展，和平与发展成为时代主题。
    - 中国之变 2分：综合国力增强、国际地位提升、承担更多国际责任；外交指导思想与时俱进，习近平外交思想为新时代中国特色大国外交提供根本遵循和行动指南。细则还列国际影响力话语权、人类命运共同体为可给分变通。
  - `不变` 5分:
    - 服务于我国人民民主专政的国家性质；国家利益/维护主权、安全、发展利益。
    - 坚持独立自主基本立场；维护世界和平、促进共同发展宗旨；促进世界和平与发展目标；和平共处五项原则；写独立自主和平外交政策可得2分；反对霸权主义强权政治可得1分。
- Boundary:
  - `国家性质` 可保留在外交政策决定/国家性质影响外交政策的表述中，但不单独扩大为政治与法治主链。
  - `人类命运共同体` 在本题是中国之变的可给分变通，不能反向改写为新中国外交一贯不变项。

## Recommendation

Proceed to Patcher/Governor as Batch04E prelim fusion. Do not write student final or Word/PDF from this batch alone.
