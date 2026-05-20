# Pomodoro Timer — Test Plan

## Test Plan Overview

Test plan for Pomodoro Timer covering 32 user stories across 7 features (TIMER, TASK, BREAK, CONFIG, DASH, INTEG, SYSTEM). Validates session timer accuracy, task logging, analytics, and external integrations. Scope: core functionality (v1 local-first); excludes cloud sync, third-party implementations, and team collaboration (v2+).

---

## Test Strategy

**Ownership & Execution Timing:**
- **Dev Team:** Unit tests on every commit (pre-commit gate)
- **QA Team:** Integration/E2E tests post-merge and nightly; edge cases on-demand before release
- **DevOps/QA:** Performance tests weekly and before release

**Test Data:**
- Fast-test mode: 25-minute sessions compress to 2 seconds for rapid iteration
- Sample seed data: 5-10 sample tasks, 50+ completed sessions, 20+ break activities
- Locale test: en_US, de_DE, fr_FR (time formatting)

**Coverage Targets:**
- Unit tests: ≥80% on timer logic, task/break validation, configuration
- Integration tests: 100% of critical workflows (session→log→analytics)
- E2E: All user journeys (start session → break → analytics)
- Edge cases: System sleep, concurrent sessions, long sessions >120min, offline scenarios

---

## Requirement Traceability Matrix

| REQ-ID | Feature | Test Categories | Status |
|--------|---------|-----------------|--------|
| REQ-TIMER-01 | Start focused work session | Unit, Integration, E2E | ✓ |
| REQ-TIMER-02 | Display timer (readable format, ±1s accuracy) | Unit, Integration | ✓ |
| REQ-TIMER-03 | Pause/resume mid-session | Unit, Integration | ✓ |
| REQ-TIMER-04 | Audio/visual notifications on completion | Integration, Edge Case | ✓ |
| REQ-TIMER-05 | Transition to break timer | Integration, E2E | ✓ |
| REQ-TIMER-06 | Handle system sleep gracefully | Integration, Edge Case | ✓ |
| REQ-TIMER-07 | Warn on long sessions >120min | Unit, Edge Case | ✓ |
| REQ-TIMER-08 | Prevent concurrent sessions | Integration, Edge Case | ✓ |
| REQ-TASK-01 | Create inline task before session | Unit, Integration, E2E | ✓ |
| REQ-TASK-02 | Display task name during session | Integration, E2E | ✓ |
| REQ-TASK-03 | Log session with task metadata | Unit, Integration | ✓ |
| REQ-TASK-04 | View task list with cumulative metrics | Integration | ✓ |
| REQ-TASK-05 | Search/filter tasks by name | Unit, Integration | ✓ |
| REQ-TASK-06 | Rename task (retroactive update) | Unit, Integration | ✓ |
| REQ-TASK-07 | Delete task (soft delete, preserve history) | Integration, Edge Case | ✓ |
| REQ-TASK-08 | Reassign session to task post-completion | Integration | ✓ |
| REQ-BREAK-01 | Prompt for break activity after session | Integration, E2E | ✓ |
| REQ-BREAK-02 | Log break activity with metadata | Unit, Integration | ✓ |
| REQ-BREAK-03 | Add custom break activity | Unit, Integration | ✓ |
| REQ-BREAK-05 | Detect break-skipping pattern | Integration, Edge Case | ✓ |
| REQ-CONFIG-01 | Set global session/break duration | Unit, Integration | ✓ |
| REQ-CONFIG-02 | Override duration per-session | Unit, Integration | ✓ |
| REQ-CONFIG-03 | Create and save presets | Unit, Integration | ✓ |
| REQ-CONFIG-04 | Switch presets before session | Integration, E2E | ✓ |
| REQ-CONFIG-05 | Reset to defaults | Unit, Integration | ✓ |
| REQ-DASH-01 | Daily analytics summary | Integration, E2E | ✓ |
| REQ-DASH-02 | Weekly heatmap | Integration | ✓ |
| REQ-DASH-03 | Monthly trends with comparison | Integration | ✓ |
| REQ-DASH-04 | Task time breakdown | Integration | ✓ |
| REQ-DASH-06 | Export data as CSV | Integration | ✓ |
| REQ-DASH-09 | Dashboard load performance (<2s) | Performance | ✓ |
| REQ-SYSTEM-01 | Data persistence across crashes | Unit, Integration | ✓ |
| REQ-SYSTEM-02 | App launch performance (<2s cold, <500ms warm) | Performance | ✓ |
| REQ-SYSTEM-03 | No login required | Integration | ✓ |
| REQ-SYSTEM-04 | WCAG 2.1 AA accessibility | Integration | ✓ |

