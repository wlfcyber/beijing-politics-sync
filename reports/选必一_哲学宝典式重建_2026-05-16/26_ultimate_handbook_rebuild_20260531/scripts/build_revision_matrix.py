#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import json
import sys
from pathlib import Path


HARD_FIXES = {
    "181": {
        "issue_type": "PROMPT_REWRITE",
        "status": "ISSUE_FIXED_DATA",
        "corrected_prompt": "结合材料，综合运用所学，谈谈以中国式现代化全面推进中华民族伟大复兴，应如何运用“审势、乘势、驭势”的智慧。",
        "fix_note": "原卷设问完整表述，Claude稿压缩改写。",
        "evidence": "/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/试卷/试卷.pdf",
    },
    "179": {
        "issue_type": "SCORE_LAYER_WRONG",
        "status": "ISSUE_FIXED_DATA",
        "corrected_score_layers": "7分；按参考答案思路，每个倡议2分：路径1分+效果1分；总论1分，放在前面或后面都可以。",
        "fix_note": "原细则不是普通等级题。",
        "evidence": "/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/分题细则/阅卷总结/21题/20小题二模阅卷总结.docx",
    },
    "186": {
        "issue_type": "SCORE_LAYER_WRONG",
        "status": "ISSUE_FIXED_DATA",
        "corrected_score_layers": "7分；按参考答案思路，每个倡议2分：路径1分+效果1分；总论1分，放在前面或后面都可以。",
        "fix_note": "原细则不是普通等级题。",
        "evidence": "/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/分题细则/阅卷总结/21题/20小题二模阅卷总结.docx",
    },
    "189": {
        "issue_type": "SCORE_LAYER_WRONG",
        "status": "ISSUE_FIXED_DATA",
        "corrected_score_layers": "7分；按参考答案思路，每个倡议2分：路径1分+效果1分；总论1分，放在前面或后面都可以。",
        "fix_note": "原细则不是普通等级题。",
        "evidence": "/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/分题细则/阅卷总结/21题/20小题二模阅卷总结.docx",
    },
    "191": {
        "issue_type": "SCORE_LAYER_WRONG",
        "status": "ISSUE_FIXED_DATA",
        "corrected_score_layers": "7分；按参考答案思路，每个倡议2分：路径1分+效果1分；总论1分，放在前面或后面都可以。",
        "fix_note": "原细则不是普通等级题。",
        "evidence": "/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/分题细则/阅卷总结/21题/20小题二模阅卷总结.docx",
    },
}

for entry_id in ["72", "82", "85", "99", "124"]:
    HARD_FIXES[entry_id] = {
        "issue_type": "UNSUPPORTED_SCORE_SPLIT",
        "status": "ISSUE_FIXED_DATA",
        "corrected_score_layers": "8分；参考答案从我国高水平开放与新发展格局、世界经济技术合作与绿色转型、全球经济治理和规则制定等方向展开；原细则未明确标出3分+3分+2分分配。",
        "fix_note": "删除无来源的3/3/2分值结构，保留原题8分和答案方向。",
        "evidence": "/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026海淀一模/细则/细则.pdf",
    }

for entry_id in ["47", "168", "194"]:
    HARD_FIXES[entry_id] = {
        "issue_type": "SCORE_LAYER_TOO_COARSE",
        "status": "ISSUE_FIXED_DATA",
        "corrected_score_layers": "第(1)问6分：总体解释2分（理念蕴含普遍价值1分；能够形成共识/促成合作和发展/应对共同问题或挑战1分）；新发展理念说明2分（新发展理念内涵1分；结合材料说明实践成就1分）；对世界意义2分（拓展发展中国家走向现代化的途径1分；贡献中国智慧中国方案1分）。第(2)问2分：举例1分，说明1分。",
        "fix_note": "补回原细则的层级。",
        "evidence": "/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025西城一模/细则/细则.docx",
    }

HARD_FIXES["9"] = {
    "issue_type": "NO_FORMAL_RUBRIC_FILE_ANSWER_ONLY",
    "status": "SOURCE_LOCATED_ANSWER_ONLY",
    "corrected_prompt": "运用《当代国际政治与经济》知识，说明全球治理倡议为什么能获得国际社会广泛认同。（6分）",
    "corrected_score_layers": "6分；教师版参考答案：全球治理倡议顺应和平与发展的时代潮流，符合世界各国人民的共同愿望；以奉行主权平等、遵守国际法治、践行多边主义、倡导以人为本、注重行动导向为核心理念，坚定捍卫联合国宪章宗旨和原则，秉持共商共建共享的全球治理观，直面全球治理的突出问题，为推动建设更加公正合理的全球治理体系指引方向。未在桌面目录发现独立正式评分细则。",
    "fix_note": "桌面仅有教师版试卷/答案与讲评材料，未见独立细则；可核原题和参考答案，不可伪称有正式分层细则。",
    "evidence": "/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期中/试卷/试卷.docx",
}

