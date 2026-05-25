# GPT Pro Review Packet V0

Status: `prepared_not_submitted`

## Review Target

Run directory:

`C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_逻辑与思维_双宝典双线重启_2026-05-24`

Key files:

- `01_source_inventory/QUESTION_COVERAGE_MATRIX.csv`
- `02_codex_lane/HARD_SAMPLE_SOURCE_PACKETS.md`
- `02_codex_lane/FAMILY_SOURCE_PACKETS_Q0006_Q0012.md`
- `02_codex_lane/B_ADDITIONS_BACKCHECK_Q0013_Q0017.md`
- `02_codex_lane/MAIN_THINKING_LEDGER.csv`
- `02_codex_lane/REASONING_FORM_LEDGER.csv`
- `02_codex_lane/CHOICE_TRAP_LEDGER.csv`
- `03_claudecode_lane/entries/main_thinking_entries.jsonl`
- `03_claudecode_lane/entries/reasoning_entries.jsonl`
- `03_claudecode_lane/entries/choice_trap_entries.jsonl`
- `03_claudecode_lane/fusion_candidates.csv`
- `03_claudecode_lane/blockers.csv`
- `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md`
- `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md`
- `04_fusion/A_B_DIFF_SNAPSHOT.md`

## Required Review

Act as strict chief content reviewer for Beijing Gaokao politics 选择性必修三《逻辑与思维》. Do not praise. Find defects.

Check:

1. 是否严格执行“双宝典”：思维部分按触发链，推理部分按同一推理形式汇总。
2. 17 个 source-locked rows 是否存在 evidence level 误判、题号误判、年份/套卷误判。
3. 思维宝典 review draft 是否达到必修四宝典式“材料触发 -> 知识节点 -> 答题句 -> 陷阱”的质量。
4. 推理宝典 review draft 是否真正按推理形式聚合，而不是地区年份流水账。
5. ClaudeCode B 线 `fusion_candidates.csv` 中哪些 high-confidence rows 可以优先要求 Codex 回源，哪些必须阻断。
6. 哪些说法不能进入最终 Word/PDF，尤其是旧索引、待回源、blocker 项。

## Output Format

Return:

- Verdict: `not_final / conditionally_usable / reject`.
- P0 findings: must fix before any external final.
- P1 findings: must fix before Word/PDF.
- Coverage gaps: list by suite/question if possible.
- Suggested next 10 source-lock rows.
- Final claim audit: what claims are currently forbidden.

Do not mark PASS.