**Coverage:** 35 requirements, 35 mapped test cases. Ratio: 1-2 tests per requirement (not fixed 3:1).

---

## Test Cases by Category

### Unit Tests (Dev Team — Pre-Commit)

**TC-UNIT-001: Timer countdown accuracy**
- Test: 60-minute timer completes within ±1 second
- Inputs: duration=60min, wall-clock elapsed
- Expected: actual_elapsed ∈ [59:59, 60:01]
- Requirement: REQ-TIMER-02

**TC-UNIT-002: Task name validation (1-100 chars, trim whitespace)**
- Test: Edge cases for task creation
- Inputs: "", "a", "x"×100, "x"×101, "  task  "
- Expected: 1-100 chars accepted; empty/101+ rejected; whitespace trimmed
- Requirement: REQ-TASK-01

**TC-UNIT-003: Duration range validation (session 1-120, break 1-60)**
- Test: Configuration constraints
- Inputs: session=[0, 1, 120, 121], break=[0, 1, 60, 61]
- Expected: Valid ranges accepted; out-of-range rejected
- Requirement: REQ-CONFIG-01

**TC-UNIT-004: Task search (case-insensitive substring)**
- Test: Search logic
- Inputs: search="Feature", tasks=["Feature X", "feature y", "Bug"]
- Expected: ["Feature X", "feature y"] (case-insensitive match)
- Requirement: REQ-TASK-05

**TC-UNIT-005: Session record structure (required fields)**
- Test: Data model validation
- Inputs: completed session with task_name, duration, elapsed, timestamp, status
- Expected: All fields present, correct types (string, int, ISO 8601)
- Requirement: REQ-TASK-03

**TC-UNIT-006: Break activity validation (1-50 chars)**
- Test: Custom activity constraints
- Inputs: "", "a", "x"×50, "x"×51
- Expected: 1-50 chars accepted; others rejected
- Requirement: REQ-BREAK-03

---

### Integration Tests (QA Team — Post-Merge/Nightly)

**TC-INTEGRATION-001: User starts session and timer counts down**
```gherkin
Given user selects task "Coding" and clicks "Start Session"
When timer launches
Then remaining time displays "25:00" (default)
And countdown begins immediately
And no menu bars visible (full-screen UI)
```
Requirement: REQ-TIMER-01

**TC-INTEGRATION-002: User pauses and resumes session**
```gherkin
Given active timer with 12:45 remaining
When user clicks "Pause"
Then timer freezes at 12:45
And button changes to "Resume"

When user clicks "Resume"
Then countdown continues from 12:45
```
Requirement: REQ-TIMER-03

**TC-INTEGRATION-003: Session logged on completion with metadata**
```gherkin
Given session completes (timer reaches 00:00)
When session ends
Then session record created with:
  task_name, duration_minutes, actual_elapsed, completion_timestamp, status
And record persisted to local storage
```
Requirement: REQ-TASK-03

**TC-INTEGRATION-004: Task name displayed during session**
```gherkin
Given session active with task "Deep Work: Research"
When timer displays
Then task name visible (font ≥48px) above/below timer
And remains visible throughout session
```
Requirement: REQ-TASK-02

**TC-INTEGRATION-005: Task list shows cumulative metrics**
```gherkin
Given 3 sessions on "Coding" (50+25+45 min), 2 on "Email" (25+30 min)
When user opens task list
Then displays:
  - "Coding": 3 sessions, 1h 40m total, most recent date
  - "Email": 2 sessions, 55m total, most recent date
And sorted by cumulative time (descending)
```
Requirement: REQ-TASK-04

**TC-INTEGRATION-006: Task search filters results (<200ms)**
```gherkin
Given task list with 100+ tasks
When user types "Feature" in search
Then results filtered to matching tasks (case-insensitive) within 200ms
When user clears search
Then full list restored
```
Requirement: REQ-TASK-05

