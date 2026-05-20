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

*Generated via User Story Expansion Skill*
