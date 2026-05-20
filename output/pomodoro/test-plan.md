# Pomodoro Timer — Comprehensive Test Plan

---

## Test Plan Overview

This test plan covers the Pomodoro Timer application, a lightweight productivity tool enabling users to manage focus sessions through customizable timers, task tracking, break activity logging, and analytics. The plan encompasses unit, integration, end-to-end, edge case, and performance testing across 6 core features (TIMER, TASK, BREAK, CONFIG, DASH, INTEG) and system-wide concerns (SYSTEM).

**Scope:** All acceptance criteria from 32 user stories across 41 unique acceptance criteria scenarios
**Testing Approach:** Multi-layered testing (unit, integration, E2E, edge case, performance) with clear ownership boundaries
**Coverage Goal:** ≥75% combined code/scenario coverage; 100% of acceptance criteria mapped to test cases

---

## Test Strategy

### Ownership & Responsibilities

**Dev Team:**
- Unit tests: Individual component and business logic testing
- Code coverage: Maintain ≥80% on timer calculations, data validation, state management
- Execution: Pre-commit gate (fail = block merge)
- Tools: Jest/pytest, code coverage reporters

**QA Team:**
- Integration tests: Feature workflow and cross-component interaction
- E2E tests: Full user journey scenarios matching acceptance criteria
- Edge case testing: Boundary conditions, error handling, unusual states
- Manual testing: UI/UX validation, performance perception, accessibility
- Execution: Post-merge (integration/E2E nightly), on-demand (edge case/manual)

**DevOps Team:**
- Performance & load testing: Response time, concurrent operations, data volume handling
- Test environment setup: Local dev, staging, test database provisioning
- CI/CD pipeline: Test automation orchestration, fail notifications, coverage reporting
- Execution: Weekly (performance), nightly (E2E)

### Environment Setup

**Local Development:**
- Node.js 18+ (or Python 3.9+ for backend, if applicable)
- Test framework: Jest (frontend), pytest (backend)
- Mock/stub libraries: Jest mocks, sinon (for timers), nock (HTTP)
- Fake timers: Use native OS timer mocks; no reliance on setTimeout for core timer logic
- Test database: SQLite in-memory (local storage mock for browser apps)
- IDE: VS Code with debug configuration for breakpoint testing

**Staging Environment:**
- Replica of production environment (if cloud-based)
- Real database (not in-memory) for integration testing
- Test data fixtures: Pre-seeded tasks, sessions, break activities
- Network conditions: Simulate offline, high latency, packet loss for integration tests

**Test Data:**
- Predefined tasks: "Coding - Feature X", "Email Processing", "Deep Work - Research"
- Sample sessions: Mix of completed (50m, 25m), paused (15m), interrupted (10m)
- Break activities: "Walk", "Meditation", "Coffee", "Custom: Guitar"
- User settings: Default (25/5), custom (90/15), preset ("Deep Coding")
- Time zones: UTC, US Eastern, Europe/Berlin, Asia/Tokyo

### CI/CD Integration

**Pre-Commit (Developer Machine):**
- Unit tests: Jest/pytest with coverage check (block if <80%)
- Linting: ESLint, Prettier (auto-fix on commit)
- Type checking: TypeScript strict mode

**On PR / Pre-Merge:**
- All unit tests must pass
- Code coverage must be ≥80%
- No console errors or warnings

**Post-Merge to Main (Automated):**
- Integration tests: Run against staging environment (≥60% critical workflow coverage)
- E2E tests: Smoke test subset (happy paths only, <10 min total)
- Performance tests: Baseline comparison (no >10% regression)
- Artifacts: Test reports, coverage dashboards, performance graphs

**Nightly Build (DevOps):**
- Full E2E test suite (100% of acceptance criteria, 30–60 min)
- Edge case and error handling tests (20–30 min)
- Performance tests under load (30 min)
- Data integrity checks (5 min)
- Report: Dashboard available next morning; failures trigger Slack alert

**Pre-Release (Manual Gate):**
- Accessibility audit (WCAG 2.1 AA)
- Cross-platform manual testing (Windows, macOS, Linux, iOS, Android)
- Performance profiling on target devices
- Localization spot-check (en_US, de_DE, ja_JP)
- Sign-off: QA lead + DevOps lead

### Dependencies & Tools

| Tool | Purpose | Usage |
|------|---------|-------|
| **Jest** | Unit + integration test framework | Dev team: pre-commit |
| **Cypress** or **Playwright** | E2E browser automation | QA team: post-merge nightly |
| **Sinon** | Timer mocking (for fast-test mode) | Dev team: unit/integration |
| **Nock** | HTTP request mocking | Dev team: API integration tests |
| **Faker.js** | Test data generation | All teams: fixtures |
| **Codecov** | Coverage reporting | DevOps: coverage dashboard |
| **k6** | Performance/load testing | DevOps: load tests |
| **Grafana** | Performance monitoring | DevOps: performance trends |
| **Slack integration** | Test failure alerts | DevOps: CI/CD notifications |

### Coverage Goals

| Category | Target | Rationale |
|----------|--------|-----------|
| Unit tests | ≥80% code coverage | Core business logic (timer calc, data validation, state) |
| Integration tests | ≥60% critical workflows | Session lifecycle, task assignment, data persistence |
| E2E tests | 100% of acceptance criteria | Every user scenario validated end-to-end |
| Edge cases | ≥90% of documented edges | Boundary conditions, error paths, unusual states |
| Performance tests | 100% of NFRs | All timing constraints verified |
| **Overall** | **≥75% combined** | Risk-balanced: deep coverage on critical paths |

---

## Test Objectives

1. **Functional Correctness:** All 32 user stories and 41 acceptance criteria are implemented as specified
2. **Data Integrity:** Session data, task assignments, break logs, settings persist reliably across app crashes and platform changes
3. **Performance:** Core interactions (session start, timer display, analytics load) meet <2 second target; timer accuracy ±1 second
4. **Reliability:** No session data loss; timer continues accurately through OS sleep/wake; task list syncs without duplication
5. **User Experience:** Intuitive workflows require <5 clicks to start session; clear visual feedback for all actions
6. **Accessibility:** Full WCAG 2.1 AA compliance; keyboard navigation; screen reader support
7. **Cross-Platform:** Identical core functionality on desktop (Windows, macOS, Linux) and mobile (iOS, Android)
8. **Security & Privacy:** Local-first design; no unencrypted data transmission; no unauthorized tracking

---

## Test Scope

### In Scope

**Features:**
- Distraction-Free Session Timer (TIMER)
- Task Attribution & Session Logging (TASK)
- Break Activity Tracking (BREAK)
- Customizable Session & Break Settings (CONFIG)
- Session Analytics & Focus Pattern Dashboard (DASH)
- Task List Integration (INTEG, v2)
- System-wide concerns (SYSTEM)

**User Scenarios:** All 32 user stories covering 3 personas (Office Worker, Developer, Student)

**Platforms:** Desktop (Windows, macOS, Linux), Mobile (iOS 14+, Android 10+)

**Data Validation:** Input validation, data persistence, query accuracy, export correctness

**Performance:** Load times, query response, timer accuracy, chart rendering

**Accessibility:** WCAG 2.1 AA, keyboard nav, screen reader, text resizing, color contrast

### Out of Scope

- Real-time collaboration or team features
- Cloud sync (v1 is local-first; cloud testing deferred to v2)
- Email/calendar/meeting integrations
- AI-driven recommendations or smart insights
- Gamification or social features
- Localization beyond English (spot-check only; full l10n in v2)
- Team/family sharing or permissions
- 3rd-party analytics or crash reporting

---

## Requirement Traceability Map

All 32 user stories map to REQ-IDs and test cases:

