set runDir to "/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02"
set scriptPath to runDir & "/START_CLAUDECODE_FINISH_ONLY.sh"

tell application "Terminal"
  activate
  do script "cd " & quoted form of runDir & " && bash " & quoted form of scriptPath
end tell
