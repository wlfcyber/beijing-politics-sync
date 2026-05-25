# ClaudeCode Opus 4.7 Batch13 Evidence-Packet Recheck

Use `claude-opus-4-7` with max effort / adaptive thinking. Do not use tools. Review only the evidence packet below and return a bounded production-line recheck. If max/adaptive proof is not machine-confirmable from inside the run, write `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Hard rules:
- Sonnet, Haiku, and model-unknown evidence do not count.
- Ordinary reference answers cannot become scoring rules.
- Choice-question correct-option chains must stay separate from subjective scoring-rule chains.
- GPTPro web and external Claude Opus full-artifact reviews are still `real_call_pending`.
- This is a ClaudeCode production-line recheck, not a lightweight audit. Do not mark final acceptance.

Batch under review: `2026门头沟一模`.

Codex verified counters:
- Matrix rows after Batch13: `897`.
- `2026门头沟一模` matrix rows: `30`.
- `2026门头沟一模` rows still needing placement/fusion adjudication: `0`.
- Global exact waiting rows: `371`.
- Global broader source-review rows: `397`.
- Ledger rows: `92`; `2026门头沟一模` ledger rows: `10`.
- Accepted JSONL rows: `92`; `2026门头沟一模` accepted rows: `10`.
- DOCX label count: `2240`.
- Unique `2026门头沟一模` student-entry headings: `10`.
- PDF page count / rendered PNG count: `243 / 243`.
- Blank-like rendered pages: `0`.

Source/rubric packet:
- Source bundle: `01_source_inventory/suite_source_bundles/2026门头沟一模.md`.
- Paper: `2026各区一模/2026门头沟一模/门头沟区高三政治一模试卷.pdf`.
- Rule files: `2026各区一模/2026门头沟一模/门头沟高三政治一模参考答案及评标细则新.docx` and `2026各区一模/2026门头沟一模/细则/2026门头沟一模细则.docx`.
- Q1-Q15 official answer key: `1 B, 2 D, 3 D, 4 B, 5 C, 6 A, 7 B, 8 C, 9 D, 10 C, 11 C, 12 A, 13 B, 14 A, 15 D`.

Q4:
- Prompt concerns Beijing `两园一河` cultural-tourism integration.
- Official answer is B, using items `①④`.
- Only item `④` supports `坚持从实际出发的态度`.
- Codex action: register existing DOCX coverage under `一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一`.
- Boundary: item `①` is culture-economy integration and is not a separate philosophy placement.

Q5:
- Prompt concerns the Beijing fresh-food market bus line whose station is creatively set in the second-floor trading area.
- Official answer is C, using items `②③`.
- Only item `②` supports `对传统公交模式进行扬弃`.
- Codex action: register existing DOCX coverage under `辩证否定 / 守正创新`.
- Boundary: item `③` is reverse thinking and stays in Logic and Thinking, not the 必修四 body.

Q7:
- Prompt concerns students walking into fields/workrooms, learning agricultural production and cooking practice, and directly feeling labor value.
- Official answer is B, using items `①④`.
- Only item `①` says leaving the classroom and joining field labor shows the practice-first view.
- Codex action: newly insert `2026门头沟一模 第7题` under `实践是认识的基础`.
- Boundary: item `④` is overall/dialectical thinking and is not inserted into 必修四 here.

Q16:
- Prompt: use `哲学与文化` knowledge to understand why 永定河古渠 is not a sleeping cultural relic but a living heritage.
- Formal scoring rules explicitly list philosophy angles: `发展的观点`, `矛盾双方对立统一`, `辩证否定观`, `联系的观点`.
- Codex action: register existing entries under:
  - `联系的普遍性 / 联系的观点（总）`
  - `根据固有联系建立新的具体联系`
  - `发展的观点 / 发展的普遍性`
  - `辩证否定 / 守正创新`
  - `矛盾就是对立统一`
- Evidence level: formal detail-rule wording, not ordinary reference-answer support.

Q21:
- Prompt: integrated knowledge; discuss why China can provide precious certainty for the world.
- Scoring rules allow material 1 to use `哲学或思维`, including `尊重客观规律与发挥主观能动性相结合`, `辩证思维`, `系统思维等`.
- Codex action: register existing entries under:
  - `尊重客观规律与发挥主观能动性相结合`
  - `系统观念 / 系统优化`
- Evidence level: comprehensive-question broad angle support, not point-by-point detailed scoring rules.

Exclusions:
- Q1: party history / red-spirit culture boundary.
- Q2: party history / politics boundary.
- Q3: education / 立德树人 boundary; missing row added.
- Q6: Logic and Thinking boundary; missing row added.
- Q8: Political and Law boundary.
- Q9: Political and Law / ethnic-policy boundary.
- Q10: Legal Life family-support boundary; missing row added.
- Q11: Legal Life / unfair-competition boundary.
- Q12: Economy and Society / social-security boundary.
- Q13: Economy and Society / innovation-index boundary.
- Q14: Contemporary International Politics and Economy boundary.
- Q15: international trade/world economy boundary.
- Q17: Political and Law.
- Q18: Q18(1) Legal Life; Q18(2) explicitly names Logic and Thinking scientific thinking. Near-neighbor terms such as connection/development/contradiction are not forced into 必修四.
- Q19: Economy and Society.
- Q20: Contemporary International Politics and Economy.
- Qunknown: extraction residue.

Render packet:
- PDF was regenerated from current DOCX through local Word COM.
- Page images and contact sheets were generated under `word_render_qa_20260525_batch13_word`.
- Render manifest: `word_render_qa_20260525_batch13_word/render_manifest.json`.
- PDF page count / rendered PNG count: `243 / 243`.
- Blank-like rendered pages: `0`.
- Contact-sheet visual QA covered pages `1-243`.
- Unique `2026门头沟一模` headings in DOCX: `10`.
- DOCX label count: `2240`.

Return exactly:

Decision: pass_with_model_gate_blocked, pass, or fail

Model evidence:
- What is confirmed and what remains blocked.

Source findings:
- Q4, Q5, Q7, Q16, Q21, exclusions, and render gate.

Required corrections:
- exact corrections or `none`.

Residual blockers:
- GPTPro full-artifact external review: real_call_pending.
- Claude Opus external full-artifact review: real_call_pending.