| REQ-ID | Feature | User Story | Scenario Count | Primary Test Cases |
|--------|---------|-----------|---|---|
| REQ-TIMER-01 | Session Timer | Start Focused Session | 4 | TC-UNIT-001, TC-INT-001, TC-E2E-001, TC-EDGE-001 |
| REQ-TIMER-02 | Session Timer | Display Readable Format | 3 | TC-UNIT-002, TC-INT-002, TC-PERF-001 |
| REQ-TIMER-03 | Session Timer | Pause/Resume | 3 | TC-INT-003, TC-E2E-002, TC-EDGE-002 |
| REQ-TIMER-04 | Session Timer | Audio/Visual Notification | 3 | TC-INT-004, TC-E2E-003, TC-EDGE-003 |
| REQ-TIMER-05 | Session Timer | Break Transition | 3 | TC-INT-005, TC-E2E-004, TC-EDGE-004 |
| REQ-TIMER-06 | Session Timer | Sleep/Hibernation | 3 | TC-INT-006, TC-E2E-005, TC-EDGE-005 |
| REQ-TIMER-07 | Session Timer | Long Session Validation | 2 | TC-INT-007, TC-EDGE-006 |
| REQ-TIMER-08 | Session Timer | Prevent Concurrent | 3 | TC-INT-008, TC-E2E-006, TC-EDGE-007 |
| REQ-TASK-01 | Task Logging | Inline Task Creation | 4 | TC-UNIT-003, TC-INT-009, TC-E2E-007, TC-EDGE-008 |
| REQ-TASK-02 | Task Logging | Display Task During Session | 2 | TC-INT-010, TC-E2E-008 |
| REQ-TASK-03 | Task Logging | Log Session Metadata | 3 | TC-UNIT-004, TC-INT-011, TC-EDGE-009 |
| REQ-TASK-04 | Task Logging | Task List Metrics | 3 | TC-INT-012, TC-E2E-009, TC-PERF-002 |
| REQ-TASK-05 | Task Logging | Search Tasks | 3 | TC-INT-013, TC-E2E-010, TC-EDGE-010 |
| REQ-TASK-06 | Task Logging | Rename Task | 3 | TC-UNIT-005, TC-INT-014, TC-EDGE-011 |
| REQ-TASK-07 | Task Logging | Delete Task (Soft) | 4 | TC-UNIT-006, TC-INT-015, TC-E2E-011, TC-EDGE-012 |
| REQ-TASK-08 | Task Logging | Reassign Session | 3 | TC-INT-016, TC-E2E-012, TC-EDGE-013 |
| REQ-BREAK-01 | Break Tracking | Activity Prompt | 3 | TC-INT-017, TC-E2E-013, TC-EDGE-014 |
| REQ-BREAK-02 | Break Tracking | Log Activity | 3 | TC-UNIT-007, TC-INT-018, TC-EDGE-015 |
| REQ-BREAK-03 | Break Tracking | Custom Activity | 3 | TC-UNIT-008, TC-INT-019, TC-EDGE-016 |
| REQ-BREAK-04 | Break Tracking | Activity History | 2 | TC-INT-020, TC-E2E-014 |
| REQ-BREAK-05 | Break Tracking | Skip Pattern Detection | 2 | TC-INT-021, TC-EDGE-017 |
| REQ-CONFIG-01 | Settings | Global Defaults | 4 | TC-UNIT-009, TC-INT-022, TC-E2E-015, TC-EDGE-018 |
| REQ-CONFIG-02 | Settings | Per-Session Override | 3 | TC-INT-023, TC-E2E-016, TC-EDGE-019 |
| REQ-CONFIG-03 | Settings | Create Preset | 4 | TC-UNIT-010, TC-INT-024, TC-E2E-017, TC-EDGE-020 |
| REQ-CONFIG-04 | Settings | Switch Preset | 3 | TC-INT-025, TC-E2E-018, TC-EDGE-021 |
| REQ-CONFIG-05 | Settings | Reset Defaults | 2 | TC-INT-026, TC-E2E-019 |
| REQ-DASH-01 | Analytics | Daily View | 3 | TC-UNIT-011, TC-INT-027, TC-E2E-020 |
| REQ-DASH-02 | Analytics | Weekly View & Heatmap | 3 | TC-UNIT-012, TC-INT-028, TC-E2E-021 |
| REQ-DASH-03 | Analytics | Monthly Trends | 3 | TC-UNIT-013, TC-INT-029, TC-E2E-022 |
| REQ-DASH-04 | Analytics | Task Breakdown | 3 | TC-UNIT-014, TC-INT-030, TC-E2E-023 |
| REQ-DASH-05 | Analytics | Break Pattern Analysis | 2 | TC-INT-031, TC-E2E-024 |
| REQ-DASH-06 | Analytics | CSV Export | 3 | TC-UNIT-015, TC-INT-032, TC-E2E-025 |
| REQ-DASH-07 | Analytics | Date Range Filter | 3 | TC-INT-033, TC-E2E-026, TC-EDGE-022 |
| REQ-DASH-08 | Analytics | Mobile Responsive | 2 | TC-INT-034, TC-E2E-027 |
| REQ-DASH-09 | Analytics | Performance <2s | 1 | TC-PERF-003 |
| REQ-INTEG-01 | Integration | OAuth Connection | 3 | TC-INT-035, TC-E2E-028, TC-EDGE-023 |
| REQ-INTEG-02 | Integration | Fetch External Tasks | 3 | TC-INT-036, TC-E2E-029, TC-EDGE-024 |
| REQ-INTEG-03 | Integration | Assign External Task | 2 | TC-INT-037, TC-E2E-030 |
| REQ-INTEG-04 | Integration | Mark Complete | 3 | TC-INT-038, TC-E2E-031, TC-EDGE-025 |
| REQ-INTEG-05 | Integration | Bi-Directional Sync | 2 | TC-INT-039, TC-E2E-032 |
| REQ-SYSTEM-01 | System | Data Persistence | 3 | TC-UNIT-016, TC-INT-040, TC-EDGE-026 |
| REQ-SYSTEM-02 | System | App Launch Performance | 1 | TC-PERF-004 |
| REQ-SYSTEM-03 | System | No Login Required | 2 | TC-INT-041, TC-E2E-033 |
| REQ-SYSTEM-04 | System | Accessibility (WCAG) | 4 | TC-INT-042, TC-E2E-034, TC-EDGE-027, TC-EDGE-028 |
| REQ-SYSTEM-05 | System | Cross-Platform | 3 | TC-INT-043, TC-E2E-035, TC-E2E-036 |

**Coverage Summary:** 41 unique acceptance criteria → 145 test cases across all categories
**Gaps:** None; all requirements mapped to test cases

---

## Test Cases by Category

### 1. Unit Tests (Dev Team - Owned)

Unit tests validate individual components and business logic in isolation. Owned by Dev Team, executed pre-commit.

---

#### TC-UNIT-001: Timer State Machine Initialization

**Test Strategy:** Validate timer state transitions during startup
- Test inputs: App cold start, app resume from background, corrupted saved state
- Expected: Timer initializes to correct default (25 min), reads saved state if present, handles corruption gracefully
- Coverage: TimerState model, initialization logic
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-TIMER-01 (Start Focused Session)

---

#### TC-UNIT-002: Timer Countdown Calculation

**Test Strategy:** Verify timer countdown accuracy with OS native timer backend
- Test inputs: Duration 25m, 50m, 90m, 120m; mock OS timer ticks at 1s intervals
- Expected: Remaining time decreases by exactly 1 second per tick; ±0 drift after 60 minutes
- Coverage: Timer countdown logic, no dependency on setTimeout
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-TIMER-02 (Display Readable Format)

---

#### TC-UNIT-003: Task Name Validation

**Test Strategy:** Validate task name input constraints
- Test inputs: Empty string, 1 char, 100 chars, 101 chars, whitespace-only, leading/trailing spaces
- Expected: 1–100 chars accepted; whitespace trimmed; empty rejected
- Coverage: Input validation function TaskValidator.validate_name()
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-TASK-01 (Inline Task Creation)

---

#### TC-UNIT-004: Session Record Creation

**Test Strategy:** Verify session log record structure and persistence
- Test inputs: Task name, duration (25–120 min), actual elapsed, status (completed/interrupted), timestamp
- Expected: Session record includes all fields with correct types; timestamp is ISO 8601; data persists to local storage
- Coverage: SessionLog model, data mapping
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-TASK-03 (Log Session Metadata)

---

#### TC-UNIT-005: Task Rename Retroactive Update

**Test Strategy:** Verify task rename updates all referencing sessions
- Test inputs: Rename "Coding" → "Coding - Feature X"; 5 existing sessions referencing old name
- Expected: All 5 sessions now reference new task name; historical data preserved
- Coverage: Task.rename() method, referential update logic
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-TASK-06 (Rename Task)

---

#### TC-UNIT-006: Soft Delete Task Integrity

**Test Strategy:** Verify soft delete preserves session history
- Test inputs: Delete task with 10 associated sessions
- Expected: Task marked as deleted; all 10 sessions remain with task name preserved; task excluded from future queries
- Coverage: Task soft delete logic, data preservation
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-TASK-07 (Delete Task)

---

#### TC-UNIT-007: Break Activity Record Structure

**Test Strategy:** Validate break activity log record
- Test inputs: Activity name (predefined & custom), timestamp, associated session ID
- Expected: Record includes activity_name, timestamp (ISO 8601), session_id; persists to local storage
- Coverage: BreakActivity model, data mapping
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-BREAK-02 (Log Activity)

---

#### TC-UNIT-008: Custom Activity Name Constraints

**Test Strategy:** Validate custom break activity name validation
- Test inputs: Empty, 1 char, 50 chars, 51 chars, special chars
- Expected: 1–50 chars accepted; trimmed; empty rejected
- Coverage: ActivityValidator.validate_custom_name()
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-BREAK-03 (Custom Activity)

---

#### TC-UNIT-009: Settings Persistence & Validation

**Test Strategy:** Verify settings are saved with constraints
- Test inputs: Session duration 1–120 min, break duration 1–60 min, long-break interval
- Expected: Valid settings persisted; invalid rejected (e.g., break > 60 min); constraints enforced
- Coverage: SettingsManager.save(), validation logic
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-CONFIG-01 (Global Defaults)

---

#### TC-UNIT-010: Preset Storage & Retrieval

**Test Strategy:** Verify presets are stored and retrieved correctly
- Test inputs: Create 3 presets with different durations; retrieve by name
- Expected: Each preset stores all 4 settings; retrievable by exact match; max 20 presets enforced
- Coverage: PresetManager.save(), .retrieve(), .list() methods
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-CONFIG-03 (Create Preset)

---

#### TC-UNIT-011: Daily Aggregation Calculation

**Test Strategy:** Calculate daily metrics (sessions completed, total focus time, etc.)
- Test inputs: 3 sessions (25m, 50m, interrupted at 10m); 2 break activities logged
- Expected: Sessions count = 3; Total focus time = 85m; Breaks logged = 2
- Coverage: Analytics.calculate_daily_metrics()
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-DASH-01 (Daily View)

---

#### TC-UNIT-012: Weekly Heatmap Data Generation

**Test Strategy:** Generate heatmap data for weekly view (hour × day matrix)
- Test inputs: Sessions logged across different hours and days; 3 on Tue 14:00, 1 on Fri 10:00, etc.
- Expected: Heatmap matrix correctly reflects session counts per hour/day; peak hour identified
- Coverage: Analytics.generate_heatmap_data()
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-DASH-02 (Weekly View & Heatmap)

---

#### TC-UNIT-013: Monthly Trend Calculation

**Test Strategy:** Calculate weekly trend data for month-long chart
- Test inputs: 4 weeks of data; week 1: 10h, week 2: 12h, week 3: 8h, week 4: 14h
- Expected: Trend array [10, 12, 8, 14]; trend line computed (linear regression)
- Coverage: Analytics.calculate_monthly_trend()
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-DASH-03 (Monthly Trends)

---

#### TC-UNIT-014: Task Time Allocation Percentage

**Test Strategy:** Calculate % of total focus time per task
- Test inputs: Task A: 100m, Task B: 150m, Task C: 50m (total 300m)
- Expected: Task A: 33.3%, Task B: 50%, Task C: 16.7% (rounded)
- Coverage: Analytics.calculate_task_allocation()
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-DASH-04 (Task Breakdown)

---

#### TC-UNIT-015: CSV Export Data Format

**Test Strategy:** Verify exported CSV has correct structure and escaping
- Test inputs: 5 sessions with special chars in task names (comma, quote, newline)
- Expected: CSV properly escapes fields; headers match spec; no data corruption
- Coverage: DataExporter.export_to_csv()
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-DASH-06 (CSV Export)

---

#### TC-UNIT-016: Data Backup Creation

**Test Strategy:** Verify automatic daily backup captures all data
- Test inputs: 50 sessions, 10 tasks, 20 break activities, 5 presets
- Expected: Backup file created with all records; backup is valid JSON; schema matches app data model
- Coverage: BackupManager.create_backup()
- Owned by: Dev Team (automated)

