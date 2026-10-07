# Database migrations

Each skill release that changes the database ships a numbered migration here. A migration only adds things: tables, fields, and choices. It never deletes, renames, or changes the type of anything, so a team with mixed skill versions keeps working (older copies ignore fields they don't know). Only an account with creator access to the base can add them, so the host should update first (step 5).

## How a run applies them

1. Read Schema Version from the Team row.
2. For each migration below with a higher number, in order: check what already exists (`get_table_schema`), add only what's missing, then refresh Schema Map with the new IDs.
3. Set Schema Version to the migration's number. If the migration says so, also raise Min Skill Version.
4. "update the base" (setup mode) says what it's adding and waits for a yes. A normal agent run, attended or not, applies only migrations marked "safe unattended" and posts one line saying so; anything else waits for "update the base", and the run stops with one alert: "A database update is waiting. Type 'update the base'."
5. Adding a table, field, or choice needs creator access to the base, and a teammate who joined as an editor doesn't have it. If an add fails with a permission error, change nothing more, leave Schema Version as it is, and stop with one alert instead: "A database update is waiting that only the base's host can apply. Ask the host ([Schedule Host]) to update their copy of the content machine skill (their next round applies it), or to type 'update the base'."

If a step fails halfway, the next run starts the same migration again. Every step checks before it adds, so nothing is added twice.

## Migrations

### 1: the starting structure

The structure in `templates/airtable-schema.json`, schema version 1. Setup builds it directly, so there's nothing to apply.

### 2: Round Hours (safe unattended)

Adds one field to the Team table: Round Hours (single line text), the hours each round starts in the Team row's Time Zone, comma-separated, like `9,13,17`. It lets a team run any number of rounds a day, or every few hours (setup Step 8).

When it's added to an existing base, fill it from Rounds Per Day: 1 gives `9`, 2 gives `9,15`, 3 gives `9,13,17`, 4 gives `9,12,15,18`, 5 gives `9,11,13,15,17`, 6 gives `8,10,12,14,16,18`, and anything else `9,13,17`. Schedules don't change. Min Skill Version stays the same: older copies ignore the field and keep using Rounds Per Day.

### 3: Open Question, API Monthly Limit, and the Exception category (safe unattended)

Adds two fields: Open Question (long text) on Content Items, for questions a run asks before going on (G25); and API Monthly Limit (number) on Team. Also adds one choice, Exception, to Reference's Category field, for a style exception a person approves (shared/rule-extraction.md, Pulling out the rules, step 3). Raise Min Skill Version to 0.3.0: an older copy would ignore Open Question and work a held row, so it must stop and ask to be updated.

Fill API Monthly Limit when it's added. When setup (Step 3, existing base), "update the base", or "repair the base" applies it, ask setup Step 4's plan question (item 7, Their Airtable plan) and save that number. Otherwise fill 1,000 (the free plan), and the one line the run posts says: "Database updated: API Monthly Limit is set to 1,000, Airtable's free plan. If this workspace is on a paid plan, type 'change Airtable plan', or new pieces may wait." If API Month is this month and API Calls This Month is already over 1,000, the workspace must be on a paid plan (the free plan stops at 1,000), so the line says instead: "Database updated: API Monthly Limit is set to 1,000, Airtable's free plan, but this workspace has already used [n] calls this month, so it looks like a paid plan. Type 'change Airtable plan' to set its real limit, or new pieces will wait."

A bot built before this migration (Bot Automation ID is set) doesn't ping for questions. A run can't change it unattended, because changes to a live automation wait for a person to publish them. So when Bot Automation ID is set, the one line the run posts ends with: "The bot doesn't ping for questions yet. Type 'repair the base' to add that." "repair the base" adds it (modes/setup.md, Repair the base, step 5).

Schedules don't change. A base still on the three per-agent schedules from skill 0.2 gets the old schedules alert from the full check after this update, and weekly after that, until the host types 'repair schedules' (shared/run-start.md, step 3).

### Heartbeat formula update (0.2.1 and 0.3.0, by hand, optional)

Bases built before skill 0.2.1 have an older Heartbeat Late formula that can send a false alarm on weekends east of UTC, after a long first run of the day, or while Limit Reached is on. Bases built before skill 0.3.0 can also send one on the 1st of the month after the Airtable limit was reached, before the new month's first round runs: the newer formula keeps the alarm quiet while Limit Reached is on through the first 4 days (UTC) of the next month too. Airtable's API can't change a formula field, so this isn't a numbered migration. "repair the base" offers it: show the person the new formula from `templates/airtable-schema.json` (addAfterCreate, Heartbeat Late) and ask them to paste it into the field's formula in Airtable. Nothing else depends on the change.
