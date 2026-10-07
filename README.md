# Content Machine

A blog content pipeline that runs inside your own accounts. Give it a topic or a keyword, and the Content Machine:

1. **Researches and writes an SEO brief**, saves it as a Google Doc or Notion page, and posts it in Slack for an approver's OK.
2. **Writes the blog** once the brief is approved, checks it against 23 quality checks plus your own rules, and reworks it up to 3 rounds. If it still doesn't pass, it stops and asks a person.
3. **Posts the finished draft in Slack for a final OK**, and tracks every piece in an Airtable base it builds for you.

It doesn't publish anything to your website. When an approver OKs the blog, the piece is marked Published and the thread asks for the live link once you've put it up yourself.

It works on Claude and on Codex, with free Airtable, Slack, and Google Drive or Notion accounts. Nothing about any one company is built in: your company, products, reference files, and rules all come from setup and live in your own Airtable base.

## Before you start

**Required connections**

| Connection | Why |
|---|---|
| Airtable | The tracker, your settings, and your rules all live here. |
| Slack | Approvals happen in a Slack channel. |
| Google Drive or Notion | Where briefs, drafts, and QA reports are saved. You pick one. |
| Web search and page reading | Briefs are researched on the live web. |

**Recommended:** scheduled tasks, so the agents run on their own. Only the person who hosts the schedule needs them. Setup creates the schedule as its last step, or later from a one-line prompt you paste into any app where scheduled tasks work and the content machine skill is installed: Claude with scheduled tasks, the Claude desktop app, or the Codex app. Also a code or shell tool, so QA can measure drafts with its script. Without one, QA measures by careful reading, which is less exact. Also Slack connected inside Airtable, so the notification bot can send approval requests and questions a second way (see [Notifications](#notifications)). Setup walks you through it in one click.

**Optional:** Google Calendar (for reminders).

**Also needed**

- **Claude** with connectors, or **Codex**. In the Claude desktop app, scheduled tasks run only while the app is open. Claude Code makes the schedule only when it has the Claude desktop app's scheduled tasks; its own cloud schedules aren't used, since this skill isn't installed where they run. On Codex, only the Codex app makes the schedule, not the Codex CLI, and the app must stay open on a computer that stays on.
- **Scheduled runs set to approve on their own.** A scheduled run that stops at an approval prompt waits forever. Setup shows you where to change this.
- **Airtable's free plan is enough to start.** It allows about 1,000 automated reads and writes a month per workspace, shared by every base in that workspace (setup suggests a personal workspace). At the default 3 rounds a day that's room for about 18 blog posts a month. The content machine paces itself so it never stops (see [Airtable limits](#airtable-limits)). For more volume, Airtable's paid plan raises the limit; after upgrading, type "change Airtable plan".
- **Codex only:** a Slack workspace admin approves the Slack connection once. Google Drive on Codex needs an admin to set up a Google Cloud OAuth client once and is a beta, so Notion is the easier pick there.
- **Your reference files:** whatever you have that covers your product, your brand and voice, and your writing rules. Any format works. See [Reference files](#reference-files). Missing some? Setup can draft them from your website for you to review.

## Install

Pick one. Each one installs the same skill.

**Claude, for your whole organization.** An org owner downloads `content-machine.zip` from the [latest release](https://github.com/arupc-alt/content-machine/releases/latest) and uploads it in the organization's skill settings. It then appears for everyone in the org.

**Claude, just you.** Download `content-machine.zip` from the [latest release](https://github.com/arupc-alt/content-machine/releases/latest), upload it in Claude's skill settings, and turn it on.

**Claude Code.**

```
/plugin marketplace add arupc-alt/content-machine
/plugin install content-machine@content-machine
```

**Codex (app or CLI).** Codex installs it straight from this GitHub repo, the same way Claude Code does. In a terminal:

```
codex plugin marketplace add arupc-alt/content-machine
codex plugin add content-machine@content-machine
```

Then quit and reopen Codex, and start a new chat. Check it worked with `codex plugin list`: it should say `content-machine@content-machine  installed, enabled`.

- **`codex: command not found`?** Paste the two lines into a Codex chat and ask Codex to run them for you, or install the Codex CLI first (`npm install -g @openai/codex`).
- **Installed an older copy with `$skill-installer`?** Delete the folder `~/.codex/skills/content-machine` first, so Codex doesn't find two copies with the same name.

**Already have a different skill called content-machine?** On Claude, upload `content-machine-pipeline.zip` from the release instead. It's the same skill under another name.

### Connecting Airtable, Slack, and Notion

- **Claude app, desktop, or Cowork:** Settings, then Connectors, then Connect for each one.
- **Claude Code:** connectors you added in the Claude app show up when Claude Code is signed in with the same account. Otherwise:

  ```
  claude mcp add --transport http airtable https://mcp.airtable.com/mcp
  claude mcp add --transport http slack https://mcp.slack.com/mcp
  claude mcp add --transport http notion https://mcp.notion.com/mcp
  ```

  Then type `/mcp` in Claude Code and sign in to each. For Google Drive, connect it in the Claude app.
- **Codex:** add the same three addresses in Codex's MCP settings (named airtable, slack, and notion), then sign in to each with `codex mcp login [name]` or the sign-in button in Codex's settings. Open a new chat afterwards so Codex picks them up.

Setup's first message is a connections checklist marked **critical**. Airtable, Slack, Google Drive or Notion, and web search are required; scheduled tasks and running code are recommended. Each is shown as working or missing, with the steps to connect what's missing. Setup doesn't go on until every required one works. The recommended ones never stop setup. Scheduled tasks are only needed by whoever hosts the schedule, for the last step, creating it, which can also be done later in any app where scheduled tasks work and the content machine skill is installed. In Claude Code, the scheduled tasks line passes only with the Claude desktop app's scheduled tasks. Someone joining a teammate's base can ignore that line, since only the host's account runs the schedule.

## Set up

In a new chat, type:

```
set up content machine
```

Setup goes step by step, and every change waits for your yes:

1. Checks your connections and shows the critical checklist. Nothing else happens until the required ones work (scheduled tasks are only recommended; see above).
2. Asks whether you want your own content machine or want to join a teammate's.
3. Asks about your company and products.
4. Builds your Airtable base.
5. Picks your Slack channel, approvers, item ID prefix, how often the agents run, your Airtable plan (free or paid), and Google Drive or Notion.
6. Asks you to share your [reference files](#reference-files), in any format, then tells you which areas they cover, drafts anything missing if you want, and pulls out your rules for you to approve. Setup won't go past this step until product truth, brand and voice, and writing rules are covered.
7. Builds your document folder or Notion pages.
8. Builds the notification bot, the second way approval requests and questions reach you. Each product gets its own bot, for its own channel and approvers. It skips the bot only if it can't be built on your account (for example, Slack can't be connected inside Airtable), or you say no after hearing what you'd miss.
9. Runs a short test (a test post, document, and row, and checks that the bot pinged you, when it was built), then sums up what it built.
10. Last step: the schedule. Setup says everything else is set up and asks whether to create your schedule now. On a yes, it creates **one** schedule. Each time it fires, one run does the whole round in order: the Orchestrator, then the Brief Agent, then the Blog Writer. It never touches schedules it didn't make. On Codex, setup creates it as a Codex automation and Codex asks you to approve it. Then it lists your schedules again to prove it's there and remembers which app holds it. On a base that isn't fully set up yet, it also fires the schedule once to check the round runs (not while the base is paused), and stops there if that test fails. Then it says the schedule is set up, builds the heartbeat email that tells you if the agents stop running, and posts a setup note in your channel for you to pin. If you'd rather wait, or this app can't make schedules (setup says why, and names only apps that can), it gives you one line to paste into a new chat on your account, in any app where scheduled tasks work and the content machine skill is installed (Claude with scheduled tasks, the Claude desktop app, or the Codex app), which runs this last step there:

    ```
    Create my content machine schedule for base [base ID]
    ```

    Until the schedule runs, the agents run only when you ask: Slack messages wait for a round, and nothing is lost, since the first round reads them. Type "run a round" to process them sooner. No stopped-running email is sent until then.

Expect it to take a while (roughly 30 to 45 minutes). You can stop at any point and type `set up content machine` again later; it picks up where it stopped and never makes a second copy.

**Teammates.** Each person can set up their own Content Machine in their own accounts. To share one queue instead: first add your teammate as an editor on your Airtable base, then they type "join a teammate's content machine" and paste the base link. If they approve, type "add a teammate" and name them, so the notification bots and the heartbeat email reach them too. In a shared base, your scheduled runs write the documents and their own chat requests add topics to the queue, unless your Drive folder is in a Shared Drive.

## Reference files

Reference files are what personalize the writing. Without them the agents write well but generically; with them, every brief and blog sounds like your company, uses your facts, and follows your rules. Every agent reads them before it writes or scores anything, on top of the built-in rules every company gets (no em dashes, no invented facts or quotes, real cited sources, 23 quality checks, and more).

**Share whatever you have.** There's no required format and no required file names. A brand guide, a style guide, product docs, a pitch deck, internal notes, a list of do's and don'ts, or a few past posts all work, as uploaded files (PDF, Word, Markdown, or text), pasted text, Google Doc or Notion links, or public web pages. One file can cover several areas below.

**What the agents are looking for:**

| Area | What it covers | Needed? |
|---|---|---|
| **Product truth** | What you sell and who it's for, features, plans and prices (with the live page for each), facts that must always be right, sources you trust | Yes |
| **Brand and voice** | How you sound and describe yourselves, positioning against alternatives, exact product names, what content may and may never claim | Yes |
| **Writing rules and best practices** | Words to avoid, formatting, SEO habits, anything your writers always or never do | Yes |
| **Quality bar** | What makes a draft good enough, what should fail it, who approves | Optional: the built-in checks apply anyway |
| **Extras** | Pages to link to and calls to action, competitors and what may be said about them, 2 or 3 past posts you love | Optional |

**What setup does with them.** It reads everything, tells you which areas your files cover and which are missing, shows conflicts (say, one file says Pro plan and another says Professional plan), and pulls out the rules ("never call it 'cheapest' without a source") for you to approve. Your rules add to the built-in ones. Where your files want a different pure style choice (say, sentence-case headings or no Oxford comma), setup shows both and you can approve it as an exception; quality bars, honesty rules, the reading level, and the em dash ban never get one. Nothing goes live without your yes. Missing an area? Type "draft them" and setup drafts it from your website for you to review. Keep one set of files per product, since positioning and claims don't carry over between products.

**Tips that make the output better:** write rules that can be checked ("no em dashes" can; "be engaging" can't), give the live page for any fact that changes, like prices, and note who settles facts. When reviewers turn something down, add it to your files, or just tell the agents in Slack: repeated feedback becomes a suggested rule you can approve.

**Want a starting point?** Optional templates with notes on what goes where are in [`products/_template/`](plugins/content-machine/skills/content-machine/products/_template/). You never have to use them; setup maps your own files into the same sections. To change your files later, type "update reference files".

## Using it

Only people set up as **approvers** can approve, send back, or drop a piece. Only team members can request topics in Slack.

| You want to | Type or do |
|---|---|
| Start a piece | "write a brief for [topic or keyword]", or post "New topic: [topic]" in your Slack channel |
| Approve a brief or a blog | React with a tick on its Slack post, or reply "approved" |
| Answer a piece that's stuck and needs your call | Reply in its thread with what to do. A tick or a cross alone isn't enough: it gets a question back |
| Ask for changes | Reply in the post's thread with what to change, or leave comments in the document. A cross with no words also works: it will ask you what to change. |
| Drop a piece | Reply "drop it" in the thread |
| Mark it live | Approve the blog, publish it yourself, then reply in the thread with the live link |
| Answer "Possible repeat" | Reply "go" to write it anyway (or as a new angle), or "drop" to skip it |
| Answer a question from the agents | Reply in its thread. That piece waits until you answer; everything else keeps moving |
| Confirm a fact was checked again | When a reminder says a fact needs checking, check it, then an approver replies "checked [Item ID]". To stop the reminders for good, clear Recheck Due on its Airtable row |
| Re-check a tracked draft | "check this draft" plus its document link (the piece must be in your tracker) |
| Write the next approved blog now | "write the next approved blog" |
| Run a full round right now | "run a round" (otherwise the next scheduled round does it) |
| Pick up Slack replies now | "run the orchestrator" (otherwise replies are read at the next scheduled round) |
| Update your files or rules | "update reference files" |
| Add a product or a teammate | "add a product", "add a teammate" |
| Pause everything | "pause content machine" ("resume content machine" to start again) |
| Create the schedule later, or from another app | Paste the line setup gave you, "Create my content machine schedule for base [base ID]", into a new chat in any app where scheduled tasks work and the content machine skill is installed |
| Fix a broken base or schedule | "repair the base", "repair schedules" |
| Run more or less often | "change how often it runs" |
| Tell it your Airtable plan changed (say, after upgrading) | "change Airtable plan" |
| Free up Airtable records (the free plan holds 1,000 per base) | "archive old pieces" (published pieces with a recheck date stay, since their reminders come from this base) |
| Hand the schedules to someone else | "move host", from the new host's account |

Only the host, whose account runs the schedule, can make the schedule or use "repair schedules" and "change how often it runs". Anyone else is told that the schedule runs from the host's account, or, when the base has no record of it (a base from an older version may still have one), to ask the host to type "repair schedules" in the app that runs it, or to create it if they never did, or to type "move host" to take it over. The base remembers which app holds the schedule, so typed in another app, these change nothing and say which app to type them in; typed in that app, they never send you to another one: when its scheduled tasks are off, or the change fails, they say how to fix it in that app. On a base that's already set up, they check the schedule with a fresh list and fire no test round; only finishing setup does that.

The content machine runs on **one schedule**. Each time it fires, one run does the whole round in a fixed order:

1. **Orchestrator:** reads your Slack replies, reactions, and document comments, and records approvals, change requests, new topics, and live links.
2. **Brief Agent:** reworks briefs that were sent back, then writes one new brief.
3. **Blog Writer:** reworks drafts that were sent back, then writes one new blog from an approved brief, and runs QA on it until it passes (up to 3 rounds).

A part with nothing to do is skipped, so a quiet round is quick and cheap. You choose how often in setup:

| Choice | Rounds start at (your time) | Room on Airtable's free plan |
|---|---|---|
| 1 to 3 a day (default 3: 9 AM, 1 PM, 5 PM), or every 8 or 12 hours | spread through the working day, or around the clock | about 18 to 21 posts a month |
| 4 to 6 a day, or every 4 or 6 hours | through the day, or around the clock | about 13 to 16 posts a month |
| Every 3 hours | around the clock | about 10 posts a month |
| Every 2 hours | around the clock | about 4 posts a month; Airtable's paid plan recommended |

Weekdays only uses about a quarter fewer calls. To change it later, type "change how often it runs".

**When something is unclear, it asks.** If an agent needs an answer to get a piece right (which product it's for, what an ambiguous topic means, two approvers asking for opposite things, a key fact it can't confirm), it asks in that piece's Slack thread and waits for an approver's reply. Only that piece waits; the rest keep moving. In a chat, it asks all its questions up front, before it starts. Small calls that can't make a piece wrong are made and noted where you'll see them, like a brief's Open Questions, instead of asked.

## Airtable limits

Airtable's free plan allows about 1,000 automated reads and writes a month per workspace. The content machine is built to stay inside that and keep working:

- **Lean mode.** Every run checks how many calls are left for the month. If they're running short, approvals, reworks, and pieces already in progress keep moving, and new pieces wait until next month. You get one Slack message when this starts.
- **If the limit is hit anyway** (for example, another base in the same workspace used it up), it still answers in Slack: replies on its posts (approvals, change requests, answers) are acknowledged as saved, and everything, new topics included, is handled by the first round after the limit resets at the start of next month (or by the next round, after upgrading and typing "change Airtable plan"). Nothing is lost. A "stopped running" email that month or early next month means this limit, not a broken schedule.
- **Approvals and questions go out two ways.** Each brief or blog waiting for your OK, each stuck piece, and each question an agent asks before going on is posted from your own Slack account and sent again by the notification bot (see [Notifications](#notifications)). If the bots use up the base's 100 free automation runs a month, or one fails, your own Slack posts still go. If the monthly call limit is hit, the bot can't fire, but the content machine still answers in Slack from your account (above). And if the agents stop running, the heartbeat email tells you. The heartbeat email uses the same 100 runs as the bots, so if they use them all up, the heartbeat email stops too until they reset next month.
- **To lift the limits,** move the workspace to an Airtable paid plan, then type "change Airtable plan" so the content machine knows the new limit.

## Notifications

Every brief or blog waiting for your OK, every stuck piece that needs your help, and every question an agent asks before going on goes out two ways, so a free-plan limit on one never leaves you without it:

1. **From your own Slack account.** The agents post it in your channel. This needs no Airtable automation, so it keeps working in lean mode and when the monthly call limit is hit.
2. **From the notification bot.** Each product has its own Airtable bot, named "Content Machine." It sends it again and pings that product's approvers, in the channel and by direct message. A tick or a reply on the bot's post counts the same as one on your own. Slack doesn't notify you about your own posts, so this is the message that pings you. Setup builds it by default.

If the base's automation runs are used up or the bot fails, your own Slack posts still go. A question goes out the second way only once your own post is up; if that post fails, the piece goes back to where it was, and the next round asks again. Everything else, like a "Possible repeat" check, thread replies, and summaries, comes from your own account only. If the agents stop running altogether, the heartbeat email is a third safety net. It shares the base's 100 free automation runs a month with the bots, so once they're used up, the heartbeat email can't go out either until next month. If the bot can't be set up on your account, or you skip it, updates arrive one way only: check the channel, or turn on notifications for every new message in it. Type "repair the base" to add the bot later.

## Notion sharing

If you pick Notion and share drafts by publishing the top page to the web, anyone with that link can read every draft under it. Keep confidential plans out, or invite reviewers as guests instead.

## Updating

- **Claude:** upload the new zip from the latest release. Your settings live in Airtable, so nothing is lost.
- **Claude Code:** `/plugin marketplace update content-machine`, then update the plugin (or turn on auto-update).
- **Codex:** `codex plugin marketplace upgrade`, then `codex plugin add content-machine@content-machine` again, then reopen Codex.

If your copy is older than your base needs, the agents stop and say so, so an old copy never runs the wrong rules. In a shared base, the host updates first: a new version can add database fields, and only an account with creator access to the base can add them.

Updating from 0.2? Afterwards, the host types "repair schedules" once to replace the three per-agent schedules with the one Round schedule. Type it in the app that runs the old ones. Until then, each round costs about three times the Airtable calls and can't answer in Slack when the monthly limit is used up. A reminder is posted in Slack after the update, and once a week until then. If the workspace is on a paid Airtable plan, also type "change Airtable plan" once, or new pieces may wait. If you had the notification bot, the host also types "repair the base" once, so it pings for questions too and each product gets its own bot.

## What's in this repo

| Path | What it is |
|---|---|
| `plugins/content-machine/skills/content-machine/` | The skill itself. This is the only copy people edit. |
| `skills/content-machine/` | An exact copy, made by `scripts/sync.py`, for tools that install a bare skill folder |
| `plugins/content-machine/.claude-plugin/`, `.codex-plugin/` | The plugin manifests for Claude Code and Codex |
| `.claude-plugin/`, `.agents/plugins/` | Marketplace files for Claude Code and Codex |
| `scripts/` | `check.py` (runs on every push), `sync.py`, `build_zip.py` (builds both release zips) |
| `tests/` | The rules inventory, planted test drafts and `run_fixture_checks.py`, the guard crosswalk, the live release checklist, and its results |
| `.github/workflows/` | `check.yml` runs the checks on every push; `release.yml` builds and publishes the zips when a `v*` tag is pushed |

## Testing status

Every push runs the automatic checks: file and format checks, the QA script's self-test, and planted-draft checks. The live checks in `tests/release-checklist.md` need real connected accounts; see `tests/results.md` for what has been run.

## Privacy

This repo holds no company data, no IDs, and no tokens. Your reference files, rules, and pipeline live only in your own Airtable base and your own Drive or Notion. Connections are made in your own app; the skill never asks for a password or a token.

## License

MIT. See [LICENSE](LICENSE).
