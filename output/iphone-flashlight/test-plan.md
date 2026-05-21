# Test Plan: iPhone Flashlight App

## Test Plan Overview

The iPhone Flashlight app is a minimal, single-screen utility that allows users to toggle an LED flashlight with a tap. This test plan ensures the app delivers instant responsiveness, reliable LED control, proper permission handling, device compatibility, and power efficiency. Testing focuses on the core toggle functionality, edge cases around permissions and device constraints, and performance/power baselines.

**Scope:** LED toggle functionality, permission handling, device compatibility, battery/CPU efficiency, and UI responsiveness.

**Testing Approach:** Unit tests for state management and validation logic (Dev Team), integration tests for permission flows and LED control (QA Team), E2E tests for user journeys (QA Team), edge case testing for device constraints and error scenarios (QA Team), and performance/power testing for battery efficiency (DevOps/QA).

---

## Test Strategy

### Ownership & Responsibilities

- **Dev Team:** Unit tests for state toggle logic, permission state validation, and error handling (automated, pre-commit)
- **QA Team:** Integration/E2E tests for full user workflows, permission flows, device compatibility, and edge cases (automated + manual)
- **DevOps/QA Team:** Performance and battery efficiency testing (automated under load)

### Environment Setup

- **Local development environment:** Xcode with iOS simulator (multiple device models: iPhone 14, iPhone SE)
- **Physical test devices:** iPhone 12 or later (with LED flash capability) and iPad (for device constraint testing)
- **Test data:** Pre-configured permission states, mock device capabilities
- **State reset:** Clear app permissions and data between test runs

### CI/CD Integration

- **Unit tests:** Run on every commit (pre-merge gate), must achieve ≥80% coverage for LED toggle logic
- **Integration/E2E tests:** Run on PR merge to main, nightly for comprehensive coverage
- **Performance/Battery tests:** Run weekly and before releases to detect regressions
- **Failed tests:** Block merges to main if any critical toggle or permission test fails

### Dependencies & Tools

