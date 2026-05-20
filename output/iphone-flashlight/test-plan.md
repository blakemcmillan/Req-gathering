# Flashlight — Test Plan

---

## Test Plan Overview

This test plan covers the Flashlight iOS app, a minimalist utility for turning the iPhone's LED flash on and off with a single tap. Testing focuses on core functionality (LED toggle, state display), permissions handling, performance (launch time, response latency, battery efficiency), and edge cases. The test strategy balances automated unit/integration tests for regression coverage with manual E2E and edge case testing to verify real-world user experience.

**Scope:** All features in the Single-Tap LED Toggle functionality (LED on/off, state display, app launch, permissions, battery efficiency).

**Testing Approach:**
- **Unit Tests:** Logic validation (state management, permissions checking)
- **Integration Tests:** Feature workflows (LED toggle → state display, permission flows)
- **E2E Tests:** Full user journeys (launch → toggle → state verification)
- **Edge Case Tests:** Boundary conditions (backgrounding, device without LED, permission denial)
- **Performance Tests:** Launch time, toggle latency, battery/CPU usage

---

## Test Strategy

### Ownership & Responsibilities

**Dev Team:**
- Unit tests: State logic, permission status, initialization
- Component-level testing: LED toggle mechanics
- Automated execution on every commit

**QA Team:**
- Integration tests: Feature workflows (LED on/off, permissions, state display)
- E2E tests: Real user scenarios (launch → use → exit)
- Edge case tests: Boundary conditions, error handling
- Manual execution on PR merge, before release
- Performance baseline testing

**DevOps Team:**
- CI/CD pipeline setup for automated test execution
- Performance monitoring infrastructure (app launch timing, LED response time)
- Test device provisioning (devices with/without LED)
- Performance test environment and tools

### Environment Setup

**Local Development:**
- Xcode with iOS simulator (iOS 14+)
- Unit test framework: XCTest
- Mock/stub library: OCMock or custom protocols
- Git hooks: Run unit tests pre-commit

**Staging/Integration Testing:**
- Physical test devices (iPhone 12, 14, 15 with LED)
- Device without LED: iPad simulator or older iPhone model
- Network conditions: Normal, offline (for background behavior)

**CI/CD Pipeline:**
- Unit tests: Run on every commit (pre-merge gate)
- Integration tests: Run on PR merge to main
- E2E tests: Run nightly or on-demand before release
- Performance tests: Run weekly and before releases
- **Failed tests block merge to main**

**Tools & Dependencies:**
- XCTest (native iOS testing framework)
- XCUITest (E2E testing)
- Instruments (performance profiling)
- CocoaPods or SPM (dependency management)
- GitHub Actions or Xcode Cloud (CI/CD)

### Coverage Goals

- **Unit Tests:** ≥85% code coverage (LED state logic, permission checks)
- **Integration Tests:** ≥70% of critical workflows
- **E2E Tests:** 100% of acceptance criteria scenarios
- **Edge Case Tests:** ≥90% of documented edge cases
- **Overall Combined Coverage:** ≥80%

---

## Test Objectives

1. Verify LED toggles on and off within 100ms response time
2. Confirm app launches to interactive state in under 500ms (cold start)
3. Validate state display (on/off) is clear and accessible
4. Test permission handling: request, denial recovery, usage without permissions
5. Verify LED turns off when app is backgrounded or closed
6. Confirm battery efficiency: LED drain matches native flashlight, idle CPU < 1%
7. Test edge cases: device without LED, rapid taps, late permission grants
8. Ensure no crashes or undefined behavior in any scenario

---

## Test Scope

### In Scope

- LED toggle on/off functionality
- Visual state indicators (on/off display)
- App launch and initialization (no splash, no onboarding)
- Permission requests and flows
- LED off when app is backgrounded/closed
- Battery and CPU efficiency
- Accessibility (WCAG AA contrast, VoiceOver support)
- Error handling (device without LED, permissions denied)

### Out of Scope

- Network-dependent features (not applicable to this app)
- Push notifications or background activity (app has none)
- Multi-language localization (UI is minimal, single button)
- Analytics or telemetry
- Third-party integrations
- Siri shortcuts or Control Center integration (deferred per open questions)

