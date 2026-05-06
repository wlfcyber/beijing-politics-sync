# Batch 01 A/B Difference Table

Run: 选必一《当代国际政治与经济》四线终极全书 2026-05-03

Inputs:

- Codex A: `codex_lane/agents/worker/worker_batch01_entries.md`
- Codex A patcher: `codex_lane/agents/patcher/patcher_batch01_review.md`
- Codex A governor: `codex_lane/agents/governor/governor_batch01_gate.md`
- ClaudeCode B: `claudecode_lane/claudecode_entries.md`, `missing_blockers.md`, `conflicts_for_codex.md`

Status: `draft_not_final`. This table is a fusion control file, not a student artifact.

## Overall Verdict

ClaudeCode B completed an independent first pass over ten priority samples and produced entries, blockers, conflicts, and suite reports. It is useful as production lane B, but several of its blockers are already superseded by Codex A local visual evidence. Codex A remains the source judge.

Batch 01 can move into `fusion candidate` only with the fixes below. It cannot become student final, Word/PDF, coverage closed, or FINAL_ACCEPTANCE PASS.

## Difference Table

| id | Question / Core | Codex A Position | ClaudeCode B Position | Local Evidence Decision | Fusion Action |
|---|---|---|---|---|---|
| AB01 | 2026通州期末 Q20 / `共商共建共享全球治理观` bucket | Worker did not fully settle final bucket; patcher recommends `政治多极化`. | B explicitly places it under `政治多极化`, not `理论`. | Accept B + patcher. This phrase answers global governance/order direction, not why cooperation arises. | Put main core under `政治多极化`; do not merge with Q17 loose `共商共建共享` cooperation wording. |
| AB02 | 2026通州期末 Q20 / full prompt punctuation | Codex A source notes resolve paper extraction punctuation against scoring PPT. | B flags missing pause between `指引方向` and `彰显担当`. | Accept corrected three-part prompt from scoring PPT: `正逢其时、指引方向、彰显担当`. | Normalize all Q20 entries to the three-part wording. |
| AB03 | 2026通州期末 Q20 / `人类命运共同体` | Worker has correct separate scoring point but answer sentence risks reading HMC as a subordinate of four initiatives. | B places HMC under 中国 and gives a clearer separate answer. | Accept patcher warning. HMC is a China diplomacy goal/value expression, not a fourth-initiative sub-item. | Rewrite answer sentence: global governance initiatives serve the goal of building HMC; keep HMC as independent core under 中国. |
| AB04 | 2026通州期末 Q20 / point 4 optional group | Codex A notes one scoring group contains political-order terms and China-diplomacy terms. | B keeps them together in one political多极化 entry, with expression accumulation. | Split by function for six-bucket index while retaining same scoring location. `国际新秩序 / 国际关系民主化 / 多边主义` -> 政治多极化. `正确义利观 / 兼顾利益` -> 中国. | Two fusion atoms with shared source location and `same_optional_group` tag. |
| AB05 | 2026朝阳期中 Q17 / Layer 2 subpoint 2 | Codex A excludes `高质量发展/经济增长` as 必修二 boundary; governor requires explicit boundary note. | B agrees and marks it as boundary. | Consensus. | Create explicit `模块边界：必修二，已排除` record; do not hide it in prose. |
| AB06 | 2026朝阳期中 Q17 / `开放型经济 / 双循环 / 政府履行经济职能监管 / 产业结构优化升级` | Governor says these must not become 选必一 main-chain core terms. | B generally trims some of these, but still includes broad Q17 wording. | Accept Governor. Some may remain as material support or boundary notes, not as 术语. | Remove from core names in fusion atoms; keep only where needed in answer/material as non-core boundary support. |
| AB07 | 2026朝阳期中 Q17 / `共商共建共享` | Patcher warns Q17 cooperation wording is not the same as `共商共建共享全球治理观`. | B does not fully distinguish in merge layer. | Accept patcher. Literal overlap is insufficient for merge. | Record `do_not_merge`: Q17 cooperation/opening use vs Tongzhou global governance view. |
| AB08 | 2025海淀期中 Q16(2) / image scoring source | Codex A visually verified DOCX embedded `image2.png` as user-confirmed image scoring material; not ordinary text-only reference answer. | B says image rubric was not found and keeps P1/reference status. | Override B with Codex A local visual evidence. Source is `user_confirmed_image_scoring_material`, usable for candidate fusion with evidence label. | Upgrade B blocker to resolved-by-Codex; core term is `利用国际组织赋予的权利，积极参与全球经济治理和规则制定...`. |
| AB09 | 2025海淀期中 Q21(2) / image scoring source | Codex A visually verified embedded `image8.png` table scoring material. | B says image table not found and keeps P1/reference status. | Override B with Codex A local visual evidence. | Upgrade to `user_confirmed_image_scoring_material`; preserve table scoring structure. |
| AB10 | 2025海淀期中 Q21(2) / world background merge | Codex A separates `和平与发展仍是时代主题` from China diplomacy宗旨 `维护世界和平、促进共同发展`. | B puts Q21 under a separate section and risks duplicated era-theme row. | Accept patcher. | Merge Q21 world-change expression into `和平与发展仍是时代主题` core; do not merge with China foreign-policy宗旨. |
| AB11 | 2025海淀期中 Q21(2) / image remarks | Codex A says remarks such as `国际影响力话语权`, `人类命运共同体`, `国家利益` need classification. | B largely leaves them as P1 note. | Pending fine visual classification, but source image is confirmed. | Use as `可用表述/不累计提醒` only after final image note; not promoted as standalone terms in this batch. |
| AB12 | 2024东城一模 Q16 / full prompt | Codex A says prompt was visually read from scanned source PDF. | B says full prompt needs Codex check. | Accept Codex A. Prompt is available from rendered page. | Fill prompt in fusion candidate, keep evidence P2 for scoring and P3 visual support for question text. |
| AB13 | 2024东城一模 Q16/Q20 / evidence level | Codex A marks P2 because the file is a teaching/analysis PPT containing marking details. | B also marks P2/provisional. | Consensus. | Enter fusion candidate as P2 only; never mix into P0 frequency without label. |
| AB14 | 2025海淀期末 Q22 | Not in Codex A Batch01 worker. | B included Q22 as P2 optional knowledge. | Accept as lane B candidate, not yet Codex A evidence-locked. | Add to next Codex A batch for source recheck before main fusion promotion. |
| AB15 | 2026朝阳一模 Q20, 2026顺义一模 Q20, 2025海淀二模 Q21 | Not in Codex A Batch01 worker. | B includes them as P0/P0/P0+评标实录 closed entries. | Useful lane B production, but Codex A has not yet personally rechecked in this run. | Queue as Phase 03 Codex A worker batch 02 before full merge/frequency. |

## Resolved By Codex A

- `2025海淀期中 Q16(2)` and `Q21(2)` are no longer blocked merely because ClaudeCode B did not find the embedded images. Codex A visually verified the DOCX media images and recorded hashes in worker source notes. They remain non-ordinary source material and must be labeled as `user_confirmed_image_scoring_material`.
- `2024东城一模 Q16` full prompt is no longer missing for Batch 01; Codex A has visual source support. The scoring source remains P2.

## Still Open

- `2025海淀期中 Q21(2)` image remarks need final classification: expression variant vs non-cumulative reminder.
- `2025海淀期末 Q22`, `2026朝阳一模 Q20`, `2026顺义一模 Q20`, and `2025海淀二模 Q21` require Codex A recheck before they can enter the main merged table.
- Claude Opus 4.7 teaching-text response is not captured because the screen is locked; no Claude-generated wording may be included yet.

