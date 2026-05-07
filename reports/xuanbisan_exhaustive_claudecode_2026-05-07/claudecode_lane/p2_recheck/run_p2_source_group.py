# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[2]
TASK_DIR = RUN_DIR / "claudecode_lane" / "p2_recheck"


def build_prompt(prefix: str, expected: str, source_ids: list[str]) -> str:
    source_block = "\n".join(f"  - `{sid}`" for sid in source_ids)
    return f"""# ClaudeCode {prefix} P2 Source Group Recheck

You are the real ClaudeCode CLI. This is a small source_id-level P2 run after
larger P2 runs stalled without file output.

Use relative paths from the current working directory. Do not write Word, PDF,
delivery, or final artifacts.

Inputs:

- `fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv`
- `fusion/p2_recheck_sources/P2_SOURCE_TEXT_INDEX.csv`
- `fusion/p2_recheck_sources/`
- `fusion/framework_first_fusion/FRAMEWORK_FIRST_FUSION_P1_PATCHED.md`

Write outputs only under `claudecode_lane/p2_recheck/`.

Required output files:

1. `{prefix}_RECHECK_DECISIONS.csv`
2. `{prefix}_RECHECK_PATCHES.jsonl`
3. `{prefix}_SOURCE_EVIDENCE.md`
4. `{prefix}_RECHECK_ACCEPTANCE.md`
5. `{prefix}_PROGRESS.md`

Scope:

- Filter manifest rows to `priority=P2`.
- Include only these source_id values:
{source_block}
- There must be exactly {expected} decision rows.
- Do not add any other P2 rows.

CSV header:

`priority,question_id,parent_question_id,source_batch,type,framework_node,evidence_level,decision,decision_reason,source_evidence,patch_needed,can_enter_fusion`

Allowed decisions:

- `confirmed`
- `confirmed_with_patch`
- `downgrade_to_index`
- `source_insufficient`
- `wrong_framework`
- `block_from_student_body`

JSONL fields:

`question_id,parent_question_id,framework_node,decision,patched_material_signal,patched_trigger_logic,patched_answer_sentence,source_evidence,notes`

Rules:

- Verify stem/options and answer key before confirming choice-trap rows.
- Use the manifest evidence_level exactly unless the source genuinely proves the
  row is misclassified; explain any exception.
- Do not invent options, answers, rubrics, or source files.
- If answer evidence is unavailable, mark `source_insufficient` and
  `can_enter_fusion=no`.
- Acceptance must state `{prefix}_RECHECK_ACCEPTANCE: NOT_FINAL`, exact row
  count {expected}, patch count {expected}, no Word/PDF/delivery.

Begin by writing `{prefix}_RECHECK_DECISIONS.csv`.
"""


def main() -> int:
    if len(sys.argv) < 4:
        raise SystemExit("usage: run_p2_source_group.py PREFIX EXPECTED SOURCE_ID [SOURCE_ID...]")
    prefix = sys.argv[1].upper()
    expected = sys.argv[2]
    source_ids = sys.argv[3:]
    prompt_path = TASK_DIR / f"CLAUDECODE_{prefix}_PROMPT.md"
    stdout = TASK_DIR / f"claudecode_{prefix.lower()}_stdout.log"
    stderr = TASK_DIR / f"claudecode_{prefix.lower()}_stderr.log"
    ret = TASK_DIR / f"claudecode_{prefix.lower()}_return_code.txt"
    prompt = build_prompt(prefix, expected, source_ids)
    prompt_path.write_text(prompt, encoding="utf-8")

    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    cmd = [
        "claude",
        "-p",
        prompt,
        "--model",
        "opus",
        "--permission-mode",
        "auto",
        "--effort",
        "max",
        "--add-dir",
        str(RUN_DIR),
        str(Path.home() / ".codex" / "skills"),
    ]
    with stdout.open("w", encoding="utf-8", errors="replace") as out, stderr.open(
        "w", encoding="utf-8", errors="replace"
    ) as err:
        out.write(f"started={datetime.now().isoformat(timespec='seconds')}\n")
        out.flush()
        code = subprocess.run(cmd, cwd=str(RUN_DIR), stdout=out, stderr=err, text=True, env=env).returncode
    ret.write_text(str(code), encoding="utf-8")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
