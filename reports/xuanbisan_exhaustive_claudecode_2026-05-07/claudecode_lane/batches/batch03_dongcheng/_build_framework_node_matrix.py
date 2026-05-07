# -*- coding: utf-8 -*-
"""Build FRAMEWORK_NODE_MATRIX.csv and FRAMEWORK_NODE_MATRIX_SUMMARY.csv via csv.DictWriter."""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DETAIL_OUT = Path(__file__).parent / "FRAMEWORK_NODE_MATRIX.csv"
SUMMARY_OUT = Path(__file__).parent / "FRAMEWORK_NODE_MATRIX_SUMMARY.csv"

DETAIL_HEADER = ["framework_node", "parent_path", "挂载题id", "挂载类型", "证据等级", "备注"]


def detail_row(node, parent, qid, attach_type, level, note):
    return {
        "framework_node": node,
        "parent_path": parent,
        "挂载题id": qid,
        "挂载类型": attach_type,
        "证据等级": level,
        "备注": note,
    }


detail_rows = []

# ============= 创新思维相关节点 =============

# 思路新方法新结果新（创新思维特征）
detail_rows.append(detail_row(
    "创新思维-思路新方法新结果新（思维特征）",
    "创新思维>思维特征",
    "Q-2025东城期末-18-2",
    "正文正例",
    "A-formal",
    "东城期末细则第一层；登月服整体定性为创新思维（思路新方法新结果新即多向性跨越性独特性）",
))
detail_rows.append(detail_row(
    "创新思维-思路新方法新结果新（思维特征）",
    "创新思维>思维特征",
    "Q-2026东城一模-19-4",
    "正文正例",
    "A-formal",
    "19（4）.pptx 创新思维知识1分支持点；中关村'坚持实践+多向思考+敢用新手段+让原创落地'体现创新思维特征",
))

# 联想思维
detail_rows.append(detail_row(
    "创新思维-联想思维",
    "创新思维>联想",
    "Q-2025东城期末-18-2",
    "正文正例",
    "A-formal",
    "东城期末细则第二层第（2）点；登月服飞天飘带+火箭尾焰造型联想",
))

# 发散思维与聚合思维
detail_rows.append(detail_row(
    "创新思维-发散思维与聚合思维",
    "创新思维>发散与聚合",
    "Q-2025东城期末-18-2",
    "正文正例",
    "A-formal",
    "东城期末细则第二层第（1）点；登月服聚焦核心问题（聚合）+综合考虑不同需要（发散）",
))
detail_rows.append(detail_row(
    "创新思维-发散思维与聚合思维",
    "创新思维>发散与聚合",
    "Q-2026东城一模-19-4",
    "正文正例",
    "A-formal",
    "19（4）.pptx 创新思维子方法支持点；中关村发散拓展应用场景+聚合围绕成果转化轴心整合资源",
))

# 超前思维
detail_rows.append(detail_row(
    "创新思维-超前思维",
    "创新思维>超前思维",
    "Q-2025东城期末-18-2",
    "正文正例",
    "A-formal",
    "东城期末细则第二层第（3）点；登月服提前预判月面环境和航天员需求并据此设计细节",
))
detail_rows.append(detail_row(
    "创新思维-超前思维",
    "创新思维>超前思维",
    "Q-2026东城一模-19-4",
    "正文正例",
    "A-formal",
    "19（4）.pptx 超前思维支持点；中关村理性分析转化矛盾+做出预见+健全制度+谋划长远布局",
))

# ============= 辩证思维相关节点 =============

# 整体性·分析与综合
detail_rows.append(detail_row(
    "辩证思维-整体性·系统优化",
    "辩证思维>整体性",
    "Q-2025东城期末-5",
    "选择题陷阱",
    "B-choice-signal",
    "教师版参考解析确认C(②④)；社区道路改造对应整体性",
))
detail_rows.append(detail_row(
    "辩证思维-整体性·系统优化",
    "辩证思维>整体性",
    "Q-2026东城一模-19-4",
    "正文正例（同类索引到必修四系统观念）",
    "A-formal",
    "19（4）.pptx 系统观念知识1分支持点；中关村全链条统筹基础研究/技术研发/成果转化/产业应用",
))

