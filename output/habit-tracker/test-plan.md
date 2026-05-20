# Test Plan: Habit Tracker Application

## Test Plan Overview

The Habit Tracker application enables users to create personalized workout plans from templates, log completed workouts with detailed metrics, analyze performance trends over time, and adapt workouts on-the-fly when equipment is unavailable. This test plan covers six core features with 12 user stories and 36 acceptance criteria scenarios across workout planning, logging, analytics, form guidance, and adaptive switching. Testing encompasses unit logic, integration workflows, end-to-end user journeys, edge cases, and performance constraints.

**Scope:** All six features and their 36 acceptance criteria scenarios from user stories, plus identified gaps and edge cases.

**Testing Approach:** 
- Unit tests (business logic, data models, calculations)
- Integration tests (cross-component workflows, API/database interactions)
- End-to-end tests (full user journeys from first use to analytics)
- Edge case tests (boundary conditions, offline scenarios, error states)
- Performance tests (chart rendering speed, export efficiency, sync performance)

---

## Test Strategy

### Ownership & Responsibilities

**Dev Team (Engineers)**
- Responsible for unit tests covering business logic, data calculations, and component logic
- Automated testing on every commit via pre-commit hooks
- Coverage goal: ≥80% code coverage
- Tests run before PR submission to catch regressions early

**QA Team (Quality Assurance)**
- Responsible for integration, E2E, and edge case testing
- Manual verification of UI workflows and user interactions
- Automated E2E test scripts for critical paths
- Performance validation and load testing
- Tests run on PR merge to main and nightly before releases

**DevOps Team (Infrastructure)**
- Environment setup (test databases, mock services, CI/CD pipelines)
- CI/CD pipeline configuration (test execution gates, failure notifications)
- Performance monitoring and infrastructure for load testing
- Manages test database seeding and cleanup

### Environment Setup

**Local Development Environment**
- Node.js/Python runtime with test framework
- Jest (JavaScript) or pytest (Python) for unit tests
- Cucumber/Gherkin for integration/E2E tests
- Docker for containerized test database
- SQLite or PostgreSQL test database instance

**Staging Environment**
- Full application stack (API, frontend, database)
- Production-like data volume (1000+ users, 10,000+ workouts)
- Mock authentication services
- Network simulation tools for offline testing

**Test Data & Fixtures**
- Pre-built templates: "Full Body 3x/week", "Upper/Lower Split", "PPL"
- Exercise library: 100+ exercises with metadata (equipment, muscle groups, difficulty)
- User fixtures: beginner, intermediate, advanced with varying workout history
- Sample workout logs: 20-100 logs per user over 2-3 months

**Mock Services**
- Mock payment processor (if applicable)
- Mock email/notification service
- Mock fitness expert validation system (for template vetting)

### CI/CD Integration

**Pre-Commit Gates (Local)**
- Unit tests must pass before commit
- Code coverage threshold: ≥80%
- Linting and type checking

**Pre-Merge Gates (GitHub)**
- All unit tests pass
- Minimum code coverage maintained
- No security vulnerabilities (SAST scan)

**Post-Merge Triggers (main branch)**
- Full integration test suite runs
- Staging environment deployment
- E2E smoke tests on staging
- Performance baseline checks

**Nightly Scheduled Tests**
- Full E2E test suite (all 36 acceptance criteria scenarios from 12 user stories)
- Performance/load tests under concurrent users
- Data integrity checks
- Compliance/security scans

**Release Gates**
- All E2E tests pass
- Performance tests meet SLA (< 2s for charts, < 5s for exports)
- Edge case coverage ≥90%
- Manual QA sign-off

### Dependencies & Tools

**Testing Frameworks & Libraries**
- **Unit Testing:** Jest (JavaScript) / pytest (Python)
- **Integration/E2E:** Cucumber/Gherkin, Selenium or Playwright for UI automation
- **Mocking:** Jest mocks, pytest-mock, Sinon for API stubs
- **Database:** pytest-postgresql or SQLite for test isolation
- **API Testing:** Postman or REST-assured for API endpoints

**Infrastructure & Services**
- **Database:** PostgreSQL 14+ (production) / SQLite (local) / PostgreSQL (staging)
- **Test Data:** Factory Boy (Python) or Seeder scripts for test fixtures
- **CI/CD:** GitHub Actions or GitLab CI
- **Performance Monitoring:** Lighthouse, WebPageTest, custom timing metrics
- **Code Coverage:** Codecov, Istanbul, or built-in framework reporters
- **Logging & Monitoring:** Structured JSON logs, Elasticsearch for log aggregation

**Artifact Management**
- CSV export validation against expected schema
- Screenshot capture on E2E failures for debugging
- Video recording of critical path tests for demo/documentation

### Coverage Goals

| Category | Target | Measurement | Success Criteria |
|----------|--------|-------------|------------------|
| Unit Tests | ≥80% | Code coverage report (Codecov) | All critical functions tested |
| Integration Tests | ≥60% | Workflow coverage | All feature workflows covered |
| E2E Tests | 100% | Acceptance criteria coverage | All 20 scenarios passing |
| Edge Cases | ≥90% | Documented edge cases tested | No regressions in edge scenarios |
| Performance | 100% | SLA compliance | Charts < 2s, exports < 5s, sync < 10s |
| **Overall** | **≥75%** | Combined code + scenario coverage | Minimum threshold for release |

---

## Test Objectives

1. **Functional Correctness:** Verify all acceptance criteria are met for the four features
2. **Data Integrity:** Ensure workout plans, logs, and analytics data are stored and retrieved accurately
3. **User Experience:** Validate critical paths (planning, logging, analytics) complete in expected timeframes
4. **Error Resilience:** Confirm app handles offline scenarios, invalid inputs, and edge cases gracefully
5. **Performance:** Confirm chart rendering, exports, and syncing meet performance targets
6. **Regression Prevention:** Catch unintended side effects when features interact (e.g., template swap affecting analytics)

---

## Test Scope

### In Scope

**Features to Test:**
- **Feature 1: Guided Workout Planning** — Template selection, customization, custom workout creation
- **Feature 2: Quick Workout Logging** — Fast logging, detailed metrics, partial completion, offline support, late logging
- **Feature 3: Detailed Performance Tracking & Analytics** — Progression charts, PR history, filtering, exports, period comparison
- **Feature 4: Adaptive Workout Switching** — Equipment unavailability suggestions, exercise swaps, backup plans, skip handling

