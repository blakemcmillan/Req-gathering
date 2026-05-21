#!/usr/bin/env python3
"""Requirements quality evaluator for AI Bootcamp."""

import sys
import re
from pathlib import Path

def parse_requirements(content):
    """Parse requirements.md and extract structure."""
    # Extract user roles (### [User Role] headers)
    user_roles = re.findall(r'^### (.+?)$', content, re.MULTILINE)
    user_roles = list(dict.fromkeys(user_roles))  # Deduplicate while preserving order

    # Extract tasks (### Task: or ### Job: or #### Task: or #### Job: pattern)
    tasks = re.findall(r'^#{3,4} (?:Task|Job): (.+?)$', content, re.MULTILINE)

    # Count gains/pains sections (look for **Gains:** and **Pains:** headers)
    gains_sections = len(re.findall(r'^\*\*Gains:\*\*', content, re.MULTILINE))
    pains_sections = len(re.findall(r'^\*\*Pains:\*\*', content, re.MULTILINE))

    return {
        'user_roles': user_roles,
        'user_role_count': len(user_roles),
        'task_count': len(tasks),
        'gains_sections': gains_sections,
        'pains_sections': pains_sections,
        'total_gains_and_pains': gains_sections + pains_sections
    }

def parse_concept(content):
    """Parse concept.md for complexity signals."""

    # Scope: distinct capabilities/features mentioned
    scope_keywords = [
        r'\bfeature', r'\bcapabilit', r'\bsupport', r'\ballow',
        r'\benable', r'\btrack', r'\bmanage', r'\bintegrat',
        r'\banalyze', r'\bshare', r'\bfilter', r'\bcustomi'
    ]
    scope_mentions = sum(len(re.findall(kw, content, re.IGNORECASE)) for kw in scope_keywords)

    # User Diversity: distinct user personas/types
    user_mentions = len(re.findall(r'\b(user|player|developer|engineer|student|worker|customer|admin|casual|competitive|power user)\b', content, re.IGNORECASE))

    # Task Interdependency: task linkage and interaction words
    dependency_words = r'\b(integrat|sync|connect|link|workflow|across|multiple|interact|coordinate|alongside)\b'
    interdependency_mentions = len(re.findall(dependency_words, content, re.IGNORECASE))

    return {
        'scope_score': scope_mentions,
        'user_diversity_score': user_mentions,
        'interdependency_score': interdependency_mentions
    }

def infer_complexity(concept_signals):
    """Infer complexity from concept signals."""
    if not concept_signals:
        return None, None

    scope = concept_signals['scope_score']
    user_div = concept_signals['user_diversity_score']
    interdep = concept_signals['interdependency_score']

    # Simple: low scores across all three
    if scope < 8 and user_div < 3 and interdep < 2:
        return 'Simple', 'Single or minimal capabilities, single user type, no task interactions'

    # Moderate: mid-range scores
    elif scope < 15 and user_div < 6 and interdep < 4:
        return 'Moderate', 'Multiple capabilities, 2-3 user types, some task interactions'

    # Complex: high scores
    else:
        return 'Complex', '5+ capabilities, multiple user types with competing needs, interdependent tasks'

def validate_structural_gates(requirements):
    """Validate minimum structural requirements."""
    checks = [
        {
            'name': 'At least 1 user role',
            'passed': requirements['user_role_count'] >= 1
        },
        {
            'name': 'At least 1 task',
            'passed': requirements['task_count'] >= 1
        },
        {
            'name': 'At least 1 gain AND 1 pain',
            'passed': requirements['gains_sections'] >= 1 and requirements['pains_sections'] >= 1
        }
    ]
    return checks

def assess_adequacy(complexity, requirements):
    """Assess whether captured requirements match product complexity."""

    roles = requirements['user_role_count']
    tasks = requirements['task_count']
    gains = requirements['gains_sections']
    pains = requirements['pains_sections']

    if not complexity:
        # No concept file; assess based on structure alone
        if roles >= 1 and tasks >= 1 and gains >= 1 and pains >= 1:
            return 'MEDIUM', 'Structural requirements met. Complexity cannot be assessed without concept file.'
        else:
            return 'LOW', 'Structural requirements not met.'

    # Simple product
    if complexity == 'Simple':
        if roles >= 1 and tasks >= 1 and gains >= 1 and pains >= 1:
            return 'HIGH', 'Minimal requirements capture is appropriate for a simple, single-purpose product. No additional exploration needed.'
        else:
            return 'LOW', 'Structural requirements not met.'

    # Moderate product
    elif complexity == 'Moderate':
        if roles >= 2 and tasks >= 2 and gains >= 2 and pains >= 2:
            return 'HIGH', 'Adequate user and task diversity matches moderate product scope.'
        elif roles >= 1 and tasks >= 1 and gains >= 1 and pains >= 1:
            return 'MEDIUM', 'Minimum structure met, but consider exploring additional user roles and task interactions.'
        else:
            return 'LOW', 'Insufficient exploration for moderate complexity.'

    # Complex product
    elif complexity == 'Complex':
        if roles >= 3 and tasks >= 3 and gains >= 3 and pains >= 3:
            return 'HIGH', 'Rich requirements depth matches complex, multi-user, interdependent product scope.'
        elif roles >= 2 and tasks >= 2 and gains >= 2 and pains >= 2:
            return 'MEDIUM', 'Good coverage, but consider deeper exploration of competing user needs and task interactions.'
        else:
            return 'LOW', 'Shallow requirements for complex product scope. Return to discovery.'

    return 'UNKNOWN', 'Unable to determine adequacy.'