**Requirement Traceability:** REQ-SYSTEM-01 (Data Persistence)

---

### 2. Integration Tests (QA Team - Owned)

Integration tests verify feature workflows and cross-component interactions. Owned by QA Team, executed post-merge.

---

#### TC-INT-001: User Starts Session from Home Screen

```gherkin
Scenario: User starts a default 25-minute session from home screen
  Given the application is installed and home screen is displayed
  When the user clicks "Start Session"
  Then a full-screen timer appears
  And the timer displays "25:00" (default)
  And the timer countdown begins immediately
  And the UI occupies 100% of viewport with no navigation visible

Test ID: TC-INT-001
Requirement Traceability: REQ-TIMER-01 (Start Focused Session)
Owned by: QA Team (automated)
Tags: @integration @timer @core-flow @REQ-TIMER-01
```

---

#### TC-INT-002: Timer Display Meets Readability Standards

```gherkin
Scenario: Timer font and contrast meet accessibility requirements
  Given a timer is running
  When the timer UI is rendered
  Then the remaining time font size is ≥120px
  And the text-to-background contrast ratio is ≥7:1 (WCAG AAA)
  And the font is sans-serif and renders crisply on desktop and mobile
  And elapsed time is ≥48px and positioned visibly below/beside remaining time

Test ID: TC-INT-002
Requirement Traceability: REQ-TIMER-02 (Display Readable Format)
Owned by: QA Team (automated)
Tags: @integration @accessibility @display @REQ-TIMER-02
```

---

#### TC-INT-003: User Pauses and Resumes Timer

```gherkin
Scenario: User pauses active timer and resumes after interruption
  Given a session timer is running with 12:45 remaining
  When the user clicks the "Pause" button
  Then the countdown stops immediately
  And the timer displays "12:45" frozen
  And the button label changes to "Resume"
  And when the user clicks "Resume"
  Then the countdown resumes from 12:45
  And timer accuracy remains within ±1 second

Test ID: TC-INT-003
Requirement Traceability: REQ-TIMER-03 (Pause/Resume)
Owned by: QA Team (automated)
Tags: @integration @timer-control @REQ-TIMER-03
```

---

#### TC-INT-004: Audio and Visual Notifications on Session Complete

```gherkin
Scenario: User receives audio and visual notification when session ends
  Given a 25-minute timer is active (or simulated via test mode: 2 seconds)
  When the timer reaches 00:00
  Then the UI visually indicates completion (color change, banner, or flash)
  And the completion notification remains visible for ≥3 seconds
  And if audio is enabled, a notification sound plays (85dB volume)
  And the notification persists even if app is backgrounded (OS-level notification)

Test ID: TC-INT-004
Requirement Traceability: REQ-TIMER-04 (Audio/Visual Notification)
Owned by: QA Team (automated)
Tags: @integration @notification @audio-visual @REQ-TIMER-04
```

---

#### TC-INT-005: Session Transition to Break Timer

```gherkin
Scenario: Work session completes and user immediately starts break
  Given a work session timer reaches 00:00
  When the session completion UI appears
  Then a "Start Break" button is prominently displayed
  And the break duration is shown (e.g., "5-minute break")
  And when user clicks "Start Break"
  Then the break timer launches with configured duration (default 5m)
  And the break timer is visually distinct from work timer

Test ID: TC-INT-005
Requirement Traceability: REQ-TIMER-05 (Break Transition)
Owned by: QA Team (automated)
Tags: @integration @workflow @REQ-TIMER-05
```

---

#### TC-INT-006: Timer Survives System Sleep/Wake

```gherkin
Scenario: Device enters sleep during active session, resumes without time loss
  Given a session timer is running with 15:00 remaining
  When the operating system enters sleep mode
  Then the timer pauses (no background countdown)
  And when the device wakes after 30 minutes
  Then the timer resumes from 15:00 (sleep time not subtracted)
  And timer accuracy remains within ±1 second after wake

Test ID: TC-INT-006
Requirement Traceability: REQ-TIMER-06 (Sleep/Hibernation)
Owned by: QA Team (automated)
Tags: @integration @system-events @reliability @REQ-TIMER-06
```

---

#### TC-INT-007: Long Session (>120 min) Requires Confirmation

```gherkin
Scenario: User attempts to create session longer than 120 minutes
  Given user is selecting session duration
  When user attempts to set duration to 180 minutes
  Then a confirmation dialog appears warning about fatigue
  And dialog offers "Continue Anyway" or "Go Back" buttons
  And if user clicks "Continue Anyway"
  Then the 180-minute session starts normally

Test ID: TC-INT-007
Requirement Traceability: REQ-TIMER-07 (Long Session Validation)
Owned by: QA Team (automated)
Tags: @integration @validation @user-intent @REQ-TIMER-07
```

---

#### TC-INT-008: Prevent Concurrent Session Start

```gherkin
Scenario: User attempts to start new session while one is active
  Given an active timer with 10:30 remaining
  When user clicks "Start Session"
  Then a warning dialog appears: "Session in progress. Start new and abandon current?"
  And if user clicks "Continue"
  Then the current session is terminated and logged as "interrupted"
  And the new session begins
  And if user clicks "Cancel"
  Then the current session continues uninterrupted

Test ID: TC-INT-008
Requirement Traceability: REQ-TIMER-08 (Prevent Concurrent)
Owned by: QA Team (automated)
Tags: @integration @validation @REQ-TIMER-08
```

---

#### TC-INT-009: Create Task Before Session Start

```gherkin
Scenario: User creates inline task and assigns to upcoming session
  Given the home screen is displayed with task input field
  When user types "Coding: Feature X" and presses Enter
  Then the task is created and selected for the session
  And when user starts the session
  Then the task name "Coding: Feature X" is displayed on timer
  And the completed session is logged with this task

Test ID: TC-INT-009
Requirement Traceability: REQ-TASK-01 (Inline Task Creation)
Owned by: QA Team (automated)
Tags: @integration @task-management @workflow @REQ-TASK-01
```

---

#### TC-INT-010: Task Name Displayed During Active Session

```gherkin
Scenario: User sees task name prominently during focus session
  Given a session is active with task "Email Processing"
  When the timer is displayed
  Then the task name "Email Processing" is visible (≥48px font)
  And the task name is positioned above or below the main timer display
  And when user wants to change task mid-session and clicks the task name
  Then a task selection dialog appears
  And when user selects a different task
  Then the session is reassigned to the new task

Test ID: TC-INT-010
Requirement Traceability: REQ-TASK-02 (Display Task During Session)
Owned by: QA Team (automated)
Tags: @integration @task-visibility @REQ-TASK-02
```

---

#### TC-INT-011: Session Logged with Complete Metadata

```gherkin
Scenario: Completed session is persisted with all required metadata
  Given a user completes a 50-minute session on task "Coding"
  When the session ends
  Then a session record is created with:
    - task_name = "Coding"
    - duration_minutes = 50
    - actual_elapsed_minutes = 50
    - completion_timestamp = <ISO 8601 datetime>
    - session_status = "completed"
  And the session record is persisted to local storage
  And the session appears in task history

Test ID: TC-INT-011
Requirement Traceability: REQ-TASK-03 (Log Session Metadata)
Owned by: QA Team (automated)
Tags: @integration @data-persistence @REQ-TASK-03
```

---

#### TC-INT-012: Task List Shows Cumulative Metrics

```gherkin
Scenario: User views task list with total sessions and focus time
  Given a user with 3 completed sessions:
    - Task A: 3 sessions, 2h 15m total
    - Task B: 5 sessions, 3h 10m total
    - Task C: 1 session, 50m total
  When user opens the Tasks view
  Then a list displays all tasks sorted by total time (descending)
  And each row shows: Task name | Sessions | Total time | Most recent date
  And Task B is listed first (highest total time)

Test ID: TC-INT-012
Requirement Traceability: REQ-TASK-04 (Task List Metrics)
Owned by: QA Team (automated)
Tags: @integration @analytics @REQ-TASK-04
```

---

#### TC-INT-013: Search/Filter Tasks by Name

```gherkin
Scenario: User searches for task by partial name match
  Given user has tasks: "Coding: Feature A", "Coding: Feature B", "Email Processing"
  When user enters "Coding" in search field
  Then the list is filtered to show 2 tasks containing "Coding"
  And results are returned within 200ms
  And when user clears the search
  Then the full task list is restored

Test ID: TC-INT-013
Requirement Traceability: REQ-TASK-05 (Search Tasks)
Owned by: QA Team (automated)
Tags: @integration @search @performance @REQ-TASK-05
```

---

#### TC-INT-014: Rename Task Updates All References

```gherkin
Scenario: User renames task and all sessions are updated retroactively
  Given 5 sessions logged with task "Math Chapter 5"
  When user renames task to "Math Chapter 5 - Review"
  Then the task name is updated
  And all 5 sessions now reference the new task name
  And the change applies retroactively (historical data updated)
  And task is no longer accessible under old name

Test ID: TC-INT-014
Requirement Traceability: REQ-TASK-06 (Rename Task)
Owned by: QA Team (automated)
Tags: @integration @data-integrity @REQ-TASK-06
```

---

#### TC-INT-015: Delete Task (Soft Delete) Preserves History

```gherkin
Scenario: User deletes task and session history is preserved
  Given a user deletes task "Old Project" with 8 associated sessions
  When delete is confirmed
  Then the task is marked as deleted
  And all 8 sessions remain in session history with task name preserved
  And the deleted task does not appear in active task list or selection dropdown

Test ID: TC-INT-015
Requirement Traceability: REQ-TASK-07 (Delete Task)
Owned by: QA Team (automated)
Tags: @integration @data-integrity @REQ-TASK-07
```

---

#### TC-INT-016: Reassign Session to Different Task

```gherkin
Scenario: User reassigns session to wrong task after completion
  Given a completed session initially assigned to "Coding"
  When user views session history and clicks to edit task
  Then a task selection dialog appears with current task selected
  And when user selects "Email Processing"
  Then the session is reassigned
  And task metrics are updated: Coding loses 1 session, Email gains 1 session
  And session metadata (duration, timestamp) remains unchanged

Test ID: TC-INT-016
Requirement Traceability: REQ-TASK-08 (Reassign Session)
Owned by: QA Team (automated)
Tags: @integration @workflow @REQ-TASK-08
```

---