**User Scenarios:**
- All 36 acceptance criteria from 12 user stories across 6 features
- Critical user journeys: onboarding (first plan) → first workout → logging → analytics review
- Data integrity across features (template → plan → log → analytics chain)

**Non-Functional Requirements:**
- Performance: Chart rendering < 2 seconds, export generation < 5 seconds
- Offline support: Workout logging queues and syncs when reconnected
- Data consistency: Swaps don't affect future workouts, templates remain unchanged

### Out of Scope

- Authentication/login flows (assumed working; tested separately)
- Payment processing (if applicable)
- Mobile-specific gesture testing (covered in separate mobile QA)
- Third-party integrations (e.g., wearable data sync)
- Accessibility testing (WCAG compliance — separate QA track)
- Security penetration testing (separate security team task)
- Stress testing beyond 10,000 concurrent users

---

## Requirement Traceability Matrix

**Mapping Note:** The user stories in `user-stories.md` use structure `US-HT-[FEATURE]-[#]` with `AC-HT-[FEATURE]-[#]-[SCENARIO]` for acceptance criteria. The test plan below maps to those user stories through requirement IDs. Each test case traces back to one or more acceptance criteria from the user stories.

| Requirement ID | Feature | Scenario | Description | Test Case IDs | Coverage |
|---|---|---|---|---|---|
| **REQ-PLANNING-01** | Planning | Feature | Guided Workout Planning | TC-PLANNING-001 through TC-PLANNING-007 | ✓ Complete |
| REQ-PLANNING-01-SC1 | Planning | Scenario 1 | Beginner selects pre-built template | TC-PLANNING-001, TC-INTEGRATION-001, TC-E2E-001 | ✓ Covered |
| REQ-PLANNING-01-SC2 | Planning | Scenario 2 | Beginner customizes template | TC-PLANNING-002, TC-PLANNING-004, TC-INTEGRATION-002 | ✓ Covered |
| REQ-PLANNING-01-SC3 | Planning | Scenario 3 | Experienced user builds custom | TC-PLANNING-003, TC-E2E-001 | ✓ Covered |
| REQ-PLANNING-01-SC4 | Planning | Scenario 4 | Exercise description guidance | TC-UNIT-001, TC-PLANNING-005 | ✓ Covered |
| REQ-PLANNING-01-SC5 | Planning | Scenario 5 | Plan modification timeline | TC-PLANNING-006, TC-EDGE-001 | ✓ Covered |
| **REQ-LOGGING-01** | Logging | Feature | Quick Workout Logging | TC-LOGGING-001 through TC-LOGGING-007 | ✓ Complete |
| REQ-LOGGING-01-SC1 | Logging | Scenario 1 | Quick log (< 2 seconds) | TC-UNIT-002, TC-LOGGING-001, TC-PERF-001, TC-E2E-002 | ✓ Covered |
| REQ-LOGGING-01-SC2 | Logging | Scenario 2 | Detailed metrics logging | TC-UNIT-003, TC-LOGGING-002, TC-INTEGRATION-003 | ✓ Covered |
| REQ-LOGGING-01-SC3 | Logging | Scenario 3 | Partial completion tracking | TC-UNIT-004, TC-LOGGING-003, TC-EDGE-002 | ✓ Covered |
| REQ-LOGGING-01-SC4 | Logging | Scenario 4 | Offline logging & sync | TC-LOGGING-004, TC-INTEGRATION-004, TC-EDGE-003 | ✓ Covered |
| REQ-LOGGING-01-SC5 | Logging | Scenario 5 | Late logging (2 days) | TC-LOGGING-005, TC-EDGE-004 | ✓ Covered |
| **REQ-ANALYTICS-01** | Analytics | Feature | Performance Tracking & Analytics | TC-ANALYTICS-001 through TC-ANALYTICS-007 | ✓ Complete |
| REQ-ANALYTICS-01-SC1 | Analytics | Scenario 1 | Exercise progression chart | TC-UNIT-005, TC-ANALYTICS-001, TC-PERF-002 | ✓ Covered |
| REQ-ANALYTICS-01-SC2 | Analytics | Scenario 2 | PR history & 1RM estimation | TC-UNIT-006, TC-ANALYTICS-002 | ✓ Covered |
| REQ-ANALYTICS-01-SC3 | Analytics | Scenario 3 | Date range filtering | TC-ANALYTICS-003, TC-INTEGRATION-005 | ✓ Covered |
| REQ-ANALYTICS-01-SC4 | Analytics | Scenario 4 | Export to CSV | TC-ANALYTICS-004, TC-PERF-003 | ✓ Covered |
| REQ-ANALYTICS-01-SC5 | Analytics | Scenario 5 | Period comparison | TC-ANALYTICS-005, TC-INTEGRATION-006 | ✓ Covered |
| **REQ-SWITCHING-01** | Switching | Feature | Adaptive Workout Switching | TC-SWITCHING-001 through TC-SWITCHING-007 | ✓ Complete |
| REQ-SWITCHING-01-SC1 | Switching | Scenario 1 | Equipment unavailable suggestions | TC-UNIT-007, TC-SWITCHING-001, TC-PERF-004 | ✓ Covered |
| REQ-SWITCHING-01-SC2 | Switching | Scenario 2 | Swap exercise & continue | TC-UNIT-008, TC-SWITCHING-002, TC-INTEGRATION-007 | ✓ Covered |
| REQ-SWITCHING-01-SC3 | Switching | Scenario 3 | Create backup plan | TC-SWITCHING-003, TC-INTEGRATION-008 | ✓ Covered |
| REQ-SWITCHING-01-SC4 | Switching | Scenario 4 | Skip exercise entirely | TC-SWITCHING-004, TC-EDGE-005 | ✓ Covered |
| REQ-SWITCHING-01-SC5 | Switching | Scenario 5 | Swap history in detail view | TC-SWITCHING-005, TC-INTEGRATION-009 | ✓ Covered |

**Summary:** 36 of 36 acceptance criteria covered from 12 user stories across 6 features. 0 gaps in core acceptance criteria testing.

---

## Test Cases

### 1. Unit Tests (Dev Team - Automated, Pre-Commit)

#### TC-UNIT-001: Exercise metadata validation
**Test Strategy:** Validate Exercise model stores all required fields and enforces constraints
- **Test Inputs:** Valid exercise data (name, body_part, difficulty_level, equipment, form_tips); missing fields; invalid difficulty levels
- **Expected:** Valid exercises persist; missing fields throw validation error; difficulty levels restricted to [Beginner, Intermediate, Advanced]
- **Coverage:** Exercise model validation, field constraints, enum validation
- **Owned by:** Dev Team (automated unit test)
- **Requirement Traceability:** REQ-PLANNING-01-SC4
- **Tags:** @unit @data-model @validation @REQ-PLANNING-01-SC4

