# Unit Converter: User Stories & Acceptance Criteria

---

## 🆔 US-UC-US-001: Browse Units by Category (Casual Converter)
- **PRD Reference:** Feature: Unit Selection & Search – Functional Requirement: "Display unit categories"
- **Story ID:** `US-UC-US-001`

**User Story:**
- **As a** Casual Converter
- **I want to** browse units organized by category (length, weight, volume, temperature)
- **So that** I can quickly find common units without searching

#### Acceptance Criteria:

- **`AC-UC-US-001-01` Display preset unit categories on app launch**
  - **Given** the application is launched for the first time
  - **When** the unit selection interface loads
  - **Then** a minimum of 5 unit categories are displayed: length, mass, volume, temperature, area
  - **And** each category displays a human-readable label (not code identifiers)

- **`AC-UC-US-001-02` Browse units within a selected category**
  - **Given** the unit selection interface displays available categories
  - **When** the user selects the "length" category
  - **Then** a list of length units is displayed (meter, kilometer, mile, foot, inch, centimeter, millimeter, etc.)
  - **And** each unit displays both full name and symbol (e.g., "meter (m)")

- **`AC-UC-US-001-03` Display common units first for casual users**
  - **Given** a category is selected (e.g., volume)
  - **When** the unit list loads
  - **Then** the most frequently used units appear first in the list (cups, milliliters, liters)
  - **And** specialized units (microliters, gallons) appear lower in the list

---

## 🆔 US-UC-US-002: Search Units by Name or Abbreviation (Casual Converter)
- **PRD Reference:** Feature: Unit Selection & Search – Functional Requirement: "Provide search functionality"
- **Story ID:** `US-UC-US-002`

**User Story:**
- **As a** Casual Converter
- **I want to** search for units by name or abbreviation (e.g., "mm", "millimeter")
- **So that** I can find specific units quickly without browsing categories

#### Acceptance Criteria:

- **`AC-UC-US-002-01` Search returns results within performance threshold**
  - **Given** the search field is active and focused
  - **When** the user types "mm"
  - **Then** search results are displayed within 100ms
  - **And** the result set includes "millimeter" as the first match

- **`AC-UC-US-002-02` Search handles both full names and abbreviations**
  - **Given** the search field contains "ml"
  - **When** the user initiates search
  - **Then** results include "milliliter" (full name match)
  - **And** results include all units with "ml" as abbreviation

- **`AC-UC-US-002-03` Search handles partial matches**
  - **Given** the search field contains "kilo"
  - **When** search executes
  - **Then** results include "kilogram", "kilometer", "kilopascal"
  - **And** results are ordered by match relevance (exact matches before partial)

- **`AC-UC-US-002-04` Search handles typos gracefully**
  - **Given** the search field contains "milimter" (missing 'l')
  - **When** search executes
  - **Then** "millimeter" is suggested or returned in results
  - **And** no error message is displayed

- **`AC-UC-US-002-05` Empty search returns all units**
  - **Given** the search field is active but empty
  - **When** search initializes
  - **Then** all units from all categories are displayed
  - **And** common units are ordered first (by frequency of use)

---

## 🆔 US-UC-US-003: Access Specialized Units (Power User)
- **PRD Reference:** Feature: Unit Selection & Search – Functional Requirement: "Access units beyond common categories"
- **Story ID:** `US-UC-US-003`

**User Story:**
- **As a** Power User
- **I want to** access specialized unit categories (pressure, energy, viscosity, flow rate) 
- **So that** I can work with industry-standard conversions in my domain

#### Acceptance Criteria:

- **`AC-UC-US-003-01` Display specialized categories in expanded unit menu**
  - **Given** the user toggles "Show All Categories" or similar option
  - **When** the unit category list expands
  - **Then** at least 10 categories are displayed including: pressure, energy, force, viscosity, flow rate, density, angle, frequency, power, torque
  - **And** each category is labeled with full name and abbreviation context

- **`AC-UC-US-003-02` Specialized units are available via search**
  - **Given** the user searches for "Pascal"
  - **When** search executes
  - **Then** "pascal (Pa)" is returned as the top result
  - **And** related pressure units (kilopascal, bar, psi) are included in results

- **`AC-UC-US-003-03` Display conversion factors for reference**
  - **Given** a specialized unit is selected or displayed in search results
  - **When** the user views unit details
  - **Then** the conversion factor relative to SI base unit is displayed (e.g., "1 bar = 100,000 Pa")
  - **And** this reference is visible without clicking into a details view

---

## 🆔 US-UC-US-004: Enter Value and See Instant Conversion (Casual Converter)
- **PRD Reference:** Feature: Instant Conversion & Value Input – Functional Requirement: "Accept numeric input" and "Display conversion result in real-time"
- **Story ID:** `US-UC-US-004`

**User Story:**
- **As a** Casual Converter
- **I want to** enter a numeric value and see the conversion result instantly
- **So that** I can convert units without delay or additional steps

