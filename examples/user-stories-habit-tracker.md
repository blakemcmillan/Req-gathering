# User Stories: Habit Tracker

## Feature: Guided Workout Planning

**User Story**
As a beginner, I want to create a weekly workout plan from curated templates, so that I feel confident about what to do at the gym instead of being overwhelmed by too many options.

### Data State

**Initial State**
User has opened the app for the first time. No workouts planned. Exercise library exists but is not yet explored.

**Final State**
User has created a weekly plan (e.g., Full Body 3x/week template). Plan specifies 3 workouts for the week with exercises, sets, reps, and rest periods assigned.

**Core Data Models**
- Workout (id, user_id, week_start_date, name, difficulty_level)
- WorkoutExercise (id, workout_id, exercise_id, sequence, sets, reps, weight, rest_seconds, notes)
- Exercise (id, name, body_part, movement_type, difficulty_level, description, form_tips, equipment)
- Template (id, name, difficulty, weekly_structure, exercises, difficulty_level)

### Acceptance Criteria

**Scenario 1: Beginner Selects Pre-Built Template**
```gherkin
Given a beginner user on the planning screen
When they tap "Use Template" and browse templates filtered by "Beginner"
And they select "Full Body 3x/week"
Then the template loads with 3 workouts pre-populated (Monday, Wednesday, Friday)
And each workout shows exercises, sets, and reps
And they can save the plan by tapping "Create Plan"
```

**Scenario 2: Beginner Customizes a Template**
```gherkin
Given a user has loaded "Full Body 3x/week" template
When they tap into Tuesday's workout and remove the barbell bench press
And select "Dumbbell press" instead
Then the system confirms the exercise swap
And the modified plan reflects the new exercise
And the original template remains unchanged
```

**Scenario 3: Experienced User Builds Custom Workout**
```gherkin
Given a gym rat on the planning screen
When they tap "Create Custom Workout"
And they filter exercises by "Equipment: Barbell, Body Part: Legs"
And they build a leg workout (squat, leg press, leg curl, 3 exercises)
And they save the workout as a template called "Heavy Leg Day"
Then the custom workout is saved to their plan
And "Heavy Leg Day" appears in their template library for future use
```

**Scenario 4: Exercise Description Provides Guidance**
```gherkin
Given a beginner viewing the exercise library
When they tap on "Back Squat"
Then the app shows:
  - 2-sentence description of what the exercise targets
  - Step-by-step form cues (4-5 bullet points)
  - 2-3 common mistakes and how to avoid them
  - Difficulty level (Intermediate)
  - Equipment needed (Barbell, Safety rack)
  - Beginner-friendly alternative (Goblet squat)
```

**Scenario 5: Plan Modification Timeline**
```gherkin
Given a user has created a plan for the week
When the week has started and they tap "Edit Monday's Workout"
And they change exercises 1 hour before the workout
Then the changes are saved
But if they tap after the scheduled workout time
Then the system shows a warning: "Workout may have already started. Continue editing?"
```

### Open Questions & Gaps

1. **Templates & Progression:** Should templates automatically progress difficulty over time (e.g., advance to intermediate after 4 weeks), or does the user manually select?
2. **Customization Limits:** Are there restrictions on how much a user can deviate from a template (e.g., max 2 exercises changed per workout)?
3. **Expert Content:** Who vets template quality and form descriptions? Do we partner with fitness experts?
4. **Equipment Awareness:** Should the app ask users what equipment they have access to and filter templates/exercises accordingly?
5. **Warm-up Guidance:** Should workouts include auto-generated warm-up suggestions, or does the user specify them?
6. **Mobile UX:** Given small phone screens, how many exercises should a user see per workout before scrolling?

---

## Feature: Quick Workout Logging

**User Story**
As a workout newbie, I want to log my completed workout in under 2 minutes with minimal friction, so that I see proof of my progress and stay motivated by a visible streak.

### Data State

**Initial State**
User has completed a workout. A scheduled workout exists in the plan for today.

**Final State**
Workout is logged. Completion is recorded. Streak counter increments. Workout log entry created.

