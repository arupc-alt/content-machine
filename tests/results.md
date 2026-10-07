# Release check results

One section per release. For each row in release-checklist.md: pass or fail, the date, the platform, and a one-line note (a link to the test item, or what failed).

## 0.1.1

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