#### Acceptance Criteria:

- **`AC-UC-US-004-01` Display conversion result in real-time as user types**
  - **Given** source and target units are selected (e.g., cups → milliliters)
  - **When** the user types "2" in the source value field
  - **Then** the target value field displays "473.176" (or similar) within 100ms of the keystroke
  - **And** the result updates with each subsequent digit typed

- **`AC-UC-US-004-02` Support decimal input**
  - **Given** the source value field is active
  - **When** the user enters "2.5"
  - **Then** the conversion result displays as "591.471" (2.5 cups in ml)
  - **And** no input error is shown

- **`AC-UC-US-004-03` Support integer input**
  - **Given** the source value field is active
  - **When** the user enters "10"
  - **Then** the conversion result displays as "2365.882" (10 cups in ml)
  - **And** decimal places are shown to 3 places by default

- **`AC-UC-US-004-04` Reject invalid characters gracefully**
  - **Given** the source value field is active
  - **When** the user types "abc"
  - **Then** the characters are not displayed in the field (or invalid character is rejected)
  - **And** no error message appears; field remains ready for valid input

- **`AC-UC-US-004-05` Handle empty input without error**
  - **Given** the source value field contains "5"
  - **When** the user clears the field (deletes all characters)
  - **Then** the target value field displays empty or "0" depending on design
  - **And** no error or validation message is displayed

---

## 🆔 US-UC-US-005: Swap Source and Target Units (Casual Converter)
- **PRD Reference:** Feature: Instant Conversion & Value Input – Functional Requirement: "Allow users to swap source and target units"
- **Story ID:** `US-UC-US-005`

**User Story:**
- **As a** Casual Converter
- **I want to** swap source and target units with a single action
- **So that** I can quickly convert in the opposite direction without re-selecting units

#### Acceptance Criteria:

- **`AC-UC-US-005-01` Swap button exchanges units and values**
  - **Given** source unit is "cups", target unit is "milliliters", source value is "2"
  - **When** the user clicks the "swap" button (↔ icon)
  - **Then** source unit becomes "milliliters", target unit becomes "cups"
  - **And** source value field displays "473.176" (the previous result)
  - **And** target value field displays "2" (the previous input)

- **`AC-UC-US-005-02` Swap preserves decimal precision during swap**
  - **Given** source unit is "kilometers", target unit is "miles", source value is "1.5"
  - **When** user clicks swap
  - **Then** source unit is "miles", target unit is "kilometers", source value is "0.932056" (rounded)
  - **And** target value field displays "1.5"

- **`AC-UC-US-005-03` Swap is single action (no confirmation)**
  - **Given** the swap button is visible in the UI
  - **When** user clicks the swap button
  - **Then** the action completes in < 200ms
  - **And** no confirmation dialog appears

---

## 🆔 US-UC-US-006: Handle Large and Small Numbers (Power User)
- **PRD Reference:** Feature: Instant Conversion & Value Input – Non-Functional Requirement: "Support input of very large numbers (up to 10^15) and very small numbers (down to 10^-15)"
- **Story ID:** `US-UC-US-006`

**User Story:**
- **As a** Power User
- **I want to** input very large and very small numbers in scientific notation
- **So that** I can perform conversions across many orders of magnitude

#### Acceptance Criteria:

- **`AC-UC-US-006-01` Accept and convert scientific notation**
  - **Given** source unit is "meters", target unit is "nanometers"
  - **When** user enters "1.5e-6" (1.5 micrometers)
  - **Then** target value displays "1500" (nanometers)
  - **And** calculation completes in < 10ms

- **`AC-UC-US-006-02` Display very large results in scientific notation**
  - **Given** source unit is "meters", target unit is "millimeters"
  - **When** user enters "1e15" (1 quadrillion meters)
  - **Then** target value displays as "1e+18" or "1.0e18" (in scientific notation)
  - **And** value is mathematically correct to floating-point precision

- **`AC-UC-US-006-03` Handle very small results with precision**
  - **Given** source unit is "millimeters", target unit is "meters"
  - **When** user enters "0.001"
  - **Then** target value displays as "0.000001" or "1e-6" (depending on precision setting)
  - **And** no underflow or rounding error occurs

- **`AC-UC-US-006-04` Support input of numbers from 10^-15 to 10^15**
  - **Given** the source value field accepts numeric input
  - **When** user enters "1e-15" (smallest supported)
  - **Then** the conversion executes without error
  - **And** when user enters "9.99e15" (largest supported)
  - **Then** the conversion executes without error
  - **And** no overflow or underflow is triggered

---

## 🆔 US-UC-US-007: Save Favorite Unit Pair (Casual Converter)
- **PRD Reference:** Feature: Favorites & Quick Access – Functional Requirement: "Allow users to save current source/target unit pair as a favorite"
- **Story ID:** `US-UC-US-007`

