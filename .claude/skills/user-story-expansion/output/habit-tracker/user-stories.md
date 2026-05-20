# User Stories: Habit Tracker

---

## 🆔 Set Initial Weekly Goal at Onboarding
- **PRD Reference:** Feature: Weekly Goal Setting
- **Story ID:** `US-HT-GOAL-01`

**User Story:**
- **As a** Workout Newbie
- **I want to** set my first weekly workout goal when I open the app
- **So that** I have a clear target to work toward and know what success looks like

#### Acceptance Criteria:

- **`AC-HT-GOAL-01-01` Newbie completes goal-setting onboarding flow**
  - **Given** a new user has just launched the app for the first time
  - **When** the app displays the onboarding goal-setting screen
  - **Then** a numeric input field is rendered with placeholder text "Enter workouts per week" and default value ""
  - **And** a "Set Goal" button is visible and clickable
  - **And** the screen loads in <500ms

- **`AC-HT-GOAL-01-02` Goal value persists and is retrievable**
  - **Given** the application is in `ENVIRONMENT=test` mode
  - **When** the user enters the value `3` and submits the goal
  - **Then** the system records goal `{ week_start: <monday_timestamp>, goal_count: 3, role: "newbie" }` to local database
  - **And** when the app is closed and reopened, querying `GET /goals/current` returns `{ goal_count: 3, week: <current_week> }` in <100ms
  - **And** the home screen displays "Goal: 3 workouts this week" in the progress bar widget

- **`AC-HT-GOAL-01-03` Edge case: user enters goal of 0**
  - **Given** the goal input form is displayed
  - **When** the user enters `0` as the weekly goal
  - **Then** the system accepts the input without validation error
  - **And** the goal is saved as `{ goal_count: 0 }`
  - **And** no confirmation message is shown (user choice is honored)

---

## 🆔 Adjust Weekly Goal Mid-Week
- **PRD Reference:** Feature: Weekly Goal Setting
- **Story ID:** `US-HT-GOAL-02`

**User Story:**
- **As a** Workout Newbie
- **I want to** change my weekly goal during the week
- **So that** I can adapt my target if circumstances change

#### Acceptance Criteria:

- **`AC-HT-GOAL-02-01` User accesses goal adjustment flow**
  - **Given** a user is on the home screen and has an active weekly goal
  - **When** the user taps the goal widget (e.g., "Goal: 3 workouts")
  - **Then** a modal or edit screen opens displaying the current goal value
  - **And** an input field is populated with the current goal value `3`
  - **And** a "Save" button is visible

- **`AC-HT-GOAL-02-02` New goal value is saved and retroactive tracking is consistent**
  - **Given** the current week is Monday–Sunday; it is Wednesday; 1 workout is logged
  - **When** the user changes the goal from `3` to `4` and taps "Save"
  - **Then** the system updates `{ week_start: <monday>, goal_count: 4 }` in the database
  - **And** the home screen progress bar immediately updates to "1 of 4"
  - **And** historical tracking for this week uses the new goal (not the old one)

- **`AC-HT-GOAL-02-03` Test mode: time-bound state override**
  - **Given** `ENVIRONMENT=test` and a goal change is triggered
  - **When** the system processes the goal update, it compresses the sync delay to 0ms (immediate)
  - **Then** the response JSON is returned in <50ms
  - **And** local cache is flushed and refreshed synchronously

---

## 🆔 Log Basic Workout (Minimal Friction)
- **PRD Reference:** Feature: Workout Logging
- **Story ID:** `US-HT-LOG-01`

**User Story:**
- **As a** Workout Newbie
- **I want to** log a completed workout in under 30 seconds with minimal fields
- **So that** logging doesn't kill my momentum after a workout

#### Acceptance Criteria:

- **`AC-HT-LOG-01-01` One-tap logging interface is accessible**
  - **Given** a user is on the home screen
  - **When** the user taps the "Log Workout" button
  - **Then** a modal or sheet slides up displaying a minimal logging form
  - **And** required fields are: `[workout_date, workout_type]`
  - **And** optional fields are: `[duration_minutes, notes]`
  - **And** `workout_type` defaults to a dropdown: `["Strength", "Cardio", "Flexibility", "Custom"]`
  - **And** form renders in <300ms

- **`AC-HT-LOG-01-02` Minimal form submission completes in <2 seconds**
  - **Given** the logging form is open
  - **When** the user selects `{ date: "today", type: "Strength", duration: null, notes: null }` and taps "Submit"
  - **Then** the system validates that `date` and `type` are present
  - **And** a workout record `{ user_id, date: <timestamp>, type: "Strength", duration_min: null, notes: null }` is committed to the local database
  - **And** the submission endpoint returns `{ status: "success", workout_id: "<uuid>" }` in <2.0s
  - **And** the modal closes and the home screen updates (progress bar increments)

