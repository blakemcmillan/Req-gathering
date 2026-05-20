---
name: test-plan
description: Generate a comprehensive test plan with categorized test cases from user stories, acceptance criteria, and requirements. Use when you need to convert feature specifications into detailed test strategies and test cases.
argument-hint: "[file path or feature description]"
allowed-tools: Read, Write
---

# Generate Test Plan from User Stories

Transform the following user stories, acceptance criteria, or PRD into a comprehensive Test Plan with categorized test cases:

**Input:** $ARGUMENTS

**Output Filename:** Create filename from feature/project name. Save to `/output/<project_name>/test-plan.md`

---

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

*Dependencies & Tools:*
- Testing framework: [pytest, Jest, Cucumber, etc.]
- Mock/stub libraries: [list specific]
- Database: [test database type]
- API mocking: [tool name]
- Performance monitoring: [tool name]
- Coverage reporting: [tool name, e.g., Codecov]

*Coverage Goals:*
- Unit tests: ≥80% code coverage
- Integration tests: ≥60% critical workflows
- E2E tests: 100% of acceptance criteria scenarios
- Overall: ≥75% combined code coverage

**Test Objectives**
- Primary testing goals
- Quality criteria
- Risk areas to focus on

**Test Scope**

*In Scope:*
- Features to be tested
- User scenarios from acceptance criteria

*Out of Scope:*
- What's not being tested
- Known limitations

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

### 1. Unit Tests (Dev Team - Owned)
- Individual component/function testing
- Data validation and business logic
- Boundary conditions and edge cases
- **Format:** Brief strategy, no Gherkin
- **Ownership:** Development Team (automated, pre-commit)
- **Coverage Goal:** ≥80% code coverage
- **Execution:** On every commit via CI pipeline
- **Example Format:**
  ```
  TC-UNIT-001: Workout completion % calculation
  Strategy: Test calculation logic with 0%, 50%, 100% completion
  Coverage: Validates WorkoutCompletion.calculate_percentage() logic
  Owned by: Dev Team
  ```

### 2. Integration Tests (QA Team - Owned)
- Feature workflow testing
- Cross-component interactions
- API/database interactions
- Data flow verification
- **Format:** Gherkin Given/When/Then
- **Ownership:** QA Team (automated, post-merge)
- **Coverage Goal:** ≥60% of critical workflows
- **Execution:** On PR merge, nightly
- **Scenario titles:** "User [action] and [system updates correctly]"

### 3. End-to-End (E2E) Tests (QA Team - Owned)
- Full user journey scenarios (derived from acceptance criteria)
- Real user workflows
- Multi-step processes
- **Format:** Gherkin Given/When/Then
- **Ownership:** QA Team (manual + automated)
- **Coverage Goal:** 100% of acceptance criteria scenarios
- **Execution:** Nightly or on-demand, before releases
- **Scenario titles:** "User completes [full workflow]"

### 4. Edge Case & Error Handling Tests (QA Team - Owned)
- Boundary conditions
- Invalid inputs
- Network/offline scenarios
- Concurrency issues
- **Format:** Gherkin Given/When/Then
- **Ownership:** QA Team (mostly manual)
- **Coverage Goal:** ≥90% of documented edge cases
- **Execution:** Before release, on-demand
- **Scenario titles:** "System handles [edge case]" or "User [action] in [unusual condition]"

### 5. Performance & Load Tests (DevOps/QA - Owned)
- Response time requirements
- Concurrent user handling
- Data volume handling
- **Format:** Gherkin with timing constraints
- **Ownership:** DevOps/QA Team (automated)
- **Coverage Goal:** All critical paths < target time
- **Execution:** Weekly or before releases
- **Scenario titles:** "[Feature] completes within [time constraint]"

---

## Test Case Format (Gherkin)

Use Gherkin syntax with requirement traceability:

```gherkin
Scenario: [Clear description of test scenario]
  Given [initial context or precondition]
  When [action the user takes]
  And [additional action or condition]
  Then [expected outcome/result]
  And [additional expected outcome]
```

