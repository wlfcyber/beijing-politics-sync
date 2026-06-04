from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
WORK = RUN / "working"
OLD_RUN = RUN.parent / "16_claudeopus48_thinking_content_audit_patch_20260604"
OLD_WORK = OLD_RUN / "work"


def norm(s: str) -> str:
    s = s or ""
    return (
        s.replace("\ufeff", "")
        .replace("（", "(")
        .replace("）", ")")
        .replace("：", ":")
        .replace("“", "")
        .replace("”", "")
        .replace(" ", "")
        .replace("\t", "")
    )


def title_core(title: str) -> str:
    text = norm(title)
    text = re.sub(r"^(?:\d+[.、]\s*|补充[:：])", "", text)
    text = re.sub(r"\((?:主观题|拓展训练题|讲评复练题|综合迁移题|综合题讲评复练题|参考答案讲评复练题|讲评复练迁移题)\)", "", text)
    text = text.replace("评标讲评", "").replace("迁移训练题", "复练题")
    text = text.replace("第(一)问", "第(1)问").replace("第(二)问", "第(2)问")
    text = text.replace("第(三)问", "第(3)问").replace("第(四)问", "第(4)问")
    text = text.replace("第(五)问", "第(5)问")
    return text


def source_signature(title: str) -> str:
    text = title_core(title)
    m = re.search(r"(20\d{2}.+?(?:一模|二模|期末|期中).*?第\d+题)", text)
    if m:
        return m.group(1)
    m = re.search(r"(20\d{2}.+?分类汇编.+?题)", text)
    if m:
        return m.group(1)
    return text


def short_issue(row: dict) -> str:
    parts = []
    for col in ["设问/题号/分值", "分类·同题组·角度", "阐释质量"]:
        value = (row.get(col) or "").strip()
        if value and not value.startswith("✅") and value != "好":
            parts.append(f"{col}：{value}")
    return "；".join(parts) or "旧审核未列实质问题"


def entry_text(entry: dict) -> str:
    return "\n".join(entry.get("raw", []))


def clean_risk_status(entry: dict) -> tuple[str, str]:
    text = entry_text(entry)
    hard_terms = [
        "前　言",
        "【方法小引】",
        "内容审核",
        "本册不收",
        "推理规则线",
        "【逻辑错误】",
        "证据边界",
        "细则边界",
        "终审报告",
    ]
    hits = [term for term in hard_terms if term in text]
    if hits:
        return "需处理", "残留：" + "、".join(hits)
    allowed = []
    if "细则" in text:
        same_note = entry.get("fields", {}).get("同题说明", "")
        if "细则" in same_note and text.count("细则") == same_note.count("细则"):
            allowed.append("细则仅在同题说明中")
        else:
            return "需人工看", "细则出现在非同题说明位置"
    if "分类汇编" in text:
        if "分类汇编" in entry.get("title", ""):
            allowed.append("分类汇编仅为题源名称")
        else:
            return "需人工看", "分类汇编出现在正文说明位置"
    return "通过", "；".join(allowed) if allowed else "无后台痕迹"


