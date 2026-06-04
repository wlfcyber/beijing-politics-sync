#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
PACKETS_JSONL = RUN_DIR / "03_source_packets" / "source_packets_final.jsonl"
OUT_DIR = RUN_DIR / "05_output"
OUT_JSON = OUT_DIR / "A_THEME_PENDING_BOUNDARY_RESOLUTIONS_20260604.json"
OUT_MD = OUT_DIR / "A_THEME_PENDING_BOUNDARY_RESOLUTIONS_20260604.md"


DECISIONS: dict[str, dict] = {
    "E009": {
        "status": "still_review_required",
        "clear_pending": False,
        "theme_decision": "A4/A10",
        "display_note": "模块内容可收入物业服务合同、违约责任与多元纠纷解决，但正式细则目前只定位到答案式文本，仍需保留核验口。",
        "residual_issue": "模块边界基本可收入A4/A10；未闭合的是正式点分布细则仍缺失，石景山一模细则PPT仅定位到答案式文字。",
        "evidence": [
            "材料为暴雨后业主与物业房屋漏雨纠纷，涉及物业服务合同、不可抗力抗辩、赔偿责任。",
            "设问要求法官为人民调解员提供专业指导，细则写人民调解、司法确认和多元纠纷解决。",
            "RUBRIC_FORMALITY_RECHECK显示该条仅找到答案式文本，未找到点分布正式细则。",
        ],
    },
    "E010": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A10",
        "display_note": "细则直接考回避制度，属于诉讼程序识别，不再作为模块边界待核。",
        "evidence": ["设问问回避理由，细则落在回避制度和程序公正。"],
    },
    "E011": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A10",
        "display_note": "细则要求辨析辩护人与诉讼代理人的用语，属于诉讼参与人程序知识。",
        "evidence": ["设问要求改正“辩护人”为“诉讼代理人”，直接对应诉讼代理制度。"],
    },
    "E012": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A7",
        "display_note": "细则直接落成年子女赡养义务、精神慰藉和法德结合，属于婚姻家庭主线。",
        "evidence": ["督促履行义务告知书的给分点是赡养义务、老年人权益和家庭美德。"],
    },
    "E018": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A5",
        "display_note": "典型案例意义围绕知识产权保护、严惩侵权、规范竞争和鼓励创新，收入A5。",
        "evidence": ["细则出现知识产权保护、侵权惩戒、市场竞争秩序和创新激励。"],
    },
    "E021": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A5",
        "display_note": "技术秘密、不正当竞争和知识产权保护是主给分点，法治价值只是设问包装。",
        "evidence": ["细则写技术秘密、不正当竞争、高额赔偿、劳动者保密义务和创新保护。"],
    },
    "E033": {
        "status": "resolved_open_container",
        "clear_pending": True,
        "theme_decision": "A4 with A5 co-trigger",
        "display_note": "两案分别触发合同违约和不正当竞争，本题以司法护航新质生产力作开放容器，主入口保留A4并提示A5共振。",
        "evidence": [
            "正式细则已从2025石景山一模细则DOC补入法理依据、事实依据和保障作用。",
            "案例一为合同违约责任，案例二为反不正当竞争法停止侵害、赔偿损失。",
        ],
    },
    "E034": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A5",
        "display_note": "法院判决分析围绕反不正当竞争、混淆和虚假宣传，收入A5。",
        "evidence": ["细则写反不正当竞争法、混淆、虚假宣传、诚信经营和数字经济营商环境。"],
    },
    "E046": {
        "status": "resolved_open_container",
        "clear_pending": True,
        "theme_decision": "A6",
        "display_note": "AI幻觉案例的法律落点是是否构成侵权、权益损害和责任边界，按A6开放容器处理。",
        "evidence": [
            "材料写AI生成错误信息、承诺赔偿、公司提示风险，法院认定不构成侵权。",
            "细则强调平衡民事权益保护与技术创新、规范AI行业和公正司法。",
        ],
    },
    "E052": {
        "status": "resolved_open_container",
        "clear_pending": True,
        "theme_decision": "A10",
        "display_note": "虽含刑事、行政、民事三类诉讼，但本分问只取举证责任和证据规则，收入A10开放容器。",
        "evidence": ["细则要求行政诉讼举证、民事谁主张谁举证、建筑物坠落过错推定和举证责任倒置。"],
    },
    "E053": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A2",
        "display_note": "细则明确生命权、身体权、健康权、财产权及合理教育边界，收入A2。",
        "evidence": ["题面虽有校园欺凌治理背景，但给分点是民法人格权益与未成年人保护。"],
    },
    "E054": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A3",
        "display_note": "民法典物权编绿色原则、物权权利义务和生态公共利益协调，收入A3。",
        "evidence": ["细则落民法绿色原则、物权行使边界、私益与生态公共利益平衡。"],
    },
    "E056": {
        "status": "resolved_open_container",
        "clear_pending": True,
        "theme_decision": "A6",
        "display_note": "生成式AI权责边界题以侵权责任和注意义务边界为法律底座，产业影响作为价值展开，收入A6开放容器。",
        "evidence": [
            "材料是用户起诉AI公司承担侵权责任，法院驳回请求。",
            "细则写明确权责边界、用户权益与技术创新平衡、行业合规。",
        ],
    },
    "E057": {
        "status": "still_review_required",
        "clear_pending": False,
        "theme_decision": "A10 tentative",
        "display_note": "本题主要问国家治理能力现代化、依法行政、司法公正和数字治理规则，选必二知识只是支撑材料，仍需保留模块边界核验。",
        "residual_issue": "国家治理现代化设问的主知识更接近政治与法治/法治中国，是否作为选必二正文题仍需教师裁决。",
        "evidence": [
            "设问要求从法治角度阐释最高人民法院发布典型案例对国家治理能力现代化的意义。",
            "细则含完善数字治理规则、依法行政、司法公正、全民守法、公共利益等跨模块表达。",
        ],
    },
    "E065": {
        "status": "resolved_open_container",
        "clear_pending": True,
        "theme_decision": "A10",
        "display_note": "涉外法治综合题中可由选必二支撑的是涉外民商事权利保护和调解、仲裁、诉讼衔接，收入A10开放容器。",
        "evidence": ["细则写外商投资法、保护中外当事人、涉外调解仲裁诉讼一站式纠纷解决。"],
    },
    "E068": {
        "status": "resolved_open_container",
        "clear_pending": True,
        "theme_decision": "A4",
        "display_note": "住房租赁条例题以合同示范文本、格式条款规制和租赁双方权益保护为主，收入A4开放容器。",
        "evidence": ["细则写合同示范文本、防止格式条款滥用、保护租赁双方权益、诚信与监管。"],
    },
    "E072": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A2",
        "display_note": "设问和细则明确要求从选必二角度说明财产权、隐私权、个人信息权益及救济方式，收入A2。",
        "evidence": ["细则明示选必2《法律与生活》角度，落财产权、隐私权、个人信息利益和维权责任。"],
    },
    "E074": {
        "status": "resolved_include",
        "clear_pending": True,
        "theme_decision": "A3",
        "display_note": "材料缺失问题已由嵌入图回源转写修复；财产制度、物权和产权保护主线收入A3。",
        "evidence": ["source repair层已根据顺义思政二模原卷嵌入image6.png转写财产制度时间轴。"],
    },
}


