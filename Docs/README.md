# Number Guess Game

A demonstration of file-based state management and PostToolUse hooks for interactive gameplay.

## How It Works

The game consists of three components working together:

1. **Prompt** (`../prompt-number-guess.txt`) — Instructions for Claude to play the game
2. **Game State** (`../guess.md`) — Record of all guesses and feedback
3. **Hook Automation** (`./.hooks/number-guess-hook.sh`) — PostToolUse hook that simulates the game master

When Claude writes a guess to `guess.md`, the hook automatically:
- Generates a random secret number (on first run)
- Reads the most recent guess
- Appends feedback (too low, too high, or correct)

## Files

- `prompt-number-guess.txt` — Game instructions (read this to understand the concept)
- `guess.md` — Game state file (created when game starts, contains all guesses + feedback)
- `answer.md` — Secret number (created by hook, removed when game is won)
- `.hooks/number-guess-hook.sh` — PostToolUse hook implementation

## Key Pattern

This demonstrates the **hooks + sentinel files** pattern:
- Sentinel files (guess.md) track state
- Hooks observe file writes and generate responses
- The combination creates the illusion of interactivity without explicit polling

## Running the Game

To run: Select the prompt in `prompt-number-guess.txt` and run it. Claude will begin guessing, and the hook will provide feedback after each write.

See `docs/HOOK_EXPLANATION.md` for technical details.