# 动态性
detail_rows.append(detail_row(
    "辩证思维-动态性",
    "辩证思维>动态性",
    "Q-2025东城期末-5",
    "选择题陷阱",
    "B-choice-signal",
    "教师版参考解析确认C(②④)；要在整体和动态中认识和优化社区环境",
))

# 矛盾分析法
detail_rows.append(detail_row(
    "辩证思维-矛盾分析法",
    "辩证思维>矛盾分析法",
    "Q-2025东城期末-5",
    "选择题陷阱",
    "B-choice-signal",
    "教师版参考解析确认C(②④)；改造把入口窄/直角转弯与居民通行需要的矛盾解决",
))

# 分析与综合
detail_rows.append(detail_row(
    "辩证思维-分析与综合",
    "辩证思维>分析综合",
    "Q-2026东城一模-5",
    "选择题陷阱",
    "B-choice-signal",
    "试卷参考答案确认B；通过分析综合海量数据获得规律性认识",
))
detail_rows.append(detail_row(
    "辩证思维-分析与综合",
    "辩证思维>分析综合",
    "Q-2026东城一模-19-1",
    "同类索引（辅助理解）",
    "A-support",
    "19（1）.pptx 替代知识含'分析与综合统一'；调查研究法理由支持点；不入正文（题干未限定运用《逻辑与思维》）",
))

# ============= 认识发展历程 / 思维抽象 =============

# 思维抽象与思维具体（boundary 作为反例陷阱）
detail_rows.append(detail_row(
    "认识发展历程-思维抽象与思维具体",
    "认识发展历程>思维抽象+思维具体",
    "Q-2026东城一模-6",
    "边界陷阱（B项抽象思维误用）",
    "B-choice-signal",
    "答案D；'画马'活动B项'用科技手段和抽象思维表达运动创意'是抽象思维误用陷阱（具体形象不是思维抽象）",
))

# ============= 形式逻辑相关节点（推理部分主链） =============

# 矛盾律
detail_rows.append(detail_row(
    "推理-逻辑思维基本要求-矛盾律",
    "推理>逻辑思维基本要求>矛盾律",
    "Q-2026东城期末-17-2",
    "正文正例",
    "A-formal",
    "2026东城期末细则Slide41；主张1联言判断两支不能同真违反矛盾律2分",
))
detail_rows.append(detail_row(
    "推理-逻辑思维基本要求-矛盾律",
    "推理>逻辑思维基本要求>矛盾律",
    "Q-2026东城期末-7",
    "选择题陷阱",
    "B-choice-signal",
    "2026东城期末细则Slide10-11；吴老师与王老师矛盾必有一真一假",
))

# 三段论·中项不周延
detail_rows.append(detail_row(
    "推理-演绎推理-三段论·中项不周延",
    "推理>演绎>三段论>中项不周延",
    "Q-2026东城期末-17-2",
    "正文正例",
    "A-formal",
    "2026东城期末细则Slide43；主张3中项'采用XX模式'两次都不周延2分",
))
detail_rows.append(detail_row(
    "推理-演绎推理-三段论·中项不周延",
    "推理>演绎>三段论>中项不周延",
    "Q-2025东城期末-13",
    "选择题陷阱",
    "B-choice-signal",
    "试卷参考答案13.B；①③共同犯中项不周延错误",
))
detail_rows.append(detail_row(
    "推理-演绎推理-三段论·中项不周延",
    "推理>演绎>三段论>中项不周延",
    "Q-2026东城期末-6",
    "选择题陷阱",
    "B-choice-signal",
    "2026东城期末细则Slide8-9；A/C/D 选项犯中项不周延错误，需选B加入大前提保真",
))

# 三段论·大项不当扩大
detail_rows.append(detail_row(
    "推理-演绎推理-三段论·大项不当扩大",
    "推理>演绎>三段论>大项不当扩大",
    "Q-2025东城期末-13",
    "选择题陷阱（②项陷阱）",
    "B-choice-signal",
    "试卷参考答案13.B；②犯大项不当扩大错误（'三盘六针'前提不周项在结论中周延）",
))
detail_rows.append(detail_row(
    "推理-演绎推理-三段论·大项不当扩大",
    "推理>演绎>三段论>大项不当扩大",
    "Q-2026东城期末-6",
    "选择题陷阱（A项陷阱）",
    "B-choice-signal",
    "2026东城期末细则Slide8-9；A选项犯中项不周+大项不当扩大错误",
))

