# User Stories & Acceptance Criteria: Habit Tracker

**Document Version:** 1.0  
**Generated:** 2026-05-20  
**Input PRD:** `examples/prd-habit-tracker.md`

---

## Feature Code Legend

| Code | Feature | User Role |
|------|---------|-----------|
| PLAN | Smart Workout Planning (Beginner Edition) | Workout Newbie |
| QUICK | Quick-Log Interface (Minimal Friction) | Workout Newbie, Gym Rat |
| DASH | Progress & Performance Dashboard | Workout Newbie, Gym Rat |
| FORM | Form Guidance & Education | Workout Newbie |
| ANALYTICS | Advanced Analytics & Insights | Gym Rat |
| ADAPT | Flexible Plan Adaptation | Gym Rat |

---

# FEATURE: Smart Workout Planning (Beginner Edition)

## 🆔 US-HT-PLAN-01: Receive Frequency Recommendation for Beginner Training

**PRD Reference:** Feature 1 — "Don't know how often per week I should work out"

**Story ID:** `US-HT-PLAN-01`

**User Story:**
- **As a** Workout Newbie
- **I want to** receive a science-backed workout frequency recommendation (3-4 days/week)
- **So that** I know exactly how many days per week to commit to, eliminating guesswork

#### Acceptance Criteria:

**`AC-HT-PLAN-01-01` Happy Path: Newbie receives 3-4 day/week recommendation**
- **Given** a new user is on the plan creation wizard with no prior workout history
- **When** they answer "beginner" to experience level
- **Then** the system displays: "We recommend 3-4 workouts per week for sustainable habit formation"
- **And** the recommendation includes a brief science-backed rationale (1-2 sentences)
- **And** the user can accept or manually override the frequency

**`AC-HT-PLAN-01-02` Fast-Test Mode: Recommendation display under 500ms**
- **Given** the application is configured with `ENVIRONMENT=test`
- **When** the frequency recommendation lookup is triggered
- **Then** the recommendation displays in <500ms from API call
- **And** no database round-trips block the UI render
- **And** the state mutation (frequency_recommended = true) is atomic

**`AC-HT-PLAN-01-03` Boundary Condition: User with prior training history shows different recommendation**
- **Given** a user's profile indicates "intermediate" experience level
- **When** they request a frequency recommendation
- **Then** the system returns 4-6 days/week recommendation (not 3-4)
- **And** the recommendation data includes the user's experience level as a decision factor

---

## 🆔 US-HT-PLAN-02: Browse Beginner-Appropriate Exercises and Filter by Movement Pattern

**PRD Reference:** Feature 1 — "Overwhelmed choosing which exercises are right for a beginner"

**Story ID:** `US-HT-PLAN-02`

**User Story:**
- **As a** Workout Newbie
- **I want to** browse a curated library of beginner-appropriate exercises organized by movement pattern (push, pull, leg, core)
- **So that** I can confidently select exercises that are compound, low-injury-risk, and minimal-equipment

#### Acceptance Criteria:

**`AC-HT-PLAN-02-01` Happy Path: Filter exercises by movement pattern and select for plan**
- **Given** a user is on the exercise selection screen with all exercises visible
- **When** they tap "Filter by Movement Pattern"
- **And** they select "Push"
- **Then** the library displays only push exercises (bench press, overhead press, dumbbell press, pushups)
- **And** each exercise shows: name, difficulty_level (Beginner), equipment_required, target_muscles
- **And** the user can tap an exercise to add it to their plan
- **And** when they tap "Add to Plan", the exercise is inserted with default beginner reps/sets

**`AC-HT-PLAN-02-02` Fast-Test Mode: Exercise filtering completes in <200ms**
- **Given** the app is running with `ENVIRONMENT=test`
- **When** a movement pattern filter is applied to an exercise library of 100+ exercises
- **Then** filtered results are returned in <200ms
- **And** the state mutation (selected_filter = "Push") is applied without re-rendering the entire library

**`AC-HT-PLAN-02-03` Boundary Condition: Empty filter results**
- **Given** a user applies a filter that matches zero exercises (e.g., "Olympic_Lifting" for beginners)
- **When** the filter is applied
- **Then** the system displays: "No beginner exercises found for [Movement Pattern]"
- **And** a fallback suggestion appears: "Try browsing [Related Movement Pattern] instead"
- **And** the UI does not crash or freeze

---

