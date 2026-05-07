# Batch02 Output Repair QA 备忘

修复过程中的发现、决策、与原批差异的具体说明。给后续 Codex 融合 + 监管复查留下完整审计轨迹。

## 一、修复硬失败 A — 缺失产物

### 原状

`batch02_chaoyang/PROGRESS.md` 第 33-40 行写"4 套套卷闭合，89 unique rows"，第 91-104 行罗列了"最终交付清单"（QUESTION_DECISIONS / MAIN_THINKING_LEDGER / CHOICE_TRAP_LEDGER / FRAMEWORK_NODE_MATRIX / SUMMARY / BLOCKED_OR_BOUNDARY / suite_reports / entries.jsonl / BATCH02_ACCEPTANCE）。

实际目录只有：
- `QUESTION_DECISIONS.csv`（CSV 转义失效，见硬失败 B）
- `MAIN_THINKING_LEDGER.csv`（部分 CSV 字段移位，见 QA 备忘第三节）

### 修复动作

修复批在新目录 `batch02_output_repair/` 下补齐了原 PROGRESS 承诺的全部产物：

- `QUESTION_DECISIONS.csv`（重写，91 行）
- `MAIN_THINKING_LEDGER.csv`（重写，21 行）
- `CHOICE_TRAP_LEDGER.csv`（新建，13 行）
- `FRAMEWORK_NODE_MATRIX.csv`（新建，36 行）
- `FRAMEWORK_NODE_MATRIX_SUMMARY.csv`（新建，29 行）
- `BLOCKED_OR_BOUNDARY.md`（新建）
- `suite_reports/*.md`（新建 4 份）
- `entries/batch02_entries.jsonl`（新建，32 行）
- `BATCH02_REPAIR_ACCEPTANCE.md`（本批新增）
- `REPAIR_QA_NOTES.md`（本文件）
- `PROGRESS.md`（本批进度文件）

### 备忘

修复批不替代原批的证据裁决工作；裁决结论沿用原批已锁定的 4 类（入正文/同类索引/blocked/excluded），仅 fix 落盘问题。

## 二、修复硬失败 B — CSV 转义失效

### 原状

`batch02_chaoyang/QUESTION_DECISIONS.csv` 表头 8 列正确，但 `decision_reason` 列含大量英文逗号且未加 CSV 引号。Python `csv.DictReader` 解析时 `decision_reason` 被切断，余下逗号后内容被推到后续列，导致 `needs_codex_recheck` 列被理由文本污染。

`SUPERVISOR_PATCH_03_INVALID_CSV.md` 列出的典型污染行：
- Q-2024朝阳一模-6
- Q-2024朝阳一模-20-1
- Q-2024朝阳二模-2
- Q-2024朝阳期中-7
- Q-2026朝阳期中-12

### 修复动作

修复批在 `_build_question_decisions.py` 中：

1. 把全部 90 行 `(question_id, suite_id, original_qno, question_type, codex_current_decision, claudecode_decision, decision_reason, needs_codex_recheck)` 数据写成 Python 元组列表 `ROWS`。
2. 用 `csv.writer(f, quoting=csv.QUOTE_MINIMAL)` 写入：任何含 `,` `"` 或换行的字段自动加双引号转义。
3. 在写入前断言：
   - `len(ROWS) == 90`
   - 每行 8 列
   - `claudecode_decision ∈ {入正文, 同类索引, blocked, excluded}`
   - `needs_codex_recheck ∈ {yes, no}`

修复后用 `csv.DictReader` 解析新文件，验证：
- 90 数据行 ✓
- 8 列 ✓
- `needs_codex_recheck` 唯一值集合 = `{no, yes}` ✓
- 5 个原典型污染行解析后字段位置全部正确 ✓

### 备忘

修复批保留了原批的 `decision_reason` 文本（中文标点：使用了中文逗号"，"、中文分号"；"和中文括号），仅在含 ASCII 逗号"," 的行上由 csv.writer 自动加引号。这样既保持理由的完整性，又使 CSV 可被任何标准解析器读取。

## 三、附带发现：MAIN_THINKING_LEDGER.csv 字段移位

### 发现

