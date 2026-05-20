# Flashlight — Product Requirements Document

## 1. Product Overview

**Product Name:** Flashlight

**Mission:** Provide instant, effortless access to your iPhone's LED light with a single tap.

**Description:** A minimalist utility app that enables iPhone users to turn the device's LED flash on and off instantly. No complexity, no settings, no distractions—just a single button for light when you need it.

---

## 2. Goals & Non-Goals

### Goals
- Enable users to turn the LED on and off with a single tap
- Provide an interface so simple that no explanation is needed
- Deliver instant light without delay or friction

### Non-Goals
- Brightness adjustments or dimming modes
- Color filters, strobing, or SOS signals
- Settings, preferences, or configuration
- History, favorites, or saved states
- Sound effects or haptic feedback
- Third-party integrations or sharing features

---

## 3. User Roles & Needs

### iPhone User

#### Task: Turn the LED on and off on my iPhone

**Gains:**
- Very easy to use

**Pains:**
- Any additional complexity would be a pain. Only on and off with one button

---

## 4. Features & How They Solve Needs

### Feature: Single-Tap LED Toggle

**Goals**
- Enable instant light access with minimal friction
- Ensure the app is immediately usable without learning curve
- Eliminate any barrier between user intent and light

**Overview**
A single, full-screen button that toggles the iPhone's LED flash on and off. When the LED is off, the button prompts the user to tap to turn it on; when it's on, the button indicates the current state and allows a tap to turn it off. The entire screen serves as the interactive surface—no menus, no options, no secondary controls.

**Solves For**
- iPhone User → Task: Turn the LED on and off on my iPhone
- Gain: Very easy to use
- Pain: Any additional complexity would be a pain. Only on and off with one button

**Functional Requirements**
- Tapping the button toggles the LED state (on → off, off → on)
- The button clearly indicates whether the LED is currently on or off
- The app launches directly to the toggle screen with no splash screen, onboarding, or modal dialogs
- Tapping anywhere on the screen toggles the LED (the entire screen is interactive, or a clearly visible button fills the screen)
- The app remains responsive even if the device is locked

**Non-Functional Requirements**
- Response time: LED state change occurs within 100ms of tap
- Battery: Light drain is equivalent to the native flashlight
- Compatibility: Works on all iPhones with LED flash capability
- Performance: App launches in under 500ms
- Reliability: 99.9% uptime (LED toggle works when attempted)

**Constraints**
- *Technical:* Requires access to AVFoundation or equivalent framework to control LED; must request camera/flashlight permissions from the system
- *Business:* No revenue model required; utility app with minimal ongoing maintenance needs

**Success Metrics**
- Users can toggle the LED without viewing instructions
- App is launched and LED is controlled in under 1 second from cold start
- Zero support tickets related to feature clarity

**Edge Cases & Considerations**
- Device does not have an LED flash: Display a graceful error message indicating the feature is unavailable
- Permissions denied: Guide user to Settings to enable camera/flashlight access
- LED already in use: Respect system constraints; app requests but does not force control
- Low battery mode: Function normally; do not alter LED behavior based on device power state
- Device locked: Ensure LED can still be toggled without unlocking (if system allows)

---

## 5. Non-Functional Requirements

- **Accessibility:** Button and text must meet WCAG AA contrast standards; support VoiceOver
- **Localization:** UI text minimal; single button and status indicator require no translation
- **Security:** No personal data collection; no external API calls; offline-only operation
- **Offline:** Fully functional with no internet connection required

---

## 6. Success Metrics

- Time to LED toggle from cold start: < 1 second
- User completion of task (toggle LED) without assistance: 100%
- App crash rate: < 0.1%

---

## 7. Open Questions

- Should the app work from the lock screen or Control Center, or only when launched?
- Should the LED turn off if the app is backgrounded, or remain on?
- What branding or visual identity should the app have?
