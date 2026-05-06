# Batch04I Manual Evidence Notes - 2026丰台一模

time: 2026-05-03 23:22 CST
operator: Codex A local evidence lane
student_doc_touched: no
cross_thread_guard: active

## Source Files Checked

- Scoring/reference PPTX: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/细则/细则.pptx`
- Paper PDF: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/试卷/试卷.pdf`
- Visual render made in this run: `02_extraction/visual_renders/batch04I_fengtai2026_paper/page_08.png`

## Paper Visual Check

The original paper PDF has no extractable text by `pypdf`, so Codex A rendered all pages in this run using PyMuPDF. Visual inspection of page 8 confirms Q19:

`结合材料，运用《当代国际政治与经济》知识，说明中国在全球可持续发展中彰显了怎样的大国情怀与担当。`

The materials reference:

- 2015年习近平主席出席联合国发展峰会.
- 《变革我们的世界：2030年可持续发展议程》.
- 经济、社会、环境三方面17个可持续发展目标.
- China's achievements in poverty reduction, education, and health cooperation.

## PPTX Source Check

PPTX slide 41:

- `结合材料，运用《当代国际政治与经济》知识，说明中国在全球可持续发展中彰显了怎样的大国情怀与担当。`
- `知识板块：当代国际政治与经济`
- `能力板块：解释与论证`

PPTX slide 42:

- `19.（8分）`
- `中国秉持人类命运共同体的理念，坚持胸怀天下，携手各国落实联合国2030年可持续发展议程，做全球发展的贡献者。`
- `中国坚定维护联合国宪章的宗旨和原则，坚持正确义利观，积极践行真正的多边主义，坚持合作共赢，致力于扩大同各国利益的汇合点。`
- `中国坚持共商共建共享的全球治理观，在消除贫困、教育普及和卫生健康等领域成就举世瞩目，生动彰显了中国在可持续发展征程中谱写的辉煌篇章，也集中展现了中国对可持续发展作出的积极贡献，展现了负责任大国的情怀和担当。`

## Evidence Boundary

This is a `细则.pptx`, but the relevant slide gives a reference-answer structure rather than point-by-point scoring rules. It is not an ordinary paper answer, yet it must not be inflated into per-point rubric evidence.

Local label: `P0_scoring_pptx_reference_answer_guarded`.

## Local Ruling

Q19 enters Batch04I guarded prelim fusion as expression accumulation. Q18 and Q20 are module-boundary exclusions. Student docs remain untouched.
