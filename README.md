# Content Machine

A blog content pipeline that runs inside your own accounts. Type a topic or a keyword, and the Content Machine:

1. **Researches and writes an SEO brief**, saves it as a Google Doc or Notion page, and asks for your OK in Slack.
2. **Writes the blog** once the brief is approved, checks it against 23 quality checks plus your own rules, and fixes it up to 3 rounds.
3. **Asks for your OK to publish** in Slack, and tracks every piece in an Airtable base it builds for you.

It works on Claude and on Codex, with free Airtable, Slack, and Google Drive or Notion accounts. Nothing about any one company is built in: your company, products, reference files, and rules all come from setup.

## Before you start

You need:

- **Claude** with connectors and scheduled tasks (so the agents can run on their own), or **Codex** with the app left open on a computer that stays on.
- **Airtable** (free). The free plan allows about 1,000 automated reads and writes a month per workspace. That's enough for about 7 blog posts a month at 3 rounds a day, or about 12 at 2 rounds a day. Each base allows 5 editors.
- **Slack** (free). On Codex, a Slack workspace admin approves the Slack connection once.
- **Google Drive or Notion** (free). On Codex, Google Drive needs an admin to set up a Google Cloud OAuth client once (beta), so Notion is the easier pick there.
- Your **reference files**: a brand guide, a writing style guide, and product knowledge. Quality checks, links and CTAs, competitors, and best past posts are optional. No files yet? Setup can draft them from your website for you to review.

## Install

Pick one.

**Claude, for your whole organization (best).** An org owner downloads `content-machine.zip` from the [latest release](https://github.com/arupc-alt/content-machine/releases/latest), then uploads it in Organization settings, under skills. It appears for everyone in Claude, the desktop app, and Cowork.

**Claude, just you.** Download `content-machine.zip` from the [latest release](https://github.com/arupc-alt/content-machine/releases/latest). In Claude, open Customize, then Skills, then add a skill and upload the zip. Turn it on.

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

**Already have a different skill called content-machine?** Upload `content-machine-pipeline.zip` from the release instead. It's the same skill under another name.

## Set up

In a new chat, type:

```
set up content machine
```

Setup checks your connections first, then asks about your company, builds your Airtable base, collects your reference files and pulls out your rules, builds your document folder, creates the schedules, and runs a short test. It takes about 30 to 45 minutes, and every change waits for your yes. You can stop at any point and run it again later; it picks up where it stopped.

**Every teammate can run their own.** Each person can set up their own Content Machine in their own accounts. To share one queue instead, a teammate types "join a teammate's content machine" and pastes your base link.

## Using it

| You want to | Type or do |
|---|---|
| Start a piece | "write a brief for [topic or keyword]", or post "New topic: [topic]" in your Slack channel |
| Approve a brief or a blog | React with a tick on its Slack post, or reply "approved" |
| Ask for changes | Reply in the post's thread with what to change, or react with a cross |
| Drop a piece | Reply "drop it" in the thread |
| Mark it live | Approve the blog, then reply in the thread with the live link |
| Re-check a tracked draft | "check this draft" plus its document link (it must be a piece in your tracker) |
| Update your files or rules | "update reference files" |
| Add a product or a teammate | "add a product", "add a teammate" |
| Pause everything | "pause content machine" ("resume content machine" to start again) |
| Fix a broken base or schedule | "repair the base", "repair schedules" |

The agents run on their own 3 times a day by default (about 9 AM, 1 PM, and 5 PM your time): first the Orchestrator reads your Slack replies, then the Brief Agent, then the Blog Writer.

## Notifications

Updates are posted in your Slack channel from your own Slack account. Slack doesn't ping you about your own posts, so setup offers an optional Airtable bot ("Content Machine") that sends a second message and pings everyone. If the bot can't be set up on your account, you still get every update in the channel: check the channel, or turn on notifications for every new message in it.

## Updating

- **Claude:** upload the new zip from the latest release. Your settings live in Airtable, so nothing is lost.
- **Claude Code:** `/plugin marketplace update content-machine`, or turn on auto-update.
- **Codex:** run the install line again.

If your copy is older than your base needs, the agents stop and say so, so an old copy never runs the wrong rules.

## What's in this repo

| Path | What it is |
|---|---|
| `plugins/content-machine/skills/content-machine/` | The skill itself. This is the only copy people edit. |
| `skills/content-machine/` | An exact copy, made by `scripts/sync.py`, so the Codex installer can find it |
| `scripts/` | `check.py` (runs on every push), `sync.py`, `build_zip.py` |
| `tests/` | The rules inventory and the release checks |
| `.claude-plugin/`, `.agents/plugins/` | Marketplace files for Claude Code and Codex |

## Privacy

This repo holds no company data, no IDs, and no tokens. Your reference files, rules, and pipeline live only in your own Airtable base and your own Drive or Notion. Connections are made in your own app; the skill never asks for a password or a token.

## License

MIT. See [LICENSE](LICENSE).