- **`AC-HT-LOG-01-03` Test mode: immediate offline sync simulation**
  - **Given** `ENVIRONMENT=test` and offline logging is triggered
  - **When** a workout is submitted while the app is offline (network unreachable)
  - **Then** the record is written to local SQLite immediately
  - **And** a background sync job is queued to fire in exactly 2 seconds (test compression)
  - **And** when connectivity is restored, the queued record syncs to backend in <1s

---

## 🆔 Log Workout with Detailed Metrics (Experienced Users)
- **PRD Reference:** Feature: Workout Logging
- **Story ID:** `US-HT-LOG-02`

**User Story:**
- **As a** Gym Rat
- **I want to** log detailed performance metrics (RPE, reps, weight, velocity, fatigue) when I complete a workout
- **So that** I can track fine-grained progression across my lifts

#### Acceptance Criteria:

- **`AC-HT-LOG-02-01` Advanced logging form is accessible to experienced users**
  - **Given** a user profile is flagged as `role: "experienced"` or has 10+ logged workouts
  - **When** the user taps "Log Workout" and selects `type: "Strength"`
  - **Then** the form expands to show advanced metric fields: `[exercise_name, weight_lbs, reps, RPE (1-10), velocity, fatigue_level]`
  - **And** each field is optional and pre-populated with user's previous values (via autocomplete)

- **`AC-HT-LOG-02-02` Detailed metrics are stored and queryable**
  - **Given** the advanced logging form is displayed
  - **When** the user enters `{ exercise: "Bench Press", weight: 185, reps: 8, RPE: 8, velocity: "medium", fatigue: 6 }` and submits
  - **Then** the system stores: `{ workout_id, exercise: "Bench Press", weight_lbs: 185, reps: 8, rpe: 8, velocity_enum: "medium", fatigue_scale: 6 }`
  - **And** when querying `GET /workouts/{workout_id}/metrics`, the full object is returned with all fields intact

- **`AC-HT-LOG-02-03` Edge case: missing optional metric fields**
  - **Given** the advanced form is open
  - **When** the user enters only `{ exercise: "Squat", weight: 225 }` (omitting reps, RPE, velocity)
  - **Then** the system accepts the submission
  - **And** stores `{ exercise: "Squat", weight_lbs: 225, reps: null, rpe: null, velocity: null }`
  - **And** no validation error is thrown

---

## 🆔 Log Workout for Past Date
- **PRD Reference:** Feature: Workout Logging
- **Story ID:** `US-HT-LOG-03`

**User Story:**
- **As a** Workout Newbie or Gym Rat
- **I want to** log a workout that I completed on a previous day
- **So that** I can capture makeup workouts or delayed logging without losing the record

#### Acceptance Criteria:

- **`AC-HT-LOG-03-01` User can select any past date**
  - **Given** the logging form is open
  - **When** the user taps the date field (currently set to "today")
  - **Then** a date picker calendar opens
  - **And** the user can select any date within the past 90 days
  - **And** the selected date is populated into the form

- **`AC-HT-LOG-03-02` Past date workout is logged with correct timestamp**
  - **Given** the current date is May 20, 2026
  - **When** the user logs a workout with `date: "May 18, 2026"` (2 days ago)
  - **Then** the system stores `{ logged_at: <timestamp_now>, workout_date: <timestamp_may_18> }`
  - **And** the workout counts toward May 18's progress (not May 20)
  - **And** when viewing the weekly summary for week of May 12, the workout appears under May 18

- **`AC-HT-LOG-03-03` Edge case: attempt to log 100+ days in past**
  - **Given** the current date is May 20, 2026
  - **When** the user attempts to select a date beyond 90 days ago (e.g., Feb 1, 2026)
  - **Then** the date picker disables dates older than 90 days
  - **And** a tooltip message appears: "Workouts older than 90 days cannot be logged"

---

## 🆔 View Home Screen Progress Bar
- **PRD Reference:** Feature: Progress Tracking & Visualization
- **Story ID:** `US-HT-PROG-01`

**User Story:**
- **As a** Workout Newbie
- **I want to** see my progress toward my weekly goal on the home screen
- **So that** I have instant visibility into how close I am to success

#### Acceptance Criteria:

- **`AC-HT-PROG-01-01` Progress bar displays workout count vs. goal**
  - **Given** a user has set a weekly goal of 3 workouts and logged 2
  - **When** the home screen is loaded
  - **Then** a progress bar widget is displayed prominently showing "2 of 3"
  - **And** the bar is 66% filled (2/3)
  - **And** the widget renders in <500ms

