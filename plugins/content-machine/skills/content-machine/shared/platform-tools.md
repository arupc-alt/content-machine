# Tools by capability, on Claude and Codex

Mode files name tools by their base name (`list_records_for_table`), never with a platform prefix. On Claude the full name carries a prefix like `mcp__Airtable__`; on Codex it carries the MCP server's name. Match by the base name: use whichever tool in this session ends with it.

Each step needs a capability, not just a name. The connections check (setup Step 0) and the first call of each run test the capabilities the chosen setup needs. If a capability is missing, use the fallback in the last column, or stop with the message from shared/run-start.md.

## Airtable (required)

| Capability | Tool | Fallback |
|---|---|---|
| List bases and workspaces | `list_bases`, `search_bases`, `list_workspaces` | none |
| Read rows with a filter and a field list | `list_records_for_table` | none |
| Create, update rows | `create_records_for_table`, `update_records_for_table` | none |
| Read the structure | `list_tables_for_base`, `get_table_schema` | none |
| Build the base (setup) | `create_base`, `create_table`, `create_field`, `update_field` | none |
| Build and check automations (setup, weekly check) | `create_automation`, `update_automation`, `get_automation`, `list_automations`, `list_automation_runs`, `list_external_accounts`, `fetch_automation_input_data` | skip the bot, so waiting updates go out one way only (shared/slack.md, The fallback message); the heartbeat then can't be built either, and setup says so |

On Codex, the Airtable server is `https://mcp.airtable.com/mcp`, added in Codex's MCP settings and signed in once. Tool names are the same.

## Slack (required for posts)

| Capability | Tool | Fallback |
|---|---|---|
| Post a message or a thread reply | `slack_send_message` | shared/slack.md, When Slack is down |
| Read a channel's history | `slack_read_channel` | none for the Orchestrator: stop with an alert in the run output |
| Read a thread | `slack_read_thread` | same |
| Read reactions | `slack_get_reactions` | treat reactions as unread and say so in the run summary |
| Search a channel's messages (for example, an alert posted earlier this month) | `slack_search_public_and_private` | read the channel's history back to the time needed (`slack_read_channel`) |
| Find a channel or a person | `slack_search_channels`, `slack_search_users`, `slack_read_user_profile` | ask in setup (attended only) |

On Codex, Slack is the official server at `https://mcp.slack.com/mcp`. A Slack workspace admin approves it once for the company.

## Google Drive (when Doc Home is Drive)

| Capability | Tool on Claude | Fallback |
|---|---|---|
| Create a Google Doc from HTML | `create_file` with `contentMimeType: "text/html"` | none: stop with G15 |
| Read a Doc with its comments | `read_file_content` with `includeComments: true` | read without comments, and say comments couldn't be checked |
| Export text and HTML for QA's measurements | `download_file_content` | measure from `read_file_content` and say so in the QA report |
| Check and share access | `get_file_permissions`, `share_file` | name the people who couldn't be shared with |
| Create a folder | `create_file` with `contentMimeType: "application/vnd.google-apps.folder"` | none |

On Codex, Drive uses Google's own Drive and Docs servers, which need a one-time Google Cloud project and OAuth client made by an admin. Their tool names and abilities differ: the Codex entries in this file are confirmed during testing, and until then Codex plus Drive is a beta, and setup suggests Notion on Codex.

## Notion (when Doc Home is Notion)

| Capability | Tool | Fallback |
|---|---|---|
| Create a page or database row | `notion-create-pages` | none |
| Read a page | `notion-fetch` | none |
| Edit a page in place | `notion-update-page` (`update_content` or `replace_content`) | none |
| Add an image | `notion-create-attachment` (SVG content) | leave an image-suggestion callout instead |
| Read and add comments | `notion-get-comments`, `notion-create-comment` | say comments couldn't be checked |
| Build the database and views (setup) | `notion-create-database`, `notion-create-view` | none |

On Codex, Notion is `https://mcp.notion.com/mcp`, signed in with `codex mcp login notion`.

## Connecting a server

- **Claude app, desktop, or Cowork:** Settings, then Connectors, find the name, and click Connect.
- **Claude Code:** connectors added in the Claude app show up in Claude Code when it's signed in with the same Claude account. Otherwise add each server, then type `/mcp` and sign in:
  - `claude mcp add --transport http airtable https://mcp.airtable.com/mcp`
  - `claude mcp add --transport http slack https://mcp.slack.com/mcp`
  - `claude mcp add --transport http notion https://mcp.notion.com/mcp`
  - Google Drive has no server line here: connect it in the Claude app (Settings, Connectors), or pick Notion.
- **Codex:** add the same addresses in Codex's MCP settings (named airtable, slack, and notion), then sign in to each with `codex mcp login [name]` in a terminal, or the sign-in button in Codex's settings. Slack needs a workspace admin's approval once. A newly added server may only show up in a new chat.

## Other

| Capability | Tool | Fallback |
|---|---|---|
| Web search and read a page | the session's web search and fetch tools | none: briefs can't be researched without them |
| Run a script (QA measurements) | the session's code or shell tool | measure by careful reading and say so in the QA report |
| Scheduled runs (setup) | Claude: `create_trigger`, `list_triggers`, `update_trigger`, `fire_trigger`, `delete_trigger` (the cloud schedule tools). In the Claude desktop app the same jobs are `create_scheduled_task`, `list_scheduled_tasks`, `update_scheduled_task`, and `run_scheduled_task` (cron in the computer's own time zone; runs only while the app is open). In Claude Code, only these desktop tools are used, and only they pass setup's Scheduled tasks check; Claude Code's own cloud schedules aren't used, even when their tools are there, because those runs start in the cloud, where this skill isn't installed. Only the Team row's Schedule Host makes or changes the schedule. It's changed in the app that Schema Map's `schedule` names, and making it in another app moves it there (setup Step 10, Where it lives). Codex: `automation_update` from the Codex app's built-in tools, not the Codex CLI (kind `cron`, a repeat rule like `RRULE:FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FR,SA;BYHOUR=9,13,17;BYMINUTE=7`; saved as `~/.codex/automations/[id]/automation.toml`) | give the prompt to paste into any app where scheduled tasks work and the content machine skill is installed: Claude with scheduled tasks, the Claude desktop app, or the Codex app, leaving out this app when its check, or creating or updating, failed here (Claude Code without the Claude desktop app's scheduled-task tools, and the Codex CLI, get the whole list; modes/setup.md, Step 10, Later, or in another app). When `schedule` names this app, "repair schedules" and "change how often it runs" name no other app, even when its scheduled tasks are off or the update or create fails there: they say how to fix it in that app and to type 'repair schedules' (or 'change how often it runs') there again (modes/setup.md, Repair schedules) |
| A browser for AI answer-engine checks | the session's browser tools | skip quietly; scheduled runs note it in Open Questions |
| Calendar reminders | Google Calendar tools | the Recheck Due field (always used) |