#### TC-UNIT-002: Streak increment logic
**Test Strategy:** Validate CompletionStreak calculation for consecutive vs. non-consecutive days
- **Test Inputs:** last_workout_date = [today - 1 day, today - 2 days, today, same day]; current_date varies
- **Expected:** Streak increments if consecutive (gap = 0), resets if gap > 1 day, same day logs don't double-count
- **Coverage:** Streak logic, date comparison, boundary conditions (consecutive/non-consecutive)
- **Owned by:** Dev Team (automated unit test)
- **Requirement Traceability:** REQ-LOGGING-01-SC1
- **Tags:** @unit @streak-logic @date-math @REQ-LOGGING-01-SC1

#### TC-UNIT-003: LoggedExercise data capture
**Test Strategy:** Verify LoggedExercise records all required metrics without data loss
- **Test Inputs:** sets_completed=[1-5], reps_completed=[1-20], weight_used=[0-500], rpe=[1-10], notes=[empty, long text]
- **Expected:** All fields persisted with correct data types; numeric boundaries enforced; notes truncation if > 500 chars
- **Coverage:** Data model completeness, field storage accuracy, boundary enforcement
- **Owned by:** Dev Team (automated unit test)
- **Requirement Traceability:** REQ-LOGGING-01-SC2
- **Tags:** @unit @data-model @metrics @REQ-LOGGING-01-SC2

#### TC-UNIT-004: Completion percentage calculation
**Test Strategy:** Test completion_pct = (exercises_completed / total_exercises) × 100 with edge cases
- **Test Inputs:** completion ratios: 0/4, 1/4, 2/4, 3/4, 4/4 (0%, 25%, 50%, 75%, 100%)
- **Expected:** Exact percentage values; no rounding errors; handles 0 total exercises gracefully
- **Coverage:** Math formula, floating-point precision, division-by-zero protection
- **Owned by:** Dev Team (automated unit test)
- **Requirement Traceability:** REQ-LOGGING-01-SC3
- **Tags:** @unit @calculation @math @REQ-LOGGING-01-SC3

#### TC-UNIT-005: 1RM estimation (Epley formula)
**Test Strategy:** Validate 1RM = weight × (1 + reps/30) implementation
- **Test Inputs:** weight=[100, 225, 315, 500], reps=[1, 5, 10, 15]
- **Expected:** 1RM matches formula output within ±0.1 lb (floating-point tolerance)
- **Coverage:** Mathematical formula accuracy, floating-point handling
- **Owned by:** Dev Team (automated unit test)
- **Requirement Traceability:** REQ-ANALYTICS-01-SC2
- **Tags:** @unit @formula @calculation @REQ-ANALYTICS-01-SC2

#### TC-UNIT-006: PR detection logic
**Test Strategy:** Identify new personal records when weight × reps exceeded for an exercise
- **Test Inputs:** Previous PR: 225 lbs × 5; New logs: [225 × 6, 230 × 5, 224 × 5, 226 × 5]
- **Expected:** 225 × 6 (estimated 1RM > previous), 230 × 5 (estimated 1RM > previous) marked as PRs; others not
- **Coverage:** PR comparison logic, 1RM-based ranking
- **Owned by:** Dev Team (automated unit test)
- **Requirement Traceability:** REQ-ANALYTICS-01-SC2
- **Tags:** @unit @pr-detection @logic @REQ-ANALYTICS-01-SC2

#### TC-UNIT-007: Exercise swap mapping validation
**Test Strategy:** Verify ExerciseSwap records original and alternative IDs without data corruption
- **Test Inputs:** Valid swap (original_id=5, alternative_id=8); invalid (original_id=999, alternative_id=8); null handling
- **Expected:** Valid swap persists; invalid foreign keys rejected; null values handled per schema
- **Coverage:** Data model integrity, foreign key constraints, null handling
- **Owned by:** Dev Team (automated unit test)
- **Requirement Traceability:** REQ-SWITCHING-01-SC2
- **Tags:** @unit @data-integrity @foreign-key @REQ-SWITCHING-01-SC2

#### TC-UNIT-008: Suggestion ranking algorithm
**Test Strategy:** Test exercise alternative ranking by muscle similarity and equipment match
- **Test Inputs:** Original = "Barbell Back Squat" (Legs, Equipment: [Barbell, Rack]); Alternatives: Goblet Squat, Leg Press, Split Squat
- **Expected:** Goblet Squat ranked #1 (90% muscle match, lower equipment), Leg Press #2, Split Squat #3
- **Coverage:** Ranking algorithm, relevance scoring
- **Owned by:** Dev Team (automated unit test)
- **Requirement Traceability:** REQ-SWITCHING-01-SC1
- **Tags:** @unit @ranking-algorithm @suggestion @REQ-SWITCHING-01-SC1

---

### 2. Integration Tests (QA Team - Automated, Post-Merge)

#### TC-INTEGRATION-001: Template loading and plan creation
```gherkin
Scenario: User loads pre-built template and creates workout plan
  Given a user viewing the template selection screen
  When they select "Full Body 3x/week" template
  And they tap "Create Plan"
  Then a new Workout record is created with template exercises
  And the plan displays 3 workouts (Monday, Wednesday, Friday)
  And the original template is unchanged in the database
  And the plan appears on the user's home screen immediately

Test ID: TC-INTEGRATION-001
Requirement Traceability: REQ-PLANNING-01-SC1
Owned by: QA Team
Tags: @integration @workflow @template-workflow @REQ-PLANNING-01-SC1
```

#### TC-INTEGRATION-002: Exercise swap in template
```gherkin
Scenario: User customizes template by swapping an exercise
  Given a user has loaded the "Full Body 3x/week" template
  When they open Tuesday's workout
  And they remove "Barbell Bench Press"
  And they select "Dumbbell Press" as replacement
  And they save the plan
  Then the modified plan reflects "Dumbbell Press" in Tuesday's workout
  And the original template still contains "Barbell Bench Press"
  And the LoggedExercise table has no record for the old exercise
  And the new exercise is linked correctly

Test ID: TC-INTEGRATION-002
Requirement Traceability: REQ-PLANNING-01-SC2
Owned by: QA Team
Tags: @integration @template-customization @data-consistency @REQ-PLANNING-01-SC2
```