## 🆔 US-HT-PLAN-03: Build and Save a Weekly Workout Plan in <5 Minutes

**PRD Reference:** Feature 1 — "Clear direction on what to do each day (no wasted time guessing)"

**Story ID:** `US-HT-PLAN-03`

**User Story:**
- **As a** Workout Newbie
- **I want to** create a complete weekly workout plan (select frequency, assign exercises, set reps/sets) in <5 minutes
- **So that** I have a structured commitment that I can start immediately

#### Acceptance Criteria:

**`AC-HT-PLAN-03-01` Happy Path: Complete plan creation flow and save**
- **Given** a user is on the plan wizard after selecting frequency (3 days/week)
- **When** they select exercises for Monday, Wednesday, Friday (3 exercises each)
- **And** the system pre-fills beginner defaults (3 sets × 8 reps for most exercises)
- **And** they review the weekly layout showing all 9 assigned exercises
- **And** they tap "Save My Plan"
- **Then** a Workout record is persisted to the database with:
  - user_id, plan_name, frequency, scheduled_dates (Mon/Wed/Fri), created_at
- **And** the plan appears on the user's home screen immediately
- **And** the home screen shows "Your Week: Monday, Wednesday, Friday - 9 exercises total"
- **And** a streak counter initializes to 0

**`AC-HT-PLAN-03-02` Fast-Test Mode: Plan save operation completes in <500ms**
- **Given** the application is running with `ENVIRONMENT=test` and plan creation data is staged
- **When** the user taps "Save My Plan"
- **Then** the save operation (database INSERT + home screen state update) completes in <500ms
- **And** the state mutation (current_user.active_plan_id = <new_plan_id>) is applied atomically
- **And** no pending sync queues or async operations block the confirmation

**`AC-HT-PLAN-03-03` Boundary Condition: User cancels plan creation mid-flow**
- **Given** a user has selected exercises but not yet saved
- **When** they tap "Cancel" or navigate away
- **Then** all unsaved selections are discarded (no partial plan created)
- **And** if they re-enter the wizard, it starts fresh (no auto-recovery of prior selections)
- **And** no orphaned Workout records are created in the database

---

---

# FEATURE: Quick-Log Interface (Minimal Friction)

## 🆔 US-HT-QUICK-01: Log Completed Workout in <2 Minutes for Newbies

**PRD Reference:** Feature 2 — "Logging takes too long and kills post-workout momentum"

**Story ID:** `US-HT-QUICK-01`

**User Story:**
- **As a** Workout Newbie
- **I want to** log my completed workout in a single-screen experience with minimal data entry
- **So that** I capture proof of my workout without interrupting my post-gym state

#### Acceptance Criteria:

**`AC-HT-QUICK-01-01` Happy Path: Quick-log completed 5-exercise workout in <2 minutes**
- **Given** a user has completed their planned workout and opens the app
- **When** they tap "Log Workout"
- **Then** the app displays a quick-log screen with:
  - Exercise name (pre-filled from the plan)
  - Input fields: Sets, Reps, Weight (optional), Notes (optional)
  - "Next Exercise" button to move to the next exercise
- **And** they enter: 3 sets, 5 reps for Exercise 1, then tap "Next Exercise"
- **And** they repeat for exercises 2-5
- **And** after the final exercise, they tap "Save Workout"
- **Then** the entire process (5 exercises logged) completes in <2 minutes
- **And** a LoggedWorkout record is created with:
  - user_id, plan_id, date, mode="quick", 5 LoggedExercise records
- **And** the home screen shows a green checkmark for today's workout

**`AC-HT-QUICK-01-02` Fast-Test Mode: Save operation under 500ms with compress test timers**
- **Given** the app is running with `ENVIRONMENT=test` and a quick-log is staged
- **When** the user taps "Save Workout"
- **Then** the save operation completes in <500ms
- **And** any post-workout timer states (e.g., rest_timer_seconds) are compressed to 1 second (not the production default)
- **And** the state mutation (logged_workouts.push(new_log)) is applied atomically
- **And** the home screen updates without additional round-trips

**`AC-HT-QUICK-01-03` Boundary Condition: User logs with missing required fields**
- **Given** a user enters Exercise 1 but leaves Weight blank
- **When** they tap "Next Exercise"
- **Then** the app accepts the entry (Weight is optional for beginners)
- **And** the LoggedExercise record is created with weight=null
- **When** they reach the final exercise and it also has weight=null
- **Then** they can still save (the validation does not block)
- **And** a note appears: "Some exercises are missing weight data. You can add it later."

