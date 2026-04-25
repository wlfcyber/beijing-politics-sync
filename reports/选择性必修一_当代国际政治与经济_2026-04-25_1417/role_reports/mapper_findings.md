# Mapper Findings

## Scope read

- Prior run main artifact.
- Prior run coverage matrix.
- New run coverage rebuild requirements.

## Files inspected

- `C:\Users\Administrator\Desktop\飞哥的政治庄园\artifacts\选必一材料-触发-答题点总框架.md`
- Prior run `COVERAGE_MATRIX.csv`
- Prior run text cache for exact question anchors.

## Findings

- Old artifact was usable as a starting point, but not directly acceptable under latest skill because some coverage rows used vague question labels.
- The new run migrated only scoring-supported chains and repaired exact question anchors.
- Mixed economic questions were retained only for selected-compulsory-one international-economy content: high-level opening-up, international markets/resources, trade and investment facilitation, global supply chains, international rules, and open economy.
- Pure compulsory-two domestic economy chains were kept out of the selected-compulsory-one framework.

## Merge candidates

- Current new coverage includes 22 included main-question rows with exact question anchors.
- `国家安全是最高国家利益` remains a framework node but should not count as included until a hard selected-compulsory-one主观题 scoring source is found.

## Blockers

- OCR/protected sources may contain additional scoring chains.
- Choice-question work remains pending.

Decision: needs-merge
