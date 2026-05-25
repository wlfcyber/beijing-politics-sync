from __future__ import annotations

import csv
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY_DIR = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
MATRIX = RECOVERY_DIR / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"

K_ID = "matrix_row_id"
K_IN = "\u662f\u5426\u8fdb\u5b9d\u5178"
K_NODE = "\u5b9d\u5178\u8282\u70b9"
K_PRINCIPLE = "\u7ec6\u5219\u652f\u6301\u539f\u7406"
K_EVIDENCE = "\u8bc1\u636e\u7b49\u7ea7"
K_MISPLACED = "\u662f\u5426\u8bef\u653e"
K_NEED = "\u662f\u5426\u9700\u8865\u539a"
K_ACTION = "\u5f53\u524d\u5904\u7406"
K_NOTE = "\u5907\u6ce8"


UPDATES = {
    "M0239": {
        K_IN: "\u662f\uff1a\u5df2\u5728\u6700\u7ec8DOCX\u8986\u76d6\uff08\u65e0\u9700\u65b0\u589e\uff09",
        K_NODE: "\u77db\u76fe\u5c31\u662f\u5bf9\u7acb\u7edf\u4e00\uff1b\u8fa9\u8bc1\u5426\u5b9a / \u5b88\u6b63\u521b\u65b0\uff1b\u77db\u76fe\u7684\u7279\u6b8a\u6027 / \u5177\u4f53\u95ee\u9898\u5177\u4f53\u5206\u6790\uff1b\u4ef7\u503c\u89c2\u7684\u5bfc\u5411\u4f5c\u7528",
        K_PRINCIPLE: "2026\u671d\u9633\u4e8c\u6a21\u7b2c16\u9898\u8bc4\u5206\u6807\u51c6\uff1a\u56f4\u7ed5\u201c\u5982\u4f55\u4f20\u627f\u201d\u3001\u201c\u5982\u4f55\u521b\u65b0\u201d\u3001\u201c\u8fa9\u8bc1\u5904\u7406\u4f20\u627f\u4e0e\u521b\u65b0\u5173\u7cfb\u201d\u3001\u201c\u793e\u4f1a\u4e3b\u4e49\u6838\u5fc3\u4ef7\u503c\u89c2\u201d\u56db\u4e2a\u7ef4\u5ea6\uff0c\u660e\u786e\u652f\u6301\u5bf9\u7acb\u7edf\u4e00\u3001\u8fa9\u8bc1\u5426\u5b9a/\u5b88\u6b63\u521b\u65b0\u3001\u5177\u4f53\u95ee\u9898\u5177\u4f53\u5206\u6790\u548c\u4ef7\u503c\u89c2\u5bfc\u5411\u4f5c\u7528\uff1bsource bundle lines 123-148, 505-524.",
        K_EVIDENCE: "\u5f3a\u7ec6\u5219",
        K_MISPLACED: "\u5426",
        K_NEED: "\u5426",
        K_ACTION: "Batch03\u56de\u6e90\u95ed\u5408\uff1aQ16\u5df2\u7531\u6700\u7ec8DOCX\u65e2\u6709\u6761\u76ee\u8986\u76d6\uff0c\u4e0d\u91cd\u590d\u65b0\u589e\u3002",
        K_NOTE: "2026\u671d\u9633\u4e8c\u6a21\u57ce\u5e02\u6587\u5316\u5efa\u8bbe\u4e3b\u89c2\u9898\uff1bBatch03\u6838\u5b9a\u4e3a\u5df2\u5165\u6b63\u6587\u8986\u76d6\u3002",
    },
    "M0240": {
        K_IN: "\u662f\uff1a\u5df2\u5728\u6700\u7ec8DOCX\u8986\u76d6\uff08\u65e0\u9700\u65b0\u589e\uff09",
        K_NODE: "\u7cfb\u7edf\u89c2\u5ff5 / \u7cfb\u7edf\u4f18\u5316\uff1b\u91cf\u53d8\u4e0e\u8d28\u53d8 / \u9002\u5ea6\u539f\u5219",
        K_PRINCIPLE: "2026\u671d\u9633\u4e8c\u6a21\u7b2c21\u9898\u8bc4\u5206\u7ec6\u5219\uff1a\u201c\u7cfb\u7edf\u89c2\u5ff5\u201d\u660e\u786e\u542b\u6574\u4f53\u6027\u3001\u5173\u8054\u6027\u3001\u534f\u540c\u6027\uff0c\u5e76\u8981\u4ee5\u666e\u904d\u8054\u7cfb\u3001\u5168\u9762\u89c6\u89d2\u7edf\u7b79\u63a8\u8fdb\uff1b\u201c\u6218\u7565\u6301\u4e45\u201d\u660e\u786e\u542b\u65b9\u5411\u575a\u5b9a\u3001\u4e45\u4e45\u4e3a\u529f\u4e0e\u91cf\u53d8\u8d28\u53d8\u3002source bundle lines 106-122, 424-440.",
        K_EVIDENCE: "\u5f3a\u7ec6\u5219",
        K_MISPLACED: "\u5426",
        K_NEED: "\u5426",
        K_ACTION: "Batch03\u56de\u6e90\u95ed\u5408\uff1aQ21\u5df2\u7531\u6700\u7ec8DOCX\u65e2\u6709\u6761\u76ee\u8986\u76d6\uff0c\u515a\u7684\u9886\u5bfc/\u4e60\u8fd1\u5e73\u65b0\u65f6\u4ee3\u4e2d\u56fd\u7279\u8272\u793e\u4f1a\u4e3b\u4e49\u601d\u60f3\u4fdd\u6301\u653f\u6cbb\u6a21\u5757\u8fb9\u754c\u6392\u9664\u3002",
        K_NOTE: "2026\u671d\u9633\u4e8c\u6a21\u4e94\u7bc7\u5927\u6587\u7ae0\u4e3b\u89c2\u9898\uff1bBatch03\u6838\u5b9a\u4e3a\u5df2\u5165\u6b63\u6587\u8986\u76d6\u3002",
    },
}


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = RECOVERY_DIR / (
        "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX_backup_before_"
        f"batch03_chaoyang_pending_cleanup_{timestamp}.csv"
    )
    shutil.copy2(MATRIX, backup)

    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise RuntimeError("matrix has no header")
        rows = list(reader)

    touched = []
    for row in rows:
        row_id = row.get(K_ID)
        if row_id in UPDATES:
            row.update(UPDATES[row_id])
            touched.append(row_id)

    missing = sorted(set(UPDATES) - set(touched))
    if missing:
        raise RuntimeError(f"missing rows: {missing}")

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"backup={backup}")
    print(f"touched={','.join(touched)}")


if __name__ == "__main__":
    main()