---

## 🆔 US-HT-QUICK-02: Log Detailed Metrics (RPE, Notes) for Gym Rats

**PRD Reference:** Feature 2 — "Granular data (RPE, velocity, fatigue)" + "Manual export friction"

**Story ID:** `US-HT-QUICK-02`

**User Story:**
- **As a** Gym Rat
- **I want to** capture RPE (Rate of Perceived Exertion), detailed notes, and weight/reps for each exercise during logging
- **So that** I have granular data to analyze trends without needing to export to external tools

#### Acceptance Criteria:

**`AC-HT-QUICK-02-01` Happy Path: Log detailed metrics including RPE and notes**
- **Given** a gym rat is on the quick-log screen for Exercise 1
- **When** they enter:
  - Sets: 5
  - Reps: 5
  - Weight: 225 lbs
  - RPE: 8 (on a 1-10 scale)
  - Notes: "felt strong, good bar speed"
- **And** they tap "Next Exercise"
- **Then** a LoggedExercise record is created with all fields:
  - sets_completed=5, reps_completed=5, weight_used=225, rpe=8, notes="felt strong, good bar speed"
- **And** when they save the complete workout, all metrics are persisted
- **And** the metrics are immediately available in the Analytics dashboard

**`AC-HT-QUICK-02-02` Fast-Test Mode: RPE input and notes field render without latency**
- **Given** the app is running with `ENVIRONMENT=test`
- **When** a gym rat navigates to the RPE input field
- **Then** the field is interactive and accepts numeric input (1-10) in <100ms
- **And** the notes text field accepts text input without debounce latency
- **And** no character limit is enforced during input (validation happens at save time)

**`AC-HT-QUICK-02-03` Boundary Condition: User enters invalid RPE (e.g., RPE=15)**
- **Given** a user attempts to enter RPE=15 (outside the 1-10 range)
- **When** they tap "Next Exercise"
- **Then** the field shows an error: "RPE must be between 1-10"
- **And** the entry is not saved until corrected
- **And** RPE=null is accepted (field is optional for those not tracking it)

---

---

# FEATURE: Progress & Performance Dashboard

## 🆔 US-HT-DASH-01: View Weekly Workout Completion Percentage (Newbie)

**PRD Reference:** Feature 3 — "See visible progress week over week to stay motivated"

**Story ID:** `US-HT-DASH-01`

**User Story:**
- **As a** Workout Newbie
- **I want to** see my weekly completion percentage (e.g., "3 of 3 workouts completed")
- **So that** I stay motivated by visible progress and accountability

#### Acceptance Criteria:

**`AC-HT-DASH-01-01` Happy Path: Display weekly completion percentage with visual affirmation**
- **Given** a user has completed 2 of 3 planned workouts this week
- **When** they open the Dashboard tab
- **Then** the Beginner View displays:
  - "This Week: 2 of 3 Completed" (66%)
  - A progress bar showing 2/3 filled
  - A green checkmark next to completed workout days
  - A message: "1 more to go to complete your week!"
- **And** when they complete the 3rd workout and refresh, the display updates to:
  - "This Week: 3 of 3 Completed" (100%)
  - A celebration message: "🎉 Week Complete! Streak: 1 week"
- **And** the CompletionStreak counter increments by 1

**`AC-HT-DASH-01-02` Fast-Test Mode: Dashboard renders completion data in <1 second**
- **Given** the app is running with `ENVIRONMENT=test` and a dashboard page is requested
- **When** the dashboard loads for a user with 2 completed workouts
- **Then** the page renders the completion percentage in <1 second
- **And** no real-time data sync blocks the initial render
- **And** the progress bar animation (if any) completes in <300ms

**`AC-HT-DASH-01-03` Boundary Condition: User with zero completed workouts this week**
- **Given** a user is viewing the dashboard on Monday of a new week with no completed workouts yet
- **When** the page loads
- **Then** the display shows: "This Week: 0 of 3 Completed"
- **And** a motivational message appears: "Start your week! Complete your first workout."
- **And** the progress bar is empty (0/3)
- **And** the streak counter remains at its previous value (e.g., "Best Streak: 3 weeks")

---

## 🆔 US-HT-DASH-02: View Strength Progression Graphs (Gym Rat)

