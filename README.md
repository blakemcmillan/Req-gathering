# Req-gathering

A structured toolkit for requirements discovery, PRD creation, and test planning. Provides reusable Claude Code skills that guide teams through product definition workflows.

## Overview

Req-gathering implements a **sequential skill-based workflow** for transforming product concepts into fully specified requirements, user stories, and test plans. Each skill is self-contained, repeatable, and designed to work with any product domain.

### Workflow

```
Concept → Requirements Discovery → PRD Creation → User Story Detail → Test Planning
```

1. **Requirements Discovery** — Structured user interview to uncover roles, tasks, gains, and pains
2. **PRD Creation** — Pattern recognition across needs; design features that solve multiple problems
3. **User Story Expansion** — Detailed acceptance criteria, data models, edge cases
4. **Test Planning** — Comprehensive test strategy with categorized test cases and traceability

## Skills

### 1. requirements-gathering

**Purpose:** Interactively discover user needs through structured conversation.

**When to use:** When you have a product concept and want to understand who will use it and what problems they're trying to solve.

**Inputs:**
- Product name or concept description

**Outputs:**
- `/output/<product_name>/requirements.md` — Discovered user roles, tasks, gains, and pains

**How it works:**
- Identifies user roles (e.g., "Workout Newbie", "Gym Rat")
- For each role, discovers tasks they want to accomplish
- For each task, captures success criteria, gains, and pains
- Organizes findings in a Value Prop Canvas format

---

### 2. prd-creation

**Purpose:** Generate a production-ready PRD from discovered requirements.

**When to use:** After running requirements-gathering, or if you already have a requirements document.

**Inputs:**
- Path to requirements file (e.g., `/output/habit-tracker/requirements.md`)

**Outputs:**
- `/output/<product_name>/prd.md` — Complete PRD with features, goals, non-goals, metrics, and traceability

**How it works:**
- Reads discovered needs
- Identifies patterns (gains/pains that appear across multiple roles)
- Designs features using many-to-one pattern (one feature solves multiple problems)
- Generates PRD sections: Overview, Goals, User Roles, Features, NFRs, Success Metrics, Open Questions
- Each feature traces back to which user roles/tasks/gains/pains it solves

---

### 3. user-story-expansion

**Purpose:** Detail acceptance criteria and workflows for features.

**When to use:** After PRD creation, when you need to specify exactly how features should behave.

**Inputs:**
- Path to PRD file (e.g., `/output/habit-tracker/prd.md`)

**Outputs:**
- `/output/<product_name>/user-stories.md` — User stories with acceptance criteria (Gherkin), data models, edge cases, and open questions

---

### 4. test-plan

**Purpose:** Create pragmatic, context-appropriate test strategy and test cases.

**When to use:** When user stories and PRD are finalized, and you need a test strategy.

**Inputs:**
- Path to user stories or PRD (e.g., `/output/pomodoro/user-stories.md`)

**Outputs:**
- `/output/<product_name>/test-plan.md` — Pragmatic test plan with:
  - **Selective categories:** Only include test types relevant to the feature (not all 5 for every feature)
  - Unit tests (dev-owned, pre-commit, ≥80% coverage)
  - Integration tests (QA-owned, post-merge, ≥60% critical workflows)
  - E2E tests (100% of user journeys where applicable)
  - Edge case tests (boundary conditions, error states)
  - Performance tests (only if feature has explicit performance requirements)
  - Concise traceability matrix (REQ-FEATURE-01 → test cases)

**Philosophy:** Generates lean, context-appropriate plans instead of boilerplate. A simple button needs 1 unit test; a dashboard with 100k+ rows needs performance tests. No mandatory sections.

---

## Usage

### Quick Start

1. **Have a product idea?** Start here:
   ```
   /requirements-gathering
   ```
   Answer prompts about user roles and what they want to accomplish. Output saved to `/output/<product_name>/requirements.md`.

2. **Done with discovery?** Create your PRD:
   ```
   /prd-creation
   ```
   Point to your `/output/<product_name>/requirements.md` file. Output saved to `/output/<product_name>/prd.md`.

3. **Ready to detail features?** Expand user stories:
   ```
   /user-story-expansion
   ```
   Point to your `/output/<product_name>/prd.md` file. Output saved to `/output/<product_name>/user-stories.md`.

