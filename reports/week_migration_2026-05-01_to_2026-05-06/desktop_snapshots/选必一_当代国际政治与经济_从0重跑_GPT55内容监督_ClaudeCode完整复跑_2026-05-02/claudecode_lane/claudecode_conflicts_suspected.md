# Suspected Conflicts — ClaudeCode Lane Phase 02

run_id: xuanbiyi_zero_gpt55_claudecode_2026-05-02
compiled_date: 2026-05-03

This file records suspected conflicts between:
- ClaudeCode lane entries vs. Codex lane entries (cross-lane divergence)
- ClaudeCode Phase 02 verified evidence vs. existing entries (within-lane revision needs)
- Source-level ambiguities where two plausible interpretations exist

These are not errors yet. They are items requiring reconciliation before Phase 5 fusion.

---

## PHASE 03 ADDENDUM — 2026-05-03 Codex Reconciliation

*Added by ClaudeCode Phase 03. Supersedes prior conflict classifications where noted.*

### CONFLICT UPDATE 1: 2026西城期末 Q20 — Old Blocker Superseded

**Prior ClaudeCode status**: `provisional_blocker` — scanned 细则.pdf unreadable; paper folder empty; question text unconfirmed.

**Superseded by**: Codex located teacher-version PDF in GaokaoPolitics mirror (allowed supplemental source). Codex visually read 细则.pdf pages 4-5 and confirms 3-angle scoring structure. 6 term entries confirmed.

**ClaudeCode position**: Acknowledges Codex visual read. Old `provisional_blocker` is SUPERSEDED. Q20 is now included in Phase 03 draft with `needs_codex_visual_ack` notation. The underlying source discrepancy (scanned PDF, missing paper in primary folder) is noted in 细则位置 for Codex fusion review.

**No longer a fusion blocker.** Codex owns the final inclusion decision.

---

### CONFLICT UPDATE 2: 2025海淀期中 Q16(2)/Q21(2) — P1 Classification Superseded

**Prior ClaudeCode classification**: `provisional_P1` — reference answer only; image/table formal rubric not found.

**Superseded by**: Codex conflict register C-2025HDQZ-evidence-level documents that `細则.docx` contains embedded scoring images. `image2.png` = Q16(2) scoring detail; `image8.png` = Q21(2) scoring table. Both images extracted to `02_extraction/codex_extraction_logs/2025海淀期中/docx_media/`.

**ClaudeCode position**: Acknowledges Codex embedded-image evidence. P1 classification is SUPERSEDED. Entries now classified `codex_visual_evidence_acknowledged` in Phase 03 draft. If Codex evidence is confirmed, these entries are P0. ClaudeCode cannot independently OCR or view the PNG images to disprove the Codex finding.

**C-2025HDQZ-evidence-level**: ClaudeCode acknowledges this conflict is resolved in Codex's favor. Status: `claudecode_ack_complete`.

---

### CONFLICT UPDATE 3: 2025海淀期末 Q22 — Remains Evidence-Level Caution, Not Exclusion

**Prior ClaudeCode classification**: P2 (teacher training PPT).

**Current status**: Confirmed P2 by both ClaudeCode and Codex. Source anomaly (小学教师研修 PPT header) is a watch item. The Q22 slides align with the paper question. Both lanes agree: include at P2 with evidence caveat.

**This is not a fusion conflict.** Both lanes confirm P2 inclusion.

---

### CONFLICT UPDATE 4: 2024东城一模 Q16/Q20 — ClaudeCode P2 vs. Codex P0

**Prior ClaudeCode classification**: P2 (试题分析 PPT header).

**Codex classification**: P0_current_run_source_checked (formal_marking_detail, based on visual read of actual slide content).

**ClaudeCode position**: The document type discrepancy (试题分析 header vs. 阅卷细则 slide content) is a real ambiguity. ClaudeCode's P2 was based on the document header. Codex's P0 is based on the slide content being verified as actual marking detail. For Phase 03 draft, these entries are included with boundary caution, and the P0/P2 discrepancy is flagged for Codex fusion review.

**Fusion action needed**: Codex should confirm that slide 26 ("16题阅卷细则") and slide 64 content are definitively from the marking session, not just teaching analysis. If confirmed, upgrade all Phase 03 draft entries for this suite from P2 to P0.

---

