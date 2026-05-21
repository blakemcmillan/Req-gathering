#!/usr/bin/env python3
"""Test plan quality evaluator - validates against pragmatic SKILL.md approach."""

import sys
import os
import re
from pathlib import Path

def evaluate_test_plan(content):
    """Evaluate test plan against pragmatic SKILL.md requirements."""
    results = []

    # Check for required sections
    sections = [
        ("## Test Plan Overview", "Has Test Plan Overview section"),
        ("## Test Strategy", "Has Test Strategy section"),
        ("## Requirement Traceability", "Has Requirement Traceability Matrix"),
        ("## Test Cases", "Has Test Cases organized by category"),
    ]

    for pattern, description in sections:
        passed = pattern in content
        result = {
            "description": description,
            "pattern": pattern,
            "passed": passed
        }
        if not passed:
            result["trace"] = f"Section not found: looking for '{pattern}'"
        results.append(result)

    # Check that test categories are selective, not prescriptive
    # Look for headings like "### Unit Tests", "### Integration Tests", etc.
    unit_tests = "### Unit Test" in content or "### Unit test" in content
    integration_tests = "### Integration Test" in content
    e2e_tests = "### E2E Test" in content or "### End-to-End" in content
    edge_case_tests = "### Edge Case" in content
    performance_tests = "### Performance Test" in content

    categories_found = sum([unit_tests, integration_tests, e2e_tests, edge_case_tests, performance_tests])
    has_selective_categories = 1 <= categories_found <= 5
    result = {
        "description": f"Test categories are selective (1-5 categories, found {categories_found})",
        "passed": has_selective_categories,
        "details": f"Categories: {'Unit' if unit_tests else ''} {'Integration' if integration_tests else ''} {'E2E' if e2e_tests else ''} {'Edge Case' if edge_case_tests else ''} {'Performance' if performance_tests else ''}".strip()
    }
    if not has_selective_categories:
        if categories_found == 0:
            result["trace"] = "No test category headings found (look for ### Unit Tests, ### Integration Tests, etc.)"
        else:
            result["trace"] = f"Found {categories_found} categories. Expected 1-5. Add missing category headings or remove unused ones."
    results.append(result)

    # Check traceability matrix is concise (5-10 rows ideally, not exhaustive)
    matrix_match = re.search(r'\|.*REQ.*\|.*\n(\|.*\n)+', content)
    if matrix_match:
        matrix_text = matrix_match.group()
        row_count = matrix_text.count('\n') - 2  # Subtract header and separator rows
        is_concise = 5 <= row_count <= 25  # Allow up to 25 for larger specs
        result = {
            "description": f"Traceability matrix is concise ({row_count} rows, ideally 5-10)",
            "passed": is_concise,
            "details": f"{row_count} requirement rows in matrix"
        }
        if not is_concise:
            if row_count < 5:
                result["trace"] = f"Matrix too small ({row_count} rows). Add more requirements or split into multiple tables."
            else:
                result["trace"] = f"Matrix is large ({row_count} rows). Consider splitting into smaller, focused tables for readability."
        results.append(result)
    else:
        results.append({
            "description": "Traceability matrix is concise",
            "passed": False,
            "details": "Matrix not found or malformed",
            "trace": "No traceability matrix found. Add a table with | REQ-ID | Feature | ... | headers and content rows."
        })

    # Check test case density (should be 1-5 per requirement, not fixed 3:1)
    req_pattern = r'REQ-[A-Z]+-\d+'
    test_case_pattern = r'TC-[A-Z]+-\d+|test case|Test Case'

    requirements = set(re.findall(req_pattern, content))
    test_cases = re.findall(test_case_pattern, content, re.IGNORECASE)

    if len(requirements) > 0:
        ratio = len(test_cases) / len(requirements)
        has_pragmatic_density = 0.5 <= ratio <= 7  # Allow some flexibility
        result = {
            "description": f"Test case density is pragmatic (ratio {ratio:.1f}:1, target 1-5:1)",
            "passed": has_pragmatic_density,
            "details": f"{len(test_cases)} test cases for {len(requirements)} requirements"
        }
        if not has_pragmatic_density:
            if ratio < 0.5:
                result["trace"] = f"Too few test cases ({len(test_cases)} for {len(requirements)} requirements). Add more test cases to achieve 1-5:1 coverage."
            else:
                result["trace"] = f"Too many test cases ({len(test_cases)} for {len(requirements)} requirements). Consider consolidating or removing redundant tests."
        results.append(result)
    else:
        results.append({
            "description": "Test case density is pragmatic",
            "passed": False,
            "details": "No requirements found (REQ- pattern)",
            "trace": "No requirements found using REQ-* pattern. Add requirement identifiers like REQ-TIMER-01, REQ-FEATURE-02, etc."
        })

    # Check for ownership clarity (Dev, QA, DevOps)
    has_ownership = bool(re.search(r'(Dev Team|Dev\b|QA Team|QA\b|DevOps|Ownership|Owned by)', content, re.IGNORECASE))
    result = {
        "description": "Test Strategy specifies ownership (Dev/QA/DevOps)",
        "passed": has_ownership
    }
    if not has_ownership:
        result["trace"] = "No ownership definition found. Add 'Dev Team:', 'QA Team:', 'DevOps', or 'Owned by' to Test Strategy section."
    results.append(result)

    # Check for execution timing (pre-commit, post-merge, nightly, etc.)
    has_timing = bool(re.search(r'(pre-commit|post-merge|nightly|weekly|on-demand|execution timing)', content, re.IGNORECASE))
    result = {
        "description": "Test Strategy specifies execution timing",
        "passed": has_timing
    }
    if not has_timing:
        result["trace"] = "No execution timing found. Add 'pre-commit', 'post-merge', 'nightly', 'weekly', or 'on-demand' to Test Strategy section."
    results.append(result)

    # Check for no placeholder text
    placeholder_patterns = [
        r'\bTBD\b', r'\bTODO\b', r'\bFIXME\b',
        r'edit this', r'fill in', r'\[PLACEHOLDER\]'
    ]
    found_placeholders = []
    for pattern in placeholder_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            line_num = content[:match.start()].count('\n') + 1
            context = content[max(0, match.start()-40):min(len(content), match.end()+40)].replace('\n', ' ')
            found_placeholders.append({
                "pattern": pattern,
                "line": line_num,
                "context": context.strip()
            })

    has_placeholders = len(found_placeholders) > 0
    results.append({
        "description": "No placeholder content (TBD, TODO, FIXME)",
        "passed": not has_placeholders,
        "failures": found_placeholders if has_placeholders else None
    })

    # Check for sufficient detail (test cases should have Given/When/Then or strategy)
    has_gherkin = bool(re.search(r'\bGiven\b|\bWhen\b|\bThen\b', content, re.IGNORECASE))
    has_test_strategy = bool(re.search(r'Test:|Inputs:|Expected:|Requirement:', content))
    has_test_detail = has_gherkin or has_test_strategy
    result = {
        "description": "Test cases use clear format (Gherkin or strategy)",
        "passed": has_test_detail
    }
    if not has_test_detail:
        result["trace"] = "No clear test format found. Use Gherkin (Given/When/Then) or structured format (Test:, Inputs:, Expected:, Requirement:)."
    results.append(result)

    # Check for effort estimate if applicable
    has_effort = bool(re.search(r'(effort|hours?|estimate|duration|time)', content, re.IGNORECASE))
    result = {
        "description": "Effort estimate provided (hours/team/effort)",
        "passed": has_effort
    }
    if not has_effort:
        result["trace"] = "No effort estimate found. Add effort/hours/estimate/duration to help with planning."
    results.append(result)

    return results

