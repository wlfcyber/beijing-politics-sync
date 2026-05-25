# -*- coding: utf-8 -*-
from __future__ import annotations

import json
import shutil
import zipfile
from datetime import datetime
from pathlib import Path


def find_project_root() -> Path:
    desktop = Path.home() / "Desktop"
    for candidate in desktop.glob("02_*"):
        root = candidate / "mac-thread-restore" / "beijing-politics-sync-visible"
        if root.exists():
            return root
    raise FileNotFoundError("beijing-politics-sync-visible project root not found")


PROJECT = find_project_root()
RUN = PROJECT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
RECOVERY = PROJECT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
DOCX = RUN / "05_delivery" / "哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx"
ACCEPTED = RUN / "04_fusion_audit" / "student_patch_entries.accepted.jsonl"

REPLACEMENTS = {
    "本题评标允许从联系、矛盾、实践与认识等角度任选展开，本条是一条可选答题路径，不代表三项累计得分。联系具有普遍性。": (
        "这道题可以从联系、矛盾、实践与认识等不同哲学路径切入。这里按联系观点展开，学生作答时选定这一条路径说透即可，不需要把多个路径机械叠加。联系具有普遍性。"
    ),
    "本题评标允许从联系、矛盾、实践与认识等角度任选展开，本条是一条可选答题路径，不代表三项累计得分。良法和善治有区别：": (
        "这道题可以从联系、矛盾、实践与认识等不同哲学路径切入。这里按矛盾观点展开，学生作答时选定这一条路径说透即可，不需要把多个路径机械叠加。良法和善治有区别："
    ),
    "本题评标允许从联系、矛盾、实践与认识等角度任选展开，本条是一条可选答题路径，不代表三项累计得分。良法来自治理实践中的问题，": (
        "这道题可以从联系、矛盾、实践与认识等不同哲学路径切入。这里按实践与认识的思路展开，学生作答时选定这一条路径说透即可，不需要把多个路径机械叠加。良法来自治理实践中的问题，"
    ),
    "辩证否定的实质是扬弃，既肯定和保留旧事物中的合理内容，又克服旧形态局限、推动发展；评标细则明确“辩证否定观”按观点加阐述给2分，并允许用发展观替代。这正对应辩证否定的逻辑：": (
        "辩证否定的实质是扬弃，既肯定和保留旧事物中的合理内容，又克服旧形态局限、推动发展；隆福寺街区改造把保留历史记忆和注入时代元素放在同一过程中推进，正对应辩证否定的逻辑："
    ),
    "设问直接把“古朴”与“创新”作为一对关系来问，材料也不是让学生二选一，而是要求说明二者怎样在同一街区改造中相互支撑、共生共荣；评标细则明确“矛盾对立统一”按观点加阐述给2分。这说明题目不是让学生二选一，": (
        "设问直接把“古朴”与“创新”作为一对关系来问，材料也不是让学生二选一，而是要求说明二者怎样在同一街区改造中相互支撑、共生共荣。这说明题目不是让学生二选一，"
    ),
    "评标材料列出实践观点；新大众文艺的生命力来自人民群众的真实生活实践，实践为文艺认识和表达提供源泉。": (
        "新大众文艺的生命力来自人民群众的真实生活实践，实践为文艺认识和表达提供源泉。"
    ),
}


def backup(path: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = path.with_name(f"{path.stem}_backup_before_student_pingbiao_cleanup_{stamp}{path.suffix}")
    shutil.copy2(path, out)
    return out


def patch_accepted_jsonl() -> int:
    backup(ACCEPTED)
    changed = 0
    rows: list[str] = []
    for line in ACCEPTED.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            rows.append(line)
            continue
        item = json.loads(line)
        for field in ("material_trigger", "question_prompt", "why_trigger", "answer_landing"):
            text = item.get(field)
            if not isinstance(text, str):
                continue
            for old, new in REPLACEMENTS.items():
                count = text.count(old)
                if count:
                    changed += count
                    text = text.replace(old, new)
            item[field] = text
        rows.append(json.dumps(item, ensure_ascii=False))
    ACCEPTED.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return changed


def patch_docx() -> int:
    backup(DOCX)
    tmp = DOCX.with_suffix(".tmp.docx")
    changed = 0
    with zipfile.ZipFile(DOCX, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == "word/document.xml":
                text = data.decode("utf-8")
                for old, new in REPLACEMENTS.items():
                    count = text.count(old)
                    if count:
                        changed += count
                        text = text.replace(old, new)
                data = text.encode("utf-8")
            zout.writestr(info, data)
    tmp.replace(DOCX)
    return changed


def main() -> int:
    json_changes = patch_accepted_jsonl()
    docx_changes = patch_docx()
    report = RECOVERY / "PINGBIAO_RESIDUE_CLEANUP_20260524.md"
    report.write_text(
        "\n".join(
            [
                "# PINGBIAO_RESIDUE_CLEANUP_20260524",
                "",
                "Status: `PATCH_APPLIED_RENDER_REQUIRED`",
                "",
                f"- accepted JSONL student-facing replacements: {json_changes}",
                f"- DOCX body replacements: {docx_changes}",
                "- Scope: only student-facing wording was changed; evidence/boundary records were not promoted to PASS.",
                "- Next: rerender DOCX/PDF and rerun residue scan.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"accepted_jsonl_replacements={json_changes}")
    print(f"docx_replacements={docx_changes}")
    print(report)
    return 0 if json_changes == 6 and docx_changes == 6 else 2


if __name__ == "__main__":
    raise SystemExit(main())
