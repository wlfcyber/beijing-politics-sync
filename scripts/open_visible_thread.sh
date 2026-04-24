#!/usr/bin/env bash
set -euo pipefail

role="${1:-supervisor}"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
codex_model="${CODEX_MODEL:-gpt-5.4}"

case "$role" in
  supervisor)
    thread_id="019dbe09-cc94-73b0-9c5c-f982409d8dfd"
    ;;
  philosophy-forward)
    thread_id="019db91f-5d73-78d3-afca-49bd7492a610"
    ;;
  philosophy-reverse)
    thread_id="019dbe59-6286-7c60-8235-48969e2cb049"
    ;;
  culture)
    thread_id="019dbe88-393f-7202-a214-cc47f5c8c75c"
    ;;
  elective1)
    thread_id="019dba05-359f-7382-8229-4bac5b46b6e2"
    ;;
  elective2)
    thread_id="019dba0d-267b-7a83-8ce0-94ac53aaf636"
    ;;
  elective3)
    thread_id="019dba73-b9bf-7bb1-8915-f30eb7aa7eac"
    ;;
  *)
    cat >&2 <<'USAGE'
Usage:
  ./scripts/open_visible_thread.sh supervisor
  ./scripts/open_visible_thread.sh philosophy-forward
  ./scripts/open_visible_thread.sh philosophy-reverse
  ./scripts/open_visible_thread.sh culture
  ./scripts/open_visible_thread.sh elective1
  ./scripts/open_visible_thread.sh elective2
  ./scripts/open_visible_thread.sh elective3
USAGE
    exit 2
    ;;
esac

cd "$repo_root"
git pull --ff-only

exec codex -m "$codex_model" -C "$repo_root" resume --all --include-non-interactive "$thread_id"