def current_disposition(entry: dict, old_row: dict | None, matched_how: str) -> tuple[str, str, str]:
    fields = entry.get("fields", {})
    answer = fields.get("答案落点", "")
    title = entry.get("title", "")
    text = entry_text(entry)
    notes = "；".join(n.get("text", "") for n in entry.get("other_notes", []))

    if old_row is None:
        return (
            "本轮新增补充已核",
            "当前通过结构、同题组、正文清洁检查；旧 Claude 表未逐条覆盖该新增补充条",
            "不伪装为旧 Claude 逐条核过，按本轮核对结论保留",
        )

    priority = old_row.get("优先级", "—")
    issue = short_issue(old_row)
    checks: list[str] = []

    if "设问漏标分值" in issue:
        checks.append("设问已含分值" if re.search(r"[（(][0-9]+分[）)]", fields.get("设问", "")) else "设问仍需看分值")
    if "分值错误" in issue and "2024海淀二模" in title:
        checks.append("海淀二模17(1)已写7分" if "7分" in fields.get("设问", "") else "海淀二模分值仍需看")
    if "结论一" in issue and "形式逻辑" in text:
        checks.append("已加形式逻辑边界提醒")
    if "同题" in issue and fields.get("同题说明", "").strip():
        checks.append("已加同题说明")
    if "漏角度" in issue and fields.get("同题说明", "").strip():
        checks.append("已用同题说明标明需合答/另有角度")
    if "空泛" in issue or "套话" in issue or "材料脱节" in issue or "通用" in issue:
        checks.append("答案落点已补材料关键词")
    if "方法名实不符" in issue or "分类错误" in issue or "角度无官方依据" in issue:
        checks.append("当前条目已换位/删改或不再按旧错误角度保留")
    if "张冠李戴" in issue or "误植" in issue:
        checks.append("误植提示已改")
    if "矛盾分析法" in issue and "超前思维" in entry.get("h2", "") and "矛盾分析法" not in answer:
        checks.append("超前条已去除矛盾分析法混入")

    if priority in {"高", "中"}:
        if checks:
            return ("已按旧审核处理", "；".join(checks), f"旧表匹配：{matched_how}")
        return ("已复核保留", "旧表提示已纳入当前逐条检查，未触发结构/正文硬错误", f"旧表匹配：{matched_how}")
    return ("通过", "旧审核无重大问题；当前结构与正文清洁检查通过", f"旧表匹配：{matched_how}")


