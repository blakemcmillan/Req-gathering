# Flashlight — User Stories & Acceptance Criteria

---

## 🆔 Toggle LED On and Off

- **PRD Reference:** Feature: Single-Tap LED Toggle (Section 4)
- **Story ID:** `US-FL-TOGGLE-01`

**User Story:**
- **As a** iPhone user
- **I want to** tap the screen to turn the LED on and off
- **So that** I have instant light when I need it and can stop it when I don't

#### Acceptance Criteria:

- **`AC-FL-TOGGLE-01-01` LED toggles on when tapped from off state**
  - **Given** the app is open, the LED is off, and the user has granted flashlight permissions
  - **When** the user taps the screen
  - **Then** the LED illuminates within 100ms
  - **And** the state indicator updates to show "on"

- **`AC-FL-TOGGLE-01-02` LED toggles off when tapped from on state**
  - **Given** the app is open and the LED is currently on
  - **When** the user taps the screen
  - **Then** the LED turns off within 100ms
  - **And** the state indicator updates to show "off"

- **`AC-FL-TOGGLE-01-03` LED turns off when app is backgrounded or closed**
  - **Given** the LED is currently on
  - **When** the user switches to another app or force-closes the Flashlight app
  - **Then** the LED turns off immediately
  - **And** the LED does not re-activate when the app is reopened

- **`AC-FL-TOGGLE-01-04` Visual state indicator is clear and accessible**
  - **Given** the app is open
  - **When** the user views the screen
  - **Then** a clear visual indicator (distinct on/off states) shows the current LED status
  - **And** the indicator meets WCAG AA contrast standards (≥4.5:1)
  - **And** the indicator is distinguishable by color-blind users (not color alone)

- **`AC-FL-TOGGLE-01-05` App launches instantly without friction**
  - **Given** the user taps the app icon from the home screen
  - **When** the app initializes
  - **Then** the toggle screen loads and is interactive within 500ms (cold start)
  - **And** no splash screen, onboarding, or permission prompts appear on first launch
  - **And** the entire screen is interactive for toggling

- **`AC-FL-TOGGLE-01-06` Permissions are requested and handled gracefully**
  - **Given** the user has not yet granted flashlight permissions
  - **When** they attempt to toggle the LED
  - **Then** the system requests camera/flashlight permission with clear context
  - **And** if denied, a message guides the user to Settings to enable permissions
  - **And** the app works immediately after permissions are granted without restarting

- **`AC-FL-TOGGLE-01-07` Device constraints are handled gracefully**
  - **Given** the device lacks LED flash capability (e.g., iPad)
  - **When** the user attempts to toggle the LED
  - **Then** an error message indicates the feature is unavailable
  - **And** no crash or undefined behavior occurs

- **`AC-FL-TOGGLE-01-08` Battery and CPU efficiency meet native flashlight baseline**
  - **Given** the LED is active in the Flashlight app
  - **When** measured over 1 hour of use
  - **Then** power consumption is ≤ native iPhone flashlight
  - **And** with the app open but LED off, idle CPU usage is <1%
  - **And** no background processes drain battery after the app is closed
