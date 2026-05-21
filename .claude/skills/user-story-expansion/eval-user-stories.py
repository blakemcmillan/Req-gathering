#!/usr/bin/env python3
"""User Story & Gherkin quality evaluator - deterministic engineering guardrails."""

import sys
import os
import re
from pathlib import Path

def evaluate_user_stories(content):
    """Evaluate User Story artifact against runtime deterministic criteria."""
    results = []

    # 1. Check for required structural sections
    sections = [
        ("## Overview", "Has Epic/Feature Overview section"),
        ("## User Stories", "Has User Stories section"),
        ("As a", "Contains standard 'As a' role definition structure"),
        ("I want to", "Contains standard 'I want to' action definition structure"),
        ("So that", "Contains standard 'So that' business value structure"),
        ("### Gherkin Acceptance Criteria", "Has Gherkin Acceptance Criteria section"),
    ]

    for pattern, description in sections:
        passed = pattern.lower() in content.lower()
        results.append({
            "description": description,
            "pattern": pattern,
            "passed": passed
        })

    # 2. Check for no placeholder text (Stops open questions from being processed)
    placeholder_patterns = [
        r'\bTBD\b', r'\bTODO\b', r'\bFIXME\b',
        r'edit this', r'fill in', r'placeholder', r'\bgeneric\b',
        r'\[insert', r'open question'
    ]
    found_placeholders = []
    for pattern in placeholder_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            context = content[max(0, match.start()-50):min(len(content), match.end()+50)].replace('\n', ' ')
            found_placeholders.append({
                "pattern": pattern,
                "line": line_num,
                "context": context.strip()
            })

    has_placeholders = len(found_placeholders) > 0
    results.append({
        "description": "Clean of placeholders or open/unresolved requirements",
        "passed": not has_placeholders,
        "failures": found_placeholders if has_placeholders else None
    })

    # 3. Check for Traceability (Enforcing link back to requirements or PRD tags)
    # Checks for brackets like [REQ-001] or [FR-12]
    has_traceability = bool(re.search(r'\[REQ-\d+\]|\[FR-\d+\]|\[NFR-\d+\]', content, re.IGNORECASE))
    results.append({
        "description": "Traceability verified (Links to source Requirement IDs, e.g., [REQ-001])",
        "passed": has_traceability
    })

    # 4. Anti-Bloat Guardrail: Check Scenario Density (Stops Token Waste)
    scenarios = re.findall(r'(?i)\b(Scenario:|Scenario Outline:)\b', content)
    scenario_count = len(scenarios)
    
    # We want thorough ACs, but anything over 12 scenarios per feature file usually indicates looping/bloat
    bloat_pass = scenario_count <= 12 and scenario_count > 0
    bloat_failures = []
    if scenario_count > 12:
        bloat_failures.append({
            "pattern": "Scenario Overloading",
            "line": 0,
            "context": f"Generated {scenario_count} scenarios. Limit to a maximum of 12 per run to prevent token waste."
        })
    elif scenario_count == 0:
        bloat_failures.append({
            "pattern": "Missing Scenarios",
            "line": 0,
            "context": "No Gherkin scenarios detected in the file."
        })

    results.append({
        "description": f"Optimal Scenario Count (Found: {scenario_count}, Cap: 12 to prevent token waste)",
        "passed": bloat_pass,
        "failures": bloat_failures if not bloat_pass else None
    })

    # 5. Gherkin Syntax Integrity Check
    has_gherkin_syntax = all(kw in content.lower() for kw in ["given ", "when ", "then "])
    results.append({
        "description": "Valid Gherkin syntax verified (Contains Given, When, Then statements)",
        "passed": has_gherkin_syntax
    })

    return results

def generate_html(user_story_file, results):
    """Generate HTML dashboard mirroring Andrei's layout rules."""
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    score = int((passed / total * 100)) if total > 0 else 0

    html = f'''<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>User Story Quality Evaluation - {Path(user_story_file).stem}</title>
    <style>
      body {{
        font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
        padding: 20px;
        background: #f5f5f5;
      }}
      h1 {{ color: #333; margin-top: 0; }}
      .score {{ font-size: 18px; font-weight: bold; margin: 20px 0; color: #0066cc; }}
      table {{ border-collapse: collapse; width: 100%; background: white; margin-top: 20px; }}
      th, td {{ border: 1px solid #ccc; padding: 12px; text-align: left; }}
      th {{ background: #f0f0f0; font-weight: 600; }}
      .pass {{ color: #228B22; font-weight: 600; }}
      .fail {{ color: #ad0000; font-weight: 600; }}
    </style>
  </head>
  <body>
    <h1>User Story & Acceptance Criteria Quality Evaluation</h1>
    <div class="score">Score: {score}/100 ({passed}/{total} checks passed)</div>
    <table>
      <thead>
        <tr>
          <th>User Story / Gherkin Verification Criterion</th>
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

        if 'failures' in result and result['failures']:
            html += '<div style="color: #ad0000; font-size: 12px; margin-top: 8px; padding: 8px; background: #fff5f5; border-radius: 4px;">'
            for failure in result['failures']:
                line_str = f"Line {failure['line']}: " if failure['line'] > 0 else ""
                html += f'''<div style="margin-bottom: 6px;">
              <strong>{line_str}</strong>{failure['pattern']}<br/>
              <code style="display: block; margin-top: 4px; padding: 4px; background: white; border-left: 2px solid #ad0000;">...{failure['context']}...</code>
            </div>'''
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
        print("Usage: eval-user-stories.py <story_file> [output_file]", file=sys.stderr)
        sys.exit(1)

    story_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else story_file.replace('.md', '-eval.html')

    if not os.path.isfile(story_file):
        print(f"Error: User Story file not found: {story_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(story_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    results = evaluate_user_stories(content)
    html = generate_html(story_file, results)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)

        passed = sum(1 for r in results if r['passed'])
        total = len(results)
        score = int((passed / total * 100)) if total > 0 else 0
        print(f"✓ User Story evaluation saved to {output_file}")
        print(f"Score: {score}/100 ({passed}/{total} checks passed)")
        
        # If any major runtime guardrail fails, exit with error so hook can notify model
        if passed < total:
            sys.exit(1)
            
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