**User Story:**
- **As a** Casual Converter
- **I want to** save a unit pair (e.g., cups ↔ milliliters) as a favorite
- **So that** I can reuse this conversion without re-selecting units

#### Acceptance Criteria:

- **`AC-UC-US-007-01` Save favorite from current unit selection**
  - **Given** source unit is "cups", target unit is "milliliters"
  - **When** user clicks "Save as Favorite" or similar action
  - **Then** a confirmation message displays (e.g., "Saved: cups ↔ ml")
  - **And** the favorite is stored in local storage

- **`AC-UC-US-007-02` Prevent duplicate favorites**
  - **Given** "cups ↔ milliliters" is already saved as a favorite
  - **When** user attempts to save the same pair again
  - **Then** a warning message displays (e.g., "Already saved as favorite")
  - **And** no duplicate entry is created

- **`AC-UC-US-007-03` Favorite persists across app sessions**
  - **Given** "cups ↔ milliliters" is saved as a favorite
  - **When** the user closes and reopens the app
  - **Then** the favorite still exists in the favorites list
  - **And** the favorite data is retrieved from local storage on app start

- **`AC-UC-US-007-04` Display confirmation with favorite save**
  - **Given** user clicks "Save as Favorite"
  - **When** the favorite is created
  - **Then** a visual confirmation (toast, checkmark, or success message) displays for 2-3 seconds
  - **And** confirmation disappears without user action

---

## 🆔 US-UC-US-008: Access Favorites Panel (Casual Converter)
- **PRD Reference:** Feature: Favorites & Quick Access – Functional Requirement: "Display saved favorites in a dedicated section/tab"
- **Story ID:** `US-UC-US-008`

**User Story:**
- **As a** Casual Converter
- **I want to** access my saved favorites in a dedicated panel
- **So that** I can quickly reuse frequent conversions with one tap

#### Acceptance Criteria:

- **`AC-UC-US-008-01` Display favorites panel on app load**
  - **Given** the app launches and user has saved favorites
  - **When** the app loads
  - **Then** a "Favorites" tab or panel is visible at the top of the interface
  - **And** the number of saved favorites is displayed (e.g., "Favorites (3)")

- **`AC-UC-US-008-02` Tap favorite to load conversion pair**
  - **Given** the Favorites panel displays "cups ↔ ml"
  - **When** user taps this favorite
  - **Then** source unit becomes "cups", target unit becomes "ml" in the conversion interface
  - **And** any previous value in the source field is cleared

- **`AC-UC-US-008-03` Display system-default favorites**
  - **Given** the Favorites panel is open and user has no saved favorites
  - **When** the app loads
  - **Then** system-provided favorites are displayed: "cups ↔ ml", "°F ↔ °C", "miles ↔ km"
  - **And** system favorites are labeled as "Default" or visually distinguished from user favorites

- **`AC-UC-US-008-04` Show usage count for each favorite**
  - **Given** a favorite is displayed in the Favorites panel
  - **When** the panel loads
  - **Then** a usage count is shown (e.g., "cups ↔ ml (Used 5 times)")
  - **And** the count is updated each time the favorite is used

---

## 🆔 US-UC-US-009: Reorder and Delete Favorites (Power User)
- **PRD Reference:** Feature: Favorites & Quick Access – Functional Requirement: "Allow users to reorder, rename, and delete favorites"
- **Story ID:** `US-UC-US-009`

**User Story:**
- **As a** Power User
- **I want to** reorder, rename, and delete my saved favorites
- **So that** I can organize my frequently used conversions by priority and maintain only relevant pairs

#### Acceptance Criteria:

- **`AC-UC-US-009-01` Reorder favorites by drag-and-drop**
  - **Given** Favorites panel displays at least 3 favorites
  - **When** user drags "pressure-psi ↔ pascal" from position 3 to position 1
  - **Then** the favorite moves to position 1 immediately
  - **And** the new order persists when app is closed and reopened

- **`AC-UC-US-009-02` Delete favorite with confirmation**
  - **Given** Favorites panel is displayed
  - **When** user clicks the "delete" button (trash icon) on a favorite
  - **Then** a confirmation dialog appears: "Delete 'cups ↔ ml'?"
  - **And** options "Delete" and "Cancel" are presented

- **`AC-UC-US-009-03` Confirm deletion removes favorite**
  - **Given** deletion confirmation dialog is displayed
  - **When** user clicks "Delete"
  - **Then** the favorite is removed from the list immediately
  - **And** the favorite is no longer available when app is reopened

- **`AC-UC-US-009-04` Rename favorite with custom label**
  - **Given** user right-clicks (or long-presses) a favorite
  - **When** a context menu or edit dialog appears
  - **Then** user can enter a custom name (e.g., "My Cooking Conversion")
  - **And** the custom name is displayed instead of the default "cups ↔ ml"

