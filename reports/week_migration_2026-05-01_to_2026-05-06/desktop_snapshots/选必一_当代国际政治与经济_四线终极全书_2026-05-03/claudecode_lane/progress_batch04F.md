# ClaudeCode Lane B — Batch04F Progress

## Run Date: 2026-05-03

## Source Suite: 2025丰台二模

### Files Read

- P0 scoring source: `2025丰台二模评标细则/20题.docx` — full table-based 评标, 4 angles × 2 pts = 8 pts. CONFIRMED P0.
- Paper: `试卷.pdf` — pages 1–10 extracted via pypdf. Q20 material confirmed on page 7.
- Also read scoring files for Q18, Q19(2), Q21 to check boundary candidates.

### Question Triage Results

| Question | Scoring Source Module | Classification | Notes |
|---|---|---|---|
| Q18 | 《经济与社会》 | excluded | 必修二模块，全部排除 |
| Q19(2) | 《法律与生活》 | excluded | 法律模块，全部排除 |
| Q20 | 《当代国际政治与经济》 | in_scope | P0评标，8分，4角度，全部选必一 |
| Q21 | 哲学/综合 水平赋分 | no_xuanbiyi | 可从唯物论、辩证法等角度作答；无直接选必一细则评分点 |

### Q20 Scoring Atoms Extracted: FT01–FT04

- FT01: 世界上最大的发展中国家；国际政治经济格局中一支重要力量 → 中国桶（地位），角度一，2分
- FT02: 全球治理体系的重要参与者、贡献者和改革者（积极参与国际组织） → 中国桶（责任/参与），角度二，2分
- FT03: 《联合国宪章》宗旨原则；践行多边主义；维护多边体制的权威性和有效性 → 联合国桶，角度三，2分
- FT04: 推动构建人类命运共同体；共建共商共享的全球治理观；推动全球治理体制向着更加公正合理的方向发展 → 政治多极化桶，角度四，2分

### Merge Flags

- FT01 overlaps with existing 2025海淀二模 Q21 ATOM "世界上最大的发展中国家/国际政治经济格局中重要力量" — treat as expression-accumulation variant with new scenario ("全球南方现代化"), NOT a new separate core term.
- FT02 "全球治理体系的重要参与者、贡献者和改革者" is a high-information new phrase not yet in accumulated atoms — promote as new expression under 中国→责任/参与.
- FT03 "践行多边主义" and "《联合国宪章》宗旨原则" overlap with existing 联合国 atoms; "维护多边体制的权威性和有效性" is a new formulation — promote as expression variant.
- FT04 "推动构建人类命运共同体" already in system; "推动全球治理体制向着更加公正合理的方向发展" is a new high-information direction phrase — promote as new accumulated phrase.

### Status

- Source read: COMPLETE
- Entry draft: COMPLETE (see batch04F_fengtai_entries.md)
- Missing blockers: Q18/Q19(2)/Q21 excluded by module boundary — no blocker (correct exclusion)
- Conflicts for Codex: FT01 merge with existing 海淀二模 atom needs Codex A confirmation
- Suite report: Written

### Next Steps for Codex A

1. Confirm FT01 merge with existing 海淀二模 Q21 地位 atom (add 丰台二模 as second source with "全球南方现代化" scenario)
2. Confirm FT02 "重要参与者、贡献者和改革者" as new accumulated phrase in 中国→责任
3. Confirm FT03 "维护多边体制的权威性和有效性" as new expression variant in 联合国桶
4. Confirm FT04 "推动全球治理体制向着更加公正合理的方向发展" as new phrase in 政治多极化桶
5. Run Patcher / Governor on these 4 atoms before student draft update