XICHENG_Q20_PROMPT = "结合材料，运用《国际政治与经济》知识，阐释参与全球气候治理的中国实践。"
XICHENG_Q20_SCORE = "8分。角度1：中国实践是什么2分：在全球气候治理中，中国的角色（建设者/引领者/做负责任的大国）1分；具体做法（坚持绿色发展/新发展理念，有为政府+有效市场，用知识概括材料）1分。角度2：中国为什么要参与该实践3分，4选3：和平发展合作共赢是时代潮流/非传统安全威胁1分；共同利益1分；中国理念（人类命运共同体/全人类共同价值/正确义利观/共商共建共享/践行真正的多边主义/坚持互利共赢）1分；自觉履行国际义务/遵循国际法/承担国际责任1分。角度3：实践效果3分：对国际2分（促进全球可持续发展/建设清洁世界1分；维护联合国核心作用/完善全球治理体系1分）；对中国1分（贡献中国智慧/中国力量1分）。"

for entry_id in ["121", "165", "212", "213", "214"]:
    HARD_FIXES[entry_id] = {
        "issue_type": "SOURCE_SUPPLEMENTED_FROM_DESKTOP_OCR",
        "status": "ISSUE_FIXED_DATA",
        "corrected_prompt": XICHENG_Q20_PROMPT,
        "corrected_score_layers": XICHENG_Q20_SCORE,
        "fix_note": "桌面未单列试卷文件；原卷正文位于“高三思想政治参考答案.pdf”前9页。已据桌面OCR补回原设问，删除Claude稿多出的“中的”，并展开原细则分层。",
        "evidence": "/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末/细则/补充材料/高三思想政治参考答案.pdf || /Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末/细则/细则.pdf",
    }

CHAOYANG_MID_Q17_SCORE = "8分。一层3分，两层6分，三层8分。每一层：“总-分”结构（处理什么关系-如何处理关系）。第一层：处理好自力更生和对外开放的关系1分；核心技术自主可控/把握创新主动权/创新驱动/技术研发/自主研发/创新的新发展理念/核心竞争力1分；国际交流合作/参与经济全球化/参与国际分工/开放型经济/共商共建共享/两个市场两种资源/双循环1分。第二层：处理好发展和安全的关系/统筹发展和安全1分；总体国家安全观/底线思维/维护国家经济安全、科技安全/应对风险/政府履行经济职能监管/完善法律法规/其他维护安全的具体措施1分；经济平稳可持续发展/高质量发展/注入新动能/降本增效/提高效率/优化资源配置/经济增长1分。第三层：处理好中国发展和世界发展的关系1分；维护本国利益/谋求本国发展/满足我国人民美好生活需要/我国产业结构优化升级/其他促进我国发展的表现1分；兼顾他国合理关切/为世界提供公共产品和机遇/正确义利观/推动发展中国家/贡献中国智慧和中国方案/大国责任/人类命运共同体1分。"

for entry_id in ["30", "154", "198"]:
    HARD_FIXES[entry_id] = {
        "issue_type": "SCORE_LAYER_NORMALIZED_TO_RUBRIC",
        "status": "ISSUE_FIXED_DATA",
        "corrected_score_layers": CHAOYANG_MID_Q17_SCORE,
        "fix_note": "按原细则补全三层1+1+1结构，保留原文“每一层：总-分结构（处理什么关系-如何处理关系）”。",
        "evidence": "/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期中/细则/细则.docx",
    }