---

## Requirement Traceability

```
| Requirement ID | Description | Test Case IDs | Coverage |
|---|---|---|---|
| REQ-FL-TOGGLE-01 | Toggle LED On | TC-UNIT-001, TC-INT-001, TC-E2E-001, TC-PERF-002 | ✓ Complete |
| REQ-FL-TOGGLE-01-SC1 | LED activates on first tap | TC-INT-001, TC-E2E-001 | ✓ Covered |
| REQ-FL-TOGGLE-01-SC2 | LED remains on in foreground | TC-UNIT-001, TC-INT-002 | ✓ Covered |
| REQ-FL-TOGGLE-01-SC3 | Permissions requested | TC-INT-003, TC-E2E-003 | ✓ Covered |
| REQ-FL-TOGGLE-01-SC4 | Graceful error without LED | TC-EDGE-002 | ✓ Covered |
| REQ-FL-TOGGLE-02 | Toggle LED Off | TC-UNIT-001, TC-INT-004, TC-E2E-001 | ✓ Complete |
| REQ-FL-TOGGLE-02-SC1 | LED deactivates on tap | TC-INT-004, TC-E2E-001 | ✓ Covered |
| REQ-FL-TOGGLE-02-SC2 | LED off when backgrounded | TC-INT-002, TC-EDGE-001 | ✓ Covered |
| REQ-FL-TOGGLE-02-SC3 | LED off when app closed | TC-EDGE-001 | ✓ Covered |
| REQ-FL-TOGGLE-03 | Display LED State Clearly | TC-UNIT-002, TC-INT-005, TC-E2E-001 | ✓ Complete |
| REQ-FL-TOGGLE-03-SC1 | Visual indicator off | TC-INT-005, TC-E2E-001 | ✓ Covered |
| REQ-FL-TOGGLE-03-SC2 | Visual indicator on | TC-INT-005, TC-E2E-001 | ✓ Covered |
| REQ-FL-TOGGLE-03-SC3 | Accessibility contrast | TC-UNIT-002 | ✓ Covered |
| REQ-FL-TOGGLE-04 | Launch App Instantly | TC-UNIT-003, TC-E2E-002, TC-PERF-001 | ✓ Complete |
| REQ-FL-TOGGLE-04-SC1 | Launch in <500ms | TC-PERF-001 | ✓ Covered |
| REQ-FL-TOGGLE-04-SC2 | No prompts on first launch | TC-E2E-002 | ✓ Covered |
| REQ-FL-TOGGLE-04-SC3 | Full screen interactive | TC-INT-006 | ✓ Covered |
| REQ-FL-TOGGLE-05 | Battery Efficiency | TC-PERF-003, TC-PERF-004 | ✓ Complete |
| REQ-FL-TOGGLE-05-SC1 | LED drain ≤ native | TC-PERF-003 | ✓ Covered |
| REQ-FL-TOGGLE-05-SC2 | Idle CPU < 1% | TC-PERF-004 | ✓ Covered |
| REQ-FL-TOGGLE-06 | Handle Permissions Gracefully | TC-INT-003, TC-EDGE-003, TC-E2E-003 | ✓ Complete |
| REQ-FL-TOGGLE-06-SC1 | Permission explanation | TC-INT-003 | ✓ Covered |
| REQ-FL-TOGGLE-06-SC2 | Guide to Settings | TC-EDGE-003 | ✓ Covered |
| REQ-FL-TOGGLE-06-SC3 | Works after permission grant | TC-EDGE-003 | ✓ Covered |

**Coverage Summary:** 23 of 23 requirements covered (100%)
**Test Count by Category:** Unit: 3, Integration: 6, E2E: 3, Edge Case: 4, Performance: 4 | **Total: 20 test cases**
```

---

## Test Cases

### 1. Unit Tests (Dev Team — Owned)

**Automated, pre-commit execution. ≥85% code coverage.**

---

#### TC-UNIT-001: LED Toggle State Management

**Test Strategy:** Validate LED state transitions (on ↔ off) and persistence.

