#!/usr/bin/env python3
"""Requirements quality evaluator - validates against SKILL.md structure requirements."""

import sys
import os
import re
from pathlib import Path

def evaluate_requirements(content):
    """Evaluate requirements against SKILL.md structure requirements."""
    results = []

    # Check for required top-level sections
    has_title = bool(re.search(r'^# ', content, re.MULTILINE))
    result = {
        "description": "Has main title (# Requirements or similar)",
        "passed": has_title
    }
    if not has_title:
        result["trace"] = "Document should start with a main title (# Requirements)."
    results.append(result)

    # Check for user roles section (### [User Role])
    user_roles = re.findall(r'^### (.+?)$', content, re.MULTILINE)
    user_roles = list(dict.fromkeys(user_roles))  # Deduplicate
    has_user_roles = len(user_roles) >= 1
    result = {
        "description": f"User roles documented (at least 1, found {len(user_roles)})",
        "passed": has_user_roles,
        "details": f"{len(user_roles)} user role(s): {', '.join(user_roles[:3])}" if user_roles else "No user roles found"
    }
    if not has_user_roles:
        result["trace"] = "Add ### [User Role] sections to document user personas and their needs. Example: ### Product Manager, ### Developer, ### End User"
    results.append(result)

    # Check for tasks (### Task: or #### Task: pattern)
    tasks = re.findall(r'^#{3,4} (?:Task|Job): (.+?)$', content, re.MULTILINE)
    has_tasks = len(tasks) >= 1
    result = {
        "description": f"Tasks documented (at least 1, found {len(tasks)})",
        "passed": has_tasks,
        "details": f"{len(tasks)} task(s) identified"
    }
    if not has_tasks:
        result["trace"] = "Add ### Task: or #### Task: sections under each user role to describe what they want to do. Example: ### Task: Create workout plan, ### Task: Log completed exercises"
    results.append(result)

    # Check for gains sections
    gains = re.findall(r'^\*\*Gains:\*\*', content, re.MULTILINE)
    has_gains = len(gains) >= 1
    result = {
        "description": f"Gains documented (at least 1, found {len(gains)})",
        "passed": has_gains,
        "details": f"{len(gains)} gain section(s) found"
    }
    if not has_gains:
        result["trace"] = "Add **Gains:** sections under each task to describe quantifiable benefits. Example: **Gains:** Save 2+ hours/week, increase workout consistency to 90%"
    results.append(result)

    # Check for pains sections
    pains = re.findall(r'^\*\*Pains:\*\*', content, re.MULTILINE)
    has_pains = len(pains) >= 1
    result = {
        "description": f"Pains documented (at least 1, found {len(pains)})",
        "passed": has_pains,
        "details": f"{len(pains)} pain section(s) found"
    }
    if not has_pains:
        result["trace"] = "Add **Pains:** sections under each task to describe current friction points. Example: **Pains:** Spreadsheets don't remind me, hard to track progress across weeks"
    results.append(result)

    # Check for balanced gains/pains (should be similar count)
    gains_pains_match = abs(len(gains) - len(pains)) <= 1  # Allow 1 difference
    result = {
        "description": "Balanced Gains and Pains (counts should match or be within 1)",
        "passed": gains_pains_match,
        "details": f"Gains: {len(gains)}, Pains: {len(pains)}"
    }
    if not gains_pains_match:
        result["trace"] = f"Current counts are unbalanced. For every task, ensure both **Gains:** AND **Pains:** are documented. Currently {len(gains)} gains vs {len(pains)} pains."
    results.append(result)

    # Check for stakeholder diversity
    stakeholder_keywords = r'\b(user|stakeholder|team|customer|admin|developer|product|manager|designer|engineer)\b'
    stakeholder_mentions = len(re.findall(stakeholder_keywords, content, re.IGNORECASE))
    has_stakeholder_diversity = stakeholder_mentions >= 5
    result = {
        "description": "Stakeholder diversity mentioned (5+ mentions of roles/personas)",
        "passed": has_stakeholder_diversity,
        "details": f"{stakeholder_mentions} stakeholder references found"
    }
    if not has_stakeholder_diversity:
        result["trace"] = "Identify diverse stakeholders (end users, admins, developers, product team). Use role names consistently throughout the document."
    results.append(result)

    # Check for success metrics/KPIs
    metric_keywords = r'\b(metric|kpi|target|goal|measure|reduce|increase|improve|percent|hour|time|cost|save)\b'
    metric_mentions = len(re.findall(metric_keywords, content, re.IGNORECASE))
    has_metrics = metric_mentions >= 5
    result = {
        "description": "Success metrics mentioned (5+ mentions, quantified where possible)",
        "passed": has_metrics,
        "details": f"{metric_mentions} metric-related words found"
    }
    if not has_metrics:
        result["trace"] = "Add quantifiable success metrics. Examples: 'reduce manual entry time by 50%', 'achieve 95% workout consistency', '2+ hours saved per week'"
    results.append(result)

    # Check for constraints/boundaries
    constraint_keywords = r'\b(constraint|boundary|limit|must|cannot|won\'t|exclude|scope|out of scope)\b'
    constraint_mentions = len(re.findall(constraint_keywords, content, re.IGNORECASE))
    has_constraints = constraint_mentions >= 3
    result = {
        "description": "Constraints and boundaries mentioned (3+)",
        "passed": has_constraints,
        "details": f"{constraint_mentions} constraint mentions found"
    }
    if not has_constraints:
        result["trace"] = "Document constraints and boundaries. Examples: 'Mobile-only (no web)', 'Offline-first design', 'iOS 15+ only'"
    results.append(result)

    # Check for assumptions documented
    assumption_keywords = r'\b(assume|assuming|assume|presume|expect|expected|given|based on|prerequisite)\b'
    assumption_mentions = len(re.findall(assumption_keywords, content, re.IGNORECASE))
    has_assumptions = assumption_mentions >= 2
    result = {
        "description": "Assumptions documented (2+)",
        "passed": has_assumptions,
        "details": f"{assumption_mentions} assumption mentions found"
    }
    if not has_assumptions:
        result["trace"] = "Document assumptions about users, technology, or market. Examples: 'Assume smartphone adoption is 80%+', 'Assume iOS 15+ support is acceptable'"
    results.append(result)

    # Check for use cases defined
    usecase_keywords = r'\b(use case|scenario|workflow|process|step|when|as a|given|then)\b'
    usecase_mentions = len(re.findall(usecase_keywords, content, re.IGNORECASE))
    has_usecases = usecase_mentions >= 8
    result = {
        "description": "Use cases/scenarios described (8+ relevant keywords)",
        "passed": has_usecases,
        "details": f"{usecase_mentions} use case keyword mentions found"
    }
    if not has_usecases:
        result["trace"] = "Define user workflows and scenarios. Use format: 'As a [role], I want to [action] so that [benefit].' or describe step-by-step workflows."
    results.append(result)

    # Check for accessibility/compliance mentioned
    accessibility_keywords = r'\b(accessibility|wcag|inclusive|disabled|screen reader|keyboard|compliance|gdpr|privacy|secure)\b'
    accessibility_mentions = len(re.findall(accessibility_keywords, content, re.IGNORECASE))
    has_accessibility = accessibility_mentions >= 2
    result = {
        "description": "Accessibility, compliance, or security considerations mentioned (2+)",
        "passed": has_accessibility,
        "details": f"{accessibility_mentions} accessibility/compliance references found"
    }
    if not has_accessibility:
        result["trace"] = "Consider and document: accessibility standards (WCAG AA), privacy regulations (GDPR), security requirements (encryption, auth)."
    results.append(result)

    # Check for placeholder content
    placeholder_patterns = [
        r'\bTBD\b', r'\bTODO\b', r'\bFIXME\b',
        r'edit this', r'fill in', r'\[PLACEHOLDER\]'
    ]
    found_placeholders = []
    for pattern in placeholder_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            found_placeholders.append({"pattern": pattern, "line": line_num})

    has_no_placeholders = len(found_placeholders) == 0
    result = {
        "description": "No placeholder content (TBD, TODO, FIXME, [PLACEHOLDER])",
        "passed": has_no_placeholders,
        "failures": found_placeholders if found_placeholders else None
    }
    if not has_no_placeholders:
        result["trace"] = f"Found {len(found_placeholders)} placeholder markers. Replace all with actual content before moving to PRD creation."
    results.append(result)

    # Check for sufficient detail
    content_quality = len(content) > 2000
    result = {
        "description": "Sufficient detail and completeness (≥2000 characters)",
        "passed": content_quality,
        "details": f"{len(content)} characters (target ≥2000)"
    }
    if not content_quality:
        result["trace"] = f"Document is {len(content)} characters (target ≥2000). Add more detailed user roles, tasks, gains, and pains."
    results.append(result)

    return results

