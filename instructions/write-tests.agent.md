# Test Writing Instructions

Create tests for the weekly reporting workflow using pytest.

## Required approach
- Write a failing test before implementing the fix.
- Keep tests focused on real behavior, not mock-only behavior.
- Prefer real inputs and outputs over heavy mock setups.
- Use the smallest test that proves the behavior.

## Core test areas
- CLI parsing and validation
- Required-field checks and missing-data errors
- Default and override date handling
- Invalid date rejection and boundary validation
- Markdown formatting and heading checks
- Empty-section handling and concise bullet rendering
- Output directory creation and unwritable-path handling
- Manual input parsing and normalization
- Jira client behavior for success, pagination, empty results, and errors
- Refresh snapshot and stale-data handling
- Merge logic for Jira and manual updates without duplication
- Security checks for credentials and sensitive output
- End-to-end workflow generation from fixture data

## Test rules
- Name tests clearly and consistently.
- Cover both success and failure paths.
- Assert on public behavior and final output, not internal implementation details.
- Keep assertions readable and specific.
- Avoid test-only production methods.

## Output expectations
- Store tests under the appropriate `tests/` module or feature path.
- Use representative fixtures and small realistic inputs.
- Ensure the relevant test subset passes before finishing.
- If a test fails, fix the root cause and rerun the targeted suite.

## Constraints
- No fluff or placeholder tests.
- No broad, redundant coverage that duplicates existing behavior.
- No secrets or credentials in fixtures or test output.
- Keep the project aligned with the backlog testing requirements and the current weekly report workflow.