- **Test Inputs:** 
  - Toggle from off → on
  - Toggle from on → off
  - Multiple consecutive toggles
  - State persistence across method calls

- **Expected Outcomes:**
  - State transitions correctly: off → on, on → off
  - `ledIsOn` boolean reflects actual LED state
  - No state corruption after multiple toggles
  - State remains consistent with system LED state

- **Coverage:** LED state machine logic, toggle() method, property getters
- **Owned by:** Dev Team (automated unit test)

**Requirement Traceability:** REQ-FL-TOGGLE-01, REQ-FL-TOGGLE-02
**Tags:** @unit @state-machine @core-logic

---

#### TC-UNIT-002: LED State Indicator Display

**Test Strategy:** Verify state indicator computation (on = green/bright, off = dim/gray).

- **Test Inputs:**
  - ledIsOn = true
  - ledIsOn = false
  - Accessibility color contrast calculation

- **Expected Outcomes:**
  - When ledIsOn = true: indicator shows "on" state (distinct color/text)
  - When ledIsOn = false: indicator shows "off" state (distinct color/text)
  - Contrast ratio ≥ 4.5:1 (WCAG AA)
  - Color is not the only differentiator (icon or text also present)

- **Coverage:** getStateIndicator() method, accessibility compliance, UI state binding
- **Owned by:** Dev Team (automated unit test)

**Requirement Traceability:** REQ-FL-TOGGLE-03-SC3
**Tags:** @unit @ui-state @accessibility

---

#### TC-UNIT-003: Permission Status Checking

**Test Strategy:** Validate permission status determination and caching.

- **Test Inputs:**
  - AVCaptureDevice.authorizationStatus() returns .authorized
  - AVCaptureDevice.authorizationStatus() returns .denied
  - AVCaptureDevice.authorizationStatus() returns .notDetermined

- **Expected Outcomes:**
  - hasFlashlightPermission() returns true when .authorized
  - hasFlashlightPermission() returns false when .denied or .notDetermined
  - Permission status is checked at app startup
  - Status is updated when requestPermission() is called

- **Coverage:** Permission request/check logic, AVCaptureDevice integration
- **Owned by:** Dev Team (automated unit test)

**Requirement Traceability:** REQ-FL-TOGGLE-01-SC3, REQ-FL-TOGGLE-06
**Tags:** @unit @permissions @authorization

---

#### TC-UNIT-004: App Launch Initialization

**Test Strategy:** Verify app state is initialized correctly on launch.

- **Test Inputs:**
  - Cold app launch (no cached state)
  - Warm launch (state cached from previous session)

- **Expected Outcomes:**
  - LED state defaults to off
  - State indicator is displayed
  - Permission check runs immediately
  - No modals or dialogs block the UI
  - All views are initialized in <100ms

- **Coverage:** AppDelegate/SceneDelegate initialization, state setup, view hierarchy
- **Owned by:** Dev Team (automated unit test)

**Requirement Traceability:** REQ-FL-TOGGLE-04-SC2
**Tags:** @unit @initialization @startup

---

### 2. Integration Tests (QA Team — Owned)

**Post-PR-merge execution. ≥70% critical workflow coverage.**

---

#### TC-INT-001: LED Toggles On When Tapped from Off State

```gherkin
Scenario: User taps to turn LED on from off state
  Given the app is open and the LED is currently off
  And the user has granted flashlight permissions
  When the user taps the screen
  Then the LED illuminates within 100ms
  And the state indicator updates to show "on"
  And the LED remains on until the user taps again

Test ID: TC-INT-001
Requirement Traceability: REQ-FL-TOGGLE-01-SC1
Owned by: QA Team
Tags: @integration @core-workflow @REQ-FL-TOGGLE-01-SC1
```

---

#### TC-INT-002: LED Remains On While App in Foreground

```gherkin
Scenario: LED stays on without turning off automatically
  Given the LED is currently on and the app is in foreground
  When 30 seconds elapse
  Then the LED remains on
  And the state indicator continues to show "on"
  And no automatic off behavior triggers

Test ID: TC-INT-002
Requirement Traceability: REQ-FL-TOGGLE-01-SC2
Owned by: QA Team
Tags: @integration @state-persistence @REQ-FL-TOGGLE-01-SC2
```