**Core Data Models**
- LoggedWorkout (id, user_id, scheduled_workout_id, date_completed, mode [quick/detailed], status [completed/partial/skipped], notes, created_at)
- LoggedExercise (id, logged_workout_id, exercise_id, sets_completed, reps_completed, weight_used, rpe, notes)
- CompletionStreak (user_id, current_streak_days, longest_streak_days, last_workout_date)

### Acceptance Criteria

**Scenario 1: User Completes Workout as Planned (Quick Log)**
```gherkin
Given a user just finished their planned workout
When they open the app and see a "Log Workout" button on the home screen
And they tap the button
And they tap "Completed as planned"
And they tap "Save"
Then the workout is logged in < 2 seconds
And the home screen shows the completion check (✓)
And the streak counter increments by 1
And the completion count updates (e.g., "3 of 7 this week")
```

**Scenario 2: User Logs Detailed Metrics**
```gherkin
Given a user taps "Log Workout" and chooses "Detailed Log"
When they are shown each exercise from their plan
And they enter actual sets/reps and weight used for each exercise
And they add optional notes (e.g., "felt strong")
And they tap "Save"
Then the detailed metrics are saved against each exercise
And the actual vs. planned comparison displays (e.g., "Planned 5x5@225, Logged 5x5@230")
And they can see the delta highlighted
```

**Scenario 3: User Partially Completed Workout**
```gherkin
Given a user completed 3 of 5 exercises before running out of time
When they log the workout and mark "Partial completion"
And they note which exercises were completed
Then the system records which exercises were done
And calculates a % completion (60%)
And asks if they want to reschedule the remaining exercises
```

**Scenario 4: Offline Logging**
```gherkin
Given a user with no internet connection after their workout
When they tap "Log Workout" while offline
And they complete the log
Then the app shows "Saved locally. Will sync when online."
And the workout is queued for sync
And when the device reconnects, the log automatically syncs to the server
```

**Scenario 5: Late Logging (2 Days After Workout)**
```gherkin
Given a user forgot to log a workout 2 days ago
When they open the app and tap "Log Past Workout"
And they select the date (2 days ago)
And they complete the log
Then the app clarifies the date: "Logging for [date]. Confirm?"
And the workout is recorded with the correct date
And the streak remains unbroken if this was a consecutive day
```

### Open Questions & Gaps

