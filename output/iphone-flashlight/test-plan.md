# iPhone Flashlight — Test Plan

**Project Code:** FL (Flashlight)

---

## Test Plan Overview

This test plan covers the LED Toggle feature for the iPhone Flashlight app. The app provides a single-button interface to turn the iPhone LED on and off. Testing focuses on core functionality (state toggling), state persistence, hardware availability handling, and performance requirements. The strategy combines unit tests for business logic, integration tests for button-to-LED-to-UI workflows, E2E tests for user journeys, and edge case coverage for error scenarios.

**Scope:** LED Toggle Button feature; state management; error handling; performance constraints
**Boundaries:** Does not cover Settings, Brightness Controls, Multiple Modes, or Customization
**Testing Approach:** Unit (automated), Integration (automated), E2E (manual + automated), Edge Case (manual + automated), Performance (automated)

---

## Test Strategy

### Ownership & Responsibilities

| Team | Responsibility | Test Categories |
|------|---|---|
| **Dev Team** | Unit tests, business logic validation | Unit Tests (TC-UNIT-*) |
| **QA Team** | Integration, E2E, edge case, manual testing | Integration (TC-INTEGRATION-*), E2E (TC-E2E-*), Edge Case (TC-EDGE-*) |
| **DevOps Team** | Performance testing, CI/CD pipeline, test infrastructure | Performance (TC-PERF-*), Environment Setup |

### Environment Setup

- **Local Development:** Xcode (iOS SDK), Swift testing framework (XCTest)
- **Staging Environment:** iOS simulator with mock LED hardware and real device testing
- **Test Infrastructure:** CI/CD pipeline (GitHub Actions / GitLab CI), test reporting, device farm for real device testing
- **Mock/Stub Libraries:** Mock LED HAL (hardware abstraction layer) for simulator testing
- **Device Testing:** Real iPhone with LED capability for E2E and performance validation
- **Test Data:** Fixtures for LED state (on/off), button press events

### CI/CD Integration

| Test Category | Trigger | Gate | Frequency |
|---|---|---|---|
| Unit Tests | Every commit | ✓ Blocks merge | Pre-commit |
| Integration Tests | PR merge to main | ✓ Blocks merge | Post-merge, before release |
| E2E Tests | On-demand, before release | ✓ Release gate | Nightly or pre-release |
| Edge Case Tests | Before release | ✓ Release gate | Before release |
| Performance Tests | Before release | ✓ Release gate | Before release |

### Dependencies & Tools

- **Testing Framework:** XCTest (native iOS testing)
- **Mock/Stub Libraries:** XCTest Mock & Spy, or equivalent LED hardware mocking
- **Real Device Testing:** iPhone physical device with LED
- **CI/CD Platform:** GitHub Actions or GitLab CI
- **Performance Monitoring:** Instruments (Xcode built-in), timing assertions in tests
- **Coverage Reporting:** Code coverage via Xcode / Codecov
- **Test Management:** Test case tracking in project management tool (Linear, Jira, etc.)

### Coverage Goals

| Category | Goal |
|---|---|
| Unit Tests | ≥85% code coverage for LED toggle logic |
| Integration Tests | ≥80% of critical workflows (button→LED→UI) |
| E2E Tests | 100% of acceptance criteria scenarios |
| Edge Cases | ≥90% of documented edge cases |
| Performance Tests | 100% of timing-critical paths |
| **Overall** | ≥80% combined code coverage |

---

## Test Objectives

1. **Verify core functionality:** LED toggles on/off with single button press
2. **Validate state consistency:** LED state matches visual indicator; persists across suspend/resume
3. **Ensure error handling:** Graceful degradation when LED is unavailable
4. **Confirm performance:** Toggle response < 100 milliseconds
5. **Prevent scope creep:** Verify no extraneous UI elements (settings, menus, options) exist
6. **Test resilience:** Handle rapid button presses without state corruption

---

## Test Scope

### In Scope
- LED toggle functionality (on/off state transitions)
- Visual state indicator (matches LED state)
- Button press event handling
- State persistence (across app suspend/resume)
- Hardware unavailability error handling
- Performance: button press → LED state change (< 100ms)
- No additional UI or settings
- Rapid/repeated toggle handling

### Out of Scope
- Settings or preferences
- Brightness controls
- Multiple lighting modes
- App customization
- Network connectivity
- Third-party integrations
- Accessibility features (covered separately if needed)

---

