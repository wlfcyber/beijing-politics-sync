#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治")
FINAL_ROOT = ROOT / "必修四最终整合_2026-05-02"
OUT_DIR = FINAL_ROOT / "outputs"
AUDIT_DIR = FINAL_ROOT / "audit"
REPORT_DIR = FINAL_ROOT / "reports"

CODEX_WORK = ROOT / "哲学宝典5.2原地修订"
CODEX_ENTRIES = CODEX_WORK / "audit" / "repaired_entries.json"
CODEX_MD = CODEX_WORK / "audit" / "最终Word写入稿.md"
CODEX_DOCX = Path("/Users/wanglifei/Desktop/哲学宝典最终版 5.2凌晨.docx")

CLAUDE_ROOT = ROOT / "必修四从0重跑_ClaudeCode_2026-05-02"
CLAUDE_ENTRIES = CLAUDE_ROOT / "audit" / "entries"

REBUILD_PATH = CODEX_WORK / "scripts" / "rebuild_in_place_baodian.py"
spec = importlib.util.spec_from_file_location("codex_rebuild_baodian", REBUILD_PATH)
rebuild = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(rebuild)

TITLE = "2026北京高考政治哲学宝典---三年模拟全触发全链条"
SIGNATURE = "飞哥正志讲堂"
FINAL_STEM = "2026北京高考政治哲学宝典---三年模拟全触发全链条_最终整合版"
FINAL_MD = OUT_DIR / f"{FINAL_STEM}.md"
FINAL_DOCX = OUT_DIR / f"{FINAL_STEM}.docx"
DESKTOP_DOCX = Path("/Users/wanglifei/Desktop/哲学宝典最终版 5.2整合终版.docx")

STRICT_FORBIDDEN_RE = re.compile(
    r"细则|评标|参考答案|答案写|答案核|答案/补充|可从.*角度|/Users/|"
    r"\.pdf|\.docx|\.pptx|OCR|debug|slide|line id|file id|PASS|"
    r"correct_option_chain|filled",
    re.IGNORECASE,
)

# Claude 线由 Codex 督工回源补过的三套。这里逐条指定落点，避免把 Claude
# 的宽泛/复合节点误映射到飞哥框架。
CLAUDE_NODE_OVERRIDES = {
    "2026_朝阳_期中__Q4__联系多样性": ("二、辩证法", "联系的多样性"),
    "2026_朝阳_期中__Q18__矛盾对立统一": ("二、辩证法", "矛盾就是对立统一"),
    "2026_朝阳_期中__Q18__具体问题具体分析": ("二、辩证法", "矛盾的特殊性 / 具体问题具体分析"),
    "2026_朝阳_期中__Q18__主观能动性": ("一、唯物论", "主观能动性 / 意识的能动作用"),
    "2026_朝阳_期中__Q18__价值判断与价值选择": ("五、价值观 / 人生观", "价值判断与价值选择"),
    "2026_朝阳_期中__Q18__辩证否定": ("二、辩证法", "辩证否定 / 守正创新"),
    "2026_丰台_期末__Q16__矛盾对立统一": ("二、辩证法", "矛盾就是对立统一"),
    "2026_丰台_期末__Q16__量变质变适度": ("二、辩证法", "量变与质变 / 适度原则"),
    "2026_丰台_期末__Q16__整体与部分联系": ("二、辩证法", "整体与部分"),
    "2026_丰台_期末__Q16__规律与能动性": ("一、唯物论", "尊重客观规律与发挥主观能动性相结合"),
    "2026_通州_期末__Q16__一切从实际出发": ("一、唯物论", "一切从实际出发 / 实事求是 / 主观与客观具体的历史的统一"),
    "2026_通州_期末__Q16__规律与能动性": ("一、唯物论", "尊重客观规律与发挥主观能动性相结合"),
    "2026_通州_期末__Q16__联系观点": ("二、辩证法", "联系的普遍性 / 联系的观点（总）"),
    "2026_通州_期末__Q16__发展的观点": ("二、辩证法", "发展的观点 / 发展的普遍性"),
    "2026_通州_期末__Q16__辩证否定守正创新": ("二、辩证法", "辩证否定 / 守正创新"),
    "2026_通州_期末__Q16__人民群众": ("四、历史唯物主义", "人民群众"),
}


