from __future__ import annotations

import shutil
import zipfile
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
DOCX = next((RUN_DIR / "05_delivery").glob("*.docx"))

REPLACEMENTS = {
    "②强化红色文化引领、厚植爱国情怀——属于《哲学与文化》文化部分，本轮按文化边界不单立条目。": (
        "②强化红色文化引领、厚植爱国情怀——这是文化角度的正确认识；"
        "放在本条下时，哲学重点主要看③“联系多样性”。"
    ),
    "①汉字以其巧妙构造承载文化价值观念——属于《哲学与文化》文化部分，本轮按文化边界不单立条目。": (
        "①汉字以其巧妙构造承载文化价值观念——这是文化角度的正确认识；"
        "放在本条下时，哲学重点主要看②“智慧与道德具有内在一致性”。"
    ),
}


def main() -> None:
    backup = DOCX.with_name(DOCX.stem + "_backup_before_audit_language_cleanup.docx")
    if not backup.exists():
        shutil.copy2(DOCX, backup)

    tmp = DOCX.with_suffix(".tmp.docx")
    replacements_done = 0
    with zipfile.ZipFile(DOCX, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                text = data.decode("utf-8")
                for old, new in REPLACEMENTS.items():
                    count = text.count(old)
                    replacements_done += count
                    text = text.replace(old, new)
                data = text.encode("utf-8")
            zout.writestr(item, data)

    tmp.replace(DOCX)
    print(f"cleaned={replacements_done}")
    print(DOCX)


if __name__ == "__main__":
    main()