**Test ID:** [TC-CATEGORY-###]

**Requirement Traceability:** REQ-[FEATURE]-[SC#] or REQ-[FEATURE]-[Scenario-ID]

**Tags:** @[category] @[priority] @[requirement-id]

Example:

```gherkin
Scenario: User can select beginner template and customize exercise
  Given a beginner user on the planning screen
  When they tap "Use Template" and select "Full Body 3x/week"
  And they remove the barbell bench press from Tuesday
  And they select "Dumbbell press" instead
  Then the modified plan reflects the new exercise
  And the original template remains unchanged

Test ID: TC-PLANNING-002
Requirement Traceability: REQ-PLANNING-01-SC2 (Beginner Customizes a Template)
Tags: @integration @core-flow @REQ-PLANNING-01-SC2
```

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

4. **Categorize scenarios** - Map each to test categories (unit, integration, E2E, edge case, performance)

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

7. **Create Traceability Matrix** - Table showing:
   - Requirement ID → Description → Test IDs → Coverage Status
   - Identify gaps

8. **Save output** to `/output/<project_name>/test-plan.md`

9. **Include summary** with:
   - Total test cases by category
   - Coverage by feature and overall %
   - Ownership breakdown (Dev/QA/DevOps test count)
   - Estimated effort by test type

---

## Requirement Traceability Matrix Example

Include this in your test plan output:

```
| Requirement ID | Description | Test Case IDs | Coverage |
|---|---|---|---|
| REQ-PLANNING-01 | Guided Workout Planning | TC-PLANNING-001, TC-PLANNING-002, TC-PLANNING-003 | ✓ Complete |
| REQ-PLANNING-01-SC1 | Beginner selects pre-built template | TC-PLANNING-001 | ✓ Covered |
| REQ-PLANNING-01-SC2 | Beginner customizes template | TC-PLANNING-002, TC-PLANNING-004 | ✓ Covered |
| REQ-PLANNING-01-SC3 | Experienced user builds custom | TC-PLANNING-003 | ✓ Covered |
| REQ-PLANNING-01-SC4 | Exercise description guidance | TC-PLANNING-005, TC-UNIT-001 | ✓ Covered |
| REQ-PLANNING-01-SC5 | Plan modification timeline | TC-PLANNING-006 | ✓ Covered |
| REQ-LOGGING-01 | Quick Workout Logging | TC-LOGGING-001, TC-LOGGING-002, TC-LOGGING-003 | ✓ Complete |
| REQ-LOGGING-01-SC1 | User logs completed workout | TC-LOGGING-001 | ✓ Covered |
| REQ-LOGGING-01-SC2 | User logs detailed metrics | TC-LOGGING-002 | ✓ Covered |
| REQ-LOGGING-01-SC3 | Partial workout completion | TC-LOGGING-003 | ✓ Covered |

**Coverage Summary:** 20 of 20 requirements covered (100%)
**Gap Analysis:** No uncovered requirements
**Test Count by Category:** Unit: 8, Integration: 12, E2E: 6, Edge Case: 4, Total: 30
```

---

## Examples of Good Test Cases

**Unit Tests (Dev Team - Strategy Format, No Gherkin):**

```
TC-UNIT-001: Workout completion % calculation
Test Strategy: Validate WorkoutCompletion.calculate_percentage() with input variations
- Test inputs: 0/4, 1/4, 2/4, 3/4, 4/4 exercises skipped
- Expected: completion_pct = (exercises_completed / total) × 100
- Coverage: Business logic for partial/full completion tracking
- Owned by: Dev Team (automated unit test)
Requirement Traceability: REQ-LOGGING-01-SC3
Tags: @unit @data-calculation @logic @REQ-LOGGING-01-SC3

TC-UNIT-002: Exercise swap history data integrity
Test Strategy: Verify ExerciseSwap model stores original and alternative IDs correctly
- Test inputs: swap with valid exercise IDs, invalid IDs, null handling
- Expected: ExerciseSwap.original_exercise_id and .alternative_exercise_id populated
- Coverage: Data model integrity, foreign key constraints
- Owned by: Dev Team (automated unit test)
Requirement Traceability: REQ-SWITCHING-01-SC2
Tags: @unit @data-integrity @model @REQ-SWITCHING-01-SC2

TC-UNIT-003: Completion streak increment logic
Test Strategy: Validate CompletionStreak increment/reset on consecutive vs gap days
- Test inputs: last_workout_date variations (consecutive, gap, same day)
- Expected: streak_days increment if consecutive, reset if gap
- Coverage: Streak calculation logic, date comparison
- Owned by: Dev Team (automated unit test)
Requirement Traceability: REQ-LOGGING-01-SC1
Tags: @unit @streak-logic @date-math @REQ-LOGGING-01-SC1

TC-UNIT-004: 1RM estimation accuracy
Test Strategy: Test Epley formula implementation: 1RM = weight × (1 + reps/30)
- Test inputs: weight=[100, 225, 315], reps=[1-10]
- Expected: 1RM within ±1 lb tolerance of formula result
- Coverage: Math formula implementation, floating point precision
- Owned by: Dev Team (automated unit test)
Requirement Traceability: REQ-ANALYTICS-01-SC2
Tags: @unit @formula @calculation @REQ-ANALYTICS-01-SC2
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
  And when the device reconnects
  Then the log automatically syncs to the server

Test ID: TC-INTEGRATION-005
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
  And they save the plan
  And they complete their first workout
  And they log it as "Completed as planned"
  Then the plan is saved with 3 workouts for the week
  And the completed workout is logged
  And the streak counter shows 1

Test ID: TC-E2E-001
Requirement Traceability: REQ-PLANNING-01-SC1, REQ-LOGGING-01-SC1
Owned by: QA Team (Manual + Automated)
Tags: @e2e @beginner-flow @onboarding @REQ-PLANNING-01-SC1
```

**Integration Test:**
```gherkin
Scenario: User loads template and saves workout without modifying original
  Given a user viewing the "Full Body 3x/week" template
  When they select "Use Template"
  And they save the plan as a new workout
  Then the new workout is created with template data
  And the original template remains unchanged

Test ID: TC-INTEGRATION-001
Requirement Traceability: REQ-PLANNING-01-SC1 (Beginner Selects Pre-Built Template)
Tags: @integration @workflow @REQ-PLANNING-01-SC1

Scenario: Offline workout logging syncs when reconnected
  Given a user with no internet connection
  When they complete a workout log
  Then the app shows "Saved locally. Will sync when online."
  And the log is queued for sync
  And when the device reconnects, the log syncs to the server

Test ID: TC-INTEGRATION-002
Requirement Traceability: REQ-LOGGING-01-SC4 (Offline Logging)
Tags: @integration @offline-sync @REQ-LOGGING-01-SC4

Scenario: Exercise swap updates LoggedExercise without affecting future workouts
  Given a user swaps an exercise in today's workout
  When the swap is completed
  Then LoggedExercise record is updated with the alternative
  And future scheduled workouts are not affected

Test ID: TC-INTEGRATION-003
Requirement Traceability: REQ-SWITCHING-01-SC2 (User Swaps and Continues Workout)
Tags: @integration @data-consistency @REQ-SWITCHING-01-SC2
```

**E2E Test:**
```gherkin
Scenario: Beginner completes full workout planning flow in under 5 minutes
  Given a beginner on the app for the first time
  When they tap "Create Plan"
  And they browse and select "Full Body 3x/week" template
  And they customize one exercise
  And they save the plan
  Then the plan is saved with 3 workouts for the week
  And the process completes in < 5 minutes

Test ID: TC-E2E-001
Requirement Traceability: REQ-PLANNING-01-SC1, REQ-PLANNING-01-SC2
Tags: @e2e @workflow @beginner-flow @REQ-PLANNING-01-SC1 @REQ-PLANNING-01-SC2

Scenario: User adapts workout when equipment is unavailable
  Given a user is mid-workout and reaches "Barbell Back Squat"
  When they mark the exercise as "equipment unavailable"
  Then the app suggests 2-3 alternatives within 1 second
  And when they select "Leg Press"
  Then the workout logs the alternative instead
  And a swap note is recorded

Test ID: TC-E2E-002
Requirement Traceability: REQ-SWITCHING-01-SC1, REQ-SWITCHING-01-SC2
Tags: @e2e @adaptive-workout @REQ-SWITCHING-01-SC1 @REQ-SWITCHING-01-SC2

Scenario: User views analytics and exports data
  Given a user with 3 months of workout logs
  When they open Analytics
  And they select "Barbell Back Squat"
  Then a progression chart displays
  And when they tap "Export"
  Then a CSV file is generated and ready to download

Test ID: TC-E2E-003
Requirement Traceability: REQ-ANALYTICS-01-SC1, REQ-ANALYTICS-01-SC4
Tags: @e2e @analytics @export @REQ-ANALYTICS-01-SC1 @REQ-ANALYTICS-01-SC4
```

**Edge Case Test:**
```gherkin
Scenario: Late logging preserves streak for consecutive day
  Given a user forgot to log a workout 2 days ago
  When they tap "Log Past Workout"
  And they select the date from 2 days ago
  And they complete the log
  Then the workout is recorded with the correct date
  And the streak remains unbroken (consecutive days)

Test ID: TC-EDGE-001
Requirement Traceability: REQ-LOGGING-01-SC5 (Late Logging 2 Days After Workout)
Tags: @edge-case @streak-logic @REQ-LOGGING-01-SC5

Scenario: System prevents unrealistic weight entries
  Given a user with previous max weight of 225 lbs in an exercise
  When they attempt to log 2250 lbs (10x max)
  Then the system shows a warning
  And the entry is not accepted

Test ID: TC-EDGE-002
Requirement Traceability: REQ-LOGGING-01 (Data Accuracy - Open Question)
Tags: @edge-case @validation @data-quality

Scenario: Partial workout completion calculates percentage correctly
  Given a workout with 4 exercises
  When the user completes 3 exercises
  And marks the workout as "partial completion"
  Then the completion percentage is 75%
  And the system prompts to reschedule the remaining 1 exercise

Test ID: TC-EDGE-003
Requirement Traceability: REQ-LOGGING-01-SC3 (Partial Completion)
Tags: @edge-case @calculation @REQ-LOGGING-01-SC3
```

---

## Prompts

### ✓ Good Fit (Positive Examples)

- File path to user stories document
- File path to detailed PRD
- Feature specification with acceptance criteria in Gherkin format
- Multi-feature product specification
- Habit tracker app with detailed user stories and data models
- Feature with multiple user scenarios and edge cases

### ✗ Poor Fit (Negative Examples)

- "Test this" with no specifications
- Implementation code or design documents
- Already-written test cases (no conversion needed)
- Vague feature descriptions without acceptance criteria
- Non-functional documents

### Why This Skill Works Best

Test-plan transforms **product specifications** into **detailed, actionable test cases**. It answers "what do we test?" and "how do we verify it works?" — converting acceptance criteria and user scenarios into executable test strategies organized by category (unit, integration, E2E, edge cases).

Use this skill when you have clear specifications (PRD, user stories, acceptance criteria) and need comprehensive test coverage.