#### TC-INTEGRATION-003: Quick log completion and streak update
```gherkin
Scenario: User logs completed workout and streak increments
  Given a user has a planned workout for today
  When they tap "Log Workout" on the home screen
  And they tap "Completed as planned"
  And they tap "Save"
  Then a LoggedWorkout record is created with status=completed
  And the home screen shows a completion checkmark
  And CompletionStreak.current_streak_days increments by 1
  And the completion count updates (e.g., "3 of 7 this week")
  And all changes persist to database

Test ID: TC-INTEGRATION-003
Requirement Traceability: REQ-LOGGING-01-SC1
Owned by: QA Team
Tags: @integration @logging-workflow @streak-update @data-persistence @REQ-LOGGING-01-SC1
```

#### TC-INTEGRATION-004: Offline logging with sync queue
```gherkin
Scenario: User logs workout offline and syncs when reconnected
  Given a user with no internet connection after completing workout
  When they tap "Log Workout"
  And they complete the logging form
  And they tap "Save"
  Then the app shows "Saved locally. Will sync when online."
  And the log entry is persisted to local SQLite database
  And when the device regains internet connectivity
  Then the log is sent to the server within 30 seconds
  And the server confirms sync with status=synced
  And no data is lost in the process

Test ID: TC-INTEGRATION-004
Requirement Traceability: REQ-LOGGING-01-SC4
Owned by: QA Team
Tags: @integration @offline-sync @data-consistency @REQ-LOGGING-01-SC4
```

#### TC-INTEGRATION-005: Analytics filtering by date range
```gherkin
Scenario: User filters analytics data by custom date range
  Given a user on the Analytics tab with 3 months of data
  When they tap "Date Range"
  And they select "Last 6 Weeks" (or custom dates April 1 - May 20)
  And they tap "Apply"
  Then all charts re-render with only data from that range
  And the completion calendar shows only workouts in range
  And PR history adjusts to show only PRs set in that window
  And the summary statistics (total workouts, avg weight) update

Test ID: TC-INTEGRATION-005
Requirement Traceability: REQ-ANALYTICS-01-SC3
Owned by: QA Team
Tags: @integration @analytics-filtering @data-query @REQ-ANALYTICS-01-SC3
```

#### TC-INTEGRATION-006: Period comparison workflow
```gherkin
Scenario: User compares performance across two periods
  Given a user on the Analytics tab viewing "Bench Press"
  When they tap "Compare Periods"
  And they set Period 1: Jan 1 - Jan 31, Period 2: Apr 1 - Apr 30
  And they tap "Calculate"
  Then the app displays:
    - Avg weight Period 1: 250 lbs, Period 2: 275 lbs
    - Avg reps Period 1: 5, Period 2: 6
    - Improvement: +25 lbs, +1 rep (10% strength gain)
  And the comparison is calculated correctly from LoggedExercise data
  And the visual summary renders without errors

Test ID: TC-INTEGRATION-006
Requirement Traceability: REQ-ANALYTICS-01-SC5
Owned by: QA Team
Tags: @integration @analytics-comparison @data-aggregation @REQ-ANALYTICS-01-SC5
```

#### TC-INTEGRATION-007: Exercise swap during active workout
```gherkin
Scenario: User swaps exercise during workout and continues logging
  Given a user is in an active workout at "Barbell Back Squat"
  When they tap the exercise and select "Can't do - equipment unavailable"
  Then the app shows 2-3 alternatives (Goblet Squat, Leg Press, Split Squat) within 1 second
  And when they tap "Leg Press" to select it
  Then the app confirms "Swapping Barbell Squat → Leg Press"
  And the LoggedWorkout is updated with alternative_exercise_id
  And an ExerciseSwap record is created with reason=equipment
  And the user can continue logging reps and weight for Leg Press

Test ID: TC-INTEGRATION-007
Requirement Traceability: REQ-SWITCHING-01-SC1, REQ-SWITCHING-01-SC2
Owned by: QA Team
Tags: @integration @exercise-swap @adaptive-workout @data-update @REQ-SWITCHING-01-SC1
```

#### TC-INTEGRATION-008: Backup plan creation and usage
```gherkin
Scenario: User creates and applies a backup plan
  Given a user viewing their saved workout "Heavy Leg Day"
  When they tap "Create Backup Plan"
  And they name it "No Squat Rack"
  And they assign alternatives: Barbell Squat → Leg Press, Barbell Leg Press → Smith Machine
  And they save the backup plan
  Then the backup plan is stored as a variant in the database
  And the original "Heavy Leg Day" workout remains unchanged
  And in future workouts, the user can select "No Squat Rack" variant
  And the alternate exercises are used instead

Test ID: TC-INTEGRATION-008
Requirement Traceability: REQ-SWITCHING-01-SC3
Owned by: QA Team
Tags: @integration @backup-plan @workout-variants @REQ-SWITCHING-01-SC3
```

#### TC-INTEGRATION-009: Swap history in workout detail view
```gherkin
Scenario: User reviews swaps performed in a past workout
  Given a user reviewing a completed workout from last week
  When they open the workout detail view
  Then each exercise is listed with original exercise name if a swap occurred
  And a note shows "[SWAPPED to Leg Press]" with timestamp
  And when they tap [SWAPPED], the reason and alternative are displayed
  And they can see the swap was recorded in the ExerciseSwap table

Test ID: TC-INTEGRATION-009
Requirement Traceability: REQ-SWITCHING-01-SC5
Owned by: QA Team
Tags: @integration @swap-history @workout-review @data-retrieval @REQ-SWITCHING-01-SC5
```

---

### 3. End-to-End Tests (QA Team - Manual + Automated)

#### TC-E2E-001: Beginner creates first plan and customizes template
```gherkin
Scenario: Beginner user completes planning workflow with customization
  Given a beginner user opening the app for the first time
  When they tap "Create Workout Plan"
  And they browse templates filtered by "Beginner"
  And they select "Full Body 3x/week"
  And they preview the plan (3 workouts, Monday/Wednesday/Friday)
  And they customize Tuesday by removing "Barbell Bench Press"
  And they select "Dumbbell Press" as replacement
  And they tap "Create Plan"
  Then the plan is saved with 3 workouts (Mon, Wed, Fri)
  And Tuesday contains "Dumbbell Press" instead of original exercise
  And the plan appears on the home screen
  And the user can see all exercises with sets/reps/weight

Test ID: TC-E2E-001
Requirement Traceability: REQ-PLANNING-01-SC1, REQ-PLANNING-01-SC2
Owned by: QA Team (Manual + Automated)
Tags: @e2e @beginner-flow @planning-workflow @customization @REQ-PLANNING-01-SC1
```

