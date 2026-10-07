# Database migrations

Each skill release that changes the database ships a numbered migration here. A migration only adds things: tables, fields, and choices. It never deletes, renames, or changes the type of anything, so a team with mixed skill versions keeps working (older copies ignore fields they don't know).

## How a run applies them

1. Read Schema Version from the Team row.
2. For each migration below with a higher number, in order: check what already exists (`get_table_schema`), add only what's missing, then refresh Schema Map with the new IDs.
3. Set Schema Version to the migration's number. If the migration says so, also raise Min Skill Version.
4. "update the base" (setup mode) says what it's adding and waits for a yes. A normal agent run, attended or not, applies only migrations marked "safe unattended" and posts one line saying so; anything else waits for "update the base", and the run stops with one alert: "A database update is waiting. Type 'update the base'."

If a step fails halfway, the next run starts the same migration again. Every step checks before it adds, so nothing is added twice.

## Migrations

### 1: the starting structure

The structure in `templates/airtable-schema.json`, schema version 1. Setup builds it directly, so there's nothing to apply.

### 2: Round Hours (safe unattended)

Adds one field to the Team table: Round Hours (single line text), the hours each round starts in the Team row's Time Zone, comma-separated, like `9,13,17`. It lets a team run any number of rounds a day, or every few hours (setup Step 8).

When it's added to an existing base, fill it from Rounds Per Day: 1 gives `9`, 2 gives `9,15`, 3 gives `9,13,17`, 4 gives `9,12,15,18`, 5 gives `9,11,13,15,17`, 6 gives `8,10,12,14,16,18`, and anything else `9,13,17`. Schedules don't change. Min Skill Version stays the same: older copies ignore the field and keep using Rounds Per Day.

### 3: Open Question and API Monthly Limit (safe unattended)

Adds two fields: Open Question (long text) on Content Items, for questions a run asks before going on (G25); and API Monthly Limit (number) on Team, filled with 1,000 when added (the free plan; "change Airtable plan" sets a higher one). Raise Min Skill Version to 0.3.0: an older copy would ignore Open Question and work a held row, so it must stop and ask to be updated.

### Heartbeat formula update (0.2.1, by hand, optional)

Bases built before skill 0.2.1 have an older Heartbeat Late formula that can send a false alarm on weekends east of UTC, after a long first run of the day, or while Limit Reached is on. Airtable's API can't change a formula field, so this isn't a numbered migration. "repair the base" offers it: show the person the new formula from `templates/airtable-schema.json` (addAfterCreate, Heartbeat Late) and ask them to paste it into the field's formula in Airtable. Nothing else depends on the change.
