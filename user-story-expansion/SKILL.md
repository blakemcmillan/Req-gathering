---
name: user-story-expansion
description: Expand vague feature requests into structured requirements. Use whenever a user describes a feature idea that needs to be formalized into a User Story, Data State, Acceptance Criteria (Gherkin), and Probing Questions.
---

# Requirement Expansion
Expand raw feature ideas into structured requirements.

## Process

### 1. Alignment Check
Is this a software feature request? If no, politely decline. If yes, proceed.

### 2. Clarify if Needed
Ask 1–3 questions if the request is vague:
- Who uses this and why?
- What's in scope?
- What does done look like?

### 3. Expand

**User Story** (Agile format):
```
As a [role], I want to [action], so that [value].
```

**Data State**:
- Initial State: What exists now?
- Final State: What exists after?
- Core Data Models: What entities/fields are needed?

**Acceptance Criteria** (Gherkin, 3–5 scenarios):
```gherkin
Scenario: [scenario title]
  Given [context]
  When [user action]
  Then [outcome]
```

**Probing Questions** (4–6 high-impact):
- What happens if...?
- How does this integrate with...?
- What are performance/scale limits?

### 4. Output: Markdown File

Generate a `.md` file with this structure:

```markdown
# [Feature Name]

**User Story**
As a [role], I want to [action], so that [value].

---

## Data State

### Initial State
[Current system state]

### Final State
[System state after feature]

### Core Data Models
- Model1 (id, fields...)
- Model2 (id, fields...)

---

## Acceptance Criteria

### Scenario 1: [Happy Path]
\`\`\`gherkin
Given [context]
When [action]
Then [outcome]
\`\`\`

### Scenario 2: [Edge Case]
\`\`\`gherkin
Given [context]
When [edge case]
Then [outcome]
\`\`\`

### Scenario 3: [Error Case]
\`\`\`gherkin
Given [context]
When [error trigger]
Then [error handling]
\`\`\`

---

## Open Questions & Gaps

1. [Category] — [Question]
2. [Category] — [Question]
3. [Category] — [Question]
4. [Category] — [Question]
5. [Category] — [Question]

---

*Generated via Requirement Expansion Skill*
```

---

## Example

**Input:** "We want to let users export reports in Excel format."

**Output:**

```markdown
# Excel Export Feature

**User Story**
As a business analyst, I want to export my reports in Excel format, so that I can share data with stakeholders who prefer spreadsheets over PDFs.

---

## Data State

### Initial State
Reports can only be exported as PDF. No Excel export option exists.

### Final State
Reports can be exported as .xlsx with formatting (bold headers, colors, totals).

### Core Data Models
- ExportJob (id, report_id, format, created_at, status)
- ExportLog (id, export_job_id, file_size, duration_ms, error_message)

---

## Acceptance Criteria

### Scenario 1: User Exports Report as Excel
\`\`\`gherkin
Given a user is viewing a report
When they click "Export" and select "Excel (.xlsx)"
And click "Download"
Then a file is generated with the report name
And column headers are bold and frozen
And the file downloads within 30 seconds
\`\`\`

### Scenario 2: Empty Report Export
\`\`\`gherkin
Given a report has no data rows
When they click "Export" and select "Excel"
Then a modal warns: "No data. Export anyway?"
And they can cancel or proceed
\`\`\`

### Scenario 3: Export Timeout
\`\`\`gherkin
Given an export job times out after 2 minutes
When the user waits for completion
Then they see: "Export failed. Please try again or contact support."
And they can retry immediately
\`\`\`

---

## Open Questions & Gaps

1. **Scope** — Should Excel exports include charts/visualizations or just tabular data?
2. **Scale** — Are there row limits (e.g., max 100K rows per export)?
3. **UX** — Should users be able to customize which columns to include?
4. **Audit** — Do we need logs for who exported what and when?
5. **Metadata** — Should exported files include the report's filters/parameters?

---

*Generated via Requirement Expansion Skill*
```