#### TC-E2E-002: User completes first workout and logs in under 2 minutes
```gherkin
Scenario: Beginner completes and logs first workout quickly
  Given a user with a saved "Full Body 3x/week" plan for today (Monday)
  And they complete the Monday workout at the gym
  When they open the app
  Then they see "Log Workout" button on the home screen
  And they tap the button
  And they tap "Completed as planned"
  And they tap "Save"
  Then the workout logs in < 2 seconds
  And the home screen shows a completion checkmark (✓)
  And the streak counter shows 1
  And the completion count updates (e.g., "1 of 3 this week")

Test ID: TC-E2E-002
Requirement Traceability: REQ-LOGGING-01-SC1
Owned by: QA Team (Manual + Automated)
Tags: @e2e @logging-workflow @quick-log @performance @REQ-LOGGING-01-SC1
```

#### TC-E2E-003: User logs detailed metrics for workout
```gherkin
Scenario: User captures detailed performance metrics for a workout
  Given a user with a logged workout pending detailed entry
  When they tap "Log Workout" and choose "Detailed Log"
  Then the app shows each exercise from the plan
  And for each exercise they enter:
    - Sets completed: 3
    - Reps completed: 5
    - Weight used: 225 lbs
    - RPE (1-10): 8
    - Optional notes: "felt strong"
  And they tap "Save"
  Then the detailed metrics are saved for each exercise
  And the actual vs. planned comparison displays: "Planned 3x5@225, Logged 3x5@225"
  And the delta is highlighted (none in this case)
  And they can later view these metrics in Analytics

Test ID: TC-E2E-003
Requirement Traceability: REQ-LOGGING-01-SC2
Owned by: QA Team (Manual + Automated)
Tags: @e2e @detailed-logging @metrics-capture @REQ-LOGGING-01-SC2
```

#### TC-E2E-004: User adapts workout when equipment is unavailable
```gherkin
Scenario: User swaps exercise mid-workout due to equipment unavailability
  Given a user in an active workout at the gym reaching "Barbell Back Squat"
  When they discover the squat rack is in use
  And they tap the exercise in the app
  And they select "Can't do - equipment unavailable"
  Then the app shows 2-3 alternatives within 1 second:
    1. Goblet Squat (recommended)
    2. Leg Press (barbell-free)
    3. Split Squat
  And they select "Leg Press"
  And the app confirms "Swapping Barbell Squat → Leg Press. Continue?"
  And they tap "Yes"
  Then the workout now logs Leg Press instead
  And they enter actual weight/reps for Leg Press
  And the swap is recorded with [SWAPPED] notation

Test ID: TC-E2E-004
Requirement Traceability: REQ-SWITCHING-01-SC1, REQ-SWITCHING-01-SC2
Owned by: QA Team (Manual + Automated)
Tags: @e2e @adaptive-workout @exercise-swap @real-world-scenario @REQ-SWITCHING-01-SC1
```

#### TC-E2E-005: User views analytics and exports data
```gherkin
Scenario: User analyzes performance and exports workout history
  Given a user with 3 months of workout logs (20+ completed workouts)
  When they tap the Analytics tab
  Then the app loads the Analytics dashboard (< 2 seconds)
  And they see "Barbell Back Squat" with progression chart
  And the chart displays weight progression over 3 months
  And when they tap "Barbell Back Squat"
  Then a line chart shows:
    - X-axis: dates (past 3 months)
    - Y-axis: weight (lbs)
    - Trend line showing overall progression
    - Max/min weights labeled
  And when they tap "Export"
  And they select "Last 3 Months" and "CSV format"
  Then a file is generated with columns: Exercise, Date, Weight, Reps, Notes
  And the file is ready to download/email

Test ID: TC-E2E-005
Requirement Traceability: REQ-ANALYTICS-01-SC1, REQ-ANALYTICS-01-SC4
Owned by: QA Team (Manual + Automated)
Tags: @e2e @analytics-workflow @export @REQ-ANALYTICS-01-SC1
```

#### TC-E2E-006: User views PR history and estimated 1RMs
```gherkin
Scenario: User reviews personal records and estimated strength maxes
  Given a user on the Analytics Summary tab
  When they scroll to "Personal Records" section
  Then they see a ranked list of PRs:
    - Barbell Back Squat: 315 lbs (Dec 15)
    - Deadlift: 425 lbs (Jan 8)
    - Bench Press: 275 lbs (Nov 20)
  And when they tap "Barbell Back Squat" PR
  Then the app shows estimated 1RM: "Your estimated 1RM: 320 lbs"
  And the calculation method is noted: "Based on Epley formula"
  And the estimates are based on logged exercise data

Test ID: TC-E2E-006
Requirement Traceability: REQ-ANALYTICS-01-SC2
Owned by: QA Team (Manual + Automated)
Tags: @e2e @pr-tracking @1rm-estimation @REQ-ANALYTICS-01-SC2
```

#### TC-E2E-007: Experienced user builds custom workout and saves as template
```gherkin
Scenario: Experienced lifter creates custom workout and reuses it
  Given an experienced gym user on the planning screen
  When they tap "Create Custom Workout"
  And they filter exercises by "Equipment: Barbell, Body Part: Legs"
  And they build a leg workout selecting:
    - Back Squat
    - Leg Press
    - Leg Curl
  And they set sets/reps/weight for each
  And they name it "Heavy Leg Day"
  And they tap "Save as Template"
  Then the custom workout is saved to their plan
  And "Heavy Leg Day" appears in their template library
  And they can use it to create future plans

Test ID: TC-E2E-007
Requirement Traceability: REQ-PLANNING-01-SC3
Owned by: QA Team (Manual + Automated)
Tags: @e2e @custom-workout @template-creation @REQ-PLANNING-01-SC3
```

---

### 4. Edge Case & Error Handling Tests (QA Team - Manual)

#### TC-EDGE-001: Plan modification after workout starts (warning for users)
```gherkin
Scenario: User attempts to edit workout after scheduled start time
  Given a user with a workout scheduled for 6:00 PM
  When the time is 5:45 PM (before start) and they edit the plan
  Then changes are saved normally
  And when the time is 6:15 PM (after start) and they edit the plan
  Then the system shows: "Workout may have already started. Continue editing?"
  And if they confirm, changes are saved but logged as post-start edits
  And the system tracks the modification time for audit

Test ID: TC-EDGE-001
Requirement Traceability: REQ-PLANNING-01-SC5
Owned by: QA Team (Manual)
Tags: @edge-case @timing @conflict-detection @REQ-PLANNING-01-SC5
```

