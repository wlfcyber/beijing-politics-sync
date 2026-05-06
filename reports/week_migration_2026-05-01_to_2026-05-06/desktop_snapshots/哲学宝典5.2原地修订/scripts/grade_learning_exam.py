import json
import re
import sys
from pathlib import Path


KEY_PATH = Path("/Users/wanglifei/Desktop/北京高考政治/哲学宝典5.2原地修订/audit/learning_exam/confucius_learning_exam_round1_key.json")


def norm(text: str) -> str:
    return re.sub(r"\s+", "", str(text or "")).replace("（", "(").replace("）", ")")


def block_map(answer_text: str):
    blocks = {}
    parts = re.split(r"(?=^##\s*T\d{2}\b|^###\s*T\d{2}\b|^T\d{2}\b)", answer_text, flags=re.M)
    for part in parts:
        m = re.search(r"\b(T\d{2})\b", part)
        if m:
            blocks[m.group(1)] = part.strip()
    return blocks


def has_chain(block: str) -> bool:
    text = norm(block)
    trigger_words = ["因为", "触发", "说明", "体现", "材料", "关系", "所以", "由此"]
    bad_words = ["文档里", "教材里", "宝典里", "原文写", "我没学会"]
    return sum(w in text for w in trigger_words) >= 3 and not any(w in text for w in bad_words)


def has_landing(block: str) -> bool:
    text = norm(block)
    if "我没学会" in text:
        return False
    return ("答案落点" in text and any(w in text for w in ["所以", "因此", "要", "应", "说明", "体现"])) or len(text) > 120


def main(answer_path: str):
    key = json.loads(KEY_PATH.read_text())
    answer_text = Path(answer_path).read_text()
    blocks = block_map(answer_text)
    rows = []
    for item in key:
        tid = item["test_id"]
        block = blocks.get(tid, "")
        expected = item["node"]
        node_hit = norm(expected) in norm(block)
        chain_hit = bool(block) and has_chain(block)
        landing_hit = bool(block) and has_landing(block)
        status = "PASS" if node_hit and chain_hit and landing_hit else "FAIL"
        rows.append({
            "test_id": tid,
            "expected_node": expected,
            "node_hit": node_hit,
            "chain_hit": chain_hit,
            "landing_hit": landing_hit,
            "status": status,
        })
    out = Path(answer_path).with_name(Path(answer_path).stem + "_graded.json")
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    total = len(rows)
    passed = sum(r["status"] == "PASS" for r in rows)
    print(json.dumps({
        "total": total,
        "pass": passed,
        "fail": total - passed,
        "output": str(out),
        "failed_items": [r for r in rows if r["status"] != "PASS"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: grade_learning_exam.py <answers.md>")
    main(sys.argv[1])
