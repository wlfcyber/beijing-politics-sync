# GPT/Claude v2 深度补跑本地裁决与返修日志

time: 2026-05-04 12:28 CST
status: PASS_AFTER_GPT55_AND_CLAUDE_OPUS_V2_PATCHES

## External Evidence

| lane | conversation/thread | captured file | verdict | local status |
|---|---|---|---|---|
| GPT-5.5 Pro | ChatGPT Pro `Opus4.6 vs 4.7` thread, marker `XBY1-GPT-DEEP-REVIEW-V2-20260504` | `08_review/deep_external_rerun/gpt55_deep_external_review_response_v2_20260504.md` | NEEDS_FIX | all substantive issues adjudicated and patched or locally routed |
| Claude Opus 4.7 Adaptive | Claude thread `学生文档审稿意见`, URL `claude.ai/chat/97d32a69-e05b-4b69-a5f9-3c3a0cf09ce6`, marker `XBY1-CLAUDE-DEEP-TEACHING-V2-20260504` | `08_review/deep_external_rerun/claude_opus_deep_teaching_response_v2_20260504.md` | NEEDS_FIX | all must-fix issues adjudicated and patched or locally routed |

Both external lanes are advisory. Codex local source/evidence rules controlled every content decision.

## GPT-5.5 Pro v2 Decisions

| issue_id | severity | decision | patch / local reason | verified closed |
|---|---|---|---|---|
| XBY1-GPTV2-01 | must_fix_content | accept | `2025东城一模 Q20` moved from `推动贸易和投资自由化便利化` to `理论 -> 国家间共同利益是国家合作的基础`; trade-free expression retained only where the local atom supports it. | bad-pattern scan no longer finds the mismap |
| XBY1-GPTV2-02 | must_fix_content | accept | `2024西城一模 Q19(6)` moved from 中国外交 to `理论 -> 当前国际竞争的实质是以经济和科技实力为基础的综合国力较量`. | index and question view now show the theory landing |
| XBY1-GPTV2-03 | must_fix_content | accept | `2025朝阳二模 Q21` moved from 中国外交 to `理论 -> 国家间共同利益是国家合作的基础`. | index and question view now show common-interest theory |
| XBY1-GPTV2-04 | should_fix_transfer | accept | `2026西城期末 Q20` no longer uses `国际发展合作、南南合作与“小而美”项目`; it now uses climate-governance-specific China responsibility. | bad-pattern scan no longer finds small-and-beautiful under this question |
| XBY1-GPTV2-05 | should_fix_transfer | accept | UN title changed to `在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善`. | question view and six-bucket review now use the precise title |
| XBY1-GPTV2-06 | should_fix_transfer | accept | `建设开放型世界经济，参与全球经济治理和规则制定` accumulation split to stable core terms only; topic-specific expressions remain in corresponding question answers. | final Markdown shows generic accumulation plus a white-note boundary |
| XBY1-GPTV2-07 | style | accept | public text normalizer fixes `共商共建共享全球治理观` to `共商共建共享的全球治理观`. | targeted scan no hit |
| XBY1-GPTV2-08 | readability | accept | Long dense summaries now include a `主干必写 / 可选补充 / 时间不足删句` line; Q17/Q20 high-density summaries use exam-like connectors. | final Markdown regenerated |

## Claude Opus v2 Decisions

| issue_id | severity | decision | patch / local reason | verified closed |
|---|---|---|---|---|
| F-01 | must_fix | accept | Removed leaked `材料事实` / `材料要点` tokens from accumulation splitting. | targeted scan no hit |
| F-02 | must_fix | accept | Removed `国际关系民主化要另看题目是否单独考` from 新型国际关系 accumulation; white-note keeps only student-facing boundary wording. | targeted scan no hit |
| F-03 | must_fix | accept | Forced `全球治理应坚持开放、合作、共享、共赢、包容和共商共建` as one complete high-information expression, not isolated single-word items. | question view and bridge table aligned |
| F-04 | must_fix | accept | Deduplicated `核心技术自主可控；把握创新主动权` accumulation and added useful extension terms. | question view and bridge table aligned |
| F-05 | must_fix | accept with semantic tightening | Bridge table and by-question view now align; `和平、发展、合作、共赢是时代潮流` was moved out of the small-and-beautiful accumulation family. | targeted scan no hit |
| F-06 | must_fix | partial accept by local rule | `2025丰台一模 Q20` remains only in 慎用/跨模块; `2024东城一模 Q20` stays in main because the user notebook pinned it as must-include, but it is visibly labeled `主属经济模块，选必一为辅`, and the unique `提升贸易投资合作质量和水平` index row is marked慎用. | heading/index note present |
| F-07 | must_fix | accept | `2026朝阳一模 Q20` compressed to five exam-style connector layers; `2026朝阳期中 Q17` uses four relationship layers. | final Markdown regenerated |
| F-08 | must_fix | accept | `2025海淀期中 Q21(2)` summary now explicitly splits `变` and `不变`. | final Markdown regenerated |

## Regenerated Artifacts

- `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md`
- `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.docx`
- `09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.pdf`
- `09_delivery/选必一_教师核查索引_最终闭环版_20260504.csv`
- `09_delivery/选必一_核心点频次统计_最终闭环版_20260504.csv`

## Regression Scans

- Forbidden content scan: PASS.
- `2026石景山期末`: no hit.
- GPT mismatch patterns: no hit.
- Claude F-01 to F-05 leakage/dedup patterns: no hit.
- Final structure count: 47 main training questions, 176 entry chains, 177 answer-sentence variants.
- PDF text QA: 100 pages, first pages extract readable Chinese text.
- DOCX structural QA: `textutil -info` identifies valid Office Open XML, 93,177 extracted characters.
- `render_docx.py`: blocked by missing `soffice`; QuickLook DOCX/PDF thumbnails were generated and visually inspected as fallback.

