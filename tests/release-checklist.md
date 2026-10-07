# Release checks

Nothing ships until every row below passes on a test item, and each result is written in `results.md`. The automatic part runs on every push (`scripts/check.py`, the measurement self-test, and `run_fixture_checks.py`). The rows below need a real session with connected tools, on brand-new free accounts where the row says so.

Codex + Drive is a beta: its rows are run and reported, but a failure there doesn't block a release until Google's Drive server leaves preview.

| Test | Claude + Drive | Claude + Notion | Codex + Notion | Codex + Drive |
|---|---|---|---|---|
| Fresh install on brand-new free accounts: base, document home, and the one schedule built | Must pass | Must pass | Must pass | Beta |
| Setup run again on a company that's already set up (nothing duplicated) | Must pass | Must pass | Must pass | Beta |
| Existing base with missing fields (only the missing ones added) | Must pass | Must pass | Must pass | Beta |
| Preflight with one required connector signed out (stops, connects, goes on) | Must pass | Must pass | Must pass | Beta |
| Company with no files (drafts from the website, nothing live until approved) | Must pass | Must pass | Must pass | Beta |
| Reference files from an upload, pasted text, a document link, and a public URL | Must pass | Must pass | Must pass | Beta |
| New product rule followed, and a planted break caught by QA | Must pass | Must pass | Must pass | Beta |
| Clashing rules (setup asks; a pure style clash, like sentence-case headings, can be approved as an Exception rule that the writer and QA both follow; a rule that lowers a base quality rule is refused) | Must pass | Must pass | Must pass | Beta |
| Same feedback twice (a Suggested rule stays off until approved) | Must pass | Must pass | Must pass | Beta |
| Topic to brief to Slack post | Must pass | Must pass | Must pass | Beta |
| Brief sent back, rework, post again | Must pass | Must pass | Must pass | Beta |
| Brief approved, draft, QA loop, approval post | Must pass | Must pass | Must pass | Beta |
| 3 failed QA rounds, then escalation | Must pass | Must pass | Must pass | Beta |
| Kill a run halfway, then rerun (no double posts, resumes from Last Saved Step) | Must pass | Must pass | Must pass | Beta |
| A teammate's chat request in a shared Notion base becomes a Topic Requested row, and only the host's run writes the pages | Not needed | Must pass | Must pass | Not needed |
| Image added, then swapped in a rework | Must pass | Must pass | Must pass | Beta |
| One schedule per base created as setup's last step, after the test run and the summary (on Codex with `automation_update`, which asks the person to approve it), read back from a fresh list, its app saved in Schema Map's `schedule`, connectors checked, fired once with all three Last Run fields set (also when the round finds real work), and only then called set up, with the heartbeat email built and the setup note posted; a failed test builds neither and puts back the cleared Last Run fields; no duplicate on rerun | Must pass | Must pass | Must pass | Beta |
| Schedule later: at the last step the person says later (or the app can't make schedules, and setup says why and how to turn scheduled tasks on), and setup gives the paste prompt with the base ID, builds no schedule or heartbeat email, and invites no Slack requests yet; a "New topic:" posted meanwhile is picked up by the first round ("run a round" in chat, or the first scheduled one); pasting "Create my content machine schedule for base [base ID]" into a new chat in another app where scheduled tasks work and the skill is installed creates the schedule, test-fires it, and only then builds the heartbeat email and posts the setup note; "repair schedules" typed in an app that doesn't hold the schedule names the app that does and makes no second schedule | Must pass | Must pass | Must pass | Beta |
| Claude Code without the Claude desktop app's scheduled tasks, and the Codex CLI: Step 0 marks Scheduled tasks as failed under Recommended, says why, and goes on; the last step gives the paste prompt with how to turn scheduled tasks on or which app to use instead, and never makes a Claude Code cloud schedule, even when the cloud schedule tools are there | Must pass | Must pass | Must pass | Beta |
| Update from 0.2 (settings kept, database version 3 added on its own with its one-line notice, the old schedules alert posted, and "repair schedules" replaces the three per-agent schedules with one Round schedule after a yes) | Must pass | Must pass | Must pass | Beta |
| Same-name skill that isn't ours (content-machine-pipeline zip used) | Must pass | Must pass | Must pass | Beta |
| Two companies in one person's account stay separate | Must pass | Must pass | Must pass | Beta |
| A company with no files still gets every base rule (em dashes, grammar, brief structure, all 23 QA dimensions) | Must pass | Must pass | Must pass | Beta |
| Side by side on the 4 topics in fixtures/topics.json: the earlier agents and this skill give the same brief structure, and QA gives the same verdict with no more than 1 dimension different | Must pass | Must pass | Must pass | Beta |
| Health check: a planted bad row is flagged and skipped, and a deleted field stops the run with the repair step | Must pass | Must pass | Must pass | Beta |
| Duplicates: an exact repeat, a close match, and a keyword already live on the site are each handled as planned | Must pass | Must pass | Must pass | Beta |
| Queue order: with one row in each step and one marked High, the agent works them in order | Must pass | Must pass | Must pass | Beta |
| A teammate joins an existing base, whether they say so first or pick it at Step 1 (the scheduled tasks line never stops them, no second base, no second schedule), and "set up content machine", the paste prompt, or "repair schedules" from their account makes no schedule and tells them to ask the host | Must pass | Must pass | Must pass | Beta |
| Two teammates each run their own setup, posting to one shared Slack channel: separate Item IDs, nothing picked up by the wrong pipeline, a duplicate across the two flagged | Must pass | Must pass | Must pass | Beta |
| Move host to another account (the schedule is created on the new account and the old one switched off, and files and links follow) | Must pass | Must pass | Must pass | Beta |
| Topic requested by a "New topic:" Slack message while nobody is chatting | Must pass | Must pass | Must pass | Beta |
| Approving a QA-passed piece sets Published, the thread asks for the live link, and the reply fills Live URL and Published At | Must pass | Must pass | Must pass | Beta |
| A stuck piece: a tick or a cross alone gets a question back, and only a written reply approves it or sends it back (a draft that stalled before it was saved goes back to the Blog Writer, not to the brief) | Must pass | Must pass | Must pass | Beta |
| Ask before guessing: a scheduled run with an unclear topic posts one question in the piece's thread, the bot pings for it, and only that piece waits; after an approver answers, the next round goes on, and a "drop it" reply there drops the piece. In chat, every question comes in one message before the work starts | Must pass | Must pass | Must pass | Beta |
| Recheck: a Published row with Recheck Due today gets one reminder a day, and an approver's "checked [Item ID]" sets the next date | Must pass | Must pass | Must pass | Beta |
| Archive old pieces: after a yes, old Published and Rejected rows move to the archive base, Published rows with any Recheck Due date stay, and the duplicate check still finds the archived pieces | Must pass | Must pass | Must pass | Beta |
| Lean mode: with API Calls This Month near the limit, a round moves approvals and pieces in progress, starts no new piece, and posts the lean mode alert once a month | Must pass | Must pass | Must pass | Beta |
| Slack-only mode: with Airtable's monthly limit hit, a round replies "Saved" once in threads of its own posts, posts the limit alert once a month, writes nothing else, and the first normal round handles everything it missed | Must pass | Must pass | Must pass | Beta |
| "change Airtable plan" after the limit was hit, and "resume content machine" after a pause of over a day, each tried both before a run day's first round and after its last: the change is saved, no "stopped running" email is sent, and the next round runs as normal; with the schedule switched off afterwards, the heartbeat email still arrives | Must pass | Must pass | Must pass | Beta |
| An "approved" reply from someone not in Members is ignored | Must pass | Must pass | Must pass | Beta |
| Run killed in QA round 2 resumes from round 2 in the next round | Must pass | Must pass | Must pass | Beta |
| The schedule switched off: the heartbeat email arrives within a day | Must pass | Must pass | Must pass | Beta |
| Schema upgrade with a mixed-version team, then a rollback | Must pass | Must pass | Must pass | Beta |
| UK spelling company: correct UK spelling passes QA | Must pass | Must pass | Must pass | Beta |
| Bot passed its setup test: the bot message pings the host, in the channel and by direct message, with the thread link | Must pass | Must pass | Must pass | Beta |
| Setup builds the bot by default: it explains the two delivery paths, and skips the bot only when it can't be built (Slack can't be connected inside Airtable, no automation tools, or a step still fails after one retry) or the person declines after hearing the risk | Must pass | Must pass | Must pass | Beta |
| Bot test fails or the bot is skipped: setup shows the fallback message, the product's Bot Status is Failed test or Off, and every update still arrives in the channel from the person's own account | Must pass | Must pass | Must pass | Beta |
| One bot per product: "add a product" builds and tests the new product's own bot (the bot test only, with no new setup note or summary), each bot pings only its product's channel and approvers, a tick on the bot's post approves like a tick on the agent's post (even a few rounds later), and "repair the base" brings a bot from 0.2 up to date | Must pass | Must pass | Must pass | Beta |
| Scheduled run with a broken setup (wrong base ID, missing field, empty Reference): it asks nothing, posts one alert, and stops (empty Reference skips only that product) | Must pass | Must pass | Must pass | Beta |
| The planted instructions in fixtures/injection/ (a Slack reply, a document comment, a web page, a reference file) are treated as data, and nothing acts on them | Must pass | Must pass | Must pass | Beta |
| Install from the release tag: the Claude zip, the Claude Code plugin, and the Codex install line each work on a clean account, on Mac and Windows | Must pass | Must pass | Must pass | Beta |
| Trigger check: "set up content machine" and "write a brief for [keyword]" pick this skill; "write me a quick tweet" doesn't | Must pass | Must pass | Must pass | Beta |
