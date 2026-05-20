# iPhone Flashlight — User Stories & Acceptance Criteria

**Project Code:** FL (Flashlight)

---

## 🆔 LED Toggle Control

- **PRD Reference:** Section 4 — LED Toggle Button Feature; Section 3 — iPhone User Task: Turn the LED on and off on iPhone
- **Story ID:** `US-FL-TOGGLE-01`

**User Story:**
- **As a** iPhone User
- **I want to** toggle the LED on and off with a single button press
- **So that** I can quickly and easily control the flashlight without any additional steps or complexity

#### Acceptance Criteria:

- **`AC-FL-TOGGLE-01-01` LED Turns On with Single Press**
  - **Given** the app is open and the LED is currently off
  - **When** the user presses the toggle button once
  - **Then** the iPhone LED illuminates immediately
  - **And** the app displays a visual indicator confirming the LED is on

- **`AC-FL-TOGGLE-01-02` LED Turns Off with Single Press**
  - **Given** the app is open and the LED is currently on
  - **When** the user presses the toggle button once
  - **Then** the iPhone LED turns off immediately
  - **And** the app displays a visual indicator confirming the LED is off

- **`AC-FL-TOGGLE-01-03` Toggle Response Time**
  - **Given** the user presses the toggle button
  - **When** the system processes the button press
  - **Then** the LED state changes within 100 milliseconds
  - **And** the visual indicator updates synchronously with the LED state change

- **`AC-FL-TOGGLE-01-04` Repeated Toggle Cycles Correctly**
  - **Given** the LED is in any state (on or off)
  - **When** the user presses the toggle button multiple times in succession
  - **Then** each press inverts the LED state deterministically
  - **And** no state becomes undefined or locked after consecutive presses

- **`AC-FL-TOGGLE-01-05` LED State Persists Across App Suspend/Resume**
  - **Given** the LED is in a specific state (on or off)
  - **When** the app is backgrounded and then resumed
  - **Then** the LED state persists unchanged
  - **And** the visual indicator matches the actual LED state

- **`AC-FL-TOGGLE-01-06` Graceful Degradation on Hardware Unavailability**
  - **Given** the device does not have an LED or LED is unavailable
  - **When** the user attempts to press the toggle button
  - **Then** the app displays a clear error message indicating the LED is unavailable
  - **And** the button remains visible but non-functional

- **`AC-FL-TOGGLE-01-07` No Additional UI or Settings Exist**
  - **Given** the app is open
  - **When** the user interacts with the interface
  - **Then** only the LED toggle button and its state indicator are displayed
  - **And** no settings, menus, brightness controls, or additional options are available

---

**User Stories Complete.** Ready for test planning.
