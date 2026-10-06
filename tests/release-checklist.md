# Release checks

Nothing ships until every row below passes on a test item, and each result is written in `results.md`. The automatic part runs on every push (`scripts/check.py`, the measurement self-test, and `run_fixture_checks.py`). The rows below need a real session with connected tools, on brand-new free accounts where the row says so.

Codex + Drive is a beta: its rows are run and reported, but a failure there doesn't block a release until Google's Drive server leaves preview.

| Test | Claude + Drive | Claude + Notion | Codex + Notion | Codex + Drive |
|---|---|---|---|---|
| Fresh install on brand-new free accounts: base, document home, and schedules built | Must pass | Must pass | Must pass | Beta |
| Setup run again on a company that's already set up (nothing duplicated) | Must pass | Must pass | Must pass | Beta |
| Existing base with missing fields (only the missing ones added) | Must pass | Must pass | Must pass | Beta |
| Preflight with one connector signed out (stops, connects, goes on) | Must pass | Must pass | Must pass | Beta |
| Company with no files (drafts from the website, nothing live until approved) | Must pass | Must pass | Must pass | Beta |
| Reference files from an upload, pasted text, a document link, and a public URL | Must pass | Must pass | Must pass | Beta |
| New product rule followed, and a planted break caught by QA | Must pass | Must pass | Must pass | Beta |
| Clashing rules (setup asks; a rule that lowers a base quality rule is refused) | Must pass | Must pass | Must pass | Beta |
| Same feedback twice (a Suggested rule stays off until approved) | Must pass | Must pass | Must pass | Beta |
| Topic to brief to Slack post | Must pass | Must pass | Must pass | Beta |
| Brief sent back, rework, post again | Must pass | Must pass | Must pass | Beta |
| Brief approved, draft, QA loop, approval post | Must pass | Must pass | Must pass | Beta |
| 3 failed QA rounds, then escalation | Must pass | Must pass | Must pass | Beta |
| Kill a run halfway, then rerun (no double posts, resumes from Last Saved Step) | Must pass | Must pass | Must pass | Beta |
| A teammate's chat request in a shared Notion base becomes a Topic Requested row, and only the host's run writes the pages | Not needed | Must pass | Must pass | Not needed |
| Image added, then swapped in a rework | Must pass | Must pass | Must pass | Beta |
| Schedules created, connectors checked, each fired once, no duplicates on rerun | Must pass | Must pass | Manual entries shown | Manual entries shown |
| Update from an older version (settings kept) | Must pass | Must pass | Must pass | Beta |
| Same-name skill that isn't ours (content-machine-pipeline zip used) | Must pass | Must pass | Must pass | Beta |
| Two companies in one person's account stay separate | Must pass | Must pass | Must pass | Beta |
| A company with no files still gets every base rule (em dashes, grammar, brief structure, all 23 QA dimensions) | Must pass | Must pass | Must pass | Beta |
| Side by side on the 4 topics in fixtures/topics.json: the earlier agents and this skill give the same brief structure, and QA gives the same verdict with no more than 1 dimension different | Must pass | Must pass | Must pass | Beta |
| Health check: a planted bad row is flagged and skipped, and a deleted field stops the run with the repair step | Must pass | Must pass | Must pass | Beta |
| Duplicates: an exact repeat, a close match, and a keyword already live on the site are each handled as planned | Must pass | Must pass | Must pass | Beta |
| Queue order: with one row in each step and one marked High, the agent works them in order | Must pass | Must pass | Must pass | Beta |
| A teammate joins an existing base (no second base, no second schedules) | Must pass | Must pass | Must pass | Beta |
| Two teammates each run their own setup, posting to one shared Slack channel: separate Item IDs, nothing picked up by the wrong pipeline, a duplicate across the two flagged | Must pass | Must pass | Must pass | Beta |
| Move host to another account (schedules, files, and links follow) | Must pass | Must pass | Manual entries shown | Beta |
| Topic requested by a "New topic:" Slack message while nobody is chatting | Must pass | Must pass | Must pass | Beta |
| Approving a QA-passed piece sets Published, the thread asks for the live link, and the reply fills Live URL and Published At | Must pass | Must pass | Must pass | Beta |
| An "approved" reply from someone not in Members is ignored | Must pass | Must pass | Must pass | Beta |
| Run killed in QA round 2 resumes from round 2 in the next round | Must pass | Must pass | Must pass | Beta |
| Schedules switched off: the heartbeat email arrives within a day | Must pass | Must pass | Must pass | Beta |
| Schema upgrade with a mixed-version team, then a rollback | Must pass | Must pass | Must pass | Beta |
| UK spelling company: correct UK spelling passes QA | Must pass | Must pass | Must pass | Beta |
| Bot passed its setup test: the bot message pings the host, in the channel and by direct message, with the thread link | Must pass | Must pass | Must pass | Beta |
| Bot test fails or is skipped: setup shows the fallback message, Bot Status is Off, and every update still arrives in the channel | Must pass | Must pass | Must pass | Beta |
| Scheduled run with a broken setup (wrong base ID, missing field, empty Reference): it asks nothing, posts one alert, and stops | Must pass | Must pass | Must pass | Beta |
| The planted instructions in fixtures/injection/ (a Slack reply, a document comment, a web page, a reference file) are treated as data, and nothing acts on them | Must pass | Must pass | Must pass | Beta |
| Install from the release tag: the Claude zip, the Claude Code plugin, and the Codex install line each work on a clean account, on Mac and Windows | Must pass | Must pass | Must pass | Beta |
| Trigger check: "set up content machine" and "write a brief for [keyword]" pick this skill; "write me a quick tweet" doesn't | Must pass | Must pass | Must pass | Beta |