#### TC-INT-017: Break Activity Selection Dialog

```gherkin
Scenario: User is prompted to log break activity after session completes
  Given a work session has just completed
  When the session completion UI appears
  Then a "What are you doing on your break?" dialog is displayed
  And predefined activities are shown as buttons: Stretch, Walk, Hydrate/Coffee, Eat, Meditation, Messages, Other
  And user can click "Skip" to skip activity logging
  And when user selects "Walk"
  Then the activity is logged and break timer starts

Test ID: TC-INT-017
Requirement Traceability: REQ-BREAK-01 (Activity Prompt)
Owned by: QA Team (automated)
Tags: @integration @user-prompt @workflow @REQ-BREAK-01
```

---

#### TC-INT-018: Break Activity Logged with Metadata

```gherkin
Scenario: Selected break activity is recorded with timestamp
  Given user selects "Meditation" from break activity dialog
  When the activity is logged
  Then a break activity record is created with:
    - activity_name = "Meditation"
    - activity_timestamp = <ISO 8601 datetime>
    - associated_session_id = <previous work session ID>
  And the break timer starts

Test ID: TC-INT-018
Requirement Traceability: REQ-BREAK-02 (Log Activity)
Owned by: QA Team (automated)
Tags: @integration @data-persistence @REQ-BREAK-02
```

---

#### TC-INT-019: Custom Break Activity Creation

```gherkin
Scenario: User creates custom break activity not in predefined list
  Given the break activity dialog is displayed
  When user clicks "Other" and types "Play Guitar"
  And confirms the custom activity
  Then the activity is logged as "Play Guitar"
  And in future breaks, "Play Guitar" appears as an option in the predefined list

Test ID: TC-INT-019
Requirement Traceability: REQ-BREAK-03 (Custom Activity)
Owned by: QA Team (automated)
Tags: @integration @extensibility @REQ-BREAK-03
```

---

#### TC-INT-020: Break Activity History Displayed

```gherkin
Scenario: User views break activity summary for the week
  Given user has logged break activities: Walk (8x), Meditation (3x), Coffee (5x), Stretch (2x)
  When user opens analytics dashboard
  Then a break activity section shows:
    - Total breaks this week: 18
    - Breakdown: Walk (44%), Coffee (28%), Meditation (17%), Stretch (11%)
    - Most common: Walk (highlighted or ranked first)

Test ID: TC-INT-020
Requirement Traceability: REQ-BREAK-04 (Activity History)
Owned by: QA Team (automated)
Tags: @integration @analytics @REQ-BREAK-04
```

---

#### TC-INT-021: Skip Break Pattern Detection and Reminder

```gherkin
Scenario: System detects user skipping breaks and prompts reminder
  Given user completes 5 consecutive sessions without logging any break activity
  When the 5th session completes
  Then system detects "skipped breaks" pattern
  And when the 6th session completes
  Then before the break activity dialog, a reminder appears: "You've skipped breaks for 5 sessions. Taking breaks helps you stay focused."
  And reminder offers "Take a Break", "Skip Reminder", or "Disable Reminders"

Test ID: TC-INT-021
Requirement Traceability: REQ-BREAK-05 (Skip Pattern Detection)
Owned by: QA Team (automated)
Tags: @integration @user-engagement @REQ-BREAK-05
```

---

#### TC-INT-022: Save and Persist Global Settings

```gherkin
Scenario: User customizes session and break durations in settings
  Given settings page is open
  When user sets:
    - Session duration: 50 minutes
    - Break duration: 15 minutes
    - Long-break interval: Every 4 sessions
    - Long-break duration: 30 minutes
  And clicks "Save"
  Then settings are persisted to local storage
  And a confirmation appears: "Settings saved"
  And when user closes and reopens app
  Then the new settings are retained (50m session, 15m break)

Test ID: TC-INT-022
Requirement Traceability: REQ-CONFIG-01 (Global Defaults)
Owned by: QA Team (automated)
Tags: @integration @settings @persistence @REQ-CONFIG-01
```

---

#### TC-INT-023: Per-Session Duration Override

```gherkin
Scenario: User overrides default session duration for single session
  Given default session duration is 25 minutes
  When user clicks "Duration: 25 min" before starting session
  Then a duration picker appears
  And user selects 90 minutes
  And starts the session
  Then the timer displays 90:00
  And when the session completes and user starts a new session
  Then the default 25 minutes is used again (override not persisted)

Test ID: TC-INT-023
Requirement Traceability: REQ-CONFIG-02 (Per-Session Override)
Owned by: QA Team (automated)
Tags: @integration @flexibility @REQ-CONFIG-02
```

---

#### TC-INT-024: Create and Save Session Preset

```gherkin
Scenario: User saves custom session configuration as reusable preset
  Given user has configured:
    - Session: 90 min
    - Break: 20 min
    - Long-break interval: Every 4 sessions
    - Long-break duration: 30 min
  When user clicks "Save as Preset"
  And enters name "Deep Coding"
  And confirms
  Then the preset is saved
  And when user views presets
  Then "Deep Coding" is listed as available

Test ID: TC-INT-024
Requirement Traceability: REQ-CONFIG-03 (Create Preset)
Owned by: QA Team (automated)
Tags: @integration @customization @REQ-CONFIG-03
```

---

#### TC-INT-025: Switch Between Presets Before Session

```gherkin
Scenario: User quickly switches between presets before starting session
  Given user has 2 presets: "Deep Coding" (90/20) and "Email Blitz" (30/5)
  When user clicks "Preset" dropdown on home screen
  And selects "Email Blitz"
  Then the upcoming session will use 30-minute timer and 5-minute break
  And when session starts
  Then timer displays 30:00
  And presets definition remains unchanged (only session uses those settings)

Test ID: TC-INT-025
Requirement Traceability: REQ-CONFIG-04 (Switch Preset)
Owned by: QA Team (automated)
Tags: @integration @workflow @REQ-CONFIG-04
```

---

#### TC-INT-026: Reset Settings to Factory Defaults

```gherkin
Scenario: User resets all settings to factory defaults
  Given user has custom settings configured
  When user clicks "Reset to Defaults"
  Then confirmation dialog appears
  And when user confirms
  Then all global settings return to defaults:
    - Session: 25 min
    - Break: 5 min
    - Long-break: Disabled
  And custom presets are NOT deleted (only globals reset)

Test ID: TC-INT-026
Requirement Traceability: REQ-CONFIG-05 (Reset Defaults)
Owned by: QA Team (automated)
Tags: @integration @settings @REQ-CONFIG-05
```

---

#### TC-INT-027: Daily Analytics View

```gherkin
Scenario: User views daily analytics summary on dashboard
  Given user has completed 4 sessions today:
    - Coding: 50 min
    - Email: 30 min
    - Coding: 45 min (paused 10 min)
    - Deep Work: 60 min
  When user opens dashboard → Daily view
  Then metrics display:
    - Sessions completed today: 4
    - Total focus time: 3h 25m
    - Longest session: 60 min
    - Break activities logged: 3
  And session list shows all 4 sessions with task name and time

Test ID: TC-INT-027
Requirement Traceability: REQ-DASH-01 (Daily View)
Owned by: QA Team (automated)
Tags: @integration @analytics @dashboard @REQ-DASH-01
```

---

#### TC-INT-028: Weekly Analytics with Heatmap

```gherkin
Scenario: User views weekly focus patterns via heatmap
  Given user has sessions across different days and hours:
    - Mon 09:00: Coding (45m)
    - Tue 14:00: Coding (50m), Email (25m)
    - Wed 10:00: Deep Work (90m)
    - Fri 14:00: Coding (30m)
  When user opens dashboard → Weekly view
  Then a heatmap displays hours × days with color intensity for focus time
  And text identifies peak productivity: "Your most productive time: Tue 2-3 PM"
  And bar chart shows focus time per day of week

Test ID: TC-INT-028
Requirement Traceability: REQ-DASH-02 (Weekly View & Heatmap)
Owned by: QA Team (automated)
Tags: @integration @analytics @visualization @REQ-DASH-02
```

---

#### TC-INT-029: Monthly Trend Analysis

```gherkin
Scenario: User views monthly trends over 4 weeks
  Given user has focus data:
    - Week 1: 10h
    - Week 2: 12h
    - Week 3: 8h
    - Week 4: 14h
  When user opens dashboard → Monthly view
  Then a line chart displays focus time per week
  And trend line shows overall trajectory
  And comparison to previous month shows: "This month: 44h. Last month: 38h. Change: +6h (+15%)"
  And user can navigate between months via picker

Test ID: TC-INT-029
Requirement Traceability: REQ-DASH-03 (Monthly Trends)
Owned by: QA Team (automated)
Tags: @integration @analytics @REQ-DASH-03
```

---

#### TC-INT-030: Task Time Allocation Breakdown

```gherkin
Scenario: User views how focus time is distributed across tasks
  Given user has tasks with sessions:
    - Coding: 15h 30m (45% of total)
    - Email: 10h 00m (29% of total)
    - Deep Work: 8h 30m (25% of total)
  When user opens dashboard → Tasks section
  Then table displays:
    - Task name | Sessions | Total time | % of total
    - Tasks ranked by total time (descending)
  And pie chart visualizes distribution
  And user can filter by date range

Test ID: TC-INT-030
Requirement Traceability: REQ-DASH-04 (Task Breakdown)
Owned by: QA Team (automated)
Tags: @integration @analytics @task-analysis @REQ-DASH-04
```

---

#### TC-INT-031: Break Activity Frequency Analysis

```gherkin
Scenario: User views which break activities they use most
  Given user has logged break activities:
    - Walk: 8 times (40%)
    - Meditation: 4 times (20%)
    - Coffee: 5 times (25%)
    - Stretch: 3 times (15%)
  When user opens dashboard → Break Activities section
  Then a bar chart shows activity frequency
  And summary statement: "Your most common break: Walk (40% of breaks)"
  And user can analyze correlations with subsequent session quality

Test ID: TC-INT-031
Requirement Traceability: REQ-BREAK-04 (Activity History - Analytics view)
Owned by: QA Team (automated)
Tags: @integration @analytics @break-analysis @REQ-DASH-05
```

---

#### TC-INT-032: Export Session Data as CSV

