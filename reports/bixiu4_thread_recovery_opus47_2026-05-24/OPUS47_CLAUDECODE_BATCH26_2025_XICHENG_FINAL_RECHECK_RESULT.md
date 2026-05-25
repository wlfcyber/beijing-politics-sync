# ClaudeCode Batch26 Recheck Result - 2025 Xicheng Final

- `content_result`: `pass`
- `local_policy_result`: `pass_with_model_gate_blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `return_code`: `0`
- `timed_out`: `false`
- Observed models: `claude-haiku-4-5-20251001, claude-opus-4-7`
- Debug model mentions: `claude-haiku-4-5-20251001, claude-opus-4-7`
- Thinking block/signature seen: `true`

## ClaudeCode Final Response

All seven required files were located and read. The matrix CSV (rows 1139–1169) contains exactly 31 `2025西城期末` rows: 14 body rows (Q1/Q2/Q3/Q4/Q7 objective + Q18 ×7 + Q21 ×2) and 17 boundary rows (Q5/Q6/Q8–Q15, Q16(1), Q16(2), Q17(1), Q17(2), Q19, Q20, Q21-nonphilosophy). Rubric lines 114 and 116 explicitly contain `矛盾具有普遍性` and `价值观具有导向作用`; rubric lines 190–193 explicitly contain the 改革 essence/social-basic-contradiction language while 法治/党领导 are kept in the Q21-nonphilosophy boundary row. Teacher-version answer key confirms 1D 2B 3C 4D 7B for the objective-only rows. Render manifest reports 259/259 pages, 0 blank body pages, DOCX/PDF labels 2423/2423, Word-visible headings 14/14, and raw PDF text extraction 0 (consistent with Batch21–25).

---

- `content_result`: `pass`
- `local_policy_result`: `pass_with_model_gate_blocked`
- `batch26_status`: `LOCAL_CLOSED_CONTENT_RENDER_PASS_WITH_MODEL_GATE_BLOCKED`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `findings`:
  - Source pair matched: `89d264a31e348be6_2025西城期末细则.md` (formal rubric) and `6662da1c2772cc38_2025北京西城高三_上_期末政治_教师版.md` (teacher version) are both referenced in the transcription, fusion, and every matrix row's `source_path` column.
  - Matrix coverage is exactly 31 rows (CSV lines 1139–1169): 14 body rows = Q1 + Q2 + Q3 + Q4 + Q7 (objective) + Q18 ×7 + Q21 ×2; 17 boundary rows = Q5, Q6, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16(1), Q16(2), Q17(1), Q17(2), Q19, Q20, Q21-nonphilosophy.
  - Q1/Q2/Q3/Q4/Q7 rows are explicitly objective-only via `KEEP_IN_BODY_OBJECTIVE_ONLY` and `必修四哲学选择题客观挂点` / `教师版客观题答案`; ordinary teacher-version key is not upgraded to subjective scoring.
  - Q18 additions are formal-rubric-supported: rubric line 114 `矛盾具有普遍性` backs matrix row M1144 (`矛盾的普遍性`); rubric line 116 `价值观具有导向作用` backs row M1141 (`价值观的导向作用`). Both rows are also recorded as new DOCX inserts in the fusion file.
  - Q21 改革 row (M1147) is anchored to rubric lines 190–193 (`改革是社会主义制度的自我完善和自我发展` / `改革是解决社会基本矛盾;社会主义社会发展的直接动力`); 法治/党的领导 dimensions are isolated in boundary row M1168 (`NONPHILOSOPHY_COMPREHENSIVE_POINT_BOUNDARY_EXCLUDED`) and are not absorbed into philosophy points.
  - Render QA per manifest: DOCX/PDF label counts `2423/2423`, DOCX heading count `14`, Word-visible heading count `14/14`, blank-like body pages excluding cover/foreword `0`, raw PDF text extraction `0` (Word-generated PDF does not preserve the exact Chinese string), with Word layout pages `88, 96, 107, 121, 131, 137, 174, 186, 196, 208, 209, 213, 239, 240` and rendered PNGs providing visibility — consistent with the Batch21–25 pattern.
  - GPTPro web review and external Claude Opus full-artifact review remain `real_call_pending`; no STRICT_FINAL_ACCEPTED claim is made; Sonnet/Haiku/model-unknown evidence is not used.
- `required_fixes`: `none`
