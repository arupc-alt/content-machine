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
- **Your reference files:** a brand guide, a writing style guide, and product knowledge. Quality checks, links and CTAs, competitors, and best past posts are optional. No files yet? Setup can draft them from your website for you to review.

## Install

Pick one. Each one installs the same skill.

**Claude, for your whole organization.** An org owner downloads `content-machine.zip` from the [latest release](https://github.com/arupc-alt/content-machine/releases/latest) and uploads it in the organization's skill settings. It then appears for everyone in the org.

**Claude, just you.** Download `content-machine.zip` from the [latest release](https://github.com/arupc-alt/content-machine/releases/latest), upload it in Claude's skill settings, and turn it on.

**Claude Code.**

```
/plugin marketplace add arupc-alt/content-machine
/plugin install content-machine@content-machine
```

**Codex (app or CLI).**

```
$skill-installer install https://github.com/arupc-alt/content-machine/tree/main/skills/content-machine
```

Then restart Codex.

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
- **Codex:** add the same three addresses in Codex's MCP settings and sign in (for Notion, `codex mcp login notion`).

Setup checks every connection and tells you exactly what's missing, all in one message.

## Set up

In a new chat, type:

```
set up content machine
```

Setup goes step by step, and every change waits for your yes:

1. Asks whether you want your own content machine or want to join a teammate's.
2. Checks your connections.
3. Asks about your company and products.
4. Builds your Airtable base.
5. Picks your Slack channel, approvers, item ID prefix, rounds per day, and Google Drive or Notion.
6. Collects your reference files and pulls out your rules for you to approve.
7. Builds your document folder or Notion pages.
8. Builds the Airtable automations: a heartbeat email if the agents stop running, and the optional notification bot.
9. Creates the schedules.
10. Runs a short test: a test post, document, and row, then fires each schedule once.

Expect it to take a while (roughly 30 to 45 minutes). You can stop at any point and type `set up content machine` again later; it picks up where it stopped and never makes a second copy.

**Teammates.** Each person can set up their own Content Machine in their own accounts. To share one queue instead: first add your teammate as an editor on your Airtable base, then they type "join a teammate's content machine" and paste the base link. In a shared base, your scheduled runs write the documents; their own chat requests add topics to the queue.

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
| Hand the schedules to someone else | "move host", from the new host's account |

The agents run on their own 3 times a day by default (just after 9 AM, 1 PM, and 5 PM your time; at 2 rounds a day, 9 AM and 3 PM). In each round the Orchestrator reads your Slack replies and document comments first, then the Brief Agent runs, then the Blog Writer.

## Notifications

Updates are posted in your Slack channel from your own Slack account. Slack doesn't notify you about your own posts, so setup offers an optional Airtable bot ("Content Machine"). When a piece needs a decision, it sends a second message that pings your approvers in the channel and by direct message. If the bot can't be set up on your account, every update still arrives in the channel: check it, or turn on notifications for every new message in it.

## Notion sharing

If you pick Notion and share drafts by publishing the top page to the web, anyone with that link can read every draft under it. Keep confidential plans out, or invite reviewers as guests instead.

## Updating

- **Claude:** upload the new zip from the latest release. Your settings live in Airtable, so nothing is lost.
- **Claude Code:** `/plugin marketplace update content-machine`, then update the plugin (or turn on auto-update).
- **Codex:** run the install line again.

If your copy is older than your base needs, the agents stop and say so, so an old copy never runs the wrong rules.

## What's in this repo

| Path | What it is |
|---|---|
| `plugins/content-machine/skills/content-machine/` | The skill itself. This is the only copy people edit. |
| `skills/content-machine/` | An exact copy, made by `scripts/sync.py`, so the Codex installer can find it |
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
