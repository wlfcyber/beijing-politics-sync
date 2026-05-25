# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
CODEX = RUN / "02_codex_lane"
CLAUDE = RUN / "03_claudecode_lane"
FUSION = RUN / "04_fusion_audit"
GOV = RUN / "05_governor"
CONTROL = RUN / "00_control"
FUSION.mkdir(parents=True, exist_ok=True)
GOV.mkdir(parents=True, exist_ok=True)


def read_csv(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open("r", encoding="utf-8-sig", newline="")))


def qnorm(q: str) -> str:
    m = re.search(r"(20|21|1[0-9]|[1-9])", q or "")
    return m.group(1) if m else "unknown"


def key(row: dict) -> tuple[str, str]:
    return row.get("suite", ""), qnorm(row.get("question_no", ""))


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def load_jsonl_count(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def main() -> int:
    codex_review = read_csv(CODEX / "codex_a_review_queue.csv")
    codex_full = read_csv(CODEX / "codex_a_coverage_matrix.csv")
    claude_matrix = read_csv(CLAUDE / "claudecode_b_coverage_matrix.csv")
    claude_jsonl_count = load_jsonl_count(CLAUDE / "claudecode_b_second_mock_insert_candidates.jsonl")

    codex_by_key: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in codex_review:
        codex_by_key[key(r)].append(r)
    claude_by_key: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in claude_matrix:
        claude_by_key[key(r)].append(r)

    all_keys = sorted(set(codex_by_key) | set(claude_by_key), key=lambda x: (x[0], int(x[1]) if x[1].isdigit() else 99))
    match_rows: list[dict] = []
    for k in all_keys:
        crows = codex_by_key.get(k, [])
        brows = claude_by_key.get(k, [])
        c_dec = " | ".join(sorted({r.get("decision", "") for r in crows}))
        b_dec = " | ".join(sorted({r.get("decision", "") for r in brows}))
        c_terms = " | ".join(sorted({r.get("terms", "") for r in crows if r.get("terms")}))
        b_nodes = " | ".join(sorted({r.get("proposed_framework_node", "") for r in brows if r.get("proposed_framework_node")}))
        if crows and brows:
            status = "dual_lane_overlap"
            if "边界排除" in b_dec and "candidate" in c_dec:
                status = "conflict_boundary_vs_candidate"
        elif crows:
            status = "codex_only_review"
        else:
            status = "claudecode_only_review"
        match_rows.append({
            "suite": k[0],
            "question_no": k[1],
            "status": status,
            "codex_decision": c_dec,
            "claudecode_decision": b_dec,
            "codex_terms": c_terms,
            "claudecode_nodes": b_nodes,
            "codex_note": (crows[0].get("note", "") if crows else "")[:220],
            "claudecode_note": (brows[0].get("note", "") if brows else "")[:220],
        })

    write_csv(
        FUSION / "dual_lane_match_matrix.csv",
        match_rows,
        ["suite", "question_no", "status", "codex_decision", "claudecode_decision", "codex_terms", "claudecode_nodes", "codex_note", "claudecode_note"],
    )
    write_csv(
        FUSION / "fusion_review_queue.csv",
        [r for r in match_rows if r["status"] != "dual_lane_overlap" or "待" in r["claudecode_decision"] or "weak" in r["codex_decision"]],
        ["suite", "question_no", "status", "codex_decision", "claudecode_decision", "codex_terms", "claudecode_nodes", "codex_note", "claudecode_note"],
    )

    status_counts = Counter(r["status"] for r in match_rows)
    claude_decisions = Counter(r.get("decision", "") for r in claude_matrix)
    codex_phase = Counter((r.get("phase", ""), r.get("decision", "")) for r in codex_review)

    blockers = [
        "2026通州一模：试卷/评标 OCR 失败，ClaudeCode 标为缺证据，不能直接纳入。",
        "2026西城二模：评标 PDF 文本 0 字节；可先用教师版题干，但细则仍需 OCR/视觉核验。",
        "2026顺义二模：试卷 PDF 文本 0 字节；评标 doc 可读，但题干完整性需补。",
        "2026海淀二模：讲评 PDF 可抽取部分文字，但 ClaudeCode 标注为弱参考/需细则核验。",
        "2024朝阳一模、2024石景山一模：ClaudeCode 认为题号/哲学部分仍需回源定位。",
    ]

    report = [
        "# 双线融合前审核报告",
        "",
        "本报告只说明 Codex A 与 ClaudeCode B 已经跑到审核/融合前阶段，不代表最终 PASS，不生成 Word/PDF。",
        "",
        "## 双线产物",
        f"- Codex A review_queue 行数：{len(codex_review)}；完整 term matrix 行数：{len(codex_full)}。",
        f"- ClaudeCode B coverage matrix 行数：{len(claude_matrix)}；二模 JSONL 候选条数：{claude_jsonl_count}。",
        f"- 双线对账状态：{dict(status_counts)}。",
        f"- ClaudeCode B 决策统计：{dict(claude_decisions)}。",
        "",
        "## 关键结论",
        "- 不能说原宝典已穷尽。ClaudeCode B 独立回源后，明确指出 2025 一模就有一批高价值哲学题需要与母版逐题比对，用户“翻来覆去就那几道题”的担心成立。",
        "- 2026 二模不是简单加 52 条旧候选。旧候选只能作定位；B 线重跑后把候选分成强细则、弱证据、边界排除三类，且指出房山二模 Q18(2) 辩证否定、丰台一模 Q16 主流支流/两点论等是高优先补丁。",
        "- 主次矛盾、矛盾主次方面、两点论重点论不能再被写成“暂无稳定挂点”。本轮两线都命中相关题，后续必须按正式节点拆入。",
        "- 目前仍停在审核阶段。下一步是按 `fusion_review_queue.csv` 回源裁决，再把确定条目原地插入母版节点。",
        "",
        "## 必须先处理的阻塞",
        *[f"- {x}" for x in blockers],
        "",
        "## 下一步审核顺序",
        "1. 先处理双线都命中的 2026 二模强细则题，尤其东城 Q16、朝阳 Q16/Q21、丰台 Q16/Q21、房山 Q16/Q18(2)。",
        "2. 再处理 ClaudeCode B 标出的 2025 一模新增疑似遗漏，逐题对母版节点查重，不重复已有同题同触发点。",
        "3. 专项处理主次矛盾/矛盾主次方面/两点论重点论：确认题源、拆节点、避免把主次矛盾和矛盾主次方面混写。",
        "4. 对 OCR 阻塞项补图像/OCR或列为 blocked，不能在无证据情况下写正文。",
    ]
    (FUSION / "dual_lane_fusion_pre_audit.md").write_text("\n".join(report), encoding="utf-8")

    governor = [
        "# Governor Gate：融合前阶段",
        "",
        "结论：FAIL_FOR_FINAL_PASS / PASS_FOR_AUDIT_STAGE",
        "",
        "允许通过的只有“已完成双线审计到审核阶段”。禁止进入最终成品声明。",
        "",
        "不得 PASS 的原因：",
        "- 还有 OCR/视觉阻塞。",
        "- 还有母版逐题查重和原地插入裁决未完成。",
        "- ClaudeCode B 产物和 Codex A 产物存在题号定位、边界排除、证据等级差异。",
        "- 尚未生成学生版新正文，也未进行 GPTPro/Claude App 审核、Governor/Confucius 最终验收。",
    ]
    (GOV / "GOVERNOR_AUDIT_STAGE_GATE.md").write_text("\n".join(governor), encoding="utf-8")

    (CONTROL / "PROGRESS.md").write_text(
        (CONTROL / "PROGRESS.md").read_text(encoding="utf-8")
        + "\n| 2026-05-24 | Fusion checker | audit_stage_reached | ClaudeCode B 已真实跑完；双线对账和 Governor 融合前门禁已生成。 |\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