---

#### TC-INT-003: Permission Request Flow

```gherkin
Scenario: System requests camera/flashlight permission on first toggle attempt
  Given the app is open and permissions are not yet granted
  When the user taps to toggle the LED
  Then the system displays the permission request prompt
  And the prompt explains that camera permission is needed for LED control
  When the user taps "Allow"
  Then the permission is granted
  And the LED toggles on

Test ID: TC-INT-003
Requirement Traceability: REQ-FL-TOGGLE-01-SC3, REQ-FL-TOGGLE-06-SC1
Owned by: QA Team
Tags: @integration @permissions @user-flow @REQ-FL-TOGGLE-06-SC1
```

---

#### TC-INT-004: LED Toggles Off When Tapped from On State

```gherkin
Scenario: User taps to turn LED off from on state
  Given the app is open and the LED is currently on
  When the user taps the screen
  Then the LED turns off within 100ms
  And the state indicator updates to show "off"
  And the LED remains off until the user taps again

Test ID: TC-INT-004
Requirement Traceability: REQ-FL-TOGGLE-02-SC1
Owned by: QA Team
Tags: @integration @core-workflow @REQ-FL-TOGGLE-02-SC1
```

---

#### TC-INT-005: State Indicator Displays Current LED Status

```gherkin
Scenario: Visual indicator clearly shows whether LED is on or off
  Given the app is open with the LED off
  When the user views the screen
  Then the state indicator clearly shows "off" state
  And the button text prompts "Tap to turn on" or similar
  When the user taps to turn LED on
  Then the state indicator updates to "on" state
  And the button text shows "Tap to turn off" or similar

Test ID: TC-INT-005
Requirement Traceability: REQ-FL-TOGGLE-03-SC1, REQ-FL-TOGGLE-03-SC2
Owned by: QA Team
Tags: @integration @ui-feedback @REQ-FL-TOGGLE-03
```

---

#### TC-INT-006: Full Screen Tap Area Toggles LED

```gherkin
Scenario: User can tap anywhere on screen to toggle LED
  Given the app is open on the toggle screen
  When the user taps in the center of the screen
  Then the LED toggles
  When the user taps near the top of the screen
  Then the LED toggles
  When the user taps near the bottom of the screen
  Then the LED toggles
  And the entire visible screen area is interactive

Test ID: TC-INT-006
Requirement Traceability: REQ-FL-TOGGLE-04-SC3
Owned by: QA Team
Tags: @integration @tap-target @usability @REQ-FL-TOGGLE-04-SC3
```

---

### 3. End-to-End Tests (QA Team — Owned)

**Nightly or on-demand execution. 100% of acceptance criteria scenarios.**

---

#### TC-E2E-001: User Toggles LED On and Off Multiple Times

```gherkin
Scenario: User opens app and toggles LED on and off multiple times
  Given a user launches the Flashlight app for the first time
  When they tap the screen to turn the LED on
  Then the LED illuminates and the state indicator shows "on"
  When they tap again
  Then the LED turns off and the state indicator shows "off"
  When they tap again
  Then the LED turns on
  And the app remains stable through all toggles
  And no errors or crashes occur

Test ID: TC-E2E-001
Requirement Traceability: REQ-FL-TOGGLE-01, REQ-FL-TOGGLE-02, REQ-FL-TOGGLE-03
Owned by: QA Team (Manual + Automated)
Tags: @e2e @core-user-journey @REQ-FL-TOGGLE-01 @REQ-FL-TOGGLE-02 @REQ-FL-TOGGLE-03
```

---

#### TC-E2E-002: User Launches App and Uses Without Setup

```gherkin
Scenario: User opens app and can toggle LED without encountering prompts
  Given a user launches the Flashlight app (after already granting permissions in a previous session)
  When the app opens
  Then no splash screen, onboarding, or permission dialog appears
  And the toggle screen is displayed
  And the LED can be toggled immediately with a single tap
  And the entire interaction completes in under 1 second

Test ID: TC-E2E-002
Requirement Traceability: REQ-FL-TOGGLE-04-SC1, REQ-FL-TOGGLE-04-SC2
Owned by: QA Team (Manual)
Tags: @e2e @user-experience @fast-launch @REQ-FL-TOGGLE-04
```

