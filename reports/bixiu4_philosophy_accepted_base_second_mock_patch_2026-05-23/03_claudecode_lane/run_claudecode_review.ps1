$lane = Split-Path -Parent $MyInvocation.MyCommand.Path
$run = Split-Path -Parent $lane
$prompt = Join-Path $lane 'CLAUDECODE_PROMPT.md'
$out = Join-Path $lane 'claudecode_review.md'
$err = Join-Path $lane 'claudecode_stderr.log'

$promptText = Get-Content -LiteralPath $prompt -Raw -Encoding UTF8
Push-Location $run
try {
  claude --print $promptText --model opus --permission-mode bypassPermissions --tools 'Read,Grep,Glob,Write' --add-dir $run > $out 2> $err
}
finally {
  Pop-Location
}
