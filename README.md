# Req-gathering

A structured toolkit for transforming product concepts into fully specified requirements, user stories, and test plans using reusable Claude Code skills.

## Workflow

```
Product Concept
    ↓ (requirements-gathering)
Requirements.md
    ↓ (prd-creation)
PRD.md
    ↓ (user-story-expansion)
User-Stories.md
    ↓ (test-plan)
Test-Plan.md
```

**4 sequential skills:**
1. **requirements-gathering** — Interview users to discover roles, tasks, gains, pains
2. **prd-creation** — Design features from requirements patterns
3. **user-story-expansion** — Detailed acceptance criteria & Gherkin scenarios
4. **test-plan** — Pragmatic test strategy with categorized test cases

## Skills

| Skill | Purpose | Input | Output |
|-------|---------|-------|--------|
| **requirements-gathering** | Interview users systematically | Product concept | `/output/<name>/requirements.md` |
| **prd-creation** | Design features from requirements | Requirements file | `/output/<name>/prd.md` |
| **user-story-expansion** | Detail acceptance criteria | PRD file | `/output/<name>/user-stories.md` |
| **test-plan** | Create test strategy | User stories | `/output/<name>/test-plan.md` |

**All four skills include automatic quality evaluation** that generates `-eval.html` reports on output.

---

## Quick Start

1. **Have a product idea?** Run requirements-gathering skill
2. **Have requirements?** Run prd-creation skill  
3. **Have a PRD?** Run user-story-expansion skill
4. **Ready to test?** Run test-plan skill

Each skill auto-evaluates its output and saves results as `-eval.html` in the same directory.

**Manual evaluation:**
```bash
echo "/path/to/file.md" > EVAL.txt  # Trigger evaluation of any file
```

---

## Automatic Quality Checks

All four skills include auto-running evaluators triggered on output:

| Skill Output | Evaluator | Checks | Status |
|--------------|-----------|--------|--------|
| `requirements.md` | eval-requirements.py | 14 checks (structure, roles, gains/pains) | ✅ |
| `prd.md` | eval-prd.py | 12 checks (structure, traceability, metrics) | ✅ |
| `user-stories.md` | eval-user-stories.py | 19 checks (ID format, Gherkin, AC structure) | ✅ |
| `test-plan.md` | eval-test-plan.py | 15 checks (coverage, density, traceability) | ✅ |

**How it works:**
- When a skill writes output to `/output/*/filename.md`, PostToolUse hook auto-triggers the evaluator
- Evaluator generates `filename-eval.html` report with score and feedback
- EVAL.txt is auto-deleted after evaluation completes
- No manual review needed—all checks run automatically

---

## Examples

**Habit Tracker** — Full workflow (concept → requirements → PRD → user stories → tests)
- 2 user roles, 5 tasks, comprehensive gains/pains
- 6 features solving multiple user needs elegantly
- 12 user stories with 36 detailed acceptance criteria
- 38 test cases across 5 categories

**Pomodoro Timer** — Pragmatic approach to test planning
- 7 features with 32 user stories
- 33 test cases (selective categories—no unnecessary tests)
- Demonstrates lean testing: performance tests only where needed

**iPhone Flashlight** — Minimal feature, comprehensive testing
- 1 core feature (LED toggle) with 8 acceptance criteria  
- 27 test cases showing that simplicity requires rigor
- Permission handling, device constraints, battery efficiency, accessibility

---

## How to Use This Toolkit

**Core principle:** Sequential handoff adds specificity at each phase
- **Discovery** → What do users need?
- **PRD** → What features solve these needs?
- **User Stories** → How do features behave?
- **Test Plan** → How do we verify everything works?

**Don't skip steps.** Skipping discovery loses user voice. Skipping PRD creates feature sprawl. Skipping user stories loses acceptance criteria. Skipping test plan ships bugs.

**Do adapt to context.** Use Habit Tracker as a detailed example. Use Pomodoro to see pragmatic, not exhaustive, test planning. Use iPhone Flashlight to challenge the assumption that "minimal = simple."

---

## Project Structure

```
.
├── README.md
├── .claude/
│   ├── settings.json          (PostToolUse hooks)
│   └── skills/
│       ├── requirements-gathering/SKILL.md
│       ├── prd-creation/SKILL.md + eval-prd.py
│       ├── user-story-expansion/SKILL.md
│       └── test-plan/SKILL.md + eval-test-plan.py
└── output/
    ├── habit-tracker/         (full workflow example)
    ├── pomodoro/              (pragmatic test planning)
    └── iphone-flashlight/     (minimal feature example)
```

---

## Getting Started

1. **Have a product idea?** → Run `/requirements-gathering`
2. **Have a requirements doc?** → Run `/prd-creation`
3. **Have a PRD?** → Run `/user-story-expansion`
4. **Ready to test?** → Run `/test-plan`

Each skill saves output to `/output/<product_name>/` and auto-evaluates the results.

**Questions?** See Examples section above or review the three worked examples in `/output/`.

## License

This toolkit is open source. Use, modify, and share freely.

---

---

## Recent Improvements

**May 21, 2026:**
- **Automatic Evaluation Hooks:** Enhanced PostToolUse configuration with EVAL.txt manual trigger support
  - PRD and test-plan evaluators auto-run on file write
  - Manual trigger via `echo "path/to/file.md" > EVAL.txt` for on-demand evaluation
  - Both evaluators auto-delete EVAL.txt after completion
- **iPhone Flashlight Example:** Real-world minimalist iOS app example
  - Single-feature (LED toggle) demonstrates comprehensive testing at any scale
  - 27 test cases across unit, integration, E2E, edge case, and performance categories
  - Shows permission handling, device constraints (iPad), battery efficiency, accessibility (WCAG AA)
- **Pragmatic Test Planning:** Refactored test-plan skill to be context-aware, not prescriptive
  - Selective test categories (include only what applies)
  - Concise traceability matrices (5-10 rows, not exhaustive)
  - Flexible test density (1-5 per requirement, not fixed ratios)
  - Brief test case format (3-7 line Gherkin, fits on one screen)
- **PRD Quality Evaluator:** Added auto-running quality checks on PRD output
  - Validates against SKILL.md structure (not generic sections)
  - Checks feature traceability ("Solves For" sections present)
  - Verifies explicit non-goals and quantified success metrics
  - PostToolUse hook triggers automatically on PRD write
- **Pomodoro Example:** Comprehensive specification for focus/timer app (32 stories, pragmatic test plan)

---

**Last Updated:** May 21, 2026
