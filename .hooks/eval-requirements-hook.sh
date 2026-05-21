#!/bin/bash
# Requirements Evaluation Hook
# PostToolUse — fires when requirements.md is written or edited in output/ folder
# Automatically evaluates requirements quality and generates eval-requirements.md

INPUT=$(cat)

# Extract file path from tool use metadata
FILE_PATH=$(echo "$INPUT" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path',''))" 2>/dev/null)

# Only run if file is in output/ folder and named requirements.md
if [[ ! "$FILE_PATH" =~ /output/.*/requirements\.md$ ]]; then
  exit 0
fi

# Locate eval-requirements.py script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EVAL_SCRIPT="$SCRIPT_DIR/.claude/skills/requirements-gathering/eval-requirements.py"

# Check if script exists
if [ ! -f "$EVAL_SCRIPT" ]; then
  echo "Warning: eval-requirements.py not found" >&2
  exit 0
fi

# Run evaluation
python3 "$EVAL_SCRIPT" "$FILE_PATH" 2>&1

exit 0