# 三段论·四概念错误
detail_rows.append(detail_row(
    "推理-演绎推理-三段论·四概念错误",
    "推理>演绎>三段论>四概念",
    "Q-2025东城期末-13",
    "选择题陷阱（④项陷阱）",
    "B-choice-signal",
    "试卷参考答案13.B；④'智能温控系统'同名不同义犯四概念错误",
))
detail_rows.append(detail_row(
    "推理-演绎推理-三段论·四概念错误",
    "推理>演绎>三段论>四概念",
    "Q-2026东城期末-6",
    "选择题陷阱（D项陷阱）",
    "B-choice-signal",
    "2026东城期末细则Slide8-9；D选项'部分生物成矿矿物'与'纯净无辐射独居石'引入第四个项犯四概念错误",
))

# 充分条件假言推理（肯前必肯后规则）
detail_rows.append(detail_row(
    "推理-演绎推理-充分条件假言推理",
    "推理>演绎>充分条件假言推理",
    "Q-2026东城期末-17-2",
    "正文正例",
    "A-formal",
    "2026东城期末细则Slide42；主张2前提'如果P则Q'结论'要Q必须P'犯肯后必肯前错误2分",
))
detail_rows.append(detail_row(
    "推理-演绎推理-充分条件假言推理",
    "推理>演绎>充分条件假言推理",
    "Q-2025东城期末-15",
    "选择题陷阱",
    "B-choice-signal",
    "试卷参考答案15.B；B项肯前否后违反'肯前必肯后'规则",
))
detail_rows.append(detail_row(
    "推理-演绎推理-充分条件假言推理",
    "推理>演绎>充分条件假言推理",
    "Q-2026东城期末-7",
    "选择题陷阱",
    "B-choice-signal",
    "2026东城期末细则Slide10-11；郑老师'¬人机赛跑→¬AI主题闯关'为假需肯前否后",
))

# 必要条件假言判断/推理
detail_rows.append(detail_row(
    "推理-演绎推理-必要条件假言推理",
    "推理>演绎>必要条件假言推理",
    "Q-2026东城期末-6",
    "选择题陷阱（B项正解作必要条件假言判断转化）",
    "B-choice-signal",
    "2026东城期末细则Slide8-9；B'只有具有绿色提取前景的，才是纯净无辐射独居石'即必要条件假言判断'P→Q'转化为周延中项的大前提",
))

# 选言推理 / 复合假言推理
detail_rows.append(detail_row(
    "推理-演绎推理-复合假言推理（除非否则/或者/如果就联立）",
    "推理>演绎>复合假言推理",
    "Q-2026东城一模-7",
    "选择题陷阱",
    "B-choice-signal",
    "18+选择7、13.pptx 符号化推理；逃逸粒子三式联立反证得A∧¬B",
))

# 换质位推理
detail_rows.append(detail_row(
    "推理-演绎推理-换质位推理（直言判断变形）",
    "推理>演绎>换质位推理",
    "Q-2026东城一模-6",
    "选择题陷阱（D项正解）",
    "B-choice-signal",
    "试卷参考答案6.D；'画马是将运动创意社交融合的活动'换质位得'未将…融合的不是画马'",
))

# 性质判断·主谓项周延
detail_rows.append(detail_row(
    "推理-判断-性质判断·主谓项周延",
    "推理>判断>性质判断>周延",
    "Q-2025东城期末-14",
    "选择题陷阱（D项正解）",
    "B-choice-signal",
    "试卷参考答案14.D；简单肯定判断谓项不周延规则",
))

# 关系判断·对称性/传递性
detail_rows.append(detail_row(
    "推理-判断-关系判断·对称性/传递性",
    "推理>判断>关系判断>对称性",
    "Q-2025东城期末-14",
    "选择题陷阱（B项陷阱）",
    "B-choice-signal",
    "试卷参考答案14.D；B'位于'是反对称关系而非传递关系",
))

# 概念外延关系（属种 vs 整体部分）
detail_rows.append(detail_row(
    "形式逻辑-概念-外延关系（属种/整体部分混淆）",
    "形式逻辑>概念>外延关系",
    "Q-2025东城期末-14",
    "选择题陷阱（A项陷阱）",
    "B-choice-signal",
    "试卷参考答案14.D；A把整体部分关系（中轴线/皇家宫苑建筑）误判为属种关系",
))

