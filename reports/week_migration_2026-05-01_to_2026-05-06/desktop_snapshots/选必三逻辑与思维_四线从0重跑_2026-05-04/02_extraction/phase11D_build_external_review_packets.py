#!/usr/bin/env python3
"""Build external-model packets for Phase11D combined 29 review."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMBINED = ROOT / "09_student_draft/phase11D_combined_source_verified_29_REVIEW_ONLY.md"
GPT_OUT = ROOT / "08_review/gpt_phase_advice/phase_11D_combined29_prompt_for_gpt55.md"
OPUS_DIR = ROOT / "08_review/opus_writer"
OPUS_OUT = OPUS_DIR / "phase_11D_combined29_prompt_for_claude_opus47_adaptive.md"


def main() -> int:
    body = COMBINED.read_text(encoding="utf-8")
    OPUS_DIR.mkdir(parents=True, exist_ok=True)

    gpt_prompt = f"""# GPT-5.5 Pro 内容审稿请求：选必三《逻辑与思维》Phase11D 合并29条

你是北京高考政治教研项目的首席内容审稿人。请严格审下面这份学生版候选稿，但不要替我扩写成终稿。

## 背景

- 本项目要求完全模仿已经成功的“哲学宝典”工作流：每题必须有真实材料触发点、真实设问、为什么能想到、答案落点。
- 学生稿必须可直接教弱学生，不要后台话术。
- GPT 不是来源权威。你提出的每个实质修改，后续都要由 Codex 回本地原题源核验。
- 你需要重点挑：概念错、题型错、四要件不充分、答案落点不像卷面话、选择题四选项理由不清、同一题多方法对应不充分、推理规则错误。
- 不要因为稿子格式好就放行；内容烂就直接判 must_fix。

## 输出格式

请只按这个结构输出：

verdict: PASS_FOR_NEXT_OPUS / MUST_FIX_BEFORE_OPUS / HARD_FAIL_REBUILD

must_fix:
- [题目标题] 问题：... | 修法：... | 为什么这会影响学生得分：...

should_fix:
- [题目标题] 问题：... | 修法：...

approved_for_next:
- 可以进入 Opus 成品化的条目标题

merge_policy:
- 哪些条目可以进学生正文
- 哪些只能做题型索引或边界提醒
- 哪些必须暂缓

## 待审稿

{body}
"""

    opus_prompt = f"""# Claude Opus 4.7 Adaptive Thinking 成品化请求：选必三《逻辑与思维》Phase11D 合并29条

请作为教学文本编辑，不作为来源裁判。你的任务是把下面 29 条已由 Codex 回源核过的候选稿改得更像“哲学宝典”的学生版：清楚、好背、好迁移、卷面答案能直接写。

硬规则：

1. 不新增题目、来源事实、答案项、选项判断或评分说法。
2. 不删任何题的四个结构：材料触发点、设问、为什么能想到、答案落点。
3. 不把候选稿写成审计报告；不得出现路径、line、评审状态、A-formal、PASS、参考答案、评标等后台话术。
4. 选择题必须保留四个选项单位，答案落点要说明正确项和主要错项陷阱。
5. 推理题要先定形式，再写规则，再落本题材料。
6. 如果你认为某条证据不足或概念不稳，标成“建议暂缓”，不要强行润色成确定结论。

请输出：

一、整体修改原则
二、逐条改写后的学生版正文
三、需要 Codex 回源复核的问题清单
四、你明确没有新增来源事实的自检说明

待成品化文本如下：

{body}
"""

    GPT_OUT.write_text(gpt_prompt, encoding="utf-8")
    OPUS_OUT.write_text(opus_prompt, encoding="utf-8")
    print(f"wrote={GPT_OUT}")
    print(f"wrote={OPUS_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