```gherkin
Scenario: User exports session history to CSV file
  Given user has 20 sessions logged
  When user clicks "Export" → "Export All Sessions"
  Then a CSV file is generated:
    - Columns: task_name, duration_minutes, actual_elapsed, timestamp, status, break_activity
    - Filename: pomodoro_sessions_[YYYY-MM-DD].csv
    - File includes all 20 session records
  And file is automatically downloaded
  And confirmation appears: "Data exported successfully"

Test ID: TC-INT-032
Requirement Traceability: REQ-DASH-06 (CSV Export)
Owned by: QA Team (automated)
Tags: @integration @data-export @REQ-DASH-06
```

---

#### TC-INT-033: Date Range Filter on Dashboard

```gherkin
Scenario: User filters analytics by custom date range
  Given user wants to compare focus time before and after changing study habits
  When user clicks "Date Range"
  And selects start date: 2026-05-01, end date: 2026-05-15
  And clicks "Apply"
  Then all dashboard views (daily, weekly, monthly, tasks) are filtered to show only data from May 1-15
  And metrics recalculate: "May 1-15: 22h focus time"
  And when user clicks "Previous Month" preset
  Then date range is automatically set to April 1-30

Test ID: TC-INT-033
Requirement Traceability: REQ-DASH-07 (Date Range Filter)
Owned by: QA Team (automated)
Tags: @integration @filtering @analytics @REQ-DASH-07
```

---

#### TC-INT-034: Mobile-Responsive Dashboard Layout

```gherkin
Scenario: Dashboard renders correctly on mobile device (320px–480px width)
  Given dashboard is viewed on mobile phone (width 375px)
  When page loads
  Then all content is readable without horizontal scrolling
  And fonts are ≥14px for body text
  And buttons are ≥44x44px (touch-friendly)
  And charts reflow (bar charts rotate to vertical, heatmaps show abbreviated labels)
  And tappable elements have sufficient spacing

Test ID: TC-INT-034
Requirement Traceability: REQ-DASH-08 (Mobile Responsive)
Owned by: QA Team (automated)
Tags: @integration @responsive-design @mobile @REQ-DASH-08
```

---

#### TC-INT-035: OAuth Connection to Task Management System

```gherkin
Scenario: User connects Pomodoro Timer to Todoist via OAuth
  Given settings → Integrations page is open
  When user clicks "Connect" for Todoist
  Then browser is redirected to Todoist authorization page
  And page displays: "Pomodoro Timer wants to access your Todoist account"
  And requested permissions are shown
  And when user authorizes
  Then user is redirected back to Pomodoro Timer within 3 seconds
  And success message appears: "Successfully connected to Todoist"

Test ID: TC-INT-035
Requirement Traceability: REQ-INTEG-01 (OAuth Connection)
Owned by: QA Team (automated)
Tags: @integration @oauth @third-party @REQ-INTEG-01
```

---

#### TC-INT-036: Fetch and Display External Task List

```gherkin
Scenario: Pomodoro Timer fetches task list from connected Todoist account
  Given user is connected to Todoist
  When user opens task selection screen
  Then Todoist tasks are fetched and displayed
  And external tasks are visually marked (e.g., "Todoist" tag or icon)
  And fetch completes within 1 second
  And when user clicks "Refresh"
  Then latest task list is pulled from Todoist (within 1s)
  And new tasks appear, deleted tasks removed

Test ID: TC-INT-036
Requirement Traceability: REQ-INTEG-02 (Fetch External Tasks)
Owned by: QA Team (automated)
Tags: @integration @external-sync @performance @REQ-INTEG-02
```

---

#### TC-INT-037: Assign Session to External Task

```gherkin
Scenario: User selects Todoist task and assigns session to it
  Given Todoist task "Fix login bug" is displayed in task selection
  When user selects this task before starting session
  Then the session is assigned to the external task
  And when session completes
  Then session record includes:
    - external_task_id = <Todoist task ID>
    - external_system_name = "Todoist"
    - external_task_name = "Fix login bug"

Test ID: TC-INT-037
Requirement Traceability: REQ-INTEG-03 (Assign External Task)
Owned by: QA Team (automated)
Tags: @integration @external-assignment @REQ-INTEG-03
```

---

#### TC-INT-038: Mark External Task Complete

```gherkin
Scenario: User marks Todoist task complete from Pomodoro Timer
  Given a session completes with external task assigned
  When session completion UI appears
  Then prompt appears: "Mark this task complete in Todoist?"
  And if user clicks "Yes"
  Then Todoist task is marked complete via API
  And confirmation appears: "Task marked complete in Todoist"
  And if sync fails (network error)
  Then message shows: "Could not sync to Todoist. Task marked complete locally."
  And user can retry sync later

Test ID: TC-INT-038
Requirement Traceability: REQ-INTEG-04 (Mark Complete)
Owned by: QA Team (automated)
Tags: @integration @external-sync @error-handling @REQ-INTEG-04
```

---

#### TC-INT-039: Bi-Directional Sync with External Task System

```gherkin
Scenario: Task completed in external system is reflected in Pomodoro Timer
  Given user is connected to Todoist
  And Todoist task is displayed in Pomodoro Timer
  When user completes the task in Todoist
  And Pomodoro Timer refreshes task list
  Then the task is marked complete in Pomodoro Timer
  And task no longer appears in active selection dropdown
  And historical sessions are still attributed to this task (no data loss)

Test ID: TC-INT-039
Requirement Traceability: REQ-INTEG-05 (Bi-Directional Sync)
Owned by: QA Team (automated)
Tags: @integration @bi-directional-sync @reliability @REQ-INTEG-05
```

---

#### TC-INT-040: Session Data Persists Through App Crash

```gherkin
Scenario: Active session survives application crash
  Given user is in middle of 25-minute session with 15:00 remaining
  When application crashes or is force-killed
  And user reopens app within 24 hours
  Then "Resume Session?" dialog appears showing 15:00 remaining
  And when user clicks "Resume"
  Then session continues from 15:00
  And completed session is properly logged to history

Test ID: TC-INT-040
Requirement Traceability: REQ-SYSTEM-01 (Data Persistence)
Owned by: QA Team (automated)
Tags: @integration @reliability @crash-recovery @REQ-SYSTEM-01
```

---

#### TC-INT-041: No Login Required for Basic Functionality

```gherkin
Scenario: New user can start app and begin sessions without registration
  Given fresh app install
  When app launches
  Then home screen appears immediately (no login, registration, or onboarding)
  And user can click "Start Session" right away
  And all data is stored locally (no user ID or account required)

Test ID: TC-INT-041
Requirement Traceability: REQ-SYSTEM-03 (No Login Required)
Owned by: QA Team (automated)
Tags: @integration @frictionless @privacy @REQ-SYSTEM-03
```

---

#### TC-INT-042: WCAG 2.1 AA Compliance - Keyboard Navigation

```gherkin
Scenario: User navigates entire app using keyboard only
  Given app is open
  When user presses Tab to navigate between elements
  Then all interactive elements are reachable (buttons, inputs, links)
  And focus indicators are always visible with ≥3:1 contrast
  And Enter key activates buttons, Space toggles checkboxes
  And Escape key closes dialogs
  And no content is keyboard-trap (user can always reach next element)

Test ID: TC-INT-042
Requirement Traceability: REQ-SYSTEM-04 (Accessibility)
Owned by: QA Team (automated)
Tags: @integration @accessibility @keyboard-nav @REQ-SYSTEM-04
```

---

#### TC-INT-043: Cross-Platform Consistency (Desktop + Mobile)

```gherkin
Scenario: Core session timer functionality is identical on desktop and mobile
  Given user starts same session on Windows desktop and iOS phone
  When session runs on both platforms
  Then timer display, accuracy, pause/resume, notifications behave identically
  And task attribution works the same
  And settings apply uniformly
  And task list and analytics are functionally equivalent (layout may differ)

Test ID: TC-INT-043
Requirement Traceability: REQ-SYSTEM-05 (Cross-Platform)
Owned by: QA Team (automated)
Tags: @integration @cross-platform @consistency @REQ-SYSTEM-05
```

---

### 3. End-to-End Tests (QA Team - Owned)

E2E tests verify complete user journeys matching acceptance criteria. Owned by QA Team, executed nightly before release.

---

#### TC-E2E-001: New User Starts First Session (Happy Path)

```gherkin
Scenario: Brand new user launches app and completes their first focus session
  Given app is freshly installed
  When app launches
  Then home screen appears with "Start Session" button
  And when user clicks "Start Session"
  Then task input field prompts "What are you working on?"
  And when user types "Learning React" and starts session
  Then full-screen timer appears with 25:00
  And timer counts down smoothly
  And when timer reaches 00:00
  Then session completion UI appears
  And user can view session in history with task "Learning React"

Test ID: TC-E2E-001
Requirement Traceability: REQ-TIMER-01, REQ-TASK-01
Owned by: QA Team (manual + automated)
Tags: @e2e @happy-path @onboarding @REQ-TIMER-01 @REQ-TASK-01
```

---

#### TC-E2E-002: Student Study Session with Break Tracking

```gherkin
Scenario: Student completes full study session with structured break
  Given student opens app
  When student starts a 50-minute session on task "Bio Chapter 5"
  And timer runs for 50 minutes (or 2 sec in test mode)
  And session completes
  Then break activity dialog appears
  And student selects "Walk"
  And activity is logged
  And break timer starts with 15-minute duration
  And when break ends
  Then student can start new study session

Test ID: TC-E2E-002
Requirement Traceability: REQ-TIMER-01, REQ-BREAK-01, REQ-BREAK-02
Owned by: QA Team (manual + automated)
Tags: @e2e @student-flow @REQ-TIMER-01 @REQ-BREAK-01
```

---

#### TC-E2E-003: Developer Customizes Settings and Saves Preset

```gherkin
Scenario: Developer creates "Deep Coding" preset for long focus sessions
  Given developer opens Settings
  When developer configures:
    - Session: 90 min
    - Break: 20 min
    - Long-break every: 4 sessions
    - Long-break duration: 30 min
  And clicks "Save as Preset"
  And names it "Deep Coding"
  And clicks "Start Session"
  Then preset selector shows "Deep Coding"
  And when developer selects the preset and starts session
  Then timer displays 90:00

Test ID: TC-E2E-003
Requirement Traceability: REQ-CONFIG-01, REQ-CONFIG-03, REQ-CONFIG-04
Owned by: QA Team (manual + automated)
Tags: @e2e @settings-customization @REQ-CONFIG-03
```

---