**PRD Reference:** Feature 3 — "See strength progression over time across all major lifts"

**Story ID:** `US-HT-DASH-02`

**User Story:**
- **As a** Gym Rat
- **I want to** view a line graph showing my strength progression (weight lifted) for a specific exercise over time
- **So that** I can visually confirm my progress and identify training trends

#### Acceptance Criteria:

**`AC-HT-DASH-02-01` Happy Path: Display barbell back squat progression over 3 months**
- **Given** a gym rat has logged barbell back squat 12+ times over 3 months with varying weights (205 → 235 lbs)
- **When** they open the Dashboard and select "Barbell Back Squat"
- **Then** a line graph displays:
  - X-axis: dates (from 3 months ago to today)
  - Y-axis: weight lifted (in lbs, e.g., 200-250 range)
  - Line plot: each logged session's weight as a point, connected by a line
  - Trend line: linear regression overlay showing overall progression direction
  - Max weight labeled: "Max: 235 lbs (2026-05-15)"
  - Min weight labeled: "Min: 205 lbs (2026-02-20)"
- **And** the graph is rendered and interactive (user can hover to see exact values)
- **And** the graph loads in <2 seconds

**`AC-HT-DASH-02-02` Fast-Test Mode: Graph data aggregation in <500ms**
- **Given** the app is running with `ENVIRONMENT=test` and a user has 50+ logged sessions
- **When** the graph is requested for "Barbell Back Squat"
- **Then** data aggregation (query logged exercises, calculate trend line) completes in <500ms
- **And** the line rendering (SVG or canvas) completes in <300ms
- **And** no blocking operations delay the chart display

**`AC-HT-DASH-02-03` Boundary Condition: Exercise with sparse or no data**
- **Given** a user has only logged an exercise twice over 3 months
- **When** they request a progression graph for that exercise
- **Then** the graph still renders with 2 data points connected by a line
- **And** the trend line is calculated (though confidence is low with n=2)
- **And** a note appears: "Limited data. Log more sessions to see clearer trends."
- **Given** a user requests a graph for an exercise they've never logged
- **When** they search for it in the analytics
- **Then** the system displays: "No data yet for this exercise. Start logging to track progress."

---

---

# FEATURE: Form Guidance & Education

## 🆔 US-HT-FORM-01: Access Exercise Form Descriptions and Cue Cards

**PRD Reference:** Feature 4 — "Unsure if I'm doing exercises correctly"

**Story ID:** `US-HT-FORM-01`

**User Story:**
- **As a** Workout Newbie
- **I want to** access form descriptions, step-by-step cues, and common mistake warnings for any exercise
- **So that** I understand proper technique and can perform exercises safely

#### Acceptance Criteria:

**`AC-HT-FORM-01-01` Happy Path: View complete form guidance for back squat**
- **Given** a beginner is viewing the exercise library or logging a workout with "Back Squat" listed
- **When** they tap "Back Squat"
- **Then** a form card displays:
  - **Exercise Name:** Back Squat
  - **Difficulty:** Intermediate
  - **Equipment:** Barbell, Safety Rack
  - **Target Muscles:** Quads, Glutes, Hamstrings
  - **2-Sentence Description:** "The barbell back squat is a compound lower-body exercise that builds leg strength and power. It requires careful setup and controlled descent to maximize effectiveness and minimize injury risk."
  - **Step-by-Step Cues (5 bullet points):**
    1. Position barbell on upper back, feet shoulder-width apart
    2. Tighten core and maintain neutral spine throughout
    3. Descend until thighs are parallel to ground
    4. Drive through heels to return to start position
    5. Keep chest up and eyes forward
  - **Common Mistakes & Corrections (3 bullet points):**
    1. "Mistake: Knees caving inward. Fix: Focus on driving knees outward throughout descent."
    2. "Mistake: Forward lean (upper body collapses). Fix: Strengthen core; practice goblet squats as regression."
    3. "Mistake: Partial range of motion. Fix: Lower until thighs are parallel; video your sets to check depth."
  - **Beginner-Friendly Alternative:** Goblet Squat (listed with link)
- **And** the text is readable in gym lighting (high contrast, font size ≥14px)

**`AC-HT-FORM-01-02` Fast-Test Mode: Form card loads in <200ms**
- **Given** the app is running with `ENVIRONMENT=test` and a user taps on an exercise
- **When** the form guidance lookup is triggered
- **Then** the form card renders in <200ms
- **And** no real-time validation or external API calls block the display
- **And** the card is interactive immediately upon display

