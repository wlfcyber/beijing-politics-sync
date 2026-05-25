# GAP006 2024海淀二模 Q5/Q6 Source Lock

Status: `source_locked_pending_external_review`

This file records the local source-lock decision for two 2024海淀二模 objective questions that were not yet promoted in the earlier Q0011 2024海淀二模主观题 package.

## Evidence

- Paper: `preprocessed_corpus/gpt_sources/13d454fdd813a039_高三二模_政治试题_以PDF为准_1.md:51-58`
- Reference answer: `preprocessed_corpus/gpt_sources/8f109fb09efc0c6a_高三二模_政治答案_2.md:20-25`
- Formal answer/rubric doc answer table: `preprocessed_corpus/gpt_sources/227192d22e10241b_2024海淀二模细则.md:20-23`

## Q0093 2024海淀二模 Q5

- Paper prompt: washed cotton towels were dried in three environments: outdoor sunlight, outdoor shade, and indoor natural drying. Only the outdoor-sunlight towel produced distinctive aroma molecules.
- Official key: Q5 = A.
- Promotion: `Q0093`, reasoning choice row.
- Evidence level: `A-formal` for local source lock, because the original paper and independent answer/rubric tables match. Still pending real GPT Pro / Claude review.
- Reasoning form: 探求因果联系的求异法.
- Boundary: not 求同法, 共变法, or 剩余法.

## Q0094 2024海淀二模 Q6

- Paper prompt: classifies government bonds and defines ultra-long-term special treasury bonds as special treasury bonds with an issuance term over ten years.
- Official key: Q6 = C.
- Promotion: `Q0094`, reasoning choice row.
- Evidence level: `A-formal` for local source lock, because the original paper and independent answer/rubric tables match. Still pending real GPT Pro / Claude review.
- Reasoning form: concept attribute / extension relation / conversion boundary.
- Boundary: "发行期限10年以上" is an attribute of ultra-long-term special treasury bonds; parallel subclasses are not contradictory concepts; a universal affirmative description cannot be simply converted into "the incremental tool is special treasury bond."

## Required Gates

- Add Q0093-Q0094 to coverage matrix and source queue.
- Add RF0059-RF0060 and CT0036-CT0037.
- Add reasoning handbook V2 sections 41-42.
- Keep both rows on hold pending GPT Pro V47 / Claude V45 and B-line rerun.