def ensure_dirs() -> None:
    for path in [OUT_DIR, AUDIT_DIR, REPORT_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def entry_key(e: dict) -> tuple[str, str, str, str, str]:
    return (
        e["module"],
        e["node"],
        rebuild.normalize_suite(e["suite"]),
        rebuild.normalize_q(e["q"]),
        e["qtype"],
    )


def clean_student_text(value: str) -> str:
    text = rebuild.clean_text(value)
    text = re.sub(r"^答案\s*([A-D])", r"正确项是 \1", text)
    text = text.replace("答案 A", "正确项是 A")
    text = text.replace("答案 B", "正确项是 B")
    text = text.replace("答案 C", "正确项是 C")
    text = text.replace("答案 D", "正确项是 D")
    return rebuild.clean_text(text)


def load_codex_entries() -> list[dict]:
    entries = json.loads(CODEX_ENTRIES.read_text(encoding="utf-8"))
    for e in entries:
        e["merge_source"] = "codex-5.2"
    return entries


def load_selected_claude_entries() -> list[dict]:
    selected = []
    for path in sorted(CLAUDE_ENTRIES.glob("*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            raw = json.loads(line)
            entry_id = raw.get("entry_id", "")
            if entry_id not in CLAUDE_NODE_OVERRIDES:
                continue
            module, node = CLAUDE_NODE_OVERRIDES[entry_id]
            qtype = "选择题" if raw.get("question_type") == "choice" else "主观题"
            suite = f"{raw.get('year')}{raw.get('district')}{raw.get('stage')}"
            q = str(raw.get("question_no") or "")
            sub_part = str(raw.get("sub_part") or "").strip()
            if sub_part:
                q = f"{q}({sub_part.strip('()（）')})"
            fields = {k: clean_student_text(raw.get(k, "")) for k in ["材料触发点", "设问", "为什么能想到", "答案落点"]}
            blob = "\n".join(fields.values())
            if STRICT_FORBIDDEN_RE.search(blob):
                raise ValueError(f"Claude selected entry still has audit residue: {entry_id}")
            if any(not fields[k] for k in fields):
                raise ValueError(f"Claude selected entry has empty student field: {entry_id}")
            selected.append(
                {
                    "module": module,
                    "node": node,
                    "suite": suite,
                    "q": q,
                    "qtype": qtype,
                    "heading_base": rebuild.title_from_parts(suite, q, qtype),
                    "fields": fields,
                    "origin": "claudecode-codex-supervised-2026-05-02",
                    "merge_source": "claude-supervised",
                    "source_entry_id": entry_id,
                    "evidence_level": raw.get("evidence_level", ""),
                    "image": "",
                }
            )
    return selected


def merge_entries(codex_entries: list[dict], claude_entries: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
    merged = list(codex_entries)
    seen = {entry_key(e) for e in merged}
    imported = []
    skipped = []
    for e in claude_entries:
        key = entry_key(e)
        if key in seen:
            skipped.append(e)
            continue
        merged.append(e)
        seen.add(key)
        imported.append(e)
    merged.sort(key=rebuild.sort_key)
    return merged, imported, skipped


def write_markdown(entries: list[dict], out_path: Path) -> None:
    lines = [f"# {TITLE}", "", f"**{SIGNATURE}**", "", "## 前言", "", "（此处留给飞哥老师自行撰写。）", ""]
    current_module = current_node = None
    for e in entries:
        if e["module"] != current_module:
            current_module = e["module"]
            current_node = None
            lines.extend([f"## {current_module}", ""])
        if e["node"] != current_node:
            current_node = e["node"]
            lines.extend([f"### {current_node}", ""])
        lines.extend([f"#### {e['heading_base']}", ""])
        for k in ["材料触发点", "设问", "为什么能想到", "答案落点"]:
            lines.extend([f"【{k}】 {e['fields'][k]}", ""])
    out_path.write_text("\n".join(lines), encoding="utf-8")


def qa_payload(entries: list[dict], imported: list[dict], skipped: list[dict]) -> dict:
    blob = "\n".join("\n".join(e["fields"].values()) for e in entries)
    forbidden = sorted(set(m.group(0) for m in STRICT_FORBIDDEN_RE.finditer(blob)))
    missing = [
        e.get("heading_base", "")
        for e in entries
        if any(not e["fields"].get(k) for k in ["材料触发点", "设问", "为什么能想到", "答案落点"])
    ]
    keys = Counter(entry_key(e) for e in entries)
    dupes = [key for key, count in keys.items() if count > 1]
    hard_samples = {
        "2026海淀一模_Q16": [
            (e["module"], e["node"]) for e in entries if e["suite"] == "2026海淀一模" and e["q"] == "16"
        ],
        "2024东城一模_Q18(3)": [
            (e["module"], e["node"]) for e in entries if e["suite"] == "2024东城一模" and e["q"] in {"18(3)", "18（3）"}
        ],
        "2026丰台期末_Q16": [
            (e["module"], e["node"]) for e in entries if e["suite"] == "2026丰台期末" and e["q"] == "16"
        ],
    }
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "codex_entries": len([e for e in entries if e.get("merge_source") == "codex-5.2"]),
        "claude_imported_entries": len(imported),
        "claude_duplicate_skipped": len(skipped),
        "final_entries": len(entries),
        "forbidden_hits": forbidden,
        "missing_student_fields": missing,
        "duplicate_keys": [str(k) for k in dupes],
        "hard_samples": hard_samples,
        "imported_source_entry_ids": [e["source_entry_id"] for e in imported],
        "skipped_duplicate_source_entry_ids": [e["source_entry_id"] for e in skipped],
    }


def write_reports(entries: list[dict], imported: list[dict], skipped: list[dict], qa: dict) -> None:
    compare_lines = [
        "# 必修四双线程对比合并报告 2026-05-02",
        "",
        "## 合并判断",
        "",
        "- 主稿采用 Codex 5.2 凌晨版：它已经完成学生稿清洗、框架排序、Word 打开保存和 PDF 导出检查。",
        "- ClaudeCode 线经 Codex 督工接管后，完成禁词清理、覆盖表重建和三套漏闭环修复；本次只吸收这些有明确证据链且能落入飞哥框架的条目。",
        "- 重复键保持 Codex 版，不用 Claude 覆盖已经通过 QA 的正文。",
        "",
        "## 吸收的 ClaudeCode 精华",
        "",
    ]
    if imported:
        for e in imported:
            compare_lines.append(f"- {e['source_entry_id']} -> {e['module']} / {e['node']} / {e['heading_base']}")
    else:
        compare_lines.append("- 无新增导入。")
    compare_lines.extend(["", "## 跳过的 ClaudeCode 条目", ""])
    if skipped:
        for e in skipped:
            compare_lines.append(f"- {e['source_entry_id']}：Codex 5.2 已有同一题目同一框架节点，保留 Codex 表述。")
    else:
        compare_lines.append("- 无重复跳过。")
    compare_lines.extend(
        [
            "",
            "## 输出文件",
            "",
            f"- Markdown：{FINAL_MD}",
            f"- Word：{FINAL_DOCX}",
            f"- 桌面副本：{DESKTOP_DOCX}",
        ]
    )
    (REPORT_DIR / "必修四双线程对比合并报告_2026-05-02.md").write_text("\n".join(compare_lines), encoding="utf-8")

    accept_lines = [
        "# 必修四最终版验收报告 2026-05-02",
        "",
        f"- Codex 主稿条目：{qa['codex_entries']}",
        f"- Claude 督工补入条目：{qa['claude_imported_entries']}",
        f"- Claude 重复跳过条目：{qa['claude_duplicate_skipped']}",
        f"- 最终条目数：{qa['final_entries']}",
        f"- 学生字段禁词命中：{qa['forbidden_hits']}",
        f"- 四字段缺失：{len(qa['missing_student_fields'])}",
        f"- 重复键残留：{len(qa['duplicate_keys'])}",
        "",
        "## 硬样本",
        "",
    ]
    for name, rows in qa["hard_samples"].items():
        accept_lines.append(f"- {name}: {rows}")
    accept_lines.extend(["", "## 待补充", "", "- Word 视觉/导出结果见同目录后续 Word 验收记录。"])
    (REPORT_DIR / "必修四最终版验收报告_2026-05-02.md").write_text("\n".join(accept_lines), encoding="utf-8")


def main() -> None:
    ensure_dirs()
    codex_entries = load_codex_entries()
    claude_entries = load_selected_claude_entries()
    merged, imported, skipped = merge_entries(codex_entries, claude_entries)
    qa = qa_payload(merged, imported, skipped)
    if qa["forbidden_hits"] or qa["missing_student_fields"] or qa["duplicate_keys"]:
        raise SystemExit(json.dumps(qa, ensure_ascii=False, indent=2))

    (AUDIT_DIR / "final_entries.json").write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    (AUDIT_DIR / "claude_selected_entries.json").write_text(json.dumps(claude_entries, ensure_ascii=False, indent=2), encoding="utf-8")
    (AUDIT_DIR / "claude_imported_entries.json").write_text(json.dumps(imported, ensure_ascii=False, indent=2), encoding="utf-8")
    (AUDIT_DIR / "claude_skipped_duplicates.json").write_text(json.dumps(skipped, ensure_ascii=False, indent=2), encoding="utf-8")
    (AUDIT_DIR / "final_qa.json").write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    write_markdown(merged, FINAL_MD)
    tmp_docx = OUT_DIR / f"{FINAL_STEM}.tmp.docx"
    rebuild.build_doc(merged, tmp_docx)
    os.replace(tmp_docx, FINAL_DOCX)
    shutil.copy2(FINAL_DOCX, DESKTOP_DOCX)
    write_reports(merged, imported, skipped, qa)
    print(json.dumps(qa, ensure_ascii=False, indent=2))
    print(f"FINAL_MD={FINAL_MD}")
    print(f"FINAL_DOCX={FINAL_DOCX}")
    print(f"DESKTOP_DOCX={DESKTOP_DOCX}")


if __name__ == "__main__":
    main()
