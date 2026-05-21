#!/usr/bin/env python3
"""PRD quality evaluator - simple checks without promptfoo complexity."""

import sys
import os
import re
from pathlib import Path

def evaluate_prd(prd_content):
    """Evaluate PRD against quality criteria."""
    results = []

    # Check for required sections
    sections = [
        ("## Goals", "Has Goals section"),
        ("## Overview", "Has Overview section"),
        ("## Requirements", "Has Requirements section"),
        ("### Functional Requirements", "Has Functional Requirements"),
        ("### Non-Functional Requirements", "Has Non-Functional Requirements"),
        ("## Constraints", "Has Constraints section"),
        ("### Technical Constraints", "Has Technical Constraints"),
        ("### Business Constraints", "Has Business Constraints"),
        ("## Success Metrics", "Has Success Metrics section"),
        ("## Edge Cases", "Has Edge Cases section"),
    ]

    for pattern, description in sections:
        passed = pattern in prd_content
        results.append({
            "description": description,
            "pattern": pattern,
            "passed": passed
        })

    # Check for no placeholder text
    placeholder_patterns = [
        r'\bTBD\b', r'\bTODO\b', r'\bFIXME\b',
        r'edit this', r'fill in', r'placeholder', r'\bgeneric\b'
    ]
    found_placeholders = []
    for pattern in placeholder_patterns:
        matches = re.finditer(pattern, prd_content, re.IGNORECASE)
        for match in matches:
            line_num = prd_content[:match.start()].count('\n') + 1
            context = prd_content[max(0, match.start()-50):min(len(prd_content), match.end()+50)].replace('\n', ' ')
            found_placeholders.append({
                "pattern": pattern,
                "line": line_num,
                "context": context.strip()
            })

    has_placeholders = len(found_placeholders) > 0
    results.append({
        "description": "No placeholder or generic content",
        "passed": not has_placeholders,
        "failures": found_placeholders if has_placeholders else None
    })

    # Check for sufficient detail/length
    content_quality = len(prd_content) > 5000  # Arbitrary minimum for "detailed"
    results.append({
        "description": "Sufficient detail (>5000 chars)",
        "passed": content_quality
    })

    # Check for quantified metrics
    has_metrics = bool(re.search(r'\d+%|\d+s|\d+ms|\$\d+|<\d+|>\d+', prd_content))
    results.append({
        "description": "Contains quantified metrics",
        "passed": has_metrics
    })

    return results

def generate_html(prd_file, results):
    """Generate HTML report."""
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    score = int((passed / total * 100)) if total > 0 else 0

    html = f'''<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>PRD Quality Evaluation - {Path(prd_file).stem}</title>
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
    </style>
  </head>
  <body>
    <h1>PRD Quality Evaluation</h1>
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

        # Add failure details if present
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
        print("Usage: eval-prd.py <prd_file> [output_file]", file=sys.stderr)
        sys.exit(1)

    prd_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = prd_file.replace('.md', '-eval.html')

    # Check if PRD file exists
    if not os.path.isfile(prd_file):
        print(f"Error: PRD file not found: {prd_file}", file=sys.stderr)
        sys.exit(1)

    # Read PRD content
    try:
        with open(prd_file, 'r') as f:
            prd_content = f.read()
    except Exception as e:
        print(f"Error reading PRD file: {e}", file=sys.stderr)
        sys.exit(1)

    # Evaluate
    results = evaluate_prd(prd_content)
    html = generate_html(prd_file, results)

    # Write output
    try:
        with open(output_file, 'w') as f:
            f.write(html)

        passed = sum(1 for r in results if r['passed'])
        total = len(results)
        score = int((passed / total * 100)) if total > 0 else 0
        print(f"✓ PRD evaluation saved to {output_file}")
        print(f"Score: {score}/100 ({passed}/{total} checks passed)")
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