#### TC-E2E-004: Office Worker Reviews Weekly Focus Analytics

```gherkin
Scenario: Office worker analyzes weekly productivity to adjust meeting schedule
  Given worker has completed 15 sessions over the week across multiple tasks
  When worker opens Dashboard → Weekly view
  Then heatmap displays focus time by hour and day
  And summary identifies: "Peak productivity: Tuesday 2-3 PM"
  And bar chart shows focus time per day (Mon–Sun)
  And task breakdown shows time allocation
  And worker can see: "Coding: 8h (45%), Email: 6h (33%), Meetings: 4h (22%)"
  And worker uses data to request no meetings 2-3 PM

Test ID: TC-E2E-004
Requirement Traceability: REQ-DASH-02, REQ-DASH-04
Owned by: QA Team (manual + automated)
Tags: @e2e @analytics-workflow @insights @REQ-DASH-02
```

---

#### TC-E2E-005: Multi-Platform Session Continuity

```gherkin
Scenario: User starts session on desktop, closes app, continues on mobile
  Given user is on Windows desktop
  When user starts a 45-minute session with task "Report writing"
  And after 15 minutes, user closes the app
  And user opens app on iOS phone
  Then app prompts "Resume Session? 30:00 remaining"
  And when user clicks "Resume"
  Then session continues from 30:00 on phone
  And completed session is logged with task name

Test ID: TC-E2E-005
Requirement Traceability: REQ-TIMER-01, REQ-SYSTEM-05
Owned by: QA Team (manual + automated)
Tags: @e2e @cross-platform @session-continuity @REQ-SYSTEM-05
```

---

#### TC-E2E-006: Break Activity Logging Identifies Best Recovery Strategy

```gherkin
Scenario: Developer tracks break activities to optimize focus routine
  Given developer completes 20 sessions over 3 days with varying break activities
  When developer logs break activities:
    - Day 1: Walk (5x), Coffee (2x)
    - Day 2: Meditation (4x), Walk (3x)
    - Day 3: Walk (6x), Coffee (1x)
  And opens Dashboard → Break Activities
  Then summary shows: "Most common: Walk (14 times)"
  And heatmap shows subsequent sessions after "Walk" had shorter focus time recovery
  And developer adjusts strategy to include more Meditation

Test ID: TC-E2E-006
Requirement Traceability: REQ-BREAK-02, REQ-BREAK-04, REQ-DASH-05
Owned by: QA Team (manual + automated)
Tags: @e2e @behavior-optimization @REQ-BREAK-02
```

---

#### TC-E2E-007: Task Reassignment and Analytics Recalculation

```gherkin
Scenario: User discovers session was logged to wrong task and reassigns it
  Given user completed session logged as "Email" but was actually "Meeting notes"
  When user opens Tasks view and sees "Email: 50m"
  And clicks on the email session to edit
  Then reassignment dialog appears
  And user selects "Meeting notes"
  And session is reassigned
  Then task metrics update: Email goes down to 0m, Meeting notes shows 50m
  And dashboard analytics automatically recalculate

Test ID: TC-E2E-007
Requirement Traceability: REQ-TASK-08, REQ-DASH-04
Owned by: QA Team (manual + automated)
Tags: @e2e @data-integrity @workflow @REQ-TASK-08
```

---

#### TC-E2E-008: Student Exports Study Data for Analysis

```gherkin
Scenario: Student exports focus data to analyze study effectiveness
  Given student has 30 days of study data across 5 courses
  When student opens Dashboard
  And selects date range: Apr 1 – May 15
  And clicks "Export" → "Export All Sessions"
  Then CSV file is downloaded: pomodoro_sessions_2026-05-20.csv
  And file includes all sessions within date range with columns: task_name, duration, timestamp, status
  And student opens CSV in Excel to correlate study hours with exam scores

Test ID: TC-E2E-008
Requirement Traceability: REQ-DASH-06, REQ-DASH-07
Owned by: QA Team (manual + automated)
Tags: @e2e @data-export @analysis @REQ-DASH-06
```

---

#### TC-E2E-009: Office Worker Integrates with Todoist

```gherkin
Scenario: Office worker connects Pomodoro Timer to Todoist task list
  Given worker has 20 tasks in Todoist
  When worker opens Settings → Integrations
  And clicks "Connect to Todoist"
  Then OAuth flow completes (user authorizes)
  And Todoist tasks are now available in Pomodoro Timer
  And when worker starts session
  Then task selection shows Todoist tasks
  And worker can assign session to "Fix login bug" (Todoist task)
  And when session completes and worker marks it complete
  Then Todoist marks the task complete automatically

Test ID: TC-E2E-009
Requirement Traceability: REQ-INTEG-01, REQ-INTEG-02, REQ-INTEG-04
Owned by: QA Team (manual + automated)
Tags: @e2e @integration @external-system @REQ-INTEG-01
```

---

#### TC-E2E-010: Accessibility: Screen Reader User Tracks Session

```gherkin
Scenario: Blind user operates app with screen reader (VoiceOver on macOS)
  Given VoiceOver is enabled
  When user opens app
  Then screen reader announces: "Pomodoro Timer, start session button"
  And when user presses Enter on "Start Session"
  Then timer UI is announced: "Timer running, 25 minutes remaining"
  And when user pauses, announcement updates: "Timer paused, 15 minutes remaining"
  And all elements have semantic labels for screen reader

Test ID: TC-E2E-010
Requirement Traceability: REQ-SYSTEM-04 (Accessibility)
Owned by: QA Team (manual)
Tags: @e2e @accessibility @screen-reader @REQ-SYSTEM-04
```

---

### 4. Edge Case & Error Handling Tests (QA Team - Owned)

---

#### TC-EDGE-001: App Crash Mid-Session Preserves State

```gherkin
Scenario: System crashes during active session without losing data
  Given session timer is running with 10:30 remaining
  When application receives SIGKILL or OS force-closes it
  And user reopens app within 24 hours
  Then resume dialog appears showing 10:30 remaining
  And timer accuracy is maintained to within ±1 second

Test ID: TC-EDGE-001
Requirement Traceability: REQ-SYSTEM-01 (Data Persistence)
Owned by: QA Team (manual + automated)
Tags: @edge-case @reliability @crash-recovery
```

---

#### TC-EDGE-002: Paused Session for Extended Duration

```gherkin
Scenario: User pauses session and leaves app paused for hours
  Given session is paused with 12:00 remaining
  When app remains paused for 3 hours
  And user returns and clicks "Resume"
  Then timer resumes from exactly 12:00 (no drift from pause duration)
  And timer accuracy remains within ±1 second

Test ID: TC-EDGE-002
Requirement Traceability: REQ-TIMER-03 (Pause/Resume)
Owned by: QA Team (manual)
Tags: @edge-case @timer-accuracy @reliability
```

---

#### TC-EDGE-003: Notification While App Backgrounded on Mobile

```gherkin
Scenario: Session completes while app is backgrounded on iOS
  Given app is backgrounded (user is using another app)
  When session timer reaches 00:00
  Then OS-level notification is delivered to notification center
  And notification displays: "Pomodoro Timer - Work Session Complete"
  And when user taps notification
  Then app foregrounds to session completion screen

Test ID: TC-EDGE-003
Requirement Traceability: REQ-TIMER-04 (Notification)
Owned by: QA Team (manual - iOS)
Tags: @edge-case @mobile @background-notification
```

---

#### TC-EDGE-004: Break Timer Skipped, Next Session Starts Immediately

```gherkin
Scenario: User skips break and starts new work session immediately
  Given break timer just started
  When user clicks "Skip Break"
  Then break timer ends
  And user can immediately start new work session
  And session log reflects break was skipped (logged or omitted)

Test ID: TC-EDGE-004
Requirement Traceability: REQ-TIMER-05 (Break Transition)
Owned by: QA Team (automated)
Tags: @edge-case @workflow @flexibility
```

---

#### TC-EDGE-005: System Wake During Paused Session

```gherkin
Scenario: Device hibernates then wakes while session is paused
  Given session is paused with 10:00 remaining
  When device enters hibernate mode
  And device wakes 4 hours later
  Then timer resumes from exactly 10:00 (not accounting for hibernate time)

Test ID: TC-EDGE-005
Requirement Traceability: REQ-TIMER-06 (Sleep/Hibernation)
Owned by: QA Team (manual)
Tags: @edge-case @system-events @timer-accuracy
```

---

#### TC-EDGE-006: User Attempts 24-Hour Session

```ghercan
Scenario: User attempts extreme session duration (1440 minutes = 24 hours)
  Given user is setting custom session duration
  When user enters 1440 minutes (or 24 hours)
  And tries to start session
  Then validation dialog appears: "Sessions >120 minutes may lead to fatigue. Continue anyway?"
  And if user confirms
  Then 24-hour session starts normally
  And timer continues running (or in test mode, completes in 2 seconds)

Test ID: TC-EDGE-006
Requirement Traceability: REQ-TIMER-07 (Long Session Validation)
Owned by: QA Team (automated)
Tags: @edge-case @validation @boundary-condition
```

---

#### TC-EDGE-007: Two Concurrent Session Start Attempts

```gherkin
Scenario: User double-clicks "Start Session" button rapidly
  Given home screen is displayed
  When user clicks "Start Session" twice in rapid succession (<500ms)
  Then only one session starts (double-click is handled)
  And second click is ignored or queued

Test ID: TC-EDGE-007
Requirement Traceability: REQ-TIMER-08 (Prevent Concurrent)
Owned by: QA Team (automated)
Tags: @edge-case @ui-robustness @race-condition
```

---

#### TC-EDGE-008: Task Name with Special Characters

```gherkin
Scenario: User creates task with special characters and symbols
  Given task creation input is active
  When user enters: "Feature #123: "Fix & Test" API (v2.0)"
  Then task is created successfully
  And task name is stored as-is without sanitization
  And task name is correctly displayed on timer and in lists

Test ID: TC-EDGE-008
Requirement Traceability: REQ-TASK-01 (Inline Task Creation)
Owned by: QA Team (automated)
Tags: @edge-case @input-validation @character-handling
```

---

#### TC-EDGE-009: Interrupted Session Status Logging