- **`AC-UC-US-009-05` Cannot delete system-default favorites**
  - **Given** Favorites panel is displayed with system-default favorite "cups ↔ ml"
  - **When** user attempts to delete the system-default favorite
  - **Then** the delete button is disabled or hidden
  - **And** a tooltip explains "Default favorites cannot be deleted"

---

## 🆔 US-UC-US-010: View Recent Conversions (Casual Converter)
- **PRD Reference:** Feature: Conversion History & Timestamps – Functional Requirement: "Display conversion history in reverse chronological order"
- **Story ID:** `US-UC-US-010`

**User Story:**
- **As a** Casual Converter
- **I want to** view a list of my recent conversions with timestamps
- **So that** I can refer back to conversions I made moments ago

#### Acceptance Criteria:

- **`AC-UC-US-010-01` Display history panel with recent conversions**
  - **Given** user has performed at least 3 conversions
  - **When** user opens the "History" tab
  - **Then** a list of conversions is displayed in reverse chronological order (most recent first)
  - **And** each entry shows: source value, source unit, target value, target unit, timestamp

- **`AC-UC-US-010-02` Show timestamp for each conversion**
  - **Given** History panel is displayed
  - **When** user views a history entry
  - **Then** timestamp is displayed in human-readable format (e.g., "2:45 PM" or "2 minutes ago")
  - **And** timestamp is in the user's local timezone

- **`AC-UC-US-010-03` Limit default history view to 50 entries**
  - **Given** user has performed 100+ conversions
  - **When** History panel opens
  - **Then** only the most recent 50 conversions are displayed by default
  - **And** a "Load More" or pagination button allows access to older entries

- **`AC-UC-US-010-04` Tap history entry to reload conversion**
  - **Given** History panel displays a past conversion entry
  - **When** user taps "2 cups → 473.176 ml (5:30 PM)"
  - **Then** source unit becomes "cups", target unit becomes "ml"
  - **And** source value field is populated with "2"
  - **And** target value field displays "473.176"

- **`AC-UC-US-010-05` History persists across app sessions**
  - **Given** user has 10 conversions in history
  - **When** user closes and reopens the app
  - **Then** all 10 conversions are still visible in History panel
  - **And** history data is retrieved from local storage

---

## 🆔 US-UC-US-011: Clear Conversion History (Casual Converter)
- **PRD Reference:** Feature: Conversion History & Timestamps – Functional Requirement: "Provide a 'clear history' option"
- **Story ID:** `US-UC-US-011`

**User Story:**
- **As a** Casual Converter
- **I want to** clear my conversion history
- **So that** I can delete old or irrelevant conversion records

#### Acceptance Criteria:

- **`AC-UC-US-011-01` Access clear history option**
  - **Given** History panel is displayed
  - **When** user opens History settings or options menu
  - **Then** a "Clear History" button or option is visible
  - **And** the button is clearly labeled

- **`AC-UC-US-011-02` Require confirmation before clearing**
  - **Given** user clicks "Clear History"
  - **When** a confirmation dialog appears
  - **Then** it displays "Clear all conversions? This cannot be undone."
  - **And** options "Clear" and "Cancel" are presented

- **`AC-UC-US-011-03` Clear all history on confirmation**
  - **Given** confirmation dialog is displayed
  - **When** user clicks "Clear"
  - **Then** all history entries are deleted immediately
  - **And** History panel displays empty (e.g., "No conversions yet")

- **`AC-UC-US-011-04` History remains cleared after app restart**
  - **Given** history has been cleared
  - **When** user closes and reopens the app
  - **Then** History panel still displays empty
  - **And** no previous history entries are recovered

---

## 🆔 US-UC-US-012: Export Conversion History (Power User)
- **PRD Reference:** Feature: Conversion History & Timestamps – Functional Requirement: "Support exporting history as CSV or JSON"
- **Story ID:** `US-UC-US-012`

**User Story:**
- **As a** Power User
- **I want to** export my conversion history as CSV or JSON
- **So that** I can document or analyze conversions for technical records

#### Acceptance Criteria:

- **`AC-UC-US-012-01` Export history as CSV**
  - **Given** History panel is displayed with at least 1 conversion
  - **When** user clicks "Export as CSV"
  - **Then** a CSV file is generated and downloaded with filename "conversion-history.csv"
  - **And** CSV headers are: "Timestamp,Source Value,Source Unit,Target Value,Target Unit"
  - **And** each row contains one conversion record

- **`AC-UC-US-012-02` Export history as JSON**
  - **Given** History panel is displayed
  - **When** user clicks "Export as JSON"
  - **Then** a JSON file is generated with structure: `[{timestamp: "...", sourceValue: ..., sourceUnit: "...", targetValue: ..., targetUnit: "..."}, ...]`
  - **And** file is named "conversion-history.json"

