---
name: user-story-expansion
description: Transform a PRD into detailed user stories with data states, acceptance criteria (Gherkin), and probing questions. Use after prd-creation to expand each feature into implementation-ready requirements.
---

# User Story Expansion

Expand features from a PRD into structured user stories with acceptance criteria and probing questions.

## Initial Gate: Do You Have a PRD?

**Do you already have a PRD file with designed features?**

### Path 1: Yes, from the prd-creation skill

**Where is the PRD file?** (e.g., `prd-habit-tracker.md`)

Read the file from the specified location. Extract the product name. Proceed to Story Expansion.

### Path 2: Yes, but from a different source

**Where is the file?** (e.g., an existing PRD or design doc)

Read the file from the specified location. Extract the product name if possible. Proceed to Story Expansion.

### Path 3: No, I don't have a PRD yet

No problem! Let's create one first.

**Invoking prd-creation skill...**

(Automatically invoke prd-creation skill. When it completes and produces `prd-<product_name>.md`, continue with Story Expansion using that file.)

---

## Story Expansion Process

### 1. Read & Extract Features

Read the PRD file. Extract:
- Product name
- All features listed in the PRD
- For each feature: name, description, user roles, goals, functional/non-functional requirements

### 2. Expand Each Feature

For each feature from the PRD, generate:

**User Story** (Agile format, derived from PRD user roles and feature description):
```
As a [role from PRD], I want to [feature action], so that [goal/value from PRD].
```

**Data State** (what changes in the system):
- Initial State: What exists before this feature?
- Final State: What exists after this feature is implemented?
- Core Data Models: Entities and fields needed (inferred from functional requirements)

**Acceptance Criteria** (Gherkin, 3–5 scenarios covering happy path, edge cases, error cases):
```gherkin
Scenario: [scenario title]
  Given [context]
  When [user action]
  Then [outcome]
```

**Probing Questions** (4–6 high-impact questions):
- Integration points: How does this feature integrate with other features/systems?
- Performance: What are performance expectations or scale limits?
- Edge cases: What happens in unusual or error conditions?
- Data: How is data validated, persisted, or synchronized?
- User experience: Are there accessibility or UX edge cases?
- Operations: Are there operational or monitoring concerns?

### 3. Output: Markdown File

Generate a single `.md` file for the entire product:

```
/output/<product_name>/user-stories.md
```

---

## Output Document Structure

```markdown
# User Stories: <Product Name>

## Feature: [Feature 1 Name]

**User Story**
As a [role], I want to [action], so that [value].

### Data State

**Initial State**
[What exists before]

**Final State**
[What exists after]

**Core Data Models**
- Model1 (fields...)
- Model2 (fields...)

### Acceptance Criteria

**Scenario 1: [Happy Path Title]**
\`\`\`gherkin
Given [context]
When [action]
Then [outcome]
\`\`\`

**Scenario 2: [Edge Case Title]**
\`\`\`gherkin
Given [context]
When [edge case]
Then [outcome]
\`\`\`

**Scenario 3: [Error Case Title]**
\`\`\`gherkin
Given [context]
When [error trigger]
Then [error handling]
\`\`\`

### Open Questions & Gaps

1. [Category] — [Question]
2. [Category] — [Question]
3. [Category] — [Question]
4. [Category] — [Question]

---

## Feature: [Feature 2 Name]

[Repeat structure for each feature in PRD]

---

*Generated via User Story Expansion Skill*
```

---

## Handoff Complete

The user stories are now ready for development, sprint planning, or technical architecture work. Each feature is fully specified with acceptance criteria, data state transitions, and open questions to resolve before implementation.