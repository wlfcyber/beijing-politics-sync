from __future__ import annotations

import csv
import random
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
FINAL = BASE / "v13_1_round05_patched_final"
OUT = Path(__file__).resolve().parent


def main() -> None:
    (OUT / "web_payloads").mkdir(parents=True, exist_ok=True)
    (OUT / "model_outputs").mkdir(parents=True, exist_ok=True)
    (OUT / "codex_adjudication").mkdir(parents=True, exist_ok=True)

    framework = next(FINAL.glob("01_*.md")).read_text(encoding="utf-8")
    readme = (FINAL / "00_READ_ME_FIRST.md").read_text(encoding="utf-8")
    trace = FINAL / "traceability" / "TRACEABILITY_MATRIX_v13_1_round05_patched.csv"

    with trace.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    rng = random.Random(20260523)
    selected = rng.sample(rows, 5)
    ids = [r["question_id"] for r in selected]

    header = f"""# Claude Zero-Baseline Random Live Test：选必二《法律与生活》

任务：请你模拟一个“什么都不知道但很聪明的高三学生”。你刚拿到下面这套框架，需要现场学习，然后对随机抽取的题进行作答。

硬规则：
1. 你不能把自己当成老师或阅卷人；你是正在考试的学生。
2. 你只能使用下面给你的框架和题目材料，不要调用外部资料，不要补充题目没有给出的事实。
3. 我只给你框架和题面，不给你标准答案、评分锚点、材料触发链、答案骨架、学生预警。你要现场判断。
4. 每道题都按固定格式回答：
   - A轴主入口判断：你认为应先落到哪个法律入口，为什么？
   - B轴设问动作判断：设问要求你做什么动作？
   - 材料信号：列出你抓到的2-4个材料触发点。
   - 现场答案：写出你会交卷的答案，不要写成提纲空话。
   - 自我估分：按满分10分估计自己能拿几分，并说最可能丢分在哪里。
5. 最后总评：这套框架对一个零基础但聪明的学生是否够用？哪些题能救，哪些题仍然容易翻车？

随机种子：20260523
随机题号：{", ".join(ids)}

---

## A. 你先学习的框架

"""

    question_parts = [
        """
---

## B. 随机盲测题

以下题目只提供题面压缩信息和设问动作，不提供答案骨架或评分锚点。
"""
    ]
    for i, r in enumerate(selected, 1):
        question_parts.append(
            f"""### 题{i}: {r["question_id"]}

- 区年卷题：{r["year"]}年 {r["district"]} {r["exam_stage"]} 第{r["question_no"]}题
- 设问：{r["prompt_action"]}
- 材料/题面压缩：{r["material_core"]}
"""
        )

    payload = header + readme + "\n\n" + framework + "\n".join(question_parts)
    payload_path = OUT / "web_payloads" / "CLAUDE_ZERO_BASELINE_RANDOM_TEST_PAYLOAD.md"
    payload_path.write_text(payload, encoding="utf-8", newline="\n")

    key_lines = [
        "# Local Answer Key for Claude Zero-Baseline Random Test\n",
        "This file is NOT sent to Claude. It is used by Codex to compare Claude live answers against locked v13.1 cards.\n",
    ]
    for i, r in enumerate(selected, 1):
        key_lines.append(
            f"""
## 题{i}: {r["question_id"]}

- expected_a_axis: {r["a_axis_primary"]}
- expected_b_axis: {r["b_axis"]}
- secondary_axis: {r["a_axis_secondary_status"]}
- adjudication_note: {r["a_axis_adjudication_note"]}
- prompt_action: {r["prompt_action"]}
- legal_relationship_trigger: {r["legal_relationship_trigger"]}
- material_core: {r["material_core"]}
- material_trigger: {r["material_trigger"]}
- rubric_scoring_anchor: {r["rubric_scoring_anchor"]}
- proposition_path: {r["proposition_path"]}
- answer_skeleton: {r["answer_skeleton"]}
- student_warning: {r["student_warning"]}
- guardrail: {r["guardrail"]}
"""
        )
    key_path = OUT / "codex_adjudication" / "LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md"
    key_path.write_text("\n".join(key_lines), encoding="utf-8", newline="\n")

    progress = f"""# Claude Zero-Baseline Random Test Progress

Status: `payload_prepared_pending_real_claude_web_capture`

- Created: 2026-05-23
- Random seed: 20260523
- Selected questions: {", ".join(ids)}
- Payload: `web_payloads/CLAUDE_ZERO_BASELINE_RANDOM_TEST_PAYLOAD.md`
- Local answer key not sent to Claude: `codex_adjudication/LOCAL_ANSWER_KEY_NOT_SENT_TO_CLAUDE.md`
"""
    (OUT / "ROUND_PROGRESS.md").write_text(progress, encoding="utf-8", newline="\n")

    print(payload_path)
    print(key_path)
    print("payload_chars", len(payload))
    print("selected", ", ".join(ids))


if __name__ == "__main__":
    main()
