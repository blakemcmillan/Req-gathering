#!/usr/bin/env python3
"""PRD quality evaluator - validates against SKILL.md structure."""

import sys
import os
import re
from pathlib import Path

def evaluate_prd(prd_content):
    """Evaluate PRD against SKILL.md structure requirements."""
    results = []

    # Check for required top-level sections per SKILL.md output structure
    sections = [
        ("## Product Overview", "Has Product Overview section"),
        ("## Goals", "Has Goals & Non-Goals section"),
        ("## User Roles", "Has User Roles & Needs section"),
        ("## Features", "Has Features & How They Solve Needs section"),
        ("## Non-Functional Requirements", "Has Product-Wide Non-Functional Requirements"),
        ("## Success Metrics", "Has Product-Wide Success Metrics"),
        ("## Open Questions", "Has Open Questions section"),
    ]

    for pattern, description in sections:
        passed = pattern in prd_content
        results.append({
            "description": description,
            "pattern": pattern,
            "passed": passed
        })

    # Check for features with "Solves For" traceability (SKILL.md line 128)
    feature_matches = re.finditer(r'###\s+\*?\*?Feature:', prd_content, re.IGNORECASE)
    features = list(feature_matches)

    if len(features) > 0:
        features_with_traceability = 0
        for i, feature_match in enumerate(features):
            # Extract feature section (from this feature to next or end)
            start = feature_match.start()
            if i + 1 < len(features):
                end = features[i + 1].start()
            else:
                end = len(prd_content)

            feature_section = prd_content[start:end]
            # Check for "Solves For" in this feature section
            if re.search(r'\*\*Solves For\*\*:?', feature_section, re.IGNORECASE):
                features_with_traceability += 1

        has_feature_traceability = features_with_traceability == len(features)
        results.append({
            "description": f"All {len(features)} features have 'Solves For' traceability",
            "passed": has_feature_traceability,
            "details": f"{features_with_traceability}/{len(features)} features traced"
        })
    else:
        results.append({
            "description": "Features documented with traceability",
            "passed": False
        })

    # Check for no placeholder text
    placeholder_patterns = [
        r'\bTBD\b', r'\bTODO\b', r'\bFIXME\b',
        r'edit this', r'fill in', r'\[PLACEHOLDER\]'
    ]
    found_placeholders = []
    for pattern in placeholder_patterns:
        matches = re.finditer(pattern, prd_content, re.IGNORECASE)
        for match in matches:
            line_num = prd_content[:match.start()].count('\n') + 1
            context = prd_content[max(0, match.start()-40):min(len(prd_content), match.end()+40)].replace('\n', ' ')
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

    # Check for sufficient detail/length
    content_quality = len(prd_content) > 4000
    results.append({
        "description": "Sufficient detail and completeness",
        "passed": content_quality
    })

    # Check for quantified metrics specifically in Success Metrics section
    success_metrics = re.search(r'## Success Metrics.*?(?=##|\Z)', prd_content, re.DOTALL)
    if success_metrics:
        metrics_text = success_metrics.group()
        has_metrics = bool(re.search(r'\d+%|\d+\s*(users?|tasks?|sessions?|hours?|minutes?|days?|seconds?)', metrics_text, re.IGNORECASE))
    else:
        has_metrics = False

    results.append({
        "description": "Success Metrics section contains quantified targets",
        "passed": has_metrics
    })

    # Check that Goals section explicitly covers non-goals
    goals_section = re.search(r'## Goals.*?(?=##|\Z)', prd_content, re.DOTALL)
    if goals_section:
        has_non_goals = bool(re.search(r'non-goal|non[- ]goal|\bnot\b.*building|out of scope|explicitly not',
                                      goals_section.group(), re.IGNORECASE))
    else:
        has_non_goals = False

    results.append({
        "description": "Goals section explicitly covers Non-Goals",
        "passed": has_non_goals
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
      .details {{ font-size: 12px; color: #666; margin-top: 4px; font-weight: normal; }}
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

        # Add details if present
        if 'details' in result and result['details']:
            html += f'''<div class="details">{result['details']}</div>'''

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