---

#### TC-E2E-003: User Grants Permission and Toggles LED

```gherkin
Scenario: First-time user grants camera/flashlight permission and toggles LED
  Given a user launching the Flashlight app for the first time
  When they tap to toggle the LED
  Then the permission request appears
  And they tap "Allow" to grant camera/flashlight permission
  Then the permission is granted
  And the LED immediately toggles on
  And the state indicator updates
  And no errors occur

Test ID: TC-E2E-003
Requirement Traceability: REQ-FL-TOGGLE-01-SC3, REQ-FL-TOGGLE-06
Owned by: QA Team (Manual)
Tags: @e2e @permissions @first-time-user @REQ-FL-TOGGLE-06
```

---

### 4. Edge Case & Error Handling Tests (QA Team — Owned)

**Manual + targeted automated execution. ≥90% of edge cases.**

---

#### TC-EDGE-001: LED Turns Off When App is Backgrounded or Closed

```gherkin
Scenario: LED turns off automatically when app is backgrounded
  Given the LED is currently on in the Flashlight app
  When the user switches to another app (e.g., Safari)
  Then the LED turns off immediately
  And when the user returns to the Flashlight app
  Then the state indicator shows "off"
  And the LED does not re-activate

Scenario: LED turns off when app is force-closed
  Given the LED is currently on
  When the user force-closes the app (swipe up in app switcher)
  Then the LED turns off immediately
  And no background process keeps the LED active

Test ID: TC-EDGE-001
Requirement Traceability: REQ-FL-TOGGLE-02-SC2, REQ-FL-TOGGLE-02-SC3
Owned by: QA Team (Manual)
Tags: @edge-case @lifecycle @background-behavior @REQ-FL-TOGGLE-02
```

---

#### TC-EDGE-002: Device Without LED Flash Shows Error Gracefully

```gherkin
Scenario: iPad (no LED) displays error when user attempts toggle
  Given a user opens the Flashlight app on an iPad (no LED flash)
  When they attempt to tap the screen to toggle the LED
  Then an error message appears: "LED flash not available on this device"
  And the app does not crash
  And no undefined behavior occurs
  And the error message is dismissible

Scenario: User with disabled LED attempts toggle
  Given a user on an iPhone with a malfunctioning LED
  When they attempt to toggle
  Then the app gracefully handles the hardware error
  And displays a clear message
  And remains stable

Test ID: TC-EDGE-002
Requirement Traceability: REQ-FL-TOGGLE-01-SC4
Owned by: QA Team (Manual on real devices)
Tags: @edge-case @error-handling @hardware-limitation @REQ-FL-TOGGLE-01-SC4
```

---

#### TC-EDGE-003: Permission Denied Then Granted in Settings

```gherkin
Scenario: User denies permission, then grants in Settings, and returns to app
  Given a user attempts to toggle with no permissions
  When the permission request appears
  And they tap "Don't Allow"
  And they leave the app
  And they go to Settings → Camera → and enable Flashlight access
  And they return to the Flashlight app
  Then the toggle works immediately without prompts
  And no crash or error state occurs

Test ID: TC-EDGE-003
Requirement Traceability: REQ-FL-TOGGLE-06-SC2, REQ-FL-TOGGLE-06-SC3
Owned by: QA Team (Manual)
Tags: @edge-case @permissions @recovery @REQ-FL-TOGGLE-06
```

---

#### TC-EDGE-004: Rapid Taps Don't Cause Race Conditions

```gherkin
Scenario: User taps rapidly multiple times
  Given the app is open
  When the user taps the screen 5 times in rapid succession (within 1 second)
  Then the LED state toggles correctly with each tap
  And no state corruption occurs
  And the UI remains responsive
  And the final state matches the expected toggle sequence

Test ID: TC-EDGE-004
Requirement Traceability: REQ-FL-TOGGLE-01, REQ-FL-TOGGLE-02
Owned by: QA Team (Automated)
Tags: @edge-case @concurrency @stress-test
```