- **`AC-HT-PROG-01-02` Progress bar updates in real-time**
  - **Given** the home screen is open and showing "2 of 3"
  - **When** the user logs a new workout via the logging form
  - **Then** the modal closes and the progress bar immediately updates to "3 of 3"
  - **And** the bar is now 100% filled

- **`AC-HT-PROG-01-03` Test mode: state machine override**
  - **Given** `ENVIRONMENT=test`
  - **When** a workout is logged, the local UI state is updated immediately (simulating optimistic update)
  - **Then** a background sync task is queued to validate with the server in exactly 500ms (test latency)
  - **And** if the server confirms, the state is locked; if not, the UI reverts

---

## 🆔 View Weekly Summary Card
- **PRD Reference:** Feature: Progress Tracking & Visualization
- **Story ID:** `US-HT-PROG-02`

**User Story:**
- **As a** Workout Newbie or Gym Rat
- **I want to** see a summary of my week's workouts (which ones I did, duration, goal met/missed)
- **So that** I understand my overall weekly performance at a glance

#### Acceptance Criteria:

- **`AC-HT-PROG-02-01` Weekly summary card displays aggregated data**
  - **Given** a user completed a week (Monday–Sunday)
  - **When** the user views the Weekly Summary card
  - **Then** the card displays:
    - Goal: `3 workouts`
    - Completed: `3 workouts`
    - Status: `Goal Met ✓`
    - Total Duration: `180 minutes`
    - Workouts by type: `Strength: 2, Cardio: 1`
    - Dates: `Mon, Wed, Fri`

- **`AC-HT-PROG-02-02` Summary is calculated from logged workouts**
  - **Given** logged workouts: `[{date: Mon, type: Strength, dur: 60}, {date: Wed, type: Strength, dur: 70}, {date: Fri, type: Cardio, dur: 50}]`
  - **When** the summary is generated
  - **Then** the calculation is: `total_count = 3`, `total_duration = 180`, `types = {Strength: 2, Cardio: 1}`
  - **And** the `Goal Met` flag is set to `true` (3 >= 3)

- **`AC-HT-PROG-02-03` Edge case: partial week (mid-week view)**
  - **Given** the current date is Wednesday and the user has logged 1 workout
  - **When** the weekly summary is viewed
  - **Then** the card displays current progress: `"1 of 3 (On Track)"`
  - **And** the total duration so far: `60 minutes`
  - **And** no "Goal Met" badge is shown (week is not complete)

---

## 🆔 Create Weekly Workout Plan
- **PRD Reference:** Feature: Flexible Plan Management
- **Story ID:** `US-HT-PLAN-01`

**User Story:**
- **As a** Workout Newbie or Gym Rat
- **I want to** create a plan for the week (which days, which workout types, target duration)
- **So that** I have a structure to follow and can adapt if needed

#### Acceptance Criteria:

- **`AC-HT-PLAN-01-01` Plan creation form is accessible**
  - **Given** a user is in the Plan section
  - **When** the user taps "+ Create Plan" or "+ New Week"
  - **Then** a form appears with fields:
    - Week Start Date (auto-populated to next Monday)
    - Planned Workouts (array): `[{day, type, target_duration_min, exercises}]`
  - **And** an "Add Workout" button allows adding rows

- **`AC-HT-PLAN-01-02` Plan is saved and rendered on calendar**
  - **Given** the user adds: `[{day: Mon, type: Strength, duration: 60, exercises: [Bench, Squat]}, {day: Wed, type: Cardio, duration: 30}]`
  - **When** the user saves the plan
  - **Then** the system stores: `{ week_start: <date>, user_id, plan_items: [...] }`
  - **And** a calendar or list view displays the planned workouts:
    - `Mon: Strength (60 min) - Bench, Squat`
    - `Wed: Cardio (30 min)`

- **`AC-HT-PLAN-01-03` Edge case: plan with duplicate day entries (split sessions)**
  - **Given** the user attempts to add two workouts on the same day (split session)
  - **When** the plan is saved
  - **Then** both entries are accepted (split sessions are allowed)
  - **And** the day displays: `"Mon: Workout 1 (60 min), Workout 2 (30 min)"`

---

## 🆔 Pivot Workout In-Gym (Log Different Workout Than Planned)
- **PRD Reference:** Feature: Flexible Plan Management
- **Story ID:** `US-HT-PLAN-02`

**User Story:**
- **As a** Gym Rat
- **I want to** log a workout different from my plan when equipment is unavailable
- **So that** I can adapt without penalizing my progress

#### Acceptance Criteria:

- **`AC-HT-PLAN-02-01` Planned workout is shown during logging**
  - **Given** today is Monday and the plan shows `{Mon: Strength - Bench Press}`
  - **When** the user opens the logging form
  - **Then** a hint or pre-fill is shown: `"Planned: Strength - Bench Press"`
  - **And** the type dropdown still allows selection of any type

- **`AC-HT-PLAN-02-02` Different workout is accepted without penalty**
  - **Given** the plan shows `{Mon: Strength}`
  - **When** the user logs `{type: Cardio, duration: 45}` instead
  - **Then** the workout is saved: `{ date: Mon, type: Cardio, duration: 45, planned_type: Strength }`
  - **And** the progress bar increments (counts toward goal regardless of deviation)
  - **And** no "deviation penalty" is applied

- **`AC-HT-PLAN-02-03` Pivot reason can be optionally captured**
  - **Given** the logging form is open for a pivot workout
  - **When** the user adds a note: `"Equipment unavailable - did cardio instead"`
  - **Then** the note is stored: `{ ..., notes: "Equipment unavailable..." }`
  - **And** the note is visible in the workout history for context

---

## 🆔 View Analytics Dashboard
- **PRD Reference:** Feature: Advanced Workout Analytics
- **Story ID:** `US-HT-ANALYTICS-01`

**User Story:**
- **As a** Gym Rat
- **I want to** view an analytics dashboard showing my training trends and progression
- **So that** I can make data-driven decisions about my programming

#### Acceptance Criteria:

- **`AC-HT-ANALYTICS-01-01` Analytics dashboard is accessible**
  - **Given** a Gym Rat user with 8+ weeks of logged data
  - **When** the user navigates to "Analytics" or "Insights"
  - **Then** a dashboard is displayed with multiple cards/sections:
    - Workout Frequency Trends (chart)
    - Strength Progression (lift-by-lift)
    - RPE & Fatigue Trends
    - Training Cycle Analysis

- **`AC-HT-ANALYTICS-01-02` Dashboard data is aggregated from logged workouts**
  - **Given** 8 weeks of workout data with metrics (weight, reps, RPE, fatigue)
  - **When** the dashboard is loaded
  - **Then** each card displays calculated insights:
    - Workout Frequency: `"Average 2.75 workouts/week"`
    - Bench Press: `"Weight progression: 185 → 210 lbs (+13.5%)"`
    - RPE Trend: `"Trend: decreasing (better form/efficiency)"`
  - **And** the dashboard loads in <1.0s

- **`AC-HT-ANALYTICS-01-03` Test mode: synthetic data dashboard**
  - **Given** `ENVIRONMENT=test` and a new user with no data
  - **When** the analytics dashboard is accessed
  - **Then** synthetic data is injected: 12 weeks of workout history, 5 exercises, realistic progression
  - **And** the `[TEST DATA]` label is displayed prominently
  - **And** all calculations are verified against the test dataset

---

## 🆔 Generate Custom Analytics Report
- **PRD Reference:** Feature: Advanced Workout Analytics
- **Story ID:** `US-HT-ANALYTICS-02`

**User Story:**
- **As a** Gym Rat
- **I want to** generate custom reports filtered by date range, workout type, or exercise
- **So that** I can analyze specific training phases or exercises

#### Acceptance Criteria:

- **`AC-HT-ANALYTICS-02-01` Report generation form is accessible**
  - **Given** the user is on the Analytics dashboard
  - **When** the user taps "+ Generate Report"
  - **Then** a form appears with filters:
    - Date Range: `[start_date, end_date]` (date pickers)
    - Workout Type: `[Strength, Cardio, Flexibility, All]` (multi-select)
    - Exercise: `[list of exercises, All]` (searchable dropdown)

- **`AC-HT-ANALYTICS-02-02` Report is generated and displayed**
  - **Given** filters selected: `{date_range: Apr 1 - May 15, type: Strength, exercise: Bench Press}`
  - **When** the user taps "Generate"
  - **Then** the system queries workouts matching the filters
  - **And** a report is displayed showing:
    - Total Workouts in Range: `12`
    - Progression: `190 lbs (Apr 1) → 210 lbs (May 15)`
    - RPE Trend: Chart
    - Sessions Summary: Table
  - **And** report generation completes in <5.0s

- **`AC-HT-ANALYTICS-02-03` Edge case: report with no matching data**
  - **Given** filters selected: `{date_range: Sep 1 - Oct 1, type: Cardio}`
  - **When** the user generates the report
  - **Then** the system returns no matching workouts
  - **And** a message displays: `"No workouts found matching these filters. Try adjusting the date range or type."`
  - **And** the user is offered a suggestion to view "Last 12 Weeks" instead

---

End of User Stories Document