```gherkin
Scenario: User abandons session mid-way
  Given session is running with 10:00 remaining
  When user clicks "Start Session" to begin new session (abandoning current)
  And confirms to start new session
  Then the abandoned session is logged with status "interrupted"
  And actual_elapsed is recorded (e.g., 15 minutes elapsed out of 25 configured)
  And session appears in history with "interrupted" tag

Test ID: TC-EDGE-009
Requirement Traceability: REQ-TASK-03 (Log Session Metadata)
Owned by: QA Team (automated)
Tags: @edge-case @session-lifecycle @data-accuracy
```

---

#### TC-EDGE-010: Search with No Matching Results

```gherkin
Scenario: User searches for task that doesn't exist
  Given user has tasks: "Coding", "Email", "Meeting notes"
  When user enters search: "Physics"
  Then empty state message appears: "No tasks match 'Physics'"
  And when user clears search
  Then full task list is restored

Test ID: TC-EDGE-010
Requirement Traceability: REQ-TASK-05 (Search Tasks)
Owned by: QA Team (automated)
Tags: @edge-case @search @empty-state
```

---

#### TC-EDGE-011: Rename Task to Duplicate Name

```gherkin
Scenario: User renames task to match another task's name
  Given tasks: "Math", "Physics", "Math" (duplicates allowed)
  When user renames "Physics" to "Math"
  Then system allows the rename (duplicates are permitted)
  And both "Math" tasks remain distinct with separate session histories

Test ID: TC-EDGE-011
Requirement Traceability: REQ-TASK-06 (Rename Task)
Owned by: QA Team (automated)
Tags: @edge-case @task-naming @duplicates
```

---

#### TC-EDGE-012: Restore Deleted Task

```gherkin
Scenario: User deletes task, then restores it from archive
  Given user deletes task "Old Project" with 10 sessions
  When user opens "Deleted Items" view
  Then "Old Project" is listed
  And when user clicks "Restore"
  Then task is restored to active list
  And all 10 sessions are still attributed to it

Test ID: TC-EDGE-012
Requirement Traceability: REQ-TASK-07 (Delete Task - Soft Delete)
Owned by: QA Team (automated)
Tags: @edge-case @data-recovery @soft-delete
```

---

#### TC-EDGE-013: Reassign Session to Self

```gherkin
Scenario: User reassigns session to the same task it's already assigned to
  Given session is assigned to "Coding"
  When user opens reassignment dialog
  And selects "Coding" again
  And confirms
  Then system acknowledges the action without error
  And session remains assigned to "Coding" (no duplicate or data corruption)

Test ID: TC-EDGE-013
Requirement Traceability: REQ-TASK-08 (Reassign Session)
Owned by: QA Team (automated)
Tags: @edge-case @idempotency @no-op-action
```

---

#### TC-EDGE-014: Break Activity Dialog Auto-Dismiss if Break Duration Very Short

```gherkin
Scenario: Break timer is <1 minute (e.g., 30 seconds)
  Given user has configured break duration to 30 seconds
  When session ends and break timer starts
  Then break activity dialog may not appear (or auto-dismisses immediately)
  And break timer counts down from 00:30
  And system acknowledges very short breaks may not support logging

Test ID: TC-EDGE-014
Requirement Traceability: REQ-BREAK-01 (Activity Prompt)
Owned by: QA Team (manual)
Tags: @edge-case @boundary-condition @break-duration
```

---

#### TC-EDGE-015: Skip Break Pattern with Mixed Sessions

```gherkin
Scenario: User logs some break activities but skips others
  Given user completes 6 sessions:
    - Session 1: Walk (logged)
    - Session 2: Skipped
    - Session 3: Coffee (logged)
    - Session 4: Skipped
    - Session 5: Skipped
    - Session 6: Skipped
  When session 6 completes
  Then skip pattern detection is triggered (4 consecutive sessions with break logged < 50% of time)
  And reminder prompt appears on session 7

Test ID: TC-EDGE-015
Requirement Traceability: REQ-BREAK-05 (Skip Pattern Detection)
Owned by: QA Team (manual)
Tags: @edge-case @behavioral-pattern @heuristic
```

---

#### TC-EDGE-016: Custom Activity Name Exactly 50 Characters

```gherkin
Scenario: User creates custom break activity with maximum allowed length
  Given break activity dialog is open
  When user enters 50-character activity: "Organizational meeting with team and leadership"
  Then activity is created successfully
  And activity is persisted and available in future breaks

Test ID: TC-EDGE-016
Requirement Traceability: REQ-BREAK-03 (Custom Activity)
Owned by: QA Team (automated)
Tags: @edge-case @boundary-condition @max-length
```

---

#### TC-EDGE-017: Skip Reminders for Break Skipping

```gherkin
Scenario: User disables skip-break reminders
  Given skip-break reminder has appeared
  When user clicks "Disable Reminders"
  Then flag is set: skip_break_reminders = false
  And in future sessions, skip-break reminders do not appear
  And user can re-enable in settings

Test ID: TC-EDGE-017
Requirement Traceability: REQ-BREAK-05 (Skip Pattern Detection)
Owned by: QA Team (manual)
Tags: @edge-case @user-preferences @reminder-control
```

---

#### TC-EDGE-018: Settings Change Mid-Session

```gherkin
Scenario: User changes global settings during active session
  Given session is running with default 25-minute timer
  When user opens Settings
  And changes session duration to 50 minutes
  And saves
  Then the active 25-minute session continues unaffected
  And the next session will use 50 minutes (change takes effect next session)

Test ID: TC-EDGE-018
Requirement Traceability: REQ-CONFIG-01 (Global Defaults)
Owned by: QA Team (automated)
Tags: @edge-case @settings @isolation
```

---

#### TC-EDGE-019: Override that Exceeds Maximum

```gherkin
Scenario: User attempts per-session override with invalid duration
  Given override duration picker is open
  When user manually enters 200 minutes (exceeds 120 max)
  And attempts to apply
  Then validation error: "Maximum session duration is 120 minutes"
  And override is rejected

Test ID: TC-EDGE-019
Requirement Traceability: REQ-CONFIG-02 (Per-Session Override)
Owned by: QA Team (automated)
Tags: @edge-case @validation @constraint-enforcement
```

---

#### TC-EDGE-020: Preset with Same Name as Existing

```gherkin
Scenario: User creates second preset with identical name
  Given preset "Deep Coding" already exists
  When user creates new preset and names it "Deep Coding"
  Then system either:
    - Rejects with: "Preset name already exists. Choose a different name." OR
    - Overwrites the existing preset (with confirmation)
  And user is explicitly informed of the action

Test ID: TC-EDGE-020
Requirement Traceability: REQ-CONFIG-03 (Create Preset)
Owned by: QA Team (automated)
Tags: @edge-case @uniqueness @name-collision
```

---

#### TC-EDGE-021: 21st Preset Creation Rejected

```gherkin
Scenario: User attempts to create 21st preset when limit is 20
  Given user has 20 presets saved
  When user clicks "Save as Preset"
  And enters name for 21st preset
  Then error appears: "Maximum 20 presets allowed. Delete a preset to create a new one."
  And preset is not created

Test ID: TC-EDGE-021
Requirement Traceability: REQ-CONFIG-03 (Create Preset)
Owned by: QA Team (automated)
Tags: @edge-case @quota @limit-enforcement
```

---

#### TC-EDGE-022: Date Range with Reversed Start/End

```gherkin
Scenario: User selects end date before start date
  Given date range picker is open
  When user sets start: 2026-05-20, end: 2026-05-01 (reversed)
  And clicks "Apply"
  Then error message: "Start date must be before end date"
  And date range is not applied

Test ID: TC-EDGE-022
Requirement Traceability: REQ-DASH-07 (Date Range Filter)
Owned by: QA Team (automated)
Tags: @edge-case @validation @date-logic
```

---

#### TC-EDGE-023: OAuth Timeout During Authorization

```gherkin
Scenario: OAuth authorization flow times out
  Given OAuth connection is initiated
  When authorization page loads but user doesn't interact for >5 minutes
  And session times out
  Then user is returned to Pomodoro Timer with error: "Authorization timed out. Please try again."
  And user can retry connection

Test ID: TC-EDGE-023
Requirement Traceability: REQ-INTEG-01 (OAuth Connection)
Owned by: QA Team (manual)
Tags: @edge-case @oauth @timeout @error-handling
```

---

#### TC-EDGE-024: API Rate Limiting on External Task Fetch

```gherkin
Scenario: User refreshes external task list multiple times rapidly
  Given external task list is connected
  When user clicks "Refresh" 10 times within 30 seconds
  Then after 5–6 refreshes, rate limiting kicks in
  And message appears: "Refresh limited. Try again in 30s"
  And subsequent refresh attempts are queued or rejected

Test ID: TC-EDGE-024
Requirement Traceability: REQ-INTEG-02 (Fetch External Tasks)
Owned by: QA Team (manual)
Tags: @edge-case @api-rate-limit @external-system
```

---

#### TC-EDGE-025: Mark Complete Fails Silently, Logs Locally

```gherkin
Scenario: Network error when attempting to mark external task complete
  Given session ends and user selects "Mark complete in Todoist"
  When network connection drops before API request completes
  Then error message: "Could not sync to Todoist. Task marked complete locally."
  And session is logged successfully with external task reference
  And user can manually sync later

Test ID: TC-EDGE-025
Requirement Traceability: REQ-INTEG-04 (Mark Complete)
Owned by: QA Team (manual)
Tags: @edge-case @network-resilience @error-handling
```

---

#### TC-EDGE-026: Data Corruption Detection and Recovery

```gherkin
Scenario: Local storage is corrupted (partial file, invalid JSON)
  Given local storage is corrupted
  When app starts
  Then system detects corruption
  And displays: "Data recovered from backup"
  And app restores from latest backup
  And core functionality is restored

Test ID: TC-EDGE-026
Requirement Traceability: REQ-SYSTEM-01 (Data Persistence)
Owned by: QA Team (manual)
Tags: @edge-case @data-integrity @recovery
```

---

#### TC-EDGE-027: Text Resize to 200% Font Size

```gherkin
Scenario: User increases OS-level text size to 200%
  Given text size is set to 200% (browser or OS setting)
  When app is opened
  Then all text is readable without horizontal scrolling
  And buttons remain tappable (≥44x44px)
  And timer display remains clear (font scales proportionally)

Test ID: TC-EDGE-027
Requirement Traceability: REQ-SYSTEM-04 (Accessibility)
Owned by: QA Team (manual)
Tags: @edge-case @accessibility @text-scaling
```

---

#### TC-EDGE-028: High Contrast Mode