def generate_markdown(requirements, complexity, complexity_rationale, adequacy, adequacy_rationale, structural_checks, concept_present):
    """Generate eval-requirements.md markdown output."""

    struct_status = 'PASS' if all(c['passed'] for c in structural_checks) else 'FAIL'

    md = f"""# Requirements Evaluation

## Structural Validation

"""
    for check in structural_checks:
        status = '✓' if check['passed'] else '✗'
        md += f"- [{status}] {check['name']}\n"

    md += f"\n**Status:** {struct_status}\n\n"

    md += f"""## Requirements Summary

- **User Roles:** {requirements['user_role_count']}
- **Tasks:** {requirements['task_count']}
- **Gains:** {requirements['gains_sections']} | **Pains:** {requirements['pains_sections']}

"""

    md += f"""## Complexity Assessment

"""

    if concept_present and complexity:
        md += f"""**Concept Signals:**
- Scope: Multiple capabilities and features identified
- User Diversity: {requirements['user_role_count']} user role(s) discovered
- Task Interdependency: {requirements['task_count']} task(s) with varying interactions

**Complexity Level:** {complexity}
- {complexity_rationale}

"""
    else:
        md += f"""**Concept File:** Not found ⚠

Complexity assessment skipped; analyzing requirements structure only.

"""

    md += f"""## Adequacy Rating

**Confidence: {adequacy}**

{adequacy_rationale}

## Recommendations

"""

    if adequacy == 'HIGH':
        md += "None. Requirements are adequate for PRD creation.\n"
    elif adequacy == 'MEDIUM':
        md += "- Ensure gains and pains are specific and concrete (not generic)\n"
        if requirements['user_role_count'] < 2:
            md += "- Consider exploring an additional user role or persona\n"
        if requirements['task_count'] < 2:
            md += "- Add tasks that show how different user types interact with the product\n"
    else:  # LOW
        if requirements['user_role_count'] < 2:
            md += f"- Expand user discovery: aim for 2+ roles (found {requirements['user_role_count']})\n"
        if requirements['task_count'] < 2:
            md += f"- Add more tasks per user: aim for 2+ tasks (found {requirements['task_count']})\n"
        if requirements['gains_sections'] < 1 or requirements['pains_sections'] < 1:
            md += "- Ensure every task has at least one gain AND one pain\n"
        md += "- Return to requirements gathering if uncertain\n"

    md += f"""
## Notes for Learning

Complexity assessment compares the product's inherent scope, user diversity, and task interactions against your discovered requirements. Simple products (single capability, one user) need minimal requirements; complex products (many capabilities, competing user needs) demand rich exploration.

"""

    return md

def main():
    if len(sys.argv) < 2:
        print("Usage: eval-requirements.py <requirements_file>", file=sys.stderr)
        sys.exit(1)

    req_file = Path(sys.argv[1])
    req_dir = req_file.parent

    if not req_file.exists():
        print(f"Error: File not found: {req_file}", file=sys.stderr)
        sys.exit(1)

    # Read requirements.md
    try:
        with open(req_file, 'r') as f:
            req_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    # Check for concept.md in same directory
    concept_file = req_dir / 'concept.md'
    concept_present = False
    complexity = None
    complexity_rationale = None

    if concept_file.exists():
        try:
            with open(concept_file, 'r') as f:
                concept_content = f.read()
            concept_signals = parse_concept(concept_content)
            complexity, complexity_rationale = infer_complexity(concept_signals)
            concept_present = True
        except Exception as e:
            print(f"Warning: Could not read concept.md: {e}", file=sys.stderr)

    # Parse requirements
    requirements = parse_requirements(req_content)

    # Validate structure
    structural_checks = validate_structural_gates(requirements)

    # Assess adequacy
    adequacy, adequacy_rationale = assess_adequacy(complexity, requirements)

    # Generate output
    markdown_output = generate_markdown(
        requirements, complexity, complexity_rationale,
        adequacy, adequacy_rationale,
        structural_checks, concept_present
    )

    # Write eval-requirements.md
    output_file = req_dir / 'eval-requirements.md'
    try:
        with open(output_file, 'w') as f:
            f.write(markdown_output)

        print(f"✓ Evaluation written to {output_file}")
        print(f"  Adequacy: {adequacy} | Complexity: {complexity or 'UNKNOWN'}")
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