### CONFLICT UPDATE 5: Phase 03 New Findings vs. Existing Index

**2026顺义一模 Q20**: NEW entry — P0 confirmed from formal scoring PPT slide 9. No prior entry exists in either lane. No conflict. Add to fusion pool.

**2026朝阳一模 Q20**: NEW entry — P0 confirmed from formal scoring rubric DOCX (lines 82-98). No prior entry exists in either lane. No conflict. Module boundary: `中国坚定不移扩大高水平对外开放` → 必修二 excluded; `推动贸易投资自由化便利化` and `两个市场两种资源` → 选必一 included.

**2025海淀二模 Q21**: NEW entry — P1 from 细则.docx (参考答案格式 with point-by-point scores); P0 via 评标实录.docx confirmation. No prior entry exists in either lane. No conflict. Add to fusion pool.

---

---

## Conflict C-01: 2026通州期末 Q20 — 完整设问标点差异

**Type**: Within-lane text accuracy
**Severity**: Low — formatting only

**Issue**:
- Existing entry `entries/2026_通州期末_Q20.md` uses: "正逢其时、指引方向彰显担当"
- Source confirmed from 细则.pptx slide 14: "正逢其时、指引方向、彰显担当" (three separate phrases)

**Correct version**: "正逢其时、指引方向、彰显担当" (with comma between 指引方向 and 彰显担当)

**Resolution**: Update existing entry's 完整设问 field with correct punctuation. Must also check Codex entry for same issue.

---

## Conflict C-02: 2026通州期末 Q20 — 共商共建共享全球治理观 Framework Bucket

**Type**: Cross-lane framework placement conflict (anticipated)
**Severity**: Medium — affects student document section organization

**Issue**:
- Existing ClaudeCode entry places 共商共建共享全球治理观 under 〔理论〕 section
- Per xuanbiyi-term-protocol.md: 共商共建共享的全球治理观 belongs in 政治多极化 (governance orientation term)
- Codex entry placement not yet verified — likely also needs checking

**Correct placement**: 政治多极化 bucket

**Resolution**: Move 共商共建共享全球治理观 entry to 政治多极化 in final student document. Both lanes need to align. This is the most likely cross-lane placement conflict.

---

## Conflict C-03: 2026通州期末 Q20 — Point 2 Grouping Method

**Type**: Entry structure interpretation
**Severity**: Low-Medium — affects student document

**Issue**:
- Source rubric groups 时代主题/经济全球化/顺应各国人民愿望 as a single 2-point item ("基本都给")
- Existing ClaudeCode entry splits them into two separate entries: 时代主题 (时代背景 bucket) and 经济全球化 (经济全球化 bucket)
- The split is acceptable for teaching purposes but must clearly signal that these are alternative/parallel within one scoring group, NOT independent mandatory points

**Risk**: If a student reads both entries as separate must-write points, they may not realize one covers the other.

**Resolution**: Both entries should include a note in 细则位置: "第2采分点共2分，与[经济全球化/时代主题]并列可替换，写任意合理内容基本均给"

---

## Conflict C-04: 2026通州期末 Q20 — Point 5 人类命运共同体 Bucket

**Type**: Framework placement conflict
**Severity**: Medium

