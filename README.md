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

**Recommended:** a code or shell tool, so QA can measure drafts with its script. Without one, QA measures by careful reading, which is less exact.

**Optional:** Slack connected inside Airtable (for the notification bot) and Google Calendar (for reminders).

**Also needed**

- **Claude** with connectors and scheduled tasks, so the agents can run on their own. In the Claude desktop app, scheduled tasks run only while the app is open. On **Codex**, the app must stay open on a computer that stays on.
- **Scheduled runs set to approve on their own.** A scheduled run that stops at an approval prompt waits forever. Setup shows you where to change this.
- **Airtable free plan limits.** About 1,000 automated reads and writes a month per workspace, shared by every base in that workspace (setup suggests a personal workspace). That's enough for about 7 blog posts a month at 3 rounds a day, or about 12 at 2 rounds a day. The notification bot has its own limit of 100 automation runs a month per base.
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

Setup's first message is a connections checklist marked **critical**: Airtable, Slack, Google Drive or Notion, web search, and scheduled tasks, each shown as working or missing, with the steps to connect what's missing. Setup doesn't go on until every required one works.

## Set up

In a new chat, type:

```
set up content machine
```

Setup goes step by step, and every change waits for your yes:

1. Checks your connections and shows the critical checklist. Nothing else happens until the required ones work.
2. Asks whether you want your own content machine or want to join a teammate's.
3. Asks about your company and products.
4. Builds your Airtable base.
5. Picks your Slack channel, approvers, item ID prefix, how often the agents run, and Google Drive or Notion.
6. Asks you to share your [reference files](#reference-files), in any format, then tells you which areas they cover, drafts anything missing if you want, and pulls out your rules for you to approve. Setup won't go past this step until product truth, brand and voice, and writing rules are covered.
7. Builds your document folder or Notion pages.
8. Builds the Airtable automations: a heartbeat email if the agents stop running, and the optional notification bot.
9. Creates the schedules: one each for the Orchestrator, the Brief Agent, and the Blog Writer. On Codex, setup creates them as Codex automations and Codex asks you to approve each one.
10. Runs a short test: a test post, document, and row, then fires each schedule once.

Expect it to take a while (roughly 30 to 45 minutes). You can stop at any point and type `set up content machine` again later; it picks up where it stopped and never makes a second copy.

**Teammates.** Each person can set up their own Content Machine in their own accounts. To share one queue instead: first add your teammate as an editor on your Airtable base, then they type "join a teammate's content machine" and paste the base link. In a shared base, your scheduled runs write the documents; their own chat requests add topics to the queue.

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

**What setup does with them.** It reads everything, tells you which areas your files cover and which are missing, shows conflicts (say, two files disagree on title case), and pulls out the rules ("never call it 'cheapest' without a source") for you to approve. Nothing goes live without your yes. Missing an area? Type "draft them" and setup drafts it from your website for you to review. Keep one set of files per product, since positioning and claims don't carry over between products.

**Tips that make the output better:** write rules that can be checked ("no em dashes" can; "be engaging" can't), give the live page for any fact that changes, like prices, and note who settles facts. When reviewers turn something down, add it to your files, or just tell the agents in Slack: repeated feedback becomes a suggested rule you can approve.

**Want a starting point?** Optional templates with notes on what goes where are in [`products/_template/`](plugins/content-machine/skills/content-machine/products/_template/). You never have to use them; setup maps your own files into the same sections. To change your files later, type "update reference files".

## Using it

Only people set up as **approvers** can approve, send back, or drop a piece. Only team members can request topics in Slack.

| You want to | Type or do |
|---|---|
| Start a piece | "write a brief for [topic or keyword]", or post "New topic: [topic]" in your Slack channel |
| Approve a brief or a blog | React with a tick on its Slack post, or reply "approved" |
| Ask for changes | Reply in the post's thread with what to change, or leave comments in the document. A cross with no words also works: it will ask you what to change. |
| Drop a piece | Reply "drop it" in the thread |
| Mark it live | Approve the blog, publish it yourself, then reply in the thread with the live link |
| Answer "Possible repeat" | Reply "go" to write it anyway (or as a new angle), or "drop" to skip it |
| Re-check a tracked draft | "check this draft" plus its document link (the piece must be in your tracker) |
| Write the next approved blog now | "write the next approved blog" |
| Pick up Slack replies now | "run the orchestrator" (otherwise replies are read at the next scheduled round) |
| Update your files or rules | "update reference files" |
| Add a product or a teammate | "add a product", "add a teammate" |
| Pause everything | "pause content machine" ("resume content machine" to start again) |
| Fix a broken base or schedule | "repair the base", "repair schedules" |
| Run more or less often | "change how often it runs" |
| Free up Airtable records (the free plan holds 1,000 per base) | "archive old pieces" |
| Hand the schedules to someone else | "move host", from the new host's account |

The agents run on their own in rounds. In each round the Orchestrator reads your Slack replies and document comments first, then the Brief Agent runs, then the Blog Writer, 20 minutes apart. You choose how often in setup:

| Choice | Rounds start at (your time) | Room on Airtable's free plan |
|---|---|---|
| 2 a day | 9 AM, 3 PM | about 12 posts a month |
| 3 a day (default) | 9 AM, 1 PM, 5 PM | about 7 posts a month |
| 4 a day, or every 6 hours | 9 AM, 12, 3 PM, 6 PM (every 6 hours: 3 AM, 9 AM, 3 PM, 9 PM) | about 3 posts a month |
| 5 or 6 a day, or every 2 to 4 hours | spread through the day, or around the clock | needs Airtable's paid plan |

Weekdays only uses about a quarter fewer calls. To change it later, type "change how often it runs".

## Notifications

Updates are posted in your Slack channel from your own Slack account. Slack doesn't notify you about your own posts, so setup offers an optional Airtable bot ("Content Machine"). When a piece needs a decision, it sends a second message that pings your approvers in the channel and by direct message. If the bot can't be set up on your account, every update still arrives in the channel: check it, or turn on notifications for every new message in it.

## Notion sharing

If you pick Notion and share drafts by publishing the top page to the web, anyone with that link can read every draft under it. Keep confidential plans out, or invite reviewers as guests instead.

## Updating

- **Claude:** upload the new zip from the latest release. Your settings live in Airtable, so nothing is lost.
- **Claude Code:** `/plugin marketplace update content-machine`, then update the plugin (or turn on auto-update).
- **Codex:** `codex plugin marketplace upgrade`, then `codex plugin add content-machine@content-machine` again, then reopen Codex.

If your copy is older than your base needs, the agents stop and say so, so an old copy never runs the wrong rules.

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
