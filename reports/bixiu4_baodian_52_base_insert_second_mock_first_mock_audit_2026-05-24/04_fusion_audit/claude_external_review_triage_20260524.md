# External Claude Triage Repair - 2026-05-24

## Accepted Hard Fixes
- Corrected `2026朝阳二模 Q21`: the source topic is `四个中国`, not `五篇大文章`.
- Corrected `2026房山二模 Q16`: the source question asks how to read `中华民族最感动人的浪漫` from Chinese industrial culture, not a generic `工匠精神的当代价值` prompt.
- Replaced thin/backfilled 2026二模 rows with source-candidate trigger chains where the candidate table had stronger material wording.
- Removed answer-landing meta language such as `答案要写出`, `答案要落到`, and `不能只罗列单个做法` from the accepted insertion data.
- Merged duplicate `2025海淀一模 Q21` system-optimization insertion into one system-view entry.
- Removed the unsupported independent `2026海淀二模 Q16` contradiction entry; bundled source text only supports `联系` and `实践与认识` angles for Q16.
- Folded the separate `认识对实践的反作用` row for `2026海淀二模 Q16` back into the broader practice/recognition answer sentence.

## Not Mechanically Collapsed
- `2026东城二模 Q16`, `2026朝阳二模 Q16`, `2026丰台二模 Q16`, `2026顺义二模 Q16`, and `2026石景山二模 Q17(3)` still keep multiple framework placements where the suite source bundle or marking document explicitly names multiple philosophy angles.
- This follows the accepted baodian pattern: framework-first placement by official principle node, with audit notes clarifying that optional angles are not cumulative point promises.

## Still Not Final PASS
- GPTPro web review is still pending because the controllable Chrome profile lacks the Codex Chrome extension.
- External review package must be rebuilt with raw source evidence before a renewed external Claude/GPT review can fairly judge the repaired artifact.