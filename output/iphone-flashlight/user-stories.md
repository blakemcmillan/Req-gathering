# Flashlight — User Stories & Acceptance Criteria

---

## 🆔 Toggle LED On

- **PRD Reference:** Feature: Single-Tap LED Toggle
- **Story ID:** `US-FL-TOGGLE-01`

**User Story:**
- **As a** iPhone user
- **I want to** tap the screen to turn the LED on
- **So that** I have instant light when I need it

#### Acceptance Criteria:

- **`AC-FL-TOGGLE-01-01` LED activates on first tap from off state**
  - **Given** the app is open and the LED is currently off
  - **When** the user taps the screen
  - **Then** the LED illuminates within 100ms
  - **And** the LED remains on until toggled off

- **`AC-FL-TOGGLE-01-02` LED remains on during continuous use**
  - **Given** the LED is on and the user is using the light
  - **When** the app remains in the foreground
  - **Then** the LED does not turn off automatically
  - **And** the LED only turns off when the user taps to toggle it off

- **`AC-FL-TOGGLE-01-03` Permissions are requested if not granted**
  - **Given** the app does not have camera/flashlight permissions
  - **When** the user attempts to toggle the LED
  - **Then** the system prompts for camera/flashlight permission
  - **And** the LED toggles only after permission is granted

- **`AC-FL-TOGGLE-01-04` Device without LED flash shows error gracefully**
  - **Given** the device does not have an LED flash capability
  - **When** the user attempts to toggle the LED
  - **Then** an error message is displayed indicating the feature is unavailable
  - **And** no crash or undefined behavior occurs

---

## 🆔 Toggle LED Off

- **PRD Reference:** Feature: Single-Tap LED Toggle
- **Story ID:** `US-FL-TOGGLE-02`

**User Story:**
- **As a** iPhone user
- **I want to** tap the screen to turn the LED off
- **So that** I can stop the light when I no longer need it

#### Acceptance Criteria:

- **`AC-FL-TOGGLE-02-01` LED deactivates on tap from on state**
  - **Given** the app is open and the LED is currently on
  - **When** the user taps the screen
  - **Then** the LED turns off within 100ms
  - **And** the LED remains off until toggled on again

- **`AC-FL-TOGGLE-02-02` LED turns off when app is backgrounded**
  - **Given** the LED is currently on
  - **When** the user switches to another app or locks the device
  - **Then** the LED turns off automatically
  - **And** the app does not re-activate the LED when returned to foreground

- **`AC-FL-TOGGLE-02-03` LED turns off when app is closed**
  - **Given** the LED is currently on
  - **When** the user force-closes or swipes the app away
  - **Then** the LED turns off immediately
  - **And** no background process keeps the LED active

---

## 🆔 Display LED State Clearly

- **PRD Reference:** Feature: Single-Tap LED Toggle
- **Story ID:** `US-FL-TOGGLE-03`

**User Story:**
- **As a** iPhone user
- **I want to** see whether the LED is currently on or off
- **So that** I know the current state without ambiguity

#### Acceptance Criteria:

- **`AC-FL-TOGGLE-03-01` Visual indicator shows LED is off**
  - **Given** the app is open and the LED is off
  - **When** the user looks at the screen
  - **Then** a clear visual indicator (color, text, or icon) shows the LED is off
  - **And** the button text or label prompts the user to tap to turn it on

- **`AC-FL-TOGGLE-03-02` Visual indicator shows LED is on**
  - **Given** the app is open and the LED is on
  - **When** the user looks at the screen
  - **Then** a clear visual indicator (distinct from off state) shows the LED is on
  - **And** the button text or label indicates the current active state

- **`AC-FL-TOGGLE-03-03` Contrast meets accessibility standards**
  - **Given** the app is displayed in any lighting condition
  - **When** the user views the state indicator
  - **Then** the indicator meets WCAG AA contrast standards (minimum 4.5:1 for text)
  - **And** the indicator is distinguishable by color-blind users (does not rely on color alone)

---

## 🆔 Launch App Instantly

- **PRD Reference:** Feature: Single-Tap LED Toggle
- **Story ID:** `US-FL-TOGGLE-04`

**User Story:**
- **As a** iPhone user
- **I want to** launch the app and access the toggle instantly
- **So that** I can turn on the LED without delay or extra steps

#### Acceptance Criteria:

- **`AC-FL-TOGGLE-04-01` App launches to toggle screen in under 500ms**
  - **Given** the user taps the app icon from the home screen or app library
  - **When** the app initializes
  - **Then** the toggle screen loads and is interactive within 500ms from cold start
  - **And** no splash screen, onboarding, or modal dialog appears

- **`AC-FL-TOGGLE-04-02` No permission or setup prompts on first launch**
  - **Given** the user launches the app for the first time
  - **When** the app initializes
  - **Then** the toggle screen appears immediately without modals or dialogs
  - **And** permission requests are deferred until the user attempts to toggle the LED

- **`AC-FL-TOGGLE-04-03` Full screen is interactive for toggle**
  - **Given** the app is open on the toggle screen
  - **When** the user taps anywhere on the screen
  - **Then** the LED toggles
  - **And** the tap target area is the entire visible screen or a clearly visible full-screen button

---

## 🆔 Maintain Battery Efficiency

- **PRD Reference:** Feature: Single-Tap LED Toggle
- **Story ID:** `US-FL-TOGGLE-05`

**User Story:**
- **As a** iPhone user
- **I want to** use the flashlight without excessive battery drain
- **So that** the light is practical for regular use

#### Acceptance Criteria:

- **`AC-FL-TOGGLE-05-01` LED power consumption matches native flashlight**
  - **Given** the LED is on in the Flashlight app
  - **When** measured over a standard duration (e.g., 1 hour)
  - **Then** power consumption is equivalent to or less than the native iPhone flashlight
  - **And** no background processes drain battery when the app is closed

- **`AC-FL-TOGGLE-05-02` App uses minimal CPU while idle**
  - **Given** the app is open but the LED is off
  - **When** the app is in the foreground idle state
  - **Then** CPU usage is negligible (< 1% average)
  - **And** no timers, background threads, or polling loops are active

---

## 🆔 Handle Permissions Gracefully

- **PRD Reference:** Feature: Single-Tap LED Toggle
- **Story ID:** `US-FL-TOGGLE-06`

**User Story:**
- **As a** iPhone user
- **I want to** understand what permissions are needed and why
- **So that** I can make an informed decision about granting access

#### Acceptance Criteria:

- **`AC-FL-TOGGLE-06-01` Permission request explains why camera access is needed**
  - **Given** the user taps the toggle and permissions are not granted
  - **When** the system displays the permission prompt
  - **Then** the app provides context explaining that camera permission is needed for LED control
  - **And** the user can choose to allow or deny without confusion

- **`AC-FL-TOGGLE-06-02` Guide user to settings if permissions are denied**
  - **Given** the user denies camera/flashlight permissions
  - **When** the user returns to the app and attempts to toggle
  - **Then** a message appears directing the user to Settings to enable permissions
  - **And** a direct link or clear instructions are provided (if iOS allows)

- **`AC-FL-TOGGLE-06-03` App remains usable after permission denial**
  - **Given** the user denies permissions
  - **When** the user later grants permissions in Settings
  - **Then** the toggle works immediately without restarting the app
  - **And** no crash or error state occurs
