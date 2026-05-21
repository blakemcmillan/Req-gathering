---
name: test-plan
description: Generate a comprehensive test plan with categorized test cases from user stories, acceptance criteria, and requirements. Use when you need to convert feature specifications into detailed test strategies and test cases.
argument-hint: "[file path or feature description]"
allowed-tools: Read, Write
---

# Generate Test Plan from User Stories

Transform the following user stories, acceptance criteria, or PRD into a comprehensive Test Plan with categorized test cases:

**Input:** $ARGUMENTS

**Output Filename:** Create filename from feature/project name. Save to `/output/<project_name>/test-plan.md`. Save file path to EVAL.txt

---

## Key Constraint

**Only include technical details or stack information if explicitly provided in the input.** 
Do not infer, assume, or add:
 - Technology stacks (languages, frameworks, databases)
 - CI/CD platforms or tools
 - Testing frameworks or tools
 - Infrastructure or deployment details
 - Cloud platforms or services

If the input does not mention these, the test plan should remain stack-agnostic and focus purely on test strategy, test cases, and coverage.

## Test Plan Structure

Create a detailed test plan with these sections:

### Project/Feature: [Name from input]

**Test Plan Overview**
- 2-3 sentence summary of what's being tested
- Scope and boundaries
- Testing approach (unit, integration, E2E)

**Test Strategy**

*Ownership & Responsibilities:*
- **Dev Team:** Unit tests, component-level testing (automated)
- **QA Team:** Integration, E2E, edge case, performance tests (manual + automated)
- **DevOps Team:** Environment setup, CI/CD pipeline configuration, test infrastructure

*Environment Setup:*
- Local development environment (Node.js, Python, test framework)
- Staging environment for integration/E2E testing
- Mock/test database with seed data
- Test data fixtures and factories

*CI/CD Integration:*
- Unit tests: Run on every commit (pre-merge gate)
- Integration tests: Run on PR merge to main
- E2E tests: Run nightly or on-demand
- Performance tests: Run weekly or before releases
- Failed tests: Block merges to main

*Dependencies & Tools (only if provided in input):*
- Testing framework: [use if specified in requirements]
- Mock/stub libraries: [use if specified in requirements]
- Database: [use if specified in requirements]
- API mocking: [use if specified in requirements]
- Performance monitoring: [use if specified in requirements]
- Coverage reporting: [use if specified in requirements]

*Coverage Goals (recommended baselines, adjust by project risk):*
- Unit tests: 80%+ code coverage (target for critical paths)
- Integration tests: 60%+ critical workflow coverage
- E2E tests: 100% of acceptance criteria scenarios
- Overall: 75%+ combined coverage (adjust based on risk profile)

*Test Data Strategy:*
- **Unit tests:** Use mocks and stubs for dependencies; test with boundary values and invalid inputs
- **Integration tests:** Use test fixtures or seeded test database; reset state between runs
- **E2E tests:** Use real or production-like staging environment; seed with realistic user workflows
- **Edge cases:** Include data edge cases (empty, null, max values, special characters)
- **Performance tests:** Use representative data volumes; simulate realistic user loads

**Test Objectives**

Extract from input:
- What quality standards must be met (performance targets, reliability, usability)
- Which user workflows are critical (user personas, happy paths)
- Known risk areas or past issues to prevent regression

**Test Scope**

*In Scope:*
- All features and user scenarios explicitly mentioned in input
- All acceptance criteria from user stories
- Data flows and integrations described in requirements

*Out of Scope:*
- Features explicitly excluded or marked "future"
- Third-party integrations not controlled by this team
- Infrastructure/DevOps configuration (unless testing it directly)

**Requirement Traceability**