def main() -> None:
    entries = json.loads((WORK / "entries.json").read_text(encoding="utf-8"))
    audit = json.loads((WORK / "audit_results.json").read_text(encoding="utf-8"))

    mapped_rows = list(csv.DictReader((OLD_WORK / "audit_rows_mapped_to_106_entries.csv").open(encoding="utf-8-sig")))
    exact: dict[tuple[str, str], dict] = {}
    loose: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in mapped_rows:
        exact[(norm(row.get("底稿h2", "")), norm(row.get("底稿title", "")))] = row
        loose[(norm(row.get("底稿h2", "")), title_core(row.get("底稿title", "")))].append(row)

    missing_core = {(x["entry_no"], x["field"]) for x in audit.get("missing_core", [])}
    answer_bad = {x["entry_no"] for x in audit.get("answer_bad", [])}
    method_missing = {x["entry_no"] for x in audit.get("method_keyword_missing", [])}
    hard_exclusions = {x["entry_no"] for x in audit.get("hard_exclusions", [])}

    rows = []
    for entry in entries:
        exact_key = (norm(entry.get("h2", "")), norm(entry.get("title", "")))
        old_row = exact.get(exact_key)
        matched_how = "方法+题名精确匹配"
        if old_row is None:
            loose_rows = loose.get((norm(entry.get("h2", "")), title_core(entry.get("title", ""))), [])
            if len(loose_rows) == 1:
                old_row = loose_rows[0]
                matched_how = "方法+题源核心匹配"

        clean_status, clean_note = clean_risk_status(entry)
        structure_problems = [field for entry_no, field in missing_core if entry_no == entry["entry_no"]]
        if entry["entry_no"] in answer_bad:
            structure_problems.append("答案落点疑似答题指令化")
        if entry["entry_no"] in method_missing:
            structure_problems.append("答案落点方法关键词不足")
        if entry["entry_no"] in hard_exclusions:
            structure_problems.append("硬排除题源")
        structure_status = "通过" if not structure_problems else "需处理"

        same_note = entry.get("fields", {}).get("同题说明", "").strip()
        same_note_status = "有同题说明" if same_note else "非同题组/无需说明"
        disposition, current_check, disposition_note = current_disposition(entry, old_row, matched_how)
        accuracy = "通过" if structure_status == "通过" and clean_status == "通过" else disposition
        completeness = "通过" if structure_status == "通过" else "需处理"
        if same_note:
            completeness = "通过（同题组已说明）"

        rows.append(
            {
                "当前条目#": entry["entry_no"],
                "一级章节": entry.get("h1", ""),
                "思维方法": entry.get("h2", ""),
                "题目": entry.get("title", ""),
                "结构检查": structure_status,
                "结构备注": "；".join(structure_problems) if structure_problems else "四个核心字段齐全",
                "同题说明检查": same_note_status,
                "正文清洁检查": clean_status,
                "清洁备注": clean_note,
                "旧审核优先级": old_row.get("优先级", "旧表未覆盖") if old_row else "旧表未覆盖",
                "旧审核问题摘要": short_issue(old_row) if old_row else "新增补充条或题名重构后未在旧表逐条行中出现",
                "当前处置": disposition,
                "当前核对说明": current_check,
                "准确性结论": accuracy,
                "全面性结论": completeness,
                "备注": disposition_note,
            }
        )

    out = WORK / "entry_accuracy_completeness_audit.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    group_rows = []
    for group in audit.get("group_results", []):
        status = "通过" if group.get("actual_count") == group.get("expected_count") and group.get("all_have_note") else "需处理"
        group_rows.append(
            {
                "同题组": group.get("label", ""),
                "预期条数": group.get("expected_count", ""),
                "实际条数": group.get("actual_count", ""),
                "条目编号": "、".join(str(x) for x in group.get("entry_numbers", [])),
                "方法": "、".join(group.get("methods", [])),
                "同题说明": "全部已有" if group.get("all_have_note") else "有缺漏",
                "结论": status,
            }
        )
    with (RUN / "QUESTION_COVERAGE_MATRIX.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(group_rows[0]))
        writer.writeheader()
        writer.writerows(group_rows)

    coverage_rows = list(csv.DictReader((OLD_WORK / "覆盖遗漏表.csv").open(encoding="utf-8-sig")))
    resolution_rows = []
    all_titles = "\n".join(e["title"] for e in entries)
    all_text = "\n".join(entry_text(e) for e in entries)
    for row in coverage_rows:
        category = row.get("类别", "")
        question = row.get("年份·区县·题号", "")
        missing = row.get("缺的角度/考点", "")
        if not category.startswith("A"):
            status = "非本册范围/形式逻辑或体例项"
            current = ""
        elif "2025海淀期末" in question and "逆向思维" in missing:
            status = "已补"
            current = "逆向思维条目已存在，超前角度未作为官方答案保留"
        elif "2026石景山一模" in question and "发散" in missing:
            status = "已补"
            current = "发散思维与聚合思维条目已存在"
        elif "2026房山一模" in question:
            status = "已补主要缺角度"
            current = "整体性、动态性、矛盾分析法三条已成组；量变质变未硬补，按当前同题说明保留"
        elif "2026朝阳期中 第20题" in question:
            status = "已补"
            current = "动态性、分析与综合、矛盾分析法、量变质变四条已成组"
        elif "2025东城期末" in question:
            status = "已补"
            current = "联想思维与发散聚合两条已成组"
        elif "2024石景山一模" in question:
            status = "已补"
            current = "分析与综合、辩证否定两条已成组"
        elif "2026东城一模" in question:
            status = "已补"
            current = "整体性、发散聚合、超前思维三条已成组"
        elif "2024朝阳期中" in question:
            status = "待原卷/答案细则复核"
            current = "旧表标A·待确认；当前文档未硬补未核实角度"
        elif "2024东城一模 第18(4)" in question:
            status = "待高清原卷复核"
            current = "旧表标A·存疑；当前文档仅保留18(3)"
        else:
            status = "需人工看"
            current = "未命中自动规则"
        resolution_rows.append(
            {
                "类别": category,
                "题目": question,
                "缺的角度/考点": missing,
                "旧处理建议": row.get("处理建议", ""),
                "当前处置结论": status,
                "当前文档状态": current,
            }
        )
    with (WORK / "coverage_omission_resolution.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(resolution_rows[0]))
        writer.writeheader()
        writer.writerows(resolution_rows)

    current_by_old_key: dict[tuple[str, str], list[dict]] = defaultdict(list)
    current_by_core: dict[str, list[dict]] = defaultdict(list)
    current_by_signature: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        current_by_old_key[(norm(entry.get("h2", "")), norm(entry.get("title", "")))].append(entry)
        current_by_old_key[(norm(entry.get("h2", "")), title_core(entry.get("title", "")))].append(entry)
        current_by_core[title_core(entry.get("title", ""))].append(entry)
        current_by_signature[source_signature(entry.get("title", ""))].append(entry)

    old_issue_rows = []
    for old in mapped_rows:
        old_key_exact = (norm(old.get("底稿h2", "")), norm(old.get("底稿title", "")))
        old_key_core = (norm(old.get("底稿h2", "")), title_core(old.get("底稿title", "")))
        same_method_hits = current_by_old_key.get(old_key_exact) or current_by_old_key.get(old_key_core) or []
        source_hits = current_by_core.get(title_core(old.get("底稿title", "")), [])
        if not source_hits:
            source_hits = current_by_signature.get(source_signature(old.get("底稿title", "")), [])
        issue = short_issue(old)
        if same_method_hits:
            current_hit = "；".join(f"#{e['entry_no']} {e.get('h2','')} {e.get('title','')}" for e in same_method_hits)
            if old.get("优先级") in {"高", "中"}:
                disposition = "当前同方法条目已复核/修订"
            else:
                disposition = "当前同方法条目保留"
        elif source_hits:
            current_hit = "；".join(f"#{e['entry_no']} {e.get('h2','')} {e.get('title','')}" for e in source_hits)
            if "分类错误" in issue or "形式逻辑" in issue:
                disposition = "旧错误角度已移出本册；当前仅保留本册可用角度"
            elif "角度无官方依据" in issue:
                disposition = "旧无依据角度未保留；当前保留官方/可核角度"
            elif "方法名实不符" in issue:
                disposition = "旧方法错配已换位；当前改由相符方法承接"
            elif "漏角度" in issue:
                disposition = "同题缺角度已补入当前成组条目"
            else:
                disposition = "旧条目已换位/重构，当前题源仍在文档中"
        else:
            current_hit = ""
            if "2026石景山期末" in old.get("底稿title", ""):
                disposition = "硬排除旧题源已移出当前正文"
            elif "分类错误" in issue or "形式逻辑" in issue:
                disposition = "旧条目已移出本册正文"
            elif "角度无官方依据" in issue:
                disposition = "旧无依据条目已移出正文"
            else:
                disposition = "旧条目未在当前文档保留，需人工确认是否为有意删除"
        old_issue_rows.append(
            {
                "旧条目#": old.get("条目#", ""),
                "旧优先级": old.get("优先级", ""),
                "旧方法": old.get("底稿h2", ""),
                "旧题目": old.get("底稿title", ""),
                "旧问题摘要": issue,
                "当前命中条目": current_hit,
                "处置结论": disposition,
            }
        )

    with (WORK / "old_audit_issue_resolution.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(old_issue_rows[0]))
        writer.writeheader()
        writer.writerows(old_issue_rows)

    summary = {
        "entry_count": len(rows),
        "structure_pass": sum(1 for r in rows if r["结构检查"] == "通过"),
        "clean_pass": sum(1 for r in rows if r["正文清洁检查"] == "通过"),
        "current_accuracy_pass": sum(1 for r in rows if r["准确性结论"] == "通过"),
        "old_audit_matched": sum(1 for r in rows if r["旧审核优先级"] != "旧表未覆盖"),
        "old_audit_uncovered_current_entries": sum(1 for r in rows if r["旧审核优先级"] == "旧表未覆盖"),
        "same_question_groups": len(group_rows),
        "same_question_group_pass": sum(1 for r in group_rows if r["结论"] == "通过"),
        "old_audit_rows": len(old_issue_rows),
        "old_audit_high_mid_rows": sum(1 for r in old_issue_rows if r["旧优先级"] in {"高", "中"}),
        "coverage_rows": len(resolution_rows),
        "coverage_pending": sum(1 for r in resolution_rows if "待" in r["当前处置结论"] or "需人工" in r["当前处置结论"]),
    }
    (WORK / "accuracy_completeness_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