1. **Data Accuracy:** Should we validate that logged data is realistic (e.g., prevent weight entries that are 10x user's max)?
2. **Edit Window:** Can users edit a log forever, or only within 24 hours? After 24 hours, read-only?
3. **Performance Capture:** Should RPE (Rate of Perceived Exertion) be numeric (1-10) or emoji-based for mobile?
4. **Missed Workouts:** If a user doesn't log on a scheduled day, should streak break immediately or after a grace period?
5. **Multi-Day Logging:** Can users batch-log multiple days of workouts at once, or must each be logged separately?
6. **Voice Logging:** Should the app support voice-to-text for quick metric capture (e.g., "3 sets of 5 at 225")?

---

## Feature: Detailed Performance Tracking & Analytics

**User Story**
As an experienced lifter, I want to view my workout performance data in one place with charts showing progression over time, so that I can stop manually tracking in notebooks and make data-driven training decisions.

### Data State

**Initial State**
User has logged 20+ workouts over 2+ months. Historical exercise data exists in the system (weights, reps, dates).

**Final State**
User views the Analytics tab. Performance charts render showing exercise progressions, PR history, completion streaks, and estimated 1RMs.

**Core Data Models**
- LoggedExercise (id, logged_workout_id, exercise_id, weight, reps, rpe, date, est_1rm)
- ExerciseProgression (user_id, exercise_id, max_weight_ever, current_estimated_1rm, last_5_sessions)
- PRRecord (user_id, exercise_id, weight, reps, date_achieved, body_weight)
- CompletionHistory (user_id, date, workout_completed, streaks)

### Acceptance Criteria

**Scenario 1: User Views Exercise Progression Chart**
```gherkin
Given a user with 3+ months of barbell squat logs
When they open Analytics and search "Squat"
And they tap "Barbell Back Squat"
Then a line chart displays:
  - X-axis: date (past 3 months)
  - Y-axis: weight (lbs)
  - Line showing actual weight used per workout
  - Trend line showing overall progression
  - Max and min weights labeled
And the chart loads in < 2 seconds
```

**Scenario 2: User Sees PR History & Estimated 1RM**
```gherkin
Given a user on the Summary tab
When they scroll to "Personal Records"
Then they see a ranked list:
  - Barbell Back Squat: 315 lbs (Dec 15)
  - Deadlift: 425 lbs (Jan 8)
  - Bench Press: 275 lbs (Nov 20)
And they tap a PR to see estimated 1RM: "Your estimated 1RM: 320 lbs"
And they see the calculation method note: "Based on Epley formula"
```

**Scenario 3: User Filters Analytics by Date Range**
```gherkin
Given a user viewing analytics
When they tap "Date Range"
And they select "Last 3 Months" (or custom dates)
And they tap "Apply"
Then all charts and summaries filter to the selected range
And completion calendar shows only workouts in the range
And PR history adjusts (showing only PRs set in that window)
```

**Scenario 4: User Exports Workout History**
```gherkin
Given a user on the Analytics tab
When they tap "Export"
And they select "Date Range: Past 6 Months"
And they tap "Export as CSV"
Then a file is generated with columns: Exercise, Date, Weight, Reps, Notes
And the file is ready to download/email
And the user can open it in Excel or Google Sheets for further analysis
```

**Scenario 5: User Compares Performance Across Periods**
```gherkin
Given a user on the Analytics tab
When they select "Bench Press" exercise
And they tap "Compare Periods"
And they set Period 1: Jan 1 - Jan 31, Period 2: Apr 1 - Apr 30
Then the app shows:
  - Avg weight (Period 1: 250 lbs, Period 2: 275 lbs)
  - Avg reps per set (Period 1: 5, Period 2: 6)
  - Improvement: +25 lbs, +1 rep
And a visual summary: "You've progressed 10% in strength"
```

### Open Questions & Gaps

1. **1RM Calculation Accuracy:** Should the app use Epley, Brzycki, or another formula? Should users be able to override with tested maxes?
2. **Movement Equivalence:** Should the app track related exercises together (e.g., Barbell Squat + Leg Press + Goblet Squat as "Leg Squat Variants") or separately?
3. **Strength Standards:** Should the app show "strength standards" (e.g., "Your squat is Advanced for your body weight") or avoid comparison?
4. **Missing Data:** If a user has gaps in logging (no workouts for 2 weeks), how should the chart display the gap—line break, interpolation, or skip?
5. **Body Weight Tracking:** Should users log body weight? Should it correlate with strength metrics?
6. **Export Formats:** Besides CSV, should we support PDF reports or integration with training platforms (e.g., sync to MyFitnessPal)?

---

## Feature: Adaptive Workout Switching

**User Story**
As a lifter, I want to swap exercises mid-workout if equipment is unavailable, so that I can maintain my training session and program integrity instead of wasting 20 minutes figuring out alternatives.

### Data State

**Initial State**
User is in the middle of a logged workout. A planned exercise is due next. Equipment is unavailable (e.g., barbell squat rack is taken).

**Final State**
User marks exercise as unavailable, selects an app-suggested alternative, and continues the workout with the new exercise recorded.

**Core Data Models**
- ActiveWorkout (id, user_id, workout_id, start_time, current_exercise_index, status [active/paused/completed])
- ExerciseSwap (id, logged_workout_id, original_exercise_id, alternative_exercise_id, reason [equipment/injury/time], timestamp)
- BackupPlan (id, user_id, workout_id, scenario_name, alternatives_map)

### Acceptance Criteria

**Scenario 1: User Marks Equipment Unavailable & Gets Suggestions**
```gherkin
Given a user is logging a workout in-progress
When they reach "Barbell Back Squat"
And they tap the exercise and select "Can't do - equipment unavailable"
Then the app shows 2-3 suggested alternatives within 1 second:
  1. Goblet Squat (recommended, minimal equipment)
  2. Leg Press (same muscles, barbell-free)
  3. Split Squat (lower-body quad alternative)
And each suggestion shows: name, target muscles, difficulty, equipment needed
```

**Scenario 2: User Swaps and Continues Workout**
```gherkin
Given a user sees the alternative suggestions
When they tap "Leg Press" to select it
Then the app confirms: "Swapping Barbell Squat → Leg Press. Continue?"
And they tap "Yes"
And the logged workout now records Leg Press instead of Back Squat
And the app shows a note: "[Swap] Barbell Squat unavailable"
And they can continue logging reps/weight for Leg Press
```

**Scenario 3: User Creates a Backup Plan**
```gherkin
Given a user who frequently encounters limited equipment
When they open their saved workout "Heavy Leg Day"
And they tap "Create Backup Plan"
And they name it "No Squat Rack"
And they assign alternatives:
  - Barbell Back Squat → Leg Press
  - Barbell Leg Press → Smith Machine Leg Press
And they save
Then "No Squat Rack" is stored as a variant of the original workout
And they can use it in future when constraints apply
```

**Scenario 4: User Skips Exercise Entirely**
```gherkin
Given a user who can't find any viable alternative
When they mark "Barbell Bench Press" as unavailable
And they view suggestions but none are suitable (e.g., all benches taken)
And they tap "Skip Exercise"
Then the app asks: "This reduces training volume. Skip anyway?"
And if they confirm, the exercise is marked as [SKIPPED]
And they continue to the next exercise
And the logged workout shows completion % adjusted (e.g., 75% if 1 of 4 exercises skipped)
```

**Scenario 5: Swap History in Workout Detail**
```gherkin
Given a user reviews a past logged workout
When they open the workout detail
Then they see each exercise with a note if a swap occurred:
  - Barbell Back Squat [SWAPPED to Leg Press]
  - Leg Press (logged as normal)
And they can tap [SWAPPED] to see the reason and alternative
And they can edit the swap for future reference
```

### Open Questions & Gaps

1. **Algorithm Ranking:** What factors determine the ranking of alternatives? (Muscle similarity, equipment, difficulty, availability stats?)
2. **Frequency Tracking:** Should the app track which alternatives are most commonly used to improve future suggestions?
3. **Injury Mode:** Should there be a dedicated "Injury - Do Not Use" flag for exercises to avoid suggesting them?
4. **Crowdsourced Alternatives:** Should users be able to submit their own alternative swaps for others to use?
5. **Equipment Library:** How does the app know what equipment is available at the gym (unless users manually select)?
6. **Time Pressure:** If a user is running short on time, should suggestions prioritize exercises with shorter duration?

---

## Feature: Streak Engine & Habit Logger

### 🆔 Quick Habit Logging
- **PRD Reference:** Streak Engine Core Feature - Pain: "I forget what I did today"
- **Story ID:** `US-HT-STRK-001`

**User Story:**
- **As a** habit tracker user
- **I want to** record a completed habit with a single tap (checkbox or button)
- **So that** I maintain an accurate historical log and build momentum toward a streak

#### Acceptance Criteria:

- **`AC-HT-STRK-001-01` User logs a habit successfully**
  - **Given** user is on the home dashboard and a habit exists in their profile (e.g., "Drank 8 glasses of water")
  - **When** user taps the habit checkbox or "Log Completion" button with current date/time
  - **Then** the log entry is saved to the database and persists within 1.0 second
  - **And** the UI displays confirmation: "✓ Logged at [HH:MM]" for 2 seconds, then fades
  - **And** the database timestamp is recorded in UTC

- **`AC-HT-STRK-001-02` Logging works offline with sync-on-reconnect**
  - **Given** user has no internet connection
  - **When** user taps the habit checkbox
  - **Then** the app displays "Saved locally. Will sync when online."
  - **And** the log is queued in local storage
  - **And** when the device reconnects, the log automatically syncs within 5 seconds without user action
  - **And** the habit is attributed to the correct date (today, not sync date)

- **`AC-HT-STRK-001-03` User cannot log the same habit twice in one day**
  - **Given** user already logged "Gym Session" on May 20
  - **When** user attempts to log "Gym Session" again on May 20 (same day, same habit)
  - **Then** the button becomes disabled or shows "Already logged today"
  - **And** a tap shows a tooltip: "You logged this on May 20 at 7:15 PM. Tap to edit or delete that entry."

---

### 🆔 Streak Display & Tracking
- **PRD Reference:** Streak Engine - Value: "Keep people hooked via Current Streak counter"
- **Story ID:** `US-HT-STRK-002`

**User Story:**
- **As a** habit tracker user
- **I want to** see my current streak and all-time best streak prominently on the home screen
- **So that** I stay motivated and see my progress at a glance

#### Acceptance Criteria:

- **`AC-HT-STRK-002-01` Current streak displays accurately**
  - **Given** user has logged the same habit on 7 consecutive days (May 14–20)
  - **When** they open the home dashboard
  - **Then** the habit card displays: "🔥 Current Streak: 7 days" in a large, prominent font (18px+)
  - **And** the streak number is in a bold, contrasting color (e.g., orange/red)
  - **And** the display updates instantly (< 500ms) when a new log is recorded

- **`AC-HT-STRK-002-02` All-time best streak is displayed**
  - **Given** user's highest consecutive streak was 30 days (achieved in March)
  - **When** they view a habit card
  - **Then** below the current streak, "Best: 30 days" is shown in smaller text (12px)
  - **And** the best streak shows the month/year it was achieved: "Best: 30 days (Mar 2026)"

- **`AC-HT-STRK-002-03` Streak breaks correctly after a missed day**
  - **Given** user logged the habit for 5 consecutive days ending May 19
  - **When** May 20 ends (11:59 PM local time) without a log entry
  - **Then** the current streak resets to 0
  - **And** the habit card shows: "Streak broken. Start a new one!" with a "Log Now" button
  - **And** the broken streak is recorded in history (for recovery tracking)

- **`AC-HT-STRK-002-04` Streak persists across app sessions**
  - **Given** user logged on May 19 and May 20
  - **When** they close the app and reopen it 6 hours later (still May 20)
  - **Then** the current streak still shows "2 days"
  - **And** the habit remains eligible for logging (day not complete)

---

### 🆔 Timezone & Midnight Reset Handling
- **PRD Reference:** Streak Engine - Pain: "Night owls lose streaks when logging after midnight"
- **Story ID:** `US-HT-STRK-003`

**User Story:**
- **As a** night shift worker or someone in a timezone different from the server
- **I want to** log habits with a grace period until 3:00 AM local time before the day resets
- **So that** I don't lose my streak for being awake at an unconventional time

#### Acceptance Criteria:

- **`AC-HT-STRK-003-01` Grace period extends until 3:00 AM local time**
  - **Given** user is in PST (UTC-7) and logs a workout at 2:15 AM on May 21
  - **When** they tap the "Gym Session" checkbox
  - **Then** the system records it as May 20 (still "today" in their timezone grace window)
  - **And** the streak is calculated as if logged on May 20, not May 21
  - **And** the log entry displays: "Logged on May 20 at 2:15 AM"

- **`AC-HT-STRK-003-02` Logs after 3:00 AM local time count as next day**
  - **Given** same user in PST logs at 3:15 AM on May 21
  - **When** they tap the habit checkbox
  - **Then** the system records it as May 21 (past the grace window)
  - **And** if they didn't log on May 20, the streak breaks
  - **And** a new streak can start on May 21

- **`AC-HT-STRK-003-03` Server uses UTC internally, local display is user-specific**
  - **Given** user A (PST) and user B (EST) both log at their local "2:30 AM" on May 21
  - **When** the backend stores both entries
  - **Then** the database records different UTC timestamps (user A's 2:30 AM PST ≈ 9:30 AM UTC; user B's ≈ 6:30 AM UTC)
  - **And** both users see "May 20" in their app (within grace window)
  - **And** the UI always displays local time to each user

- **`AC-HT-STRK-003-04` Timezone changes are handled gracefully**
  - **Given** user travels from PST to EST (3-hour time difference)
  - **When** they log a habit at 1:00 AM on May 21 EST (first time in EST)
  - **Then** the system recognizes the timezone shift via device settings
  - **And** the grace window applies to the NEW timezone (EST, not PST)
  - **And** the log is recorded correctly without breaking the streak

---

### 🆔 Streak Freeze Feature
- **PRD Reference:** Streak Engine - Gain: "Safety net for illness/vacation without losing streaks"
- **Story ID:** `US-HT-STRK-004`

**User Story:**
- **As a** dedicated habit tracker user
- **I want to** use a "Streak Freeze" token to pause a streak for 1 day without breaking it
- **So that** I can protect my streaks during illness, vacation, or unexpected life events

#### Acceptance Criteria:

- **`AC-HT-STRK-004-01` Regular user gets 1 free freeze per month**
  - **Given** a free-tier user on May 20 with an active 15-day streak
  - **When** they tap the habit and select "Freeze Streak" (or menu → Streak Options)
  - **Then** they see: "You have 1 freeze available this month. Use now?"
  - **And** if they confirm, the freeze is applied
  - **And** they can skip logging for May 21 without the streak breaking
  - **And** on May 22, the streak resumes at 16 days (May 21 is skipped, not broken)

- **`AC-HT-STRK-004-02` Premium user gets 3 freezes per month**
  - **Given** a premium subscriber with an active 25-day streak
  - **When** they tap "Freeze Streak"
  - **Then** they see: "You have 3 freezes available this month. Use now?"
  - **And** they can freeze up to 3 separate days per month
  - **And** freezes reset on the 1st of each month

- **`AC-HT-STRK-004-03` Freezes can be earned at 30-day milestone**
  - **Given** a user just hit a 30-day streak for the first time
  - **When** the 30-day milestone achievement unlocks
  - **Then** a popup shows: "Milestone unlocked! +1 Bonus Freeze Token earned."
  - **And** the free-tier user now has 2 freezes available (1 monthly + 1 bonus)
  - **And** the bonus does not reset monthly (permanent)

- **`AC-HT-STRK-004-04` Freeze prevents streak break, not activity**
  - **Given** a user has frozen a streak for May 21
  - **When** May 21 ends without a log entry
  - **Then** the streak count remains the same (e.g., 25 days)
  - **And** May 21 is marked as [FROZEN] in the habit history (not blank)
  - **And** if the user logs on May 21 anyway (feels better), the log is recorded and counts
  - **And** the freeze is still consumed (used up for the month)

---

### 🆔 Instant Streak Recalculation Performance
- **PRD Reference:** Streak Engine - Technical Requirement: "Streak count recalculates instantly < 1 second"
- **Story ID:** `US-HT-STRK-005`

**User Story:**
- **As a** habit tracker user
- **I want to** see my streak count update instantly when I log a habit
- **So that** the app feels snappy and I get immediate gratification

#### Acceptance Criteria:

- **`AC-HT-STRK-005-01` Streak updates in < 1.0 second after logging**
  - **Given** user is on the home dashboard with a visible habit card showing "Current Streak: 4 days"
  - **When** they tap the checkbox to log the habit
  - **Then** the UI displays a checkmark within 300ms
  - **And** within 1.0 second total, the streak count updates to "5 days"
  - **And** no loading spinner or "recalculating..." message is shown (instant update)

- **`AC-HT-STRK-005-02` Recalculation happens server-side, optimistic UI update client-side**
  - **Given** user taps to log a habit
  - **When** the tap is registered
  - **Then** the UI immediately updates locally (optimistic update)
  - **And** the request is sent to the server in the background
  - **And** if the server confirms success, the state persists
  - **And** if the server rejects (e.g., duplicate log), the UI reverts within 500ms
  - **And** a brief toast message shows: "Couldn't log. Already logged today."

- **`AC-HT-STRK-005-03` Streak recalc includes logic for grace period & freezes**
  - **Given** user's data includes: current streak, frozen days, timezone offset, past logs
  - **When** they log a new habit
  - **Then** the recalculation:
    1. Checks for duplicates (same habit, same calendar day)
    2. Applies timezone grace window (until 3 AM local)
    3. Honors streak freezes (skipped days don't break chain)
    4. Increments current streak if consecutive
    5. Stores timestamp in UTC
  - **And** all calculations complete in < 500ms server-side

- **`AC-HT-STRK-005-04` Cache strategy prevents thundering herd**
  - **Given** 1000 users try to log a habit at the same time (e.g., 12:00 PM noon)
  - **When** the requests hit the server
  - **Then** streak calculations are cached at the user level (no cross-user contention)
  - **And** database queries use indexed lookups (user_id, habit_id, date)
  - **And** 95th percentile response time remains < 1.0 second even under load

---

### 🆔 Milestone Celebrations & Gamification
- **PRD Reference:** Streak Engine - Gain: "Visual celebration at 3, 7, 30-day milestones"
- **Story ID:** `US-HT-STRK-006`

**User Story:**
- **As a** habit tracker user
- **I want to** receive visual celebrations (badges, confetti, notifications) when I hit streak milestones
- **So that** I feel recognized for my progress and stay motivated

#### Acceptance Criteria:

- **`AC-HT-STRK-006-01` 3-day milestone triggers celebration popup**
  - **Given** user just logged their 3rd consecutive day of a habit
  - **When** the streak updates to "3 days"
  - **Then** a full-screen modal appears with:
    - Animated confetti falling for 2–3 seconds
    - Badge image: "🔥 3-Day Streak!"
    - Message: "Nice work! You're on fire."
    - Sound effect (optional, can be muted)
    - "Continue" button to dismiss
  - **And** the badge is added to their profile/trophy case

- **`AC-HT-STRK-006-02` 7-day and 30-day milestones unlock premium rewards**
  - **Given** user reaches a 7-day streak
  - **When** the celebration popup appears
  - **Then** it shows: "7-Day Streak Unlocked! Bonus: +1 Freeze Token"
  - **And** the token is credited to their account immediately
  - **And** for 30-day: "30-Day Legend! Unlock premium badge."
  - **And** the badge appears in their profile with date achieved

- **`AC-HT-STRK-006-03` Celebration only triggers once per milestone**
  - **Given** user hit the 7-day milestone on May 20
  - **When** they log again on May 21 (streak now 8 days)
  - **Then** no celebration popup appears
  - **And** the 7-day badge remains in their trophy case, not repeated

- **`AC-HT-STRK-006-04` Milestone celebration can be dismissed**
  - **Given** a celebration popup is displayed
  - **When** user taps "Continue" or the X button
  - **Then** the popup closes immediately (< 200ms)
  - **And** the app returns to the home dashboard
  - **And** the achievement is recorded in history

---

### 🆔 Micro-Calendar View (Last 7 Days)
- **PRD Reference:** Streak Engine - UI Feature: "Visual momentum via last 7 days calendar"
- **Story ID:** `US-HT-STRK-007`

**User Story:**
- **As a** habit tracker user
- **I want to** see a micro-calendar showing the last 7 days with visual indicators (✓ or ○)
- **So that** I can visually assess my momentum and identify gaps at a glance

#### Acceptance Criteria:

- **`AC-HT-STRK-007-01` Micro-calendar displays last 7 days horizontally**
  - **Given** user is viewing a habit card (e.g., "Gym Session")
  - **When** they open the habit detail or scroll within the card
  - **Then** a 7-day horizontal calendar is visible:
    - Days shown: Sun, Mon, Tue, Wed, Thu, Fri, Sat (most recent on right)
    - Green checkmark (✓) for days logged
    - Gray empty circle (○) for days not logged
    - Current day is highlighted with a border
    - Dates are shown below each day (e.g., "May 20")
  - **And** the calendar is responsive and scales to screen width

- **`AC-HT-STRK-007-02` Clicking a day shows log details**
  - **Given** user sees the 7-day calendar
  - **When** they tap a green checkmark (logged day)
  - **Then** a tooltip or popup shows:
    - Date: "May 20"
    - Time logged: "7:15 PM"
    - Optional notes: [if entered by user]
  - **And** they can tap "Edit" to modify the entry
  - **And** when they tap a gray circle (not logged), it shows: "Not logged. Log now?"

- **`AC-HT-STRK-007-03` Calendar updates in real-time**
  - **Given** user is viewing the 7-day calendar
  - **When** they log a new entry (tap checkbox)
  - **Then** the corresponding day updates to green checkmark immediately (< 300ms)
  - **And** the streak counter increments simultaneously

- **`AC-HT-STRK-007-04` Frozen days are visually distinct**
  - **Given** user has frozen a streak day (e.g., May 18)
  - **When** they view the 7-day calendar
  - **Then** May 18 shows a snowflake icon (❄) instead of ✓ or ○
  - **And** hovering/tapping the snowflake shows: "Streak Frozen - no activity required"

---

### 🆔 Habit Logger Core
- **PRD Reference:** Streak Engine - Core Feature: "Simple checkbox UI for daily habit logging"
- **Story ID:** `US-HT-STRK-008`

**User Story:**
- **As a** any habit tracker user
- **I want to** have a simple, large, tappable checkbox or button next to each habit
- **So that** I can log habits with minimal friction (single tap)

#### Acceptance Criteria:

- **`AC-HT-STRK-008-01` Checkbox is large and easy to tap**
  - **Given** user is on the home dashboard
  - **When** they view a habit list
  - **Then** each habit has a large checkbox (minimum 48px × 48px) or "Log" button
  - **And** the button uses high contrast colors (e.g., white background, green checkbox)
  - **And** the tap target meets accessibility standards (WCAG 2.1 Level AA)

- **`AC-HT-STRK-008-02` Habit label clearly describes the action**
  - **Given** a habit card is displayed
  - **When** user reads the habit text
  - **Then** the text is clear and actionable, e.g.:
    - ✅ "Drank 8 glasses of water"
    - ✅ "Hit the gym"
    - ✅ "Meditated 10 minutes"
    - ❌ "Health" (too vague)
    - ❌ "Exercise" (too vague)

- **`AC-HT-STRK-008-03` Logged habits show visual feedback**
  - **Given** a habit has been logged today
  - **When** user views the habit card
  - **Then** the checkbox is checked (✓) or the button shows "Logged ✓"
  - **And** the button is disabled (grayed out or shows "Already logged today")
  - **And** the habit card has a subtle background highlight (light green)

- **`AC-HT-STRK-008-04` Unlogged habits are visually distinct**
  - **Given** a habit has not been logged today
  - **When** user views the habit card
  - **Then** the checkbox is empty (○) or the button shows "Log"
  - **And** the button is clickable and has a call-to-action color (e.g., blue, orange)
  - **And** the card background is neutral (white or light gray)

---

### 🆔 Habit Reminders & Notifications
- **PRD Reference:** Streak Engine - Separate System: "Push notifications to remind users about streaks"
- **Story ID:** `US-HT-STRK-009`

**User Story:**
- **As a** a habit tracker user
- **I want to** receive push notifications reminding me to log habits
- **So that** I don't forget and break my streaks

#### Acceptance Criteria:

- **`AC-HT-STRK-009-01` Notifications are sent at user-defined time**
  - **Given** user has set a reminder time for "Gym Session" at 6:00 PM
  - **When** 6:00 PM arrives (in user's local timezone)
  - **Then** a push notification is sent: "Remember your streak! Time to hit the gym. 🔥"
  - **And** the notification is delivered within 2 minutes of the set time
  - **And** the user can tap the notification to open the app and log

- **`AC-HT-STRK-009-02` Notifications adapt based on streak status**
  - **Given** user has a 5-day active streak
  - **When** the reminder notification is sent
  - **Then** the message reads: "Don't break your 5-day streak! Time to gym. 🔥"
  - **And** for a new habit (1-day streak): "Great start! Keep it up. Time to gym. 💪"
  - **And** for a frozen streak: "Your streak is frozen. No pressure today—rest up!"

- **`AC-HT-STRK-009-03` Notifications respect quiet hours**
  - **Given** user has set quiet hours from 10:00 PM to 8:00 AM
  - **When** a reminder is scheduled for 11:00 PM
  - **Then** the notification is NOT sent at 11:00 PM
  - **And** the notification is queued and sent at 8:05 AM (first opportunity after quiet hours)
  - **And** the user receives an alert: "Reminder queued. Will notify at 8:05 AM."

- **`AC-HT-STRK-009-04` Users can opt out of notifications per habit**
  - **Given** user is viewing a habit card
  - **When** they tap "Settings" for that habit
  - **And** they toggle "Reminders" OFF
  - **Then** no notifications are sent for that habit
  - **And** they can re-enable by toggling ON again

- **`AC-HT-STRK-009-05` Notification system is decoupled from logging**
  - **Given** the notification service is down or delayed
  - **When** user logs a habit manually (via the app)
  - **Then** the logging works as normal (streak updates, etc.)
  - **And** the notification failure does NOT block or delay logging
  - **And** when the notification service recovers, pending notifications are sent

---

*Generated via User Story Expansion Skill*
