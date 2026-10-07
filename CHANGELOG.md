# Changelog

## 0.3.0

From a live setup on Codex. Database version 3: four new fields and one new rule category, added on their own by the next run (safe unattended). Update the host's copy first: adding fields needs creator access to the base, which a teammate who joined as an editor doesn't have. Once the base is updated, a copy older than 0.3.0 stops and asks to be updated.

- **One schedule per base.** A new Round mode runs the whole round in one run, in order: the Orchestrator, then the Brief Agent, then the Blog Writer with QA. Setup creates exactly one schedule, never one per agent. A quiet round costs 2 Airtable calls instead of 6, so the free plan now fits about 18 posts a month at 3 rounds a day instead of about 7. Type "run a round" to run one now. Updating from 0.2? The host types "repair schedules" once to replace the three per-agent schedules; until then each round costs about three times the calls and can't answer in Slack when the limit is used up, and a Slack reminder says so after the update and once a week.
- **Setup never touches schedules it didn't make.** Other schedules on the account are ignored; if they look like another content pipeline, setup says so once.
- **Ask before guessing (G25).** When an input the piece depends on is missing or unclear, a scheduled run asks in the piece's Slack thread and holds only that piece (new field: Open Question) until an approver answers or drops it; a chat run asks everything up front. Small calls are still made and noted, not asked. If the question can't be posted, the piece isn't held, and the next run asks again. The notification bot pings for these questions too.
- **Airtable limits never stop the content machine.** Lean mode keeps approvals and pieces in progress moving and holds new pieces when the month's calls run short. If the limit is hit anyway, rounds answer in Slack and catch up when it resets, with nothing lost. New field API Monthly Limit, set with the new "change Airtable plan" command. Already on a paid Airtable plan? Type it once after updating, or new pieces may wait. The schedule prompt now carries the channel IDs for this, and a weekly check says when they're out of date. The heartbeat no longer sends a false alarm on the 1st of the month after the limit was reached; older bases can paste the new formula ("repair the base" offers it).
- **Approvals and questions go out two ways.** Each brief or blog waiting for approval, each stuck piece, and each question an agent asks before going on is posted from the person's own Slack account and sent again by the Airtable notification bot, which setup now builds by default (skipped only when it can't be built, or the person says no after hearing the risk). Each product gets its own bot, for its own channel and approvers (new Settings fields: Bot Status and Bot Automation ID), and a tick or reply on the bot's post counts the same as one on the agent's. Other posts, like "Possible repeat", thread replies, and summaries, go out from the person's account only. The heartbeat email is a third safety net, but it shares the base's 100 free automation runs a month with the bots. "add a product" builds and tests the new product's bot, and "repair the base" offers one to each product that doesn't have one and brings a bot from 0.2 up to date.
- **Style exceptions.** A company's files can now swap one pure style choice in the built-in rules for their own, like heading case, the Oxford comma, or a date format. Setup shows the clash and, after a yes, saves it as an Exception rule that the writer and QA follow. The em dash ban, the reading level, the honesty rules, and every quality bar never get an exception. Before, such a line could make drafts loop through rework, since QA still checked the built-in rule.
- A suggested rule that repeats one the product already has, or one the approvers already turned down, is no longer saved or asked about again.
- Approver look-up reads the final list back once, instead of asking about each name again.
- **The schedule is setup's last step.** After the test run and the summary, setup asks whether to create the schedule now. To do it later, or when this app can't make schedules (setup then says why, and names only apps that can), setup gives one line to paste into a new chat in any app where scheduled tasks work and the content machine skill is installed (Claude with scheduled tasks, the Claude desktop app, or the Codex app): "Create my content machine schedule for base [base ID]". The schedule is created and checked with a fresh list. On a base that isn't fully set up yet, it's also test-fired once (not while the base is paused), and a failed test stops setup there. Then setup calls it set up, builds the heartbeat email, and posts the setup note in the channel. Until then, Slack messages wait for a round ("run a round" processes them), and nothing is lost. The base remembers which app holds the schedule, so "repair schedules" and "change how often it runs", typed in another app, change nothing and say which app to type them in; typed in that app, they never send the host to another one, even when its scheduled tasks are off or the change fails there: they say how to fix it there. A second schedule is never made in another app without saying the first must be switched off. On a base that's already set up, these, "add a product", and "move host" check the schedule with a fresh list and fire no test round, so a live base never gets the day's reminders twice. Scheduled tasks are now recommended, not required, and only whoever hosts the schedule needs them. Claude Code makes the schedule only with the Claude desktop app's scheduled tasks, never its own cloud schedules (this skill isn't installed where those run), and on Codex only the Codex app makes it, not the Codex CLI.
- A piece that's stuck and needs a person's call now needs a written reply. A tick or a cross alone gets a question back, so a "seen" tick can't publish a draft that failed its checks. A draft that stalled before it was saved goes back to the writer, not back to the brief.
- Recheck reminders can be closed: an approver replies "checked [Item ID]" and the next recheck date is set. Before, a due recheck was posted every day for good. "archive old pieces" now keeps back published pieces that have a recheck date, due or not, since their reminders come only from the base; clearing Recheck Due lets one move.
- In a channel shared with other people's pipelines, their messages no longer make a round read the base for each of their pieces.
- Upkeep commands: "resume content machine", and "change Airtable plan" after the limit was hit, no longer set off a false "stopped running" email. "add a teammate" no longer adds a second row for someone who joined on their own, and it brings each product bot's and the heartbeat email's lists up to date (a bot from 0.2 needs "repair the base" first). Only the host can make or change the schedule (in setup, "repair schedules", and "change how often it runs"), so a teammate can't make a second one; a teammate is told the schedule runs from the host's account, or, when the base has no record of it yet, to ask the host to type "repair schedules" in the app that runs it, or to create it.