4. **Need a test strategy?** Generate a test plan:
   ```
   /test-plan
   ```
   Point to your `/output/<product_name>/user-stories.md` or `/output/<product_name>/prd.md`. Output saved to `/output/<product_name>/test-plan.md`.

### Output Structure

All skills generate markdown files in a consistent structure:

```
/output/
├── <product_1>/
│   ├── requirements.md      (from requirements-gathering)
│   ├── prd.md              (from prd-creation)
│   ├── user-stories.md     (from user-story-expansion)
│   └── test-plan.md        (from test-plan)
├── <product_2>/
│   ├── requirements.md
│   ├── prd.md
│   └── ...
```

Each product folder contains the complete product specification chain, making it easy to organize, version, and archive project deliverables.

### End-to-End Examples

**Habit Tracker (Fitness App)** — Complete workflow with all steps:
- `output/habit-tracker/concept.md` — Initial product idea
- `output/habit-tracker/requirements.md` — Discovered user needs (from requirements-gathering)
- `output/habit-tracker/prd.md` — Generated PRD with 6 features (from prd-creation)
- `output/habit-tracker/user-stories.md` — Detailed user stories with 12 stories & 36 acceptance criteria (from user-story-expansion)
- `output/habit-tracker/test-plan.md` — Comprehensive test strategy with 38 test cases (from test-plan)

**Pomodoro Timer (Focus App)** — Pragmatic test planning example:
- `output/pomodoro/prd.md` — 7-feature PRD (Timer, Task, Break, Config, Dashboard, Integration, System)
- `output/pomodoro/user-stories.md` — Detailed specification with 32 user stories, 140+ acceptance criteria
- `output/pomodoro/test-plan.md` — **Pragmatic test plan:** 33 test cases (not 62), selective categories, concise format
  - Demonstrates lean approach: performance tests only for dashboard load (<2s), no performance tests for simple features
  - Shows how to scale test density: 1-5 tests per requirement based on complexity

**iPhone Flashlight (Minimalist iOS App)** — Real-world mobile example:
- `output/iphone-flashlight/user-stories.md` — 1 core feature (LED toggle) with 8 detailed acceptance criteria
- `output/iphone-flashlight/test-plan.md` — **Comprehensive test strategy:** 27 test cases across 5 categories
  - 6 Unit Tests (Dev Team): State machine, permissions, device detection, concurrent toggle handling
  - 6 Integration Tests (QA Team): Permission flows, app lifecycle, state sync
  - 4 E2E Tests (QA Team): Cold/warm start, rapid toggle, accessibility compliance
  - 5 Edge Case Tests (QA Team): Device constraints (iPad), permission cycles, state mismatch recovery
  - 6 Performance Tests (DevOps/QA): Battery parity, latency <100ms, cold start <500ms, memory stability
  - Shows how minimal features (1 toggle button) still require comprehensive testing (permission, background, device capability, battery efficiency)