**`AC-HT-FORM-01-03` Boundary Condition: Exercise with incomplete form data**
- **Given** a user requests form guidance for an exercise that has minimal data (e.g., newly added exercise)
- **When** the form card loads
- **Then** it displays all available fields (name, equipment, target muscles)
- **And** missing fields (e.g., common mistakes) show: "[Coming Soon] Form guidance for this exercise is being updated."
- **And** a link to "Suggest a form tip" appears so users can contribute
- **And** the card does not crash or freeze

---

---

# FEATURE: Advanced Analytics & Insights

## 🆔 US-HT-ANALYTICS-01: Generate Strength Progression Trends and Volume Analysis

**PRD Reference:** Feature 5 — "Data-driven insights to identify what's working and refine programming"

**Story ID:** `US-HT-ANALYTICS-01`

**User Story:**
- **As a** Gym Rat
- **I want to** view automatically calculated trends (strength progression, volume, fatigue patterns) without exporting to external tools
- **So that** I can make data-driven decisions about my training cycle and deload timing

#### Acceptance Criteria:

**`AC-HT-ANALYTICS-01-01` Happy Path: Display strength progression trend for bench press over 3 months**
- **Given** a gym rat has logged bench press 12+ times over 3 months
- **When** they open Analytics → "Strength Trends" → "Bench Press"
- **Then** the system displays:
  - **Trend Summary:** "Strength Progression: +25 lbs over 3 months (linear increase from 225 → 250 lbs)"
  - **Graph:** Line chart showing weight per session with trend overlay
  - **Volume Summary:** "Total Volume Lifted: 45,000 lbs (this month: 12,000 lbs)"
  - **Session Count:** "12 logged sessions in the selected range"
  - **RPE Pattern:** "Average RPE: 7.5/10. Range: 6-9."
  - **Insight Generated:** "Your bench press is trending up. Consider a deload week if volume exceeds 50k lbs/month to prevent overuse."
- **And** the insights are calculated automatically based on logged data

**`AC-HT-ANALYTICS-01-02` Fast-Test Mode: Trend calculation and rendering in <500ms**
- **Given** the app is running with `ENVIRONMENT=test` and analytics data is staged
- **When** an analytics view is requested for a lift with 50+ logged sessions
- **Then** trend calculation (mean, linear regression, volume aggregation) completes in <500ms
- **And** the page renders in <1 second
- **And** no blocking I/O or real-time sync operations delay the display

**`AC-HT-ANALYTICS-01-03` Boundary Condition: Declining trend (deload detection)**
- **Given** a gym rat's bench press weight has decreased over the past 2 weeks (250 → 235 lbs)
- **When** they view the trend
- **Then** the trend direction is indicated as "declining" (not "improving")
- **And** an insight appears: "Your bench press weight has decreased. This could indicate fatigue. Consider a deload week or recovery day."
- **And** the system suggests a deload if volume_per_week > 40k lbs

---

## 🆔 US-HT-ANALYTICS-02: Filter and Compare Performance Across Custom Date Ranges

**PRD Reference:** Feature 5 — "Custom date range filtering and multi-lift comparison"

**Story ID:** `US-HT-ANALYTICS-02`

**User Story:**
- **As a** Gym Rat
- **I want to** filter analytics data by custom date ranges and compare performance between two periods (e.g., January vs. April)
- **So that** I can evaluate the effectiveness of different training cycles

#### Acceptance Criteria:

**`AC-HT-ANALYTICS-02-01` Happy Path: Compare bench press performance between two months**
- **Given** a gym rat is on the Analytics page with data from Jan-Apr 2026
- **When** they tap "Date Range Filter"
- **And** they select "Period 1: January 1-31" and "Period 2: April 1-30"
- **Then** the system recalculates and displays:
  - **Period 1 Stats:** Avg weight: 225 lbs, Avg reps: 5, Total sessions: 3
  - **Period 2 Stats:** Avg weight: 245 lbs, Avg reps: 6, Total sessions: 4
  - **Improvement:** "+20 lbs avg weight, +1 rep average (9% strength gain)"
  - **Visual:** Side-by-side bar chart comparing metrics
- **And** all graphs and summaries update to reflect only data from the selected periods
- **And** the PR history adjusts to show only PRs set within the selected range

