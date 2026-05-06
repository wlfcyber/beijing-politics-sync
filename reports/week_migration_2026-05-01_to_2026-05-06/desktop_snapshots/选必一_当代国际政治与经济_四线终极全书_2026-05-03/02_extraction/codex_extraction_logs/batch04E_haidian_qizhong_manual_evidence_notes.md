# Batch04E 2024海淀期中 Manual Evidence Notes

generated: 2026-05-03
scope: 2024海淀期中补遗
student_doc_touched: no

## Source Files

- P0 scoring:
  - `/Users/wanglifei/Desktop/2024模拟题/2024海淀期中/细则/细则.pdf`
  - cache: `02_extraction/full_source_text_cache_20260503/SRC_e3f88f68dd56_细则_pdf.txt`
- P3 paper:
  - `/Users/wanglifei/Desktop/2024模拟题/2024海淀期中/试卷/试卷.pdf`
  - cache text is garbled: `02_extraction/full_source_text_cache_20260503/SRC_132d9a876bce_试卷_pdf.txt`
  - current visual renders:
    - `02_extraction/screenshots/batch04E_2024海淀期中_paper/page_06.png`
    - `02_extraction/screenshots/batch04E_2024海淀期中_paper/page_08.png`

## Module Map

The scoring PDF page 3 explicitly maps:

- 选择性必修一主观题：`16(2)` and `21(2)`.
- 选择性必修一主观分值：15.

## Q16(2)

- Paper prompt visually checked on paper page 6:
  - `结合材料三，从经济角度，为中国咖啡企业“出海”提出建议。（6分）`
- Scoring position:
  - scoring page 13: `经济角度：必修二 + 选必一；分值角度：必修二4分 + 选必一2分；主体角度：企业4分 + 政府2分；题型角度：路径 + 结果`
  - scoring page 14: `贸易摩擦：企业和政府可利用国际组织赋予的权利，积极参与全球经济治理和规则制定，为企业“出海”营造良好的国际环境 2分`
- Decision:
  - Candidate with boundary guard.
  - Promote only the international-organization/global-governance/rule-making point.
  - Do not promote brand strategy, product development, cost reduction, supply-chain infrastructure, tax policy, market research, or enterprise-management material as Xuanbiyi cores.

## Q21(2)

- Paper prompt visually checked on paper page 8:
  - `结合材料，运用《当代国际政治与经济》知识，分析新中国外交的“变”与“不变”。（9分）`
- Scoring position:
  - scoring pages 61-65.
- Core structure:
  - `变` 4分:
    - 世界之变 2分：时代背景变化；政治多极化、经济全球化深入发展；和平与发展成为时代主题。
    - 中国之变 2分：综合国力增强、国际地位提升、承担更多国际责任；习近平外交思想为新时代中国特色大国外交提供根本遵循和行动指南。变通包括国际影响力话语权不断提升、人类命运共同体。
  - `不变` 5分:
    - 服务于我国人民民主专政的国家性质；国家利益/维护主权安全发展利益。
    - 独立自主基本立场；维护世界和平、促进共同发展宗旨；促进世界和平与发展目标；和平共处五项原则；独立自主和平外交政策可得2分；反对霸权主义强权政治可得1分。
- Decision:
  - Candidate.
  - Preserve `变` and `不变` as two separate answer frames.
  - Do not move `人类命运共同体` into the `不变` side.

## Current Boundary State

- Q16(2): mixed-module; selected Xuanbiyi 2分 only.
- Q21(2): direct Xuanbiyi 9分; some terms need functional placement rather than flat frequency counting.
