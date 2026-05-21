#!/bin/bash
# Number Guess Hook
# PostToolUse — fires when guess.md is written.
# Creates answer.md with a random number if not present.
# Overwrites guess.md with feedback: too high, too low, or correct.

INPUT=$(cat)

FILE_PATH=$(echo "$INPUT" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path',''))" 2>/dev/null)

# Only run when guess.md is written
if [[ "$FILE_PATH" != */Number_Guess/guess.md ]]; then
  exit 0
fi

GAME_DIR="$(dirname "$FILE_PATH")"

python3 << PYEOF
import random, re, os

game_dir   = "$GAME_DIR"
answer_file = os.path.join(game_dir, "answer.md")
guess_file  = "$FILE_PATH"

# Create answer.md if it doesn't exist yet
if not os.path.exists(answer_file):
    answer = random.randint(1, 100)
    with open(answer_file, 'w') as f:
        f.write(f"{answer}\n")
else:
    with open(answer_file) as f:
        answer = int(f.read().strip())

# Read the last number in the file — that's the most recent guess
with open(guess_file) as f:
    numbers = re.findall(r'^\d+$', f.read(), re.MULTILINE)
guess = int(numbers[-1]) if numbers else None

# Append feedback
with open(guess_file, 'a') as f:
    if guess is None:
        f.write("Invalid guess. Write a number between 1 and 100 and guess again.\n")
    elif guess < answer:
        f.write(f"That guess is too low! Guess again.\n")
    elif guess > answer:
        f.write(f"That guess is too high! Guess again.\n")
    else:
        f.write(f"Congrats! You guessed the number!\n")
        os.remove(answer_file)
PYEOF

exit 0
