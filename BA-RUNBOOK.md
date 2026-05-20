# BA Runbook: Sequential Skill Workflow

This runbook defines the best order to use the skills in this repository and the quality gates for each stage.

## Purpose

Use this process to move from problem discovery to implementation-ready stories with strong traceability.

Outcomes:
- Clear user needs grounded in evidence
- Product-level scope and priorities in a PRD
- Testable, engineering-ready user stories

## Skill Sequence

Run these skills in this order:

1. requirements-gathering
2. prd-creation
3. user-story-expansion

Optional accelerator:
1. expand-req (only for quick single-feature expansion)

## Stage 1: Requirement Discovery

Skill:
- requirements-gathering/SKILL.md

Objective:
- Discover user roles, tasks, gains, pains, and success expectations.

Inputs:
- Product concept or product name
- Stakeholder context

Method:
- Identify user roles
- Capture each role's tasks
- Capture gains and pains per task
- Consolidate duplicates and overlaps

Deliverable:
- requirements-product-name.md

Exit Criteria:
- At least one validated user role and task exists
- Gains and pains are captured for every in-scope task
- No major unknown role/task remains for current release scope

## Stage 2: PRD Synthesis

Skill:
- prd-creation/SKILL.md

Objective:
- Convert discovered needs into a product-level requirements document.

Inputs:
- requirements-product-name.md

Method:
- Analyze role/task/gain/pain patterns
- Design features that solve clustered needs
- Define goals, non-goals, constraints, NFRs, and success metrics

Deliverable:
- prd-product-name.md

Exit Criteria:
- Every feature maps to one or more discovered pains or gains
- Scope boundaries are explicit (goals and non-goals)
- Success metrics are measurable and owner-ready

## Prioritization Method (Before Story Expansion)

Use MoSCoW to decide what enters the next build cycle.

Rules:
- Must: Critical for user value, compliance, or basic usability
- Should: High value but workable workaround exists
- Could: Nice-to-have with lower immediate impact
- Won't (Now): Explicitly deferred

Template:

| PRD Feature | User Impact | Business Impact | Complexity | MoSCoW | Reason |
|---|---|---|---|---|---|
|  |  |  |  | Must |  |

## Stage 3: Story Expansion

Skill:
- user-story-expansion/SKILL.md

Objective:
- Convert each approved PRD feature into implementation-ready stories.

Inputs:
- prd-product-name.md
- Prioritized feature list

Method:
- Expand feature into Agile user story
- Define data state: initial, final, core models
- Write 3-5 Gherkin scenarios
- Capture open questions and assumptions

Deliverable:
- Story markdown for each feature or slice

Exit Criteria:
- Story is testable through acceptance criteria
- Data changes are explicit and consistent
- Open questions are tracked with owner and due date

## Optional Stage: Quick Feature Expansion

Skill:
- expand-req/SKILL.md

Use only when:
- You have one clear feature request
- You need a fast draft PRD for alignment

Do not use when:
- Multiple user roles or major unknowns exist
- Discovery has not been done and risk is high

## Traceability Standard

Maintain this chain for every delivery item:

User Pain or Gain -> PRD Feature -> User Story -> Acceptance Scenario

If any link is missing, the item is not ready.

## Operating Cadence

1. Discovery workshop
2. PRD synthesis and review
3. Story expansion for top priorities
4. Backlog readiness review
5. Decision log updates

Recommended cadence:
- Weekly for active product teams
- Per epic for project-based teams

## Review Checklists

Discovery Checklist:
- Roles identified and validated
- Tasks are outcome-focused, not solution-biased
- Gains and pains are specific and non-duplicative

PRD Checklist:
- Features are need-driven, not assumption-driven
- NFRs cover performance, reliability, security, scale
- Metrics include baseline, target, and measurement source

Story Checklist:
- User story has clear value statement
- Gherkin scenarios include happy, edge, and failure paths
- Dependencies and data impacts are explicit

## Rubric Mapping (Assessment Ready)

Use this section to map work artifacts to grading criteria.

