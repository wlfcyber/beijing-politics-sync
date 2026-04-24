# GitHub Sync

## Recommendation

GitHub is the best default solution for this project if used as a versioned research repository, not as a raw-file dump.

Use a private GitHub repository for:

- the skill folder;
- cumulative Markdown artifacts;
- governor board;
- extracted text that is small enough to diff;
- helper scripts;
- progress logs.

Do not put large raw corpora into normal Git:

- raw PDFs;
- scanned papers;
- zip archives;
- OCR page images;
- large PPTX files.

For large raw sources, choose one:

1. Git LFS in the same private repo if you want everything under GitHub.
2. iCloud Drive / OneDrive / external SSD for raw files, with stable local paths.
3. A separate private `source-corpus` repo with Git LFS, while the main repo stores only artifacts and references.

## Suggested Repository Layout

```text
beijing-politics-sync/
  skills/
    beijing-gaokao-politics-rubric/
  artifacts/
    必修四哲学材料-知识触发总框架_持续更新版_v2.md
    北京高考政治错肢库_持续更新版.md
  reports/
    governor_board.md
  extracted_text/
    2025_ermo/
    2026_yimo/
  scripts/
    sync_artifacts.py
  .gitignore
```

Suggested `.gitignore`:

```gitignore
# raw large source files
*.zip
*.pdf
*.pptx
*.doc
*.docx
*.png
*.jpg
*.jpeg

# allow skill docs and lightweight artifacts
!skills/**/*.md
!skills/**/*.py
!artifacts/**/*.md
!reports/**/*.md
!extracted_text/**/*.txt

# local caches
.DS_Store
__pycache__/
.venv/
```

If using Git LFS for raw files:

```bash
git lfs install
git lfs track "*.pdf" "*.pptx" "*.doc" "*.docx" "*.zip" "*.png" "*.jpg"
git add .gitattributes
```

## Windows Setup

From PowerShell:

```powershell
cd C:\Users\Administrator\Desktop
mkdir beijing-politics-sync
cd beijing-politics-sync
git init
mkdir skills artifacts reports scripts extracted_text
Copy-Item -Recurse C:\Users\Administrator\Desktop\codex-thread-transfer\beijing-gaokao-politics-rubric .\skills\
Copy-Item C:\Users\Administrator\Desktop\必修四哲学材料-知识触发总框架_持续更新版_v2.md .\artifacts\
Copy-Item C:\Users\Administrator\Desktop\北京高考政治错肢库_持续更新版.md .\artifacts\
Copy-Item C:\Users\Administrator\Desktop\beijing_politics_research\data\reports\governor_board.md .\reports\
git add .
git commit -m "Initialize Beijing politics rubric sync"
git branch -M main
git remote add origin git@github.com:YOUR_ACCOUNT/beijing-politics-sync.git
git push -u origin main
```

Use HTTPS instead of SSH if preferred:

```powershell
git remote add origin https://github.com/YOUR_ACCOUNT/beijing-politics-sync.git
```

## Mac Setup

```bash
mkdir -p ~/GaokaoPolitics
cd ~/GaokaoPolitics
git clone git@github.com:YOUR_ACCOUNT/beijing-politics-sync.git
mkdir -p ~/.codex/skills
cp -R beijing-politics-sync/skills/beijing-gaokao-politics-rubric ~/.codex/skills/
```

Put raw source corpora somewhere stable, for example:

```bash
mkdir -p ~/GaokaoPolitics/source
```

Then copy or sync:

- `2025各区模拟题`
- `2026各区模拟题`
- `哲学与文化  2026班课.pdf`

## Daily Switching Protocol

Before switching computers:

```bash
git status
git add artifacts reports extracted_text skills
git commit -m "Update rubric framework and governor board"
git push
```

After switching computers:

```bash
git pull
cp -R beijing-politics-sync/skills/beijing-gaokao-politics-rubric ~/.codex/skills/
```

Then start Codex and say:

```text
Use the beijing-gaokao-politics-rubric skill. Continue from references/current-state.md and the synced artifacts.
```

For a full handoff on a new computer, paste the prompt in:

- `skills/beijing-gaokao-politics-rubric/references/new-computer-absorb-prompt.md`

That prompt makes the new Codex session read the project skill, operating rules, continuous-task controller, current state, GitHub sync rules, and governor board before it resumes work.

## Conflict Rules

If both devices edited the same Markdown file:

1. Open the conflict markers.
2. Preserve all valid entries.
3. Prefer later governor-approved entries when duplicate.
4. Do not delete a source-labeled trigger or wrong-option entry unless it is explicitly marked as wrong.
5. Re-run governor checks after resolving.

## Why GitHub Is Better Than Plain Cloud Drive

GitHub gives:

- version history;
- diffs for Markdown;
- rollback after mistakes;
- branches for experimental reorganization;
- clear commit messages for each research round;
- safe review before merging device changes.

Cloud drive is still useful for raw scans and huge files, but it is weaker for versioning the teaching framework itself.
