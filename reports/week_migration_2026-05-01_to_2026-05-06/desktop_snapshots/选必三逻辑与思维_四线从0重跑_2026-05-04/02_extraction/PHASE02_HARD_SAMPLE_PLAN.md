# Phase 02 Hard Sample Plan

本阶段只做五大硬样本回源试跑，不写学生稿，不生成 Word/PDF，不宣称穷尽。

## Inputs

- Codex lane A: `01_source_inventory/PRIORITY_SOURCE_QUEUE.md`
- ClaudeCode lane B: `04_suite_reports/claudecode_suite_reports/phase01_inventory_report.md`
- GPT-5.5 Pro: `08_review/gpt_phase_advice/phase_00_gpt55_raw.md`
- Governor/Patcher: `governor_confucius/failure_patch_manifest.md`

## Five Hard Samples

| sample_id | suite | question | module_target | raw paper | raw rubric |
|---|---|---|---|---|---|
| HS01 | 2026顺义一模 | Q19(2) | 思维-科学思维 | `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/试卷/试卷.pdf` | `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/细则/细则.pptx` |
| HS02 | 2025海淀二模 | Q20 | 思维-辩证思维 | `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/试卷/试卷.pdf` | `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/细则/补充材料/2025年海淀二模评标实录.docx` |
| HS03 | 2026朝阳期中 | Q21(2) | 思维-创新思维 | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/试卷/试卷.pdf` | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/细则.docx`; `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/补充材料/细则.docx` |
| HS04 | 2026通州期末 | Q11 | 思维选择题-抽象到具体 | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/试卷/试卷.pdf` | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026通州期末/细则/细则.pptx` |
| HS05 | 2026东城期末 | Q17(2) | 推理/边界 | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026东城期末/试卷/试卷.pdf` | `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026东城期末/细则/细则.pptx`; `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026东城期末/细则/分题细则/*.pptx` |

## Required Output Per Sample

- `stable_locator`
- `full_stem_or_question`
- `full_options` for choice questions
- `answer_key_or_scoring_points`
- `rubric_source_type`
- `material_trigger_points`
- `question_ask`
- `why_think_of_this`
- `answer_landing_points`
- `module_boundary_decision`
- `blocked_or_next_actions`

## Pass Gate

All five hard samples must be processed with real source text or rendered/visual fallback evidence before full-scale suite processing begins.