CHAOYANG_FINAL_Q20_SCORE = "8分。解构设问：哪些方面更有作为（4个角度）—为什么要更有作为（背景+目标）。聚焦和平发展、政治、经济、我国国家利益4个角度。中国特色大国外交主动作为，是顺应世界发展大势、服务国家发展大局的必然选择（此点不单独赋分，但在以下4个角度没满分时可加1分）。角度1：和平发展（背景1分+目标1分）：和平与发展是当今时代的主题1分；命运共同体/共同利益/国际新秩序/全球治理（结合材料/做法+目标）1分。角度2：政治（背景1分+目标1分）：多极化/单边主义/霸权强权1分；提升发展中国家代表性话语权/维护发展中国家利益/全球南方联合自强（结合材料/做法+目标）1分。角度3：经济（背景1分+目标1分）：全球化/贸易保护主义1分；开放型世界经济/世界经济共同繁荣/互利共赢/开放合作/共享成果（结合材料/做法+目标）1分。角度4：我国国家利益（背景1分+目标1分）：主权、安全、发展利益是国家核心利益/国家利益是国际关系的决定性因素/维护国家利益是主权国家对外活动的出发点和落脚点1分；维护人民利益/中国式现代化（结合材料/做法+目标）1分。"

for entry_id in ["8", "28", "29", "56", "104", "146", "226"]:
    HARD_FIXES[entry_id] = {
        "issue_type": "SCORE_LAYER_EXPANDED_FROM_RUBRIC",
        "status": "ISSUE_FIXED_DATA",
        "corrected_score_layers": CHAOYANG_FINAL_Q20_SCORE,
        "fix_note": "将“四个角度各2分”展开为原细则的背景+目标明细。",
        "evidence": "/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/细则/细则.pdf",
    }


def load_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: build_revision_matrix.py ENTRY_INDEX.csv AUTOMATED_AUDIT.csv OUTDIR", file=sys.stderr)
        return 2
    entries_path = Path(sys.argv[1])
    audit_path = Path(sys.argv[2])
    out_dir = Path(sys.argv[3])
    out_dir.mkdir(parents=True, exist_ok=True)

    entries = {row["global_entry_no"]: row for row in load_csv(entries_path)}
    audits = {row["global_entry_no"]: row for row in load_csv(audit_path)}

    rows = []
    for entry_id, entry in entries.items():
        audit = audits.get(entry_id, {})
        fix = HARD_FIXES.get(entry_id, {})
        status = fix.get("status")
        issue_type = fix.get("issue_type", "")
        if not status:
            auto_status = audit.get("overall_auto_status", "")
            if auto_status == "AUTO_LOCATED_NEEDS_MANUAL_CONFIRM":
                status = "SOURCE_LOCATED_PENDING_HUMAN_PASS"
            elif auto_status == "NEEDS_MANUAL_SURFACE_CHECK":
                status = "NEEDS_MANUAL_SURFACE_CHECK"
            elif auto_status.startswith("BLOCKED"):
                status = auto_status
            elif auto_status.startswith("ISSUE"):
                status = auto_status
            else:
                status = "PENDING_REVIEW"
        corrected_prompt = fix.get("corrected_prompt", entry.get("prompt", ""))
        corrected_score_layers = fix.get("corrected_score_layers", entry.get("score_layers", ""))
        row = {
            "global_entry_no": entry_id,
            "source_label": entry.get("source_label", ""),
            "bucket": entry.get("bucket", ""),
            "second_level": entry.get("second_level", ""),
            "core_point": entry.get("core_point", ""),
            "revision_status": status,
            "issue_type": issue_type,
            "original_prompt": entry.get("prompt", ""),
            "corrected_prompt": corrected_prompt,
            "original_score_layers": entry.get("score_layers", ""),
            "corrected_score_layers": corrected_score_layers,
            "when_to_write": entry.get("when_to_write", ""),
            "why_signal": entry.get("why_signal", ""),
            "surface_sentence": entry.get("surface_sentence", ""),
            "same_group": entry.get("same_group", ""),
            "auto_status": audit.get("overall_auto_status", ""),
            "paper_paths": audit.get("paper_paths", ""),
            "rubric_paths": audit.get("rubric_paths", ""),
            "evidence": fix.get("evidence", ""),
            "fix_note": fix.get("fix_note", ""),
            "raw_block": entry.get("raw_block", ""),
        }
        rows.append(row)

    fieldnames = list(rows[0].keys()) if rows else []
    with (out_dir / "REVISION_MATRIX.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    with (out_dir / "REVISION_MATRIX.jsonl").open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    summary = {"entries": len(rows), "by_status": {}, "hard_fixes": len(HARD_FIXES)}
    for row in rows:
        summary["by_status"][row["revision_status"]] = summary["by_status"].get(row["revision_status"], 0) + 1
    (out_dir / "revision_matrix_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