# 概念量项·特称量项（有些）
detail_rows.append(detail_row(
    "形式逻辑-判断-量项识别（有些/必然）",
    "形式逻辑>判断>量项",
    "Q-2026东城一模-6",
    "选择题陷阱（C项陷阱）",
    "B-choice-signal",
    "试卷参考答案6.D；C'有些A是B'不能必然推出'有些A不是B'，特称量项误推",
))

# ============= 综合短文同类索引 =============

detail_rows.append(detail_row(
    "综合应用-综合短文（同类索引节点）",
    "综合",
    "Q-2025东城期末-21",
    "同类索引",
    "boundary",
    "10分；'中国式现代化民生为大'综合题，细则水平描述含党的领导/以人民为中心等多角度；本节点fusion-only attach不入正文",
))
detail_rows.append(detail_row(
    "综合应用-综合短文（同类索引节点）",
    "综合",
    "Q-2026东城期末-21",
    "同类索引",
    "boundary",
    "8分；'区域发展落差势能转化为动能'综合题，细则'思维方法角度'含系统观念/科学思维/辩证思维/矛盾观/尊重客观规律等可选项；本节点fusion-only attach不入正文",
))

# Write detail
with DETAIL_OUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=DETAIL_HEADER, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(detail_rows)

print(f"wrote {len(detail_rows)} rows to {DETAIL_OUT}")

# Build summary
SUMMARY_HEADER = [
    "framework_node",
    "parent_path",
    "入正文题",
    "选择题陷阱题",
    "辅助挂载题",
    "辅助理解题",
    "同类索引题",
    "blocked题",
    "excluded题",
    "证据等级集合",
    "备注",
]

# Group by node
node_index = defaultdict(lambda: {
    "parent_path": "",
    "入正文题": [],
    "选择题陷阱题": [],
    "辅助挂载题": [],
    "辅助理解题": [],
    "同类索引题": [],
    "blocked题": [],
    "excluded题": [],
    "证据等级集合": set(),
    "备注": [],
})

for r in detail_rows:
    nb = node_index[r["framework_node"]]
    nb["parent_path"] = r["parent_path"]
    if r["挂载类型"].startswith("正文正例"):
        nb["入正文题"].append(r["挂载题id"])
    elif r["挂载类型"].startswith("选择题陷阱") or r["挂载类型"].startswith("边界陷阱"):
        nb["选择题陷阱题"].append(r["挂载题id"])
    elif r["挂载类型"].startswith("辅助挂载"):
        nb["辅助挂载题"].append(r["挂载题id"])
    elif r["挂载类型"].startswith("辅助理解") or "辅助理解" in r["挂载类型"]:
        nb["辅助理解题"].append(r["挂载题id"])
    elif r["挂载类型"].startswith("同类索引") or r["挂载类型"] == "同类索引":
        nb["同类索引题"].append(r["挂载题id"])
    elif r["挂载类型"].startswith("blocked"):
        nb["blocked题"].append(r["挂载题id"])
    elif r["挂载类型"].startswith("excluded"):
        nb["excluded题"].append(r["挂载题id"])
    nb["证据等级集合"].add(r["证据等级"])
    nb["备注"].append(r["备注"])

summary_rows = []
for node, info in node_index.items():
    summary_rows.append({
        "framework_node": node,
        "parent_path": info["parent_path"],
        "入正文题": ";".join(info["入正文题"]),
        "选择题陷阱题": ";".join(info["选择题陷阱题"]),
        "辅助挂载题": ";".join(info["辅助挂载题"]),
        "辅助理解题": ";".join(info["辅助理解题"]),
        "同类索引题": ";".join(info["同类索引题"]),
        "blocked题": ";".join(info["blocked题"]),
        "excluded题": ";".join(info["excluded题"]),
        "证据等级集合": ";".join(sorted(info["证据等级集合"])),
        "备注": " / ".join(info["备注"]),
    })

with SUMMARY_OUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=SUMMARY_HEADER, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(summary_rows)

print(f"wrote {len(summary_rows)} unique nodes to {SUMMARY_OUT}")