**`AC-HT-ANALYTICS-02-02` Fast-Test Mode: Date filter application in <300ms**
- **Given** the app is running with `ENVIRONMENT=test` and a date range filter is applied
- **When** the filter is submitted
- **Then** all data recalculation and re-render completes in <300ms
- **And** no multiple API round-trips block the update
- **And** the state mutation (selected_date_range = [Period1, Period2]) is applied atomically

**`AC-HT-ANALYTICS-02-03` Boundary Condition: Date range with no data**
- **Given** a user selects a date range (e.g., June 1-30) with zero logged workouts
- **When** they apply the filter
- **Then** the system displays: "No workouts logged in this date range"
- **And** the previous data is not cleared (user can see "No data for this range" message)
- **And** they can tap "Clear Filter" to revert to the full date range

---

---

# FEATURE: Flexible Plan Adaptation

## 🆔 US-HT-ADAPT-01: Swap Exercise Mid-Week and Receive Substitution Recommendations

**PRD Reference:** Feature 6 — "Hard to find substitute exercises that properly fit my training cycle"

**Story ID:** `US-HT-ADAPT-01`

**User Story:**
- **As a** Gym Rat
- **I want to** mark an exercise as unavailable and receive 2-3 smart substitute recommendations that target the same muscles with similar intensity
- **So that** I can adapt my plan when equipment is not available without derailing my training cycle

#### Acceptance Criteria:

**`AC-HT-ADAPT-01-01` Happy Path: Swap barbell squat for leg press due to unavailable rack**
- **Given** a gym rat is mid-workout and needs to complete "Barbell Back Squat"
- **When** they tap the exercise and select "Equipment unavailable"
- **Then** the system displays 2-3 substitute recommendations within 1 second:
  1. **Leg Press** (Recommended: Same muscles, barbell-free, similar intensity)
  2. **Goblet Squat** (Alternate: Lower body quad focus, minimal equipment)
  3. **Smith Machine Squat** (Alternate: Barbell alternative, easier equipment access)
- **And** each recommendation shows:
  - Exercise name, target muscles, equipment required, difficulty level
  - "Why this substitute: Targets same muscle groups (quads, glutes) with similar intensity"
- **When** they select "Leg Press"
- **Then** the app confirms: "Swapping Barbell Back Squat → Leg Press. Continue?"
- **And** when they confirm, the LoggedWorkout is updated:
  - ExerciseSwap record created: original_exercise_id=5, alternative_exercise_id=8, reason="equipment_unavailable"
  - The workout now shows [SWAPPED] tag next to the original exercise name

**`AC-HT-ADAPT-01-02` Fast-Test Mode: Substitution recommendation generation in <1 second**
- **Given** the app is running with `ENVIRONMENT=test` and a swap is requested
- **When** the recommendation algorithm runs (muscle group matching + intensity matching)
- **Then** 2-3 alternatives are returned in <1 second
- **And** no real-time API calls to external exercise databases block the response
- **And** ranking algorithm (relevance score) is deterministic and cached

**`AC-HT-ADAPT-01-03` Boundary Condition: No viable substitutes available**
- **Given** a user requests substitutes for a rare/niche exercise with no close alternatives in the library
- **When** the recommendation engine runs
- **Then** it displays: "No close alternatives found for [Exercise]"
- **And** a fallback option appears: "Create custom substitute" (user manually selects an exercise)
- **And** the system does not crash or return empty/null recommendations

---

## 🆔 US-HT-ADAPT-02: Modify Planned Workout Reps/Weight and Preserve Edit History

**PRD Reference:** Feature 6 — "Mid-week plan editing that allows users to adjust intensity"

**Story ID:** `US-HT-ADAPT-02`

**User Story:**
- **As a** Gym Rat
- **I want to** quickly modify reps/weight for a planned exercise before or during my workout
- **So that** I can adjust intensity on the fly while maintaining a clear record of planned vs. actual data

#### Acceptance Criteria:

**`AC-HT-ADAPT-02-01` Happy Path: Modify planned bench press weight and save**
- **Given** a gym rat's plan specifies "Bench Press 5x5 @ 225 lbs"
- **When** they open the plan and tap the exercise
- **And** they change the weight to 230 lbs (they feel stronger today)
- **And** they tap "Save Changes"
- **Then** the plan is updated with weight=230 lbs
- **And** the home screen now shows: "Bench Press 5x5 @ 230 lbs"
- **And** when they complete the workout and log "actual" data, the system calculates:
  - Planned: 5x5 @ 225 lbs
  - Actual: 5x5 @ 230 lbs
  - Delta: +5 lbs