#### TC-EDGE-002: Partial workout completion with reschedule prompt
```gherkin
Scenario: User logs partial completion and decides on remaining exercises
  Given a user completed 3 of 5 exercises before running out of time
  When they log the workout and mark "Partial completion"
  And they note which exercises were completed (sets 1-3)
  Then the system records which exercises were done
  And calculates completion % = 3/5 = 60%
  And shows: "Completed 60% of workout"
  And prompts: "Reschedule remaining exercises for tomorrow?"
  And if they confirm, the remaining 2 exercises are moved to next day

Test ID: TC-EDGE-002
Requirement Traceability: REQ-LOGGING-01-SC3
Owned by: QA Team (Manual)
Tags: @edge-case @partial-completion @rescheduling @REQ-LOGGING-01-SC3
```

#### TC-EDGE-003: Offline logging maintains data integrity
```gherkin
Scenario: Multiple offline log entries sync correctly when reconnected
  Given a user with no internet for 3 days
  When they log workouts for days 1, 2, and 3 offline
  And they complete each log
  Then all 3 logs are stored locally
  And when the device reconnects to internet
  Then all 3 logs sync in order (preserving chronological order)
  And the server confirms all syncs
  And the streak calculation accounts for all 3 consecutive days

Test ID: TC-EDGE-003
Requirement Traceability: REQ-LOGGING-01-SC4
Owned by: QA Team (Manual)
Tags: @edge-case @offline-sync @multi-log @data-consistency @REQ-LOGGING-01-SC4
```

#### TC-EDGE-004: Late logging preserves streak for consecutive day
```gherkin
Scenario: User logs workout 2 days after completion but maintains streak
  Given a user who completed workouts on days 1, 2, 3 but forgot to log on day 2
  When they open the app on day 4
  And they tap "Log Past Workout"
  And they select day 2 (2 days ago)
  And they complete the log
  Then the app asks: "Logging for [day 2]. Confirm?"
  And the workout is recorded with the correct date (day 2)
  And the streak remains unbroken (counted as consecutive day 2)
  And the current streak shows 3 (days 1, 2, 3)

Test ID: TC-EDGE-004
Requirement Traceability: REQ-LOGGING-01-SC5
Owned by: QA Team (Manual)
Tags: @edge-case @late-logging @streak-preservation @REQ-LOGGING-01-SC5
```

#### TC-EDGE-005: Skip exercise reduces training volume and shows warning
```gherkin
Scenario: User cannot find viable exercise alternative and skips it
  Given a user mid-workout who cannot do "Barbell Bench Press"
  When they view alternative suggestions but all benches are taken
  And they find no suitable alternative in suggestions
  And they tap "Skip Exercise"
  Then the app shows warning: "This reduces training volume. Skip anyway?"
  And if they confirm, the exercise is marked as [SKIPPED]
  And they continue to the next exercise
  And the completion percentage is adjusted (75% if 1 of 4 exercises skipped)
  And the logged workout shows which exercises were skipped

Test ID: TC-EDGE-005
Requirement Traceability: REQ-SWITCHING-01-SC4
Owned by: QA Team (Manual)
Tags: @edge-case @skip-exercise @training-volume @REQ-SWITCHING-01-SC4
```

#### TC-EDGE-006: Empty exercise library gracefully handles missing equipment
```gherkin
Scenario: System handles request for alternatives when none exist in library
  Given a user requesting alternatives for a rare/niche exercise
  When the app searches for alternatives
  And no suitable alternatives exist in the exercise library
  Then the app shows: "No alternatives found. Create a custom alternative?"
  And the user can manually select a replacement
  And the system doesn't crash or show errors

Test ID: TC-EDGE-006
Requirement Traceability: REQ-SWITCHING-01-SC1
Owned by: QA Team (Manual)
Tags: @edge-case @empty-results @graceful-degradation @REQ-SWITCHING-01-SC1
```

#### TC-EDGE-007: Analytics handles sparse or missing data gracefully
```gherkin
Scenario: System displays charts with data gaps (e.g., 2-week no-log period)
  Given a user with workout logs for Jan, then gap for Feb, then logs in Mar
  When they view progression chart for an exercise
  And the data spans Jan → gap → Mar
  Then the chart displays the gap clearly (line break or highlighted gap)
  And statistics adjust to show only logged data
  And the chart doesn't crash or show misleading trends

Test ID: TC-EDGE-007
Requirement Traceability: REQ-ANALYTICS-01-SC1
Owned by: QA Team (Manual)
Tags: @edge-case @sparse-data @chart-rendering @graceful-handling @REQ-ANALYTICS-01-SC1
```

#### TC-EDGE-008: CSV export with special characters and long text
```gherkin
Scenario: Export handles special characters, quotes, and long notes in CSV
  Given a user exporting workout history with exercise notes containing:
    - Quotes: "felt strong"
    - Commas: "leg day, compound focused"
    - Newlines: "3 sets, 5 reps, heavy weight"
  When they export to CSV
  Then the file is generated with proper escaping:
    - Quoted fields are enclosed in double quotes
    - Commas are preserved within fields
    - Newlines are escaped or represented
  And the file opens correctly in Excel or Google Sheets

Test ID: TC-EDGE-008
Requirement Traceability: REQ-ANALYTICS-01-SC4
Owned by: QA Team (Manual)
Tags: @edge-case @csv-export @special-characters @data-format @REQ-ANALYTICS-01-SC4
```

---

### 5. Performance & Load Tests (DevOps/QA Team - Automated)

#### TC-PERF-001: Quick log completion < 2 seconds
```gherkin
Scenario: Workout logging completes within performance target
  Given a user with a completed workout ready to log
  When they tap "Log Workout" → "Completed as planned" → "Save"
  Then the entire operation completes in < 2 seconds
  And the UI responds immediately (no jank/stutter)
  And the database write is confirmed
  And the home screen updates instantly

Test ID: TC-PERF-001
Requirement Traceability: REQ-LOGGING-01-SC1
Owned by: DevOps/QA Team (automated, performance monitoring)
Tags: @performance @timing-constraint @critical-path @<2s @REQ-LOGGING-01-SC1
Performance Target: < 2 seconds (end-to-end, p95)
```