*Not specified in requirements; assume iOS standard libraries:*
- **iOS Framework:** AVFoundation (torch mode for LED control)
- **Permission System:** AVCaptureDevice, CoreMotion for device capability detection
- **Testing Framework:** XCTest (Apple's standard)
- **Performance Monitoring:** Xcode Profiler, Activity Monitor for battery/CPU metrics

### Coverage Goals

- **Unit tests:** 85%+ coverage of toggle state machine and permission validation
- **Integration tests:** 100% of permission grant/deny flows, all device types
- **E2E tests:** 100% of user journeys (cold start, toggle, background/close)
- **Edge cases:** 100% of device constraints, permission denial scenarios
- **Performance tests:** Battery parity with native flashlight (measured on real devices)
- **Overall:** 90%+ combined coverage

### Test Data Strategy

- **Unit tests:** Mock AVCaptureDevice, mock permission states (granted/denied/undetermined)
- **Integration tests:** Real device permission flows, test fixtures for app state
- **E2E tests:** Real or simulator environment with permissions pre-configured
- **Edge cases:** Simulate device without LED (iPad), permission denial, permission revocation after startup
- **Performance tests:** Real devices with 1-hour usage cycles, battery drain measurement

---

## Test Objectives

**Quality Standards:**
- Instant responsiveness: LED illuminates within 100ms, app loads in <500ms
- Reliability: No crashes on permission denial, device constraint, or background transition
- Accessibility: WCAG AA contrast (≥4.5:1), color-blind friendly indicators
- Efficiency: Power consumption ≤ native iPhone flashlight, idle CPU <1%

**Critical User Workflows:**
- Tap to toggle LED on, tap to toggle off
- Cold start (home screen to interactive) in <500ms
- Permission grant flow without interruption
- App backgrounding without LED hang-over

**Risk Areas to Prevent Regression:**
- Permission state inconsistencies (app thinks LED is on, hardware is off)
- Memory leaks during repeated toggle
- Battery drain from background processes
- Crash on unsupported devices

---

## Test Scope

### In Scope

- LED toggle on/off functionality (core feature)
- State indicator UI (on/off visual feedback)
- Permission request and grant flow
- Permission denial and recovery
- Device capability detection (LED availability)
- Cold start performance (<500ms)
- Warm start performance (reopen app)
- Background/foreground transitions
- Battery and CPU efficiency
- WCAG AA accessibility (contrast, color-blind design)

### Out of Scope

- iOS system-level permission settings UI (controlled by OS)
- Third-party permission management tools
- Network connectivity (app does not require network)
- iCloud sync or user accounts (app is standalone)
- Custom gestures beyond tap-to-toggle
- Multi-device (iPad) feature parity (iPad lacks LED; feature unavailable by design)

---

## Requirement Traceability Matrix

| REQ ID | Feature | Acceptance Criteria | Test Category | Owned by |
|--------|---------|-------------------|----------------|----------|
| REQ-TOGGLE-01 | Single-Tap LED Toggle | AC-FL-TOGGLE-01-01 to 01-08 | Unit, Integration, E2E, Edge, Performance | Dev/QA/DevOps |
| REQ-TOGGLE-01-SC1 | LED On from Off State | AC-FL-TOGGLE-01-01 | Unit, Integration, E2E | Dev/QA |
| REQ-TOGGLE-01-SC2 | LED Off from On State | AC-FL-TOGGLE-01-02 | Unit, Integration, E2E | Dev/QA |
| REQ-TOGGLE-01-SC3 | App Background/Close | AC-FL-TOGGLE-01-03 | Integration, E2E | QA |
| REQ-TOGGLE-01-SC4 | Visual State Indicator | AC-FL-TOGGLE-01-04 | E2E, Accessibility | QA |
| REQ-TOGGLE-01-SC5 | Cold Start Performance | AC-FL-TOGGLE-01-05 | Performance, E2E | DevOps/QA |
| REQ-TOGGLE-01-SC6 | Permission Handling | AC-FL-TOGGLE-01-06 | Integration, E2E, Edge | QA |
| REQ-TOGGLE-01-SC7 | Device Constraints | AC-FL-TOGGLE-01-07 | Edge Case | QA |
| REQ-TOGGLE-01-SC8 | Battery & CPU Efficiency | AC-FL-TOGGLE-01-08 | Performance | DevOps/QA |

---

## Test Cases

### 1. Unit Tests (Dev Team)

**TC-UNIT-001: LED state toggles from off to on**
- **Test Strategy:** Validate toggle state machine transition from off→on
- **Test Inputs:** Current state = off, toggle action triggered
- **Expected:** State changes to on, no exceptions thrown
- **Coverage:** State machine transition logic for off→on
- **Owned by:** Dev Team (automated unit test, pre-commit)
- **Requirement Traceability:** REQ-TOGGLE-01-SC1
- **Tags:** @unit @state-machine @toggle

**TC-UNIT-002: LED state toggles from on to off**
- **Test Strategy:** Validate toggle state machine transition from on→off
- **Test Inputs:** Current state = on, toggle action triggered
- **Expected:** State changes to off, no exceptions thrown
- **Coverage:** State machine transition logic for on→off
- **Owned by:** Dev Team (automated unit test, pre-commit)
- **Requirement Traceability:** REQ-TOGGLE-01-SC2
- **Tags:** @unit @state-machine @toggle

**TC-UNIT-003: Permission validation allows toggle only when granted**
- **Test Strategy:** Verify toggle action is blocked if permission not granted
- **Test Inputs:** Permission state = denied/undetermined, toggle action triggered
- **Expected:** Toggle is rejected, permission request is triggered
- **Coverage:** Permission check before toggle execution
- **Owned by:** Dev Team (automated unit test, pre-commit)
- **Requirement Traceability:** REQ-TOGGLE-01-SC6
- **Tags:** @unit @permission @validation

**TC-UNIT-004: Device capability check detects LED availability**
- **Test Strategy:** Validate device capability detection for LED flash
- **Test Inputs:** AVCaptureDevice.default() with torch mode, device without LED (mocked)
- **Expected:** Torch device found on iPhone, nil on iPad/unsupported device
- **Coverage:** Device capability detection logic
- **Owned by:** Dev Team (automated unit test, pre-commit)
- **Requirement Traceability:** REQ-TOGGLE-01-SC7
- **Tags:** @unit @device-check @capability

**TC-UNIT-005: Error state when device lacks LED capability**
- **Test Strategy:** Verify graceful error handling for devices without LED
- **Test Inputs:** AVCaptureDevice.default(for: .video) returns nil (iPad simulation)
- **Expected:** App sets error state, no crash, error message queued for UI
- **Coverage:** Error handling for missing hardware
- **Owned by:** Dev Team (automated unit test, pre-commit)
- **Requirement Traceability:** REQ-TOGGLE-01-SC7
- **Tags:** @unit @error-handling @device-constraint

**TC-UNIT-006: Toggle action ignored if LED is currently transitioning**
- **Test Strategy:** Verify rapid taps don't cause conflicting state changes
- **Test Inputs:** User taps rapidly (within 50ms of previous toggle)
- **Expected:** Second tap is queued or ignored, no concurrent state changes
- **Coverage:** State mutation safety, concurrent tap handling
- **Owned by:** Dev Team (automated unit test, pre-commit)
- **Requirement Traceability:** REQ-TOGGLE-01-SC1, SC2
- **Tags:** @unit @concurrency @state-safety

---

### 2. Integration Tests (QA Team)

**TC-INTEGRATION-001: Permission grant enables LED toggle**
```gherkin
Scenario: User grants permission and toggles LED immediately
  Given the app is open and flashlight permission is undetermined
  When the user attempts to toggle the LED
  Then the system shows the permission request dialog
  And when the user taps "Allow"
  Then the LED turns on within 100ms
  And the permission is persisted for future toggles

Test ID: TC-INTEGRATION-001
Requirement Traceability: REQ-TOGGLE-01-SC6
Owned by: QA Team (manual + automated)
Tags: @integration @permission-flow @REQ-TOGGLE-01-SC6
```

**TC-INTEGRATION-002: Permission denial prevents toggle and shows guidance**
```gherkin
Scenario: User denies permission and sees guidance
  Given the app is open and flashlight permission is undetermined
  When the user attempts to toggle the LED
  Then the system shows the permission request dialog
  And when the user taps "Don't Allow"
  Then the LED does not turn on
  And a message guides the user: "Enable flashlight in Settings > [App Name] > Camera"

Test ID: TC-INTEGRATION-002
Requirement Traceability: REQ-TOGGLE-01-SC6
Owned by: QA Team (manual + automated)
Tags: @integration @permission-denial @error-message @REQ-TOGGLE-01-SC6
```

**TC-INTEGRATION-003: LED turns off when app is backgrounded**
```gherkin
Scenario: LED stops immediately when app is backgrounded
  Given the app is open and the LED is on
  When the user switches to another app (home button or swipe up)
  Then the LED turns off within 100ms
  And when the user returns to the Flashlight app
  And the LED state indicator shows "off"

Test ID: TC-INTEGRATION-003
Requirement Traceability: REQ-TOGGLE-01-SC3
Owned by: QA Team (manual + automated)
Tags: @integration @lifecycle @background-transition @REQ-TOGGLE-01-SC3
```

**TC-INTEGRATION-004: LED turns off when app is force-closed**
```gherkin
Scenario: LED stops when user force-quits app
  Given the app is open and the LED is on
  When the user force-closes the app (swipe up and hold, then close)
  Then the LED turns off immediately
  And when the user reopens the app
  And the LED state indicator shows "off"

Test ID: TC-INTEGRATION-004
Requirement Traceability: REQ-TOGGLE-01-SC3
Owned by: QA Team (manual + automated)
Tags: @integration @lifecycle @app-termination @REQ-TOGGLE-01-SC3
```

**TC-INTEGRATION-005: State indicator updates synchronously with LED**
```gherkin
Scenario: Visual indicator matches LED state in real-time
  Given the app is open and the LED is off
  When the user taps the screen to toggle on
  Then the state indicator changes to "on" state (color, text, or symbol)
  And when the user taps again to toggle off
  Then the state indicator changes to "off" state

Test ID: TC-INTEGRATION-005
Requirement Traceability: REQ-TOGGLE-01-SC4
Owned by: QA Team (automated visual verification)
Tags: @integration @ui-state-sync @REQ-TOGGLE-01-SC4
```

**TC-INTEGRATION-006: Permission revocation is handled on app restart**
```gherkin
Scenario: User revokes permission in Settings, app detects on restart
  Given the app has flashlight permission granted
  And the user opens Settings and revokes flashlight (Camera) permission
  When the user reopens the Flashlight app
  Then the app detects the permission revocation
  And when the user attempts to toggle the LED
  Then the permission request dialog appears again
  And a message guides the user to Settings

Test ID: TC-INTEGRATION-006
Requirement Traceability: REQ-TOGGLE-01-SC6
Owned by: QA Team (manual + automated)
Tags: @integration @permission-revocation @REQ-TOGGLE-01-SC6
```

---

### 3. End-to-End Tests (QA Team)

**TC-E2E-001: Full cold start to first toggle**
```gherkin
Scenario: User launches app for first time and toggles LED
  Given the user taps the Flashlight app icon from the home screen
  And the app is launching for the first time
  When the app loads
  Then the toggle screen is visible and interactive within 500ms
  And no splash screen, onboarding, or unexpected permission prompts appear
  And when the user taps the screen to toggle
  Then the LED turns on within 100ms
  And the state indicator shows "on"

Test ID: TC-E2E-001
Requirement Traceability: REQ-TOGGLE-01-SC5, REQ-TOGGLE-01-SC1
Owned by: QA Team (manual + automated)
Tags: @e2e @cold-start @first-launch @REQ-TOGGLE-01-SC5
```

**TC-E2E-002: Rapid toggle on and off**
```gherkin
Scenario: User toggles LED on and off rapidly
  Given the app is open and the LED is off
  When the user taps to toggle on
  And waits 200ms
  And taps to toggle off
  And waits 200ms
  And taps to toggle on again
  Then each toggle completes within 100ms
  And the state indicator reflects the current LED state accurately each time
  And no LED flicker or state inconsistency occurs

Test ID: TC-E2E-002
Requirement Traceability: REQ-TOGGLE-01-SC1, REQ-TOGGLE-01-SC2
Owned by: QA Team (automated)
Tags: @e2e @rapid-toggle @state-consistency @REQ-TOGGLE-01-SC1
```

**TC-E2E-003: Warm start (reopen app with LED on)**
```gherkin
Scenario: User closes and reopens app, LED state is preserved
  Given the app is open and the LED is on
  When the user switches away (background app)
  And within 2 minutes, reopens the app
  Then the LED remains off (per backgrounding requirement)
  And the state indicator shows "off"
  And the user can toggle on again without issues

Test ID: TC-E2E-003
Requirement Traceability: REQ-TOGGLE-01-SC3, REQ-TOGGLE-01-SC2
Owned by: QA Team (manual + automated)
Tags: @e2e @warm-start @state-recovery @REQ-TOGGLE-01-SC3
```

**TC-E2E-004: Accessibility - State indicator contrast and color-blindness**
```gherkin
Scenario: State indicator meets accessibility standards
  Given the app is open
  When the user views the state indicator in on and off states
  Then the contrast ratio between indicator and background is ≥4.5:1 (WCAG AA)
  And the indicator is distinguishable without relying on color alone
  (e.g., includes text label, pattern, or shape change)
  And screen readers announce "LED is on" and "LED is off" correctly

Test ID: TC-E2E-004
Requirement Traceability: REQ-TOGGLE-01-SC4
Owned by: QA Team (manual accessibility review + automated contrast test)
Tags: @e2e @accessibility @wcag-aa @color-blind @REQ-TOGGLE-01-SC4
```

---

### 4. Edge Case & Error Handling Tests (QA Team)

**TC-EDGE-001: Device without LED flash (iPad)**
```gherkin
Scenario: User opens Flashlight app on iPad (no LED)
  Given the user opens the Flashlight app on an iPad
  When the app initializes and detects no LED capability
  Then an error message displays: "Flashlight not available on this device"
  And the toggle button is disabled or hidden
  And the app does not crash or hang
  And the user can dismiss the message

Test ID: TC-EDGE-001
Requirement Traceability: REQ-TOGGLE-01-SC7
Owned by: QA Team (manual on iPad, automated simulator test)
Tags: @edge-case @device-constraint @unsupported-hardware @REQ-TOGGLE-01-SC7
```

**TC-EDGE-002: Rapid permission grant/deny cycles**
```gherkin
Scenario: User grants, denies, then re-grants permission rapidly
  Given the app is open and permission is undetermined
  When the user taps to toggle (permission request appears)
  And taps "Allow" (permission granted)
  Then the LED toggles on
  And when the user reopens the app, goes to Settings, revokes permission, and returns
  And taps to toggle again
  Then the permission request appears
  And when the user taps "Allow" again
  Then the LED toggles on and the app works normally

Test ID: TC-EDGE-002
Requirement Traceability: REQ-TOGGLE-01-SC6
Owned by: QA Team (manual)
Tags: @edge-case @permission-cycles @state-recovery @REQ-TOGGLE-01-SC6
```

**TC-EDGE-003: LED state mismatch detection**
```gherkin
Scenario: Hardware and app state become out of sync (rare but testable)
  Given the LED is on in the app
  When a background system process interferes or LED hardware becomes unavailable
  And the app attempts to toggle
  Then the app detects the state mismatch
  And the state indicator corrects to reflect reality
  And the next toggle succeeds

Test ID: TC-EDGE-003
Requirement Traceability: REQ-TOGGLE-01-SC1, REQ-TOGGLE-01-SC2
Owned by: QA Team (simulated in integration test environment)
Tags: @edge-case @state-mismatch @recovery @REQ-TOGGLE-01-SC1
```

**TC-EDGE-004: Screen timeout while LED is on**
```gherkin
Scenario: Device screen locks while LED is on
  Given the app is open and the LED is on
  When the device screen times out and locks (after 30-60 seconds)
  Then the LED remains on (app is backgrounded but still running)
  And when the user unlocks the device and reopens the app
  And the LED state shows "on"
  And the user can toggle off successfully

Test ID: TC-EDGE-004
Requirement Traceability: REQ-TOGGLE-01-SC3
Owned by: QA Team (manual)
Tags: @edge-case @screen-lock @state-persistence @REQ-TOGGLE-01-SC3
```

**TC-EDGE-005: Multiple rapid taps before first LED activation**
```gherkin
Scenario: User mashes the toggle button before LED first activates
  Given the app is open, LED is off, and user taps rapidly 5+ times
  When the taps are received faster than LED hardware can respond
  Then the app queues or coalesces the taps
  And after the first activation (100ms), the subsequent taps are processed in order
  And the LED state is predictable and consistent
  And no crash or undefined behavior occurs

Test ID: TC-EDGE-005
Requirement Traceability: REQ-TOGGLE-01-SC1, REQ-TOGGLE-01-SC2
Owned by: QA Team (automated rapid-tap stress test)
Tags: @edge-case @rapid-input @state-stability @REQ-TOGGLE-01-SC1
```

---

### 5. Performance & Load Tests (DevOps/QA)

**TC-PERF-001: Cold start time <500ms**
```gherkin
Scenario: App launches from home screen in <500ms
  Given the user taps the Flashlight app icon from the home screen
  When the app initializes (cold start, no background process)
  Then the toggle screen is loaded and interactive within 500ms
  And the user can tap to toggle within this time
  And this latency is consistent across multiple cold starts

Test ID: TC-PERF-001
Requirement Traceability: REQ-TOGGLE-01-SC5
Owned by: DevOps/QA Team (automated performance profiling)
Tags: @performance @cold-start @responsiveness @REQ-TOGGLE-01-SC5
```

**TC-PERF-002: LED toggle latency <100ms**
```gherkin
Scenario: LED illuminates within 100ms of tap
  Given the app is open, LED is off, and permission is granted
  When the user taps the screen to toggle on
  Then the LED hardware activates within 100ms
  (Measured from touch event to LED light output)
  And this latency holds under repeated toggles over 1 hour of continuous use

Test ID: TC-PERF-002
Requirement Traceability: REQ-TOGGLE-01-SC1
Owned by: DevOps/QA Team (automated instrumented testing with LED sensor)
Tags: @performance @responsiveness @latency @REQ-TOGGLE-01-SC1
```

**TC-PERF-003: Battery consumption ≤ native flashlight**
```gherkin
Scenario: Flashlight app power draw matches native iOS flashlight
  Given an iPhone with full battery (100%)
  When the Flashlight app LED is on continuously for 1 hour
  And the native iOS Control Center flashlight is on for 1 hour (separate test)
  Then the Flashlight app power consumption ≤ native flashlight
  And battery drain is measured in mAh and compared

Test ID: TC-PERF-003
Requirement Traceability: REQ-TOGGLE-01-SC8
Owned by: DevOps/QA Team (manual battery drain test on real device)
Tags: @performance @power-efficiency @battery-drain @REQ-TOGGLE-01-SC8
```

**TC-PERF-004: CPU usage idle <1%**
```gherkin
Scenario: App consumes minimal CPU when LED is off
  Given the app is open and the LED is off
  When the user leaves the app idle for 2 minutes (no toggles)
  Then CPU usage is <1% average during the idle period
  (Measured via Xcode Profiler or Activity Monitor on real device)
  And no background threads are spinning or polling

Test ID: TC-PERF-004
Requirement Traceability: REQ-TOGGLE-01-SC8
Owned by: DevOps/QA Team (automated CPU profiling)
Tags: @performance @cpu-efficiency @idle-power @REQ-TOGGLE-01-SC8
```

**TC-PERF-005: No battery drain after app close**
```gherkin
Scenario: App does not drain battery after being closed
  Given the Flashlight app was open with LED on
  When the user closes the app
  Then all background processes terminate
  And CPU usage drops to 0%
  And no LED hardware activity persists
  And battery drain over 1 hour post-close is the baseline device idle drain (no app contribution)

Test ID: TC-PERF-005
Requirement Traceability: REQ-TOGGLE-01-SC8
Owned by: DevOps/QA Team (manual battery baseline test)
Tags: @performance @background-power @cleanup @REQ-TOGGLE-01-SC8
```

**TC-PERF-006: Memory stability over extended use**
```gherkin
Scenario: App memory footprint remains stable over 1000 toggles
  Given the app is open
  When the user toggles the LED on/off repeatedly for 1000 cycles over 30 minutes
  Then memory usage remains ≤ 50MB at end of test
  And no memory leaks are detected (heap grows <5MB from start)
  And the app remains responsive (toggle latency stays <100ms)

Test ID: TC-PERF-006
Requirement Traceability: REQ-TOGGLE-01-SC1, REQ-TOGGLE-01-SC8
Owned by: DevOps/QA Team (automated stress test with memory profiling)
Tags: @performance @memory-stability @stress-test @REQ-TOGGLE-01-SC1
```

---

## Test Execution Summary

### Test Case Count by Category

| Category | Count | Owned by | Execution Timing |
|----------|-------|----------|------------------|
| Unit Tests | 6 | Dev Team | Pre-commit (automated) |
| Integration Tests | 6 | QA Team | Post-merge (automated + manual) |
| E2E Tests | 4 | QA Team | Nightly (automated + manual) |
| Edge Case Tests | 5 | QA Team | Pre-release (manual) |
| Performance Tests | 6 | DevOps/QA | Weekly (automated) |
| **Total** | **27** | **Dev/QA/DevOps** | **Continuous + Nightly + Weekly** |

### Coverage by Requirement

| Requirement | Test Cases | Coverage % |
|-------------|-----------|-----------|
| REQ-TOGGLE-01-SC1 (LED On) | TC-UNIT-001, TC-UNIT-002, TC-E2E-001, TC-E2E-002, TC-PERF-002, TC-PERF-006 | 100% |
| REQ-TOGGLE-01-SC2 (LED Off) | TC-UNIT-002, TC-E2E-002, TC-E2E-003 | 100% |
| REQ-TOGGLE-01-SC3 (Background/Close) | TC-INTEGRATION-003, TC-INTEGRATION-004, TC-E2E-003, TC-EDGE-004 | 100% |
| REQ-TOGGLE-01-SC4 (Visual Indicator) | TC-INTEGRATION-005, TC-E2E-004 | 100% |
| REQ-TOGGLE-01-SC5 (Cold Start) | TC-E2E-001, TC-PERF-001 | 100% |
| REQ-TOGGLE-01-SC6 (Permissions) | TC-UNIT-003, TC-INTEGRATION-001, TC-INTEGRATION-002, TC-INTEGRATION-006, TC-EDGE-002 | 100% |
| REQ-TOGGLE-01-SC7 (Device Constraints) | TC-UNIT-004, TC-UNIT-005, TC-EDGE-001 | 100% |
| REQ-TOGGLE-01-SC8 (Battery & CPU) | TC-PERF-003, TC-PERF-004, TC-PERF-005, TC-PERF-006 | 100% |

**Overall Coverage:** 100% of acceptance criteria mapped to test cases.

### Ownership Breakdown

- **Dev Team:** 6 unit tests (pre-commit, fully automated)
- **QA Team:** 15 integration/E2E/edge case tests (post-merge + nightly + pre-release, manual + automated)
- **DevOps/QA Team:** 6 performance tests (weekly + pre-release, automated profiling + manual)

### Estimated Effort

| Phase | Task | Effort | Timeline |
|-------|------|--------|----------|
| **Setup** | Xcode project, test framework, device setup (iPhone + iPad) | 4 hours | 1 day |
| **Unit Tests** | 6 tests, mocking AVCaptureDevice & permission states | 8 hours | 1-2 days |
| **Integration Tests** | 6 tests, permission flows, app lifecycle, state sync | 12 hours | 2-3 days |
| **E2E Tests** | 4 tests, cold/warm start, accessibility, full workflows | 8 hours | 1-2 days |
| **Edge Cases** | 5 tests, device constraints, permission cycles, state mismatch | 10 hours | 2-3 days |
| **Performance Tests** | 6 tests, battery profiling, cold start timing, memory stability | 12 hours | 2-3 days |
| **CI/CD Integration** | GitHub Actions or similar, automated test runs, reporting | 6 hours | 1 day |
| **Total (all phases)** | | **60 hours** | **2-3 weeks** |

---

## Key Testing Assumptions & Flags

1. **iOS SDK Tools:** Assumes Xcode and XCTest are available; no additional test framework specified (using Apple standard).
2. **Permission Testing:** Requires manual toggling of iOS Settings; simulator permission flows may differ from real device.
3. **Battery Profiling:** Real device testing required; simulator cannot accurately measure power consumption.
4. **Device Availability:** Assumes access to iPhone (with LED) and iPad (without LED) for device constraint testing.
5. **WCAG Accessibility:** Manual review required for color-blind design validation; automated contrast ratio tools can supplement.
6. **Baseline Comparison:** Battery parity test requires running native iOS flashlight in parallel on same device.

---

## Success Criteria

All test categories must **pass** before release:

- ✅ 100% of unit tests pass (0 failures)
- ✅ 100% of integration/E2E tests pass (0 failures)
- ✅ 100% of edge case tests pass (0 failures)
- ✅ Cold start latency <500ms (measured on iPhone 12+)
- ✅ LED toggle latency <100ms (measured 100+ times)
- ✅ Battery consumption ≤ native flashlight (measured 1 hour continuous)
- ✅ Idle CPU usage <1% (measured 2 minutes idle)
- ✅ State indicator meets WCAG AA contrast (≥4.5:1)
- ✅ No memory leaks detected over 1000 toggle cycles
- ✅ App does not crash on unsupported device (iPad)
