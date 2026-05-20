---
name: prd-creation
description: Generate a production-quality PRD from gathered requirements
keywords: [create prd, make prd, create project requirements document, make project requirements document]
argument-hint: "[file path to requirements document]"
allowed-tools: Read, Write
---

# PRD Generation Skill

## Input & Output

**Input:** Path to requirements document (e.g., `/output/habit-tracker/requirements.md`)

**Output:** Save PRD to `/output/<project_name>/prd.md`

---

## Initial Gate: Do You Have Requirements?

**Do you already have a requirements file with discovered user needs?**

### Path 1: Yes, from the requirements-gathering skill

**Where is the file?** (e.g., `requirements-habit-tracker.md`)

Read the file from the specified location. Proceed to PRD Generation.

### Path 2: Yes, but from a different source

**Where is the file?** (e.g., a requirements doc, user research, etc.)

⚠️ **Note:** This PRD will be stronger if you ran the requirements-gathering skill first, which uses a structured approach to elicit user needs. The discovery process captures gains and pains alongside tasks, which leads to features that solve multiple user problems elegantly.

**Would you like to run the requirements-gathering skill now?**
- If **yes** → Invoke requirements-gathering skill (don't ask just do it)
- If **no** → Proceed with what you have ("YOLO mode" - we'll do our best with the information available)

Read the file from the specified location. Proceed to PRD Generation.

### Path 3: No, I don't have a requirements file yet

No problem! Let's gather requirements first.

**Invoking requirements-gathering skill...**

(Automatically invoke requirements-gathering skill. When it completes and hands off, continue with PRD Generation using the generated `requirements-<product_name>.md` file.)

---

## PRD Generation Process

### Step 1: Read & Analyze Requirements

Read the discovered requirements file. Extract:
- Product name and concept
- All user roles
- All tasks per role
- All gains per task
- All pains per task

### Step 2: Pattern Recognition

Identify themes and overlaps:
- Which gains/pains appear across multiple roles/tasks?
- Where can a single feature solve multiple problems (many-to-one pattern)?
- What are the key constraints or needs that emerge?

### Step 3: Design Features

For each major gain or pain cluster, design a feature that solves it. Show the many-to-one relationships (which users/gains/pains does each feature address?).

### Step 4: Generate PRD

Create a markdown PRD with these sections:

#### 1. Product Overview
- Product name, mission, high-level description

#### 2. Goals & Non-Goals
- What we're building and what we're explicitly not building
- Include 2–3 primary business goals for the product

#### 3. User Roles & Needs

For each user role, document their tasks, gains, and pains in structured format (grounded in discovered data):

```
### [User Role 1]

#### Task: [Task Description]
**Gains:**
- [gain 1]
- [gain 2]

**Pains:**
- [pain 1]
- [pain 2]

#### Task: [Task Description]
**Gains:**
- [gain 1]

**Pains:**
- [pain 1]

### [User Role 2]
[Continue with all roles and tasks discovered]
```

#### 4. Features & How They Solve Needs

For each feature, include:

**Feature: [Name]**

- **Goals** — 2–3 business goals this specific feature achieves
- **Overview** — 2–3 sentence summary: what it does, why it matters
- **Solves For** — which user roles, tasks, gains, and pains this feature addresses (many-to-one traceability)
- **Functional Requirements** — what the feature does, user workflows it enables, integration points
- **Non-Functional Requirements** — performance expectations, scalability, security, reliability
- **Constraints**
  - *Technical:* architecture limitations, technology choices, integration dependencies
  - *Business:* timeline/availability, resource constraints, cost considerations
- **Success Metrics** — how we measure success, KPIs tied to user goals
- **Edge Cases & Considerations** — potential issues or failure modes, user scenarios to handle, data validation, error handling strategies

#### 5. Non-Functional Requirements (Product-Wide)
- Cross-cutting concerns not tied to individual features

#### 6. Success Metrics (Product-Wide)
- High-level product success metrics and KPIs

#### 7. Open Questions
- Ambiguities or deferred decisions

Key principles:
- Every feature traces back to user needs (no generic features)
- Skip persona fluff (ages, names, irrelevant details)
- Use the many-to-one pattern: celebrate features that elegantly solve multiple problems
- Ground everything in the data we collected
- **Traceability goes in "Solves For" sections of each feature—do not add an appendix table**

---

## Output

Save the complete PRD to:

```
/output/<product_name>/prd.md
```

Display the PRD in the conversation.

---

## Handoff Complete

The PRD is now ready for downstream stages (user story expansion, test planning).
