# Weekly Status Report Generation Workflow

## Input format
Provide the weekly report data as a structured payload or CLI arguments containing:
- project name
- owner or team
- executive summary
- completed work
- in-flight work
- blockers or risks
- next-week priorities
- decisions or notes
- reporting start date
- reporting end date
- output path

Use date values in YYYY-MM-DD format. If the report dates are omitted, default to the current Monday-through-Sunday reporting week. If a required field is missing, stop with a clear validation error instead of inventing values.

## Processing steps
1. Validate required values for project name, owner/team, summary, and output path.
2. Validate date inputs, including format and week boundaries; reject invalid ranges with a concise actionable error.
3. Normalize manual updates into the internal report structure, preserving ownership, status, milestone timing, risk impact, mitigation, and decisions where provided.
4. Separate completed items from in-flight items and identify explicit blockers and risks.
5. Merge report data with the latest available refreshed snapshot when relevant, without duplicating issue entries or losing manual context.
6. Generate the Markdown report using the required headings and concise bullet lists.
7. Create the destination directory if needed and save the output to the specified path.

## Output format
Produce Markdown with these sections in this order:
- Executive Summary
- Completed
- In Flight
- Risks / Blockers
- Next Week
- Decisions Needed

Use bullet points only under each section. Keep entries concise and factual. Use explicit `None` when a section has no items.

## Constraints
- Use Markdown only.
- Keep the tone professional and direct.
- No fluff phrases, filler text, or marketing language.
- Keep entries brief and specific to weekly execution status.
- Do not expose secrets, credentials, or sensitive Jira details in logs or output.
- Preserve manual context when Jira data is incomplete or unavailable.
- Do not generate email, dashboard, or forecasting content beyond the weekly report scope.
- If refreshed data is stale, warn or fail clearly according to the configured freshness threshold.
