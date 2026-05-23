from __future__ import annotations

from html import escape
from pathlib import Path

import generate_baodian as data


OUT = Path(__file__).resolve().parent
HTML_PATH = OUT / "选必二法律与生活_法律宝典_v12_2.html"
GENERATED_AT = "2026-05-23 02:30 +08:00"


def h(text: str) -> str:
    return escape(text or "")


def label(label_text: str, value: str) -> str:
    return f'<p class="kv"><strong>{h(label_text)}</strong>{h(value)}</p>'


def render() -> str:
    grouped = {code: [] for code in data.ENTRY_ORDER}
    for row in data.CORE:
        grouped[data.entry_code(row)].append(row)

    counts = {code: len(grouped[code]) for code in data.ENTRY_ORDER}
    body: list[str] = []

    body.append(
        f"""
<section class="cover">
  <h1>选必二《法律与生活》法律宝典</h1>
  <p class="subtitle">v12.2｜从42道题源生长出的主观题框架与逐题解析</p>
  <div class="meta">
    <p><strong>生成时间</strong>{GENERATED_AT}</p>
    <p><strong>状态</strong>HTML/PDF baodian candidate; Markdown gate already passed</p>
    <p><strong>证据底座</strong>42 locked core 主观题；参考/开放/下一版回填题不晋升正文</p>
    <p><strong>模型链条</strong>真实 GPT Round 03 + Claude Round 03 审查；Codex 源检查裁决</p>
  </div>
</section>
"""
    )

    body.append("<section><h2>一、六入口框架</h2>")
    body.append("<p>选必二主观题不是按教材页码出题，而是按设问动作出题。先看题目让你做什么，再判断命题人要学生完成哪一种法律工作：补链、判责、判诉求、评观点、写意义、走路径。</p>")
    body.append("<table class='counts'><thead><tr><th>入口</th><th>题数</th><th>适用场景</th></tr></thead><tbody>")
    for code in data.ENTRY_ORDER:
        spec = data.ENTRY_DEFS[code]
        body.append(f"<tr><td>{h(code)}</td><td>{counts[code]}</td><td>{h(spec['cue'])}</td></tr>")
    body.append("</tbody></table>")
    for code in data.ENTRY_ORDER:
        spec = data.ENTRY_DEFS[code]
        ids = "、".join(r["question_id"] for r in grouped[code])
        body.append(f"<article class='entry'><h3>{h(spec['title'])}（{counts[code]}题）</h3>")
        body.append(label("识别口令：", spec["cue"]))
        body.append(label("命题路径：", spec["path"]))
        body.append(label("作答骨架：", spec["skeleton"]))
        body.append(label("学生预警：", spec["warning"]))
        body.append(label("本版题源：", ids))
        body.append("</article>")
    body.append("</section>")

    body.append("<section><h2>二、42题按框架解析</h2>")
    n = 1
    for code in data.ENTRY_ORDER:
        spec = data.ENTRY_DEFS[code]
        body.append(f"<h3 class='group'>{h(spec['title'])}（{counts[code]}题）</h3>")
        for row in grouped[code]:
            qid = row["question_id"]
            trace = data.TRACE.get(qid, {})
            body.append(f"<article class='card'><h4>{n}. {h(qid)}</h4>")
            body.append(label("区年卷题：", f"{data.cell(row, 'year')}年 {data.cell(row, 'district')} {data.cell(row, 'exam_stage')} 第{data.cell(row, 'question_no')}题"))
            body.append(label("设问动作：", data.cell(row, "真实设问")))
            body.append(label("材料核心：", data.cell(row, "真实材料核心")))
            body.append(label("框架入口：", f"{spec['title']}；原题源主入口：{data.cell(row, '主入口')}"))
            body.append(label("副入口：", data.secondary_entry(row)))
            body.append(label("命题路径：", spec["path"]))
            body.append(label("细则/评分锚点：", data.scoring_anchor(row)))
            for idx, trig in enumerate(data.trigger_lines(row), 1):
                body.append(label(f"材料触发{idx}：", trig))
            body.append(label("答案骨架：", data.cell(row, "答案骨架")))
            body.append(label("学生预警：", data.cell(row, "禁止命中") or spec["warning"]))
            body.append(label("讲解口径：", data.cell(row, "飞哥想说")))
            body.append(label("证据与来源：", f"{data.cell(row, 'evidence_status')}；{data.cell(row, 'chain_state')}；source_check_state={data.cell(trace, 'source_check_state', 'not_recorded')}"))
            body.append("</article>")
            n += 1
    body.append("</section>")

    body.append("<section><h2>三、开放容器与治理附录</h2>")
    body.append("<h3>不晋升规则</h3>")
    body.append("<p>参考题、开放容器、别名风险行、下一版回填候选不能直接提升为第七入口。只有当新证据证明 locked core 正文题无法被六入口覆盖，才允许重开框架结构。</p>")
    body.append("<h3>Round 03 明确不晋升行</h3>")
    non_promoted = [
        r for r in data.PENDING_CHECKS
        if not data.cell(r, "decision").startswith("KEEP_CORE")
    ]
    for r in non_promoted:
        body.append(label(f"{data.cell(r, 'question_id')}：", f"{data.cell(r, 'source_status')}；{data.cell(r, 'entrance_after_check')}；{data.cell(r, 'decision')}；{data.cell(r, 'guardrail')}"))

    body.append("<h3>GPT / Claude 真实结论</h3>")
    body.append(label("GPT Round 03：", "ChatGPT web clean conversation，visible mode 为“进阶专业”，保留模型标签 caution；verdict 为 accept_source_checked_candidate_no_structural_change。"))
    body.append(label("Claude Round 03：", "Claude web 可见模型 Opus 4.7 Adaptive；verdict 为 accept_source_checked_candidate_no_structural_change。"))
    body.append(label("Codex 裁决：", "本地源证据优先。双模型一致意见只确认六入口结构可作为 v12.2 source-checked baseline；下一版回填仍不自动进入正文。"))
    body.append("</section>")

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>选必二法律与生活法律宝典 v12.2</title>
<style>
@page {{ size: A4; margin: 18mm 17mm 19mm 17mm; }}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: "Microsoft YaHei", "Noto Sans CJK SC", "PingFang SC", Arial, sans-serif;
  color: #111827;
  font-size: 11pt;
  line-height: 1.48;
}}
.cover {{
  min-height: 245mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  page-break-after: always;
}}
h1 {{
  font-size: 30pt;
  line-height: 1.18;
  color: #1f4d78;
  margin: 0 0 10pt;
  text-align: center;
}}
.subtitle {{
  font-size: 14pt;
  color: #4b5563;
  text-align: center;
  margin: 0 0 24pt;
}}
.meta {{
  border: 1px solid #cbd5e1;
  border-left: 5px solid #2e74b5;
  padding: 12pt 15pt;
  background: #f8fafc;
}}
.meta p, p {{ margin: 0 0 7pt; }}
.meta strong, .kv strong {{
  color: #1f4d78;
  display: inline-block;
  min-width: 86pt;
}}
h2 {{
  font-size: 18pt;
  color: #2e74b5;
  border-bottom: 1px solid #cbd5e1;
  padding-bottom: 4pt;
  margin: 0 0 12pt;
  page-break-before: always;
}}
h3 {{
  font-size: 14pt;
  color: #2e74b5;
  margin: 14pt 0 7pt;
}}
h3.group {{
  background: #e8eef5;
  border-left: 4px solid #2e74b5;
  padding: 5pt 8pt;
}}
h4 {{
  font-size: 12pt;
  color: #1f4d78;
  margin: 0 0 6pt;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 8pt 0 12pt;
  page-break-inside: avoid;
}}
th, td {{
  border: 1px solid #cbd5e1;
  padding: 5pt 6pt;
  vertical-align: top;
}}
th {{ background: #e8eef5; color: #1f4d78; }}
.entry {{
  border-left: 3px solid #d6e4f2;
  padding-left: 10pt;
  margin-bottom: 10pt;
}}
.card {{
  border: 1px solid #d7dde6;
  border-left: 4px solid #2e74b5;
  padding: 8pt 10pt 5pt;
  margin: 0 0 10pt;
  break-inside: avoid;
  page-break-inside: avoid;
}}
.kv {{ margin: 0 0 4pt; }}
code {{ font-family: Consolas, monospace; }}
</style>
</head>
<body>
{''.join(body)}
</body>
</html>
"""


if __name__ == "__main__":
    HTML_PATH.write_text(render(), encoding="utf-8")
    print(HTML_PATH)
