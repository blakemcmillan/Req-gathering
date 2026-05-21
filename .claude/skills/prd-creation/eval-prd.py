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
        (r"##\s+\d+\.\s+Product Overview|## Product Overview", "Has Product Overview section"),
        (r"##\s+\d+\.\s+Goals|## Goals", "Has Goals & Non-Goals section"),
        (r"##\s+\d+\.\s+User Roles|## User Roles", "Has User Roles & Needs section"),
        (r"##\s+\d+\.\s+Features|## Features", "Has Features & How They Solve Needs section"),
        (r"##\s+\d+\.\s+Non-Functional|## Non-Functional", "Has Product-Wide Non-Functional Requirements"),
        (r"##\s+\d+\.\s+Success Metrics|## Success Metrics", "Has Product-Wide Success Metrics"),
        (r"##\s+\d+\.\s+Open Questions|## Open Questions", "Has Open Questions section"),
    ]

    for pattern, description in sections:
        passed = bool(re.search(pattern, prd_content))
        result = {
            "description": description,
            "pattern": pattern,
            "passed": passed
        }
        if not passed:
            # Extract a more readable version of the section name
            section_name = description.split("Has ")[1].split(" section")[0] if "Has " in description else "required section"
            result["trace"] = f"Section '{section_name}' not found. Add this section to the PRD."
        results.append(result)

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
        result = {
            "description": f"All {len(features)} features have 'Solves For' traceability",
            "passed": has_feature_traceability,
            "details": f"{features_with_traceability}/{len(features)} features traced"
        }
        if not has_feature_traceability:
            missing = len(features) - features_with_traceability
            result["trace"] = f"Missing traceability on {missing} feature(s). Add '**Solves For:**' section to each feature explaining which user roles, tasks, gains, or pains it addresses."
        results.append(result)
    else:
        results.append({
            "description": "Features documented with traceability",
            "passed": False,
            "trace": "No features found. Add features using '### Feature: [name]' headings to the Features section."
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
    result = {
        "description": "No placeholder content (TBD, TODO, FIXME)",
        "passed": not has_placeholders,
        "failures": found_placeholders if has_placeholders else None
    }
    if has_placeholders:
        result["trace"] = f"Found {len(found_placeholders)} placeholder marker(s). Replace all TBD, TODO, FIXME with actual content."
    results.append(result)

    # Check for sufficient detail/length
    content_quality = len(prd_content) > 4000
    result = {
        "description": "Sufficient detail and completeness",
        "passed": content_quality
    }
    if not content_quality:
        result["trace"] = f"PRD is {len(prd_content)} characters (target ≥4000). Add more detail to features, acceptance criteria, and non-functional requirements."
    results.append(result)

    # Check for quantified metrics specifically in Success Metrics section
    success_metrics = re.search(r'## Success Metrics.*?(?=##|\Z)', prd_content, re.DOTALL)
    if success_metrics:
        metrics_text = success_metrics.group()
        has_metrics = bool(re.search(r'\d+%|\d+\s*(users?|tasks?|sessions?|hours?|minutes?|days?|seconds?)', metrics_text, re.IGNORECASE))
    else:
        has_metrics = False

    result = {
        "description": "Success Metrics section contains quantified targets",
        "passed": has_metrics
    }
    if not has_metrics:
        if not success_metrics:
            result["trace"] = "Success Metrics section not found or empty. Add quantified targets like '90% success rate', '10 sessions/day', '5% error reduction'."
        else:
            result["trace"] = "Success Metrics section lacks quantification. Replace generic goals with specific targets: percentages, counts, time periods, or thresholds."
    results.append(result)

    # Check that Goals section explicitly covers non-goals
    goals_section = re.search(r'## Goals.*?(?=##|\Z)', prd_content, re.DOTALL)
    if goals_section:
        has_non_goals = bool(re.search(r'non-goal|non[- ]goal|\bnot\b.*building|out of scope|explicitly not',
                                      goals_section.group(), re.IGNORECASE))
    else:
        has_non_goals = False

    result = {
        "description": "Goals section explicitly covers Non-Goals",
        "passed": has_non_goals
    }
    if not has_non_goals:
        if not goals_section:
            result["trace"] = "Goals section not found. Add '## Goals' section with both what you WILL build and what you WON'T build."
        else:
            result["trace"] = "Goals section missing Non-Goals. Add subsection '### Non-Goals' or list 'Out of scope:' items to clarify boundaries."
    results.append(result)

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
