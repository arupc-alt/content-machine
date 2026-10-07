# Airtable: the one source of truth

Every mode reads and writes the pipeline through this file's rules. The base is built by setup from `templates/airtable-schema.json`. Never create a second base during a normal run, never use a base found by search, and never guess an ID.

## Finding the base

1. The run's own message names the base ID (schedules always do: "Base: app..."). Use it.
2. If the message names no base (a person typed in chat), use the base ID from this person's last run in this chat, if any. Otherwise call `list_bases` (or `search_bases` with "Content Machine") and pick the base named "[Company] Content Machine". If more than one matches, ask the person which one (attended runs only). An unattended run with no base ID stops with one alert.
3. Read the Team table (one row). Its Base ID must equal the base you opened. If it doesn't, stop: "This schedule points at a base whose Team row names a different base. Type 'repair schedules'."
4. Parse the Team row's Schema Map (JSON). From now on use only the IDs in it.

## Schema Map

Setup writes it, and "repair the base" rewrites it. Shape:

```json
{
  "base": "app...",
  "tables": {"content_items": "tbl...", "settings": "tbl...", "team": "tbl...", "reference": "tbl...", "members": "tbl...", "rework_history": "tbl...", "feedback_log": "tbl..."},
  "fields": {"content_items.Status": "fld...", "content_items.Item ID": "fld...", "...": "..."},
  "choices": {"content_items.Status.Awaiting Brief Approval": "sel...", "...": "..."},
  "channels": {"[Product]": "[Slack Channel ID]"},
  "archive": "app... (only after 'archive old pieces')"
}
```

Keys are the table key, a dot, and the field name exactly as in the template. Choices add a dot and the choice name. `channels` copies each product's Slack Channel ID from its Settings row, so the Orchestrator can read Slack without reading Settings on a run with nothing to do. Setup writes it, "add a product" and "repair the base" rewrite it from Settings, and the weekly full check sets it right when it differs from Settings.

- Filter single-select fields by choice ID (`choices`), never by name: a wrong name can quietly return zero rows instead of an error.
- Write single-select values by their plain name.
- If an ID this run needs is missing from Schema Map, or `get_table_schema` shows it no longer exists, stop the run with: "A field the pipeline needs is missing: [table].[field]. Type 'repair the base'." Never guess, never create fields during a normal run, except a 'safe unattended' migration from shared/migrations.md.

## Tables and who writes what

| Table | Rows | Read by | Written by |
|---|---|---|---|
| Team | exactly 1 | every run | setup; every agent writes its own Last Run field and the API counter fields; the Orchestrator also writes Last Orchestrator Sweep, and Reference Row Count when a learned rule goes Active or Retired; any run that loads more Active Reference rows than Reference Row Count expects sets that product's number to the new count |
| Settings | 1 per product | every run with work (the Orchestrator: only when it has something to act on) | setup only |
| Members | 1 per person | runs that post or decide | setup, and "add a teammate" |
| Reference | files and rules | runs with real work, filtered to one product and Status Active | setup and "update reference files"; any agent may add a learned rule, only as Suggested; only the Orchestrator sets one Active or Retired, and only on an approver's yes or no |
| Content Items | 1 per piece | every run | the agent that holds the claim; the Orchestrator for its own fields |
| Rework History | 1 per rework pass | Brief Agent, Blog Writer, QA, and the Orchestrator (to tell used feedback from new) | the agent doing that pass |
| Feedback Log | 1 per piece of feedback | Orchestrator, Brief Agent, Blog Writer | Orchestrator, QA, Brief Agent, Blog Writer create rows; only the Orchestrator updates one, to set Status Active or Retired when the approver answers, matched by Reference Rule ID |

## Content Items field ownership

