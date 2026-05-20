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

**Purpose:** Create comprehensive test strategy and categorized test cases.

**When to use:** When user stories and PRD are finalized, and you need a test strategy.

**Inputs:**
- Path to user stories or PRD (e.g., `/output/habit-tracker/user-stories.md`)

**Outputs:**
- `/output/<product_name>/test-plan.md` — Test plan with:
  - Unit tests (dev-owned, ≥80% coverage)
  - Integration tests (QA-owned, ≥60% critical workflows)
  - E2E tests (100% of acceptance criteria)
  - Edge case tests
  - Performance tests
  - Requirement traceability (REQ-FEATURE-01 → test cases)

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

### End-to-End Example

See `examples/` for a complete walkthrough using a **Habit Tracker** (fitness app):

- `examples/concept.md` — Initial product idea
- `examples/reqs-gather-user-test-data.md` — Discovered requirements (same as `/output/habit-tracker/requirements.md`)
- `examples/prd-habit-tracker.md` — Generated PRD with 6 features (same as `/output/habit-tracker/prd.md`)
- `examples/user-stories-habit-tracker.md` — Detailed user stories with acceptance criteria (same as `/output/habit-tracker/user-stories.md`)

To see how the workflow flows:
1. Start with `concept.md` (what we're building)
2. Read `reqs-gather-user-test-data.md` (what we learned from users)
3. Study `prd-habit-tracker.md` (how we turned discovery into features)
4. Review `user-stories-habit-tracker.md` (detailed acceptance criteria)

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
├── examples/
│   ├── concept.md                      (Habit Tracker: initial idea)
│   ├── reqs-gather-user-test-data.md   (Habit Tracker: discovered needs)
│   ├── prd-habit-tracker.md            (Habit Tracker: full PRD)
│   └── user-stories-habit-tracker.md   (Habit Tracker: detailed stories)
└── .claude/
    └── skills/
        ├── requirements-gathering/
        │   └── SKILL.md                (discovery workflow)
        ├── prd-creation/
        │   └── SKILL.md                (PRD generation workflow)
        ├── user-story-expansion/
        │   └── SKILL.md                (acceptance criteria workflow)
        └── test-plan/
            └── SKILL.md                (test strategy workflow)
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

**Last Updated:** May 20, 2026
