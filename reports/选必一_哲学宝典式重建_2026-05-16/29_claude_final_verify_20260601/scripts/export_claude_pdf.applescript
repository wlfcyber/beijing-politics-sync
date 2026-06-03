set inputPath to POSIX file "/Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/2c0a1a14-78ce-4ddc-8f72-9d4f74dbff6e/703c2d6a-ade6-4ee8-94a4-92b2abb47bf1/local_ea19f1a6-c672-4010-9aa6-235ad1631aa4/outputs/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.docx"
set outputPath to "/Users/wanglifei/Desktop/Claude_final_20260601_render_check.pdf"

tell application "Microsoft Word"
	open inputPath
	do Visual Basic "ActiveDocument.ExportAsFixedFormat OutputFileName:=" & quote & outputPath & quote & ", ExportFormat:=17"
	close active document saving no
end tell
