# Notes for coding agents working on this repo

- The skill lives in `plugins/content-machine/skills/content-machine/`. Edit only that copy. Run `python3 scripts/sync.py` after every change, so `skills/content-machine/` matches.
- Run `python3 scripts/check.py` before every commit. It must pass.
- House style for every file: plain words, short sentences, no em dashes, no en dashes as dashes, no curly quotes, no emoji (except the status marks in setup's connections checklist, which people asked for), US spelling.
- Never add a company's name, people, IDs, channels, or tokens to any file. Everything company-specific lives in each team's own Airtable base.
- Keep every rule in `tests/rules-inventory/`. If you move or reword a rule, update its anchor. Never drop a quality rule without saying why in the inventory.
- A change to the database ships as a numbered migration in `shared/migrations.md` and raises `schema_version` in SKILL.md and `schemaVersion` in `templates/airtable-schema.json`. Migrations only add things.
- Bump the version in SKILL.md and both plugin manifests together, and add a CHANGELOG entry.