def load_packets() -> list[dict]:
    packets = []
    with PACKETS_JSONL.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                packets.append(json.loads(line))
    return packets


def main() -> None:
    packets = load_packets()
    pending_ids = {row["entry_id"] for row in packets if row.get("pending_reason")}
    decisions = []
    for entry_id, decision in DECISIONS.items():
        row = dict(decision)
        row["entry_id"] = entry_id
        row["source_has_pending_reason"] = entry_id in pending_ids
        decisions.append(row)
    decisions.sort(key=lambda item: item["entry_id"])

    unresolved = [row for row in decisions if not row["clear_pending"]]
    resolved = [row for row in decisions if row["clear_pending"]]
    missing_decisions = sorted(pending_ids - set(DECISIONS))
    stale_decisions = sorted(set(DECISIONS) - pending_ids)

    payload = {
        "generated_at": "2026-06-04T16:35:00+08:00",
        "source": str(PACKETS_JSONL),
        "source_pending_count": len(pending_ids),
        "decision_count": len(decisions),
        "resolved_count": len(resolved),
        "unresolved_count": len(unresolved),
        "missing_decisions_for_pending_ids": missing_decisions,
        "decisions_without_source_pending_reason": stale_decisions,
        "entries": {row["entry_id"]: row for row in decisions},
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# A类 pending 边界裁决覆盖层",
        "",
        "## 1. 口径",
        "",
        f"- 原始 pending_reason：{len(pending_ids)} 个。",
        f"- 本轮裁决覆盖：{len(decisions)} 个；已清除：{len(resolved)} 个；仍保留：{len(unresolved)} 个。",
        f"- 待裁决但无决定：{', '.join(missing_decisions) if missing_decisions else '无'}。",
        f"- 决定已写但源包当前无 pending_reason：{', '.join(stale_decisions) if stale_decisions else '无'}。",
        "",
        "## 2. 已清除 pending",
        "",
    ]
    for row in resolved:
        lines.append(f"- {row['entry_id']}｜{row['theme_decision']}｜{row['status']}：{row['display_note']}")
    lines.extend(["", "## 3. 仍保留待核", ""])
    for row in unresolved:
        lines.append(f"- {row['entry_id']}｜{row['theme_decision']}｜{row['status']}：{row.get('residual_issue') or row['display_note']}")
    lines.extend(["", "## 4. 逐条证据摘要", ""])
    for row in decisions:
        lines.append(f"### {row['entry_id']} {row['status']}")
        lines.append("")
        lines.append(f"- 主题裁决：{row['theme_decision']}")
        lines.append(f"- 正文显示：{row['display_note']}")
        if row.get("residual_issue"):
            lines.append(f"- 残余问题：{row['residual_issue']}")
        for evidence in row.get("evidence", []):
            lines.append(f"- 证据：{evidence}")
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    print(f"pending={len(pending_ids)} resolved={len(resolved)} unresolved={len(unresolved)}")


if __name__ == "__main__":
    main()