## 0.2.1

Edge cases found by a full review of timing, human input, and setup. No new database fields.

- Feedback sent while an agent is working is no longer lost: it becomes a change request once the piece is posted, unless a rework already used it.
- The Blog Writer now reads an approver's answers to the brief's open questions, and a person's feedback now outranks the brief's strategy in a draft rework.
- Reactions added after an earlier decision are now seen. A late approve on an older version's post is asked about instead of approving a version nobody saw. "+1" replies carry the message they agree with.
- Live links: draft links (Docs, Drive, Notion, Slack) are refused, other-domain links are flagged for a person, and a corrected link replaces a wrong one.
- Items waiting on a person for 3 days or more are listed once a day under "Needs you".
- Claims: every write refreshes Claimed At, so long runs never look stale and dead runs always do. A computer that slept mid-run re-checks its claim before writing again. Two Orchestrator runs at once no longer record the same feedback twice.
- The heartbeat no longer sends false alarms on weekends in time zones east of UTC, after a long first run, or while the monthly Airtable limit is reached. Older bases can paste the new formula ("repair the base" offers it).
- Setup can finish when scheduled tasks are waived. "repair schedules" clears Last Run before its test fires. Move host asks for creator access for the new host. Adding a product on a new document tool repairs the schedules. Two installed copies of this skill are caught.
- Reference files: a website that can't be read gets a paste-or-five-questions fallback, non-English files are flagged, and very large files are kept in full only where they matter.
- New "archive old pieces" command for the 1,000-record free plan limit. The duplicate check also reads the archive.
- Idle Orchestrator runs no longer read every finished piece, so their cost stays flat as the base grows. Long Agent Notes and Human Feedback cells are shortened before they hit Airtable's limit.

## 0.2.0

Fixes found by testing 0.1.0, including a live test on Codex. Database version 2: one new Team field, added on its own by the next run (safe unattended), so existing setups keep working.