## Requirement Traceability

| Requirement ID | Description | User Story | Acceptance Criteria | Test IDs | Coverage |
|---|---|---|---|---|---|
| **REQ-FL-TOGGLE-01** | LED Toggle Control | US-FL-TOGGLE-01 | AC-FL-TOGGLE-01-01 through -07 | TC-UNIT-001, TC-INTEGRATION-001, TC-INTEGRATION-002, TC-E2E-001, TC-E2E-002, TC-EDGE-001, TC-EDGE-002, TC-EDGE-003, TC-PERF-001 | ✓ Complete |
| **REQ-FL-TOGGLE-01-SC1** | LED Turns On with Single Press | US-FL-TOGGLE-01 | AC-FL-TOGGLE-01-01 | TC-INTEGRATION-001, TC-E2E-001 | ✓ Covered |
| **REQ-FL-TOGGLE-01-SC2** | LED Turns Off with Single Press | US-FL-TOGGLE-01 | AC-FL-TOGGLE-01-02 | TC-INTEGRATION-002, TC-E2E-001 | ✓ Covered |
| **REQ-FL-TOGGLE-01-SC3** | Toggle Response Time < 100ms | US-FL-TOGGLE-01 | AC-FL-TOGGLE-01-03 | TC-UNIT-001, TC-PERF-001 | ✓ Covered |
| **REQ-FL-TOGGLE-01-SC4** | Repeated Toggle Cycles Correctly | US-FL-TOGGLE-01 | AC-FL-TOGGLE-01-04 | TC-EDGE-002, TC-INTEGRATION-003 | ✓ Covered |
| **REQ-FL-TOGGLE-01-SC5** | State Persists Across Suspend/Resume | US-FL-TOGGLE-01 | AC-FL-TOGGLE-01-05 | TC-INTEGRATION-003, TC-E2E-002 | ✓ Covered |
| **REQ-FL-TOGGLE-01-SC6** | Graceful Degradation on Hardware Unavailable | US-FL-TOGGLE-01 | AC-FL-TOGGLE-01-06 | TC-EDGE-001, TC-EDGE-003 | ✓ Covered |
| **REQ-FL-TOGGLE-01-SC7** | No Additional UI or Settings | US-FL-TOGGLE-01 | AC-FL-TOGGLE-01-07 | TC-EDGE-004 | ✓ Covered |

**Coverage Summary:** 7 of 7 requirements covered (100%)
**Gap Analysis:** No uncovered requirements
**Test Count by Category:** Unit: 3, Integration: 4, E2E: 2, Edge Case: 4, Performance: 1 | **Total: 14 test cases**

---

## Test Categories

### 1. Unit Tests (Dev Team - Owned)

**TC-UNIT-001: LED Toggle State Inversion Logic**

Test Strategy: Validate LED state toggle logic inverts state correctly from on↔off

- **Test Inputs:** 
  - Current state: off → toggle → expected: on
  - Current state: on → toggle → expected: off
  - Repeated toggles: off → on → off → on (verify state cycles correctly)
- **Expected Outcomes:** 
  - State inverts deterministically on each toggle
  - No state becomes undefined or locked
  - State matches boolean value (true=on, false=off)
- **Coverage:** LEDToggle.toggle() method, state inversion logic
- **Owned by:** Dev Team (automated, pre-commit)

Requirement Traceability: REQ-FL-TOGGLE-01-SC3, REQ-FL-TOGGLE-01-SC4
Tags: @unit @logic @state-inversion @REQ-FL-TOGGLE-01

---

**TC-UNIT-002: LED State Persistence to Storage**

Test Strategy: Validate LED state is persisted to local storage and retrieved correctly

- **Test Inputs:**
  - LED state on → save to storage → retrieve → verify = on
  - LED state off → save to storage → retrieve → verify = off
  - App terminated with LED on → app reopened → retrieve state = on
- **Expected Outcomes:**
  - State persists to UserDefaults / local storage
  - State retrieves correctly without data corruption
  - Default state (off) is used if no saved state exists
- **Coverage:** StateManager.saveState(), StateManager.loadState(), data persistence logic
- **Owned by:** Dev Team (automated, pre-commit)

Requirement Traceability: REQ-FL-TOGGLE-01-SC5
Tags: @unit @persistence @storage @REQ-FL-TOGGLE-01

---

**TC-UNIT-003: UI State Indicator Update Logic**

Test Strategy: Validate visual indicator matches LED state

