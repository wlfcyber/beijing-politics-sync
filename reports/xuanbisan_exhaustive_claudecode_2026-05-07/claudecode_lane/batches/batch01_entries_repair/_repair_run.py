# -*- coding: utf-8 -*-
"""
Batch01 Entries Repair: read MAIN_THINKING_LEDGER and CHOICE_TRAP_LEDGER,
emit batch01_entries.jsonl with the requested field schema.

Field mapping (中文含义映射):

MAIN_THINKING_LEDGER -> main_thinking entries
  question_id           <- question_id
  framework_node        <- 框架落点
  material_signal       <- 材料动作
  trigger_logic         <- 触发逻辑
  answer_sentence       <- 答案句
  evidence_level        <- 证据等级
  needs_codex_recheck   <- QUESTION_DECISIONS.csv [needs_codex_recheck]
  source_batch          = 'batch01_haidian_xicheng'

CHOICE_TRAP_LEDGER -> choice_trap entries
  question_id           <- question_id
  framework_node        <- 陷阱类型 (closest 中文 match in source CSV)
  material_signal       <- 题干信号
  trigger_logic         <- (源 CSV 无对应字段，留空)
  answer_sentence       <- 正确项理由
  evidence_level        <- (源 CSV 无对应字段，留空)
  needs_codex_recheck   <- QUESTION_DECISIONS.csv [needs_codex_recheck]
  source_batch          = 'batch01_haidian_xicheng'

Note on robust parsing: source CSVs contain rows where unquoted commas appear
inside parenthetical Chinese text (e.g. (种与属可换写,关系本身不变)). When a row
has more fields than the header count, we collapse extras into the known
"messy" middle column for that file, leaving fixed-shape leading and trailing
columns intact.
"""
import csv
import json
import os
import io

BASE = r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07\claudecode_lane\batches"
SRC = os.path.join(BASE, "batch01_haidian_xicheng")
DST = os.path.join(BASE, "batch01_entries_repair")

QD_PATH = os.path.join(SRC, "QUESTION_DECISIONS.csv")
MTL_PATH = os.path.join(SRC, "MAIN_THINKING_LEDGER.csv")
CTL_PATH = os.path.join(SRC, "CHOICE_TRAP_LEDGER.csv")
OUT_JSONL = os.path.join(DST, "batch01_entries.jsonl")


def read_robust_dicts(path, messy_col_index_from_left, num_left_fixed, num_right_fixed):
    """
    Read a CSV that may contain unquoted commas inside one specific 'messy' column.
    Standard csv.reader handles quoted fields. For rows with extra fields, collapse
    the surplus into the messy column.

    num_left_fixed: number of leading columns that are reliably comma-free or quoted.
    num_right_fixed: number of trailing columns that are reliably comma-free.
    The messy column sits between left and right blocks.
    """
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    header = rows[0]
    n = len(header)
    out = []
    fix_count = 0
    for raw in rows[1:]:
        if not raw or all(not c.strip() for c in raw):
            continue
        if len(raw) == n:
            row = dict(zip(header, raw))
        elif len(raw) > n:
            # Collapse extras into the messy column.
            left = raw[:num_left_fixed]
            right = raw[-num_right_fixed:] if num_right_fixed > 0 else []
            middle_chunks = raw[num_left_fixed:len(raw) - num_right_fixed]
            messy = ",".join(middle_chunks)
            collapsed = left + [messy] + right
            assert len(collapsed) == n, (path, len(collapsed), n, raw)
            row = dict(zip(header, collapsed))
            fix_count += 1
        else:
            # Row is short - pad with empties (shouldn't happen for well-formed source).
            padded = raw + [""] * (n - len(raw))
            row = dict(zip(header, padded))
        out.append(row)
    return header, out, fix_count