- **And** the delta is displayed in the logged workout for comparison

**`AC-HT-ADAPT-02-02` Fast-Test Mode: Plan modification save in <200ms**
- **Given** the app is running with `ENVIRONMENT=test` and a weight modification is staged
- **When** the user taps "Save Changes"
- **Then** the Workout record is updated (weight field) in <200ms
- **And** the state mutation is atomic (no partial updates)
- **And** the home screen reflectsupdated plan data without additional queries

**`AC-HT-ADAPT-02-03` Boundary Condition: User modifies plan after workout has started**
- **Given** a user's workout has started (they've logged 2 of 4 exercises)
- **When** they attempt to modify a future exercise in the plan
- **Then** the modification is allowed (allows mid-workout adjustments)
- **And** the system logs a timestamp of when the modification occurred
- **And** the audit trail shows: "Modified Exercise 3 weight at 2026-05-20 14:35:22"

---

---

## Open Questions & Gaps

### From Original PRD — Deferred to Future Phases

1. **Form video/animation:** Text + cue cards are MVP. Video demonstrations are deferred to post-launch.
2. **Social/sharing features:** Deferred; focus on individual tracking first.
3. **Wearable integration:** Deferred; manual logging is MVP.
4. **Periodization templates:** Deferred; evaluate post-launch demand.
5. **Pricing model:** To be determined during business planning phase.
6. **Exercise database strategy:** Build vs. partner decision deferred to tech design.
7. **Gym Rat segmentation:** Conduct post-launch interviews to identify specific sub-segments.
8. **Beginner retention curve:** Monitor cohort analytics post-launch.

### Test-Driven Gaps Identified During Story Expansion

1. **Edit window for logged workouts:** Can users edit forever, or only within 24 hours? Define post-launch.
2. **Streak grace period:** If a user misses a day, does streak break immediately or after a 1-day grace period? Define in phase 2.
3. **Offline sync ordering:** When a user logs multiple workouts offline, what order do they sync? Define sync queue strategy.
4. **Duplicate prevention:** If a user logs the same workout twice (network error), prevent duplicates. Define deduplication logic.
5. **Data export formats:** MVP supports CSV. PDF and integration with MyFitnessPal are future features.

---

## Requirement Traceability Matrix

| User Story ID | Feature | User Role | PRD Reference | Acceptance Criteria Count | Status |
|---|---|---|---|---|---|
| US-HT-PLAN-01 | Smart Workout Planning | Newbie | Feature 1 | 3 | ✓ Complete |
| US-HT-PLAN-02 | Smart Workout Planning | Newbie | Feature 1 | 3 | ✓ Complete |
| US-HT-PLAN-03 | Smart Workout Planning | Newbie | Feature 1 | 3 | ✓ Complete |
| US-HT-QUICK-01 | Quick-Log Interface | Newbie | Feature 2 | 3 | ✓ Complete |
| US-HT-QUICK-02 | Quick-Log Interface | Gym Rat | Feature 2 | 3 | ✓ Complete |
| US-HT-DASH-01 | Progress Dashboard | Newbie | Feature 3 | 3 | ✓ Complete |
| US-HT-DASH-02 | Progress Dashboard | Gym Rat | Feature 3 | 3 | ✓ Complete |
| US-HT-FORM-01 | Form Guidance | Newbie | Feature 4 | 3 | ✓ Complete |
| US-HT-ANALYTICS-01 | Advanced Analytics | Gym Rat | Feature 5 | 3 | ✓ Complete |
| US-HT-ANALYTICS-02 | Advanced Analytics | Gym Rat | Feature 5 | 3 | ✓ Complete |
| US-HT-ADAPT-01 | Flexible Plan Adaptation | Gym Rat | Feature 6 | 3 | ✓ Complete |
| US-HT-ADAPT-02 | Flexible Plan Adaptation | Gym Rat | Feature 6 | 3 | ✓ Complete |

**Summary:** 12 user stories, 36 acceptance criteria (3 per story), 100% feature coverage.

---

**Document Version:** 1.0  
**Status:** Ready for Development  
**Next Phase:** Technical architecture + test plan generation
