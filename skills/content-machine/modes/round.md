# Round mode

One scheduled run does the whole round, in a fixed order: the Orchestrator first, then the Brief Agent, then the Blog Writer (with QA inside it). This is what setup's single schedule runs: `Use the [Skill Name] skill. Mode: Round. Base: [base ID]. Channels: [Slack Channel IDs]. Unattended run.` Each part follows its own mode file exactly; this file only sets the order and what's shared.

A scheduled round is unattended (shared/run-start.md, Attended or unattended): it never asks in chat, and asks in Slack instead when it must (G25). A round someone starts in chat ("run a round") is attended and may ask in chat.

## Start once

1. Do shared/run-start.md steps 1 to 3 once, for the whole round: connectors, pause, version and limits, and base health. If any of them stops the run, the whole round stops there, except Airtable's monthly limit, which switches the round to Slack-only mode (shared/airtable.md, When the limit is reached) instead of stopping.
2. Work out lean mode (shared/airtable.md, The API budget): a lean round skips step 4 of the Brief Agent's queue and step 6 of the Blog Writer's (no new pieces) and does everything else.
3. Make one batched read (shared/airtable.md): the Team row, and Content Items as modes/orchestrator.md's batched read describes (it covers what the Brief Agent and Blog Writer need too). Settings, Members, and Reference are read only when a part has real work, as each mode file says.

## The three parts, in order

Each part does shared/run-start.md steps 4 to 6 for its own mode (recovery, row checks, and its work queue), then its mode file's work, with that mode's own limits (G3). Steps 1 to 3 already ran; don't repeat them.

1. **Orchestrator** (modes/orchestrator.md): read Slack and document comments, and record every decision, change request, new topic, and live link. It always runs, because only it can tell whether anything new came in.
2. **Brief Agent** (modes/brief.md): only if its queue has work after part 1 (a recovery row, a stalled brief, a brief sent back, or a `Topic Requested` row). Otherwise skip it.
3. **Blog Writer** (modes/blog-writer.md, with modes/qa.md for the loop): only if its queue has work after parts 1 and 2. Otherwise skip it.

**Between parts:** if an earlier part changed any Content Items row, read Content Items again before the next part builds its queue (one call), so it sees the new statuses. If nothing changed, reuse the batched read.

**Load each part's files only when that part has work,** from the load map in SKILL.md. A round with nothing to do loads only this file, shared/run-start.md, shared/guards.md, shared/airtable.md, shared/slack.md, and modes/orchestrator.md, and costs 2 Airtable calls.

**If one part fails,** say why in the run summary and go on to the next part, unless the failure is one that stops every run (shared/run-start.md, steps 1 and 2). A part that runs out of time or room ends cleanly at its next saved step (Last Saved Step), and the next round picks it up.

## End once

- **One Team write a day.** On the round's first run of each run day, write Last Run Orchestrator, Last Run Brief, and Last Run Blog Writer (all three, even for a part that had nothing to do, since the round ran), Last Orchestrator Sweep, and the API counter, in one update (shared/run-start.md, The heartbeat). On later rounds the same day, write the Team row only when the Orchestrator's own rules need it (modes/orchestrator.md, End of run) or the API counter must be saved.
- **One run summary** (shared/run-start.md, The run summary), with a short section per part that did something. The Orchestrator's Slack summary is posted only as modes/orchestrator.md says.