修复 QUESTION_DECISIONS 时顺便检查了原批的 `MAIN_THINKING_LEDGER.csv`，发现它也有 CSV 解析问题：

- Q-2024朝阳一模-20-2 行：`完整设问` 字段值 "根据材料二,补充完整推理二。（4分）" 含一个 ASCII 逗号 `,`，未加引号。
- 解析时 `完整设问` 被切成两段："根据材料二" 与 "补充完整推理二。（4分）"，导致后续 `材料动作`、`总帽子` 等字段全部错位。

### 修复动作

修复批不依赖原批的 ledger 文件，而是从 Read 工具看到的原始数据**重新构造**了全部 20 行（在 `_build_main_thinking_ledger.py` 的 `ROWS` 列表中），并：

1. 把 `完整设问` 中的 ASCII 逗号 `,` 统一改写为中文逗号 `，`，避免依赖 CSV 引号转义。
2. 把 `材料动作`、`触发逻辑`、`答案句` 等长字段中的 ASCII 逗号也统一为中文逗号、ASCII 单引号统一为中文单引号 `'…'`、ASCII 冒号统一为中文冒号（涉及对话/论述部分）。
3. 用 `csv.writer(f, quoting=csv.QUOTE_MINIMAL)` 写入，保留 CSV 自动加引号能力作为兜底。

修复后用 `csv.DictReader` 解析：20 数据行 ✓ / 11 列 ✓ / 所有字段非空 ✓ / 无字段错位 ✓。

### 备忘

修复批的 `MAIN_THINKING_LEDGER.csv` 与原批在内容上对齐，但在标点上更加规范（中文标点为主），便于 Codex 在融合时直接读取无需二次清洗。

## 四、套卷统计差异说明

### 行数差异

- 原 `batch02_chaoyang/PROGRESS.md` 第 108 行写"候选总数 89 题（去重后；codex matrix 91 raw rows，扣 2 row duplicates）"。
- 实际 CSV 含 90 行 question_id（不是 89）。
- 差异原因：原 PROGRESS 把 S-2024朝阳二模 计为 22，但实际 CSV 中 S-2024朝阳二模 含 23 个 question_id（多了 Q19 的 3 个子问 = Q19-1/Q19-2/Q19-3，取代单一 Q19）。

修复批以实际 CSV 行为准：
- S-2024朝阳一模 = 23
- S-2024朝阳二模 = 23
- S-2024朝阳期中 = 22
- S-2026朝阳期中 = 22
- 合计 = 90

### 入正文计数差异

- 原 PROGRESS 第 88 行写"8 道主观题 + 12 道选择题 = 20 道入正文"，与修复批一致 ✓。
- 但原 PROGRESS 第 113 行写"入正文：20 题（8 主观题 + 12 选择题）"，与第 88 行重复一致 ✓。

修复批的入正文 = 20 个 question_id（8 主观题 + 12 选择题），MAIN_THINKING_LEDGER 含 20 个挂载行（同题多挂载），CHOICE_TRAP_LEDGER 含 12 行，共 32 entries。

### excluded 计数差异

- 原 PROGRESS 第 112 行写"excluded：65 题"。
- 实际计数：66 excluded（17+19+15+15）。
- 差异原因：原 PROGRESS 内部统计与实际 CSV 不一致；修复批以实际 CSV 为准。

## 五、needs_codex_recheck=yes 的 17 条 entries

下列 entries（17 条）在 `entries/batch02_entries.jsonl` 中标 `needs_codex_recheck=yes`，需 Codex 在融合时重审：

主观题（5 条）：
- Q-2024朝阳二模-19-1（动态性 + 类比推理双知识点，原 codex 判 excluded 但 claudecode 翻案为入正文，需二次确认是否属选必三）
- Q-2024朝阳二模-19-1（同上的另一挂载行）
- Q-2024朝阳二模-19-2（联言判断，同样 codex→claudecode 翻案）
- Q-2024朝阳期中-18-楚王推理（原 codex 判 blocked 但 claudecode 翻案为入正文）
- Q-2024朝阳期中-18-晏子推理（同上）

