# Tools by capability, on Claude and Codex

Mode files name tools by their base name (`list_records_for_table`), never with a platform prefix. On Claude the full name carries a prefix like `mcp__Airtable__`; on Codex it carries the MCP server's name. Match by the base name: use whichever tool in this session ends with it.

Each step needs a capability, not just a name. Preflight (setup) and the first call of each run test the capabilities the chosen setup needs. If a capability is missing, use the fallback in the last column, or stop with the message from shared/run-start.md.

## Airtable (required)

| Capability | Tool | Fallback |
|---|---|---|
| List bases and workspaces | `list_bases`, `search_bases`, `list_workspaces` | none |
| Read rows with a filter and a field list | `list_records_for_table` | none |
| Create, update rows | `create_records_for_table`, `update_records_for_table` | none |
| Read the structure | `list_tables_for_base`, `get_table_schema` | none |
| Build the base (setup) | `create_base`, `create_table`, `create_field`, `update_field` | none |
| Build and check automations (setup, weekly check) | `create_automation`, `update_automation`, `list_automations`, `list_automation_runs`, `list_external_accounts`, `fetch_automation_input_data` | skip the bot (it's optional); the heartbeat then can't be built, and setup says so |

On Codex, the Airtable server is `https://mcp.airtable.com/mcp`, added in Codex's MCP settings and signed in once. Tool names are the same.

## Slack (required for posts)

| Capability | Tool | Fallback |
|---|---|---|
| Post a message or a thread reply | `slack_send_message` | shared/slack.md, When Slack is down |
| Read a channel's history | `slack_read_channel` | none for the Orchestrator: stop with an alert in the run output |
| Read a thread | `slack_read_thread` | same |
| Read reactions | `slack_get_reactions` | treat reactions as unread and say so in the run summary |
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

## Other

| Capability | Tool | Fallback |
|---|---|---|
| Web search and read a page | the session's web search and fetch tools | none: briefs can't be researched without them |
| Run a script (QA measurements) | the session's code or shell tool | measure by careful reading and say so in the QA report |
| Scheduled runs (setup) | Claude: `create_trigger`, `list_triggers`, `update_trigger`, `fire_trigger` | Codex: show ready-to-paste Automations entries |
| A browser for AI answer-engine checks | the session's browser tools | skip quietly; scheduled runs note it in Open Questions |
| Calendar reminders | Google Calendar tools | the Recheck Due field (always used) |