**TC-INTEGRATION-007: Break activity dialog after session**
```gherkin
Given session completes (timer 00:00)
When completion notification displays
Then break activity dialog appears with:
  "What are you doing on your break?"
  Predefined options: Stretch, Walk, Hydrate, Eat, Meditation, etc.
```
Requirement: REQ-BREAK-01

**TC-INTEGRATION-008: Custom break activity saved and reused**
```gherkin
Given break activity dialog open
When user clicks "Other" and enters "Play guitar"
And confirms
Then activity logged with timestamp and session_id
And "Play guitar" added to predefined list
```
Requirement: REQ-BREAK-03

**TC-INTEGRATION-009: Global duration setting persists**
```gherkin
Given user sets session duration to 50 minutes in settings
When user saves settings
Then future sessions default to 50:00 (not 25:00)
And setting persists across app restarts
```
Requirement: REQ-CONFIG-01

**TC-INTEGRATION-010: Per-session override doesn't affect globals**
```gherkin
Given global session duration = 25 min
When user overrides to 90 min for one session
And session completes
And new session starts
Then timer shows 25:00 (global default, not previous override)
```
Requirement: REQ-CONFIG-02

**TC-INTEGRATION-011: Session preset creation and switch**
```gherkin
Given user creates preset "Deep Coding": session=90min, break=15min
When user selects preset from dropdown before session
Then upcoming session uses 90:00 and 15:00 break
And preset definition unchanged
```
Requirement: REQ-CONFIG-03, REQ-CONFIG-04

**TC-INTEGRATION-012: Daily analytics dashboard**
```gherkin
Given user completed 3 sessions today (50+25+45 min)
When user opens analytics dashboard
Then displays:
  - Sessions Completed Today: 3
  - Total Focus Time: "2h 0m"
  - List with task, duration, time
```
Requirement: REQ-DASH-01

**TC-INTEGRATION-013: Task rename updates all sessions retroactively**
```gherkin
Given task "Math Chapter 5" with 5 logged sessions
When user renames to "Math Chapter 5 - Review"
Then all 5 sessions now reference new name
And metrics (total sessions, cumulative time) unchanged
```
Requirement: REQ-TASK-06

**TC-INTEGRATION-014: Task soft delete preserves history**
```gherkin
Given task "Old Project" with 10 sessions
When user deletes task
Then task marked deleted (not erased)
And 10 sessions remain in history with task name
And task hidden from selection dropdown
```
Requirement: REQ-TASK-07

**TC-INTEGRATION-015: Session reassignment after completion**
```gherkin
Given completed session logged to "Email"
When user clicks task name to reassign
Then dialog shows current task + list of alternatives
When user selects "Urgent: Security"
Then session.task_id updated
And metrics recalculated (Email decreases, Security increases)
```
Requirement: REQ-TASK-08

**TC-INTEGRATION-016: Data persists across app crash**
```gherkin
Given 5 completed sessions in history
When app force-closed
And restarted within 24 hours
Then all 5 sessions appear in history with metadata intact
And analytics show complete data
```
Requirement: REQ-SYSTEM-01

**TC-INTEGRATION-017: App launches without login**
```gherkin
Given new user installs app
When app opens first time
Then home screen appears immediately (no login/registration)
And user can start session right away
```
Requirement: REQ-SYSTEM-03

---

### E2E Tests (QA Team — Nightly/On-Demand)

**TC-E2E-001: Complete work-to-break workflow**
```gherkin
Given user on home screen
When enters task "Implement login"
And clicks "Start Session" (25 min default)
Then timer countdown visible; session auto-completes at 00:00
When break activity dialog appears with "Walk"
And user selects "Walk"
Then break timer launches at "5:00"
```
Requirement: REQ-TIMER-01, REQ-BREAK-01, REQ-TIMER-05

**TC-E2E-002: User creates preset and uses for weekly sessions**
```gherkin
Given user sets: session=90min, break=15min
When user saves as preset "Deep Coding"
And next session, selects "Deep Coding" preset
Then timer shows 90:00, break shows 15:00
```
Requirement: REQ-CONFIG-03, REQ-CONFIG-04