```gherkin
Scenario: User enables high contrast mode (Windows or OS setting)
  Given high contrast mode is enabled
  When app is viewed
  Then all UI elements respect high contrast colors
  And text-to-background contrast is ≥7:1
  And focused elements have clearly visible indicators

Test ID: TC-EDGE-028
Requirement Traceability: REQ-SYSTEM-04 (Accessibility)
Owned by: QA Team (manual - Windows)
Tags: @edge-case @accessibility @high-contrast
```

---

### 5. Performance Tests (DevOps/QA - Owned)

---

#### TC-PERF-001: Timer Display Refresh Rate at 60 FPS

```gherkin
Scenario: Timer countdown displays smoothly without visual jitter
  Given a session timer is running
  When the timer counts down over 60 seconds
  Then frame rate remains ≥60 FPS (no dropped frames)
  And visual updates are smooth (no visible jumps or stutter)
  And CPU usage remains <10% during countdown

Test ID: TC-PERF-001
Requirement Traceability: REQ-TIMER-02 (Display Readable Format)
Owned by: DevOps/QA (automated)
Tags: @performance @rendering @smoothness
```

---

#### TC-PERF-002: Task List Load Time with 1000 Tasks

```gherkin
Scenario: Task list loads quickly even with maximum task count
  Given user has 1000 unique tasks in local storage
  When task list is requested
  Then list is rendered within 500ms
  And pagination is available (50 tasks per page)
  And search remains responsive (<200ms per query)

Test ID: TC-PERF-002
Requirement Traceability: REQ-TASK-04 (Task List Metrics)
Owned by: DevOps/QA (automated)
Tags: @performance @scalability @data-volume
```

---

#### TC-PERF-003: Analytics Dashboard Load Time <2 Seconds

```gherkin
Scenario: Analytics dashboard renders with 100K sessions logged
  Given user has 100,000 sessions across 1 year
  When dashboard is requested
  Then initial UI (with aggregated data) renders within 2 seconds
  And charts (heatmap, line chart, pie chart) render smoothly
  And filtering and date range changes complete within <500ms

Test ID: TC-PERF-003
Requirement Traceability: REQ-DASH-09 (Dashboard Performance)
Owned by: DevOps/QA (automated)
Tags: @performance @dashboard @load-time
```

---

#### TC-PERF-004: App Cold Launch Time

```gherkin
Scenario: App launches and is interactive within 2 seconds
  Given app is not in memory (cold start)
  When user taps app icon
  Then home screen is fully interactive (ready for "Start Session" click) within 2.0 seconds
  And time is measured from launch icon tap to first interactive element

Test ID: TC-PERF-004
Requirement Traceability: REQ-SYSTEM-02 (App Launch Performance)
Owned by: DevOps/QA (automated)
Tags: @performance @startup @responsiveness
```

---

## Test Execution Schedule

| Test Category | Frequency | Duration | Owner | Trigger |
|---|---|---|---|---|
| Unit Tests | Every commit (pre-merge gate) | <5 min | Dev Team | Pre-commit hook |
| Integration Tests | Post-merge to main | 15–20 min | QA Team | GitHub Actions / CI/CD |
| E2E Tests (Happy Paths) | Nightly | 30–45 min | QA Team | Scheduled (11 PM) |
| E2E Tests (Full Suite) | Pre-release | 60–90 min | QA Team | Manual trigger |
| Edge Case Tests | Before release | 30–40 min | QA Team | Manual trigger |
| Performance Tests | Weekly | 20–30 min | DevOps/QA | Scheduled (Friday) |
| Manual Accessibility | Pre-release | 2–3 hours | QA Team | Manual trigger |

---

## Test Case Summary

| Category | Count | Ownership | Automation |
|---|---|---|---|
| Unit Tests | 16 | Dev Team | 100% automated |
| Integration Tests | 43 | QA Team | 90% automated, 10% manual setup |
| E2E Tests | 36 | QA Team | 80% automated, 20% manual |
| Edge Case Tests | 28 | QA Team | 70% automated, 30% manual |
| Performance Tests | 4 | DevOps/QA | 100% automated |
| **Total** | **127** | — | — |

---

## Coverage by Requirement

| Requirement | Test Cases | Coverage Status |
|---|---|---|
| REQ-TIMER-01 (Start Session) | 6 | ✓ Complete |
| REQ-TIMER-02 (Display Format) | 5 | ✓ Complete |
| REQ-TIMER-03 (Pause/Resume) | 5 | ✓ Complete |
| REQ-TIMER-04 (Notification) | 5 | ✓ Complete |
| REQ-TIMER-05 (Break Transition) | 5 | ✓ Complete |
| REQ-TIMER-06 (Sleep/Wake) | 4 | ✓ Complete |
| REQ-TIMER-07 (Long Session) | 3 | ✓ Complete |
| REQ-TIMER-08 (Concurrent) | 5 | ✓ Complete |
| REQ-TASK-01 (Inline Create) | 6 | ✓ Complete |
| REQ-TASK-02 (Display During) | 4 | ✓ Complete |
| REQ-TASK-03 (Log Metadata) | 5 | ✓ Complete |
| REQ-TASK-04 (List Metrics) | 4 | ✓ Complete |
| REQ-TASK-05 (Search) | 4 | ✓ Complete |
| REQ-TASK-06 (Rename) | 4 | ✓ Complete |
| REQ-TASK-07 (Delete/Soft) | 5 | ✓ Complete |
| REQ-TASK-08 (Reassign) | 5 | ✓ Complete |
| REQ-BREAK-01 (Prompt) | 4 | ✓ Complete |
| REQ-BREAK-02 (Log) | 4 | ✓ Complete |
| REQ-BREAK-03 (Custom) | 4 | ✓ Complete |
| REQ-BREAK-04 (History) | 3 | ✓ Complete |
| REQ-BREAK-05 (Pattern) | 4 | ✓ Complete |
| REQ-CONFIG-01 (Defaults) | 5 | ✓ Complete |
| REQ-CONFIG-02 (Override) | 4 | ✓ Complete |
| REQ-CONFIG-03 (Preset) | 5 | ✓ Complete |
| REQ-CONFIG-04 (Switch) | 4 | ✓ Complete |
| REQ-CONFIG-05 (Reset) | 3 | ✓ Complete |
| REQ-DASH-01 (Daily) | 4 | ✓ Complete |
| REQ-DASH-02 (Weekly) | 4 | ✓ Complete |
| REQ-DASH-03 (Monthly) | 4 | ✓ Complete |
| REQ-DASH-04 (Task) | 4 | ✓ Complete |
| REQ-DASH-05 (Break) | 3 | ✓ Complete |
| REQ-DASH-06 (Export) | 4 | ✓ Complete |
| REQ-DASH-07 (Filter) | 4 | ✓ Complete |
| REQ-DASH-08 (Mobile) | 3 | ✓ Complete |
| REQ-DASH-09 (Perf) | 1 | ✓ Complete |
| REQ-INTEG-01 (OAuth) | 4 | ✓ Complete |
| REQ-INTEG-02 (Fetch) | 4 | ✓ Complete |
| REQ-INTEG-03 (Assign) | 3 | ✓ Complete |
| REQ-INTEG-04 (Complete) | 4 | ✓ Complete |
| REQ-INTEG-05 (Bi-Sync) | 3 | ✓ Complete |
| REQ-SYSTEM-01 (Persistence) | 4 | ✓ Complete |
| REQ-SYSTEM-02 (Launch Perf) | 1 | ✓ Complete |
| REQ-SYSTEM-03 (No Login) | 3 | ✓ Complete |
| REQ-SYSTEM-04 (Accessibility) | 6 | ✓ Complete |
| REQ-SYSTEM-05 (Cross-Platform) | 4 | ✓ Complete |

**Overall Coverage: 41 of 41 requirements covered (100%)**

---

## Risk Assessment & Mitigation

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| Timer accuracy drift over 24+ hours | High | Low | OS native timer; weekly performance test |
| Data loss on app crash | Critical | Very Low | Automatic backup; backup on every session end |
| OAuth token expiration during integration | Medium | Medium | Refresh token handling; manual retry flow |
| Performance degradation with 100K sessions | Medium | Low | Pagination, lazy loading, client-side indexing |
| Screen reader compatibility gaps | Medium | Medium | WCAG 2.1 AA audit; semantic HTML enforcement |
| Cross-platform UI inconsistency | Low | Low | Automated visual regression tests; manual spot-check |

---

## Test Environment Requirements

- Local dev: Node 18+, Jest, Sinon, test DB (SQLite in-memory)
- Staging: Docker containers, real database, test fixtures
- CI/CD: GitHub Actions, codecov integration, automated reporting
- Load testing: k6 for concurrent user simulation
- Monitoring: Grafana dashboards for performance trends

---

## Success Criteria

- ✓ All 127 test cases pass pre-release
- ✓ Code coverage ≥75% (≥80% for critical paths)
- ✓ 100% of acceptance criteria scenarios mapped to test cases
- ✓ Zero data loss incidents in crash recovery tests
- ✓ Timer accuracy ±1 second verified across all platforms
- ✓ WCAG 2.1 AA accessibility compliance achieved
- ✓ Cross-platform consistency verified (Windows, macOS, Linux, iOS, Android)
- ✓ Performance targets met (launch <2s, dashboard <2s, search <200ms)
- ✓ No critical bugs blocking release (severity 1 = 0 open)

---

## Appendix: Test Data Fixtures

**Sample Sessions:**
```
Session 1: Task="Coding: Feature A", Duration=50m, Status="completed"
Session 2: Task="Email", Duration=30m, Status="completed"
Session 3: Task="Coding: Feature A", Duration=90m, Status="interrupted" (paused at 45m)
Session 4: Task="Deep Work", Duration=60m, Status="completed"
```

**Sample Tasks:**
```
- Coding: Feature A (3 sessions, 2h 35m)
- Email Processing (8 sessions, 2h 40m)
- Deep Work - Research (2 sessions, 2h 00m)
- Meeting prep (1 session, 45m)
```

**Sample Break Activities:**
```
- Walk (12 logged)
- Meditation (5 logged)
- Coffee (8 logged)
- Stretch (3 logged)
- Custom: Guitar (2 logged)
```

---

**Test Plan Version:** 1.0  
**Created:** May 20, 2026  
**Owner:** QA Team + Dev Team + DevOps  
**Status:** Ready for Implementation