| Rubric Criterion | Where It Is Satisfied | Evidence Artifact |
|---|---|---|
| Problem understanding | Stage 1 Discovery + Discovery Checklist | requirements-product-name.md |
| Structured requirements | Stage 2 PRD Synthesis + PRD Checklist | prd-product-name.md |
| Testable delivery detail | Stage 3 Story Expansion + Story Checklist | story markdown with Gherkin |
| Traceability quality | Traceability Standard + Template D | matrix rows linking need to scenario |
| Prioritization rationale | Prioritization Method | MoSCoW table |

## RACI (Lightweight)

- BA: leads discovery, traceability, and quality gates
- Product Owner: approves scope, priorities, and success metrics
- Engineering Lead: validates technical feasibility and constraints
- QA: validates testability and acceptance criteria quality
- UX: validates workflow clarity and user fit where applicable

## Templates

### Template A: Feature-to-Story Planning Table

| Priority | PRD Feature | User Value | Story Slice | Dependencies | Status |
|---|---|---|---|---|---|
| P1 |  |  |  |  | Draft |

### Template B: Open Questions Log

| ID | Question | Impact | Owner | Due Date | Decision |
|---|---|---|---|---|---|
| Q-001 |  |  |  |  |  |

### Template C: Metrics Definition

| Metric | Baseline | Target | Data Source | Owner | Review Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Template D: End-to-End Traceability Matrix

| Pain or Gain ID | PRD Feature | Story ID | Scenario ID | Metric | Notes |
|---|---|---|---|---|---|
| PG-001 |  | US-001 | AC-001 |  |  |

## Definition of Ready (For Engineering Handoff)

An item is ready only if all are true:
- Linked to a PRD feature and user need
- Acceptance criteria are complete and testable
- Data state and dependencies are identified
- Open questions are resolved or time-boxed with explicit risk

## Definition of Done (Per Stage)

Discovery Done:
- requirements-product-name.md exists and is complete
- Role/task/gain/pain coverage is reviewed with stakeholders
- Duplicate items are consolidated

PRD Done:
- prd-product-name.md exists and passes PRD checklist
- Each feature has explicit user-need linkage
- Metrics include baseline or rationale when baseline is unavailable

Story Expansion Done:
- Each prioritized feature has at least one story markdown
- Each story has 3-5 acceptance scenarios
- Open questions have owner and decision date

## Submission Checklist

Use before handing in or opening a PR.

- requirements-product-name.md included
- prd-product-name.md included
- Story markdown files included for prioritized features
- MoSCoW prioritization table completed
- Traceability matrix completed for in-scope items
- Open questions log present with owners and due dates
- Naming conventions are consistent across artifacts
- All markdown files are readable and section-complete

## Example Walkthrough (Mini)

Example feature idea:
- User can export team activity report to CSV

Discovery excerpt:
- Role: Team Lead
- Task: Share weekly activity with stakeholders
- Gain: Faster reporting cycle
- Pain: Manual copy/paste causes errors

PRD feature:
- CSV Export with filter preservation and audit logging

Story excerpt:
- As a Team Lead, I want to export filtered activity data to CSV, so that I can share accurate updates quickly.

Acceptance scenario excerpt:

```gherkin
Scenario: Export filtered activity to CSV
	Given I am viewing team activity with date and member filters applied
	When I click Export and choose CSV
	Then the downloaded file includes only filtered rows
	And the file is generated within 30 seconds
```

Traceability row example:

| Pain or Gain ID | PRD Feature | Story ID | Scenario ID | Metric | Notes |
|---|---|---|---|---|---|
| PG-001 Manual reporting is slow | CSV Export | US-001 | AC-001 | Report prep time reduced by 50% | Compare baseline vs 4-week average |

## How to Use This Runbook in This Repo

1. Run requirements-gathering/SKILL.md and save discovery output.
2. Run prd-creation/SKILL.md using the discovery file.
3. Run user-story-expansion/SKILL.md for each prioritized feature.
4. Use the checklists above before moving to the next stage.

This ensures consistent quality, faster alignment, and cleaner handoffs.
