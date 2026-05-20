User Stories & Acceptance Criteria: Feature 1
🗺️ Traceability Mapping
PRD Source: Feature 1: Guided Workout Plan Builder (Blake's PRD)

User Story Tracking: US-HT-PLAN-01, US-HT-PLAN-02

Test Case Mapping Target: TC-HT-PLAN-XX-YY (Andrei's Tests)

🆔 Story 1: Frequency & Goal Questionnaire
Requirement Reference: Feature 1 - Functional Requirement 1 & 6

Solves Pain: Newbie doesn't know how many days a week to work out.

US-HT-PLAN-01
As a fitness newbie setting up my routine,

I want to complete a brief guidance questionnaire about my experience level, goals, and weekly time availability,

So that the app can recommend a clear, appropriate workout frequency without making me guess.

AC-HT-PLAN-01-01 (Questionnaire Input)

Given a user opens the Guided Workout Plan Builder.

When they navigate the questionnaire.

Then they must be able to input their fitness level (Beginner/Intermediate/Advanced), available days per week (1–7), and main goal (Build Strength/Lose Weight/Improve Endurance).

AC-HT-PLAN-01-02 (Contextual Guidance Output)

Given a user has selected "Beginner" and "3 days per week" in the questionnaire.

When they submit their answers.

Then the app must display a summary screen explaining why a 3-day split is ideal for a beginner.

And provide a direct action button to view matching templates.

🆔 Story 2: Curated Beginner Templates
Requirement Reference: Feature 1 - Functional Requirement 3 & 4

Solves Pain: Newbie is overwhelmed choosing exercises.

US-HT-PLAN-02
As a fitness newbie looking for day-to-day direction,

I want to select a pre-filled weekly workout template based on my questionnaire recommendations,

So that I have an instant, structured plan containing appropriate exercises, sets, and reps.

AC-HT-PLAN-02-01 (Template Selection & Preview)

Given the user is viewing recommended templates.

When they tap on the "Full Body 3x/week" beginner template.

Then the app must display a preview screen showing a 3-day calendar layout (e.g., Monday, Wednesday, Friday).

And each day must display pre-filled, beginner-appropriate exercises (e.g., Goblet Squats instead of heavy Barbell Back Squats).

AC-HT-PLAN-02-02 (Plan Activation)

Given a user is previewing a pre-filled beginner template.

When they tap the "Save and Create Plan" button.

Then the app must instantiate this schedule into their active calendar view.

And set all initial exercise tracking variables to default baseline weights (e.g., bodyweight or empty bar).