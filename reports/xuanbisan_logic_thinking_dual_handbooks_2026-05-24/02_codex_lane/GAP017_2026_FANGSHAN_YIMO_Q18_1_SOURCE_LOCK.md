# GAP017 2026房山一模 Q18(1) Source Lock

Status: `source_locked_pending_external_review`

This file records a 2026房山一模 source lock for Q18(1). The original paper text layer is not reliable, so the prompt and material are locked from the rendered paper page. The paired formal scoring rules explicitly allocate points to overall/system thinking, contradiction analysis / concrete analysis, and dynamicity / quality-change logic. It can enter the thinking main-question chain as `A-formal`, pending B-line rerun and real external review.

## Evidence

- Paper prompt and material render: `preprocessed_corpus/renders/e37482eff39f3618/page_009.png`
- Formal answer and scoring rules: `preprocessed_corpus/gpt_sources/0ca482adfc64b0d7_2026房山一模细则.md:61-68`

## Q0102 2026房山一模 Q18(1)

- Paper prompt: 结合材料一，运用辩证思维方法，分析北京是如何通过科学治理实现“常态蓝天”的。
- Material: 北京 2025 年空气质量优良天数达 348 天，优良天数比例近 95%，从“雾霾困扰”转向“常态蓝天”。治理路径包括系统治理、精准施策、久久为功。
- Formal rubric: 治理路径一给整体性/分析与综合/联系/系统优化；治理路径二给矛盾分析法/具体问题具体分析/两点论与重点论统一/分析与综合；治理路径三给动态性/质量互变/发展。立足实践可给支持分，但总分不超过 6 分。
- Promotion: `Q0102`, thinking main-question row.
- Evidence level: `A-formal`.
- Trigger chain: 系统治理、统筹四大结构和多污染物协同控制 -> 整体性/分析与综合/系统优化；精准施策、分区分类、一企一策 -> 矛盾分析法/具体问题具体分析；久久为功、日积月累推动空气质量稳步提升 -> 动态性/质量互变/发展。

## Required Gates

- Add Q0102 to coverage matrix and source queue.
- Add MT0047.
- Add thinking handbook V2 section 54.
- Keep Q0102 on hold pending GPT Pro V52 / Claude V50 and B-line rerun.
