# Changelog

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