def generate_html(requirements_file, results):
    """Generate HTML report."""
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    score = int((passed / total * 100)) if total > 0 else 0

    html = f'''<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Requirements Quality Evaluation - {Path(requirements_file).stem}</title>
    <style>
      body {{
        font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
        padding: 20px;
        background: #f5f5f5;
      }}
      h1 {{ color: #333; margin-top: 0; }}
      .score {{ font-size: 18px; font-weight: bold; margin: 20px 0; color: #228B22; }}
      table {{ border-collapse: collapse; width: 100%; background: white; margin-top: 20px; }}
      th, td {{ border: 1px solid #ccc; padding: 12px; text-align: left; }}
      th {{ background: #f0f0f0; font-weight: 600; }}
      .pass {{ color: #228B22; font-weight: 600; }}
      .fail {{ color: #ad0000; font-weight: 600; }}
      .details {{ font-size: 12px; color: #666; margin-top: 4px; font-weight: normal; }}
    </style>
  </head>
  <body>
    <h1>Requirements Quality Evaluation</h1>
    <div class="score">Score: {score}/100 ({passed}/{total} checks passed)</div>
    <table>
      <thead>
        <tr>
          <th>Evaluation Criterion</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
'''

    for result in results:
        status = "PASS" if result['passed'] else "FAIL"
        status_class = "pass" if result['passed'] else "fail"
        html += f'''        <tr>
          <td>
            <div>{result['description']}</div>'''

        # Add details if present
        if 'details' in result and result['details']:
            html += f'''<div class="details">{result['details']}</div>'''

        # Add trace if present (for failures)
        if not result['passed'] and 'trace' in result and result['trace']:
            html += f'''<div style="color: #ad0000; font-size: 12px; margin-top: 6px; padding: 6px; background: #fff5f5; border-left: 3px solid #ad0000; border-radius: 2px;">
            <strong>Why it failed:</strong> {result['trace']}
            </div>'''

        # Add detailed failure markers
        if 'failures' in result and result['failures']:
            html += '<div style="color: #ad0000; font-size: 12px; margin-top: 8px; padding: 8px; background: #fff5f5; border-radius: 4px;">'
            for failure in result['failures']:
                if isinstance(failure, dict) and 'line' in failure:
                    html += f'''<div style="margin-bottom: 4px;">Line {failure['line']}: {failure['pattern']}</div>'''
            html += '</div>'

        html += f'''
          </td>
          <td class="{status_class}">[{status}]</td>
        </tr>
'''

    html += '''      </tbody>
    </table>
  </body>
</html>
'''
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: eval-requirements.py <requirements_file>", file=sys.stderr)
        sys.exit(1)

    requirements_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = requirements_file.replace('.md', '-eval.html')

    # Check if file exists
    if not os.path.isfile(requirements_file):
        print(f"Error: Requirements file not found: {requirements_file}", file=sys.stderr)
        sys.exit(1)

    # Read content
    try:
        with open(requirements_file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading requirements file: {e}", file=sys.stderr)
        sys.exit(1)

    # Evaluate
    results = evaluate_requirements(content)
    html = generate_html(requirements_file, results)

    # Write output
    try:
        with open(output_file, 'w') as f:
            f.write(html)

        passed = sum(1 for r in results if r['passed'])
        total = len(results)
        score = int((passed / total * 100)) if total > 0 else 0
        print(f"✓ Requirements evaluation saved to {output_file}")
        print(f"Score: {score}/100 ({passed}/{total} checks passed)")
        
        # Delete EVAL.txt if it exists
        eval_file = "EVAL.txt"
        if os.path.isfile(eval_file):
            os.remove(eval_file)
            print(f"✓ Cleaned up {eval_file}")
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
