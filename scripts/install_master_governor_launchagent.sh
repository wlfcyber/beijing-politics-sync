#!/usr/bin/env bash
set -euo pipefail

LABEL="com.wanglifei.beijing-politics-master-governor"
SYNC_ROOT="${SYNC_ROOT:-/Users/wanglifei/GaokaoPolitics/beijing-politics-sync}"
SRC="$SYNC_ROOT/reports/master_governor/$LABEL.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

mkdir -p "$HOME/Library/LaunchAgents"
cp "$SRC" "$DEST"
plutil -lint "$DEST"

UID_VALUE="$(id -u)"
launchctl bootout "gui/$UID_VALUE" "$DEST" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$UID_VALUE" "$DEST"
launchctl print "gui/$UID_VALUE/$LABEL" >/dev/null

echo "installed $DEST"
echo "schedule: daily 07:30 local time"