To see how the workflow flows (Habit Tracker):
1. Start with `concept.md` (what we're building)
2. Read `requirements.md` (what we learned from users)
3. Study `prd.md` (how we turned discovery into features)
4. Review `user-stories.md` (detailed acceptance criteria with Gherkin format)
5. Examine `test-plan.md` (how we verify everything works)

To see pragmatic test planning (Pomodoro):
1. Check `test-plan.md` (35-row traceability matrix, 33 concise test cases)
2. Note selective categories: TIMER has Unit+Integration+E2E; DASH has Integration+Performance only
3. See how test cases fit on one screen (no verbose examples)
4. Review honest gaps section (v2 features, platform-specific work deferred)

---

## Automation & Quality Checks

### PRD Quality Evaluator

The toolkit includes automatic PRD quality evaluation triggered on every PRD output.

**Files:**
- `.claude/settings.json` — Configures PostToolUse hooks to trigger evaluation
- `.claude/skills/prd-creation/eval-prd.py` — PRD quality validator aligned with SKILL.md structure

**How it works:**
1. When prd-creation skill outputs a PRD to `/output/<product>/prd.md`
2. PostToolUse hook automatically triggers eval-prd.py
3. Validator checks:
   - **Structure:** All required sections per SKILL.md (Product Overview, Goals & Non-Goals, User Roles & Needs, Features, Product-Wide NFRs, Success Metrics, Open Questions)
   - **Traceability:** Every feature has "Solves For" section linking to user roles/tasks/gains/pains
   - **Completeness:** Non-Goals explicitly stated in Goals section; quantified success metrics present
   - **Placeholders:** No TBD, TODO, FIXME content
   - **Depth:** Sufficient detail (≥4000 chars) indicating thorough requirements
4. Generates HTML evaluation report with pass/fail status and actionable feedback

**No manual review needed** — Evaluation runs automatically after PRD generation, with results displayed inline in console and saved as HTML.

### Test Plan Quality Evaluator

The toolkit also includes automatic test plan quality evaluation triggered on every test plan output.

**Files:**
- `.claude/settings.json` — Configures PostToolUse hooks to trigger evaluation
- `.claude/skills/test-plan/eval-test-plan.py` — Test plan quality validator

**How it works:**
1. When test-plan skill outputs a test plan to `/output/<product>/test-plan.md`
2. PostToolUse hook automatically triggers eval-test-plan.py
3. Validator checks:
   - **Structure:** All required sections (Overview, Strategy, Traceability Matrix, Test Cases)
   - **Test Categories:** Selective categories (only include relevant types: Unit, Integration, E2E, Edge Case, Performance)
   - **Traceability:** Each test case links to requirements (REQ-* identifiers present)
   - **Gherkin Format:** Scenario-based tests use Given/When/Then format
   - **Test Ownership:** Clear ownership model defined (Dev/QA/DevOps/timing)
   - **Pragmatic Density:** Ratio of test cases to requirements is reasonable (1-5:1)
   - **Placeholders:** No TBD, TODO, FIXME content
   - **Depth:** Sufficient detail (≥3000 chars) indicating completeness
4. Generates HTML evaluation report with pass/fail status and actionable feedback

**No manual review needed** — Evaluation runs automatically after test plan generation, with results displayed inline in console and saved as HTML.

### Hook Configuration

The automation is wired via Claude Code's PostToolUse hooks in `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "filter": "jq -r 'select(.tool_input.file_path | test(\"/output/.*\\.md$\")) | .tool_input.file_path' | head -1",
            "command": "[hook for PRD evaluation on write]"
          },
          {
            "type": "command",
            "filter": "jq -r 'select(.tool_input.file_path | test(\"/output/.*\\.md$\")) | .tool_input.file_path' | head -1",
            "command": "[hook for test plan evaluation on write]"
          },
          {
            "type": "command",
            "filter": "jq -r 'select(.tool_input.file_path | test(\"EVAL\\.txt$\")) | .tool_input.file_path' | head -1",
            "command": "[hook for manual EVAL.txt trigger]"
          }
        ]
      }
    ]
  }
}
```

This configuration:
- Intercepts Write operations on files matching `/output/*/prd.md` and `/output/*/test-plan.md`
- Automatically runs respective evaluators on each file written
- Supports manual evaluation via `EVAL.txt` trigger file (write file path to EVAL.txt, hook reads and evaluates)
- Displays evaluation results with status, failed checks, and context
- Auto-deletes EVAL.txt after evaluation completes

**Manual Evaluation:**
```bash
# Trigger evaluation of any markdown file:
echo "/path/to/file.md" > EVAL.txt
```

The hook detects the EVAL.txt write, routes to the appropriate evaluator (based on filename), generates the HTML report, and cleans up.

No additional setup needed—hooks are configured once and work on all PRDs and test plans.

---

## Key Principles

### 1. Traceability First
Every feature traces back to discovered user needs. No feature exists in a vacuum; every requirement solves a specific pain or enables a gain.

### 2. Many-to-One Pattern
A single feature often solves multiple user problems elegantly. Rather than designing separate features for each pain, we identify where problems cluster and design features that address multiple needs simultaneously.

Example from Habit Tracker:
- **Pain 1 (Newbie):** "Logging takes too long and kills momentum"
- **Pain 2 (Gym Rat):** "Manual export to spreadsheets for analysis"
- **Solution 1 Feature:** Quick-log interface solves both (fast capture + granular data)

### 3. Sequential Handoff
Each skill's output becomes the next skill's input. Don't skip phases; each phase adds specificity:
- Discovery → focus on *what users need*
- PRD → focus on *what features solve*
- User Stories → focus on *how features behave*
- Test Plan → focus on *how to verify features work*

### 4. User-Centric, Not Feature-Centric
Start by understanding problems (gains/pains), not by designing solutions. Users describe their world; we design the responses.

---

## Project Structure

```
.
├── README.md                           (this file)
├── .claude/
│   ├── settings.json                   (PostToolUse hooks for automatic PRD & test-plan evaluation)
│   └── skills/
│       ├── requirements-gathering/
│       │   └── SKILL.md                (discovery workflow)
│       ├── prd-creation/
│       │   ├── SKILL.md                (PRD generation workflow)
│       │   └── eval-prd.py             (SKILL.md-aligned quality validator, auto-triggered)
│       ├── user-story-expansion/
│       │   └── SKILL.md                (acceptance criteria workflow)
│       └── test-plan/
│           ├── SKILL.md                (pragmatic test strategy workflow)
│           └── eval-test-plan.py       (test plan quality validator, auto-triggered)
└── output/
    ├── habit-tracker/
    │   ├── concept.md                  (initial product idea)
    │   ├── requirements.md             (discovered user needs)
    │   ├── prd.md                      (6-feature PRD)
    │   ├── user-stories.md             (12 user stories, 36 acceptance criteria)
    │   └── test-plan.md                (38 test cases, 5 categories, 100% coverage)
    ├── pomodoro/
    │   ├── prd.md                      (Pomodoro Timer PRD)
    │   ├── user-stories.md             (32 user stories across 7 features)
    │   ├── test-plan.md                (33 pragmatic test cases, 118 hours effort)
    │   └── pomodoro-reqs-test-data.md  (test data fixtures & fast-test constants)
    └── iphone-flashlight/
        └── test-plan.md                (27 comprehensive test cases for minimalist LED toggle app)
