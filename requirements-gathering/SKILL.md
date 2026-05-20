---
name: requirements-gathering
description: Interactively gather user needs through structured discovery of roles, tasks, gains, and pains
keywords: [gather requirements, user interview, product discovery]
---

# Requirements Discovery Skill

## Initial Setup

**Do you have a product concept ready?** (concept.md or a clear product idea)

- **If yes:** What is the product you want to gather requirements for?
- **If no:** Tell me about the product idea, and we'll use that to get started.

Once I have the product name, we'll proceed with discovery.

---

## Discovery Process

### Step 1: Identify Users

**Who is someone you envision using <product>?** What is their role or relationship to <product domain>?

(Record: User Role)

**Does <user role> have another task they want to accomplish with <product>?**
- If no → move to Step 3
- If yes → go to Step 2

### Step 2: Capture Tasks & Gains/Pains

**What is something you want to do with <product>?**

(Record: Task)

**What would success look like for <task>?**

(Record: Success Criteria)

**What do you want to get out of <task>? What outcomes or benefits matter to you?**

(Record: Gains - may be multiple)

**Are there other things you'd like to see or experience with <task>?**
- If no → move to pains
- If yes → record additional gains

**What frustrates you about <task>? What gets in the way?**

(Record: Pains - may be multiple)

**Are there other frustrations about <task>?**
- If no → check for another task for this user
- If yes → record additional pains

**Does <user role> have another task they want to accomplish with <product>?**
- If yes → loop back to Step 2
- If no → check for another user role

### Step 3: Check for Additional Users

**Would you like to explore another user role for <product>?**
- If yes → loop back to Step 1
- If no → proceed to Step 4

### Step 4: Display Value Prop Canvas & Final Gate

Display the discovered data as a Value Prop Canvas (user side):

| Role | Task | Gains | Pains |
|------|------|-------|-------|
| [User 1] | [Task] | [list] | [list] |
| ... | ... | ... | ... |

**Any other things we need to cover before I begin creating your PRD?**
- If yes → return to appropriate step
- If no → proceed

---

## Output & Handoff

Save the complete discovery data to `requirements-<product_name>.md` in `/Users/blakemcmillan/Documents/VSCode/Req-gathering/`

### Output Format

Structure the requirements file with each user role as a top-level section, followed by their jobs (tasks), gains, and pains:

```
# Requirements: <Product Name>

### [User Role 1]

#### Job 1: [Job Description]
**Gains:**
- [gain 1]
- [gain 2]
- [as many as needed]

**Pains:**
- [pain 1]
- [pain 2]
- [as many as needed]

#### Job 2: [Job Description]
**Gains:**
- [gain 1]
- [gain 2]

**Pains:**
- [pain 1]

[Continue with as many jobs as needed]

### [User Role 2]

#### Job 1: [Job Description]
**Gains:**
- [gain 1]

**Pains:**
- [pain 1]

[Continue with as many user roles as needed]

---

## Value Prop Canvas (User Side)

[Canvas table showing aggregated user needs]
```

Then offer:

**Ready for me to create your PRD based on this discovery?**
- If yes → Invoke prd-generation skill with product_name parameter
- If no → End skill

---

## Key Principles for the Skill

- Use variables for traceability: `<product>`, `<user role>`, `<task>`
- Users describe their world; we design solutions (don't ask for features, ask for problems)
- Recognize task boundaries (if they introduce a new capability, treat it as a separate task)
- Consolidate repetition (combine similar statements; don't create duplicates)
- Be curious; ask follow-ups for clarity
