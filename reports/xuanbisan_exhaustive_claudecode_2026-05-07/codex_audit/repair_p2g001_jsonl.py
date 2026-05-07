import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
PATCH_PATH = RUN_DIR / "claudecode_lane" / "p2_recheck" / "P2G001_RECHECK_PATCHES.jsonl"
BACKUP_PATH = PATCH_PATH.with_suffix(".jsonl.bak_p2g001_repair")


def main() -> None:
    raw_lines = PATCH_PATH.read_text(encoding="utf-8").splitlines()
    valid_rows = []
    for line in raw_lines[:3]:
        valid_rows.append(json.loads(line))

    repaired_q6 = {
        "question_id": "Q-2026顺义一模-6",
        "parent_question_id": "Q-2026顺义一模-6",
        "framework_node": "创新思维-迁移和想象（A正解）",
        "decision": "confirmed_with_patch",
        "patched_material_signal": "人机认知边界四象限基于拉姆斯菲尔德“已知-未知”认知框架与乔哈里视窗，迁移到AI与人类认知差异场景，用于界定人机知识和信息掌握边界。",
        "patched_trigger_logic": "看到把既有认知框架迁移到AI人机协作新问题，触发迁移方法识别；迁移是把已有认识、方法或模型用于解决新情境中的问题。",
        "patched_answer_sentence": "Q6答案A。该模型的建构把“已知-未知”框架和乔哈里视窗迁移到AI与人的认知边界问题，属于用迁移方法认识和解决新问题；B把边界说成确定不变，C把AI拟人化为具有能动性，D把分析框架夸大为具体操作路径，均不成立。",
        "source_evidence": "001 paper.txt::Q6 stem/options; 001 support 2026顺义一模细则.pptx.txt::SLIDE 1 answer table gives Q6=A.",
        "notes": "Codex repaired malformed JSONL line caused by unescaped quotes; decision and evidence follow ClaudeCode decisions CSV and source files.",
    }
    valid_rows.append(repaired_q6)

    if not BACKUP_PATH.exists():
        BACKUP_PATH.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

    PATCH_PATH.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in valid_rows) + "\n",
        encoding="utf-8",
    )
    print(f"repaired_rows={len(valid_rows)}")
    print(f"backup={BACKUP_PATH}")


if __name__ == "__main__":
    main()