- **`AC-UC-US-012-03` Export includes all historical records**
  - **Given** user has 500 conversions in history (beyond 50-entry default view)
  - **When** user exports history
  - **Then** all 500 conversions are included in the export (not just the visible 50)

- **`AC-UC-US-012-04` File download completes within 1 second**
  - **Given** user initiates export
  - **When** export function executes
  - **Then** file download begins within 1000ms
  - **And** no timeout or error occurs for histories up to 10,000 entries

---

## 🆔 US-UC-US-013: Filter History by Date Range (Power User)
- **PRD Reference:** Feature: Conversion History & Timestamps – Functional Requirement: "Add search/filter by date range"
- **Story ID:** `US-UC-US-013`

**User Story:**
- **As a** Power User
- **I want to** filter my conversion history by date range
- **So that** I can focus on conversions from a specific time period

#### Acceptance Criteria:

- **`AC-UC-US-013-01` Access filter/search options in History panel**
  - **Given** History panel is open
  - **When** user clicks "Filter" or "Search" button
  - **Then** a filter panel or modal appears with options: "Date From", "Date To"
  - **And** date pickers or text input fields are provided

- **`AC-UC-US-013-02` Filter history by date range**
  - **Given** filter panel shows date pickers
  - **When** user selects "From: 2026-05-15, To: 2026-05-20"
  - **Then** History panel displays only conversions within that date range
  - **And** filtering completes in < 500ms

- **`AC-UC-US-013-03` Display filtered count**
  - **Given** history is filtered by date range
  - **When** filter results are displayed
  - **Then** a count is shown (e.g., "Showing 23 of 150 conversions")
  - **And** user can clear filter to see all history again

---

## 🆔 US-UC-US-014: Conversions Work Without Internet (All Users)
- **PRD Reference:** Feature: Offline Functionality – Functional Requirement: "Pre-bundle all unit conversion data" and "All unit categories and conversions offline"
- **Story ID:** `US-UC-US-014`

**User Story:**
- **As a** User (both Casual and Power)
- **I want to** perform conversions when the app is offline or has no internet connection
- **So that** I can use the unit converter anytime, anywhere, without dependency on network connectivity

#### Acceptance Criteria:

- **`AC-UC-US-014-01` All units bundled in app on first launch**
  - **Given** the app is downloaded and installed
  - **When** the app launches for the first time
  - **Then** all unit conversion data is available locally (no network call required)
  - **And** no "Loading units..." message or delay occurs

- **`AC-UC-US-014-02` Conversions work when internet is disconnected**
  - **Given** all unit data is loaded and internet is disabled (airplane mode)
  - **When** user performs a conversion (e.g., 5 miles → kilometers)
  - **Then** the conversion executes successfully and displays the result
  - **And** no error message about network connectivity is shown

- **`AC-UC-US-014-03` Offline indicator is optional or absent**
  - **Given** the app is functioning in offline mode
  - **When** the user interacts with the interface
  - **Then** no persistent "Offline" banner or indicator is displayed
  - **And** the app functions normally without visual distinction

- **`AC-UC-US-014-04` No performance penalty for offline vs. online**
  - **Given** user performs 10 conversions in offline mode
  - **When** each conversion completes
  - **Then** average conversion time is < 10ms (same as online performance)
  - **And** no latency or slowdown is introduced by offline operation

- **`AC-UC-US-014-05` Unit database survives app reinstall (v2 or cloud sync)**
  - **Given** user uninstalls and reinstalls the app
  - **When** the app launches
  - **Then** the unit database loads with no internet call required
  - **And** app bundle includes full unit data (no external download needed)

---

## 🆔 US-UC-US-015: Set Custom Decimal Precision (Power User)
- **PRD Reference:** Feature: Precision & Decimal Place Control – Functional Requirement: "Allow users to set custom decimal places"
- **Story ID:** `US-UC-US-015`

**User Story:**
- **As a** Power User
- **I want to** set the number of decimal places for conversion results
- **So that** I can control precision to match my technical requirements

#### Acceptance Criteria:

- **`AC-UC-US-015-01` Access precision settings**
  - **Given** the app is open
  - **When** user clicks "Settings" or "Precision" menu
  - **Then** a settings panel appears with options: preset decimal places (0, 2, 4, 6) and "Custom"
  - **And** the current precision setting is highlighted or indicated

- **`AC-UC-US-015-02` Select preset precision**
  - **Given** precision settings panel is open
  - **When** user selects "4 decimal places"
  - **Then** all subsequent conversions display results with exactly 4 decimal places
  - **And** the setting is applied immediately (no "Save" button required)

- **`AC-UC-US-015-03` Set custom decimal places (0-15)**
  - **Given** user selects "Custom" in precision settings
  - **When** user enters "7" for custom decimal places
  - **Then** a numeric input field accepts values from 0 to 15
  - **And** all conversions thereafter display with 7 decimal places

