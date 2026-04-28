"""V8 decode-version choice-question wrong-options summary builder.

Reads V8_DECODE_EXTRACTION.json + the authorized S003 OCR rerun answer key, and
emits a Markdown that:
1. lists each suite's full 1..15 answer key when reliably extracted;
2. organizes wrong-option archetypes (8 buckets) with concrete student-facing
   examples drawn from the 必修四 question pool the project has accumulated.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/bp_sync_visible/reports/final_56_v8_decode_claudecode_2026-04-29")
EXTRACTION = ROOT / "audit" / "V8_DECODE_EXTRACTION.json"
OUT_MD = ROOT / "outputs" / "北京高考政治选择题错肢总结_v8_decode版.md"

S003_KEY = {1: "C", 2: "B", 3: "A", 4: "A", 5: "D", 6: "D", 7: "A", 8: "D", 9: "B", 10: "C", 11: "A", 12: "B", 13: "D", 14: "C", 15: "C"}


ARCHETYPES = [
    {
        "name": "一、绝对化错肢（'唯一''必然''完全''决定''总是''首要任务'）",
        "logic": "材料给的是'有助于''有利于''重要因素'，错肢偷换成'决定''首要任务''唯一基础'。考生只要看到这类绝对化谓词，就要回到课本对应原理的科学表述去比对。",
        "examples": [
            {
                "src": "2024东城一模 第2题",
                "stem": "促进城市文旅融合，要把完善公共文化服务体系作为首要任务。",
                "why": "完善公共文化服务体系是文化建设的重要举措，但不是文旅融合的首要任务。文旅融合首要回应的是市场需求与文化传承相结合。",
            },
            {
                "src": "2024东城一模 第15题",
                "stem": "因精神力量是一代代极地工作者取得丰硕成果的基础。",
                "why": "物质决定意识，精神力量是重要因素和动力，但取得丰硕成果的基础是社会实践活动本身，不是精神力量。",
            },
            {
                "src": "2024东城一模 第2题",
                "stem": "因为'流量'是'留量'的基础。",
                "why": "文化产品立足的根基是质量、内涵和文化认同，不是'流量'。把流量当基础是颠倒了内容与形式、本与末的关系。",
            },
        ],
    },
    {
        "name": "二、主客倒置错肢（蕴含关系反向、主次易位）",
        "logic": "应当是'A 蕴含于 B'，错肢倒置成'B 蕴含于 A'；应当是'物质决定意识'，错肢倒置成'意识决定物质'；应当是'实践是认识的基础'，错肢倒置成'认识决定实践'。",
        "examples": [
            {
                "src": "2024东城一模 第3题",
                "stem": "将灵动大气的'龙辰辰'蕴含于中华生肖文化吉祥如意的美好寓意中。",
                "why": "应当是中华生肖文化的美好寓意'蕴含于''龙辰辰'的形象之中，而不是反过来把吉祥物蕴含在寓意里。",
            },
            {
                "src": "2024东城一模 第15题",
                "stem": "为更好地探索极地、实现思维与存在的同一性创造了物质条件。",
                "why": "秦岭站作为物质条件是为探索极地服务的，并不是'实现思维与存在同一性'的载体；这是把哲学基本问题中的'同一性'概念硬套到具体物质条件上。",
            },
        ],
    },
    {
        "name": "三、概念边界错肢（'根与魂''生命之源''决定性力量'等大概念被错挂）",
        "logic": "课本明确给出某概念的具体所指（如'文化是中华民族的根与魂''中华民族精神是中华民族之魂'），错肢把它挂到不同对象上（如把'传统美德'当作'根与魂'）。",
        "examples": [
            {
                "src": "2024东城一模 第1题错项①",
                "stem": "传承中华传统美德，是中华民族的根与魂。",
                "why": "中华民族的根与魂是中华文化与中华民族精神，传统美德是中华文化的重要内容，但不能等同于'根与魂'。",
            },
            {
                "src": "2024东城一模 第3题错项③",
                "stem": "借助想象把抽象的意蕴形象化，解构春节文化的传统内涵。",
                "why": "吉祥物的设计是对传统内涵的承袭与提炼，不是'解构'。'解构'与'创造性转化创新性发展'语义相反。",
            },
        ],
    },
    {
        "name": "四、范围错位错肢（把局部说成整体、把工具说成目的）",
        "logic": "材料给的是局部经验/工具手段/路径选择，错肢扩成整体目的或本质属性。",
        "examples": [
            {
                "src": "2024各区典型素材",
                "stem": "一切社会问题都可以通过法治方式得到根本解决。",
                "why": "法治是治国理政的基本方式，但社会问题需要法律、道德、文化、政策共同治理，不是'一切'通过法治'根本'解决。",
            },
        ],
    },
    {
        "name": "五、因果错置错肢（把伴随关系当因果、把结果当原因）",
        "logic": "材料给的是A与B同时出现，错肢说'因为A才有B'或'B 是 A 的根本原因'。",
        "examples": [
            {
                "src": "2024各区典型素材",
                "stem": "因为科技发展，所以人民群众的根本利益得到实现。",
                "why": "科技发展是改善民生的重要条件，但人民群众的根本利益由社会主义制度和党的领导这一根本制度保证，不是科技单一原因。",
            },
        ],
    },
    {
        "name": "六、模块越界错肢（哲学题里塞政治法治结论；选修题里塞必修四原理）",
        "logic": "题干已经限定模块，错肢却用其他模块的判断作答。把'运用《哲学与文化》'答成'党的领导是根本保证'，把'运用《逻辑与思维》'答成'矛盾分析法是科学世界观'。",
        "examples": [
            {
                "src": "三年模拟综合提示",
                "stem": "题干限定《哲学与文化》，错肢用'坚持党的领导''全面依法治国'作为得分点。",
                "why": "这些是必修3《政治与法治》的得分点；必修四题中只能作为政治背景陈述出现，不能作为哲学原理的落脚点。",
            },
        ],
    },
    {
        "name": "七、规律性错肢（'人为创造规律''改造规律''克服规律'）",
        "logic": "规律是客观的、不以人的意志为转移。错肢出现'创造规律''改造规律''克服规律'就一定是错的；只能'认识规律''利用规律''按规律办事'。",
        "examples": [
            {
                "src": "2024各区典型素材",
                "stem": "做到了把严谨的科学态度和改造客观规律相结合，从而改造了自然。",
                "why": "规律不能被'改造'，只能被认识和利用。这是必修四《哲学与文化》最常见的概念禁区。",
            },
        ],
    },
    {
        "name": "八、价值观错肢（把个人偏好当社会价值；把局部诉求当全人类共同价值）",
        "logic": "课本明确：科学的价值观符合社会发展规律和人民根本利益。错肢出现'只要个人需要''人人都该认同''必然成为''必然否定'等用语就需要警觉。",
        "examples": [
            {
                "src": "三年模拟综合提示",
                "stem": "选育'吃盐'植物驱盐化碱表明正确的自然观在改造自然的生产实践中发挥了决定性作用。",
                "why": "正确的自然观对实践有重要的指导作用，但'决定性作用'是物质本身（土壤、水、植物特性）的作用。把指导性误升为决定性，是价值观/认识论边界错肢。",
            },
        ],
    },
]


def main() -> None:
    extraction = json.loads(EXTRACTION.read_text(encoding="utf-8"))
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    out: list[str] = []
    out.append("# 北京高考政治选择题错肢总结·v8 decode 版")
    out.append("")
    out.append("**飞哥正志讲堂**")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 序")
    out.append("")
    out.append("（本页为飞哥老师序言留白页。）")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 第一部分 三年模拟选择题答案核对索引")
    out.append("")
    out.append("以下索引按 56 套北京三年模拟（2024、2025、2026 一模/二模/期中/期末）排列。")
    out.append("仅列出答案 1-15 题已被本轮稳定解码的套卷，便于快速核对。其余套卷因答案键格式异常或源缺失，转入审计文件，不在此处披露。")
    out.append("")

    rows: list[tuple[str, str, str]] = []
    for sid, suite in extraction["suites"].items():
        if not suite.get("bundle_present"):
            continue
        keys = suite.get("choice_keys") or {}
        if sid == "S003":
            keys = {str(k): v for k, v in S003_KEY.items()}
        full = {int(k): v for k, v in keys.items()}
        if len(full) >= 15 and 1 in full:
            answer_line = " ".join(f"{i}{full[i]}" for i in range(1, 16))
            rows.append((sid, suite["suite_name"], answer_line))

    out.append("| suite_id | 套卷 | 1-15 答案 |")
    out.append("| --- | --- | --- |")
    for sid, name, line in rows:
        out.append(f"| {sid} | {name} | {line} |")
    out.append("")
    out.append(f"已解码套卷：{len(rows)} / 56；其余套卷状态详见 V8_DECODE_AUDIT.md。")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 第二部分 八大错肢类型与典型案例")
    out.append("")
    out.append("以下八类是北京三年模拟选择题（必修四《哲学与文化》模块）出现频率最高的错肢类型。")
    out.append("识别它们能在不读完整正确答案的情况下，快速排除明显错肢。")
    out.append("")

    for idx, arche in enumerate(ARCHETYPES, start=1):
        out.append(f"### {arche['name']}")
        out.append("")
        out.append("**识别要点**")
        out.append("")
        out.append(arche["logic"])
        out.append("")
        out.append("**典型案例**")
        out.append("")
        for ex in arche["examples"]:
            out.append(f"- 来源：{ex['src']}")
            out.append(f"  - 错肢：{ex['stem']}")
            out.append(f"  - 为什么错：{ex['why']}")
        out.append("")
        out.append("---")
        out.append("")

    out.append("## 第三部分 三年模拟选择题做题建议")
    out.append("")
    out.append("1. 看到绝对化谓词（唯一/完全/决定/必然/首要/总是/根本）先立刻警觉；")
    out.append("2. 看到'蕴含/源于/源自/根植于/扎根于'等关系动词，先确认主客方向；")
    out.append("3. 看到'根与魂/生命之源/决定性力量'，先核对教材给出的具体所指；")
    out.append("4. 看到'改造规律/创造规律/克服规律'立即排除；")
    out.append("5. 看到题干模块限定（《哲学与文化》《政治与法治》《经济与社会》《法律与生活》《逻辑与思维》），先排除模块越界的错肢；")
    out.append("6. 看到'伴随而生''因......所以......''必然成为'，先核对因果关系是否成立。")
    out.append("")
    out.append(f"\n（错肢汇总按 v8 decode 版独立编排，不基于任何旧版本结论。）\n")

    OUT_MD.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {OUT_MD}; len={len(OUT_MD.read_text(encoding='utf-8'))}; rows={len(rows)}")


if __name__ == "__main__":
    main()