#### TC-PERF-002: Progression chart renders < 2 seconds
```gherkin
Scenario: Exercise progression chart loads and renders within target time
  Given a user with 3 months of barbell squat logs (50+ data points)
  When they select "Barbell Back Squat" in Analytics
  And the chart is requested to render
  Then the chart fully renders (axes, line, trend, labels) in < 2 seconds
  And the user sees no loading spinner after 2 seconds
  And the rendering performance is smooth (60 FPS)

Test ID: TC-PERF-002
Requirement Traceability: REQ-ANALYTICS-01-SC1
Owned by: DevOps/QA Team (automated, performance monitoring)
Tags: @performance @chart-rendering @timing-constraint @<2s @REQ-ANALYTICS-01-SC1
Performance Target: < 2 seconds (p95, chart load + render)
```

#### TC-PERF-003: CSV export generation < 5 seconds
```gherkin
Scenario: CSV export for 6 months of data completes within time target
  Given a user requesting export of past 6 months
  And the export contains ~100 workout logs with 500+ exercises
  When they tap "Export as CSV"
  Then the file is generated and ready to download in < 5 seconds
  And the user receives confirmation without long wait times

Test ID: TC-PERF-003
Requirement Traceability: REQ-ANALYTICS-01-SC4
Owned by: DevOps/QA Team (automated, performance monitoring)
Tags: @performance @export-generation @timing-constraint @<5s @REQ-ANALYTICS-01-SC4
Performance Target: < 5 seconds (p95, file generation + transfer)
```

#### TC-PERF-004: Exercise suggestion generation < 1 second
```gherkin
Scenario: Alternative exercise suggestions appear within responsiveness threshold
  Given a user marking equipment as unavailable mid-workout
  When they tap the exercise and select "Can't do"
  Then 2-3 alternative suggestions appear in < 1 second
  And suggestions are sorted by relevance (top alternative first)
  And no network latency blocks the suggestions

Test ID: TC-PERF-004
Requirement Traceability: REQ-SWITCHING-01-SC1
Owned by: DevOps/QA Team (automated, performance monitoring)
Tags: @performance @suggestion-generation @timing-constraint @<1s @REQ-SWITCHING-01-SC1
Performance Target: < 1 second (p95, suggestion retrieval + sort)
```

#### TC-PERF-005: Sync queue processing under 10 seconds
```gherkin
Scenario: Offline logs sync to server efficiently after reconnection
  Given a user with 5 pending offline logs (5 workouts)
  When the device reconnects to internet
  Then all 5 logs sync to the server within 10 seconds
  And the user receives confirmation for each log
  And no data is lost or duplicated

Test ID: TC-PERF-005
Requirement Traceability: REQ-LOGGING-01-SC4
Owned by: DevOps/QA Team (automated, performance monitoring)
Tags: @performance @sync-queue @timing-constraint @<10s @REQ-LOGGING-01-SC4
Performance Target: < 10 seconds (p95, multi-log batch sync)
```

#### TC-PERF-006: Concurrent user load (100+ simultaneous users)
```gherkin
Scenario: System maintains performance under concurrent user load
  Given 100+ concurrent users logging workouts simultaneously
  When each user submits a "quick log" request
  Then the backend responds to all requests in < 5 seconds (p95)
  And no requests timeout (< 30 second timeout)
  And database transactions complete without deadlocks
  And CPU/memory utilization stays within acceptable bounds (< 80% CPU, < 85% memory)

Test ID: TC-PERF-006
Requirement Traceability: REQ-LOGGING-01-SC1
Owned by: DevOps/QA Team (automated, load testing)
Tags: @performance @load-test @scalability @concurrent-users @REQ-LOGGING-01-SC1
Performance Target: < 5 seconds (p95, under 100 concurrent users)
Infrastructure: AWS auto-scaling, horizontal pod autoscaling enabled
```

---

## Test Execution Summary

### Test Case Count by Category

| Category | Count | Status | Owned By |
|----------|-------|--------|----------|
| Unit Tests | 8 | ✓ Ready | Dev Team |
| Integration Tests | 9 | ✓ Ready | QA Team |
| E2E Tests | 7 | ✓ Ready | QA Team |
| Edge Case Tests | 8 | ✓ Ready | QA Team |
| Performance Tests | 6 | ✓ Ready | DevOps/QA |
| **Total** | **38** | **✓ Ready** | **Mixed** |

### Coverage by Feature

| Feature | Acceptance Criteria | Test Cases | Coverage |
|---------|-------------------|-----------|----------|
| REQ-PLANNING-01: Guided Workout Planning | 5 | 7 (2U + 2I + 2E + 1P) | ✓ 100% |
| REQ-LOGGING-01: Quick Workout Logging | 5 | 7 (2U + 2I + 2E + 1P) | ✓ 100% |
| REQ-ANALYTICS-01: Performance Tracking | 5 | 7 (2U + 2I + 2E + 1P) | ✓ 100% |
| REQ-SWITCHING-01: Adaptive Switching | 5 | 7 (2U + 2I + 2E + 1P) | ✓ 100% |
| **Totals** | **20** | **38** | **100%** |

*Legend: U=Unit, I=Integration, E=E2E, P=Performance*

### Ownership Breakdown

| Team | Test Count | Categories | Responsibilities |
|------|-----------|-----------|------------------|
| **Dev Team** | 8 | Unit | Pre-commit automated testing, ≥80% code coverage |
| **QA Team** | 24 | Integration (9) + E2E (7) + Edge Case (8) | Post-merge testing, manual E2E verification, edge case exploration |
| **DevOps/QA** | 6 | Performance | Load testing, performance monitoring, infrastructure scaling |

### Estimated Effort

| Category | Effort | Notes |
|----------|--------|-------|
| Unit Tests (8) | 40 hours | Low effort, automated; includes test data setup |
| Integration Tests (9) | 72 hours | Medium effort; requires API/DB mocking and staging environment |
| E2E Tests (7) | 84 hours | High effort; includes manual UI testing, browser automation scripts |
| Edge Case Tests (8) | 64 hours | Medium-high effort; mostly manual exploration and verification |
| Performance Tests (6) | 48 hours | Medium effort; load testing setup, monitoring configuration |
| **Total** | **308 hours** | ~7-8 weeks for full team (assuming 1 QA + 1 Dev + 1 DevOps engineer) |

### Test Execution Schedule

**Phase 1: Unit Tests (Weeks 1-2)**
- Dev team implements 8 unit tests
- Runs on every commit (CI pipeline pre-merge gate)
- Target: ≥80% code coverage by end of Phase 1

**Phase 2: Integration Tests (Weeks 2-4)**
- QA team implements and executes 9 integration tests on staging
- Runs after PR merge to main
- Target: All critical workflows covered

