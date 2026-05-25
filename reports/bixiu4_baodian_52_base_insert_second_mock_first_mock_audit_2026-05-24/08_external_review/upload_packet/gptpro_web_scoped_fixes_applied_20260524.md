# GPTPro web scoped audit fixes applied 2026-05-24

Status: `SCOPED_FIX_APPLIED_NOT_FINAL_PASS`.

- accepted backup: `student_patch_entries.accepted.backup_before_gptpro_web_scoped_fixes_20260524_215523.jsonl`
- blocked backup: `student_patch_entries.blocked.backup_before_gptpro_web_scoped_fixes_20260524_215523.jsonl`
- accepted rows before: 36
- accepted rows after: 36
- moved/deleted from student正文 in this run: 0
- moved/deleted from student正文 cumulative current state: 2
- rewritten student rows: 36

## Deleted From Student Body

- 2026房山二模 Q18(2) `辩证否定 / 守正创新`
- 2026西城二模 Q16 `价值观的导向作用`

## Main Fixes

- 删除 `2026房山二模 Q18(2) 辩证否定 / 守正创新`：题干点名《逻辑与思维》，属于选必三边界。
- 删除 `2026西城二模 Q16 价值观的导向作用`：本地回查评标原文未点名价值观，按高风险术语规则撤正文。
- 重写 `2026东城二模 Q16 物质决定意识`：只保留一切从实际出发，不再混入主观能动性。
- 重写 `2026顺义二模 Q16 两点论与重点论`：不再写“主要矛盾和次要矛盾”，落到多样与主流、社会效益优先。
- 重写 `2026西城二模 Q16 矛盾普遍性和特殊性`：从“中国式日常特殊表达”落到“跨文化普遍生活追求”。
- 重写 `2026房山二模 Q16 量变质变`：从工匠精度、长期积累、制造能力跃升解释，不再沿用规划题模板。
- 为 `2026石景山二模 Q17(3)` 三条可选哲学路径加入边界句，避免被误读为三项累计得分。
- 批量去掉新增条目的模板化尾句，改为本题可直接写进卷面的材料化答案句。

## Evidence Cards

- `weak_evidence_cards_20260524.md` 已补海淀、西城、顺义、石景山四套外审证据卡。

## Gate

本补丁只处理 GPTPro scoped audit 已指出或本地回查新发现的问题；它不等于全书外部 final PASS。
