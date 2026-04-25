$ErrorActionPreference = 'Continue'
$desktop = [Environment]::GetFolderPath('Desktop')
$started = Get-Date
$log = Join-Path $desktop 'claude_safety_watchdog.log'
$runPattern = 'philosophy_rerun_claudecode_2026-04-25_2230'
$packagePattern = 'claudecode_philosophy_rerun_package'
$maxMinutes = 180

function Write-Log {
  param([string]$Message)
  $line = '{0} {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Message
  Add-Content -LiteralPath $log -Value $line -Encoding UTF8
}

function Get-ClaudeTree {
  $all = Get-CimInstance Win32_Process
  $claude = @($all | Where-Object { $_.Name -ieq 'claude.exe' })
  $ids = New-Object System.Collections.Generic.HashSet[int]
  foreach ($p in $claude) { [void]$ids.Add([int]$p.ProcessId) }

  $changed = $true
  while ($changed) {
    $changed = $false
    foreach ($p in $all) {
      if ($ids.Contains([int]$p.ParentProcessId) -and -not $ids.Contains([int]$p.ProcessId)) {
        [void]$ids.Add([int]$p.ProcessId)
        $changed = $true
      }
    }
  }

  $all | Where-Object { $ids.Contains([int]$_.ProcessId) }
}

function Stop-ClaudeTree {
  param([string]$Reason)
  Write-Log "ALERT: $Reason"
  $tree = @(Get-ClaudeTree)
  foreach ($p in ($tree | Sort-Object ProcessId -Descending)) {
    try {
      Write-Log ("Stopping PID={0} Name={1} Cmd={2}" -f $p.ProcessId, $p.Name, $p.CommandLine)
      Stop-Process -Id $p.ProcessId -Force -ErrorAction Stop
    } catch {
      Write-Log ("Stop failed PID={0}: {1}" -f $p.ProcessId, $_.Exception.Message)
    }
  }
}

function Is-DangerousCommand {
  param([string]$CommandLine)
  if ([string]::IsNullOrWhiteSpace($CommandLine)) { return $false }
  $patterns = @(
    'Remove-Item\b.*\b-Recurse\b',
    '\brm\s+-rf\b',
    '\brmdir\b',
    '\bdel\s+',
    '\berase\s+',
    '\bMove-Item\b',
    '\bgit\s+reset\s+--hard\b',
    '\bgit\s+clean\b',
    '\brobocopy\b.*\s/MIR\b',
    '\bformat\b',
    '\btakeown\b',
    '\bicacls\b',
    '\bschtasks\b',
    '\breg\s+(delete|add)\b'
  )
  foreach ($pattern in $patterns) {
    if ($CommandLine -match $pattern) { return $true }
  }
  return $false
}

function Get-SensitiveRoots {
  $roots = New-Object System.Collections.Generic.List[string]
  Get-ChildItem -LiteralPath $desktop -Directory -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.Name -match '^202[456]' -or $_.Name -eq 'beijing_politics_research' -or $_.Name -eq '02_代码项目与工具') {
      $roots.Add($_.FullName)
    }
  }
  $roots
}

function Path-IsAllowedClaudeOutput {
  param([string]$Path)
  if ($Path -like "*$runPattern*") { return $true }
  if ($Path -like "*$packagePattern*") { return $true }
  if ($Path -like '*ClaudeCode*') { return $true }
  return $false
}

Write-Log "Watchdog started. start=$started"

while (((Get-Date) - $started).TotalMinutes -lt $maxMinutes) {
  $tree = @(Get-ClaudeTree)
  $claude = @($tree | Where-Object { $_.Name -ieq 'claude.exe' })
  if ($claude.Count -eq 0) {
    Write-Log 'Claude processes exited; watchdog stopping.'
    break
  }

  foreach ($p in $tree) {
    if (Is-DangerousCommand $p.CommandLine) {
      Stop-ClaudeTree ("dangerous command in PID={0}: {1}" -f $p.ProcessId, $p.CommandLine)
      exit 2
    }
  }

  foreach ($root in Get-SensitiveRoots) {
    Get-ChildItem -LiteralPath $root -Recurse -File -ErrorAction SilentlyContinue |
      Where-Object { $_.LastWriteTime -gt $started } |
      Select-Object -First 5 |
      ForEach-Object {
        if (-not (Path-IsAllowedClaudeOutput $_.FullName)) {
          Stop-ClaudeTree ("write inside sensitive root: {0}" -f $_.FullName)
          exit 3
        }
      }
  }

  Start-Sleep -Seconds 10
}

Write-Log 'Watchdog finished without alert.'