- **Test Inputs:**
  - LED state = on → UI indicator text/color/icon = "On" / green / filled
  - LED state = off → UI indicator text/color/icon = "Off" / gray / outlined
  - State change on → off → UI updates immediately
- **Expected Outcomes:**
  - UI indicator reflects current LED state
  - Indicator updates synchronously with state change
  - No lag or desynchronization between LED and UI
- **Coverage:** UIStateController.updateIndicator(), view binding logic
- **Owned by:** Dev Team (automated, pre-commit)

Requirement Traceability: REQ-FL-TOGGLE-01-SC1, REQ-FL-TOGGLE-01-SC2
Tags: @unit @ui-binding @state-sync @REQ-FL-TOGGLE-01

---

### 2. Integration Tests (QA Team - Owned)

**TC-INTEGRATION-001: Button Press Toggles LED From Off to On**

```gherkin
Scenario: User presses button and LED turns on
  Given the app is open and the LED is currently off
  When the user presses the toggle button once
  Then the iPhone LED illuminates immediately
  And the app displays a visual indicator confirming the LED is on
  And the LED state is saved to storage
```

- **Test ID:** TC-INTEGRATION-001
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC1
- **Owned by:** QA Team (automated + manual validation on real device)
- **Preconditions:** App is running, LED is off, device has LED capability
- **Expected Outcomes:** LED on, indicator shows "On", state persisted
- **Tags:** @integration @button-press @led-on @REQ-FL-TOGGLE-01-SC1

---

**TC-INTEGRATION-002: Button Press Toggles LED From On to Off**

```gherkin
Scenario: User presses button and LED turns off
  Given the app is open and the LED is currently on
  When the user presses the toggle button once
  Then the iPhone LED turns off immediately
  And the app displays a visual indicator confirming the LED is off
  And the LED state is saved to storage
```

- **Test ID:** TC-INTEGRATION-002
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC2
- **Owned by:** QA Team (automated + manual validation on real device)
- **Preconditions:** App is running, LED is on, device has LED capability
- **Expected Outcomes:** LED off, indicator shows "Off", state persisted
- **Tags:** @integration @button-press @led-off @REQ-FL-TOGGLE-01-SC2

---

**TC-INTEGRATION-003: LED State Persists Across App Suspend/Resume**

```gherkin
Scenario: User suspends and resumes app while LED is on
  Given the LED is currently on
  When the user backgrounds the app (swipe up / home button)
  And the user resumes the app
  Then the LED remains on
  And the visual indicator matches the actual LED state
  And no state desynchronization occurs
```

- **Test ID:** TC-INTEGRATION-003
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC5
- **Owned by:** QA Team (manual on real device)
- **Preconditions:** App running, LED is on
- **Expected Outcomes:** LED state unchanged, indicator matches actual state
- **Tags:** @integration @state-persistence @app-lifecycle @REQ-FL-TOGGLE-01-SC5

---

**TC-INTEGRATION-004: Button Press Handled Gracefully When LED Unavailable**

```gherkin
Scenario: User presses button on device without LED
  Given the device does not have an LED or LED is unavailable
  When the user presses the toggle button
  Then the app detects the unavailability within 500ms
  And displays a clear error message: "LED is not available on this device"
  And the button remains visible but non-functional
```

- **Test ID:** TC-INTEGRATION-004
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC6
- **Owned by:** QA Team (automated via LED mock, manual on simulator)
- **Preconditions:** App running, LED hardware unavailable or mocked as unavailable
- **Expected Outcomes:** Error message displayed, button visible but disabled
- **Tags:** @integration @error-handling @hardware-unavailable @REQ-FL-TOGGLE-01-SC6

---

### 3. End-to-End Tests (QA Team - Owned)

**TC-E2E-001: User Toggles LED On and Off in Sequence**

```gherkin
Scenario: User performs complete on/off toggle sequence
  Given a user opening the Flashlight app for the first time
  When they press the toggle button
  Then the LED turns on
  And the indicator shows "On"
  And when they press the button again
  Then the LED turns off
  And the indicator shows "Off"
  And when they press the button a third time
  Then the LED turns on again
```

- **Test ID:** TC-E2E-001
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC1, REQ-FL-TOGGLE-01-SC2
- **Owned by:** QA Team (manual on real device + automated)
- **Execution:** Manual on iPhone device
- **Expected Outcomes:** LED toggles correctly on/off/on, indicator synced
- **Tags:** @e2e @user-journey @toggle-sequence @REQ-FL-TOGGLE-01

