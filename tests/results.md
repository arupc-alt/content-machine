# Release check results

One section per release. For each row in release-checklist.md: pass or fail, the date, the platform, and a one-line note (a link to the test item, or what failed).

## 0.3.0 (not released yet)

Automatic checks, 2026-10-07: pass (scripts/check.py, measure.py self-test, run_fixture_checks.py).

Live checks: not run yet, including the rows new in 0.3.0 (the one Round schedule, the update from 0.2, ask before guessing, lean and Slack-only mode, style exceptions, and the bot built by default).

## 0.2.0

Codex plugin install, 2026-10-07, Mac, clean CODEX_HOME: `codex plugin marketplace add arupc-alt/content-machine`, `codex plugin add content-machine@content-machine` (listed as installed, enabled), and `codex plugin marketplace upgrade` all passed.

Dry runs (agents following the skill with simulated tools): new setup on Codex (connections checklist first, reference-file gate, every-4-hours weekday schedules with correct RRULEs, verified with a calendar-rule parser), and one piece traced from "New topic:" to Published. Problems found were fixed in 0.2.0.

Live test on Codex, 2026-10-07 (by the repo owner): setup didn't ask for reference files, didn't check connections first, and didn't create schedules; the skill wasn't found until it was installed from GitHub. Fixed in 0.2.0; not re-tested live yet.

## 0.1.1 (not released; folded into 0.2.0)

Automatic checks: pass (scripts/check.py, measure.py self-test, run_fixture_checks.py).

Install, 2026-10-07, Mac:
- Claude Code: `/plugin marketplace add arupc-alt/content-machine`, `/plugin install content-machine@content-machine`, and `/plugin marketplace update content-machine` all passed on a clean config. `claude plugin validate` passed for the marketplace and the plugin.
- Codex install line: not run yet.
- Claude zip upload: not run yet.

Dry runs with no connectors (each mode read and followed by an agent, no accounts touched): set up, pause, write a brief (chat and scheduled), run the orchestrator, check this draft, a schedule with no mode, and an unclear request. Each stopped cleanly with a clear message, wrote nothing, and asked nothing in scheduled runs. The problems they found are fixed in 0.1.1.

Live checks: not run yet.

## 0.1.0

Automatic checks: pass (scripts/check.py, measure.py self-test, run_fixture_checks.py).

Live checks: not run yet.