```

---

## For Your First Product

When using this toolkit for a new product:

1. **Start small** — You don't need a polished concept. "A task management app" is enough to begin discovery.

2. **Validate in discovery** — The requirements-gathering skill helps you interview users systematically. Capture their language, not your solutions.

3. **Identify patterns early** — As you build the PRD, look for gains/pains that repeat across roles. These are opportunities to design elegant, multi-purpose features.

4. **Keep traceability links** — Reference user roles and tasks in feature descriptions. This makes it easy to push back on feature creep ("Does this solve a discovered pain?").

5. **Defer implementation details** — PRDs should specify *what* users need, not *how* to code it. Tech decisions come later.

---

## Tips for Success

### For Product Managers
- Use discovery to challenge assumptions. Users often describe problems differently than you expected.
- Prioritize by traceability. Features that solve multiple user problems have higher ROI.
- Keep PRDs user-focused. When a feature seems generic ("improve performance"), trace it back to a specific user need.

### For Designers
- User stories + acceptance criteria give you concrete workflows to design. Don't go broader.
- Form guidance, dashboard views, and quick-log flows are all defined in the example PRD—use them as interaction starting points.
- Edge cases and open questions in user stories highlight areas needing design decisions.

### For Developers
- Test plan provides traceability from code to user needs. Organize tests by layer (unit, integration, E2E).
- User stories define acceptance criteria in Gherkin. These should map 1:1 to your test cases.
- Non-functional requirements (performance, offline, reliability) are in the PRD—use them to drive architecture.

### For QA/Test Engineers
- Test plan categorizes tests by ownership (dev unit tests, QA integration/E2E, DevOps performance).
- Every test traces back to a requirement (REQ-FEATURE-01 maps to specific test cases).
- Edge cases and error handling tests are explicitly scoped in the test plan.

---

## Common Questions

**Q: Do I need to run all four skills?**
A: No. You can use any skill standalone. Requirements discovery → PRD is the core workflow. User story expansion and test planning are optional but recommended.

**Q: Can I use this for existing products?**
A: Yes. Start with the PRD creation skill if you already have a requirements document. Or run discovery to understand what users actually need vs. what was built.

**Q: What if my product doesn't fit the discovery questions?**
A: The framework is flexible. The skill prompts are starting points. Adapt them to your domain (jobs, gains, pains work across B2B, B2C, internal tools, marketplaces, etc.).

**Q: How detailed should PRDs be?**
A: Use the Habit Tracker example as a guide. Include enough detail that a designer/dev can start work, but not so much that you've designed the implementation (that's their job).

---

## Contributing

This toolkit is designed to be extended with:
- Additional example products (SaaS, B2B, marketplaces)
- Domain-specific discovery questions (healthcare, fintech, etc.)
- Custom feature design patterns
- Integration with AI agents for automated discovery or PRD generation

---

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