def main():
    # QUESTION_DECISIONS: 8 cols
    # 0 question_id, 1 suite_id, 2 original_qno, 3 question_type,
    # 4 codex_current_decision, 5 claudecode_decision,
    # 6 decision_reason (messy), 7 needs_codex_recheck
    qd_header, qd_rows, qd_fixes = read_robust_dicts(
        QD_PATH, messy_col_index_from_left=6, num_left_fixed=6, num_right_fixed=1
    )

    # MAIN_THINKING_LEDGER: 11 cols
    # 0 question_id, 1 来源, 2 完整设问, 3 材料动作, 4 总帽子, 5 小方法,
    # 6 触发逻辑, 7 答案句, 8 证据等级, 9 框架落点, 10 题型标签
    # The long fields (2/3/6) are quoted in source. 答案句(7) is unquoted but uses
    # Chinese commas only. Treat 7 as the safest "messy" candidate just in case.
    mtl_header, mtl_rows, mtl_fixes = read_robust_dicts(
        MTL_PATH, messy_col_index_from_left=7, num_left_fixed=7, num_right_fixed=3
    )

    # CHOICE_TRAP_LEDGER: 8 cols
    # 0 question_id, 1 题干信号, 2 完整选项或选项单位, 3 答案源,
    # 4 正确项理由, 5 诱人错项 (messy), 6 陷阱类型, 7 是否可入学生稿
    ctl_header, ctl_rows, ctl_fixes = read_robust_dicts(
        CTL_PATH, messy_col_index_from_left=5, num_left_fixed=5, num_right_fixed=2
    )

    qd_lookup = {r["question_id"]: r.get("needs_codex_recheck", "") for r in qd_rows}

    entries = []
    main_count = 0
    choice_count = 0
    main_missing_qd = []
    choice_missing_qd = []

    for r in mtl_rows:
        qid = (r.get("question_id") or "").strip()
        if not qid:
            continue
        ncr = qd_lookup.get(qid, "")
        if qid not in qd_lookup:
            main_missing_qd.append(qid)
        entries.append({
            "question_id": qid,
            "type": "main_thinking",
            "framework_node": (r.get("框架落点") or "").strip(),
            "material_signal": (r.get("材料动作") or "").strip(),
            "trigger_logic": (r.get("触发逻辑") or "").strip(),
            "answer_sentence": (r.get("答案句") or "").strip(),
            "evidence_level": (r.get("证据等级") or "").strip(),
            "needs_codex_recheck": (ncr or "").strip(),
            "source_batch": "batch01_haidian_xicheng",
        })
        main_count += 1

    for r in ctl_rows:
        qid = (r.get("question_id") or "").strip()
        if not qid:
            continue
        ncr = qd_lookup.get(qid, "")
        if qid not in qd_lookup:
            choice_missing_qd.append(qid)
        entries.append({
            "question_id": qid,
            "type": "choice_trap",
            "framework_node": (r.get("陷阱类型") or "").strip(),
            "material_signal": (r.get("题干信号") or "").strip(),
            "trigger_logic": "",
            "answer_sentence": (r.get("正确项理由") or "").strip(),
            "evidence_level": "",
            "needs_codex_recheck": (ncr or "").strip(),
            "source_batch": "batch01_haidian_xicheng",
        })
        choice_count += 1

    with open(OUT_JSONL, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    print(f"main_thinking entries: {main_count}")
    print(f"choice_trap entries:   {choice_count}")
    print(f"total:                 {len(entries)}")
    print(f"QUESTION_DECISIONS rows fixed (extra-comma collapse): {qd_fixes}")
    print(f"MAIN_THINKING_LEDGER rows fixed: {mtl_fixes}")
    print(f"CHOICE_TRAP_LEDGER rows fixed:   {ctl_fixes}")
    print(f"main qid missing in QUESTION_DECISIONS: {main_missing_qd}")
    print(f"choice qid missing in QUESTION_DECISIONS: {choice_missing_qd}")
    print(f"wrote: {OUT_JSONL}")


if __name__ == "__main__":
    main()