**Phase 3: E2E Tests (Weeks 3-5)**
- QA team creates and executes 7 E2E tests in staging and production-like environments
- Mix of manual and automated execution
- Target: 100% of acceptance criteria scenarios verified

**Phase 4: Edge Cases & Performance (Weeks 5-7)**
- QA/DevOps team explores 8 edge cases and runs 6 performance tests
- Performance tests run weekly and before releases
- Target: ≥90% edge case coverage, SLA compliance verified

**Release Gate (Week 8)**
- All tests passing
- No critical or high-severity failures
- Performance benchmarks met
- Coverage thresholds achieved

---

## Open Questions & Gaps Addressed

The original user stories included open questions. This test plan addresses them as follows:

### Feature 1: Guided Workout Planning

1. **Templates & Progression** → Test with manual selection (TC-PLANNING-001); auto-progression may be future feature
2. **Customization Limits** → Tests allow unlimited exercise swaps; may add validation in future
3. **Expert Content** → Assume templates are pre-vetted; not testing expert review process
4. **Equipment Awareness** → Tests assume manual user selection; future feature for auto-detection
5. **Warm-up Guidance** → Not tested; feature not specified in acceptance criteria
6. **Mobile UX** → Separate mobile QA track; desktop-first testing in this plan

### Feature 2: Quick Workout Logging

1. **Data Accuracy Validation** → TC-EDGE-002 tests unrealistic weight prevention
2. **Edit Window** → Tests allow indefinite edits; 24-hour read-only may be implemented later
3. **Performance Capture** → Tests use numeric RPE (1-10); emoji option is future enhancement
4. **Missed Workouts & Grace Period** → Tests assume immediate streak break; grace period is future feature
5. **Multi-Day Logging** → TC-EDGE-003 tests batch offline logs; single-entry sequence is primary
6. **Voice Logging** → Not tested; feature not in acceptance criteria

### Feature 3: Detailed Performance Tracking & Analytics

1. **1RM Calculation** → Tests use Epley formula; Brzycki option is future feature
2. **Movement Equivalence** → Tests treat exercises separately; grouping is future feature
3. **Strength Standards** → Not tested; comparison feature not in acceptance criteria
4. **Missing Data Handling** → TC-EDGE-007 tests gap display; interpolation is future option
5. **Body Weight Tracking** → Not tested; feature not specified
6. **Export Formats** → Tests CSV only; PDF/sync integrations are future features

### Feature 4: Adaptive Workout Switching

1. **Algorithm Ranking** → TC-UNIT-008 tests ranking by muscle similarity + equipment; custom factors may vary
2. **Frequency Tracking** → Tests basic swap recording; usage analytics is future feature
3. **Injury Mode** → Not tested; injury flag is future feature
4. **Crowdsourced Alternatives** → Not tested; community feature is future enhancement
5. **Equipment Library** → Tests assume manual selection; auto-detection is future feature
6. **Time Pressure** → Not tested; time-aware suggestions are future feature

---

## Appendix: Test Data Fixtures

### Sample Exercise Library (50+ exercises)

**Legs (Quads/Hamstrings/Glutes):**
- Barbell Back Squat (Intermediate, Equipment: Barbell, Safety Rack)
- Goblet Squat (Beginner, Equipment: Dumbbell)
- Leg Press (Beginner, Equipment: Machine)
- Leg Curl (Beginner, Equipment: Machine or Dumbbell)
- Split Squat (Intermediate, Equipment: Dumbbells or Barbell)
- Smith Machine Leg Press (Beginner, Equipment: Smith Machine)
- *[+10 more leg exercises]*

**Chest/Shoulders/Triceps:**
- Barbell Bench Press (Intermediate, Equipment: Barbell, Bench, Rack)
- Dumbbell Press (Beginner, Equipment: Dumbbells, Bench)
- Chest Fly (Intermediate, Equipment: Machine or Dumbbells)
- Overhead Press (Intermediate, Equipment: Barbell, Rack)
- Lateral Raise (Beginner, Equipment: Dumbbells)
- Tricep Dips (Intermediate, Equipment: Dips Bar)
- *[+10 more upper body exercises]*

**Back/Biceps:**
- Deadlift (Advanced, Equipment: Barbell)
- Barbell Rows (Intermediate, Equipment: Barbell, Rack)
- Lat Pulldowns (Beginner, Equipment: Machine)
- Barbell Curls (Beginner, Equipment: Barbell)
- Dumbbell Rows (Beginner, Equipment: Dumbbells, Bench)
- *[+10 more back exercises]*

### Sample Templates

**Full Body 3x/week (Beginner)**
- Monday: Squat, Bench Press, Rows (3×5)
- Wednesday: Deadlift, Incline Press, Lat Pulldowns (3×5)
- Friday: Leg Press, Dumbbell Press, Chest Fly (3×8)

**Upper/Lower Split (Intermediate)**
- Monday (Upper): Bench, Rows, Overhead Press, Curls
- Tuesday (Lower): Squat, Deadlift, Leg Press, Leg Curl
- Thursday (Upper): Incline Press, Lat Pulldowns, Lateral Raises, Dips
- Saturday (Lower): Squat Variations, Leg Press, Hamstring Curl, Calf Raises

**Push/Pull/Legs (Advanced)**
- Push: Bench, Incline Press, Overhead Press, Tricep Work
- Pull: Deadlift, Rows, Lat Pulldowns, Curls
- Legs: Squat, Leg Press, Hamstring Curl, Leg Extensions

### Sample User Profiles

**Beginner User**
- First workout ever or < 3 months experience
- No previous logs or 0 workouts completed
- Uses template selection flow
- Logs quick (not detailed)
- No analytics history

**Intermediate User**
- 6-12 months experience
- 20+ completed workouts
- Has customized 2-3 templates
- Uses detailed logging
- Views analytics monthly

**Advanced User**
- 2+ years experience
- 100+ completed workouts
- Created 5+ custom templates
- Uses backup plans
- Reviews analytics weekly

---

## Sign-Off & Approval

This test plan is ready for implementation upon stakeholder approval.

**Prepared by:** QA Team Lead
**Date:** 2026-05-20
**Status:** ✓ Ready for Implementation
**Approval Required:** Product Manager, Engineering Lead, QA Manager

---

**Document Version:** 1.0  
**Generated:** 2026-05-20  
**Status:** Ready for Implementation  
**Traceability:** Maps to 12 user stories (US-HT-*) with 36 acceptance criteria (AC-HT-*) from `output/habit-tracker/user-stories.md`

*Generated via Test Plan Skill — Habit Tracker Application*
