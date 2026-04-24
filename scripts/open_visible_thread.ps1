param(
  [ValidateSet(
    "supervisor",
    "philosophy-forward",
    "philosophy-reverse",
    "culture",
    "elective1",
    "elective2",
    "elective3"
  )]
  [string]$Role = "supervisor",

  [string]$Model = "gpt-5.4"
)

$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

$threadIds = @{
  "supervisor" = "019dbe09-cc94-73b0-9c5c-f982409d8dfd"
  "philosophy-forward" = "019db91f-5d73-78d3-afca-49bd7492a610"
  "philosophy-reverse" = "019dbe59-6286-7c60-8235-48969e2cb049"
  "culture" = "019dbe88-393f-7202-a214-cc47f5c8c75c"
  "elective1" = "019dba05-359f-7382-8229-4bac5b46b6e2"
  "elective2" = "019dba0d-267b-7a83-8ce0-94ac53aaf636"
  "elective3" = "019dba73-b9bf-7bb1-8915-f30eb7aa7eac"
}

$threadId = $threadIds[$Role]

Set-Location $repoRoot
git pull --ff-only

$codex = Get-Command codex -ErrorAction SilentlyContinue
if (-not $codex) {
  throw "Codex CLI was not found on PATH. Use RESTORE_THREADS.md to create a visible handoff thread in Codex Desktop."
}

& codex -m $Model -C $repoRoot resume --all --include-non-interactive $threadId