---

**TC-E2E-002: User Suspends App Mid-Toggle and Resumes**

```gherkin
Scenario: User toggles LED, suspends app, resumes, and verifies state
  Given the app is open with LED off
  When the user presses the button to turn LED on
  Then the LED is on
  And when the user immediately backgrounds the app
  And quickly resumes the app (within 2 seconds)
  Then the LED is still on
  And the indicator displays "On"
  And the state is consistent
```

- **Test ID:** TC-E2E-002
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC5
- **Owned by:** QA Team (manual on real device)
- **Execution:** Manual on iPhone device
- **Expected Outcomes:** LED state persists, no desynchronization
- **Tags:** @e2e @state-persistence @app-lifecycle @REQ-FL-TOGGLE-01-SC5

---

### 4. Edge Case & Error Handling Tests (QA Team - Owned)

**TC-EDGE-001: LED Unavailable Error Displays Clear Message**

```gherkin
Scenario: User presses button on device without LED capability
  Given the device lacks an LED or LED driver is unavailable
  When the user presses the toggle button
  Then the app detects unavailability
  And displays the error: "LED is not available on this device"
  And the button remains visible but visually disabled (grayed out / non-interactive)
```

- **Test ID:** TC-EDGE-001
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC6
- **Owned by:** QA Team (manual)
- **Edge Case:** Hardware missing or driver unavailable
- **Expected Outcomes:** User sees clear error, button visible but disabled
- **Tags:** @edge-case @hardware-unavailable @error-handling @REQ-FL-TOGGLE-01-SC6

---

**TC-EDGE-002: Rapid Repeated Toggling Does Not Corrupt State**

```gherkin
Scenario: User presses button rapidly (5 times in < 1 second)
  Given the app is open with LED off
  When the user presses the button 5 times rapidly in succession
  Then each press inverts the LED state
  And the final state is on (off→on→off→on→off→on)
  And no state becomes undefined or locked
  And the visual indicator matches the LED state
```

- **Test ID:** TC-EDGE-002
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC4
- **Owned by:** QA Team (automated + manual stress test)
- **Edge Case:** Rapid input handling
- **Expected Outcomes:** All toggles processed, final state correct, no lock-up
- **Tags:** @edge-case @concurrency @rapid-input @REQ-FL-TOGGLE-01-SC4

---

**TC-EDGE-003: Button Remains Visible When LED Unavailable**

```gherkin
Scenario: User views button UI on device without LED
  Given the device does not have an LED
  When the app loads
  Then the toggle button is visible on screen
  And the button text is readable
  And the button is visually disabled (grayed out, reduced opacity, or similar)
  And tapping the button displays the error message
```

- **Test ID:** TC-EDGE-003
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC6, REQ-FL-TOGGLE-01-SC7
- **Owned by:** QA Team (manual on simulator)
- **Edge Case:** Hardware missing
- **Expected Outcomes:** Button visible but disabled, clear visual feedback
- **Tags:** @edge-case @ui-feedback @REQ-FL-TOGGLE-01-SC6

---

**TC-EDGE-004: No Settings, Menus, or Additional UI Elements Exist**

```gherkin
Scenario: User explores app interface for hidden options
  Given the app is open
  When the user looks at the entire screen
  And taps in corners, swipes for menus, or long-presses
  Then only the LED toggle button and state indicator are visible
  And no settings icon, menu, gear icon, or options button exists
  And no hidden UI panels or additional screens are accessible
```

- **Test ID:** TC-EDGE-004
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC7
- **Owned by:** QA Team (manual exploration)
- **Edge Case:** Scope creep verification
- **Expected Outcomes:** Minimal UI, no extraneous elements
- **Tags:** @edge-case @scope-verification @REQ-FL-TOGGLE-01-SC7

---

### 5. Performance & Timing Tests (DevOps/QA - Owned)

**TC-PERF-001: LED Toggle Response Time < 100 Milliseconds**

```gherkin
Scenario: LED responds to button press within 100ms
  Given the user presses the toggle button
  When the system processes the button press
  Then the LED state changes within 100 milliseconds
  And the visual indicator updates within 100 milliseconds
  And no perceptible lag is observed
```

