---
name: prd-creation
description: Generate a production-quality PRD from gathered requirements
keywords: [create prd, make prd, create project requirements document, make project requirements document]
---

# PRD Generation Skill

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

Create a markdown PRD with:
1. **Product Overview** — name, mission, description
2. **Goals & Non-Goals** — what we're building, what we're not
3. **User Roles & Needs** — each role, their tasks, gains, pains (grounded in discovered data)
4. **Features & How They Solve Needs** — each feature with clear linkage to user gains/pains
5. **Non-Functional Requirements** — derived from feature design and user needs
6. **Success Metrics** — tied to user goals
7. **Open Questions** — ambiguities or deferred decisions

Key principles:
- Every feature traces back to user needs (no generic features)
- Skip persona fluff (ages, names, irrelevant details)
- Use the many-to-one pattern: celebrate features that elegantly solve multiple problems
- Ground everything in the data we collected

---

## Output

Save the complete PRD to:

```
prd-<product_name>.md
```

in the root directory where this skill was invoked.

Display the PRD in the conversation.

---

## Handoff Complete

The PRD is now ready for downstream stages (architecture, UX, epic creation).