All test cases map to specific requirements. Use the format:
- **REQ-[Feature-#]**: Feature-level requirement (e.g., REQ-PLANNING-01)
- **REQ-[Feature-#]-[Scenario]**: Scenario/acceptance criteria (e.g., REQ-PLANNING-01-SC1)

Example mapping from input:
```
REQ-PLANNING-01: Guided Workout Planning feature
  REQ-PLANNING-01-SC1: Beginner selects pre-built template
  REQ-PLANNING-01-SC2: Beginner customizes a template
```

**Test Categories**

*Categorization guide:*
- **Unit:** Tests a single function/component in isolation? → Unit
- **Integration:** Tests interaction between 2+ components, database, or external systems? → Integration
- **E2E:** Tests a complete user workflow from start to finish? → E2E
- **Edge Case:** Tests boundary conditions, invalid input, or error scenarios? → Edge Case
- **Performance:** Tests response time, throughput, or load handling? → Performance

### 1. Unit Tests (Dev Team)
- Individual component/function testing
- Data validation and business logic
- Boundary conditions and edge cases
- **Ownership:** Development Team (automated, pre-commit)
- **Execution:** On every commit via CI pipeline
- **Format:** Gherkin Given/When/Then

### 2. Integration Tests (QA Team)
- Feature workflow testing
- Cross-component interactions
- API/database interactions
- Data flow verification
- **Ownership:** QA Team (automated, post-merge)
- **Execution:** On PR merge, nightly
- **Format:** Gherkin Given/When/Then

### 3. End-to-End (E2E) Tests (QA Team)
- Full user journey scenarios (derived from acceptance criteria)
- Real user workflows
- Multi-step processes
- **Ownership:** QA Team (manual + automated)
- **Execution:** Nightly or on-demand, before releases
- **Format:** Gherkin Given/When/Then

### 4. Edge Case & Error Handling Tests (QA Team)
- Boundary conditions
- Invalid inputs
- Network/offline scenarios
- Concurrency issues
- **Ownership:** QA Team (mostly manual)
- **Execution:** Before release, on-demand
- **Format:** Gherkin Given/When/Then

### 5. Performance & Load Tests (DevOps/QA)
- Response time requirements
- Concurrent user handling
- Data volume handling
- **Ownership:** DevOps/QA Team (automated)
- **Execution:** Weekly or before releases
- **Format:** Gherkin with timing constraints

---

## Output Instructions

1. **Parse input** - Read user stories, acceptance criteria, or PRD

2. **Create Test Strategy Section** with:
   - Ownership & responsibilities (Dev Team, QA Team, DevOps)
   - Environment setup requirements (tools, frameworks, databases)
   - CI/CD integration points (when tests run, what blocks merges)
   - Dependencies & tools needed
   - Coverage goals by test category

3. **Extract requirements** - Identify all features, scenarios, and acceptance criteria
   - Assign REQ-IDs: REQ-[FEATURE-PREFIX]-[Number] for features
   - Assign scenario IDs: REQ-[FEATURE-PREFIX]-SC[#]

4. **Categorize scenarios** - Map each to test categories using the decision tree:
   - Single function/component in isolation? → Unit
   - Interaction between components/systems? → Integration
   - Complete user workflow end-to-end? → E2E
   - Boundary conditions or error handling? → Edge Case
   - Response time or load requirements? → Performance

5. **Generate test cases**:
   - **Unit Tests** (Dev Team): Use brief strategy format, NO Gherkin
     - Title: [Component] [behavior]
     - Test Strategy: What is being tested and how
     - Test Inputs: Specific test data/variations
     - Expected: Clear expected outcomes
     - Coverage: What code path/logic is validated
     - Owned by: Dev Team
   - **Integration/E2E/Edge Cases** (QA Team): Use Gherkin Given/When/Then format
     - Scenario: Clear user-readable description
     - Preconditions and steps
     - Expected measurable results
     - Owned by: QA Team
   - **Performance Tests** (DevOps/QA): Use Gherkin with timing constraints

6. **Add Requirement Traceability** to each test:
   - Link to original requirement/scenario (REQ-FEATURE-SC#)
   - Add "Owned by: [Team]" field
   - Include relevant tags

7. **Save output** to `/output/<project_name>/test-plan.md`

8. **Include summary** with:
   - Total test cases by category
   - Coverage by feature and overall %
   - Ownership breakdown (Dev/QA/DevOps test count)
   - Estimated effort by test type

**Handling incomplete input:**
- If tools/stack not specified, skip the Dependencies section or mark as "TBD"
- If roles/ownership not mentioned, default to: Dev Team = unit tests, QA Team = integration/E2E/edge cases, DevOps = performance/infrastructure
- If coverage targets not provided, use the recommended baselines
- If test data strategy not clear, assume: unit = mocks, integration = fixtures, E2E = staging environment
- Flag missing information in the test plan summary for the team to clarify

---

## Examples of Good Test Cases

**Unit Tests (Dev Team - Strategy Format, No Gherkin):**

```
TC-UNIT-001: Workout completion percentage calculation
Test Strategy: Validate WorkoutCompletion.calculate_percentage() with various completion counts
- Test inputs: 0/4, 1/4, 2/4, 3/4, 4/4 exercises completed
- Expected: completion_pct = (exercises_completed / total) × 100
- Coverage: Percentage calculation logic for partial/full completion tracking
- Owned by: Dev Team (automated unit test)
Requirement Traceability: REQ-LOGGING-01-SC3
Tags: @unit @calculation @REQ-LOGGING-01-SC3

TC-UNIT-002: Completion streak reset on gap days
Test Strategy: Validate streak increment/reset logic based on day gaps
- Test inputs: last_workout_date as consecutive day, gap, same day
- Expected: streak_days increments if consecutive, resets if gap
- Coverage: Streak calculation and date comparison logic
- Owned by: Dev Team (automated unit test)
Requirement Traceability: REQ-LOGGING-01-SC1
Tags: @unit @streak-logic @REQ-LOGGING-01-SC1
```

**Integration Tests (QA Team - Gherkin Format):**

```gherkin
Scenario: User loads template and saves workout plan
  Given a user viewing the "Full Body 3x/week" template
  When they tap "Use Template" and "Create Plan"
  Then a new Workout record is created
  And the original template remains unmodified
  And the plan appears on the user's home screen

Test ID: TC-INTEGRATION-001
Requirement Traceability: REQ-PLANNING-01-SC1
Owned by: QA Team
Tags: @integration @workflow @template @REQ-PLANNING-01-SC1

Scenario: User logs workout offline and syncs when reconnected
  Given a user with no internet connection after their workout
  When they complete a workout log offline
  Then the app shows "Saved locally. Will sync when online."
  And when the device reconnects, the log automatically syncs to the server

Test ID: TC-INTEGRATION-002
Requirement Traceability: REQ-LOGGING-01-SC4
Owned by: QA Team
Tags: @integration @offline-sync @connectivity @REQ-LOGGING-01-SC4
```

**E2E Tests (QA Team - Gherkin Format):**

```gherkin
Scenario: Beginner completes full workout planning and first logging
  Given a beginner user opening the app for first time
  When they create a plan from "Full Body 3x/week" template
  And they customize one exercise
  And they complete their first workout and log it as "Completed as planned"
  Then the plan is saved with 3 workouts for the week
  And the completed workout is logged
  And the streak counter shows 1

Test ID: TC-E2E-001
Requirement Traceability: REQ-PLANNING-01-SC1, REQ-LOGGING-01-SC1
Owned by: QA Team (Manual + Automated)
Tags: @e2e @beginner-flow @onboarding @REQ-PLANNING-01-SC1
```

**Edge Case Tests:**
```gherkin
Scenario: System prevents unrealistic weight entries
  Given a user with previous max weight of 225 lbs in an exercise
  When they attempt to log 2250 lbs (10x previous max)
  Then the system shows a validation warning
  And the entry is rejected

Test ID: TC-EDGE-001
Requirement Traceability: REQ-LOGGING-01
Owned by: QA Team
Tags: @edge-case @validation @data-quality

Scenario: Partial workout completion calculates percentage correctly
  Given a workout with 4 exercises
  When the user completes 3 exercises and marks as "partial completion"
  Then the completion percentage shows 75%
  And the system offers to reschedule the remaining exercise

Test ID: TC-EDGE-002
Requirement Traceability: REQ-LOGGING-01-SC3
Owned by: QA Team
Tags: @edge-case @calculation @REQ-LOGGING-01-SC3
```

**Performance Tests (DevOps/QA - Gherkin Format with Timing):**

```gherkin
Scenario: Workout plan creation completes within 2 seconds
  Given a user with 50 previous workouts in the system
  When they select "Create Plan" and browse templates
  And they select "Full Body 3x/week" and save it
  Then the plan is created and displayed within 2 seconds
  And the response time remains <2s under 100 concurrent users

Test ID: TC-PERF-001
Requirement Traceability: REQ-PLANNING-01
Owned by: DevOps/QA Team
Tags: @performance @responsiveness @load-test @REQ-PLANNING-01

Scenario: Batch workout logging syncs within 5 seconds
  Given a user logging 10 workouts in offline mode
  When the device reconnects to network
  Then all logs sync to the server within 5 seconds
  And no data is lost during sync

Test ID: TC-PERF-002
Requirement Traceability: REQ-LOGGING-01-SC4
Owned by: DevOps/QA Team
Tags: @performance @sync @offline-handling @REQ-LOGGING-01-SC4
```

---

## When to Use This Skill

**Good inputs:** User stories with acceptance criteria, PRDs with feature specs, detailed requirements with scenarios.

**Poor inputs:** Vague feature descriptions, implementation code, existing test cases, "test this" without specs.

**This skill works when:** You have clear product specifications and need to convert them into organized, actionable test strategies and test cases by category (unit, integration, E2E, edge case, performance).

**Best for:** Ensuring nothing is missed. Maps every acceptance criterion to test cases, identifies coverage gaps, and structures tests by team ownership (Dev, QA, DevOps).
