"""Generate entries/batch02_entries.jsonl with valid JSON per line.

Required fields per row:
  question_id, type, framework_node, material_signal, trigger_logic,
  answer_sentence, evidence_level, needs_codex_recheck, source_batch
"""
import csv
import json
from pathlib import Path

OUT_DIR = Path(__file__).parent / "entries"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "batch02_entries.jsonl"

REQUIRED = [
    "question_id", "type", "framework_node", "material_signal",
    "trigger_logic", "answer_sentence", "evidence_level",
    "needs_codex_recheck", "source_batch",
]

SOURCE_BATCH = "batch02_output_repair"

# Read MAIN_THINKING_LEDGER (subjective entries) and CHOICE_TRAP_LEDGER
# (choice entries) and assemble JSONL.
LEDGER_DIR = Path(__file__).parent

entries = []

# --- Subjective entries from MAIN_THINKING_LEDGER ---
with open(LEDGER_DIR / "MAIN_THINKING_LEDGER.csv", encoding="utf-8") as f:
    rdr = csv.DictReader(f)
    for r in rdr:
        entries.append({
            "question_id": r["question_id"],
            "type": "main_thinking",
            "framework_node": r["框架落点"],
            "material_signal": r["材料动作"],
            "trigger_logic": r["触发逻辑"],
            "answer_sentence": r["答案句"],
            "evidence_level": r["证据等级"],
            "needs_codex_recheck": "no",  # subjective entries here are all locked
            "source_batch": SOURCE_BATCH,
        })

# Mark hard samples + Q-2024朝阳二模-19 entries that originated from
# codex=excluded but flipped to claudecode=入正文 -> need recheck=yes
# (matches the QUESTION_DECISIONS.csv recheck flags)
recheck_yes_qids = {
    "Q-2024朝阳二模-19-1-动态性",
    "Q-2024朝阳二模-19-1-类比推理",
    "Q-2024朝阳二模-19-2",
    "Q-2024朝阳期中-18-楚王推理",
    "Q-2024朝阳期中-18-晏子推理",
}
for e in entries:
    if e["question_id"] in recheck_yes_qids:
        e["needs_codex_recheck"] = "yes"

# --- Choice entries from CHOICE_TRAP_LEDGER ---
# For choice entries, we map: framework_node from FRAMEWORK_NODE_MATRIX,
# material_signal from 题干信号, trigger_logic from 正确项理由,
# answer_sentence from a synthesized "正确选项 + 推理 + 陷阱辨别" string.
# This keeps each choice-entry self-contained with the 9 required fields.
choice_framework_map = {
    "Q-2024朝阳一模-6": "形式逻辑>逻辑规则综合（排中律/矛盾律/越级划分/四概念）",
    "Q-2024朝阳一模-7": "创新思维>多角度判断（创新思维 vs 逻辑思维边界）",
    "Q-2024朝阳二模-7": "推理>三段论>小项不当扩大",
    "Q-2024朝阳期中-7": "推理>三段论>第三格AAI式",
    "Q-2024朝阳期中-8": "形式逻辑>判断>必要条件假言判断（三种等价表达式）",
    "Q-2024朝阳期中-9": "推理>归纳>共变法（因果探求三法）",
    "Q-2024朝阳期中-10": "形式逻辑>概念>外延关系>属种关系",
    "Q-2026朝阳期中-11": "推理>三段论>第二格补大前提",
    "Q-2026朝阳期中-12": "形式逻辑>判断>相容选言判断",
    "Q-2026朝阳期中-13": "创新思维>联想思维（与认识发展历程综合）",
    "Q-2026朝阳期中-14": "推理>归纳>不完全归纳推理或然性",
    "Q-2026朝阳期中-15": "形式逻辑>判断>联言判断（真值条件）",
}

choice_recheck_map = {
    # Mirrors QUESTION_DECISIONS.csv needs_codex_recheck
    "Q-2024朝阳一模-6": "no",
    "Q-2024朝阳一模-7": "no",
    "Q-2024朝阳二模-7": "no",
    "Q-2024朝阳期中-7": "yes",
    "Q-2024朝阳期中-8": "yes",
    "Q-2024朝阳期中-9": "no",
    "Q-2024朝阳期中-10": "yes",
    "Q-2026朝阳期中-11": "yes",
    "Q-2026朝阳期中-12": "yes",
    "Q-2026朝阳期中-13": "yes",
    "Q-2026朝阳期中-14": "yes",
    "Q-2026朝阳期中-15": "yes",
}

with open(LEDGER_DIR / "CHOICE_TRAP_LEDGER.csv", encoding="utf-8") as f:
    rdr = csv.DictReader(f)
    for r in rdr:
        qid = r["question_id"]
        # Synthesize answer_sentence: 正确项理由 (compressed) — choice entries
        # show the candidate-facing reasoning that selects the right option
        # and rejects the traps.
        ans_sentence = r["正确项理由"] + " ｜ 错项排除：" + r["诱人错项"][:200]
        entries.append({
            "question_id": qid,
            "type": "choice_trap",
            "framework_node": choice_framework_map[qid],
            "material_signal": r["题干信号"],
            "trigger_logic": r["陷阱类型"],
            "answer_sentence": ans_sentence,
            "evidence_level": "B-choice-signal",
            "needs_codex_recheck": choice_recheck_map[qid],
            "source_batch": SOURCE_BATCH,
        })


def main():
    # Validate every entry is parseable JSON and has all 9 fields
    forbidden_in_student = ["yes", "pass", "filled", "correct_option_chain",
                            "A-formal", "B-choice-signal", "phase",
                            "source_pool", "OCR", "debug",
                            "/Users/", "C:\\"]

    with open(OUT, "w", encoding="utf-8") as f:
        for e in entries:
            for k in REQUIRED:
                assert k in e, f"missing field {k} in {e.get('question_id', '?')}"
                assert e[k] != "", f"empty field {k} in {e['question_id']}"
            assert e["needs_codex_recheck"] in ("yes", "no"), \
                f"bad needs_codex_recheck for {e['question_id']}: {e['needs_codex_recheck']}"
            line = json.dumps(e, ensure_ascii=False)
            # Ensure each line round-trips through json.loads
            json.loads(line)
            f.write(line + "\n")

    print(f"wrote {OUT} entries={len(entries)}")
    print(f"  main_thinking: {sum(1 for e in entries if e['type'] == 'main_thinking')}")
    print(f"  choice_trap:   {sum(1 for e in entries if e['type'] == 'choice_trap')}")


if __name__ == "__main__":
    main()
