# Test Plan: Habit Tracker

## Test Plan Overview

**Project:** Habit Tracker Mobile App

**Scope:** Comprehensive testing of 5 core features across 2 user personas, covering 14 user stories with 42+ acceptance criteria scenarios.

**Testing Approach:**
- **Unit Tests** (Dev Team): Automated, pre-commit, ≥80% code coverage
- **Integration Tests** (QA Team): Automated, post-merge, ≥60% critical workflows
- **E2E Tests** (QA Team): Manual + automated, nightly, 100% acceptance criteria
- **Edge Case Tests** (QA Team): Manual, pre-release, ≥90% edge cases
- **Performance Tests** (DevOps/QA): Automated, weekly, all critical paths <target time

---

## Test Strategy

### Ownership & Responsibilities

**Development Team:**
- Unit tests: Business logic, data validation
- Automated execution on every commit (pre-merge gate)
- Coverage goal: ≥80% code coverage

**QA Team:**
- Integration, E2E, edge case testing
- Manual + automated execution
- Coverage goal: ≥60% critical workflows, 100% acceptance criteria

**DevOps Team:**
- Performance testing and infrastructure
- CI/CD pipeline configuration
- Test environment setup

### Environment Setup

**Local Dev:**
- SQLite test database
- Mock API server for offline testing
- Test fixtures and seed data

**Staging:**
- PostgreSQL test database
- Full backend API (staging)
- Redis cache

**CI/CD Integration:**
```
Commit → Unit Tests (must pass)
  ↓
Code Coverage Check (≥80%)
  ↓
PR Merge → Integration Tests, E2E Smoke
  ↓
Nightly → Full Integration, Full E2E, Performance Regression
  ↓
Pre-Release → Edge Cases, Performance Load, Manual QA
```

### Dependencies & Tools

- **Testing Framework:** pytest (Python) or Jest (Node.js)
- **Database:** SQLite (local), PostgreSQL (staging)
- **API Mocking:** requests-mock or msw
- **Performance:** locust or k6
- **Coverage:** coverage.py or nyc

### Coverage Goals

| Category | Target | Rationale |
|----------|--------|-----------|
| Unit | ≥80% code coverage | Core logic thoroughly tested |
| Integration | ≥60% critical workflows | Major feature interactions |
| E2E | 100% acceptance criteria | Every user story scenario |
| Edge Cases | ≥90% documented cases | Error handling, boundaries |
| Performance | All critical paths <target | Response time requirements |
| **Overall** | **≥75% combined** | High quality, low risk |

---

## Test Objectives

1. Verify all 5 features function as specified
2. Validate both user personas complete core tasks
3. Ensure data integrity and persistence
4. Confirm performance requirements met (<500ms screens, <2s submissions)
5. Test offline-first architecture
6. Handle edge cases gracefully

---

## Test Scope

### In Scope

**Features:** Goal Setting, Logging, Progress Tracking, Plan Management, Analytics

**Quality Aspects:** Functional correctness, data persistence, performance, offline functionality, error handling

### Out of Scope

- Social features (Phase 2)
- Wearable integration (Phase 1)
- Nutrition tracking
- Native platform internals
- Backend infrastructure

---

## Test Cases by Category

### 1. Unit Tests (Dev Team)

**TC-UNIT-GOAL-001:** Goal value validation
- **Test:** Parse and validate goal inputs (0-10, negatives, strings)
- **Expected:** Valid inputs parsed; invalid rejected
- **Coverage:** Goal parsing and validation logic

**TC-UNIT-LOG-001:** Workout schema validation
- **Test:** Verify required (date, type) vs optional fields
- **Expected:** Complete and minimal records accepted; missing required fields rejected
- **Coverage:** WorkoutRecord schema enforcement

**TC-UNIT-PROG-001:** Progress percentage calculation
- **Test:** Calculate (completed/goal) × 100 with various inputs
- **Expected:** Correct percentage, rounded to 2 decimals
- **Coverage:** Math formula implementation

**TC-UNIT-PLAN-001:** Plan overlap detection
- **Test:** Allow multiple workouts same day (split sessions)
- **Expected:** Both stored; no error
- **Coverage:** Plan validation logic

**TC-UNIT-ANALYTICS-001:** 1RM progression calculation
- **Test:** Epley formula: 1RM = weight × (1 + reps/30)
- **Expected:** ±1 lb accuracy
- **Coverage:** Math formula, floating point precision

*[10+ additional unit tests for edge cases and calculation logic]*

---

### 2. Integration Tests (QA Team)

**TC-INTEG-GOAL-001:** Goal persistence across restart

