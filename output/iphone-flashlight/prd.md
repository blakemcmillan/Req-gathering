# iPhone Flashlight — Product Requirements Document

## 1. Product Overview

**Product Name:** iPhone Flashlight

**Mission:** Provide the simplest possible way to turn the iPhone LED on and off.

**Description:** A single-button flashlight app that toggles the iPhone's LED with one press. No settings, no complexity—just on and off.

---

## 2. Goals & Non-Goals

### Goals
- Enable users to turn the iPhone LED on and off with a single press
- Deliver an experience so simple that any user can operate it without instruction
- Prioritize simplicity and ease of use as the core competitive advantage

### Non-Goals
- Add settings, brightness controls, or customization options
- Support multiple lighting modes or effects
- Integrate with device features beyond the LED
- Provide any UI element or functionality beyond the on/off toggle

---

## 3. User Roles & Needs

### iPhone User

#### Task: Turn the LED on and off on iPhone

**Success Criteria:**
- The LED turns on and off with a single press

**Gains:**
- Very easy to use

**Pains:**
- Any additional complexity would be a pain
- Users want only on and off with one button

---

## 4. Features & How They Solve Needs

### Feature: LED Toggle Button

**Goals**
- Enable users to control the LED with a single interaction
- Deliver an interface so simple that complexity is eliminated as a source of friction

**Overview**
A single button that toggles the iPhone LED on and off. One press turns it on; another press turns it off. No additional UI, settings, or options.

**Solves For**
- **User Role:** iPhone User
- **Task:** Turn the LED on and off on iPhone
- **Gains Addressed:** Very easy to use
- **Pains Addressed:** Eliminates any complexity beyond a single on/off button

**Functional Requirements**
- Pressing the button toggles the LED between on and off states
- The app displays the current state of the LED (on or off)
- The app respects the device's LED hardware capabilities

**Non-Functional Requirements**
- Toggle response time: immediate (< 100 ms)
- Reliability: the LED must respond every time the button is pressed
- The app must work on all iPhone models with an LED

**Success Metrics**
- Users can turn the LED on and off with a single press 100% of the time
- No user training or documentation required for basic operation

---

## 5. Non-Functional Requirements (Product-Wide)

- **Simplicity:** The app's entire interface and behavior must remain simple; no hidden menus, settings, or advanced options
- **Reliability:** The LED control must never fail or lag
- **Accessibility:** The button and feedback must be clear and usable by all users

---

## 6. Success Metrics (Product-Wide)

- **Task Completion:** Users can toggle the LED with a single press
- **Usability:** No user documentation or support requests due to complexity

---

## 7. Open Questions

None identified from the requirements.

---

**PRD Status:** Ready for user story expansion and test planning.
