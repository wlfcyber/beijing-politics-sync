# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import re
import shutil
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
FUSION = RUN / "04_fusion_audit"
SOURCE = RUN / "01_source_inventory"

ACCEPTED = FUSION / "student_patch_entries.accepted.jsonl"
BACKUP = FUSION / "student_patch_entries.accepted.backup_before_external_claude_triage_20260524.jsonl"
TRIAGE = FUSION / "claude_external_review_triage_20260524.md"


def load_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_rows(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )


def candidate_rows() -> dict[str, dict]:
    path = SOURCE / "second_mock_candidate_entries.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return {row["candidate_id"]: row for row in csv.DictReader(f)}


def evidence_level_from(text: str, fallback: str) -> str:
    if "正式" in text or "细则" in text or "阅卷" in text or "评标" in text:
        if "阅卷" in text:
            return "强阅卷版"
        return "强细则"
    return fallback


def apply_candidate(row: dict, candidate: dict) -> None:
    row["framework_node"] = candidate["section"]
    row["canonical_node"] = candidate["section"]
    row["material_trigger"] = candidate["trigger"]
    row["question_prompt"] = candidate["question"]
    row["why_trigger"] = candidate["why"]
    row["answer_landing"] = candidate["answer"]
    row["evidence_level"] = evidence_level_from(candidate.get("evidence", ""), row.get("evidence_level", ""))
    row["source_repair_basis"] = candidate.get("evidence", "")


def clean_meta(text: str) -> str:
    text = re.sub(r"。?答案要(?:写出|落到)[^。]*。?", "。", text)
    text = re.sub(r"，?不能只罗列单个做法。?", "。", text)
    text = re.sub(r"。{2,}", "。", text)
    text = text.replace("；。", "。").replace("，。", "。")
    return text.strip()


def patch_manual(row: dict, *, trigger: str, why: str, answer: str, prompt: str | None = None) -> None:
    row["material_trigger"] = trigger
    row["why_trigger"] = why
    row["answer_landing"] = answer
    if prompt is not None:
        row["question_prompt"] = prompt
    row["source_repair_basis"] = row.get("source_repair_basis", "") or "external Claude triage + suite source bundle repair"