- **`AC-UC-US-015-04` Precision setting persists across sessions**
  - **Given** user sets precision to "6 decimal places"
  - **When** user closes and reopens the app
  - **Then** precision setting is still "6 decimal places"
  - **And** the setting is retrieved from local storage

- **`AC-UC-US-015-05` Display current precision setting visibly**
  - **Given** precision is set to "4 decimal places"
  - **When** user performs a conversion
  - **Then** the precision setting (e.g., "4 decimals") is displayed somewhere in the UI
  - **And** user can change it without navigating away from conversion interface

- **`AC-UC-US-015-06` Precision changes apply to all active conversions**
  - **Given** a conversion shows "2.5678 meters"
  - **When** user changes precision from 4 to 2 decimal places
  - **Then** the result immediately updates to "2.57 meters"
  - **And** no manual re-conversion is required

---

## 🆔 US-UC-US-016: Handle Temperature Conversions Accurately (All Users)
- **PRD Reference:** Feature: Instant Conversion & Value Input – Edge Case: "Handle temperature conversions that require both multiplication and addition"
- **Story ID:** `US-UC-US-016`

**User Story:**
- **As a** User (both Casual and Power)
- **I want to** convert between temperature scales (Celsius, Fahrenheit, Kelvin) accurately
- **So that** I get correct temperature values regardless of the conversion direction

#### Acceptance Criteria:

- **`AC-UC-US-016-01` Convert Celsius to Fahrenheit accurately**
  - **Given** source unit is "Celsius", target unit is "Fahrenheit"
  - **When** user enters "0" (freezing point)
  - **Then** target value displays "32" (Fahrenheit freezing point)
  - **And** when user enters "100" (boiling point)
  - **Then** target value displays "212" (Fahrenheit boiling point)

- **`AC-UC-US-016-02` Convert Fahrenheit to Celsius accurately**
  - **Given** source unit is "Fahrenheit", target unit is "Celsius"
  - **When** user enters "32"
  - **Then** target value displays "0"
  - **And** when user enters "212"
  - **Then** target value displays "100"

- **`AC-UC-US-016-03` Handle decimal temperatures**
  - **Given** source is "Celsius", target is "Fahrenheit"
  - **When** user enters "25.5"
  - **Then** target value displays approximately "77.9"
  - **And** precision matches the user's decimal place setting

- **`AC-UC-US-016-04` Convert Celsius to Kelvin**
  - **Given** source is "Celsius", target is "Kelvin"
  - **When** user enters "25"
  - **Then** target value displays "298.15" (absolute temperature)

- **`AC-UC-US-016-05` Prevent invalid Kelvin values**
  - **Given** source is "Kelvin", target is "Celsius"
  - **When** user enters "-100" (invalid for absolute temperature)
  - **Then** a warning message displays (e.g., "Kelvin cannot be negative")
  - **And** the conversion is rejected or user is prompted to correct input

---

## 🆔 US-UC-US-017: Define Custom Unit (Power User)
- **PRD Reference:** Feature: Custom Unit Definitions – Functional Requirement: "Provide an interface to create custom units"
- **Story ID:** `US-UC-US-017`

**User Story:**
- **As a** Power User
- **I want to** define a custom unit with a specific conversion factor
- **So that** I can work with domain-specific or company-specific units not in the standard database

#### Acceptance Criteria:

- **`AC-UC-US-017-01` Access custom unit creation interface**
  - **Given** the app is open
  - **When** user clicks "Create Custom Unit" or "Add Unit"
  - **Then** a dialog or form appears with fields: "Unit Name", "Unit Symbol", "Category", "Conversion Factor", "Base Unit"
  - **And** each field is clearly labeled with placeholder text or help text

- **`AC-UC-US-017-02` Create custom unit with relative conversion factor**
  - **Given** the custom unit form is open
  - **When** user enters:
    - Name: "My Custom Length"
    - Symbol: "MCL"
    - Category: "length"
    - Base Unit: "meter"
    - Conversion Factor: "2.5"
  - **Then** the custom unit is created and stored
  - **And** success message displays: "Custom unit 'My Custom Length (MCL)' created"

- **`AC-UC-US-017-03` Validate conversion factor**
  - **Given** the custom unit form is open
  - **When** user enters conversion factor "0" or "-5"
  - **Then** an error message displays: "Conversion factor must be positive and non-zero"
  - **And** the form does not submit

- **`AC-UC-US-017-04` Prevent duplicate custom units**
  - **Given** custom unit "My Custom Length (MCL)" already exists
  - **When** user attempts to create another unit with the same name or symbol
  - **Then** an error message displays: "A custom unit with this name or symbol already exists"
  - **And** the form does not submit

- **`AC-UC-US-017-05` Custom unit available in unit selection immediately**
  - **Given** custom unit "My Custom Length (MCL)" has been created
  - **When** user opens the unit selection interface
  - **Then** "My Custom Length" appears in the length category or in a "Custom Units" section
  - **And** the unit can be selected as source or target unit for conversion

