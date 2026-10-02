#!/usr/bin/env python3
import argparse
import subprocess
from datetime import date, timedelta
from pathlib import Path


def run_git_command(args):
    try:
        result = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return ""
    except FileNotFoundError:
        return ""


def get_git_summary():
    branch = run_git_command(["branch", "--show-current"])
    status = run_git_command(["status", "--short"])
    recent = run_git_command(["log", "--since=7.days.ago", "--pretty=format:%ad | %h | %s", "--date=short"])
    if not branch and not status and not recent:
        return "Git summary unavailable (not a git repo or git is not installed)."

    lines = ["## Git activity", ""]
    if branch:
        lines.append(f"- Current branch: {branch}")
    if status:
        lines.append("- Working tree changes:")
        for item in status.splitlines():
            lines.append(f"  - {item}")
    else:
        lines.append("- Working tree is clean.")
    if recent:
        lines.append("- Recent commits:")
        for item in recent.splitlines():
            lines.append(f"  - {item}")
    else:
        lines.append("- No commits in the last 7 days.")
    return "\n".join(lines)


def build_report(args):
    week_start = (date.today() - timedelta(days=date.today().weekday())).isoformat()
    week_end = (date.today() + timedelta(days=6 - date.today().weekday())).isoformat()

    report = [
        "# Executive Weekly Status",
        "",
        f"- Project: {args.project}",
        f"- Owner: {args.owner}",
        f"- Week: {args.week_start or week_start} to {args.week_end or week_end}",
        "",
        "## Executive Summary",
        f"- {args.summary}",
        "",
        "## Completed",
    ]

    if args.completed:
        for item in args.completed:
            report.append(f"- {item}")
    else:
        report.append("- No major completed items.")

    report.extend(["", "## In Flight",])
    if args.in_progress:
        for item in args.in_progress:
            report.append(f"- {item}")
    else:
        report.append("- No active work items.")

    report.extend(["", "## Risks / Blockers",])
    if args.blockers:
        for item in args.blockers:
            report.append(f"- {item}")
    else:
        report.append("- No material blockers.")

    report.extend(["", "## Next Week",])
    if args.next_week:
        for item in args.next_week:
            report.append(f"- {item}")
    else:
        report.append("- No next-week plan provided.")

    report.extend(["", "## Decisions Needed",])
    if args.notes:
        report.append(f"- {args.notes}")
    else:
        report.append("- None at this time.")

    report.extend(["", get_git_summary()])

    return "\n".join(report) + "\n"


def parse_list(value):
    if not value:
        return []
    return [item.strip() for item in value.split("|") if item.strip()]


def main():
    parser = argparse.ArgumentParser(description="Generate a concise executive weekly status report in Markdown.")
    parser.add_argument("--project", default="General Project", help="Project name.")
    parser.add_argument("--owner", default="Your Name", help="Owner or team name.")
    parser.add_argument("--summary", default="Progress remained on track; key milestones were completed.", help="Short executive summary.")
    parser.add_argument("--completed", type=parse_list, default=[], help="Completed items separated by pipes, e.g. 'a|b|c'.")
    parser.add_argument("--in-progress", dest="in_progress", type=parse_list, default=[], help="In-progress items separated by pipes.")
    parser.add_argument("--blockers", type=parse_list, default=[], help="Current blockers separated by pipes.")
    parser.add_argument("--next-week", dest="next_week", type=parse_list, default=[], help="Planned items for next week separated by pipes.")
    parser.add_argument("--notes", default="", help="Any additional notes.")
    parser.add_argument("--week-start", default="", help="Override week start date (YYYY-MM-DD).")
    parser.add_argument("--week-end", default="", help="Override week end date (YYYY-MM-DD).")
    parser.add_argument("--output", default="work/weekly-status-report.md", help="Output Markdown file path.")
    args = parser.parse_args()

    report = build_report(args)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Weekly status report saved to {output_path}")


if __name__ == "__main__":
    main()
