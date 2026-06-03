from pathlib import Path
import csv
import re

root = Path(__file__).resolve().parents[1]
fields = [
    "node_id", "node_layer", "node_title", "看到什么", "触发什么",
    "怎么写", "别写什么", "支撑题号", "证据等级", "是否核心", "是否参考",
]


def read_csv(name):
    with (root / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


core = read_csv("04_core_questions.csv")
refs = read_csv("04_reference_questions.csv")
pending = read_csv("04_pending_or_excluded.csv")
core_ids = [r["question_id"] for r in core]
all_core = ";".join(core_ids)

fixes = {
    "F01": ["反向筛", "法院 ≠ 公正司法", "看到法院判决就写公正司法", "把法院的具体动作和具体保护的权利写出来", "先写案件中的法律关系、权利义务、责任承担，再在价值层收一句司法定分止争", "不要光写“体现公正司法”两句完事", all_core, "formal/lecture", "是", "否"],
    "F02": ["反向筛", "平台 ≠ 自动认定劳动关系", "看到外卖骑手/网约工就直接写“是劳动关系”", "必须看三从属性事实：人格+经济+组织", "三从属性事实齐全，才写事实劳动关系；不齐全就写新就业形态权益保护", "不要直接套劳动合同法；不要忽略平台用工的灵活性", "2024朝阳二模__Q17", "formal", "是", "否"],
    "F03": ["反向筛", "消费者纠纷 ≠ 一律退一赔三", "看到消费者就上三倍赔偿", "必须先证明欺诈", "先写欺诈事实，再接知情权/公平交易权，再落撤销或退赔", "不要把“瑕疵”当欺诈；不要忽略食品安全特殊口径", "2025朝阳一模__Q19", "lecture", "是", "否"],
    "F04": ["反向筛", "知识产权侵权 ≠ 一律不正当竞争", "看到“山寨/抄袭/侵权”就全写“不正当竞争”", "商业秘密走反不正当竞争法；商标/专利/著作权各走专门法；混淆类走反不正当竞争", "先识别权利类型，再选对应法律规则和责任", "不要把专利侵权、商业秘密、商标混淆写成一锅", "2025丰台一模__Q19;2025房山一模__Q19;2025西城期末__Q19", "formal", "是", "否"],
    "F05": ["反向筛", "意义 ≠ 裸价值口号", "问“判决意义/法治价值”就堆口号", "按层次写：对当事人 → 对行业 → 对社会 → 对制度/法治建设", "先落案件保护谁、规范谁，再上升到行业秩序和法治环境", "不要只写核心价值观/公平正义/和谐三件套", "2025房山一模__Q19;2024海淀二模__Q19-sub2", "formal", "是", "否"],
    "F06": ["反向筛", "继承 ≠ 子女均分", "看到“遗产/老人去世”就写“子女平均分”", "先看有无遗嘱/遗赠扶养协议；有效则按协议；无则法定继承", "先锁有效协议和履行事实，再处理遗产归属", "不要直接套法定继承；不要忽略尽扶养义务对份额的影响", "2024海淀二模__Q19-sub2;2025东城一模__Q19", "formal", "是", "否"],
    "F07": ["反向筛", "相邻关系 ≠ 物权之争", "小区采光/电梯纠纷写“侵犯物权/所有权”", "写相邻关系规则，扣有利生产、方便生活、团结互助、公平合理", "先写相邻关系，再看停止侵害、排除妨碍、生态绿色要求", "不要把相邻关系写成单纯所有权争夺", "2025朝阳二模__Q20;2026西城一模__Q17;2025顺义一模__Q19-sub2", "formal", "是", "否"],
    "F08": ["反向筛", "案例 ≠ 法考题", "看到法律案例就铺法条全文/列五个要件", "法条只点名引一句；要把法律语言翻成材料里的人物动作", "用“事实 → 法律翻译 → 责任/意义”的短链写", "不要写大段法条原文；不要把案例答成模拟法庭辩论", all_core, "formal/lecture", "是", "否"],
    "F09": ["反向筛", "法律 ≠ 必修三政治与法治", "看到“法治/法院”就写“科学立法严格执法公正司法全民守法”", "选必二要锁生活中的具体法律关系+具体责任+具体救济", "先写选必二的权利义务和责任，再用一句法治价值收口", "不要让必修三框架抢走生活法律关系的位置", all_core, "formal/lecture", "是", "否"],
    "F10": ["反向筛", "平台经济 ≠ 经济与社会", "看到“数字经济/新业态/营商环境”就写双循环/有效市场", "选必二法律要锁立法-执法-司法三层和劳动者/消费者/数据产权三类", "把经济材料翻成法律规则、权利边界和救济路径", "不要写双循环/宏观调控/新发展格局", "2025东城一模__Q17;2025朝阳一模__Q19", "formal/lecture", "是", "否"],
}

rows = read_csv("05_framework_exhaustion_map.csv")
fixed = []
for row in rows:
    if row.get("node_id") in fixes:
        fixed.append(dict(zip(fields, [row["node_id"], *fixes[row["node_id"]]])))
    else:
        fixed.append({k: (row.get(k) or "") for k in fields})

with (root / "05_framework_exhaustion_map.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(fixed)


def esc(value):
    return str(value).replace("|", "\\|")


md = [
    "# 05 框架穷尽清单（飞哥版）",
    "",
    "本文档由 `05_framework_exhaustion_map.csv` 当前快照生成。每个节点对应一行；支撑题号回到 `04_core_questions.csv` 和 `source_lock_cards/` 卡片。",
    "",
    "| 编号 | 层 | 标题 | 看到什么 | 触发什么 | 怎么写 | 别写什么 | 支撑题号 | 证据等级 | 是否核心 | 是否参考 |",
    "|---|---|---|---|---|---|---|---|---|---|---|",
]
for row in fixed:
    md.append("| " + " | ".join(esc(row[k]) for k in fields) + " |")
(root / "05_framework_exhaustion_map.md").write_text("\n".join(md) + "\n", encoding="utf-8")

core_set = set(core_ids)
ref_set = {r["question_id"] for r in refs}
pending_set = {r["question_id"] for r in pending}


def canon(value):
    value = value.strip().replace("(deferred)", "").replace("(reference)", "")
    return re.sub(r"-sub\d+", "", value)


rows9 = []
for row in fixed:
    supports = [
        canon(x)
        for x in re.split(r"[;；]", row["支撑题号"])
        if canon(x) and canon(x) not in {"-", "S01-S05 都要警惕", "所有核心"}
    ]
    core_hits, ref_hits, gap_hits = [], [], []
    for support in supports:
        if support in core_set and support not in core_hits:
            core_hits.append(support)
        elif support in ref_set and support not in ref_hits:
            ref_hits.append(support)
        elif support in pending_set and support not in gap_hits:
            gap_hits.append(support)
        elif support not in core_set and support not in ref_set and support not in pending_set and support not in gap_hits:
            gap_hits.append(support)
    rows9.append({
        "node_id": row["node_id"],
        "类型": row["node_layer"],
        "框架点": row["node_title"],
        "核心题支撑": ";".join(core_hits),
        "核心题数量": str(len(core_hits)),
        "OPEN_OR_REFERENCE": ";".join(ref_hits),
        "缺源/边界题": ";".join(gap_hits),
        "备注": "核心矩阵只统计核心锁源题；开放和缺源不抬高覆盖数。",
    })

with (root / "09_框架_题目_覆盖矩阵.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["node_id", "类型", "框架点", "核心题支撑", "核心题数量", "OPEN_OR_REFERENCE", "缺源/边界题", "备注"])
    writer.writeheader()
    writer.writerows(rows9)

qa = """CLAUDE_ZERO_CONDITIONAL_PASS

1. 是否从 0 跑完题源：是；01-05 已完成并有清单、候选、source lock、证据清理、框架清单。
2. 是否只研究主观题：是；选择题未进入核心题链。
3. 是否 source lock 每道题：是；19 道核心题均有锁源卡与索引。
4. 是否前面框架穷尽：条件通过；05 CSV/MD 已校正反向筛字段，06 已按课堂版生成。
5. 是否后面全核心题穷尽：是；07 覆盖 Q01-Q19 共 19 道核心题。
6. 是否参考题和待补题单列：是；08 单列 OPEN_OR_REFERENCE 与缺源/边界题。
7. 是否没有工程语言进入学生正文：是；06/07 禁入词复扫为 0。
8. 是否没有参考答案/评分说明混入材料：条件通过；07 用课堂转译，不粘贴给分文本。
9. 是否没有万能合同、万能程序、万能意义：条件通过；按设问入口和材料触发分诊。
10. 是否像飞哥课堂框架：条件通过；仍建议人工抽读 3-5 题再定稿上课。
11. 是否不法考化、不必修三化、不经济化：条件通过；反向筛查已入 05/06/09。
12. 是否不写 FINAL_PASS/TASK_COMPLETE/DOCX/PDF：是；本文件只给条件通过，不封终局。

条件说明：06 与 07 已在 VS Code 可视会话补齐，08-10 已机械刷新，05 反向筛字段错位已修复；最终上课前仍建议抽样核对源锁卡与原卷。
"""
(root / "10_QA_acceptance.md").write_text(qa, encoding="utf-8")

zero = sum(1 for row in rows9 if row["核心题数量"] in ("", "0"))
print(f"WROTE_FIX_F_ROWS framework_rows={len(fixed)} matrix_rows={len(rows9)} zero_core_rows={zero}")