---

## 🆔 US-UC-US-018: Manage Custom Units (Power User)
- **PRD Reference:** Feature: Custom Unit Definitions – Functional Requirement: "List all custom units with option to edit or delete"
- **Story ID:** `US-UC-US-018`

**User Story:**
- **As a** Power User
- **I want to** view, edit, and delete my custom units
- **So that** I can maintain my custom unit library and correct any mistakes

#### Acceptance Criteria:

- **`AC-UC-US-018-01` List all custom units**
  - **Given** user has created 3 custom units
  - **When** user opens "Manage Custom Units" or settings
  - **Then** a list displays all 3 custom units with: Name, Symbol, Category, Conversion Factor, Base Unit
  - **And** each entry has "Edit" and "Delete" buttons

- **`AC-UC-US-018-02` Edit custom unit**
  - **Given** "My Custom Length (MCL)" is displayed in the custom units list
  - **When** user clicks "Edit"
  - **Then** an edit form appears pre-populated with current values
  - **And** user can modify Name, Symbol, Conversion Factor, or Category
  - **And** clicking "Save" updates the custom unit

- **`AC-UC-US-018-03` Delete custom unit with confirmation**
  - **Given** custom unit list is displayed
  - **When** user clicks "Delete" for "My Custom Length"
  - **Then** a confirmation dialog appears: "Delete 'My Custom Length'?"
  - **And** options "Delete" and "Cancel" are presented

- **`AC-UC-US-018-04` Confirm deletion removes custom unit**
  - **Given** deletion confirmation is displayed
  - **When** user clicks "Delete"
  - **Then** the custom unit is removed from the list
  - **And** the unit is no longer available in unit selection interface

- **`AC-UC-US-018-05` Custom units persist across app sessions**
  - **Given** user has 5 custom units
  - **When** user closes and reopens the app
  - **Then** all 5 custom units are still available
  - **And** units are retrieved from local storage

- **`AC-UC-US-018-06` Custom unit edits persist immediately**
  - **Given** user edits a custom unit conversion factor
  - **When** user saves the edit
  - **Then** the change is immediately applied to all conversions using this unit
  - **And** the change persists across sessions

---

## 🆔 US-UC-US-019: Input Validation and Error Handling (All Users)
- **PRD Reference:** Feature: Instant Conversion & Value Input – Functional Requirement: "Validate input and reject invalid characters gracefully"
- **Story ID:** `US-UC-US-019`

**User Story:**
- **As a** User (both Casual and Power)
- **I want to** have invalid input rejected clearly without breaking the app
- **So that** I can correct mistakes and proceed without frustration

#### Acceptance Criteria:

- **`AC-UC-US-019-01` Reject non-numeric characters silently**
  - **Given** the source value field is active
  - **When** user types "abc"
  - **Then** the characters are not displayed in the field (or prevented from appearing)
  - **And** no error message is shown

- **`AC-UC-US-019-02` Allow special numeric characters**
  - **Given** the source value field is active
  - **When** user types "1.5e-3" (scientific notation)
  - **Then** all characters are accepted
  - **And** conversion executes correctly

- **`AC-UC-US-019-03` Handle division by zero gracefully**
  - **Given** a mathematical operation could result in division by zero
  - **When** such a condition is triggered
  - **Then** app displays error message (e.g., "Invalid conversion")
  - **And** app does not crash or enter invalid state

- **`AC-UC-US-019-04` Handle very large result overflow**
  - **Given** user performs a conversion that results in a number > 10^308
  - **When** conversion executes
  - **Then** result displays as "Infinity" or in scientific notation
  - **And** app displays explanation (e.g., "Result exceeds display limit")

- **`AC-UC-US-019-05` Handle very small result underflow**
  - **Given** user performs a conversion that results in a number < 10^-308
  - **When** conversion executes
  - **Then** result displays as "0" or in scientific notation
  - **And** no app crash occurs

---

## 🆔 US-UC-US-020: App Performance Baseline (All Users)
- **PRD Reference:** Non-Functional Requirements – Performance section
- **Story ID:** `US-UC-US-020`

**User Story:**
- **As a** User (both Casual and Power)
- **I want to** use the app without perceivable delays
- **So that** the experience feels fast and responsive

#### Acceptance Criteria:

- **`AC-UC-US-020-01` App launches within 1 second**
  - **Given** user taps the app icon
  - **When** the app initializes
  - **Then** the unit converter interface is displayed and interactive within 1000ms
  - **And** all unit data is loaded and available

- **`AC-UC-US-020-02` Conversion calculation completes in < 10ms**
  - **Given** user enters a value in the source field
  - **When** conversion calculates
  - **Then** the result is displayed within 10ms of the input keystroke
  - **And** this holds for all supported unit types