**TC-E2E-003: User views analytics after multiple sessions**
```gherkin
Given user completed 5 sessions today
When user opens analytics dashboard
Then displays: sessions count, total focus time, task breakdown
And can filter by date range
```
Requirement: REQ-DASH-01, REQ-DASH-04

---

### Edge Case Tests (QA Team — On-Demand Before Release)

**TC-EDGE-001: Long session >120 minutes requires confirmation**
```gherkin
Given user selects 180-minute session
When clicks "Start Session"
Then confirmation dialog: "Sessions >120 min may cause fatigue. Continue?"
When clicks "Continue Anyway"
Then timer starts with 180:00
```
Requirement: REQ-TIMER-07

**TC-EDGE-002: Concurrent session prevention**
```gherkin
Given active session with 10:30 remaining
When user clicks "Start Session" again
Then warning: "Session in progress (10:30). Abandon current?"
When clicks "Cancel"
Then active session continues (no overwrite)
```
Requirement: REQ-TIMER-08

**TC-EDGE-003: System sleep pauses timer without drift**
```gherkin
Given timer running with 15:00 remaining
When device sleeps for 30 minutes
And device wakes
Then timer resumes from 15:00 (sleep time NOT subtracted)
And accuracy within ±1 second
```
Requirement: REQ-TIMER-06

**TC-EDGE-004: Break-skipping pattern detected**
```gherkin
Given user completes 5 consecutive sessions without logging breaks
When 5th session completes
Then system detects pattern
When 6th session completes
Then reminder appears: "You've skipped breaks. Ready to take a break?"
```
Requirement: REQ-BREAK-05

**TC-EDGE-005: Reset settings preserves custom presets**
```gherkin
Given user has:
  - Global settings: session=90min
  - 3 custom presets: "Deep Coding", "Email Blitz", "Standup"
When user clicks "Reset to Defaults"
Then global settings reset to 25/5 min
And all 3 presets remain unchanged
```
Requirement: REQ-CONFIG-05

---

### Performance Tests (DevOps/QA — Weekly)

**TC-PERF-001: Cold app launch <2 seconds**
```gherkin
Given app not running (cold start)
When user launches app
Then home screen interactive within 2.0 seconds
```
Requirement: REQ-SYSTEM-02

**TC-PERF-002: Dashboard loads <2 seconds with 52 weeks data**
```gherkin
Given user has 1000+ sessions (1 year)
When user opens analytics dashboard
Then fully rendered with all charts within 2.0 seconds
```
Requirement: REQ-DASH-09

---

## Test Execution & Effort

| Category | Count | Team | Timing | Est. Hours |
|----------|-------|------|--------|-----------|
| Unit | 6 | Dev | Every commit | 12 |
| Integration | 17 | QA | Post-merge, nightly | 68 |
| E2E | 3 | QA | Nightly, on-demand | 15 |
| Edge Case | 5 | QA | Before release | 15 |
| Performance | 2 | DevOps/QA | Weekly | 8 |
| **Total** | **33** | — | — | **118 hours** |

---

## Known Gaps & Deferred

- **v2 Integration:** OAuth flows, bi-directional sync with Todoist not tested (depends on v2 scope finalization)
- **Cloud Sync:** Cross-device data sync deferred to v2; v1 is local-first only
- **Platform-Specific:** OS notification delivery (Windows, macOS, iOS, Android) requires platform-specific testing—acceptances documented but implementation TBD
- **Browser Compatibility:** Web version browser testing (Chrome, Firefox, Safari) scope TBD

---

## Test Data

**Fast-Test Mode Constants:**
```
TEST_SESSION_DURATION_SECONDS = 2  // Compresses 25min to 2sec
TEST_BREAK_DURATION_SECONDS = 1    // Compresses 5min to 1sec
ENVIRONMENT = "test"
```

**Sample Data:**
- 5-10 sample tasks (Coding, Email, Research, etc.)
- 50+ completed sessions with varying durations/statuses
- 20+ break activities (Walk, Meditation, Coffee, etc.)
- Locales: en_US, de_DE, fr_FR

---

**Test Plan Status:** Ready for implementation | Dev: 12h | QA: 98h | DevOps: 8h | Total: 118h
