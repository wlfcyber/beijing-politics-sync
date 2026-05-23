from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


DESKTOP = Path.home() / "Desktop"
ROOT = DESKTOP / "02_代码项目与工具" / "mac-thread-restore" / "beijing-politics-sync-visible"
RUN = ROOT / "reports" / "bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23"
STRICT = ROOT / "reports" / "bixiu4_philosophy_strict_v8_2026-05-23"
OUT = RUN / "04_review_packages"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size <= 10:
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def trim(text: str, n: int = 420) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= n else text[: n - 1] + "…"


def row_block(row: dict[str, str], idx: int) -> str:
    return "\n".join(
        [
            f"### {idx}. {row.get('suite_name') or row.get('source')} {row.get('question') or ('第' + row.get('question_no_norm', '') + '题')}",
            "",
            f"- 当前/建议节点：{row.get('section') or row.get('trigger') or row.get('knowledge_point', '')}",
            f"- 材料触发：{trim(row.get('material') or row.get('material_trigger') or '')}",
            f"- 触发知识：{trim(row.get('trigger') or row.get('knowledge_point') or '')}",
            f"- 现有逻辑：{trim(row.get('logic') or row.get('correct_chain') or row.get('answer_landing') or '')}",
            f"- 证据等级：{row.get('evidence_grade_initial') or row.get('evidence_level') or ''}",
            "",
            "请审核：是否应进入哲学宝典？当前节点是否错放？若错，应放到哪个节点？是否存在过度归因？",
            "",
        ]
    )


def make_package(name: str, title: str, rows: list[dict[str, str]], extra: str = "") -> None:
    lines = [
        f"# {title}",
        "",
        "你是网页版 GPT Pro / Claude 外部审核员。请只做严格审核，不要替 Codex 找借口。",
        "",
        "审核标准：",
        "- 不能用“等角度”兜底新增原理。",
        "- 主观题必须判断：材料是否真实触发该原理、答案落点是否能直接回应设问。",
        "- 选择题必须判断：这是正确项链、错肢辨析，还是文化-only/政治-only，不要硬塞哲学。",
        "- 高风险词（主要矛盾、矛盾主要方面、两点论重点论、主流支流、辩证否定、量变质变、价值观导向）必须有明确文本支持。",
        "- 输出按四栏：KEEP / MOVE / DELETE_OR_DOWNGRADE / NEED_EVIDENCE。",
        "- 每条意见必须具体到套卷、题号、当前节点、建议节点、理由。",
        "",
    ]
    if extra:
        lines.extend([extra, ""])
    for i, row in enumerate(rows, 1):
        lines.append(row_block(row, i))
    (OUT / name).write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    roster = read_csv(STRICT / "current_65_suite_roster.csv")
    subj = read_csv(STRICT / "old_subjective_rows_present_but_quality_failed_v8.csv")
    choices = read_csv(STRICT / "remaining_old_choice_presence_gaps_after_v7.csv")

    # Existing v8 new-9 data is embedded in scripts; pull the generated CSV if present, otherwise focus packages on strict gate rows.
    new9_rows: list[dict[str, str]] = []
    new9_csvs = list((STRICT / "new_9_suite_integration").rglob("*.csv")) if (STRICT / "new_9_suite_integration").exists() else []
    for p in new9_csvs:
        if "entries" in p.name or "candidate" in p.name or "choice" in p.name:
            new9_rows.extend(read_csv(p))

    priority = {"海淀", "西城", "东城", "朝阳"}

    def is_priority(row: dict[str, str]) -> bool:
        blob = (row.get("suite_name", "") + row.get("source", "") + row.get("district", ""))
        return any(d in blob for d in priority)

    subj_priority = [r for r in subj if is_priority(r)]
    subj_other = [r for r in subj if not is_priority(r)]
    choice_priority = [r for r in choices if is_priority(r)]
    choice_other = [r for r in choices if not is_priority(r)]

    high_terms = ["主要矛盾", "矛盾的主要方面", "两点论", "重点论", "主流", "支流", "辩证否定", "量变", "质变", "价值观"]
    highrisk = [
        r
        for r in subj + choices
        if any(term in " ".join(r.values()) for term in high_terms)
    ]

    make_package(
        "GPTPRO_WEB_BATCH_A_海西东朝主观题.md",
        "GPT Pro 网页版审核包 A：海淀/西城/东城/朝阳主观题错位审查",
        subj_priority,
        "重点：海淀、西城、东城、朝阳权重最高；请优先查这些主观题是不是放错原理节点。",
    )
    make_package(
        "GPTPRO_WEB_BATCH_B_郊区主观题.md",
        "GPT Pro 网页版审核包 B：郊区主观题错位审查",
        subj_other,
        "重点：丰台、石景山、门头沟、房山、通州、顺义、昌平、延庆等。",
    )
    make_package(
        "GPTPRO_WEB_BATCH_C_高风险原理.md",
        "GPT Pro 网页版审核包 C：高风险原理专项",
        highrisk,
        "重点：凡是涉及主要矛盾、矛盾主要方面、两点论重点论、主流支流、辩证否定、量变质变、价值观导向，都要逐条判定是否过度归因。",
    )
    make_package(
        "GPTPRO_WEB_BATCH_D_选择题海西东朝.md",
        "GPT Pro 网页版审核包 D：海西东朝选择题",
        choice_priority,
        "重点：选择题不能按主观题给分点处理；请判断正确项链和错肢类型。",
    )
    make_package(
        "GPTPRO_WEB_BATCH_E_选择题郊区.md",
        "GPT Pro 网页版审核包 E：郊区选择题",
        choice_other,
        "重点：选择题不能按主观题给分点处理；请判断正确项链和错肢类型。",
    )
    if new9_rows:
        make_package(
            "GPTPRO_WEB_BATCH_F_新增9套.md",
            "GPT Pro 网页版审核包 F：新增 9 套 2026 一模/二模",
            new9_rows,
            "重点：新增 9 套必须并入 65 套总验收，不得只做附录。",
        )

    manifest = [
        "# 外部模型审核包清单",
        "",
        f"- 65套 roster：{len(roster)}",
        f"- 主观质量失败待审：{len(subj)}",
        f"- 选择题未闭环待审：{len(choices)}",
        f"- 高风险原理专项：{len(highrisk)}",
        "",
    ]
    for p in sorted(OUT.glob("GPTPRO_WEB_BATCH_*.md")):
        manifest.append(f"- {p.name}: {p.stat().st_size} bytes")
    (OUT / "REVIEW_PACKAGE_MANIFEST.md").write_text("\n".join(manifest), encoding="utf-8")
    print("\n".join(manifest))


if __name__ == "__main__":
    main()