| Field | Who writes it |
|---|---|
| Item ID, Seq, Product, Trigger Type, Input, Doc Home, Created At | the agent that creates the row |
| Working Title, Primary Keyword, Secondary Keywords, Format Skeleton, Brief Doc Link | Brief Agent (Blog Writer for a pasted brief) |
| Freshness Flags | Brief Agent and Blog Writer, while holding the claim |
| Recheck Due | QA, on an Approved verdict |
| Status | the agent holding the claim, or the Orchestrator per its deciding table (always after re-reading the row) |
| Claimed By, Claimed At, Claim Token | the claiming agent (see Claims) |
| Last Saved Step, QA Round | the agent holding the claim |
| Stall Count | the agent that finds the stall adds 1 (run-start step 4); the agent that sets a waiting status (`Awaiting Brief Approval`, `QA Passed - Awaiting Publish Review`, `Escalated - Needs Human Input`) resets it to 0 in that same update |
| Brief Rework Count | Brief Agent |
| Draft Rework Count | Blog Writer only (it closes every draft pass; QA never writes it) |
| Human Feedback | Orchestrator only. Each entry starts `[ISO time] [reviewer name] via [Slack reply / Slack reaction / Doc comment / chat]:`, then the reviewer's exact words and the source link. The time is when the Orchestrator recorded it, not when the message was sent. The source link is how the Orchestrator knows a message was already recorded. Entries are only ever added at the end. An agent knows which entries it has already used by comparing their times with its newest Rework History row for that stage. |
| Agent Notes | the agent holding the claim, adding a block at the end that starts `[agent] [ISO time]:`. This is where writer notes, QA issue lists, a Blog Writer's send-back of a brief, and post history go. Never overwrite it. Because only the claim holder writes it, two runs can't erase each other's lines. |
| Duplicate Decision | the agent that finds the overlap sets Pending; the Orchestrator sets Go or Drop from an approver's reply |
| Health Flag | run-start row checks |
| Live URL, Published At | Orchestrator |
| Everything else | the agent holding the claim, for its own stage |
| Notes | people. An agent may add one short line per run that it never reads back |

**Blank values.** A blank count means 0. A blank Priority means Normal. A blank Owner gets the Team row's Schedule Host when an agent claims the row. Never flag a row for any of these.

## Claims

Two people, or a person and a schedule, can run the same mode at once. Before working on a row:

1. Make a token: the mode name, the current UTC time to the second, and 4 random letters, like `blog-20261006T091502-kqzm`.
2. Write Claimed By (mode, and "scheduled" or the person's name), Claimed At (now), Claim Token, the working Status for this step, and Last Updated At, in one `update_records_for_table` call.
3. Read the row back. If Claim Token is your token, go ahead. If not, another run has it: drop the row and move to the next one. Before any write that comes more than an hour after this run's last write to the row (a computer that slept mid-run), read Claim Token again; if it isn't yours anymore, stop work on that row without writing.
4. Every write that keeps the claim also sets Claimed At to now, so a long run that's still working never looks stale. A claim is stale when Claimed At is more than 2 rounds old. (Last Updated At isn't used for this, since other runs, like the Orchestrator adding feedback, also write it.) Two rounds means twice the longest gap between the Team row's Round Hours within a day, and never less than 4 hours (8 hours at 3 a day, 12 hours at 2 a day, 8 hours every 4 hours). A stale claim may be taken over by the owning agent's next run (run-start step 4).

When the work for a step is done, clear Claimed By, Claimed At, and Claim Token in the same update that sets the next Status.

## Last Saved Step

The claim holder writes a short value after each step, so a run that dies can be resumed. Each mode file has its own resume table, which is the authority for what the next run does. The values in use:

| Mode | Values |
|---|---|
| Brief Agent | `brief started`, `brief saved`, `brief posted`, `brief rework [N] started`, `brief rework [N] saved`, `brief rework [N] posted`, `brief escalated` |
| Blog Writer | `brief copy saved`, `brief sent back`, `draft started`, `draft v1 saved`, `rework [N] started`, `rework [N] saved`, `rework escalated` |
| QA | `QA round [n] started`, `QA round [n] verdict saved: [Approved / Needs Rework / Escalated]` |

A check for "a QA verdict was saved" matches any value that starts with `QA round [n] verdict saved`.

## Writing rules

