#!/usr/bin/env python3
"""User Story quality evaluator - validates against SKILL.md structure requirements."""

import sys
import os
import re
from pathlib import Path

def evaluate_user_stories(content):
    """Evaluate user stories against SKILL.md requirements."""
    results = []

    # Check for required top-level sections
    sections = [
        (r"# User Stories", "Has main title"),
        (r"## Feature Code Legend", "Has Feature Code Legend section (maps codes to features)"),
        (r"# FEATURE:", "Has feature sections (at least one)"),
    ]

    for pattern, description in sections:
        passed = bool(re.search(pattern, content, re.IGNORECASE))
        result = {
            "description": description,
            "pattern": pattern,
            "passed": passed
        }
        if not passed:
            result["trace"] = f"Section not found. Add this section to the user stories document."
        results.append(result)

    # Check for user story ID format (US-[PROJ]-[FEATURE]-[NUMBER])
    user_story_ids = re.findall(r'US-[A-Z]{2,3}-[A-Z]+-\d+', content)
    has_user_stories = len(user_story_ids) > 0
    
    result = {
        "description": f"User stories follow strict ID format (US-[PROJ]-[FEATURE]-[NUM])",
        "passed": has_user_stories,
        "details": f"{len(user_story_ids)} user stories found"
    }
    if not has_user_stories:
        result["trace"] = "No user story IDs found. Use format: US-HT-PLAN-01, US-FL-TOGGLE-01 (2-3 letter project code, feature name, number)."
    results.append(result)

    # Check for acceptance criteria with strict format (AC-[PROJ]-[FEATURE]-[NUM]-[SCENARIO])
    ac_ids = re.findall(r'AC-[A-Z]{2,3}-[A-Z]+-\d+-\d+', content)
    has_acceptance_criteria = len(ac_ids) > 0
    
    result = {
        "description": f"Acceptance criteria follow strict ID format (AC-[PROJ]-[FEATURE]-[NUM]-[SCENARIO])",
        "passed": has_acceptance_criteria,
        "details": f"{len(ac_ids)} acceptance criteria found"
    }
    if not has_acceptance_criteria:
        result["trace"] = "No acceptance criteria IDs found. Use format: AC-HT-PLAN-01-01, AC-FL-TOGGLE-01-02 (project code, feature, story number, scenario number)."
    results.append(result)

    # Check for required acceptance criteria scenarios (per SKILL.md line 51-71)
    # AC-01: Happy Path, AC-02: Fast-Test Mode, AC-03: Boundary/Edge Case, AC-04+: NFR/Constraints
    has_happy_path = bool(re.search(r'AC-[A-Z0-9]+-01.*Happy Path', content, re.IGNORECASE))
    has_fast_test = bool(re.search(r'AC-[A-Z0-9]+-02.*Fast-Test Mode|ENVIRONMENT\s*=\s*["\']?test', content, re.IGNORECASE))
    has_boundary = bool(re.search(r'AC-[A-Z0-9]+-03.*Boundary Condition|AC-[A-Z0-9]+-03.*Edge Case', content, re.IGNORECASE))
    has_nfr = bool(re.search(r'AC-[A-Z0-9]+-04', content, re.IGNORECASE))

    result = {
        "description": "Acceptance criteria follow SKILL.md structure (AC-01 Happy Path, AC-02 Fast-Test, AC-03 Boundary, AC-04+ NFR)",
        "passed": has_happy_path and has_fast_test and has_boundary,
        "details": f"Happy Path: {has_happy_path}, Fast-Test: {has_fast_test}, Boundary: {has_boundary}, NFR: {has_nfr}"
    }
    if not (has_happy_path and has_fast_test and has_boundary):
        result["trace"] = "Missing required acceptance criteria patterns. Each user story should have: AC-XX-01 (Happy Path), AC-XX-02 (Fast-Test Mode with ENVIRONMENT=test), AC-XX-03 (Boundary Condition)."
    results.append(result)

    # Check for Gherkin format (Given/When/Then) in acceptance criteria
    gherkin_keywords = r'Given|When|Then|And'
    gherkin_matches = len(re.findall(gherkin_keywords, content, re.IGNORECASE))
    has_gherkin = gherkin_matches >= 10  # Expect multiple Gherkin structures
    
    result = {
        "description": "Acceptance criteria use strict Gherkin format (Given/When/Then/And)",
        "passed": has_gherkin,
        "details": f"{gherkin_matches} Gherkin keywords found"
    }
    if not has_gherkin:
        result["trace"] = "Insufficient Gherkin format. Each acceptance criterion MUST follow: **Given** [state], **When** [action], **Then** [result], **And** [constraint]."
    results.append(result)

    # Check for user story structure (As a / I want to / So that)
    as_a_count = len(re.findall(r'\*\*As a\*\*', content))
    i_want_count = len(re.findall(r'\*\*I want to\*\*', content))
    so_that_count = len(re.findall(r'\*\*So that\*\*', content))
    
    has_proper_stories = as_a_count > 0 and i_want_count > 0 and so_that_count > 0
    story_counts_match = as_a_count == i_want_count == so_that_count
    
    result = {
        "description": "User stories follow strict format (**As a** / **I want to** / **So that**)",
        "passed": has_proper_stories and story_counts_match,
        "details": f"**As a**: {as_a_count}, **I want to**: {i_want_count}, **So that**: {so_that_count}"
    }
    if not has_proper_stories or not story_counts_match:
        result["trace"] = "User story structure mismatch. Each story MUST have: '**As a** [role]', '**I want to** [action]', '**So that** [quantifiable value]'. Count should match."
    results.append(result)

    # Check for Feature Code Legend with proper table format
    has_legend_table = bool(re.search(r'\| Code \| Feature \| User Role \||\| Code.*Feature.*Role', content))
    result = {
        "description": "Feature Code Legend includes table mapping codes to features and roles (SKILL.md requirement)",
        "passed": has_legend_table
    }
    if not has_legend_table:
        result["trace"] = "Missing or malformed Feature Code Legend. Add a table: | Code | Feature | User Role | with entries like | PLAN | Smart Workout Planning | Workout Newbie |"
    results.append(result)

    # Check for PRD Reference in each user story (per SKILL.md line 42)
    prd_references = len(re.findall(r'\*\*PRD Reference:\*\*', content))
    user_story_count = len(user_story_ids)
    has_traceability = prd_references > 0 and (prd_references >= user_story_count * 0.9)  # 90% of stories have reference
    
    result = {
        "description": "User stories include **PRD Reference** linking back to requirements",
        "passed": has_traceability,
        "details": f"{prd_references} PRD references for {user_story_count} stories"
    }
    if not has_traceability:
        result["trace"] = f"Missing PRD references. Each user story MUST include '**PRD Reference:** [Feature from PRD]' to establish traceability (per SKILL.md line 42)."
    results.append(result)

    # Check for Story IDs in each user story (per SKILL.md line 43)
    story_ids = len(re.findall(r'\*\*Story ID:\*\*', content))
    has_story_ids = story_ids > 0 and (story_ids >= user_story_count * 0.9)
    
    result = {
        "description": "User stories include **Story ID** field with correct format",
        "passed": has_story_ids,
        "details": f"{story_ids} Story IDs found"
    }
    if not has_story_ids:
        result["trace"] = "Missing Story IDs. Each user story MUST include '**Story ID:** US-[PROJ]-[FEATURE]-[NUM]'."
    results.append(result)

    # Check for Fast-Test Mode specifically (ENVIRONMENT=test per SKILL.md line 58)
    fast_test_env = len(re.findall(r'ENVIRONMENT\s*=\s*["\']?test["\']?', content, re.IGNORECASE))
    has_fast_test_env = fast_test_env > 0
    
    result = {
        "description": "Fast-Test Mode scenarios explicitly use ENVIRONMENT=test (per SKILL.md line 58)",
        "passed": has_fast_test_env,
        "details": f"{fast_test_env} ENVIRONMENT=test references found"
    }
    if not has_fast_test_env:
        result["trace"] = "Missing ENVIRONMENT=test in Fast-Test Mode ACs. AC-02 scenarios MUST include: 'Given the application configuration is executing under an active testing flag (ENVIRONMENT=test)'."
    results.append(result)

    # Check for boundary/edge case scenarios (per SKILL.md line 63-66)
    boundary_scenarios = len(re.findall(r'Boundary Condition.*Edge Case|AC-[A-Z0-9]+-03', content, re.IGNORECASE))
    has_edge_cases = boundary_scenarios > 0
    
    result = {
        "description": "Boundary Condition / Edge Case scenarios present (AC-03 per SKILL.md)",
        "passed": has_edge_cases,
        "details": f"{boundary_scenarios} boundary condition scenarios found"
    }
    if not has_edge_cases:
        result["trace"] = "Missing edge case coverage. AC-03 MUST cover: empty arrays, missing payloads, network failures, invalid inputs (per SKILL.md line 63-66)."
    results.append(result)

    # Check for NFR/System Constraint scenarios (per SKILL.md line 68-71)
    nfr_scenarios = len(re.findall(r'AC-[A-Z0-9]+-04|NFR|Non-Functional|performance|security|hardware|permission', content, re.IGNORECASE))
    has_nfr_scenarios = nfr_scenarios > 0
    
    result = {
        "description": "NFR / System Constraint scenarios present (AC-04+ per SKILL.md)",
        "passed": has_nfr_scenarios,
        "details": f"{nfr_scenarios} NFR/constraint references found"
    }
    if not has_nfr_scenarios:
        result["trace"] = "Missing NFR scenarios. AC-04+ MUST cover non-functional requirements: launch time, CPU usage, permissions, memory (per SKILL.md line 68-71)."
    results.append(result)

    # Check for no standalone NFR stories (per SKILL.md line 76)
    # Count user stories that only have "NFR" or "Performance" etc in title without a core feature
    has_standalone_nfr = bool(re.search(r'## [A-Z ]*(?:Performance|Security|NFR|Non-Functional|Permission|Constraint)\b', content, re.IGNORECASE))
    
    result = {
        "description": "No standalone NFR user stories (NFRs are ACs within feature stories per SKILL.md line 76)",
        "passed": not has_standalone_nfr
    }
    if has_standalone_nfr:
        result["trace"] = "Found standalone NFR stories. Per SKILL.md: 'Never create independent user stories for NFRs.' These must be AC-04+ within feature stories (per line 76)."
    results.append(result)

    # Check for placeholder content (TBD, TODO, FIXME)
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
    result = {
        "description": "No placeholder content (TBD, TODO, FIXME, [PLACEHOLDER])",
        "passed": not has_placeholders,
        "failures": found_placeholders if has_placeholders else None
    }
    if has_placeholders:
        result["trace"] = f"Found {len(found_placeholders)} placeholder markers. Per SKILL.md 'Zero Scope Innovation': replace all with actual content."
    results.append(result)

    # Check for sufficient detail
    content_quality = len(content) > 5000
    result = {
        "description": "Sufficient detail and completeness (≥5000 characters)",
        "passed": content_quality
    }
    if not content_quality:
        result["trace"] = f"Document is {len(content)} characters (target ≥5000). Add more detailed acceptance criteria, boundary conditions, and NFR scenarios."
    results.append(result)

    # Check for scannability (no verbose paragraphs per SKILL.md line 79)
    has_prose_blocks = len(re.findall(r'\n\n[A-Za-z]+.*\n[A-Za-z]+.*\n[A-Za-z]+', content)) > 5
    result = {
        "description": "Dense Markdown block structure (scannability per SKILL.md line 79)",
        "passed": not has_prose_blocks
    }
    if has_prose_blocks:
        result["trace"] = "Found verbose prose blocks. Per SKILL.md: 'Maintain pristine, dense Markdown block structures.' Use tables and lists, not paragraphs."
    results.append(result)

    # Check for consolidated bidirectional actions (no splitting per SKILL.md line 36)
    # This is harder to automate, but check for suspicious On/Off or Start/Stop being separate stories
    bidirectional_words = [
        (r'.*on.*', r'.*off.*'),
        (r'.*start.*', r'.*stop.*'),
        (r'.*create.*', r'.*delete.*'),
        (r'.*lock.*', r'.*unlock.*'),
    ]
    separate_bidirectional = []
    for pos_pattern, neg_pattern in bidirectional_words:
        pos_matches = len(re.findall(pos_pattern, content, re.IGNORECASE))
        neg_matches = len(re.findall(neg_pattern, content, re.IGNORECASE))
        if pos_matches > 0 and neg_matches > 0:
            # Check if they appear in separate user story sections
            if pos_matches != neg_matches:
                separate_bidirectional.append((pos_pattern, pos_matches, neg_pattern, neg_matches))
    
    has_separated_bidirectional = len(separate_bidirectional) > 0
    result = {
        "description": "Bidirectional actions consolidated (not split per SKILL.md line 36)",
        "passed": not has_separated_bidirectional
    }
    if has_separated_bidirectional:
        result["trace"] = "Possible separated bidirectional actions. Per SKILL.md line 36: consolidate On/Off, Start/Stop, etc. into unified stories, not separate ones."
    results.append(result)

    return results

def generate_html(user_stories_file, results):
    """Generate HTML report."""
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    score = int((passed / total * 100)) if total > 0 else 0

    html = f'''<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>User Stories Quality Evaluation - {Path(user_stories_file).stem}</title>
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
    <h1>User Stories Quality Evaluation</h1>
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
        print("Usage: eval-user-stories.py <user_stories_file> [output_file]", file=sys.stderr)
        sys.exit(1)

    user_stories_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = user_stories_file.replace('.md', '-eval.html')

    # Check if file exists
    if not os.path.isfile(user_stories_file):
        print(f"Error: User stories file not found: {user_stories_file}", file=sys.stderr)
        sys.exit(1)

    # Read content
    try:
        with open(user_stories_file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading user stories file: {e}", file=sys.stderr)
        sys.exit(1)

    # Evaluate
    results = evaluate_user_stories(content)
    html = generate_html(user_stories_file, results)

    # Write output
    try:
        with open(output_file, 'w') as f:
            f.write(html)

        passed = sum(1 for r in results if r['passed'])
        total = len(results)
        score = int((passed / total * 100)) if total > 0 else 0
        print(f"✓ User stories evaluation saved to {output_file}")
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
