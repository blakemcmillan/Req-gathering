# Hook Implementation Details

## What Is the Hook?

A **PostToolUse hook** is a script that executes automatically after Claude writes to a file. In this case, it's triggered whenever `guess.md` is written to.

## How the Hook Works

File: `.hooks/number-guess-hook.sh`

### Step 1: Trigger Detection
The hook receives metadata about every tool execution. It checks if the file being written is `Number_Guess/guess.md`. If not, it exits early.

### Step 2: Answer Generation
On the first write:
- Hook checks if `answer.md` exists
- If not, generates a random integer between 1 and 100
- Writes it to `answer.md` (this file persists for the duration of the game)

### Step 3: Extract Latest Guess
The hook reads `guess.md` and extracts all numbers using regex `^\d+$` (one number per line).
Takes the last number as the most recent guess.

### Step 4: Generate Feedback
Compares the guess to the answer:
- If guess < answer → "That guess is too low! Guess again."
- If guess > answer → "That guess is too high! Guess again."
- If guess == answer → "Congrats! You guessed the number!" + removes `answer.md`

Appends the feedback to `guess.md` using `echo`.

## Why This Pattern?

Instead of:
- Claude polling for feedback (calling a function after each guess)
- Passing data through JSON or external services

This approach:
- Keeps all state visible in plain text files
- Uses file writes as the trigger for automation
- Makes the interaction transparent and debuggable
- Simulates two-way interaction with no explicit back-and-forth

## State Files

- `guess.md` — Game log (guesses + feedback, appended by both Claude and hook)
- `answer.md` — Secret state (created and maintained by hook)

Both are plain text, readable, and fully traceable.