- One update per step. Status, links, counts, and Last Saved Step for a step go in a single `update_records_for_table` call, so a row never shows a status without the links that status needs.
- Post to Slack first, then set the status that depends on the post (see shared/slack.md, Confirmed post).
- Confirm every write from its own response. If a write fails, retry once after 2 seconds. If it fails again, stop the run with one alert naming the row and the field.
- Every write sets Last Updated At to now.
- New rows in Rework History and Feedback Log are always `create_records_for_table`, never an update.
- **Agent Notes and Human Feedback only ever grow, but an Airtable cell holds 100,000 characters.** Before a write would take either past about 90,000 characters, shorten the oldest blocks to one line each, keeping every source link and every Item ID, and add one line saying older entries were shortened. Never drop a source link: the Orchestrator uses them to know what's been processed.
- Never delete a row. Never merge rows. That's always a person's call. The one exception is setup's "archive old pieces", after a person's yes.

## Creating a Content Items row

1. Create it with Product, Trigger Type, Input, Status (`Topic Requested` or `Brief In Progress`), Doc Home (from Settings), Owner, Created At, Last Updated At, and the claim fields when the creating run will work on it now.
2. The response gives Seq. Write Item ID = Settings' Item ID Prefix plus Seq zero-padded to 4 digits (`ACME-AR-0012`).
3. Run the duplicate re-check in shared/run-start.md (step 5).

## The batched read

Every run starts with as few reads as possible (each table read is 1 API call, and each page of 100 rows is its own call):

- Team row (1 call).
- Content Items, filtered to rows that are not Published and not Rejected, with only the fields this mode needs (1 call, more pages only for a big backlog). The Orchestrator reads a wider but still filtered set, since feedback can arrive on finished pieces too (modes/orchestrator.md, The batched read). The duplicate check (run-start step 5) also needs every row's Primary Keyword, Input, and Status, so a run that creates a row reads them too.
- Settings, Members, and Reference only when the queue has real work. Reference is filtered to one product and Status Active, and its row count is checked against Team's Reference Row Count for that product (a JSON object of product name to number, like `{"Acme Writer": 42}`; always write it back in that shape). If fewer rows come back than Reference Row Count, read the next page; if still fewer, skip that product this run (other products go on) with one alert: "Reference rows for [product] didn't all load. If rows were retired on purpose, type 'update reference files'." If more come back, use them all, set Reference Row Count for that product to the new number, and note it in the run summary.
- The Orchestrator reads Settings and Members only when its Content Items read or its Slack window shows something to act on, and reads Reference only on its first run of each run day, or when a learned rule is in play (modes/orchestrator.md).

## The API budget

Airtable's free plan allows 1,000 API calls a month for each workspace, shared by every base in it.

How the calls add up. A run with nothing to do costs 2 calls (the Team row and Content Items). Each mode also writes the Team row once per run day (its Last Run field and the API counter). The Orchestrator reads Reference once per run day, and the weekly full check costs about 10 calls. One piece, from topic to live link, costs about 40 more calls in all. Each round a day adds about 180 calls a month on its own (3 agents, 2 calls each, 30 days). So 3 rounds a day, every day, uses about 700 calls a month before any real work, which leaves room for about 7 pieces a month. 2 rounds a day, or weekdays only, leaves room for about 12.

- Each run keeps a count of the Airtable calls it made.
- At the end of a run that already writes the Team row (its Last Run field, once per run day), add this run's count, plus 2 for every run since the last write, to API Calls This Month. If API Month isn't this month (UTC), reset the count to this run's count, set API Month, and turn Limit Reached off, in the same update.
- When API Calls This Month passes 800, post one alert (once per month): "[Company] Content Machine has used about 800 of 1,000 free Airtable calls this month. Runs will slow down. Consider 2 rounds a day, or Airtable's paid plan."
- If any call fails with Airtable's monthly limit error, try to set Limit Reached on, post one alert, and stop. If that write fails too, put the alert in the run's own output and stop. Every run that sees Limit Reached on stops at step 2 of run-start until API Month changes.
- Airtable allows 5 calls a second. If a call fails for rate, wait 1 second and retry, up to 3 tries.

## Records

The free plan holds 1,000 records per base. The weekly full check counts rows in every table and saves Records Count. Past 900, post one alert: "[Company] Content Machine is close to the free plan's 1,000 records. Type 'archive old pieces' to move old finished pieces to an archive base." Archiving (setup mode) runs only after a person says yes, and the duplicate check reads the archive base too.