```gherkin
Scenario: User sets goal, closes app, reopens and sees persisted goal
  Given a new user setting goal=3
  When they confirm and close the app
  And reopen the app
  Then the home screen displays "Goal: 3 workouts this week"
  And the goal persists correctly
```

**TC-INTEG-LOG-001:** Workout logging increments progress bar

```gherkin
Scenario: Logged workout updates progress immediately
  Given user with progress "1 of 3"
  When they log a workout
  Then progress bar updates to "2 of 3" without refresh
  And modal closes automatically
```

**TC-INTEG-LOG-002:** Offline sync when reconnected

```gherkin
Scenario: Offline workout syncs when connectivity restored
  Given app is offline
  When user logs a workout
  Then app shows "Saved locally. Will sync when online."
  And when device reconnects, sync runs automatically
```

**TC-INTEG-PROG-001:** Weekly summary aggregates correctly

```gherkin
Scenario: Summary displays count, duration, and goal status
  Given week with 3 workouts (60+70+50 min)
  When weekly summary viewed
  Then displays: 3 workouts, 180 min total, "Goal Met ✓"
```

**TC-INTEG-PLAN-001:** Plan renders on calendar

```gherkin
Scenario: Created plan appears on calendar
  Given user creates plan with 3 workouts
  When plan saved
  Then all 3 workouts display on calendar
  And persist across app restart
```

*[6+ additional integration tests]*

---

### 3. E2E Tests (QA Team)

**TC-E2E-001:** Newbie onboards, sets goal, logs, views progress

```gherkin
Scenario: Complete beginner journey
  Given new user opening app for first time
  When they set goal=3
  And log 3 workouts (Mon, Wed, Fri)
  And view progress
  Then progress bar shows "3 of 3"
  And weekly summary shows "Goal Met ✓"
```

**TC-E2E-002:** Gym Rat creates plan, adapts, logs detailed metrics

```gherkin
Scenario: Experienced user adapts when equipment unavailable
  Given Gym Rat with planned {Mon: Bench Press}
  When they arrive and equipment busy
  And pivot to {Dumbbell Press}
  And log metrics {weight: 75, reps: 8, RPE: 7}
  Then workout logged, progress increments
  And original plan unchanged
```

**TC-E2E-003:** Gym Rat analyzes progression and exports

```gherkin
Scenario: User views analytics and exports data
  Given user with 12 weeks of lift data
  When they open Analytics
  And filter to "Bench Press, last 8 weeks"
  Then report displays progression chart
  And export creates CSV with all lift data
```

---

### 4. Edge Case Tests (QA Team)

**TC-EDGE-001:** Goal of 0 accepted

```gherkin
Scenario: System accepts goal=0 (rest week)
  Given goal-setting screen
  When user enters 0
  Then system accepts without error
  And saves {goal_count: 0}
```

**TC-EDGE-002:** Prevents logging >90 days past

```gherkin
Scenario: Date picker disables dates >90 days old
  Given current date May 20, 2026
  When date picker opened
  Then dates before Feb 20, 2026 are disabled
  And tooltip: "Workouts older than 90 days cannot be logged"
```

**TC-EDGE-003:** Multiple workouts same day

```gherkin
Scenario: Split sessions on one day accepted
  Given plan with {Mon: Strength 60min, Cardio 30min}
  When both logged on Monday
  Then both recorded
  And progress shows "2 workouts today"
```

**TC-EDGE-004:** Goal change retroactive

```gherkin
Scenario: Mid-week goal change updates progress
  Given Wed, goal=3, logged=1
  When goal changed to 4
  Then progress bar shows "1 of 4"
  And change is retroactive for this week
```

**TC-EDGE-005:** Deletion reverts goal status

```gherkin
Scenario: Deleting workout after goal met reverts status
  Given 3 workouts logged, "Goal Met ✓" shown
  When one deleted
  Then progress "2 of 3", badge removed
```

**TC-EDGE-006:** Past-date workout in correct week

```gherkin
Scenario: Late logging counts toward its own week
  Given current date May 20 (Wed)
  When log workout {date: May 18 (Fri)}
  Then appears in May 12-18 week (not current week)
```

---

### 5. Performance Tests (DevOps/QA)

**TC-PERF-001:** Goal screen <500ms

```gherkin
Scenario: Onboarding goal screen loads within budget
  Given app launching for first time
  When goal-setting screen displayed
  Then renders in <500ms
  And all UI elements interactive
```

**TC-PERF-002:** Logging submission <2s