- **Test ID:** TC-PERF-001
- **Requirement Traceability:** REQ-FL-TOGGLE-01-SC3
- **Owned by:** DevOps/QA (automated performance test)
- **Performance Constraint:** ≤100ms
- **Measurement:** Use XCTest performance testing API to measure button press → LED state change latency
- **Acceptance:** 95th percentile response time < 100ms (allow 5% of measurements to be slightly over)
- **Tags:** @performance @timing @REQ-FL-TOGGLE-01-SC3

Measurement Implementation:
```swift
measure {
  // Simulate button press
  viewController.toggleButtonTapped()
  // Measure LED state change timing
  let startTime = CACurrentMediaTime()
  while ledState != expectedState {
    // Poll or wait for state change
  }
  let elapsed = CACurrentMediaTime() - startTime
  XCTAssert(elapsed < 0.1, "LED toggle response exceeded 100ms: \(elapsed * 1000)ms")
}
```

---

## Test Execution Summary

| Test Category | Count | Automation | Frequency | Est. Duration | Owned By |
|---|---|---|---|---|---|
| Unit Tests | 3 | ✓ Fully Automated | Per commit | ~2 min | Dev Team |
| Integration Tests | 4 | ✓ Fully Automated | Post-merge | ~5 min | QA Team |
| E2E Tests | 2 | ✓ Automated + Manual | Nightly / Pre-release | ~10 min (automated), ~15 min (manual) | QA Team |
| Edge Case Tests | 4 | Partial (2 auto, 2 manual) | Before release | ~20 min (manual) | QA Team |
| Performance Tests | 1 | ✓ Automated | Before release | ~3 min | DevOps/QA |
| **Total** | **14** | **11 Automated, 3 Manual** | **Various** | **~60 min (all)** | **Dev/QA/DevOps** |

---

## Test Coverage Matrix

### By Requirement
- REQ-FL-TOGGLE-01: ✓ 9 test cases (Unit, Integration, E2E, Edge, Perf)
- REQ-FL-TOGGLE-01-SC1: ✓ 2 test cases (Integration, E2E)
- REQ-FL-TOGGLE-01-SC2: ✓ 2 test cases (Integration, E2E)
- REQ-FL-TOGGLE-01-SC3: ✓ 2 test cases (Unit, Performance)
- REQ-FL-TOGGLE-01-SC4: ✓ 2 test cases (Unit, Edge Case)
- REQ-FL-TOGGLE-01-SC5: ✓ 3 test cases (Unit, Integration, E2E)
- REQ-FL-TOGGLE-01-SC6: ✓ 3 test cases (Integration, Edge Case x2)
- REQ-FL-TOGGLE-01-SC7: ✓ 1 test case (Edge Case)

### By Test Type
- **Unit:** 3 tests — LED logic, state persistence, UI binding
- **Integration:** 4 tests — Button → LED → UI workflows, state handling
- **E2E:** 2 tests — Full user journeys, toggle sequences
- **Edge Cases:** 4 tests — Hardware unavailable, rapid input, UI scope
- **Performance:** 1 test — Response time constraint

---

## Risk Assessment & Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| LED unavailable on simulator | Medium | Use mocked LED hardware in unit/integration tests; test on real device for E2E |
| State desynchronization between LED and UI | High | Unit test (TC-UNIT-003), Integration test (TC-INTEGRATION-003), E2E test (TC-E2E-002) |
| Rapid input causes state corruption | Medium | Edge case test (TC-EDGE-002) with rapid toggle stress test |
| Hardware abstraction layer changes | Medium | Mock LED HAL in tests; maintain hardware interface contract |
| Performance regression | Low | Automated performance test (TC-PERF-001) in CI/CD; fail build if > 100ms |

---

## Test Data & Fixtures

- **LED State Fixtures:** on (true), off (false)
- **Button Press Events:** Single tap, rapid taps (5 in < 1 sec)
- **Hardware Mock:** Mock LED driver returning unavailable status
- **Storage Mock:** UserDefaults mock for state persistence testing

---

## Success Criteria

✓ All 14 test cases pass
✓ ≥85% code coverage on LED toggle logic
✓ 100% acceptance criteria covered
✓ All tests automated except 3 manual E2E/edge case validations
✓ Performance tests confirm < 100ms response time
✓ No scope creep (UI validation passes)
✓ All tests integrated into CI/CD pipeline and blocking merge gate

---

**Test Plan Status:** Ready for implementation and execution.
**Next Steps:** Dev team implements unit tests; QA team implements integration/E2E/edge case tests; DevOps configures CI/CD pipeline.