**Issue**:
- Existing ClaudeCode entry places 人类命运共同体 under 〔理论〕 section
- Term protocol: 推动构建人类命运共同体 when the emphasis is on global political order → 政治多极化
- But when China is the actor and purpose is China's global responsibility → 中国 bucket
- The scoring rubric labels it as point 5 which is about the vision/direction of the倡议 — this leans toward 政治多极化 or 中国 depending on how the question is framed
- The question asks about "指引方向" (Point 5 is the direction goal) and "彰显担当" (Point 6 is China's contribution)

**Resolution**: Per term protocol, when 人类命运共同体 answers "what direction" → 政治多极化. When answering "China's goal/contribution" → 中国. For Q20 Point 5, it is the goal of the 倡议, so 政治多极化 is more appropriate. But this is not a hard error — the entry should include a placement note.

---

## Conflict C-05: 2026朝阳期中 Q17 — 变通规则 Not Documented in Entry

**Type**: Within-lane missing information
**Severity**: Low — does not affect accuracy, affects completeness

**Issue**:
- Source rubric includes an explicit 变通 rule for all three layers: if no formal 总说 phrase but context implies the relationship, full layer points can still be awarded
- Existing ClaudeCode entry does not mention this 变通 rule anywhere

**Resolution**: Add 变通 note to 细则位置 field of all three layer entries. This is important for student understanding of how to write the answer.

---

## Conflict C-06: 2026朝阳期中 Q17 — 满分结构 Not Clearly Stated

**Type**: Within-lane missing information
**Severity**: Low

**Issue**:
- Source rubric: 一层3分，两层6分，三层8分 (scoring caps at 8分 for three layers; each layer is 3 points)
- Existing entry does not clearly state this structure in 细则位置

**Resolution**: Add "一层3分两层6分三层8分满分结构" to 细则位置 in each layer entry.

---

## Conflict C-07: 2025海淀期末 Q22 — Evidence Level Disagreement (Anticipated Cross-Lane)

**Type**: Anticipated cross-lane evidence classification conflict
**Severity**: Medium

**Issue**:
- ClaudeCode Phase 02 classifies 2025海淀期末 细则.pptx as P2 (teacher training PPT with scoring content)
- Codex may have classified it differently (P0 if not verifying the file header, or P2 if checking)
- The previous run's blocker said "细则.pptx是小学教师研修课程PPT，非本题评分细则；正式细则下落不明" — this ClaudeCode run confirms the P2 classification but notes the file DOES contain Q22 scoring detail

**Resolution**: ClaudeCode verdict: P2 source with confirmed 选必一 terms. Codex should independently verify. If Codex finds formal 评标 elsewhere and classifies as P0, that would be a positive resolution. If both confirm P2, entries should be marked P2.

---

## Conflict C-08: 2024东城一模 Q20 — 推进制度型开放 Module Boundary

**Type**: Module boundary disputed
**Severity**: Medium — affects inclusion in 选必一 main table

**Issue**:
- Source (试题分析 PPTX slide 64): "推进制度型开放" appears as a Q20 scoring point alongside 经济全球化/两个市场两种资源
- "推进制度型开放" can be 必修二 (深化改革开放/对外开放) or 选必一 (经济全球化参与路径)
- User requirement states: "2024东城一模 Q20：推进制度型开放...属于选必一经济全球化链，必须补入" — user explicitly assigns it to 选必一
- But the source document is P2 and the boundary is inherently ambiguous

**Resolution**: Follow user requirement — 推进制度型开放 goes in 选必一 经济全球化 chain. Mark evidence level P2 and add module boundary note.

---

## Conflict C-09: 2025海淀期中 Q16(2) — "充分利用两种资源两个市场" Module Boundary

**Type**: Module boundary ambiguity
**Severity**: Low — user requirement already resolves this

**Issue**:
- "充分利用国际国内两种资源、两个市场" appears in Q16(2) reference answer
- This term appears in both 必修二 (对外开放/国内大循环) and 选必一 (经济全球化) contexts
- Q16(2) is about enterprise "出海" strategy (企业跨国经营) — this could be either module depending on how the question frames the knowledge requirement

**Resolution**: User requirement states this is 选必一 content. Include in 选必一 table with P1 evidence level. Note module context in entry.

---

## Summary Table

| Conflict ID | Suite/Question | Type | Severity | Action Required |
|---|---|---|---|---|
| C-01 | 2026通州Q20 | 标点差异 | Low | 修正完整设问标点 |
| C-02 | 2026通州Q20 | Bucket placement | Medium | 移动到政治多极化 |
| C-03 | 2026通州Q20 | Point 2 grouping | Low-Medium | 添加并列说明注释 |
| C-04 | 2026通州Q20 | Point 5 bucket | Medium | 确认人类命运共同体最终放政治多极化 |
| C-05 | 2026朝阳期中Q17 | Missing 变通 rule | Low | 补充细则位置字段 |
| C-06 | 2026朝阳期中Q17 | Missing 满分结构 | Low | 补充细则位置字段 |
| C-07 | 2025海淀期末Q22 | Cross-lane P2 vs P0 | Medium | 等待Codex验证 |
| C-08 | 2024东城一模Q20 | 制度型开放 boundary | Medium | 按用户规定选必一 |
| C-09 | 2025海淀期中Q16(2) | 两种资源 boundary | Low | 按用户规定选必一 |