```gherkin
Scenario: Workout submission completes within SLA
  Given logging form filled
  When user submits
  Then local save <500ms
  And API response <2.0s total
  And modal closes, home screen updates
```

**TC-PERF-003:** Progress bar update <100ms

```gherkin
Scenario: UI updates immediately after logging
  Given progress showing "2 of 3"
  When new workout logged
  Then updates to "3 of 3" in <100ms
  And animation smooth
```

**TC-PERF-004:** Analytics with large dataset <1s

```gherkin
Scenario: Dashboard with 1000+ workouts loads fast
  Given user with 2 years data (500+ sessions)
  When analytics opened
  Then loads in <1.0 second
  And remains responsive
```

**TC-PERF-005:** Concurrent user load

```gherkin
Scenario: System handles 100 concurrent logging users
  Given 100 simulated users logging in parallel
  When all submit within 5 seconds
  Then all complete in <2s
  And error rate <0.5%
  And p95 response <500ms
```

---

## Traceability Matrix

| Requirement | Description | Test IDs | Coverage |
|---|---|---|---|
| REQ-HT-GOAL-01 | Set initial goal | TC-UNIT-GOAL-001, TC-INTEG-GOAL-001, TC-E2E-001, TC-PERF-001 | ✓ |
| REQ-HT-GOAL-02 | Adjust goal mid-week | TC-UNIT-GOAL-002, TC-INTEG-GOAL-002, TC-EDGE-004 | ✓ |
| REQ-HT-LOG-01 | Log basic workout | TC-UNIT-LOG-001, TC-INTEG-LOG-001, TC-INTEG-LOG-003, TC-E2E-001, TC-PERF-002 | ✓ |
| REQ-HT-LOG-02 | Log detailed metrics | TC-UNIT-LOG-002, TC-INTEG-LOG-002, TC-E2E-002 | ✓ |
| REQ-HT-LOG-03 | Log past-date | TC-UNIT-LOG-003, TC-EDGE-002, TC-EDGE-006 | ✓ |
| REQ-HT-PROG-01 | Progress bar | TC-UNIT-PROG-001, TC-INTEG-PROG-001, TC-E2E-001, TC-EDGE-005, TC-PERF-003 | ✓ |
| REQ-HT-PROG-02 | Weekly summary | TC-UNIT-PROG-002, TC-INTEG-PROG-002, TC-E2E-001 | ✓ |
| REQ-HT-PLAN-01 | Create plan | TC-UNIT-PLAN-001, TC-INTEG-PLAN-001, TC-E2E-002 | ✓ |
| REQ-HT-PLAN-02 | Pivot in-gym | TC-UNIT-PLAN-002, TC-INTEG-PLAN-002, TC-E2E-002, TC-EDGE-003 | ✓ |
| REQ-HT-ANALYTICS-01 | Analytics dashboard | TC-UNIT-ANALYTICS-001, TC-INTEG-ANALYTICS-001, TC-E2E-003, TC-PERF-004 | ✓ |
| REQ-HT-ANALYTICS-02 | Custom reports | TC-UNIT-ANALYTICS-002, TC-INTEG-ANALYTICS-002, TC-E2E-003 | ✓ |

**Coverage:** 11 of 11 requirements covered (100%)

---

## Test Execution Summary

| Category | Count | Team | Automated | Trigger |
|----------|-------|------|-----------|---------|
| Unit | 14 | Dev | 100% | Every commit |
| Integration | 11 | QA | 100% | Post-merge |
| E2E | 3 | QA | 80% | Nightly + manual |
| Edge Case | 6 | QA | 50% | Pre-release |
| Performance | 5 | DevOps/QA | 100% | Weekly + pre-release |
| **Total** | **39** | | **~85% automated** | |

### Estimated Effort

| Activity | Hours | Notes |
|----------|-------|-------|
| Unit test development | 40 | Dev team, parallel with features |
| Integration tests | 60 | QA team, post-development |
| E2E tests | 40 | QA team, manual + automation setup |
| Edge case testing | 30 | QA team, exploratory |
| Performance testing | 25 | DevOps/QA, infrastructure setup |
| **Total** | **195** | Spans development + QA phases |

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| Offline sync data loss | High | TC-INTEG-LOG-003 comprehensive testing |
| Concurrent goal edits | Medium | Lock/version control, TC-INTEG-GOAL-002 |
| Date boundary bugs | Medium | TC-EDGE-002, TC-EDGE-006 strict testing |
| Performance degradation | Medium | TC-PERF-004, TC-PERF-005 load testing |
| Plan/logging inconsistency | Low | TC-EDGE-003, TC-E2E-002 integration testing |

---

**End of Test Plan**
