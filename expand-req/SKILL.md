---
name: expand-req
description: Expand a feature request into a structured PRD with goals, constraints, and success metrics. Use when you need to turn a brief user story or feature idea into a detailed product requirements document.
argument-hint: "[feature request]"
allowed-tools: Write
---

# Expand Feature Request

Transform the following feature request into a comprehensive Product Requirements Document:

**Feature Request:** $ARGUMENTS

**Output Filename:** Create filename from feature name by converting to lowercase and replacing spaces with hyphens. Save to `/outputs/expand-req/[feature-name].md`

---

## Expanded PRD

Create a detailed PRD with these sections:

### Feature: [Name from request]

**Goals**

- List 2-3 primary business goals this feature achieves

**Overview**

- 2-3 sentence summary of what the feature does and why it matters

**Requirements**

*Functional Requirements:*

- What the feature does
- User workflows it enables
- Integration points

*Non-Functional Requirements:*

- Performance expectations
- Scalability requirements
- Security considerations

**Constraints**

*Technical Constraints:*

- Architecture limitations
- Technology choices
- Integration dependencies

*Business Constraints:*

- Timeline/availability
- Resource constraints
- Cost considerations

**Success Metrics**

- How we measure if this is successful
- Key performance indicators (KPIs)
- User satisfaction measures

**Edge Cases & Considerations**

- Potential issues or failure modes
- User scenarios to handle
- Data validation requirements
- Error handling strategies

---

## Output Instructions

Save your expanded PRD to `/outputs/expand-req/[feature-name].md` where [feature-name] is derived from the feature request (lowercase, spaces as hyphens). For example, "User can export data as CSV" → `user-can-export-data-as-csv.md`. Include all sections above with specific details relevant to the feature request. Be concrete and actionable rather than generic.

---

## Prompts

### ✓ Good Fit (Positive Examples)

- `pomodoro tracker` - High-level product idea, needs expansion into full spec
- `user can export data as CSV` - Named feature with clear scope
- `real-time collaboration` - Feature concept that benefits from goals/requirements/metrics
- `dark mode toggle` - Simple feature that needs functional and non-functional requirements fleshed out
- `two-factor authentication` - Security feature requiring detailed implementation guidance
- `analytics dashboard` - Complex feature needing success metrics and edge cases
- `offline-first mobile app` - Product architecture concept benefiting from structured planning

### ✗ Poor Fit (Negative Examples)

- `make it better` - Too vague; no specific feature to expand
- `fix the login bug` - Bug fix, not a feature; expand-req is for new functionality
- `refactor the component tree` - Implementation task, not a feature request
- `optimize database queries` - Performance improvement; not a product feature
- `what should we build?` - Meta question; needs your input first on *what*
- `add tests` - Technical task, not a user-facing feature
- `update dependencies` - Maintenance work, not a feature
- `Here's my detailed 5-page spec...` - Already fully specified; doesn't need expansion

### Why This Skill Works Best

Expand-req transforms **brief, high-level feature concepts** into **structured product specifications**. It answers "what should we build and how do we measure success?" — not "how do we build it?" and not "how do we fix it?"

Use this skill when you have a feature idea or user story that's clear enough to name, but needs goals, requirements, constraints, and success metrics filled in.
