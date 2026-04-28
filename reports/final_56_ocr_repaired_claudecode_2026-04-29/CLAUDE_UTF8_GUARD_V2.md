# UTF-8 guard for this Windows run

Critical correction before executing the task below:

1. Do not use ClaudeCode's built-in `Read` tool for Chinese UTF-8 project files in this Windows session. It decodes UTF-8 as the system default encoding and turns Chinese into mojibake such as `鍚`, `瀛`, `涓`, `鎶`, `锛?`.
2. Read Chinese text files through PowerShell or Python with explicit UTF-8:
   - PowerShell pattern:
     `$OutputEncoding = [System.Text.UTF8Encoding]::new(); [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new(); Get-Content -Encoding UTF8 -Raw -Path "PATH"`
   - Python pattern:
     `Path("PATH").read_text(encoding="utf-8", errors="replace")`
3. Prefer writing a Python builder script in the run directory and executing it. The script must read all inputs with `encoding="utf-8-sig"` or `encoding="utf-8"` and write outputs with `encoding="utf-8"`.
4. If you need to inspect a snippet in the model context, print it from PowerShell/Python after forcing UTF-8 output. Do not inspect Chinese through `Read`.
5. Before finishing, scan student-facing files for both engineering residues and mojibake residues:
   - engineering: `C:\\|source_path|hash|sha256|page_|OCR|debug|visible_runs|crops_|F\d{2}|L\d{2}|slide|pdf|pptx|docx|\.jsonl`
   - mojibake: `鍚|瀛|涓|鎶|锛\?|绛旀|璁鹃|鏉愭|鐭ヨ|摬瀛|鏈濋|娴锋|涓滃`
6. If any student-facing file contains mojibake residues, regenerate it from UTF-8 inputs before creating DOCX.
7. The previous v1 process was stopped only because of the encoding defect. Restart the same 56-suite OCR-repaired final-document task; do not narrow the task or skip any repair queue item.