- Setup now starts with a critical connections checklist, before any other question: Airtable, Slack, Google Drive or Notion, web search, and scheduled tasks, each marked as working or missing, with the exact steps to connect what's missing. Setup doesn't go on until every required one works.
- Setup now asks for your reference files plainly (brand guide, style guide, product knowledge, plus the optional ones), waits for them, and won't go past that step without them. You can still type 'draft them' to get drafts from your website.
- Choose how often the agents run: 1 to 6 times a day, or every 2, 3, 4, 6, 8, or 12 hours. Each time, the Orchestrator, Brief Agent, and Blog Writer each run once. Setup shows what each choice costs on Airtable's free plan. The chosen hours are saved in a new Team field, Round Hours (migration 2).
- On Codex, setup now creates the three schedules itself with Codex's automation tool, instead of only showing entries to paste.
- After creating the schedules, setup lists them again with a fresh call and shows a table of each agent's times, fixing or flagging any that are missing. The weekly health check also confirms they still exist.
- Codex installs from this GitHub repo as a plugin, the same way Claude Code does (`codex plugin marketplace add arupc-alt/content-machine`, then `codex plugin add content-machine@content-machine`). No more `$skill-installer`.
- Reference files: setup and the README now explain what the agents are looking for (product truth, brand and voice, writing rules and best practices, and an optional quality bar), in any format, and offer optional templates with notes on each section.
- A live link sent together with the approval is now saved instead of lost.
- Before QA, the Blog Writer now also self-checks the style guide's never-use list, brand voice and terminology, prohibited claims, every rule meant for QA, and the company's own quality checks.
- Fixed: the QA loop's rework no longer mistakes its own status change for another run; the first draft rework no longer pulls in brief-stage feedback; the duplicate check no longer matches a piece's own Slack posts; "Rules loaded" now counts the reference files.
- New accuracy rules for every product: when sources disagree the vendor's live page wins, nothing is called "new" without checking the changelog, no promised outcomes the product can't control, and each source is queried once. QA now also fails a piece that doesn't deliver its title's promise or repeats a point.

- Learned rules and product rules are now saved with their rule text (Content), and product rules with their Product. Before, rules approved from feedback were skipped as incomplete, and product rules from setup could fail to load.
- The "Possible repeat" question for a live post now asks for "go" or "drop", the same answers the Orchestrator reads. Before, an answer like "new angle" left the piece waiting forever.
- A brief whose save failed is now picked up again on the next run instead of being stranded.
- Brief, Blog Writer, and QA now load the rule ID scheme they use when saving a learned rule, so IDs don't clash.
- An escalation post that never went out is now always posted again, even though Escalated rows are otherwise skipped.
- "check this draft [link]" now checks the linked draft first, instead of after up to three other pieces.
- Setup lists every missing connection in one message, and shows the exact Claude Code commands to connect Airtable, Slack, and Notion.
- Setup and "repair schedules" now also work with the Claude desktop app's scheduled tasks.
- "pause content machine" and "resume content machine" now find the base first and say what to do when Airtable isn't connected or no base is found. Resume now waits for a yes too.
- The "Possible repeat" and "Can't open a document" messages now live in shared/slack.md, so every mode uses the same wording.
- A row that stalls twice is escalated with its own message instead of the "Stuck after 3 rounds" one.
- The Orchestrator reads Slack channels from Schema Map, so a run with nothing to do no longer reads Settings.
- The README now matches what the skill does: the setup order, required and optional connections, Claude Code connector commands, who can approve, the bot's limits, Notion sharing, and that nothing is published to your website for you.

## 0.1.0

The first release.

- One skill, five modes: Setup, Brief, Blog Writer (with the quality check and rework loop built in), QA, and Orchestrator.
- Setup builds everything in your own accounts: an Airtable base with 7 tables, a Google Drive folder or Notion workspace layout, your reference files and product rules, the schedules, and an optional Slack bot, then runs a short test.
- Every teammate can run their own, or join a teammate's base.
- Every writing rule, brief structure, and quality check from the earlier four agents carries over as the base for every product. Your reference files only add to it.
- Scheduled runs never ask questions. When something needs a person, they post one alert and stop.
- Database version 1.