---

### 5. Performance Tests (DevOps/QA — Owned)

**Weekly or pre-release execution. Automated with performance monitoring.**

---

#### TC-PERF-001: Cold Start App Launch Under 500ms

```gherkin
Scenario: App launches from cold start to interactive in <500ms
  Given the app is not in memory (force-quit)
  When the user taps the app icon from home screen
  Then the toggle screen appears and is interactive
  And the time from tap to interactive screen is <500ms
  And no splash screen delays the launch
  And no initialization dialogs appear

Acceptance: ✓ Launch completes in <500ms

Test ID: TC-PERF-001
Requirement Traceability: REQ-FL-TOGGLE-04-SC1
Owned by: DevOps/QA Team (automated performance monitoring)
Tags: @performance @startup-latency @REQ-FL-TOGGLE-04-SC1
```

---

#### TC-PERF-002: LED Toggle Response Time <100ms

```gherkin
Scenario: LED responds to tap within 100ms
  Given the app is open and the LED is off
  When the user taps the screen at T=0
  Then the LED illuminates by T=100ms
  And the state indicator updates visually within 100ms

Acceptance: ✓ Toggle latency <100ms

Test ID: TC-PERF-002
Requirement Traceability: REQ-FL-TOGGLE-01-SC1, REQ-FL-TOGGLE-02-SC1
Owned by: DevOps/QA Team (automated performance monitoring)
Tags: @performance @response-latency @REQ-FL-TOGGLE-01 @REQ-FL-TOGGLE-02
```

---

#### TC-PERF-003: Battery Drain Matches Native Flashlight

```gherkin
Scenario: LED battery consumption is ≤ native iPhone flashlight
  Given the Flashlight app with LED on
  When the LED is active for 1 hour
  Then battery drain is measured using Instruments (Energy Impact)
  And the Flashlight app drain is ≤ native flashlight drain
  And no background processes drain battery after app closes

Acceptance: ✓ Energy drain equivalent or better than native

Test ID: TC-PERF-003
Requirement Traceability: REQ-FL-TOGGLE-05-SC1
Owned by: DevOps/QA Team (manual with Instruments profiling)
Tags: @performance @battery @energy-efficiency @REQ-FL-TOGGLE-05-SC1
```

---

#### TC-PERF-004: Idle CPU Usage <1%

```gherkin
Scenario: App uses minimal CPU when LED is off
  Given the app is open in foreground with LED off
  When the app is idle for 1 minute
  Then CPU usage is <1% average
  And no background timers or polling loops are active
  And battery drain in idle state is negligible

Acceptance: ✓ CPU idle <1%

Test ID: TC-PERF-004
Requirement Traceability: REQ-FL-TOGGLE-05-SC2
Owned by: DevOps/QA Team (automated with Instruments)
Tags: @performance @cpu-efficiency @idle-state @REQ-FL-TOGGLE-05-SC2
```

---

## Summary

**Total Test Cases:** 20
- **Unit Tests:** 4 (Dev Team)
- **Integration Tests:** 6 (QA Team)
- **E2E Tests:** 3 (QA Team)
- **Edge Case Tests:** 4 (QA Team)
- **Performance Tests:** 4 (DevOps/QA Team)

**Coverage:**
- Requirements Covered: 23/23 (100%)
- Estimated Code Coverage: ≥80%
- Critical Workflows: 100%
- Edge Cases: ≥90%

**Execution Timeline:**
- Unit tests: Every commit (pre-merge gate)
- Integration tests: PR merge to main
- E2E tests: Nightly + on-demand before release
- Performance tests: Weekly or before releases
- Full test suite completion: ~45 minutes (CI automated) + 2-3 hours (manual QA)

---

## Open Questions for Testing

- Should app support Control Center or lock screen shortcuts for faster access? (defer to v2)
- What device models should be included in performance baseline? (iPhone 12, 14, 15 minimum)
- Should battery drain be tested in low-power mode? (yes, add to TC-PERF-003)
- How frequently should performance benchmarks be re-baselined? (quarterly or after iOS updates)