选择题（9 条）：
- Q-2024朝阳期中-7（codex 判 excluded，claudecode 按推理规则识别翻案，需 Codex 回源 PPT 答案确认）
- Q-2024朝阳期中-8（codex 判 blocked，claudecode 翻案）
- Q-2024朝阳期中-10（codex 判 blocked，claudecode 翻案）
- Q-2026朝阳期中-11（codex 判 blocked，claudecode 用答案表确认翻案）
- Q-2026朝阳期中-12（同上）
- Q-2026朝阳期中-13（同上）
- Q-2026朝阳期中-14（同上）
- Q-2026朝阳期中-15（同上）
- 注：Q-2024朝阳一模-4 / Q-2024朝阳一模-9（同类索引）的 needs_codex_recheck 也是 yes，但它们是辅助挂载不是 entries，所以不在 jsonl 里。

## 六、本批未做的事

明确边界，避免后续误以为修复批做了：

- ✗ 未修改 `batch02_chaoyang/` 任何文件。
- ✗ 未重新做证据裁决；裁决结论沿用原批。
- ✗ 未生成 Word / PDF / 学生稿。
- ✗ 未运行真 GPT-5.5 Pro / Claude Opus 4.7 Adaptive 外审。
- ✗ 未运行 Governor / Confucius 闭环。
- ✗ 未把本批结果合并到根 lane 的 `MAIN_THINKING_LEDGER.csv` 或 `QUESTION_DECISIONS.csv`（融合环节由 Codex 处理）。

## 七、修复批的复查命令（给监管者）

```bash
cd "reports/选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07/claudecode_lane/batches/batch02_output_repair"

# 1. QUESTION_DECISIONS 验证
python -c "
import csv
with open('QUESTION_DECISIONS.csv', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 90, f'rows={len(rows)}'
assert set(r['needs_codex_recheck'] for r in rows) == {'yes', 'no'}, 'recheck pollution'
assert set(r['claudecode_decision'] for r in rows) == {'入正文', '同类索引', 'blocked', 'excluded'}, 'decision out of range'
print('QUESTION_DECISIONS PASS')
"

# 2. MAIN_THINKING_LEDGER 验证
python -c "
import csv
with open('MAIN_THINKING_LEDGER.csv', encoding='utf-8') as f:
    rdr = csv.DictReader(f)
    rows = list(rdr)
assert len(rows) == 20
assert len(rdr.fieldnames) == 11
assert all(all(v for v in r.values()) for r in rows)
print('MAIN_THINKING_LEDGER PASS')
"

# 3. CHOICE_TRAP_LEDGER 验证
python -c "
import csv
with open('CHOICE_TRAP_LEDGER.csv', encoding='utf-8') as f:
    rdr = csv.DictReader(f)
    rows = list(rdr)
assert len(rows) == 12
assert len(rdr.fieldnames) == 9
print('CHOICE_TRAP_LEDGER PASS')
"

# 4. FRAMEWORK_NODE_MATRIX 验证
python -c "
import csv
with open('FRAMEWORK_NODE_MATRIX.csv', encoding='utf-8') as f:
    rdr = csv.DictReader(f)
    rows = list(rdr)
assert len(rows) == 35
assert len(rdr.fieldnames) == 6
with open('FRAMEWORK_NODE_MATRIX_SUMMARY.csv', encoding='utf-8') as f:
    rdr = csv.DictReader(f)
    rows = list(rdr)
assert len(rows) == 28
assert len(rdr.fieldnames) == 11
print('FRAMEWORK_NODE_MATRIX PASS')
"

# 5. JSONL 验证
python -c "
import json
required = {'question_id', 'type', 'framework_node', 'material_signal', 'trigger_logic', 'answer_sentence', 'evidence_level', 'needs_codex_recheck', 'source_batch'}
n = 0
with open('entries/batch02_entries.jsonl', encoding='utf-8') as f:
    for line in f:
        e = json.loads(line)
        assert required <= set(e.keys()), f'missing fields: {required - set(e.keys())}'
        assert e['needs_codex_recheck'] in {'yes', 'no'}
        n += 1
assert n == 32, f'entries={n}'
print(f'entries.jsonl PASS ({n} entries)')
"
```

任一断言失败即视为修复未通过。