def main() -> int:
    if not BACKUP.exists():
        shutil.copy2(ACCEPTED, BACKUP)

    rows = load_rows(ACCEPTED)
    candidates = candidate_rows()

    # Replace thin or source-drifted 2026 second-mock rows with source-grounded candidate text.
    candidate_map = {
        1: "old_2026_2mock_007",
        4: "old_2026_2mock_008",
        7: "old_2026_2mock_001",
        8: "old_2026_2mock_002",
        9: "old_2026_2mock_003",
        10: "old_2026_2mock_004",
        11: "old_2026_2mock_005",
        12: "old_2026_2mock_006",
        13: "old_2026_2mock_018",
        14: "old_2026_2mock_016",
        15: "old_2026_2mock_017",
        17: "old_2026_2mock_019",
        18: "old_2026_2mock_022",
        19: "old_2026_2mock_023",
        20: "old_2026_2mock_024",
        21: "old_2026_2mock_026",
        27: "old_2026_2mock_009",
        29: "old_2026_2mock_010",
        31: "old_2026_2mock_011",
        32: "old_2026_2mock_012",
        34: "old_2026_2mock_035",
        35: "old_2026_2mock_036",
        36: "old_2026_2mock_034",
        38: "old_2026_2mock_039",
        39: "old_2026_2mock_029",
        40: "old_2026_2mock_030",
        41: "old_2026_2mock_031",
    }
    for one_based, candidate_id in candidate_map.items():
        apply_candidate(rows[one_based - 1], candidates[candidate_id])

    # Source bundle still supports these East District nodes, but the old text was backfilled from principles.
    common_dongcheng_prompt = "结合材料，运用《哲学与文化》知识，谈谈“京彩课堂”的精彩所在。"
    patch_manual(
        rows[1],
        prompt=common_dongcheng_prompt,
        trigger="“京彩课堂”立足北京真实城市资源和学生成长实际，把思政课放到首都发展场景中设计。",
        why="物质决定意识要求从客观实际出发；课程内容和教学方案由北京真实资源、学生成长需要和时代育人任务决定，不能脱离现实空想。",
        answer="“京彩课堂”的精彩在于从北京实际和学生实际出发，把课程设计建立在真实城市资源和现实育人需要上，使思政学习更贴近现实、更有说服力。",
    )
    patch_manual(
        rows[2],
        prompt=common_dongcheng_prompt,
        trigger="课程把中轴线、故宫、科创基地、临空经济等真实场景与课堂任务、探究活动、数字资源联结起来。",
        why="多个场景、任务和资源不是孤立堆放，而是在同一育人目标下相互配合，触发整体与部分、系统优化的分析。",
        answer="“京彩课堂”的精彩在于坚持系统观念，统筹课堂学习、社会实践、城市文化和数字技术，让各类资源协同服务铸魂育人的整体目标。",
    )
    patch_manual(
        rows[4],
        prompt=common_dongcheng_prompt,
        trigger="课程围绕北京独有的历史文化资源、科技创新场景和学生探究任务展开，而不是套用一般化课堂模板。",
        why="矛盾具有特殊性，不同地区、不同课程资源、不同学生任务有自身特点；京彩课堂要把北京特色情境具体化。",
        answer="“京彩课堂”的精彩在于具体问题具体分析，把北京独特的文化场景、发展实践和学生学习任务结合起来，形成有首都特色的思政课堂。",
    )
    patch_manual(
        rows[5],
        prompt=common_dongcheng_prompt,
        trigger="材料强调课程的育人价值和铸魂作用，引导学生在北京实践中形成文化自信、责任意识和正确价值追求。",
        why="思政课不只是知识传递，还要解决价值引领问题；正确价值观会影响学生怎样认识城市、怎样选择行动方向。",
        answer="“京彩课堂”的精彩在于发挥正确价值观的导向作用，引导学生在真实场景中理解国家、城市与个人责任，形成正确价值判断和价值选择。",
    )

    patch_manual(
        rows[15],
        trigger="湿地保护既守护当前生态之美，也延续文化根脉，并要求从“治湖泊”转向“治流域”的持续治理。",
        why="材料强调湿地保护不是一次性动作，而是随着生态格局和治理对象变化持续推进，适合用发展的观点动态把握。",
        answer="守护湿地要坚持发展的观点，在长期治理中动态把握生态变化和文化延续，处理好当前修复与长远保护的关系，让生态之美持续生长。",
    )

    # Keep the practice node for Shunyi Q16, but align prompt and wording with the source candidate family.
    patch_manual(
        rows[36],
        prompt=candidates["old_2026_2mock_034"]["question"],
        trigger="新大众文艺扎根外卖员、快递员、家政工、退休职工、百姓演员等普通人的生活实践，创作来自真实生活而不是凭空编造。",
        why="评标材料列出实践观点；新大众文艺的生命力来自人民群众的真实生活实践，实践为文艺认识和表达提供源泉。",
        answer="新大众文艺要扎根人民群众生活实践，观察时代变化和百姓真实需求，把真实生活转化为有共鸣的文艺表达。",
    )

    # Merge duplicate/weak entries found by external Claude.
    delete_original_indices = {
        24,  # 2025海淀一模 Q21 duplicated system-optimization entry.
        28,  # 2026海淀二模 Q16 contradiction was not supported by the bundled source text.
        30,  # 2026海淀二模 Q16 recognition-reaction is folded into the practice/recognition entry.
    }
    rows[21]["answer_landing"] = (
        rows[21]["answer_landing"]
        + " 具体作答时，可把“整体性、关联性、协同性”和“整体与部分相互配合”合在一个系统观念链条里展开。"
    )
    rows[28]["answer_landing"] = (
        "青年既要学习系统理论和文明智慧，也要投身社会实践；在实践中理解、检验和发展认识，"
        "再用正确认识指导行动，把读书所得转化为服务社会的真本领。"
    )

    for row in rows:
        if row.get("source_suite") == "2025海淀一模" and row.get("question_no") == "Q21":
            row["question_no"] = "Q22"
        row["answer_landing"] = clean_meta(row.get("answer_landing", ""))
        row["material_trigger"] = row.get("material_trigger", "").replace("，体现量变积累到质变的规律", "")
        row["boundary_note"] = row.get("boundary_note", "").replace(
            "，禁止再展开为“传统政策/政策创新”或误解 OPC 缩写",
            "，禁止再误解 OPC 缩写",
        ).replace(
            "；文化多样性和中华优秀传统文化当代价值另属文化线，不在本条扩张",
            "；文化多样性和相关文化线内容不在本条扩张",
        )
        if row.get("source_suite") == "2026朝阳二模" and row.get("question_no") == "Q21":
            row["boundary_note"] = (row.get("boundary_note", "") + "；external repair: 主题已校正为“四个中国”。").strip("；")

    repaired_rows = [row for idx, row in enumerate(rows, 1) if idx not in delete_original_indices]
    write_rows(ACCEPTED, repaired_rows)

    TRIAGE.write_text(
        "\n".join(
            [
                "# External Claude Triage Repair - 2026-05-24",
                "",
                "## Accepted Hard Fixes",
                "- Corrected `2026朝阳二模 Q21`: the source topic is `四个中国`, not `五篇大文章`.",
                "- Corrected `2026房山二模 Q16`: the source question asks how to read `中华民族最感动人的浪漫` from Chinese industrial culture, not a generic `工匠精神的当代价值` prompt.",
                "- Replaced thin/backfilled 2026二模 rows with source-candidate trigger chains where the candidate table had stronger material wording.",
                "- Removed answer-landing meta language such as `答案要写出`, `答案要落到`, and `不能只罗列单个做法` from the accepted insertion data.",
                "- Merged duplicate `2025海淀一模 Q21` system-optimization insertion into one system-view entry.",
                "- Removed the unsupported independent `2026海淀二模 Q16` contradiction entry; bundled source text only supports `联系` and `实践与认识` angles for Q16.",
                "- Folded the separate `认识对实践的反作用` row for `2026海淀二模 Q16` back into the broader practice/recognition answer sentence.",
                "- Corrected `2025海淀一模` system-view/main-secondary-contradiction entries from `Q21` to `Q22`; the source bundle shows the system-view question is Q22.",
                "",
                "## Not Mechanically Collapsed",
                "- `2026东城二模 Q16`, `2026朝阳二模 Q16`, `2026丰台二模 Q16`, `2026顺义二模 Q16`, and `2026石景山二模 Q17(3)` still keep multiple framework placements where the suite source bundle or marking document explicitly names multiple philosophy angles.",
                "- This follows the accepted baodian pattern: framework-first placement by official principle node, with audit notes clarifying that optional angles are not cumulative point promises.",
                "",
                "## Still Not Final PASS",
                "- GPTPro web review is still pending because the controllable Chrome profile lacks the Codex Chrome extension.",
                "- External review package must be rebuilt with raw source evidence before a renewed external Claude/GPT review can fairly judge the repaired artifact.",
            ]
        ),
        encoding="utf-8",
    )

    print(f"repaired_rows={len(repaired_rows)} deleted={sorted(delete_original_indices)}")
    print(TRIAGE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