- **`AC-UC-US-020-03` Unit search returns results within 100ms**
  - **Given** user types "meter" in the search field
  - **When** search executes
  - **Then** results appear within 100ms
  - **And** search completes even for multi-character queries (e.g., "millimeter")

- **`AC-UC-US-020-04` All UI interactions respond within 500ms**
  - **Given** user interacts with any UI element (button, tap, scroll)
  - **When** the interaction is triggered
  - **Then** visual feedback (change of state, animation, response) occurs within 500ms
  - **And** this applies to favorites, history, settings, and custom units

- **`AC-UC-US-020-05` App bundle size remains under 10 MB**
  - **Given** the app is downloaded
  - **When** installation completes
  - **Then** the total app size is < 10 MB (including all unit data)
  - **And** this constraint supports lightweight distribution

---

## 🆔 US-UC-US-021: Data Persistence Without Network (All Users)
- **PRD Reference:** Non-Functional Requirements – Offline & Persistence section
- **Story ID:** `US-UC-US-021`

**User Story:**
- **As a** User (both Casual and Power)
- **I want to** have all my data (favorites, history, custom units, settings) saved locally
- **So that** my personal preferences and records persist across sessions and are never lost

#### Acceptance Criteria:

- **`AC-UC-US-021-01` Favorites persist locally without network**
  - **Given** user saves favorites while offline
  - **When** the app closes
  - **Then** favorites are stored in local storage
  - **And** favorites are available when the app reopens (no cloud sync required)

- **`AC-UC-US-021-02` History persists locally**
  - **Given** user performs conversions while offline
  - **When** the app closes
  - **Then** all conversion records are stored locally
  - **And** history is available without network access

- **`AC-UC-US-021-03` Custom units persist locally**
  - **Given** user creates custom units while offline
  - **When** the app closes
  - **Then** custom units are stored in local storage
  - **And** custom units are immediately available on app relaunch

- **`AC-UC-US-021-04` Settings persist locally**
  - **Given** user changes precision setting to "6 decimals"
  - **When** the app closes
  - **Then** the precision setting is stored locally
  - **And** the setting is restored when the app reopens

- **`AC-UC-US-021-05` No data loss on app update**
  - **Given** user has existing favorites, history, custom units, and settings
  - **When** the app is updated to a new version
  - **Then** all user data is preserved
  - **And** no manual data export/import is required

- **`AC-UC-US-021-06` Storage quota handling**
  - **Given** user has 1000+ conversions in history
  - **When** local storage approaches capacity
  - **Then** app displays warning: "Storage limit approaching"
  - **And** user is offered option to clear old history entries or export history

---

## 🆔 US-UC-US-022: Conversion Accuracy (All Users)
- **PRD Reference:** Non-Functional Requirements – Reliability section
- **Story ID:** `US-UC-US-022`

**User Story:**
- **As a** User (both Casual and Power)
- **I want to** trust that conversion results are accurate
- **So that** I can rely on the app for important measurements and calculations

#### Acceptance Criteria:

- **`AC-UC-US-022-01` Conversions match reference standards**
  - **Given** standard conversion test cases (1 mile = 1.60934 km, 1 lb = 0.453592 kg)
  - **When** conversions are performed
  - **Then** results match reference values to within floating-point precision (15-17 significant digits)

- **`AC-UC-US-022-02` No precision loss in chained conversions**
  - **Given** user converts 1 meter → feet → inches → centimeters → meters
  - **When** the conversion chain completes
  - **Then** the final result is within floating-point precision of the original value (1 meter)
  - **And** no cumulative rounding error occurs

- **`AC-UC-US-022-03` SI base unit conversions are authoritative**
  - **Given** all conversions use SI base units as the reference
  - **When** conversions are calculated
  - **Then** consistency is maintained across all unit types
  - **And** the conversion factor relationships are mathematically sound

---

## Summary

**Total User Stories:** 22  
**Feature Coverage:**
- Unit Selection & Search: 3 stories (US-001, US-002, US-003)
- Instant Conversion & Value Input: 5 stories (US-004, US-005, US-006, US-016, US-019)
- Favorites & Quick Access: 3 stories (US-007, US-008, US-009)
- Conversion History & Timestamps: 4 stories (US-010, US-011, US-012, US-013)
- Offline Functionality: 1 story (US-014)
- Precision & Decimal Place Control: 1 story (US-015)
- Custom Unit Definitions: 2 stories (US-017, US-018)
- Cross-Cutting (Performance, Data Persistence, Accuracy): 3 stories (US-020, US-021, US-022)

**User Role Coverage:**
- Casual Converter: 12 stories
- Power User: 11 stories
- All Users: 6 stories (some overlap with role-specific stories)

**Acceptance Criteria:** 110+ total criteria, each with deterministic, machine-readable, pass/fail conditions

---

**Document Version:** 1.0  
**Date:** 2026-05-20  
**Prepared By:** User Story Expansion Pipeline