def generate_html(test_plan_file, results):
    """Generate HTML report."""
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    score = int((passed / total * 100)) if total > 0 else 0

    html = f'''<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Test Plan Quality Evaluation - {Path(test_plan_file).stem}</title>
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
    <h1>Test Plan Quality Evaluation</h1>
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

        # Add detailed failure markers (for placeholders)
        if 'failures' in result and result['failures']:
            html += '<div style="color: #ad0000; font-size: 12px; margin-top: 8px; padding: 8px; background: #fff5f5; border-radius: 4px;">'
            for failure in result['failures']:
                if isinstance(failure, dict) and 'line' in failure:
                    html += f'''<div style="margin-bottom: 6px;">
              <strong>Line {failure['line']}:</strong> {failure['pattern']}<br/>
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
        print("Usage: eval-test-plan.py <test_plan_file> [output_file]", file=sys.stderr)
        sys.exit(1)

    test_plan_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = test_plan_file.replace('.md', '-eval.html')

    # Check if file exists
    if not os.path.isfile(test_plan_file):
        print(f"Error: Test plan file not found: {test_plan_file}", file=sys.stderr)
        sys.exit(1)

    # Read content
    try:
        with open(test_plan_file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading test plan file: {e}", file=sys.stderr)
        sys.exit(1)

    # Evaluate
    results = evaluate_test_plan(content)
    html = generate_html(test_plan_file, results)

    # Write output
    try:
        with open(output_file, 'w') as f:
            f.write(html)
 
        passed = sum(1 for r in results if r['passed'])
        total = len(results)
        score = int((passed / total * 100)) if total > 0 else 0
        print(f"✓ Test plan evaluation saved to {output_file}")
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
