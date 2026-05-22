# CC0364 Rubric Atom Split Patch

- target: `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/04_merge_audit/merged_rubric_atoms_subjective.csv`
- backup: `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/tool_outputs/pre_cc0364_split_patch_20260519_195037/merged_rubric_atoms_subjective.csv`
- question_id: `CC0364_2026_通州_期末_19_1`
- removed collapsed atoms: 1
- added split atoms: 7

## Split Logic

- `PATCH_CC0364_R01`: 民法典依据 1 分；“以事实为根据，以法律为准绳”只作不重复替代锚点。
- `PATCH_CC0364_R02`: 相邻关系原则 2 分。
- `PATCH_CC0364_R03`: 业主角度事实分析 2 分。
- `PATCH_CC0364_R04`: 范某角度事实分析 1 分；不与 R03 累加。
- `PATCH_CC0364_R05`: 维护业主合法权益 1 分。
- `PATCH_CC0364_R06`: 促进邻里和谐 1 分。
- `PATCH_CC0364_R07`: 践行友善等社会主义核心价值观 1 分。

## Gate Impact

`CC0364` is no longer source-check pending at atom level. It may now be counted as limited support for the expanded 004/006 code branch, while its value-tail atoms cannot independently support a core framework node.
